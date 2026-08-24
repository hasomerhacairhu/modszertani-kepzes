#!/usr/bin/env python3
"""Static integrity checks for the training repository.

This intentionally separates objective repository errors from release blockers.
Normal CI fails on broken local links, resurrected duplicate canonicals and known
unsafe regressions. Organisation-specific KITÖLTENDŐ fields are reported as
release blockers, but are not guessed or auto-filled.
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

LEGACY_PATHS = [
    '02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-től a használható visszajelzésig (45’).md',
    '02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyerekvédelem.md',
    '02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyerekvédelem 101 – red flag felismerése & első lépések.md',
    '02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyerekvédelem (Study Lab).md',
]

FORBIDDEN_ACTIVE = {
    'te leszel az a felnőtt': '15+ célcsoportban a madrich maga is lehet kiskorú',
    'érzelmi „gáz” (amygdala)': 'túlzottan leegyszerűsítő fejlődéslélektani metafora',
    '2–3 perces minijelenetet': 'súlyos safeguarding-helyzetek kötelező eljátszása visszatérne',
}

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


def markdown_files():
    for path in ROOT.rglob('*.md'):
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


def check_structure(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f'MISSING-REQUIRED {rel}')
    for rel in LEGACY_PATHS:
        if (ROOT / rel).exists():
            errors.append(f'LEGACY-DUPLICATE {rel}')


def check_regressions(errors: list[str]) -> None:
    for path in MODULE_ROOT.rglob('*.md'):
        text = path.read_text(encoding='utf-8', errors='replace').lower()
        for phrase, why in FORBIDDEN_ACTIVE.items():
            if phrase.lower() in text:
                errors.append(f'REGRESSION {path.relative_to(ROOT)}: {phrase!r} ({why})')
    z4 = MODULE_ROOT / 'Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md'
    if z4.exists():
        text = z4.read_text(encoding='utf-8', errors='replace')
        if 'Documentation Tool' in text and ('mentve marad' in text or 'később folytathatod' in text):
            errors.append('REGRESSION Z.4 unsupported H5P Documentation Tool resume promise')


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-release', action='store_true', help='also fail when release blockers remain')
    parser.add_argument('--release-report', action='store_true', help='print release blockers but do not fail for them')
    args = parser.parse_args()

    errors: list[str] = []
    check_structure(errors)
    check_links(errors)
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
