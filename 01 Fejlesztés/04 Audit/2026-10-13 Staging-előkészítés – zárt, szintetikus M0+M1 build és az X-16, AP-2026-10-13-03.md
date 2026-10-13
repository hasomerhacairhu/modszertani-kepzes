# Staging-előkészítés – zárt, szintetikus M0+M1 build és az X-16, AP-2026-10-13-03

> **Audit trail, nem kánon.** A `98be6aa` állapotból: (1) az X-16 – a rubrikás Assignmentek numerikus összpontja – Moodle
> 4.5-forrásból levezetett javasolt megoldása; (2) a zárt, szintetikus staging buildhez szükséges konfiguráció, ütemezés,
> kontaktok és tesztfiókok leltára. Hiányzó adatot a dokumentum nem tölt ki: ahol érték kell, a felelős szerepet nevezi meg.
> Forrás-rövidítések: MAN = `LMS – activity manifest.md`, RA = `LMS – H5P runtime acceptance.md`, HUM = `Emberi
> jóváhagyás szükséges.md`, RR = `RELEASE-READINESS.md`, ADV = `Adatvédelem – tanulói adatok és AI.md` (mind a
> `02 Tervezet/` alatt). A sorszámok a `851c09f` állapotra vonatkoznak.

## 1. X-16 – a javasolt megoldás

**Cél (projektgazda, 2026-10-13):** a tanuló megkapja a szöveges rubrikaszintet és a mentori visszajelzést, de numerikus
összpontot ne lásson – sem az Assignmentben, sem a Grades nézetben. A grade item nem rejthető, a rubrikapont, a küszöb és a
completion nem változik.

**Amit a forrás mutat (moodle/moodle `MOODLE_405_STABLE`, a fő session olvasta 2026-10-13-án):**

| Felület | Mi jelenik meg | Forrás |
|---|---|---|
| Assignment, „Grade” sor | `str_long_grade`: „Real” megjelenítésnél „pont / max”, más típusnál csak a formázott érték | `mod/assign/locallib.php` `get_assign_feedback_status_renderable()`; `mod/assign/classes/output/renderer.php`; `lib/gradelib.php` `grade_get_grades()` |
| Assignment, rejtett grade item | a teljes visszajelzés (rubrika, komment) eltűnik a tanuló elől | `get_assign_feedback_status_renderable()`: `$gradevisible … !$gradebookgrade->hidden` |
| Assignment, „Grade breakdown” | a rubrika; a szintpont `showscorestudent` = No mellett nem látszik, összpontot a rubrika nem ír ki | `grade/grading/form/rubric/renderer.php` (`display_instances()`, `showscorestudent`) |
| Grades user report | pontszám oszlop a megjelenítési típus szerint; a „Percentage” oszlop mindig százalék, a „Range” mindig valós szám; alapértelmezésben mindkettő be van kapcsolva | `grade/report/user/classes/report/user.php`; `grade/report/user/settings.php` (`showpercentage` = 1, `showrange` = 1) |
| Overview report (minden kurzus) | a kurzus összesítője; rejtett „Course total” mellett a tanuló nem kap értéket | `grade/report/overview/lib.php` (`$coursegrade->is_hidden()`) |
| Kurzus Assignment-listája | `str_grade` (a megjelenítési típus szerint) | `mod/assign/locallib.php` `view_course_index()` |
| Visszajelzés-értesítés | szöveg pontszám nélkül | `mod/assign/lang/en/assign.php` (`feedbackavailabletext`) |
| Betűjegy | a kurzus betűjegy-készletéből, százalékhatár szerint; a készlet kurzusszintű, egyetlen 0 %-os betűjegy elfogadott | `grade_format_gradevalue_letter()`, `grade_get_letters()`; `grade/edit/letter/index.php` |

**Elvetett utak:** a grade item rejtése (a visszajelzés is eltűnik); a „Percentage” megjelenítés (szám); a Scale grade
type (rubrikával nem használható, és a pontozást változtatná); a pontkönyv elrejtése a tanulók elől (az Assignment oldalán a
pontszám akkor is látszik); a szintnév-betűjegy (a betűjegy-készlet kurzusszintű, a három rubrika maximuma eltér: 2, 8, 15).

**Javasolt konfiguráció** (beírva: MAN LMS-M4-05, „javasolt mód (X-16)”; döntés: projektgazda mint build-spec gazda +
LMS-gazda):

1. A három Assignment rubrikája: „Display points for each level to those being graded” (`showscorestudent`) = No; a többi
   rubrika-beállítás a saját manifest-sora szerint. Rubrikapont, maximum, Grade to pass, completion változatlan.
2. A három grade item: „Grade display type” = „Letter”; a grade item nem rejtett.
3. A kurzus „Grade letters” készlete („Override site defaults”): egyetlen semleges betűjegy 0 %-os határral – a címke
   szövegéről a projektgazda dönt.
4. A kurzus user report-beállítása: „Show percentage”, „Show ranges”, „Show contribution to course total”, „Show
   weightings”, „Show letter grades” és „Show rank” = No; a „Show average” értéke rögzítendő; „Show grades” és „Show
   feedback” = Yes.
5. A „Course total” grade item rejtett (a repóban nincs kurzuspontszám-alapú feltétel).

**Mellékhatás és korlát** (a döntéshez): a „Letter” megjelenítés az értékelő pontozási tábláján is a címkét mutatja
(`display_grade()`), a pontszám a táblaletöltésben vagy a pontkönyv-exportban olvasható; a tanuló saját nyers pontszáma a
pontkönyv webszolgáltatás-válaszában (`gradereport_user_get_grade_items`, `graderaw`) elérhető marad, ha a webszolgáltatás
vagy a mobil-elérés engedélyezett. A megjelenítés tehát egységes, a hozzáférés technikailag nem zárt.

**Csak cél-Moodle-ben dönthető el** (runtime acceptance 28. pont, RT-P0-28, nyitva): a theme vagy helyi testreszabás nem
ír-e ki számot; a mobilalkalmazás nézete, ha engedélyezett; hogy a betűjegy-címke és a beállítások a célverzióban így
viselkednek. A 28. pont negatív esetei (a)–(g), pozitív esetei (h)–(k); kontroll: „Real” megjelenítés mellett ugyanaz a
fiók látja a számot. A 4. és az 5. pont kurzusszintű: a kurzus minden tételének tanulói pontkönyv-nézetét érinti (például a kvízek
százalékát és tartományát sem mutatja), ezt a döntésnél figyelembe kell venni; az RA 26 és 28 visszaolvasása az M1-re is
kiterjed.

