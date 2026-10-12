# 2026-10-12 Célzott QA – M6 átvezetés (fbebec0), AP-2026-10-12-01

- **Scope:** az M6 modul HUM 14. szakasz szerinti átvezetésének diffje (`fbebec0`), csak a módosított sorok és közvetlen környezetük. Nem teljes új audit.
- **Lencsék (ténylegesen lefutott):** biztonság-jog (`safety-policy-reviewer`), értékelés + LMS (`assessment-reviewer`), nyelv (`hungarian-editorial-reviewer`). Adverzális második kör: `verifier`, mind a 20 ID-ra.
- **Run-ID:** AP-2026-10-12-01 · **Review-bázis:** `fbebec0` · **Javítás:** `511d9e0`, media `b409d02`.
- **Állapot:** VALIDÁLT.

## I. Riport

### 1. Validált objektív findingok — javítva (`511d9e0`)

| ID | Súly | Hely | Javítás |
|---|---|---|---|
| M6:QA-BIZT-5 (objektív része; GYV-17) | P2 | M6.A:466 | „(Ez a keret soha nem maradhat el, kiskorú résztvevőkkel sem.)”; a keret tartalma változatlan |
| M6:QA-BIZT-6 + QA-NYELV-2 (ADV-8) | P2 | M6.F:272, :334, :397–398 | a szóbeli gyűjtés az alap; a begyűjtött lap „nem tekinthető anonimnak”; a 30 napos megsemmisítés marad |
| M6:QA-ERT-1 (ERT-31) | P2 | KAPU:412 | a döntési szabály kimondja: a kvíz beküldése kötelező completion-elem, az eredménye nem blokkol |
| M6:QA-IMPL-1 + QA-NYELV-8 (RÉSZBEN; ERT-1, ERT-2) | P2 | M6.1–M6.3:9; záró diák | „nem önálló completion-elem” + a célverziós igazolás feltétele (RA 9); a záró dián „Lapozz tovább az összefoglaló diára …”; a completion-feltétel nem változott |
| M6:QA-NYELV-1 (ERT-35) | P2 | M6.4:961, KAPU:165 | „az utolsó helyzetből, akármelyik eszközt választottad”; két mondat; a KAPU leíró megnevezést kapott; ✅ változatlan |
| M6:QA-NYELV-3 (ADV-11) | P2 | M6.F:508 | három mondatra bontva, minden protokollelem megmaradt |
| M6:QA-NYELV-4 (RÉSZBEN; ADV-11) | P2 | M6.F:474 (`@asset`) | a protokoll tagolva, a tiltás nem fordulhat meg |
| M6:QA-NYELV-9 (ADV-4, ERT-33) | P2 | M6.1:170, M6.2:118, M6.3:190, KAPU:392 | „ne rögzüljön a követett H5P próbálkozásban”; a társas visszajelzés mondata |
| M6:QA-NYELV-10 (PRG-2) | P2 | HUB:122, M6.4:55 | „a döntésekre kapott visszajelzésből”, „egy-egy” |
| M6:QA-NYELV-11 (ADV-10) | P2 | M6.3:550 | állítmányos mondat a lista mintájára; a feltételek változatlanok |

### 2. Emberi döntést igénylő tételek

| ID | Mit kell eldönteni | Kitől |
|---|---|---|
| M6:QA-BIZT-1 (GYV-7) | vonatkozik-e a kétlépcsős küszöb az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára (a 6D/ZÁRÓ ismétlése a 2026-10-05-i döntés szerint Memuna-QA alatt áll) | Memuna |
| M6:QA-BIZT-2 (GYV-7) | ki adja a „támogató mentorálást” a madrih–hanih viszonyban (a madrih maga is lehet kiskorú), és kell-e konzultációs út | Memuna |
| M6:QA-BIZT-3 (GYV-18) | a KAPU 12. item új szára és ✅-ja; a narráció a VO fix packkal | értékelési felelős + Memuna; a kulcs: projektgazda; VO: médiafelelős |
| M6:QA-BIZT-4 (+ QA-NYELV-6; GYV-5) | a 4.3.2/B négy lépése az M6.A „kötelező megállítási protokollja”-e; alkalmazható-e az egyszemélyes kivétel, ki dokumentálja | Memuna + programvezető |
| M6:QA-BIZT-5 tartalmi része (+ QA-NYELV-7; GYV-17) | mit jelent a keretben „a kiskorúakra is térjen ki” | Memuna + a peula tartalomfelelőse |

### 3. Bizonyíték-kapu

M6:QA-BIZT-7 — Memuna (GYV-5/7/16/17/18), programvezető (GYV-5, ADV-9, ADV-10), DPO / jogi felelős (ADV-8–11), LMS-gazda (ADV-11), értékelési felelős (ADV-8, GYV-18), modulgazda és hozzáférhetőségi gazda (PRG-13), hub-tartalomfelelős (PRG-16).

### 4. Elvetve

M6:QA-NYELV-5 — a „személyes munkapéldány” az ADV-11 szó szerinti szava; az értelmezése az ADV-11 utólagos QA-ja.

## B. Verifier-verdiktek (szó szerint)

<!-- agent a4706c4e8ff27931a -->

M6 célzott QA (AP-2026-10-12-01, fbebec0): adverzális második kör. A 20 ID-ből 16 megerősítve, 3 részben, 1 elvetve. Minden hivatkozott helyet a mostani fájlban olvastam vissza, a diffel és a tervvel összevetve. Fájlt nem szerkesztettem.

M6:QA-BIZT-1 | MEGERŐSÍTVE | emberi-döntés | P1 | Az M6.2:783 a GYV-7 szerint a pusztán nehéz érzést (friss gyászt) nem jelzési ügynek veszi, az M6.3:749 és az M6.4:933/:1028 viszont a „friss seb”-et továbbra is az ötlépéses jelzési útra küldi. A 6D/ZÁRÓ ismétlése a 2026-10-05-i döntés jegyzőkönyve (04 Audit) szerint „remains Memuna QA; do not change it now”. | Korlát: Memuna-döntésig egyik dobozhoz sem nyúlunk; az M6.2 új mondata marad.

M6:QA-BIZT-2 | MEGERŐSÍTVE | emberi-döntés | P1 | Az M6.2:783 utolsó mondata („az nem jelzési ügy: támogatást ajánlasz neki…”) a döntés „támogató mentorálás” elemét a madrihra teszi, felnőtt vagy mentor megnevezése nélkül. Ez a kiskorú madrih szerepét érinti, és a döntés új alkalmazási esete. | Korlát: új szabály nem kerül be; Memuna döntse el, ki ad mentorálást, és van-e konzultációs út.

