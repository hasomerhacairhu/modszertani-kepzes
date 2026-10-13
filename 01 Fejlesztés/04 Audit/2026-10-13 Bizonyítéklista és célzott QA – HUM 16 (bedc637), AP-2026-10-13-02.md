# Bizonyítéklista a staginghez és a release-hez, célzott QA – HUM 16 (bedc637), AP-2026-10-13-02

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i nyolc döntésének átvezetése után (`bedc637`, média: `926adf3`)
> szerepenként felsorolja, milyen bizonyíték hiányzik még a staging deploymenthez és a learner release-hez, és rögzíti a
> diffre szabott célzott QA (QA18) eredményét. A repó egyiket sem állítja elő: a szerepköri döntést, a jóváhagyást és a
> runtime-eredményt a megnevezett szerep adja. Gépi állapot: `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` ·
> `LEARNER-RELEASE-VERDICT: NO-GO`.

## 1. Staging deployment

A gépi verdikt engedi a staging buildet. A tényleges deploymenthez kell:

- a projektgazda külön, kifejezett engedélye (ebben a futásban nem volt);
- a célkörnyezet (Moodle-példány, verzió, site-adminisztrátori hozzáférés); a valódi `SCHEDULE_TO_RESYNC` dátumok és
  kontaktok a staginghez nem kellenek: az RR G8 sora szerint RELEASE-EVIDENCE tételek, stagingben belső build-jelölő
  megengedett, és a dátumfüggő activity dátum nélkül is felépíthető (PILOT-2) (javítva 2026-10-13, AP-2026-10-13-03:
  az első változat ezeket tévesen staging-előfeltételnek írta);
- a staging-szabály: szintetikus tesztadat, személyes adat nélkül; emberi döntés helyén csak belső build-jelölő.

A Memuna, a DPO és az értékelési felelős jóváhagyása a staging buildnek nem előfeltétele; a staging runtime-tesztjei
viszont az ő bizonyítékaik alapja (lásd a 2. pontot).

## 2. Learner release – szerepenként

Gépi számok (`--release-report`, `bedc637`): POST-BUILD ellenőrzőlista 14, RELEASE-EVIDENCE 8, FINAL-RELEASE-QA 15,
SIGNOFF 4 nyitott; 76 feloldatlan `BUILD_OUTPUT`, 19 `RUNTIME_OUTPUT`, 38 nem `RUNTIME_VERIFIED` teszt; média: 1 asset
fallbacken (M0.3-FOTO-01), jogosultsági részkapuk: J1, J2, V1, V3 hiányzik.

### Memuna (G1; csomag: `2026-10-13 Jóváhagyási csomag – Memuna, AP-2026-10-13-01.md`)

- **Szerepköri döntések:** D-05 (sürgős: a 116-111 / 116-000 leírása, a HUM:471 formális újranyitása); D-01 (+ programvezető:
  megállítási protokoll, helyettes, két 18+ felnőtt, létszámnorma); D-04 (eszkaláció; az M6.4 6D/ZÁRÓ küszöbéről a HUM 16
  szerint szakmai review, módosítás külön jóváhagyással); D-08 (a) (+ programvezető: az M2.4 passz-útja); D-09 (+ DPO); D-10
  (+ DPO); D-13 (d) (+ DPO); a D-21 terv E1 (+ programvezető), E2 és 6–7. pontja.
- **QA és verdiktek:** a D-08 (b) előnézeti csomópont címei (különösen a 3. és a 4. szitu címe) megterhelők-e; GYV-3 helyenkénti
  verdikt (hét hely); GYV-6 küszöb (+ programvezető); PRG-12 (az M3.B 4. esetkártyája); az ADV-2 szerinti Memuna-hozzáférés
  módja; a mentor pontkönyvi rálátása az M0 belépőkvíz egyéni pontszámára (+ programvezető, adatkör: DPO).