## 2. A zárt, szintetikus staging build (M0+M1)

**Hatókör és szabály:** a legkisebb staging-szelet az M0+M1, belső tesztfiókokkal (RR „Legkisebb értelmes
staging-szelet”); rejtett staging-kurzus (MAN :211); csak szintetikus tesztadat; emberi döntés helyén belső build-jelölő,
amely nem kerül tanulói nézetbe (RR „Staging-szabály” 1–3.). A gépi verdikt: `READY_FOR_STAGING_BUILD`.

### 2.1 Konfiguráció – eldöntve, a buildhez kész

- Kurzus: egy Topics-kurzus, M0–M7 + Z szakasz; „Group mode” = „Separate groups”, „Force group mode” = „No” (MAN :31; ADV
  :135, :141); H5P-C, QUIZ, ASSIGN, GATE-CP, TEXT-C: Separate groups, grouping nélkül; FORUM-C: „No groups”.
- Completion: kurzusszinten be, „Condition requires” = All, a kötelező sorok (MAN :171); GATE-CP csak „complete, pass”; az
  LMS-M0-05 a futó kohorszban nem feltétel.
- H5P-C profil (MAN :16), LMS-M0-06 role override (`mod/quiz:viewreports`, `mod/quiz:grade`), LMS-M1-05 (Point, max 8,
  rubrika-előnézet, egy fájl), LMS-M1-06 GATE-CP (kételemes skála, Grade to pass = 2), LMS-M1-07 TEXT-C; LMS-M0-05 rejtve.
- Kurzusszintű elemek: „Segítség és kapcsolatok” blokk, „ha téged is érint” blokk, adatvédelmi tájékoztató és glosszárium
  (PAGE-C), offline alacsony adatigényű fájlok (MAN :118–135).
- Build-eszköz: `neongodio/moodle-ai-mcp` Core 1.0 (MAN :189); kézi tartalékutak: MAN :196–204.

### 2.2 Konfiguráció – nyitott bemenet (ki adja)

| Tétel | Mi hiányzik | Ki adja | Blokkolja a staging buildet? |
|---|---|---|---|
| Célkörnyezet | a Moodle-példány, a pontos Moodle- és H5P-verzió (a 4.5–5.2 csak kutatási tartomány, MAN :177), site-adminisztrátori hozzáférés | LMS-gazda / build-felelős (RR G3a, G3b) | **igen** |
| Staging deployment engedélye | kifejezett engedély | projektgazda | **igen** |
| A11Y-07 (iframe-cím) | theme-JS/AMD, renderer vagy local plugin (A11Y :93–103) | a repó nem nevez meg felelőst | nem (a release-t blokkolja, ha egyik sem telepíthető) |
| H5P mentett állapot | `enablesavestate`, `savestatefreq` (RA :11; a célkörnyezet adja) | site-adminisztrátor | nem; rögzítendő |
| LMS-M0-06 próbálkozásszám | „több próbálkozás” (M0 hub), a pontos szám nincs | a repó nem nevez meg felelőst | nem; build előtt rögzítendő |
| LMS-M1-05 elfogadott fájltípus | „például .docx, .odt, .pdf” | LMS-gazda + DPO + hozzáférhetőségi gazda | nem |
| Név szerinti szerepkiosztás | szerkesztő tanár, menedzser, admin (ADV :105–107) | adatvédelmi felelős tölti ki, LMS-gazda rögzíti | stagingben tesztfiók elég |
| ADV-2 hozzáférési mód | második értékelő, F-peula képző, Memuna (ADV :139) | LMS-gazda | nem; az RA 15 előtt kell |
| A „képző” Moodle-szerepe | a tesztlépések „képzői fiókja” nincs szerephez rendelve | LMS-gazda + adatvédelmi felelős | nem; az RA 6, 15, 16, 21, 24 előtt kell |
| Build-ID a kurzusszintű elemekre | a PAGE-C és File elemeknek nincs build-ID-ja (RR „Staging-szabály” 4.) | a repó nem nevez meg felelőst | nem; a build-visszaolvasás előtt kell |
| X-16 | a javasolt mód elfogadása és a betűjegy-címke | projektgazda + LMS-gazda | nem az M0+M1-hez, de a 4–5. beállítás kurzusszintű |

### 2.3 Ütemezés

- **A staginghez valódi dátum nem kell:** a dátumok beállítása tanulónak nyitás előtt RELEASE-EVIDENCE, a dátumfüggő
  activity dátum nélkül is felépíthető (RR G8; HUM 11. szakasz, PILOT-2). A `SCHEDULE_TO_RESYNC` jelölő tanulói nézetbe nem
  kerülhet (MAN :222).
- **Nyitott döntés:** a dátumhoz kötött nyitások (LMS-M0-03 „M0.A után nyílik dátummal”, LMS-M1-03) staging-teszteléséhez
  dátum kell; a repó nem mondja ki, hogy a staging-kurzusban szintetikus tesztdátum használható-e. Döntés: programvezető.
- **A pilothoz és a learner release-hez hiányzó dátumok** (a programvezető adja; a MAN §7 az egyetlen forrás): kurzus-hozzáférés
  időpontja (a dátum 2026-10-10); M0.A, M1.A, M1.B; `M0_L3`, `M0_FORUM`, `M0_QUIZ`, `M1_L3`, `M1_ASSIGN` (a határidő az M2.A
  előtti szerda 18:00, ezért az M2.A dátuma már az M0+M1-hez is kell); az M1 megerősítés, az M1.F, a javító határidő és a
  javító megerősítése; az M2–Z összes `SCHEDULE_TO_RESYNC` kulcsa.

### 2.4 Kontaktok

- **Stagingben:** belső build-jelölő, tanulói nézet nélkül; szintetikus kontaktérték nem írható be (RR „Staging-szabály” 1–2.).
- **A learner release-hez hiányzik** (a programvezető adja, HUM-OPS-02): a technikai segítség csatornája és elérési ideje,
  a Moodle-súgólink URL-je; a tanulási/programkontakt csatornája és elérési ideje; az, hogy a blokk hogyan mutatja minden
  tanulónak a saját mentorát. Az adatvédelmi kontakt (`PRIVACY_CONTACT_TO_CONFIGURE`, ADV :248): az adatkezelő
  adatvédelmi/jogi felelőse adja; a tájékoztató a DPO jóváhagyása előtt nem élesíthető.
