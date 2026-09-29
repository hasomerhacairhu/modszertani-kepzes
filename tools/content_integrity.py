#!/usr/bin/env python3
"""Static integrity checks for the training repository.

Read-only and deterministic. Two separate concerns:

* **Objective errors** (exit 1) — things that are simply wrong in the repository:
  broken internal links, resurrected duplicate canonical files, merge-conflict
  markers, terminology drift, and a small set of *known* content regressions that
  have actually happened here before and are dangerous to reintroduce.
* **Release blockers** (reported, not failing unless ``--strict-release``) —
  learner-release human decisions, unresolved LMS/runtime outputs and open release
  checklists. These are never guessed or auto-filled.
* **Production-only blockers** — media decisions that can block asset production
  without automatically blocking the learner release when an equivalent fallback
  exists. These are reported separately and do not make ``--strict-release`` fail.

Every rule below exists because the corresponding defect occurred in this
repository. Do not add speculative prose linting: legitimate Hungarian text must
never fail this check.
"""
from __future__ import annotations

import argparse
import json
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
    'műhelyban':
        'hibás magyar toldalékolás: műhelyben',
    'műhelyhoz':
        'hibás magyar toldalékolás: műhelyhez',
    'műhelyon':
        'hibás magyar toldalékolás: műhelyen',
    'a idővonal':
        'hibás névelő: az idővonal',
    'idővonal-t':
        'hibás tárgyrag: idővonalat',
    'visszajelzés-tapasztalat':
        'természetellenes főnévtorlódás: visszajelzéssel kapcsolatos tapasztalat',
    'lektor: [ ]':
        'forrásszintű szakmai-lektor placeholder: a jóváhagyás a release-jegyzőkönyvbe tartozik',
    'dátum: [ ]':
        'forrásszintű jóváhagyási dátum-placeholder: a release-jegyzőkönyvbe tartozik',
    'verzió: [ ]':
        'forrásszintű jóváhagyási verzió-placeholder: a release-jegyzőkönyvbe tartozik',
}

