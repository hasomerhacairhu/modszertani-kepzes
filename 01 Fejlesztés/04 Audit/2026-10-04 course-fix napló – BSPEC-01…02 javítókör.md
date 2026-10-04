# course-fix napló — BSPEC-01…02 javítókör (2026-10-04)

> **Audit trail, nem kánon.** A 14 scope-onkénti, read-only `/course-review` utáni javítókör lépésenkénti naplója.
> Bemenet: a projektgazda deduplikált, validált findinglistája (A–M; szó szerint lent, a „Bemenet” szakaszban). Döntési
> források: BS-D1…D6, BS-D8 (`2026-10-04 Projektgazdai döntések – BSPEC-01…04 maradék.md`), Q-REL-2, RM-D6 (HUM 10.
> szakasz). Evidence (nem kánon): `2026-10-04 Moodle-kutatás – BIZT-1, GATE_CONFIRMED tartalékút, IMPL-8.md`. Bázis:
> `e980a70`, munkaág `fix/moodle-build-hardening`. Rövidítések: M = `02 Tervezet/LMS – activity manifest.md`,
> RA = `02 Tervezet/LMS – H5P runtime acceptance.md`, PT = `02 Tervezet/Program terv.md`.

## Elsődleges források, amelyeket ez a kör ellenőrzött (2026-10-04)

- Feedback, nem anonim, „Allow multiple submissions” = Yes: az űrlap a tanuló utolsó válaszával töltődik ki
  (`mod/feedback/classes/completion.php`, `create_completed_tmp_from_last_completed()`), az újabb beküldés ugyanazt a
  rekordot frissíti, a régi értékeket törli (`mod/feedback/lib.php`, `feedback_save_tmp_values()`: „first drop all
  existing values … update the current completed”); „multiple_submit = 0” mellett a második beküldés tiltott
  (`can_submit()`). `MOODLE_405_STABLE`.
- Feedback-válaszok megtekintése: `mod/feedback:viewreports` mindig; a `viewanalysepage` csak bekapcsolt „Show
  analysis page” mellett (`feedback_can_view_analysis()`, `mod/feedback/lib.php`, `MOODLE_405_STABLE`).
- Kurzusteljesítés activity-kritériuma: csak `COMPLETION_COMPLETE` vagy `COMPLETION_COMPLETE_PASS` teljesíti, a
  `COMPLETION_COMPLETE_FAIL` nem (`completion/criteria/completion_criteria_activity.php`, `review()`,
  `MOODLE_405_STABLE`).
- „Receive a grade”: bármely jegy teljesít; a „Receive a passing grade” ezzel együtt használható külön feltétel
  (`docs.moodle.org/405/en/Activity_completion_settings`).

## Eltérés a bemenettől (a fájlban igazolva)

- **BSPEC-02 leltára a bemenetben felsoroltnál bővebb.** Read-only leltár (Explore-agent, majd a fő session
  szúrópróbája) szerint kötelező szabad szöveg van TEXT-C sor nélkül: M1.3 :926 „Csak **completion**: ha mindhárom
  mezőben van valami, „kész”.”; M2.2 :507 „ez a „kötelező kérdés””, M2 hub :183 „M2.2 = … a nyitott mezők ki vannak
  töltve”; M2.4 :584 „A Moodle-be csak ezt az egy, **nem érzékeny** mondatot add be”, M2 hub :183; M7.1 :540 „ehhez
  manifest-sor is kell”. Valószínű még: Z.1 :453, Z.2 :276 (minimális karakterszám). Ezek nem validált findingok (a 14
  scope-on kívül estek, és a projektgazda mezőnkénti nyolcszempontos vizsgálatot írt elő), ezért ez a kör nem hoz rájuk
  sort; a BSPEC-02 emiatt `BUILD_SPEC_OPEN` marad, a maradék hatókör a nyilvántartásban.
