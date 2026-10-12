# 2026-10-12 Célzott QA – M5 átvezetés (aadf41b), AP-2026-10-12-01

- **Állapot:** NYERS — verifikáció folyamatban.
- **Review-bázis:** `aadf41b`.

## C. Nyers lencse-kimenetek (szó szerint)

<!-- agent a89967d37b076e65f -->

## M5:QA-BIZT, célzott QA (biztonság-jog lencse), aadf41b, AP-2026-10-12-01

Három findingot találtam. A GYV-7 két lépcsője és a passz, a GYV-6, a PRG-5, az ADV-1, az ADV-7, az ADV-8, az ADV-10 és a PRG-13 a döntés szövegét követi. Nem gyengült és nem tűnt el védelem, és a modulon belül nem maradt ellentmondó régi mondat. Az ERT-28 22–24. blokkja szándékosan maradt ki, ez nem az én lencsém.

---

**M5:QA-BIZT-1**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md:56`
  - ugyanez a fájl, `:401`
- **Probléma:** az ADV-11 a személyes munkapéldányt tiltja a közös eszközön. Az átvezetés csak azt tiltja, hogy rajta maradjon. Ez a csomag (b) opciója („munkapéldány engedélyezett, kötelező törlési lépéssel”), vagyis gyengébb a döntésnél.
- **Bizonyíték:**
  - A fájlban: „jelszót nem ment, személyes munkapéldányt nem hagy rajta, a letöltött fájlokat törli”, illetve a `:401` sorban „munkapéldányt nem hagy rajta, a letöltéseit törli”.
  - A HUM 14., ADV-11 sorában: „jelszómentés és személyes munkapéldány tilos; kijelentkezés, munkamenet-ellenőrzés, letöltési törlés”.
- **Hatás:** az F-peulán a résztvevő a közös eszközön is letöltheti és szerkesztheti a visszaküldött M5.4 táblázatát, holott a döntés ezt nem engedi.
- **Javaslat:**
  - `:56` OLD „személyes munkapéldányt nem hagy rajta” → NEW „személyes munkapéldányt nem készít rajta”.
  - `:401` OLD „munkapéldányt nem hagy rajta” → NEW „munkapéldányt nem készít rajta”.
  - A letöltések törlése, a kijelentkezés, a munkamenet ellenőrzése, valamint a papír és a saját eszköz lehetősége maradjon.
  - Megjegyzés a fő sessionnek, scope-on kívül: az M0.A:604 („hagyni tilos”) és az M4.F:52 („se maradjon rajta”) ugyanígy olvassa a döntést.
  - Ha a fő session a „tilos” szót „nem maradhat rajta” értelemben olvassa, akkor ez EMBERI DÖNTÉS: az LMS-gazda és a DPO mondja meg, hogy az ADV-11 a munkapéldány elkészítését vagy csak a rajta hagyását tiltja-e.
- **Típus:** objektív

**M5:QA-BIZT-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md:293` (R2, Erős szint), összevetve a `:283` sorba most bekerült ADV-9 adatmondattal.
- **Probléma:**
  - Az átvezetési terv lezártként kezeli, hogy az R2 Erős példája („néhányan visszahúzódók”) „általános hangulat”, ezért nem változik. A döntési csomag ezt a kérdést kifejezetten DPO-ítéletnek jelölte.
  - Az Erős szint ráadásul „a módszerválasztást érdemben befolyásoló részlet” megadását jutalmazza. Ez a kis csoporton belüli alcsoportra vonatkozó részlet felé terel, miközben az új szabály csak csoportszintű információt enged.
- **Bizonyíték:**
  - KAPU:293: „Kor + hangulat + a módszerválasztást **érdemben befolyásoló** részlet: „11–12, péntek délután fáradtak, néhányan visszahúzódók””.
  - Döntési csomag, ADV-9: „Belefér-e a csoportszintbe a „nevesített korosztály/élethelyzet” és a „néhányan visszahúzódók”?”, illetve „Hogy a „nevesített korosztály/élethelyzet” csoportszintű-e, az DPO-ítélet.”