M6:QA-BIZT-3 | MEGERŐSÍTVE | emberi-döntés | P1 | A KAPU:328/:331 (régi szár, ✅ A passz nélkül) és az M6.2:631–632 narráció egyezik az idézettel. A GYV-18 maga köti a ✅/disztraktor szövegét az értékelési felelős és a Memuna jóváhagyásához. | Korlát: a 12. item és a kulcs jóváhagyásig változatlan; a narráció csak VO-fix packkal változhat, `@source` nem.

M6:QA-BIZT-4 | MEGERŐSÍTVE | emberi-döntés | P2 | Az M6.A:10/:182/:712 „kötelező megállítási protokoll”-ja nincs azonosítva. Az M0:QA-BIZT-2 szerint a 4.3.2/B protokollnak minősítése a Memuna és a programvezető döntése. Az egyszemélyes kivétel szó szerinti GYV-5-szöveg, M6.A-beli alkalmazhatósága új alkalmazás. Ez a megtartandó a NYELV-6-tal szemben. | Korlát: a döntés szövege nem változik; 4.3.2/B-azonosítás nem írható be.

M6:QA-BIZT-5 | MEGERŐSÍTVE | emberi-döntés (objektív részjavítással) | P2 | A :462 „kötelező” címe és a GYV-17 „kötelezően kimondott” szövege mellett a :466 zárójel a kötelezőséget kiskorúakra szűkíti. Ez ellentmond a döntésnek, tehát objektív. Hogy mit jelent a „kiskorúakra is térjen ki”, az a Memuna és a peula tartalomfelelősének döntése. Ez a megtartandó a NYELV-7-tel szemben. | Az átmeneti javaslat használható: OLD „*(Kiskorú résztvevőkkel ez a keret soha nem maradhat el.)*” → NEW „*(Ez a keret soha nem maradhat el, kiskorú résztvevőkkel sem.)*”. A keret tartalma nem változik.

M6:QA-BIZT-6 | MEGERŐSÍTVE | objektív | P2 | A 4.2 (:334) az ADV-8 szerint a szóbeli gyűjtést teszi elsődlegessé. A 4.3 (:397–398) a begyűjtést első helyen, egyenrangú „Név nélkül” módként kínálja; ez az alapállapotban is így volt, a döntés óta ellentmondás. A javaslat iránya jó, de csak „pl.”-szintű. A NYELV-2-vel együtt kell alkalmazni. | Minimális javítás (és a Nyílt pont kerüljön előre):
- :397 OLD „Két mód közül választhatsz, akár kombinálva.” → NEW „Elsősorban szóban gyűjtsd a kérdéseket (Nyílt mód, lásd 4.2); a jegyzetlapokból csak akkor dolgozz, ha a 4.2 végén mégis begyűjtötted őket.”
- :398 OLD „**Név nélkül:** begyűjtöd gyorsan a jegyzetlapokat (kis csoportban ez sem névtelen, lásd 4.2), átfutod,” → NEW „**Ha a 4.2 végén begyűjtötted a lapokat** (kis csoportban ezek sem anonimak, lásd 4.2)**:** gyorsan átfutod őket,”
- :272 notes OLD „Név nélkül begyűjthető (4.2 Blokk 2 vége) a kérdésgyűjtéshez (4.3 Blokk 3, 2. lépés).” → NEW „Elsősorban a résztvevőknél marad; ha a képző a 4.2 Blokk 2 végén mégis begyűjti, a kérdésgyűjtéshez (4.3 Blokk 3, 2. lépés) használható, de kis csoportban nem anonim.”
- Utána build. A 30 napos megsemmisítés marad.

M6:QA-BIZT-7 | MEGERŐSÍTVE | bizonyíték-kapu | P1 | A HUM :613 idézete pontos, a :617 a bizonyíték-bejegyzéseket kifejezetten nyitva hagyja. A szerepek egyeznek a 14. szakasz megfelelő soraival (GYV-5/7/16/17/18, ADV-8–11, PRG-13, PRG-16). | Nem javítható: a RELEASE-READINESS G-kapuihoz és a tracker-issue-hoz tartozik.

M6:QA-ERT-1 | MEGERŐSÍTVE | objektív | P2 | A KAPU:412 „ajánlott formatív előkészítő (nem blokkol)” mondata nem említi az ERT-31 szerinti kötelező beküldést, amelyet a KAPU:38 rögzít. A :412 alapállapot-maradvány, a diff nem érintette. | A javasolt OLD → NEW helyes és minimális. A ≥80%, a korlátlan próbálkozás, a nem blokkoló státusz és a kaputípus marad. A §0-tábla módosítása opcionális.

M6:QA-IMPL-1 | MEGERŐSÍTVE | objektív | P2 | Az M6.1–M6.3:9-ből hiányzik az ERT-1 célverziós feltétele és a negatív teszt. A „Lapozz tovább…” tanulói mondat sincs meg; az M0.1:13, az M0.2–M0.4, az M2.1 és az M4.4 ezt már tartalmazza (M0:QA-IMPL-1). | A javaslat helyes:
- a 9. sor végére az M0.1:13 mondata „megválaszolatlan vagy kihagyott interakcióval” alakban;
- a záró dia látható, nem narrált szövegébe „Lapozz tovább az összefoglaló diára, mert ott küldi el a lecke az eredményedet.”;
- az M0-precedens szerint a Moodle-intro mondata („Menj végig a diákon…”) opcionális;
- a completion-feltétel nem változik, pin kell.

M6:QA-NYELV-1 | MEGERŐSÍTVE | objektív | P2 | A „D-helyzet” fejlesztői ágcímke, a tanuló sehol nem látja (intro :78, 3D-cím :732). A mondatot az fbebec0 (ERT-35) hozta be, tehát a szerkesztés regressziója. A 2026-10-05-i befagyasztás a :1028-as biztonsági ismétlésre vonatkozik, nem erre. | A fő OLD → NEW helyes. A KAPU:165-re szóló mellékjavaslat csak akkor alkalmazható, ha a ✅ marad: OLD „(M6.4, záró oldal; részletesen: a D. szcenárió)” → NEW „(M6.4, záró oldal; részletesen: az idősebb Leviatán-kvuca helyzete)”. Pin kell.

M6:QA-NYELV-2 | MEGERŐSÍTVE | objektív | P2 | A „név nélküli lap … nem névtelen” önellentmondásnak hangzik; a döntés szava „ne minősítsünk anonimnak”. Nem duplikátum, de a :398-at a BIZT-6-tal közös szerkesztésben kell javítani. | :334 OLD „ezért nem névtelen:” → NEW „ezért nem tekinthető anonimnak:”. A :398 a BIZT-6 NEW-jában.

