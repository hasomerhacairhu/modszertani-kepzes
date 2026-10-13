# Staging tesztfixture-terv és eltávolítási protokoll – QA-elemek, AP-2026-10-13-05

> **Audit trail, nem kánon; nem deployment.** Végrehajtási sorrend a zárt, szintetikus M0+M1 staging-szelet teszt-only
> QA-elemeihez. A normatív szabály a kánonban van: MAN §8 (azonosítók, beállítások, elkülönítés), RA 8, 28, 29 és 30
> (tesztlépések, érvényesség, eltávolítás), RR „Staging-szabály” 6., HUM 18. szakasz (projektgazdai döntés, 2026-10-13).
> Ütközésnél a kánon az irányadó. A deploymenthez a projektgazda külön engedélye és a P2–P6 környezeti bemenet kell
> (`2026-10-13 Staging build-terv – M0+M1 szintetikus szelet és X-16 tesztkiegészítés, AP-2026-10-13-04.md`, 0. pont);
> addig a Moodle-példányon semmi nem épül, és runtime-teszt nem jelölhető sikeresnek. Hitelesítő adat a repóba nem kerül.
> Rövidítések: MAN = `02 Tervezet/LMS – activity manifest.md`, RA = `02 Tervezet/LMS – H5P runtime acceptance.md`,
> RR = `02 Tervezet/RELEASE-READINESS.md`, HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`.

## 1. Build-sorrend (a deployment engedélye után)

1. A 13 kanonikus M0+M1 activity a build-terv 4. pontja szerint, változatlanul (MAN §2); `build_id ↔ cmid` a MAN §2-be.
2. A QA-szakasz a Z után: „QA – teszt-only (nem tanulói tartalom)” (MAN §8).
3. A hat X-16-másolat (QA-X16-M2-05, -M2-10, -M4-05, -M4-10, -M6-05, -M6-07) a modellsor minden beállításával, hozzáférési
   feltétel nélkül; a rubrika és a GATE-CP skála kézi út (MAN §5: MANUAL FALLBACK).
4. A két csonk (QA-STUB-M1-MEG, QA-STUB-M1-COMPL): Page, tartalom és saját completion nélkül; a hozzáférési feltétel kézi út
   (MAN §5: MANUAL FALLBACK), a MAN §8 táblázata szerint.
5. A nyolc QA-elem `test_id ↔ cmid` kötése a MAN §8 táblázatába (`BUILD_OUTPUT` helyére).
6. Visszaolvasás (`moodle_course_inspect`, `moodle_activity_inspect`, képernyőkép a feltételekről): a QA-elemek a
   QA-szakaszban vannak; a kurzusteljesítés kritériumai között egy sincs; a pontkönyvben külön kategória nélkül állnak; a
   kanonikus elemek beállítása nem változott.

## 2. Tesztfiókok és állapotok

| Fixture | Fiók (szintetikus) | Előállítandó állapot | Teszt |
|---|---|---|---|
| X-16-másolatok | szintenként egy-egy tanulói fiók (a build-terv 3. pontján felül), a mentor-A csoportjában (a modellsorok „Separate groups” módban futnak, a mentornak nincs `moodle/site:accessallgroups` joga: MAN §1, „Mentori csoportszűkítés”; mentoronként legfeljebb 8 tanuló) | LMS-M4-05-modell: 0, 1, 2; LMS-M2-05- és LMS-M6-05-modell: a legkisebb, egy közbülső és a legnagyobb összeg; mindegyikhez szöveges visszajelzés a kijelölt mentortól; a GATE-CP-másolatokon érték | RA 28 (a)–(k); RA 29 (a), (f) |
| kontroll a kurzus alapértelmezett megjelenítésével | ugyanazok a fiókok az LMS-M1-05-ön; ehhez végigjárják a teljes M0-t és az M1.1–M1.4-et, a szintetikus M1.A-tesztdátummal (build-terv 7. pont, X-17) | értékelt leadás; az LMS-M1-05 megjelenítése a site/kurzus alapértelmezése (a manifest nem rögzíti; Moodle-alapérték: Real, `admin/settings/grades.php`), a teszt idején visszaolvasva | RA 28 (j) |
| csonkok | tanuló-A1, tanuló-A2 | mindkettőnél előbb az M1 completion-elemei; utána az LMS-M1-06: érték nélkül → A1 „Még nem teljesítve” (LMS-M1-05: 0/1/2/2), A2 „Teljesítve” (minden sor ≥1, összpont ≥5/8) → A1 javítása „Teljesítve”-re | RA 8 (M1, állapotmátrix); RA 29 (d) |

Ha a célverzión az LMS-M1-05 nem „pont / max” alakot mutat, a RA 28 (j) kontrolljához nincs jóváhagyott QA-elem: a
hiányt a teszt-jegyzőkönyvben rögzíteni kell, és a kontroll módjáról a projektgazda dönt (újabb QA-elem csak az ő
döntésével készülhet).

## 3. Rögzítés

- A RA „Teszt-állapot” táblájában a QA-elemen kapott eredmény a Bizonyíték oszlopba kerül, „mechanizmus-bizonyíték
  (QA-elemen)” jelöléssel; az RT-P0-08, RT-P0-28 és RT-P0-29 sor ettől `IMPLEMENTATION_TEST_REQUIRED` marad (RA 30 (c),
  (d); RA „Teszt-állapot”).
- Minden bejegyzés: dátum, Moodle-verzió, `test_id` és `cmid`, a fiók szintetikus címkéje; képernyőkép személyes adat
  nélkül.
- A webszolgáltatás és a mobil-elérés staging-állapota a RA 28 (g), (g2) szerint rögzítendő; a site-szintű letiltás nem
  engedélyezett, és a cél-Moodle-ben nem bizonyított hatású jogosultsági korlátozás nem állítható be (HUM 18. és 19.
  szakasz, X-16-WS), ezért a staging a site meglévő beállításával fut.
- **Kiegészítés (AP-2026-10-13-06, HUM 19. szakasz, X-16-KANON):** a QA-X16 elemeken kapott RT-P0-28 és RT-P0-29 (a), (f)
  eredmény előzetes, mechanizmusszintű runtime-bizonyíték; az Állapot oszlop nem kap új értéket (RA „Teszt-állapot”).

## 4. Eltávolítás és a valódi lánc (RA 30)

Tanulói release előtt, és mielőtt a kurzus vagy annak másolata, mentése vagy importja pilot- vagy éles kurzussá válik:

1. A nyolc QA-elem és a QA-szakasz törlése.
2. Visszaolvasás: a kurzusban és a pontkönyvben nincs `QA-` azonosítójú elem; a kurzus lomtárában sincs QA-elem
   (véglegesen törölve vagy a lomtár kiürítve; a lomtár állapotát rögzíteni kell); a kurzusteljesítés kritériumai a MAN §4
   szerintiek; a kanonikus elemek beállítása nem változott.
3. A MAN §8 táblázatában a `cmid` mellé a törlés dátuma kerül (a sor a nyilvántartásban marad).
4. A valódi előfeltétel-lánc külön teszt (RA 30 (b)): a RA 8 M1-sora az LMS-M2-01 és az LMS-M3-05 célponttal, a RA 29 (d)
   a kanonikus Grade-feltételes elemeken; a kanonikus LMS-M2-05, LMS-M4-05, LMS-M6-05 és GATE-CP soruk beállításainak
   visszaolvasása, a QA-másolattal egyezően. Ehhez a staging-build az érintett M2–M6 sorokkal bővül; ez külön build-lépés, a
   projektgazda deployment-engedélyével.
5. Az RT-P0-30 sor a törlés, a visszaolvasás (lomtárral) és a 4. lépés lánc-tesztjének bizonyítékával. Az RT-P0-08 és az
   RT-P0-29 (d) esete csak a 4. lépés után állítható `RUNTIME_VERIFIED`-re; az RT-P0-28-nál és az RT-P0-29 (a), (f) esetnél
   nyitott projektgazdai döntés, hogy a QA-másolat eredménye a kanonikus beállítások visszaolvasásával elegendő-e (RA 30 (c)).
   **Eldöntve (AP-2026-10-13-06, HUM 19. szakasz, X-16-KANON):** a teljes megismétlés nem kell; a kanonikus elemeken
   célzott visszaellenőrzés kell, a RA 30 (d) öt feltételével (a beállítások egyezése dokumentált eltérésekkel; tanulói
   fiókkal a három kanonikus Assignmenten a rejtés, a szöveges rubrikaszint és a mentori komment; változatlan értékelői
   munkafolyamat, GATE-CP, rubrikapontok, completion és kapuküszöbök; a RA 29 (a), (f) kanonikus eredménye; a nyitott
   API-, mobil- és adatvédelmi kapuk valós bizonyíték szerinti kezelése).

## 5. Célzott QA (QA21, implementáció) és feldolgozása

A diffre (HUM 18. szakasz, manifest §8 és kapcsolódó sorok, RA 8, 28–30, RR Staging-szabály 6., a build-terv
döntés-jegyzetei) és e terv vázlatára futott, read-only. A fő session a Moodle 4.5 (`MOODLE_405_STABLE`) forrásában
ellenőrizte a lomtár alapértékeit (`admin/tool/recyclebin/settings.php`: `coursebinenable` = 1, `coursebinexpiry` =
`WEEKSECS`).

| ID | Feldolgozás |
|---|---|
| QA21-IMPL-1 | a RA 30 (b)–(c) javítva: a valódi lánc a 8. pont M1-sora és a 29. (d) (a „valódi unlock-szabályokkal” kitétel a 28. pontnál kikerült, mert az nem nyitást mér); a kanonikus X-16-elemek beállításai visszaolvasandók. Emberi döntés (projektgazda): elég-e az RT-P0-28-hoz és az RT-P0-29 (a), (f) esetéhez a QA-másolat eredménye a kanonikus beállítások visszaolvasásával; addig ezek nem állíthatók `RUNTIME_VERIFIED`-re (HUM 18. szakasz, X-16-TESZT sor) |
| QA21-IMPL-2 | javítva: RA 30 (a) és e terv 4. pontja a kurzus lomtárát is visszaolvassa |
| QA21-IMPL-3 | javítva: a manifest §8 „Szakasz” pontja a csonkok teljes feltételét nevezi meg |
| QA21-IMPL-4 | javítva e tervben: csoport (mentor-A), a kontrollfiókok M0+M1 útja, az LMS-M1-05 megjelenítése a kurzus alapértelmezése, az RT-P0-30 bizonyítéka a lánc-teszttel |
| QA21-IMPL-5 | emberi döntés (projektgazda, a DPO-csomag előtt): az X-16-PRIV javaslat „numerikus értékelés” kifejezése csak a három X-16 Assignment pontszámára vonatkozik-e, vagy a kvízpontszámra is (az utóbbi az ERT-5 szerinti Review options-szal ütközne); a PROPOSED szöveg nem változott |
| QA21-IMPL-6 | javítva: a HUM 18. szakasz X-16-TESZT sora a 29. pont (a), (f) esetét és az RT-P0-29-et is megnevezi |

### A. melléklet – a QA21 nyers kimenete

> QA21-IMPL: célzott implementációs QA a diffre (AP-2026-10-13-05), read-only. 6 finding, mind P2: 4 objektív, 2 emberi-döntés. Moodle-forrás: a moodle/moodle `MOODLE_405_STABLE` ága és a MoodleDocs 405.
>
> **QA21-IMPL-1**
> - **Súlyosság:** P2
> - **Bizalom:** közepes
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:117` (30. pont, (b) és (c)); `:115` (28. pont, „a sor `RUNTIME_VERIFIED`-re csak a 30. pont szerint állítható”); a fixture-terv §4, 4. lépés
> - **Probléma:** A projektgazda a „csak az adott mechanizmust igazolja” korlátot a két csonkra mondta ki. A RA 30 (b)–(c) ezt kiterjeszti az X-16-másolatokra is: az RT-P0-28 csak akkor lehet `RUNTIME_VERIFIED`, ha a 28. pont a kanonikus elemeken „a valódi unlock-szabályokkal” újra lefut. Ez a feltétel sem a projektgazda szövegében, sem a HUM 17. szakaszban nem szerepel. Ráadásul ellentmond annak az indoklásnak, amellyel az (a) változatot elfogadták.
> - **Bizonyíték:** RA:117: „a 28. pont a kanonikus LMS-M2-05, LMS-M4-05, LMS-M6-05 elemen és GATE-CP sorukon, a valódi unlock-szabályokkal”. Build-terv §5: „Javaslat: (a), mert az RT-P0-28 a tanulói megjelenítést méri, nem a nyitást”.
> - **Hatás:** A projektgazda azért választotta az (a)-t, hogy elkerülje a „lényegesen nagyobb build”-et. A RA 30 és a fixture §4.4 szerint viszont az RT-P0-28 csak egy M2–M6-tal bővített buildön zárható. A QA-másolaton futó 28. pont így soha nem zárja az RT-P0-28-at. Erről a terjedelmi következményről a projektgazda nem döntött.
> - **Javaslat:** EMBERI DÖNTÉS (projektgazda, a TEST_OWNER bevonásával): az RT-P0-28-hoz elég-e a QA-másolaton kapott eredmény és a kanonikus elemek beállításainak visszaolvasása, vagy a teljes 28. pontot meg kell ismételni a kanonikus elemeken. Ha megismétlés kell, a (b) mondja meg, hogy a 28. pont ott a megjelenítést méri; a „valódi unlock-szabályokkal” kitétel félrevezető, mert a 28. pont nyitást nem mér. Amíg nincs döntés, a RA 30 (c) kapuja nem gyengíthető. Tilos módosítani: a RA 8 M1-sorára és a 29. (d)-re vonatkozó csonk-korlátot, a rubrikát, a GATE-CP-szemantikát és az unlockot.
> - **Típus:** emberi-döntés
> - **Verdikt:**
>
> **QA21-IMPL-2**
> - **Súlyosság:** P2
> - **Bizalom:** közepes
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:117` (30. pont (a)); a fixture-terv §4, 1–2. lépés
> - **Probléma:** Az eltávolítás visszaolvasása csak a kurzust és a pontkönyvet nézi. A Moodle kurzusszintű lomtára alapból be van kapcsolva, és a törölt activityt egy hétig visszaállíthatóan őrzi; ezt a visszaolvasás nem ellenőrzi.
> - **Bizonyíték:** RA:117: „visszaolvasás: a kurzusban és a pontkönyvben nincs `QA-` azonosítójú elem”. MoodleDocs 405, Recycle bin: „click the 'restore' icon to retrieve the assignment or other item you accidentally deleted” és „automatically permanently deleted after seven days (or a time specified by the admin.)”. `admin/tool/recyclebin/settings.php`: `'tool_recyclebin/coursebinenable'` alapértéke `1`, a `coursebinexpiry` alapértéke `WEEKSECS`.
> - **Hatás:** Ha a kurzus a megőrzési időn belül pilot-kurzussá válik, egy tanár a QA-elemeket a szintetikus pontokkal együtt visszaállíthatja. A RA 30 (a) visszaolvasása ettől még átmegy.
> - **Javaslat:** A RA 30 (a) visszaolvasása és a fixture §4 2. lépése egészüljön ki: a kurzus lomtárában nincs QA-elem (véglegesen törölve vagy kiürítve), és a lomtár állapotát rögzíteni kell. Tilos: site-beállítás módosítását előírni, és a RA 30 többi részéhez nyúlni.
> - **Típus:** objektív
> - **Verdikt:**
>
> **QA21-IMPL-3**
> - **Súlyosság:** P2
> - **Bizalom:** magas
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/LMS – activity manifest.md:315` (§8, „Szakasz” bullet), összevetve a `:338–339` csonk-sorokkal
> - **Probléma:** A szabály szerint a QA-elem „csak az LMS-M1-06 értékét olvassa”. Ugyanennek a szakasznak a táblázata szerint viszont a csonkok hat M1-activity completion-állapotát is feltételként olvassák.
> - **Bizonyíték:** :315: „a QA-elem rájuk nem hat, csak az LMS-M1-06 értékét olvassa.” :338: „az M1 completion-elemeinek (LMS-M1-01, LMS-M1-02, LMS-M1-03, LMS-M1-07, LMS-M1-04; LMS-M1-05 leadva) Activity completion-feltételei **és** Grade-feltétel”.
> - **Hatás:** Ha a fejlesztő a prózát követi, csak a Grade-feltételt állítja be. Ilyenkor a csonk nem a §4 „Mx megerősítve” / „Mx complete” konjunkcióját modellezi, és a RA 8 M1-sora hiányos feltétellel fut.
> - **Javaslat:** A mondat így szóljon: „…csak az M1 completion-elemeinek completion-állapotát és az LMS-M1-06 értékét olvassa (a táblázat Hozzáférés oszlopa szerint)”. Tilos: a táblázathoz és a feltételekhez nyúlni.
> - **Típus:** objektív
> - **Verdikt:**
>
> **QA21-IMPL-4**
> - **Súlyosság:** P2
> - **Bizalom:** magas ((i), (ii), (iv)); közepes ((iii))
> - **Lencse:** implementáció
> - **Hely:** a fixture-terv §2 táblázat („X-16-másolatok” és „kontroll” sor); §4, 5. lépés
> - **Probléma:** A fixture-tervből négy dolog hiányzik vagy pontatlan:
>   - (i) Az X-16 tesztfiókoknak nincs csoportjuk. A modellsorok „Separate groups” módban futnak, a mentornak nincs `moodle/site:accessallgroups` joga, így a kijelölt mentor nem tudja őket értékelni.
>   - (ii) A RA 28 (j) kontrollja szerint „ugyanaz a tanulói fiók” lát „pont / max” alakot. Ehhez az X-16 fiókoknak az LMS-M1-05-be is be kell adniuk, vagyis végig kell járniuk a teljes M0-t és az M1.1–M1.4-et, a szintetikus M1.A-dátummal együtt (X-17). A terv ezt nem mondja ki.
>   - (iii) A „(kanonikus, „Real” megjelenítés)” nem manifest-érték. A manifest az LMS-M1-05 megjelenítési típusát nem rögzíti, így a site/kurzus alapértéke érvényes. Ez a Moodle-ban alapból Real (`admin/settings/grades.php`: `'grade_displaytype'` … `GRADE_DISPLAY_TYPE_REAL`), de a site felülírhatja.
>   - (iv) A §4 5. lépése az RT-P0-30 bizonyítékából kihagyja a valódi lánc (b) tesztjét, pedig az a 30. pont része.
> - **Bizonyíték:** fixture: „| X-16-másolatok | szintenként egy-egy tanulói fiók (a build-terv 3. pontján felül) |” és „ugyanazok a fiókok az LMS-M1-05-ön (kanonikus, „Real” megjelenítés)”. MAN:32: „a mentor a nem szerkesztő tanári szerepet csak a mentor-csoportjába sorolás után kapja, `moodle/site:accessallgroups` nélkül”.
> - **Hatás:** A RA 28 előkészítése (mentori rubrikás értékelés) és a (j) kontroll a terv alapján nem hajtható végre. A TEST_OWNER rögtönözni kényszerül, például szerkesztő tanárral értékel a kijelölt mentor helyett.
> - **Javaslat:**
>   - Az X-16 fiókok csoportját meg kell adni (a mentor-A csoportja, mentoronként legfeljebb 8 tanuló).
>   - A kontrollfiókoknál ki kell mondani az M0+M1 utat.
>   - A „Real” helyére: „a site/kurzus alapértelmezett megjelenítése (Moodle-alapérték: Real), a teszt idején visszaolvasva”.
>   - Az RT-P0-30 bizonyítéka: törlés, visszaolvasás és a (b) lánc-teszt.
>   - Tilos: új QA-elemet felvenni, a RA 28 (j)-hez és a kánonhoz nyúlni.
> - **Típus:** objektív
> - **Verdikt:**
>
> **QA21-IMPL-5**
> - **Súlyosság:** P2
> - **Bizalom:** közepes
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:885` (X-16-PRIV); `02 Tervezet/LMS – activity manifest.md:81` (LMS-M4-05, PROPOSED mondat); összevetve: manifest `:19` (QUIZ-M, ERT-5) és RA `:116` (29. (b))
> - **Probléma:** A PROPOSED X-16-PRIV hatóköre nem egyértelmű. Az X-16 kontextusában a „numerikus értékelés” a három rubrikás Assignment pontszáma, ez azonban Quiz-felületen nem jelenik meg. Szó szerint olvasva a javaslat a kvízpontszámot is rejtené, ami ütközik a lezárt ERT-5-tel és a 29. (b) regressziós elvárásával.
> - **Bizonyíték:** HUM:885: „A numerikus értékelés ne jelenjen meg a normál tanulói Assignment-, Grades-, Quiz- vagy mobilos tanulási felületen.” MAN:19: „az első próbálkozás után a pontszám és a hibázott kompetencia / kritikus követelmény”.
> - **Hatás:** Ha a DPO és a jogi felelős a javaslatot szó szerint fogadja el, a release-feltétel vagy a QUIZ-M Review options lezárt beállításával ütközik, vagy vitatható marad, mire vonatkozik. Adatvédelmi tétel, ezért emberi döntésként jelentem.
> - **Javaslat:** EMBERI DÖNTÉS (projektgazda, mielőtt a csomag a DPO-hoz és a jogi felelőshöz megy): a „numerikus értékelés” csak a három X-16 Assignment pontszámára vonatkozik-e (Assignment-, Grades- és mobilos felület), vagy a kvízpontszámra is. Tilos: a PROPOSED szó szerinti szövegét átírni, és az ERT-5-höz nyúlni.
> - **Típus:** emberi-döntés
> - **Verdikt:**
>
> **QA21-IMPL-6**
> - **Súlyosság:** P2
> - **Bizalom:** magas
> - **Lencse:** implementáció
> - **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:882` (X-16-TESZT sor, „Érintett hely” és „Nyitva marad” oszlop)
> - **Probléma:** Az X-16-másolatokon a RA 29 (a) és (f) esete is fut, a RA 30 (c) az RT-P0-29-et is ehhez köti. A sor kereszthivatkozásai mégis csak a 28. és a 30. pontot, illetve az RT-P0-28-at és az RT-P0-30-at nevezik meg.
> - **Bizonyíték:** HUM:882: „| manifest §8; runtime acceptance 28., 30. pont | a runtime-teszt (RT-P0-28, RT-P0-30). |”. RA:116: „A zárt M0+M1 szeletben az (a) és az (f) eset a manifest §8 X-16-másolataival … futtatható”.
> - **Hatás:** Kis hatású: aki a döntési nyilvántartásból indul, nem látja, hogy a 29. pont (a) és (f) esete is ettől a döntéstől függ.
> - **Javaslat:** Az „Érintett hely” oszlopba: „29. pont (a), (f)”; a „Nyitva marad” oszlopba: RT-P0-29. Tilos: a döntésszöveg oszlopához nyúlni.
> - **Típus:** objektív
> - **Verdikt:**
>
> ---
>
> **A feladat öt kérdésére röviden:**
>
> 1. **A döntés átvezetése** (a projektgazda szövegével és a manifesttel összevetve):
>    - (a) A hat modellsor és a profilok egyeznek a manifest §2-vel: ASSIGN-S/GATE-CP az M2-nél és az M4-nél, ASSIGN-M/GATE-CP az M6-nál. A rubrika, a pontozás, a szintek, a GATE-CP és az unlock változatlan.
>    - (b) A csonkok határai megfelelnek a §4-nek: az „M1 megerősítve” határ nélküli, az „M1 complete” alsó határa 50 %. Az M1 completion-elemei is egyeznek (a TEXT-C LMS-M1-07-tel együtt, a §2 bevezetője szerint). A negatív és a pozitív állapot előállítható.
>    - (c) Mind az öt elkülönítési pont szerepel.
>    - (d) Az X-16-PRIV mindenhol PROPOSED és nyitott; a HUM-sor szó szerint egyezik a projektgazda szövegével.
>    - (e) A mobil-webszolgáltatás letiltása mindenhol „nincs jóváhagyva”.
> 2. **Gépi következmény:** a `BUILD_OUTPUT_ROW` a `QA-` sorokat nem számolja, és ez helyes, mert a QA-elem nem tanulói release-elem. Az RT-P0-30 sort a `RUNTIME_TEST_OPEN_ROW` illeszti, ezért a tanulói verdiktet blokkolja, a buildet nem. Ez megfelel a szándéknak. Más parser (`RUNTIME_OUTPUT_ROW`, `BUILD_SPEC_OPEN_ROW`, HUM-fejléc) nem akad meg a §8 táblán vagy az új soron. A látható szöveg pinjei a négy fájlra a szokásos `--pin-visible` lépést igénylik.
> 3. **Moodle-tények:**
>    - `availability/condition/grade/classes/condition.php`: „(($record->finalgrade - $record->rawgrademin) * 100) / ($record->rawgrademax - $record->rawgrademin)”. A Grade-feltétel tehát a nyers értékből számol, a „Letter” megjelenítéstől és a rejtett összesítőtől függetlenül; a csonkok és a 29. (d)/(e) elvárás ezzel összhangban van.
>    - `grade/report/user/classes/report/user.php`: a nem rejtett kategória összesítő sora a tanulónak megjelenik, a saját megjelenítési típusával formázva (`grade_format_gradevalue($gradeval, $gradegrade->grade_item, true)`), ez alapból Real. A §8 kategóriatilalma tehát megalapozott. A §8 ezt a tényt egyébként nem állítja, az indoklása a „valódi elrendezés”; ez nem téves és nem túlzó.
> 4. **RA 30 (c) és RA 28:** a HUM 17. szakasszal nincs közvetlen ellentmondás, mert az nem mondja meg, melyik elemen fut a teszt. A projektgazda szövegén és az (a) elfogadott indoklásán viszont túlmegy: lásd QA21-IMPL-1.
> 5. **Fixture-terv:** kitalált adat, dátum, kontakt vagy hitelesítő adat nincs benne. A (j) kontroll csak feltételesen megalapozott: lásd QA21-IMPL-4 (iii), a fallback-mondat ezt részben kezeli.
>
> **Fájlonként, ahol nincs bizonyított hiba:**
> - `02 Tervezet/RELEASE-READINESS.md` (Staging-szabály 6., a „Legkisebb értelmes staging-szelet” mondata): nincs bizonyított hiba.
> - A build-terv auditfájl (5–7. pont döntés-jegyzetei): nincs bizonyított hiba.
> - A HUM 17. szakasz módosított mondata: nincs bizonyított hiba.
>
> **Nem ellenőriztem:**
> - Hogy a modul törlése a célverzión háttérfeladatként (cron) fut-e, és így időzíti-e a pontkönyv visszaolvasását.
> - Hogy a „rejtett staging-kurzusba” a tanulói tesztfiókok beléphetnek-e. Ez a diff előtti kérdés, nem ennek a változtatásnak a következménye.
>
> Érintett fájlok:
> - 02 Tervezet/LMS – H5P runtime acceptance.md
> - 02 Tervezet/LMS – activity manifest.md
> - 02 Tervezet/Emberi jóváhagyás szükséges.md
> - a fixture-terv (scratchpad-vázlat)
>
> Sources:
> - [availability/condition/grade/classes/condition.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/availability/condition/grade/classes/condition.php)
> - [grade/report/user/classes/report/user.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/report/user/classes/report/user.php)
> - [admin/settings/grades.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/admin/settings/grades.php)
> - [admin/tool/recyclebin/settings.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/admin/tool/recyclebin/settings.php)
> - [MoodleDocs 405 – Recycle bin](https://docs.moodle.org/405/en/Recycle_bin)