- **Az M7 v2 nyitásának kötése.** M §4 :151 „ha a kvíz összetett feltétele nem kódolható bizonyítottan, a v2 restrict
  accessét is kézi stáb-checkpointhoz kell kötni”, RA 8: a kvíz feltétele „skalár küszöbbel **nem is kódolható**”. A
  stáb-checkpoint tehát a kánon szerint kötelező, csak a sora hiányzott; az E finding („Peula v2 … remains blocked”) és a
  D („one deterministic core-Moodle primary mechanism”) determinisztikus megvalósításához ez a kör felveszi: LMS-M7-09
  (GATE-CP). Vétólistán.
- **Az újraértékelés „downstream feloldás előtt” zárópontja (BS-D2, H).** A BS-D2 kifejezetten előírta, hogy ez a
  szövegezés minden érintett helyen egyértelmű legyen; a PT :290 és öt KAPU-fájl ma a *következő modul* feloldását nevezi
  zárópontnak, ami a Q-REL-2 mellett lehetetlen (a következő modul a megerősítéssel nyílik). A H finding („Align this
  with Program terv's second-review/re-evaluation rules”) keretében átvezetve.
- **M3.1 / M3.2:** a bemenet (2. pont) szerint a reflexió opcionális marad; új sor nincs.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| F01 | A: TEXT-C profil → Moodle Feedback, „Longer text answer” | M §1 | alkalmazva | Feedback-forráskód ellenőrizve (fent); „Allow multiple submissions” = Yes minden TEXT-C-nél, mert a BS-D4 szerinti emberi ellenőrzés bármelyik sornál javítást kérhet |
| F02 | D+H: GATE-CP profil: rögzített beállítások, módosíthatóság, láthatóság, kurzusteljesítés | M §1 | alkalmazva | a profil az LMS-M7-09-re és az LMS-Z-07-re is szól |
| F03 | A+B: §2 bevezető — TEXT-C sorok listája, Moodle-oldali kísérő activity | M §2 | alkalmazva | |
| F03b | A (következmény): hozzáférhetőségi sztenderd §6, 1. út — Assignment online text helyett Feedback | a11y-sztenderd | alkalmazva | a TEXT-C profil erre hivatkozik |
| F04 | A: §5 — a Feedback kézi létrehozása a TEXT-C-re is | M §5 | alkalmazva | |
| F05 | B: LMS-M2-04 completion + új LMS-M2-07 | M §2 | alkalmazva | |
| F06 | B: LMS-M4-04 completion + új LMS-M4-09 | M §2 | alkalmazva | az LMS-M4-05-tel nincs összevonva |
| F07 | B: M3.1 :686 — opcionális, nem completion | M3.1 | alkalmazva | |
| F08 | B: M3.2 :747 — opcionális, nem completion | M3.2 | alkalmazva | |
| F09 | B+L: M2.3 :44 — a záró mondat helye: LMS-M2-07 | M2.3 | alkalmazva | |
| F10 | B+L: M4.4 :26 — a vázlat helye: LMS-M4-09 | M4.4 | alkalmazva | az F11-gyel egy `Edit`-ben (szomszédos sorok) |
| F11 | L: M4.4 :27 — „a H5P-ben elkészített” | M4.4 | alkalmazva | → „a leckében elkészített” |
| F12 | L: M4.4 :68 — alapértelmezett út | M4.4 | alkalmazva | |
| F13 | L: M4.4 :677 — „ide írd le a H5P-be” (tanulói) | M4.4 | alkalmazva | → „írd le a lecke szövegmezőjébe” |
| F14 | L: M4.4 :725 — „a H5P-mező tartalma” | M4.4 | alkalmazva | |
| F15 | C: LMS-Z-06 sor (BS-D8, BS-D6) | M §2 | alkalmazva | a megőrzési sor nyitva, DPO (BS-D6) |
| F16 | C: új LMS-Z-07 sor | M §2 | alkalmazva | GATE-CP technikai profil; „ha a tanuló az elfogadás után módosít, a mentor újraellenőriz” — a BS-D8 következménye (a Feedback felülírható), vétólistán |
| F17 | C: §4 Z sor | M §4 | alkalmazva | |
| F18 | C+L: Z.3 :57 — alapértelmezett út, LMS-Z-06 | Z.3 | alkalmazva | |
| F19 | C+L: Z.3 :232–234 — 4. dia mezője | Z.3 | alkalmazva | „Beágyazott kérdés” → „Kérdés” (csak a három kötelező mezőnél) |
| F20 | C+L: Z.3 :285–287 — 6. dia mezője | Z.3 | alkalmazva | |
| F21 | C+L: Z.3 :302–304 — biztonsági lépés | Z.3 | alkalmazva | + egy tanulói mondat a mentori átnézésről és az elfogadásról (BS-D8; a JIT „ki látja” pontja) — vétólistán |
| F22 | C: Z hub — minimális teljesítés + mentori elfogadás | Z hub | alkalmazva | |
| F23 | C: Adatvédelem §3 — LMS-Z-06 megőrzése DPO-döntés (BS-D6) | Adatvédelem | alkalmazva | + a TEXT-C activityk adatleltára mint review-tétel; nem checklist-sor |
| F24 | D: §4 „Fontos” — mechanizmus, „nincs tartalékút” | M §4 | alkalmazva | „Mx complete” = Grade-feltétel ≥ 50 % |
| F25 | D+E: §4 — a v2 nyitása LMS-M7-09-hez | M §4 | alkalmazva | |
| F26 | D+E: új LMS-M7-09; LMS-M7-06 unlock; LMS-M7-07 megjegyzés | M §2 | alkalmazva | vétólistán (új build-sor, lásd „Eltérés”) |
| F27 | E: LMS-M7-08 sor (BS-D3) | M §2 | alkalmazva | |
| F28 | E: §4 M7 sor | M §4 | alkalmazva | |
| F29 | E: M7 KAPU :27 | M7 KAPU | alkalmazva | |
| F30 | E: M7 KAPU :416 | M7 KAPU | alkalmazva | |
| F31 | F: M1.4 :496 (tanulói) | M1.4 | alkalmazva | |
| F32 | G: M0 belépőkvíz 4. item D) + visszajelzés | M0 hub | alkalmazva | a D) szövege a projektgazda javaslata szó szerint; kérdés, C) és kulcs változatlan |
| F33 | G: M0 belépőkvíz forrássora — BS-D5 | M0 hub | alkalmazva | |
| F34 | H: §4 újraértékelés — BS-D2 zárópont | M §4 | alkalmazva | + a checkpoint visszakereshető módosítása |
| F35 | H: PT :290 — BS-D2 zárópont | PT | alkalmazva | |
| F36 | H: M1 KAPU :25 | M1 KAPU | alkalmazva | zárópont: az M3 kapufeladata |
| F37 | H: M3 KAPU :36 | M3 KAPU | alkalmazva | zárópont: az M5 modulproduktuma |
| F38 | H: M5 KAPU :27 | M5 KAPU | alkalmazva | zárópont: az M6 játéklapja |
| F39 | H: M6 KAPU :42 | M6 KAPU | alkalmazva | zárópont: az M7 felkészültségi kvíze |
| F40 | H: M7 KAPU :29 | M7 KAPU | alkalmazva | zárópont: az online félév teljesítése |
| F41 | I: LMS-M3-05 szerepek | M §2 | alkalmazva | |
| F42 | I: LMS-M3-07 szerepek | M §2 | alkalmazva | |
| F43 | I: §4 :155 szerepek | M §4 | alkalmazva | |
| F44 | J: LMS-M5-07 sor | M §2 | alkalmazva | két `Edit` (unlock + megjegyzés vége) |
| F45 | J: §7 — késleltetett felidézés | M §7 | alkalmazva | |
| F46 | J: M5.3 :516 | M5.3 | alkalmazva | |
| F47 | J: M5.3 :518–521 „Megvalósítás” — értesítés nélkül | M5.3 | alkalmazva | a „Moodle Reminder” ígéret kikerült |
| F48 | J: M5.3 — tartalékút tanulói mondata | M5.3 | alkalmazva | új tanulói mondat, vétólistán |
| F49 | J: M5.3 :674 | M5.3 | alkalmazva | |
| F50 | J: M5 hub :191 | M5 hub | alkalmazva | |
| F51 | K: RA 4 | RA | alkalmazva | |
| F52 | K: RA 6 — a TEXT-C (Feedback) tesztjei | RA | alkalmazva | |
| F53 | K: RA 8 — GATE-CP állapotmátrix | RA | alkalmazva | kilenc eset + a beállítások visszaolvasása |
| F54 | K: RA 10 — az M2.3 záró mondata | RA | alkalmazva | |
| F55 | K: RA 12 — Z.3 két állapot | RA | alkalmazva | |
| F56 | K: RA 15 — Feedback-nézetek | RA | alkalmazva | |
| F57 | BS-D1…D6, BS-D8 átvezetése a HUM 10. szakaszába | HUM | alkalmazva | a jobb oldali szerep a szülődöntés meglévő ellenőrzőjéből, forrásmegjelöléssel; a BS-D4-nél nincs |
| F58 | M: BSPEC-01 → `BUILD_SPEC_RESOLVED` | M | alkalmazva (szöveg) | az állapotváltás és a hash a követő nyilvántartási commitban, a megoldó commit után |
| F59 | M: BSPEC-02 → `BUILD_SPEC_OPEN`, frissített maradék | M | alkalmazva | a leltár-maradék tételesen |
| F60 | M: BSPEC-03 javított hivatkozás | M | alkalmazva | + BSPEC-04 (BS-D2 pontosítás) |