M6:QA-NYELV-3 | MEGERŐSÍTVE | objektív | P2 | A :508 „helyette” előzménye kétértelmű, a sor túlhalmozott. A javasolt NEW minden protokollelemet megtart. | A javasolt OLD → NEW helyes.

M6:QA-NYELV-4 | RÉSZBEN | objektív | P2 | A :474 torlódása valós. A javasolt NEW-ban viszont a „belépés, jelszómentés és … nélkül” vessző miatt a „jelszómentés” önálló, pipálható pontnak olvasható, így a tiltás megfordulhat. | Helyette: OLD „wifi/Moodle/H5P, a közös eszközön saját fiókkal belépés jelszómentés és személyes munkapéldány nélkül, kijelentkezés, munkamenet-ellenőrzés és a letöltések törlése, alternatívaként papír vagy saját eszköz, az M6.1” → NEW „wifi/Moodle/H5P; közös eszköz: belépés saját fiókkal, jelszót nem ment, személyes munkapéldányt nem hoz létre, kijelentkezés, munkamenet-ellenőrzés, a letöltések törlése, helyette papír vagy saját eszköz is választható; az M6.1”. Utána build.

M6:QA-NYELV-5 | ELVETVE | — | — | A „személyes munkapéldány” az ADV-11 szó szerinti, helyesen átvezetett szava; hibát a finding nem bizonyít (bizalom: alacsony). Az értelmezése az ADV-11 utólagos QA-jába tartozik (LMS-gazda + DPO), amelyet a BIZT-7 már lefed. | Nincs változtatás.

M6:QA-NYELV-6 | RÉSZBEN | emberi-döntés | P2 | A probléma valós, de a BIZT-4 duplikátuma. Az objektívnek javasolt „(itt: a 4.3.2/B négy lépése)” azonosítást az M0:QA-BIZT-2 verifier-ítélete Memuna- és programvezetői döntésnek minősítette. A mellérendelés („…vagy helyettes és protokoll”) a GYV-5 szó szerinti szerkezete. | A javasolt három NEW egyike sem alkalmazható; a BIZT-4 a megtartandó.

M6:QA-NYELV-7 | MEGERŐSÍTVE | emberi-döntés | P2 | A BIZT-5 duplikátuma: ugyanaz a hely és a probléma. | A BIZT-5 a megtartandó, a javítás az ott leírt átmeneti NEW.

M6:QA-NYELV-8 | RÉSZBEN | objektív | P2 | Az „önálló” minősítő kiesése valós: az ERT-2 és a saját runtime-doboz (:170/:118/:190) „nem önálló completion-elem”-et ír. A „választó → választós kérdés” csere viszont alaptalan: a „választó” maga a döntés (ERT-2) szava, és az M0.1:13 is így használja. | Mindhárom 9. sorban: OLD „pontozatlan választója nem completion-elem;” → NEW „pontozatlan választója nem önálló completion-elem;”. Az IMPL-1-gyel együtt, egy szerkesztésben.

M6:QA-NYELV-9 | MEGERŐSÍTVE | objektív | P2 | A „ne rögzítse a követett H5P próbálkozás” élettelen alanyú tükörszerkezet; a döntés (ADV-4) „ne rögzítsük … próbálkozásban” formát használ. A KAPU:392 „visszajelzése … figyeljen” ugyanez a minta. | A javasolt OLD → NEW (3 runtime-doboz és KAPU:392) helyes; a „lehetőleg” marad.

M6:QA-NYELV-10 | MEGERŐSÍTVE | objektív | P2 | Mindkét mondatot az fbebec0 hozta be (PRG-2); a döntés nem így fogalmaz. A nagykötőjeles „1–1” tartománynak olvasható, a párhuzamos M6.4 „egy-egy”-et ír. | A javasolt OLD → NEW helyes; a PRG-2 szűkítés tartalma marad, az M6.4-ben pin kell.

M6:QA-NYELV-11 | MEGERŐSÍTVE | objektív | P2 | Az M6.3:550 fbebec0-ban bekerült pontja állítmány nélküli, és megtöri a lista „címke: változat” párhuzamát. | A javasolt NEW helyes: a jóváhagyás, a négy ismérv és a papíros alapértelmezés marad. Pin kell.

**Összesítés:**
- Verdiktek: MEGERŐSÍTVE 16, RÉSZBEN 3 (NYELV-4, NYELV-6, NYELV-8), ELVETVE 1 (NYELV-5).
- Típus szerint: objektív 11, emberi-döntés 7, ebből 2 duplikátum (NYELV-6, NYELV-7); bizonyíték-kapu 1 (BIZT-7).

**Duplikátumok:** a NYELV-6 a BIZT-4-é (a BIZT-4 marad), a NYELV-7 a BIZT-5-é (a BIZT-5 marad).

**Együtt alkalmazandó, nem duplikátum:** BIZT-6 és NYELV-2 (közös :398); IMPL-1 és NYELV-8 (közös 9. sor); NYELV-3 és NYELV-4 (azonos protokoll, más hely).

Releváns fájlok:
- 02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md
- 02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md
- 02 Tervezet/Modulok/M6/Online leckék/ (M6.1–M6.4)
- 02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md
- 01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – M6.4 elfogadás és Command 5 hatókör.md


## C. Nyers lencse-kimenetek (szó szerint)

<!-- agent a3ab13182a5d8e53a -->

## M6 – célzott QA, biztonság-jog lencse (fbebec0, HUM 14. szakasz, AP-2026-10-12-01)

Hat findingot találtam: 3×P1 és 3×P2, ebből 5 emberi döntés és 1 objektív. Mellé egy összesítő bizonyíték-kaput. Csak olvastam, fájlt nem módosítottam.

**Ahol nem találtam hibát:**
- **Szó szerinti, hiánytalan átvezetés, nem gyengült védelem:** a GYV-16 (az M6.1:1070–1072 minimuma betűre átment), a PRG-13, a PRG-16, az ADV-9, az ADV-10 és az ADV-11.
- **ADV-1:** az M6-ban nincs olyan tanulói mondat, amely tagadná a rendszergazda hozzáférését. A meghagyott „hogy a szabad szöveges válaszait más ne lássa” a közös eszköz többi használójáról szól, nem az adminról.
- **GYV-17, a döntés második fele:** átvezetettnek tekintem. A tiltott zóna most kötelező keret, így a KAPU 7. itemjének (:221, :233) forrása már nem opcionálisan hallott tartalom. A P1 négy lépése a kötelező M6.4 ZÁRÓ oldalon is áll (:1028), és a 6D-ben is (:939).