- **Kánoni, nem hiányzik:** a Memuna és a kijelölt helyettes elérése, a Somer központi száma (HUM :30; GK :87–88); a release
  előtt újra ellenőrizendő (GYV-24), és a segélyvonalak leírása a nyitott D-05-től függ.

### 2.5 Tesztfiókok (szintetikus, név nélkül)

| Fiók | Moodle-szerep | Csoport | Mely tesztek (M0+M1) | Megkötés |
|---|---|---|---|---|
| tanulói fiókok, A és B csoport | Student | A vagy B | RA 1, 6–9, 13–15, 17, 22–28, RT-A11Y | a 8. ponthoz legalább kettő; a 15. ponthoz két külön csoport; a 28. ponthoz szintenként egy; a pontos számot a TEST_OWNER rögzíti |
| tanulói fiók egy második kurzuspéldányban | Student | — | RA 27 | a 27. pont futó és új kohorszot kér, ezért két kurzuspéldány kell |
| mentor A, mentor B | Non-editing teacher | csak a saját | RA 6, 8, 15, 24, 26 | a szerep csak a csoportba sorolás után; `moodle/site:accessallgroups` nincs |
| csoport nélküli mentor | Non-editing teacher | nincs | RA 15 (negatív eset) | csak ideiglenesen, a TEXT-C (LMS-M1-07) visszaolvasásán kívül (RA 15) |
| szerkesztő tanár, menedzser | Editing teacher, Manager | — | RA 15 | név szerint, auditálhatóan (ADV-1) |
| site-adminisztrátor | Administrator | — | build, site-beállítások | — |
| második / fellebbezési értékelő, F-peula képző, Memuna | az ADV-2 szerinti mód | — | RA 15, M1 újraértékelés | csak dokumentált eljárásban |

A kapacitás felső határa mentoronként 8 tanuló (HUM :245; a :243 kapacitás-mondata az `AP-2026-10-13-03` óta [SUPERSEDED]).

### 2.6 Környezeti rekord

A RA „Environment record” 19 `RUNTIME_OUTPUT` sora (Moodle, H5P core/plugin, a mentett állapot két beállítása, a content
type-ok verziói, böngésző/eszköz-mátrix, az A11Y-07 megoldás), valamint a `RUN_DATE` és a `TEST_OWNER` a staging-teszt
idején töltendő ki; a `TEST_OWNER` szerepet az LMS-gazda jelöli ki. A build 76 `BUILD_OUTPUT` értéket (cmid) állít elő,
ebből 13 az M0+M1-é.

## 3. Javítva ebben a körben (validált, objektív)

- RA Teszt-állapot: a 27. pont sora (RT-P0-27) hiányzott, a 28. pont sora (RT-P0-28) új; az RT-P0-26 címe a 26. ponthoz
  igazítva.
- HUM :243: [SUPERSEDED] jelölés, mert ugyanazon döntés :245 bekezdése az 1:10-es tartalékot kivette.
- Három korábbi auditfájl tévesen staging-előfeltételnek írta a valódi dátumokat és kontaktokat; javítva az RR G8 sora szerint.
- Célzott implementációs QA (QA19, a diffre): 5 finding, mind javítva – a 28. pont zárómondata nem zárja le az X-16-ot; a
  „Show rank” oszlop; a „Letter” megjelenítés hatása az értékelői nézetre és a visszaolvasás útja; a webszolgáltatás-korlát;
  a [SUPERSEDED] jelölés hatóköre (csak a kapacitás-mondat).

## A. Melléklet – a staging-leltár nyers kimenete (Explore, read-only)

#### Staging inventory (read-only): M0+M1 slice, with M2–Z listed separately

All paths below are relative to the repository root, and these abbreviations are used:

