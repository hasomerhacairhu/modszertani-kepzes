#!/usr/bin/env python3
"""Static integrity checks for the training repository.

Read-only and deterministic. Two separate concerns:

* **Objective errors** (exit 1) — things that are simply wrong in the repository:
  broken internal links, resurrected duplicate canonical files, merge-conflict
  markers, terminology drift, and a small set of *known* content regressions that
  have actually happened here before and are dangerous to reintroduce.
* **Release state** (reported with ``--release-report``; failing only with
  ``--strict-release``) — two verdicts since the release-model v2 owner decisions of
  2026-10-04 (`Emberi jóváhagyás szükséges.md` §10):
  ``MOODLE-BUILD-VERDICT`` (``NOT_READY`` / ``READY_FOR_STAGING_BUILD``) asks whether
  the spec is ready to be built; evidence that only a build or a runtime test can
  produce never blocks it. ``LEARNER-RELEASE-VERDICT`` (``NO-GO`` /
  ``CONTENT_READY / MEDIA_PENDING`` / ``READY_FOR_CONTROLLED_PILOT``) asks whether the
  built system may go to real participants as a controlled pilot. Program transfer
  is a post-release lifecycle phase, not a gate. ``RELEASE-VERDICT`` is a
  compatibility alias of the learner verdict for one release cycle. Nothing is
  guessed or auto-filled.

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

# Files whose duplicates were deleted during the 2026-08 canonicalisation, and the
# old names of the files renamed by the 2026-09 consolidation (PR #8). If one
# reappears, two "canonical" versions of the same lesson exist again.
LEGACY_PATHS = [
    '02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-től a használható visszajelzésig (45’).md',
    '02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyerekvédelem.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyerekvédelem 101 – red flag felismerése & első lépések.md',
    '02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyerekvédelem (Study Lab).md',
    '02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md',
    '02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v2 + AI – modulproduktum váz.md',
    '02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a gate.md',
    '02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, feedback – Önismeret & visszajelzés – Johari + SBI.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md',
    '02 Tervezet/Modulok/M4/Online leckék/M4.4 – 45 mp-es peula-pitch – vázlat egy konkrét kvucára.md',
    '02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & pitch gyakorlása.md',
    '02 Tervezet/Modulok/M4/Peulák/M4.F – Felzárkóztató peula – Test, hang, kérdések & pitch (Study Lab).md',
    '02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, visszahívás, spacing.md',
    '02 Tervezet/Modulok/M6/M6 – Toolbox – játék, történet, kézműves & inkluzivitás.md',
    '02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md',
    '02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md',
    '02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap workshop – saját eszköz tervezése (45’).md',
    '02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Toolbox & játéklap (Study Lab).md',
    '02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 timeline.md',
    '02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md',
    # 2026-10-02 projektgazdai döntés: „lépéstérkép” és „Nemcsak” (egyszeri, atomikus átnevezés).
    '02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md',
    '02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nem csak játék, hanem peula – 11 tervezési pont & AI-támogatás.md',
    # 2026-10-02 projektgazdai döntés (HUM-SOMER-02): helyi Somer-írásmód (madrih, dugma isit, Leviatán).
    '02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrich, nem terapeuta – szerepek és elvárások.md',
    '02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma ishit az online térben + bemutatkozó fórum.md',
    '02 Tervezet/Modulok/M2/M2 – Ki vagyok madrichként – Identitás, Somer-értékek és dugma ishit.md',
    '02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md',
    '02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan – 3 kvuca, 3 világ.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md',
    '02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrichként.md',
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
        'a 15+ célcsoportban a madrih maga is lehet kiskorú, nem ő az egyedüli felelős felnőtt',
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
            'a tananyag a háromcsoportos korosztálymodellt használja (HUM-SOMER-02: javasolt, jóváhagyásra vár)',
        '4 kvuca-profil':
            'az M3 aktuális korosztálymodellje Parparim 6–9, Kivsza 10–12, Leviatan 13–17',
    },
    '02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md': {
        '6–10 / 11–13 / 14–16 / 16+':
            'az M6 korosztály-illesztése a három aktuális kvucát használja (HUM-SOMER-02)',
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
            'az M7 kvuca-választója a három aktuális kvucát használja (HUM-SOMER-02)',
        'Parparim / Kivsza / Leviatán / Zorea':
            'az M7 kvuca-választója a három aktuális kvucát használja (HUM-SOMER-02)',
    },
    '02 Tervezet/Média-assetek/produkcios-szabalyok.json': {
        '4-kvuca piktogramok':
            'az R5 produkciós szabály is a három aktuális kvucát használja (HUM-SOMER-02)',
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
    'biztonságos felnőttként': '15+ célcsoportban a madrih maga is lehet kiskorú, nem ő a felelős felnőtt',
    'megbízható felnőtt': '15+ célcsoportban a madrih maga is lehet kiskorú, nem ő a felelős felnőtt',
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

# The separate Zorea age group is gone (three-group model, HUM-SOMER-02: applied,
# awaiting approval). A per-file phrase list missed the inflected "Zoreánál" in
# M3.A, so the stem is checked in every module file: in the visible text and in
# the media metadata that specifies what gets produced (title, purpose, spec …).
# Only the historical record of an asset (notes, legacy, review) may still say
# where the old profile went.
RETIRED_AGE_GROUP = re.compile(r'zore', re.I)
METADATA_OPEN = re.compile(r'^\s*<!--\s*@(?:asset-free|asset|source)\b')
HISTORICAL_FIELDS = frozenset({'notes', 'legacy', 'review'})


def _names_retired_group(value, top_level: bool = True) -> bool:
    if isinstance(value, str):
        return bool(RETIRED_AGE_GROUP.search(value))
    if isinstance(value, dict):
        return any(_names_retired_group(v, False) for k, v in value.items()
                   if not (top_level and k in HISTORICAL_FIELDS))
    if isinstance(value, list):
        return any(_names_retired_group(v, False) for v in value)
    return False


def retired_age_group_hits(text: str) -> list[int]:
    """Line numbers where module text or a production spec names the retired Zorea group.

    A metadata block is reported at its opening line. A block whose JSON cannot be
    read is checked line by line, so a broken block never hides a hit.
    """
    hits: list[int] = []
    lines = text.splitlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if METADATA_OPEN.match(line):
            end = idx
            while '-->' not in lines[end] and end + 1 < len(lines):
                end += 1
            block = '\n'.join(lines[idx:end + 1])
            start, stop = block.find('{'), block.rfind('}')
            try:
                payload = json.loads(block[start:stop + 1]) if 0 <= start < stop else {}
            except ValueError:
                payload = None
            if payload is None:
                hits.extend(n + 1 for n in range(idx, end + 1) if RETIRED_AGE_GROUP.search(lines[n]))
            elif _names_retired_group(payload):
                hits.append(idx + 1)
            idx = end + 1
            continue
        if RETIRED_AGE_GROUP.search(line):
            hits.append(idx + 1)
        idx += 1
    return hits


CONFLICT_MARKERS = re.compile(r'^(?:<{7}|={7}|>{7})(?:\s|$)', re.M)
RESUME_PROMISE = re.compile(r'(mentve marad|később folytathatod|folytathatod később)')
STALE_TERM = re.compile(r'[Gg]yerekvéd')
ARTICLE_REGRESSIONS = (
    (re.compile(r'(?<!\w)a\s+\*{0,2}aktív\b', re.I), 'hibás névelő: az aktív'),
    (re.compile(r'(?<!\w)a\s+[„"\']aktív\b', re.I), 'hibás névelő: az aktív'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}időben\b', re.I), 'hibás névelő: az időben'),
    (re.compile(r'(?<!\w)a\s+[„"\']időben\b', re.I), 'hibás névelő: az időben'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}eredetet\b', re.I), 'hibás névelő: az eredetet'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}idősebb\b', re.I), 'hibás névelő: az idősebb'),
    (re.compile(r'(?<!\w)az\s+\*{0,2}SMART(?=[\s-])', re.I), 'hibás névelő: a SMART…'),
    (re.compile(r'(?<!\w)a\s+\*{0,2}\[?[„"`]?M[0-7](?=[.\-–\sA-Z])', re.I),
     'hibás névelő modulazonosító előtt: az M…'),
    (re.compile(r'(?<!\w)[Aa]\s+[*„"`\[]{0,3}LMS\b'), 'hibás névelő: az LMS'),
    (re.compile(r'(?<!\w)[Aa]z\s+[*„"`\[]{0,3}H5P\b'), 'hibás névelő: a H5P'),
    (re.compile(r'(?<!\w)[Aa]\s+[*„"`]{0,3}S–B'), 'hibás névelő: az S–B…'),
    (re.compile(r'(?<!\w)[Aa]\s+[*„"`]{0,3}NIDCD\b'), 'hibás névelő: az NIDCD'),
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
        for lineno in retired_age_group_hits(text):
            errors.append(f'REGRESSION {rel}:{lineno} Zorea (a tananyag a háromcsoportos '
                          'korosztálymodellt használja; HUM-SOMER-02: javasolt, jóváhagyásra vár)')
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
# Release-model v2 (2026-10-04, RM-D1…D6): a P0/a11y runtime test that has not run
# yet, and an activity definition that cannot be built yet. Each is a table row.
RUNTIME_TEST_OPEN_ROW = re.compile(r'^\|\s*RT-[A-Z0-9-]+\s*\|\s*`?IMPLEMENTATION_TEST_REQUIRED`?\s*\|')
BUILD_SPEC_OPEN_ROW = re.compile(r'^\|\s*(BSPEC-\d+)\s*\|\s*`?BUILD_SPEC_OPEN`?\s*\|')
# A checklist item's gate class: `- [ ] … <!-- gate: post-build -->`. Without a tag
# the item is unclassified, and an unclassified item blocks the build (fail-safe).
CHECKLIST_GATE_TAG = re.compile(r'<!--\s*gate:\s*([^>]*?)\s*-->')
GATE_CLASSES = ('build', 'post-build', 'release-evidence', 'human-qa', 'signoff', 'lifecycle')
# RIGHTS-EVIDENCE.md §1/A.5: a legal/safeguarding media sub-gate (J1, J2, V1, V3…)
# still missing its evidence. Read so that clearing the R2 marker alone cannot open
# the legal media gate.
RIGHTS_SUBGATE_MISSING = re.compile(r'^\|\s*\*\*([JV]\d+)\*\*\s*\|.*\*\*HIÁNYZIK\*\*')
# Q-MED-1 phases read straight from the decision: narration is phase B, video is
# phase C. Every other kind is phase A until the media manifest carries
# release_phase (fail-safe: phase A is release-mandatory).
KIND_DEFAULT_PHASE = {'voiceover': 'B', 'video': 'C'}

BUILD_NOT_READY = 'NOT_READY'
BUILD_READY = 'READY_FOR_STAGING_BUILD'
LEARNER_NO_GO = 'NO-GO'
LEARNER_MEDIA_PENDING = 'CONTENT_READY / MEDIA_PENDING'
LEARNER_PILOT_READY = 'READY_FOR_CONTROLLED_PILOT'

# Where each blocker of the single-verdict model (before 2026-10-04) went. The
# selftest checks that a fixture of each lands in exactly one new bucket.
LEGACY_BLOCKER_CATEGORY = {
    'ERROR': 'build_spec',
    'MODULE-PLACEHOLDERS': 'build_spec',
    'HUMAN-DECISIONS': 'build_spec',
    'RUNTIME-ACCEPTANCE': 'learner',
    'LMS-BUILD': 'learner',
    'SAFEGUARDING-CHECKLIST': 'by gate tag (untagged: build_spec)',
    'PRIVACY-CHECKLIST': 'by gate tag (untagged: build_spec)',
    'A11Y-CHECKLIST': 'by gate tag (untagged: build_spec)',
    'PROGRAM-TRANSFER': 'lifecycle',
    'PRODUCTION-RULES': 'asset-level media (build_spec or media_release)',
    'MEDIA-HUMAN-DECISIONS': 'media_release',
    'GOVERNANCE-DECISIONS': 'governance',
}


# Which report an open HUM-* decision belongs to. A prefix not listed here falls
# back to 'release' on purpose: before 2026-10 an open HUM-GOV decision was
# printed by neither report, so a new or unknown prefix must fail safe.
PRODUCTION_DECISION_PREFIXES = ('HUM-MEDIA-',)
GOVERNANCE_DECISION_PREFIXES = ('HUM-GOV-',)

# A LEZÁRVA heading alone once closed two decisions whose approver line had been
# deleted. RELEASE-READINESS.md: a gate is closed only with the decision, its
# date, its approver and its evidence recorded.
# A field's value is read on its own line and ends at the next bold label, a
# table pipe or the line end: an empty field must not borrow the next field's text.
_FIELD_VALUE = r'[ \t]*(?:\|[ \t]*)?((?:(?!\*\*[^*\n|]{1,40}:\*\*|\*\*[^*\n|]{1,40}\*\*:)[^|\n])*)'
CLOSURE_FIELDS = (
    ('dátum', re.compile(r'\*\*Lezárva:?\*\*:?[ \t]*(?:\|[ \t]*)?(\d{4}-\d{2}-\d{2})\b')),
    ('jóváhagyó', re.compile(r'\*\*Jóváhagyta:?\*\*:?' + _FIELD_VALUE)),
    ('bizonyíték', re.compile(r'\*\*Bizonyíték:?\*\*:?' + _FIELD_VALUE)),
)
PLACEHOLDER_VALUE = re.compile(r'KITÖLTENDŐ|⟬|\[\s*\]|\bTBD\b|^[\s.…—–-]*$')


def decision_register(decision_id: str) -> str:
    """'production', 'governance' or — the fail-safe default — 'release'."""
    if decision_id.startswith(PRODUCTION_DECISION_PREFIXES):
        return 'production'
    if decision_id.startswith(GOVERNANCE_DECISION_PREFIXES):
        return 'governance'
    return 'release'


def closed_decision_sections(text: str) -> list[tuple[str, str]]:
    """(id, body) of every HUM-* decision whose heading says LEZÁRVA."""
    sections: list[tuple[str, str]] = []
    current: str | None = None
    body: list[str] = []
    for line in text.splitlines():
        heading = HUMAN_DECISION_HEADING.match(line)
        if heading or line.startswith(('# ', '## ', '---')):
            if current is not None:
                sections.append((current, '\n'.join(body)))
            current = (heading.group(1)
                       if heading and 'LEZÁRVA' in heading.group(2) else None)
            body = []
        elif current is not None:
            body.append(line)
    if current is not None:
        sections.append((current, '\n'.join(body)))
    return sections


def unevidenced_closures(text: str) -> list[str]:
    """Closed decisions that lack a closing date, the approver or the evidence."""
    defects: list[str] = []
    for decision_id, body in closed_decision_sections(text):
        missing = []
        for label, pattern in CLOSURE_FIELDS:
            match = pattern.search(body)
            value = match.group(1).strip(' *') if match else ''
            if not value or PLACEHOLDER_VALUE.search(value):
                missing.append(label)
        if missing:
            defects.append(f'{decision_id}: hiányzó lezárási mező: {", ".join(missing)}')
    return defects


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


def classify_checklist(text: str) -> list[tuple[str, str | None, bool]]:
    """(text, gate class or None, repo-fixable) of every unchecked checklist item.

    The class comes from a trailing `<!-- gate: … -->` comment. No tag, an unknown
    word or two classes leave the item unclassified (None), which blocks the build:
    until the item is classified nobody knows whether the build needs it. A tag
    with only `repo-fixable` means a spec fix, so it counts as `build`.
    """
    items: list[tuple[str, str | None, bool]] = []
    for line in text.splitlines():
        match = UNCHECKED_BOX.match(line)
        if not match:
            continue
        body = match.group(1)
        gate_class: str | None = None
        fixable = False
        tag = CHECKLIST_GATE_TAG.search(body)
        if tag:
            words = [w.strip() for w in tag.group(1).split(',') if w.strip()]
            fixable = 'repo-fixable' in words
            classes = [w for w in words if w in GATE_CLASSES]
            unknown = [w for w in words if w not in GATE_CLASSES and w != 'repo-fixable']
            if not unknown and len(classes) == 1:
                gate_class = classes[0]
            elif not unknown and not classes and fixable:
                gate_class = 'build'
            body = CHECKLIST_GATE_TAG.sub('', body)
        items.append((body.strip(), gate_class, fixable))
    return items


def missing_rights_subgates(text: str) -> list[str]:
    """IDs of the legal/safeguarding media sub-gates still marked HIÁNYZIK."""
    return [m.group(1) for line in text.splitlines()
            if (m := RIGHTS_SUBGATE_MISSING.match(line))]


# The checklist sources of the release state. RELEASE-READINESS.md holds the
# lifecycle item (program transfer) and the go/no-go and G4b evidence items.
CHECKLIST_SOURCES = (
    ('SAFEGUARDING', 'Gyermekvédelem – release gate.md'),
    ('PRIVACY', 'Adatvédelem – tanulói adatok és AI.md'),
    ('A11Y', 'LMS – hozzáférhetőségi sztenderd.md'),
    ('RELEASE-READINESS', 'RELEASE-READINESS.md'),
)


def _read(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''


def collect_release_inputs() -> dict:
    """Read every source of the release state. No classification happens here."""
    module_placeholders: list[str] = []
    for path in MODULE_ROOT.rglob('*.md'):
        for lineno, line in enumerate(_read(path).splitlines(), 1):
            if MODULE_PLACEHOLDER.search(line):
                module_placeholders.append(f'{path.relative_to(ROOT)}:{lineno}')

    human_open = open_human_decision_ids(_read(ACTIVE_ROOT / 'Emberi jóváhagyás szükséges.md'))
    runtime_text = _read(ACTIVE_ROOT / 'LMS – H5P runtime acceptance.md')
    manifest_text = _read(ACTIVE_ROOT / 'LMS – activity manifest.md')

    rules_file = MEDIA_ROOT / 'produkcios-szabalyok.json'
    open_rules: list[str] = []
    if rules_file.exists():
        payload = json.loads(rules_file.read_text(encoding='utf-8'))
        open_rules = [rule['id'] for rule in payload.get('rules', [])
                      if '⟬KITÖLTENDŐ⟭' in rule.get('text', '')]

    media_manifest = MEDIA_ROOT / '_build' / 'media-manifest.v2.json'
    assets = (json.loads(media_manifest.read_text(encoding='utf-8')).get('assets', [])
              if media_manifest.exists() else None)

    return {
        'module_placeholders': module_placeholders,
        'human_open_release': [d for d in human_open if decision_register(d) == 'release'],
        'human_open_media': [d for d in human_open if decision_register(d) == 'production'],
        'environment_rows': unresolved_output_rows(runtime_text, RUNTIME_OUTPUT_ROW),
        'runtime_tests_open': unresolved_output_rows(runtime_text, RUNTIME_TEST_OPEN_ROW),
        'build_output_rows': unresolved_output_rows(manifest_text, BUILD_OUTPUT_ROW),
        'build_spec_open': [m.group(1) for line in manifest_text.splitlines()
                            if (m := BUILD_SPEC_OPEN_ROW.match(line))],
        'checklists': {label: classify_checklist(_read(ACTIVE_ROOT / name))
                       for label, name in CHECKLIST_SOURCES},
        'open_rules': open_rules,
        'rights_missing': missing_rights_subgates(_read(MEDIA_ROOT / 'RIGHTS-EVIDENCE.md')),
        'assets': assets,
    }


def media_assessment(assets: list[dict], legal_gate_open: bool) -> tuple[list[str], list[str], int]:
    """Asset-level media gate (Q-MED-1, RM-D4).

    Returns (phase-A assets on an open media gate without a fallback — a build-spec
    gap; phase-A assets on an open gate shipping a temporary fallback — media
    pending; number of assets without an explicit release_phase). Phase B and C
    always carry a fallback under Q-MED-1, so they never block.
    """
    build_blocked: list[str] = []
    pending: list[str] = []
    unassigned = 0
    for asset in assets:
        if not asset.get('release_phase'):
            unassigned += 1
        phase = asset.get('release_phase') or KIND_DEFAULT_PHASE.get(asset.get('kind'), 'A')
        gated = (asset.get('status') != 'spec-ready'
                 or ('R2' in (asset.get('production_rules') or []) and legal_gate_open))
        if not gated or phase != 'A' or asset.get('fallback_final'):
            continue
        (pending if asset.get('fallback') else build_blocked).append(asset.get('id', '?'))
    return build_blocked, pending, unassigned


def _checklist_summary(items_by_source: dict[str, list[str]]) -> str:
    return ', '.join(f'{label} {len(items)}' for label, items in items_by_source.items() if items)


def assemble_release_state(inputs: dict) -> dict[str, list[str]]:
    """Sort every open item into exactly one bucket of the two-verdict model.

    build_spec    — blocks MOODLE-BUILD-VERDICT (and therefore the learner verdict)
    learner       — blocks LEARNER-RELEASE-VERDICT only (post-build, evidence, QA, sign-off)
    media_release — CONTENT_READY / MEDIA_PENDING
    lifecycle     — reported, never a gate (program transfer, Q-REL-1)
    media_info    — reported for orientation, never a gate by itself
    """
    state: dict[str, list[str]] = {
        'build_spec': [], 'learner': [], 'media_release': [], 'lifecycle': [], 'media_info': [],
    }
    build_spec, learner = state['build_spec'], state['learner']

    if inputs['module_placeholders']:
        build_spec.append(f'SOURCE-PLACEHOLDERS {len(inputs["module_placeholders"])} open: '
                          + ', '.join(inputs['module_placeholders']))
    if inputs['human_open_release']:
        build_spec.append(f'HUMAN-DECISIONS {len(inputs["human_open_release"])} open: '
                          + ', '.join(inputs['human_open_release']))
    if inputs['build_spec_open']:
        build_spec.append(f'MANIFEST-OPEN {len(inputs["build_spec_open"])} open: '
                          + ', '.join(inputs['build_spec_open']))

    by_class: dict[str | None, dict[str, list[str]]] = {}
    for label, items in inputs['checklists'].items():
        for text, gate_class, _fixable in items:
            by_class.setdefault(gate_class, {}).setdefault(label, []).append(text)

    def checklist_line(prefix: str, gate_class: str | None) -> str | None:
        sources = by_class.get(gate_class, {})
        count = sum(len(items) for items in sources.values())
        return f'{prefix} {count} open ({_checklist_summary(sources)})' if count else None

    for prefix, gate_class, bucket in (
            ('CHECKLIST-BUILD', 'build', build_spec),
            ('CHECKLIST-UNCLASSIFIED', None, build_spec),
            ('POST-BUILD: CHECKLIST', 'post-build', learner),
            ('RELEASE-EVIDENCE: CHECKLIST', 'release-evidence', learner),
            ('FINAL-RELEASE-QA: CHECKLIST', 'human-qa', learner),
            ('SIGNOFF: CHECKLIST', 'signoff', learner),
            ('PROGRAM-TRANSFER', 'lifecycle', state['lifecycle'])):
        line = checklist_line(prefix, gate_class)
        if line:
            bucket.append(line + (' — release utáni validáció (Q-REL-1), nem kapu'
                                  if gate_class == 'lifecycle' else ''))

    if inputs['build_output_rows']:
        learner.append(f'POST-BUILD: BUILD-OUTPUT {inputs["build_output_rows"]} unresolved BUILD_OUTPUT values')
    if inputs['environment_rows']:
        learner.append(f'POST-BUILD: ENVIRONMENT-RECORD {inputs["environment_rows"]} unresolved RUNTIME_OUTPUT values')
    if inputs['runtime_tests_open']:
        learner.append(f'POST-BUILD: RUNTIME-TESTS {inputs["runtime_tests_open"]} not RUNTIME_VERIFIED')

    legal_gate_open = 'R2' in inputs['open_rules'] or bool(inputs['rights_missing'])
    if inputs['assets'] is None:
        build_spec.append('MEDIA-MANIFEST-MISSING: a média-manifest nélkül a release-kötelező assetek nem értékelhetők')
    else:
        blocked, pending, unassigned = media_assessment(inputs['assets'], legal_gate_open)
        if blocked:
            build_spec.append(f'MEDIA-REQUIRED-WITHOUT-FALLBACK {len(blocked)}: ' + ', '.join(blocked))
        if pending:
            state['media_release'].append(f'MEDIA-ASSETS {len(pending)} on fallback: ' + ', '.join(pending))
        if unassigned:
            state['media_info'].append(
                f'MEDIA-PHASE-UNASSIGNED {unassigned} asset (release_phase hiányzik; '
                'alapértelmezés: voiceover → B, video → C, minden más → A)')
    if inputs['human_open_media']:
        state['media_release'].append(f'MEDIA-HUMAN-DECISIONS {len(inputs["human_open_media"])} open: '
                                      + ', '.join(inputs['human_open_media']))
    if inputs['open_rules']:
        state['media_info'].append(f'PRODUCTION-RULES {len(inputs["open_rules"])} open: '
                                   + ', '.join(inputs['open_rules']) + ' (asset-szinten értékelve)')
    if inputs['rights_missing']:
        state['media_info'].append(f'RIGHTS-SUBGATES {len(inputs["rights_missing"])} HIÁNYZIK: '
                                   + ', '.join(inputs['rights_missing']))
    return state


def build_verdict(errors: list[str], build_spec: list[str]) -> str:
    """MOODLE-BUILD-VERDICT. An objective error is never build-ready (RM-D4)."""
    return BUILD_NOT_READY if errors or build_spec else BUILD_READY


def learner_verdict(build: str, learner: list[str], media_release: list[str]) -> str:
    """LEARNER-RELEASE-VERDICT. Nothing is learner-ready before the build is."""
    if build != BUILD_READY or learner:
        return LEARNER_NO_GO
    if media_release:
        return LEARNER_MEDIA_PENDING
    return LEARNER_PILOT_READY


def governance_items() -> list[str]:
    """Open governance decisions: reported, but not a learner-release gate.

    A HUM-GOV-* entry blocks an organisational report (e.g. the field KPI), not
    the Moodle release, so it gets its own line instead of disappearing.
    """
    human_file = ACTIVE_ROOT / 'Emberi jóváhagyás szükséges.md'
    if not human_file.exists():
        return []
    human_open = open_human_decision_ids(
        human_file.read_text(encoding='utf-8', errors='replace'))
    governance_open = [
        decision_id for decision_id in human_open
        if decision_register(decision_id) == 'governance'
    ]
    if not governance_open:
        return []
    return [f'GOVERNANCE-DECISIONS {len(governance_open)} open: '
            + ', '.join(governance_open)]


def check_closed_decisions(errors: list[str]) -> None:
    """A HUM-* decision may be LEZÁRVA only with date, approver and evidence."""
    human_file = ACTIVE_ROOT / 'Emberi jóváhagyás szükséges.md'
    if not human_file.exists():
        return
    rel = human_file.relative_to(ROOT)
    text = human_file.read_text(encoding='utf-8', errors='replace')
    for defect in unevidenced_closures(text):
        errors.append(f'UNEVIDENCED-CLOSURE {rel} {defect}')


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
    ('jelöld meg az eredetet', True, 'helyes névelő eredetet előtt'),
    ('jelöld meg a eredetet', False, 'hibás névelő eredetet előtt'),
    ('ehhez az idősebb Leviatan-kvucához', True, 'helyes névelő idősebb előtt'),
    ('ehhez a idősebb Leviatan-kvucához', False, 'hibás névelő idősebb előtt'),
    ('a SMART 5 eleme', True, 'helyes névelő SMART előtt'),
    ('az [M1 – KAPU – értékelő](./M1.md) szerint', True, 'helyes névelő linkelt modulazonosító előtt'),
    ('a [M1 – KAPU – értékelő](./M1.md) szerint', False, 'hibás névelő linkelt modulazonosító előtt'),
    ('az `LMS – activity manifest.md` szerint', True, 'helyes névelő kódolt LMS előtt'),
    ('a `LMS – activity manifest.md` szerint', False, 'hibás névelő kódolt LMS előtt'),
    ('A LMS-ben nincs ilyen mező', False, 'hibás névelő LMS előtt (mondatkezdő)'),
    ('a H5P Course Presentation', True, 'helyes névelő H5P előtt'),
    ('az H5P beépített kvíz-UI', False, 'hibás névelő H5P előtt'),
    ('a SLIDE 3 kérdése', True, '„a SLIDE” nem false positive'),
    ('az S–B–I modell', True, 'helyes névelő S–B–I előtt'),
    ('a S–B–I modell', False, 'hibás névelő S–B–I előtt'),
    ('az amerikai NIDCD szerint', True, 'helyes névelő NIDCD előtt (jelzővel)'),
    ('a NIDCD szerint', False, 'hibás névelő NIDCD előtt'),
    ('A SBI-mondata', True, 'szerepbetű, nem névelő: nem false positive'),
    ('az SMART 5 eleme', False, 'hibás névelő SMART előtt'),
    ('a SMART-elemekhez', True, 'helyes névelő SMART-összetétel előtt'),
    ('az SMART-elemekhez', False, 'hibás névelő SMART-összetétel előtt'),
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

    register_fixture = {
        'HUM-SAFE-01': 'release', 'HUM-PRIV-01': 'release', 'HUM-OPS-01': 'release',
        'HUM-A11Y-01': 'release', 'HUM-SOMER-01': 'release', 'HUM-PED-01': 'release',
        'HUM-UJ-01': 'release',
        'HUM-MEDIA-01': 'production', 'HUM-GOV-01': 'governance',
    }
    separation_ok = all(decision_register(decision_id) == register
                        for decision_id, register in register_fixture.items())
    if not separation_ok:
        failures += 1
    print(f'{"ok  " if separation_ok else "HIBA"} release-parser — release/media/governance szétválasztás, ismeretlen előtag = release')

    closure_fixture = (
        '### HUM-GOV-09 — teljes — LEZÁRVA\n'
        '**Lezárva:** 2026-09-28. **Jóváhagyta:** programvezető. '
        '**Bizonyíték:** jegyzőkönyv, 2026-09-28.\n'
        '### HUM-GOV-08 — jóváhagyó nélkül — LEZÁRVA\n'
        '**Lezárva:** 2026-09-28.\n'
        '**Bizonyíték:** CI zöld.\n'
        '### HUM-SOMER-09 — helykitöltő — LEZÁRVA\n'
        '**Lezárva:** 2026-09-28. **Jóváhagyta:** ⟬KITÖLTENDŐ⟭ **Bizonyíték:** —\n'
        '### HUM-SAFE-09 — nyitott, mezők nélkül\n'
        '**Jóváhagyó:** gyermekvédelmi felelős.\n'
        '### HUM-GOV-07 — üres jóváhagyó, a következő mező új sorban — LEZÁRVA\n'
        '**Lezárva:** 2026-09-28.\n**Jóváhagyta:**\n**Bizonyíték:** jegyzőkönyv.\n'
        '### HUM-GOV-06 — üres jóváhagyó egy sorban — LEZÁRVA\n'
        '**Lezárva:** 2026-09-28. **Jóváhagyta:** — **Bizonyíték:** jegyzőkönyv.\n'
    )
    closure_ok = unevidenced_closures(closure_fixture) == [
        'HUM-GOV-08: hiányzó lezárási mező: jóváhagyó',
        'HUM-SOMER-09: hiányzó lezárási mező: jóváhagyó, bizonyíték',
        'HUM-GOV-07: hiányzó lezárási mező: jóváhagyó',
        'HUM-GOV-06: hiányzó lezárási mező: jóváhagyó',
    ]
    if not closure_ok:
        failures += 1
    print(f'{"ok  " if closure_ok else "HIBA"} release-parser — LEZÁRVA csak dátummal, jóváhagyóval és bizonyítékkal')

    zorea_fixture = (
        '<!-- @asset\n'
        '{"id": "X-ILL-01", "notes": "A korábbi Zorea-profil az idősebb Leviatanba olvad.",\n'
        ' "legacy": {"spec": "Zorea-kártya"}}\n'
        '-->\n'
        '<!-- @source {"id": "X-NAR-01"} -->\n'
        'Ezt másképp mondod egy Parparimnál, és mást Zoreánál.\n'
        '<!-- @endsource -->\n'
        'egy idősebb Leviatan-kvucánál\n'
        '<!-- @asset\n'
        '{"id": "X-ILL-02", "spec": "profilkártya Zorea fejléccel"}\n'
        '-->\n'
    )
    zorea_ok = retired_age_group_hits(zorea_fixture) == [6, 9]
    if not zorea_ok:
        failures += 1
    print(f'{"ok  " if zorea_ok else "HIBA"} korosztály-őr — Zorea a látható szövegben, metaadat kivétel')

    fixed_checks = 4  # the HUM status, register, closure and Zorea checks above

    def check(ok: bool, label: str) -> None:
        nonlocal failures, fixed_checks
        fixed_checks += 1
        if not ok:
            failures += 1
        print(f'{"ok  " if ok else "HIBA"} {label}')

    check(unchecked_items('- [ ] nyitott\n- [x] kész\n') == ['nyitott'], 'release-parser — checklist')

    output_fixture = (
        '> `cmid`: **BUILD_OUTPUT**, magyarázó definíció.\n'
        '| LMS-X-01 | BUILD_OUTPUT | M0 | valódi sor |\n'
        '| Moodle | `RUNTIME_OUTPUT` | RUN_DATE | TEST_OWNER |\n'
        '| RT-P0-01 | `IMPLEMENTATION_TEST_REQUIRED` | teszt |\n'
        '| RT-P0-02 | `RUNTIME_VERIFIED` | 2026-11-01 |\n'
        '| BSPEC-01 | `BUILD_SPEC_OPEN` | hiány |\n'
        '| BSPEC-02 | `BUILD_SPEC_RESOLVED` | megoldva |\n'
        '| **J1** | kérdés | felelős | bizonyíték | **HIÁNYZIK** | érint |\n'
        '| **V2** | kérdés | felelős | bizonyíték | **MEGVAN** | érint |\n'
    )
    check(unresolved_output_rows(output_fixture, BUILD_OUTPUT_ROW) == 1
          and unresolved_output_rows(output_fixture, RUNTIME_OUTPUT_ROW) == 1
          and unresolved_output_rows(output_fixture, RUNTIME_TEST_OPEN_ROW) == 1
          and [m.group(1) for line in output_fixture.splitlines()
               if (m := BUILD_SPEC_OPEN_ROW.match(line))] == ['BSPEC-01']
          and missing_rights_subgates(output_fixture) == ['J1'],
          'release-parser — output-, teszt-, build-spec- és alkapu-sorok')

    def inputs(**override) -> dict:
        base = {'module_placeholders': [], 'human_open_release': [], 'human_open_media': [],
                'environment_rows': 0, 'runtime_tests_open': 0, 'build_output_rows': 0,
                'build_spec_open': [], 'checklists': {}, 'open_rules': [], 'rights_missing': [],
                'assets': []}
        base.update(override)
        return base

    def verdicts(state: dict, errors: tuple = ()) -> tuple[str, str]:
        build = build_verdict(list(errors), state['build_spec'])
        return build, learner_verdict(build, state['learner'], state['media_release'])

    check(build_verdict(['E'], []) == BUILD_NOT_READY
          and build_verdict([], ['X']) == BUILD_NOT_READY
          and build_verdict([], []) == BUILD_READY
          and verdicts(assemble_release_state(inputs()), errors=('E',)) == (BUILD_NOT_READY, LEARNER_NO_GO),
          'build-verdikt — ERROR mellett nincs READY_FOR_STAGING_BUILD')
    check(learner_verdict(BUILD_NOT_READY, [], []) == LEARNER_NO_GO
          and learner_verdict(BUILD_READY, ['X'], []) == LEARNER_NO_GO
          and learner_verdict(BUILD_READY, [], ['M']) == LEARNER_MEDIA_PENDING
          and learner_verdict(BUILD_READY, [], []) == LEARNER_PILOT_READY
          and 'READY' not in (BUILD_READY, LEARNER_PILOT_READY),
          'learner-verdikt — build nélkül NO-GO, csupasz READY nincs')

    tag_fixture = (
        '- [ ] a\n- [ ] b <!-- gate: post-build -->\n- [ ] c <!-- gate: lifecycle -->\n'
        '- [ ] d <!-- gate: repo-fixable -->\n- [ ] e <!-- gate: build, signoff -->\n'
        '- [ ] f <!-- gate: bogus -->\n- [ ] g <!-- gate: human-qa, repo-fixable -->\n'
        '- [x] h <!-- gate: build -->\n'
    )
    check(classify_checklist(tag_fixture) == [
        ('a', None, False), ('b', 'post-build', False), ('c', 'lifecycle', False),
        ('d', 'build', True), ('e', None, False), ('f', None, False), ('g', 'human-qa', True)],
          'checklist-jelölés — osztály, repo-fixable, hibás jelölés = besorolatlan')

    unclassified = assemble_release_state(inputs(checklists={'SAFEGUARDING': classify_checklist('- [ ] x\n')}))
    check(verdicts(unclassified) == (BUILD_NOT_READY, LEARNER_NO_GO)
          and any(line.startswith('CHECKLIST-UNCLASSIFIED') for line in unclassified['build_spec']),
          'hamis zöld — besorolatlan checklist-tétel blokkolja a buildet')

    lifecycle = assemble_release_state(inputs(checklists={
        'RELEASE-READINESS': classify_checklist('- [ ] transzfer <!-- gate: lifecycle -->\n')}))
    check(verdicts(lifecycle) == (BUILD_READY, LEARNER_PILOT_READY) and lifecycle['lifecycle'],
          'életciklus — a program-transzfer egyik verdiktet sem blokkolja')

    check(verdicts(assemble_release_state(inputs(environment_rows=0, runtime_tests_open=1)))
          == (BUILD_READY, LEARNER_NO_GO),
          'hamis zöld — kitöltött környezeti rekord, futatlan runtime-teszt: NO-GO')

    r2_photo = {'id': 'X-FOTO-01', 'kind': 'photo', 'status': 'spec-ready', 'production_rules': ['R2']}
    check(verdicts(assemble_release_state(inputs(open_rules=[], rights_missing=['J1'], assets=[r2_photo])))[0]
          == BUILD_NOT_READY
          and verdicts(assemble_release_state(inputs(assets=[r2_photo]))) == (BUILD_READY, LEARNER_PILOT_READY),
          'hamis zöld — az R2-jelölő kivétele nem nyitja a jogi kaput, amíg alkapu HIÁNYZIK')

    media_fixture = [
        {'id': 'a1', 'kind': 'voiceover', 'status': 'pending-rights'},
        {'id': 'a2', 'kind': 'video', 'status': 'pending-rights'},
        {'id': 'a3', 'kind': 'photo', 'status': 'pending-rights'},
        {'id': 'a4', 'kind': 'photo', 'status': 'pending-rights', 'fallback': 'szöveges leírás'},
        {'id': 'a5', 'kind': 'photo', 'status': 'pending-rights', 'fallback': 'x', 'fallback_final': True},
        {'id': 'a6', 'kind': 'diagram', 'status': 'spec-ready'},
        {'id': 'a7', 'kind': 'voiceover', 'status': 'pending-rights', 'release_phase': 'A'},
    ]
    check(media_assessment(media_fixture, False) == (['a3', 'a7'], ['a4'], 6)
          and verdicts(assemble_release_state(inputs(assets=[media_fixture[3]])))
          == (BUILD_READY, LEARNER_MEDIA_PENDING),
          'médiakapu — asset-szinten: A fallback nélkül build-spec, átmeneti fallbackkel MEDIA_PENDING, B/C nem blokkol')

    legacy_fixtures = {
        'MODULE-PLACEHOLDERS': (inputs(module_placeholders=['x.md:1']), 'build_spec'),
        'HUMAN-DECISIONS': (inputs(human_open_release=['HUM-SAFE-09']), 'build_spec'),
        'RUNTIME-ACCEPTANCE': (inputs(environment_rows=1), 'learner'),
        'LMS-BUILD': (inputs(build_output_rows=1), 'learner'),
        'SAFEGUARDING-CHECKLIST': (inputs(checklists={'SAFEGUARDING': classify_checklist('- [ ] x\n')}), 'build_spec'),
        'PROGRAM-TRANSFER': (inputs(checklists={'RELEASE-READINESS': classify_checklist(
            '- [ ] x <!-- gate: lifecycle -->\n')}), 'lifecycle'),
        'PRODUCTION-RULES': (inputs(open_rules=['R3']), 'media_info'),
        'MEDIA-HUMAN-DECISIONS': (inputs(human_open_media=['HUM-MEDIA-09']), 'media_release'),
    }
    legacy_ok = set(legacy_fixtures) <= set(LEGACY_BLOCKER_CATEGORY)
    for fixture, bucket in legacy_fixtures.values():
        state = assemble_release_state(fixture)
        legacy_ok &= [name for name, items in state.items() if items] == [bucket]
    check(legacy_ok, 'migráció — minden régi blokker pontosan egy új kategóriába kerül')

    total = len(SELFTEST_CASES) + len(SELFTEST_Z4) + len(ARTICLE_SELFTEST) + fixed_checks
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
    check_closed_decisions(errors)

    print(f'Objective integrity errors: {len(errors)}')
    for item in errors:
        print(f'ERROR: {item}')

    learner = None
    if args.strict_release or args.release_report:
        state = assemble_release_state(collect_release_inputs())
        build = build_verdict(errors, state['build_spec'])
        learner = learner_verdict(build, state['learner'], state['media_release'])
        build_lines = ([f'ERROR {len(errors)} objective integrity errors (G7)'] if errors else []) \
            + state['build_spec']
        print(f'Build-spec blockers: {len(build_lines)}')
        for item in build_lines:
            print(f'BUILD-SPEC: {item}')
        print(f'MOODLE-BUILD-VERDICT: {build}')
        print(f'Learner-release blockers: {len(state["learner"])}')
        for item in state['learner']:
            print(item)
        for item in state['media_release']:
            print(f'MEDIA-RELEASE: {item}')
        for item in state['media_info']:
            print(f'MEDIA-INFO: {item}')
        for item in state['lifecycle']:
            print(f'LIFECYCLE: {item}')
        if args.release_report:
            governance = governance_items()
            if governance:
                print(f'Governance-only items (not a release gate): {len(governance)}')
                for item in governance:
                    print(f'GOVERNANCE: {item}')
        print(f'LEARNER-RELEASE-VERDICT: {learner}')
        # Compatibility alias for one release cycle (RM-D3): same value as above.
        print(f'RELEASE-VERDICT: {learner}')

    if errors:
        return 1
    if args.strict_release and learner != LEARNER_PILOT_READY:
        return 2
    print('Objective content integrity checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
