# 🎨 Vizuális rendszer — produkciós lock-lap

Az R5 produkciós szabály végrehajtási lapja. **Nem arculati kézikönyv:** csak azokat az
értékeket rögzíti, amelyek nélkül a 265 vizuális és nyomtatott asset nem gyártható le
egységesen. Ami már objektíven megvan a tananyagban, azt kimondja; ami hiányzik, azt
nyitottként jelöli, és a [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D1
pontjára mutat.

> ✅ **A D1 2026-10-02-án lezárult** (projektgazdai döntés, `HUM-MEDIA-01`): a hivatalos
> Somer-paletta; a 2022-es arculati kézikönyv és a hivatalos SVG színgenerációja a kánon; a
> [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) **B változata** (Source Sans 3 +
> produkciós semleges skála); a szín szemantikája modulhatókörű; a `#2B2523` csak a logón
> belül. A 4. szakasz mezői ennek alapján kitöltve. Utólagos ellenőrzés (vétó/QA): a
> kreatív/márkafelelős.

Három bizonyíték-osztályt tart külön:

| | Jelentés |
|---|---|
| ✅ **KÖTELEZŐ, MEGVAN** | a jelenlegi tananyag vagy egy kánoni dokumentum kimondja; ez már most kötelező a gyártásra |
| 🟡 **KÖVETKEZETES, DE NEM HIVATALOS** | több lecke ugyanazt használja, de semmilyen kánoni döntés nem nyilvánítja hivatalossá — **javaslat, nem szabály** |
| ⛔ **NINCS BIZONYÍTÉK** | a repositoryban nincs hozzá adat; a döntés emberé (D1) |

---

## 1. A kereséssel megállapított tény

**A döntés előtt a tananyagban nem volt hexadecimális színérték.** A teljes fa átvizsgálva
(Markdown, JSON, Python, YAML; a `_legacy` és a generált kimenetek kivételével) `#RRGGBB`
alakú érték a leckékben, a kánoni szabályokban és a kódban **sehol nem fordult elő**; csak
ennek a mappának négy produkciós dokumentumában állt — az akkor még jóvá nem hagyott
[`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) javaslatban, valamint a rá
épülő `PILOT-PRODUCTION-PACK.md`-ben, `PRODUCTION-STACK.md`-ben és ebben a lapban. Jóváhagyott
design-system fájl, arculati leírás és logó-specifikáció nem volt; betűtípus-név is csak
ezekben a produkciós dokumentumokban szerepelt.

Ez azt jelentette, hogy az R5 hex-palettája jóváhagyott formában nem volt a
repositoryban. **2026-10-02 óta** a hivatalos palettát és a stílus-tokent a kánoni R5
szabály (`produkcios-szabalyok.json`) rögzíti, projektgazdai döntés alapján (lásd fent). A
leckékben továbbra sincs hex-érték: azok szín-szerepet írnak, nem árnyalatot.

> 🔎 **2026-08-27-i kiegészítés: a repositoryn KÍVÜL viszont létezik.** Egy célzott külső
> keresés megtalálta a mozgalom **saját, nyilvánosan elérhető arculati kézikönyvét** és
> logócsomagját (`https://somer.hu/arculat/`), deklarált HEX / RGB / CMYK / Pantone
> értékekkel; a hat alapszín a hivatalos SVG `<style>` blokkjából **byte-azonosan
> megerősítve**. A palettát tehát **nem kell kitalálni — át lehet venni**, ha a
> jóváhagyó így dönt.
>
> A teljes bizonyíték-lánc, a számított kontrasztok és a két változat:
> [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md).
>
> **Ettől az R5 NEM zárul le.** Egy megtalált first-party dokumentum bizonyíték, nem
> szervezeti jóváhagyás: a kézikönyv verzió- és dátumbélyeg nélküli, szerkeszthető Google
> Doc, a `somer.hu` élő oldala pedig még egy **korábbi, eltérő színgenerációt** szállít.
> Amíg a jóváhagyó nem mondja ki, melyik a hatályos, mind a 258 érintett szemantikus asset R5-blokkolója marad.
>
> **2026-10-02:** a projektgazda kimondta (D1-b): a 2022-es kézikönyv és a hivatalos SVG
> színgenerációja a hatályos. Az R5 nyitott értéke ezzel kitöltve; az asset-szintű
> R5-blokkolók kivezetése a manifesztben külön lépés.

## 2. Ami viszont KÖTELEZŐEN megvan

### 2.1. Akadálymentesítési kényszerek — ✅ KÖTELEZŐ, MEGVAN

Forrás: `LMS – hozzáférhetőségi sztenderd.md`. Ezek nem stílus-preferenciák, hanem
mérhető követelmények, és **bármelyik paletta csak akkor fogadható el, ha teljesíti őket**:

- **Szövegkontraszt** (WCAG 2.2 SC 1.4.3, AA): törzsszöveg **≥ 4,5:1**, nagy méretű
  szöveg **≥ 3:1**.
- **Nem-szöveges kontraszt** (SC 1.4.11, AA): a jelentést hordozó grafikai elemek és a
  UI-komponensek szükséges vizuális információja **≥ 3:1** a szomszédos színekhez képest.
- **Projekt-cél a minimum felett** (nem normatív): a kapus elemeknél a lényeges
  UI-kontraszt is 4,5:1 felé, mert „a madrihok jellemzően olcsó kijelzőn, gyenge
  fényben, mozgás közben használják”.
- **A szín soha nem egyedüli információhordozó.** Ezt a leckék asset-jegyzetei
  tucatnyi helyen külön kikötik — például: „ne csak színkódolás különböztesse meg, a betű
  (S/B/I) is jelölje az elemet”; „a megkülönböztetés ne csak színnel (felirat +
  szimbólum is)”; „szín + forma (színvakság-barát)”.

**Következmény a palettára:** minden szemantikus szín mellé **forma vagy betűjel** is
kell, és a paletta minden párosításának át kell mennie a kontraszt-ellenőrzésen — nem
utólag, hanem a lock-lap elfogadásakor.

### 2.2. Szemantikus szín-szerepek — ✅ KÖTELEZŐ, MEGVAN (a szerep; a szerepenkénti márkaszín a pilotban)

A tananyag **mit** jelöl színnel, az rögzített. Az, hogy **melyik hex**, a leckékben nem: a
paletta 2026-10-02 óta kánon (D1), a szerepenkénti márkaszínt a családonkénti pilot
rögzíti (például a [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) P-IKO briefje).

| Család | Szerep | Jelenlegi megnevezés | Assetek |
|---|---|---|---|
| **SBI** | S = Situation | kék, óra + helyszín(pin) ikon | `M1.3-IKO-01`, `M1.4-DIA-01`, `M1.4-IKO-01`, `M1.3-DIA-01` |
| | B = Behavior | zöld, szem/fül ikon | ugyanazok |
| | I = Impact | narancs, szív/hullám ikon | ugyanazok |
| **3 someres pillér** | cionizmus | kék | `M2.3-IKO-01` |
| | szocializmus | piros | |
| | világi humanista zsidóság | zöld | |
| **Kérdéstípusok** | nyitott / zárt / tisztázó / irányító | zöld / kék / sárga / piros | `M4.3-IKO-01`, `M4.3-DIA-01` |
| **Do / Don't** | helyes / kerülendő | zöld / piros | `M3.4-DIA-01`, `M3-HUB-POSZ-02` |
| **M6.4 szekció-ikonok** | 9 szemantikus jelölő | egységes lapos stílus, transzparens, min. 64×64 px | `M6.4-IKO-01` |
| **3 kvuca piktogram** | Parparim / Kivsza / Leviatán | 🦋 🐑 🐋 | `M7.4-IKO-01`, `M3.2-IKO-01` |

> ⚠️ **Az R6 ütközése itt él.** A „kék” egyszerre SBI-S, cionizmus-pillér és „zárt
> kérdés”; a „zöld” egyszerre SBI-B, humanista zsidóság, „nyitott kérdés” és „DO”. Az R6
> szabály pontosan ezt tiltja vagy jelölteti: „ugyanazon alapszín eltérő szemantikai
> újrahasznosítását kerülni vagy explicit jelölni kell”. **A paletta-döntésnek erre
> választ kell adnia** — vagy külön árnyalatokkal, vagy azzal a kimondott döntéssel, hogy
> a kontextus elválasztja őket (moduláris színszótár).
>
> **Feloldva (D1-d, projektgazdai döntés, 2026-10-02):** a szín szemantikája
> modulhatókörű; az elsődleges jel a forma és a felirat (betűjel). A szín soha nem önálló
> jelentéshordozó, ezért ugyanaz a szín más modulban újrahasznosítható. A kánoni helye az R6
> szabály (`produkcios-szabalyok.json`).

### 2.3. Formátum és méret — ✅ KÖTELEZŐ, MEGVAN

A leckék technikai jegyzeteiből, tételenként:

- **Ikon-készletek:** SVG (előnyben) vagy PNG, **átlátszó háttér**, min. 64×64 px,
  H5P-kompatibilis, „retina-méret”.
- **Diagramok:** SVG; mobil-first elrendezés (függőleges lépcsőként is olvasható);
  az animáció mindenhol **opcionális**, a statikus változat mindig megfelel.
- **Videó:** 16:9.
- **Nyomtatványok:** A4 álló az alap; A5 / fél A4 a cédula-méret; A3 / A1 / A2 a
  flipchart és a fali poszter; „távolról olvasható”, „nagy kontrasztos betűtípus”.
- **Nyomtathatóság:** **29 tétel a saját jegyzete szerint fekete-fehérben is
  nyomtatható** (ebből 26 kizárólag fekete-fehér, hue megnevezése nélkül). Ezek a
  hex-palettától **nem** függenek.

### 2.4. Stílus-kikötések — ✅ KÖTELEZŐ, MEGVAN

- **R4 — védjegy-semlegesség:** tilos a Messenger / WhatsApp / Discord / Insta / Moodle
  vizuális nyelvének másolása. Semleges chat-buborék, sztori-kör, LMS-felület.
- **R1 — egységes AI-jelölés:** minden `provenance=AI` asseten **egyetlen kanonikus,
  ember-olvasható AI-címke** kell. A **szöveg 2026-08-27-én jóváhagyva**, szó szerint:
  **„AI-generált médiaelem · emberi lektorálással.”** — rögzítve a `produkcios-szabalyok.json` R1 szabályában, kivezetve a
  tananyag mind a 21 aktív előfordulására, és regressziós teszt őrzi. A címkét külön
  UI-text assetek viszik (`M5.1-EGY-01`, `M6.1-EGY-01`). Ahol a generáló eszköz gépi
  provenance-jelölést ad (C2PA / Content Credentials / vízjel), az export **ne távolítsa
  el**.
- **R5 — egyszer gyártás, újrahasznosítás:** a visszatérő ikon-készletek (SBI 3-szín,
  3-kvuca piktogramok, M6.4 9 szekció-ikon) **egyszer** készülnek közös stílus-tokennel,
  és több helyen újra felhasználódnak. A manifeszt ezt már kikényszeríti: 8 asset
  `mode: reuse`, saját deliverable nélkül.
- **AI karakter-jelenetek:** rögzített referencia-karakterrel és seeddel készülnek
  (`M1.1-VID-02`, `M1.3-VID-01`, `M4.1-VID-03/04/05`), a freeze-frame-ek
  (`M4.1-FOTO-01/02`) a videó-gyártás részeként.
- **Gyermekvédelmi és krízis-HOOK:** a projektgazdai döntés szerint (`HUM-MEDIA-03`,
  2026-10-02) az `M2.4-VID-01`, az `M3.3-VID-01` és az `M3.4-VID-01` nem AI-beszélőfej,
  hanem hangalámondás + kinetikus tipográfia/grafika. Ezért az R5 (stílus-token)
  produkciós szabály rájuk is vonatkozik. Utólagos ellenőrzés (vétó/QA): a
  jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna.
- **Fotó helyett illusztráció, ahol a képmás-kockázat elkerülhető:** ez már **megtörtént
  projektdöntés** az M6.3-ban („DÖNTÉS: illusztráció (GDPR-kockázat elkerülése),
  FOTO→ILL”). A tananyagban ma **két** valós felvétel van összesen
  (`M0.3-FOTO-01` Moodle-képernyőkép, `M0.A-FOTO-01` kvuca-plakát fotók) — minden más
  „fotó” AI-generált vagy illusztráció.

## 3. Ami következetes, de NEM hivatalos

🟡 **A kék / zöld / narancs / piros / sárga alapszavak.** A leckék ezeket használják, és
egymással is konzisztensek (az SBI kék-zöld-narancs például három asseten át azonos).
De **egyetlen kánoni dokumentum sem nyilvánítja őket hivatalos someres színnek**, és
árnyalatot sem ad hozzájuk.

**Javaslat a D1-hez, nem szabály:** ha a paletta-döntés máshova visz, ezeket a
szín-szerepeket kell elsőként újragondolni, mert 6 asset-család épül rájuk. Ha viszont
megmaradnak, akkor a döntésnek csak a konkrét árnyalatot kell hozzájuk rendelnie — a
szerep, az ikon-metafora és az alt-szöveg-megfogalmazás már kész.
→ **2026-10-02:** a hivatalos paletta kánon (D1); a leckék szín-szavaihoz a konkrét
márkaszínt a családonkénti pilot rendeli.

🟡 **A fekete-fehér nyomtatvány mint alapértelmezés.** 29 tétel jegyzete kimondja, hogy
elég a fekete-fehér nyomtatás — ez erős jel arra, hogy a nyomtatott anyagcsalád
**tipográfiára épül, nem színre**. Nincs viszont olyan döntés, ami ezt szabállyá tenné.
→ **2026-10-02 óta szabály:** a D1-ben elfogadott B változat
([`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 7.1.) szerint a fekete-fehér
kompatibilitás minden nyomtatványon kötelező.

## 4. Ami hiányzik — a D1 döntés tárgya

Új bizonyíték-osztály a 2026-08-27-i külső kutatás után:

| | Jelentés |
|---|---|
| 🔎 **KÜLSŐ FORRÁSBÓL MEGVAN** | a mozgalom saját, nyilvános arculati anyaga kimondja; **bizonyíték, nem jóváhagyás** — a jóváhagyónak meg kell erősítenie, hogy ez a hatályos változat |

**2026-10-02 óta minden mező kitöltve** — a D1 projektgazdai döntése alapján (✅). A
korábbi bizonyíték-állapot (🔎 / ⛔) zárójelben marad, nyomon követhetőségért.

| Mező | Állapot | Kire hat |
|---|---|---|
| Someres alap-hex-paletta (elsődleges, másodlagos, akcent) | ✅ **eldőlt** (D1-a, D1-b): `#D84C15` piros, `#F2BC00` sárga, `#87B027` zöld, `#369D37` sötétzöld, `#08A0CA` sötétkék, `#82CDE9` kék; az árnyalatok: [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 1.2. *(korábban: 🔎 megvan — 6 alapszín + 18 árnyalat, HEX/RGB/CMYK/Pantone; jóváhagyásra várt)* | a terv 1C alkötegében jelölt színfüggő tételek + minden színes vizuál |
| Háttér- és szövegszín (világos/sötét) | ✅ **eldőlt** (D1-c, B változat): szöveg `#1D1D1B`, halvány `#5C5C5B`, szerkezeti vonal `#8E8E8D`, dekoratív vonal `#CDCDCD`, felület `#F1F1F1`; sötét módot a döntés nem ír elő *(korábban: 🔎 részben)* | minden vizuál |
| Betűtípus — címsor és törzs | ✅ **eldőlt** (D1-c): **Source Sans 3** (SIL OFL 1.1) a tananyag-produkcióhoz; a betűméret-skála: [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 3.4. A Myriad Pro beágyazási licence így a tananyagot nem érinti *(korábban: 🔎 részben — a kézikönyv betűméret-skálája kitöltetlen)* | mind a 265 R5-tétel |
| Ikon-stílus: vonal vagy kitöltés, vonalvastagság, sarokkerekítés | ✅ **eldőlt**: körvonalas, 24×24-es rács, 2/24 vonalvastagság, kerek vonalvég és -illesztés ([`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 5.) *(korábban: ⛔ a kézikönyv nem rendelkezik róla)* | 40 ikon-készlet |
| Karakter-stílus és rögzített referencia-seed | ✅ **a stílus eldőlt**: lapos vektoros illusztráció, nem fotorealisztikus 3D, generált képben nincs szöveg; a referencia-karakter és a seed rögzítése a karakter-gyártás első lépése ([`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md), P-KAR) *(korábban: ⛔ nincs bizonyíték)* | 6 AI karakter-videó + 2 freeze-frame |
| Logóhasználat, elhelyezés, biztonsági margó | ✅ **eldőlt**: a 2022-es kézikönyv használati tiltásai szerint (nem átszínezni, nem újrarajzolni, nem nyújtani, nem forgatni, effekt és árnyék nélkül); a `#2B2523` csak a logón belül (D1-e). Biztonsági margót és minimális méretet a kézikönyv nem ad meg | poszterek, nyomtatványok |
| Az R6 szín-ütközés feloldása (kék és zöld többes szerepe) | ✅ **eldőlt** (D1-d): a szín szemantikája modulhatókörű, az elsődleges jel a forma és a felirat; a szín soha nem önálló jelentéshordozó *(a kontraszt-mérés szerint a paletta 15 színpárja közül egy sem éri el a 3:1-et, tehát más feloldás nem is működne)* | SBI, 3 pillér, kérdéstípusok, Do/Don't |
| Az AI-jelölés vizuális formája és elhelyezése (a **szövege eldőlt**) | ✅ **eldőlt**: mindig élő LMS-szöveg, nem képbe égetve (ezt a tananyag is kimondja: `M5.1-EGY-01`, `M6.1-EGY-01`); a méret, a szín és az igazítás a [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 7.3. pontja szerint | **329 R1-hatályú asset** (273 `ai` + 56 `mixed`) |

**Amit ez a lap kifejezetten NEM tesz:** nem talál ki hex-értéket, nem nevez meg
betűtípust és nem rögzít logóhasználatot. Ezek szervezeti-arculati döntések; egy kitalált
érték az akkori 258 érintett szemantikus asseten vált volna szabállyá, mielőtt bárki jóváhagyta volna. A
fenti értékeket sem ez a lap találta ki: a megtalált bizonyítékokra és a
[`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) B változatára a projektgazda
2026-10-02-i döntése mondott igent.

## 5. Javasolt zárási sorrend

> **2026-10-02:** a D1 lezárásával az 1. és a 3. lépés egyszerre teljesült; a 2.
> (pilot-jóváhagyás) és a 4. (karakter-lock) lépés a gyártás része maradt.

1. **Stílus-token** (betűtípus, fejléc- és margórend, ikon-vonalstílus, valamint az
   AI-jelölés **megjelenése** — a szövege már eldőlt). Ezzel a **26 kizárólag
   fekete-fehér nyomtatvány** gyártása elindulhat; a manifeszt R5-blokkolója viszont
   csak a teljes R5-zárással kerül le róluk (lásd `PRODUCTION-DECISIONS.md` D1).
2. **Pilot-jóváhagyás** családonként. A pilotokat a terv generálja, ezért a konkrét
   ID-ket mindig ott nézd meg: `MEDIA-PRODUCTION-PLAN.md` 5. szakasz (munkalap, poszter,
   ikon, diagram, illusztráció). Egy döntés lezárása megváltoztathatja, melyik tétel a
   legkevésbé blokkolt, tehát melyik lesz a pilot. A
   [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) briefjei rögzített ID-kre
   készültek, ezért eltérhetnek a terv aktuális pilotjától (a csomag 1. szakasza jelzi).
3. **Hex-paletta + R6 feloldás.** Ezzel indul a színfüggőként jelölt tételek köre és
   minden színes diagram/ikon (a pontos darabszám a terv 4. szakaszának 1C alkötegében).
4. **Karakter-lock** (referencia-karakter és seed). Csak ezután szabad bármelyik
   AI karakter-videót legyártani, különben a jelenetek szereplője leckénként más lesz.

## 6. Elfogadási feltétel

A lock-lap akkor kész, ha:

- [x] minden 4. szakaszbeli mező ki van töltve; *(2026-10-02, D1)*
- [ ] a paletta minden szöveg–háttér párosítása teljesíti a 4,5:1 (nagy szövegnél 3:1)
      arányt, és minden jelentéshordozó grafikai elem a 3:1 arányt;
- [ ] minden szemantikus színhez tartozik **forma vagy betűjel** is;
- [x] az R6 szín-ütközésre van kimondott válasz; *(D1-d)*
- [x] a `produkcios-szabalyok.json` R5 szövegéből kivezethető a nyitott-érték jelölés; *(kivezetve, 2026-10-02)*
- [ ] `python3 tools/media_manifest.py build` lefutott, és a köteg-terv frissült.