**Fájlcsoport vége:** `content_integrity.py` 0 ERROR; `git diff --check` tiszta; `media_manifest.py check` és
`reconcile` OK; a média-tesztek közül a látható-szöveg pin a várt módon bukik (újrapinnelés a végén).

## Célzott újraellenőrzés a diff-hunkokon (2026-10-04)

Négy read-only reviewer csak a módosított sorokon (implementation, safety-policy, assessment, hungarian-editorial).
Verifier nem futott. A projektgazda utasítása szerint („Fix any regressions those narrow reviews find”) a futás a saját
diffje által okozott vagy felszínre hozott objektív hibákat javította; az emberi döntést igénylő tételek csak ide kerültek.

**Javítva (objektív, a diff hibája vagy közvetlen következménye):**

| ID | Lényeg | Javítás |
|---|---|---|
| BIZT-R1 / IMPL-R4 (rész) / ERT-R5 (rész) | az LMS-Z-07-be kitalált szabály került: „ha a tanuló az elfogadás után módosít, a mentor újraellenőriz” (a BS-D8-on túlmegy) | a mondat törölve a manifestből és az RA 12-ből; a kérdés emberi döntésként lent |
| BIZT-R4 / IMPL-R5 | az M4.4 :704 mező melletti megjegyzése a modul beadandójának nevezte a vázlatot, a TEXT-C szerint ez szó szerint a JIT-be kerülne | „ez a vázlat a modul beadandójának első változata …”; „beadandódat” → „vázlatodat”; a védő szabály változatlan |
| BIZT-R6 | a TEXT-C nevesítésének indoklása hamis volt („mert a completion fiókhoz kötött”) | indoklás: a BS-D4 szerinti, tanulóhoz kötött ellenőrzés és javítás, a saját válasz felülírása |
| BIZT-R5 (rész) | az LMS-M2-07 megjegyzése eldöntötte, hogy a mondat nem világnézeti adat | az osztályozó tagmondat törölve; a kérdés emberi döntésként lent |
| BIZT-R7 | a HUM 10 BS-D6 sorában a nyitott döntés gazdája a vétó-oszlopban állt | „— (nyitott DPO-döntés; gazdája a DPO)”; a RELEASE-READINESS G2 sorában nevesítve (csak nyilvántartás) |
| BIZT-R9 / IMPL-R9 / NYELV-R4 | a Z.3 tanulói mondata csak a 3. válaszról és az újrabeküldés nélkül szólt | „Ezt a választ és a 4. és a 6. dián írtakat a mentorod átnézi … kiegészíted, és újra beküldöd …” |
| IMPL-R1 | az online félév Moodle-beli kódolása (course completion) nem volt rögzítve | §4: „Az online félév teljesítése Moodle-ben” blokk |
| IMPL-R3 | „Feedback comments” nem volt a GATE-CP beállításai között | GATE-CP profil + RA 8 visszaolvasás |
| IMPL-R5 (rész) | M4.4 :664 és M2.3 :880 a mezőt a dián írta le | mindkettőhöz: alapértelmezett helye a Moodle-oldali mező (LMS-M4-09 / LMS-M2-07) |
| IMPL-R6 / NYELV-R10 | az LMS-M7-08 megjegyzése a v2-t LMS-M7-09-ként azonosította | „a v2 leadása (LMS-M7-06; feltétele az LMS-M7-09)” |
| IMPL-R7 | az M2.3 ág-specifikus mini-reflexiói kimaradtak a BSPEC-02 nyitott listájából | felvéve a „tisztázandó státuszú mezők” közé |
| IMPL-R8 | az új TEXT-C sorok terjedelmi elvárását a Moodle nem ellenőrzi | LMS-M2-07, LMS-M4-09: „a terjedelmet / a mondatszámot a Moodle nem ellenőrzi, BS-D4” |
| IMPL-R10 | az a11y-sztenderd új mondata a Z.4 Assignmentet is kizárhatta | a mondat a lecke melletti mezőre szűkítve; a beadandó produktumok Assignmentben maradnak |
| ERT-R1 | az M5.4 :320 tanulói mondata még a következő modul megnyílását nevezte zárópontnak (BS-D2 kimaradt) | „még mielőtt az M6 játéklapja megnyílik (az M6 leckéi … már megnyílnak)” |
| ERT-R2 | a „complete, fail” kurzusteljesítési viselkedése csak 4.5-ön volt ellenőrizve | `MOODLE_502_STABLE` `review()` ellenőrizve (ugyanaz); a hivatkozás mindkét ágat nevezi; a „Receive a grade” marad (a D finding rögzíti) |
| ERT-R3 | az M0 hub :143 az F-peulát „vagy más javítási út”-ként írta le, az új D-visszajelzéssel ellentétben | „a kötelező F-peula (javítási út)”; kérdés, C, kulcs, disztraktorok változatlanok |
| ERT-R4 | az RA 8 mátrixa az LMS-M7-09-re és az LMS-Z-07-re nem adott várt eredményt | activitynkénti várt eredmény az RA 8-ban |
| ERT-R6 | az LMS-Z-07 elfogadásának nem volt megfigyelhető eleme | a Z.3 mezőnkénti elemei szó szerint, új kritérium nélkül |
| ERT-R9 / NYELV-R8 | M1 és M6 KAPU: nem létező PT-címre hivatkozás („kizáró kapukon”) | „Újraértékelés az éles kapukon” |
| NYELV-R1 | az M5.3 tartalékúti tanulói mondata a 72 óra után visszatérőt is halasztásra utasította | „Ha még nem telt el legalább 72 óra (3 nap) azóta, hogy befejezted az M5.3-at, …” |
| NYELV-R2 | M1.4: fejlesztői metanyelv a tanulói mondatban | „Az M3 kapufeladata viszont csak akkor nyílik meg …”; „eredményed” |
| NYELV-R3 | M4.4: „a lecke szövegmezője” nem mondta meg, hol a mező | „az „M4.4 – A vázlat első változata” szövegmezőbe” |
| NYELV-R5, R6, R7, R9, R11, R12b | névmási előzmény (a11y), alany nélküli mondat, „feloldás” a teljesítésre, „50 %” → „50%”, csonka nyilvántartási mondatok, „primary út” | javítva a saját diff soraiban |