- **Bizonyíték:** a G1 „átnéztem” bejegyzés egyazon végleges SHA-ra (GYV-24); a JOG-1 jóváhagyása a jogász ellenőrzése után
  (a #1 issue-ban).

### DPO (G2; csomag: `2026-10-13 Jóváhagyási csomag – DPO, AP-2026-10-13-01.md`)

- **Szerepköri döntések:** D-10; D-13 (b), (c) és az (e) megőrzési sora; D-14 (AI-adatfolyam); D-09 és D-13 (d) a Memunával; a
  D-21 terv E6-ja (+ programvezető: ki tarthatja az F-peulát, ki fér a kapueredményhez); az ADV-4 tárolásmentes technikája
  (a BK-05 runtime-visszaolvasás után, a Memunával); a FEEDBACK-N (Z.4) csoportmódja; LMS-Z-06, LMS-M2-07, LMS-M7-10
  (GDPR 9. cikk), LMS-M4-06/-08 (TEXT-C adatkör), ERT-42 adatvédelmi stop, ADV-6 fórum.
- **Vétó/QA:** a D-11 csoportszűkítés (az LMS-M0-06 override a `mod/quiz:grade`-re is; FORUM-C „No groups”), D-12, D-15 (b),
  (e), a D-16 Z.4-része.
- **Bizonyíték:** ADV-E1–E3 activitynkénti release-QA (adatmezők, szerepek, megőrzés, export, xAPI/LRS, saved-state, backup),
  teljes adatleltár, HUM-PRIV-04 AI-kapcsolat; a staging role-matrix visszaolvasásának átnézése (RA 15).

### Értékelési felelős (+ lektor, modulgazda; csomag: `2026-10-13 Jóváhagyási csomag – értékelési felelős, AP-2026-10-13-01.md`)

- **Szerepköri döntések:** D-16 jóváhagyása (a Z.4 „Teljesítve”-mércéje és a „kiürítés”; az implementáció addig marad) és a
  D-16 (b) passz-jelölés (+ DPO); D-07 kalibráció (+ Memuna); D-17 (a) ERT-26, (b) ERT-42 (+ DPO), (c) ERT-43: az elv
  elfogadva, hatályba csak az értékelési felelős és a lektor QA-ja és előzetes tanulói tájékoztató után; D-18 kulcsok (+ M5
  szerző / lektor); D-19 (a), (c); a mentori kulcs-átbeszélés az M7 kapukvíz után; a D-21 terv E5-je (+ programvezető).
- **QA:** az LMS-M4-05 rubrika (egy kritérium, 0/1/2, a három szint szövege változatlan); a végső pontszám rejtésének módja
  (a projektgazda és az LMS-gazda döntése után); D-15 (a), (c), (d), D-23 vétó/QA.
- **Bizonyíték (SIGNOFF):** ERT-19 aláírás és tájékoztató; SIG-1…SIG-6.

### LMS-gazda / build-felelős és hozzáférhetőségi gazda (csomag: `2026-10-13 Bizonyítékcsomag – LMS-gazda és hozzáférhetőségi gazda, AP-2026-10-13-01.md`)

- **Döntés (a projektgazdával):** a rubrikás Assignmentek (LMS-M2-05, -M4-05, -M6-05) végső pontszámának rejtése: a rejtett
  grade item a teljes visszajelzést elrejti, látható grade itemnél „pont / max” látszik (X-16); a D-21 terv E4-je.
- **Runtime (G3b):** a környezeti rekord (verziók), a 76 `BUILD_OUTPUT` és 19 `RUNTIME_OUTPUT` érték, a 38 teszt
  `RUNTIME_VERIFIED` állapota; kiemelten: RA 8 (LMS-M3-08, LMS-M6-05), RA 11 (PV-1…PV-4 előnézeti csomópont, képernyőolvasóval
  is), RA 15 (csoportszűkítés, Manual grading, pontkönyv), RA 16 (Z.4 üres beküldés), RA 19 (M7 Review options), RA 21 (M2.1
  statikus dia), RA 26 (rubrikák: M1-05, M2-05, M4-05, M6-05), RA 27 (fórum).
- **G4b, G5b:** a renderelt felület visszaauditja; az a11y renderteszt és a független pre-flight; LMS-7 alt-szöveg (BK-08);
  megfigyelés: az M3.3 többi tartalomcsomópontjának tartalomcíme.

### Mások

- **Jogász:** a JOG-1 ellenőrzése (Gyvt. 17. §), bejegyzés a #1 issue-ban.
- **Modulgazdák és programvezető:** a D-20 vágási tervek tervenkénti jóváhagyása (a B-változat a 45 perces blokkon és a
  naptáron belül); a D-21 modulspecifikus betétjei a `/course-develop` futás után.
- **Médiafelelős:** a VO fix pack; a jogosultsági részkapuk (J1, J2, V1, V3); az M0.3-FOTO-01 végleges assetje.
- **Projektgazda:** a staging deployment engedélye; a végső pontszám rejtésének módja (az LMS-gazdával); a `/course-develop`
  futás indítása (D-21); a végén a go/no-go döntés.
- **Release-lánc:** `FINAL_RELEASE_QA` (Memuna, DPO, független a11y pre-flight), SIGNOFF-ok, go/no-go a release-jegyzőkönyvben.

## 3. Célzott QA (QA18) a `aca6c1f..bedc637` tartalmi változtatásra

Lencsék: implementáció, biztonság-jog, értékelés; csak a módosított sorok. 9 finding, mind javítva a `bedc637`-ben (a fő session
a fájlban, a H5P- és a Moodle-állításokat az elsődleges forrásban ellenőrizte):

| Kulcs | Súly | Javítás |
|---|---|---|
| KANON:QA18-BIZT-1 | P1 | a D-21 E1–E6 döntéshozói a terv E és F pontja szerint (DPO az E6-nál, LMS-gazda, értékelési felelős) |
| KANON:QA18-ERT-1 | P1 | a D-20 időkerete a döntés szavával: a 45 perces peulablokk és a központi naptár |
| KANON:QA18-ERT-2 | P2 | a végső pont rejtésének nyitott módja a HUM 16-ban; RA 26: a tanulói felületek megnevezve |
| KANON:QA18-ERT-3 | P2 | RA 26: cím és a két ellenőrzés egyértelmű, a build-paraméterek soronként |
| KANON:QA18-ERT-4 | P2 | RA 26: a három szintleírás szó szerinti visszaolvasása |
| KANON:QA18-ERT-5 | P2 | HUM 15 D-20: tervenkénti programvezetői jóváhagyás a döntés szavával |
| KANON:QA18-IMPL-1 | P1 | RA 26: a végső pontra vonatkozó elvárás a mód eldöntéséig nem átmenő teszt |
| KANON:QA18-IMPL-2 | P2 | LMS-M2-05 / LMS-M6-05: `showscorestudent` = No és a „grade item nem lehet rejtett” korlát |
| M3:QA18-IMPL-3 | P1 | a PV-csomópontok tartalomcíme a szitu-cím (a fókuszba kerülő fejléc neve), RA 11 képernyőolvasós lépés |

Új emberi döntés: KANON:QA18-IMPL-4 (a végső pontszám rejtésének módja; projektgazda + LMS-gazda). A nyers lencse-kimenetek
lent, a munkamenet-útvonalak repó-relatívra rövidítve.

## A. Nyers lencse-kimenet – implementáció

QA18-IMPL: célzott QA (implementációs lencse) a `diff-fix.txt` módosított soraira. 3 finding: 2×P1, 1×P2.

Ellenőrzés, finding nélkül:
- **M3.3 csomóponttérkép (24 sor)** – minden „Következő csomópont” cél helyes:
  - P1: passz → 8 (S1-SAFE-1)
  - P2: passz → 14 (INSTR-34; az S2-nek nincs biztonsági csomópontja)
  - P3: passz → 18 (S3-SAFE)
  - P4: passz → 23 (S4-SAFE)
  - A „Végigmegyek” mindenhol a szitu első K-csomópontjára mutat.
  - A K- és a SAFE-láncok lineárisak, a CP-3 → egyetlen végképernyő.
  - A completion-szemantika és a „gráf lineáris” állítás érvényes; az előnézeti csomópont `static-end-score` mellett nem hat a grade-re.
- **H5P-tények** – az Advanced Text a Branching Scenario megengedett típusa (`semantics.json`: „H5P.AdvancedText 1.1”). A Branching Question nem használ metadata-címet, ez megerősíti a QA17-IMPL-1 alapját.
- **Manifest BSPEC-05 és runtime acceptance 11.** – a „24 csomópontos” szám és a PV-hivatkozások konzisztensek. Elavult „20 csomópont” vagy `showContentTitle` hivatkozás a `02 Tervezet/`-ben már csak a HUM 15/16 szándékos felváltó soraiban van.
- **Runtime acceptance 16., Z.4:343, manifest LMS-Z-08** – a D-16 „projektgazdai irány, … szakmai jóváhagyásra vár” címke megfelel a HUM 16-nak.
- **Moodle-állítások** az elsődleges forrás szerint helyesek:
  - a `showscorestudent` felirata;
  - a `grade_get_grades()` Real megjelenítésnél „pont / max” alakot ad;
  - a `grade_grade::is_hidden()` a grade item rejtettségét is figyelembe veszi.
- **Nem érhető el:** a `get_assign_feedback_status_renderable()` szövegét nem tudtam szó szerint lekérni (a `mod/assign/locallib.php` túl nagy a fetch-eszköznek). Az állítás összhangban van a gradelib/is_hidden lánccal, findingot nem írok rá.

---

**QA18-IMPL-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:111` (26. pont); `02 Tervezet/Emberi jóváhagyás szükséges.md:848` (16. szakasz, LMS-M4-05, „Nyitva marad”); `02 Tervezet/LMS – activity manifest.md:80`
- **Probléma:**
  - A döntés szerint „a numerikus érték a tanuló elől rejtett”. A manifest szerint a grade item nem rejthető, látható itemnél pedig „pont / 2” látszik, ezért a rejtés módját nyitott build-döntésként a projektgazdára és az LMS-gazdára teszi.
  - A HUM 16 „Nyitva marad” oszlopa ezt a nyitott döntést nem rögzíti.
  - A runtime acceptance 26. pontja egyszerre várja el, hogy a végső pontszám ne látsszon, és hogy rögzítsék, milyen alakban látszik.
- **Bizonyíték:**
  - RA:111: „…a szintpont és a végső pontszám nem; …” és „rögzíteni kell, hogy a végső pontszám milyen alakban jelenik meg a tanulónak.”
  - HUM:848 Nyitva marad: „értékelési QA; Moodle-visszaolvasás a célverzión.”
  - Manifest:80: „a végső pontszám rejtésének módjáról a projektgazda mint build-spec gazda és az LMS-gazda dönt”.
  - Webforrás: moodle/moodle MOODLE_405_STABLE `grade/grading/form/rubric/renderer.php`, `display_instances()`: `return $return. $defaultcontent;` (a rubrika után a `str_long_grade` mindig kiíródik).
  - Webforrás: MoodleDocs 4.5 „Course settings”: „If grades are used and this link is disabled, students can still see their grade from the actual activity itself, such as an assignment”.
- **Hatás:**
  - A manifest paramétereivel épített activity a tanulónak „1,00 / 2,00” alakot mutat az Assignmentben és a pontkönyvben. Ez ellentmond a döntésnek és az M4 hub §6 „nincs fix pontszám” mondatának.
  - A tesztnek nincs egyértelmű átmenő kritériuma.
  - A döntési nyilvántartás teljesnek mutatja a tételt.
- **Javaslat:**
  - (1) A HUM 16 LMS-M4-05 sorának „Nyitva marad” oszlopába: „a végső pontszám tanulói rejtésének módja (projektgazda mint build-spec gazda + LMS-gazda; manifest LMS-M4-05)”.
  - (2) A runtime acceptance 26. pontjában a végső pontszámra vonatkozó elvárás a mód eldöntéséig ne legyen átmenő teszt. Két felületet kell rögzíteni: az Assignment saját nézetét és a pontkönyvet (Grades).
  - EMBERI DÖNTÉS: a rejtés módja – projektgazda (build-spec gazda) + LMS-gazda. Forrástény: nem Real megjelenítési típusnál a `str_long_grade` = `str_grade`; a pontkönyv-link elrejtése az activity nézetét nem fedi le.
  - Tilos: a mechanizmust beírni, a grade itemet rejtettre állítani, a Maximum grade-et, a szintpontokat vagy a három szint szövegét módosítani.
- **Típus:** objektív (a nyilvántartás és a teszt ellentmondása; a mód maga emberi döntés)
- **Verdikt:**

**QA18-IMPL-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:111` (26. pont, utolsó mondat); `02 Tervezet/LMS – activity manifest.md:62` (LMS-M2-05), `:94` (LMS-M6-05)
- **Probléma:**
  - Az „Ugyanezt a két ellenőrzést…” nem nevezi meg, melyik két ellenőrzésről van szó.
  - A közvetlenül előtte álló build-paraméter-lista csak az M4-re érvényes (egy kritérium, 0/1/2, Maximum grade = 2), és ellentmond az LMS-M2-05 (Maximum grade = 8) és az LMS-M6-05 (Maximum grade = 15, szintpont 1/2/3) sorának.
  - A két manifest-sorba nem került át a `showscorestudent` beállítás neve és a „grade item nem lehet rejtett” korlát.
- **Bizonyíték:**
  - RA:111: „Maximum grade = 2, Grade to pass üres, … (`showscorestudent`) = No. … Ugyanezt a két ellenőrzést az LMS-M2-05-nél és az LMS-M6-05-nél is el kell végezni.”
  - Manifest:62: „Maximum grade = 8 … (… a rejtés Moodle-beállításának nevét stagingben kell igazolni)”.
- **Hatás:**
  - Szó szerinti olvasatban a tesztelő az LMS-M2-05-ön Maximum grade = 2-t keres, és a teszt hamisan bukik.
  - Vagy az M2-05/M6-05 építője a „végső pontszámot nem látja” elvárást a grade item rejtésével teljesíti. Ez a rubrikát és a kommentet is elrejti, pedig a sorok szerint ezeknek látszaniuk kell.
- **Javaslat:**
  - A 26. pont utolsó mondata nevezze meg a két ellenőrzést: (a) `showscorestudent` = No visszaolvasása; (b) a grade item nem rejtett, és rögzíteni kell a végső pontszám tanulói alakját.
  - A build-paraméterek soronként az adott manifest-sor szerint: LMS-M2-05: Maximum grade = 8; LMS-M6-05: Maximum grade = 15, `lockzeropoints`.
  - Az LMS-M2-05 és az LMS-M6-05 sorába az LMS-M4-05 mintájára, forrással kerüljön át a `showscorestudent` = No és a „grade item nem lehet rejtett” korlát.
  - Tilos: Maximum grade, rubrikapontérték, küszöb és az R4/R5 módosítása.
- **Típus:** objektív
- **Verdikt:**

**QA18-IMPL-3**
- **Súlyosság:** P1
- **Bizalom:** közepes (upstream master 1.11.1, a célverzió ismeretlen)
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md:58, 64, 69, 73, 82` (PV-1…PV-4 és a „Témajelzés előnézeti csomóponton” szabály); `02 Tervezet/LMS – H5P runtime acceptance.md:78`
- **Probléma:**
  - A spec nem rögzíti a PV-csomópontok H5P tartalomcímét (metadata title) és a `showContentTitle` értékét.
  - A Branching Scenario minden tartalomcsomópontra lépéskor a fejléc h2-jére viszi a fókuszt. Ennek akadálymentes neve a metadata-cím, üresen „Untitled Content”, a `showContentTitle` értékétől függetlenül.
- **Bizonyíték:**
  - M3.3:82: „Tartalma kizárólag a soron következő szitu meglévő címe …”
  - Webforrás: h5p/h5p-branching-scenario `src/scripts/libraryScreen.js`, `showNextLibrary()`: `this.libraryTitle.setAttribute('aria-label', contentTitle ? contentTitle : 'Untitled Content');` … `this.libraryTitle.focus();`
  - WCAG 2.2 SC 2.4.6 (AA): „Headings and labels describe topic or purpose.”
- **Hatás:**
  - A képernyőolvasós tanuló a témajelző képernyőn „Untitled Content”-et vagy egy belső nevet (pl. „PV-1”) hall a szitu címe helyett. Így a D-08 (b) témajelzése nem jut el hozzá a látó tanulóval egyenértékűen.
  - Bekapcsolt `showContentTitle`-nél a cím kétszer jelenik meg.
  - Ugyanez áll a térkép többi tartalomcsomópontjára is (CP-1…CP-3, INSTR-12, INSTR-34, S1-SAFE-1/2, S3-SAFE, S4-SAFE).
- **Javaslat:**
  - Az M3.3 §3 szabálya rögzítse: a PV-n metadata-címe ugyanaz a meglévő szitu-cím, előtag nélkül; a `showContentTitle` = ki, mert a cím a szövegtörzsben áll; belső azonosító nem lehet metadata-cím.
  - A runtime acceptance 11. pontjának PV-bulletje kapjon képernyőolvasós visszaolvasást: a fókuszba kerülő fejléc neve a szitu címe legyen.
  - Új tanulói szöveg nem készül. Tilos a §7.1 kérdéséhez és a két opcióhoz, a gráfhoz és a pontozáshoz nyúlni.
- **Típus:** objektív
- **Verdikt:**

Források:
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/grading/form/rubric/lang/en/gradingform_rubric.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/grading/form/rubric/renderer.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lib/gradelib.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lib/grade/grade_grade.php
- https://docs.moodle.org/405/en/Course_settings
- https://raw.githubusercontent.com/h5p/h5p-branching-scenario/master/src/scripts/libraryScreen.js
- https://raw.githubusercontent.com/h5p/h5p-branching-scenario/master/semantics.json
- https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html

## B. Nyers lencse-kimenet – biztonság-jog

#### QA18-BIZT – célzott QA, biztonság-jog lencse (AP-2026-10-13-02)

Egy findingot találtam. A D-08 (b) előnézeti csomópont, a SAFE-1…SAFE-4, a passz utáni biztonsági csomópontok, a D-16 átsorolása, az M6-NY-D27 és a JOG-1 rendben van. Hiba a D-21 két átírt sorában van: rosszul nevezik meg, ki dönt az E1–E6 kérdésekben, és kimarad a DPO.

---

- **ID:** QA18-BIZT-1
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:843` (16. szakasz, D-21 sor, „Nyitva marad” oszlop) és `:826` (15. szakasz, nyitott tábla, D-21 sor, „Ki dönt” oszlop)
- **Probléma:** Mindkét sor az E1–E6 döntéshozóiként egy olyan szereplistát ad, amely nem egyezik a hivatkozott terv E és F pontjával. Kimarad a DPO, aki az E6-ban a programvezetővel együtt dönt arról, ki tarthatja az F-peulát és ki fér hozzá a kapueredményhez. Kimarad az értékelési felelős (E5) és az LMS-gazda (E4). A 16. szakasz sora ráadásul a modulgazdát is döntéshozóként nevezi meg, pedig az E1–E6 egyikében sem ő dönt. A 16. szakasz sora azt sem mondja ki, hogy a terv 6–7. pontját (egy résztvevő kiskorúval, 1:1 út, biztonsági minimum) a Memuna hagyja jóvá. A 15. szakasz sorában ez „Memuna (1:1)” formában még szerepel.
- **Bizonyíték:** HUM:843: „az E1–E6 szerepköri döntés (a terv F pontja szerint: Memuna, programvezető, modulgazda)”. HUM:826: „nyitott az E1–E6: modulgazda; Memuna (1:1); programvezető (kapacitás)”. A hivatkozott forrás (`01 Fejlesztés/04 Audit/2026-10-13 course-develop terv – 1–5 fős F-peula keret, D-21, AP-2026-10-13-01.md`):
  - :75: „E6: Ki tarthatja az F-peulát, és ki férhet hozzá a kapueredményhez (BIZT-G3-8, nyitott). Dönt: DPO + programvezető.”
  - :239: „Memuna: a 6–7. pont, az E1 (a programvezetővel), az E2.”
- **Hatás:** Aki a kánoni sort olvassa, azt hiheti, hogy a kapueredményhez való hozzáférésről (E6, adatkör) a programvezető DPO nélkül dönthet. Azt is hiheti, hogy a terv elfogadásával a kiskorúval kialakuló 1:1 helyzet kezelése (6. pont) lezárult. Így egy adatvédelmi és egy gyermekvédelmi szerepköri jóváhagyás kieshet.
- **Javaslat:** A két cellában a döntéshozókat szó szerint a terv E és F pontja szerint kell felsorolni:
  - E1: Memuna + programvezető
  - E2: Memuna
  - E3: programvezető
  - E4: programvezető, illetve LMS-gazda
  - E5: programvezető + értékelési felelős
  - E6: DPO + programvezető
  - a terv 6–7. pontja: Memuna
  - a modulspecifikus betétek: modulgazdák

  A 16. szakasz sorában a „(a terv F pontja szerint: …)” zárójelet erre kell cserélni. A projektgazdai döntés-oszlophoz (a terv elfogadása, 6a, 6b, E7) nem szabad hozzányúlni, és új szerepet sem szabad kitalálni.
- **Típus:** objektív
- **Verdikt:**

---

**A többi ellenőrzött pont, fájlonként:**

- **`02 Tervezet/Modulok/M3/Online leckék/M3.3 – … .md:53–84`**
  - **Átkötések:** A 24 csomópontos térképet végigkövettem. A P1/P2/P3/P4 „Passzolom” átkötései a 8/14/18/23. csomópontra visznek, vagyis az S1-SAFE-1 / INSTR-34 / S3-SAFE / S4-SAFE-re. A passz után tehát a biztonsági csomópont minden úton megmarad. Az S2-nek nincs biztonsági csomópontja, ezért ott nem is kell; ez a SAFE-1 7.1 szerint van így.
  - **Előnézeti csomópontok (PV):** csak a címet mutatják, nem kérnek választ, nem pontozottak és nem completion-feltételek.
  - **Passz-választó:** a kérdés és a két opció változatlan, megerősítő ablak nincs. A passzjog nem gyengül.
  - **A szituk címei:** a 3. és a 4. szitu címe érzékeny téma jelzése („vágásnyomok”, „párkapcsolat-gyanú”). Hogy ez megterhelő-e, azt a Memuna QA-ja dönti el, és ez a szöveg szerint is nyitott. Nem új hiba.
- **`LMS – H5P runtime acceptance.md` 11. pont:** a PV-teszt lefedi, hogy csak a cím jelenik meg, hogy a kérdés és az opciók változatlanok, hogy passz után megvan a biztonsági csomópont, és hogy a grade és a completion változatlan (1/1). A 16. pont (D-16) „projektgazdai irány, szakmai jóváhagyásra vár” lett; a nyers válaszok törlése DPO-tétel maradt.
- **`LMS – activity manifest.md` BSPEC-05 és LMS-Z-08:** a `showContentTitle` megoldás kikerült, a PV-1…PV-4 bekerült, a SAFE-1 és a SAFE-4 megmaradt. Az LMS-Z-08-ban a D-16 „irány” lett. Az LMS-M4-05 sornak nincs biztonsági-jogi vonatkozása; a DPO adatkör-QA-ja ott is megmaradt.
- **`Emberi jóváhagyás szükséges.md` 15. és 16. szakasz:**
  - **M6-NY-D27:** csak a Memuna reviewja céljára oldja fel, a küszöb változatlan. Ez egyezik a projektgazda szó szerinti 4. pontjával.
  - **D-16:** a nyitott táblába került. A szerepek egyeznek a 14. szakasz ERT-3 és ERT-38 sorával: értékelési felelős; vétó/QA: programvezető, a Z.4-nél DPO + programvezető.
  - **D-04, D-17, D-20:** egyik sem zár le Memuna-, DPO- vagy értékelési hatáskört.
- **JOG-1 (HUM:850):** a sor nem állít jogászi vagy Memuna-jóváhagyást, és mindkettőt nyitottként tartja a G1-ben. Megnéztem a GitHub #1 issue-t (https://github.com/hasomerhacairhu/modszertani-kepzes/issues/1). A 2026-10-13-i komment fent van, csak szerepneveket használ, személyes adat nincs benne. Az issue szerint a Memuna jóváhagyása csak a jogászi ellenőrzés után jön („ezt követi a Memuna jóváhagyása”), ezért a „közzétéve” állítás igaz.

Sources:
- https://github.com/hasomerhacairhu/modszertani-kepzes/issues/1

## C. Nyers lencse-kimenet – értékelés

#### QA18 – értékelés lencse, célzott QA (AP-2026-10-13-02)

A diffben öt findingot találtam: 1×P1 és 4×P2. A fókuszkérdésekre röviden: az LMS-M4-05 rubrika egyezik az M4 hub §6 szintjeivel, a küszöb, a completion és a puha kapu nem változott. A D-16 hivatkozások és sorok, valamint az ERT-43 sor rendben vannak (részletek a findingok után). A D-20 sor nem hagy jóvá vágást a modulgazda helyett, de két átvezetési hibája van (QA18-ERT-1, QA18-ERT-5).

**QA18-ERT-1**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:844` (16. szakasz, D-20 sor)
- **Probléma:** A D-20 lezárt döntés átvezetése tágabb feltételt ír, mint a döntés. „A modul teljes időkerete” áll benne, a projektgazda viszont „a teljes időkeret”-ről beszélt, és a D-20 csomag B-változata a peula 45 percét tartja meg. A 15. szakasz D-20 sora (:825) a döntés eredeti szavát használja.
- **Bizonyíték:** HUM:844 „a belső blokkhatár eltolható, ha a modul teljes időkerete és a védett lépések változatlanok”; döntés 2. pont: „amennyiben a teljes időkeret és a védett lépések változatlanok”; D-20 csomag :541: „B-változat: csak a 45’ és a központi naptár marad, egy-egy belső blokkhatár 1–3’-cel elmozdul”.
- **Hatás:** A kánoni szöveg alapján egy peula túllépheti a 45 percet, ha a modul összideje nem változik. Konkrét eset is van: a csomag :827 galéria-változata összesen 45,5–46’. Ez ütközik a PRG-1 45 perces peulablokkjával, így egy időtartam lezárt döntés címén csúszhat el.
- **Javaslat:** A 16. szakasz D-20 sorában „a modul teljes időkerete” helyett „a teljes időkeret” álljon, a döntés szavával, a 15. szakasz sorával egyezően. Ha pontosítás kell, csak a csomag :541-ből: „(a 45 perces peulablokk)”. A modulgazdai, Memuna- és programvezetői jóváhagyáshoz és a tervekhez ne nyúlj.
- **Típus:** objektív

**QA18-ERT-2**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – activity manifest.md:80` (LMS-M4-05); `02 Tervezet/Emberi jóváhagyás szükséges.md:848`; `02 Tervezet/LMS – H5P runtime acceptance.md:111` (26. pont)
- **Probléma:** A manifest nyitott kérdésként rögzíti, hogyan rejtsük el a végső pontszámot: erről a projektgazda (mint build-spec gazda) és az LMS-gazda dönt. Maga a manifest mutatja ki, hogy a grade item nem lehet rejtett, látható grade itemnél pedig a „pont / 2” alak látszik. A HUM 16. szakasz LMS-M4-05 sorának „Nyitva marad” oszlopából ez a nyitott tétel hiányzik. A 26. pont csak általánosan írja elő a megjelenési alak rögzítését, és nem nevez meg tanulói felületet. A pontkönyv tanulói nézete is ilyen felület; ezt a célverzión kell igazolni.
- **Bizonyíték:** manifest:80 „látható grade itemnél pedig valós (Real) megjelenítési típus mellett a „pont / 2” alak látszik … a végső pontszám rejtésének módjáról a projektgazda mint build-spec gazda és az LMS-gazda dönt”; HUM:848 „értékelési QA; Moodle-visszaolvasás a célverzión.”
- **Hatás:** Amíg a mód nincs eldöntve, az alapbeállítású build a formatív puha kapun „0 / 2” típusú pontszámot mutathat. Ez ellentmond a lezárt döntésnek („A numerikus érték a tanuló elől rejtett”) és az M4 hub §6-nak („nincs fix pontszám”). A nyitott tétel ráadásul kieshet a HUM-ból és a státuszjelentésből.
- **Javaslat:** A HUM 16. szakasz LMS-M4-05 sorának jobb oszlopába kerüljön be: „a végső pontszám rejtésének módja (projektgazda mint build-spec gazda + LMS-gazda; manifest LMS-M4-05)”. A 26. pontban a megjelenési alak rögzítése nevezze meg a tanulói felületeket: az Assignment visszajelzés-nézetét és a tanuló pontkönyv-nézetét. A rejtés módját ne válaszd ki. A 0/1/2, Point, Maximum grade = 2 és az üres Grade to pass paraméterhez ne nyúlj.
- **Típus:** objektív

**QA18-ERT-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:111` (26. pont)
- **Probléma:** A „két ellenőrzés” nem egyértelmű. Visszamutathat az LMS-M4-05 saját build-paraméter-listájára is (egy kritérium, 0/1/2, Maximum grade = 2). Ez ütközne az LMS-M2-05 (Maximum grade = 8) és az LMS-M6-05 (a rubrika nyers összege, 1/2/3 pont) saját sorával. A pont címe ráadásul csak az LMS-M1-05-öt nevezi meg.
- **Bizonyíték:** „Ugyanezt a két ellenőrzést az LMS-M2-05-nél és az LMS-M6-05-nél is el kell végezni.”; cím: „26. **Rubrika tanulói megjelenítése (LMS-M1-05):**”
- **Hatás:** A tesztelő egy rubrikát rossz paraméterekkel olvashat vissza vagy jelölhet hibásnak; ez az éles kapus LMS-M6-05-nél is megtörténhet. Azonosító szerinti keresésnél a 26. pont az M2, M4 és M6 teszteknél kimaradhat.
- **Javaslat:** A mondat legyen egyértelmű, például: „A grade item láthatóságának ellenőrzését és a végső pontszám megjelenési alakjának rögzítését az LMS-M2-05-nél és az LMS-M6-05-nél is el kell végezni; a build-paramétereik a saját manifest-soruk szerintiek.” A cím legyen „(LMS-M1-05, LMS-M2-05, LMS-M4-05, LMS-M6-05)”. A paraméterértékekhez ne nyúlj.
- **Típus:** objektív

**QA18-ERT-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:111` (26. pont); `02 Tervezet/Emberi jóváhagyás szükséges.md:848`
- **Probléma:** A döntés kimondja, hogy a három szint szövege nem változik, és Moodle-visszaolvasást ír elő. A 26. pont build-paraméter-listája viszont csak a szerkezetet olvastatja vissza; azt nem, hogy a szintleírások szó szerint egyeznek-e az M4 hub §6 Kapu 2 szövegével.
- **Bizonyíték:** HUM:848 „A három szint szövege nem változik.”; runtime:111 „egyetlen kritérium a három szinttel, szintpont 0/1/2, Grade type: Point, Maximum grade = 2, Grade to pass üres”.
- **Hatás:** A szám rejtett, ezért a szintleírás a tanuló egyetlen formatív rubrika-visszajelzése. Ha a build rövidített címkét használ (pl. csak „Fejlettebb”), a tanuló nem tudja meg, melyik sablonelem hiányzik, vagy mit jelent a kvucára szabottság. A manifest „szövegük változatlan” követelményét így semmi nem ellenőrzi.
- **Javaslat:** A 26. pont listája egészüljön ki ezzel: „a három szintleírás szó szerint egyezik az M4 hub §6 Kapu 2 szövegével”. Más paraméterhez ne nyúlj.
- **Típus:** objektív

**QA18-ERT-5**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:825` (15. szakasz, D-20) és `:844` (16. szakasz, D-20)
- **Probléma:** A két D-20 sor másképp írja le a programvezető szerepét. A 15. szakasz nyitott D-20 sora csak vétó/QA szerepben nevezi meg. A projektgazda döntése és a 16. szakasz viszont tervenkénti programvezetői jóváhagyást ír elő. A módosított sor ezt nem igazította hozzá.
- **Bizonyíték:** HUM:825 „az adott modulgazda (M3.B: + Memuna); vétó/QA: programvezető; a B-változatok belső blokkhatár-eltolása … engedélyezett (16. szakasz)”; döntés 2. pont: „A modulgazdai és programvezetői jóváhagyás továbbra is szükséges.”; HUM:844 „modulgazdai (M3.B: + Memuna) és programvezetői jóváhagyás tervenként.”
- **Hatás:** Ugyanarra a tételre két eltérő kapuszemantika él: utólagos vétó vagy előzetes jóváhagyás. Egy vágási terv így programvezetői jóváhagyás nélkül is jóváhagyottnak tűnhet.
- **Javaslat:** A 15. szakasz D-20 sorában a „vétó/QA: programvezető” igazodjon a 16. szakaszhoz és a döntés szövegéhez: „programvezetői jóváhagyás tervenként”. A lezárt döntés áll a forrás fölött. A „belső blokkhatár-eltolás engedélyezett” részhez ne nyúlj. A bizalom azért alacsony, mert a D-20 csomag „programvezetői vétóval” fogalmaz, így a döntés „jóváhagyás” szava lehet laza megfogalmazás is.
- **Típus:** objektív

##### Amit findingok nélkül ellenőriztem
- **LMS-M4-05 (manifest:80, HUM:848):** a három szint és a 0/1/2 sorrend egyezik a hub §6:133–135 szintjeivel. A küszöb továbbra is „Alapszint / rendben”, a Grade to pass üres. A completion `completionsubmit` + LMS-M4-10 CONFIRMED, a kapu puha, a rubrikaszint nem completion- és nem nyitási feltétel. A 0/1/2 szintpont a Maximum grade = 2 mellett torzítás nélkül képeződik le.
- **D-16:** a manifest LMS-Z-08 sora, a Z.4 Completion rule és a runtime 16. pont mindenhol „projektgazdai irány, … szakmai jóváhagyásra vár” jelölést kapott. A HUM 15. szakasz nyitott táblája és a 16. szakasz sora megfelel a döntés 7. pontjának. Az implementáció marad, más kánoni helyen nincs „projektgazdai döntés” jelölésű D-16 hivatkozás.
- **ERT-43:** a 16. szakasz sora és a 15. szakasz D-17 sora csak az elvet fogadja el, a hatálybalépést a QA-hoz és az előzetes tanulói tájékoztatóhoz köti. Az M7 KAPU nem szerepel a diffben.
- **M3.3 PV-csomópontok:** nem pontozottak és nem completion-feltételek. A 24 csomópontos útvonal és a passz utáni biztonsági csomópontok helyesek.
