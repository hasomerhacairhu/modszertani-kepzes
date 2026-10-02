# Gyermekvédelem – release gate

## 1. Mire szolgál ez a kapu?

Ez a dokumentum három külön réteget tart szét:

1. **jogi kötelezettség**, amit hatályos jogszabály alapoz meg;
2. **safeguarding szakmai minimum**, amit a képzés akkor is követ, ha egy konkrét jogi minősítés még nyitott;
3. **szervezeti policy**, amelyet a képzésben a Gyermekvédelmi működési standard v1.0 rögzít (§5.1).

A három réteget nem nevezzük egymás helyett „törvényi kötelezettségnek”.

A **Gyermekvédelmi működési standard v1.0 (Child Protection Operating Standard v1.0)** a képzés elsődleges normatív gyermekvédelmi dokumentuma: a HUM-SAFE-01…05 projektgazdai döntései együtt, az elemek helyével (§5.1).

## 2. Release-szabály

M3.3, M3.B, az M3-kapu, valamint minden olyan tananyagelem, amely bántalmazásról, önsértésről, groomingról, szexuális/romantikus határátlépésről, súlyos veszélyeztetettségről vagy külső jelzésről tanít, **nem nyitható meg valódi madrihoknak írásos gyermekvédelmi jóváhagyás nélkül**. A jóváhagyó a §5 jóváhagyói rendje (projektgazdai döntés, 2026-10-02) szerint a Memuna; jogi kérdésben a jogi szakértő.

Zárt Moodle-stagingben, szintetikus tesztadatokkal és csak szerkesztői/QA hozzáféréssel ezek az elemek felépíthetők és technikailag tesztelhetők.

A jelen repo biztonságos szakmai alapértelmezése: súlyos helyzeteket **harmadik személyű esetelemzéssel**, nem traumatikus szerepjátékkal dolgozunk fel. **Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna és a DPO. Esetalapú kapuproduktumba (elsősorban az M3 helyzetleírásába) **csak kitalált, életszerű eset** kerülhet; valós eset névtelenítve sem, mert kis közösségben könnyen visszaazonosítható. Valós gyermekvédelmi eset soha nem pedagógiai feladat.

**Médiakapuk.** **Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a release owner és a jogi/adatvédelmi felelős. A jogi és gyermekvédelmi médiakapuk (köztük a HUM-MEDIA-02 alkapui: J1, J2, V1, V3, valamint a HUM-MEDIA-03) blokkolják az általuk érintett tanulói asset release-ét. Gyermekvédelmi vagy krízis-HOOK-ban nem használunk készlet (stock) AI-beszélőfejet. A tételeket az `Emberi jóváhagyás szükséges.md` 5. szakasza tartja nyilván.

## 3. Jogi keret, amit a jogi szakértőnek a szervezet konkrét jogállására kell alkalmaznia

### 3.1. Gyvt. 17. §

A hatályos 1997. évi XXXI. törvény 17. § (1) a gyermekvédelmi jelzőrendszer résztvevői között **egyesületeket, alapítványokat és egyházi jogi személyeket is nevesít**. A 17. § (2) a felsorolt intézmények és személyek számára veszélyeztetettség esetére jelzést, súlyos esetekben hatósági eljárás kezdeményezését írja elő.

**Nyitott jogi alkalmazási kérdés:** a képzést ténylegesen működtető szervezeti jogalany, a madrihok és az egyes önkéntes szerepkörök pontosan hogyan esnek a törvényi kötelezettségek alá. Ezt a repository nem minősíti önállóan.

### 3.2. Btk. 209/A. §

A Btk. 209/A. § **nem általános „elmulasztott gyermekvédelmi jelzés = bűncselekmény” szabály**. A tényállás kifejezetten a Gyvt. 17. § **(4a)–(4c)** bekezdéseiben meghatározott, kiemelt veszélyeztető okra utaló körülménnyel összefüggő kötelezettség megszegésére hivatkozik.

Ezért learner-facing tananyagban nem használunk olyan mondatot, amely minden red flagre automatikus büntetőjogi következményt állít. A konkrét jogi kötelezettséget jogi szakértő igazolja a szerepkör és a helyzet alapján.

### 3.3. Akut veszély

