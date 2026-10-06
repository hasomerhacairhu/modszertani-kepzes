# Build-blocker leltár — H-1…H-5, 38 checklist-tétel, 4 fotó (2026-10-05)

> **Audit trail, nem kánon. Javaslat, projektgazdai döntésre vár.** Besorolási kör, javítás nélkül: kánoni fájl nem
> változott, commit nincs. Bázis: `fix/moodle-build-hardening` @ `9ef2b25` (a távoli ág `e980a70`-on áll; a
> `9fdeebc`…`9ef2b25` öt commit nincs pusholva). A gépi állapot a besorolás előtt (`--release-report`):
> `CHECKLIST-UNCLASSIFIED 38` (SAFEGUARDING 11, PRIVACY 7, A11Y 20), `MEDIA-REQUIRED-WITHOUT-FALLBACK 4`,
> `MOODLE-BUILD-VERDICT: NOT_READY`, `LEARNER-RELEASE-VERDICT: NO-GO`.
>
> Rövidítések: GK = `Gyermekvédelem – release gate.md`; ADV = `Adatvédelem – tanulói adatok és AI.md`; STD = `LMS –
> hozzáférhetőségi sztenderd.md`; MAN = `LMS – activity manifest.md`; RA = `LMS – H5P runtime acceptance.md`; RR =
> `RELEASE-READINESS.md`; PT = `Program terv.md`; RMS = `Média-assetek/RELEASE-MEDIA-STATUS.md`.
> **Döntések (2026-10-05):** D-a, D-b elfogadva, D-c ugyanezen az ágon, D-d (az M7.4 SLIDE 4 nem completion-elem) —
> `2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`.
> Bizonyíték-forrás: a fő session célzott olvasása és két read-only Explore-subagent tényleltára; a döntő állításokat a
> fő session szúrópróbával ellenőrizte. Az **ÚJ** jelölésű tételek ebben a körben kerültek elő, verifier még nem
> nézte őket.

## 0. Besorolási szabály

- **BUILD** (`MOODLE-BUILD-VERDICT`): ami nélkül a build nem determinisztikus — nem rögzített Moodle-beállítás,
  hivatkozott, de definiálatlan objektum (tartalékút), vagy amit az RR G-táblájának „Besorolás” oszlopa kifejezetten
  BUILD-nek mond (G2: adatleltár szerepkör/capability, tájékoztató szövege; G3a: mechanizmusok tartalékúttal; G5a:
  autoplay, Auto continue, iframe-cím, AD-besorolás).
- **Nem BUILD**: ami csak a build/runtime során keletkező bizonyíték (RT-sorok, környezeti rekord, cmid), szerepköri
  átnézés vagy aláírás, szervezeti nyilvántartás, valamint a tanulói tartalom tulajdonsága, ha a szabály maga már a
  specben van. A GK §2 (:21) kifejezetten engedi a gyermekvédelmi elemek felépítését zárt stagingben.
- RR staging-szabály 2: emberi döntés helyén belső build-jelölő maradhat (kontakt, megőrzési érték).
- Gate-jelölés (`content_integrity.py`): `build`, `post-build`, `release-evidence`, `human-qa`, `signoff`,
  `lifecycle`, + `repo-fixable`. Megfeleltetés: REPO_FIX (build) → `build, repo-fixable`; RUNTIME → `post-build`;
  FINAL_RELEASE_QA-szerep (Memuna, DPO, független a11y pre-flight) → `human-qa`; egyéb szakértői/szervezeti
  jóváhagyás, dátum → `signoff`; szervezeti/környezeti bizonyíték, learner-release emberi döntés → `release-evidence`.

## 1. H-1…H-5 normalizálása (Phase 0)

