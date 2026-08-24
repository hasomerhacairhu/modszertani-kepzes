#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / '02 Tervezet/Modulok'


def get(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def put(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text.rstrip() + '\n', encoding='utf-8')


def edit(rel: str, fn) -> None:
    text = get(rel)
    new = fn(text)
    put(rel, new)


def exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f'{label}: expected source text missing')
    return text.replace(old, new)


# ---------------------------------------------------------------------------
# M0: remove learner-facing unresolved operational placeholders without
# inventing retention periods, contacts or psychometric thresholds.
# ---------------------------------------------------------------------------
M0 = '02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md'
def fix_m0(text: str) -> str:
    return text.replace(
        'Pontos küszöb-finomítás az első kohorsz adatai után: ⟬KITÖLTENDŐ: első futás item-statisztikái alapján⟭.',
        'A jelzőszintet az első kohorsz item-statisztikái után dokumentált stáb-review-ban kell újrakalibrálni; addig ez támogatási jelzés, nem pszichometriai cut-score.'
    )
edit(M0, fix_m0)

M01 = '02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md'
def fix_m01(text: str) -> str:
    text = re.sub(
        r'> – \*\*Meddig marad meg\?\*\* A reflexiód a ⟬KITÖLTENDŐ: képzés/félév vége \+ megőrzési idő⟭-ig marad meg, utána ⟬KITÖLTENDŐ: töröljük / anonimizáljuk⟭\.',
        '> – **Meddig marad meg?** A pontos megőrzési és törlési időt a kurzushoz közzétett **adatkezelési tájékoztató** rögzíti; ennek ennél a feladatnál közvetlenül elérhetőnek kell lennie. A kurzus nem ígérhet konkrét időt addig, amíg ezt a privacy/DPO review jóvá nem hagyta.',
        text,
    )
    text = re.sub(
        r'> – \*\*Kihez fordulhatsz\?\*\* Ha kérdésed van arról, mi történik az adataiddal, vagy szeretnéd, hogy töröljük, írj ⟬KITÖLTENDŐ: mentor / adatkezelési felelős – kapcsolat⟭-nak\.',
        '> – **Kihez fordulhatsz?** Adatkezelési kérdéssel vagy érintetti kéréssel a Moodle-kurzus adatkezelési tájékoztatójában **névvel és elérhetőséggel megadott kapcsolattartóhoz** fordulhatsz. Ha ez a kontakt nincs kint, a feladat nem nyitható meg tanulóknak.',
        text,
    )
    return text
edit(M01, fix_m01)

M02 = '02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrich, nem terapeuta – szerepek és elvárások.md'
def fix_m02(text: str) -> str:
    return re.sub(
        r' ⟬KITÖLTENDŐ: kihez fordulhat a madrich személyesen, ha a leckében leírtak rosszul érintik – megnevezett gyermekvédelmi felelős / mentor \+ elérhetőség⟭',
        ' Ha ez rosszul érint, állj meg, és keresd a Moodle-kurzus fejlécében és a helyi gyermekvédelmi protokollban **névvel és elérhetőséggel megadott kijelölt gyermekvédelmi felelőst vagy mentorodat**. Ha ilyen kontakt nincs láthatóan megadva, a kurzus nem élesíthető.',
        text,
    )
edit(M02, fix_m02)


