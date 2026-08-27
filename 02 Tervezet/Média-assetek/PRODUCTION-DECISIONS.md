# ⚖️ Média-produkció — nyitott döntések

**Ez a dokumentum kézzel karbantartott.** Nem generált, és nem asset-regiszter: csak
azokat a kérdéseket tartalmazza, amelyekre **ember** válaszol, és amelyek nélkül a
gyártás egy része nem indulhat el. Ha egy döntés megszületik, itt kell kivezetni a
nyitott-érték jelölést, és elvégezni a „Mit kell utána átírni” pontban felsoroltakat.

A darabszámok forrása a jelenlegi v2 manifeszt
(`MEDIA-PRODUCTION-PLAN.md` 2. és 3. szakasz).
**Egy asset több kapun is ülhet**, ezért az „önmagában felszabadul” szám mindig
kisebb vagy egyenlő, mint az „érintett”.

| | Asset | Deliverable |
|---|---:|---:|
| Összesen | 418 | 906 |
| Ebből most gyártható | **39** | **39** |

---

## D1 — Vizuális rendszer: stílus-token és someres paletta (R5)

**Kérdés:** mi a tananyag kötelező vizuális rendszere — betűtípus, elrendezés, ikon- és
karakterstílus —, és mik a someres alapszínek pontos hex-értékei?

**Miért ez a legfontosabb:** ez a legnagyobb tétel. Amíg nyitva van, 258 asset nem
gyártható, és ha rosszul indul, 258 asseten kell újragyártani.

**Jelenlegi bizonyíték:** a repositoryban **nulla hex-érték** van — se design-system
fájl, se arculati leírás, se logó-specifikáció. Ami van, az szemantikus színhasználat a
leckékben (SBI: kék/zöld/narancs; 3 pillér: kék/piros/zöld; red flag: piros/zöld; M6.4:
kék/sárga/zöld) és 26 olyan tétel, amelynek a saját technikai jegyzete szerint elég a
fekete-fehér nyomtatás. Részletek és a teljes lock-lap:
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md).

**A) Két lépésben zárjuk (ajánlott).** Először a **stílus-token** (betűtípus, fejléc- és
margórend, ikon-vonalvastagság, karakterstílus, AI-jelölés helye) — ezzel a 26
fekete-fehér nyomtatvány azonnal indul; utána a **hex-paletta**, ami a 17 kimondottan
színfüggő tételt engedi el.
**B) Egyben zárjuk.** Egyszerre születik meg a teljes lock-lap; addig a 248 R5-tétel
egyike sem indul.

**Ajánlás: A.** A fekete-fehér nyomtatványok soha nem hivatkoznak hex-értékre, tehát a
paletta-vita nem is érinti őket; a korai indulás viszont a legnagyobb kötegnél nyer időt.
A kockázat kicsi, mert a stílus-token nélkül egyik változat sem indulhat.

**Mit szabadít fel:** R5 lezárása önmagában **248 asset / 491 deliverable**. Az érintett
258-ból 10 azért marad zárva, mert R2-re, R3-ra vagy emberi döntésre is vár.

**Ki dönt:** program-/arculatfelelős, a mozgalmi vizuális identitás jóváhagyójával.

**A válasz helye:**
- someres alap-hex-paletta: ⟬KITÖLTENDŐ⟭
- betűtípus (címsor / törzs): ⟬KITÖLTENDŐ⟭
- ikon-stílus (vonal/kitöltés, vonalvastagság): ⟬KITÖLTENDŐ⟭
- karakter-stílus és referencia-seed: ⟬KITÖLTENDŐ⟭
- logóhasználat és biztonsági margó: ⟬KITÖLTENDŐ⟭

**Mit kell utána átírni:** `produkcios-szabalyok.json` R5 (a nyitott-érték jelölés kivezetése),
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) értékei, majd
`python3 tools/media_manifest.py build`.

---

## D2 — Narrátor: TTS-motor vagy emberi felmondó, és melyik hang (R3)

**Kérdés:** a 91 narráció és a videók hangja **szintetizált hang** legyen-e (és ha igen,
melyik motor és melyik voice-ID), vagy **emberi felmondó** (és ki)?

**Miért fontos:** ez az egyetlen igazi nyitott kérdés az R3-ban. Minden más — nyelv,
tegező regiszter, tempó, hangulat, kiejtés, felirat-viszony — a tananyagból objektíven
levezethető, és készen áll: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md).

