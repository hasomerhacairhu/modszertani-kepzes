# course-fix napló — Command 5, teljes BSPEC-kör (2026-10-05)

> **Audit trail, nem kánon.** Bemenet:
> - validált findingok:
>   - `2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`: IMPL-3, -4, -5, -6, -7, -9;
>   - `2026-10-05 Validált findingok – M3.3 Branching Scenario-flow.md`: M33-IMPL-1, -2, -3, -4, -7, -8, SAFE-2, -3, -5;
> - a projektgazda szó szerinti utasítása: `2026-10-05 Projektgazdai döntés – M6.4 elfogadás és Command 5 hatókör.md`, a két kiegészítő safeguarddal;
> - döntések: D-d, D-e, D-f, D-g (a), D-h, D-i, D-j, M33-IMPL-6, SAFE-1, SAFE-4, §7.1, §7.2 (`2026-10-05 Projektgazdai döntések – MAN completion és mentor-láthatóság D-e…D-j.md`).
>
> Munkaág: `fix/moodle-build-hardening`. Commit és push nincs.

## Elsődleges forrásból ellenőrzött tények (a futás előtt)

- **H5P Branching Scenario** (`h5p-branching-scenario`, `master`):
  - `scoringOption` ∈ `static-end-score` / `dynamic-score` / `no-score` (alapérték: `no-score`).
  - Statikus módban a pontszám a végképernyő `endScreenScore` értéke (`scoring.js`, `getScore`). A maximum a végpontok (`nextContentId === -1`) legnagyobb értéke (`calculateStaticMaxScore`).
  - Az `includeInteractionsScores` csak a dinamikus módban hat (`addLibraryScore`).
  - A végképernyő statikus és dinamikus módban kiírja a pontszámot (`shouldShowScore`); a címke az `l10n.scoreText`.
  - A végképernyőnél `triggerXAPICompleted(score, maxScore)` fut.
  - `randomizeBranchingQuestions` alapértéke: `false`. `enableBackwardsNavigation` alapértéke: `false`. `forceContentFinished` alapértéke: `false`.
  - A tartalomcsomópontonkénti `proceedButtonText` létezik.
- **H5P Course Presentation** (`h5p-course-presentation`, `master`):
  - Az eredmény (`triggerXAPICompleted`) az összefoglaló dián megy el (`summary-slide.js`).
  - Az összefoglaló dia akkor jelenik meg, ha a `override.hideSummarySlide` = `false`, és a CP-nek van feladata (`cp.js`).
- **Moodle `lib/completionlib.php`** (`MOODLE_405_STABLE`, `internal_get_grade_state`):
  - Grade to pass nélkül bármely nem üres grade `COMPLETION_COMPLETE`, rejtett grade itemnél is.
  - Pass/fail csak beállított `gradepass` mellett van.
- **Az M3.3 pontozási stop-feltétele nem teljesül**, mert a statikus végpontszám (egyetlen végpont, `endScreenScore` = 1) minden úton ugyanazt a nem üres grade-et adja:
  - csupa ❌ és csupa passz esetén is;
  - a passz és a továbblépés pontozási hatása azonos.

  A végképernyőn megjelenő érték állandó befejezési jelző, nem teljesítménypontszám. Ezért a címkéje semleges („Befejezve:”), és a grade item a tanulók elől rejtett.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| C5-01 | C-VÁLASZTÓ: „kvucát” → „kvucával” | M6.4 | alkalmazva | projektgazdai utasítás |