- **Hatás:** a rubrika legmagasabb szintje épp azt a részletezést jutalmazhatja, amelyet az ADV-9 („kis csoportban az egyedi élethelyzet is visszaazonosítható lehet”) korlátoz. Az `M5:BIZT-G1-5` → FIXED állapot ezt a részt hallgatólagosan lezárja.
- **Javaslat:**
  - EMBERI DÖNTÉS a DPO-nak és a programvezetőnek (az ADV-9 QA-szerepei): belefér-e a csoportszintű szabályba az R2 Erős szintjének „érdemben befolyásoló részlet” követelménye és a „néhányan visszahúzódók” példa.
  - Bizonyíték: KAPU:293 és :283, valamint a csomag ADV-9 kérdése.
  - Addig a rubrikaszöveg nem változik (rubrikaszint-invariáns). A ledgerben ez a rész nyitott QA-tételként szerepeljen, ne FIXED-ként.
- **Típus:** emberi-döntés

**M5:QA-BIZT-3**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M5/Online leckék/M5.2 – Feladat → módszer döntési fa – Mit választok először.md:317` (GYV-7, GYV-2)
  - `02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md:20` (PRG-5, a kiskorúval kettesben szóló kitétel) és `:89` (GYV-6)
  - az ADV-1, -7, -8, -9, -10 és -11 helyei az M5.4-ben, az M5.A-ban és az M5.F-ben
- **Probléma:** az átvezetett gyermekvédelmi és adatvédelmi döntésekhez hiányzik a megnevezett szerepek írásos QA-bizonyítéka:
  - Memuna és programvezető: GYV-6, GYV-7, valamint a PRG-5 kiskorúval kettesben szóló kitétele;
  - DPO, illetve jogi felelős: az ADV-sorok.
  - A GYV-7 a csomag szerint az M5 learner release-ét blokkolja.
- **Bizonyíték:**
  - Döntési csomag, GYV-7: „**Mit blokkol:** az M5 learner release-ét (P1)”.
  - HUM 14., GYV-7, a QA-oszlop: „Memuna (HUM-SAFE-01/03); az M5-nél a programvezetővel.”
- **Hatás:** ha az IMPLEMENTED állapotból Memuna- vagy DPO-jóváhagyásra következtetünk, az M5 hamis release-készséggel kerülhet tovább.
- **Javaslat:**
  - A tananyag nem változik.
  - A G1 kaput (Memuna és programvezető: GYV-6, GYV-7, PRG-5) és a G2 kaput (DPO, illetve jogi felelős: ADV-1, -7, -8, -9, -10, -11) bizonyíték-kapuként kell rögzíteni a `RELEASE-READINESS.md`-ben és a tracker-issue-ban.
  - A ledger a tételt IMPLEMENTED, de FINAL_RELEASE_QA szempontból nyitott állapotban vezesse.
- **Típus:** bizonyíték-kapu

Átnéztem és nem jelentek findingot:
- **GYV-6:** a GK §4 védelmi minimumát szó szerint vezeti át.
- **GYV-7:** a kétlépcsős küszöb a csomag (a) opciója szerinti; a passz és a „madrih, nem terapeuta” határ megmaradt; a Memuna első előfordulásának formulája a GK §4.1 szerinti.
- **PRG-5:** a döntés szövegét követi. A 1–5 fős változat PRG4-ként külön nyilvántartott.
- **ADV-1:** a mondat egyezik az M4-es mintával.
- **ADV-7:** a felvétel nélküli részvételi út megmaradt.
- **ADV-8:** a „név nélküli” gyűjtést mindhárom helyen, és az asset notes mezőjében is, a „ténylegesen senkihez sem köthető” feltételhez köti; létszámküszöb nem került be.
- **ADV-10:** a Google-sablon mindkét helyen feltételes.
- **PRG-13:** a mozgás nélküli részvétel és a passz bekerült.
- **PRG-10:** a zárókör-mondatok átvezetése rendben van.

<!-- agent a4713a97fe535f98c -->

## M5 célzott QA: értékelés és LMS (aadf41b, HUM 14. szakasz)

Hat finding van, ebből 1 P1 és 5 P2.

---

**M5:QA-ERT-1**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – Nonformális nevelés, módszerválasztás & tanulástan.md:35` ↔ `02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md:286, :294`
- **Probléma:** Az ERT-26 második mondata („Soronként legyen látható módszertani indok”) csak a HUB 4. kompetenciájába került be. A KAPU kapuszabályába nem került be, és a rubrika soronkénti indokot csak az Erős szinten kér, átmenő szinten nem.
- **Bizonyíték:** HUB:35 „amelyben minden sorban látható a módszertani indok”. KAPU:294 R3 Alapszint: „A módszer **megfelel** a célnak és a kvucának”, Erős: „Az illeszkedés **indokolt is**: 1 mondatban kiderül, *miért*”.
- **Hatás:** A kimondott cél (minden sorban indok) a kapun mérés nélkül marad. Az értékelők sem egyformán döntenek: van, aki átmenéshez is explicit indokot kér (ez valójában az Erős szint), van, aki nem.
- **Javaslat:** EMBERI DÖNTÉS: a „soronként látható módszertani indok” rubrikaszintre fordítása. Két lehetőség van: az R3 Alapszint („megfelel”) elég, vagy az Erős szint „indokolt is” leírója kell. Ezt az értékelési felelős és a projektgazda dönti el, a QA a módszertani lektoré; ez a döntés saját „Értékelési kalibráció” kitétele, magát a döntést nem nyitja újra. Utána a KAPU:286 szó szerint átveheti a döntés mondatát. Addig nem változhat: az R1–R4 szintleírók, a ≥ Alapszint küszöb és az R4 kritikus státusza.
- **Típus:** emberi-döntés · **Verdikt:** —

