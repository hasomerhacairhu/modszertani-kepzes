#!/usr/bin/env python3
"""Static integrity checks for the training repository.

Read-only and deterministic. Two separate concerns:

* **Objective errors** (exit 1) — things that are simply wrong in the repository:
  broken internal links, resurrected duplicate canonical files, merge-conflict
  markers, terminology drift, and a small set of *known* content regressions that
  have actually happened here before and are dangerous to reintroduce.
* **Release blockers** (reported, not failing unless ``--strict-release``) —
  organisation-specific `KITÖLTENDŐ` fields and open release gates. These are
  never guessed or auto-filled.

Every rule below exists because the corresponding defect occurred in this
repository. Do not add speculative prose linting: legitimate Hungarian text must
never fail this check.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {'.git'}
ACTIVE_ROOT = ROOT / '02 Tervezet'
MODULE_ROOT = ACTIVE_ROOT / 'Modulok'
MEDIA_ROOT = ACTIVE_ROOT / 'Média-assetek'
AUDIT_ROOT = ROOT / '01 Fejlesztés' / '04 Audit'

# Files whose duplicates were deleted during the 2026-08 canonicalisation. If one
# reappears, two "canonical" versions of the same lesson exist again.
LEGACY_PATHS = [
    '02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-től a használható visszajelzésig (45’).md',
    '02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyerekvédelem.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyerekvédelem 101 – red flag felismerése & első lépések.md',
    '02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyerekvédelem (Study Lab).md',
    '02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md',
    '02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v2 + AI – modulproduktum váz.md',
]

REQUIRED_FILES = [
    'LICENSE',
    '02 Tervezet/RELEASE-READINESS.md',
    '02 Tervezet/Gyermekvédelem – release gate.md',
    '02 Tervezet/Adatvédelem – tanulói adatok és AI.md',
    '02 Tervezet/LMS – activity manifest.md',
    '02 Tervezet/LMS – H5P runtime acceptance.md',
    '02 Tervezet/Terepgyakorlat – 2. félév.md',
    '01 Fejlesztés/04 Audit/DEEP-AUDIT-RUBRIC.md',
]

# Phrases that must not come back anywhere under Modulok/.
FORBIDDEN_ANYWHERE = {
    'te leszel az a felnőtt':
        'a 15+ célcsoportban a madrich maga is lehet kiskorú, nem ő az egyedüli felelős felnőtt',
    'érzelmi „gáz” (amygdala)':
        'túlzottan leegyszerűsítő, nem védhető fejlődéslélektani metafora',
    'fotózd le a rajzot, és töltsd fel':
        'az M2.1 teljes identitástérkép-feltöltése adatminimalizálási regresszió',
}

# ---------------------------------------------------------------------------
# ACTIVE-SPEC rules (02 Tervezet, excluding the generated media register).
#
# These exist because the 2026-08-25 follow-up review found the module files
# already correct while the PROGRAM-LEVEL documents still specified the old
# behaviour. Scoping the M3 roleplay rule to Modulok/M3 was the blind spot.
#
# Each rule is a (phrase, why) pair plus a set of EXEMPTION markers. A line is
# only reported when it contains the phrase and none of the exemption markers —
# so that an explicit "we deliberately do NOT do this" note never trips it.
# ---------------------------------------------------------------------------

# Deliberate-exclusion markers. Kept narrow on purpose: a bare "nem" is NOT
# enough, because the original stale sentence also contained "ez nem opció".
NOT_A_REGRESSION = (
    'kikerült', 'nem szerepjáték', 'nem játsszuk el', 'nem eljátszani',
    'tudatosan nem', 'tudatosan NEM', 'ne használd', 'nem használjuk',
    'NEM Documentation Tool', 'nem támaszkodunk', 'Nem támaszkodunk',
    'helyett', 'tilos', 'nem helyettesíti', 'már nem',
    # the canonical rule itself has to be able to name the thing it forbids
    'nem nevezz meg nem létező', 'nem szerepel', 'nincs „Short Answer”',
)

ACTIVE_SPEC_RULES = {
    'miniszínház': 'az M3.B kánoni formátuma harmadik személyű esetelemzés, nem szerepjáték',
    'mini-színház': 'az M3.B kánoni formátuma harmadik személyű esetelemzés, nem szerepjáték',
    'fórum-színház': 'az M3.B-ből a fórum-színház kikerült',
    'minijelenet': 'súlyos gyermekvédelmi helyzet eljátszatása visszatérne',
    'biztonságos felnőttként': '15+ célcsoportban a madrich maga is lehet kiskorú, nem ő a felelős felnőtt',
    'megbízható felnőtt': '15+ célcsoportban a madrich maga is lehet kiskorú, nem ő a felelős felnőtt',
    'kapu teljesítése a jogalap': 'a kurzusteljesítés nem GDPR 6. cikk szerinti jogalap',
    'felirat VAGY': 'szinkronizált médiánál a felirat kötelező (WCAG 2.2 SC 1.2.2), a leirat nem helyettesíti',
    'Short Answer': 'a H5P-ben nincs „Short Answer” content type',
}


# M3 teaches disclosure, abuse and self-harm handling. The agreed safe default is
# third-person case analysis, so *instructions to enact* those situations must not
# reappear anywhere in M3. Matching is on instruction-level phrases, not on the
# words "szerep" or "eset" in general.
M3_ROLEPLAY_PHRASES = {
    'miniszínház': 'a red flag helyzetek eljátszatása visszatérne',
    'mini-színház': 'a red flag helyzetek eljátszatása visszatérne',
    'minijelenet': 'a red flag helyzetek eljátszatása visszatérne',
    'fórum-színház': 'a fórum-színház mikroelem szerepbe lépést kér',
    'de-roling': 'a de-roling csak eljátszott szerep esetén értelmes',
    'eljátssza a jelenetet': 'jelenet eljátszása súlyos gyermekvédelmi témán',
    'eljátsszák': 'jelenet eljátszása súlyos gyermekvédelmi témán',
    'gyermekvédelmi szerepjáték': 'a modul nem szerepjátékkal dolgozza fel a red flageket',
}

CONFLICT_MARKERS = re.compile(r'^(?:<{7}|={7}|>{7})(?:\s|$)', re.M)
RESUME_PROMISE = re.compile(r'(mentve marad|később folytathatod|folytathatod később)')
STALE_TERM = re.compile(r'[Gg]yerekvéd')


def markdown_files(base: Path = ROOT):
    for path in base.rglob('*.md'):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def strip_code_fences(text: str) -> str:
    return re.sub(r'```.*?```', '', text, flags=re.S)


def markdown_destinations(text: str):
    """Yield destinations from inline Markdown links using balanced parens."""
    text = strip_code_fences(text)
    i = 0
    while True:
        start = text.find('](', i)
        if start < 0:
            return
        j = start + 2
        depth = 1
        escaped = False
        while j < len(text) and depth:
            ch = text[j]
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            j += 1
        if depth == 0:
            raw = text[start + 2:j - 1].strip()
            if raw:
                yield raw
        i = max(j, start + 2)


def normalize_destination(raw: str) -> str | None:
    if raw.startswith('<') and raw.endswith('>'):
        raw = raw[1:-1].strip()
    lower = raw.lower()
    if lower.startswith(('http://', 'https://', 'file://', 'mailto:', 'tel:', 'data:', 'javascript:')):
        return None
    m = re.match(r'^(.*?)(?:\s+["\'].*["\'])$', raw)
    if m:
        raw = m.group(1)
    raw = raw.split('#', 1)[0].split('?', 1)[0]
    if not raw:
        return None
    return unquote(raw)


def check_structure(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f'MISSING-REQUIRED {rel}')
    for rel in LEGACY_PATHS:
        if (ROOT / rel).exists():
            errors.append(f'LEGACY-DUPLICATE {rel}')


def check_links(errors: list[str]) -> None:
    for md in markdown_files():
        text = md.read_text(encoding='utf-8', errors='replace')
        for raw in markdown_destinations(text):
            dest = normalize_destination(raw)
            if dest is None:
                continue
            target = (md.parent / dest).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f'BROKEN-LINK {md.relative_to(ROOT)} -> {raw!r} (escapes repository)')
                continue
            if not target.exists():
                errors.append(f'BROKEN-LINK {md.relative_to(ROOT)} -> {raw!r}')


def check_conflict_markers(errors: list[str]) -> None:
    for md in markdown_files():
        text = md.read_text(encoding='utf-8', errors='replace')
        if CONFLICT_MARKERS.search(text):
            errors.append(f'CONFLICT-MARKER {md.relative_to(ROOT)}')


def check_terminology(errors: list[str]) -> None:
    """`gyermekvédelem` is canonical (1997. évi XXXI. tv.); the audit logs keep
    their historical wording, and the derived media register is regenerated."""
    for md in markdown_files(ACTIVE_ROOT):
        if md.is_relative_to(MEDIA_ROOT):
            continue
        for lineno, line in enumerate(md.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            if STALE_TERM.search(line):
                errors.append(f'TERMINOLOGY {md.relative_to(ROOT)}:{lineno} „gyerekvéd…” — kánoni alak: „gyermekvéd…”')


def check_active_spec(errors: list[str]) -> None:
    """Rules that must hold across the whole active specification, not just Modulok.

    Z.4 must not name the H5P Documentation Tool as its runtime, and the
    program-level documents must not re-specify behaviour the modules dropped.
    """
    for md in markdown_files(ACTIVE_ROOT):
        if md.is_relative_to(MEDIA_ROOT):
            continue
        rel = md.relative_to(ROOT)
        for lineno, line in enumerate(md.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            if any(marker in line for marker in NOT_A_REGRESSION):
                continue
            for phrase, why in ACTIVE_SPEC_RULES.items():
                if phrase in line:
                    errors.append(f'SPEC-DRIFT {rel}:{lineno} {phrase!r} ({why})')
            if 'Documentation Tool' in line and 'Z.4' in line:
                errors.append(
                    f'SPEC-DRIFT {rel}:{lineno} a Z.4 futtatókörnyezete Moodle Assignment, '
                    'nem H5P Documentation Tool'
                )


def check_regressions(errors: list[str]) -> None:
    for path in MODULE_ROOT.rglob('*.md'):
        text = path.read_text(encoding='utf-8', errors='replace')
        low = text.lower()
        rel = path.relative_to(ROOT)
        for phrase, why in FORBIDDEN_ANYWHERE.items():
            if phrase.lower() in low:
                errors.append(f'REGRESSION {rel}: {phrase!r} ({why})')
        if path.parts[-3] == 'M3' or '/M3/' in path.as_posix():
            for phrase, why in M3_ROLEPLAY_PHRASES.items():
                if phrase in low:
                    errors.append(f'SAFEGUARDING {rel}: {phrase!r} ({why})')
        # H5P Documentation Tool has no content-state saving, so no lesson may
        # promise resume for it. Scoped to a single line, so that explaining *why
        # we avoid it* does not trip the check.
        for lineno, line in enumerate(text.splitlines(), 1):
            if 'Documentation Tool' in line and RESUME_PROMISE.search(line):
                errors.append(f'REGRESSION {rel}:{lineno} H5P Documentation Tool resume-ígéret')


def release_blockers() -> list[str]:
    blockers: list[str] = []
    placeholder_re = re.compile(r'KITÖLTENDŐ')
    for path in ACTIVE_ROOT.rglob('*.md'):
        text = path.read_text(encoding='utf-8', errors='replace')
        if path.is_relative_to(MODULE_ROOT):
            for lineno, line in enumerate(text.splitlines(), 1):
                if placeholder_re.search(line):
                    excerpt = ' '.join(line.strip().split())
                    if len(excerpt) > 240:
                        excerpt = excerpt[:237] + '...'
                    blockers.append(f'MODULE-PLACEHOLDER {path.relative_to(ROOT)}:{lineno}: {excerpt}')
        else:
            count = len(placeholder_re.findall(text))
            if count:
                blockers.append(f'GOVERNANCE-PLACEHOLDER {path.relative_to(ROOT)}: {count}')
    rr = ACTIVE_ROOT / 'RELEASE-READINESS.md'
    if rr.exists() and '- [ ]' in rr.read_text(encoding='utf-8'):
        blockers.append('RELEASE-GATES RELEASE-READINESS.md contains open checklist items')
    return blockers


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict-release', action='store_true', help='also fail when release blockers remain')
    parser.add_argument('--release-report', action='store_true', help='print release blockers but do not fail for them')
    args = parser.parse_args()

    errors: list[str] = []
    check_structure(errors)
    check_links(errors)
    check_conflict_markers(errors)
    check_terminology(errors)
    check_active_spec(errors)
    check_regressions(errors)

    blockers = release_blockers() if (args.strict_release or args.release_report) else []

    print(f'Objective integrity errors: {len(errors)}')
    for item in errors:
        print(f'ERROR: {item}')
    if blockers:
        print(f'Release blockers: {len(blockers)}')
        for item in blockers:
            print(f'BLOCKER: {item}')

    if errors:
        return 1
    if args.strict_release and blockers:
        return 2
    print('Objective content integrity checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