- MAN = `02 Tervezet/LMS – activity manifest.md`
- RA = `02 Tervezet/LMS – H5P runtime acceptance.md`
- HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`
- RR = `02 Tervezet/RELEASE-READINESS.md`
- GK = `02 Tervezet/Gyermekvédelem – release gate.md`
- ADV = `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`
- PT = `02 Tervezet/Program terv.md`
- A11Y = `02 Tervezet/LMS – hozzáférhetőségi sztenderd.md`
- M0H = `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md`
- M1H = `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md`
- M1K = `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`
- M14 = `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`

**Warning: two files changed while I was reading them.** MAN and RA have uncommitted changes, saved at 11:03 (HEAD = `98be6aa`). Those changes add RA point 28, the rows RT-P0-27 and RT-P0-28, and the X-16 wording in the MAN rows for M2-05, M4-05 and M6-05. RA line numbers after :112 refer to the working tree, not HEAD.

---

##### A) SCHEDULE

**General rules**
- MAN §7 is the only source for Moodle dates (MAN:222).
- Date decisions from 2026-10-05 (HUM:549):
  - authoring/build: 2026-10-06
  - first pilot cohort start: 2026-10-10, a Saturday (HUM:571)
  - the pilot covers M0 and M1 in October
  - every other date is `SCHEDULE_TO_RESYNC` and waits for a new schedule from the programvezető (HUM:549, MAN:222).
- Fixed rules (MAN:181, HUM:220):
  - a gate result must be confirmed at least 24 hours before the next fixed session
  - if the A-peula is on a Friday: submission Wednesday 18:00, first assessment Thursday afternoon, confirmation Thursday 18:00
  - F-peula on the Monday after confirmation, from 18:00; retry deadline the following Wednesday 18:00; retry confirmation Thursday 18:00 (MAN:251).
- Canonical start time is Friday 18:00, Europe/Budapest (Q-REL-4, HUM:512). But "a régi pénteki alkalmakra épülő feltevések erre a pilotra nem érvényesek automatikusan" (HUM:571, MAN:222). So for the pilot even the weekday is not guaranteed wherever it conflicts.
- Who provides dates: the programvezető (HUM-OPS-01 approver, HUM:216; HUM:549).

**PILOT-2: can date-dependent activities be built without a date?**
- Yes. "felépíthető, de valódi tanulónak nem nyitható meg, amíg a dátum nincs konfigurálva" (HUM:551, MAN:222, RR:34).
- The `SCHEDULE_TO_RESYNC` marker must never appear in a learner view (MAN:222).
- The M0.A date cannot be inferred from the cohort start (HUM:551).

**Does staging need real dates?**
- No. Staging has test accounts only, no real madrih (RR:10, RR:98, HUM:10).
- Under G8, "a naptár szabályai: BUILD"; setting the dates is RELEASE-EVIDENCE (RR:34).
- Gap: testing the date-based unlocks (LMS-M0-03 "M0.A után nyílik dátummal", MAN:43; LMS-M1-03 "M1.A után", MAN:49) needs some date value. The repo does not say whether a synthetic staging date is allowed. MISSING decision; the schedule owner is the programvezető.

**M0+M1 keys**

| Key / point | What the repo fixes | MISSING | Provides |
|---|---|---|---|
| Course access | date 2026-10-10 (Saturday) (MAN:250) | time (`SCHEDULE_TO_RESYNC`) | programvezető |
| `M0_L1` (`M0_L2` follows §2) | opens with course access (MAN:272) | time | programvezető |
| M0.A (offline) | "a központi naptár szerint" (M0H:12) | date and time (HUM:551) | programvezető |
| `M0_L3` (`M0_L4` follows §2) | opens after M0.A (MAN:273) | date | programvezető |
| `M0_FORUM`, `M0_QUIZ` | open per §2; due 18:00; a communicated target, not a lock: no "Close the quiz", no "Cut-off date" (MAN:274, MAN:226); no confirmation (PRG-6) | date (weekday not stated for M0) | programvezető |
| `M1_L1`, `M1_L2` | open on "M0 complete" (MAN:275) | — | — |
| M1.A, M1.B (offline) | first and second Friday (MAN:222, MAN:227) — but see the pilot override (HUM:571) | dates | programvezető |
| `M1_L3` (`M1_L4` follows §2) | opens after M1.A (MAN:276) | date | programvezető |
| `M1_ASSIGN` | due 18:00 (MAN:277); "legkésőbb az M2.A peula előtti szerdán 18:00" (M14:505; M1H:9; M1K:26) | date — this depends on the **M2.A** date, so one M2 key is needed even for the M0+M1 slice | programvezető |
| M1 confirmation (LMS-M1-06) | Thursday 18:00 (MAN:227, MAN:53) | date | programvezető |
| M1.F / retry / retry confirmation | Monday from 18:00 / Wednesday 18:00 / Thursday 18:00 (MAN:261); no F-peula activity, the trainer opens the retry with a user override (MAN:254) | dates (HUM:551) | programvezető |

**M2–Z keys** (all dates `SCHEDULE_TO_RESYNC`; programvezető unless noted)
- Fixed by rule:
  - `M2_L4`/`M2_L3`, `M3_L3`/`L4`, `M4_L3`/`L4`, `M5_L3`/`L4`, `M6_L3`/`L4`, `M7_L3`/`L4`: open after the module's A-peula.
  - `M2_ASSIGN`, `M4_ASSIGN`, `M5_ASSIGN`, `M6_ASSIGN`: open after the B-peula, due 18:00.
  - `M3_ASSIGN`: Monday 18:00. Rubric confirmation by the next day 18:00. `M3_QUIZ`: Wednesday 18:00. Gate confirmation: Thursday 18:00 (MAN:257, MAN:283–284).
  - `M7_V1_DUE`: Wednesday before M7.B, 18:00. Mentor feedback: the following Thursday 18:00 (MAN:239–240).
  - `M7_QUIZ`: no close date; mandatory before `M7_V2_DUE` (MAN:299).
  - `M7_V2_DUE`: 18:00 (MAN:300).
  - `Z_REFLECTION`, `Z_FEEDBACK`: after Z.A, 18:00 (MAN:302).
  - Winter break (MAN:230).
  - Notifications 24 hours before M4.A and M4.B (MAN:245).
  - F-peula and retry rows for M3, M5, M6, the M6 alternative, and M7 (MAN:262–266).
- No date needed: every "§2 szerint / —" key (MAN:278–301). LMS-M5-07 is relative (+72 hours, MAN:246).
- Different owners:
  - LMS-M7-09 confirmation time: the programvezető decides (MAN:106).
  - Soft-gate (M2, M4) retry timing: the trainer (képző) sets it (MAN:255).
  - Z retry: the assigned mentor (MAN:256).
  - Field-practice calendar: not part of HUM-OPS-01 (`02 Tervezet/Terepgyakorlat – 2. félév.md:66`).

---

##### B) CONTACTS

**The block itself:** four role-based contacts — technical help, learning/program contact, assigned mentor, and separately the Memuna; no "mentor / felelős / vezető" chain (HUM:243, PT:251, RR:42).
- HUM-OPS-02 blocks "learner-facing support szöveg véglegesítése, nem a belső staging build" (HUM:240).

**Staging rule for placeholders**
- "nem találunk ki … support-… adatot", so **no synthetic contact values** (RR:75).
- An internal build marker is allowed, but "nem kerülhet learner-facing nézetbe" (RR:76, HUM:552, RR:34).
- Only test data may be synthetic (RR:77).
- Lessons give the role only, never a name or phone number. Names appear only in governance texts and the block description, as "role + jelenleg: <név>" (GK:89). I found no numbers or names in the M0/M1 module files.

| Role | Fixed in repo | MISSING | Staging | Real value provided by |
|---|---|---|---|---|
| Technical help | role and slot (HUM:243, HUM:552, PT:240) | channel, hours, role label (RT-1, HUM:764); the Moodle help link required by PT:244 has no URL | build marker only, hidden from learner view | programvezető (approver, HUM:239); RT-1 evidence: LMS-gazda + programvezető (HUM:764) |
| Learning / program contact | role (HUM:243) | channel and hours (HUM:552) | same as above | same as above |
| Assigned mentor | per-group mentor; hard cap 1:8 (HUM:245); role assignment recorded by the LMS-gazda (MAN:31) | real mentor channel. How one block shows each learner their own group's mentor is **not specified** | synthetic mentor test accounts (test data) | programvezető (HUM-OPS-02); LMS-gazda records |
| Memuna (and named deputy) | the Memuna published at `somer.hu/kapcsolat` ("jelenleg: Marci"); deputy Ros Hinuh ("jelenleg: Lili"); Somer central number +36 70 42 76 637, weekdays 10–18, not an on-call line (HUM:30, GK:87–88, PT:251); shown in the block, separate from the other contacts (GK:148; RT-P0-17: RA:89) | nothing new — "a meglévő kánoni adatok" (HUM:552) — but numbers must be rechecked before release (GK:50, GK:151; GYV-24, HUM:754) | canonical data may be used; no placeholder needed | Memuna. Ambiguity: whether real first names should render in staging is not separately addressed against RR:77 |
| Crisis lines | 112; Kék Vonal 116-111; 116-000 (HUM:30); descriptions in GK:46–48 (GK also lists 116-123, an adult line) | **D-05 is open and marked urgent:** "A 116-111 és a 116-000 félrevezető leírásának javítása" (HUM:815) | canonical text, subject to D-05 | Memuna |
| Data-protection / DPO contact | the privacy notice is a PAGE-C page; its text is in ADV §11 | `PRIVACY_CONTACT_TO_CONFIGURE` (ADV:248, ADV:221). Side effect: the learner text "az elérhetősége ez alatt áll" (ADV:278) will dangle in staging | marker only in the internal table, never rendered (ADV:244) | "adatkezelő privacy/DPO/jogi felelőse" (HUM-PRIV-01 approver, HUM:135); the page cannot go live before DPO approval (ADV:242) |

**Correction to your pointer:** RT-1 is not in the runtime acceptance file. It is an evidence entry in HUM 14. szakasz, HUM:764 ("LMS-gazda + programvezető", open). The runtime-acceptance equivalent is point 17 / RT-P0-17 (RA:89, RA:154).

---

##### C) TEST ACCOUNTS (deduplicated)

**Global constraints**
- Synthetic data only; no real madrih (RR:10, RR:77; ADV:5; GK:21).
- Every learner is in exactly one mentor group; the mentor is a member of the same group; no other groups exist (ADV:128).
- At most 8 learners per mentor (HUM:245).
- Evidence records list account roles without names (non-canon audit `01 Fejlesztés/04 Audit/2026-10-13 Bizonyítékcsomag…:18`).

| Account | Moodle role | Group | Tests (M0+M1-relevant in bold) | Constraints |
|---|---|---|---|---|
| Learner A1… / B1… | Student (ADV:103) | A or B | **1, 6, 7, 8, 9, 13, 14, 15, 17, 19, 22–27, RT-A11Y**; also 12, 16, 21, 28 | Point 8 needs **two learner accounts** (RA:58). Point 15 needs two separated groups (RA:87). Point 19 needs a "**tisztán tanulói szerepű**" account, i.e. not holding `moodle/grade:viewhidden` + `mod/quiz:viewreports` together, plus one failing and one passing account (RA:96). Point 28 needs one learner per rubric level (RA:113, working tree). The exact number of learners is **not fixed** (MISSING; TEST_OWNER/LMS-gazda) |
| Learner in a second course copy | Student | — | **27** | Needs a "megnyitást követően induló kohorsz kurzusa" and a "futó kohorsz kurzusa" (RA:112), so **two course instances** |
| Mentor A | Non-editing teacher (ADV:104) | A only | **6, 8 (writes GATE-CP values), 15, 24, 26** | Role given only after joining the group; no `moodle/site:accessallgroups` (ADV:129–130, ADV:137). LMS-M0-06 override removes `mod/quiz:viewreports` and `mod/quiz:grade` (MAN:46, ADV:140) |
| Mentor B | Non-editing teacher | B only | same | same |
| Ungrouped mentor | Non-editing teacher | none | **15** (negative test: sees no group's ASSIGN/H5P/QUIZ/GATE-CP data) | Clashes with the TEXT-C readback "nincs csoport nélküli, `mod/feedback:viewreports` jogú mentorfiók" (RA:87; ADV:129). Use it only temporarily, never while TEXT-C (LMS-M1-07) is being read back |
| "Képzői" (trainer) account | **not mapped to a Moodle role in the repo** | — | 6, 15, 16, 21, 24; grants the M1-05 retry ("Grant attempts = Manually", MAN:20) | MISSING mapping (privacy felelős / LMS-gazda) |
| Editing teacher | Editing teacher | — | **15** | narrow, assigned by name, auditable (ADV-1; RA:87; ADV:105, ADV:138) |
| Manager | Manager | — | **15** | same (ADV:106) |
| Site admin | site administrator (ADV:107) | — | needed for the build (A11Y-07 plugin, site settings, `moodle_site_inspect`) | the privacy text must not deny admin's full access (ADV:109) |
| Second / appeal grader | not specified | — | **15**; M1 re-assessment (MAN:185); point 8 "jogosult stábtag" edit with Grade history (RA:62) | access only in a concrete, documented procedure; technical method recorded by the LMS-gazda (ADV:139; ADV-2, HUM:648) |
| F-peula trainer | not specified | — | **15**; M1.F | sees only aggregates or a minimal shortfall list (ADV:158) |
| Memuna (if needed) | not specified | — | **15** | ADV-2 procedure only; synthetic account in staging |
| DPO | **no Moodle account required** | — | — | QA reviewer for RT-P0-15 (HUM:576) |
| TEST_OWNER | — | — | Environment record | MISSING (RA:9–10) |

---

##### D) CONFIGURATION

**Decided and specified**
- **Course:** one Topics course; sections M0–M7 + Z (PT:219); build in a hidden staging course (MAN:211).
- **Groups:**
  - Course group mode "Separate groups", "Force group mode" = No (MAN:31; ADV:135, ADV:141).
  - Activities of profile H5P-C, QUIZ-D/M, ASSIGN-S/M, GATE-CP and TEXT-C: Separate groups, no grouping.
  - FORUM-C: "No groups" (MAN:21, MAN:24).
  - No group- or grouping-based access conditions (BS-D1).
- **Completion:**
  - course completion on, "Condition requires" = All, criteria = every mandatory row (MAN:171)
  - GATE-CP rows count only as "complete, pass"
  - LMS-M0-05 is not a criterion for a running cohort (D-15 f).
- **H5P-C:** attempt tracking Yes; Point grade; no grade to pass; completion "Receive a grade"; Course Presentation "Hide summary slide" = No (MAN:16).
- **H5P, other:** Hungarian editor language; Title = activity name (A11Y:90–91); autoplay off (RA:108); Single Choice Set "Auto continue" off (A11Y:83); M1.2 radio buttons only (MAN:48).
- **LMS-M0-06 (quiz):** 7 items, no cut score, completion = all 7 answered, options shuffled (M0H:182–183); role override as above.
- **LMS-M1-07 (TEXT-C):** full Feedback settings (MAN:24, MAN:50).
- **LMS-M1-05:** completion on submission; Point, maximum 8; rubric preview Yes; one file; online text + file path; Grant attempts Manually / Unlimited (MAN:20, MAN:52).
- **LMS-M1-06 (GATE-CP):** two-item custom scale; Grade to pass = 2; marking workflow No; feedback comments Yes; grade item not hidden or locked. "Mx megerősítve" = Grade condition with no limits; "Mx complete" = lower limit 50% (MAN:25, MAN:175–176).
- **LMS-M0-05 (forum):** hidden, and nothing references it while closed (MAN:45).
- **Course-level elements (MAN:118–135):**
  - the Segítség és kapcsolatok block
  - the "ha téged is érint" block at M0.1
  - privacy notice PAGE-C
  - glossary PAGE-C
  - offline low-data File resources for the video lessons (M1.1–M1.3 in this slice)
- **MCP:** `moodle-ai-mcp` Core 1.0 (MAN:189).
- **Manual fallbacks (MAN:196–204):** rubric, custom scale, restrict access, Feedback activity, forum completion. Per-user grade writing is not supported.
- **Build specs:** BSPEC-01…07 are all `BUILD_SPEC_RESOLVED` (MAN:314–320).

**Open, needs a decision or input (owner)**

*M0+M1-relevant:*
- **Target Moodle/H5P version:** unknown; "4.5–5.2" is a research range, not a decision (MAN:177; HUM:501). Comes from the target environment.
- **A11Y-07 (iframe titles):** which mechanism to use (theme JS/AMD, renderer, or local plugin). If none can be installed, it becomes a TARGET-ENVIRONMENT blocker (A11Y:93–103; RA:27). Owner not named.
- **H5P save-state settings:** `enablesavestate` and `savestatefreq` are not prescribed — "a célkörnyezet adja, ez a dokumentum nem írja elő". They are recorded as `RUNTIME_OUTPUT` (RA:11, RA:109).
- **LMS-M0-06:**
  - whether a mentor sees their own group's score in the gradebook — expected result open (programvezető + Memuna; DPO for the data scope, RA:87)
  - statistics report access — to be verified (ADV:140)
  - number of attempts — not fixed: "több próbálkozás" (M0H:149); profile default 2–3.
- **LMS-M1-05 accepted file types:** "például .docx, .odt, .pdf" (LMS-gazda + DPO + hozzáférhetőségi gazda; HUM:738).
- **Named role assignments:** who gets editing teacher, manager and admin — privacy felelős fills it in, LMS-gazda records it (ADV:105–107).
- **ADV-2 access mechanism** for second grader, F-peula trainer and Memuna (LMS-gazda; ADV:139).
- **"Ki látja?" privacy text:** must be adjusted after the staging role matrix (ADV:242).
- **`PRIVACY_CONTACT_TO_CONFIGURE`** (see B).
- **Unspecified:** mentor display in the block; the trainer (képző) role mapping; synthetic staging dates.
- **No build_id/cmid for course-level Page and File resources:** RR:78 requires a "build-ID" and cmid for every real Moodle activity, but MAN:118–135 gives these none. Owner not named.
- **Course-level gradebook settings (X-16, working tree only):** proposed for M2-05/M4-05/M6-05. Course "Grade letters" override with one neutral letter; user report "Show percentage/ranges/contribution/weightings/letter grades" = No; "Course total" hidden (MAN:80; RA:113). Decided by the projektgazda (as build-spec owner) + LMS-gazda. These are course-wide, so they would also affect M1 items.

*Out of slice:* Feedback-N group mode (DPO, BIZT-6; MAN:22); M2/M4/M6 final-score hiding; `availability_relativedate` plugin (site admin installs it; the build does not wait, HUM:516); whether the mobile app is enabled (RA:113).

**Produced by the build** (counted, not decided)
- **`BUILD_OUTPUT` cmids: 76** (M0+M1 = 13).
  - Whole course: H5P-C 35, plus 1 "H5P-C vagy PAGE-C" (LMS-M5-07); GATE-CP 12; TEXT-C 11; ASSIGN-M 5; ASSIGN-S 4; QUIZ-D 3; QUIZ-M 2; FORUM-C, FEEDBACK-N, PAGE-C 1 each.
  - M0+M1: H5P-C 8; FORUM-C 1; QUIZ-D 1; TEXT-C 1; ASSIGN-M 1; GATE-CP 1.
- **`RUNTIME_OUTPUT`: 19** Environment record rows (RA:9–27), plus `RUN_DATE` ×2 and `TEST_OWNER` ×2.
- **`IMPLEMENTATION_TEST_REQUIRED`: 40 rows** in the working tree (RT-P0-01…28 + RT-A11Y-01…12); 38 in HEAD.
- **TARGET-ENVIRONMENT:** none recorded; one conditional (A11Y-07).

---

##### Inconsistencies

**Certain**
1. **HUM:243 vs HUM:245** (same item, both 2026-10-02):
   - HUM:243: „Mentor:madrih kapacitás: javasolt kiinduló plafon 1:8, legfeljebb 1:10."
   - HUM:245: „**kemény plafon 1:8** … az 1:10 tartalék kikerült"
   - HUM:243 has no [SUPERSEDED] marker, unlike HUM:226 and HUM:483. Relevant to synthetic group sizes.
2. **RA in HEAD `98be6aa`:** point 27 exists („27. **A bemutatkozó fórum feltétele (LMS-M0-05…**", RA:112), but the machine-tracked table ends at `| RT-P0-26 | … 26. Rubrika tanulói megjelenítése (LMS-M1-05) |`, so test 27 is untracked in HEAD. The uncommitted working tree adds RT-P0-27 and RT-P0-28 (RA:164–165).
3. **Non-canon audit vs canon** (canon governs):
   - Audit (`01 Fejlesztés/04 Audit/2026-10-13 Bizonyítékcsomag…:55–56`): staging deployment needs „a G4 build-előfeltételei (dátumok, kontaktok, `#4`)".
   - RR:34: dates are „RELEASE-EVIDENCE … a valódi kontaktok: RELEASE-EVIDENCE (stagingben belső build-jelölő megengedett)".
   - HUM:240: „nem a belső staging build".