| ID | Tárgy (forrás) | Besorolás | Indoklás (bizonyíték) | Build? |
|---|---|---|---|---|
| H-1 + M6.4 O-1 | Branching Scenario completion tartalékútja: M2.3 :11, :114 és M2 hub :81 („különben Moodle-checkpoint kell”); M6.4 :104 („külön H5P-aktivitásként vagy Moodle-checkpointtal”) | **NEW_BUILD_SPEC_REQUIRED → BSPEC-05** | A hivatkozott checkpointnak nincs profilja, `build_id`-ja, completionje, unlock-kötése (MAN LMS-M2-04, LMS-M6-04). Az LMS-M2-07 az LMS-M2-04 completionje után nyílik → ha a BS-completion nem jön meg, az M2 nem teljesíthető; az LMS-M6-06 az LMS-M6-04 után nyílik. M6.4: minden visszajelző oldalon „Tovább a lezáráshoz” (:101, :271…) → a végképernyő 1 ág után elérhető, tehát a natív BS-completion a „3 külön ág” feltételt nem fejezi ki; az M6.4 két tartalékutat nevez, választás nélkül. A BSPEC-01 precedense (feltételes, definiálatlan checkpoint = `BUILD_SPEC_OPEN`) és az RR G3a („mechanizmusok tartalékúttal” = BUILD) ide sorolja; a BSPEC-02 verifiere is külön BSPEC-sort kért. Az RT-P0-02/-10 csak tesztel, nem specifikál. | **igen** |
| H-2 | a kijelölt mentor tanulónkénti láthatóságának mechanizmusa (BIZT-R3) | **CHECKLIST_ITEM → PR-01** (ADV :168) | Az RR G2 az „adatleltár (Moodle-szerepkör/capability)” részt BUILD-nek sorolja; ez pontosan a PR-01. Mechanizmus sehol (MAN/ADV-ben nincs separate groups, `accessallgroups`, `viewreports`-szűkítés; csak a tanulói `viewanalysepage` Prohibit). Feltételes emberi döntés: ha nincs core tanulónkénti mechanizmus, elfogadható-e a szerepkör-szintű láthatóság (DPO/jogi felelős). A `build` jelölésű checklist-tétel gépileg követett, ezért külön BSPEC nem kell. | **igen** (PR-01-en át) |
| H-3 | M7.1 SLIDE 4 Fill in the Blanks: a „reális szám” elfogadott halmaza nincs rögzítve | **LEARNER_RELEASE_ONLY** (emberi döntés) | Gazda: értékelési felelős / modulgazda (a verifier szerint). A kánon (:333) „bármilyen konkrét szám jó válasz”, de a FitB-hez felsorolt halmaz kell; stagingben ideiglenes halmaz belső build-jelölőként (RR staging-szabály 2). A completiont csak akkor érinti, ha a BSPEC-06 „passing grade”-et választ. Megjegyzés: az 1–7. fájl F-M7.1-3 (:145) ugyanezt „H-4”-nek hívja — belső számozási eltérés az audit trailben. | nem |
| H-4 | a H5P-C completion forrása: a profil nem rögzít Moodle-beállítást; a leckék interakciónkénti completion-halmazt írnak (pl. M0.1 :13, M7.4 :14) | **NEW_BUILD_SPEC_REQUIRED → BSPEC-06** | A TEXT-C (`completionsubmit`), a GATE-CP („Receive a grade”) és a QUIZ-M rögzíti a Moodle-beállítását, a H5P-C nem („a forrásban előírt interakció(k) érdemi befejezése”); az RA 9 „a választott Moodle-beállítást” teszteli, de a választás sehol nincs. Az unlock-lánc (pl. LMS-M2-07, LMS-M6-06, modul-completion „H5P-k”) ettől függ → két építő eltérően építene. A Z.2 implementációs lencséje szerint a `mod_h5pactivity` csak megtekintés- vagy grade-alapú completiont ismer (elsődleges forrásból ebben a körben nem ellenőrizve). Az M7.4 completion-sora maga nyitott elemet tartalmaz (SLIDE 4 fókuszválasztás, R-24). | **igen** |
| H-5 | M7 hub :243 a Peula v1 „minimum elvárásai” közül hiányzik a SMART cél (M7.4 SLIDE 3/5 kéri) | **LEARNER_RELEASE_ONLY** (repo-javítás, pin) | Az LMS-M7-05 (ASSIGN-S) completionje a mentor megerősítésén múlik, ennek kritériuma a lista; Moodle-objektum és -beállítás nem változik. | nem |

**ÚJ, a Phase 0 ellenőrzésében előkerült (validálandó):**

- **C-1 — ASSIGN-S megerősítés és tartalékút.** MAN §4 utolsó bekezdése: a puha kapuknál és minden ASSIGN-S beadásnál
  „ha ez nem kódolható bizonyítottan, ugyanez a checkpoint-út érvényes”; az RA 1 ugyanígy. Az ASSIGN-S profil nem
  rögzít Moodle completion-beállítást (a „technikai út: RA 1. pont”), és GATE-CP sor csak az éles kapukhoz, az
  LMS-M7-09-hez és az LMS-Z-07-hez van; az LMS-M2-05, LMS-M4-05, LMS-M7-05, LMS-Z-04 tartalékútjának nincs sora. A
  H-1-gyel azonos osztály → a BSPEC-05/06 hatókörébe javasolt, validálás után.
- **BS-kiterjesztés:** az M3.3 (LMS-M3-03, BS-befoglaló, a kapu belépő feltétele) és az M5.2 (LMS-M5-02) is
  Branching Scenario-completionre épül, tartalékút-hivatkozás nélkül; az RA 5 Moodle 5.1.1-es BS-hibát említ. A
  BSPEC-05-ben vagy tartalékút, vagy a BS-D1 mintájára indokolt „tartalékút nincs” rögzítendő.

**A többi nyitott, BSPEC-02-n kívüli tétel (változatlanul nyitva):** F-M0.4-6, F-M0.4-7, F-M3.4-4 (produktum-fele),
F-M3.4-6 → learner release; F-M5.4-2 (lecke-szöveg vs. MAN unlock), F-M5.4-3 (MAN „Név” oszlop) → nem blokkoló
repo-javítás; R-24 (M7.4 SLIDE 4 completion-szerepe) → a BSPEC-06 része, emberi/értékelési döntés.