# ---------------------------------------------------------------------------
# M2.3: replace open ideology placeholder with the movement's own published
# Hungarian handbook wording; remove production-estimate debris.
# ---------------------------------------------------------------------------
M23 = '02 Tervezet/Modulok/M2/Online leckék/M2.3 – Somer 3 pillére – mini-kapszula.md'
def fix_m23(text: str) -> str:
    text = re.sub(
        r'> \*\*Gyártási embernap:\*\* ⟬KITÖLTENDŐ: Branching-gyártás becsült embernap .*?⟭\.\n',
        '> **Gyártási becslés:** az implementáló csapat backlogjában, a végleges ágak és a cél H5P-verzió rögzítése után becsülendő; ez nem tanulói tartalom.\n',
        text,
    )
    old = ('> **A Somer szerint minden népnek joga van az önrendelkezéshez – Izrael a zsidó önrendelkezés kifejeződése.** Ezt mi **pluralizmussal és a mindenkire kiterjedő társadalmi igazságossággal** együtt képzeljük el, nem azok ellenében. **A someres béke-örökség szerint ehhez hozzátartozik a zsidó és a palesztin nép kölcsönös önrendelkezésének és békés együttélésének keresése is.** ⟬KITÖLTENDŐ: a palesztin-/béke-dimenzió pontos mozgalmi megfogalmazását a helyi Somer/ken erősítse meg.⟭')
    new = ('> **A Hasomer Hacair Magyarország Ideológiai Kézikönyve szerint minden népnek joga van az önmeghatározáshoz, Izrael pedig a zsidó önmeghatározást fejezi ki.** A kézikönyv a többelvű, demokratikus és világi állam, a társadalmi egyenlőség, valamint a diaszpóra és Izrael közti párbeszéd és kritika fontosságát is hangsúlyozza; oktatási gyakorlatként pedig kifejezetten **többelvű és kritikus szempontokat** kér. A Hasomer Hacair Magyarország jelenlegi stratégiája értékként nevezi meg a **békés együttélés** iránti vágyat.\n>\n> **Forrás a build/lektor számára:** Hasomer Hacair Magyarország, *Ideológiai Kézikönyv*, „3. Cionizmus” (2023), valamint a szervezet nyilvános *Stratégia* oldala. A tanulói anyag nem tesz ennél részletesebb aktuálpolitikai állítást helyi szakmai döntés nélkül.')
    if old not in text:
        raise RuntimeError('M2.3 ideology placeholder block changed unexpectedly')
    return text.replace(old, new)
edit(M23, fix_m23)


# ---------------------------------------------------------------------------
# M4.1: never ship an empty support token to learners.
# ---------------------------------------------------------------------------
M41 = '02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md'
def fix_m41(text: str) -> str:
    return re.sub(
        r'írj ⟬KITÖLTENDŐ: technikai support kontakt – megnevezett csatorna/felelős⟭;',
        'használd a Moodle-kurzus fejlécében **konkrétan megadott technikai support csatornát**;',
        text,
    )
edit(M41, fix_m41)


# ---------------------------------------------------------------------------
# M5.3: H5P Repetition is Leitner-inspired adaptive repetition inside the
# activity. It does not itself prove persistent multi-day spacing.
# ---------------------------------------------------------------------------
M53 = '02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, visszahívás, spacing.md'
def fix_m53(text: str) -> str:
    text = text.replace('H5P **Dialog Cards** (Leitner / `Repetition` mód – 6–7 kártyás gyakorló-pakli; lásd 3.5)',
                        'H5P **Dialog Cards** (`Repetition` mód – 6–7 kártyás, azonos ülésen ismételt előhívási gyakorló-pakli; lásd 3.5)')
    text = text.replace('**Dialog Cards (Leitner-pakli)**', '**Dialog Cards (Repetition-pakli)**')
    text = text.replace('## 3.5 H5P Dialog Cards – „Leitner-pakli” (élő spacing & visszahívás)',
                        '## 3.5 H5P Dialog Cards – „Repetition-pakli” (ismételt visszahívás ugyanabban az aktivitásban)')
    old = ('> Mert ez a lecke **maga a visszahívásról és a spacingről szól** – akkor hiteles, ha **modellezi is** azt, amiről beszél.\n'
           '> A Dialog Cards Leitner-módban **élő spaced retrieval**: a kártya **elejét** látod (kérdés/inger), **fejből** megpróbálod a választ, **csak utána fordítod meg** (önellenőrzés), és amit nem tudtál, az **újra előkerül**. Pontosan a gyakorlás + visszahívás + spacing hármas, működés közben.')
    new = ('> Mert ez a lecke a **visszahívásról és az elosztott gyakorlásról** szól, de a kettőt nem szabad összemosni. A H5P Dialog Cards `Repetition` módja **Leitner-ihlette, adaptív ismétlést** ad az aktivitáson belül: a kevésbé biztos kártyák gyakrabban kerülnek elő, miközben a tanuló előbb fejből válaszol, majd önellenőriz. Ez jó **retrieval practice / ismételt előhívás**, de **önmagában nem bizonyít többnapos, tartós állapotú spaced-repetition rendszert**.\n'
           '> A valódi időbeli spacinget ebben a leckében a **külön, késleltetett Moodle-visszahívó pont** adja egy későbbi időpontban; ennek időzítését és működését a célrendszeren tesztelni kell.')
    if old not in text:
        raise RuntimeError('M5.3 repetition rationale changed unexpectedly')
    text = text.replace(old, new)
    text = re.sub(
        r'\* \*\*Mód:\*\* `Repetition` \(ismétlő / „Leitner”\) – ne `Normal`\. Így a megfordítás után a chanich jelzi, hogy \*„tudtam” / „még gyakorolnám”\*, és amit nem tudott, az \*\*visszakerül a pakliba\*\* \(több külön találkozás ugyanazzal = spacing\)\.',
        '* **Mód:** `Repetition` – ne `Normal`. A tanuló önjelzi, hogy tudta-e a kártyát; a kevésbé biztos kártyák az aktivitás további köreiben gyakrabban térnek vissza. **Ezt itt ismételt előhívásnak nevezzük, nem többnapos spacingnek.**',
        text,
    )
    text = re.sub(
        r'\* ⟬KITÖLTENDŐ: a ken/kurzus által használt pontos időzítő-eszköz és a beállított késleltetés .*?⟭',
        '* **Runtime-követelmény:** a tényleges időzítő-eszközt és késleltetést az `LMS – activity manifest.md` és az `LMS – H5P runtime acceptance.md` rögzíti. A tanulónak csak olyan emlékeztetőt ígérünk, amely a cél Moodle-környezetben tesztelve működik.',
        text,
    )
    text = text.replace('* **⟬KITÖLTENDŐ⟭ az +1 napos előhívóhoz:** a tényleges Moodle-időzítő (eszköz + késleltetés) beállítása éles indítás előtt.',
                        '* **Késleltetett előhívó acceptance:** a tényleges Moodle-időzítő, késleltetés, értesítés és completion működését éles indítás előtt tesztelni és az LMS-manifestben rögzíteni kell.')
    text = text.replace('**Önreferenciális modalitás (3.5–3.6):** a Dialog Cards **Leitner-módban** (`Repetition`) élő spaced retrieval, az „1 nap múlva visszatérő” előhívó pont pedig egy adag valódi spacing – a lecke **csinálja** is, amiről beszél.',
                        '**Önreferenciális modalitás (3.5–3.6):** a Dialog Cards `Repetition` módja azonos aktivitáson belüli **ismételt előhívást** modellez; a későbbi, külön Moodle-előhívó pont adja az időben elosztott gyakorlást. A lecke így a két mechanizmust külön és pontosan modellezi.')
    return text
