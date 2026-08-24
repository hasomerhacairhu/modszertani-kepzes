#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / '02 Tervezet/Modulok'


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text.rstrip() + '\n', encoding='utf-8')


def replace_required(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f'{label}: expected source text not found')
    return text.replace(old, new)


def sub_required(text: str, pattern: str, repl: str, label: str, flags: int = 0) -> str:
    new, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected one match, got {n}')
    return new


# ---------------------------------------------------------------------------
# M2.1: the learning objective is identity awareness -> observable madrich
# behaviour. Uploading a photo of the whole identity map is unnecessary and
# can collect family/religion/relationship information. Keep the map private;
# submit only a behaviour-level reflection.
# ---------------------------------------------------------------------------
rel = '02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md'
s = read(rel)
s = s.replace('**Flow:** Hook → Input 1 → Input 2 → Mini-activity → **Rajzos feladat + fotófeltöltés** → Check → Outro',
              '**Flow:** Hook → Input 1 → Input 2 → Mini-activity → **privát rajzos identitástérkép + nem érzékeny viselkedés-reflexió** → Check → Outro')
s = s.replace('**Completion:** H5P Course Presentation végignézve, a rajz fotójának feltöltésével és a rövid szöveges válasszal együtt.',
              '**Completion:** H5P Course Presentation végignézve + a rövid, **viselkedés-szintű** szöveges válasz beadva. A teljes identitástérképet **nem kell és nem szabad a teljesítéshez feltölteni**.')
s = s.replace('> A lecke részeként papíron meg fogod rajzolni a **saját identitás-köreidet**, lefotózod, és **itt, a leckén belül** feltöltöd.',
              '> A lecke részeként papíron meg fogod rajzolni a **saját identitás-köreidet**, de ez a lap **nálad marad**. A Moodle-be csak egy rövid, nem érzékeny, madrich-viselkedésről szóló mondatot adsz be. Ne írj be teljes neveket, konkrét családi történetet vagy olyan identitásrészletet, amit nem akarsz a kurzusban tárolni.')
s = s.replace('### SLIDE 5 – FELADAT: Papíros identitás-térkép + fotófeltöltés',
              '### SLIDE 5 – FELADAT: Privát identitás-térkép + viselkedés-reflexió')
s = s.replace('**Cél:** a lecke részeként megszületik a saját identitás-térkép rajzban, és be is küldi.',
              '**Cél:** a tanuló elkészíti a saját identitás-térképét **magának**, majd abból egy pedagógiailag szükséges, nem érzékeny viselkedés-fókuszt küld be.')
s = s.replace('*(Technikailag: ha a H5P-ből nem tudtok fájlt feltöltetni, akkor ezen a slide-on legyen az instrukció,\nés **közvetlenül utána**, ugyanebben az aktivitásban a Moodle „File upload” kérdésoldala – de a user szempontjából ez a lecke része.)*',
              '*(Privacy-by-design: ehhez a feladathoz **ne legyen File upload**. A teljes identitástérkép pedagógiailag nem szükséges a képzőnek; a rövid viselkedés-reflexió elegendő bizonyíték a mikrocélhoz.)*')
s = s.replace('* Jobb oldalon (vagy alul) **fájlfeltöltő mező** + egy rövid szövegmező (Short answer).',
              '* Jobb oldalon (vagy alul) egy rövid szövegmező (Short answer / Essay). **Nincs fájlfeltöltő mező.**')
s = s.replace('> **Feladat – rajzold meg az identitás-köreidet, fotózd le, töltsd fel!**',
              '> **Feladat – rajzold meg az identitás-köreidet magadnak, majd válassz belőle egy viselkedés-fókuszt!**')
