# ⚖️ Média-produkció — nyitott döntések

**Ez a dokumentum kézzel karbantartott.** Nem generált, és nem asset-regiszter: csak
azokat a kérdéseket tartalmazza, amelyekre **ember** válaszol, és amelyek nélkül a
gyártás egy része nem indulhat el. Ha egy döntés megszületik, itt kell kivezetni a
nyitott-érték jelölést, és elvégezni a „Mit kell utána átírni” pontban felsoroltakat.
A lezárt döntések a lap alján, egy táblázatban maradnak — nyomon követhetőségért, nem
kérdésként.

A darabszámok forrása a jelenlegi v2 manifeszt (`MEDIA-PRODUCTION-PLAN.md` 2. és 3.
szakasz). **Egy asset több kapun is ülhet**, ezért az „önmagában felszabadul” szám mindig
kisebb vagy egyenlő, mint az „érintett”.

| | Asset | Deliverable |
|---|---:|---:|
| Összesen | 417 | 903 |
| Ebből központilag előgyártható | 407 | 898 |
| Ebből **most gyártható** | **37** | **37** |
| Élő/runtime tétel (a képző hozza létre a peulán) | 3 | 5 |

---

## D1 — Vizuális rendszer: stílus-token és someres paletta (R5)

**A folyamat eldőlt** (2026-08-27): két lépésben zárjuk — előbb a **stílus-token**, utána
a **hex-paletta**. Ami hiányzik, az maga a tizenegy érték.

**Miért ez a legfontosabb:** ez a legnagyobb tétel. Amíg nyitva van, 258 asset nem
gyártható, és ha rosszul indul, 258 asseten kell újragyártani.

**Jelenlegi bizonyíték:** a repositoryban **nulla hex-érték** van — se design-system
fájl, se arculati leírás, se logó-specifikáció. Ami van, az szemantikus színhasználat a
leckékben (SBI: kék/zöld/narancs; 3 pillér: kék/piros/zöld; red flag: piros/zöld; M6.4:
kék/sárga/zöld) és 26 olyan tétel, amelynek a saját technikai jegyzete szerint elég a
fekete-fehér nyomtatás. Részletek és a teljes lock-lap:
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md).

> 🔎 **2026-08-27: a kérdés lényegesen szűkült.** Egy célzott külső kutatás megtalálta a
> mozgalom **saját, nyilvánosan elérhető arculati kézikönyvét** és logócsomagját
> (`somer.hu/arculat/`) — deklarált HEX / RGB / CMYK / Pantone palettával, amelynek mind
> a hat alapszíne **byte-azonosan megerősíthető a hivatalos logó-SVG-ből**. A D1 kérdése
> ezért már nem „mi legyen a paletta”, hanem: **átvesszük-e a meglévőt**, melyik
> színgeneráció a hatályos, és mit teszünk oda, ahol a kézikönyv hallgat (betűméret-skála,
> ikon-stílus, semleges skála). A teljes bizonyíték-lánc, a **kiszámított** WCAG-kontrasztok
> és a két jóváhagyható változat: [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md).
> **Ez bizonyíték, nem jóváhagyás — az R5 blokkolók a 257 asseten a helyükön maradnak.**

**Mit szabadít fel:** R5 lezárása önmagában **247 asset / 489 deliverable**. Az érintett
257-ből 10 azért marad zárva, mert R2-re, R3-ra vagy emberi döntésre is vár.

**Ki dönt:** program-/arculatfelelős, a mozgalmi vizuális identitás jóváhagyójával.

### 1. lépcső — stílus-token

- betűtípus (címsor / törzs): ⟬KITÖLTENDŐ⟭
- fejléc-, margó- és rácsrend a nyomtatványokhoz: ⟬KITÖLTENDŐ⟭
- ikon-stílus: vonal vagy kitöltés, vonalvastagság, sarokkerekítés: ⟬KITÖLTENDŐ⟭
- az AI-provenance címke **vizuális formája és elhelyezése** (a szövege eldőlt — lásd a
  lezárt D9-et a lap alján): ⟬KITÖLTENDŐ⟭
- logóhasználat és biztonsági margó: ⟬KITÖLTENDŐ⟭

### 2. lépcső — paletta és karakter