---

**M6:QA-BIZT-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:783`
  - `…/M6.3 – Kézműves, ami tanít is.md:749`
  - `…/M6.4 – Döntési szcenáriók – mit választanál.md:933`, `:1028`
- **Probléma:** A GYV-7 kétlépcsős küszöbe csak az M6.2-ben él. Az M6.3 és az M6.4 dobozaiban a „friss seb” továbbra is az ötlépéses jelzési utat indítja. Ugyanarra a helyzetre (friss gyász) a modulon belül két ellentétes utasítás áll.
- **Bizonyíték:**
  - M6.2:783: „Ha valaki pusztán nehéz érzésről beszél (például friss gyászról), és veszélyeztetettség nem merül fel, az nem jelzési ügy”
  - M6.4:1028: „valós, súlyos témát (bántalmazás, önsértés, friss seb) tár fel, az már **nem játék**: az **ötlépéses jelzési utat** követed”
- **Hatás:** A madrih leckétől függően kap ellentétes jelzési küszöböt.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna döntse el, hogy a kétlépcsős küszöb az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára is vonatkozik-e. A 6D/ZÁRÓ ismétlése a 2026-10-05-i döntés szerint Memuna-QA alatt áll („do not change it now”), ezért ezekhez a dobozokhoz Memuna-döntés nélkül nem nyúlunk.
- **Típus:** emberi-döntés · **Besorolás:** EMBERI JÓVÁHAGYÁS KELL
- **Verdikt:**

**M6:QA-BIZT-2**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:783` (az új utolsó mondat)
- **Probléma:** A döntés második lépcsője „támogató mentorálás, választási lehetőséggel”. A szöveg ebből azt csinálta, hogy a madrih maga mondja ki: „nem jelzési ügy”, és ő ajánl támogatást. A madrih maga is lehet kiskorú. Nincs megnevezve felnőtt vagy mentor, és nincs útvonal arra az esetre, ha a madrih bizonytalan. Ez a lezárt döntés új alkalmazási esete (madrih és hanih viszonya, nem mentor és tanuló).
- **Bizonyíték:** „az nem jelzési ügy: támogatást ajánlasz neki, és ő választja meg, él-e vele.” A döntés szövege (HUM :630): „pusztán nem veszélyeztető nehéz érzelemnél támogató mentorálás, választási lehetőséggel”
- **Hatás:** A veszélyeztetettség kizárása és a támogatás egyedül a kiskorú madrihra hárulhat.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna döntse el, ki adja a „támogató mentorálást” a madrih és a hanih viszonyában, és kell-e bizonytalanság esetén konzultációs út (Memuna vagy 18+ felelős). Új szabályt a tananyagba addig nem írunk.
- **Típus:** emberi-döntés · **Besorolás:** EMBERI JÓVÁHAGYÁS KELL
- **Verdikt:**

**M6:QA-BIZT-3**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:327–331` (12. item, szár és ✅)
  - `…/M6.2 – Történet, mint tükör.md:631–632` (`M6.2-NAR-05-VO`, látható leirattal)
- **Probléma:** A GYV-18 után a „nálatok” típusú önfeltáró kérdés opcionális és passzolható. A modul két helyen még a régi alakot tanítja:
  - **a KAPU 12. item ✅-ja:** valódi, friss kicsúfolás után önfeltáró kérdés, passz nélkül;
  - **a narráció:** a kérdést passz és opcionalitás nélkül mondja.
- **Bizonyíték:**
  - KAPU:328/331: „Tudod, hogy a kvucában nemrég valakit tényleg kicsúfoltak.” … „„Láttál-e már olyat, hogy egy beszólás miatt valaki kívül érezte magát? (Nem kell nevet mondani.)” ✅”
  - M6.2:631: „– ‘Milyen hasonló helyzet volt már nálatok? / Nem kell nevet mondani.’”
- **Hatás:** A kapukvíz és a hang azt erősíti meg, amit a döntés megváltoztatott.
- **Javaslat:** EMBERI DÖNTÉS. Az új 12. item szárát és ✅-ját az értékelési felelős és a Memuna hagyja jóvá, a kulcsot a projektgazda (a döntés szerint addig változatlan). A narráció kimondott szövege és a leirat egy VO-fix packban, a VO-gazdánál változik, a lecke-kódban nem.
- **Típus:** emberi-döntés · **Besorolás:** EMBERI JÓVÁHAGYÁS KELL (a 12. item, a VO); a GYV-18 maga PROJEKT-DÖNTÉS
- **Verdikt:**

**M6:QA-BIZT-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:182` (2.3)
  - ugyanott `:712` (5. lista) és `:10` (az ellenőrzőlista specje)
- **Probléma:** A fő session döntése szerint a GYV-5 szó szerint került be, a 4.3.2/B-azonosítás nélkül. Emiatt a „kötelező megállítási protokoll” az M6.A-ban sehol nincs meghatározva, a képzői lista mégis kipipáltatja. Az „Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben” mondat olyan peulán áll, amelyet ugyanez a sor érzékenynek nevez. Nem derül ki, alkalmazható-e itt a kivétel, és ki dokumentálja.
- **Bizonyíték:**
  - :712: „Megvan a második felkészített 18+ felelős, vagy egy azonnal elérhető helyettes és a kötelező megállítási protokoll (2.3).”
  - :182: „Érzékeny peula … Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet”
- **Hatás:** A képző nem tudja ellenőrizni a protokoll meglétét. Az egyszemélyes kivétel kiskaput nyithat az érzékeny peulán.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna és a programvezető döntse el:
  - a 4.3.2/B négy lépése az M6.A „kötelező megállítási protokollja”, vagy külön protokoll kell;
  - alkalmazható-e az egyszemélyes kivétel az M6.A-n, és ki, hol dokumentálja.

  A döntés szövegét nem nyitjuk újra.
- **Típus:** emberi-döntés · **Besorolás:** EMBERI JÓVÁHAGYÁS KELL (a GYV-5 PROJEKT-DÖNTÉS, az M6.A-beli konkretizálása új alkalmazás)
- **Verdikt:**