**Not certain (flagged only)**
- MAN:120 lists "a „Segítség és kapcsolatok” blokk … és a gyermekvédelmi kontaktblokk" as two items, while HUM:35 says "egyetlen jóváhagyott kontaktblokk".
- M14:505 states the Wednesday deadline without M1K:26's „Pénteki M2.A esetén" condition, given the HUM:571 pilot-weekday override.

## B. Melléklet – célzott implementációs QA (QA19) nyers kimenete

QA19-IMPL: célzott, diffre szabott QA az X-16 változásról (diff-x16.txt). 5 finding, mind P2. P0 vagy P1 nincs.

**Amit a forrásban ellenőriztem és rendben találtam** (moodle/moodle MOODLE_405_STABLE, raw.githubusercontent.com):
- **Betűjegy az Assignmentben és a pontkönyvben:** nem Real megjelenítési típusnál a `str_long_grade` megegyezik a `str_grade`-del, ez a forrás `lib/gradelib.php` sora: „`if ($grade_item->gradetype == GRADE_TYPE_SCALE or $grade_item->get_displaytype() != GRADE_DISPLAY_TYPE_REAL) { $grade->str_long_grade = $grade->str_grade;`”.
- **A betűjegy-készlet kurzusszintű:** `grade_format_gradevalue_letter()` a `context_course::instance($grade_item->courseid…)` alapján választ betűt, és „`if ($value >= $boundary) { return format_string($letter); }`”. Így a 0 %-os egyetlen betűjegy minden pontszámra ugyanazt a címkét adja.
- **A 0 %-os egyetlen betűjegy elfogadott:** a `grade/edit/letter/index.php` csak az üres betűt és a 0–100 közén kívüli határt hagyja ki. Az `edit_form.php`-ban nincs `validation()`.
- **UI-feliratok** (`lang/en/grades.php`): „Show percentage”, „Show ranges”, „Show contribution to course total”, „Show weightings”, „Show letter grades”, „Grade display type”, „Letter”, „Grade letters”, „Override site defaults”. Mind egyezik a diffben szereplőkkel.
- **A tartomány mindig valós szám:** `get_formatted_range(GRADE_DISPLAY_TYPE_REAL, $this->rangedecimals)`.
- **Rejtett összesítő az overview reportban:** „`if ($coursegrade->is_hidden()) { $finalgrade = null;`”.
- **Az értesítés nem tartalmaz pontszámot:** `feedbackavailabletext`, `feedbackavailablesmall`. A „Grade breakdown” felirat létezik (`gradebreakdown`).
- **Rubrikapont, küszöb, completion:** a javaslat egyiket sem változtatja; a manifest „javasolt mód”-ként jelöli.