s = s.replace('> 4️⃣ Minden körbe írj **3–5 kulcsszót** (nevek, helyzetek, jellemzők – ami neked fontos). A „zsidóság” körbe is azt írd, **ami a te viszonyodat** fejezi ki – nincs „helyes” tartalom.\n\n> 5️⃣ Ha kész vagy, **fotózd le a rajzot**, és töltsd fel itt a leckén belül.',
              '> 4️⃣ Minden körbe írj **3–5 kulcsszót**. Használhatsz kategóriákat, monogramot vagy általános szót; **nem kell teljes nevet, családi részletet, vallási/egészségügyi vagy más érzékeny információt leírnod**. A „zsidóság” körbe is azt írd, ami a te viszonyodat fejezi ki – nincs „helyes” tartalom.\n\n> 5️⃣ Ha kész vagy, **tartsd meg magadnak a rajzot**. Nem kell lefotózni és nem kerül a Moodle-be. Ha később vissza akarsz térni hozzá, tedd olyan helyre, ahol te rendelkezel vele.')
s = s.replace('* **File upload mező:** „Ide töltsd fel a fotót az identitás-térképedről.”\n* **Short answer / Essay mező:** 2–3 mondatos válasz a fenti kérdésre.',
              '* **Short answer / Essay mező:** 2–3 mondatos válasz a fenti kérdésre. A beadás **ne tartalmazzon chanich-nevet, családi történetet vagy érzékeny identitásadatot**; elég a saját megfigyelhető madrich-viselkedésed és az általános kör megnevezése.')
s = s.replace('*(Fejlesztői megjegyzés: ha a H5P Course Presentation nem enged fájlfeltöltést,\nakkor a dián legyen csak az instrukció, és ugyanitt a lecke alatt egy Moodle „File upload” kérdés –\nde UX-ben úgy jelenjen meg, mintha még mindig a lecke része lenne.)*',
              '*(Fejlesztői megjegyzés: **ne építs File upload kerülőutat**. A rajz privát munkalap; a Moodle csak a rövid viselkedés-reflexiót tárolja.)*')
write(rel, s)


# ---------------------------------------------------------------------------
# M2.4: remove compelled personal disclosure. Keep the competence focused on
# boundaries and safe action in a hypothetical case. Also fix the minor-role
# framing: a 15–17-year-old madrich is not "the trusted adult".
# ---------------------------------------------------------------------------
rel = '02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md'
s = read(rel)
s = s.replace('> A lecke **csendes, napló jellegű** – amit írsz, azt csak a képzőid / mentorod látják.',
              '> A lecke **csendes, reflektív**. **Nem kell érzékeny magánéleti történetet megosztanod a teljesítéshez.** Használhatsz általánosított vagy fiktív példát. A Moodle-be csak azt írd, ami szükséges a határtartás és a biztonságos madrich-reakció bemutatásához; chanich nevét vagy beazonosítható történetét ne add meg.')
s = s.replace('* Lehetsz **megbízható felnőtt**, aki meghallgat, visszajelez,\n  és **szól**, ha valaki veszélyben lehet.',
              '* Lehetsz **megbízható madrich**, aki meghallgat, visszajelez és **szól**, ha valaki veszélyben lehet. Ha te magad 18 év alatti vagy, különösen fontos, hogy **ne maradj egyedül a felelősséggel**, hanem vond be a kijelölt felelős felnőttet / gyermekvédelmi felelőst.')