**M5:QA-ERT-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** HUB:186; KAPU:305
- **Probléma:** Az ERT-26 a kapuszabályt a HUB:176, :211 és a KAPU:26, :288 helyen „rubrikasor”-ra írta át. A HUB:186 és a KAPU:305 viszont maradt „minden sor ≥ Alapszint”. A HUB:186-ban a mondat alanya a táblázat, így könnyen táblázatsornak olvasható, pedig a döntés éppen ezt az olvasatot zárja ki.
- **Bizonyíték:** HUB:186 „táblázat** eléri a KAPU-rubrika küszöbét: **minden sor ≥ Alapszint”. KAPU:305 „A „minden sor ≥ Alapszint, az R4 kritikus” feltételt”. Ugyanez a fájl, KAPU:288: „„Teljesítve” = MINDEN rubrikasor ≥ Alapszint”.
- **Hatás:** Ugyanabban a modulban két olvasat él a kapuegységről (rubrikasor vagy táblázatsor). Az értékelő a táblázatsoronkénti mikropontozáshoz térhet vissza.
- **Javaslat:** HUB:186 „**minden sor ≥ Alapszint, az R4” → „**minden rubrikasor ≥ Alapszint, az R4”. KAPU:305 „„minden sor ≥ Alapszint, az R4 kritikus”” → „„minden rubrikasor ≥ Alapszint, az R4 kritikus””. A küszöb és a szintek nem változnak. A KAPU:305 idézete a manifestet követi, ezért a MAN:83/:86 sorral együtt kell átírni (lásd lent).
- **Típus:** objektív · **Verdikt:** —