---

**QA19-IMPL-1**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:113` (28. pont, utolsó mondat)
- **Probléma:** A mondatból az következik, hogy sikeres teszt után az X-16 lezárul, pedig a manifest és a HUM 16. szakasza szerint a módról a projektgazda és az LMS-gazda dönt. A 28. pont ráadásul csak a projektgazdát nevezi meg.
- **Bizonyíték:**
  - RA:113: „Ha bármelyik negatív eset konfigurációval nem teljesíthető, az X-16 nyitva marad, és a projektgazda a manifest LMS-M4-05 sora szerint dönt.”
  - Manifest:80: „a végső pontszám rejtésének módjáról a projektgazda mint build-spec gazda és az LMS-gazda dönt”.
  - HUM:848, a „Nyitva marad” oszlop: „(projektgazda mint build-spec gazda + LMS-gazda; manifest LMS-M4-05)”.
- **Hatás:**
  - Egy átmenő RT-P0-28 után a javasolt módot eldöntöttnek lehet tekinteni, holott a döntés nem született meg.
  - A címke szövegéről szóló döntés (manifest:80) is kimaradhat.
- **Javaslat:** A mondat helyett: „Az X-16 a teszt eredményétől függetlenül a projektgazda (build-spec gazda) és az LMS-gazda döntésére vár; a teszt ehhez ad bizonyítékot. Ha bármelyik negatív eset konfigurációval nem teljesíthető, a javasolt mód nem alkalmazható.”
  - Tilos: a javasolt mechanizmust elfogadottnak jelölni, és a negatív vagy pozitív eseteken változtatni.
- **Típus:** objektív
- **Verdikt:**

**QA19-IMPL-2**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – activity manifest.md:80` (LMS-M4-05, a javasolt mód pontkönyv-beállításai)
  - `02 Tervezet/LMS – H5P runtime acceptance.md:113` (28. pont, (b) eset)