Közvetlen életveszély vagy azonnali sürgősségi helyzet esetén a **112** sürgősségi út. Ez nem helyettesíti a belső jelzést: a jelzési út (§4.1) 5. lépése szerint közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés.

A segélyvonalak jelenlegi szolgáltatásleírása szerint (forrásuk: §7):
- **116-111**: a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak; gyerek érdekében telefonáló, aggódó felnőtt is hívhatja;
- **116-000**: a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: eltűnt, szökésben lévő vagy szökést fontolgató, illetve bántalmazott gyerek ügyében, felnőttek is hívhatják; nem általános „szülői vonal”;
- **116-123**: felnőtt lelki elsősegély (a Lelki Elsősegély Telefonszolgálatok Szövetsége vonala).

A telefonszámokat learner release előtt újra ellenőrizni kell.

## 4. Safeguarding szakmai minimum

Ezek a szabályok a tananyagban akkor is maradnak, ha a konkrét szervezeti/jogi minősítés még nyitott:

- nincs 100%-os titoktartási ígéret;
- a madrih meghallgat, de **nem nyomoz**, nem folytat rávezető kérdésekkel „kihallgatást”;
- a madrih nem konfrontál feltételezett elkövetőt;
- a madrih nem vállal egyedüli felelősséget gyermekvédelmi ügyben;
- a 15–17 éves madrih **vezethet peulát, de soha nem ő az egyetlen felelős felnőtt**: minden éles terepi alkalmon jelen van egy jóváhagyott, felkészített, 18 év feletti felnőtt – fizikailag ott van, vagy ugyanazon a helyszínen azonnal elérhető –, és **a gyermekvédelmi felelősség az övé**; a madrih a saját szerepében figyel és jelez;
- érzékeny, súlyos vagy személyesen érintő gyakorlatból bárki **indoklás nélkül passzolhat**, szünetet vagy egyenértékű alternatívát kérhet;
- a résztvevőnek nem kell saját traumát vagy érzékeny történetet megosztania;
- ha a képzés közben saját érintettség kerül elő, a facilitátor nem folytat nyilvános feldolgozást, hanem biztonságos támogatási útra terel (a tanulói „ha téged is érint” blokk: §4.3);
- felkavart kiskorút **nem küldünk ki egyedül**: legyen kijelölt biztonságos hely és egy felnőtt, aki vele van;
- a tananyag nem ír elő automatikus négyszemközti félrevonulást;
- diszkrét beszélgetés csak **átlátható helyzetben**, a §4.2 safer-working szabálya szerint.

A kiskorú madrihra, a passzra és a felkavart kiskorúra vonatkozó pontok, valamint a §4.1–4.3 szervezeti szabályként a HUM-SAFE-01–03 **projektgazdai döntéseit (2026-10-02)** rögzítik; utólagos ellenőrzés (vétó/QA): a Memuna és a §5-ben tételenként megnevezett további szerepek.

### 4.1. Az ötlépéses jelzési út (HUM-SAFE-01)

**Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna és a helyettese. Az M3.B ötlépéses jelzési útja az egyetlen kánon. Ahol a tananyag a teljes utat felsorolja, ezt a szöveget használja szó szerint:

1. **Észleld, és vedd komolyan.**
2. **Hallgasd meg, és ne ígérj teljes titoktartást.**
3. **Ne nyomozz, ne konfrontálj, és ne próbáld egyedül megoldani.**
4. **Azonnal vond be a kijelölt Memunát** – összeférhetetlenség esetén a név szerint kijelölt helyettesét.
5. **Közvetlen veszélynél előbb a biztonság és a 112**, utána a belső jelzés.