**Válasz:** „The only Moodle-build blockers are the 38 checklist items and 4 photos.” — **a repó bizonyítékai nem
támasztják alá.** A gépi riport csak azt látja, ami regiszterben van; a H-1/O-1 és a H-4 olyan determinisztikus
build-követelmény, amely egyik regiszterben sincs (lásd 2.).

## 2. A javított build-blocker halmaz

| # | Blokkoló | Típus | Forrás |
|---|---|---|---|
| 1 | BSPEC-05 (javasolt): BS completion → Moodle + tartalékút (LMS-M2-04, LMS-M6-04; kiterjesztés: LMS-M3-03, LMS-M5-02; C-1 validálás után) | MANIFEST-OPEN | H-1, M6.4 O-1 |
| 2 | BSPEC-06 (javasolt): H5P-C (és C-1 után ASSIGN-S) Moodle completion-beállítás rögzítése; R-24 | MANIFEST-OPEN | H-4 |
| 3 | PR-01 (ADV :168) adatleltár szerepkör/capability + mentor-mechanizmus | CHECKLIST-BUILD | RR G2, H-2 |
| 4 | PR-02 (ADV :169) a tanulói adatvédelmi tájékoztató szövege | CHECKLIST-BUILD | RR G2 |
| 5 | A11Y-07 (STD :88) H5P-nyelv + iframe-cím build-szabálya | CHECKLIST-BUILD | RR G5a |
| 6 | A11Y-17 (STD :113) offline, alacsony adatigényű leckeváltozat build-definíciója | CHECKLIST-BUILD | RR G5a; M4.1 :68 |
| 7 | M0.3-FOTO-01, M0.A-FOTO-01, M4.1-FOTO-01, M4.1-FOTO-02 | MEDIA-REQUIRED-WITHOUT-FALLBACK | a 4. pont szerint feloldható; előfeltétel a `release_phase`/`fallback`/`fallback_final` séma |

A többi 34 checklist-tétel learner-release (3. pont). Gépi következmény a jelölések és a két BSPEC-sor felvétele után
(egyéb javítás nélkül): `MANIFEST-OPEN 2`, `CHECKLIST-BUILD 4`, `MEDIA-REQUIRED-WITHOUT-FALLBACK 4` → továbbra is
`NOT_READY`, de minden blokkoló regiszterben.

## 3. A 38 checklist-tétel

Oszlopok: ID (sor) · besorolás · javasolt jelölés · build-blokk · lezáró bizonyíték · szerep · függőség/duplikáció.
Minden tétel, amely nem build-blokk, csak a learner release-t blokkolja.

### 3.1. SAFEGUARDING (GK §6)

| ID (sor) | Tétel röviden | Besorolás | Jelölés | Build | Lezáró bizonyíték · szerep | Függőség |
|---|---|---|---|---|---|---|
| SG-01 (145) | Memuna „átnéztem” (M3.3, M3.B, M3-kapu, M7) | SIGNOFF_REQUIRED | `human-qa` | nem | írásos „átnéztem” a release-jegyzőkönyvben (PT §9.3) a fagyasztott release-jelöltre · Memuna | a 145 hatóköre szűkebb a GK §2 (:17) témaalapú hatókörénél (és az RR :40-nél) → repo-javítás (szó szerinti átvezetés); a BSPEC-02 átírt veszély-dobozai Memuna-QA alatt |
| SG-02 (147) | a kontakt ténylegesen látható a Moodle-ben | DUPLICATE_OF:RT-P0-17 | `post-build` | nem | RT-P0-17 tanulói tesztfiókkal · LMS-gazda | a valódi név/kontakt: RR G8 RELEASE-EVIDENCE (stagingben build-jelölő); a blokk tartalma: HUM-OPS-02 (HUM :241); MAN :110–112 csak megnevezi |
| SG-03 (148) | nincs 100%-os titoktartási ígéret | SIGNOFF_REQUIRED | `human-qa` | nem | a Memuna átnézése (standard v1.0, 2. elem); támogató: datált repo-sweep a fagyasztáskor · Memuna | gépi őr nincs (`content_integrity` erre nem keres); SG-01 |
| SG-04 (149) | nincs nyomozás/konfrontáció/„lerendezés” | SIGNOFF_REQUIRED | `human-qa` | nem | mint SG-03 (3. elem) · Memuna | SG-01 |
| SG-05 (150) | akut út és segélyvonalak a review napján ellenőrizve | ENVIRONMENT_EVIDENCE_REQUIRED | `release-evidence` | nem | datált „ellenőrizve” bejegyzés (116-111, 116-000, 116-123, 112) a release-jegyzőkönyvben · Memuna / release owner | GK :50; ma nincs datált ellenőrzés |
| SG-06 (151) | szégyenítés nélküli kilépési/támogatási út (§4.3) | HUMAN_DECISION_REQUIRED | `signoff` | nem | a §4.3 blokk forrásszinten szó szerint megvan mind az öt előírt helyen (M0.1, M2.A, M2.4, M3.3, M3.B — ellenőrizve); nyitott: N-4 (passzjog egyenértékű útja az LMS-M2-09 SLIDE 5 kötelező válaszánál) · Memuna + programvezető | a blokk további 10 helyen is áll (GK :102 csak ad hoc blokk helyére engedi; nincs nyoma, melyik volt ilyen) → Memuna-QA megfigyelés; renderelve: G4b |
| SG-07 (152) | 1:1 tananyag és kvízkulcsok = HUM-SAFE-02 | SIGNOFF_REQUIRED | `human-qa` | nem | Memuna átnézése (4–5. elem); támogató repo-sweep · Memuna | SG-01 |
| SG-08 (153) | alkohol/dohány/nikotin = HUM-SAFE-04 | SIGNOFF_REQUIRED | `human-qa` | nem | Memuna átnézése (7. elem); vétó: szervezeti vezetés · Memuna | SG-01 |
| SG-09 (154) | stáb-alkalmasság és 15–17 éves madrih felügyelete dokumentált (HUM-SAFE-05) | ENVIRONMENT_EVIDENCE_REQUIRED | `release-evidence` | nem | szervezeti nyilvántartás a korlátozott tárhelyen; a release-jegyzőkönyvbe csak nem személyes igazolás · szervezeti vezetés + Memuna | személyes adat nem kerülhet a repóba |
| SG-10 (155) | jogi kötelezettség / szakmai minimum / policy elkülönítve | SIGNOFF_REQUIRED | `signoff` | nem | jogi szakértő írásos átnézése a tanulói jogi állításokról · jogi szakértő (+ Memuna) | GK §3.1 nyitott jogi alkalmazási kérdés |
| SG-11 (156) | jóváhagyás és következő felülvizsgálat dátuma | SIGNOFF_REQUIRED | `signoff` | nem | dátumok a release-jegyzőkönyvben · Memuna | release-jegyzőkönyv ma nincs (M3.3 :10 „még nincs rögzítve”) |