- **Probléma:** A beállításlista és a (b) negatív eset nem tér ki a „Show rank” oszlopra. Ez az oszlop szintenként eltérő számot mutat a tanulónak.
- **Bizonyíték:**
  - Manifest:80: „„Show percentage”, „Show ranges”, „Show contribution to course total”, „Show weightings” és „Show letter grades” = No”.
  - Forrás, `grade/report/user/classes/report/user.php`: „`$data['rank']['content'] = "$rank/$numusers";`”.
  - Forrás, `grade/report/user/settings.php`: `grade_report_user_showrank`, alapérték `0` (a `showaverage` alapértéke szintén `0`).
- **Hatás:**
  - Ha a site-szintű beállítás bekapcsolt rangsort ad (a kurzus ezt örökli), a tanuló „1/17” típusú számot lát. Ebből kiderül a relatív helye, és ez az (f) esetet is sérti.
  - A teszt (b) listája ezt nem kéri számon.
- **Javaslat:**
  - A manifest:80 listájába: „Show rank” = No (és a „Show average” beállított értékének rögzítése is). A (b) esetbe: „…és nincs rangsor-oszlop”.
  - Az átlag megjelenítési típusát nem ellenőriztem, ezért arról nem állítok szivárgást.
  - Tilos: a meglévő öt beállítást vagy a rubrikaparamétereket módosítani.
- **Típus:** objektív
- **Verdikt:**