edit(M53, fix_m53)


# ---------------------------------------------------------------------------
# M6.1: align shorthand age examples with M3.2's science-aware heuristic.
# ---------------------------------------------------------------------------
M61 = '02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md'
def fix_m61(text: str) -> str:
    text = re.sub(r'írj ⟬KITÖLTENDŐ: technikai support / megnevezett felelős – kapcsolat⟭ címre',
                  'használd a Moodle-kurzus fejlécében **konkrétan megadott technikai support csatornát**', text)
    text = re.sub(r'írj a \*\*mentorodnak\*\* ⟬KITÖLTENDŐ: mentor-kapcsolat⟭',
                  'írj a **Moodle-ban névvel megadott mentorodnak**', text)
    old_list = '''  * **6–10 évesek** – fiatalabb gyerekek, sok mozgás, konkrét szabályok.
  * **11–13 évesek** – tweensek, egyszerre gyerekes és kamaszos, fontos a státusz és a „ki a menő”.
  * **14–16 évesek** – tinik, identitás-keresés, barátságok/drámák, intenzív érzelmek.
  * **16+** – *bogrim* (a legidősebb, „felnőttebb” korosztály), vélemények, viták, több reflexió, nagyobb felelősség.'''
    new_list = '''  * **6–10 évesek** – gyakori jó kiindulópont a rövid, világos instrukció, mozgás és konkrét példa; az egyéni figyelem és igény ettől eltérhet.
  * **11–13 évesek** – a kortárs- és státuszdinamika sok csoportban erősödhet; a konkrét kvuca viselkedéséből indulj ki, ne életkori címkéből.
  * **14–16 évesek** – identitás, barátság és tartozás sokaknál hangsúlyos lehet; az „érzelmileg hullámzó/drámás” nem korosztály-diagnózis.
  * **16+** – több vita, önálló döntés és reflexió sok csoportban jól működhet; a magasabb életkor nem jelent automatikus érettséget vagy nagyobb terhelhetőséget.'''
    if old_list not in text:
        raise RuntimeError('M6.1 age list changed unexpectedly')
    text = text.replace(old_list, new_list)
    text = text.replace('**„Négysoros korosztály-táblázat: 6–10 (sok mozgás, konkrét szabályok); 11–13 (státusz, »ki a menő«); 14–16 (identitás, intenzív érzelmek); 16+ / bogrim (vélemények, viták, reflexió, felelősség).”**',
                        '**„Négysoros korosztály-táblázat tervezési kiindulópontokkal: 6–10 (rövid instrukció, mozgás, konkrét példa); 11–13 (kortárs- és státuszdinamika megfigyelése); 14–16 (identitás, tartozás, barátság lehetséges fókusza); 16+ / bogrim (vita és reflexió gyakran működhet). Minden sor mellett: »heurisztika, a konkrét kvucához igazítsd«.”**')
    old_narr = '''> **6–10 évesek**:
> sok mozgás, rövid instrukciók,
> konkrét, egyszerű szabályok, kevés elvont beszélgetés.
>
> **11–13 évesek**:
> egyszerre gyerekesek és kamaszosak,
> fontos nekik a státusz és a ‘ki a menő’;
> gyorsan lelkesednek, de gyorsan megsértődnek is.
>
> **14–16 évesek**:
> fontosabb, ‘ki vagyok én’, a barátságok és az identitás;
> intenzív, hullámzó érzelmek, és csúcson a kortárs-hatás.
>
> **16+ kvucák**:
> erősebbek a vélemények és a viták,
> több a reflexió és a felelősség,
> itt már több mély beszélgetés is belefér.'''
    new_narr = '''> **6–10 éveseknél** gyakran jó kiindulópont a rövid, világos instrukció, a mozgás és a konkrét példa – de figyeld, hogy a te kvucádnak mi működik.
>
> **11–13 éveseknél** a kortársak és a státusz kérdése sok csoportban fontosabbá válhat. Ez nem szabály: nézd meg a tényleges dinamikát.
>
> **14–16 éveseknél** identitás, barátság és valahová tartozás sokaknál hangsúlyos téma lehet. Ne indulj abból, hogy a koruk miatt „drámásak” vagy érzelmileg kiszámíthatatlanok.
>
> **16+ kvucáknál** gyakran több tér adható vitának, önálló döntésnek és reflexiónak, de a magasabb életkor nem jelent automatikus érettséget vagy nagyobb terhelhetőséget.'''
    if old_narr not in text:
        raise RuntimeError('M6.1 age narration changed unexpectedly')
    return text.replace(old_narr, new_narr)