**Jelenlegi bizonyíték:** az R3 szövege maga mondja ki, hogy „modulonként a TTS vs.
emberi felmondó döntés dokumentálandó”, és hogy a konkrét TTS-motor / voice-ID
kitöltetlen.
A leckék technikai jegyzetei közül 21 említi egyáltalán a TTS-t; ebből három mondja ki
szó szerint, hogy „TTS vagy emberi narráció” (mind az M1.4-ben), és hat az M6.1-ben már
csak „Hang (TTS)”-t ír. A döntés tehát nem egységesen van nyitva hagyva a leckékben sem.
A repositoryban **nincs kiválasztott szolgáltató**, és a specifikáció nem nevez meg egyet
sem.

**A) Egyetlen szintetikus hang** az egész tananyagra.
**B) Egyetlen emberi felmondó** az egész tananyagra.
**C) Vegyes** — a beszélőfej-videók szintetikusak, a sima narráció emberi (vagy fordítva).

**Ajánlás: nincs.** Ez szolgáltató- és költségdöntés, amihez a repository nem tartalmaz
bizonyítékot; kitalálni nem szabad. Amit érdemes tudni a döntéshez: a **C** két hangot
jelentene, amit az R3 első mondata („EGYETLEN konzisztens narrátor-hang az egész
tananyagban”) kizár, hacsak a jóváhagyó ezt felül nem írja. Az **A** választása a **D3**
jogi kérdést is élesíti; a **B** nem.

**Mit szabadít fel:** R3 lezárása önmagában **90 asset / 267 deliverable**. További 26
tétel ekkor is R2-re vár (beszélőfej- és karaktervideók); az R3 + R2 együtt — az R5-öt
még nyitva hagyva — **111 asset / 351 deliverable**. (Ha az R5 is zárva van, a maradék 7
karakter-tétel is felszabadul.)

**Ki dönt:** program- és költségvetési felelős; szintetikus hangnál a jogi jóváhagyóval együtt.

**A válasz helye:**
- felmondó típusa (szintetikus / emberi): ⟬KITÖLTENDŐ⟭
- motor vagy felmondó személy: ⟬KITÖLTENDŐ⟭
- voice-ID / hangminta hivatkozás: ⟬KITÖLTENDŐ⟭

**Mit kell utána átírni:** `produkcios-szabalyok.json` R3,
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) „Motor és hang” szakasza,
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) hang-sorai, majd build.

---

## D3 — Az R2 hatálya és a szükséges jogi bizonyíték

**Kérdés:** az R2 („AI-avatar / AI-hang IP-megfelelőség”) csak a 21 beszélőfej-videóra
vonatkozik, vagy a teljes alakos AI-karakterjelenetekre és a belőlük kivett állóképekre is?

**Miért fontos:** ez a különbség 7 asset (M1.3-VID-01, M4.1-VID-02/03/04/05,
M4.1-FOTO-01/02) besorolását dönti el, és azt, hogy kell-e rájuk licenc-bizonyíték.

**Jelenlegi bizonyíték:** az R2 szövege „minden AI-avatar és AI-hang assethez” írja elő a
generátor nevét, a kereskedelmi licencet és a voice-talent release-t. A hét tétel
AI-generált emberi alakot ábrázol, a videók szintetikus narrációval. Ezért **a jelenlegi
manifeszt a szigorúbb olvasatot alkalmazza**: mind a hét R2 alá került. A hétköznapi
AI-illusztrációk, ikonok és diagramok **nem** kaptak R2-t — azokra az R1 (AI-jelölés)
vonatkozik.

**A) Marad a szigorúbb olvasat** (jelenlegi állapot): a karakterjelenetek és a
freeze-frame-ek is R2 alá tartoznak.
**B) Szűkítés a beszélőfejekre**: a karakterjelenetekre csak R1 + R5 vonatkozik.

**Ajánlás: A**, amíg jogi jóváhagyó mást nem mond. A szűkítés visszavonható egy soros
módosítás; a fordítottja — utólag kiderülő licenchiány 7 legyártott videón — nem.

**Mit szabadít fel:** önmagában **0**. A 28 R2-tételből 26 R3-ra is vár, a másik kettő
(`M4.1-FOTO-01/02`, néma állóképek) R5-re. R2 + R3 együtt, R5 nélkül **111 asset /
351 deliverable**.

