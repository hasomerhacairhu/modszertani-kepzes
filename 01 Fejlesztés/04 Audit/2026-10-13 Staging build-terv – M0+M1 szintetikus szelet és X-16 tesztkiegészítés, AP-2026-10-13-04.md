# Staging build-terv – M0+M1 szintetikus szelet és X-16 tesztkiegészítés, AP-2026-10-13-04

> **Audit trail, nem kánon; nem deployment.** A legkisebb értelmes staging-szelet (M0+M1, RR „Legkisebb értelmes
> staging-szelet”) végrehajtható build-terve a jóváhagyott manifest és a staging-leltár
> (`2026-10-13 Staging-előkészítés – zárt, szintetikus M0+M1 build és az X-16, AP-2026-10-13-03.md`) alapján. A tényleges
> deploymentre nincs engedély (projektgazda, 2026-10-13). A runtime-teszteket csak a célkörnyezetben lefutott eredmény
> mozdíthatja `RUNTIME_VERIFIED`-re. **Hitelesítő adat (jelszó, token, kulcs, URL-be ágyazott titok) a repóba nem kerül:**
> a fiókok és tokenek az LMS-gazda által kezelt, repón kívüli tárolóban vannak; a terv csak szerepet és szintetikus
> fiókcímkét nevez meg. Rövidítések: MAN = `02 Tervezet/LMS – activity manifest.md`, RA = `02 Tervezet/LMS – H5P runtime
> acceptance.md`, HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`, RR = `02 Tervezet/RELEASE-READINESS.md`.

## 0. Blokkoló előfeltételek (staging build előtt)

| # | Bemenet | Ki adja | Hova kerül |
|---|---|---|---|
| P1 | a staging deployment engedélye | projektgazda | release-tracker (#4), Napló |
| P2 | a célkörnyezet: a staging Moodle-példány címe (titok nélkül), a pontos Moodle-verzió és -build | LMS-gazda / build-felelős | RA „Environment record” (Moodle sor) |
| P3 | a H5P: a `mod_h5pactivity` és a H5P core verziója, valamint a content type-ok telepített verziója (RA :12–25) | LMS-gazda / site-adminisztrátor | RA „Environment record” |
| P4 | site-adminisztrátori hozzáférés a buildhez (a fiók és a hitelesítő adat repón kívül) | site-adminisztrátor | — |
| P5 | a `neongodio/moodle-ai-mcp` Core 1.0 kapcsolat a célkörnyezethez (MAN :189; a token repón kívül) | LMS-gazda | — |
| P6 | a TEST_OWNER kijelölése | LMS-gazda | RA „Environment record” |

Nem előfeltétel: valódi dátum, valódi kontakt, a Memuna, a DPO vagy az értékelési felelős jóváhagyása (RR G8; RR
„Staging-szabály” 1–3.).

## 1. Site-szintű beállítások (rögzítendő, nem tervezett érték)

- `mod_h5pactivity/enablesavestate` és `mod_h5pactivity/savestatefreq`: a célkörnyezet értéke, a teszt idején rögzítve (RA
  :11, 24. pont).
- Teljesítéskövetés site-szinten bekapcsolva (a kurzusszintű completion feltétele).
- „Enable web services for mobile devices” és a `moodle/webservice:createmobiletoken` rendszerkontextusbeli állapota (az
  „Authenticated user” és bármely rendszerszinten kiosztott szerep; a Student szerep definíciójában beállított tiltás nem
  hat, MAN LMS-M4-05): rögzítendő, mert az X-16 API-tesztje (RA 28 (g2)) ettől függ; a beállítás megváltoztatásáról a
  projektgazda, az LMS-gazda és a site-adminisztrátor dönt (HUM 17. szakasz).
- A „Data requests” elérhetősége és az „Automatic data export request approval” beállítás: rögzítendő (RA 28 (g4)); a
  build nem változtat rajta (HUM 17. szakasz, adatvédelmi kérdés).
- A11Y-07 (iframe-cím): a telepített megoldás vagy annak hiánya (RA :27).

## 2. Kurzus

1. Rejtett staging-kurzus (MAN :211), Topics formátum, szakaszok M0–M7 + Z; a szeletben csak az M0 és az M1 töltődik.
2. „Group mode” = „Separate groups”, „Force group mode” = „No” (MAN :31).
3. Completion bekapcsolva; kurzusteljesítés: „Condition requires” = All, a kötelező sorok (MAN :171); az LMS-M0-05 a futó
   kohorszban nem feltétel (D-15 (f)).
4. X-16 kurzusszintű beállítások (staging-validáció, HUM 17. szakasz): „Grade letters” – „Override site defaults”, egyetlen
   betűjegy: „Szöveges értékelés” ≥ 0 %; tanulói pontkönyv: „Show percentage”, „Show ranges”, „Show contribution to course
   total”, „Show weightings”, „Show letter grades”, „Show rank”, „Show average” = No, „Show grades” és „Show feedback” = Yes;
   a „Course total” rejtett. A szeletben ezek a regressziós tesztet (RA 29) szolgálják.
5. Kurzusszintű elemek (MAN :118–135): „Segítség és kapcsolatok” blokk (a technikai és a programkontakt helyén belső
   build-jelölő, tanulói nézet nélkül; a Memuna és a helyettese a kánoni adatokkal), „ha téged is érint” blokk (kánoni
   szöveg), glosszárium (PAGE-C), az M1.1–M1.3 offline fájljai. Az adatvédelmi tájékoztató (PAGE-C) a
   `PRIVACY_CONTACT_TO_CONFIGURE` jelölő miatt a stagingben rejtve marad, amíg az adatvédelmi kontakt nincs megadva.

## 3. Csoportok és tesztfiókok (szintetikus, név nélkül)

A fiókcímkék szintetikusak; a hitelesítő adat repón kívül. Mentoronként legfeljebb 8 tanuló (HUM :245).

| Címke | Moodle-szerep | Csoport | Mire kell (RA) |
|---|---|---|---|
| tanuló-A1, tanuló-A2 | Student | A | 1, 6–9, 13–15, 17, 19, 22–26, 29, RT-A11Y |
| tanuló-B1 | Student | B | 15 (csoportelválasztás) |
| tanuló-K1 | Student | — (második kurzuspéldány) | 27 |
| mentor-A, mentor-B | Non-editing teacher | csak a saját | 6, 8, 15, 24, 26 |
| mentor-0 | Non-editing teacher | nincs | 15 negatív eset; csak ideiglenesen, a TEXT-C visszaolvasásán kívül |
| szerkesztő-1, menedzser-1 | Editing teacher, Manager | — | 15 |
| képző-1 | nyitott: a szerep nincs kijelölve (X-17) | — | 6, 15, 16, 21, 24 |
| ADV-2-fiók | nyitott: az ADV-2 hozzáférési mód (X-17) | — | 15 |

A tanulói fiókok száma minimum; a végleges számot a TEST_OWNER rögzíti. Az X-16 tesztkiegészítéshez (5. pont) szintenként
további egy-egy tanulói fiók kell.

## 4. Activityk – build-sorrend (M0+M1, 13 elem)

A `cmid` a létrehozás után kerül a MAN-be (`BUILD_OUTPUT`). Dátumfüggő elem dátum nélkül épül, a jelölő tanulói nézetbe nem
kerül (MAN :222).

| # | build_id | Név | Profil | Unlock (MAN) | Staging-megjegyzés |
|---|---|---|---|---|---|
| 1 | LMS-M0-01 | M0.1 – Üdv a képzésben! | H5P-C | kurzushozzáférés | — |
| 2 | LMS-M0-02 | M0.2 – Madrih, nem terapeuta | H5P-C | LMS-M0-01 | — |
| 3 | LMS-M0-03 | M0.3 – Moodle, H5P és kapuk | H5P-C | M0.A után, dátummal | a nyitás teszteléséhez szintetikus tesztdátum kell (X-17) |
| 4 | LMS-M0-04 | M0.4 – Dugma isit online | H5P-C | LMS-M0-03 | — |
| 5 | LMS-M0-05 | Bemutatkozó fal | FORUM-C | LMS-M0-04 | rejtett, semmi nem hivatkozik rá; „Group mode” = „No groups”; RA 27 |
| 6 | LMS-M0-06 | M0 belépőkvíz | QUIZ-D | LMS-M0-04 | role override: `mod/quiz:viewreports`, `mod/quiz:grade`; próbálkozásszám nyitott (X-17) |
| 7 | LMS-M1-01 | M1.1 – Johari-ablak | H5P-C | M0 complete | — |
| 8 | LMS-M1-02 | M1.2 – Megfigyelés ≠ értelmezés | H5P-C | LMS-M1-01 | — |
| 9 | LMS-M1-03 | M1.3 – SBI-modell | H5P-C | M1.A után | szintetikus tesztdátum kell (X-17) |
| 10 | LMS-M1-07 | M1.3 – Saját mini-SBI | TEXT-C | LMS-M1-03 | TEXT-C beállítások (MAN :24, :50); csoport nélküli mentorfiók nincs |
| 11 | LMS-M1-04 | M1.4 – Mondd el SBI-ben | H5P-C | LMS-M1-07 | — |
| 12 | LMS-M1-05 | M1.4 – SBI-beadandó | ASSIGN-M | LMS-M1-04 | Point, max 8, rubrika-előnézet; „Grant attempts” = Manually; elfogadott fájltípus nyitott (X-17) |
| 13 | LMS-M1-06 | M1 – kapueredmény (`GATE_CONFIRMED_M1`) | GATE-CP | a stáb tölti ki | kételemes skála, Grade to pass = 2; nem rejtett, nem zárolt |

A kurzusszintű PAGE-C és File elemeknek nincs build-ID-ja (RR „Staging-szabály” 4.); a build-visszaolvasás előtt ki kell
jelölni (X-17; a repó nem nevez meg felelőst).

## 5. X-16 tesztkiegészítés (döntésre vár)

Az RT-P0-28 az LMS-M2-05, LMS-M4-05 és LMS-M6-05 Assignmentet kéri, ezek nincsenek az M0+M1 szeletben. Két út; a választás a
projektgazdáé:

- **(a)** a három Assignment és a hozzájuk tartozó GATE-CP sor (LMS-M2-10, LMS-M4-10, LMS-M6-07; a RA 28 (k) esetéhez) a
  staging-kurzusban a manifest szerinti rubrikával, pontozással és skálával, a hozzáférési feltétel nélkül, kizárólag
  tesztcélra (a környezeti rekordban rögzítve);
- **(b)** a három Assignment a manifest szerinti feltételekkel; a tesztfiókoknak előtte az M2–M6 előfeltételeit teljesíteniük
  kell (lényegesen nagyobb build).

Javaslat: (a), mert az RT-P0-28 a tanulói megjelenítést méri, nem a nyitást; a nyitásokat a modulok saját tesztjei mérik.

## 6. Tesztek a szeleten

- A szeletben futtatható: RA 1, 6, 7, 9, 13–15, 17, 19 (az ASSIGN-M ág: LMS-M1-05), 22–27 és RT-A11Y; az X-16
  tesztkiegészítéssel (5. pont) a 28. is.
- Részben futtatható, a hiányzó elem megnevezésével kell rögzíteni:
  - RA 8: az M1 kapueredménye (LMS-M1-05 rubrika, LMS-M1-06) a szeletben rögzíthető, de a Grade-feltételű célpont (LMS-M2-01
    „M1 megerősítve”, LMS-M3-05 „M1 complete”, MAN §4) nincs benne, ezért a negatív eset („nem nyílik meg”) nem mérhető;
  - RA 29: az (a) és az (f) eset az 5. pont kiegészítésével; a (b) a szeletben csak az LMS-M0-06-ra (a QUIZ-M és az
    LMS-M7-07 nincs benne); a (d) Grade-feltételű célpont nélkül nem mérhető (az LMS-M3-06 nincs benne).
- Opció a RA 8 és a RA 29 (d) esetére: tesztcélú csonk-activity a szeletben, a MAN §4 „M1 megerősítve”, illetve „M1
  complete” Grade-feltételével az LMS-M1-06-ra, a környezeti rekordban rögzítve; a manifest unlock-feltételei és a RA-pontok
  nem változnak. A választás a projektgazdáé (7. pont).
- Az eredmény a RA „Teszt-állapot” táblájába dátummal, verzióval és bizonyítékkal kerül; tesztfiókok név nélkül,
  képernyőkép személyes adat nélkül.

## 7. Nyitott bemenetek (X-17) – nem blokkolják a buildet, a tesztek előtt kellenek

| Tétel | Ki adja |
|---|---|
| szintetikus tesztdátum használata a staging-kurzusban | programvezető |
| a „képző” Moodle-szerepe; az ADV-2 hozzáférési mód | LMS-gazda + adatvédelmi felelős |
| build-ID a kurzusszintű PAGE-C/File elemekre | a repó nem nevez meg felelőst |
| az LMS-M0-06 próbálkozásszáma | a repó nem nevez meg felelőst |
| az LMS-M1-05 elfogadott fájltípusa | LMS-gazda + DPO + hozzáférhetőségi gazda |
| az X-16 tesztkiegészítés módja (5. pont) | projektgazda |
| tesztcélú csonk-activity a RA 8 és a RA 29 (d) esetére (6. pont) | projektgazda |
| a tanulói webszolgáltatás-elérés lezárása (X-16 release-kapu) | projektgazda + LMS-gazda + site-adminisztrátor |
| az adatexport-út: vonatkozik-e rá a rejtés release-feltétele (HUM 17. szakasz) | DPO + jogi felelős + projektgazda |

## 8. Célzott QA (QA20, implementáció) és feldolgozása

A diffre (HUM 17. szakasz, manifest LMS-M4-05, RA 28–29) és e terv vázlatára futott, read-only. A fő session a három
findingot a Moodle 4.5 (`MOODLE_405_STABLE`) forrásában ellenőrizte: `lib/db/access.php` (`moodle/webservice:createmobiletoken`:
`CONTEXT_SYSTEM`, archetípus `user`), `lib/external/classes/util.php` (`generate_token_for_current_user()`: az érvényes tokent
jogellenőrzés nélkül adja ki újra), `mod/assign/externallib.php` (`get_submission_status()`: `feedback.grade` és
`previousattempts[].grade` a nyers ponttal), `mod/assign/classes/privacy/provider.php` (`export_grade_data()`: `'grade' =>
$grade->grade`), `admin/tool/dataprivacy/lang/en/tool_dataprivacy.php` és `settings.php` (a „Data requests”, „Export all of
my personal data”, „Automatic data export request approval” felirat).

| ID | Feldolgozás |
|---|---|
| QA20-IMPL-1 | javítva (`65d883e`): a manifest a `createmobiletoken`-tiltást rendszerkontextushoz köti, a Student szerepen hatástalannak mondja, és a kiadott tokenek visszavonását kéri; RA 28 (g2) a lezárás előtt tokent kapott fiókkal is; e terv 1. pontja |
| QA20-IMPL-2 | a tény javítva (`65d883e`): HUM 17. szakasz „Nyitott (adatvédelmi kérdés)”, manifest LMS-M4-05, RA 28 (g4); a release-feltétel hatóköre (vonatkozik-e az adatexportra) emberi döntés: DPO + jogi felelős + projektgazda |
| QA20-IMPL-3 | javítva ebben a tervben: 3. pont (RA 19), 5. pont (a) a három GATE-CP sorral, 6. pont (a RA 8 és a RA 29 részleges, a csonk-activity opció), 7. pont |

A QA nem ellenőrizte, és a fő session sem: hogy az „Enable web services for mobile devices” = No a már kiadott tokeneket
érvényteleníti-e. A RA 28 (g2) ezért mindkét lezárási módnál a lezárás előtt tokent kapott fiókkal is tesztel.

### A. melléklet – a QA20 nyers kimenete

> QA20-IMPL: célzott, diffre szabott implementációs QA, read-only. **3 finding: 2×P1, 1×P2.** A forrás mindenhol a moodle/moodle `MOODLE_405_STABLE` ága, a raw.githubusercontent.com-ról olvasva, valamint a MoodleDocs 405.
>
> **QA20-IMPL-1**
> - **Súlyosság:** P1
> - **Bizalom:** magas
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/LMS – activity manifest.md:80` (LMS-M4-05, „lehetséges lezárás”); `02 Tervezet/LMS – H5P runtime acceptance.md:113` (28. pont, (g2): „a token-kérés elutasítását kell rögzíteni”); `a build-terv (scratchpad-vázlat)` §1, 3. pont („a tanulói `moodle/webservice:createmobiletoken` állapota”)
> - **Probléma:** A második lezárási mód nem működik. A manifest szövege: „a tanulói szerepen rendszerszinten a `moodle/webservice:createmobiletoken` tiltása”.
>   - A jogot a Moodle alapból az „Authenticated user” szerepnek adja, és a tokenkiadás rendszerkontextusban ellenőrzi.
>   - A kurzusban kiosztott Student szerep a rendszerkontextusban nem érvényes, ezért a tiltás hatástalan.
>   - A már kiadott, érvényes tokent a Moodle jogellenőrzés nélkül újra kiadja. Egy friss tesztfióknál elutasított token-kérés ezért nem bizonyítja a lezárást.
> - **Bizonyíték:**
>   - `lib/db/access.php`: „'moodle/webservice:createmobiletoken' … 'contextlevel' => CONTEXT_SYSTEM, 'archetypes' => array( 'user' => CAP_ALLOW )”.
>   - `lib/external/classes/util.php`, `generate_token_for_current_user()`: „If some valid tokens exist then use the most recent.”, majd „($isofficialservice && has_capability('moodle/webservice:createmobiletoken', $context))”, ahol a kontextus `context_system::instance()`.
>   - MoodleDocs 405, Capabilities/moodle/webservice:createmobiletoken: „This capability is allowed for the default role of authenticated user”.
> - **Hatás:** A döntéshozók (projektgazda, LMS-gazda, site-adminisztrátor) hatástalan lezárást választhatnak. Ilyenkor a tanuló a mobilalkalmazáson vagy a webszolgáltatáson át továbbra is megkapja a nyers pontot (`graderaw`, illetve a diff szerint `feedback.grade`), az RT-P0-28 (g2) pedig mégis lezártnak mutathatja az utat.
> - **Javaslat:**
>   - A manifest :80 második opcióját pontosítani kell. A tiltás csak rendszerkontextusban hat: az „Authenticated user” szerepen (ez minden felhasználót érint, a stábot is), vagy egy külön, a tanulóknak rendszerszinten kiosztott tiltó szerepen. A Student szerep definíciójában beállított tiltás nem hat.
>   - Ennél az opciónál a már kiadott tanulói tokeneket vissza kell vonni.
>   - A (g2) kiegészül egy esettel: a lezárás előtt tokent szerzett tanulói fiók a lezárás után sem kap választ a két függvénytől.
>   - Tilos: a lezárásról dönteni, és a többi X-16-beállítást módosítani.
> - **Típus:** objektív
> - **Verdikt:**
>
> **QA20-IMPL-2**
> - **Súlyosság:** P1
> - **Bizalom:** közepes
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md` > 17. szakasz („Nyitott (release-kapu)” bekezdés; az X-16 sor „Nyitva marad” oszlopa); `02 Tervezet/LMS – activity manifest.md:80` (korlát-mondat); `02 Tervezet/LMS – H5P runtime acceptance.md:113` (28. pont, (g2))
> - **Probléma:** A kánon csak a webszolgáltatás-utat nevezi meg. Van egy másik tanulói út is: a Moodle adatkérés-exportja (Data requests, „Export all of my personal data”) a tanuló saját Assignment-pontszámát nyersen adja ki. Ezt sem a 28. pont, sem a lezárási opciók nem fedik le, és ez az út a GDPR hozzáférési joga miatt valószínűleg nem is zárható le.
> - **Bizonyíték:**
>   - `mod/assign/classes/privacy/provider.php`, `export_grade_data()`: „'grade' => $grade->grade,”.
>   - MoodleDocs 405, Data privacy: „Click the link 'Data requests' then click the 'New request' button. Select 'Export all of my personal data' …”.
> - **Hatás:** A projektgazdai döntés szerint „Ha a tanuló a `graderaw` vagy más út révén mégis hozzáfér a numerikus pontszámhoz, ezt ne minősítsd teljesített rejtésnek.” Ezen az úton a rejtés nem teljesül. Ha a release-feltétel azt jelenti, hogy a tanuló semmilyen úton nem fér a számhoz, akkor a webszolgáltatás lezárása után is teljesíthetetlen marad, és ezt a döntéshozók most nem tudják.
> - **Javaslat:**
>   - A 28. pontba új eset (g4): tanulói fiókkal adatexport-kérés. Rögzíteni kell, hogy a csomagban van-e nyers pont, és mi a site Data requests- és automatikus jóváhagyási beállítása.
>   - A HUM 17. szakaszban és a manifest :80 korlát-mondatában meg kell nevezni ezt az utat.
>   - EMBERI DÖNTÉS (DPO/jogi felelős + projektgazda): a „rejtés” release-feltétele a tanulói felületre vonatkozik-e, vagy minden hozzáférési útra, beleértve a GDPR szerinti adatkérést is.
>   - Tilos: az adatkérési utat DPO-döntés nélkül lezárni vagy korlátozni.
> - **Típus:** emberi-döntés
> - **Verdikt:**
>
> **QA20-IMPL-3**
> - **Súlyosság:** P2
> - **Bizalom:** magas
> - **Lencse:** implementáció
> - **Hely:** `a build-terv (scratchpad-vázlat)` §6, 1. pont; §3 táblája (tanuló-A1, A2, „Mire kell”); §5 (a)
> - **Probléma:** A szelet tesztlistája nem egyezik azzal, ami a szeletben ténylegesen megépül:
>   1. A RA 19 kimaradt, pedig az LMS-M1-05 (ASSIGN-M) javító beadása a szeletben van.
>   2. A RA 8 és a RA 29 futtathatónak van jelölve, de a szeletben nincs olyan activity, amelynek Grade-feltétele az LMS-M1-06-ra mutat. Az M1 downstreamje az M2 első leckéje („M1 megerősítve”) és az LMS-M3-05 („M1 complete”), egyik sincs a szeletben.
>   3. A 29. pont (b) és (d) esete QUIZ-M-et, LMS-M7-07-et és LMS-M3-06-ot nevez meg; ezek nincsenek a szeletben. Az (a) és az (f) esethez kell az X-16 három tétele, ezek pedig csak az 5. pont kiegészítésével épülnek meg.
>   4. Az 5. pont (a) útja csak a három Assignmentet építi meg. A 28. pont (k) esetéhez kellenek a GATE-CP-értékek is (LMS-M2-10, LMS-M4-10, LMS-M6-07), ezek kimaradtak.
> - **Bizonyíték:**
>   - buildplan §6: „A szeletben futtatható: RA 1, 6–9, 13–15, 17, 22–27, 29 és RT-A11Y; az X-16 tesztkiegészítéssel a 28. is.”
>   - RA :93 (19. pont): „az ASSIGN-M beadásoknál (éles kapu: M1, M3, M5, M6, M7) a javító beadás ugyanígy csak az F-peula után nyílik”.
> - **Hatás:**
>   - A TEST_OWNER a 8. és a 29. pontot célpont nélkül vehet futtatottnak, vagy célpontot rögtönöz.
>   - A 19. pont az M1-en kimarad.
>   - A 28. pont (k) esete nem értékelhető.
> - **Javaslat:**
>   - A §6-ba és a §3-ba fel kell venni a 19. pontot (az ASSIGN-M ágat).
>   - A 8. és a 29. pontot „részben futtatható” jelöléssel kell ellátni, a hiányzó elemek felsorolásával. Másik lehetőség: tesztcélú csonk-activity a szeletben, Grade-feltétellel az LMS-M1-06-ra (határ nélkül, illetve 50 %-os alsó határral), a környezeti rekordban rögzítve.
>   - Az 5. pont (a) útjába fel kell venni a három GATE-CP sort.
>   - Tilos: a manifest unlock-feltételeit és a RA-pontokat módosítani. Az 5. pontban a választás a projektgazdáé.
> - **Típus:** objektív
> - **Verdikt:**
>
> ---
>
> **Fájlonként:**
> - `02 Tervezet/Emberi jóváhagyás szükséges.md` (17. szakasz): QA20-IMPL-2. A szakasz egyezik a projektgazdai döntés szó szerinti szövegével: staging-jóváhagyás, „Szöveges értékelés” címke, „Show average” = No, rejtett „Course total”, nyitott release-kapu.
> - `02 Tervezet/LMS – activity manifest.md`: QA20-IMPL-1, QA20-IMPL-2 (:80). A forrásban beigazolódott:
>   - A két pontkönyv-függvény nem AJAX-hívás: `grade/report/user/db/services.php`, a `gradereport_user_get_grade_items` definíciója `'capabilities' => 'gradereport/user:view', 'services' => [MOODLE_OFFICIAL_MOBILE_SERVICE]`, `ajax` kulcs nélkül.
>   - A `mod_assign_get_submission_status` sem AJAX-hívás, és `mod/assign:view` jogot kér (`mod/assign/db/services.php`). Ezért a kurzusszintű `gradereport/user:view` tiltás ezt az utat nem zárja, a Grades nézetet viszont elveszi.
> - `02 Tervezet/LMS – H5P runtime acceptance.md`: QA20-IMPL-1 és QA20-IMPL-2 a (g2) esetre. A 29. ponthoz nincs bizonyított hiba.
> - `buildplan.md`: QA20-IMPL-3.
>   - A 13 activity, a sorrend (M0-01…06, M1-01, -02, -03, -07, -04, -05, -06), a profilok és az unlockok egyeznek a manifest §2-vel.
>   - Hitelesítő adat, kitalált dátum vagy kontaktérték nincs benne.
>   - A P1–P6 előfeltételek lefedik a kánonban hiányzó célkörnyezeti bemeneteket.
>
> **Nem ellenőriztem:**
> - A `mod_assign_get_submission_status` válaszának `feedback.grade` mezőjét (HUM 17., manifest :80). A `mod/assign/externallib.php` a fetch-eszközben a függvény előtt csonkolódott; csak a szolgáltatás-definíciót láttam.
> - A 29. pont (f) esetét (a grader report címkét mutat). Ezt nem olvastam vissza a forrásban; valószínű, hogy szerkesztési módban a gyors értékelés mezője számot mutat.
> - Azt, hogy a Grade-feltételek függetlenek-e a megjelenítéstől. Ezt ebben a körben nem olvastam újra (`availability/condition/grade`); a teszt-elvárásként írt mondat ellentmondást nem tartalmaz.
> - Azt, hogy az „Enable web services for mobile devices” = No a már kiadott tokeneket is érvényteleníti-e.
>
> Sources:
> - [grade/report/user/db/services.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/report/user/db/services.php)
> - [mod/assign/db/services.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/assign/db/services.php)
> - [lib/db/access.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lib/db/access.php)
> - [lib/external/classes/util.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lib/external/classes/util.php)
> - [mod/assign/classes/privacy/provider.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/assign/classes/privacy/provider.php)
> - [grade/report/overview/classes/external.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/report/overview/classes/external.php)
> - [MoodleDocs 405 – Capabilities/moodle/webservice:createmobiletoken](https://docs.moodle.org/405/en/Capabilities/moodle/webservice:createmobiletoken)
> - [MoodleDocs 405 – Data privacy](https://docs.moodle.org/405/en/Data_privacy)
