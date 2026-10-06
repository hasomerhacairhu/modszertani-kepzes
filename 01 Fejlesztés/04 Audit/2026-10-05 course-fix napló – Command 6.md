# course-fix napló — Command 6 (2026-10-05)

> **Audit trail, nem kánon.** Bemenet: `2026-10-05 Fix pack – Command 6 – PR-01, PR-02, A11Y-07, A11Y-17 és
> konzisztencia.md` (3. változat). Munkaág: `fix/moodle-build-hardening`. Sorrend a fix pack táblázata szerint (a C6-19
> a C6-11 után). Commit és push nincs.

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| C6-01 | TEXT-C rögzített beállítások (BIZT-4, -3, -11) | `LMS – activity manifest.md` :24 | alkalmazva | |
| C6-02 | TEXT-C mentor-láthatóság cella (BIZT-2 objektív) | `LMS – activity manifest.md` :24 | alkalmazva | a két csere egy horgonnyal, egy Edit |
| C6-03 | RT 15. pont kiegészítése (BIZT-3, -11) | `LMS – H5P runtime acceptance.md` :79 | alkalmazva | |
| C6-04 | PR-01 build-rész alszakasz (A.1) | `Adatvédelem – tanulói adatok és AI.md` §3 | alkalmazva | az A.1 blokk szó szerint egyezik (géppel összevetve) |
| C6-05 | PR-01 checklist kettébontása | `Adatvédelem…` :168 | alkalmazva | |
| C6-06 | PR-02 §11 tájékoztató (A.2) | `Adatvédelem…` §10 után | alkalmazva | az A.2 blokk szó szerint egyezik; a tanulói blokkban 0 jelölő |
| C6-07 | PR-02 checklist kettébontása | `Adatvédelem…` :169 | alkalmazva | |
| C6-08 | kurzusszintű elem: tájékoztató helye | `LMS – activity manifest.md` :114 | alkalmazva | |
| C6-09 | A11Y-07 H5P-C A11y cella | `LMS – activity manifest.md` :16 | alkalmazva | |
| C6-10 | A11Y-07 checklist-átmenet (A.4) | `LMS – hozzáférhetőségi sztenderd.md` :88 | alkalmazva | 3. változat szerinti A.4 szöveg |
| C6-11 | A11Y-07 RT screen-reader pont | `LMS – H5P runtime acceptance.md` | alkalmazva | az RT-A11Y-03 sora és állapota változatlan |
| C6-19 | A11Y-07 environment record sor | `LMS – H5P runtime acceptance.md` | alkalmazva | |
| C6-12 | A11Y-17 kurzusszintű elem (A.3) | `LMS – activity manifest.md` §2 | alkalmazva | az A.3 blokk szó szerint egyezik |
| C6-13 | A11Y-17 checklist kettébontása | `LMS – hozzáférhetőségi sztenderd.md` :113 | alkalmazva | |
| C6-14 | M0 hub ütemezési sor | `M0 – Kickoff, keret, technika.md` :12 | alkalmazva | |
| C6-15 | M1 hub ütemezési sor | `M1 – Vakfolt, tükör, visszajelzés … .md` :6 | alkalmazva | |
| C6-16 | Memuna-felsorolás példálózó jelölése | `Program terv.md` :392 | alkalmazva | |
| C6-17 | Memuna-felsorolás példálózó jelölése | `LMS – activity manifest.md` :200 | alkalmazva | |
| C6-18 | M4.1 modalitássemleges szóhasználat (B.2, 7 csere) | `M4.1 – Mit üzen a testem … .md` SLIDE 4 | alkalmazva | 7 csere (a kártyacímkék `replace_all`, 2-2 előfordulás); a ✅ ugyanazon az opción; a NAR-06-ban és a 2. kérdésben 0 „kép” |

## Záró lépések

- **Pin:** egyetlen pin, 8 fájl.
- **Média-build:** kétszer futott, a kimenet bájtra azonos (ellenőrző összeggel). A `check` OK, a `reconcile` szerint 0 sor nincs egyeztetve.
- **Ellenőrzések:**
  - média-tesztek: 159 OK;
  - `content_integrity`: 0 hiba;
  - `git diff --check`: tiszta, a teljes PR-tartományon is.