- **Memuna:** a Somer gyermekvédelmi felelőse. A Somer–Magyar szótár szerint ő felel azért, hogy a sértéssel, bántalmazással, zaklatással kapcsolatos ügyekben felelősen, gyorsan és biztonságosan járjon el. Tanulói fájlban az első előforduláskor: „a kijelölt **Memuna** (a Somer gyermekvédelmi felelőse)”, utána „a Memuna”.
- A jelzés címzettje gyermekvédelmi ügyben mindig a Memuna (összeférhetetlenségnél a név szerint kijelölt helyettese), nem a mentor, nem a ken-vezető, nem „egy felnőtt” és nem a szülő. Ahol a mentor nem gyermekvédelmi ügyben, hanem tanulástámogatóként szerepel, ott a mentor marad.
- Első személyű változat (pl. az M3.B közös flipchartján) megengedett, ha tartalmilag pontosan ez az öt lépés, ugyanebben a sorrendben. Ahol a teljes felsorolás nem a hely feladata, elég az utalás: „az ötlépéses jelzési út szerint (M3.B lépéstérkép)” vagy „azonnal vond be a Memunát”. Négylépéses, csonka vagy versengő változat nem maradhat a tananyagban.
- A régi szövegek védő elemei maradnak: a titoktartás határáról szóló minta-mondat, a „nem faggatom”, a „ne találj ki helyi útvonalat, ha nincs” utasítás, és az, hogy a további lépésekről (szülő, szakember bevonása) innentől nem a madrih dönt egyedül (a 3–4. lépés magyarázataként).
- **Dokumentálás:** a gyermekvédelmi ügy dokumentációja nem Moodle-ben készül, hanem külön, hozzáférés-korlátozott incidensnyilvántartásban. A madrih nem ír Moodle-be, csoportchatbe, kvízválaszba vagy beadandóba az esetről azonosítható részletet.
- **Incidensnyilvántartás (projektgazdai döntés, 2026-10-02):** Google Workspace Shared Drive → `Restricted / Safeguarding / Incidents`; hozzáférés csak a Memunának, a helyettesnek és a szervezeti vezetőnek. Nem Moodle, nem GitHub.
- **Kontakt és helyettes (projektgazdai döntés, 2026-10-02):** a tanulói elsődleges gyermekvédelmi kontakt a Somer mindenkori, a `somer.hu/kapcsolat` oldalon publikált **Memunája** (2026-10-02-án: Marci). **Helyettes:** a **Ros Hinuh** (oktatási vezető; 2026-10-02-án: Lili). Ha bármelyikük érintett, a másikhoz kell fordulni. Ha mindkettő érintett vagy nem elérhető: Kék Vonal **116-111**, bántalmazott vagy eltűnt gyermek ügyében **116-000**, közvetlen veszélyben **112** (§3.3).
- **Telefon:** a Somer központi száma, **+36 70 42 76 637** (+36-70-HA-SO-MER), a kapcsolati oldal szerint hétköznap 10–18 óra között. Ez nem ügyeleti vonal: munkaidőn kívül és közvetlen veszélyben a 112, illetve a Kék Vonal az út.
- **Hol áll a név:** a nevek csak governance- és gate-szövegbe, valamint a „Segítség és kapcsolatok” blokk leírásába kerülnek (szerep + „jelenleg: <név>”). A leckékben a szerep áll („a Memuna”, „a helyettese”), és a „Segítség és kapcsolatok” blokkra mutat; név és telefonszám a leckékbe nem kerül. Az M3.B helyi útvonal-lapja (MUNK-02) a szerepeket előre kitöltheti: Memuna – `somer.hu/kapcsolat`; helyettes – Ros Hinuh; külső út – 116-111 / 116-000 / 112.

### 4.2. Safer-working szabály (HUM-SAFE-02)

**Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna. A szabály egyetlen helye ez a pont; a tananyag erre hivatkozik, és értelemszerűen rövidítve használja:

> A safer-working szabály **minden fizikai és digitális kettesben zajló (1:1) helyzetre** vonatkozik: privát üzenet (DM), voice chat, videóhívás és mentori beszélgetés is ide tartozik. Kiskorúval **személyes közösségimédia-fiókról** nem kommunikálunk; **szervezeti csatorna** használható. 1:1 helyzet csak **indokolt esetben, átlátható módon és egy másik felelős tudtával** jöhet létre. Online kiscsoportos szobában (breakout room) se maradjon ellenőrizetlen felnőtt–kiskorú 1:1: lehetőleg legalább két résztvevő legyen egy szobában, a felnőtt jelenléte váltakozó és ellenőrizhető; egy felnőtt és egy kiskorú elszigetelt szobája csak **előre meghatározott kivételként** megengedett.