| C5-02 | a napzárás elve (a meglévő M6.4 C-elv) minimális mondatként | M6.1 energizer-kártya | alkalmazva | forrásellenőrzés: a 3. item elve („fáradt napzárás → rövid, kis intenzitású lezárás”) csak az M6.4 5C-J/5C-K-ban állt; az M6.1 energizer-kártyája ma azt írja, hogy az energizer „felrázza a fáradt kvucát” — az új mondat az M6.4 C meglévő elvét viszi át (5C-J kockázatai + 5C-K) |
| C5-03 | 3. item visszajelzés-forrás | M6 kapu | alkalmazva | forrás: M6.1 új mondata + M6.3 SLIDE 3 közös plakát; az M6.4 C opcionális példa; ✅ B, szár változatlan |
| C5-04 | 10. item: címsor, A opció szövege, visszajelzés | M6 kapu | alkalmazva | forrásellenőrzés: az elv az M6.1-ben már kötelező (:627 „ülve is játszhat”; SLIDE 7 :1242 „legyen mód lassabban vagy ülve, jelzéssel is részt venni”); a C-only „energiatakarékos üzemmód” címke és a C-only „mini-kör” kikerült; ✅ = A, szár változatlan |
| C5-05 | lefedettségi tábla és ismétlési útvonal | M6 kapu | alkalmazva | 3. item → M6.3 is; 10. item → M6.1 is |
| C5-06 | M3.3 meta (eszköz, completion) | M3.3 | alkalmazva | a hub „Branching végigvitele döntésekkel” kritériuma megmaradt, a mechanizmus hozzáadva |
| C5-07 | M3.3 §3: csomóponttérkép + BS-beállítások + pontozás | M3.3 | alkalmazva | 20 csomópont; P1–P4 passz-választó a §7.1 szövegével; biztonsági csomópont passz után is; S2-nek nincs doboza, így csomópontja sincs; SAFE-4: C → S1-K2; statikus végpontszám; a pontozási stop-feltétel nem teljesül |
| C5-08 | M3 hub szerkezeti sor | M3 hub | alkalmazva | „3–4 szituáció” → 4 szituáció, egyetlen BS-befoglaló |
| C5-09 | M2.3 asset-spec + §3 completion | M2.3 | alkalmazva | a checkpoint-tartalékút kikerült; D-j-megjegyzés a pillérválasztásról; @asset-spec változott → build |
| C5-10 | M2 hub tartalékút-mondat | M2 hub | alkalmazva | |
| C5-11 | M5.2 completion (körbehivatkozás) | M5.2 | alkalmazva | a feltétel a lecke forrásából (1 ág + SLIDE 7–9), nem gyengült |
| C5-12 | M4.3, M4.4 completion | M4.3, M4.4 | alkalmazva | a szigorúbb, profil szerinti irány (mini-kvíz grade) |
| C5-13 | H5P-C profil completion-cellája (BSPEC-06) | MAN §1 | alkalmazva | „Hide summary slide” = No (elsődleges forrás) |
| C5-14 | LMS-M2-04, -M3-03, -M5-02, -M4-03, -M4-04 completion | MAN §2 | alkalmazva | |
| C5-15 | ASSIGN-S profil: SUBMITTED / CONFIRMED | MAN §1 | alkalmazva | |
| C5-16 | ASSIGN-S sorok + új GATE-CP sorok + LMS-M7-07/-06 unlock | MAN §2 | alkalmazva | új sorok: LMS-M2-10, LMS-M4-10, LMS-M7-11, LMS-Z-08 (BUILD_OUTPUT 70 → 74); az LMS-M7-06-hoz v1-megerősítési feltétel nem került (a kánon nem írja elő) |
| C5-17 | §4 modul-completion + kurzusteljesítés + checkpoint-bekezdés | MAN §4 | alkalmazva | az „M2/M4 complete” Grade-feltétellel; a „checkpoint-út” tartalékmondat kikerült |
| C5-18 | BSPEC-05/06/07 → `BUILD_SPEC_RESOLVED` | MAN | alkalmazva | `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` (build-spec blockers: 0) |
| C5-19 | runtime acceptance 1., 3., 9., 10., 11., 18., 19. pont | RT | alkalmazva | az M33-IMPL-4 negatív és a SAFE-5 pozitív esetei; D-g visszanyitás |
| C5-20 | D-d / D-i átvezetése a BSPEC-06 lezárásához | M7.4 :14; M2.2 :31; M2 hub | alkalmazva | az M7.4 még „nyitott”-at írt (IMPL-8 kánoni maradványa); az M2.2 és az M2 hub az értékválasztást completion-elemnek írta |

## Célzott újraellenőrzés (a diff-hunkokra) és a hurokzáró javítások

Négy lencse futott a Command 5 diff-hunkjain: biztonsági, értékelési, implementációs és nyelvi. A Command 5 saját szerkesztésében talált objektív hibákat ugyanebben a futásban javítottam (hurokzáró szabály); utójavító kör nincs.