**M6:QA-BIZT-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:462–466`
- **Probléma:** A döntés szerint a tiltott zóna „a kiskorúakra … is térjen ki”. Az átvezetés ezt saját olvasattal eljárási szabállyá tette: „kiskorú résztvevőkkel ne maradjon el”. A terv maga is QA-pontosítást kér ehhez. A zárójeles mondat ráadásul azt sugallja, hogy felnőtt résztvevőknél a keret elhagyható, ami ütközik a „kötelező” címmel.
- **Bizonyíték:** „**Tiltott zóna (kötelező, a játék indítása előtt mondd ki röviden):**” … „*(Kiskorú résztvevőkkel ez a keret soha nem maradhat el.)*”
- **Hatás:** A kötelező keret felnőtt csoportnál opcionálisnak olvasható. A „kiskorúak” tartalmi eleme pedig valójában nincs átvezetve.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna és a peula tartalomfelelőse mondja meg, mit jelent a keretben a „kiskorúakra is térjen ki”. Addig a zárójel ne sugalljon elhagyhatóságot:
  - OLD: „(Kiskorú résztvevőkkel ez a keret soha nem maradhat el.)”
  - NEW: „(Ez a keret soha nem maradhat el, kiskorú résztvevőkkel sem.)”
- **Típus:** emberi-döntés · **Besorolás:** EMBERI JÓVÁHAGYÁS KELL (a GYV-17 PROJEKT-DÖNTÉS)
- **Verdikt:**

**M6:QA-BIZT-6**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:397–398` (4.3, 2. lépés)
  - ugyanott `:272` (MUNK-01 notes)
- **Probléma:** Az ADV-8 szerint a 4.2 (:334) elsődleges útnak a lapok résztvevőknél maradását és a szóbeli gyűjtést teszi. A 4.3 viszont a begyűjtést egyenrangú, első helyen álló választásként kínálja, „Név nélkül” címkével. A modulon belül ellentmondó mondat maradt.
- **Bizonyíték:**
  - :397: „Két mód közül választhatsz, akár kombinálva.”
  - :398: „**Név nélkül:** begyűjtöd gyorsan a jegyzetlapokat (kis csoportban ez sem névtelen, lásd 4.2)”
  - :334: „Elsősorban a lapok a résztvevőknél maradnak, és a kérdéseket szóban gyűjtitek össze.”
- **Hatás:** A képző a begyűjtést alapútnak veszi, így szükségtelenül keletkezik visszaazonosítható adat.
- **Javaslat:** A 4.3-ban a szóbeli („Nyílt”) mód legyen az elsődleges. A begyűjtés csak a 4.2 „ha mégis begyűjtöd” esetére maradjon, pl. „**Ha a 4.2 végén mégis begyűjtötted a lapokat** (kis csoportban ez sem névtelen, lásd 4.2): …”. A :272 notes „Név nélkül begyűjthető” fordulata ennek megfelelően igazodjon. Ez `@asset`, tehát build kell utána. A 30 napos megsemmisítés és az ADV-hivatkozás marad.
- **Típus:** objektív · **Besorolás:** PROJEKT-DÖNTÉS (ADV-8)
- **Verdikt:**

**M6:QA-BIZT-7**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:613` és a 14. szakasz megfelelő sorai (`:628`, `:630`, `:639–641`, `:654–657`, `:733`, `:736`), illetve a `02 Tervezet/RELEASE-READINESS.md` G-kapui
- **Probléma:** A döntések lezártak és most átvezetve. A megnevezett szerepek írásos QA- vagy vétóbizonyítéka azonban hiányzik:
  - Memuna: GYV-5, GYV-7, GYV-16, GYV-17, GYV-18;
  - programvezető: GYV-5, ADV-9, ADV-10;
  - DPO / jogi felelős: ADV-8, ADV-9, ADV-10, ADV-11;
  - LMS-gazda: ADV-11;
  - értékelési felelős: ADV-8, GYV-18;
  - modulgazda és hozzáférhetőségi gazda: PRG-13;
  - a hub tartalomfelelőse: PRG-16.
- **Bizonyíték:** HUM :613: „**Vétó/QA:** a jobb oldali oszlop a döntési csomagban bejegyzésenként megnevezett szerepeket adja; ellenőrzésük utólagos vétó/QA.”
- **Hatás:** Az átvezetés `IMPLEMENTED`, de nem `FINAL_RELEASE_QA`. Vétónál a sor `REOPENED`.
- **Javaslat:** Megvalósítási döntés: a projektgazda jóváhagyta; a formális szerepköri bizonyíték függő. A G-kapukhoz és a tracker-issue-hoz kell rögzíteni, nem javítható.
- **Típus:** bizonyíték-kapu · **Besorolás:** PROJEKT-DÖNTÉS + függő szerepköri bizonyíték
- **Verdikt:**

Releváns fájlok:
- `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md`
- `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md`
- `02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md`
- `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md`
- `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md`
- `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md`
- `02 Tervezet/Emberi jóváhagyás szükséges.md`

<!-- agent a9b253a99a09714ac -->

## M6: értékelési és LMS-QA a HUM 14. szakasz átvezetéséről (fbebec0, AP-2026-10-12-01)

Két finding van, mindkettő P2. Answer key, opció, küszöb (≥2 „Oké”, 80%, ≥10/12, >30%, >25%), rubrikaszint, kaputípus és időtartam nem változott a döntéseken túl.

### M6:QA-ERT-1
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:412` (Döntési szabály). Kapcsolódó, a beküldési kötelezettséget nem említő helyek: ugyanott a :23 (§0 komponenstábla, (A) sor) és a HUB §6.1 (:191–202).
- **Probléma:** Az ERT-31 átvezetése után a KAPU döntési szabálya a kvízt továbbra is „ajánlott”-nak nevezi. A :38 és a HUB §6 3. pontja szerint viszont a beküldése kötelező completion-elem.
- **Bizonyíték:** KAPU:412 „A **szcenárió-kvíz** ehhez **ajánlott formatív előkészítő** (nem blokkol)” ↔ KAPU:38 „A kvíz **beküldése** ugyanakkor az M6 teljesítésének kötelező eleme (LMS-M6-06)”
- **Hatás:** A képző vagy a tanuló a döntési szabályból kihagyhatónak olvassa a kvízt. Beküldés nélkül az M6 complete nem áll be, így az M7 felkészültségi kvíze („az M6 complete feltétellel”, LMS-M7-07) zárva marad.
- **Javaslat:**
  - KAPU:412, OLD: „A **szcenárió-kvíz** ehhez **ajánlott formatív előkészítő** (nem blokkol);” → NEW: „A **szcenárió-kvíz** ehhez **formatív előkészítő**: a beküldése az M6 teljesítésének kötelező eleme (LMS-M6-06), az eredménye nem blokkol;”
  - Opcionálisan a §0 tábla (A) sorának Szerep-cellája: „formatív / diagnosztikus (nem blokkol; a beküldés az M6 completion eleme)”.
  - Tilos módosítani: a ≥80%-ot, a korlátlan próbálkozást, a nem blokkoló státuszt és a kaputípust.