**Ki dönt:** jogi jóváhagyó. A bizonyítékok nyilvántartása:
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).

**A válasz helye:**
- R2 hatálya (csak beszélőfej / karakterjelenet is): ⟬KITÖLTENDŐ⟭
- generátor / szolgáltató neve: ⟬KITÖLTENDŐ⟭
- kereskedelmi-oktatási felhasználást engedő licenc hivatkozása: ⟬KITÖLTENDŐ⟭
- avatar-/képmás-jogosultság igazolása: ⟬KITÖLTENDŐ⟭
- hang-jogosultság (voice-talent release vagy klónozási engedély): ⟬KITÖLTENDŐ⟭

---

## D4 — M4 HOOK-formátum (`M4.2-ILL-01`)

**Kérdés:** az M4.2–M4.4 leckék statikus illusztrációval nyissanak (jelenlegi állapot),
vagy az M4.1-hez hasonlóan beszélőfej-videóval?

**Jelenlegi bizonyíték:** a korpuszban **nincs egységes HOOK-konvenció.** 17 lecke nyit
beszélőfejjel (M1.1, M1.2, M2.1–M2.4, M3.1–M3.4, M4.1, M5.1, M6.1, M6.2, M7.2–M7.4),
15 statikus vizuállal vagy interaktív videóval (M0.1, M0.2, M0.4, M1.3, M1.4, M4.2–M4.4,
M5.2, M5.3, M6.3, M7.1, Z.1–Z.3). A vegyes nyitás **modulon belül** is előfordul az M1,
M5, M6 és M7 modulokban. Az M4 tehát nem kivétel, hanem a minta.

**A) A jelenlegi vegyes nyitás megerősítése.** Nincs új gyártás; `M4.2-ILL-01` az R5
kötegbe kerül a többi illusztrációval.
**B) M4-en belüli egységesítés beszélőfejre.** Három új beszélőfej-videó (M4.2, M4.3,
M4.4), három új szkript, mindegyik R2 + R3 alatt — tehát a jelenlegi három illusztráció
helyett a leglassabb kötegbe kerülnek.

**Ajánlás: A.** A „modulon belüli inkonzisztencia” megállapítás a korpusz egészén nem
áll meg, a **B** pedig három tételt a legkorábbi kötegből a legkésőbbibe mozgatna.

**Mit szabadít fel:** A választása 1 asset / 2 deliverable (R5 alá). B választása 3
tételt R5-ből R2+R3-ba tol, és 3 új szkriptet igényel.

**Ki dönt:** a tananyag szerzője / program-felelős.

**A válasz helye:** HOOK-formátum M4.2–M4.4: ⟬KITÖLTENDŐ⟭

**Mit kell utána átírni:** az `M4.2 – Aktív hallgatás & visszatükrözés.md` fájlban az
`M4.2-ILL-01` `decision` mezőjét ki kell üríteni (A választásánál), vagy fel kell venni
a három új videó-assetet (B), majd build.

---

## D5 — M3 gyermekvédelmi lépés-térkép poszter (`M3-HUB-POSZ-01`)

**Kérdés:** a modul-áttekintőben leírt poszter ugyanaz az anyag-e, mint a peula ötlépéses
lépés-térkép sablonja (`M3.B-MUNK-01`)?

**Miért biztonságkritikus:** a peula sablonjának **2. csomópontja** a nem alkudható
instrukció: „Meghallgatom röviden, biztonságosan (nem ígérek 100% titoktartást)”.
A hub összefoglalója négy lépést sorol (észreveszem → jelzek → nem maradok egyedül → kit
vonok be), amiből ez a lépés és az utánkövetés hiányzik. A titoktartás-tilalom a
tananyagban **blokkoló** követelmény: szerepel a modul kompetenciasorában (§2), a hub
operatív szabályában, az M3.3 és M3.4 visszajelzéseiben, a peula négy pontján, és a
KAPU-rubrika **blokkoló R2 (titoktartás)** sorában.

**A) Egy anyag.** A hub posztere a peula ötcsomópontos sablonjának megjelenése →
`mode: reuse`, `reuse_of: M3.B-MUNK-01`, és a hub összefoglaló mondatát hozzá kell
igazítani.
**B) Két külön anyag.** Marad a négylépéses poszter is — ekkor le kell írni, milyen
gyermekvédelmi tartalommal áll meg a rövidebb változat a titoktartás-lépés nélkül.