**M5:QA-ERT-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** HUB:181; KAPU:26
- **Probléma:** A PRG-7 a HUB:208-at támogató, nem kötelező mentori ajánlásra szűkítette. A HUB:181 és a KAPU:26 viszont továbbra is azt írja, hogy a küszöb alatti madrih „felzárkóztató hurokba kerül”. A modulban ez a hurok sehol nincs definiálva, és automatikus besorolást sugall.
- **Bizonyíték:** HUB:181 „aki alatta van, **nem bukik**, hanem felzárkóztató hurokba kerül (a kvíz item-szintű analitikája alapján célzott visszairányítás)”. HUB:208 „az eredményből a mentor támogató, nem kötelező beavatkozási ajánlást kap”.
- **Hatás:** Ugyanaz a hub egyszer automatikus hurkot, egyszer nem kötelező ajánlást ígér. A PRG-7 éppen az olyan ígéretet zárja ki, amely mögött nincs végrehajtó.
- **Javaslat:**
  - HUB:181: „hanem felzárkóztató hurokba kerül (a kvíz item-szintű analitikája alapján célzott visszairányítás).” → „hanem a kvíz kérdésszintű visszajelzése visszairányítja a megfelelő leckéhez, a mentor pedig támogató, nem kötelező beavatkozási ajánlást kap.”
  - KAPU:26: ugyanígy, a KAPU:24 „visszairányítás a hibás itemekhez” mintájára, „(PRG-7)” jelöléssel.
  - Nem változik: a ≥80% küszöb, a formatív státusz és a „nem bukik”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-ERT-4**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M5/Online leckék/M5.2 – Feladat → módszer döntési fa – Mit választok először.md:9`
- **Probléma:** Az ERT-1 kivette a HUB §6-ból az „érdemi kitöltéssel” fordulatot. Az M5.2 completion-sora viszont még mindig ezzel a fordulattal hivatkozik a HUB §6-ra, így a hivatkozott szöveg már nincs ott.
- **Bizonyíték:** M5.2:9 „**Completion (lecke):** érdemi kitöltéssel (M5 hub §6): egy választott ág (A–D) végigvitele”. HUB:185 „activity completion a manifest profilja szerint – … az M5.2-nél egy ág végigvitele a végképernyőig”.
- **Hatás:** A lecke a hubbal ellentétes, régi completion-elvet tulajdonít a hubnak. Ez a build-spec olvasóját félrevezeti.
- **Javaslat:** „érdemi kitöltéssel (M5 hub §6): egy választott ág” → „a manifest profilja szerint (M5 hub §6): egy választott ág”. A sor többi része (BSPEC-05, végképernyő, „Receive a grade”) nem változik.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-ERT-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrihként.md:183` (SLIDE 3, a True/False visszajelzése)
- **Probléma:** A visszajelzés szerint mind a négy mezőt ki kell tölteni. Mivel ugyanez a dia a tanulástant „a 4. mező”-nek hívja, ez úgy olvasható, hogy tanulástan-elem minden sorba kell. Ez ellentmond az ERT-26-nak („nem feltétlenül kell minden sorba”) és a dia saját 4. pontjának.
- **Bizonyíték:** M5.4:183 „Ezért kell mind a négy mezőt kitölteni.” ↔ M5.4:164 „Legalább 1 sorban – de jó, ha minél többben – … és ott a 4. mező konkrét cselekvést ír le”.
- **Hatás:** A tanuló szigorúbb szabályt tanul, mint amit a kapu mér. Ugyanazon a dián két ellentétes elvárást kap.
- **Javaslat:** „Ezért kell mind a négy mezőt kitölteni.” → „Ezért kell minden sorban kitölteni a feladat / cél, a kvuca és a módszer mezőjét is.” A ✅ (Igaz) és a kérdés nem változik; kulcsközeli szöveg, QA: értékelési felelős. Ha a szerző a négy láncelemre gondolt, a javítás akkor is csak egyértelműsít.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-IMPL-1**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** M5.4:250, :252, :254, :256 (SLIDE 6)
- **Probléma:** Az ERT-29/ADV-4 szerint a dia beviteli elem nélküli lett, de a ✅ helyére ☐ került. A ☐ így kattinthatatlan jelölőnégyzetnek látszik. A tananyagban sehol máshol nincs ☐.
- **Bizonyíték:** M5.4:247 „Interakció: pontozatlan önellenőrzés, beviteli elem nélkül”. M5.4:250 „– ☐ Igaz rám / ☐ Még nem, de pótolni fogom.”
- **Hatás:** A tanuló kattintani próbál, és nem történik semmi. A képernyőolvasó vezérlőnek tűnő jelet olvas fel. A buildelő a régi Checkbox-specet olvashatja ki belőle, ami ellentmond a „nem rögzítjük” elvnek.
- **Javaslat:** Mind a négy sorból töröld a ☐ jeleket, például „– ☐ Igaz rám / ☐ Még nem, de pótolni fogom.” → „– Igaz rám / Még nem, de pótolni fogom.” Az állítások, a zárómondat és a ✅ eltávolítása nem változik.
- **Típus:** objektív · **Verdikt:** —

---

**A manifesttel való eltérés (nem finding; a kánoni kör DEFER_CANON tételei):**
- **MAN:84 (LMS-M5-06):** még „kitöltve” és „2–3 próbálkozás” áll benne, a HUB:180/:187 és a KAPU:24/:313 szerint (ERT-3, ERT-6) a beküldés ténye és 3 próbálkozás a helyes.
- **MAN:160:** „diagnosztikus kvíz kitöltve”.
- **MAN:82 (LMS-M5-04):** a SLIDE 6 pontozatlan, nem completion-elem jellege még nem szerepel benne.
- **MAN:85 (LMS-M5-07):** a profil még „rövid H5P; … interakció, nem megtekintés”. A completion-cella („a forrás szerinti felidézési interakció elvégzése”) az M5.3 §3.6 beviteli elem nélküli útján nem teljesíthető. Ez a LMS-3 nyitott EXTERNAL tétele.
- **MAN:83, :86 és PT:183:** „minden sor ≥ Alapszint”; a QA-ERT-2 javításával együtt kell átírni.
- **MAN:16 (H5P-C):** „a forrásban előírt interakció(k) érdemi befejezése”, szemben az ERT-1 összefoglaló diás CP-completionjével.

