# 2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), AP-2026-10-12-01

- **Scope:** a Z modul HUM 14. szakasz szerinti átvezetésének diffje (`c5bc2c4`), csak a módosított sorok és közvetlen környezetük. Nem teljes új audit.
- **Lencsék (ténylegesen lefutott):** biztonság-jog (`safety-policy-reviewer`), értékelés + LMS (`assessment-reviewer`, IMPL-tételekkel), nyelv (`hungarian-editorial-reviewer`). Adverzális második kör: `verifier`, mind a 20 ID-ra és a fő session egy saját tételére (Z:QA-NYELV-11).
- **Run-ID:** AP-2026-10-12-01 · **Review-bázis:** `c5bc2c4` (media `56c0f6b`) · **Javítás:** `a0c0c83` (a generált média nem változott); a kánoni rész a `bdb94ab`-ban.
- **Állapot:** VALIDÁLT.

## I. Riport

### 1. Validált objektív findingok — javítva (`a0c0c83`; kánon: `bdb94ab`)

| ID | Súly | Hely | Javítás |
|---|---|---|---|
| Z:QA-IMPL-1 (LMS-1, ADV-14) | P1 | Z.4:303, :336; manifest LMS-Z-04 | a dokumentumos fájlút a sablonhoz megmarad; csak a videós út kikapcsolt, külön DPO-profilon |
| Z:QA-IMPL-2 (ERT-1, ERT-2, ADV-4) | P2 | Z.2:13, Z.3:59; manifest LMS-Z-02/-03 | összefoglaló diás completion csak ott, ahol van összefoglaló dia; különben a build-spec gazda rögzíti a legitim alapot |
| Z:QA-NYELV-2 (GYV-11) | P2 | Z.4:359 | az automatikus törlés tilalma a gyermekvédelmi feltárást tartalmazó beadásra szól |
| Z:QA-IMPL-4 (+ QA-NYELV-8; ADV-3) | P2 | Z.3:339 | a „tanuló-lokális, beviteli elem nélkül” csak a szöveges válaszra vonatkozik |
| Z:QA-NYELV-6 (PRG-6) | P2 | Z.3:217, HUB:95 | „ha a Peula v2-d még nincs kész” mindenütt |
| Z:QA-ERT-3 (ERT-39) | P2 | Z.4:402, HUB:194; manifest LMS-Z-05, RA 16 | a visszajelző űrlap a §7 szerinti dátummal nyílik, jelenléti feltétel nélkül |
| Z:QA-NYELV-10 (RÉSZBEN) | P3 | Z.4:398 | zárójel a zárójelben feloldva |

### 2. Emberi döntést igénylő tételek

| ID | Mit kell eldönteni | Kitől |
|---|---|---|
| Z:QA-NYELV-1 (+ QA-ERT-1; ERT-38) | a „Teljesítve” alsó határa: mindhárom szakaszban kell-e értelmezhető tartalom (az érzékeny rész passzolható), vagy elég a beadás egészének értelmezhetősége; a döntés után a Z.4:98, :329, :343, :347, :353, a HUB:185 és a manifest LMS-Z-08 együtt igazodik | értékelési felelős; vétó/QA: programvezető |
| Z:QA-ERT-2 (ERT-38) | hogyan jelzi a tanuló a passzt, és mi a mentor első lépése üres szakasznál | értékelési felelős, a DPO-val |
| Z:QA-BIZT-1 (GYV-11) | kiterjed-e a GYV-11 megőrzési kivétele a Z.4 Feedback nyers válaszaira (ADV §3 „90 nap”); szabad-e a tárolt felhasználónévvel visszakeresni; kell-e tájékoztató mondat a :370-be. Ha nem, a :401 GYV-11-tagmondata kikerül; a Memuna-bevonás és a HUM-SAFE-01 rész marad | Memuna + DPO |
| Z:QA-BIZT-2 (GYV-8) | kerüljön-e a Z.3 terepi mintamondatába „közvetlen veszélyben előbb a biztonság és a 112” | Memuna + programvezető |
| Z:QA-BIZT-3 (ADV-7) | személyes, önfeltáró cetlinek számít-e az egyszavas szófelhő-cetli | DPO / jogi felelős |
| Z:QA-IMPL-3 (ERT-3) | mit jelent a „kiürítés” (az RA 16 tesztje ezután végrehajtható) | projektgazda mint build-spec gazda; QA: értékelési felelős |

### 3. Bizonyíték-kapu

Nincs új.

### 4. Elvetve

- Z:QA-NYELV-3, QA-NYELV-4 — a mondat az ERT-38 szóhasználata; a bekezdés a K1-döntés tárgya.
- Z:QA-NYELV-5 — a Z:QA-BIZT-1 blokkolja.
- Z:QA-NYELV-7 — általános megnevezés, érthető.
- Z:QA-NYELV-9 — ízlésbeli alternatíva.
- Z:QA-NYELV-11 — a „18 év feletti” a korpusz és a GK §4:60 alakja.

## B. Verifier-verdiktek (szó szerint)

<!-- agent af28b1e490a320d48 -->

Adverzális második kör: a Z célzott QA-findingjai (c5bc2c4, AP-2026-10-12-01). Read-only maradtam, egy fájlt sem módosítottam. A vizsgált fájlok: 02 Tervezet/Modulok/Z/ (HUB, Z.2, Z.3, Z.4, Z.A), és mellettük a HUM 14. szakasz, a manifest, a GK, a hozzáférhetőségi sztenderd és a döntési csomag.

Z:QA-NYELV-1 | MEGERŐSÍTVE (a K1 megtartandó ID-je) | emberi-döntés | P1 | Az ellentmondás valós, és a c5bc2c4 hozta be. A Z.4:343 Completion rule ezt írja: „ha a beadás előírt részeiben (a három szakaszban; …) tényleges, minimálisan értelmezhető tartalom van”. A Z.4:347 ezt: „ha egy eleme hiányzik, de a beadás értelmezhető, akkor is „Teljesítve” jár”. Az ERT-38 (HUM:708) nem dönti el, hogy szakaszonként vagy a beadás egészére kell-e tartalom. A „minimálisan értelmezhető, tényleges beadás” és a „három részes … szerkezet legyen formatív útmutató” az egészre utaló olvasatot erősíti. A csomag elfogadott (b) opciója viszont („mint az M2/M4-nél, MAN:173”) az „előírt mezőkben” mércére utal, és ugyanezt mondja a MAN:111 LMS-Z-08 is. | Döntési igény az értékelési felelőstől (vétó/QA: programvezető). (i) Mindhárom szakaszban kell-e értelmezhető tartalom (az érzékeny rész passzolható)? Ekkor a Completion rule és az LMS-Z-08 marad, és a Z:QA-ERT-1 három OLD → NEW cseréje átvehető (:347, :353, valamint :98/:329/HUB:185). (ii) Vagy elég, ha a beadás egésze értelmezhető? Ekkor a :343 zárójele és a MAN LMS-Z-08 „előírt mezőiben” fordulata módosul. A döntésig a :98, :329, :343, :347, :353, HUB:185 és a MAN #58 blokk egyike sem írható át, nyelvi alapon sem.

Z:QA-ERT-1 | MEGERŐSÍTVE (duplikátum → Z:QA-NYELV-1) | emberi-döntés (az objektív besorolás téves) | P1 | Ugyanaz az ellentmondás (Z.4:343 ↔ :347). A javaslat előre a szűkebb olvasatot választja, és az ERT-38 ezt nem mondja ki. | Önálló objektív javításként nem használható. Csak a K1 (i) ágában vehető át szó szerint.

Z:QA-ERT-2 | MEGERŐSÍTVE | emberi-döntés | P2 | A passz jelzésének módja sehol nincs leírva. Z.4:329: „adatvédelmi szempontból érzékeny részt kihagyhatsz”. Z.4:355: „„Még nem teljesítve” … hogy mivel egészítse ki”. A probléma a K1 (i) olvasatában éles. | Döntési igény az értékelési felelőstől a DPO-val, célszerűen a K1 döntéssel együtt: hogyan jelzi a tanuló a passzt, és mi a mentor első lépése üres szakasznál. A Z.4:167 és a GYV-11 nem gyengülhet.