- **Release report:**
  - `MOODLE-BUILD-VERDICT: NOT_READY`, csak a `MANIFEST-OPEN 3` (BSPEC-05/06/07) miatt; a `CHECKLIST-BUILD` sor megszűnt;
  - post-build checklist: 12 → 14;
  - release-evidence: 6 → 8;
  - environment record: 17 → 18.

## `/release-check`

A fork tartalmi riport nélkül tért vissza („Skill execution completed”). Ezért a főszálban közvetlenül lefutott:
- checker-selftest: 57/57;
- release report: `MOODLE-BUILD-VERDICT: NOT_READY` (csak BSPEC-05/06/07), `LEARNER-RELEASE-VERDICT: NO-GO`;
- média-`validate` és `lint --high-only`: 0 jelzés.

A governance-ellenőrzések (hook-selftestek, sandbox-próba) ebben a körben nem futottak.

## Célzott újraellenőrzés — a biztonság-jog lencse (csak a módosított sorokon)

**Rendben van:**
- a §11 és a build-rész szó szerint egyezik a fix pack szövegével;
- a Z.4-es és az AI-s kanonikus mondat szó szerint egyezik;
- a tanulói blokkban nincs jelölő;
- a Memuna-jelölés a GK §2 hatókörét nem szűkíti és nem bővíti;
- a nyitott BIZT-tételek nyitva maradtak.

A talált hibák nem kerültek javításra: a parancs csak a fix pack szó szerinti szövegét engedte, ezért a riportba mennek.

| ID | Súly | Hely (`Adatvédelem…`) | Típus | Lényeg |
|---|---|---|---|---|
| C6-BIZT-1 | P1 | :245 | emberi döntés (DPO; BIZT-2, BIZT-5) | a „Ki látja?” csak a mentort és az értékelőt nevezi meg, a Moodle-alapértelmezés szerint viszont többen látnak |
| C6-BIZT-2 | P1 | :241 | objektív | a „nem kér kötelezően: írhatsz fiktív … példát is” azt sugallja, hogy valós gyermekvédelmi vagy egészségügyi ügy beírható; ez a §3 :75-tel és a PT :234-gyel ütközik |
| C6-BIZT-3 | P1 | :239–266 | emberi döntés (DPO, jogi felelős) | a GDPR 13. cikk elemei (adatkezelő, jogalap, érintetti jogok, panasz, címzettek); réteges tájékoztató-e |
| C6-BIZT-4 | P1 | :241, :247–256 | emberi döntés (DPO, Memuna) | hiányzó adatkörök (fórum, H5P-próbálkozás, napló, incidens); a beadandók megőrzési sorának hozzárendelése a §9 :207 szerint nyitott |
| C6-BIZT-5 | P2 | :245 | objektív | a kötelező beadandót és a Z.3 válaszait a mentor mindig elolvassa (MAN :19, :106), a szöveg mást sugall |
| C6-BIZT-6 | P2 | :254 | objektív | „a téma kategóriája” → „a cél kategóriája” (a §5 kanonikus „célkategória” szava) |
| C6-BIZT-7 | P2 | :260 | objektív | a hosszabb megőrzéshez adott hozzájárulásnál hiányzik a 18 év alattiakra vonatkozó gondviselői feltétel (§4) |
| C6-BIZT-8 | P2 | :260, :243 | emberi döntés (DPO, jogi felelős) | a kötelező felvétel önkéntes hozzájárulással; a kiskorú hozzájárulása a nem felvételi célú felhasználáshoz |

## Célzott újraellenőrzés — nyelvi lencse (csak a módosított sorokon)

**Rendben van:** az M4.1 SLIDE 4 módosított soraiban (994–1055) nincs nyelvi hiba, és az Adatvédelem-fájl belső fejlesztői részében (227–237) sincs durva hiba. A talált hibák nem kerültek javításra: a parancs csak a fix pack szó szerinti szövegét engedte, ezért a riportba mennek.