edit(M61, fix_m61)


# ---------------------------------------------------------------------------
# M6.3: centralize image rights in the media registry and avoid falsely
# claiming that GDPR universally requires written parental consent.
# ---------------------------------------------------------------------------
M63 = '02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md'
def fix_m63(text: str) -> str:
    pattern = re.compile(r'> 📷 \*\*Fotó / kép forrás- és licenc-követelmény.*?(?=\n\n\*\*\*)', re.S)
    repl = '''> 📷 **Fotó / kép forrás-, jog- és adatvédelmi követelmény (buildhez):**
> A lecke minden ténylegesen használt képéhez a **Média-asset regiszterben** kötelező rögzíteni a forrást/fotóst, a felhasználási jogcímet/licencet, a szükséges attribúciót és a jóváhagyási státuszt. **Nem kerülhet éles buildbe olyan kép, amelynek ezek a mezői nincsenek lezárva.**
>
> ⚠️ **Felismerhető kiskorú képmása:** csak akkor használható, ha a szervezet adatvédelmi/jogi review-ja az adott felhasználásra érvényes jogalapot és dokumentációt igazolt, beleértve a szülő/gondviselő hozzájárulását **ott, ahol ez az alkalmazandó jogalap vagy szervezeti policy**. A GDPR-ból nem vezetünk le univerzális „minden gyerekfotóhoz mindig írásos szülői hozzájárulás” szabályt. Ha a jogalap vagy dokumentáció nem egyértelmű, **ne használj felismerhető gyerekfotót**; válassz semleges illusztrációt, tárgyfotót vagy rajzot.'''
    new, n = pattern.subn(repl, text, count=1)
    if n != 1:
        raise RuntimeError('M6.3 image-rights block changed unexpectedly')
    return new
edit(M63, fix_m63)