**Ajánlás: A**, de **Claude nem dönti el.** A hub látható gyermekvédelmi mondatának
átírása szakpolitikai döntés; a repository szabálya szerint ide nem nyúlunk jóváhagyás
nélkül. Az A melletti tárgyi érv: az ötcsomópontos sablon már létezik, teljes, és minden
kötelező elemet tartalmaz.

**Mit szabadít fel:** 1 asset / 1 deliverable. A tét nem a darabszám, hanem hogy ne
készüljön olyan fali poszter, amiről lemarad egy kötelező gyermekvédelmi lépés.

**Ki dönt:** a `Gyermekvédelem – release gate.md` dokumentumban névvel jóváhagyott
gyermekvédelmi felelős.

**A válasz helye:** kanonikus lépés-térkép csomópontszáma és a hub mondatának sorsa:
⟬KITÖLTENDŐ⟭

---

## D6 — `M1.3-VID-01` HOOK-dialóg: végleges szöveg jóváhagyása

**Kérdés:** a lecke SLIDE 1 „Mit látunk?” blokkjában álló négy mondat a **végleges,
felmondható** dialóg?

**Jelenlegi bizonyíték:** a lecke kiírja mind a négy mondatot, de a „Mit hallunk? (videó
dialóg)” sor kifejezetten így fogalmaz: „**Nagyjából** a fenti mondatok, rövid, érthető
felirattal (max. 1–2 sor).” Ez implementációs szabadság, nem jóváhagyott szkript, ezért
az asset `blokkolt` marad, és a felirat/leirat nem gyártható.

### Javasolt szövegváltozat (JAVASLAT — NEM jóváhagyott forrás)

> **1. verzió — címkéző**
> **Madrich A:** „Te mindig szétvered a peulát, komolyan mondom…”
> **Madrich B:** „Mi van?! Csak próbáltam feldobni a hangulatot…”
>
> **2. verzió — SBI-szerű**
> **Madrich A:** „Figyelj, amikor ma a játék közben háromszor félbeszakítottad a
> többieket, nagyon nehéz volt megtartani a figyelmüket és a bevonódásukat. Jó lenne, ha
> ők is több teret kapnának.”
> **Madrich B:** „Jaa… erre nem is gondoltam. Oké, figyelek rá.”

Ez a változat **kizárólag a lecke jelenlegi mondataiból** áll; egyetlen új pedagógiai
tartalom sincs benne. A hangsúlyjelölés (`**…**`) a videóban az S/B/I ikonok
felvillanásának helye.

**A) Jóváhagyás.** A fenti szöveg a végleges dialóg → `@source` blokkba kerül a leckében,
`source_ref` az assetre, és a felirat/leirat automatikusan feltöltődik.
**B) Átírás.** A szerző más szöveget ad; ugyanaz a lépés, más tartalommal.

**Ajánlás: A**, de csak szerzői jóváhagyással. Amíg nincs, marad blokkolt.

**Mit szabadít fel:** 1 asset / 3 deliverable — de az asset R2 + R3 + R5 alatt is áll,
tehát a szkript jóváhagyása önmagában nem teszi gyárthatóvá.

**Ki dönt:** a lecke szerzője.

**A válasz helye:** végleges dialóg jóváhagyva: ⟬KITÖLTENDŐ⟭

---

## D7 — `M3.2-NAR-02` Input 1 narráció: van-e egyáltalán, és mi a szövege?

**Kérdés:** elkészüljön-e az „Input 1” opcionális narráció, és ha igen, mi a szó szerinti
szövege?

**Jelenlegi bizonyíték:** a lecke a diaszöveget teljes egészében megadja (négy
kvuca-profil fókuszszavai; „Ha madrichként minden kvucának ugyanúgy próbálsz peulát
tartani, előbb-utóbb vagy ők fognak unatkozni, vagy te készülsz ki teljesen.”; „Ezért
segít, ha van 1–1 gyors »fejprofilod« mind a négy kvucáról.”), de a narrációt csak
**opcionálisként** jelzi, verbatim szöveg nélkül.

### Javasolt szövegváltozat (JAVASLAT — NEM jóváhagyott forrás)