**QA19-IMPL-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – H5P runtime acceptance.md:113` (28. pont, (i) eset)
  - `02 Tervezet/LMS – activity manifest.md:80`
- **Probléma:** A „Grade display type” a grade item tulajdonsága, és a mentorra is érvényes: az Assignment pontozási táblájában ő is csak a címkét látja. Az (i) eset ezért nem nevez meg olyan értékelői nézetet, ahol a pontszám ellenőrizhető, és a javaslat ezt a mellékhatást sem közli.
- **Bizonyíték:**
  - RA:113: „(i) az értékelő nézetében a pontszám rögzült (LMS-M4-05: 0/1/2; a másik kettőnél a saját soruk szerinti összeg)”.
  - Forrás, `mod/assign/locallib.php` `display_grade()`: „`$o .= grade_format_gradevalue($grade, $item); if ($item->get_displaytype() == GRADE_DISPLAY_TYPE_REAL) { $o .= '&nbsp;/&nbsp;' …`”. Nézői megkülönböztetés nincs benne.
  - Forrás, `mod/assign/gradingtable.php` `col_finalgrade()`: „`$o = $this->display_grade($grade->grade, false, …)`”. Számot csak a táblaletöltés ad: „`return format_float($grade, $gradeitem->get_decimals());`”.
- **Hatás:**
  - A tesztelő a pontozási táblában címkét lát, így az (i) eset nem értékelhető vagy félreolvasható.
  - Az LMS-M2-05 és az LMS-M6-05 rubrikaösszegét a mentor a felületen sehol nem látja egyben.
  - A döntéshozók erről a mellékhatásról nem tudnak.
- **Javaslat:**
  - Az (i) esetben meg kell nevezni a visszaolvasás útját. LMS-M4-05-nél a rubrika értékelői nézetének szintpontja ad pontszámot. LMS-M2-05-nél és LMS-M6-05-nél a pontozási tábla letöltése vagy a pontkönyv-export (Real) ad számot.
  - A manifest:80 javasolt módjához egy mondat: „a Letter megjelenítés az értékelő pontozási tábláján is a címkét mutatja”.
  - Tilos: a javasolt módot vagy a rubrikaparamétereket megváltoztatni.
- **Típus:** objektív
- **Verdikt:**

**QA19-IMPL-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – activity manifest.md:80` („így minden pontszám ugyanazt a címkét mutatja”)
  - `02 Tervezet/LMS – H5P runtime acceptance.md:113` ((g) eset)
- **Probléma:** A javasolt mód csak a megjelenítést egységesíti. A tanuló a saját nyers pontszámát a pontkönyv webszolgáltatásán át továbbra is megkapja, és ezt a 28. pont nem fedi le.
- **Bizonyíték:**
  - Forrás, `grade/report/user/classes/report/user.php`: „`$gradeitemdata['graderaw'] = $gradeval;`”. Nem rejtett itemnél ez beállítódik.
  - Forrás, `grade/report/user/classes/external/user.php`: „`'graderaw' => new external_value(PARAM_FLOAT, 'Grade raw', VALUE_OPTIONAL),`”. Saját adatra a hozzáférés feltétele: „`$userid == $USER->id && has_capability('moodle/grade:view', $context) && $course->showgrades`”.
- **Hatás:**
  - Ahol a webszolgáltatás vagy a mobil-elérés be van kapcsolva, a „pont / max” érték technikailag elérhető marad.
  - A döntéshozók azt hihetik, hogy a numerikus érték nem hozzáférhető.
- **Javaslat:**
  - A manifest:80 javasolt módjához korlát-mondat: „a nyers pont a webszolgáltatás-válaszban (`gradereport_user_get_grade_items`, `graderaw`) elérhető marad; a megjelenítés egységes”.
  - A (g) esetben rögzíteni kell, hogy a webszolgáltatás vagy a mobil-elérés engedélyezett-e.
  - EMBERI DÖNTÉS: hogy ez a korlát elfogadható-e, az a nyitott X-16 része (projektgazda + LMS-gazda).
  - A Moodle mobilalkalmazás saját megjelenítését nem ellenőriztem.
- **Típus:** objektív (a korlát közlése; az elfogadása emberi döntés)
- **Verdikt:**

**QA19-IMPL-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:243`
- **Probléma:** A `[SUPERSEDED]` jelölés a bekezdés végén áll, hatókör megadása nélkül. Ugyanebben a bekezdésben él a még aktív négykontaktos szabály is, a Memunával mint külön gyermekvédelmi kontakttal. A szabályfájl szerint „A `SUPERSEDED` nem aktív kánon”.
- **Bizonyíték:** HUM:243: „…és ettől külön a Memuna (gyermekvédelem). Nincs „mentor / felelős / vezető” típusú lánc. Mentor:madrih kapacitás: javasolt kiinduló plafon 1:8, legfeljebb 1:10. **[SUPERSEDED: a következő bekezdés kemény 1:8-as plafonja; az 1:10 tartalék kikerült]**”. A :483 sor mintája a hatókört kifejezetten megnevezi: „[SUPERSEDED: a naptári dátumokat …]”.
- **Hatás:** Az egész bekezdést inaktívnak lehet olvasni. Ezzel a „Segítség és kapcsolatok” négy kontaktja, köztük a külön gyermekvédelmi kontakt, elveszítené a kánoni státuszát.
- **Javaslat:**
  - A jelölést közvetlenül a „Mentor:madrih kapacitás:” elé kell tenni, kifejezett hatókörrel: „[SUPERSEDED (csak a kapacitás-mondat): …]”.
  - Tilos: a négykontaktos mondatot vagy a :245 kemény plafonját módosítani.
- **Típus:** objektív
- **Verdikt:**

---

**Fájlonként:**
- `02 Tervezet/LMS – activity manifest.md`: QA19-IMPL-2, -3, -4 (:80). A :62 és :94 módosítása (a „javasolt mód (X-16)” mutató) rendben.
- `02 Tervezet/LMS – H5P runtime acceptance.md`: QA19-IMPL-1, -2, -3, -4 (:113). A 26. pont hivatkozása és az RT-P0-26/27/28 sorok rendben; más fájl nem rögzít RT-P0-darabszámot.
- `02 Tervezet/Emberi jóváhagyás szükséges.md`: QA19-IMPL-5 (:243).

**Nem ellenőriztem** (a fetch-eszköz csonkolta a nagy fájlokat):
- a `mod/assign/locallib.php` `get_assign_feedback_status_renderable()` és `view_course_index()` függvényét;
- a pontkönyv grader reportját;
- a Moodle mobilalkalmazás megjelenítését.

A docs.moodle.org/405 oldalt nem használtam, mert a forráskód elég volt.
