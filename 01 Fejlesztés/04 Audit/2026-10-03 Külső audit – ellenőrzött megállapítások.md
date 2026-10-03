# Külső audit (2026-10-03, cfeef1e) – ellenőrzött megállapítások

> **Audit trail, nem kánon.** A projektgazda által 2026-10-03-án továbbított külső „mély repository-audit”
> állításait egyenként ellenőriztük a repóban (két read-only verifier-ügynök + git/GitHub-lekérdezés). Az auditot
> nem vettük át készen: minden sor ítélete a lent idézett fájlhelyen alapul. Javítás csak `/course-fix`-szel,
> emberi döntést igénylő kérdésben a projektgazda döntése után.

## Összesítés

| # | Állítás (külső audit) | Ítélet | Ami ténylegesen igaz | Teendő / ki dönt |
|---|---|---|---|---|
| 1 | Valódi voice-source nevek a publikus git-historyban (P0) | **MEGERŐSÍTVE, súlyosabb** | A repo publikus (0 fork). A két forrás-beszélő vezetékneve 4 commitban szerepel a `main`-ről elérhetően, **és mind az 5 GitHub `refs/pull/*/head` ref-ben**; ezeket force push nem tisztítja. Issue- és PR-szövegekben 0 találat. | History rewrite + force push + GitHub Support a PR-refekre és a cache-elt nézetekre — **csak a projektgazda**. Javasolt sorrend: a függő branchek merge-e után, egyetlen menetben; utána mindenki újraklónoz. |
| 2 | Release/pilot állapotmodell ellentmondásos, körkörös (P0) | **RÉSZBEN** (a hurok valós, a repón belül is) | `RELEASE-READINESS.md:87`: a learner pilot „későbbi mérés, nem release-kapu” (egyezik a `Program terv.md:61`-gyel). De `:86` (hat valós terepi peula) nyitott checklist-sor, és a checker `PROGRAM-TRANSFER` blokkolóként számolja (`content_integrity.py:678`, `:730–733`). A terepi peulák az online félév után, valódi kohorsszal történnek (`Terepgyakorlat:9`), valódi madrih viszont release előtt nem kap hozzáférést (`RELEASE-READINESS.md:5`) → hurok. Kontrollált (valódi kohorszos) pilot-állapot a repóban nincs definiálva. A `:6` ráadásul a READY-t a G1–G8-hoz köti, a program-transzfer nem G-kapu. | **Projektgazda / release-felelős:** a program-transzfer release előtti kapu vagy release utáni program-teljesítési tétel? Legyen-e `CONTROLLED_PILOT` állapot? A döntés után a checker módosítása objektív. |
| 3 | „HUM LEZÁRVA” túl erős jelentés (P1) | **RÉSZBEN** | A HUM-fájl fejléce (`:8`) kimondja: a projektgazda döntött, a szerepek ellenőrzése vétó/QA. Azt, hogy a **kapuk ettől nem zártak**, csak a `RELEASE-READINESS.md:23` mondja ki, a HUM-fájl nem. | **Objektív:** a `RELEASE-READINESS.md:23` mondatának átvezetése a HUM-fejlécbe (AF-02). Az állapotgép (PROPOSED → … → RELEASE_APPROVED) bevezetése projektgazdai döntés. |
| 4 | Terepgyakorlat: egyéni kompetenciakapu gyenge (P1) | **MEGERŐSÍTVE** | `Terepgyakorlat – 2. félév.md:52–54`: az átlag ≥1,6 „programmutató, nem egyéni feltétel”; egyéni rubrika-feltétel csak a biztonsági sor ≥1; a soronkénti szintleírások „nyitott feladat”. Az audit következtetése (minden más sor 0 mellett is teljesíthető) igaz; a 6 peula + megfigyelés + átdolgozás külön feltétel. | **Emberi döntés:** a HUM-GOV-01 lezárt; egyéni minimum bevezetése újranyitja (programvezető + módszertani felelős). A szintleírások megírása a módszertani felelős nyitott feladata. |
| 5 | M3.1: Tuckman túl lineáris (P2) | **RÉSZBEN** | `M3.1:258`: „a legtöbb csoport négy fő szakaszon megy át … (plusz van egy ötödik, a lezárás)”; a visszalépés/átfedés sehol nincs kimondva. Az M3.A „irány, nem dogma” mondata (`:425`) viszont a kártyák megoldókulcsára vonatkozik, nem ellentmondás. | **Pedagógiai döntés** (módszertani felelős/lektor): kerüljön-e be egy „szemüveg, nem menetrend” mondat. |
| 6 | M3.A 4.3: 17–19 perc egy 15 perces blokkban (P2) | **MEGERŐSÍTVE** | `M3.A:313` 15 perces blokk; lépések `:391` 2’, `:442` 10’, `:460` 5–7’. A 3 kártyás döntés alkalmazva (`:462`), a percek nem. A repó maga is jelzi (`Emberi jóváhagyás szükséges.md:490`). | **Emberi döntés** (modulgazda): melyik lépés rövidül — az időtartam védett szám. |
| 7 | M5: a kutatási állítások forráslánca gyenge (P2) | **MEGERŐSÍTVE** | `M5.3:122` „A kutatások szerint…”; elsődleges forrás (Dunlosky, Roediger, Karpicke, Cepeda, Bjork) sem a `02 Tervezet/`-ben, sem a `01 Fejlesztés/`-ben nincs. A Dialog Cards és a +72 órás felidézési pont pontos leírása igaz (`:470`, `:475`, `:471`). | **Szerkesztői/pedagógiai döntés:** forrásjegyzék (elsődleges forrásból, nem kitalálva). |
| 8 | Z terhelés: 40–65 vs 70–110 perc (P2) | **RÉSZBEN** | A „70–110” az auditor számítása, a repóban nincs. A `Program terv.md:73` és a Z-hub `:37` már helyesen bontja (Z.4 40–65 + Z.1–Z.3 3×10–15); csak a `Program terv.md:13` összefoglalója hagyja ki a Z.1–Z.3-at. | **Objektív:** a `:73` zárójeles bontásának átvezetése a `:13`-ba (AF-01). Új összeg kimondása a HUM-OPS-01 megfogalmazásán túlmegy → projektgazda. |
| 9 | 2 fős „modified-Angoff panel” túlállítás (P2) | **MEGERŐSÍTVE** | `Program terv.md:277`: „Egyszerűsített modified-Angoff: a Memuna + a módszertani lektor…” — két bíráló. | **Emberi döntés** (Memuna/programvezető): átnevezés „strukturált szakértői küszöb-megállapításra” vagy bővítés. |
| 10 | Média túlméretezett (416/907, 120 jogfüggő) (P1) | **MEGERŐSÍTVE (számok)** | `media_manifest.py stats`: 416 asset, 907 deliverable, ai 279, pending-rights 120, R2 119, R3 117. A fallback-szabály létezik (`RELEASE-MEDIA-STATUS.md:53`, `:61`, `:74`), de a nyomtatott segédlet nem fallback, hanem saját médiaosztály (`:73`), és a §3-fallbackek csak az M0+M1 stagingre vonatkoznak. | **Projektgazda / producer:** média-MVP és scope-freeze. |
| 11 | Issue-tracker drift (#6) (P3) | **MEGERŐSÍTVE** | A #6 lezárt, 4 kipipálatlan és 2 kipipált elfogadási feltétellel. | Javasolt: a kipipálatlan feltételek `SUPERSEDED`-jelölése a felváltó döntés linkjével (GitHub-szerkesztés, jóváhagyással). |
| 12 | `content_integrity.py` monolit (P3) | **MEGERŐSÍTVE** | 1009 sor. | Későbbi refaktor; most nem. |
| 13 | Adatvédelem/AI: `store=false` ≠ ZDR | **MEGERŐSÍTVE, a repó helyes** | `Adatvédelem:139`, `:152`, `M7.2:24`: ZDR csak „ha a szervezet számára elérhető”, abszolút megőrzési ígéret nincs; egyik `store=false` hely sem állít nulla megőrzést. | Nincs teendő. |
| 14 | Akadálymentesség: húzás-alternatíva (WCAG 2.5.7) | **MEGERŐSÍTVE** | `LMS – hozzáférhetőségi sztenderd.md:30`, nyitott ellenőrzés `:108`. | Nincs új teendő (runtime-teszt a #3/#4 része). |
| 15 | Neuromítoszok nincsenek | **MEGERŐSÍTVE** | VARK/tanulási stílus, agyfélteke, Mehrabian, figyelmi mítoszok, tanulási piramis: 0 találat a `02 Tervezet/`-ben. | Nincs teendő. |
| 16 | CI-eredmények (49/49, 0 ERROR, 148 teszt, NO-GO 6 blokkolóval) | **MEGERŐSÍTVE** | Helyben újrafuttatva ugyanez. | — |

Az audit 24. pontjával egyetértünk: nem indítunk újabb általános „nézd át és javíts mindent” menetet; a hátralévő
munka célzott lezárás (history, állapotmodell, terepi értékelés, szakértői bizonyíték, runtime).

## Objektív javítások (`/course-fix`-bemenet)

### AF-01 — Z-terhelés az összefoglalóban

- **ID:** AF-01 (külső audit 18. pont; HUM-OPS-01)
- **fájl:** `02 Tervezet/Program terv.md`
- **hely:** L13 (bevezető összefoglaló)
- **probléma:** Az összefoglaló a Z online részét 40–65 percnek mondja, a Z.1–Z.3 mikroleckék 3×10–15 percét kihagyja, holott ugyanez a dokumentum (L73) és a Z-hub (L35–37) kiírja.
- **bizonyíték:** L13: „a **Z** online része **40–65 perc**, a terepi rész külön (részletesen: 1. szakasz)”; L73: „a Z online része 40–65 perc (a Z.4 záró produktum), a Z.1–Z.3 mikroleckék további 3×10–15 percet adnak; a terepi rész külön”
- **javítás:** L13-ban `a **Z** online része **40–65 perc**, a terepi rész külön` → `a **Z** online része **40–65 perc** (a Z.4 záró produktum), a Z.1–Z.3 mikroleckék további 3×10–15 percet adnak; a terepi rész külön`
- **javítási korlát:** csak a L73 meglévő szövegének átvezetése; új összeg (70–110) nem kerül be; a HUM-OPS-01 „40–65 perc” megfogalmazása marad. Látható szöveg → `--pin-visible`.

### AF-02 — „Lezárt döntés ≠ zárt kapu” a HUM-fájlban

- **ID:** AF-02 (külső audit 7. pont)
- **fájl:** `02 Tervezet/Emberi jóváhagyás szükséges.md`
- **hely:** L8 (fejléc, „2026-10-02 – projektgazdai döntések” bekezdés)
- **probléma:** A fejléc szerint a tételek lezártak, de azt, hogy a release-kapuk ettől még nem zártak, csak a `RELEASE-READINESS.md:23` mondja ki; a HUM-fájlt önmagában olvasva a „LEZÁRVA” bizonyított lezárásnak tűnik.
- **bizonyíték:** HUM L8: „A tételek lezártak (dátum, jóváhagyó és bizonyíték a `tools/content_integrity.py` lezárási szabálya szerint).”; RELEASE-READINESS L23: „A kapuk ettől még nem zártak: mindegyik csak a táblázat „Bizonyíték” oszlopa szerinti bizonyítékkal és a tracker-issue-ban rögzített lezárással zárul (lásd: GitHub release-tracker).”
- **javítás:** a L8 bekezdés végére: ` A release-kapuk ettől még nem zártak: mindegyik csak a `RELEASE-READINESS.md` táblázatának „Bizonyíték” oszlopa szerinti bizonyítékkal és a tracker-issue-ban rögzített lezárással zárul.`
- **javítási korlát:** a kánoni mondat átvezetése (a „táblázat” helyett a forrásfájl megnevezésével); a tételek státusza, jóváhagyója és a vétó/QA-szabály nem változik. Látható szöveg → `--pin-visible`.
