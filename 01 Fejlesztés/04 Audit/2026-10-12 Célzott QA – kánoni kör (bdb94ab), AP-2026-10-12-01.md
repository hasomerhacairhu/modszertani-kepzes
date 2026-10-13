# 2026-10-12 Célzott QA – kánoni kör (bdb94ab), AP-2026-10-12-01

- **Scope:** a HUM 14. szakasz döntéseinek kánoni átvezetése (`bdb94ab`): `LMS – activity manifest.md`, `LMS – H5P runtime acceptance.md`, `Adatvédelem – tanulói adatok és AI.md`, `Program terv.md`, `Gyermekvédelem – release gate.md`, `LMS – hozzáférhetőségi sztenderd.md`, `Glosszárium`. Csak a diff-hunkok és közvetlen környezetük; nem teljes új audit.
- **Lencsék (ténylegesen lefutott):** biztonság-jog (`safety-policy-reviewer`), értékelés + LMS (`assessment-reviewer`, IMPL-tételekkel; egy folytatással a levágott 3 tételre), nyelv (`hungarian-editorial-reviewer`). Adverzális második kör: `verifier`, két csoportban, mind a 34 ID-ra.
- **Run-ID:** AP-2026-10-12-01 · **Review-bázis:** `bdb94ab` · **Javítás:** `35a9ddd` (látható szöveg; a generált média nem változott).
- **Állapot:** VALIDÁLT.

## I. Riport

### 1. Validált objektív findingok — javítva (`35a9ddd`)

| ID | Súly | Hely | Javítás |
|---|---|---|---|
| CANON:QA-ERT-1 (RÉSZBEN; + QA-NYELV-13; ERT-9) | P1 | manifest ASSIGN-M profil, §4 M1/M6/M7 sor | SUBMITTED/CONFIRMED szétválasztás; az M3 sora nem változott (lent); vétólista: completion-szöveg |
| CANON:QA-NYELV-9 (ERT-9) | P2 | manifest LMS-M7-06 | „egy „Receive a passing grade” kipipálása az Assignmenten” |
| CANON:QA-ERT-3 (RÉSZBEN; ERT-40) | P2 | PT:257, :263; manifest §7 | darabszám-alapú küszöb („≥12/14 teljesen helyes item”) |
| CANON:QA-ERT-5 (ERT-40) | P2 | RA 8. pont | a 11 + 2 negatív eset: a részpontok összege ≥1, a nyers pont ≥12 |
| CANON:QA-IMPL-3 + QA-NYELV-12 (ERT-1, ERT-2) | P2 | manifest H5P-C profil, LMS-Z-02/-03; RA 9. pont | tartalékút a profilban; várt eredmény; „a CP csak akkor kap” |
| CANON:QA-IMPL-1 (RÉSZBEN) + QA-NYELV-14 (ADV-6) | P1 | manifest kurzusteljesítés; LMS-M0-05 | a zárt fórum nem kurzusteljesítési kritérium; „jogszerű” vissza; vétólista |
| CANON:QA-IMPL-2 (RÉSZBEN; ERT-48) | P1 | manifest új sor LMS-M7-12; LMS-M7-02 | az AI-jártassági Page saját PAGE-C sora; az LMS-M7-02 unlockja változatlan; vétólista: új completion-elem |
| CANON:QA-ERT-6 (RÉSZBEN) | P2 | manifest QUIZ-M profil, „Mentor-láthatóság” | a `bdb94ab` által felülírt mentori tartalom vissza, mellette az ERT-5 tanulói visszanézési szabálya |
| CANON:QA-IMPL-4 (RÉSZBEN; LMS-3) | P2 | manifest LMS-M5-07 | a completion a választott profil szerint, hamis „Receive a grade” nélkül; vétólista |
| CANON:QA-IMPL-5 (RÉSZBEN; ERT-39) | P2 | manifest §3 offline események, LMS-Z-04 | a Z.A-hoz kötött tartalom nyitása nem köthető jelenléti checkpointhoz |
| CANON:QA-IMPL-7 (RÉSZBEN; ADV-3, LMS-5) | P2 | manifest BSPEC-02 | a leltár a Z.3 és az M7.3 tanuló-lokális lépéseivel bővül; a Z.3 5. dia besorolása emberi döntés |
| CANON:QA-IMPL-6 (ADV-1) | P2 | manifest TEXT-C profil | a BIZT-2 hozzáférésről a döntés rendelkezik (szűk, név szerinti, auditálható; az admin hozzáférését a tájékoztató nem tagadja) |
| CANON:QA-NYELV-10 (RÉSZBEN; ERT-41) | P2 | manifest LMS-M7-06 | kitöltési pótlás, rövid, érthető, nem értékelő visszajelzés; a „nem értékelő” marad |
| CANON:QA-NYELV-11 (ERT-6) | P2 | manifest LMS-M5-06, LMS-M6-06 | a döntés szövege szerinti alak |
| CANON:QA-NYELV-8 (ERT-3) | P2 | RA 16. pont | a csonka mondat javítva |
| CANON:QA-BIZT-2 + QA-NYELV-5 (GYV-10, LMS-8, ADV-12) | P2 | ADV §7, RA 20. pont, PT AI-pont | az LMS-8 review-feltétele mindenütt; „a tanulói AI-segéd ki van kapcsolva” |
| CANON:QA-BIZT-3 (a) (ADV-2) | P2 | ADV §11 „Ki látja?” | az F-peula képzőjének hiánylistája (a §5 mondata) |
| CANON:QA-ERT-4, QA-NYELV-6, QA-NYELV-7 (RÉSZBEN; ERT-8) | P2 | PT §5, §6; GL; A11Y (következmény) | „is kiváltja, és ez nem bukás” |
| CANON:QA-BIZT-6 (ADV-14) | P2 | PT:113, :213 | a Z videója csak bekapcsolt videós úttal |
| CANON:QA-NYELV-1, -2, -3, -15 (ADV-9, TERM-5, ADV-10, GYV-5) | P2 | ADV:53, :82, :83; GK:65 | alaptag és minősítő vissza; „helyzetleírás”; „legyen” |

### 2. Emberi döntést igénylő tételek

| ID | Mit kell eldönteni | Kitől |
|---|---|---|
| CANON:QA-BIZT-1 (ADV-1) | kiterjed-e az ADV-1 (c) csoportszűkítése a H5P-C, a QUIZ és a GATE-CP mentori nézetére (a döntés „beadást” mond, a döntési csomag kérdése a négy profilt nevezte meg); addig átmeneti szöveg az ADV §3 :104, :109 és §11 :232 helyén | projektgazda; vétó/QA: DPO / jogi felelős |
| CANON:QA-ERT-2 (ERT-9) | hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy a kapukvíz (LMS-M3-06) csak a megerősített rubrika után nyíljon (külön GATE-CP vagy M3-kivétel) | projektgazda mint build-spec gazda; QA: értékelési felelős |
| CANON:QA-BIZT-4 (GYV-11) | a „kikerül a Moodle-ből” (HUM-PRIV-01) a GYV-11 szerinti jóváhagyott korlátozást/törlést jelenti-e, az incidensnyilvántartásba mentés után | Memuna + DPO |
| CANON:QA-BIZT-5 (ADV-12) | az AI-végpont technikai metaadatainak jogalapja és megőrzési ideje az ADV §3 táblában | DPO / jogi felelős; QA: programvezető |
| CANON:QA-BIZT-3 (b) (GYV-10, LMS-8) | kell-e és milyen szöveggel kerüljön a tanulói tájékoztatóba (ADV §11) a képző által közvetített AI-út | programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| CANON:QA-IMPL-7 (b) (ADV-3) | a Z.3 5. dia célmondata kötelező vagy opcionális tanuló-lokális lépés | projektgazda (X-6 szerint) |

### 3. Bizonyíték-kapu

Nincs új.

### 4. Elvetve

- CANON:QA-NYELV-4 — a mondat nyelvtanilag helyes; a „csak” a Memunára az ADV-2 szövegében sincs meg.

## B. Verifier-verdiktek (szó szerint)

<!-- agent a5a716f35fc0d24f3 -->

## Adverzális második kör, A csoport (bdb94ab, kánoni kör): 18 ID

Mind a 18 ID-t visszaolvastam a fájlokban és a diffben. Hamis idézetet nem találtam, ELVETVE verdikt nincs. Kilenc findingnál a probléma valós, de a javaslatból csak egy rész használható (RÉSZBEN). Egy finding emberi döntés (ERT-2), egy pedig duplikátum (NYELV-13 → ERT-1).

Röviden, mi a baseline és mi a bdb94ab következménye:
- **Baseline, nem a bdb94ab nyúlt hozzá:** az ASSIGN-M profil (MAN:20) és a kurzusteljesítés szabálya (MAN:167).
- **A bdb94ab szerkesztésének következménye:** az ERT-6 a 251→252. diffsor regressziója. Az IMPL-4 is ide tartozik: a régi profilcella („a sor completionje interakció, nem megtekintés”) eltűnt, a Completion cella viszont maradt.

### K-ERT9 (megtartandó: ERT-1)

**CANON:QA-ERT-1 | RÉSZBEN | objektív | P1**
- **Indok:** A MAN:20 profilcellája ezt írja: „beadvány leadva **és** megerősített kapueredmény”. Az ERT-9 (HUM:679) szerint viszont „ASSIGN-M saját completion = SUBMITTED; … CONFIRMED állapot külön GATE-CP-n álljon be”.
  - A §4 MAN:158/163/164 sorai „LMS-M1-05 mastery” formában írnak. Az M5-sor (:162) már az új minta.
  - Az RA 1. pontjába javasolt új visszaolvasási sor nem következik szó szerint az ERT-9-ből, ezért kimarad.
- **Javítás:**
  - **MAN:20, „Alapértelmezett completion” cella.** OLD: „beadvány leadva **és** megerősített kapueredmény (… teljes zárójel …)”. NEW: „két külön állapot (projektgazdai döntés, 2026-10-12, ERT-9; D-h): **SUBMITTED** – az Assignment saját completionje a leadás („Make a submission”, `completionsubmit`); **CONFIRMED** – a tényleges szakmai kapueredmény a modul külön GATE-CP során áll be (LMS-M1-06, LMS-M5-08, LMS-M6-07, LMS-M7-08), a kapufájl teljes feltétele szerint, nem a nyers pont alapján; egy „Receive a passing grade” kipipálása az Assignmenten nem helyettesíti a kritikus rubrikasorok és a mentor-konfirmáció összetett feltételeit; a korábbi pontküszöb nem változik. A kétkomponensű M3 kapunál a kapukvíz az Assignment-komponens megerősített rubrikája után nyílik; ennek kódolása ERT-9 mellett nyitott (build-spec gazda; CANON:QA-ERT-2). Az M7-nél a kvíz a v2 előtt fut, ezért a v2 csak a kvíz megerősített eredménye után adható le.”
  - **MAN:158:** „LMS-M1-05 mastery” → „LMS-M1-05 leadva + LMS-M1-06 „Teljesítve””.
  - **MAN:163:** „LMS-M6-05 mastery” → „LMS-M6-05 leadva + LMS-M6-07 „Teljesítve””.
  - **MAN:164:** „LMS-M7-07 mastery (a v2 előtt) + LMS-M7-06 mastery” → „LMS-M7-07 + LMS-M7-09 „Teljesítve” (a v2 előtt) + LMS-M7-06 leadva + LMS-M7-08 „Teljesítve””.
  - **Korlát:** az M3 §4-sorához (:160) és az LMS-M3-05/06 sorhoz nem nyúlunk. Az RA-hoz és a küszöbökhöz sem. Completion-szöveg változik, ezért vétólistára kerül.

**CANON:QA-ERT-2 | MEGERŐSÍTVE | emberi-döntés | P1**
- **Indok:**
  - LMS-M3-05 (MAN:66): „leadva + megerősített rubrika”.
  - LMS-M3-06 (MAN:67) unlock: „az LMS-M3-05 megerősített rubrikája (§7: az M3 kapuablaka)”.
  - Az M3 modulban nincs ERT-9-blokk; a canon_blocks és a Modulok/M3 grepje is üres.
  - Az ERT-9 szó szerint lefedi az ASSIGN-M-et. Ha viszont az LMS-M3-05 completionje SUBMITTED lesz, a kapukvíz nyitásához új mechanizmus kell (külön GATE-CP vagy kivétel). Ez új manifest-sor vagy új alkalmazási eset, tehát nem szó szerinti átvezetés.
