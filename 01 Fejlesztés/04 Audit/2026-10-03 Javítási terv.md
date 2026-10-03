# Javítási terv (2026-10-03)

> **Audit trail, nem kánon.** Forrás: `2026-10-03 Külső audit – ellenőrzött megállapítások.md` (a külső audit
> repóban ellenőrzött állításai) és a VO 2. fázis nyitott lépései. A terv a sorrendet, a döntéshozót, a
> végrehajtót és az elfogadási feltételt rögzíti; javaslatai **nem döntések**. Végrehajtás csak a repó szabályai
> szerint: tartalom `/course-fix` / `/course-develop` / `/hungarian-edit`, a projektgazda döntése után.

## Elvek

1. **Nincs újabb általános „nézd át és javíts mindent” menet.** A hátralévő munka célzott lezárás.
2. **Előbb döntés, aztán végrehajtás.** Ahol a tétel emberi döntés, a terv csak ajánlást ad.
3. **Bizonyíték a végállapot visszaolvasása**, nem a záró riport (CLAUDE.md „Nincs hamis készjelentés”).
4. **A history-tisztítás az utolsó git-művelet egy hullámban:** minden függő branch merge-e után, mert minden
   későbbi commit SHA-ja megváltozik.

## Áttekintés

| Lépés | Tétel | Prioritás | Döntéshozó | Végrehajtó | Függ |
|---|---|---|---|---|---|
| 0.1 | VO 2. fázis fix pack (CF-01…CF-106) + AF-01, AF-02 | — | lezárt (D-01…D-23, 2026-10-03-A/B) | projektgazda indítja a `/course-fix`-et; Claude végrehajt | — |
| 0.2 | PR-ek: governance + VO/audit-javítás, merge | — | projektgazda (merge-mód) | Claude PR-t nyit kérésre | 0.1 |
| 0.3 | Issue-higiénia (#6 elfogadási feltételei) | P3 | projektgazda (jóváhagyás) | Claude (`gh`) | — |
| 1 | **Git-history adatvédelmi tisztítás** | **P0** | projektgazda | **csak a projektgazda** | 0.2 |
| 2 | **Release-állapotmodell (pilot ↔ program-transzfer hurok)** | **P0** | projektgazda / release-felelős | `/course-fix` + Claude (checker + teszt) | — |
| 3 | HUM-állapotszemantika | P1 | — (AF-02 objektív) | a 0.1 része | 0.1 |
| 4 | **Terepgyakorlat egyéni kompetenciakapu** | **P1** | programvezető + módszertani felelős | módszertani felelős (szintleírás) → `/course-fix` | — |
| 5 | Tartalmi pontjavítások (M3.A, Tuckman, M5-források, Angoff) | P2 | modulgazda / módszertani felelős / Memuna | `/course-fix`, a forrásjegyzékhez `/course-develop` | — |
| 6 | Média-MVP, scope-freeze | P1 | projektgazda + producer | Claude (szabály + manifeszt) | — |
| 7 | Külső bizonyítékok (#1–#4, a11y) | P0 a pilothoz | Memuna, DPO/jogi, LMS-gazda, a11y-felelős | emberek; Claude csak előkészít | 2 |
| 8 | Karbantartás (checker-modularizálás, governance-követés) | P3 | — | Claude | 2 |

## 0. Folyamatban lévő lezárás

**0.1 — `/course-fix`.** Bemenet: a VO QA-repó `reports/phase2/course-fix-pack.md` fájlja és az AF-01/AF-02.
Elfogadás: `media_manifest.py build` kétszer stabil, `check`, `reconcile` (747/747), `validate`, `lint --high-only`,
`content_integrity` 0 ERROR, 150 teszt OK, egyetlen `--pin-visible` indoklással, `git diff --check origin/main`
tiszta, a teljes diff visszaolvasva; a VO QA-repó extraktora és időzítés-ellenőrzése (nincs OVER) zöld; a
kurzusba kerülő szövegben 0 hangnév. Commitok: `fix(copy)`, `docs(media)`, `test(media)`, külön `chore(media)`
rebuild. Utána: a 2. fázis záró riportja (A–L).

**0.2 — PR-ek.** `governance/actualize-2026-10-03` és a rá épülő `vo/phase2-course-fix`. Push és merge
csak kérésre; merge commit ajánlott (megőrzi a tematikus commitokat). Push előtt a VO QA-repó névellenőrzője
(`tools/check-course-push.py`) fut. A helyi `superseded/*` branchek nem pusholhatók; a projektgazda törli őket.

**0.3 — Issue-higiénia.** A #6 négy kipipálatlan elfogadási feltétele (HUM-SOMER-01, HUM-SOMER-03, az
átvezetés és a jóváhagyási bizonyíték) `SUPERSEDED` jelölést kap a felváltó projektgazdai döntés (2026-10-02,
`Emberi jóváhagyás szükséges.md` HUM-SOMER-01–03, PR #12) linkjével; a mozgalmi felelős utólagos ellenőrzése
vétó/QA marad. Általános szabály a governance-be: issue csak akkor zárható, ha
minden feltétel `[x]`, vagy indoklással és linkkel `SUPERSEDED` / `N/A`.

## 1. P0 — Git-history adatvédelmi tisztítás (csak a projektgazda)

**Tény:** a két forrás-beszélő valódi neve 4 commitban szerepel (első: 17b2b6c, 2026-08-28) a publikus `main`-ről
elérhetően, és mind az 5 `refs/pull/*/head` ref-ben. Issue- és PR-szövegekben nincs.

**Runbook (a 0.2 merge után):**
1. Mentés: `git bundle create ../modszertani-kepzes-before-rewrite.bundle --all` (repón kívül, korlátozott helyen).
2. Kifejezésfájl **a repón kívül** (pl. `~/private/names.txt`): a nevek minden írásmódja (ékezettel, ékezet
   nélkül, kis-/nagybetűvel, birtokos és ragozott alakok) → `***REMOVED***` vagy `VOICE-SRC-01/02`.
3. Friss tükörklónon: `git filter-repo --replace-text ~/private/names.txt` (az összes ref-en).
4. Ellenőrzés: minden változatra `git log --all -S"<név>"` = 0; `git grep` a teljes historyn.
5. Force push a `main`-re; a stale távoli branchek (`audit/final-2026-10-01`) törlése.
6. **GitHub Support:** a `refs/pull/*` (PR #1–#12 head-jei) és a cache-elt commit-nézetek tisztítása —
   force push ezeket nem éri el (GitHub „Removing sensitive data from a repository” eljárás).
7. Minden gépen újraklónozás (a régi klónok és branchek — a két `superseded/*` is — eldobandók).
8. **SHA-hivatkozások frissítése** a `filter-repo` commit-map alapján: a CLAUDE.md (`43fd22a`), a
   `.claude/rules/course-content.md` (`450fef7`), az audit trail és a VO QA-repó dokumentumai rövid SHA-kat
   idéznek, amelyek megváltoznak. A CI és a média-tesztek kiindulási commitja (`a8629732…`) **nem** változik
   (régebbi az első érintett commitnál — ellenőrizve).
9. Teljes CI-futás a tisztított `main`-en.

**Elfogadás:** 0 találat minden névváltozatra az összes ref-en; GitHub Support visszaigazolása; zöld CI; a
commit-map régi SHA-i nem fordulnak elő a repóban.

## 2. P0 — Release-állapotmodell

**Tény:** a learner pilot „nem release-kapu” (`RELEASE-READINESS.md:87`), de a hat valós terepi peula
(`:86`) nyitott release-blokkoló (`PROGRAM-TRANSFER`, `content_integrity.py:678`); a terepi peulákhoz valódi
kohorsz kell, valódi madrih viszont release előtt nem kap hozzáférést (`:5`) → hurok. Kontrollált, valódi kohorszos
pilot-állapot nincs definiálva; a `:6` a READY-t a G1–G8-hoz köti, a program-transzfer nem G-kapu.

**Döntés (D-R1, projektgazda / release-felelős) — ajánlás:** három állapot.

| Állapot | Ki férhet hozzá | Blokkolja |
|---|---|---|
| `INTERNAL_STAGING` | stáb, QA, szintetikus adat | objektív integritási hiba |
| `CONTROLLED_PILOT` | korlátozott valódi kohorsz | G1 (gyermekvédelem), G2 (adatvédelem), runtime acceptance, Moodle-build, a11y P0 |
| `GENERAL_RELEASE` | normál működés | a fentiek + program-transzfer (6 terepi peula + pilot-findingek javítva) + média-kapuk |

**Végrehajtás a döntés után:** `RELEASE-READINESS.md` (állapottábla; a `:86` a `GENERAL_RELEASE` alá; a `:6`
pontosítása), `Program terv.md:61`, `:366`, a #9 issue szövege („a `GENERAL_RELEASE`-et blokkolja, a pilotot
nem”); `content_integrity.py`: a `release_verdict` kiegészül pilot-készültséggel (`PILOT_READY`), a
`PROGRAM-TRANSFER` csak a `GENERAL_RELEASE`-et blokkolja — teszttel és selftesttel; a `/release-check` és a
README szövege. **Elfogadás:** a release-report külön sorban mondja a pilot- és a general-release-állapotot;
a hurok megszűnt.

## 3. P1 — HUM-állapotszemantika

Az AF-02 (a 0.1 része) a HUM-fejlécbe hozza: a lezárt döntés nem zárt kapu. Külön állapotgép (PROPOSED → … →
RELEASE_APPROVED) **most nem ajánlott**: a kapu-bizonyíték állapotát a `RELEASE-READINESS.md` G-táblázata már
viseli; a 2. lépés állapotmodellje után érdemes újranézni.

## 4. P1 — Terepgyakorlat: egyéni kompetenciakapu

**Tény:** egyéni rubrika-feltétel csak a „biztonság és határtartás” ≥ 1; az átlag ≥ 1,6 programmutató; a
soronkénti 0/1/2 szintleírás a módszertani felelős nyitott feladata (`Terepgyakorlat – 2. félév.md:52–54`, `:61`).

1. **Szintleírások** (módszertani felelős; Claude vázlatot készíthet jóváhagyásra) a kilenc sorra: cél és
   alignment; instrukció/keretezés; kvuca-reakciók megfigyelése; facilitálás és kérdezés; idő/tér adaptáció;
   inkluzivitás; biztonság és határtartás; visszajelzés felhasználása; reflektív javítás — viselkedéssel
   lehorgonyzott (BARS) leírásokkal.
2. **Döntés (D-F1, programvezető + módszertani felelős; a HUM-GOV-01-et újranyitja) — ajánlás:** a biztonsági sor
   minden megfigyelt alkalmon ≥ 1 (nem kompenzálható); a végső értékelésen a kulcssorokon (cél és alignment,
   facilitálás és kérdezés, reflektív javítás) nem maradhat 0; az 1,6 programmutató marad. Új százalékos egyéni
   küszöb **csak** a szintleírások kipróbálása után.
3. **Végrehajtás:** `Terepgyakorlat – 2. félév.md:52–61`, `Program terv.md:444`, a HUM-GOV-01 újranyitása és
   lezárása, a rubrika-sablon. **Elfogadás:** a „mindenhol 0, biztonság 1” eset nem teljesít.

## 5. P2 — Tartalmi pontjavítások (mindegyik kis döntés, utána `/course-fix`)

| Tétel | Tény | Ajánlás | Döntéshozó |
|---|---|---|---|
| **5.1** M3.A 4.3 blokk | 2′ + 10′ + 5–7′ = 17–19′ egy 15 perces blokkban; a 3 kártyás döntés alkalmazva, a percek nem | 2′ + **8′** kiscsoportos munka + **5′** közös átbeszélés (3 kártya) = 15′; a 45 perces peula marad | modulgazda |
| **5.2** M3.1 Tuckman | „a legtöbb csoport négy fő szakaszon megy át” (`:258`, összefoglaló `:804`); visszalépés nincs kimondva | egy mondat a `:258` után: „A modell szemüveg, nem menetrend: egy valódi csoport visszaléphet, átugorhat szakaszt, és egy helyzet többféleképpen is olvasható.” A kvíz (`:749`) marad | módszertani felelős |
| **5.3** M5 forráslánc | „A kutatások szerint…” (`M5.3:122`), elsődleges forrás sehol | képzői/módszertani forrásjegyzék (állításcsaládonként 1–3 elsődleges vagy meta-forrás, pl. a gyakorlás/felidézés/elosztott gyakorlás irodalmából), a leckében csak hivatkozás; minden tételt `/course-develop` közben az eredeti publikációval kell igazolni — kitalált hivatkozás nem kerülhet be | módszertani felelős |
| **5.4** Angoff | „Egyszerűsített modified-Angoff: a Memuna + a módszertani lektor” (`Program terv.md:277`) | átnevezés: „strukturált szakértői küszöb-megállapítás (Angoff-elemekkel)”, a pilot itemadataival utólagos kalibráció; bővítés opcionális | Memuna + programvezető |

## 6. P1 — Média-MVP és scope-freeze

**Tény:** 416 asset / 907 deliverable, 120 jogfüggő, R2 119, R3 117; a fallback-szabály csak az M0+M1 stagingre
vonatkozik, a nyomtatott segédlet saját médiaosztály. **Döntés (D-M1, projektgazda + producer) — ajánlás:** három
gyártási fázis — **A:** szöveg + natív H5P + segédlet + diagram + alt-szöveg; **B:** a pedagógiailag indokolt
narráció + felirat + leirat (a VO 2. fázis ezt készíti elő); **C:** videó, avatar, márkás csiszolás csak ott, ahol a
tanulási funkció igazolt. **Végrehajtás:** gyártási szabály (`produkcios-szabalyok.json`) és a manifeszt
fázismezője, a `MEDIA-PRODUCTION-PLAN` sorrendje; a G8 gyártási keret ehhez igazodik.

## 7. Külső bizonyítékok (a `CONTROLLED_PILOT` feltételei)

| Issue / kapu | Kell | Claude szerepe |
|---|---|---|
| #1 gyermekvédelem (G1) | a Memuna írásos „átnéztem”-je (M3.3, M3.B, M3-kapu, M7), élő kontakt a tanulói felületen, release-napi segélyvonal-ellenőrzés | ellenőrzőlista és jegyzőkönyv-sablon; **nem pipál** |
| #2 adatvédelem (G2) | adatvédelmi tájékoztató, aktivitásszintű adatleltár, szerepkör-teszt Moodle-ban, törlési/megőrzési folyamat, kiskorúak jogalapja, AI-konfiguráció bizonyítéka, DPO/jogi jóváhagyás | adatleltár-vázlat a manifesztből |
| #3 runtime, #4 Moodle-build | cél-Moodle/H5P build, 17 runtime-teszt, 52 build-kimenet | tesztforgatókönyvek, eredményrögzítés |
| a11y (HUM-A11Y-01) | 19 ellenőrzési pont renderen (billentyűzet, képernyőolvasó, nagyítás, mobil, húzás-alternatíva, autoplay) | ellenőrzési jegyzőkönyv-sablon |

## 8. P3 — Karbantartás

- `content_integrity.py` (1009 sor) modulokra bontása **a 2. lépés után** (az a release-logikát érinti):
  struktúra / tartalom / release / biztonság, külön tesztekkel; nem második linter.
- Governance-követés: a 2026-10-03-i governance-ellenőrzés nyitott tételei (külön lista a záró riportban).

## Döntési lista (összesítve)

| ID | Kérdés | Ajánlás | Döntéshozó |
|---|---|---|---|
| D-R1 | Release-állapotmodell | 3 állapot; a program-transzfer csak a `GENERAL_RELEASE`-et blokkolja | projektgazda / release-felelős |
| D-F1 | Terepgyakorlat egyéni minimuma | biztonság ≥ 1 minden alkalmon + nincs 0 a három kulcssoron; előbb szintleírások | programvezető + módszertani felelős |
| D-C1 | M3.A 4.3 percei | 2′ + 8′ + 5′ | modulgazda |
| D-C2 | Tuckman-mondat | igen, a javasolt egy mondattal | módszertani felelős |
| D-C3 | M5 forrásjegyzék | igen, ellenőrzött elsődleges forrásokkal | módszertani felelős |
| D-C4 | Angoff megnevezése | átnevezés + utólagos kalibráció | Memuna + programvezető |
| D-M1 | Média-MVP | A/B/C fázisok | projektgazda + producer |
| — | #6 `SUPERSEDED`-jelölés | igen | projektgazda |
| — | History rewrite indítása | a 0.2 merge után | projektgazda |