- A „diszkrét, de átlátható” elv marad: a diszkrét beszélgetés is átlátható helyzetben zajlik.
- **Kvízkulcs:** kiskorúnak küldött személyes privát üzenet soha nem „helyes” válasz. Hivatalos csatornán küldött logisztikai üzenet lehet helyes, de gyermekvédelmi helyzet megoldásaként nem.
- **Előre meghatározott 1:1 kivételek (projektgazdai döntés, 2026-10-02):** Engedélyezett kivétel csak: (a) előre egyeztetett mentorbeszélgetés, (b) biztonsági vagy feltárási beszélgetés, (c) rövid technikai segítség. Legfeljebb **30 perc**, hivatalos csatornán vagy fizikailag átlátható térben, és egy másik felelős tud róla. Nincs zárt privát szoba, személyes közösségimédia-fiók, eltűnő üzenet vagy felvétel. A naplóba csak dátum, résztvevők, időtartam, célkategória és utánkövetés kerül, a beszélgetés tartalma nem. Ha gyermekvédelmi ügy lesz belőle, külön incidens-azonosítóra vált (§4.1).

### 4.3. „Ha téged is érint” blokk és gondviselői szabály (HUM-SAFE-03)

**Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna és a programvezető. A blokk szövegét ez a pont rögzíti; a tananyag szó szerint ezt használja. Minden meglévő, ad hoc „ha nehéz / ha téged is érint / ha felkavar” típusú támogató blokk helyére ez kerül, új blokként pedig a kurzus elejére (M0.1), valamint az M2.A, az M2.4, az M3.3 és az M3.B érzékeny része elé kerül. Máshol nem kerül be új blokk.

> **Ha ez a téma téged is érint:** nem kell személyes részletet megosztanod. Mondhatsz passzt, kérhetsz szünetet, vagy beszélhetsz külön a mentoroddal vagy a Somer gyermekvédelmi kontaktjával. Ha te vagy valaki más veszélyben van, ezzel ne maradj egyedül: használd a „Segítség és kapcsolatok” blokkban megadott gyermekvédelmi utat. Közvetlen veszélyben hívd a 112-t. Ha 18 év alatti vagy, a gondviselődet bevonhatjuk, amikor ez a biztonságodat szolgálja. Ha a gondviselő bevonása növelhetné a veszélyt, vagy ő maga érintett a helyzetben, a Memuna más biztonságos felnőttet vagy hivatalos segítséget von be.

- **Gondviselői szabály:** kiskorúnál a gondviselőt bevonjuk, kivéve, ha ez növelheti a veszélyt, vagy maga a gondviselő érintett a feltételezett problémában; ilyenkor a Memuna a biztonságos külső utat választja.

## 5. Szervezeti döntések

A konkrét értékeket az **Emberi jóváhagyás szükséges.md** tartja nyilván. Itt nem ismételjük meg őket külön placeholderként.

Mind az öt tételben **projektgazdai döntés (2026-10-02)** született; a tartalmuk alább és a §4-ben szerepel, együtt pedig a Gyermekvédelmi működési standard v1.0-t alkotják (§5.1). A tételek az `Emberi jóváhagyás szükséges.md`-ben lezártak. A tételenként megnevezett szerepek későbbi ellenőrzése **utólagos ellenőrzés (vétó/QA)**, nem új döntési kapu. A §2 release-szabálya és a §6 átvételi listájának nyitott sorai változatlanul érvényesek.

