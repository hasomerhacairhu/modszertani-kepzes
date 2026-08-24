#!/usr/bin/env python3
from pathlib import Path

# M3.B: eliminate any residual roleplay presentation block.
path = Path('02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md')
text = path.read_text(encoding='utf-8')
start_marker = '### 4.2.4. Jelenetek bemutatása + megbeszélés (kb. 3–4 perc / csoport)'
end_marker = '**Képző kérdései a nagykörnek:**'
if start_marker in text and end_marker in text:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    replacement = '''### 4.2.4. Esetek visszahozása + megbeszélés (kb. 3–4 perc / csoport)\n\nAlapértelmezés: 3 csoport → kb. 12 perc. Minden csoport röviden bemutatja a saját négy pontját. **Nem jelenetet mutat be**, hanem az elemzését: red flag → első mondat → tiltott reakció → bevonandó felelős.\n\nHa a megbeszélés közben valaki személyes érintettséget tár fel, állítsd meg a szakmai elemzést, ne kérdezd ki, és kövesd a fenti triage- és jelzési keretet.\n\n'''
    text = text[:start] + replacement + text[end:]
text = text.replace('Jelenetek bemutatása', 'Esetek visszahozása')
text = text.replace('minijelenet', 'esetfeldolgozás')
text = text.replace('miniszínház', 'esetelemzés')
path.write_text(text, encoding='utf-8')

# M6.A: eliminate residual chair-race safety text.
path = Path('02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md')
text = path.read_text(encoding='utf-8')
start_marker = '> **Fizikai safety-mondat (a helycseréhez – mondd ki ELŐRE):**'
end_marker = '*(Lehet röviden megbeszélni, mi a „nem oké” állítás'
if start_marker in text and end_marker in text:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    replacement = '''> **Fizikai safety-mondat (mondd ki ELŐRE):**\n\n> „Nem versenyzünk a helyekért. Nyugodt tempóban mozgunk, nézünk magunk elé, nem lökünk és nem húzunk ki széket más alól. Ha a tér szűk vagy valaki nem szeretne helyet változtatni, elég egy kézjel / felállás is.”\n\n'''
    text = text[:start] + replacement + text[end:]
path.write_text(text, encoding='utf-8')

errors = []
def must(rel, phrase):
    if phrase not in Path(rel).read_text(encoding='utf-8'):
        errors.append(f'MISSING {phrase!r} in {rel}')
def must_not(rel, phrase):
    if phrase in Path(rel).read_text(encoding='utf-8'):
        errors.append(f'FORBIDDEN {phrase!r} in {rel}')

must('README.md', 'Release-státusz')
must('02 Tervezet/RELEASE-READINESS.md', 'Állapot: NO-GO')
must_not('02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, feedback – Önismeret & visszajelzés – Johari + SBI.md', 'SBI-vázatot')
must('02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md', 'nem ígérünk teljes titoktartást')
must_not('02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md', 'érzelmi „gáz” (amygdala)')
must('02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md', 'Kötelező feldolgozási mód a jelen release-ben: harmadik személyű esetanalízis')
must_not('02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md', '2–3 perces minijelenetet')
must('02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md', 'Nincs eggyel kevesebb szék, nincs székszerző verseny')
must('02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md', 'legalább 3 különböző teljes ágon')
must('02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md', 'AI Act szerepek pontosan')
must('02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nem csak játék, hanem peula – 11 tervezési pont & AI-támogatás.md', 'Az AI **opcionális segédeszköz**')
must('02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v2 + AI – modulproduktum váz.md', 'Peula v1')
must_not('02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md', 'te leszel az a felnőtt')
must('02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md', 'Moodle Assignment')
must('02 Tervezet/LMS – hozzáférhetőségi sztenderd.md', 'WCAG 2.2 SC 1.2.2')
must('02 Tervezet/Terepgyakorlat – 2. félév.md', '6 valódi, 60–90 perces peulát')
must('.claude/workflows/deep-audit.js', "const MOD = ABS + '/Modulok'")

if errors:
    raise SystemExit('\n'.join(errors))
print('All critical stabilization invariants passed.')