> „Miért fontos, hogy máshogy nézz rá a kvucákra?
> A Parparimnál a játék, a mozgás és a fantázia visz;
> a Kivszánál a státusz, a poén és az, hogy ki a menő;
> a Leviatannál a drámák, a barátságok és az identitás;
> a Zoreánál a vélemények, a viták és a felelősség.
>
> Ha minden kvucának ugyanúgy próbálsz peulát tartani,
> előbb-utóbb vagy ők fognak unatkozni, vagy te készülsz ki teljesen.
> Ezért segít, ha van egy-egy gyors fejprofilod mind a négy kvucáról.”

30–40 másodperc, tegező, a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) szerint. A szöveg
**kizárólag a jelenlegi diaszövegből** áll: nincs benne új tény, nincs új korosztályi
állítás, és a profilokat ugyanazokkal a szavakkal írja le, mint a dia.

**A) Jóváhagyás** — `@source` blokkba kerül, `source_ref` az assetre.
**B) Elhagyás** — a narráció opcionális; ha nem készül el, az assetet törölni kell a
leckéből (a v1 sor a történeti egyeztetésben marad).

**Ajánlás: A.** A dia szövege hangban is elhangzik, ami a mobil-first és a
képernyőolvasós használatnak is jót tesz; az elhagyás viszont legitim, mert a forrás maga
opcionálisnak jelöli.

**Mit szabadít fel:** 1 asset / 3 deliverable, utána már csak R3-ra vár.

**Ki dönt:** a lecke szerzője.

**A válasz helye:** Input 1 narráció sorsa és szövege: ⟬KITÖLTENDŐ⟭

---

## D8 — Az R8 státusza: betartandó szabály vagy önálló jóváhagyási kapu?

**Kérdés:** a két valós felvétel (`M0.3-FOTO-01` Moodle-képernyőkép, `M0.A-FOTO-01`
kvuca-plakát fotók) legyártható-e az R8 **betartásával**, vagy külön adatvédelmi és
gyermekvédelmi **jóváhagyás** kell hozzá?

**Jelenlegi bizonyíték:** az R8 szövegében — az R2/R3/R5-tel ellentétben — **nincs**
kitöltetlen érték: kész, betartható előírás (anonimizálás vagy kikeretezés,
kiskorúnál előzetes dokumentált szülői hozzájárulás, képernyőképen nincs valós
felhasználónév/arc). A `README.md` viszont kimondja, hogy ennek a státusza nyitott.
Az `M0.A-FOTO-01` kézírásos plakátokról készül, és **képzői feladat gyártáskor, nem
előre legyártott anyag** — ez a különbség a döntésben számít.

**A) Betartandó szabály.** Az R8 nem kapu: a két tétel a szabály betartásával gyártható,
a bizonyítékot a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) rögzíti.
**B) Önálló jóváhagyási kapu.** A két tétel csak a gyermekvédelmi és adatvédelmi felelős
írásos jóváhagyása után élesíthető.

**Ajánlás: nincs.** Adatvédelmi és gyermekvédelmi hatáskör; a repository nem tartalmaz
olyan bizonyítékot, amiből ez levezethető lenne.

**Mit szabadít fel:** R8 önmagában 1 asset / 2 deliverable (`M0.A-FOTO-01`).
Az `M0.3-FOTO-01` az R7-re (éles Moodle-felület) is vár, tehát utolsóként készül.

**Ki dönt:** gyermekvédelmi felelős + adatvédelmi (DPO) felelős.

**A válasz helye:** R8 státusza (szabály / kapu): ⟬KITÖLTENDŐ⟭

---

## Ami NEM döntés, csak függőség

**R7 — véglegesített Moodle-felület.** Egyetlen assetet érint (`M0.3-FOTO-01`), és nem
kérdés, hanem sorrend: a kurzus-főoldal képernyőképe csak az éles felület után
készíthető. Nem indokolja egyetlen más köteg csúszását sem — ez az utolsó tétel.
A vonatkozó runtime-elfogadás a `LMS – H5P runtime acceptance.md` dokumentumban lakik.

**A kurzus release-kapui.** A `RELEASE-READINESS.md`, a gyermekvédelmi és az adatvédelmi
gate NEM ennek a dokumentumnak a hatásköre, és nem is zárható le média-oldalról.