- **HUM-SAFE-01:** helyi gyermekvédelmi felelős, elérhetőség, helyettes/külső út, akut-eszkaláció, dokumentálás. *Projektgazdai döntés:* az ötlépéses jelzési út az egyetlen kánon (§4.1); a jelzés címzettje a Memuna, helyettese a Ros Hinuh; közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés; a dokumentáció külön, hozzáférés-korlátozott incidensnyilvántartásban készül, nem Moodle-ben. A kontaktot, a külső utat és a nyilvántartás helyét a §4.1 rögzíti. Utólagos ellenőrzés (vétó/QA): a Memuna és a helyettese.
- **HUM-SAFE-02:** négyszemközti / safer-working szabály. *Projektgazdai döntés:* a szabály minden fizikai és digitális 1:1 helyzetre kiterjed; az előre meghatározott kivételek: előre egyeztetett mentorbeszélgetés, biztonsági vagy feltárási beszélgetés, rövid technikai segítség, legfeljebb 30 percig (§4.2). Utólagos ellenőrzés (vétó/QA): a Memuna.
- **HUM-SAFE-03:** a madrih saját érintettsége, passz/alternatíva, kiskorú madrih felügyelete. *Projektgazdai döntés:* a 15–17 éves madrih vezethet peulát, de soha nem ő az egyetlen felelős felnőtt; minden éles terepi alkalmon jelen van egy jóváhagyott, felkészített, 18 év feletti felnőtt, akié a gyermekvédelmi felelősség; érzékeny gyakorlatból bárki indoklás nélkül passzolhat; felkavart kiskorút nem küldünk ki egyedül (§4). A „ha téged is érint” blokk és a gondviselői szabály: §4.3. Utólagos ellenőrzés (vétó/QA): a Memuna és a programvezető.
- **HUM-SAFE-04:** alkohol- és dohányzási szabály. *Projektgazdai döntés:* kiskorúaknak szóló programon **nulla alkohol, dohány, e-cigaretta (vape) és nikotintermék**; 18 év alatt ezek egyike sem. Felelős felnőtt szolgálat alatt nem fogyaszt alkoholt, és nem lehet befolyásolt állapotban. Dohányozni csak szolgálaton kívül, kijelölt helyen, a gyerekektől elkülönítve lehet. A törvény minimumként tiltja az alkohol és a dohány kiszolgálását 18 év alatt; a szervezet ennél **szigorúbb** szabályt alkalmaz. Utólagos ellenőrzés (vétó/QA): a szervezeti vezetés és a Memuna.
- **HUM-SAFE-05:** a programban dolgozó 18 év feletti stáb és a 15–17 éves madrihok szerepkörönkénti alkalmassági ellenőrzése, dokumentált gyermekvédelmi felkészítése és felülvizsgálata. *Projektgazdai döntés:* szerepkör-alapú alkalmassági rend. 18 év feletti képző, mentor és rendszeresen gyerekekkel dolgozó önkéntes: személyazonosság-ellenőrzés, a szerephez szükséges erkölcsi bizonyítvány, a Child Protection Policy – a képzésben a Gyermekvédelmi működési standard v1.0 (§5.1) – elfogadása, gyermekvédelmi + safer-working + adatvédelmi képzés; évente rövid megújító képzés és nyilatkozat; új szerepkörnél új ellenőrzés. 15–17 éves madrih: képzés + magatartási kódex + felnőtt felügyelet. *Erkölcsi bizonyítvány (projektgazdai döntés, 2026-10-02):* 18 év feletti képző, mentor és rendszeresen, közvetlenül gyermekekkel dolgozó önkéntes: **hatósági erkölcsi bizonyítvány**, amely igazolja, hogy (a) büntetlen előéletű, és (b) nem áll foglalkozástól vagy tevékenységtől eltiltás hatálya alatt. Belépéskor legfeljebb 90 napos dokumentum, majd **kétévente új**, közben éves önnyilatkozat (jogszabályi háttér: a bűnügyi nyilvántartási rendszerről szóló 2009. évi XLVII. törvény). Utólagos ellenőrzés (vétó/QA): a szervezeti vezetés és a Memuna; jogi kérdésben jogi szakértő.

**Gyermekvédelmi jóváhagyó.** **Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna és a helyettese (HUM-SAFE-01). A gyermekvédelmi jóváhagyás egyetlen felelőse a **Memuna** (a Somer gyermekvédelmi felelőse); a programvezető operatív társdöntő; jogi szakértő csak a jogi minősítésnél.

### 5.1. Gyermekvédelmi működési standard v1.0 (Child Protection Operating Standard v1.0)

**Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna, tételenként a fenti szerepekkel. A madrihképzés kanonikus minimum-gyermekvédelmi szabályrendszere a HUM-SAFE-01…05 együtt, **Gyermekvédelmi működési standard v1.0 (Child Protection Operating Standard v1.0)** néven. A képzésben ez az elsődleges normatív dokumentum, nem a régi, elérhetetlen Child Protection Policy PDF. Ahol a tananyag Child Protection Policyra hivatkozik, ezt a standardot érti rajta. A standard nem külön fájl: elemei ennek a dokumentumnak (és az adatvédelmi elemnél az `Adatvédelem – tanulói adatok és AI.md`-nek) az alábbi pontjaiban élnek.

