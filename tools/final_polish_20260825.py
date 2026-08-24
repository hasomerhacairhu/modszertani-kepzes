#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / '02 Tervezet/Modulok'

# M7 hub: fix Anna-era duplicate numbering and clean policy wording.
p = MOD / 'M7/M7 – Peula a papírtól a valóságig – Programírás, Zmán Kvucá & AI-támogatott tervezés.md'
s = p.read_text(encoding='utf-8')
s = s.replace('ahol az AI (szervezetileg jóváhagyott generatív AI-eszköz) csak **segít**, nem helyettesít?',
              'ahol a **szervezetileg jóváhagyott generatív AI-eszköz** csak segít, nem helyettesít?')
s = s.replace('etikusan vonja be az **AI-t (szervezetileg jóváhagyott generatív AI-eszköz)** a tervezésbe',
              'etikusan von be **szervezetileg jóváhagyott generatív AI-eszközt** a tervezésbe')
s = s.replace('\n1. **AI-etikusság & adatbiztonság**', '\n4. **AI-etikusság & adatbiztonság**')
p.write_text(s.rstrip() + '\n', encoding='utf-8')

# M4.A: repair list numbering regression left by manual audit edits.
p = MOD / 'M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md'
s = p.read_text(encoding='utf-8')
s = s.replace('\n1. **Szobor-alkotás + bemutatás (5–7 perc)**', '\n3. **Szobor-alkotás + bemutatás (5–7 perc)**')
p.write_text(s.rstrip() + '\n', encoding='utf-8')

# Study Labs: remove residual public-status-board implementation language.
for p in MOD.rglob('*.md'):
    if '/Peulák/' not in p.as_posix() or '.F ' not in p.name:
        continue
    s = p.read_text(encoding='utf-8')
    s = s.replace('vizuális állapotfelmérés', 'privát állapotfelmérés')
    s = s.replace('amit az előbb bejelölt a táblán', 'amit a privát self-checkben kiválasztott')
    s = s.replace('amit az előbb bejelölt', 'amit a privát self-checkben kiválasztott')
    s = re.sub(
        r'^\* 1 tábla / flipchart, rajta .*?:\n(?:  \* .*\n)+',
        '* 1 tábla / flipchart az **anonim témakérésekhez** és a közös fogalom-térképhez; név szerinti completion/státusz nem kerül rá.\n',
        s,
        flags=re.M,
    )
    s = re.sub(
        r'^\* 1 \*\*tábla / flipchart\*\*, rajta .*?:\n(?:  \* .*\n)+',
        '* 1 **tábla / flipchart** az anonim témakérésekhez és a közös fogalom-térképhez; név szerinti completion/státusz nem kerül rá.\n',
        s,
        flags=re.M,
    )
    # Any leftover "Kész az Mx" board row is a public-status artefact, not needed.
    s = re.sub(r'^\s*\* extra sor: `„?Kész az M\d.*?`\s*\n', '', s, flags=re.M)
    s = re.sub(r'^\s*\* `„?Kész az M\d.*?`\s*\n', '', s, flags=re.M)
    # Repair common prep numbering after deleted board/sticker step.
    lines = s.splitlines()
    in_prep = False
    prep_counter = 0
    out = []
    for line in lines:
        if line.startswith('### 2.3.') and ('Előkészítés' in line or 'Képző' in line):
            in_prep = True
            prep_counter = 0
            out.append(line)
            continue
        if in_prep and line.startswith('***'):
            in_prep = False
        if in_prep:
            m = re.match(r'^(\d+)\. (.+)$', line)
            if m:
                prep_counter += 1
                line = f'{prep_counter}. {m.group(2)}'
        out.append(line)
    s = '\n'.join(out)
    p.write_text(s.rstrip() + '\n', encoding='utf-8')

# Assertions.
errors = []
m7 = (MOD / 'M7/M7 – Peula a papírtól a valóságig – Programírás, Zmán Kvucá & AI-támogatott tervezés.md').read_text(encoding='utf-8')
for n, label in [(1,'SMART nevelési cél'), (2,'„Peula 11 pontja”'), (3,'Zmán Kvucá & operáció'), (4,'AI-etikusság & adatbiztonság'), (5,'Peula v2 + Zmán Kvucá produktum')]:
    if f'{n}. **{label}' not in m7:
        errors.append(f'M7 competency numbering missing {n}: {label}')
if 'AI (szervezetileg jóváhagyott generatív AI-eszköz)' in m7:
    errors.append('M7 awkward parenthetical AI wording remains')

m4a = (MOD / 'M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md').read_text(encoding='utf-8')
if '\n3. **Szobor-alkotás + bemutatás' not in m4a:
    errors.append('M4.A list numbering not repaired')

for p in MOD.rglob('*.md'):
    if '/Peulák/' not in p.as_posix() or '.F ' not in p.name:
        continue
    low = p.read_text(encoding='utf-8').lower()
    for forbidden in ['vizuális állapotfelmérés', 'bejelölt a táblán', 'ragaszd fel a matric', 'ragaszd fel a sticker']:
        if forbidden in low:
            errors.append(f'STUDY-LAB residual {forbidden!r}: {p.relative_to(ROOT)}')

if errors:
    raise SystemExit('\n'.join(errors))
print('Final consistency polish assertions passed.')