Z:QA-NYELV-3 | ELVETVE | — | — | A Z.4:98/:329 mondata („útmutató, nem bukási feltétel”) az ERT-38 saját szóhasználatához igazodik. A „(például a legalább 3 pillanat)” nem alaptag nélküli. A javasolt NEW („csak útmutató, nem a teljesítés feltétele”) a K1 előtt értékelési jelentést tolna el. A mondat úgyis újraíródik a K1 döntés után. | —

Z:QA-NYELV-4 | ELVETVE | — | — | Z.4:347: „Ezeket érdemes szem előtt tartani:”. A kettőspont után közvetlenül a lista jön, ezért az „Ezeket” előre mutat, a magyarban ez szabályos. A bekezdés amúgy is a K1 döntés tárgya. | —

Z:QA-IMPL-1 | MEGERŐSÍTVE (K3) | objektív | P1 | A c5bc2c4 a teljes fájlutat kikapcsolta: Z.4:336 „File submissions: **OFF** – a videós út alapból ki van kapcsolva”. Az ADV-14 (HUM:660) csak a videót kapcsolja ki. Az LMS-1 (HUM:738) kimondja: „Az egyenértékű online szöveges és fájlfeltöltéses út maradjon. … A Z.4 videó csak külön, DPO által engedélyezett profilon szerepelhet.” A csomag forrásként maga hivatkozza a Z.4:303/:336 sort, és a (A) opció egyik eleme: „a Z.4 videós útja külön profil”. A fájlutat megköveteli az ASSIGN-S profil is (MAN:19: „online text **és** fájlút, hozzáférhető sablon”), a hozzáférhetőségi sztenderd 4. szakasza (:46–47), és a Z.4:81 letölthető sablonja sem adható be nélküle. Az „OFF” tehát túlmegy az ADV-14-en, és regresszió. | :336 OLD: „File submissions: **OFF** – a videós út alapból ki van kapcsolva (projektgazdai döntés, 2026-10-12, ADV-14). Csak akkor kapcsolható be (ekkor: ON, max 1 file, max size 100–200 MB), ha” → NEW: „File submissions: **ON** a dokumentumos úthoz (LMS-1): legfeljebb 1 fájl; az elfogadott fájltípusok a tényleges akadálymentes sablonhoz igazítva (például .docx, .odt, .pdf); képfeltöltés vagy képernyőkép nem szükséges és nem ösztönzött. A videós út alapból ki van kapcsolva (projektgazdai döntés, 2026-10-12, ADV-14): csak külön, DPO által engedélyezett profilon kapcsolható be (ekkor: max 1 file, max size 100–200 MB), ha”. A mondat többi része változatlan. :303 OLD: „File submission – opcionális videós út, alapból kikapcsolva” → NEW: „File submission – dokumentumos út a sablonhoz (LMS-1); a videós út külön profil, alapból kikapcsolva”. Korlátok: végleges fájltípus-lista nem kerülhet be (csak az LMS-1 „például” alakja), videós típus sem. Az ADV-14 feltételei, a „puszta fájlfeltöltés nem elég” és a tanulói videós mondatok feltételessége változatlan. Új tanulói szöveg nem kerül be. A MAN #57 blokkja nem azonosíthatja a File submissiont a videós úttal.

Z:QA-NYELV-2 | MEGERŐSÍTVE | objektív | P2 (P1-ről lefokozva: a mostani olvasat a megőrzés irányába téved, nem a törlés irányába) | Z.4:359: „A különleges adatot a HUM-PRIV-01 szerint kezeljük (…). A beadás nem az incidens elsődleges nyilvántartása; kezeléséhez … automatikusan nem töröljük.” A pont fejléce a különleges adatot is lefedi. A GYV-11 csak a „gyermekvédelmi feltárásnál” szól. | A finding OLD → NEW cseréje szó szerint átvehető („A gyermekvédelmi feltárást tartalmazó beadás nem az incidens elsődleges nyilvántartása. Az ilyen beadás kezeléséhez …; jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük.”). Korlát: egyik GYV-11-feltétel sem hagyható el. A pótlási út és a „Teljesítve”-mondat változatlan.

Z:QA-BIZT-1 | MEGERŐSÍTVE (a K4 megtartandó ID-je) | emberi-döntés | P1 | A GYV-11 szó szerinti szövege (HUM:634): „Tárolt beadandóba kerülő gyermekvédelmi feltárásnál”. A csomag kérdése még a Feedback-ágat is említette (:301, „vagy visszajelzésben”), az elfogadott szöveg viszont már nem. A Z.4:401 Feedback-ágra alkalmazás ezért új alkalmazási eset, és ütközik az ADV §3 „Z visszajelzés nyers válaszai | 90 nap” sorával. | Helyes kezelés a :401 betoldásánál. A kánoni rész megmarad: „a válaszokat feldolgozó azonnal bevonja a Memunát (az ötlépéses jelzési út szerint), az ügy dokumentációja … az incidensnyilvántartásban készül (HUM-SAFE-01)”. Ez GK §4.1 és HUM-SAFE-01 (GK:82, :84), nem törölhető. A GYV-11-többlet BLOCKED_HUMAN: „és ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük; a korlátozáshoz … (projektgazdai döntés, 2026-10-12, GYV-11)”. Ebben a javítási körben egyik irányba sem írandó át. Döntési igény a Memunától és a DPO-tól: (a) kiterjed-e a GYV-11 megőrzési kivétele a Feedback nyers válaszaira, és hogyan módosul az ADV §3; (b) szabad-e az adatbázisban tárolt felhasználónévvel visszakeresni a válaszadót; (c) kell-e a :370-be a :201 mintájára tájékoztató mondat. Ha (a) nem, a tagmondat és a GYV-11-hivatkozás kikerül a Feedback-ágból.

Z:QA-NYELV-5 | ELVETVE | — | — | A Z.4:401 mondata olvasható. Megfogalmazását a Z:QA-BIZT-1 blokkolja: a nyelvi átírás rögzítené egy függő tagmondat szövegét. A Memuna- és DPO-döntés után a mondatot úgyis újra kell írni. | —

Z:QA-BIZT-2 | MEGERŐSÍTVE | emberi-döntés | P2 | A Z.3:310 új tagmondata („ha pedig akut kockázatot látok, a Memunát is azonnal bevonom”) a GYV-8 szó szerinti átvezetése (HUM:631: „akut kockázatnál Memuna is”). A dián (:301–316) nincs 112. A GK §4.1:82 megengedi a rövid utalást, ahol a teljes felsorolás nem a hely feladata: „elég az utalás: … „azonnal vond be a Memunát””. A mostani szöveg tehát kánonkonform. A 112 (GK:78, 5. lépés) bevitele a mintamondatba új alkalmazás lenne, nem szó szerinti átvezetés, és a mintamondat egyben az LMS-Z-07 elfogadási tárgya. | Döntési igény a Memunától és a programvezetőtől (a GYV-8 jóváhagyói): kerüljön-e a mintamondatba „közvetlen veszélyben előbb a biztonság és a 112”. A „jelzem a képzőnek” és az „akut kockázatnál Memuna is” tagmondat nem törölhető, az LMS-Z-07 kritériuma változatlan.

Z:QA-BIZT-3 | MEGERŐSÍTVE | emberi-döntés | P2 | Z.A:41: „a személyes, önfeltáró cetli … nem gyűjtjük be (a szófelhő cetlijére nem kerül név, 4.4.2)”. Z.A:40 a szófelhőt fotózható csoportproduktumnak nevezi, a 4.4.2 (:464–472) pedig nem mondja meg, mi lesz a cetlikkel. A besorolás adatvédelmi kérdés, és kétesnél a szabály emberi döntést kér. | Döntési igény a DPO-tól vagy a jogi felelőstől (az ADV-7 vétó/QA-szerepe): személyes, önfeltáró cetlinek számít-e az egyszavas szófelhő-cetli. Korlát: a „nincs fotó” alapértelmezés, a HUM-PRIV-02-feltétel, a „Nevet ne írj rá” és a saját telefonra vonatkozó tilalom nem gyengülhet.