| # | Elem | Helye |
|---|---|---|
| 1 | ötlépéses jelzési út | §4.1 |
| 2 | a teljes titoktartás ígéretének tilalma | §4; §4.1, 2. lépés |
| 3 | a nyomozás és a konfrontáció tilalma | §4; §4.1, 3. lépés |
| 4 | 1:1 safer-working | §4.2 |
| 5 | digitális kommunikációs szabály | §4.2 |
| 6 | a kiskorú madrih felnőtt felügyelete | §4; §5, HUM-SAFE-03 |
| 7 | zéró alkohol és nikotin a programokon | §5, HUM-SAFE-04 |
| 8 | fotó- és adatminimalizálás | `Adatvédelem – tanulói adatok és AI.md` §2, §3 és §6 |
| 9 | képzett és ellenőrzött stáb | §5, HUM-SAFE-05 |
| 10 | passzolási jog | §4; §4.3 |
| 11 | 112 közvetlen veszélynél | §3.3; §4.1, 5. lépés |
| 12 | külön incidensnyilvántartás | §4.1 |

## 6. Tartalmi acceptance

Learner-facing release előtt mindegyik legyen igazolt:

- [ ] M3.3, M3.B, M3-kapu és M7 gyermekvédelmi kapuelemek a gyermekvédelmi jóváhagyó (a §5 szerint a Memuna) által átnézve;
- [x] HUM-SAFE-01–05 lezárva; **projektgazdai döntés: 2026-10-02** – az `Emberi jóváhagyás szükséges.md` mind az öt tételt dátummal, jóváhagyóval és bizonyítékkal zárta; a későbbi ellenőrzés vétó/QA (§5);
- [ ] a learner-facing gyermekvédelmi kontakt – a Memuna és összeférhetetlenség esetére a név szerint kijelölt helyettese – a „Segítség és kapcsolatok” blokkban, a többi kontakttól külön, ténylegesen látható a Moodle-ben;
- [ ] nincs 100%-os titoktartási ígéret;
- [ ] nincs nyomozásra, konfrontációra vagy otthoni „lerendezésre” utasítás;
- [ ] akut veszély útja és a segélyvonalak a review napján ellenőrizve;
- [ ] saját érintettségre van rövid, szégyenítés nélküli kilépési/támogatási út (egységes szövege: §4.3);
- [ ] a négyszemközti (1:1) helyzetek tananyaga és kvízkulcsai a HUM-SAFE-02 szerinti safer-working szabállyal és kivételeivel egyeznek (szövege: §4.2);
- [ ] az alkohol-, dohány- és nikotinpéldák csak a HUM-SAFE-04 szerinti szervezeti szabályt állítják (tartalma: §5);
- [ ] a 18 év feletti stáb alkalmassági ellenőrzése és gyermekvédelmi felkészítése, valamint a 15–17 éves madrih képzése, magatartási kódexe és felnőtt felügyelete HUM-SAFE-05 szerint dokumentált;
- [ ] a jogszabályi állításoknál külön látszik, mi jogi kötelezettség, mi safeguarding szakmai minimum, és mi szervezeti policy;
- [ ] jóváhagyás dátuma és következő felülvizsgálat dátuma rögzítve.

## 7. Elsődleges források a szakértői review-hoz

- **1997. évi XXXI. törvény 17. §**, Nemzeti Jogszabálytár.
- **2012. évi C. törvény 209/A. §**, Nemzeti Jogszabálytár.
- **2009. évi XLVII. törvény** a bűnügyi nyilvántartási rendszerről, Nemzeti Jogszabálytár – az erkölcsi bizonyítványhoz (HUM-SAFE-05).
- **Kék Vonal Gyermekkrízis Alapítvány**, 116-111 és 116-000 aktuális szolgáltatásleírás.
- **Lelki Elsősegély Telefonszolgálatok Szövetsége**, 116-123.
- **Hasomer Hacair Magyarország – Somer–Magyar szótár**, „Memuna” szócikk (https://somer.hu/somer-magyar-szotar/).
- **Hasomer Hacair Magyarország – Kapcsolat** (https://somer.hu/kapcsolat/): a mindenkori Memuna és a Somer központi telefonszáma (HUM-SAFE-01).
- Az éles review napján elérhető aktuális állami/ágazati gyermekvédelmi módszertani útmutató.

A repository nem dönthet a szervezet konkrét jogállásáról, jelzési láncáról vagy egyedi ügy jogi minősítéséről a kijelölt jóváhagyók (§5) helyett.