### 3.2. PRIVACY (ADV §9)

| ID (sor) | Tétel röviden | Besorolás | Jelölés | Build | Lezáró bizonyíték · szerep | Függőség |
|---|---|---|---|---|---|---|
| PR-01 (168) | teljes activity-szintű adatleltár (§3), mentori jegyzettel, Google-sablonokkal | REPO_FIX_REQUIRED | `build, repo-fixable` | **igen** (RR G2) | activitynkénti leltár a §3 11 mezőjével; a build-rész: címzettek + Moodle-szerepkör/capability + mechanizmus (elsődleges forrású Moodle-kutatással) · LMS-gazda + privacy felelős; vétó: DPO | H-2; feltételes DPO-döntés; a harmadik fél/tárhely, export, törlés-felelős mezők szervezeti tények → javasolt kettébontás (build-rész + `release-evidence` rész) |
| PR-02 (169) | rövid, magyar, érthető tanulói adatvédelmi tájékoztató | REPO_FIX_REQUIRED | `build, repo-fixable` | **igen** (RR G2) | a kurzusszintű tájékoztató szövege a PT §7 sablonjából és a lezárt HUM-PRIV döntésekből; DPO-kontakt és LMS-Z-06 megőrzés belső build-jelölővel · szövegíró: `/course-fix`; DPO release-ellenőrzés: PR-07 | PR-01 („Ki látja?” szerepkörei); PR-04; ma csak sablon (PT :319–324) |
| PR-03 (170) | mentor/képző hozzáférés tesztfiókkal | DUPLICATE_OF:RT-P0-15 | `post-build` | nem | RT-P0-15 · LMS-gazda | PR-01 |
| PR-04 (171) | megőrzés/törlés folyamata és felelőse dokumentálva, tesztelve | HUMAN_DECISION_REQUIRED | `release-evidence` | nem | a törlési eljárás és a felelős szerep rögzítése (DPO), majd teszt a célkörnyezetben · DPO / LMS-gazda | LMS-Z-06 megőrzése (BS-D6, DPO); HUM :137 |
| PR-05 (172) | a no-AI út végigvihető | DUPLICATE_OF:RT-P0-20 | `post-build` | nem | RT-P0-20, 4. alpont · LMS-gazda | — |
| PR-06 (174) | fotó/videó/hang folyamat HUM-PRIV-02 szerint | ENVIRONMENT_EVIDENCE_REQUIRED | `release-evidence` | nem | a hozzájárulási folyamat (gondviselővel), tárhely, törlés működik; DPO igazolja · DPO | a feltöltési utak (ASSIGN-S fájlút, LMS-Z-04 opcionális videó, LMS-M6-03 fotó) ma nincsenek hozzá kötve: pilot előtt a folyamat vagy a feltöltés tiltása |
| PR-07 (176) | privacy/DPO/jogi signoff rögzítve | SIGNOFF_REQUIRED | `human-qa` | nem | DPO release-ellenőrzés (FINAL_RELEASE_QA), jogi jóváhagyás · DPO, jogi felelős | PR-01…06 |

### 3.3. A11Y (STD)