- **Döntési igény:** ki dönt: a projektgazda mint build-spec gazda, QA-ként az értékelési felelős. Mit: az LMS-M3-05 hogyan kap SUBMITTED completiont úgy, hogy az LMS-M3-06 csak a megerősített rubrika után nyíljon (külön GATE-CP az Assignment-komponensre, vagy kifejezett M3-kivétel). Addig a MAN:66/67/160 változatlan.

**CANON:QA-NYELV-13 | MEGERŐSÍTVE (duplikátum → CANON:QA-ERT-1) | objektív | P2**
- **Indok:** A §4-es rész ugyanaz, mint az ERT-1 MAN:158/163/164 pontja. A §2-sorok szerkezeti egységesítése, és a „jegyalapú completion kikapcsolva” betoldása az M6/M7-sorba, stílusjavaslat. A MAN:91/103 „leadva (SUBMITTED, `completionsubmit`)” szövege már a SUBMITTED-completiont rögzíti, ezért ez a rész nem hiba.
- **Javítás:** csak az ERT-1 szerint.

**CANON:QA-NYELV-9 | MEGERŐSÍTVE | objektív | P2**
- **Indok:** MAN:103: „egy „Receive a passing grade” az Assignmenten nem helyettesíti” – hiányzó alaptag (1. regressziós minta). Az ERT-9 szövege (HUM:679): „Egy „Receive a passing grade” kipipálása az Assignmenten…”.
- **Javítás:** MAN:103: „egy „Receive a passing grade” az Assignmenten” → „egy „Receive a passing grade” kipipálása az Assignmenten”. A döntés saját szava kerül be, nem a javasolt „bekapcsolása”.

### K-ERT40