old = '''> Írj minden oszlopba **legalább 3–3 kulcsszót** olyan témákról,
> amik az életedben jelen vannak (pl. „családi veszekedés”, „tanulási nehézség”, „aktivizmus”, „mentális egészség” stb.).

> Válassz 2-3 kulcsszót (minimum 2 oszlopból) és fejtsd ki pár (4-7) mondatban, hogy miért abba az oszlopba került az adott téma / kulcsszó!

#### Szövegmező alatti megnyugtatás:

> A válaszaidat csak a képzőid / mentorod látják.
> Nem dolgozatot kérünk, hanem őszinte gondolkodást.

> 🔒 *Emlékeztető: ez **nem feltétel nélküli titoktartás**. Ha a leírtakból az derül ki, hogy te vagy más veszélyben van, a mentorodnak jeleznie kell – a te biztonságod érdekében.*

(H5P: Essay típus, minimális karakterszám beállítható.)'''
new = '''> A három oszlopba írj **témakategóriákat**, nem élettörténetet. Használhatsz teljesen fiktív példákat is, például: „hobbi”, „családi téma”, „párkapcsolati téma”, „iskolai nehézség”, „egészség”, „politikai vélemény”.
>
> Ez a háromoszlopos lista **privát munkalap: nem kerül beadásra és nem kell a képzőnek megmutatnod**. A cél az, hogy észrevedd: más a „megosztható”, a „személyes” és a „privát/szakemberrel való” tér.
>
> A Moodle-be csak ezt az egy, **nem személyes** mondatot add be:  
> **„Madrichként akkor osztok meg személyes dolgot, ha …; nem osztom meg, ha …; és felelős felnőttet / szakembert vonok be, ha …”**
>
> Ne írj be valódi chanich-nevet, saját diagnózist, konkrét családi konfliktust, traumát vagy más érzékeny részletet. Ha valamit mégis meg akarsz beszélni a mentoroddal, azt külön, az erre jóváhagyott csatornán kezdeményezd.

(H5P/Moodle: egy rövid Essay/Short Answer a háromrészes **szabálymondathoz**; a privát oszloplista nem tárolódik.)'''
s = replace_required(s, old, new, 'M2.4 private/sensitive diary task')
old = '''> Írj erről **5–8 mondatot** (egy szövegmezőben):

> 1️⃣ Mit érzel **elsőre** egy ilyen üzenettől?

> 2️⃣ Mit írnál vissza **abban a pillanatban**,
> hogy empatikus legyél, **röviden**, de ne ígérj olyat, amit nem tudsz tartani
> (pl. nem vállalod, hogy minden éjjel chaten leszel),
> és hogyan **terelnéd át** a privát éjszakai chatről egy **transzparens, nappali, csoportos / hivatalos** csatornára?

> 3️⃣ **Kit vonnál be?** – mentor, szülő, szervezeti felelős, szakember…'''
new = '''> Ez **fiktív eset**, és a válaszodnak nem kell saját hasonló élményt vagy érzékeny történetet felidéznie. Írj **4–6 mondatos szakmai választ**:
>
> 1️⃣ Mi lenne az **első rövid, empatikus mondatod**?
>
> 2️⃣ Hogyan kerülnéd el az éjszakai privát 1:1 kapcsolat elmélyítését, és hogyan terelnéd a kommunikációt **transzparens, nappali, jóváhagyott csatornára**?
>
> 3️⃣ **Melyik kijelölt felelős szerepet** vonnád be azonnal a helyi protokoll szerint, és mit nem kezdenél el egyedül (pl. nyomozás, diagnózis, titoktartás ígérete)?'''
s = replace_required(s, old, new, 'M2.4 hypothetical crisis task')
s = s.replace('> 4️⃣ Szerinted mitől lenne ebben a helyzetben **személyes példamutatás**,\n> ahogyan reagálsz? (pl. nem maradsz egyedül, jelzel, segítséget kérsz.)',
              '> 4️⃣ Szerinted mitől lenne ebben a helyzetben **személyes példamutatás** a reakciód? (pl. nem maradsz egyedül, jelzel, segítséget kérsz.) **Ne írj be valódi esetet vagy nevet.**')
write(rel, s)