# ---------------------------------------------------------------------------
# Z.3: placeholders are learner inputs or release-configured contacts, not
# authoring TODOs.
# ---------------------------------------------------------------------------
Z3 = '02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md'
def fix_z3(text: str) -> str:
    text = text.replace('> – **MELYIK KVUCÁVAL**? (pl. ⟬KITÖLTENDŐ: a saját kvucád neve / korosztály – pl. Kivsza, Leviatan⟭)',
                        '> – **MELYIK KVUCÁVAL?** Írd be a saját kvucád **konkrét nevét és korosztályát**. Ha még nincs saját kvucád, írd be azt a csoportot, amelyikkel a terepgyakorlatot várhatóan végzed.')
    text = text.replace('> **„Elmondom a Peula v2-tervemet ⟬KITÖLTENDŐ: kinek⟭-nek, és ha elakadok / közbejön az akadály, akkor tőle kérek segítséget.”**',
                        '> **„Elmondom a Peula v2-tervemet annak a konkrét mentoromnak vagy kijelölt tapasztalt madrichnak, akit név szerint ide beírok, és ha elakadok / közbejön az akadály, tőle kérek segítséget.”**')
    text = re.sub(
        r'> \*\*„Az első éles Zmán Kvucám előtt megerősítem, ki a kened gyermekvédelmi felelőse \(⟬KITÖLTENDŐ: név / elérhetőség – vagy: kit kérdezek meg róla⟭\), és jelzés esetén neki / a ken-vezetőnek jelzek\.”\*\*',
        '> **„Az első éles Zmán Kvucám előtt a Moodle-kurzusban és a helyi protokollban ellenőrzöm a kijelölt gyermekvédelmi felelős és helyettes **nevét + elérhetőségét**, és felírom magamnak. Ha ez nincs egyértelműen megadva, nem vezetek önállóan éles foglalkozást, hanem jelzem a képzőnek.”**',
        text,
    )
    return text
edit(Z3, fix_z3)


# ---------------------------------------------------------------------------
# M7 version semantics and scheduling. v1 = first full draft; v2 = revised
# mastery product after the live workshop. No arbitrary scientific "X day".
# ---------------------------------------------------------------------------
for path in (MOD / 'M7').rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    text = text.replace('Peula v2 – első vázlat', 'Peula v1 – első vázlat')
    text = text.replace('Peula v2 első vázlat', 'Peula v1 első vázlat')
    text = re.sub(r'⟬KITÖLTENDŐ: v1(?: first-draft)?[- ]leadás(?: határideje)?⟭', 'a Moodle-ben előre beállított és kommunikált v1-határidő', text, flags=re.I)
    text = re.sub(r'⟬KITÖLTENDŐ: v2 mastery[- ]leadás(?: határideje)?⟭', 'a Moodle-ben előre beállított és kommunikált v2-határidő', text, flags=re.I)
    text = re.sub(r'⟬KITÖLTENDŐ: v2 mastery-leadás⟭', 'a Moodle-ben előre beállított és kommunikált v2-határidő', text, flags=re.I)
    text = re.sub(r'⟬KITÖLTENDŐ: spacing-minimum napban, javasolt ≥ X nap⟭', 'az M7.B köztes feedback- és revíziós szakasza', text)
    # Child-protection contact placeholder inside the gate feedback.
    text = re.sub(r'⟬KITÖLTENDŐ: a ken nevesített gyermekvédelmi felelőse és a helyi jelzési protokoll⟭',
                  'a Moodle-kurzusban névvel megadott kijelölt gyermekvédelmi felelős és a jóváhagyott helyi jelzési protokoll', text)
    text = text.replace('⟬KITÖLTENDŐ⟭ dátumok', 'konkrét Moodle-dátumok')
    path.write_text(text.rstrip() + '\n', encoding='utf-8')

M7K = '02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md'
def fix_m7k(text: str) -> str:
    pattern = re.compile(r'\* 🔒 \*\*Spacing-invariáns.*?\n', re.S)
    match = pattern.search(text)
    if not match:
        raise RuntimeError('M7 spacing invariant missing')
    replacement = ('* 🔒 **Spacing- és feedback-invariáns:** a v1 és v2 **nem lehet ugyanazon a napon**. A v1 leadása után következik az M7.B köztes workshop/feedback, majd külön revíziós munka, és csak ezután adható le v2. A program alapritmusában ez nagyjából egyhetes köz, de **nem állítunk tudományosan indokolatlan univerzális minimum-napszámot**; azt védjük, hogy valódi időbeli elosztás + feedback → revízió történjen. A konkrét Moodle-dátumokat ehhez igazítva kell beállítani.\n')
    return text[:match.start()] + replacement + text[match.end():]
edit(M7K, fix_m7k)