A :80–89 a kapus H5P elemenkénti pre-flight sablonja (STD :76–78 „Kész = élesíthető”: nem a szerző végzi, független
második ellenőrzés, a hozzáférhetőségi felelős aláírása); a :105–116 a fejlesztői gyors-checklist. A pre-flight
tételeket `human-qa`-ra javaslom, mert más gépileg követett hely a független a11y pre-flightnak nincs.

| ID (sor) | Tétel röviden | Besorolás | Jelölés | Build | Lezáró bizonyíték · szerep | Függőség |
|---|---|---|---|---|---|---|
| A11Y-01 (80) | célméret ≥24×24 | DUPLICATE_OF:RT-A11Y-11 | `human-qa` | nem | pre-flight napló + RT-A11Y-11 (RT-P0-13 mobil mérés) · független pre-flight | — |
| A11Y-02 (81) | billentyűzettel teljesíthető | DUPLICATE_OF:RT-A11Y-01 | `human-qa` | nem | RT-A11Y-01/-02 · független pre-flight | — |
| A11Y-03 (82) | húzásmentes egypontos út | DUPLICATE_OF:RT-P0-13 | `human-qa` | nem | RT-P0-13 · független pre-flight | spec: mind a 7 húzós elemnél a lecke előírja (M1.2 :797, M3.1 :576, M3.2 :679, M3.4 :436, M4.2 :661, M4.3 :485, M0.3 :233) |
| A11Y-04 (83) | nincs időzített továbblépés, Auto continue ki | DUPLICATE_OF:RT-A11Y-09 | `human-qa` | nem | RT-A11Y-09 + RT-P0-14 · független pre-flight | a beállítás rögzítve: STD :31, :83; RA 14 |
| A11Y-05 (84) | alt-szöveg / szöveges ekvivalens | RUNTIME_EVIDENCE_REQUIRED | `human-qa` | nem | elemenkénti pre-flight a renderen (RT-A11Y-03) · független pre-flight | 133 informatív vizuálból 121 alt-szövege a gyártás után készül; ÚJ: az M6.3-FOTO-02-nek és az M7.4-IKO-01-nek nincs ALTTEXT deliverable-je (repo-javítás, nem build) |
| A11Y-06 (85) | kontraszt | DUPLICATE_OF:RT-A11Y-11 | `human-qa` | nem | RT-A11Y-11 · független pre-flight | D1 paletta |
| A11Y-07 (88) | magyar nyelv + beszédes iframe-cím | REPO_FIX_REQUIRED | `build, repo-fixable` | **igen** (RR G5a „iframe-cím”) | build-szabály a MAN H5P-C profiljában vagy az STD-ben (H5P-tartalom nyelve = hu; cím = a MAN „Név” értéke), elsődleges forrással igazolva; RT-visszaolvasás (az RT-A11Y-03 bővítése vagy új sor) · `/course-fix` | ma sem a MAN-ben, sem az RA-ban nincs (0 találat; ellenőrizve); F-M5.4-3 (Név-oszlop) |
| A11Y-08 (89) | felirat + leirat + videónkénti AD-besorolás | RUNTIME_EVIDENCE_REQUIRED | `human-qa` | nem | RT-A11Y-06/-07, RT-P0-22 · független pre-flight | spec: mind a 27 videó besorolása megvan (szabad szövegben; az M1.1-VID-02 néma, alt-szöveges út); a videók C fázisúak |
| A11Y-09 (105) | felirat/leirat/AD (gyors-checklist) | DUPLICATE_OF:A11Y-08 | `post-build` | nem | mint A11Y-08 | — |
| A11Y-10 (106) | narráció nem csak hangban | DUPLICATE_OF:RT-P0-22 | `post-build` | nem | RT-P0-22 + RT-A11Y-07 | VO D-19, D-21 |
| A11Y-11 (107) | nincs autoplay | DUPLICATE_OF:RT-P0-23 | `post-build` | nem | RT-P0-23 + RT-A11Y-10 | 2026-10-03-B; STD :20 |
| A11Y-12 (108) | IV-jelenetek feliratozva | DUPLICATE_OF:RT-A11Y-06 | `post-build` | nem | RT-A11Y-06 | C fázis |
| A11Y-13 (109) | alt-szöveg (gyors-checklist) | DUPLICATE_OF:A11Y-05 | `post-build` | nem | mint A11Y-05 | — |
| A11Y-14 (110) | húzásmentes út (gyors-checklist) | DUPLICATE_OF:A11Y-03 | `post-build` | nem | mint A11Y-03 | — |
| A11Y-15 (111) | interakció-típus következetes a modulon belül | REPO_FIX_REQUIRED | `release-evidence, repo-fixable` | nem | ÚJ, validálandó: az M3-ban az M3.1 (:548) és az M3.4 (:400) Drag & Drop-elsődleges, az M3.2 (:679) koppintásos; az STD :32–33 szerint a D&D kerülendő, és ha mégis, a fejlesztői megjegyzésben indokolni kell · modulgazda (indoklás vagy típuscsere) | húzásmentes út mindenhol van (A11Y-03) |
| A11Y-16 (112) | mobil-táblázat = kártya/akkordeon | RUNTIME_EVIDENCE_REQUIRED | `post-build` | nem | RT-A11Y-05 mobil portrait | ÚJ: az M3.2 :573 „mobilon akár görgethető” ellentmond az STD :43-nak (repo-javítás, nem build); M1.4 :480, M7.4 :769 kártya-előírás nélkül (az STD szabálya globálisan köti a buildet) |
| A11Y-17 (113) | offline, alacsony adatigényű leckeváltozat + eszközhöz-jutás | REPO_FIX_REQUIRED | `build, repo-fixable` | **igen** (RR G5a, ahogy ma írva van) | a változat build-definíciója (erőforrás-típus, mely leckékhez, tartalom) a MAN-ben; vagy a Q-MED-1 fázismodellből levezetett hatókör-szabály (csak a videót/adatigényes médiát ténylegesen szállító leckékhez), az M4.1 :68-cal összhangban · `/course-fix` | ma csak elv (STD :52–58); MAN-sor és asset nincs |
| A11Y-18 (114) | letölthető sablon + online text | REPO_FIX_REQUIRED | `release-evidence, repo-fixable` | nem | a profil előírja (MAN :19–20); ÚJ, validálandó: deklarált sablon-asset csak az M3.4, M5.4, M6 Assignmentnél; az M1, M2, M4 (M4.4 :759 hivatkozik rá), M7 v1/v2 sablonja nincs deklarálva; a Z.4 tervezetten csak online text · `/course-fix` | „Online text ON” visszaolvasására nincs RT-sor |
| A11Y-19 (115) | szabad szöveg completion-alapú; Essay/FTQ korlát | DUPLICATE_OF:RT-P0-06 | `post-build` | nem | RT-P0-06 | spec teljes: TEXT-C (MAN :24), BSPEC-02 |
| A11Y-20 (116) | plain-language leckeszöveg | SIGNOFF_REQUIRED | `human-qa` | nem | a hozzáférhetőségi gazda (HUM-A11Y-01) átnézése; támogató: a lezárt magyar QA-naplók · hozzáférhetőségi gazda | RT-sor nincs |