**A fókuszlista többi pontja (finding nélkül):**
- **ERT-6:** a HUB és a KAPU egyezik, „2–3 próbálkozás” sehol nem maradt.
- **ERT-27, ERT-3:** rendben, modulon belül nincs eltérés.
- **ERT-1:** a fenti QA-ERT-4-en kívül nincs eltérés.
- **ADV-4 (M5.1), LMS-3 (modulon belül):** nincs eltérés.
- **ERT-29:** a cím, az utasítás és a „mind a négy állításra” zárómondat egymással egyezik; a probléma csak a ☐ jel (QA-IMPL-1).
- **Invariánsok:** más ✅, a ≥80% / 12 item, a rubrikaszintek és a kaputípus nem változott.
- **ERT-28:** a 22–24. blokk szándékosan kimaradt, nem jelentem.

<!-- agent a5a0907791d7de7be -->

## M5 célzott QA, nyelvi lencse (aadf41b, AP-2026-10-12-01)

Csak a diff hunkjait és a közvetlen környezetüket néztem. 10 findingot találtam, mind P2. P0 vagy P1 nincs. A tíz regressziós minta közül a hiányzó alaptag (9), a névmási vagy referenciazuhanás (4, 10) és az elveszett minősítő (6, 7) fordul elő. Kitalált racionalizálást, hibás névelőt, nagykötőjel- vagy idézőjelhibát és tegezés-elcsúszást nem találtam. Tanulói szövegbe fejlesztői metanyelv nem szivárgott: az azonosítók, a „completion” és a „Receive a grade” csak fejlesztői sorokban áll.

Ezeket ellenőriztem, és nem jelentem: a „safer-working szabály” a GK §4.2 kánoni neve, az „a lecke … teljesül” a korpusz mintája (M5.2:21, M2), a `*passz*` dőlt írása szintén korpuszminta. Az M4.4:737-ből átvett „nem azonosító, csoportszintű információ” formulát és az M5.4-ben használt „a 4. mező” megnevezést (:140, :164) sem jelentem.

---