# File-scoped regressions found by the 2026-09 release-readiness follow-up.
# These phrases are narrow on purpose: each one is the exact stale wording that
# previously contradicted the canonical rule elsewhere in the same curriculum.
FILE_FORBIDDEN_PHRASES = {
    '02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md': {
        'Szervezett, de önkéntes;':
            'az önkéntesség a Somer sajátja, nem a nonformális tanulás általános definíciós jegye',
    },
    '02 Tervezet/Modulok/M7/Peulák/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md': {
        'Csoportonként legalább **1 AI-eszköz**.':
            'az M7 no-AI útja teljes értékű; AI-fiók vagy AI-eszköz nem lehet teljesítési feltétel',
    },
    '02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md': {
        'rugalmasan szervezhető (1:1 vagy 3–4 fős kiscsoport)':
            'a kiskorú résztvevővel végzett 1:1 beszélgetést HUM-SAFE-02-höz kell kötni',
    },
    '02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md': {
        'észreveszem → jelzek → nem maradok egyedül → kit vonok be':
            'az M3 learner-facing safeguarding folyamat egységesen az M3.B ötlépéses térképe',
        '4 someres kvuca':
            'a 2025/26-os Hasomer Hacair Magyarország oktatási terv három aktuális kvucát rögzít',
        '4 kvuca-profil':
            'az M3 aktuális korosztálymodellje Parparim 6–9, Kivsza 10–12, Leviatan 13–17',
    },
    '02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md': {
        '6–10 / 11–13 / 14–16 / 16+':
            'az M6 korosztály-illesztése a 2025/26-os három aktuális Somer-csoportot használja',
        'Játék-kategóriák 4 kvucára':
            'az M6.1 címe és tartalma a három aktuális kvucát használja',
        'Játék-labor 4 kvucára':
            'az M6.A címe és tartalma a három aktuális kvucát használja',
    },
    '02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md': {
        'négy alap korosztályban':
            'az M6.1 learner-facing narrációja a három aktuális korosztályt használja',
        '4 kvucára':
            'az M6.1-ben a régi négycsoportos címke nem térhet vissza',
    },
    '02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md': {
        '4 kvucára':
            'az M6.A-ban a régi négycsoportos címke nem térhet vissza',
    },
    '02 Tervezet/LMS – activity manifest.md': {
        'M6.1 – Játék-kategóriák 4 kvucára':
            'az LMS manifestnek ugyanazt a háromcsoportos M6.1 címet kell használnia',
    },
    '02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md': {
        'Parparim / Kivsza / Leviatan / Zorea':
            'az M7 kvuca-választója a 2025/26-os három aktuális csoportot használja',
    },
    '02 Tervezet/Média-assetek/produkcios-szabalyok.json': {
        '4-kvuca piktogramok':
            'az R5 produkciós szabály is a három aktuális kvuca kánonját használja',
    },
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

# Matching is case-insensitive on BOTH sides. The same forbidden spec phrase is
# the same defect however the source capitalises it — a real earlier miss here:
# 'Short Answer' failed while 'Short answer' / 'short answer' passed. Folding the
# exemption markers too keeps the canonical documentation that must *name* the
# forbidden thing ("nincs „Short Answer”") passing.
#
# ONE rule stays case-sensitive: in 'felirat VAGY' the capitals ARE the signal.
# It targets the emphatic stale-spec construction "felirat VAGY leirat" (either
# one suffices). Folded, it would also match ordinary Hungarian prose such as
# "a felirat vagy a leirat is elérhető" — and this checker must never fail
# legitimate Hungarian text (see the module docstring).
CASE_SENSITIVE_RULES = {'felirat VAGY'}

_EXEMPT_FOLDED = tuple(marker.casefold() for marker in NOT_A_REGRESSION)
_RULES = tuple(
    (phrase, why, phrase if phrase in CASE_SENSITIVE_RULES else phrase.casefold(),
     phrase in CASE_SENSITIVE_RULES)
    for phrase, why in ACTIVE_SPEC_RULES.items()
)


def is_deliberate_exclusion(line: str) -> bool:
    """True when the line explicitly says it does NOT do the forbidden thing."""
    folded = line.casefold()
    return any(marker in folded for marker in _EXEMPT_FOLDED)


def active_spec_hits(line: str) -> list[tuple[str, str]]:
    """Which ACTIVE_SPEC_RULES a single line violates, exemptions applied."""
    if is_deliberate_exclusion(line):
        return []
    folded = line.casefold()
    return [(phrase, why) for phrase, why, needle, cased in _RULES
            if (needle in line if cased else needle in folded)]


def z4_runtime_hit(line: str) -> str | None:
    """The Z.4 runtime rule for a single line, exemptions applied.

    Kept as a function (not inline in the file loop) so that ``--selftest``
    exercises the deliberate-exclusion guard on the path the checker actually
    takes — a refactor already dropped that guard here once.
    """
    if is_deliberate_exclusion(line):
        return None
    if 'Documentation Tool' in line and 'Z.4' in line:
        return 'a Z.4 futtatókörnyezete Moodle Assignment, nem H5P Documentation Tool'
    return None


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
ARTICLE_REGRESSIONS = (
    (re.compile(r'(?<!\w)a\s+\*{0,2}aktív\b', re.I), 'hibás névelő: az aktív'),
    (re.compile(r'(?<!\w)a\s+[„"\']aktív\b', re.I), 'hibás névelő: az aktív'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}időben\b', re.I), 'hibás névelő: az időben'),
    (re.compile(r'(?<!\w)a\s+[„"\']időben\b', re.I), 'hibás névelő: az időben'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}[„"`]?M[0-7](?=[.\-–\sA-Z])', re.I),
     'hibás névelő modulazonosító előtt: az M…'),
)


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
            for phrase, why in active_spec_hits(line):
                errors.append(f'SPEC-DRIFT {rel}:{lineno} {phrase!r} ({why})')
            z4 = z4_runtime_hit(line)
            if z4:
                errors.append(f'SPEC-DRIFT {rel}:{lineno} {z4}')


def check_file_scoped_regressions(errors: list[str]) -> None:
    """Exact stale wordings that are only invalid in their canonical file."""
    for rel, phrases in FILE_FORBIDDEN_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        for phrase, why in phrases.items():
            if phrase in text:
                errors.append(f'REGRESSION {rel}: {phrase!r} ({why})')


def check_nonmodule_article_regressions(errors: list[str]) -> None:
    """Apply deterministic Hungarian article guards to active non-module docs too."""
    for path in markdown_files(ACTIVE_ROOT):
        if path.is_relative_to(MODULE_ROOT):
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        rel = path.relative_to(ROOT)
        for pattern, why in ARTICLE_REGRESSIONS:
            for match in pattern.finditer(text):
                errors.append(f'REGRESSION {rel}: {match.group(0)!r} ({why})')


def check_regressions(errors: list[str]) -> None:
    for path in MODULE_ROOT.rglob('*.md'):
        text = path.read_text(encoding='utf-8', errors='replace')
        low = text.lower()
        rel = path.relative_to(ROOT)
        for phrase, why in FORBIDDEN_ANYWHERE.items():
            if phrase.lower() in low:
                errors.append(f'REGRESSION {rel}: {phrase!r} ({why})')
        for pattern, why in ARTICLE_REGRESSIONS:
            for match in pattern.finditer(text):
                errors.append(f'REGRESSION {rel}: {match.group(0)!r} ({why})')
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


HUMAN_DECISION_HEADING = re.compile(r'^###\s+(HUM-[A-Z0-9-]+)\b(.*)$')
UNCHECKED_BOX = re.compile(r'^\s*-\s*\[\s\]\s*(.+)$')
MODULE_PLACEHOLDER = re.compile(r'⟬KITÖLTENDŐ(?:[:][^⟭]*)?⟭')
RUNTIME_OUTPUT_ROW = re.compile(r'^\|\s*[^|]+\|\s*`RUNTIME_OUTPUT`\s*\|')
BUILD_OUTPUT_ROW = re.compile(r'^\|\s*LMS-[^|]+\|\s*BUILD_OUTPUT\s*\|')


def open_human_decision_ids(text: str) -> list[str]:
    """Return canonical HUM-* decisions whose heading is not explicitly closed."""
    open_ids: list[str] = []
    for line in text.splitlines():
        match = HUMAN_DECISION_HEADING.match(line)
        if match and 'LEZÁRVA' not in match.group(2):
            open_ids.append(match.group(1))
    return open_ids


def unchecked_items(text: str) -> list[str]:
    """Return the text of unchecked Markdown checklist items."""
    return [m.group(1).strip() for line in text.splitlines()
            if (m := UNCHECKED_BOX.match(line))]


def unresolved_output_rows(text: str, pattern: re.Pattern[str]) -> int:
    """Count only unresolved table rows, never explanatory prose mentions."""
    return sum(1 for line in text.splitlines() if pattern.match(line))


def release_blockers() -> list[str]:
    """Report canonical unresolved release state without double-counting prose.

    Human decisions live in one source-of-truth document. Generated media
    registers and explanatory mentions of the word KITÖLTENDŐ are deliberately
    not counted as separate blockers.
    """
    blockers: list[str] = []

    # Learner-facing/module source may never carry a real unresolved placeholder.
    module_placeholders: list[str] = []
    for path in MODULE_ROOT.rglob('*.md'):
        for lineno, line in enumerate(
                path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            if MODULE_PLACEHOLDER.search(line):
                module_placeholders.append(f'{path.relative_to(ROOT)}:{lineno}')
    if module_placeholders:
        blockers.append(
            f'MODULE-PLACEHOLDERS {len(module_placeholders)} open: '
            + ', '.join(module_placeholders)
        )

    # Canonical organisational decisions. A decision is closed only when its
    # HUM-* heading itself says LEZÁRVA; prose mentioning KITÖLTENDŐ is irrelevant.
    human_file = ACTIVE_ROOT / 'Emberi jóváhagyás szükséges.md'
    if human_file.exists():
        human_open = open_human_decision_ids(
            human_file.read_text(encoding='utf-8', errors='replace'))
        release_prefixes = (
            'HUM-SAFE-', 'HUM-PRIV-', 'HUM-OPS-', 'HUM-A11Y-', 'HUM-SOMER-',
        )
        release_open = [
            decision_id for decision_id in human_open
            if decision_id.startswith(release_prefixes)
        ]
        if release_open:
            blockers.append(
                f'HUMAN-DECISIONS {len(release_open)} open: '
                + ', '.join(release_open)
            )

    # Concrete LMS build/runtime outputs are implementation facts, not human
    # decisions. They stay blocking until the staging system writes real values.
    runtime_file = ACTIVE_ROOT / 'LMS – H5P runtime acceptance.md'
    if runtime_file.exists():
        runtime_count = unresolved_output_rows(
            runtime_file.read_text(encoding='utf-8', errors='replace'),
            RUNTIME_OUTPUT_ROW,
        )
        if runtime_count:
            blockers.append(
                f'RUNTIME-ACCEPTANCE {runtime_count} unresolved RUNTIME_OUTPUT values'
            )

    manifest_file = ACTIVE_ROOT / 'LMS – activity manifest.md'
    if manifest_file.exists():
        build_count = unresolved_output_rows(
            manifest_file.read_text(encoding='utf-8', errors='replace'),
            BUILD_OUTPUT_ROW,
        )
        if build_count:
            blockers.append(
                f'LMS-BUILD {build_count} unresolved BUILD_OUTPUT values'
            )

    # Release/sign-off checklists are separate evidence layers. Report each once,
    # rather than turning every explanatory placeholder mention into a blocker.
    checklist_files = (
        ('SAFEGUARDING-CHECKLIST', ACTIVE_ROOT / 'Gyermekvédelem – release gate.md'),
        ('PRIVACY-CHECKLIST', ACTIVE_ROOT / 'Adatvédelem – tanulói adatok és AI.md'),
        ('A11Y-CHECKLIST', ACTIVE_ROOT / 'LMS – hozzáférhetőségi sztenderd.md'),
        ('PROGRAM-TRANSFER', ACTIVE_ROOT / 'RELEASE-READINESS.md'),
    )
    for label, path in checklist_files:
        if not path.exists():
            continue
        items = unchecked_items(path.read_text(encoding='utf-8', errors='replace'))
        if items:
            blockers.append(f'{label} {len(items)} open checklist items')

    return blockers


def production_blockers() -> list[str]:
    """Report unresolved media-production decisions without redefining release.

    RELEASE-MEDIA-STATUS.md explicitly permits equivalent fallbacks and states
    that R2/R3/R5 do not block the internal M0+M1 staging pilot. Therefore these
    are operational production blockers, not automatic learner-release gates.
    """
    blockers: list[str] = []

    human_file = ACTIVE_ROOT / 'Emberi jóváhagyás szükséges.md'
    if human_file.exists():
        human_open = open_human_decision_ids(
            human_file.read_text(encoding='utf-8', errors='replace'))
        media_open = [
            decision_id for decision_id in human_open
            if decision_id.startswith('HUM-MEDIA-')
        ]
        if media_open:
            blockers.append(
                f'MEDIA-HUMAN-DECISIONS {len(media_open)} open: '
                + ', '.join(media_open)
            )

    rules_file = MEDIA_ROOT / 'produkcios-szabalyok.json'
    if rules_file.exists():
        payload = json.loads(rules_file.read_text(encoding='utf-8'))
        open_rules = [
            rule['id'] for rule in payload.get('rules', [])
            if '⟬KITÖLTENDŐ⟭' in rule.get('text', '')
        ]
        if open_rules:
            blockers.append(
                f'PRODUCTION-RULES {len(open_rules)} open: '
                + ', '.join(open_rules)
            )

    return blockers


# Regression cases for the rule matcher itself. Kept next to the rules so a rule
# change and its expectation move together; run with ``--selftest``.
SELFTEST_CASES = [
    ('Alatta 1 szövegmező (Short Answer) a lezáró mondathoz.', True, 'aktív spec — „Short Answer”'),
    ('Alatta 1 szövegmező (Short answer) a lezáró mondathoz.', True, 'aktív spec — „Short answer”'),
    ('Alatta 1 szövegmező (short answer) a lezáró mondathoz.', True, 'aktív spec — „short answer”'),
    ('A hivatalos H5P listában **nincs „Short Answer”** — helyette Essay van.', False, 'kánoni dokumentáció kivétel'),
    ('Forrás: h5p.org content type lista — „Short Answer” nem szerepel.', False, 'kánoni dokumentáció kivétel'),
    ('Alatta 1 rövid szabad szöveges mező a lezáró mondathoz.', False, 'legitim magyar szöveg'),
    # 'felirat VAGY' is deliberately case-sensitive: the stale-spec construction
    # must fail, ordinary Hungarian prose must not.
    ('Elég a felirat VAGY a leirat valamelyike.', True, 'aktív spec — „felirat VAGY”'),
    ('A videóhoz felirat vagy a leirat is elérhető lesz.', False, 'legitim magyar prózai „vagy”'),
]
ARTICLE_SELFTEST = [
    ('az **aktív felidézés** segít', True, 'helyes névelő'),
    ('a **aktív felidézés** segít', False, 'hibás névelő'),
    ('akkor a legerősebb, ha **aktív felidézéssel** párosul', True, '„ha aktív” nem false positive'),
    ('Mi az „időben elosztott gyakorlás”?', True, 'helyes névelő időben'),
    ('Mi a „időben elosztott gyakorlás”?', False, 'hibás névelő időben'),
    ('az M7.3 után folytatjuk', True, 'helyes névelő modulazonosító előtt'),
    ('a M7.3 után folytatjuk', False, 'hibás névelő modulazonosító előtt'),
    ('az `M1.2 – Megfigyelés ≠ értelmezés` leckével mész tovább', True, 'helyes névelő kódolt modulazonosító előtt'),
    ('a `M1.2 – Megfigyelés ≠ értelmezés` leckével mész tovább', False, 'hibás névelő kódolt modulazonosító előtt'),
]

# The deliberate-exclusion guard must cover the Z.4 Documentation Tool rule too,
# not only ACTIVE_SPEC_RULES — a refactor already dropped that once. These cases
# run `z4_runtime_hit`, i.e. the function `check_active_spec` itself calls.
SELFTEST_Z4 = [
    ('Nem támaszkodunk H5P Documentation Tool session-resume állításra.', False, 'Z.4 — tudatos kizárás'),
    ('a Z.4 NEM Documentation Toolra épül, hanem Moodle Assignmentre', False, 'Z.4 — tudatos kizárás'),
    ('A Z.4 hosszú reflexió H5P Documentation Toolban készül.', True, 'Z.4 — valódi spec-drift'),
    ('A Z.4 Moodle Assignmentben készül.', False, 'Z.4 — helyes futtatókörnyezet'),
]


def selftest() -> int:
    """Assert the ACTIVE_SPEC matcher behaves on known-tricky lines."""
    failures = 0
    for line, should_fail, label in SELFTEST_CASES:
        hits = active_spec_hits(line)
        ok = bool(hits) == should_fail
        if not ok:
            failures += 1
        want = 'FAIL' if should_fail else 'PASS'
        got = 'FAIL' if hits else 'PASS'
        mark = 'ok  ' if ok else 'HIBA'
        print(f'{mark} {label}: várt={want} kapott={got}' + (f' {[p for p, _ in hits]}' if hits else ''))
    for line, should_fail, label in SELFTEST_Z4:
        got = z4_runtime_hit(line) is not None
        ok = got == should_fail
        if not ok:
            failures += 1
        want = 'FAIL' if should_fail else 'PASS'
        print(f'{"ok  " if ok else "HIBA"} {label}: várt={want} kapott={"FAIL" if got else "PASS"}')
    for line, should_pass, label in ARTICLE_SELFTEST:
        got = any(pattern.search(line) for pattern, _ in ARTICLE_REGRESSIONS)
        ok = (not got) == should_pass
        if not ok:
            failures += 1
        print(f'{"ok  " if ok else "HIBA"} {label}: várt={"PASS" if should_pass else "FAIL"} kapott={"FAIL" if got else "PASS"}')
    decision_fixture = (
        '### HUM-SAFE-01 — nyitott\n'
        '### HUM-MEDIA-01 — produkciós\n'
        '### HUM-GOV-01 — lezárt — LEZÁRVA\n'
    )
    decision_ok = open_human_decision_ids(decision_fixture) == [
        'HUM-SAFE-01', 'HUM-MEDIA-01'
    ]
    if not decision_ok:
        failures += 1
    print(f'{"ok  " if decision_ok else "HIBA"} release-parser — HUM döntés státusz')

    release_ids = [
        decision_id for decision_id in open_human_decision_ids(decision_fixture)
        if decision_id.startswith(
            ('HUM-SAFE-', 'HUM-PRIV-', 'HUM-OPS-', 'HUM-A11Y-', 'HUM-SOMER-')
        )
    ]
    separation_ok = release_ids == ['HUM-SAFE-01']
    if not separation_ok:
        failures += 1
    print(f'{"ok  " if separation_ok else "HIBA"} release-parser — release/media szétválasztás')

    checklist_fixture = '- [ ] nyitott\n- [x] kész\n'
    checklist_ok = unchecked_items(checklist_fixture) == ['nyitott']
    if not checklist_ok:
        failures += 1
    print(f'{"ok  " if checklist_ok else "HIBA"} release-parser — checklist')

    output_fixture = (
        '> `cmid`: **BUILD_OUTPUT**, magyarázó definíció.\n'
        '| LMS-X-01 | BUILD_OUTPUT | M0 | valódi sor |\n'
        '| Moodle | `RUNTIME_OUTPUT` | RUN_DATE | TEST_OWNER |\n'
    )
    output_ok = (
        unresolved_output_rows(output_fixture, BUILD_OUTPUT_ROW) == 1
        and unresolved_output_rows(output_fixture, RUNTIME_OUTPUT_ROW) == 1
    )
    if not output_ok:
        failures += 1
    print(f'{"ok  " if output_ok else "HIBA"} release-parser — output táblázatsorok')

    total = len(SELFTEST_CASES) + len(SELFTEST_Z4) + len(ARTICLE_SELFTEST) + 4
    print(f'Selftest: {total - failures}/{total} eset rendben.')
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict-release', action='store_true', help='also fail when release blockers remain')
    parser.add_argument('--release-report', action='store_true', help='print release blockers but do not fail for them')
    parser.add_argument('--selftest', action='store_true', help='run the rule-matcher regression cases and exit')
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    errors: list[str] = []
    check_structure(errors)
    check_links(errors)
    check_conflict_markers(errors)
    check_terminology(errors)
    check_active_spec(errors)
    check_file_scoped_regressions(errors)
    check_nonmodule_article_regressions(errors)
    check_regressions(errors)

    blockers = release_blockers() if (args.strict_release or args.release_report) else []
    production = production_blockers() if args.release_report else []

    print(f'Objective integrity errors: {len(errors)}')
    for item in errors:
        print(f'ERROR: {item}')
    if blockers:
        print(f'Release blockers: {len(blockers)}')
        for item in blockers:
            print(f'BLOCKER: {item}')
    if production:
        print(f'Production-only blockers: {len(production)}')
        for item in production:
            print(f'PRODUCTION: {item}')

    if errors:
        return 1
    if args.strict_release and blockers:
        return 2
    print('Objective content integrity checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