Z:QA-IMPL-4 | MEGERŐSÍTVE (a K2 megtartandó ID-je) | objektív | P2 | A c5bc2c4 regressziója. A Z.3:339 címe („Beágyazott kérdés – Single Choice + rövid szöveges válasz (opcionális, tanuló-lokális)”) a CP-be ágyazott Single Choice-ra is kiterjeszti a „tanuló-lokális” jelzőt. A Z.3:59 szerint ezt a követett próbálkozás „lehetőleg ne” rögzítse, beviteli elem nélküli csak a :360 mini válasza. | OLD: „**Beágyazott kérdés – Single Choice + rövid szöveges válasz (opcionális, tanuló-lokális)**” → NEW: „**Beágyazott kérdés – Single Choice (opcionális) + rövid szöveges válasz (opcionális, tanuló-lokális, beviteli elem nélkül)**”. A „beviteli elem nélkül” a :360-ból szó szerint jön. A Single Choice besorolása és a :360 változatlan.

Z:QA-NYELV-8 | MEGERŐSÍTVE (duplikátum → Z:QA-IMPL-4) | objektív | P2 | Ugyanaz a Z.3:339 cím. | Az összehangolt cserét lásd a Z:QA-IMPL-4-nél.

Z:QA-NYELV-6 | MEGERŐSÍTVE (a K5 megtartandó ID-je) | objektív | P2 | A PRG-6 (HUM:726) szövege: „a Z.3 v1-út azoknak is működjön, akiknek az M7 v2-je még nincs kész”. A Z.3:217 (baseline) ezt írja: „Ha a Peula v2-det még nem adtad le” – ez szűkebb, kizárja a leadott, de „Még nem teljesítve” v2-t. A közvetlenül alatta álló :219 és a :281 a döntés alakját használja. A HUB:95 („az M7-ben elkészített Peula v2-jéhez (ha az még nincs kész …”) önellentmondó. | A finding két OLD → NEW cseréje szó szerint átvehető. Z.3:217: „Ha a Peula v2-det még nem adtad le, mert” → „Ha a Peula v2-d még nincs kész, mert”. HUB:95: „a tanuló az M7-ben elkészített Peula v2-jéhez (ha az még nincs kész, mert az M7 javítási útján van, a Peula v1-éhez; PRG-6) konkrét terepi tervet ír” → „a tanuló az M7-ben elkészített Peula v2-jéhez – vagy, ha az M7 javítási útján van, és a v2-je még nincs kész, a Peula v1-éhez (PRG-6) – konkrét terepi tervet ír”.

Z:QA-NYELV-7 | ELVETVE | — | — | HUB:33: „a javító beadás időpontját”. Ez általános megnevezés, a PRG-6 maga is általánosan fogalmaz („a mentor jelölje ki a javító időpontját”). Az „elfogadása „Még nem teljesítve”” a fejlesztői hubban a GATE-CP mezőértékre utal, és érthető. Bizonyított nyelvi hiba nincs. | —

Z:QA-ERT-3 | MEGERŐSÍTVE | objektív | P2 (baseline, nem regresszió) | Z.4:402: „**Feloldás:** a Z.A után (manifest LMS-Z-05)”. HUB:194: „a visszajelző űrlap: „Z.A után”, LMS-Z-05”. Közvetlenül előtte a reflexiónál ez áll: „Z.A után, a §7 szerinti dátummal”. A MAN:295 szerint a `Z_FEEDBACK` nyitása is „`SCHEDULE_TO_RESYNC`, a Z.A után”, vagyis dátumhoz kötött. Az ERT-39 (HUM:709) szerint a hiányzó jelenlét nem akadályozhat. | Z.4:402 OLD: „a Z.A után (manifest LMS-Z-05)” → NEW: „a Z.A után, a §7 szerinti dátummal (`Z_FEEDBACK`; manifest LMS-Z-05)”. HUB:194 OLD: „a visszajelző űrlap: „Z.A után”, LMS-Z-05” → NEW: „a visszajelző űrlap: „Z.A után, a §7 szerinti dátummal”, LMS-Z-05”. Jelenléti feltétel nem kerülhet be. A MAN:112 LMS-Z-05 sorát és az RA 16-ot a kánoni kör igazítja.

Z:QA-IMPL-2 | MEGERŐSÍTVE | objektív | P2 (P1-ről lefokozva: a Z.2:13 maga is jelzi a célverziós igazolást, RA 9) | A Z.2:13 és a Z.3:59 feltétel nélkül mondja ki: „A Course Presentation completionje az összefoglaló dia elérése (ERT-1)”, holott a két CP-ben csak pontozatlan választók vannak. Az ERT-1 (HUM:671) szó szerinti korlátja hiányzik: „Csak olyan CP kapjon erre épülő completiont, amelynek valóban van összefoglaló diája”. A csomag ERT-1 ajánlása (:735) ugyanezt a feltételt köti ki, és a Z:IMPL-G1-7-re hivatkozik. | Mindkét helyen a célverziós mondat után álljon: „Csak olyan CP kapjon erre épülő completiont, amelynek valóban van összefoglaló diája (ERT-1); ha a célverzión nincs, a completion-alapot (megtekintés/összefoglaló vagy más legitim aktivitás, ERT-2) a projektgazda mint build-spec gazda rögzíti, és a választó nem lehet pontozott vagy önálló completion-elem (ERT-2, ADV-4).” Korlát: konkrét alternatív technikát a javítás nem választ.

Z:QA-IMPL-3 | MEGERŐSÍTVE | emberi-döntés | P2 | A „kiürítés” csak idézőjelben szerepel az ERT-3-ban (HUM:673), és a repóban sehol nincs meghatározva (3 találat, mind idézet). A Z.4:400 szó szerint, helyesen vezeti át. A hiba nem a Z-szövegben van: az RA 16 teszt végrehajthatatlan. | Döntési igény a projektgazdától mint az ERT-3 build-spec gazdájától (QA: értékelési felelős): mit jelent a „kiürítés”. Utána az RA 16 (kánoni kör), szükség esetén a Z.4:400 pontosul. Addig a Z.4:400 nem írható át találgatásból.

Z:QA-NYELV-9 | ELVETVE | — | — | A „ha a kurzusban a videós beadás be van kapcsolva” helyes és egységes feltétel, az „elérhető” csak ízlésbeli alternatíva. A Z.4:16 dőlt „videós út” baseline szöveg. Bizonyított hiba nincs. | —

Z:QA-NYELV-10 | RÉSZBEN | objektív | P3 | (b) Valós tipográfiai hiba: a Z.4:398-ban zárójelen belül zárójel áll: „(projektgazdai döntés, 2026-10-12, ADV-15; utólagos ellenőrzés (vétó/QA): …)”. (a) A Z.3:59-ben az új „a cél verzión kell igazolni” mellett ugyanabban a bekezdésben a régi „tesztelni a cél verzión” is ott áll. Ha csak az újat javítjuk, a bekezdésen belül vegyes írásmód lesz; a különírás korpusz-szintű baseline (Z.1:55, :57, Z.2:61, :63, Z.3:57). | Csak a (b): „utólagos ellenőrzés (vétó/QA):” → „utólagos ellenőrzés [vétó/QA]:”. Az (a) külön, korpusz-szintű nyelvi körbe tartozik.

Z:QA-NYELV-11 | ELVETVE | — | — | A premissza egy ponton téves. Az M3.B:275 nem „18+”, hanem „felkészített, 18 év feletti” alakot használ, ugyanúgy, mint az M0.A:94 és az M7.B:565. „18+” csak az M2.A:65-ben és az M6.A:182-ben áll. Ugyanerre a szerepre a GK §4:60 kánonja is „18 év feletti felnőtt”-et ír. A korpusz a 18 évest a „felett” csoportba sorolja: HUB:183 „18 év alatt … 18 év felett a résztvevő”. A Z.A:59 alakja tehát nem bizonyítottan jelentésváltoztató, és megfelel a hungarian-editorial „`+` helyett rendes mondat” szabályának. | —

Összesen: 14 MEGERŐSÍTVE (ebből 2 duplikátum: Z:QA-ERT-1 → Z:QA-NYELV-1, Z:QA-NYELV-8 → Z:QA-IMPL-4), 1 RÉSZBEN, 6 ELVETVE. Bizonyíték-kapu: 0. A megerősítettekből 7 emberi döntés (NYELV-1, ERT-1, ERT-2, BIZT-1, BIZT-2, BIZT-3, IMPL-3) és 7 objektív (IMPL-1, NYELV-2, IMPL-4, NYELV-8, NYELV-6, ERT-3, IMPL-2); a RÉSZBEN (NYELV-10 (b)) szintén objektív.

## C. Nyers lencse-kimenetek (szó szerint)

<!-- agent aa60ff5e591535c72 -->

Célzott QA, biztonság-jog lencse, Z (c5bc2c4, AP-2026-10-12-01). Read-only maradtam: csak a diff hunkjait és a hozzájuk közvetlenül kapcsolódó mondatokat néztem, a terv, a HUM 14. szakasza, a GK §4 és §4.1–4.3, valamint az ADV §3 és §5 alapján.

**Eredmény:** 3 finding (1×P1, 2×P2), mindhárom `emberi-döntés`, objektív javítandó nincs köztük.

**Rendben találtam:**
- **ADV-14 / LMS-1:** nem maradt feltétel nélküli videós ígéret. A Z.4 :293 és :278 a tanuló választásához köti a videót, ez csak bekapcsolt útnál lehetséges. A HUB :56 kompetencia vagylagos megfogalmazás, nem ígéret. A hozzájárulási mondat megvan (Z.4 :117 és :310, HUB :183).
- **ADV-15, ERT-3, ADV-1:** mindhárom szó szerint átvezetve. Az ADV-1 mindhárom „csak a mentorod látja” helyen megjelent (Z.4 :98, :307, :329). Az RBAC-igazítás külső függőség, ezt precedensként nem jelentem.
- **ADV-3 / ADV-4:** átvezetve.
- **GYV-5:** szó szerint átvezetve, megegyezik az M0.A, M2.A, M3.B és M6.A szövegével. A megállítási protokoll tartalmát nem nevezi meg.
- **GYV-6:** a sorrend jó (meghallgatás és biztonság, gyermekvédelmi aggálynál azonnal a Memuna), a GK §4:63–64 minimuma benne van. A madrih nem kap egyedüli felelős szerepet.
- **GYV-11, Assignment-ág (Z.4 :359):** a döntés minden eleme megvan, többlet nélkül.

---

- **ID:** Z:QA-BIZT-1
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md` > Moodle Feedback, Beállítás-javaslatok, „Megőrzés” (:401); kapcsolódik a :370 tanulói leíráshoz.
- **Probléma:** A GYV-11 Feedback-ága eljárást ír elő a név nélkül megjelenő visszajelzésekre: azonnal be kell vonni a Memunát, és a választ nem töröljük automatikusan a 90 napos megőrzés végén. Három kérdés nyitva marad:
  - Visszakereshető-e a válaszadó a feltárás kezeléséhez? A felhasználónév az adatbázisban akkor is tárolódik, ha a felületen név nélkül jelenik meg.
  - Kap-e erről a tanuló tájékoztatást? A :370 csak arra kéri, hogy ne csak az űrlapba írjon. Nem mondja ki, hogy a válasz a Memunához kerül, és tovább megőrizhetjük. Az Assignment-ágban a :201 ezt kimondja.
  - Alkalmazható-e egyáltalán a GYV-11 a Feedbackre? A döntés szövege „tárolt beadandó”-ról szól. A Feedbackre alkalmazva kivételt nyit a DPO-mátrix „Z visszajelzés nyers válaszai | 90 nap” sora alól (ADV §3 :70).
  - Besorolás:
    - TÉNY: az adatbázis-tárolás (Moodle-dokumentáció).
    - PROJEKT-DÖNTÉS: a Memuna bevonása és a HUM-SAFE-01 szerinti dokumentálás (GK §4.1).
    - EMBERI JÓVÁHAGYÁS KELL: a megőrzési kivétel, a visszakereshetőség és a tájékoztatás.
- **Bizonyíték:**
  - Fájl: „Ha egy válasz gyermekvédelmi feltárást tartalmaz, a válaszokat feldolgozó azonnal bevonja a Memunát (…), és ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük”.
  - HUM :634 (GYV-11): „Tárolt beadandóba kerülő gyermekvédelmi feltárásnál ne legyen az LMS az incidens elsődleges nyilvántartása.”
  - Moodle docs, Feedback FAQ (https://docs.moodle.org/en/Feedback_FAQ): „even in Anonymous mode the username of the user who took the Feedback is still recorded in the database just as with non-anonymous Feedbacks, but the name is not show to anyone on screen”.
- **Hatás:** Aki az űrlapot feldolgozza, nem tudja, szabad-e azonosítania a veszélyben lévő válaszadót. A tanuló név nélküli feldolgozást kap ígéretként, de nem tudja, hogy egy feltárás a Memunához kerül, és 90 napon túl is megőrizhetjük. Ez átláthatósági (GDPR) és gyermekvédelmi bizonytalanság.
- **Javaslat:** EMBERI DÖNTÉS: a DPO és a Memuna (a GYV-11 és a HUM-PRIV-03 gazdái) döntsön három kérdésben:
  - (a) Alkalmazható-e a GYV-11 megőrzési kivétele a Z.4 Feedback nyers válaszaira, és hogyan módosul az ADV §3 mátrix.
  - (b) A Memuna-eljárásban szabad-e az adatbázisban tárolt felhasználói azonosítóval visszakeresni a válaszadót.
  - (c) Kell-e a :370-be a :201 mintájára egy „nem ígérünk teljes titoktartást / a Memunához kerül” mondat.
  - Bizonyíték: írásos DPO- és Memuna-döntés.
  - Javítási korlát: a Memuna bevonása és a HUM-SAFE-01 szerinti dokumentálás nem törölhető (GK §4.1).
- **Típus:** emberi-döntés
- **Verdikt:**

---

- **ID:** Z:QA-BIZT-2
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md` :310 (SLIDE 6, a biztonsági lépés mintamondata)
- **Probléma:** A GYV-8 új tagmondata az akut kockázatra csak a Memuna bevonását írja elő. A helyzetben a madrih maga is lehet kiskorú, és nincs jelen 18 év feletti felnőtt. A közvetlen veszélyre a GK §4.1 kánoni 5. lépése „előbb a biztonság és a 112”. Ez sem a mondatban, sem a dián (:301–316) nem szerepel. A Somer telefonja ráadásul nem ügyeleti vonal.
  - Besorolás:
    - PROJEKT-DÖNTÉS: az „akut kockázatnál Memuna is” (GYV-8), valamint a GK §4.1 5. lépése.
    - EMBERI JÓVÁHAGYÁS KELL: hogy a mintamondat utaljon-e a 112-re.
- **Bizonyíték:**
  - Fájl: „…nem vezetek éles foglalkozást, hanem jelzem a képzőnek; ha pedig akut kockázatot látok, a Memunát is azonnal bevonom.”
  - GK §4.1 :78: „**Közvetlen veszélynél előbb a biztonság és a 112**, utána a belső jelzés.”
  - GK §4.1 :87: „Ez nem ügyeleti vonal: munkaidőn kívül és közvetlen veszélyben a 112, illetve a Kék Vonal az út.”
- **Hatás:** A kiskorú madrih az általa vállalt mondatot követve közvetlen veszélyben is a Memunát hívhatja először, nem a 112-t.
- **Javaslat:** EMBERI DÖNTÉS: a Memuna és a programvezető (a GYV-8 jóváhagyói) döntse el, kapjon-e a mintamondat kánoni utalást („közvetlen veszélyben előbb a biztonság és a 112”, GK §4.1 5. lépés). Ha nem, a döntés rögzítse, hogy a „Memunát is azonnal bevonom” közvetlen veszélyben is elegendő-e.
  - Javítási korlát: a „jelzem a képzőnek” és az „akut kockázatnál Memuna is” tagmondat nem törölhető. Az LMS-Z-07 elfogadási kritériuma nem változik.
- **Típus:** emberi-döntés
- **Verdikt:**

---

- **ID:** Z:QA-BIZT-3
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md` :40 (Felvétel), :41 (Papír), 4.4.2 :464–472 (szófelhő)
- **Probléma:** Az ADV-7 átvezetése ugyanazt a tárgyat két ellentétes szabály alá sorolja:
  - A Papír-pont zárójele a szófelhő cetlijét a személyes, önfeltáró cetli példájaként hozza. Ilyen cetlit nem gyűjtünk be: a résztvevőnél marad, vagy visszakerül hozzá.
  - A Felvétel-pont ugyanezt a szófelhőt fotózható csoportproduktumnak nevezi.
  - A 4.4.2-ben a cetlik közös felületre kerülnek, és a lépések nem mondják meg, mi lesz velük a peula után.
  - Besorolás:
    - PROJEKT-DÖNTÉS: az ADV-7 papír- és fotószabálya.
    - EMBERI JÓVÁHAGYÁS KELL: hogy az egyszavas szófelhő-cetli „személyes, önfeltáró”-e.
- **Bizonyíték:**
  - :41: „a személyes, önfeltáró cetli a résztvevőnél marad, vagy visszakerül hozzá; névvel nem függesztjük ki, és nem gyűjtjük be (a szófelhő cetlijére nem kerül név, 4.4.2).”
  - :40: „Szükséges csoportproduktumról (például a „Híd a terepre” poszterről vagy a szófelhőről) csak előre rögzített céllal…”
- **Hatás:** A képző nem tudja, hogy a peula végén visszaadja-e a cetliket, vagy a szófelhőt csoportproduktumként megtarthatja és lefotózhatja.
- **Javaslat:** EMBERI DÖNTÉS: a DPO vagy a jogi felelős (az ADV-7 vétó- és QA-szerepe) mondja ki, hogy a szófelhő-cetli személyes, önfeltáró cetlinek számít-e. Igen esetén a 4.4.2-be visszaadó vagy „nálad marad” lépés kell, és a szófelhő kikerül a fotópéldák közül. Nem esetén a Papír-pont zárójeles hivatkozása a szófelhőre kerül át más alakba.
  - Javítási korlát: a „nincs fotó” alapértelmezés, a HUM-PRIV-02-feltétel, a „Nevet ne írj rá” és a saját telefonra vonatkozó tilalom nem gyengülhet.
- **Típus:** emberi-döntés
- **Verdikt:**

<!-- agent a0adb4cded8a971c6 -->

Célzott QA, Z modul (c5bc2c4), lencse: értékelés és Moodle/H5P-megvalósíthatóság. Read-only; 7 finding: 3×P1, 4×P2.

Fájlok:
- HUB = 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- Z.2 = 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md
- Z.3 = 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- Z.4 = 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- RA = 02 Tervezet/LMS – H5P runtime acceptance.md

---

**Z:QA-ERT-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** értékelés
- **Hely:** Z.4 > Beállítás-javaslatok > Completion rule (:343) ↔ „A „Teljesítve” mércéje és az ideális szerkezet” (:347, :353); a tanulói mondat (:98, :329); HUB:185
- **Probléma:** A „Teljesítve” két mércéje ellentmond egymásnak:
  - A változatlan CONFIRMED-szabály mindhárom szakaszban tényleges tartalmat követel.
  - Az új mérce-szakasz és a tanulói szöveg a beadás egészére szól. Kifejezetten „Teljesítve” jár akkor is, ha a háromrészes szerkezet egy eleme hiányzik.
  - Egy egész, nem érzékeny szakasz hiányára tehát az egyik szöveg szerint „Még nem teljesítve”, a másik szerint „Teljesítve” jár.
- **Bizonyíték:** :343 „ha a beadás előírt részeiben (a három szakaszban; a videós útnál a videóban mindhárom kérdésre kitérve) **tényleges, minimálisan értelmezhető tartalom** van … egyébként „Még nem teljesítve” értéket.” · :347 „az alábbi háromrészes szerkezet formatív útmutató, nem rejtett bukási küszöb: ha egy eleme hiányzik, de a beadás értelmezhető, akkor is „Teljesítve” jár”
- **Hatás:** Két mentor ugyanarra a beadásra ellentétes kapueredményt adhat. A tanuló a „tényleges, értelmezhető beadás kell” mondatból nem tudja előre, hogy szakaszonként kell tartalom, pedig az ERT-38 szerint „a tanulói követelmény előre ismert”.
- **Javaslat:** Igazítsd a szöveget a Completion rule-hoz és a kánoni mércéhez: LMS-Z-08 „előírt mezőiben” (MAN:111), ASSIGN-S (MAN:19, :173). A Completion rule-hoz ne nyúlj.
  - :347 „ha egy eleme hiányzik, de a beadás értelmezhető” → „ha a részletes szerkezet egy eleme hiányzik (például 3-nál kevesebb pillanat, vagy a lépés nem határidős), de mindhárom szakaszban van tényleges, értelmezhető tartalom (az érzékeny rész passzolható)”.
  - :353 „Ha a beadásban nincs …” → „Ha a beadás valamelyik szakaszában nincs … (és nem érzékeny rész passzáról van szó)”.
  - :98, :329 és HUB:185 „tényleges, értelmezhető beadás kell” → „mindhárom szakaszban tényleges, értelmezhető tartalom kell”.
  - Ha az ERT-38 szándéka az, hogy egy egész szakasz is hiányozhat, az a Completion rule és az LMS-Z-08 módosítása. EMBERI DÖNTÉS: értékelési felelős; vétó/QA: programvezető.
- **Típus:** objektív

**Z:QA-ERT-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** Z.4:329 (tanulói leírás), :343, :355
- **Probléma:** A tanuló kihagyhatja az érzékeny részt, de sehol nincs leírva, hogyan jelezze ezt. Így a mentor egy üres szakaszt nem tud megkülönböztetni a passztól. A „Még nem teljesítve” plusz „mivel egészítse ki” visszajelzés épp az érzékeny rész megírására szoríthatja a tanulót.
- **Bizonyíték:** :329 „és adatvédelmi szempontból érzékeny részt kihagyhatsz.” · :355 „**„Még nem teljesítve”** státusz + rövid visszajelzés …, hogy mivel egészítse ki.”
- **Hatás:** Az értékelés nem lesz egységes, és a passzjog ellenére adatvédelmi nyomás keletkezik.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős, a DPO-val):
  - Hogyan jelzi a tanuló a passzt? Például egy „passz” szó a szakaszcím alatt.
  - Üres szakasznál a mentor első lépése a passz felajánlása legyen, ne a kiegészítés kérése.
  - A Z.4:167 és a GYV-11 védelme nem gyengülhet.
- **Típus:** emberi-döntés

**Z:QA-ERT-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** értékelés
- **Hely:** Z.4:402 (Feedback „Feloldás”); HUB:194
- **Probléma:** A Feedback a Z completion része, mégis dátum nélkül, „a Z.A után” alakban nyílik. A Z.4 reflexiónál viszont az áll: „Z.A után, a §7 szerinti dátummal”. A dátum nélküli alak jelenléti feltételnek is olvasható, ez pedig a Z.A-ról hiányzót elzárná a kötelező Feedbacktől (ERT-39).
- **Bizonyíték:** Z.4:402 „* **Feloldás:** a Z.A után (manifest LMS-Z-05)” · HUB:194 „(… a visszajelző űrlap: „Z.A után”, LMS-Z-05)”
- **Javaslat:** Vezesd át mindkét helyre a manifest §7 `Z_FEEDBACK` sorát (MAN:295 „`SCHEDULE_TO_RESYNC`, a Z.A után”) az LMS-Z-04 mintájára: „a Z.A után, a §7 szerinti dátummal (`Z_FEEDBACK`)”. Jelenléti feltételt ne vezess be.
- **Típus:** objektív

**Z:QA-IMPL-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:** Z.4:336 (File submissions), :303 (Típus-sor)
- **Probléma:** Az ADV-14 csak a videós utat kapcsolja ki, a módosítás viszont a teljes fájlfeltöltést. Ezzel megszűnik a dokumentumfeltöltés útja, amely az LMS-1 szerint megmarad. Ugyanezt írja elő az LMS-Z-04 ASSIGN-S profilja (MAN:19 „online text **és** fájlút, hozzáférhető sablon”) és a hozzáférhetőségi sztenderd 4. szakasza (letölthető sablon a feltöltéshez). A Z.4:81 letölthető sablont kínál, amelyet így nem lehet beadni.
- **Bizonyíték:** Z.4:336 „File submissions: **OFF** – a videós út alapból ki van kapcsolva” · HUM 14. szakasz, LMS-1: „Az egyenértékű online szöveges és fájlfeltöltéses út maradjon. … A Z.4 videó csak külön, DPO által engedélyezett profilon szerepelhet.”
- **Hatás:** Aki a sablont offline, közös eszközön vagy akadálymentességi okból dokumentumban tölti ki, nem tudja beadni. A build eltér a kánoni profiltól (akadálymentesítési hiány).
- **Javaslat:**
  - :336 → „File submissions: ON, max 1 file; Accepted file types: a hozzáférhető sablonhoz igazított dokumentumtípusok (LMS-1: például .docx, .odt, .pdf)”.
  - A videótípus és a 100–200 MB-os méret csak a külön, DPO által engedélyezett videós profilon jelenjen meg, az ADV-14 feltételeivel.
  - A :303 Típus-sor ugyanígy: a fájlfeltöltés dokumentumot jelent, a videós út külön, alapból kikapcsolt profil.
  - Az ADV-14 feltételei és a tanulói videós mondatok feltételessége maradjon.
- **Típus:** objektív

**Z:QA-IMPL-2**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** Z.2:13 (Completion-sor), Z.2:63 és Z.3:59 (runtime-doboz)
- **Probléma:** A Z.2 és a Z.3 completionje feltétel nélkül az összefoglaló dia elérése, holott a CP-ben csak pontozatlan választók vannak. A döntési csomag forráselemzése szerint összefoglaló dia csak feladatelemnél keletkezik. Ez zsákutca:
  - Ha a választók feladatelemek, a követett próbálkozás rögzíti őket (ADV-4: „lehetőleg ne”).
  - Ha nem azok, nincs completion-alap.
  - Tartalékút nincs megnevezve.
- **Bizonyíték:** Z.2:13 „**Completion (lecke):** az összefoglaló dia elérése … Hogy a Course Presentationnek feladatelem nélkül is van-e összefoglaló diája … a célverzión kell igazolni” · döntési csomag ERT-1 (01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag…, :733): „Z `cp.js` (összefoglaló dia csak feladatelemnél)”
- **Hatás:** Vagy az LMS-Z-02/-03 sosem teljesül, és vele a Z és az online félév sem (MAN:163, :165). Vagy a választókat rögzítik vagy pontozzák, az ADV-4 és az ERT-2 ellenére.
- **Javaslat:**
  - A Z.2:13 és a Z.3:59 completion-mondata legyen feltételes, az ERT-1 szó szerinti korlátjával: „Csak olyan CP kapjon erre épülő completiont, amelynek valóban van összefoglaló diája”.
  - Nevezze meg a tartalékutat: ha a célverzión nincs összefoglaló dia, a completion-alapot (ERT-2: „megtekintés/összefoglaló vagy más legitim aktivitás”) a build-spec gazda rögzíti.
  - Tilos a választót pontozott vagy önálló completion-elemmé tenni.
  - Maga az alap és a tárolásmentes technika kiválasztása külső: projektgazda (build-spec gazda) + DPO.
- **Típus:** objektív

**Z:QA-IMPL-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** Z.4:400 (Kötelező kérdés – Required)
- **Probléma:** A „kiürítés” sehol nincs meghatározva, ezért tesztként nem hajtható végre. Lehet az üres beküldés elutasítása, egy kötelező válasz törlése, vagy a közvetlenül utána (:401) tárgyalt 90 napos nyers-válasz-törlés. A döntés szövege maga is csak idézőjelben hozza.
- **Bizonyíték:** Z.4:400 „A „kiürítés” valós működését stagingben tesztelni kell (`LMS – H5P runtime acceptance.md` 16. pont).”
- **Hatás:** Az RA 16 tesztje (a kánoni kör #61 blokkja ugyanezt viszi át) nem végrehajtható, a G3b-bizonyíték nem rögzíthető.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda mint az ERT-3 build-spec gazdája mondja meg, mit jelent a „kiürítés” (QA: értékelési felelős). Utána a Z.4:400 és az RA 16 egyértelmű tesztté pontosul. Addig ne találgassunk. Ez a szó pontosítása, a döntés nem nyílik újra.
- **Típus:** emberi-döntés

**Z:QA-IMPL-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** Z.3:339 (SLIDE 7 címe)
- **Probléma:** A „tanuló-lokális” jelző (D-2/D-3: nincs CP-be ágyazott beviteli elem, nem tárolt) a teljes címre vonatkozik. Így a CP-be ágyazott Single Choice-ra is, pedig az a követett próbálkozásban rögzülhet. A terv (#23) csak a mini szöveges válaszra szánta.
- **Bizonyíték:** Z.3:339 „**Beágyazott kérdés – Single Choice + rövid szöveges válasz (opcionális, tanuló-lokális)**” · :360 „A tanuló a saját jegyzetébe írja; nem tárolt, nem completion-feltétel: ADV-3.”
- **Hatás:** A fejlesztő és az RA 24 visszaolvasása a Single Choice-t is nem tároltnak veheti, és ebből hamis „nem tároljuk” ígéret lehet.
- **Javaslat:** „Beágyazott kérdés – Single Choice (opcionális) + rövid szöveges válasz (opcionális, tanuló-lokális)”.
- **Típus:** objektív

---

**Összesítő megjegyzés – kánon (a kánoni körhöz, nem Z-finding):**
- **ERT-39:** a manifest nem mond ellent.
  - A §4 Z sora (MAN:163) és a kurzusteljesítés (MAN:165) nem sorolja a Z.A-t.
  - A `Z_REFLECTION` és a `Z_FEEDBACK` nyitása dátumhoz kötött (MAN:295).
  - Csak az LMS-Z-05 „Z.A után” alakja (MAN:112) és az RA 16 „a Feedback a Z.A után nyílik” mondata igazítandó a §7 dátumhoz (lásd Z:QA-ERT-3).
- **H5P-C profil:** a MAN:16 és az RA 9 („a forrásban előírt interakció(k) érdemi befejezése”) eltér a Z.1–Z.3 új, összefoglaló diás completion-mondatától (ERT-1; az M0 terv #29 és #36 blokkja). Az LMS-Z-03 sora üres (MAN:107), az LMS-Z-02 sora nem mondja ki az ERT-1/ERT-2-t (MAN:106).
- **Feedback:** az LMS-Z-05 (MAN:112) és az RA 16 (RA:87) nem tartalmazza azt, amire a Z.4:398 és :400 hivatkozik: az ADV-15 két „No” értékét, a back-end vizsgálatot és az ERT-3 Required-tesztjét.
- **LMS-Z-04/-08 (MAN:110–111):** az ERT-38 és az ADV-14 nincs átvezetve. Előbb a Z:QA-IMPL-1-et és a Z:QA-ERT-1-et kell rendezni:
  - a tervezett #57 blokk a File submissiont a videós úttal azonosítja;
  - a #58 blokk a szakaszonkénti mérce kérdését dönti el.
- **§7 (MAN:249):** a Z javító útja (PRG-6, #60) hiányzik.

<!-- agent aa3784ba8399f1a5d -->

Célzott nyelvi QA, Z modul (c5bc2c4, AP-2026-10-12-01): 10 finding, ebből 2 P1 és 8 P2. A legfontosabb a QA-NYELV-1: emberi döntés kell, mert a Z.4-ben két egymásnak ellentmondó „Teljesítve”-mérce áll.

Fájlok, a „Hely” mezőkben rövidítve:
- **HUB** = 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- **Z.3** = 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- **Z.4** = 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md

---

**Z:QA-NYELV-1**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv (értékelést is érint)
- **Hely:** Z.4:347 (§4 „A „Teljesítve” mércéje…”) ↔ Z.4:343 (Completion rule)
- **Probléma:** Az új §4-mondat „ha egy eleme hiányzik” fordulata egy teljes szakasz hiányára is érthető. Közben a Completion rule változatlanul mindhárom szakaszban értelmezhető tartalmat követel. Így ugyanabban a szakaszban két ellentétes mérce áll.
- **Bizonyíték:**
  - :343 „ha a beadás előírt részeiben (a három szakaszban; …) **tényleges, minimálisan értelmezhető tartalom** van”
  - :347 „ha egy eleme hiányzik, de a beadás értelmezhető, akkor is „Teljesítve” jár”
- **Hatás:** Ha a 3. szakasz üres (nincs következő lépés), az egyik mentor a §4 alapján „Teljesítve”-t ad, a másik a Completion rule alapján „Még nem teljesítve”-t. A tanulói :98/:329 mondat („részletes szerkezet (például a legalább 3 pillanat)”) a szűkebb olvasatot sugallja, a terv #41-es blokkja a tágabbat.
- **Javaslat:** EMBERI DÖNTÉS – az értékelési felelős dönt (ő az ERT-38 QA-gazdája), a kánoni körrel együtt, mert a MAN LMS-Z-08 is „előírt mezőiben” követel tartalmat.
  - A kérdés: a „Teljesítve” alsó határa az, hogy mindhárom szakaszban van értelmezhető tartalom, vagy elég, ha a beadás egésze értelmezhető?
  - A döntés után ugyanahhoz kell igazítani a §4 „ha egy eleme hiányzik” fordulatát, a Completion rule zárójelét és a :98/:329 tanulói mondatot.
  - Addig nyelvi alapon senki ne írja át.
- **Típus:** emberi-döntés
- **Verdikt:** —

**Z:QA-NYELV-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** Z.4:359
- **Probléma:** Az új GYV-11-mondat alanya csak „A beadás”, és közvetlenül a különleges adatról szóló mondat után áll. Ezért nem egyértelmű, hogy a „kezeléséhez” és a „nem töröljük” a feltárásra vagy a különleges adatra vonatkozik. A pont fejléce ráadásul mindkét esetet lefedi.
- **Bizonyíték:** „A különleges adatot a HUM-PRIV-01 szerint kezeljük (…). A beadás nem az incidens elsődleges nyilvántartása; kezeléséhez … kell, és jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük.”
- **Hatás:** Az automatikus törlés tilalma a csak különleges adatot tartalmazó beadásra is olvasható. A GYV-11 viszont csak a gyermekvédelmi feltárásra szól, így a különleges adat megőrzése indokolatlanul elhúzódhat.
- **Javaslat:**
  - OLD: „A beadás nem az incidens elsődleges nyilvántartása; kezeléséhez dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás vagy helyesbítés és adatvédelmileg jóváhagyott törlési és megőrzési rend kell, és jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük.”
  - NEW: „A gyermekvédelmi feltárást tartalmazó beadás nem az incidens elsődleges nyilvántartása. Az ilyen beadás kezeléséhez dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás vagy helyesbítés, valamint adatvédelmileg jóváhagyott törlési és megőrzési rend kell; jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük.”
  - A következő mondat (pótlási út, „Teljesítve”) változatlan marad. A feltételek közül egyik sem hagyható el.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** Z.4:98 és Z.4:329 (a két mondat azonos)
- **Probléma:**
  - A beillesztett tanulói mondat három tagmondatot fűz pontosvesszős láncba.
  - A „bukási feltétel” értékelői zsargon, és ütközik a közvetlenül előtte álló „nem jegy” kerettel.
  - A „(például a legalább 3 pillanat)” alaptag nélküli.
  - A „csak … látja; … is hozzáférhet” szerkezetből hiányzik a szembeállítást jelző szó.
- **Bizonyíték:**
  - „a 3 kérdés szerinti részletes szerkezet (például a legalább 3 pillanat) útmutató, nem bukási feltétel, és adatvédelmi szempontból érzékeny részt kihagyhatsz.”
  - „csak a kijelölt mentorod vagy értékelőd látja, …; technikai okból a Moodle rendszergazdája is hozzáférhet.”
- **Hatás:** A tanuló nehezen olvassa ki, mi kötelező, és a „csak … is” ellentmondásnak hat.
- **Javaslat:**
  - OLD: „A „Teljesítve”-hez tényleges, értelmezhető beadás kell; a 3 kérdés szerinti részletes szerkezet (például a legalább 3 pillanat) útmutató, nem bukási feltétel, és adatvédelmi szempontból érzékeny részt kihagyhatsz. A beadásodat csak a kijelölt mentorod vagy értékelőd látja, aki a visszajelzést adja; technikai okból a Moodle rendszergazdája is hozzáférhet.”
  - NEW: „A „Teljesítve”-hez tényleges, értelmezhető beadás kell. A 3 kérdés részletes szerkezete (például hogy legalább 3 pillanatot nevezz meg) csak útmutató, nem a teljesítés feltétele. Adatvédelmi szempontból érzékeny részt kihagyhatsz. A beadásodat csak a kijelölt mentorod vagy értékelőd látja, aki a visszajelzést adja; technikai okból ugyanakkor a Moodle rendszergazdája is hozzáférhet.”
  - Mindkét helyen ugyanígy.
  - Ha a QA-NYELV-1 döntése a tágabb olvasat lesz, a második mondatot a döntés szerint kell igazítani, nem ezt a javaslatot átvenni.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** Z.4:347
- **Probléma:** A kibővített bekezdésben az „Ezeket” közvetlenül az érzékeny részekről szóló mondat után áll, így visszafelé, az érzékeny részekre is olvasható (névmási zuhanás). Valójában az alatta álló listára mutat.
- **Bizonyíték:** „Az adatvédelmi szempontból érzékeny részek passzolhatók; ezt a tanuló a feladatleírásból előre tudja (…). Ezeket érdemes szem előtt tartani:”
- **Hatás:** Az értékelő félreolvashatja, mire vezet be a mondat.
- **Javaslat:**
  - OLD: „Ezeket érdemes szem előtt tartani:”
  - NEW: „Az ideális szerkezet, amelyet érdemes szem előtt tartani:”
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** Z.4:401 (Feedback, „Megőrzés”)
- **Probléma:** A beillesztett GYV-11-mondat négy tagmondatot fűz egyetlen mondatba (vesszők, „és”, pontosvessző). A „válaszokat feldolgozó” igenévi alany is nehezíti a végrehajtást.
- **Bizonyíték:** „Ha egy válasz gyermekvédelmi feltárást tartalmaz, a válaszokat feldolgozó azonnal bevonja a Memunát (…), az ügy dokumentációja … készül (HUM-SAFE-01), és ezt a választ … automatikusan nem töröljük; a korlátozáshoz, …”
- **Hatás:** Lépéssorként nem olvasható ki, mit tegyen elsőként a feldolgozó.
- **Javaslat:**
  - OLD: a „Ha egy válasz gyermekvédelmi feltárást tartalmaz, …” kezdetű mondat a „(projektgazdai döntés, 2026-10-12, GYV-11).” zárásig.
  - NEW: „Ha egy válasz gyermekvédelmi feltárást tartalmaz, aki a válaszokat feldolgozza, azonnal bevonja a Memunát (az ötlépéses jelzési út szerint). Az ügy dokumentációja nem a Moodle-ben, hanem a hozzáférés-korlátozott incidensnyilvántartásban készül (HUM-SAFE-01). Ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük; a korlátozáshoz, a helyesbítéshez és a törlési vagy megőrzési döntéshez dokumentált, jogosult Memuna-eljárás és adatvédelmileg jóváhagyott rend kell (projektgazdai döntés, 2026-10-12, GYV-11).”
  - A tartalom nem változik.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** Z.3:217 ↔ Z.3:219, :241, :281; HUB:95
- **Probléma:** A v1-út feltétele két alakban szerepel.
  - A :217 azt írja, „még nem adtad le”; az új sorok a döntés szavával azt, hogy „még nincs kész”. A kettő nem ugyanaz: egy leadott, de „Még nem teljesítve” értékelésű v2 „nincs kész”, mégis „leadtad”.
  - A hubban az „elkészített … ha az még nincs kész” egyetlen szerkezeten belül mond ellent önmagának.
- **Bizonyíték:**
  - Z.3:217 „Ha a Peula v2-det még nem adtad le, mert még az M7 javítási útján vagy,”
  - Z.3:219 „(vagy, ha az még nincs kész, a Peula v1-edre)”
  - HUB:95 „az M7-ben elkészített Peula v2-jéhez (ha az még nincs kész, …”
- **Hatás:** Két egymást követő sorban két különböző feltételt olvas a tanuló.
- **Javaslat:**
  - Z.3:217 OLD: „Ha a Peula v2-det még nem adtad le, mert még az M7 javítási útján vagy,” → NEW: „Ha a Peula v2-d még nincs kész, mert még az M7 javítási útján vagy,” (így egyezik a :281-gyel és a PRG-6 szövegével).
  - HUB:95 OLD: „a tanuló az M7-ben elkészített Peula v2-jéhez (ha az még nincs kész, mert az M7 javítási útján van, a Peula v1-éhez; PRG-6) konkrét terepi tervet ír” → NEW: „a tanuló az M7-ben elkészített Peula v2-jéhez – vagy, ha az M7 javítási útján van, és a v2-je még nincs kész, a Peula v1-éhez (PRG-6) – konkrét terepi tervet ír”.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** HUB:33
- **Probléma:**
  - Az új mondat a Z.3 javítását is „javító beadás”-nak hívja, holott a Z.3 szövege „újra beküld / újrabeküldés” (ott mezőbe való beküldés van, nem Assignment-beadás).
  - Az „elfogadása „Még nem teljesítve”” szerkezet hibás: az elfogadás maga nem lehet „Még nem teljesítve”.
- **Bizonyíték:**
  - HUB:33 „Ha a Z.3 mentori elfogadása (LMS-Z-07) vagy a Z.4 megerősítése (LMS-Z-08) „Még nem teljesítve”, a javító beadás időpontját…”
  - Z.3:312 „az újrabeküldés időpontját a mentorod jelöli ki.”
- **Hatás:** Egy fogalomra két megnevezés jut, és a hub olvasója nem köti össze a Z.3 újrabeküldésével.
- **Javaslat:**
  - OLD: „Ha a Z.3 mentori elfogadása (LMS-Z-07) vagy a Z.4 megerősítése (LMS-Z-08) „Még nem teljesítve”, a javító beadás időpontját”
  - NEW: „Ha a Z.3 mentori elfogadásánál (LMS-Z-07) vagy a Z.4 megerősítésénél (LMS-Z-08) az eredmény „Még nem teljesítve”, a javítás (a Z.3-nál az újrabeküldés, a Z.4-nél a javító beadás) időpontját”
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** Z.3:339
- **Probléma:** A címben a „tanuló-lokális” minősítő a Single Choice-ra is vonatkozik. A Single Choice azonban beágyazott H5P-elem, amelyet a Z.3:59 szerint a követett próbálkozás csak „lehetőleg” nem rögzít. Tanuló-lokális, beviteli elem nélküli csak a mini szöveges válasz (:360).
- **Bizonyíték:**
  - Z.3:339 „**Beágyazott kérdés – Single Choice + rövid szöveges válasz (opcionális, tanuló-lokális)**”
  - Z.3:360 „(Opcionálisan alul, beviteli elem nélkül: …)”
- **Hatás:** A fejlesztő a Single Choice-t is beviteli elem és követés nélkül építheti meg.
- **Javaslat:**
  - OLD: „(opcionális, tanuló-lokális)”
  - NEW: „(opcionális; a szöveges válasz tanuló-lokális, beviteli elem nélkül)”
  - A Single Choice besorolásához nem szabad nyúlni.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** Z.4:16, :55, :144, :310, :327 (tanulói szöveg)
- **Probléma:** A feltétel szövege egységes, de adminisztrátori nézőpontból szól a tanulóhoz („be van kapcsolva”), és ezt a tanuló nem tudja ellenőrizni.
  - A :16 egyetlen pontjában a „videós beadás” mellett „videós út” is áll.
  - A :144-ből hiányzik az „a kurzusban”.
- **Bizonyíték:** :16 „ha a kurzusban a videós beadás be van kapcsolva, és szeretnéd, helyette abból egy 2–3 perces videót készíthetsz): **~15–25’** *(a videós út a felvétel + …)*”
- **Hatás:** A tanuló nem tudja, honnan derül ki, hogy él-e számára a lehetőség, és ugyanabban a sorban két szót kap egy fogalomra.
- **Javaslat:**
  - A tanulói helyeken: „ha a kurzusban a videós beadás be van kapcsolva” → „ha a kurzusban elérhető a videós beadás”.
  - :144: „ha a videós beadás be van kapcsolva, és azt választod” → „ha a kurzusban elérhető a videós beadás, és azt választod”.
  - :16, a dőlt zárójelben: „a videós út” → „a videós beadás”.
  - A fejlesztői sorok (:28, :105, :303, :336, HUB) maradhatnak „be van kapcsolva” / „videós út” alakban.
- **Típus:** objektív
- **Verdikt:** —

**Z:QA-NYELV-10**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** Z.3:59 (az új mondat); Z.4:398
- **Probléma:**
  - (a) Az új Z.3-mondat különírja a „célverzió” összetételt, a többi új mondat (Z.2:13, Z.4:336) viszont egybeírja.
  - (b) A Z.4:398-ban kerek zárójelen belül újabb kerek zárójel áll.
- **Bizonyíték:**
  - Z.3:59 „hogy feladatelem nélkül is van-e összefoglaló diája, a cél verzión kell igazolni”
  - Z.4:398 „(projektgazdai döntés, 2026-10-12, ADV-15; utólagos ellenőrzés (vétó/QA): a DPO és a programvezető, HUM-PRIV-03)”
- **Hatás:** Csekély helyesírási és következetességi hiba.
- **Javaslat:**
  - (a) „a cél verzión kell igazolni” → „a célverzión kell igazolni”, csak az új mondatban. A régebbi „cél verzión” alakok (Z.1:55, :57, Z.2:61, :63, Z.3:57, illetve a :59 első mondata) kívül esnek ezen a QA-n.
  - (b) „utólagos ellenőrzés (vétó/QA):” → „utólagos ellenőrzés [vétó/QA]:”.
- **Típus:** objektív
- **Verdikt:** —

---

A Z-mappában sorvégi szóközt vagy `\`-t nem találtam. A régi írásmód (madrich, chanich, hagshama, dugma ishit, Leviatan) a diffben nem jelent meg. A GYV-5 mondatát, a GK §4:63 fordulatát („biztonságos támogatási útra terel”) és a döntések szó szerinti szövegét a kérés szerint nem jelentettem.