**M5:QA-NYELV-1**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M5/Online leckék/M5.2 – Feladat → módszer döntési fa – Mit választok először.md:317`
- **Probléma:** Két egymást követő mondatban a „feltárás” két jelentésben áll: előbb a madrih tevékenysége („feltárása nem a te feladatod”), utána a gyermek közlése, a korpusz értelmében. A „feltárás gyanúja” ráadásul szemantikusan félrecsúszik, mert egy közlést nem gyanítunk, hanem meghallunk.
- **Bizonyíték:** „érzelmi nehézségeinek feltárása nem peula-cél és nem a te feladatod” → „Ha zaklatás, gyermekvédelmi feltárás, önsértés vagy más veszélyeztetettség gyanúja merül fel”
- **Hatás:** A 15+ éves tanuló a második „feltárást” könnyen az elsővel azonosítja. A Memuna-jelzés kiváltó okai így kevésbé egyértelműek.
- **Javaslat:** OLD „Ha zaklatás, gyermekvédelmi feltárás, önsértés vagy más veszélyeztetettség gyanúja merül fel, azonnal bevonod” → NEW „Ha egy hanih gyermekvédelmi ügyet tár fel előtted, vagy zaklatás, önsértés, illetve más veszélyeztetettség gyanúja merül fel, azonnal bevonod”.
  - Javítási korlát: a négy kiváltó ok és az „azonnal bevonod a kijelölt **Memunát** (a Somer gyermekvédelmi felelősét)” formula nem változik.
  - A GYV-7 QA-ja (Memuna + programvezető) lássa.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** ugyanott, M5.2:317, utolsó mondat
- **Probléma:** A „veszély nélküli nehéz érzés” természetellenes jelzős szerkezet, a döntés „pusztán nem veszélyeztető nehéz érzelem” kifejezésének tükre.
- **Bizonyíték:** „Ha veszély nélküli nehéz érzés jön elő, a mentoroddal beszéled meg”
- **Hatás:** A második lépcső feltétele nehezen olvasható. Ez a mondat választja el a mentoros utat a Memunás úttól.
- **Javaslat:** OLD „Ha veszély nélküli nehéz érzés jön elő,” → NEW „Ha nehéz érzés jön elő, de veszélyre utaló jel nincs,”. A mondat többi része, köztük „a Memunához ilyenkor is fordulhatsz”, marad.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-3**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md:24`; vö. a HUB:180-nal
- **Probléma:** A birtokos szerkezet kétértelmű. A „madrih és a stáb jelzése” úgy olvasható, mintha ők adnák a jelzést, holott nekik szól. A HUB ugyanezt „a diagnosztikus jelzést” alakban mondja, így a két fájl eltér.
- **Bizonyíték:** „a madrih és a stáb jelzését az **első, visszajelzés előtti próbálkozás** adja”
- **Hatás:** Az értékelő félreértheti, kinek a jelzéséről van szó. Az ERT-6 átvezetése a HUB-ban és a KAPU-ban nem egyforma.
- **Javaslat:** OLD „a madrih és a stáb jelzését” → NEW „a madrihnak és a stábnak szóló diagnosztikus jelzést”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-4**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** KAPU:288
- **Probléma:** Egy mondatban két különböző „táblázat” áll: a beillesztett „a teljes táblázat alapján” a tanuló leadott táblázata, a régi „(lásd a táblázatot)” viszont a lenti rubrikatábla. A referencia összecsúszik (3. minta).
- **Bizonyíték:** „külön pontozódik a Hiányos / Alapszint / Erős skálán, a teljes táblázat alapján (lásd a táblázatot)”
- **Hatás:** Az értékelő nem tudja, melyik táblázatra utal a zárójel. Ez éppen az ERT-26 új egységénél, a kapuszabály pontozási bekezdésében történik.
- **Javaslat:** OLD „a teljes táblázat alapján (lásd a táblázatot)” → NEW „a teljes leadott táblázat alapján (a szintleírásokat lásd az alábbi rubrikában)”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – … .md:185`
- **Probléma:** A felsorolás párhuzama megbomlott. Az M5.1 és az M5.2 főszövegben áll, az M5.4 viszont zárójelben, közvetlenül az M5.2 tagja után, így az M5.2-höz tartozó megjegyzésnek látszik.
- **Bizonyíték:** „az M5.2-nél egy ág végigvitele a végképernyőig (M5.4-nél: az LMS-M5-04 H5P-C profilja; …)”
- **Hatás:** Az olvasó az M5.4 completion-szabályát az M5.2-höz kötheti.
- **Javaslat:** OLD „a végképernyőig (M5.4-nél: az LMS-M5-04 H5P-C profilja; a táblázat leadása” → NEW „a végképernyőig, az M5.4-nél az LMS-M5-04 H5P-C profilja (a táblázat leadása”. A zárójel többi része marad.
  - Javítási korlát: az M5.3-ról nem kerül be új completion-állítás.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M5/Peulák/M5.F – … (Study Lab).md:225`
- **Probléma:** A kategorikus „A lap náluk marad” után rögtön a begyűjtés feltételes engedélye jön, így a két mondat ellentmond egymást. Az asset notes ugyanezt „Alapból a résztvevőnél marad” alakban mondja: a szövegből ez a minősítő hiányzik (2. minta).
- **Bizonyíték:** „A lap náluk marad; … Név nélkül csak akkor gyűjtheted be a lapokat, ha ténylegesen senkihez sem köthetők”
- **Hatás:** A képző nem tudja eldönteni, szabad-e egyáltalán begyűjteni.
- **Javaslat:** OLD „A lap náluk marad;” → NEW „A lap alapból náluk marad;”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M5.F:56 és M5.F:401
- **Probléma:** Egy fájlon belül ugyanaz az ADV-11-protokoll kétféle megnevezéssel áll. A :401-ből kiesett a „személyes” minősítő („munkapéldányt”), és a „letöltött fájlokat” helyett „letöltéseit” szerepel.
- **Bizonyíték:**
  - :56 „jelszót nem ment, személyes munkapéldányt nem hagy rajta, a letöltött fájlokat törli”
  - :401 „jelszót nem ment, munkapéldányt nem hagy rajta, a letöltéseit törli”
