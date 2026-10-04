# course-fix napló — BSPEC-01…04 (2026-10-04)

> **Audit trail, nem kánon.** A `/course-fix` futásának lépésenkénti naplója. Bemenet: a négy build-spec finding
> (`2026-10-04 Release-modell v2 – Moodle build és learner release.md`, 11. pont). Döntési források: Q-REL-2, RM-D6
> (`Emberi jóváhagyás szükséges.md` 10. szakasz), HUM 6. szakasz. Bázis: `24cc091`, munkaág `fix/moodle-build-hardening`.
> Rövidítések: M = `02 Tervezet/LMS – activity manifest.md`, RA = `02 Tervezet/LMS – H5P runtime acceptance.md`.

## Elsődleges források a mechanizmusokhoz (lekérdezve 2026-10-04)

- Core restrict access feltételek (activity completion, date, grade, group/grouping, user profile, restriction set):
  `docs.moodle.org/502/en/Restrict_access_settings`.
- Az „Activity completion: must be marked complete” feltétel a „complete, fail” állapotot **nem** fogadja el
  (`moodle/moodle`, `availability/condition/completion/classes/condition.php`, `main` és `MOODLE_405_STABLE`).
- A „Grade” feltétel alsó és felső határ nélkül bármely beírt értékkel teljesül, érték nélkül nem
  (`availability/condition/grade/classes/condition.php`).
- Assignment beadási típus nélkül, csak értékelésre: core (`docs.moodle.org/502/en/Using_Assignment`).
- „Receive a grade” + beállított grade to pass + nem rejtett grade item: bukó értéknél „complete, fail”, átmenőnél
  „complete, pass” (`lib/completionlib.php`).
- `availability_relativedate` („Restriction by relative date”): van „after the completion of an activity” alap,
  tanulónként; a kódja a completion-rekord módosítási idejét veszi, az állapotot nem vizsgálja. Kiadások
  (`version.php` a plugin hivatalos repójában): v4.4.2 → Moodle 4.3–4.5; v5.4.2 → 5.0–5.1; v5.7.2 (2026-09-29) →
  5.1–5.2.

## Eltérés a findingtól

- **BSPEC-02:** a finding érintett sorai közül kimaradt az **M4.3** (LMS-M4-03), pedig a leckéje kötelező szabad
  szöveges mezőt ír elő (M4.3 :20 „a záró reflektív **szabad szöveges válasz** kitöltve”; :615 „1 szabad szöveges
  mező (kötelező)”), és a manifest-sora completionje „mini-kvíz + reflexió”. A finding javaslata „mezőnként”
  szól; nélküle a BSPEC-02 `BUILD_SPEC_RESOLVED` állapota hamis zöld volna. A lépései: S17–S19.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| S01 | BSPEC-01: GATE-CP profil a §1-be | M | alkalmazva | skála a Program terv §5 címkepárjával; Grade to pass = „Teljesítve” |