Összesítés (38): `build` 4 (PR-01, PR-02, A11Y-07, A11Y-17); `human-qa` 14; `post-build` 11; `release-evidence` 6
(ebből 2 `repo-fixable`: A11Y-15, A11Y-18); `signoff` 3. A `repo-fixable` jelző, nem osztály: a
`classify_checklist` az osztályt a mellette álló szóból veszi.

## 4. A négy fotó (Phase 2)

| Asset | Pedagógiailag kell? | A fotó médium kell? | Meglévő nem-fotó asset? | Generált illusztráció? | Működik nélküle? | A blokkoló természete | Emberi döntés? | Javaslat |
|---|---|---|---|---|---|---|---|---|
| M0.3-FOTO-01 (Moodle főoldal screenshot) | hasznos tájékozódási segéd, nem feltétel (RMS 3.2: `OPTIONAL + RUNTIME_ONLY`) | a valós felület képe a természetes médium; kitalált UI-makett félrevezethet | nincs (a lecke egyetlen vizuálja) | nem javasolt (eltérhet a valós témától) | igen: a SLIDE 2 szövege (:147–160) és az alt-szöveg (:143) hordozza a szerkezetet; a dián nincs kérdés | R7: csak a kész Moodle-ből készülhet → körkörös build-függőség; R8 stagingből, tesztfiókkal kielégíthető | nem (RMS 3.2, Q-MED-1) | **ADD_NONPHOTO_FALLBACK** — átmeneti fallback = a meglévő diaszöveg + alt; a screenshot a staging build után készül (→ addig MEDIA_PENDING) |
| M0.A-FOTO-01 (kvuca-plakátok archív fotója) | a plakát megőrzése kell a Z.A „M0-tükörhöz”, a fotó nem | nem | igen: a fizikai plakát a stáb-dossziéban (alapút) és a Z.A név nélküli idézet-kártyái a képzői jegyzetből (Z.A :159–178) | nem értelmes (a kvuca saját szavai kellenek) | igen | nem Moodle-asset: képzői, helyszíni, opcionális felvétel; R8 + HUM-PRIV-02 (kiskorú kézírása, gondviselői hozzájárulás) | nem: a HUM-PRIV-02 (lezárt) alapértelmezése a felvétel nélküli megőrzés; az asset saját specje „Nem alapút” | **MAKE_OPTIONAL** — `fallback_final`: felvétel nélküli megőrzés (HUM-PRIV-02) + Z.A képzői jegyzet; az R8-követelmény a ténylegesen készülő fotóra marad |
| M4.1-FOTO-01 (képpár: karba tett vs. nyitott kéz) | a SLIDE 4 feladat lényege a két kiállás összevetése (:1044) | nem fotó: AI-karakterjelenet állóképe (provenance `ai`) | nincs | igen, opcionálisan: nem fotorealisztikus vonalrajz-pár (A fázisú pedagógiai grafika, R2-függés nélkül) | igen, szöveges kártyákkal: a két kérdés szövegből is megválaszolható (a 2. kérdés opciói leírják a képeket); a vizuális felismerés gyakorlása részben elvész | jogi médiakapu (R2; J1/J2/V1/V3 HIÁNYZIK) + a forrás C fázisú videó (M4.1-VID-03/04/05); az R5 szerint „a freeze-frame-ek a videó-gyártás részeként” készülnek; ráadásul a karba tett kéz egyik jelenet-specben sem szerepel (asset-megjegyzés) | nem: a Q-MED-1 (C fázis: karakterjelenet; jogfüggő elemnél A/B-s statikus vagy szöveges fallback) és az R5 közvetlen alkalmazása; vétó/QA: médiafelelős + programvezető | **ADD_NONPHOTO_FALLBACK** — `release_phase: C` + fallback: bal/jobb jelölésű szöveges leíró kártyák a lecke saját alt-mintái szerint (:1046), az AI-címke nélkül; opcionális javítás: vonalrajz-pár |
| M4.1-FOTO-02 (képpár: földre nézés vs. körre nézés) | mint fent | mint fent | nincs | mint fent | igen (a 2. kérdés opciói szövegben írják le a két képet) | mint fent (forrás: M4.1-VID-03/05) | nem | **ADD_NONPHOTO_FALLBACK** — mint FOTO-01 |