**Nem javítva — emberi döntés vagy hatókörön kívül (a jelentésbe):**

| ID | Kérdés | Ki dönt |
|---|---|---|
| BIZT-R1 / ERT-R5 / IMPL-R4 | az elfogadott LMS-Z-06 válasz utólagos felülírása: zárolás, a „Teljesítve” visszaírása (a GATE-CP „nem ronthat le” szabályának kivétele) vagy értesítés a mentornak | projektgazda, Memuna-vétóval; értékelési felelős |
| BIZT-R2 | az LMS-Z-07 elfogadási minimuma a biztonsági lépésnél (pl. a mentornak jelzés vs. a Memunának jelzés) | Memuna + értékelési felelős |
| BIZT-R3 | a „kijelölt mentor/értékelő” láthatóságának tanulónkénti mechanizmusa (a capability-override szerepkör-szintű; a csoport a BS-D1 miatt nem) — minden P2 activityre, nem csak a TEXT-C-re | DPO/jogi felelős (HUM-PRIV-01) |
| BIZT-R5 | kötelező, nevesített, tárolt mező lehet-e az LMS-M2-07 (pillér-ágban hozott döntésről szóló mondat) | DPO/jogi felelős; someres vonatkozásban a projektgazda |
| BIZT-R8 | a BS-D8 Memuna-vétója döntésszintű vagy egyedi elfogadásra is vonatkozik (és akkor milyen hozzáféréssel) | projektgazda + Memuna; hozzáférés: DPO |
| BIZT-R10 | az LMS-Z-06 2. kérdése harmadik személy nevét kéri: elég-e a szerep | DPO (a BS-D6-tal együtt) |
| IMPL-R2 / ERT-R8 | az LMS-M7-09 megerősítési határideje (a kvíz és a v2 határideje azonos) | programvezető (HUM-OPS-01); a manifest sorában jelölve |
| ERT-R7 | bukott eredménynél az újraértékelés viszonya az F-peulához és a javító próbálkozáshoz | programvezető + értékelési felelős |
| NYELV-R12a | a „kétszemes” terminus háromszereplős (M3) döntésre; egységes csere 10 helyen | `/hungarian-edit` (PT §5-tel kezdve) |
| NYELV-R13 | „min. 3–5 mondatos”: alsó határ 3 vagy sáv | értékelési felelős / projektgazda |