# ---------------------------------------------------------------------------
# Z.2: reflection can be meaningful without compelled intimate disclosure.
# ---------------------------------------------------------------------------
rel = '02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md'
s = read(rel)
s = s.replace('> A lecke **csendes, reflektív** – amit írsz, azt csak a képzőid / mentorod látják.\n> Nem fogalmazásverseny, hanem **őszinte gondolkodás**.',
              '> A lecke **csendes, reflektív**. A beadott válaszokat csak a kurzusban erre jogosult képző/mentor láthatja a jóváhagyott hozzáférési beállítás szerint. **Nem kell intim vagy érzékeny részletet megosztanod.** Használj anonimizált/általánosított helyzetet, ne írj chanich-nevet vagy beazonosítható történetet; ha egy tanulási pillanat túl személyes, válassz másikat.\n> Nem fogalmazásverseny, hanem **a tanulásod felismerése**.')
s = s.replace('> Itt egy **valóságos, őszinte** pillanatra van szükség.',
              '> Itt egy **konkrét tanulási pillanatra** van szükség, de nem személyes kitárulkozásra. Leírhatod anonimizálva, és elég annyi kontextus, amennyi a tanulság megértéséhez kell.')
s = s.replace('> Amit ide leírsz, azt csak a képzőid / mentorod látják.\n> Nem az a cél, hogy „jó madrichnak tűnj”, hanem hogy **tudd, mit tanultál**.',
              '> A beadást csak az arra jogosult képző/mentor láthatja. **Ne adj meg chanich-nevet, egészségügyi/mentális, családi vagy más érzékeny részletet, ha az nem szükséges.** Nem az a cél, hogy „jó madrichnak tűnj”, hanem hogy **tudd, mit tanultál**.')
s = s.replace('> Itt sem kell „szépen” fogalmazni – **az őszinteség többet ér**, mint a szép mondatok.',
              '> Itt sem kell „szépen” fogalmazni. Ha a „mit mond ez rólad?” kérdés túl személyes lenne, válaszolj inkább így: **„Mit tanultál arról, milyen támogatás vagy tanulási forma segít neked, és mit próbálsz ki legközelebb?”** A teljesítéshez nem kell érzékeny önfeltárás.')
write(rel, s)


# ---------------------------------------------------------------------------
# M4: actually teach audibility/projection, in a voice-safe way, and remove
# personal-phone video capture from the core path.
# NIDCD guidance: avoid shouting/noisy-place overtalk, support speech with
# breathing, use amplification when appropriate.
# ---------------------------------------------------------------------------
hub = '02 Tervezet/Modulok/M4/M4 – Hallható és érthető vagyok – Kiállás, kapcsolódás & kérdezéstechnika.md'
s = read(hub)
s = s.replace('2. **Hanghasználat & érthetőség (tudatosítás szintjén)**', '2. **Hanghasználat & érthetőség (gyakorlati alapszinten)**')
s = s.replace('   * **Észreveszi**, hogy a **hangerő, a beszédtempó és a tagolás** hat az érthetőségére (pl. a túl halk, hadaró vagy monoton beszéd nehezíti a követést) – ezt a fő úton elsősorban **felismeri / tudatosítja**, nem külön gyakorolt készségként.\n   * Képes rövid, **érthető mondatokban** összefoglalni, mit szeretne, és vissza is kérdez: „Követtek?”\n     *(Tudatosítás: az M4.A „mini színpadon” a hangerő/tempó a társak megfigyelési szempontjai közt is megjelenhet. A célzott hangkészség-fejlesztés nem önálló tananyag a modulban.)*',
              '   * **Észreveszi és kipróbálja**, hogyan hat a **hallhatóságra a hangerő, a beszédtempó, a tagolás, a levegő és a térhez fordulás**. Nem a kiabálást gyakorolja, hanem azt, hogyan ér el a hangja a terem végéig erőlködés nélkül.\n   * Képes egy 20–30 mp-es belépőt úgy elmondani, hogy a kijelölt távolságból a társ legalább a kulcsmondatot érthetően hallja; ha a tér/zaj ezt nem teszi lehetővé, **környezeti megoldást választ** (közelebb hívja a csoportot, csökkenti a háttérzajt, szükség esetén mikrofont használ), nem „túlharsogja” a teret.\n     *(Főleg: M4.A „Hang-létra” gyakorlat; a blokk nem hangterápia és nem értékeli a hangszínt.)*')