| ID | Súly | Hely | Típus | Lényeg |
|---|---|---|---|---|
| C6-NYELV-1 | P1 | `Adatvédelem…` :241 | emberi döntés (DPO, Memuna) | ugyanaz, mint a C6-BIZT-2: valós ügy beírhatóságát sugallja |
| C6-NYELV-2 | P1 | `Adatvédelem…` :260, :253 | objektív | két minősítő kiesett a forrásból: „a cél teljesüléséig” (§3 :72) és „a terepi megfigyelési jegyzet is” (§3 :69, §5) |
| C6-NYELV-3 | P2 | `Adatvédelem…` :250, :256 | emberi döntés (DPO) | a 24 hónap és a 90 nap kezdőpontja a §3 forrásában sincs rögzítve |
| C6-NYELV-4 | P2 | `Adatvédelem…` :264 | objektív | „Záró visszajelzés” → „Záró képzési visszajelzés”; „A válaszok” → „A képzési visszajelzésre adott válaszaid” (a kanonikus fordulat marad) |
| C6-NYELV-5 | P2 | `Adatvédelem…` :245 | objektív | hiányzó ige: „… értékelőd **látja**, és ő is csak akkor nézi meg **őket** …” |
| C6-NYELV-6 | P2 | M0 hub :12, M1 hub :6 | objektív, de a projektgazda által előírt szöveg | „a központi naptár szerint” → „időpontja / időpontjuk a központi naptár szerint”; a szöveg a projektgazda mintamondatát követi |

## Célzott újraellenőrzés — implementációs lencse (csak a módosított sorokon)

**Rendben van:**
- a checklist-szintaxis és a gate-jelölések helyesek;
- jelöletlen nyitott tétel nincs;
- az A11Y-17 18 leckéje pontosan egyezik az `assetek.csv` videós soraival;
- a sablon-, `embed.php`- és `analysis.php`-tények elsődleges forrásból igazolva.

**Nem ellenőrizte:** a capability-archetípusokat (a fix pack ellenőrizte), az Excel-exportot, a `receivemail`-t, a „Force group mode” viselkedését és az 5.0/5.1 ágakat.

| ID | Súly | Hely | Típus | Lényeg |
|---|---|---|---|---|
| C6-IMPL-1 | P2 | STD :100 (:92) | objektív | A `moodle_page::set_title()` alapból hozzáfűzi a ` \| <oldalnév>` utótagot (`lib/pagelib.php` :1401–1419, `MOODLE_405_STABLE`; a főszálban újra ellenőrizve). A beágyazott dokumentum címe ezért „<H5P-cím> \| <oldalnév>”, és a minta szerinti átvételnél az utótagot le kell vágni. |
| C6-IMPL-2 | P1 | `Adatvédelem…` :125; RT :80 | objektív (döntés átvezetése) | Az RT 15. pontjából hiányzik a D-a…D-d 2. pontjának négy tesztfeltétele: két mentor, két csoport, URL-es hozzáférés, tanuló–tanuló láthatóság. |
| C6-IMPL-3 | P2 | RT :26, :108 | objektív | Az „A11Y-07” összetéveszthető a meglévő, más tesztet jelölő „RT-A11Y-07”-tel. |
| C6-IMPL-4 | P2 | MAN :121 | objektív | Az offline File-erőforrásnak nincs hozzáférési feltétele, így megkerüli a lecke nyitási sorrendjét. Azonos feltétel kell, mint a lecke activityjénél. |
| C6-IMPL-5 | P1 | MAN :120, :122 | emberi döntés (projektgazda, Memuna QA) | Az M2.4 és az M3.3 offline változatában nincs rögzítve a HUM-SAFE-03 blokk és a SAFE-1 passz-kerete. |
| C6-IMPL-6 | P2 | STD :88–89; HUM 11. szakasz | objektív (döntés átvezetése) | Az A11Y-07 2026-10-05-i G5a/G5b-döntése csak a fix pack 0. szakaszában van, a HUM 11. szakaszba nincs átvezetve. |
| C6-IMPL-7 | P2 | `Adatvédelem…` :104 | objektív | A mentor sorában csak a TEXT-C-szűkítés szerepel, holott az ASSIGN és a H5P-C P2-adatait csoporttól függetlenül látja (BIZT-5). |
| C6-IMPL-8 | P2 | MAN :122 | objektív | A 18 offline dokumentumnak nincs megnevezett forrása vagy előállítási útja. |