**Közös előfeltétel:** a média-manifestben egyik asset sem hordoz `release_phase`, `fallback` vagy `fallback_final`
mezőt, és a `tools/media_manifest.py` sem ismeri őket (csak a `content_integrity.py` olvassa). A release-modell v2
migrációs terve ezt 7. fázisként jelöli („következik”). A fenti négy javaslat ezért csak a séma bővítése (eszközkód +
tesztek) után rögzíthető az `@asset` deklarációkban.

## 5. Deduplikált repo-javítási lista

| # | Tétel | Build? | Út | Validálás |
|---|---|---|---|---|
| R-1 | BSPEC-05 és BSPEC-06 felvétele `BUILD_SPEC_OPEN`-ként a MAN nyilvántartásába | igen (regisztráció) | `/course-fix` | H-1/O-1/H-4 verifier által validált megfigyelés |
| R-2 | a 38 tétel gate-jelölése a 3. pont szerint | igen (a verdikt őszintesége) | `/course-fix` | projektgazdai jóváhagyás |
| R-3 | `release_phase`/`fallback`/`fallback_final` a `media_manifest.py` sémájában + tesztek | igen (a fotók előfeltétele) | eszközkód (nem tananyag-skill), kifejezett kérésre | — |
| R-4 | a 4 fotó `@asset` mezői; M4.1 SLIDE 4 fallback-szövege; média-build külön `chore(media)` commitban | igen | `/course-fix` (R-3 után) | — |
| R-5 | BSPEC-05: BS completion-beállítás + tartalékút-sorok (M2.3, M6.4) / indokolt „nincs tartalékút” (M3.3, M5.2) | igen | kutatás (elsődleges forrás) → `/course-fix` | C-1 és a kiterjesztés: validálandó |
| R-6 | BSPEC-06: H5P-C (és C-1 után ASSIGN-S) Moodle completion-beállítás; az R-24 döntés után | igen | kutatás → `/course-fix` | validálandó |
| R-7 | PR-01: adatleltár build-része + mentor-mechanizmus | igen | kutatás → `/course-fix` (feltételes DPO-döntés) | — |
| R-8 | PR-02: kurzusszintű tájékoztató szövege build-jelölőkkel | igen | `/course-fix` | — |
| R-9 | A11Y-07: nyelv + iframe-cím szabály, RT-visszaolvasás | igen | `/course-fix` | — |
| R-10 | A11Y-17: az offline változat build-definíciója vagy hatókör-szabálya | igen | `/course-fix` | — |
| R-11 | SG-01 hatókörének összhangja a GK §2-vel (és RR :40) | nem | `/course-fix` (szó szerinti átvezetés) | — |
| R-12 | H-5: M7 hub :243 SMART cél | nem (learner) | `/course-fix` (pin) | validált |
| R-13 | A11Y-15 M3 interakció-következetesség | nem (learner) | `/course-fix` | ÚJ, validálandó |
| R-14 | A11Y-16 M3.2 :573 görgethető táblázat | nem (learner) | `/course-fix` | ÚJ, validálandó |
| R-15 | A11Y-18 hiányzó sablon-assetek (M1, M2, M4, M7) + RT-sor az „Online text ON”-ra | nem (learner) | `/course-fix` | ÚJ, validálandó |
| R-16 | A11Y-05 ALTTEXT deliverable: M6.3-FOTO-02, M7.4-IKO-01 | nem (learner) | `/course-fix` | ÚJ, validálandó |
| R-17 | F-M5.4-2, F-M5.4-3 | nem | `/course-fix` | validált |
| R-18 | F-M0.4-6, F-M0.4-7, F-M3.4-4 (produktum-fele), F-M3.4-6 | nem (learner) | `/course-fix` | validált |