| ID | lencse | hely | állapot | megjegyzés |
|---|---|---|---|---|
| C5-BIZT-1 | biztonság | M3.3; RT 11.; BSPEC-05 | alkalmazva | „Review attempts” (`reviewmode`) = „Participants cannot review their own attempts”; enélkül a tanuló a saját riportjában kérdésenkénti pontot látna |
| C5-BIZT-2 | biztonság | RT 11. bevezető; M3 hub §6 | alkalmazva | a passzolt út (SAFE-1) is beszámít |
| C5-BIZT-3 | biztonság | M3.3 attempt tracking | **megállva: emberi döntés** | tárolhatja-e a próbálkozás-riport a passz-választást (DPO/Memuna); a completion nem használja |
| C5-ERT-1 | értékelés | M6 kapu 3. item visszajelzése | alkalmazva | a csak a C-ágban szereplő „kis játékosság” kikerült |
| C5-ERT-2 | értékelés | M6 kapu 10. item címsora | alkalmazva | semleges címsor, nem árulja el a választ |
| C5-IMPL-1 | implementáció | MAN §4 checkpoint-bekezdés | alkalmazva | „nem completion a puszta leadás” → „nem elég a megerősített teljesítéshez (CONFIRMED)”: ellentmondott a SUBMITTED = `completionsubmit` szabálynak |
| C5-IMPL-2 | implementáció | MAN §1 GATE-CP; MAN §4 kurzusteljesítés; RT 8. | alkalmazva | a négy új CONFIRMED sor a GATE-CP hatókörében és az RT 8. állapotmátrixában; a negatív esetek az 1., a 8. és a 12. pontban |
| C5-IMPL-3 | implementáció | M2.2 :31; M4.3 :20; M4.4 :26 | alkalmazva | az eredményt a Course Presentation az összefoglaló dián küldi el („Hide summary slide” = No), a H5P-C profillal egyezően |
| C5-IMPL-4 | implementáció | M2.3 3. szakasz | alkalmazva | „Navigate back” = be (a BSPEC-05 közös mintája) |
| C5-IMPL-5 | implementáció | MAN LMS-M7-11; BSPEC-07 | **részben alkalmazva**: a nyitási szemantika nem változott | a javasolt kivétel (az LMS-M7-11 ne legyen az „M7 megerősítve” eleme) a kánont gyengítené: a v1 completionjéhez tényleges tartalom kell (M7 KAPU: az üres sablon nem completion), és az M7 sor a Command 5 előtt is tartalmazta a „v1 folyamat” elemet. Ezért csak az LMS-M7-11 sora és a BSPEC-07 soronkénti unlock-listája mondja ki, hogy a v1 completionje az „M7 megerősítve” és az „M7 complete” eleme |
| C5-IMPL-6 | implementáció | MAN LMS-M2-10, -M4-10, -M7-11, -Z-08 | alkalmazva | a már megerősített „Teljesítve” értéket a későbbi önkéntes újrabeadás nem rontja le (§1, GATE-CP) |
| C5-IMPL-7 | implementáció | MAN BSPEC-05; RT 11.; M3.3 | alkalmazva | a puszta „§7.1, §7.2” hivatkozás a döntési jegyzőkönyvre (7.1. és 7.2. szakasz), illetve az `Emberi jóváhagyás szükséges.md` 11. szakaszára mutat |
| C5-NYELV-1 | nyelv | M6 kapu 10. item visszajelzése | alkalmazva | a napzárási minősítő visszakerült („Ha napzáráskor néhányan már nagyon fáradtak…”); forrás: M6.1 „Napzáráskor” energizer-kártya + a meglévő „legyen mód lassabban vagy ülve…” mondat; ✅ = A, szár változatlan |
| C5-NYELV-2 | nyelv | M6 kapu 3. item | már alkalmazva | a C5-ERT-1 javítása után a szöveg „pontot tesz a mondat végére” |
| C5-NYELV-3 | nyelv | M6 kapu 3. item forrássora | alkalmazva | egységes hivatkozási alak |
| C5-NYELV-4 | nyelv | M2.3 3. szakasz | alkalmazva | hiányzó alany: „A tanuló minden ág végén visszatérhet…” |
| C5-NYELV-5 | nyelv | M4.3 :20 (és ugyanígy M4.4 :26) | alkalmazva | „– +” → „–, valamint” |

## Záró futás

- Pin: egyetlen `--pin-visible` (14 fájl).
- Média: `media_manifest.py build` kétszer, azonos kimenettel; `check`: 10 generált kimenet naprakész, 747 történeti sor egyeztetve.
- `py_compile` OK; `content_integrity.py` 0 hiba; `--selftest` 57/57; `unittest tools.test_media_manifest`: 159 teszt OK; `git diff --check` és a PR-tartomány `--check`-je tiszta.
- `--release-report`: `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` (build-spec blockers: 0); `LEARNER-RELEASE-VERDICT: NO-GO` (learner-release blockers: 7; BUILD-OUTPUT 74).
- Nem került lezárásra (bizonyíték-kapu, illetve emberi döntés): a célverziós runtime-bizonyíték, a Memuna/DPO/final QA, a SAFE-7, az A11Y-15/18 bizonyítéka, a cmid-ek és a build-kimenetek, valamint a C5-BIZT-3.
- Nem commitolva, nem pusholva.