s = s.replace('* **Fő fókusz:** „Hogyan állok be, mozgok, nézek végig egy képzős kvucán, hogy **érezhető legyen a jelenlétem**?” – a nonverbális jelek „testbe vitele” és társak általi megfigyelés-alapú visszajelzés.',
              '* **Fő fókusz:** „Hogyan állok be, mozgok, nézek és **hogyan szólalok meg úgy, hogy hallható és érthető legyek**?” – nonverbális jelenlét + rövid, hangkímélő projekciós „Hang-létra” gyakorlat + megfigyelés-alapú visszajelzés.')
write(hub, s)

rel = '02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md'
s = read(rel)
s = s.replace('4. Megfogalmaz 1 mondatos személyes fókuszt:', '4. **Kipróbál egy hangkímélő „teremhangot”**: nem kiabálva, hanem nyugodt levegővel, tagolással és a csoport felé fordulva elmond egy 20–30 mp-es belépőt, amit a kijelölt távolságból érteni lehet.\n5. Megfogalmaz 1 mondatos személyes fókuszt:')
s = s.replace('* Telefon(ok) videózáshoz (opcionális, csak ha a csoportnak oké).\n', '')
s = s.replace('**30–40’** – Kis csoportos gyakorlás, opcionális mini-videóval (A mond, B figyel, C felveszi / jegyzetel).',
              '**30–40’** – Kis csoportos **Hang-létra**: hallhatóság, tempó, tagolás és térhez igazítás triádokban.')
s = s.replace('> **Terhelés / időkezelés (core vs. rövidíthető):** a percbontás feszes, ~8–12 fős körre méretezve. **Core (el ne hagyd):** a check-in safety-kerete (4.1), a „Mini színpad” beállás-kör (4.3) és a reflexió + zárókör (4.5) – a tanulási mag és a biztonságos zárás ezeken áll. **Rövidíthető, ha csúszol:** a „Kiállás-szobrok” bemutató-rész (4.2) és a triádos mini-videós kör (4.4) hossza – nagy létszámnál a 4.3-nál jelzett mintabeállás-alternatívát használd. **Tervezz ~10–15% puffert**, és ha kell, a rövidíthető részekből vegyél vissza, ne a zárókörből.',
              '> **Terhelés / időkezelés (core vs. rövidíthető):** a percbontás feszes, ~8–12 fős körre méretezve. **Core (el ne hagyd):** a check-in safety-kerete (4.1), a „Mini színpad” beállás-kör (4.3), a 4.4 Hang-létra legalább egy köre és a reflexió + zárókör (4.5). **Rövidíthető, ha csúszol:** a „Kiállás-szobrok” bemutató-rész (4.2), illetve a Hang-létra második köre. **Tervezz ~10–15% puffert**, és ha kell, a rövidíthető részekből vegyél vissza, ne a zárókörből.')
# Align 4.3 with the new competency: peers can report audibility factually.
s = s.replace('A **hangerő és a tempó** nem társas megfigyelési szempont: ezt maga a beálló figyelheti meg magán (ön-tudatosítás), nem mi minősítjük.',
              'A hangról **nem esztétikai minősítést** adunk („szép/rossz hang”), hanem megfigyelhető információt: „innen minden szót hallottam / két szó elveszett”, „a mondat vége felgyorsult”. A hangerő célja az érthetőség, nem a kiabálás.')