- **Hatás:** Az egy fogalomra egy megnevezés elve sérül. A „munkapéldány” magyarázat nélkül homályos a képzőnek.
- **Javaslat:** :401-ben OLD „munkapéldányt nem hagy rajta, a letöltéseit törli” → NEW „személyes munkapéldányt nem hagy rajta, a letöltött fájlokat törli”. Opcionális: a :56-ban a korpusz glosszája, az M4.F:52 mintájára: „személyes munkapéldányt (letöltött vagy helyben mentett fájlt)”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv (D10, következetesség)
- **Hely:** KAPU:283 ↔ `…/M5.4 – Cél–kvuca–módszer mini-táblázat – … .md:149`
- **Probléma:** Ugyanannak a kvuca-adatszabálynak a tiltólistája a modulon belül eltér: az értékelői változatból hiányzik az „egyéni érzékeny történet”, amely a tanulói változatban szerepel.
- **Bizonyíték:**
  - KAPU: „név, diagnózis vagy beazonosítható eset nem”
  - M5.4: „név, egyéni érzékeny történet, diagnózis vagy beazonosítható eset nem kerülhet bele”
- **Hatás:** Az értékelő szűkebb listával dolgozik, mint amit a tanuló kapott.
- **Javaslat:** OLD „(korosztály, körülbelüli létszám, hangulat; név, diagnózis vagy beazonosítható eset nem)” → NEW „(korosztály, körülbelüli létszám, hangulat; név, egyéni érzékeny történet, diagnózis vagy beazonosítható eset nem)”.
- **Típus:** objektív · **Verdikt:** —

**M5:QA-NYELV-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M5.F:20 (meta, „Ha valaki nem tud részt venni”)
- **Probléma:** Hiányzó alaptag (1. minta): nem derül ki, minek a kapacitásáról van szó. Lehet a pótidőpont és a mentoros út kapacitása, vagy az F-peula programszintű kapacitása. A PRG-5 döntés szövege („rögzítse a kapacitást”) ezt nem dönti el.
- **Bizonyíték:** „A kapacitást és a pótlás felelősét a programvezető rögzíti.”
- **Hatás:** A programvezetőnek szóló instrukció nem hajtható végre egyértelműen.
- **Javaslat:** EMBERI DÖNTÉS: melyik kapacitás értendő. Dönti a projektgazda vagy a programvezető (PRG-5). Utána az alaptag kitehető. Szöveget nem javaslok helyette.
- **Típus:** emberi-döntés · **Verdikt:** —

**M5:QA-NYELV-10**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** HUB:208
- **Probléma:** Két gond van a mondatban.
  - Az alany a kettőspont után a tanulókról a mentorra vált, és az „az eredményből” nem köti vissza, kinek az eredményéről van szó.
  - A „a meglévő tananyagból … beszélgetést rendelhet” zeugma: beszélgetést nem lehet a tananyagból rendelni.
- **Bizonyíték:** „az eredményből a mentor támogató, nem kötelező beavatkozási ajánlást kap, és a programvezető a meglévő tananyagból ismétlést vagy beszélgetést rendelhet.”
- **Hatás:** A képzői analitikai teendő nehezen olvasható.
- **Javaslat:** OLD „az eredményből a mentor” → NEW „az eredményük alapján a mentor”. OLD „a meglévő tananyagból ismétlést vagy beszélgetést rendelhet.” → NEW „a meglévő tananyag ismétlését vagy egy beszélgetést rendelhet el.”
  - Javítási korlát: a „támogató, nem kötelező” jelleg és a PRG-7 tartalma nem változik.
- **Típus:** objektív · **Verdikt:** —

---

**Lencsén kívüli megfigyelés (nem nyelvi finding, a döntéshűségi QA-nak):** az átvezetési terv ERT-28-blokkjai (22–24.) nincsenek a commitban.
- Az M5.2:574 ✅ opciója változatlan: „Először a nevelési célt találom ki…”.
- A HUB:207 és a KAPU:312 ma is „cél az első” címkét visel.

Lehet, hogy ez szándékos: a terv „Fő session figyelmébe” jegyzete jelzi, hogy a döntés szövege „feladat–kvuca–módszer–cél” sorrendet ír. Ha nem szándékos, ezt a döntéshűségi lencsének kell rögzítenie.

Hivatkozott fájlok:
- `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – Nonformális nevelés, módszerválasztás & tanulástan.md`
- `02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md`
- `02 Tervezet/Modulok/M5/Online leckék/M5.2 – Feladat → módszer döntési fa – Mit választok először.md`
- `02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrihként.md`
- `02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md`