- someres alap-hex-paletta (elsődleges, másodlagos, akcent): ⟬KITÖLTENDŐ⟭
- háttér- és szövegszín (világos/sötét): ⟬KITÖLTENDŐ⟭
- az R6 szín-ütközés feloldása (a kék és a zöld ma több jelentést is visel): ⟬KITÖLTENDŐ⟭
- karakter-stílus és rögzített referencia-seed: ⟬KITÖLTENDŐ⟭

### Mit jelent a kétlépcsős zárás a manifesztben — pontosan

**A jelenlegi manifeszt egyetlen R5-blokkolót ismer, nem kettőt.** Az első lépcső
lezárásakor tehát **nem** oldódik fel automatikusan a 26 fekete-fehér nyomtatvány: a terv
`media-production-plan.csv` `Szín-függés` oszlopa megmutatja, melyik az a 26 tétel
(`1A — fekete-fehér is elég`), de a státuszuk addig `produkciós szabályra vár`, amíg az R5
blokkoló rajtuk marad. A gyártás **elindítható** rájuk a stílus-token birtokában — a
manifeszt viszont csak akkor követi ezt, ha a második lépcsőben az R5 egészében lezárul,
vagy ha az érintett 26 asset `blockers` mezőjéből külön, tudatos metaadat-művelettel
kivezetjük az R5-öt. Ez utóbbi önálló feladat; ez a pass nem végezte el, és séma-módosítást
nem igényel.

**Mit kell utána átírni:** `produkcios-szabalyok.json` R5 (a nyitott-érték jelölés
kivezetése), [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) értékei, majd
`python3 tools/media_manifest.py build`.

---

## D2 — Narrátor: TTS-motor vagy emberi felmondó, és melyik hang (R3)

**Kérdés:** a 90 narráció és a videók hangja **szintetizált hang** legyen-e (és ha igen,
melyik motor és melyik voice-ID), vagy **emberi felmondó** (és ki)?

**Miért fontos:** ez az egyetlen igazi nyitott kérdés az R3-ban. Minden más — nyelv,
tegező regiszter, tempó, hangulat, kiejtés, felirat-viszony — a tananyagból objektíven
levezethető, és készen áll: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md).

**Jelenlegi bizonyíték:** az R3 szövege maga mondja ki, hogy „modulonként a TTS vs.
emberi felmondó döntés dokumentálandó”, és hogy a konkrét TTS-motor / voice-ID
kitöltetlen. A leckék technikai jegyzetei közül 21 említi egyáltalán a TTS-t; ebből három
mondja ki szó szerint, hogy „TTS vagy emberi narráció” (mind az M1.4-ben), és hat az
M6.1-ben már csak „Hang (TTS)”-t ír. A döntés tehát nem egységesen van nyitva hagyva a
leckékben sem. A repositoryban **nincs kiválasztott szolgáltató**, és a specifikáció nem
nevez meg egyet sem.

**A) Egyetlen szintetikus hang** az egész tananyagra.
**B) Egyetlen emberi felmondó** az egész tananyagra.
**C) Vegyes** — a beszélőfej-videók szintetikusak, a sima narráció emberi (vagy fordítva).

**Ajánlás: nincs.** Ez szolgáltató- és költségdöntés, amihez a repository nem tartalmaz
bizonyítékot; kitalálni nem szabad. Amit érdemes tudni a döntéshez: a **C** két hangot
jelentene, amit az R3 első mondata („EGYETLEN konzisztens narrátor-hang az egész
tananyagban”) kizár, hacsak a jóváhagyó ezt felül nem írja. Az **A** választása a **D3**
bizonyíték-listát is bővíti; a **B** nem.

