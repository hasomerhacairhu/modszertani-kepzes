# 🎨 Vizuális rendszer — produkciós lock-lap

Az R5 produkciós szabály végrehajtási lapja. **Nem arculati kézikönyv:** csak azokat az
értékeket rögzíti, amelyek nélkül a 257 vizuális és nyomtatott asset nem gyártható le
egységesen. Ami már objektíven megvan a tananyagban, azt kimondja; ami hiányzik, azt
nyitottként jelöli, és a [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D1
pontjára mutat.

Három bizonyíték-osztályt tart külön:

| | Jelentés |
|---|---|
| ✅ **KÖTELEZŐ, MEGVAN** | a jelenlegi tananyag vagy egy kánoni dokumentum kimondja; ez már most kötelező a gyártásra |
| 🟡 **KÖVETKEZETES, DE NEM HIVATALOS** | több lecke ugyanazt használja, de semmilyen kánoni döntés nem nyilvánítja hivatalossá — **javaslat, nem szabály** |
| ⛔ **NINCS BIZONYÍTÉK** | a repositoryban nincs hozzá adat; a döntés emberé (D1) |

---

## 1. A kereséssel megállapított tény

**A repositoryban nulla hexadecimális színérték van.** A teljes fa átvizsgálva
(Markdown, JSON, Python, YAML; a `_legacy` és a generált kimenetek kivételével):
`#RRGGBB` alakú érték **sehol nem fordul elő**. Nincs design-system fájl, nincs arculati
leírás, nincs logó-specifikáció, nincs betűtípus-megnevezés.

Ez azt jelenti, hogy az R5 hex-palettája **nem „elveszett”, hanem soha nem is létezett a
repositoryban**. Nem lehet kinyerni; el kell dönteni.

## 2. Ami viszont KÖTELEZŐEN megvan

### 2.1. Akadálymentesítési kényszerek — ✅ KÖTELEZŐ, MEGVAN

Forrás: `LMS – hozzáférhetőségi sztenderd.md`. Ezek nem stílus-preferenciák, hanem
mérhető követelmények, és **bármelyik paletta csak akkor fogadható el, ha teljesíti őket**:

- **Szövegkontraszt** (WCAG 2.2 SC 1.4.3, AA): törzsszöveg **≥ 4,5:1**, nagy méretű
  szöveg **≥ 3:1**.
- **Nem-szöveges kontraszt** (SC 1.4.11, AA): a jelentést hordozó grafikai elemek és a
  UI-komponensek szükséges vizuális információja **≥ 3:1** a szomszédos színekhez képest.
- **Projekt-cél a minimum felett** (nem normatív): a kapus elemeknél a lényeges
  UI-kontraszt is 4,5:1 felé, mert „a madrichok jellemzően olcsó kijelzőn, gyenge
  fényben, mozgás közben használják”.
- **A szín soha nem egyedüli információhordozó.** Ezt a leckék asset-jegyzetei
  tucatnyi helyen külön kikötik — például: „ne csak színkódolás különböztesse meg, a betű
  (S/B/I) is jelölje az elemet”; „a megkülönböztetés ne csak színnel (felirat +
  szimbólum is)”; „szín + forma (színvakság-barát)”.

**Következmény a palettára:** minden szemantikus szín mellé **forma vagy betűjel** is
kell, és a paletta minden párosításának át kell mennie a kontraszt-ellenőrzésen — nem
utólag, hanem a lock-lap elfogadásakor.

### 2.2. Szemantikus szín-szerepek — ✅ KÖTELEZŐ, MEGVAN (a szerep; ⛔ a hex)

A tananyag **mit** jelöl színnel, az rögzített. Az, hogy **melyik hex**, nem.

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
| **4 kvuca piktogram** | Parparim / Kivsza / Leviatan / Zorea | 🦋 🐑 🐋 🌱 | `M7.4-IKO-01`, `M3.2-IKO-01` |

> ⚠️ **Az R6 ütközése itt él.** A „kék” egyszerre SBI-S, cionizmus-pillér és „zárt
> kérdés”; a „zöld” egyszerre SBI-B, humanista zsidóság, „nyitott kérdés” és „DO”. Az R6
> szabály pontosan ezt tiltja vagy jelölteti: „ugyanazon alapszín eltérő szemantikai
> újrahasznosítását kerülni vagy explicit jelölni kell”. **A paletta-döntésnek erre
> választ kell adnia** — vagy külön árnyalatokkal, vagy azzal a kimondott döntéssel, hogy
> a kontextus elválasztja őket (moduláris színszótár).

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
  ember-olvasható AI-címke**, azonos szöveggel és megjelenéssel. A tananyag már megadja a
  szövegét is: „🤖 Ez a videó generatív AI-val készült.” (`M4.1-IKO-01`), és külön
  UI-text assetek viszik (`M5.1-EGY-01`, `M6.1-EGY-01`). Ahol a generáló eszköz gépi
  provenance-jelölést ad (C2PA / Content Credentials / vízjel), az export **ne távolítsa
  el**.
- **R5 — egyszer gyártás, újrahasznosítás:** a visszatérő ikon-készletek (SBI 3-szín,
  4-kvuca piktogramok, M6.4 9 szekció-ikon) **egyszer** készülnek közös stílus-tokennel,
  és több helyen újra felhasználódnak. A manifeszt ezt már kikényszeríti: 7 asset
  `mode: reuse`, saját deliverable nélkül.
- **AI karakter-jelenetek:** rögzített referencia-karakterrel és seeddel készülnek
  (`M1.1-VID-02`, `M1.3-VID-01`, `M4.1-VID-03/04/05`), a freeze-frame-ek
  (`M4.1-FOTO-01/02`) a videó-gyártás részeként.
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

🟡 **A fekete-fehér nyomtatvány mint alapértelmezés.** 29 tétel jegyzete kimondja, hogy
elég a fekete-fehér nyomtatás — ez erős jel arra, hogy a nyomtatott anyagcsalád
**tipográfiára épül, nem színre**. Nincs viszont olyan döntés, ami ezt szabállyá tenné.

## 4. Ami hiányzik — a D1 döntés tárgya

| Mező | Állapot | Kire hat |
|---|---|---|
| Someres alap-hex-paletta (elsődleges, másodlagos, akcent) | ⛔ nincs bizonyíték | 16 kimondottan színfüggő asset + minden színes vizuál |
| Háttér- és szövegszín (világos/sötét) | ⛔ nincs bizonyíték | minden vizuál |
| Betűtípus — címsor és törzs | ⛔ nincs bizonyíték | mind a 257 R5-tétel |
| Ikon-stílus: vonal vagy kitöltés, vonalvastagság, sarokkerekítés | ⛔ nincs bizonyíték | 40 ikon-készlet |
| Karakter-stílus és rögzített referencia-seed | ⛔ nincs bizonyíték | 6 AI karakter-videó + 2 freeze-frame |
| Logóhasználat, elhelyezés, biztonsági margó | ⛔ nincs bizonyíték | poszterek, nyomtatványok |
| Az R6 szín-ütközés feloldása (kék és zöld többes szerepe) | ⛔ döntés kell | SBI, 3 pillér, kérdéstípusok, Do/Don't |
| Az AI-jelölés vizuális formája (a szövege megvan) | ⛔ nincs bizonyíték | 280 AI-eredetű asset |

**Amit ez a lap kifejezetten NEM tesz:** nem talál ki hex-értéket, nem nevez meg
betűtípust és nem rögzít logóhasználatot. Ezek szervezeti-arculati döntések; egy kitalált
érték 257 asseten válna szabállyá, mielőtt bárki jóváhagyta volna.

## 5. Javasolt zárási sorrend

1. **Stílus-token** (betűtípus, fejléc- és margórend, ikon-vonalstílus, AI-jelölés
   megjelenése). Ezzel a **26 kizárólag fekete-fehér nyomtatvány** azonnal indulhat.
2. **Pilot-jóváhagyás** családonként, a
   `MEDIA-PRODUCTION-PLAN.md` 5. szakaszának pilotjain:
   `M6.A-MUNK-02` (munkalap), `M7.B-POSZ-01` (poszter), `M0.2-IKO-02` (ikon),
   `M5.2-DIA-02` (diagram), `M4.2-ILL-03` (illusztráció).
3. **Hex-paletta + R6 feloldás.** Ezzel indul a 16 színfüggő tétel és minden színes
   diagram/ikon.
4. **Karakter-lock** (referencia-karakter és seed). Csak ezután szabad bármelyik
   AI karakter-videót legyártani, különben a jelenetek szereplője leckénként más lesz.

## 6. Elfogadási feltétel

A lock-lap akkor kész, ha:

- [ ] minden 4. szakaszbeli mező ki van töltve;
- [ ] a paletta minden szöveg–háttér párosítása teljesíti a 4,5:1 (nagy szövegnél 3:1)
      arányt, és minden jelentéshordozó grafikai elem a 3:1 arányt;
- [ ] minden szemantikus színhez tartozik **forma vagy betűjel** is;
- [ ] az R6 szín-ütközésre van kimondott válasz;
- [ ] a `produkcios-szabalyok.json` R5 szövegéből kivezethető a nyitott-érték jelölés;
- [ ] `python3 tools/media_manifest.py build` lefutott, és a köteg-terv frissült.