- **Típus:** objektív

### M6:QA-IMPL-1
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** M6.1:9, M6.2:9, M6.3:9 („Completion (lecke)”), mellette a záró „CHECK + OUTRO” diák (M6.1 SLIDE 8, M6.2 SLIDE 8, M6.3 SLIDE 7), a `02 Tervezet/Modulok/M6/Online leckék/` alatt.
- **Probléma:** A CP-completion („az összefoglaló dia elérése”) igazolatlan tényként áll. Ugyanennek a döntésnek (ERT-1) az elsődleges, M0-beli átvezetése két dolgot tartalmaz, ami itt hiányzik:
  - a célverziós igazolás feltételét (runtime acceptance 9. pont: van-e összefoglaló dia, és kihagyott interakcióval is beáll-e a completion);
  - a tanulói utasítást, hogy lapozzon el az összefoglaló diáig.
  - Az összefoglaló dia egyébként indokolt: mindhárom CP-ben van pontozott Check-feladat.
- **Bizonyíték:** M6.1:9 „**Completion (lecke):** az összefoglaló dia elérése (az LMS-M6-01 H5P-C profilja, BSPEC-06; M6 hub §6)” ↔ M0.1:13 „Hogy a Course Presentationnek ténylegesen van-e összefoglaló diája, és megválaszolatlan választókkal is beáll-e a completion, a célverzión kell igazolni (runtime acceptance 9. pont).” és M0.3:366 „Lapozz tovább az összefoglaló diára, mert ott küldi el a lecke az eredményedet.” Az M6-ban a „9. pont” és a „Lapozz tovább” keresés 0 találatot ad.
- **Hatás:**
  - Az ERT-1 kötelező negatív tesztje (üres vagy kihagyott interakció) nem kötődik az M6-specifikációhoz.
  - Ha a tanuló a CHECK + OUTRO dián kilép, a grade nem jön létre. Ekkor az M6.2 (unlock: LMS-M6-01) nem nyílik meg.
- **Javaslat:**
  - Az M6.1–M6.3:9 sor végére az M0.1:13 mondata szó szerint, „megválaszolatlan vagy kihagyott interakcióval” alakban.
  - A záró diák látható szövegébe (a narráción kívül) az M0.3:366 mondata.
  - Tilos módosítani: a completion-feltételt, a ✅-okat és a tanuló-lokális lépések besorolását. A látható szöveg változik, ezért pin kell.
- **Típus:** objektív

### Összesítő megjegyzés a kánoni körnek (nem finding)
- **ERT-31:** a modulon belül nem maradt „két feltétel” vagy „nem feltétel” mondat. A HUB §6 1–3. pontja, a KAPU:38 és a MAN:161 egyezik.
- **ERT-33:** sem a KAPU-ban, sem a HUB-ban, sem az M6.B-ben nem maradt „társak pontoznak” mondat. Az M6.B-MUNK-02 „értékelő lap … háromfokú skálával” specje határeset, de nem állítja, hogy a társak pontoznak.
- **ERT-35:** a ZÁRÓ oldalra került mondat az 5D-T és az 5D-J meglévő szövegéből áll. A 4. item ✅ B elvét tanítja, és nem ütközik a kulccsal.
- **ERT-34, ERT-37, ERT-9 (KAPU), LMS-4, PRG-2, PRG-7, ERT-6 (KAPU, HUB):** a modulon belül egységes. A Review options sor szó szerint a validált IMPL-G1-3 alpont.
- **A manifesttel és a kánonnal még eltérő helyek:**
  - MAN:16: a H5P-C profil („érdemi befejezés; puszta megtekintés nem elég”) eltér az ERT-1 szerinti összefoglalódia-completiontől.
  - MAN:91 / MAN:20: az ERT-9 (ASSIGN-M, SUBMITTED / CONFIRMED) még nincs átvezetve.
  - MAN:92: az ERT-6 első próbálkozása hiányzik.
  - PT:288: még a „társas–stáb kalibráció” kifejezés áll (ERT-33).
  - PT:111, :193, :274: nem említik, hogy a kvíz beküldése kötelező.
  - RA:55: hiányzik a „csupa Oké” = 10/15 pozitív eset (LMS-4).
  - RA 9: a negatív teszt hatókörét ki kell terjeszteni az LMS-M6-01…03 sorokra.
- **Bizonyíték-kapu:** a döntésekben megnevezett QA-szerepek (értékelési felelős, programvezető, LMS-gazda) írásos bizonyítéka függőben van; erre nem következtettem.

<!-- agent a1de25b27e31eaba7 -->

M6 célzott QA, nyelvi lencse (fbebec0, AP-2026-10-12-01). A diff minden hozzáadott és módosított mondatát átnéztem, read-only módon. 11 finding van: 9 objektív és 2 emberi döntés, mind P2. P0 vagy P1 nincs, a cap nem telt be.

Fájlrövidítések (a teljes elérési út):
- HUB = 02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md
- KAPU = 02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md
- M6.1 = 02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md
- M6.2 = 02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md
- M6.3 = 02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md
- M6.4 = 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md
- M6.A = 02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md
- M6.F = 02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md

---

**M6:QA-NYELV-1**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M6.4:961 (ZÁRÓ OLDAL, Szöveg); a párja KAPU:165 (a 4. item tanulói visszajelzése)
- **Probléma:**
  - A tanuló által látott záró szövegben fejlesztői ágcímke áll („D-helyzet”).
  - A tanuló a leckében sehol nem látja az ágak betűjelét: a 3D oldal címe „Idősebb Leviatán-kvuca (16–17) – komolyabb téma előtt”.
  - A mondat két gondolatot „míg ha” halmozással köt össze.
  - Az „akármelyik utat” eltér a 6D oldal fordulatától: „Akármelyik eszközt választottad”.
- **Bizonyíték:** „Egy példa a D-helyzetből, akármelyik utat választottad: … egy komolyabb témára, míg ha rögtön nagyon mély, konfliktusos helyzetet hozol, …”
- **Hatás:**
  - A tanuló nem tudja, melyik helyzetre utal a példa.
  - A KAPU 4. iteme éppen ide küldi a tanulót, ráadásul más címkével („D. szcenárió”).