# Replace the whole video block with a compact, evidence-informed voice practice.
s = sub_required(
    s,
    r'### 4\.4\. Blokk 4 – Élmény / játék 3: Kis csoportos gyakorlás, mini-videóval \(30–40’\).*?(?=\n\*\*\*\n\n### 4\.5\.)',
    '''### 4.4. Blokk 4 – Hang-létra: „Elér a hangom?” (30–40’)

**Cím:** Hang-létra – hallhatóság erőlködés nélkül
**Időtartam:** 30–40’

**Cél:**

* Kipróbálni, hogyan változik a hallhatóság **távolság, tempó, tagolás, testirány és levegő** szerint.
* Megkülönböztetni a **projekciót** a kiabálástól: ha a tér/zaj nem engedi a kényelmes beszédet, a környezeten változtatunk.
* Konkrét, nem minősítő feedbacket adni arról, hogy **mi volt érthető**.

> **Hangkímélő keret:** nem kiabálunk és nem „versenyzünk hangerőben”. Ha rekedt vagy fáj a torkod, maradj megfigyelő. Zajos térben ne próbáld túlharsogni a zajt: csökkentsd a zajt, közelítsd a csoportot vagy használjatok erősítést. A blokk alapja a NIDCD hanghigiénés ajánlása: kerüld a kiabálást / túl hangos beszédet, támaszd a beszédet jó légzéssel, és használj mikrofont, ha a helyzet indokolja.

**Triádok:** A = beszélő, B = „első sor”, C = „terem vége”.

1. **Próba 1 – normál beszéd (kb. 2 perc/fő):** A elmond egy 20–30 mp-es peula-belépőt kényelmes hangon. B és C csak ezt jelzi vissza:  
   – „Minden szót értettem / itt veszett el egy rész.”  
   – „A tempó itt követhető volt / itt felgyorsult.”  
   Nincs „túl halk személyiség”, „szép hang”, „magabiztos hang” típusú címkézés.
2. **Próba 2 – teremhang (kb. 2 perc/fő):** A ugyanazt a belépőt újramondja úgy, hogy **nem préseli a torkát**: stabilan áll, vesz levegőt a mondat előtt, a csoport felé fordul, rövidebb egységekre tagol és hagy szünetet. C jelzi, eljutott-e hozzá érthetően.
3. **Környezeti döntés:** ha C továbbra sem érti kényelmes hangon, a megoldás **nem a kiabálás**. A triád választ egyet: közelebb hozza a „kvucát”, csökkenti a háttérzajt, más pozícióba áll vagy mikrofont/erősítést kérne.
4. **Szerepcsere** addig, amíg mindenki legalább egyszer beszélő volt. Ha idő szűk, egy kör kötelező, a második próba páronként rövidíthető.

**Mini-reflexió:**

> „Mi javította leginkább az érthetőségedet: hangerő helyett inkább a levegő, a tagolás, a tempó, a testirány vagy a tér átrendezése?”

**Adatvédelem:** ehhez a gyakorlathoz **nem készítünk személyes telefonos felvételt**. Ha a szervezet később külön, jóváhagyott felvételi workflow-t biztosít dokumentált jogalappal, hozzáféréssel, tárolással és törléssel, az lehet opcionális kiegészítő, de **nem feltétele a feladatnak**.
''',
    'M4.A replace video block',
    flags=re.S,
)
s = s.replace('* Telefon(ok) töltve, ha videózni akartok.\n', '')
s = s.replace('– saját kiállás kipróbálása,\n     – 1 fókuszmondat megfogalmazása.',
              '– saját kiállás kipróbálása,\n     – hang/projekció alapszintű kipróbálása,\n     – 1 fókuszmondat megfogalmazása.')
write(rel, s)