# Rename two canonical files whose names still contradicted their corrected content.
renames = [
    (
        MOD / 'M7/Online leckék/M7.4 – Peula v2 + AI – modulproduktum váz.md',
        MOD / 'M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md',
    ),
    (
        MOD / 'M3/Peulák/M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md',
        MOD / 'M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md',
    ),
]
for old, new in renames:
    if old.exists():
        old.rename(new)
    elif not new.exists():
        raise RuntimeError(f'Neither old nor new canonical exists: {old}')

# Update literal and common %-encoded references throughout text/code/registry files.
name_pairs = [
    ('M7.4 – Peula v2 + AI – modulproduktum váz.md', 'M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md'),
    ('M7.4%20–%20Peula%20v2%20+%20AI%20–%20modulproduktum%20váz.md', 'M7.4%20–%20Peula%20v1%20+%20AI%20–%20első%20modulproduktum-vázlat.md'),
    ('M3.B – Red flag vagy nem – Miniszínház & lépés-térkép.md', 'M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md'),
    ('M3.B%20–%20Red%20flag%20vagy%20nem%20–%20Miniszínház%20&%20lépés-térkép.md', 'M3.B%20–%20Red%20flag%20vagy%20nem%20–%20Esetelemzés%20&%20lépés-térkép.md'),
]
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or path.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.webp','.pdf','.zip','.woff','.woff2'}:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    new = text
    for old, replacement in name_pairs:
        new = new.replace(old, replacement)
    if new != text:
        path.write_text(new, encoding='utf-8')


# ---------------------------------------------------------------------------
# Remaining module placeholders: only replace classes whose value is correctly
# supplied at release/runtime. Unknown TODOs fail the pass instead of guessing.
# ---------------------------------------------------------------------------
def placeholder_value(raw: str, path: Path) -> str:
    low = raw.lower()
    if 'országos mozgalmi' in low and ('gyermekvéd' in low or 'gyerekvéd' in low):
        return 'a `Gyermekvédelem – release gate.md` szerint jóváhagyott alternatív/országos eszkalációs kontakt'
    if ('gyermekvédelmi felelős neve' in low or 'gyerekvédelmi felelős neve' in low):
        return 'a `Gyermekvédelem – release gate.md`-ben jóváhagyott, névvel megadott kijelölt gyermekvédelmi felelős'
    if 'mentálhigiénés szakértő' in low:
        return 'a release-review-ban rögzített traumaérzékenységi szakértő, ha a gyermekvédelmi felelős ezt szükségesnek ítéli'
    if 'jóváhagyás dátuma' in low:
        return 'a release evidence-ben rögzített jóváhagyási dátum'
    if 'következő felülvizsgálat' in low:
        return 'a release evidence-ben rögzített következő felülvizsgálati dátum'
    if 'hivatalos alkohol' in low or ('alkohol' in low and 'code of conduct' in low):
        return 'a szervezet élesítéskor hatályos, írásban elérhető és jóváhagyott alkohol- és dohányzási szabályzata; ennek hiányában ez a tartalmi rész nem élesíthető'
    if 'technikai support' in low:
        return 'a Moodle-kurzus fejlécében névvel/csatornával megadott technikai support'
    if 'mentor-kapcsolat' in low:
        return 'a Moodle-kurzusban névvel megadott mentor'
    if 'v1' in low and 'leadás' in low:
        return 'a Moodle-ben előre beállított és kommunikált v1-határidő'
    if 'v2' in low and 'leadás' in low:
        return 'a Moodle-ben előre beállított és kommunikált v2-határidő'
    if raw.replace(' ', '') in {'⟬KITÖLTENDŐ⟭', '⟬**KITÖLTENDŐ**⟭'}:
        return 'release előtt konkrétan rögzítendő'
    raise RuntimeError(f'Unknown module placeholder in {path.relative_to(ROOT)}: {raw}')

placeholder_re = re.compile(r'⟬[^⟭]*KITÖLTENDŐ[^⟭]*⟭', re.I)
for path in MOD.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    new = placeholder_re.sub(lambda m: placeholder_value(m.group(0), path), text)
    path.write_text(new.rstrip() + '\n', encoding='utf-8')

remaining = []
for path in MOD.rglob('*.md'):
    for no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if 'KITÖLTENDŐ' in line:
            remaining.append(f'{path.relative_to(ROOT)}:{no}: {line.strip()}')
if remaining:
    raise SystemExit('Unresolved module placeholders:\n' + '\n'.join(remaining))

print('Module cleanup completed: 0 KITÖLTENDŐ tokens remain under 02 Tervezet/Modulok.')