| S02 | BSPEC-01: LMS-M1-06 sor | M | alkalmazva | küszöb szó szerint az LMS-M1-05 sorából |
| S03 | BSPEC-01: LMS-M3-07 sor | M | alkalmazva | küszöb szó szerint az LMS-M3-05/06 sorából |
| S04 | BSPEC-01: LMS-M5-08 sor | M | alkalmazva | küszöb szó szerint az LMS-M5-05 sorából |
| S05 | BSPEC-01: LMS-M6-07 sor | M | alkalmazva | küszöb szó szerint az LMS-M6-05 sorából |
| S06 | BSPEC-01: LMS-M7-08 sor | M | alkalmazva | küszöb szó szerint az LMS-M7-06/07 sorából |
| S07 | BSPEC-01: §4 „Fontos” — a checkpoint mechanizmusa és tartalékútja | M | alkalmazva | „Mx megerősítve”: Grade-feltétel határ nélkül; „Mx complete”: pass grade; tartalék: Group |
| S08 | BSPEC-01: nyilvántartás → `BUILD_SPEC_RESOLVED` | M | megállva: részben alkalmazva | a célzott újraellenőrzés után visszaállítva `BUILD_SPEC_OPEN`-re: a Group-tartalékút a HUM-PRIV-01-gyel nem állítható be (IMPL-3, BIZT-2); az LMS-M7-08 kitöltése bukott kvíznél nyitott (IMPL-4) |
| S09 | BSPEC-02: TEXT-C profil a §1-be | M | alkalmazva | Assignment, csak online szöveg (hozzáférhetőségi sztenderd §6, 1. út) |
| S10 | BSPEC-02: §2 bevezető — alapértelmezett út | M | alkalmazva | |
| S11 | BSPEC-02: LMS-M2-06 sor | M | alkalmazva | az S12-vel egy `Edit`-ben (közös horgony) |
| S12 | BSPEC-02: LMS-M2-02 unlock → LMS-M2-06 | M | alkalmazva | az S11-gyel egy `Edit`-ben |
| S13 | BSPEC-02: LMS-M4-01 completion → LMS-M4-06 | M | alkalmazva | |
| S14 | BSPEC-02: LMS-M4-06 sor | M | alkalmazva | |
| S15 | BSPEC-02: LMS-M4-02 unlock és completion | M | alkalmazva | az S16-tal egy `Edit`-ben |
| S16 | BSPEC-02: LMS-M4-07 sor | M | alkalmazva | az S15-tel egy `Edit`-ben |
| S17 | BSPEC-02 (kiterjesztés): LMS-M4-03 completion → LMS-M4-08 | M | alkalmazva | az S18–S19-cel egy `Edit`-ben |
| S18 | BSPEC-02 (kiterjesztés): LMS-M4-08 sor | M | alkalmazva | M4.3 :615 „két mondatot várunk” |
| S19 | BSPEC-02 (kiterjesztés): LMS-M4-04 unlock → LMS-M4-08 | M | alkalmazva | |
| S20 | BSPEC-02: LMS-Z-06 sor | M | alkalmazva | a Z.3 három kötelező mezője |
| S21 | BSPEC-02: RA 6. pont — alapértelmezett út | RA | alkalmazva | |
| S22 | BSPEC-02: RA 12. pont — hely és completion-kötés | RA | alkalmazva | |
| S23 | BSPEC-02: nyilvántartás → `BUILD_SPEC_RESOLVED` | M | megállva: részben alkalmazva | a célzott újraellenőrzés után visszaállítva `BUILD_SPEC_OPEN`-re: az M4.4 :26 kötelező mezője kimaradt (IMPL-1, a fájlban igazolva), és completionhöz kötött szabad szöveg van az M2.3-ban (RA 10), az M3.1 :686-ban és az M3.2 :747-ben is; az online szöveg képbeágyazása az M2.1 korlátját gyengíti (BIZT-1) |
| S24 | BSPEC-03: LMS-M5-07 sor (típus, út, tartalékút) | M | alkalmazva | H5P-C: a sor completionje interakció (§1); a plugin-kiadások a hivatalos repóból |
| S25 | BSPEC-03: §7 „További ütemezett pontok” — tartalékút | M | alkalmazva | |
| S26 | BSPEC-03: nyilvántartás → `BUILD_SPEC_RESOLVED` | M | alkalmazva | maradék: a tartalékút tanulói mondata az M5.3-ban hiányzik (jelentés, nyitott finding) |
| S27 | BSPEC-04: LMS-M2-01 unlock | M | alkalmazva | „M1 megerősítve” |
| S28 | BSPEC-04: LMS-M3-05 unlock | M | alkalmazva | + „M1 complete” |
| S29 | BSPEC-04: LMS-M4-01 unlock | M | alkalmazva | „M3 megerősítve” |
| S30 | BSPEC-04: LMS-M5-05 unlock | M | alkalmazva | + „M3 complete” |
| S31 | BSPEC-04: LMS-M6-01 unlock | M | alkalmazva | „M5 megerősítve” |
| S32 | BSPEC-04: LMS-M6-05 unlock | M | alkalmazva | + „M5 complete” |
| S33 | BSPEC-04: LMS-M7-01 unlock | M | alkalmazva | „M6 megerősítve” |
| S34 | BSPEC-04: LMS-M7-07 unlock | M | alkalmazva | + „M6 complete” |
| S35 | BSPEC-04: LMS-Z-01 unlock | M | alkalmazva | „M7 megerősítve” |
| S36 | BSPEC-04: §4 M1 sor | M | alkalmazva | |
| S37 | BSPEC-04: §4 M3 sor | M | alkalmazva | |
| S38 | BSPEC-04: §4 M5 sor | M | alkalmazva | |
| S39 | BSPEC-04: §4 M6 sor | M | alkalmazva | |
| S40 | BSPEC-04: §4 M7 sor | M | alkalmazva | |
| S41 | BSPEC-04: §4 Z sor — az M7 complete kifejezetten | M | alkalmazva | a régi láncban a Z nyitása hozta; most kimondva |
| S42 | BSPEC-04: §7 kiegészítő naptár — a Z nyitása | M | alkalmazva | csak a premissza; az egyéni ütemezés marad |
| S43 | BSPEC-04: RA 8. pont — a negatív eset következménye | RA | alkalmazva | |
| S44 | BSPEC-04: nyilvántartás → `BUILD_SPEC_RESOLVED` | M | alkalmazva | |

**Fájlcsoport vége (az S08/S23 visszaállítása előtt):** `content_integrity.py` 0 ERROR; `git diff --check` tiszta;
a `BUILD-OUTPUT` 52 → 62 (10 új activity-sor); `MOODLE-BUILD-VERDICT: NOT_READY`.

## Célzott újraellenőrzés (2026-10-04) — nem validált findingok, a következő körhöz

Két read-only reviewer a diff-hunkokon (implementation-reviewer, safety-policy-reviewer). Verifier nem futott, ezért ezek
nem validált findingok. A skill szerint jelentésbe kerülnek, nem újabb javításba. Kivétel: az S08 és az S23 saját,
bizonyítottan hamis „megoldva” állapotát a futás visszavonta (lásd fent).