# ---------------------------------------------------------------------------
# Study Labs: replace public named status boards with private self-checks.
# ---------------------------------------------------------------------------
for path in MOD.rglob('*.md'):
    if '/Peulák/' not in path.as_posix() or '.F ' not in path.name:
        continue
    text = path.read_text(encoding='utf-8')
    text = text.replace('nem tesszük ki névvel nyilvános anonim témakérő cetli/post-it/progress boardra',
                        'nem tesszük ki névvel nyilvános táblára, matricára, post-itre vagy progress boardra')
    # If the standard Study Lab 4.1 asks participants to mark public progress,
    # replace the entire check-in section. Keep the module-specific 4.2 onward.
    m = re.search(r'### 4\.1\..*?(?=\n\*\*\*\n\n### 4\.2\.)', text, flags=re.S)
    if m and re.search(r'(?i)matric|ragaszd|progress bar|hol tart', m.group(0)):
        block = '''### 4.1. Blokk 1 – Privát check-in: „Hol tartok, miben kérek segítséget?” (0–5’)

**Cél:** a tanuló és a képző lássa a kiindulópontot **nyilvános státuszjelölés nélkül**.

**Előkészítés:** a képző a peula előtt **privát módon** nézze át a Moodle completiont, és csak támogatási célra használja. Ne olvassa fel, ki mivel van lemaradva.

**Tanulói instrukció:**

> „Nézd meg **magadnak** az adott modul leckéit a Moodle-ben, és válassz egyet:  
> **A)** kész / csak ismételnék, **B)** elkezdtem, **C)** még nem kezdtem, **D)** elakadtam és segítség kell.  
> Ezt nem kell a többiek előtt megmutatnod. Írd fel magadnak, **melyik konkrét leckén vagy feladaton** dolgozol a következő 20 percben.”

**Közös, anonim jelzés (opcionális):** ha használtok cetlit, arra **nem státusz és nem név** kerül, hanem egyetlen kérdés/téma, például: „kérdéstípusok”, „pitch”, „nem értem a kaput”. Ezekből a képző gyorsan látja, milyen közös segítség kell.

**Képzői mondat:**

> „Ez support space, nem rangsor. A saját előző állapotodhoz képest akarunk ma egy lépést haladni.”
'''
        text = text[:m.start()] + block + text[m.end():]
    # Remove preparation requirements for a public completion board/stickers.
    text = re.sub(r'^\* \*\*Matricák vagy kis post-it-ek\*\* \(minden résztvevőnek 1 db a check-inhez\)\.\n',
                  '* Opcionális **névtelen témakérő cetlik** a közös segítségkérésekhez; státuszjelölésre nem használjuk.\n', text, flags=re.M)
    text = re.sub(r'^\d+\. Írd fel a táblára .*?`Kész.*?`.*?\n', '', text, flags=re.M)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# Cohort consistency: program is 15+. Do not silently exclude 15-year-olds
# in live peula metadata. This only changes lines explicitly describing the
# trainee cohort, never chanich age profiles.
# ---------------------------------------------------------------------------
for path in MOD.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(\*\*Korosztály:\*\*[^\n]*képzős madrich[^\n]*?)\(\*\*16\+[^\n]*?\)', r'\1(**15+; a program célcsoportja**)', text)
    text = re.sub(r'(\*\*Korosztály:\*\*[^\n]*képzős madrich[^\n]*?)\(16\+\)', r'\1(15+; a program célcsoportja)', text)
    text = re.sub(r'(\*\*Korosztály:\*\*[^\n]*madrichok[^\n]*?)\(16\+\)', r'\1(15+; a program célcsoportja)', text)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# M7 final consistency: numbering and approved-AI language.
# ---------------------------------------------------------------------------
rel = '02 Tervezet/Modulok/M7/M7 – Peula a papírtól a valóságig – Programírás, Zmán Kvucá & AI-támogatott tervezés.md'
s = read(rel)
s = s.replace('4. **AI mint társtervező, nem mint „főnök”**', '4. **AI mint társtervező, nem mint „főnök”**')
# Anna's edit left a duplicated list number: fix only the exact sequence around competency 4.
s = re.sub(r'(3\. \*\*[^\n]+\*\*.*?\n)(1\. \*\*AI mint társtervező)', r'\1\n4. **AI mint társtervező', s, count=1, flags=re.S)
s = s.replace('(pl. ChatGPT)', '(szervezetileg jóváhagyott generatív AI-eszköz)')
s = s.replace('AI-t (pl. ChatGPT)', 'szervezetileg jóváhagyott generatív AI-eszközt')
s = s.replace('gyermekvédelmi ügyben mindig felnőtt/mentor a kontakt',
              'gyermekvédelmi ügyben mindig a kijelölt felelős felnőtt / gyermekvédelmi felelős a kontakt')