> 🔎 **2026-08-27: a szolgáltatói mező kutatva.** A jelöltek, a magyar támogatásuk, a
> kiejtés-vezérlésük, a licencfeltételeik és az áraik elsődleges, szolgáltatói forrásból:
> [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13. szakasz. Röviden: a szintetikus ágon a
> **költség nem differenciál** (0–22 $ a teljes tananyagra), a kiejtés-kikényszeríthetőség
> viszont igen — egyetlen jelölt dokumentál magyar IPA fonéma-készletet. A hangot
> **meghallgatással** kell kiválasztani, ehhez három tananyagbeli tesztszkript készült:
> [`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md). **Az R3 blokkoló mind a 117
> tételen a helyén marad.**
>
> ⚠️ **Új emberi kapu, amit a kutatás hozott elő (V1).** Az egyik jelölt szolgáltató a
> saját átláthatósági dokumentumában **megköveteli** a szintetikus hang tényének közlését,
> és külön kimondja, hogy kiskorúakat érintő felhasználásnál a **szülő/gondviselő** felé is
> világos tájékoztatás kell. A tananyag R1-címkéje a **tanulónak** szól. Hogy ez önmagában
> kielégíti-e az elvárást, **gyermekvédelmi és adatvédelmi kérdés** — a gyermekvédelmi
> felelősé és a DPO-é, nem a médiaprodukcióé. Ez a lap nem dönti el.

**Mit szabadít fel:** R3 lezárása önmagában **90 asset / 267 deliverable**. További 27
tétel ekkor is R2-re vagy R5-re vár, ezért az R3 + R2 együtt — az R5-öt még nyitva hagyva
— **111 asset / 351 deliverable**.

**Ki dönt:** program- és költségvetési felelős; szintetikus hangnál a jogi jóváhagyóval
együtt.

**A válasz helye:**
- felmondó típusa (szintetikus / emberi): ⟬KITÖLTENDŐ⟭
- motor vagy felmondó személy: ⟬KITÖLTENDŐ⟭
- voice-ID / hangminta hivatkozás: ⟬KITÖLTENDŐ⟭

**Mit kell utána átírni:** `produkcios-szabalyok.json` R3,
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) „Motor és hang” szakasza,
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) hang-sorai, majd build.

---

## D3 — Az R2 jogi bizonyítékai

**A hatály eldőlt** (2026-08-27, A opció): az R2 a beszélőfej-videókra, az AI emberi
karakterjelenetekre és a belőlük kivett állóképekre egyaránt vonatkozik — összesen **28
asset** —, hacsak egy későbbi jogi review kifejezetten nem szűkíti. A hétköznapi
AI-illusztrációk, ikonok és diagramok **nem** tartoznak ide: azokra az R1 (AI-jelölés)
vonatkozik.

**Ami nyitva maradt: maga a bizonyíték.** Az R2 szövege szerint minden ilyen assethez
dokumentálni kell a generátort, a kereskedelmi/oktatási felhasználást engedő licencet és a
hang-jogosultságot. Ebből ma **egy sincs meg**; a teljes lista soronként:
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1. szakasz.

**Mit szabadít fel:** önmagában **0**. A 28 R2-tételből 26 R3-ra is vár, a másik kettő
(`M4.1-FOTO-01/02`, néma állóképek) R5-re. R2 + R3 együtt, R5 nélkül **111 asset /
351 deliverable**.

**Ki dönt:** jogi jóváhagyó.

> 🔎 **2026-08-27: a jelöltek és a feltételeik kutatva.** Megnevezett jelöltek, idézett
> kereskedelmi, kimenet-tulajdonlási, képmás- és provenance-záradékokkal, jelöltenkénti
> bizonyíték-állapottal: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A. szakasz. A
> javasolt gyártási útvonal és a tartalékok:
> [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 4–5. szakasz.
>
> **A nyilvános szolgáltatási feltétel nem azonos a produkciós fiók bizonyítékával.**
> Fiókot nem hoztunk létre, próbaidőszakot nem indítottunk, generálást nem futtattunk. Az
> R2 mind a hat bizonyíték-sora **HIÁNYZIK** marad, és a 28 asset blokkolója a helyén.
>
> ⚠️ **Két új emberi kapu, amit a kutatás hozott elő.**
>
> **J1 — jogi.** A javasolt karakter-jelenet szolgáltató feltételei tartalmaznak egy
> záradékot, amely tiltja a generatív szolgáltatás használatát olyan online szolgáltatás
> részeként, amely 18 év alattiakhoz szól vagy hozzájuk valószínűleg eljut. A tananyag
> célközönsége **15+**. Hogy az **offline legyártott, majd Moodle-ön kiszolgált** asset
> ebbe a mondatba esik-e, **jogi olvasat** — és ha igen, az kizárja a javasolt stacket.
>
> **J2 — gyermekvédelmi és szerzői.** A vizsgált szolgáltatók feltételei egybehangzóan
> **felnőtt** megjelenésű avatart és karaktert engednek (kiskorú ábrázolása avatarral
> tiltott, egyedi avatarhoz nagykorúság kell, a személy-generálás EU-ban felnőttre
> korlátozott). A tananyag viszont **madrichot** ábrázol, és a kánoni szabály szerint a
> madrich maga is lehet kiskorú. Ez **nem eszközválasztási kérdés**: a gyermekvédelmi
> felelősnek és a szerzőnek kell rendeznie. Ez a lap megáll itt.

**A válasz helye:**
- generátor / szolgáltató neve és verziója: ⟬KITÖLTENDŐ⟭
- kereskedelmi-oktatási felhasználást engedő licenc hivatkozása: ⟬KITÖLTENDŐ⟭
- avatar-/képmás-jogosultság igazolása: ⟬KITÖLTENDŐ⟭
- hang-jogosultság (voice-talent release vagy klónozási engedély): ⟬KITÖLTENDŐ⟭

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

**Ajánlás: A**, de ez **nem** hajtható végre jóváhagyás nélkül: a hub látható
gyermekvédelmi mondatának átírása szakpolitikai döntés. Az A melletti tárgyi érv: az
ötcsomópontos sablon már létezik, teljes, és minden kötelező elemet tartalmaz. A „nem
ígérek 100% titoktartást” követelmény egyik változatban sem gyengülhet.

**Mit szabadít fel:** 1 asset / 1 deliverable. A tét nem a darabszám, hanem hogy ne
készüljön olyan fali poszter, amiről lemarad egy kötelező gyermekvédelmi lépés.

**Ki dönt:** a `Gyermekvédelem – release gate.md` dokumentumban névvel jóváhagyott
gyermekvédelmi felelős.

**A válasz helye:** kanonikus lépés-térkép csomópontszáma és a hub mondatának sorsa:
⟬KITÖLTENDŐ⟭

---

## D8 — Az R8 státusza: betartandó szabály vagy önálló jóváhagyási kapu?

**Kérdés:** a két valós felvétel (`M0.3-FOTO-01` Moodle-képernyőkép, `M0.A-FOTO-01`
kvuca-plakát fotók) legyártható-e az R8 **betartásával**, vagy külön adatvédelmi és
gyermekvédelmi **jóváhagyás** kell hozzá?

**Jelenlegi bizonyíték:** az R8 szövegében — az R2/R3/R5-tel ellentétben — **nincs**
kitöltetlen érték: kész, betartható előírás (anonimizálás vagy kikeretezés, kiskorúnál
előzetes dokumentált szülői hozzájárulás, képernyőképen nincs valós felhasználónév/arc).
A `README.md` viszont kimondja, hogy ennek a státusza nyitott. Az `M0.A-FOTO-01`
kézírásos plakátokról készül, és a képző hozza létre a peula után — a produkciós tervben
ezért az élő/runtime szakaszban áll, nem gyártási kötegben.

**A) Betartandó szabály.** Az R8 nem kapu: a két tétel a szabály betartásával gyártható,
a bizonyítékot a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) rögzíti.
**B) Önálló jóváhagyási kapu.** A két tétel csak a gyermekvédelmi és adatvédelmi felelős
írásos jóváhagyása után élesíthető.

**Reviewer-ajánlás: A** — asset-szintű kötelező produkciós szabály, előírt bizonyítékkal
és átalakítással, nem külön általános jóváhagyás. **Ez nem jogi lezárás:** a jelenlegi R8
blokkolók emiatt nem kerültek ki egyik assetről sem.

**Mit szabadít fel:** R8 önmagában **0 asset** a központi gyártásból — az egyetlen érintett
tétel (`M0.3-FOTO-01`) az R7-re is vár. Az `M0.A-FOTO-01` élő/runtime tétel.

**Ki dönt:** gyermekvédelmi felelős + adatvédelmi (DPO) felelős.

**A válasz helye:** R8 státusza (szabály / kapu): ⟬KITÖLTENDŐ⟭

---

## D10 — A ken alkohol- és dohányzási magatartási kódexe (M3.4)

**Kérdés:** mi a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és
dohányzási szabályzata (mit, hol, milyen kortól)?

**Miért van itt:** ez nem új döntés — a kánoni `Emberi jóváhagyás szükséges.md` már
nyitott szervezeti tételként tartja nyilván. Az viszont csak most látszik, hogy **két
média-assetet is gátol**: az `M3.4-EGY-03` sorting-feladat 6–8. kártyája és az
`M3.4-DIA-01` diagram 3C blokkja a kódex tartalmától függ. A lecke maga mondja ki:
„Ennek hiányában ez a tartalmi rész nem élesíthető.” Korábban egyik asset készültségi
állapota sem tükrözte ezt — az `M3.4-EGY-03` emiatt tévesen a „most gyártható” kötegben
állt.

**Mit szabadít fel:** 2 asset / 3 deliverable. Az `M3.4-DIA-01` ezen felül az R5-re is vár.

**Ki dönt:** a ken vezetése / a képzésért felelős; a válasz helye a kánoni
`Emberi jóváhagyás szükséges.md`, nem ez a lap.

**Megjegyzés:** a 3A és 3B témablokk tartalma kész; csak a 3C függ a kódextől.

---

## Ami NEM döntés, csak függőség

**R7 — véglegesített Moodle-felület.** Egyetlen assetet érint (`M0.3-FOTO-01`), és nem
kérdés, hanem sorrend: a kurzus-főoldal képernyőképe csak az éles felület után
készíthető. Nem indokolja egyetlen más köteg csúszását sem — ez az utolsó tétel. A
vonatkozó runtime-elfogadás a `LMS – H5P runtime acceptance.md` dokumentumban lakik.

**A kurzus release-kapui.** A `RELEASE-READINESS.md`, a gyermekvédelmi és az adatvédelmi
gate NEM ennek a dokumentumnak a hatásköre, és nem is zárható le média-oldalról.

---

## Lezárt döntések (2026-08-27)

Nyomon követhetőségért; ezek már nem kérdések.

| ID | Döntés | Mi történt a kánoni forrásban |
|---|---|---|
| **D3 (hatály)** | Az R2 a beszélőfej-videókra, az AI karakterjelenetekre és a freeze-frame-ekre is vonatkozik (A opció). | A 28 asset `blockers` mezője változatlanul viszi az R2-t. A bizonyíték-kérdés fent, D3 alatt marad nyitva. |
| **D4** | Az M4 HOOK-formátum marad vegyes: az M4.2–M4.4 statikus illusztrációval nyit, új beszélőfej-videó nem készül (A opció). | Az `M4.2-ILL-01` `decision` mezője kiürült; az asset a szokásos R5 alatt gyártandó. |
| **D6** | Az `M1.3-VID-01` HOOK-dialógjának szövege jóváhagyva (A opció). | A szó szerinti szöveg `@source` blokkba került az M1.3 leckében (`M1.3-VID-01-VO`), az asset `source_ref`-fel hivatkozik rá, a felirat és a leirat onnan generálódik. Az asset továbbra is R2 + R3 + R5 alatt áll. |
| **D7** | Az `M3.2-NAR-02` opcionális narráció **nem készül el** (B opció). | A szemantikus asset és a három deliverable megszűnt; a dia látható tartalma változatlan, csak az „Opcionális narráció (30–40 mp)” sor került ki. A három történeti v1 sor `NO_LONGER_REQUIRED` diszpozícióval, indoklással egyeztetve (`_legacy/legacy-dispositions.json`). |
| **D9** | A kanonikus, tanulónak látható AI-provenance címke szövege: **„AI-generált médiaelem · emberi lektorálással.”** | Rögzítve a `produkcios-szabalyok.json` R1 szabályában (`human_label` mező), és kivezetve mind a 21 aktív előfordulásra a tananyagban. A címke **vizuális megjelenése és elhelyezése** továbbra is a D1 első lépcsőjétől függ. |
| **F-02** | Az élő/runtime tételek nem számítanak a központi „most gyártható” kötegbe. | `technical.production_phase: trainer-at-runtime` három asseten (`M0.A-EGY-01`, `M0.A-FOTO-01`, `Z.A-KART-04`); a produkciós terv külön szakaszban mutatja őket, a rájuk vonatkozó kapukkal együtt. A követelményük és a deliverable-jük megmarad. |