**CANON:QA-ERT-3 | RÉSZBEN | objektív | P2**
- **Indok:** A PT:263 az M7-et az „általában **≥80%**” szabály alá sorolja („az M7 14 itemes kapujánál **≥12/14**”). Közben az M7 kánoni köre (M7#30/31) a PT M7-helyeiről éppen a „≥80% =” formulát vette ki, a PT:112/203/275 pedig már ezt írja: „teljesen helyes item, darabszám-alapú”. A PT:257 és a MAN:175 „≥12/14 ÉS a Q13” alakja pontatlan összefoglaló. A §4 M7-sort az ERT-1 javítása kezeli.
- **Javítás:**
  - **PT:263:** „(a 12 itemes kvízeknél ez **≥10/12**, az M7 14 itemes kapujánál **≥12/14**)” → „(a 12 itemes kvízeknél ez **≥10/12**); az M7 14 itemes kapujánál a küszöb darabszám-alapú: **≥12/14 teljesen helyes item**, nem átszámított részpontszázalék (ERT-40)”.
  - **PT:257:** „≥12/14 ÉS a gyermekvédelmi Q13” → „≥12/14 teljesen helyes item ÉS a gyermekvédelmi Q13”.
  - **MAN:175:** „(≥12/14 ÉS a Q13 helyes)” → „(≥12/14 teljesen helyes item ÉS a Q13 helyes)”.
  - **Korlát:** szám nem változik.

**CANON:QA-ERT-5 | MEGERŐSÍTVE | objektív | P2**
- **Indok:** RA:57: „11 teljesen helyes + 2 részpontos Multi-Select item, amely a „Grade to pass = 12” mellett sem teljesülhet: ERT-40”. Ha a két részpont összege 1 alatt marad, a nyers pont 12 alatt van, és a teszt nem azt a hibamódot próbálja ki, amely ellen az ERT-40 szól („Ne engedjen át „Grade to pass 12” önmagában”, HUM:710). Ez számtan, nem runtime-állítás.
- **Javítás:** RA:57: „11 teljesen helyes + 2 részpontos Multi-Select item, amely a „Grade to pass = 12” mellett sem teljesülhet: ERT-40” → „11 teljesen helyes + 2 részpontos Multi-Select item, ahol a két részpont összege legalább 1 (nyers pont ≥12): a kapu a „Grade to pass = 12” teljesülése mellett sem teljesülhet: ERT-40”.

### K-ERT1

**CANON:QA-IMPL-3 | MEGERŐSÍTVE | objektív | P2**
- **Indok:**
  - A tartalékút csak a MAN:106/107 Z-soraiban áll. A H5P-C profilban (MAN:16) és az LMS-M0-01-nél (MAN:39) nincs ott, pedig az ERT-2 (HUM:672) kifejezetten ezt írja: „M0.1-nél ezt kifejezetten rögzítsük, nehogy a completion feltétel nélkül megszűnjön”.
  - Az RA:72 várt eredmény nélkül zárul: „rögzíteni kell … hogy ilyenkor keletkezik-e grade, és beáll-e a completion”.
  - A döntési csomag ERT-1 következménye szerint az összefoglaló dia „megválaszolás nélkül is teljesít”.
- **Javítás:**
  - **MAN:16:** a „(runtime acceptance 9. pont).” után szó szerint a Z-02 mondata: „Ha a CP-nek a célverzión nincs összefoglaló diája, a completion-alapot (megtekintés/összefoglaló vagy más legitim aktivitás) a build-spec gazda rögzíti, és a választó nem lehet pontozott vagy önálló completion-elem (ERT-2, ADV-4).”
  - **RA:72**, a mondat végére: „Várt eredmény (ERT-1): az összefoglaló dia elérésével a completion megválaszolatlan interakciók mellett is beáll; ha a célverzión nem áll be, a pontozatlan választós sorok (LMS-M0-01, LMS-Z-02, LMS-Z-03) completion-alapját a build-spec gazda rögzíti, és a választó nem válhat completion-elemmé (ERT-2).”

**CANON:QA-NYELV-12 | MEGERŐSÍTVE | objektív | P2**
- **Indok:** MAN:106/107: „a completion az összefoglaló dia elérése …; erre épülő completiont csak akkor kap” – a „kap” igének nincs alanya.
- **Javítás:** mindkét sorban „erre épülő completiont csak akkor kap” → „erre épülő completiont a CP csak akkor kap”. Ha az IMPL-3 mondata a profilba kerül, ez a forma megy át.

### K-ADV6 (egy összehangolt szerkesztés)

**CANON:QA-IMPL-1 | RÉSZBEN | objektív | P1**
- **Indok:** Az LMS-M0-05 (MAN:43) „Kötelező” cellája „igen”, a sor szövege viszont ezt mondja: „addig nem completion-feltétel”. A MAN:167 szerint „activity-kritérium minden „Kötelező = igen” §2-sor”, így egy zárt fórum kurzusteljesítési kritérium lenne. A §4 M0-sora (:157) már feltételes.
- **Javítás:**
  - **MAN:167:** „activity-kritérium minden „Kötelező = igen” §2-sor,” → „activity-kritérium minden „Kötelező = igen” §2-sor (az LMS-M0-05 csak akkor, ha a fórum az ADV-6 feltételeivel valódi tanulóknak megnyílt),”.
  - **Korlát:** a „Kötelező” cella átírása nem szükséges (besorolás-szöveg), maradjon. Vétólista.

**CANON:QA-NYELV-14 | MEGERŐSÍTVE | objektív | P2**
- **Indok:** MAN:43: „nem automatikus alapérték”. Az ADV-6 szövege (HUM:652): „nem automatikus jogszerű alapérték”. A minősítő a M0#32 modulblokkból már kiesett (2. regressziós minta).
- **Javítás:** MAN:43: „nem automatikus alapérték” → „nem automatikus jogszerű alapérték”.

### Önálló findingok

**CANON:QA-NYELV-10 | RÉSZBEN | objektív | P2**
- **Indok:** MAN:103: „pótlást kér, nem értékelő visszajelzéssel; tartalmilag nem pontozza, nem buktat, és a v2 szakmai értékelését nem akadályozza”.
  - Az ERT-41 „kitöltési” és „értelmezhető” minősítője kiesett.
  - A „nem akadályozza” alanya az értékelőre csúszott.
  - Az M7 KAPU:260 helyes mintája: „pótlást kér, és rövid, érthető, nem értékelő visszajelzést ad; ez nem buktatja a kaput”.
  - A korábbi verifierhez (M7:QA-NYELV-7) igazodom: a „nem értékelői” alakot elvetem, a KAPU 263/426/427 nem változik.
- **Javítás:** MAN:103: „pótlást kér, nem értékelő visszajelzéssel; tartalmilag nem pontozza, nem buktat, és a v2 szakmai értékelését nem akadályozza” → „kitöltési pótlást kér, és rövid, érthető, nem értékelő visszajelzést ad; a mezőket tartalmilag nem pontozza; a hiány nem buktatja a kaput, és a v2 szakmai értékelését sem akadályozza”.

**CANON:QA-ERT-6 | RÉSZBEN | objektív | P2**
- **Indok:** A regressziót a diff igazolja. A 251. sor („-”) a „Mentor-láthatóság” oszlopban ezt tartalmazta: „eredmény + item-szintű review ott, ahol kritikus item van”. A 252. sor („+”) ezt az ERT-5 tanulói Review options szövegére cserélte (MAN:18). A javaslat „(a GATE-CP kézi megerősítéséhez: LMS-M3-07, LMS-M7-09)” betoldása forrás nélküli indoklás (8. regressziós minta), ezért kimarad.
- **Javítás:** MAN:18, 6. oszlop. NEW: „eredmény + item-szintű review ott, ahol kritikus item van; tanulói Review options (ERT-5, projektgazdai döntés, 2026-10-12): az első próbálkozás után a pontszám és a hibázott kompetencia / kritikus követelmény; a helyes kulcs és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; a kritikus itemekhez (M3, M7) a mentor szabályos javítási útmutatást ad; az eltérő Review options célverzión visszaolvasandó”.

**CANON:QA-IMPL-2 | RÉSZBEN | objektív | P1**
- **Indok:** Az M7.2:9 szerint: „Completion (lecke): az AI-jártassági blokk megtekintését a befogadó Moodle-oldal completionje jelöli”. Az M7.2:88 szerint: „Moodle-oldal (Page) a Moodle-intro után, a H5P Course Presentation előtt”. Az ERT-48 (HUM:718): „a kötelező tanulási tartalom megtekintését a befogadó activity completionje jelölje”. A Page-nek nincs §2-sora (MAN:96). A modulszöveg és a döntés együtt egyértelműen előírja, ezért ez a 2. szabály szerint objektív.
- **Javítás:**
  - Új sor az LMS-M7-02 elé: „| LMS-M7-12 | BUILD_OUTPUT | M7 | M7.2 – AI-jártassági blokk | PAGE-C | igen | M7/Online leckék/M7.2 | LMS-M7-10 | profil: megtekintés | nincs | M7_L2 | a lecke része: ahol a §4 a lecke H5P-jére hivatkozik, ez a sor is beleértendő; a beágyazott H5P ellenőrző kérdés lehetőleg próbálkozás-rögzítés nélkül, nem külön pontozva, nem önálló completion-elem, külön H5P-activity és gradebook-nyom nélkül; a blokk megtekintését ennek az oldalnak a completionje jelöli; no-AI azonos teljesítési út (ERT-48, HUM-PRIV-04) |”.
  - MAN:96: „Moodle-oldal (Page)” → „Moodle-oldal (Page, LMS-M7-12)”.
  - **Korlát:** az LMS-M7-02 unlockjának átkötése nem objektív, ezt a build-spec gazda dönti el. Új completion-elem, ezért vétólista.

**CANON:QA-IMPL-4 | RÉSZBEN | objektív | P2**
- **Indok:** A MAN:85 Completion cellája: „a forrás szerinti felidézési interakció elvégzése”. Az LMS-3 (HUM:740) és az M5.3:529 szerint viszont a felidézés saját jegyzetben történik, beviteli elem nélkül, a profilt pedig a teszt dönti el. A javaslat megtekintéses PAGE-C-completiont rögzítene; ez túlmegy az LMS-3-on.
- **Javítás:** MAN:85: „a forrás szerinti felidézési interakció elvégzése” → „a választott profil szerint; üres Course Presentationre hamis „Receive a grade” completion nem állítható, pontozott önellenőrző item csak jóváhagyott tartalommal kerülhet mellé; a végleges completiont a valós H5P és ennek a sornak a tesztje dönti el (LMS-3; runtime acceptance 4. pont)”. Vétólista.

**CANON:QA-IMPL-5 | RÉSZBEN | objektív | P2**
- **Indok:** A MAN:135 szerint: „vagy, ha később tényleges jelenléti checkpoint készül, annak igazolt completionjével nyitjuk”. Ez a Z.A-ra ellentmond az ERT-39-nek (HUM:709): „Hiányzó jelenlét ne akadályozzon…”. A Z-05 (MAN:112) már „jelenléti feltétel nélkül”, a Z-04 (MAN:110) nem. A javasolt „jelenléti checkpointtal sem nyitható” megfordítja a jelentést, ezért ez a szöveg nem használható.
- **Javítás:**
  - MAN:135 végére: „A Z.A-hoz kötött online tartalom (LMS-Z-04, LMS-Z-05) nyitása nem köthető jelenléti checkpointhoz (ERT-39).”
  - MAN:110 unlock: „**Z.A után, a §7 szerinti dátummal**” → „**Z.A után, a §7 szerinti dátummal** (jelenléti feltétel nélkül, ERT-39)”.

**CANON:QA-IMPL-7 | RÉSZBEN | objektív + emberi-döntés | P2**
- **Indok:** Az RA:107 listája tartalmazza az „LMS-M7-03 … LMS-Z-03” sorokat. A BSPEC-02 (MAN:311) leltárából a Z.3 és az M7.3 hiányzik.
  - A Z.3 7. dia az LMS-Z-03-ban és a Z.3:339-ben kifejezetten opcionális.
  - A Z.3 5. dia kötelező/opcionális besorolását se a MAN:107, se a Z.3:264–266 nem mondja ki. A finding a kötelező besorolást következtetéssel kapja; ez a HUM:649 ADV-3 sora szerint az X-6 tárgya.
- **Javítás:** a MAN:311 cella végére: „**Kiegészítés (2026-10-12; projektgazdai döntés, `Emberi jóváhagyás szükséges.md` 14. szakasz):** az „opcionális, tanuló-lokális” lista a Z.3 7. dia mini válaszával bővül (LMS-Z-03; ADV-3); a Z.3 5. dia célmondata (LMS-Z-03; ADV-3) és az M7.3 Zmán Kvucá-checklist (LMS-M7-03; LMS-5) tanuló-lokális, külön sor nélkül; rögzítésmentességük visszaolvasása: runtime acceptance 24. pont. A sor állapota nem változik.”
- **Döntési igény:** a Z.3 5. dia kötelező vagy opcionális besorolása; a projektgazda dönt, az X-6 szerint.

**CANON:QA-NYELV-8 | MEGERŐSÍTVE | objektív | P2**
- **Indok:** RA:87: „Tesztelni kell, hogy az 1. kérdés „Required”, a többi kihagyható, és stagingben a „kiürítés” valós működését is”. A hogy-mellékmondat és egy tárgy van mellérendelve, a mondat csonka.
- **Javítás:** a javaslat szerint: „Tesztelni kell, hogy az 1. kérdés „Required”, a többi pedig kihagyható; stagingben a „kiürítés” valós működését is tesztelni kell (ERT-3; projektgazdai döntés, 2026-10-12; a „kiürítés” pontos jelentését a build-spec gazda rögzíti).”

**CANON:QA-NYELV-11 | MEGERŐSÍTVE | objektív | P2**
- **Indok:**
  - MAN:84: „a tanulói és a stáb-jelzés az első, visszajelzés előtti próbálkozásból számol” – az igének rossz az alanya.
  - MAN:92: „a diagnosztikus jelzés az első, visszajelzés előtti próbálkozás” – azonosító állítás lett belőle. Az ERT-6 (HUM:676) szövege: „Diagnosztikus jelzéshez az első … próbálkozás a mérvadó; … nem írják felül a korai szükségletet”.
- **Javítás:**
  - **MAN:84:** „a tanulói és a stáb-jelzés az első, visszajelzés előtti próbálkozásból számol, a további próbálkozások gyakorlásra szolgálnak és nem írják felül” → „a tanulói és a stáb-jelzést az első, visszajelzés előtti próbálkozásból kell számolni; a további próbálkozások gyakorlásra szolgálnak, és a korai szükségletet nem írják felül”. A „korai szükségletet” a döntés szava, a javasolt „korai jelzést” helyett.
  - **MAN:92:** „a diagnosztikus jelzés az első, visszajelzés előtti próbálkozás, a stáb-jelzést” → „a diagnosztikus jelzéshez az első, visszajelzés előtti próbálkozás a mérvadó, a stáb-jelzést”.

### Összesítés
- 18 ID, ebből 9 MEGERŐSÍTVE: ERT-2, NYELV-13 (duplikátum), NYELV-9, ERT-5, IMPL-3, NYELV-12, NYELV-14, NYELV-8, NYELV-11.
- 9 RÉSZBEN: ERT-1, ERT-3, IMPL-1, NYELV-10, ERT-6, IMPL-2, IMPL-4, IMPL-5, IMPL-7.
- 0 ELVETVE.
- Emberi döntés: 1 teljes (ERT-2), 1 részleges (IMPL-7, a Z.3 5. dia besorolása). Bizonyíték-kapu: 0.
- Duplikátum: NYELV-13 → ERT-1.
- Vétólistára kerül (completion vagy kötelező-besorolás változik): ERT-1, IMPL-1, IMPL-2, IMPL-4.

A forrásfindingok itt vannak: (munkamenet-scratchpad)/impl/ (qa-canon-ert.md, qa-canon-ert-b.md, qa-canon-nyelv.md).

<!-- agent a04d7c4b02077609f -->

Adverzális második kör, B csoport (bdb94ab, AP-2026-10-12-01). Read-only maradtam, és mind a 16 ID kapott verdiktet. Minden helyet ma visszaolvastam a fájlban: HUM 14 :628–678 és :745, döntési csomag ADV-1 :451–458, javaslat ADV-1 :90, canon_blocks :460–521, manifest :14–25, ADV :45–268, PT :113/:250/:286/:309, GLO :185–194, GK :56–67, RA :97–102, M3.4 :67, M4 hub :108, M4.F :37.

**K-ADV1 eldöntése: a (b) eset áll, nem egyértelmű.**
- A HUM 14 ADV-1 (:647) szövege: „mentor csak saját csoportjának lássa a beadást”.
- A manifest :25 szerint a GATE-CP „Assignment beadási típus nélkül … a tanuló semmit nem tud beadni”, a H5P-C és a QUIZ pedig próbálkozás, nem beadás.
- Ezzel szemben a csomag kérdése (:452) a négy profilt nevezi meg, a (c) opció (:454) pedig általánosan szól: „a mentorokat csoport szerint szűkítik”.
- A két modulterv ellentétesen értelmezte a döntést: M1#1/#3 szűken, M2#3/#4/#5 tágan (canon_blocks :460–521).
- Adatvédelmi bizonytalanság, ezért emberi döntés. Az IMPL-6 ettől független: a BIZT-2 (szerkesztői, menedzseri, rendszergazdai hozzáférés) a döntés szövegéből egyértelműen következik.

---

CANON:QA-BIZT-1 | MEGERŐSÍTVE | emberi-döntés | P1
- **Indok:** ADV :109 szó szerint: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése továbbra is DPO-kérdés (BIZT-5).” A profiltábla :115/:116/:117 „nincs rögzítve (BIZT-5)”, a :232 „DPO-kérdés marad”. A hatókör a fenti okok miatt nem dönthető el a repóból. Az, hogy a kérdés DPO-kérdésként szerepel, pontatlan: a döntést a projektgazda hozta, a DPO vétó/QA. Megtartandó a klaszterben az IMPL-6 mellett; nem duplikátum.
- **Döntési igény:** a projektgazda döntse el, kiterjed-e az ADV-1 (c) a H5P-C, a QUIZ és a GATE-CP mentori nézetére. Utólagos ellenőrzés (vétó/QA): a DPO / jogi felelős. Bizonyíték: HUM :647, csomag :452 és :454, canon_blocks M1#1/#3 és M2#3/#4/#5.
- **Átmeneti szöveg, ADV :109:**
  - OLD: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése továbbra is DPO-kérdés (BIZT-5).”
  - NEW: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése nincs rögzítve: a döntés „beadást” mond, a döntési csomag ADV-1 kérdése viszont ezeket a profilokat is megnevezte; a döntés kiterjedéséről a projektgazda dönt, utólagos ellenőrzés (vétó/QA): a DPO / jogi felelős (BIZT-5).”
- **Következmény:** a :104 „a szűkítés DPO-kérdés: BIZT-5” és a :232 „DPO-kérdés marad” ugyanígy „nyitott: az ADV-1 kiterjedése (BIZT-5)” alakra vált.
- **Korlát:** a profiltábla „nincs rögzítve” cellái maradnak, és egyetlen sort sem szabad „eldöntött”-nek írni.

CANON:QA-IMPL-6 | MEGERŐSÍTVE | objektív | P2
- **Indok:** manifest :24 „(a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés elfogadhatósága DPO-kérdés: BIZT-2)”. A HUM :647 ezt szó szerint eldönti: „admin/editor jogosultság szűk, név szerint kiosztott, auditálható, de technikai admin teljes hozzáférését ne tagadja a tájékoztató”. Az ADV :109 és :232 már így szól. Független a BIZT-1-től.
- **Javítás:**
  - OLD: a fenti zárójeles rész.
  - NEW: „(a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférésről projektgazdai döntés rendelkezik: a jogosultság szűk, név szerint kiosztott és auditálható, a technikai adminisztrátor teljes hozzáférését a tájékoztató nem tagadja; 2026-10-12, ADV-1, BIZT-2; `Adatvédelem – tanulói adatok és AI.md` §3)”
- **Korlát:** a mentorszűkítési mondatok, a „ha ténylegesen szükséges” és a staging-visszaolvasás változatlan. A finding NEW-ja is használható, csak benne kétszer szerepel a „projektgazda”.

**K-AI (BIZT-2 és NYELV-5, egy összehangolt szerkesztés)**

CANON:QA-BIZT-2 | MEGERŐSÍTVE | objektív | P2
- **Indok:**
  - ADV :183 egy bekezdésen belül ellentmond magának: előbb „kezdetben az AI-segéd csak képző által közvetített … úton használható”, majd „ideiglenesen az AI-segéd kikapcsolva”. A GYV-10 (:633) alanya a tanulói szabad beszélgetéses AI-segéd, az LMS-8 (:745) a közvetített utat kifejezetten engedi.
  - RA :102 „amíg ez nem igazolt, közvetlen tanulói AI-hozzáférés nincs” – ez csak az ADV-12 naplózási feltétele.
  - PT :250 „addig nem nyílik, amíg nincs igazolt adatkezelési és kríziskezelési út”.
  - Mindkét helyről hiányzik az LMS-8 „krízis-, adatkezelési, jogosultsági és no-AI parity review” feltétele, holott mindkettő hivatkozik az LMS-8-ra. Ez a lezárt döntés részleges átvezetése, a szó szerinti pótlás objektív.
- **Javítás:**
  - ADV :183, első hely: OLD „ideiglenesen az AI-segéd kikapcsolva, a no-AI út teljes értékű” → NEW „ideiglenesen a tanulói AI-segéd ki van kapcsolva, a no-AI út teljes értékű”.
  - ADV :183, második hely: OLD „Az AI-végponton a tartalom naplózása alapból kikapcsolva, csak” → NEW „Az AI-végponton a tartalom naplózása alapból ki van kapcsolva, csak”.
  - RA :102: OLD „amíg ez nem igazolt, közvetlen tanulói AI-hozzáférés nincs” → NEW „amíg ez, valamint az LMS-8 szerinti krízis-, adatkezelési, jogosultsági és no-AI parity review nem igazolt, közvetlen tanulói AI-hozzáférés nincs”.
  - PT :250: OLD „közvetlen tanulói AI-segéd addig nem nyílik, amíg nincs igazolt adatkezelési és kríziskezelési út; a végponton a tartalom naplózása alapból kikapcsolva, és” → NEW „közvetlen tanulói AI-segéd addig nem nyílik, amíg nincs igazolt adatkezelési és kríziskezelési út, és csak krízis-, adatkezelési, jogosultsági és no-AI parity review után nyílhat; a végponton a tartalom naplózása alapból ki van kapcsolva, és”.
- **Korlát:** új feltétel, időtartam vagy szolgáltatói állítás nem kerül be.

CANON:QA-NYELV-5 | MEGERŐSÍTVE (a BIZT-2 összehangolt szerkesztésébe olvad; nem duplikátum) | objektív | P2
- **Indok:** PT :250 „naplózása alapból kikapcsolva, és a `store=false` önmagában nem bizonyít”: ige nélküli tag véges igés taggal mellérendelve. Az ADV :183 „kikapcsolva, csak … marad” ugyanilyen. Az RA :102 már „ki van kapcsolva”.
- **Javítás:** a BIZT-2 sorában megadott „ki van kapcsolva” cserék, mindkét fájlban.

**K-§11 (BIZT-3 és NYELV-4)**

CANON:QA-BIZT-3 | RÉSZBEN | (a) objektív / (b) emberi-döntés | P2
- **(a) indok:** a :232 szerint „A „Ki látja?” rész a §5 lezárt szabályát közli”. A §5 :148 tartalmazza: „az F-peula képzője a kapueredményekből csak összesített vagy minimális hiánylistát lát”. A :247 ADV-2-es mondatából ez kimaradt.
- **(a) javítás:** a :247 „…, a Memuna pedig szükség esetén.” mondata után új mondat: „Az F-peula képzője a kapueredményekből csak összesített vagy minimális hiánylistát lát.” A szöveg szó szerint a §5-ből jön; a finding „javításhoz szükséges” indoklását ne vegyük át.
- **(b) indok:** a :264 AI-mondata ugyanaz, mint a §7 :194 kanonikus, HUM-PRIV-04-es tanulói szövege. A mostani mondat nem hamis. Hogy a közvetített út a tanuló felé hogyan működik, abból nem vezethető le: a képző vagy a szervezeti backend küldi a promptot (:180).
- **(b) döntési igény:** kell-e és milyen szöveggel kerüljön a tájékoztatóba a közvetített út, összhangban a §7 :194-gyel és az M7 tanulói szövegeivel. Kitől: programvezető és Moodle-adminisztrátor (LMS-8), vétó/QA: DPO / jogi felelős. Addig a :264 változatlan.

CANON:QA-NYELV-4 | ELVETVE | — | —
- **Indok:** a :247 „Egy kapubeadványt … csak konkrét eljárásnál – például ha újraértékelést kérsz – lát, a Memuna pedig szükség esetén.” mondat nyelvtanilag helyes; a fókusz és az ige közé ékelt betét szabályos. A határozatlan tárgy ízlés kérdése. A Memunára vonatkozó „csak” az ADV-2 döntés szövegében (:648) sincs meg; az M3.4 :67-ből átvenni szűkítés volna, nem javítás.

**K-ERT8 (ERT-4, NYELV-6, NYELV-7)**

A gyökérok közös: az ERT-8 (:678) szerint puha kapunál a gyenge munka nem bukás, tehát a kapu nem „nem teljesült”. Egy „is” beszúrásával összehangolva:

CANON:QA-ERT-4 | MEGERŐSÍTVE | objektív | P2
- **Indok:** PT :309 „facilitált, strukturált javítási alkalom annak, akinek a modul kapuja nem teljesült** … **puha kapunál (M2, M4) ajánlott** (projektgazdai döntés, 2026-10-02)”. Itt nincs ERT-8; a PT :286 közben ki is mondja.
- **Javítás:** OLD „ajánlott** (projektgazdai döntés, 2026-10-02).” → NEW „ajánlott** (projektgazdai döntés, 2026-10-02); puha kapunál a küszöb alatti, de értelmezhető beadás is kiváltja, és ez nem bukás (HUM 14. szakasz, ERT-8).”

CANON:QA-NYELV-6 | MEGERŐSÍTVE | objektív | P2
- **Indok:** GLO :188 „a gyenge, de értelmezhető munka (…) váltja ki, nem „nem teljesült” bukás”. A ragtalan alak a kiváltóval állítható szembe („nem a bukás váltja ki”). Az ERT-8 viszont azt mondja, hogy a kimenet nem bukás.
- **Javítás:** OLD „váltja ki, nem „nem teljesült” bukás;” → NEW „is kiváltja, és ez nem „nem teljesült” bukás;”

CANON:QA-NYELV-7 | RÉSZBEN | objektív | P2
- **Indok:** a probléma valós. GLO :194 „ha egy kapu nem teljesült (M1.F–M7.F)”, PT :286 „Ha a kapu nem teljesült: **F-peula** – … puha kapunál a küszöb alatti, de értelmezhető beadás váltja ki”. A keret kizárja azt az esetet, amit maga a mondat leír.
- **Ami nem áll:** a „szó szerinti modulmásolatok” rész téves.
  - Az M3 hub :224 éles kapura szól („Kötelező … M3 éles kapuja nem teljesült”).
  - Az M4 hub :108 és az M4.F :37 már ERT-8-konform („még nem éri el … küszöböt; … formatív javaslat, nem bukás”).
  - Ezekhez nem kell nyúlni.
- **Javítás:**
  - GLO :194: OLD „puha kapunál a küszöb alatti, de értelmezhető munka váltja ki, és ez nem bukás” → NEW „puha kapunál a küszöb alatti, de értelmezhető munka is kiváltja, és ez nem bukás”.
  - PT :286: OLD „puha kapunál a küszöb alatti, de értelmezhető beadás váltja ki, és ez nem bukás” → NEW „puha kapunál a küszöb alatti, de értelmezhető beadás is kiváltja, és ez nem bukás”.
  - A finding első mondatos átírása helyett ez a minimális változat; a keretmondatok maradnak.
- **Következmény-ellenőrzés:** a fő session nézze meg a `LMS – hozzáférhetőségi sztenderd.md` :56 „F-peula csak nem teljesült kapu után jár” mondatát.

**Önálló tételek**

CANON:QA-BIZT-4 | MEGERŐSÍTVE | emberi-döntés | P2 (alacsony bizalom)
- **Indok:** ADV :153 egy pontban: „az kikerül a Moodle-ből, és az incidensfolyamatba kerül (§3)” (HUM-PRIV-01), utána „bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan … adatvédelmileg jóváhagyott törlést vagy megőrzést” (GYV-11, :634). A sorrend és a hatáskör nincs rögzítve. Két lezárt gyermekvédelmi-adatvédelmi döntés összeillesztése; a kétes eset emberi döntés.
- **Döntési igény:** a Memuna és a DPO döntse el, hogy a „kikerül a Moodle-ből” a GYV-11 szerinti jóváhagyott korlátozást vagy törlést jelenti-e, az incidensnyilvántartásba mentés után. Addig nincs szövegváltozás és nincs sorrendi szabály.

CANON:QA-BIZT-5 | MEGERŐSÍTVE | emberi-döntés | P2
- **Indok:** ADV :58 „A jogalap és a megőrzés kanonikus helye ez a tábla”. A :183 „rövid, dokumentált megőrzéssel” (ADV-12, :658). A :60–73 táblában nincs AI-végpont-metaadat sor. A megőrzési idő és az adatkör DPO-döntés.
- **Döntési igény:** a DPO / jogi felelős (QA: programvezető) rögzítse az AI-végpont technikai metaadatainak jogalapját és megőrzési idejét a §3 táblában.
- **Korlát:** addig legfeljebb egy „nyitott: DPO (ADV-12)” sor kerülhet be, időtartam nélkül, ahogy a :90 BS-D6 mintája mutatja.

CANON:QA-BIZT-6 | MEGERŐSÍTVE | objektív | P2
- **Indok:** PT :113 „rövid reflektív írás vagy videó + „következő lépés””, PT :213 „reflektív írás/videó + „következő lépés””. A PT :211 már átvezette: „ha a videós út be van kapcsolva – videó; alapból kikapcsolva, ADV-14”. A HUM :660 alapján ez a fájlon belüli átvezetés hiányos.
- **Javítás:**
  - PT :113: OLD „rövid reflektív írás vagy videó” → NEW „rövid reflektív írás (videó csak bekapcsolt videós úttal; alapból kikapcsolva, ADV-14)”.
  - PT :213: OLD „reflektív írás/videó” → NEW „reflektív írás (videó csak bekapcsolt videós úttal, ADV-14)”.
  - A „+ „következő lépés”” és minden más változatlan.

CANON:QA-NYELV-1 | MEGERŐSÍTVE | objektív | P2 (az átvezetés regressziója)
- **Indok:** ADV :83 „csak a Peula v2 csoportszintű kvuca-adata:”. Az ADV-9 (:655) szövege: „A Peula v2 minimális csoportszintű kvuca-adatszabályát alkalmazzuk az M4/M5/M6 produktumokra”. Kiesett az alaptag és a minősítő, és a mondat időrendi képtelenséget állít (M4 az M7 előtt).
- **Javítás:** OLD „csak a Peula v2 csoportszintű kvuca-adata:” → NEW „csak a Peula v2 minimális, csoportszintű kvuca-adatszabálya szerinti adat:”. Az adatkör változatlan.

CANON:QA-NYELV-2 | MEGERŐSÍTVE | objektív | P2 (baseline: kontextussor, nem a bdb94ab regressziója)
- **Indok:** ADV :82 „M3 gyermekvédelmi helyzetelemzés:”. A grep szerint ez az egyetlen „helyzetelemzés” a `02 Tervezet` `.md`-fájljaiban. A TERM-5 (:667) „következetesen „M3 – Helyzetleírás””, a PT :108 is „helyzetleírás”.
- **Javítás:** OLD „M3 gyermekvédelmi helyzetelemzés:” → NEW „M3 gyermekvédelmi helyzetleírás:”. A sor szabálya változatlan.

CANON:QA-NYELV-3 | MEGERŐSÍTVE | objektív | P2
- **Indok:** ADV :53 „az alap a Moodle és a papír, nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladattal, és a szolgáltató, …”. Felsorolásnak olvasható, a „teljesíthető” alanya pedig hiányzik. Az ADV-10 (:656) szövege: „nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladat”.
- **Javítás:** OLD „használható; az alap a Moodle és a papír, nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladattal, és a szolgáltató,” → NEW „használható; az alap a Moodle és a papír; nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladat legyen; a szolgáltató,”. Ez közelebb áll a döntés szövegéhez, mint a finding „van egyenértékű, teljesíthető” változata. A pont többi része változatlan.

CANON:QA-NYELV-15 | MEGERŐSÍTVE | objektív | P2 (alacsony)
- **Indok:** GK :65 „peulán előzetesen legalább két … felelős van, vagy …”, a GYV-5 (:628) szövege viszont „előzetesen legyen”. A GK §4 lista módja vegyes: a :60 kijelentő normát használ („jelen van”), a :64 felszólítót („legyen kijelölt biztonságos hely”). A normagyengülés vádja ezért túlzó. Az „előzetesen” határozó mellé azonban felszólító állítmány illik, és a döntés szó szerinti alakja biztonságos.
- **Javítás:** OLD „peulán előzetesen legalább két rendelkezésre álló, felkészített, 18 év feletti felelős van, vagy azonnal elérhető helyettes és kötelező megállítási protokoll” → NEW „peulán előzetesen legyen legalább két rendelkezésre álló, felkészített, 18 év feletti felelős, vagy azonnal elérhető helyettes és kötelező megállítási protokoll”. A létszám, a „18 év feletti” és a pont többi része változatlan.

---

**Összesítő:** 16 ID.
- MEGERŐSÍTVE 13 (ebből emberi-döntés 3: BIZT-1, BIZT-4, BIZT-5).
- RÉSZBEN 2: BIZT-3 (a: objektív, b: emberi-döntés) és NYELV-7 (a modulmásolatos rész téves).
- ELVETVE 1: NYELV-4.
- Bizonyíték-kapu: 0.
- Duplikátum nincs. Összehangolt szerkesztés: a NYELV-5 a BIZT-2-vel együtt, egy OLD → NEW-ban; az ERT-4, a NYELV-6 és a NYELV-7 együtt az „is kiváltja” mintával. A BIZT-1 és az IMPL-6 külön tétel.
- K-ADV1: (b), emberi döntés a projektgazdától, DPO-vétóval. Addig a :109 a fenti átmeneti szöveggel áll.

**Releváns fájlok:**
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Program terv.md
- 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md

## C. Nyers lencse-kimenetek (szó szerint)

<!-- agent a6c6a9d96e8e72153 -->

Célzott QA, biztonság-jog lencse, kánoni kör (bdb94ab, AP-2026-10-12-01). Read-only maradtam. Átnéztem a diff-hunkokat, a HUM 14. szakasz érintett sorait, a döntési csomag és a javaslat ADV-1 szakaszát, valamint a canon_blocks.txt ADV-1/GYV-11 blokkjait. Hat findingot találtam, P0 nincs köztük.

**A szándékos döntésekről röviden:**
- **ADV-1:** szerintem nem egyértelműen hű átvezetés, ez a CANON:QA-BIZT-1.
- **GYV-5:** a „18 év feletti felelős” alakot elfogadom. A HUM-SAFE-03 szó szerint így fogalmaz (HUM :72), és a GK §4:60 is.
- **GYV-11:** az, hogy csak a tárolt beadandóra szól, hű átvezetés. Egy belső feszültséget viszont lásd a CANON:QA-BIZT-4-ben.
- **Az ERT-38 kihagyása:** biztonság-jogi szempontból nem érint.
- **Hű és teljes átvezetésnek látom:** GYV-21, ADV-2 (§5), ADV-6, ADV-7 (a „fotózás alapból nincs” elemet a §6 HUM-PRIV-02 mondata már tartalmazza), ADV-9, ADV-10, ADV-11, ADV-14, ADV-15, ERT-12. Az LMS-M1-07 idézete szó szerint egyezik az M1.3 :885 szövegével.

---

**ID:** CANON:QA-BIZT-1
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:104`, `:109`, `:115–117`, `:232`
- **Probléma:** Az ADV-1 csoportszűkítése csak az ASSIGN-S/M beadásokra került át. A H5P-C, a QUIZ és a GATE-CP szűkítése „DPO-kérdés (BIZT-5)” néven nyitva maradt, pedig a döntés a csomag (c) opcióját választotta. A csomag kérdése kifejezetten ezt a négy profilt nevezte meg.
- **Bizonyíték:**
  - Kánon :109: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése továbbra is DPO-kérdés (BIZT-5).”
  - Döntési csomag, ADV-1: „Szűkíteni kell-e csoport szerint a mentor hozzáférését a nem TEXT-C profilokon (ASSIGN-S/M, GATE-CP, H5P-C, QUIZ; BIZT-5)? … (c) Vegyes megoldás: a mentorokat csoport szerint szűkítik”.
  - HUM 14, ADV-1: „Vegyes (c) hozzáférési modell: mentor csak saját csoportjának lássa a beadást”.
- **Hatás:** A P2 szabad szöveget rögzítő H5P-C próbálkozásokat és a kvízpróbálkozásokat a mentor a Moodle-alapértelmezés szerint más csoportoknál is látja. Ez a kevésbé védő állapot. A kánon közben egy már eldöntött kérdést nyitottként tart nyilván. A két modulterv is ellentétesen értelmezte a döntést: az M1#1/#3 szűken, az M2#3/#4/#5 a H5P-C, QUIZ és GATE-CP sorra is kiterjesztve.
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. A „beadás” szó a döntés szövegében a hatókört szűkíti, a (c) opcióra hivatkozás tágítja.
- **Javaslat:** EMBERI DÖNTÉS. A projektgazdának kell eldöntenie, DPO-vétóval, hogy az ADV-1 „(c)” kiterjed-e a H5P-C, QUIZ és GATE-CP mentori nézetére. Bizonyíték hozzá: a döntési csomag ADV-1 kérdése és (c) opciója, valamint a két modulterv eltérő blokkja.
  - Szerintem a (c) opcióra hivatkozás és az F-döntés óvatos alapértelmezése a tág olvasatot támogatja.
  - Addig a :109 mondata ne „DPO-kérdés”-ként rögzítse a tételt, hanem nyitott döntés-értelmezésként, hivatkozva erre a findingra.
  - Tilos addig a profiltábla bármely sorát „eldöntött”-nek írni.
- **Típus:** emberi-döntés · **Verdikt:**

---

**ID:** CANON:QA-BIZT-2
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:183`
  - `02 Tervezet/LMS – H5P runtime acceptance.md:102`
  - `02 Tervezet/Program terv.md:250`
- **Probléma:** Az AI-hozzáférés feltételei a három kánoni helyen nem egyformán szerepelnek.
  - Az ADV §7 mondatai ellentmondhatnak egymásnak: „képző által közvetített úton használható”, utána „ideiglenesen az AI-segéd kikapcsolva”.
  - A runtime acceptance 20. pontja csak a naplózási feltételt nevezi meg a közvetlen tanulói hozzáférés feltételeként. A GYV-10 kríziskezelési útja és az LMS-8 jogosultsági és no-AI parity review-ja kimarad.
  - A Program terv a jogosultsági és a no-AI parity review-t hagyja ki.
- **Bizonyíték:**
  - ADV :183: „ideiglenesen az AI-segéd kikapcsolva, a no-AI út teljes értékű”.
  - RA :102: „amíg ez nem igazolt, közvetlen tanulói AI-hozzáférés nincs, csak a képző által közvetített út”.
  - HUM, LMS-8: „Közvetlen tanulói chatbot/plugin csak krízis-, adatkezelési, jogosultsági és no-AI parity review után.”
- **Hatás:** A build kikapcsolhatja a képző által közvetített utat is. A runtime acceptance-ből pedig az olvasható ki, hogy egy sikeres naplózási teszt után megnyitható a közvetlen tanulói AI, krízis-review nélkül.
- **Állítás-osztály:** PROJEKT-DÖNTÉS (GYV-10, LMS-8, ADV-12)
- **Javaslat:** A javítás a döntések szövegének átvezetése, új feltétel nem kerül be.
  - ADV :183: „ideiglenesen az AI-segéd kikapcsolva” → „ideiglenesen a tanulói AI-segéd kikapcsolva”.
  - RA :102: „amíg ez nem igazolt, közvetlen tanulói AI-hozzáférés nincs” → „amíg ez, valamint az LMS-8 szerinti krízis-, adatkezelési, jogosultsági és no-AI parity review nem igazolt, közvetlen tanulói AI-hozzáférés nincs”.
  - Program terv :250: a „közvetlen tanulói AI-segéd addig nem nyílik” mondatba ugyanez a felsorolás kerüljön.
- **Típus:** objektív · **Verdikt:**

---

**ID:** CANON:QA-BIZT-3
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:247` és `:264` (a §11 tanulói tájékoztató)
- **Probléma:** A diff a „Ki látja?” részt az ADV-2-vel bővítette, a tájékoztató két mondata mégsem követi a 14. szakaszt.
  - (a) Nem szerepel benne, hogy az F-peula képzője minimális hiánylistát lát. Ez címzett, az ADV-2 szerint.
  - (b) Az „AI-segéd” bekezdés közvetlen tanulói használatot sugall. A GYV-10/LMS-8 szerint kezdetben csak a képző közvetít, így a prompt tartalma a képzőhöz is eljut.
- **Bizonyíték:**
  - :264: „a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.”
  - ADV :152: „az F-peula képzője a kapueredményekből csak összesített vagy minimális hiánylistát lát”.
- **Hatás:** A tanulói tájékoztató nem mondja meg pontosan, kik a címzettek és milyen az adatút. Ez átláthatósági hiány kiskorú résztvevők felé.
- **Állítás-osztály:** PROJEKT-DÖNTÉS (ADV-2, GYV-10, LMS-8). A tájékoztató végleges szövege és élesítése DPO-kapu, a §11 :232 szerint.
- **Javaslat:** A tanulói szöveg minimális, a döntésből levezetett kiegészítése:
  - a „Ki látja?” részbe egy félmondat: az F-peulád képzője csak a javításhoz szükséges hiánylistát látja;
  - az AI-bekezdésbe egy mondat: kezdetben az AI-segédet csak a képződ közvetítésével használhatod.

  Ha a tájékoztatóra freeze vonatkozik, a freeze-kivételről a projektgazda dönt (HUM 14, ADV-6 vétó-oszlop). Új adatkezelési ígéret nem kerülhet be.
- **Típus:** objektív · **Verdikt:**

---

**ID:** CANON:QA-BIZT-4
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:153` (§5, „gyermekvédelmi feltárás”); vö. `:75` és `:243`
- **Probléma:** Ugyanabban a pontban áll két szabály, és a viszonyuk nincs tisztázva:
  - a régi, feltétel nélküli mondat: a különleges adat „kikerül a Moodle-ből”;
  - a GYV-11 mondata: bizonyítékot nem törlünk automatikusan, a törlés vagy megőrzés adatvédelmileg jóváhagyott és dokumentált.
- **Bizonyíték:** „az kikerül a Moodle-ből, és az incidensfolyamatba kerül (§3). … bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan”
- **Hatás:** Az LMS-gazda a Moodle-példányt azonnal törölheti, mielőtt megvolna a Memuna-eljárás és a jogi megőrzési felülvizsgálat. Az ellenkezője is lehet: a „kikerül” nem teljesül, mert senki nem tudja, ki dönt róla.
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. Két lezárt döntés (HUM-PRIV-01 és GYV-11) összeillesztéséről van szó, sorrendről és hatáskörről.
- **Javaslat:** EMBERI DÖNTÉS. A Memunának és a DPO-nak kell eldöntenie, hogy a „kikerül a Moodle-ből” a GYV-11 szerinti, adatvédelmileg jóváhagyott törlést vagy korlátozást jelenti-e, amely az incidensnyilvántartásba mentés után következik. Bizonyíték: a :75/:153 és a HUM 14 GYV-11 sora. Addig ne írjunk be sorrendi szabályt.
- **Típus:** emberi-döntés · **Verdikt:**

---

**ID:** CANON:QA-BIZT-5
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:183` és a §3 jogalap- és megőrzési mátrix (`:60–73`)
- **Probléma:** Az ADV-12 átvezetése „rövid, dokumentált megőrzést” ír elő az AI-végpont technikai metaadataira. A §3 ugyanakkor kimondja magáról, hogy ez a megőrzés kanonikus helye, és nincs benne ilyen sor. A képző által közvetített út ma is ezen a végponton fut.
- **Bizonyíték:**
  - :58: „A jogalap és a megőrzés kanonikus helye ez a tábla”.
  - :183: „csak a feltétlenül szükséges technikai metaadat marad, rövid, dokumentált megőrzéssel”.
- **Hatás:** A közvetített AI-út metaadatainak jogalapja és megőrzési ideje dokumentálatlan, ezért a „dokumentált” feltétel nem teljesül.
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL (DPO: adatkör és megőrzés)
- **Javaslat:** EMBERI DÖNTÉS. A DPO-nak (QA: programvezető) kell rögzítenie az AI-végpont technikai metaadatainak jogalapját és megőrzési idejét a §3 mátrixban. Bizonyíték: az ADV-12 szövege és a csatornafelmérés eredménye. Addig a sor „nyitott: DPO” jelöléssel kerülhet be. Időtartamot nem szabad kitalálni.
- **Típus:** emberi-döntés · **Verdikt:**

---

**ID:** CANON:QA-BIZT-6
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Program terv.md:113` (modultábla, Z sor) és `:213` (Z, „Produktum & kapu”)
- **Probléma:** Az ADV-14 csak a Z „Online” sorába került át (:211). Ugyanebben a fájlban két mondat továbbra is feltétel nélküli, egyenrangú opcióként írja le a videót.
- **Bizonyíték:**
  - :113: „rövid reflektív írás vagy videó + „következő lépés””.
  - :213: „reflektív írás/videó + „következő lépés” + képzési visszajelző űrlap”.
  - Az ADV-14 szerint: „A Z.4 videóopció legyen alapból kikapcsolva”.
- **Hatás:** A program-architektúra egymásnak ellentmondó jelet ad a buildnek és a képzőknek a kiskorúak videós adatkezeléséről.
- **Állítás-osztály:** PROJEKT-DÖNTÉS (ADV-14, LMS-1)
- **Javaslat:**
  - :113: „rövid reflektív írás vagy videó” → „rövid reflektív írás (videó csak bekapcsolt videós úttal; alapból kikapcsolva, ADV-14)”.
  - :213: „reflektív írás/videó” → „reflektív írás (videó csak bekapcsolt videós úttal, ADV-14)”.

  Más nem változik.
- **Típus:** objektív · **Verdikt:**

---

Releváns fájlok:
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Program terv.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md (14. szakasz)
- 01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md (ADV-1, :451–458)
- (munkamenet-scratchpad)/impl/canon_blocks.txt (:460–521, az ADV-1 eltérő értelmezései)

<!-- agent a280133b2e4c238e0 -->

## Célzott QA: kánoni kör (bdb94ab), értékelés és megvalósíthatóság

Csak a diffet néztem, és az ahhoz közvetlenül kapcsolódó sorokat. Az LMS-Z-08 ERT-38-mondatát nem jelentem hiányként. Tíz findingot adok le; a cap miatt három P2 kimaradt, ezeket a lista végén jelzem.

---

**CANON:QA-ERT-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – activity manifest.md:20` (ASSIGN-M profil); ugyanott :158, :163, :164 (a §4 M1-, M6- és M7-sora); `LMS – H5P runtime acceptance.md:33–36` (1. pont)
- **Probléma:** Az ERT-9-et csak a §2 soraiba vezették át (LMS-M1-05, M5-05, M6-05, M7-06). Az ASSIGN-M profil alapértelmezett completionje és a §4 M1-, M6- és M7-sorának „mastery” eleme a régi, összevont modellt írja. Az RA-ban nincs pont, amely visszaolvasná, hogy az ASSIGN-M completionje `completionsubmit`, jegyalapú completion nélkül.
- **Bizonyíték:** profil: „beadvány leadva **és** megerősített kapueredmény (a kapufájl teljes feltétele, nem a nyers pont; …)”; §4: „| M1 | H5P-k + LMS-M1-05 mastery |”. Ezzel szemben az ERT-9: „ASSIGN-M saját completion = SUBMITTED”.
- **Hatás:** Aki a profilból épít, az Assignmenten jegyalapú completiont állít be. Az ERT-9 pontosan ezt zárja ki: „nem helyettesíti a kritikus rubrikasorok … összetett feltételeit”. Az M5-sor már az új mintát követi, a többi nem.
- **Javaslat:**
  - A profilcellában: OLD „beadvány leadva **és** megerősített kapueredmény (…)” → NEW „SUBMITTED: a beadvány leadva (`completionsubmit`, jegyalapú completion kikapcsolva); CONFIRMED: a modul GATE-CP sora (LMS-M1-06, LMS-M5-08, LMS-M6-07, LMS-M7-08); egy »Receive a passing grade« az Assignmenten nem helyettesíti a kapufeltételt (ERT-9)”. Az M3-tagmondatot lásd a QA-ERT-2-nél.
  - A §4-ben az M5-sor mintájára: „LMS-M1-05 leadva + LMS-M1-06 »Teljesítve«”; ugyanígy az M6-ban (M6-05/M6-07) és az M7-ben (M7-06/M7-08).
  - Az RA 1. pontjába egy visszaolvasási sor az ASSIGN-M completion-beállításáról.
  - Küszöbhöz nem nyúlunk. Completion-szöveg változik, ezért vétólista.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-ERT-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** `LMS – activity manifest.md:66` (LMS-M3-05), :67 (LMS-M3-06), :20 (az ASSIGN-M profil M3-tagmondata)
- **Probléma:** Az ERT-9 általános („ASSIGN-M saját completion = SUBMITTED”), az M3 Assignmentje mégis a régi modellen maradt, és ezt semmi nem jelzi. A sima átírás viszont eltörné a kapuablakot: a kapukvíz nyitása az Assignment-komponens megerősített rubrikájához kötődik, ehhez pedig nincs külön GATE-CP.
- **Bizonyíték:** LMS-M3-05: „leadva + megerősített rubrika”; LMS-M3-06 unlock: „az LMS-M3-05 megerősített rubrikája (§7: az M3 kapuablaka)”.
- **Hatás:** Ha az ERT-9-et itt is alkalmazzák, a kapukvíz már a leadáskor megnyílik, a rubrika megerősítése előtt (az M3 KAPU szerint az ablak: „a rubrika megerősítése kedd 18:00-ig; a kapukvíz ezután nyílik”). Ha nem alkalmazzák, a kánon ellentmond a lezárt döntésnek.
- **Javaslat:** EMBERI DÖNTÉS (a build-spec gazda, azaz a projektgazda; QA: az értékelési felelős): hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy az LMS-M3-06 csak a megerősített rubrika után nyíljon. Két lehetőség: külön GATE-CP az Assignment-komponensre, vagy kifejezett M3-kivétel. Addig az LMS-M3-05 sorához és a profil M3-tagmondatához nem nyúlunk.
- **Típus:** emberi-döntés
- **Verdikt:** —

**CANON:QA-IMPL-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `LMS – activity manifest.md:38`-tól (LMS-M0-05, „Kötelező” oszlop), :167 (az online félév teljesítése)
- **Probléma:** Az ADV-6 miatt a sor azt mondja, hogy a fórum zárva marad, és „addig nem completion-feltétel”. A „Kötelező” cella viszont „igen” maradt. A kurzusteljesítés szabálya ráadásul minden „Kötelező = igen” sort activity-kritériumnak vesz.
- **Bizonyíték:** :167: „activity-kritérium minden »Kötelező = igen« §2-sor”; LMS-M0-05: „| FORUM-C | igen | … addig nem completion-feltétel”.
- **Hatás:** Ha a :167 szerint építenek, egy valódi tanulóknak zárt fórum kurzusteljesítési kritérium lesz. Így senki nem teljesítheti a kurzust (blokkoló sorrendi hiba), és ugyanez fenyegeti az „M0 complete” → M1 nyitást is.
- **Javaslat:**
  - A :167-be kivétel: „az LMS-M0-05 csak akkor, ha a fórum az ADV-6 feltételeivel valódi tanulóknak megnyílt”.
  - A „Kötelező” cellában: „igen (csak megnyitás után; ADV-6)”.
  - Ez a kötelező/opcionális besorolás feltételessé tétele; az ADV-6 és a sor saját szövege közvetlenül következik belőle. Vétólista.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-IMPL-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `LMS – activity manifest.md:96` (LMS-M7-02); `Modulok/M7/Online leckék/M7.2 – …md:9`, :88
- **Probléma:** Az ERT-48 átvezetése egy külön Moodle-oldal (Page) activityt ír elő saját completionnel, a CP előtt. Ennek nincs §2-sora: nincs build_id, unlock, „Kötelező” érték, és nem kurzusteljesítési kritérium.
- **Bizonyíték:** manifest: „AI-jártassági blokk: Moodle-oldal (Page), … a megtekintést az oldal completionje jelöli (ERT-48)”; M7.2 :88: „(Page) a Moodle-intro után, a H5P Course Presentation előtt”.
- **Hatás:** A kötelező AI-jártassági tartalom megtekintését jelző completion nem kerül be sem a modul-, sem a kurzusteljesítésbe. Az M7 a blokk megnyitása nélkül is teljesíthető.
- **Javaslat:**
  - Új §2-sor: PAGE-C, „Kötelező: igen”, unlock: LMS-M7-10, completion: megtekintés.
  - Az LMS-M7-02 unlockja erre a sorra kötődjön.
  - Másik út: ha a build-spec gazda az ERT-48 által megengedett CP-be ágyazott változatot választja, az LMS-M7-02-t és az M7.2-t kell egységesen arra átírni.
  - Új completion-elem kerül be, ezért vétólista.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-ERT-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** `Program terv.md:263`, :257; `LMS – activity manifest.md:175`, :164 („LMS-M7-07 mastery”)
- **Probléma:** Az ERT-40 darabszám-alapú küszöbe nem jutott el mindenhová. A Program terv §5 általános elve az M7-küszöböt a ≥80%-os százalékszabály alá sorolja, és két további hely sem mondja ki, hogy csak a teljesen helyes item számít.
- **Bizonyíték:** PT :263: „Quiz: általában **≥80%** (… az M7 14 itemes kapujánál **≥12/14**).”; manifest :175: „A kvíz összetett feltétele (≥12/14 ÉS a Q13 helyes)”.
- **Hatás:** Az ERT-40 kifejezetten tiltja az „átszámított részpontszázalékot” és a puszta „Grade to pass 12”-t. A régi megfogalmazás pontosan ezt a beállítást sugallja.
- **Javaslat:**
  - PT :263: „… (a 12 itemes kvízeknél ez ≥10/12); az M7 14 itemes kapujánál darabszám-alapú: ≥12/14 teljesen helyes item (ERT-40)”.
  - PT :257 és manifest :175: „≥12/14 teljesen helyes item ÉS …”.
  - §4 M7-sor: „LMS-M7-07 mastery” → „LMS-M7-09 = »Teljesítve«”.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-ERT-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `Program terv.md:309` (§6, az F-peula meghatározása)
- **Probléma:** Az ERT-8 kivételét a Glosszáriumba és a Program terv §4–§5-be beírták, az F-peula §6-beli meghatározásába viszont nem. Itt a célcsoport továbbra is csak az, „akinek a modul kapuja nem teljesült”.
- **Bizonyíték:** „strukturált javítási alkalom annak, akinek a modul kapuja nem teljesült** – … **puha kapunál (M2, M4) ajánlott**”.
- **Hatás:** A puha kapunál küszöb alatti, de értelmezhető munka az ERT-8 szerint „nem bukás”, mégis F-peula-ajánlást vált ki. A §6 meghatározása ezt a csoportot kizárja, így a Program terv két szakasza ellentmond egymásnak.
- **Javaslat:** Az „ajánlott** (projektgazdai döntés, 2026-10-02)” után: „; puha kapunál a küszöb alatti, de értelmezhető beadás is kiváltja, és ez nem bukás (HUM 14. szakasz, ERT-8)”.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-ERT-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `LMS – H5P runtime acceptance.md:57` (8. pont, M7)
- **Probléma:** A „11 teljes + 2 részpontos” negatív eset nem rögzíti, hogy a részpontok összege legalább 1 legyen. Ha a nyers pont 12 alatt marad, a „Grade to pass = 12” amúgy is blokkol, és a teszt ki sem próbálja azt a kockázatot, amely miatt az ERT-40 előírta.
- **Bizonyíték:** „11 teljesen helyes + 2 részpontos Multi-Select item, amely a »Grade to pass = 12« mellett sem teljesülhet: ERT-40”.
- **Hatás:** A teszt látszólag átmegy, miközben a valós hibamódot (a részpontokkal 12-re felkerekedő nyers összpontot) nem igazolja.
- **Javaslat:** NEW: „… 2 részpontos Multi-Select item, a részpontok összege legalább 1 (nyers pont ≥12, azaz a »Grade to pass = 12« teljesülne), a kapu mégsem teljesülhet: ERT-40”.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-IMPL-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `LMS – activity manifest.md:16` (H5P-C profil), :39 (LMS-M0-01); `LMS – H5P runtime acceptance.md:72` (9. pont)
- **Probléma:** Az ERT-1 és ERT-2 átvezetése két ponton hiányos.
  - A tartalékút („ha nincs összefoglaló dia, a completion-alapot a build-spec gazda rögzíti”) csak az LMS-Z-02 és Z-03 sorában áll. A profilban nincs, így az LMS-M0-01-re sem vonatkozik, pedig az ERT-2 éppen az M0.1-et nevezi meg.
  - Az RA 9. pont „negatív esete” nem mondja meg a várt eredményt.
- **Bizonyíték:** profil: „erre épülő completiont csak olyan CP kap, amelynek ténylegesen van összefoglaló diája (feladatelem nélkül nincs)”; RA: „rögzíteni kell … hogy ilyenkor keletkezik-e grade, és beáll-e a completion.”
- **Hatás:** Ha egy pontozatlan választós CP-nek nincs összefoglaló diája, vagy megválaszolatlan elemekkel nem áll be a completion, annak nincs definiált completion-alapja. Ez az M0.1 esetében az egész kurzust blokkolja. A 9. pont pass/fail feltétel nélkül nem dönt.
- **Javaslat:**
  - A Z-02-sor tartalékút-mondata kerüljön szó szerint a H5P-C profil ERT-1-mondata után.
  - Az RA 9-be: „Várt eredmény (ERT-1): a completion beáll; ha nem, a pontozatlan választós sorok (LMS-M0-01, LMS-Z-02, LMS-Z-03) completion-alapját a build-spec gazda rögzíti, és a választó nem válhat completion-elemmé (ERT-2).”
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-IMPL-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `LMS – activity manifest.md:85` (LMS-M5-07, Completion oszlop)
- **Probléma:** A Profil oszlop már „H5P-C vagy PAGE-C”, és a felidézés az LMS-3 szerint a tanuló saját jegyzetében történik, beviteli elem nélkül. A Completion cella mégis követett interakciót ír elő. Ilyen interakció ezen az úton nincs, a PAGE-C profil pedig megtekintést ad.
- **Bizonyíték:** Completion: „a forrás szerinti felidézési interakció elvégzése”; PAGE-C profil (:23): „megtekintés, csak ha valóban információátadás a cél”.
- **Hatás:** A cella nem valósítható meg. A builder vagy hamis „Receive a grade”-et állít egy üres CP-re (az LMS-3 ezt tiltja), vagy a cellától eltérő megtekintéses completiont.
- **Javaslat:** OLD „a forrás szerinti felidézési interakció elvégzése” → NEW „a választott profil szerint: H5P-C-nél »Receive a grade« csak jóváhagyott, pontozott önellenőrző itemmel (üres CP-re nem), PAGE-C-nél megtekintés; a véglegeset a valós H5P és ennek a sornak a tesztje dönti el (LMS-3; runtime acceptance 4. pont)”. Completion-szöveg változik, ezért vétólista.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-IMPL-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `LMS – activity manifest.md:135` (offline események), :110 (LMS-Z-04 unlock)
- **Probléma:** Az ERT-39 „jelenléti feltétel nélkül” kikötése csak az LMS-Z-05-be került be. Az általános §3-mondat továbbra is megengedi, hogy az offline eseményhez kötött tartalom később jelenléti checkpointtal nyíljon. Így a Z.A után nyíló, kurzusteljesítéshez szükséges LMS-Z-04 jelenléthez köthető marad.
- **Bizonyíték:** „vagy, ha később tényleges jelenléti checkpoint készül, annak igazolt completionjével nyitjuk.”; Z-04: „**Z.A után, a §7 szerinti dátummal**”.
- **Hatás:** Az ERT-39 szerint a „hiányzó jelenlét ne akadályozzon minden egyéb kaput teljesítő tanulót”. Egy jövőbeli Z.A-checkpoint ennek ellenére blokkolhatná a Z.4-et és a programteljesítést.
- **Javaslat:**
  - A :135 után: „A Z.A-hoz kötött online tartalom (LMS-Z-04, LMS-Z-05) jelenléti checkpointtal sem nyitható (ERT-39).”
  - A Z-04 unlockjába: „(jelenléti feltétel nélkül, ERT-39)”.
- **Típus:** objektív
- **Verdikt:** —

---

LEVÁGVA: 3 további finding, súlyosságuk: 3×P2. Röviden:
- a TEXT-C profil (:24) BIZT-2 maradványa, amely az ADV-1 után is DPO-kérdésnek mondja a hozzáférést;
- a QUIZ-M profilban az ERT-5 tanulói Review options szövege a „Mentor-láthatóság” oszlopba került, a mentori sor helyére;
- a BSPEC-02 leltárból hiányzik a Z.3 5. és 7. diája és az M7.3 checklist, miközben az RA 24. pont listája már tartalmazza őket.

<!-- agent a280133b2e4c238e0 -->

## Célzott QA: kánoni kör (bdb94ab), a levágott 3 finding

Ez a folytatás. Itt csak a korábban levágott három P2 áll, a már leadott tíz nem ismétlődik.

---

**CANON:QA-IMPL-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – activity manifest.md:24` (TEXT-C profil, „Mentor-láthatóság” oszlop)
- **Probléma:** A TEXT-C profil még nyitott DPO-kérdésnek nevezi a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférést. Erről az ADV-1 alapján a projektgazda már döntött, és az Adatvédelem §3 és §11 így is írja.
- **Bizonyíték:** manifest :24: „(a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés elfogadhatósága DPO-kérdés: BIZT-2)”. Ezzel szemben az Adatvédelem :232: „a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférésről (BIZT-2) … a projektgazda döntött (2026-10-12, ADV-1; §3)”.
- **Hatás:** A build-spec és az adatkezelési mátrix ellentmond egymásnak. A builder vagy a tájékoztató szerzője nyitott kérdésként kezeli azt, ami eldőlt, és kimaradhat az ADV-1 két feltétele:
  - a szerepkiosztás szűk, név szerinti és auditálható;
  - a tájékoztató nem tagadja a technikai adminisztrátor teljes hozzáférését.
- **Javaslat:** OLD „(a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés elfogadhatósága DPO-kérdés: BIZT-2)” → NEW „(a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférésről a projektgazda döntött: szűk, név szerint kiosztott, auditálható jogosultság, a technikai adminisztrátor teljes hozzáférését a tájékoztató nem tagadja; projektgazdai döntés, 2026-10-12, ADV-1, BIZT-2; `Adatvédelem – tanulói adatok és AI.md` §3)”.
  - A DPO vétó/QA-szerepéhez és a profil mentorszűkítési mondataihoz nem nyúlunk.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-ERT-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – activity manifest.md:18` (QUIZ-M profil, 6. oszlop: „Mentor-láthatóság”)
- **Probléma:** Az ERT-5 tanulói Review options-szövege a „Mentor-láthatóság” oszlopba került, és felülírta a korábbi mentori sort. Így a QUIZ-M profilból eltűnt, hogy a mentor/értékelő item-szinten látja a kritikus itemeket. Erre a GATE-CP kézi megerősítése épül.
- **Bizonyíték:** A fejléc: „| Retry | Mentor-láthatóság | Privacy |”. A cella új szövege: „az első próbálkozás után a pontszám és a hibázott kompetencia / kritikus követelmény; a helyes kulcs … csak a javító próbálkozás lezárása után”. A régi szöveg (a diff „-” sora): „eredmény + item-szintű review ott, ahol kritikus item van”.
- **Hatás:**
  - Tanulói beállítás áll egy mentori oszlopban, és a mentori item-szintű nézet nincs specifikálva.
  - Az LMS-M7-09 kézi ellenőrzése („a Q11/Q14 Multi-Select csak teljes ponttal számít”) és az M3 Q2/Q4/Q7/Q9 ellenőrzése (LMS-M3-07) erre a nézetre támaszkodik.
  - A régi mondat egyszerű visszaállítása tanulói nézetként is olvasható volna, és akkor ellentmondana az ERT-5-nek.
- **Javaslat:** NEW cella: „mentor/értékelő: eredmény és item-szintű review a kritikus itemeknél (a GATE-CP kézi megerősítéséhez: LMS-M3-07, LMS-M7-09); tanulói Review options: az első próbálkozás után a pontszám és a hibázott kompetencia / kritikus követelmény, a helyes kulcs és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; a kritikus itemekhez (M3, M7) a mentor szabályos javítási útmutatást ad (ERT-5, projektgazdai döntés, 2026-10-12; az eltérő Review options célverzión visszaolvasandó)”.
  - Az ERT-5 tartalmához nem nyúlunk, csak a mentori és a tanulói nézetet választjuk szét.
- **Típus:** objektív
- **Verdikt:** —

**CANON:QA-IMPL-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – activity manifest.md:311` (BSPEC-02, a „kötelező, de tanuló-lokális” és az „opcionális, tanuló-lokális” leltár), összevetve: `LMS – H5P runtime acceptance.md` > 24. pont
- **Probléma:** Az RA 24. pont sorlistája most már tartalmazza az LMS-M7-03-at (a Zmán Kvucá-checklist, LMS-5) és az LMS-Z-03-at (a Z.3 5. dia célmondata és 7. dia mini válasza, ADV-3). A BSPEC-02 leltár azonban csak az M3.1/M3.2 és az M4.1 tételekkel bővült, ezekkel nem.
- **Bizonyíték:** RA 24: „LMS-M7-03, LMS-M7-04, LMS-Z-01, LMS-Z-02 és LMS-Z-03 sorának megjegyzése szerint”. BSPEC-02 (kötelező lista vége): „M7.4 SLIDE 3; Z.1 SLIDE 5–6; Z.2 SLIDE 5–7;”. A Z.3 és az M7.3 egyik listában sincs.
- **Hatás:** A tanuló-lokális lépések kánoni leltára (DPO QA, `RELEASE-READINESS.md` G2) és a rögzítésmentességet igazoló tesztlista eltér egymásnak. Három tanuló-lokális lépésnek nincs rögzített besorolása a leltárban.
- **Javaslat:** Az ADV-3 kiegészítés mintájára új mondat a BSPEC-02 cella végére:
  - „**Kiegészítés (2026-10-12; projektgazdai döntés, `Emberi jóváhagyás szükséges.md` 14. szakasz):** a „kötelező, de tanuló-lokális” lista a Z.3 5. dia célmondatával, az „opcionális, tanuló-lokális” lista a Z.3 7. dia mini válaszával bővül (LMS-Z-03; ADV-3); az M7.3 Zmán Kvucá-checklist tanuló-lokális, külön sor nélkül (LMS-M7-03; LMS-5); rögzítésmentességük visszaolvasása: runtime acceptance 24. pont. A sor állapota nem változik.”
  - A Z.3 5. diájának kötelező besorolása az LMS-Z-03 sorából következik: a sor csak a 7. diát nevezi opcionálisnak.
  - Az M7.3 checklist kötelező/opcionális besorolását se a manifest, se az M7.3 :8 és :825 nem mondja ki. Ezért ott csak a „tanuló-lokális (LMS-5)” jelölés kerüljön be; új besorolást nem találunk ki.
- **Típus:** objektív
- **Verdikt:** —

<!-- agent aecfe4ddf14953741 -->

Célzott QA, nyelvi lencse, kánoni kör (AP-2026-10-12-01, bdb94ab). Csak a diff új vagy módosított mondatait és a közvetlen környezetüket néztem. Minden tétel P2, mindegyik `objektív`. A döntések szó szerinti szövegét nem jelentem. Nem jelentem azt sem, ahol a kánon a döntés szövegét követi: GYV-10, ADV-12 és LMS-8 háromféle megnevezése, ERT-2 „legitim aktivitás”, PRG-6 „ne szorítsa ki”, ADV-6 „addig”. Az ADV-7-ből kimaradt „fotózás alapból nincs” sem finding, mert az Adatvédelem §6 HUM-PRIV-02 bekezdése már kimondja. 15 finding van, ennél több nem volt, ezért nincs LEVÁGVA sor.

Rövidítések:
- ADV = 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- RTA = 02 Tervezet/LMS – H5P runtime acceptance.md
- GLO = 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md
- PT = 02 Tervezet/Program terv.md
- GK = 02 Tervezet/Gyermekvédelem – release gate.md

---

**CANON:QA-NYELV-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** ADV:83 (§3, „Külön review szükséges legalább”, M4 pont)
- **Probléma:** Az ADV-9 átvezetésekor kiesett az alaptag. A döntés „kvuca-adatszabályt” mond, a szöveg csak „kvuca-adatot”. Így azt állítja, hogy az M4-be a Peula v2 adata kerülhet, holott ez M7-es produktum, és az M4 idején még nem létezik.
- **Bizonyíték:** „valós kvucáról csak a Peula v2 csoportszintű kvuca-adata: korosztály, …” · ADV-9: „A Peula v2 minimális csoportszintű kvuca-adatszabályát alkalmazzuk az M4/M5/M6 produktumokra is”
- **Hatás:** A DPO vagy a build-olvasó időrendi képtelenséget lát, a szabály forrása homályos.
- **Javaslat:** „csak a Peula v2 csoportszintű kvuca-adata:” → „csak a Peula v2 csoportszintű kvuca-adatszabálya szerinti adat:”. A felsorolt adatkör nem változik.
- **Típus:** objektív

**CANON:QA-NYELV-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** ADV:82 (§3, M3 pont; ez a diff egyik kontextussora)
- **Probléma:** A TERM-5 („M3 – Helyzetleírás” következetesen) átvezetése után a 02 Tervezet `.md`-fájljaiban ez az egyetlen „helyzetelemzés”. Ugyanarra a kapuproduktumra így két név él.
- **Bizonyíték:** „M3 gyermekvédelmi helyzetelemzés: a kapuproduktumba **csak kitalált, életszerű eset** kerülhet” · MAN LMS-M3-07: „„Teljesítve” = helyzetleírás: …”
- **Hatás:** Egy fogalomnak két megnevezése van a kánonban.
- **Javaslat:** „M3 gyermekvédelmi helyzetelemzés:” → „M3 gyermekvédelmi helyzetleírás:”. A „harmadik személyű esetelemzés” más fogalom, ahhoz nem kell nyúlni.
- **Típus:** objektív

**CANON:QA-NYELV-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** ADV:53 (alapelvek, Google-sablon pont)
- **Probléma:** Az ADV-10 két külön mondata egy tagmondatba olvadt. Elsőre felsorolásnak olvasható, mintha a nyílt digitális fal is az „alap” része lenne. Az „egyenértékű feladattal” határozónak nincs mihez kapcsolódnia.
- **Bizonyíték:** „az alap a Moodle és a papír, nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladattal, és a szolgáltató, …”
- **Hatás:** Az adatvédelmi szabály félreolvasható, felolvasva nem követhető.
- **Javaslat:** „…használható; az alap a Moodle és a papír, nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladattal, és a szolgáltató, …” → „…használható; az alap a Moodle és a papír; nyílt digitális fal vagy QR-eszköz nélkül is van egyenértékű, teljesíthető feladat; a szolgáltató, …”. A pont többi része változatlan.
- **Típus:** objektív

**CANON:QA-NYELV-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** ADV:247 (§11 tanulói tájékoztató, „Ki látja?”)
- **Probléma:** Az új tanulói mondat határozatlan tárggyal szól („Egy kapubeadványt”), a bekezdés többi mondata viszont tegező birtokos alakot használ („a beadandóidat”, „a szöveges válaszaidat”). Az ige a nagykötőjeles betét után a mondat végére szorul. A Memunára vonatkozó tagból hiányzik a „csak”, amely az M3.4 azonos tanulói mondatában megvan.
- **Bizonyíték:** „Egy kapubeadványt második vagy fellebbezési értékelő csak konkrét eljárásnál – például ha újraértékelést kérsz – lát, a Memuna pedig szükség esetén.”
- **Hatás:** Felolvasva nehezen követhető, és nem egyértelmű, hogy a tanuló saját beadványáról van szó.
- **Javaslat:** A teljes mondat cseréje erre: „A kapubeadványodat második vagy fellebbezési értékelő csak konkrét eljárásban látja – például ha újraértékelést kérsz –, a Memuna pedig csak szükség esetén.” A szereplők, a „fellebbezési” szó (az M3.4 tanulói szövege is használja) és a példa maradjon.
- **Típus:** objektív

**CANON:QA-NYELV-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** ADV:183, két helyen (§7, „Hozzáférés és naplózás”); PT:250 (AI-segéd pont)
- **Probléma:** Folyó szövegben az állítmány a „van” nélküli határozói igenév. A PT-ben ez véges igés taggal áll mellérendelve, ezért a mondat nyelvtanilag csonka.
- **Bizonyíték:** PT: „a végponton a tartalom naplózása alapból kikapcsolva, és a `store=false` önmagában nem bizonyít …” · ADV: „ideiglenesen az AI-segéd kikapcsolva, a no-AI út teljes értékű”
- **Hatás:** A mondatok jegyzetszerűek, a PT-ben a mellérendelés hibás.
- **Javaslat:** Mindkét fájlban „alapból kikapcsolva,” → „alapból ki van kapcsolva,”, valamint „ideiglenesen az AI-segéd kikapcsolva,” → „ideiglenesen az AI-segéd ki van kapcsolva,”. Az RTA 20. pontja már így írja.
- **Típus:** objektív

**CANON:QA-NYELV-6**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** GLO:188 (teljesítési kapu, F-peula pont)
- **Probléma:** A ragtalan „nem „nem teljesült” bukás” alanyként olvasódik, vagyis úgy, hogy nem a bukás váltja ki az F-peulát. Az ERT-8 viszont azt mondja, hogy a gyenge munka nem eredményez bukást. A PT:286 és a GLO:194 ezt egyértelműen „és ez nem bukás” alakban mondja.
- **Bizonyíték:** „a gyenge, de értelmezhető munka (a rubrika-küszöb alatti eredmény) váltja ki, nem „nem teljesült” bukás;”
- **Hatás:** A szabály jelentése elcsúszik.
- **Javaslat:** „váltja ki, nem „nem teljesült” bukás;” → „váltja ki, és ez nem „nem teljesült” bukás;”
- **Típus:** objektív

**CANON:QA-NYELV-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** GLO:194 (F-peula szócikk, első mondat); PT:286 (§5, „Nem teljesítés kezelése”)
- **Probléma:** Az ERT-8 beillesztése után a keretmondat („ha egy kapu nem teljesült” / „Ha a kapu nem teljesült:”) nem fedi a közvetlenül utána leírt puha kapus esetet. A beillesztett mondat szerint az az eset nem bukás, tehát nem „nem teljesült” kapu.
- **Bizonyíték:** GLO: „Facilitált, strukturált javítási alkalom, ha egy kapu nem teljesült (M1.F–M7.F). … puha kapunál a küszöb alatti, de értelmezhető munka váltja ki, és ez nem bukás” · PT: „* Ha a kapu nem teljesült: **F-peula** – … puha kapunál a küszöb alatti, de értelmezhető beadás váltja ki, és ez nem bukás”
- **Hatás:** A definíció önellentmondó.
- **Javaslat:**
  - GLO: „Facilitált, strukturált javítási alkalom, ha egy kapu nem teljesült (M1.F–M7.F).” → „Facilitált, strukturált javítási alkalom, ha egy kapu nem teljesült, puha kapunál pedig a küszöb alatti, de értelmezhető munka után (M1.F–M7.F).”
  - PT: a puha kapus félmondat külön mondatba kerül a „Ha a kapu nem teljesült:” keret alól, a szavai változatlanok.
  - A definíció szó szerinti másolatai is igazítandók, a modul-scope-ban: M3 hub:224, M4 hub:108, M4.F:37.
- **Típus:** objektív

**CANON:QA-NYELV-8**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** RTA:87 (16. pont)
- **Probléma:** A „hogy”-mellékmondatba ige nélküli tárgy került, a mondat csonka.
- **Bizonyíték:** „Tesztelni kell, hogy az 1. kérdés „Required”, a többi kihagyható, és stagingben a „kiürítés” valós működését is (ERT-3; …)”
- **Hatás:** A tesztlépés nem olvasható fel egyértelműen.
- **Javaslat:** → „Tesztelni kell, hogy az 1. kérdés „Required”, a többi pedig kihagyható; stagingben a „kiürítés” valós működését is tesztelni kell (ERT-3; projektgazdai döntés, 2026-10-12; a „kiürítés” pontos jelentését a build-spec gazda rögzíti).”
- **Típus:** objektív

**CANON:QA-NYELV-9**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** MAN:103 (LMS-M7-06, Completion oszlop)
- **Probléma:** Hiányzó alaptag: a döntés „kipipálása” szava kiesett, így a határozatlan névelő egy angol UI-címkére vonatkozik.
- **Bizonyíték:** „egy „Receive a passing grade” az Assignmenten nem helyettesíti a konjunktív feltételt (ERT-9)” · ERT-9: „Egy „Receive a passing grade” kipipálása az Assignmenten…”
- **Hatás:** A mondat nyelvtanilag hiányos.
- **Javaslat:** „egy „Receive a passing grade” az Assignmenten” → „a „Receive a passing grade” bekapcsolása az Assignmenten”
- **Típus:** objektív

**CANON:QA-NYELV-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** MAN:103 (LMS-M7-06, Megjegyzés, ERT-41)
- **Probléma:** Két hiba van egy helyen.
  - A „pótlást kér, nem értékelő visszajelzéssel” kétféleképp olvasható (visszajelzés helyett, vagy nem értékelő jellegű visszajelzéssel), és kiesett a döntés „értelmezhető” minősítője.
  - Az alany jelöletlenül vált: a „nem buktat” és a „nem akadályozza” nyelvtanilag az értékelőre mutat („az értékelő nem akadályozza a v2 szakmai értékelését”).
- **Bizonyíték:** „hiányzó vagy üres mezőnél (…) pótlást kér, nem értékelő visszajelzéssel; tartalmilag nem pontozza, nem buktat, és a v2 szakmai értékelését nem akadályozza”
- **Hatás:** Az értékelő nem tudja, kell-e visszajelzést adnia, és mi az, ami nem buktat.
- **Javaslat:** → „…az értékelő az érdemi leadást nézi; ha a vállalás vagy az AI-sor hiányzik vagy üres, kitöltési pótlást kér, és értelmezhető, nem értékelői visszajelzést ad; a vállalást tartalmilag nem pontozza; a hiány nem buktatja a kaput, és nem akadályozza a v2 szakmai értékelését (M7 KAPU; ERT-41)”. Ugyanez a megfogalmazás áll a `Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md` 263., 426. és 427. sorában. A 7. regressziós minta miatt ezeket együtt kell javítani, de az M7-scope-ban.
- **Típus:** objektív

**CANON:QA-NYELV-11**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** MAN:84 (LMS-M5-06), MAN:92 (LMS-M6-06), Megjegyzés oszlop
- **Probléma:** Ugyanaz az ERT-6 két sorban, két hibás alakban.
  - M5: a „jelzés … számol” igéje rossz alanyhoz kerül, a „nem írják felül” tárgya hiányzik.
  - M6: azonosító állítás lett belőle („a jelzés az első próbálkozás”), kiesett a „-hoz … a mérvadó”.
- **Bizonyíték:** „a tanulói és a stáb-jelzés az első, visszajelzés előtti próbálkozásból számol, … és nem írják felül” · „a diagnosztikus jelzés az első, visszajelzés előtti próbálkozás, a stáb-jelzést …”
- **Hatás:** A build-szabály pontatlanul olvasható.
- **Javaslat:**
  - M5 → „a tanulói és a stáb-jelzést az első, visszajelzés előtti próbálkozásból kell számolni; a további próbálkozások gyakorlásra szolgálnak, és a korai jelzést nem írják felül”
  - M6 → „a diagnosztikus jelzéshez az első, visszajelzés előtti próbálkozás a mérvadó, a stáb-jelzést ennek item-statisztikájából kell számolni”
- **Típus:** objektív

**CANON:QA-NYELV-12**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** MAN:106 (LMS-Z-02), MAN:107 (LMS-Z-03), Megjegyzés oszlop
- **Probléma:** A „kap” igének nincs alanya. Az előző tag alanya a „completion”, így a mondat szerint a completion kap completiont.
- **Bizonyíték:** „a completion az összefoglaló dia elérése (…); erre épülő completiont csak akkor kap, ha a célverzión ténylegesen van összefoglaló diája”
- **Hatás:** A mondat logikailag zavaros.
- **Javaslat:** Mindkét sorban → „erre épülő completiont a CP csak akkor kap, ha a célverzión ténylegesen van összefoglaló diája”. Ez a §1 H5P-C profil megfogalmazását követi.
- **Típus:** objektív

**CANON:QA-NYELV-13**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** MAN §2: LMS-M1-05, LMS-M5-05, LMS-M6-05, LMS-M7-06, Completion oszlop; MAN §4 táblázat: M1, M5, M6, M7 sor
- **Probléma:** Ugyanaz az ERT-9-felosztás négy sorban négyféle szerkezettel szerepel.
  - A „jegyalapú completion kikapcsolva/nélkül” kitétel csak az M1 és az M5 sorban van meg.
  - A §4-ben csak az M5 sor kapta meg az új állapotneveket, az M1, M6 és M7 sor „mastery” maradt.
  - Megjegyzés: az LMS-M3-05 (szintén ASSIGN-M) régi formulája a döntéshűségi lencsére tartozik.
- **Bizonyíték:** M5: „a megerősített kapueredmény (CONFIRMED) az LMS-M5-08 GATE-CP sor” · M6: „… az LMS-M6-07 GATE-CP-n áll be” · §4: „| M1 | H5P-k + LMS-M1-05 mastery |” ↔ „LMS-M5-05 leadva + LMS-M5-08 „Teljesítve””
- **Hatás:** A build-olvasó nem tudja, szándékos-e az eltérés. Például az M6/M7 Assignmenten bekapcsolható-e a jegyalapú completion.
- **Javaslat:**
  - Egységes minta a meglévő ASSIGN-S sorok szerint: „SUBMITTED: a <produktum> leadva (`completionsubmit`; jegyalapú completion kikapcsolva); CONFIRMED: <GATE-CP build_id> – a megerősített kapueredmény (ERT-9)”.
  - A §4-ben „<Assignment> leadva + <GATE-CP> „Teljesítve”” a „mastery” helyett.
  - Hogy az M6/M7 sorba is kell-e a „jegyalapú completion kikapcsolva”, azt az implementációs lencse igazolja.
- **Típus:** objektív

**CANON:QA-NYELV-14**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** MAN:43 (LMS-M0-05, Megjegyzés)
- **Probléma:** Elveszett minősítő (2. regressziós minta). A döntés, az ADV:79, az M0 hub:138 és az M0.4:586 egyaránt „jogszerű alapértéket” mond, a manifestből ez a szó kimaradt.
- **Bizonyíték:** „a „képzés vége + 90 nap” nem automatikus alapérték” · ADV-6: „nem automatikus jogszerű alapérték”
- **Hatás:** A jogszerűségi kitétel elvész, a kánon két helyen eltér.
- **Javaslat:** „nem automatikus alapérték” → „nem automatikus jogszerű alapérték”
- **Típus:** objektív

**CANON:QA-NYELV-15**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** GK:65 (§5 szabálylista, GYV-5)
- **Probléma:** A döntés „legyen” előírása „van” tényállítássá vált, és az „előzetesen” a létigével értelmesen nem kapcsolható össze. A létszámszabály így leírásnak olvasható.
- **Bizonyíték:** „érzékeny, potenciálisan felkavaró peulán előzetesen legalább két rendelkezésre álló, felkészített, 18 év feletti felelős van, vagy azonnal elérhető helyettes …”
- **Hatás:** Gyermekvédelmi létszámszabályról van szó, ezért a normatív erő gyengülése kockázat.
- **Javaslat:** „peulán előzetesen legalább két … felelős van, vagy azonnal elérhető helyettes és kötelező megállítási protokoll” → „peulán előzetesen legyen legalább két … felelős, vagy azonnal elérhető helyettes és kötelező megállítási protokoll”. A pont többi része változatlan.
- **Típus:** objektív