write(rel, s)

for path in (MOD / 'M7').rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    text = text.replace('pl. ChatGPT', 'szervezetileg jóváhagyott AI-eszköz')
    text = text.replace('például ChatGPT', 'például a szervezetileg jóváhagyott AI-eszköz')
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# Extend permanent integrity rules for newly closed regressions.
# ---------------------------------------------------------------------------
checker = ROOT / 'tools/content_integrity.py'
s = checker.read_text(encoding='utf-8')
if "'M2.1 identity-map upload'" not in s:
    insert_after = "FORBIDDEN_ACTIVE = {\n"
    # Keep the existing dict intact; add generic phrase-based checks below.
    marker = "REQUIRED_FILES = ["
    block = '''CLOSED_REGRESSIONS = {
    'fotózd le a rajzot, és töltsd fel': 'M2.1 teljes identitástérkép feltöltése visszatérne',
    '2–3 perces minijelenetet': 'súlyos safeguarding-helyzetek kötelező eljátszása visszatérne',
}

'''
    s = s.replace(marker, block + marker, 1)
    old_loop = """        for phrase, why in FORBIDDEN_ACTIVE.items():
            if phrase.lower() in text:
                errors.append(f'REGRESSION {path.relative_to(ROOT)}: {phrase!r} ({why})')"""
    new_loop = old_loop + """
        for phrase, why in CLOSED_REGRESSIONS.items():
            if phrase.lower() in text:
                errors.append(f'REGRESSION {path.relative_to(ROOT)}: {phrase!r} ({why})')"""
    if old_loop not in s:
        raise RuntimeError('content_integrity regression loop changed unexpectedly')
    s = s.replace(old_loop, new_loop, 1)
checker.write_text(s, encoding='utf-8')


# ---------------------------------------------------------------------------
# Assertions: fail before commit if any of these content invariants are false.
# ---------------------------------------------------------------------------
errors: list[str] = []

def must(rel: str, phrase: str) -> None:
    if phrase not in read(rel):
        errors.append(f'MISSING {phrase!r} in {rel}')


def must_not(rel: str, phrase: str) -> None:
    if phrase in read(rel):
        errors.append(f'FORBIDDEN {phrase!r} in {rel}')

must('02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md', 'teljes identitástérképet **nem kell és nem szabad')
must_not('02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md', 'fotózd le a rajzot, és töltsd fel')
must('02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md', 'privát munkalap: nem kerül beadásra')
must_not('02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md', 'Lehetsz **megbízható felnőtt**')
must('02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md', 'Nem kell intim vagy érzékeny részletet')
must('02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md', 'Hang-létra')
must_not('02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md', 'videóra veszi')
# No public progress marking may remain in F peulas.
for path in MOD.rglob('*.md'):
    if '/Peulák/' in path.as_posix() and '.F ' in path.name:
        text = path.read_text(encoding='utf-8').lower()
        if 'ragaszd fel a matric' in text or 'ragaszd fel a sticker' in text:
            errors.append(f'PUBLIC-PROGRESS remains in {path.relative_to(ROOT)}')
# Cohort live peulas should not say trainee cohort 16+.
for path in MOD.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for line in text.splitlines():
        if '**Korosztály:**' in line and 'képzős madrich' in line.lower() and '16+' in line:
            errors.append(f'AGE-MISMATCH {path.relative_to(ROOT)}: {line.strip()}')

if errors:
    raise SystemExit('\n'.join(errors))
print('Final learner-facing content pass assertions passed.')