- **Javaslat:**
  - OLD: „Egy példa a D-helyzetből, akármelyik utat választottad: egy idősebb, 16–17 éves Leviatán-kvucánál egy esetleírás segít **kívülről ránézni** egy komolyabb témára, míg ha rögtön nagyon mély, konfliktusos helyzetet hozol, könnyen jön védekezés vagy cinizmus.”
  - NEW: „Egy példa az utolsó helyzetből, akármelyik eszközt választottad: egy idősebb, 16–17 éves Leviatán-kvucánál egy esetleírás segít **kívülről ránézni** egy komolyabb témára. Ha viszont rögtön nagyon mély, konfliktusos helyzetet hozol, könnyen jön védekezés vagy cinizmus.”
  - Mellékjavaslat, közepes bizalommal: a KAPU:165 „(részletesen: a D. szcenárió)” sem tanulói címke, oda is leíró megnevezés kell.
  - Tilos: a példa tartalmához, a ✅-hoz és a D-e topológiához nyúlni. A látható szöveg változik, ezért pin kell.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M6.F:334 (4.2), M6.F:398 (4.3)
- **Probléma:**
  - A „név nélküli” és a „névtelen” a magyarban szinonima, ezért a mondat önellentmondásnak hangzik.
  - A döntés (ADV-8) szava: „ne minősítsünk anonimnak”.
- **Bizonyíték:** „a név nélküli lap is visszaazonosítható, ezért nem névtelen” · „**Név nélkül:** begyűjtöd gyorsan a jegyzetlapokat (kis csoportban ez sem névtelen, lásd 4.2)”
- **Hatás:** elsikkad az adatvédelmi lényeg: attól, hogy a lapon nincs név, a lap még nem anonim.
- **Javaslat:**
  - :334 – OLD: „ezért nem névtelen:” → NEW: „ezért nem tekinthető anonimnak:”
  - :398 – OLD: „(kis csoportban ez sem névtelen, lásd 4.2)” → NEW: „(kis csoportban ez sem anonim, lásd 4.2)”
  - Változatlan marad a 30 napos megsemmisítés, a „csak a kérdéseket” és a személyes adatról szóló mondat.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M6.F:508 (5. képzői lista, 2. pont)
- **Probléma:**
  - Hét tagmondatos sor, pontosvesszővel toldva.
  - A végén álló „helyette” előzménye kétértelmű: a legközelebbi főnév „a szabad szöveges válaszait”.
  - Ugyanezt a 2.1 pont (:96) három mondatban mondja, kiírt „A közös eszköz helyett” alakkal.
- **Bizonyíték:** „… és törli a letöltéseit, hogy a szabad szöveges válaszait más ne lássa; helyette papír vagy saját eszköz is választható.”
- **Hatás:** a pipálható pont nehezen olvasható, és nem egyértelmű, minek a kiváltásáról szól az utolsó tagmondat.
- **Javaslat:**
  - OLD: a teljes pont.
  - NEW: „A közös eszközön mindenki a saját fiókjával dolgozik, jelszót nem ment el, és személyes munkapéldányt nem hoz létre. A munka végén kijelentkezik, ellenőrzi, hogy a munkamenet lezárult, és törli a letöltéseit, hogy a szabad szöveges válaszait más ne lássa. A közös eszköz helyett papír vagy saját eszköz is választható.”
  - Tilos a protokoll bármely elemét elhagyni.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M6.F:474 (`@asset` spec, a 2. blokk)
- **Probléma:**
  - A protokoll belső vesszői összefolynak a 2. blokk elemeit elválasztó vesszőkkel.
  - Úgy is olvasható, hogy az offline lecke is az „alternatíva” része.
  - Főnévtorlódás: „saját fiókkal belépés jelszómentés és személyes munkapéldány nélkül”.
- **Bizonyíték:** „…kijelentkezés, munkamenet-ellenőrzés és a letöltések törlése, alternatívaként papír vagy saját eszköz, az M6.1 és az M6.2 offline letölthető leckeváltozata, …”
- **Hatás:** a specből generált, AI-s ellenőrzőlista rosszul tagolhatja a pipálható pontokat.
- **Javaslat:**
  - OLD: „wifi/Moodle/H5P, a közös eszközön saját fiókkal belépés jelszómentés és személyes munkapéldány nélkül, kijelentkezés, munkamenet-ellenőrzés és a letöltések törlése, alternatívaként papír vagy saját eszköz, az M6.1 és az M6.2 offline letölthető leckeváltozata,”
  - NEW: „wifi/Moodle/H5P; közös eszköz: saját fiókkal belépés, jelszómentés és személyes munkapéldány nélkül, kijelentkezés, munkamenet-ellenőrzés, a letöltések törlése, alternatívaként papír vagy saját eszköz; az M6.1 és az M6.2 offline letölthető leckeváltozata,”
  - A többi elem változatlan. Utána `media_manifest.py build`.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-5**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M6.F:96, :474, :508
- **Probléma:**
  - A „személyes munkapéldány” a döntés (ADV-11) szava.
  - A képzői szöveg nem mondja meg, mit jelent a gyakorlatban: letöltött fájlmásolatot, böngészőprofilt vagy mentett piszkozatot.
- **Bizonyíték:** „jelszót nem ment el, és személyes munkapéldányt nem hoz létre rajta.”
- **Hatás:** a képző nem tudja a tilalmat elmagyarázni vagy ellenőrizni (adatvédelmi kikötés).
- **Javaslat:**
  - EMBERI DÖNTÉS: mit ért a döntés „személyes munkapéldány” alatt, és kell-e hozzá rövid, képzőnek szóló példa. Kitől: LMS-gazda + DPO, az ADV-11 gazdái.
  - A tilalom addig változatlan, magyarázatot nem írunk hozzá.
- **Típus:** emberi-döntés
- **Verdikt:** —

**M6:QA-NYELV-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M6.A:182 (2.3), :712 (5. lista), :10 (`@asset` spec)
- **Probléma:**
  - A „kötelező megállítási protokoll” sehol nincs azonosítva, a hivatkozás körbe mutat:
    - a 2.3 a 4.3.2/B-t csak az érzékenység indoklásánál említi;
    - az 5. lista „(2.3)”-ra mutat vissza.
  - A terv BLOCK 61-e ezt kifejezetten tartalmazta, de a végszövegből kimaradt: „a kötelező megállítási protokoll a 4.3.2/B négy lépése”.
  - A „…vagy azonnal elérhető helyettes és kötelező megállítási protokoll” mellérendelés azt is sugallhatja, hogy két felnőttnél a megállítási lépés nem kell.