| ID | P | Típus | Lényeg |
|---|---|---|---|
| IMPL-1 | P1 | objektív | az M4.4 kötelező szabadszöveg-mezőjének nincs TEXT-C sora (M4.4 :26); a fő session szerint az M2.3, M3.1, M3.2 is érintett → leltár |
| IMPL-2 | P1 | objektív | az RA 8 záró bekezdése a checkpointot még feltételesnek veszi; nincs teszteset az „Mx megerősítve” / „Mx complete” feltételre |
| IMPL-3 / BIZT-2 | P1 | emberi döntés | a Group-tartalékút: hozzáférés-korlátozásra csak „Visible” / „Only visible to members” tagságú csoport használható (MoodleDocs 5.2 Groups) → a kapueredmény a társak felé kiszivároghat; DPO + LMS-gazda |
| BIZT-1 | P1 | objektív | az online szöveg szerkesztője alapból korlátlan beágyazott fájlt fogad (`onlinetext/locallib.php`, `EDITOR_UNLIMITED_FILES`) → az M2.1 „Nincs fájlfeltöltő mező” korlátja megkerülhető; a célverzión ki kell zárni, különben emberi döntés |
| BIZT-3 | P1 | objektív | a TEXT-C activity leírásába a lecke mező melletti adatvédelmi/biztonsági megjegyzése is kerüljön át szó szerint |
| IMPL-4 | P2 | emberi döntés | bukott M7-kvíznél a v2 nem adható le, ezért az LMS-M7-08 „mindkettő értékelése után” kitöltése nem teljesül → a Z nyitása ennél a csoportnál késik; programvezető + értékelési felelős |
| IMPL-5 | P2 | emberi döntés | az „Mx megerősítve” nyitás és az újraértékelés „a downstream feloldás előtt” zárópontja (M §4, PT :290) ütközik |
| IMPL-6 | P2 | objektív | LMS-M5-07: a relatív dátum mellé ÉS-feltételként a core „LMS-M5-03 must be marked complete” kell; az RA 4 utanként bontandó; az „értesítés” mechanizmusa nincs megadva |
| IMPL-7 | P2 | objektív | a lecke- és asset-specifikációk még dián belüli mezőt írnak elő (pl. M4.2 :751 M4.2-EGY-05, Z.3 :234) |
| IMPL-8 | P2 | emberi döntés | a TEXT-C automatikus nem-üres completionje elég-e a Program terv §5 „minimálisan értelmezhető tartalom” szabályához (főleg LMS-Z-06); értékelési felelős |
| IMPL-9 | P2 | objektív | GATE-CP: „a „Teljesítve” érték nem írható vissza” túlterjeszti a Program terv §5 önkéntes-újrabeadás szabályát, és ütközik az újraértékeléssel (M §4) |
| IMPL-10 | P2 | objektív | a `BUILD_SPEC_RESOLVED` sorokhoz a megoldó commit hash-e kell (a nyilvántartás saját szabálya) |
| IMPL-11 | P2 | objektív | GATE-CP: skálánál a Grade to pass számértéke (2), és a „Use marking workflow” kikapcsolása nincs megadva |
| BIZT-4 | P2 | objektív | LMS-M3-07: „kétszemes döntés, a Memunával” → szó szerint „mentor + második képző + a Memuna” (PT :288) |
| BIZT-5 | P2 | objektív | GATE-CP láthatóság: a TEXT-C-ben meglévő „tanári szerepkör alapból látja … stagingben visszaolvasni” figyelmeztetés hiányzik |
| BIZT-6 | P2 | objektív | Z.3 :234, :287, :304 „kötelező a továbblépéshez” tanulói állítás pontosítandó az RA 12 szerint |
| BIZT-7 | P2 | emberi döntés | az LMS-Z-06 válaszainak megőrzési sora („Szabad szöveges reflexió” vagy „Assignment / peulatervek”); DPO |
| BIZT-8 | P2 | bizonyíték-kapu | a 10 új activity adatleltára a DPO FINAL_RELEASE_QA-jának része legyen |

## A fő session által talált, nem szerkesztett következmények

- **M0 belépőkvíz, 4. item (answer key):** a D) „A következő modulba lép, és majd később javít.” disztraktor a Q-REL-2
  után részben igaz leírás; a visszajelzése: „éles kapunál a következő kapuzott tartalom addig nem nyílik meg …”
  (`M0 – Kickoff, keret, technika.md` :230–231). Vétólista; a tétel a projektgazda szövege (HUM 8. szakasz).
- **M1.4 :496 (tanulói):** „az M2 csak akkor nyílik meg, ha a képződ a rubrika alapján megerősíti, hogy a beadásod
  elérte a fenti átmenő szintet” — ellentmond a Q-REL-2-nek.
- **M5.3 §3.6:** nincs a tartalékúthoz (RM-D6) tanulói mondat, amely a 72 órás várakozást kéri; az M5 hub :191 és az
  RA 4 csak a 72 órás nyílást ismeri.
- **M7 KAPU :27, :416:** a checkpointot még feltételesnek írja („Ha az összetett feltétel Moodle-ben nem kódolható
  bizonyítottan …”).