## 6. Emberi döntések

**A továbblépéshez most:** (D-a) a 3. pont besorolásainak jóváhagyása, különösen a négy `build` tételé; (D-b) a
BSPEC-05/06 felvétele; (D-c) az R-3 eszközmunka ezen az ágon vagy külön ágon.

**A buildet a BSPEC-06-on át érinti:** R-24 — az M7.4 SLIDE 4 nem pontozott fókuszválasztása completion-elem-e
(értékelési felelős / projektgazda). Feltételes: ha a BSPEC-05/06 kutatása szerint a megvalósítható Moodle-beállítás
gyengítené a lecke completion-szabályát, az a projektgazda döntése (a completion-logika tananyag-invariáns).

**Feltételes (PR-01):** ha nincs core tanulónkénti mentor-láthatóság, elfogadható-e a szerepkör-szintű (DPO/jogi
felelős).

**Learner-release, változatlanul nyitva (nem old meg ez a kör):** N-1, N-3, N-4 (SG-06), N-5…N-9; BIZT-R5 (LMS-M2-07,
DPO; projektgazda someres vonatkozásban); LMS-Z-06 megőrzése (BS-D6, DPO); H-3 (értékelési felelős); PR-04 törlési
eljárás és felelős (DPO); a BSPEC-02 1–7. fájl 7. szakaszának nyitott tételei (#3, #5–#9); Memuna-QA a BSPEC-02-ben
átírt veszély-dobozokra.

## 7. Bizonyíték-kapuk (nem írjuk be, nem feltételezzük)

- **FINAL_RELEASE_QA (`human-qa`):** Memuna „átnéztem” (SG-01, SG-03, SG-04, SG-07, SG-08); DPO release-ellenőrzés
  (PR-07); független a11y pre-flight + hozzáférhetőségi gazda (A11Y-01…08, A11Y-20).
- **SIGNOFF:** jogi szakértő (SG-10); jóváhagyás/felülvizsgálat dátuma (SG-11); passzjog-döntés (SG-06/N-4); Go/No-Go
  (RR :113).
- **RELEASE-EVIDENCE:** segélyvonalak napi ellenőrzése (SG-05); stáb-alkalmasság (SG-09); törlési folyamat (PR-04);
  felvételi hozzájárulási folyamat (PR-06); valódi kontaktok (RR G8).
- **POST-BUILD / RUNTIME:** RT-P0-01…24 (benne RT-P0-24) és RT-A11Y-01…12 (36); 70 `BUILD_OUTPUT`; 17
  `RUNTIME_OUTPUT` környezeti sor; G4b visszaaudit; SG-02, PR-03, PR-05 és az A11Y-duplikátumok.
- **G1/G2/G3b** ezekből zárul; a HUM-tételek lezárása nem release-jóváhagyás.

## 8. Javasolt BSPEC-sorok (szövegjavaslat, a `/course-fix` R-1 lépéséhez)

| ID | Állapot | Tárgy | Hol | Döntés / forrás |
|---|---|---|---|---|
| BSPEC-05 | `BUILD_SPEC_OPEN` | a Branching Scenario-alapú H5P activityk Moodle completion-beállítása és tartalékútja: LMS-M2-04 (M2.3 :11, :114; M2 hub :81 „Moodle-checkpoint”), LMS-M6-04 (M6.4 :104; a „Tovább a lezáráshoz” minden ág után elérhető), LMS-M3-03, LMS-M5-02 | §1 H5P-C; §2; runtime acceptance 2., 5., 10., 11., 18. pont | BSPEC-02 leltár H-1 és M6.4 O-1 (verifier: külön BSPEC-sor); precedens: BSPEC-01; RR G3a |
| BSPEC-06 | `BUILD_SPEC_OPEN` | a H5P-C profil Moodle completion-beállítása (a leckék interakciónkénti completion-halmazai, pl. M0.1 :13; nyitott: M7.4 :14 SLIDE 4) — validálás után az ASSIGN-S megerősítés kódolása és a MAN §4 „ugyanez a checkpoint-út” | §1 H5P-C, ASSIGN-S; §4; runtime acceptance 1., 9., 14. pont | BSPEC-02 leltár H-4; R-24; RR G3a |

## 9. Javasolt sorrend

1. Projektgazdai jóváhagyás: D-a, D-b, D-c (6. pont).
2. `/course-review` validálás a ÚJ tételekre (C-1, BS-kiterjesztés, A11Y-15/16/18, R-16).
3. `/course-fix` A csomag: R-1, R-2, R-11 (regisztráció és jelölés — a verdikt utána is `NOT_READY`, de minden
   blokkoló regiszterben).
4. R-3 eszközmunka (séma + tesztek), majd `/course-fix` B csomag: R-4 → média-build.
5. Kutatás (Moodle/H5P elsődleges forrás) → `/course-fix` C csomag: R-5, R-6 (R-24 után), R-7, R-8, R-9, R-10.
6. `/release-check`.
7. A learner-release javítások (R-12…R-18) bármikor, a build-úttól függetlenül.