## Bemenet — a projektgazda validált findinglistája (szó szerint, 2026-10-04)

> ## 2. Critical correction from the review
>
> DO NOT create new mandatory stored-text activities for M3.1 or M3.2.
>
> Both reflections are explicitly optional in their lesson specs. The stale text that says they count for completion is the bug.
>
> Correct fix:
>
> - M3.1: preserve the reflection as optional and remove/correct the stale completion dependency.
> - M3.2: same.
>
> This supersedes the earlier assumption that M3.1/M3.2 needed new mandatory TEXT-C activities.
>
> ## 3. Deduplicated validated findings
>
> ### P1 / build blocking
>
> #### A. BIZT-1 / BSPEC-02
>
> The current `TEXT-C = Moodle Assignment online text` does not satisfy the project's strict fileless-input requirement.
>
> The repo's primary-source Moodle research already established this.
>
> Use a genuinely fileless core Moodle primitive for normal non-assessment free-text inputs.
>
> Recommended final primitive:
>
> **Moodle Feedback + Longer Text Answer**
>
> Important required behavior:
>
> - plain textarea, no editor/file picker
> - non-anonymous where learner identity/completion must be tracked
> - required question where the source says mandatory
> - show-analysis page disabled
> - student access to analysis prohibited
> - least-privilege response visibility
> - JIT privacy notice
> - resubmission enabled where correction is required
>
> The repo's research note is evidence, not automatically canon. Integrate the final solution coherently into manifest/runtime/privacy specs.
>
> #### B. Missing mandatory text activities
>
> Add:
>
> - new `LMS-M2-07`: M2.3 required closing response
> - new `LMS-M4-09`: M4.4 required 3–5 sentence lesson-closing draft
>
> Do NOT add M3.1/M3.2 rows.
>
> Existing rows that remain necessary but must migrate away from Assignment-based TEXT-C:
>
> - `LMS-M2-06`
> - `LMS-M4-06`
> - `LMS-M4-07`
> - `LMS-M4-08`
> - `LMS-Z-06`
>
> M4.4 has two distinct artifacts:
>
> 1. the lesson-closing 3–5 sentence free-text draft
> 2. the later module-product Assignment (`LMS-M4-05`)
>
> Do not merge them.
>
> #### C. BS-D8 / Z.3 two-state model
>
> Implement the already approved BS-D8 decision.
>
> Separate:
>
> 1. learner submission
> 2. semantic mentor acceptance
>
> `LMS-Z-06`:
> - contains the three required Z.3 text responses
> - fileless/privacy-safe
> - submission is mandatory
> - submission allows the learning flow to continue
> - non-empty does NOT imply semantically adequate
>
> Add a separate staff-controlled state, preferably a new stable build ID such as:
>
> `LMS-Z-07`
>
> Purpose:
>
> mentor acceptance of the Z.3 safety/commitment content.
>
> Final Z / online-semester completion requires mentor acceptance.
>
> If mentor rejects:
> - learner corrects
> - resubmits
> - mentor rechecks
>
> Do not invent automatic semantic validation.
>
> Memuna safeguarding veto remains intact.
>
> Retention classification for `LMS-Z-06` is NOT ours to invent. See BIZT-7 / BS-D6 below.
>
> #### D. BSPEC-01 GATE_CONFIRMED
>
> Remove the Group/grouping fallback completely.
>
> BS-D1 already rejected it.
>
> Use one deterministic core-Moodle primary mechanism:
>
> `GATE-CP = Moodle Assignment with all submission types disabled, grading only`
>
> Pin the settings explicitly:
>
> - scale values:
>   1. `Még nem teljesítve`
>   2. `Teljesítve`
> - `Grade to pass = 2`
> - `Marking workflow = Off`
> - anonymous submissions = Off
> - grade item visible
> - grade item unlocked
> - automatic completion = `Receive a grade`
> - staff writes the value through the intended grading interface
> - student cannot submit anything to this activity
>
> Define:
>
> `Mx megerősítve`
> = checkpoint has any grade/value, fail or pass.
>
> This opens the next module's learning portion under Q-REL-2.
>
> `Mx complete`
> = checkpoint has the passing value `Teljesítve`.
>
> This gates success-dependent/high-stakes progression and final completion.
>
> Prefer deterministic Grade conditions where required rather than relying on fragile generic activity-completion semantics.
>
> #### E. M7 early-fail state
>
> Current `LMS-M7-08` is wrong because it says staff fills it only after BOTH the M7 quiz and Peula v2 have been evaluated.
>
> BS-D3 requires:
>
> If the M7 readiness quiz has a confirmed failing result before v2 exists:
>
> `LMS-M7-08 = Még nem teljesítve`
>
> must already be recordable.
>
> Effects:
>
> - this is NOT M7 completion
> - Q-REL-2 may open Z learning
> - Peula v2 / high-stakes completion remains blocked
> - online/program completion remains blocked
> - correction/F-peula/retry continues normally
>
> After successful correction and completion of the full conjunctive M7 gate, the checkpoint may become `Teljesítve`.
>
> Update both manifest and M7 KAPU wording, including the stale logic around approximately lines 27 and 416.
>
> #### F. Q-REL-2 learner-facing regression
>
> Fix M1.4 around the current line ~496.
>
> Current stale meaning:
>
> M2 opens only after an M1 passing result.
>
> Correct meaning:
>
> M2 learning opens after the M1 gate result is **confirmed**, including confirmed `Még nem teljesítve`.
>
> High-stakes success-dependent progression remains blocked until M1 is actually complete.
>
> #### G. M0 quiz item 4
>
> Q-REL-2 made the current D distractor partially true.
>
> Do NOT change:
>
> - question
> - correct answer C
> - answer key
> - other distractors
>
> Replace only D and its feedback.
>
> Recommended D:
>
> `D) Elég ugyanazt újra beadnia; külön fejlesztő visszajelzésre és F-peulára nincs szükség.`
>
> Feedback should state that failed hard gates require developmental feedback and the required F-peula/correction route before the retry.
>
> ### P2 / objectively fixable
>
> #### H. GATE-CP mutability wording
>
> The current absolute statement that a `Teljesítve` checkpoint value can never be written back is too strong.
>
> Correct invariant:
>
> A learner's voluntary later retry must not downgrade an already confirmed pass.
>
> However authorized correction/re-evaluation by staff must remain possible with an audit trail.
>
> Align this with Program terv's second-review/re-evaluation rules.
>
> #### I. M3 blocking decision roles
>
> Where the M3 blocking decision is described, make the roles explicit:
>
> `mentor + második képző + Memuna`
>
> Do not use ambiguous wording that sounds like only two people with the Memuna somehow attached.
>
> #### J. M5.3 delayed retrieval
>
> Keep BSPEC-03 resolved at the decision level, but remove implementation ambiguity.
>
> Primary route must mean:
>
> `LMS-M5-03 complete AND relative +72h condition`
>
> Do not rely merely on the plugin having a timestamp.
>
> Plugin-free fallback:
>
> the recall activity may be visible after M5.3 completion, with explicit learner instruction to return after 72 hours.
>
> The fallback must NOT pretend Moodle technically enforces the delay.
>
> Do not promise a notification unless the target implementation/runtime proves one.
>
> The build must not wait for the plugin, per RM-D6.
>
> #### K. Runtime acceptance
>
> Update the runtime acceptance specification so it matches the final BSPEC-01/02 architecture.
>
> At minimum explicitly test the GATE-CP state matrix:
>
> 1. no checkpoint value
> 2. `Még nem teljesítve`
> 3. `Teljesítve`
> 4. fail → authorized pass after correction/re-evaluation
> 5. learner voluntary retry cannot downgrade confirmed pass
> 6. special M7 early quiz-fail state
> 7. next-learning unlock vs success-dependent unlock
> 8. learner sees only own result
> 9. correct mentor/teacher visibility
>
> Update the free-text tests to test the actual Feedback-based TEXT-C primitive, including:
>
> - file picker/editor absent
> - required field behavior
> - completion on submission
> - correction/resubmission where configured
> - student cannot see other learners' responses
> - only intended mentor/evaluator access
> - JIT notice visible before input
>
> For Z.3 explicitly test that submission and mentor acceptance are separate.
>
> #### L. H5P/free-text assumptions
>
> Remove wording that assumes required free text lives inside Course Presentation slides.
>
> Lesson specs may describe the pedagogical position of the input, but implementation must be compatible with Moodle-side companion activities.
>
> Do not weaken the requirement simply because the field moves outside H5P.
>
> #### M. BSPEC registry provenance
>
> The manifest says a resolved BSPEC row must cite its solving commit.
>
> Do not fabricate a future SHA.
>
> Implement the actual fixes first.
>
> When the implementation commit exists, update BSPEC-01/02 and any repaired BSPEC-03/04 provenance to point at the real solving commit, using a follow-up registry-only commit if necessary.
>
> ## 4. BIZT-7 / BS-D6: do not solve
>
> The retention classification for `LMS-Z-06` remains a DPO decision.
>
> Do NOT decide whether it belongs to:
>
> - free-text reflection / 90-day retention
> or
> - Assignment/peulaterv / 12-month retention
>
> Keep the ambiguity explicit and preserve the DPO gate.
>
> Do not invent policy.
>
> ## 5. Privacy constraints
>
> Preserve the current privacy canon:
>
> - P2 free text only visible to the designated mentor/evaluator where genuinely necessary
> - sensitive identity/family/health/safeguarding stories may not become mandatory learner artifacts
> - special-category/safeguarding data is not normal Moodle learning data
> - real safeguarding disclosures move to the separate safeguarding process
> - JIT notice must state purpose, visibility, retention, contact and relevant handling
> - actual role/capability behavior remains a staging runtime evidence requirement
>
> Do not claim runtime verification from repository text alone.
>
> ## 6. Moodle research constraint
>
> Exact target Moodle version is still:
>
> `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED`
>
> Research compatibility range:
>
> `Moodle 4.5–5.2`
>
> This is NOT a project decision and must NOT be turned into a fictional BS-D7.
>
> There is no BS-D7 decision.
>
> Keep BS-D1…D6 and BS-D8 as the actual project-owner decisions.