- **Bizonyíték:** „vagy azonnal elérhető helyettes és kötelező megállítási protokoll.” · „…és a kötelező megállítási protokoll (2.3).”
- **Hatás:** a képző nem tudja, mi az, aminek pipáláskor „meg kell lennie”.
- **Javaslat:**
  - :182 – OLD: „…és kötelező megállítási protokoll.” → NEW: „…és kötelező megállítási protokoll (itt: a 4.3.2/B négy lépése).”
  - :712 – OLD: „(2.3).” → NEW: „(4.3.2/B; lásd 2.3).”
  - :10 – a spec „kötelező megállítási protokoll” szövegrésze után: „(4.3.2/B)”, utána build.
  - A döntés szövege nem változik: két 18+ felelős vagy helyettes, az egyszemélyes működés kivétele, felkavart kiskorú nem marad egyedül.
  - Ha a 4.3.2/B nem számít a döntés szerinti protokollnak: EMBERI DÖNTÉS (Memuna + programvezető).
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M6.A:462–466 (4.3.1, Tiltott zóna)
- **Probléma:**
  - A cím szerint a keret „kötelező”.
  - A zárójeles mondat viszont a „soha nem maradhat el” szabályt kiskorú résztvevőkre szűkíti. Ebből az következik, hogy felnőttekkel elhagyható.
  - A GYV-17 „a kiskorúakra … is térjen ki” része a keret tartalmára utal, ez pedig a szövegben nem jelenik meg.
- **Bizonyíték:** „**Tiltott zóna (kötelező, a játék indítása előtt mondd ki röviden):**” · „*(Kiskorú résztvevőkkel ez a keret soha nem maradhat el.)*”
- **Hatás:** a képző 18+ madrihjelölteknél kihagyhatónak olvashatja a keretet.
- **Javaslat:**
  - EMBERI DÖNTÉS: mit jelent az M6.A-ban a „kiskorúakra is térjen ki”. Kitől: Memuna + a peula tartalomfelelőse, a GYV-17 QA-ján belül; a terv már QA-ra jelöli.
  - A „kötelező” címke nem gyengülhet. Helyettesítő mondatot nem javaslok.
- **Típus:** emberi-döntés
- **Verdikt:** —

**M6:QA-NYELV-8**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M6.1:9, M6.2:9, M6.3:9; a párjuk M6.1:170, M6.2:118, M6.3:190
- **Probléma:**
  - A „választó” főnév jelentése szavazó, illetve elválasztó. A fájl többi helye „választós kérdés”-t és „a választás”-t ír.
  - A completion-sorból kimaradt az „önálló” minősítő. A runtime-doboz és a döntés (ERT-2) szava: „nem önálló completion-elem”.
- **Bizonyíték:** „a SLIDE 1 pontozatlan választója nem completion-elem;” · „A választás pontozatlan, nem önálló completion-elem,”
- **Hatás:** egy fogalomra két megnevezés jut, és a két helyen eltér a minősítő.
- **Javaslat:**
  - OLD: „a SLIDE 1 pontozatlan választója nem completion-elem;” → NEW: „a SLIDE 1 pontozatlan választós kérdése nem önálló completion-elem;” – mindhárom lecke 9. sorában.
  - A completion-feltétel (az összefoglaló dia elérése) változatlan.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M6.1:170, M6.2:118, M6.3:190 (a runtime-doboz utolsó mondata); KAPU:392
- **Probléma:**
  - Élettelen főnév áll cselekvő alanyként, angol tükörfordításként.
  - A próbálkozás nem „rögzít”: abban rögzül valami. A döntés (ADV-4) helyesen fogalmaz: „lehetőleg ne rögzítsük a követett H5P próbálkozásban”.
  - A KAPU-ban a „visszajelzés figyeljen” ugyanez a minta.
- **Bizonyíték:** „és lehetőleg ne rögzítse a követett H5P próbálkozás” · „és a társak pontozás nélküli visszajelzése is ugyanezekre a jegyekre figyeljen.”
- **Hatás:** a buildelő és az értékelő természetellenes, nehezen értelmezhető mondatot kap.
- **Javaslat:**
  - Runtime-doboz, 3 helyen – OLD: „és lehetőleg ne rögzítse a követett H5P próbálkozás” → NEW: „és lehetőleg ne rögzüljön a követett H5P próbálkozásban”
  - KAPU:392 – OLD: „és a társak pontozás nélküli visszajelzése is ugyanezekre a jegyekre figyeljen.” → NEW: „és a társak is ugyanezekre a jegyekre figyeljenek, amikor pontozás nélkül visszajeleznek.”
  - A „lehetőleg” minősítő és a hivatkozások maradnak.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-10**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** HUB:122; M6.4:55 (mikrocél)
- **Probléma:**
  - A birtokos szerkezet tükörfordítás: a visszajelzés nem a döntésé, hanem a döntésre kapott visszajelzés.
  - A HUB-ban az „1–1” nagykötőjellel tartománynak olvasható; a párhuzamos M6.4-mikrocél „egy-egy”-et ír.
- **Bizonyíték:** „a döntések visszajelzéséből megismerni …, és a saját helyzetéhez legalább 1–1 ilyet megnevezni,” · „a döntéseid visszajelzéséből megismered a …”
- **Hatás:** a tanulói mikrocél nem hangzik magyarul.
- **Javaslat:**
  - HUB:122 – OLD: „a döntések visszajelzéséből” → NEW: „a döntésekre kapott visszajelzésből”
  - HUB:122 – OLD: „legalább 1–1 ilyet” → NEW: „legalább egy-egy ilyet”
  - M6.4:55 – OLD: „a döntéseid visszajelzéséből” → NEW: „a döntéseidre kapott visszajelzésből”
  - A PRG-2 szűkítés tartalma nem változik. Az M6.4-ben látható szöveg változik, ezért pin kell.
- **Típus:** objektív
- **Verdikt:** —

**M6:QA-NYELV-11**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M6.3:550 (SLIDE 3, Variációk; tanulói szöveg)
- **Probléma:**
  - Az új pontból hiányzik az állítmány: nem derül ki, mi lehetséges „csak akkor, ha”.
  - Megtöri a lista „feltétel/címke: változat” párhuzamát.
- **Bizonyíték:** „* online változat (közös digitális „fal”) csak akkor, ha a szervezet jóváhagyta az eszközt, vagyis tudjuk, ki üzemelteti, …”
- **Hatás:** a tanuló töredékes mondatot olvas egy adatvédelmi feltételnél.
- **Javaslat:**
  - OLD: a teljes pont.
  - NEW: „* online: közös digitális „fal”, de csak akkor, ha a szervezet jóváhagyta az eszközt (tudjuk, ki üzemelteti, milyen adatot kezel, meddig őrzi, és kinek adja tovább); addig a papíros plakát az alap.”
  - A jóváhagyás, a négy ismérv és a papíros alapértelmezés nem változik. A látható szöveg változik, ezért pin kell.
- **Típus:** objektív
- **Verdikt:** —

