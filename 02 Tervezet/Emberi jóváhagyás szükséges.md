# Emberi döntési csomag

> **Cél:** egyetlen helyen legyen minden olyan nyitott tétel, amelyet a repository nem dönthet el a szervezet helyett.
> A szakmailag vagy dokumentációból eldönthető kérdések nem kerülnek ide.
>
> **Szabály:** minden érintett fájl az alábbi döntésazonosítóra hivatkozik. Ugyanazt a döntést nem tartjuk fenn több, egymástól független `KITÖLTENDŐ` mezőben.
>
> **2026-10-02 – projektgazdai döntések:** a projektgazda minden tételben döntött, és a tananyag ezeket alkalmazza. A tételek lezártak (dátum, jóváhagyó és bizonyíték a `tools/content_integrity.py` lezárási szabálya szerint). A megnevezett szerepek (Memuna, DPO, programvezető stb.) későbbi ellenőrzése **vétó / minőségellenőrzés (QA)**, nem új döntési kapu: ha valamelyikük vétóz, a tétel újranyílik, és a tananyag ahhoz igazodik. A release-kapuk ettől még nem zártak: mindegyik csak a `RELEASE-READINESS.md` táblázatának „Bizonyíték” oszlopa szerinti bizonyítékkal és a tracker-issue-ban rögzített lezárással zárul.
>
> **Staging ≠ élesítés:** ezek a döntések nem akadályozzák a zárt, szerkesztői Moodle-staging felépítését tesztadatokkal. Ahol a táblázat „éles kurzust” blokkol, ott valódi madrih nem kaphat hozzáférést a döntés lezárásáig.

## 1. Gyermekvédelem

### HUM-SAFE-01 — Helyi gyermekvédelmi jelzési lánc — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

| Mező | Tartalom |
|---|---|
| **Kérdés** | Ki a kijelölt gyermekvédelmi felelős, mi az elérhetősége, ki a helyettes/alternatív út összeférhetetlenség esetén, és mi a helyi akut-veszély eszkaláció? |
| **Miért szükséges** | M0, M3 és M7 több helyen konkrét felelőshöz küldi a madrihot. Ezt név és jóváhagyott helyi folyamat nélkül nem szabad élesben ígérni. |
| **Mi bizonyítható a repóból** | A madrih nem nyomoz, nem konfrontál feltételezett elkövetőt, nem ígér teljes titoktartást, és felelős felnőttet von be. Közvetlen életveszélynél a 112 sürgősségi út. |
| **Mit kell eldönteni** | felelős neve/szerepe és elérhetősége; helyettes/külső út; mozgalmi/országos eszkaláció; akut veszély helyi protokollja; dokumentálás helye és jogosultsága; **az M3 kanonikus lépéstérképe (eldöntve: az M3.B ötlépéses útja – lásd lent)**; jóváhagyás és következő felülvizsgálat dátuma |
| **Javasolt alapértelmezés** | Nincs szervezetfüggetlen alapértelmezés. A kurzus addig csak szerepnevet használhat belső stagingben, learner-facing kiadásban nem maradhat névtelen kontakt. |
| **Projektgazdai döntés (2026-10-02)** | Az **M3.B ötlépéses jelzési útja az egyetlen kánon**: 1. Észleld, és vedd komolyan. 2. Hallgasd meg, és ne ígérj teljes titoktartást. 3. Ne nyomozz, ne konfrontálj, és ne próbáld egyedül megoldani. 4. Azonnal vond be a kijelölt **Memunát** – összeférhetetlenség esetén a név szerint kijelölt helyettesét. 5. Közvetlen veszélynél előbb a biztonság és a **112**, utána a belső jelzés. A gyermekvédelmi ügy dokumentációja nem Moodle-ben, hanem külön, hozzáférés-korlátozott incidensnyilvántartásban készül. Indoklás: a Somer–Magyar szótár a Memunát nevezi meg a sértéssel, bántalmazással, zaklatással kapcsolatos ügyek felelőseként; a Gyvt. 17. § (1) a jelzőrendszer résztvevői között egyesületeket is nevesít (`Gyermekvédelem – release gate.md` §3.1). |
| **Kontakt és nyilvántartás (projektgazdai döntés, 2026-10-02)** | Tanulói elsődleges gyermekvédelmi kontakt: a Somer mindenkori, a `somer.hu/kapcsolat` oldalon publikált **Memunája** (2026-10-02-án: Marci). Helyettes: a **Ros Hinuh** (oktatási vezető; 2026-10-02-án: Lili). Ha bármelyikük érintett, a másikhoz kell fordulni; ha mindkettő érintett vagy nem elérhető: Kék Vonal **116-111**, bántalmazott vagy eltűnt gyermek ügyében **116-000**, közvetlen veszélyben **112**. Telefon: a Somer központi száma, **+36 70 42 76 637** (+36-70-HA-SO-MER; a kapcsolati oldal szerint hétköznap 10–18). Incidensnyilvántartás: Google Workspace Shared Drive → `Restricted / Safeguarding / Incidents`; hozzáférés csak a Memunának, a helyettesnek és a szervezeti vezetőnek; nem Moodle, nem GitHub. A HUM-SAFE-01…05 együtt a **Gyermekvédelmi működési standard v1.0 (Child Protection Operating Standard v1.0)**: a képzés elsődleges normatív gyermekvédelmi dokumentuma (`Gyermekvédelem – release gate.md` §5.1). |
| **Utólagos ellenőrzés (vétó/QA)** | a Memuna; a helyettes (Ros Hinuh). |
| **Jóváhagyó** | **Memuna** (a Somer gyermekvédelmi felelőse) mint egyetlen felelős jóváhagyó; a programvezető operatív társdöntő; jogi szakértő csak a jogi minősítésnél. *(Projektgazdai döntés a jóváhagyói rendről, 2026-10-02; korábban: gyermekvédelmi felelős + szervezeti vezetés.)* |
| **Blokkol** | éles M0 safety-kontakt, M3.3, M3.B, M3-kapu, M7 gyermekvédelmi részei és M7-kapu |
| **Érintett források** | `Gyermekvédelem – release gate.md`, M0.2, M0.4, M0.A, M1.A, M2.A, M2.4, M2-kapu, M3.3, M3.B, M3-kapu, M4.2, M4.3, M4.A, M4.B, M5.2, M6.3, M6.4, M6.A, M7.2, M7.3, M7.4, M7.B, M7-kapu, Z.3, Z.A |
| **Implementáció a döntés után** | egyetlen jóváhagyott kontaktblokk kerül a Moodle-be; minden tananyag-hivatkozás ezt használja. |

### HUM-SAFE-02 — Négyszemközti / safer-working szabály — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

| Mező | Tartalom |
|---|---|
| **Kérdés** | Milyen feltételekkel beszélhet képző vagy madrih kettesben kiskorúval? |
| **Miért szükséges** | A tananyag több helyen felkavaró témát dolgoz fel, és M7-ben a peulatervnek is kezelnie kell a négyszemközti helyzeteket. |
| **Biztonságos jelenlegi minimum** | A tananyag nem ír elő automatikus félrevonulást. A beszélgetés diszkrét, de átlátható. *(A korábbi „kérj be egy másik képzőt/felnőttet” tartalékszabályt a lenti projektgazdai döntés váltotta fel; a szabály szövege a `Gyermekvédelem – release gate.md` §4.2-ben él.)* |
| **Valódi alternatívák** | pl. látótávolság/nyitott ajtó; második felnőtt jelenléte; második felnőtt tudtával végzett beszélgetés. A szervezet dönti el, melyik és milyen dokumentálással elfogadható. |
| **Projektgazdai döntés (2026-10-02)** | A safer-working szabály **minden fizikai és digitális 1:1 helyzetre** vonatkozik: privát üzenet, voice chat, videóhívás és mentori beszélgetés is. Kiskorúval személyes közösségimédia-fiókról nem kommunikálunk, szervezeti csatorna használható. 1:1 helyzet csak indokolt esetben, átlátható módon, egy másik felelős tudtával. Online kiscsoportos szobában lehetőleg legalább két résztvevő legyen, a felnőtt jelenléte váltakozó és ellenőrizhető; egy felnőtt és egy kiskorú elszigetelt szobája csak előre meghatározott kivételként. Kiskorúnak küldött személyes privát üzenet soha nem „helyes” kvízválasz; hivatalos csatornán küldött logisztikai üzenet lehet helyes, gyermekvédelmi helyzet megoldásaként nem. A szabály szövege a `Gyermekvédelem – release gate.md` §4-ben él. |
| **1:1 kivételek (projektgazdai döntés, 2026-10-02)** | Engedélyezett kivétel csak: (a) előre egyeztetett mentorbeszélgetés, (b) biztonsági vagy feltárási beszélgetés, (c) rövid technikai segítség. Legfeljebb 30 perc, hivatalos csatornán vagy fizikailag átlátható térben, és egy másik felelős tud róla. Nincs zárt privát szoba, személyes közösségimédia-fiók, eltűnő üzenet vagy felvétel. A naplóba csak dátum, résztvevők, időtartam, célkategória és utánkövetés kerül, a beszélgetés tartalma nem. Ha gyermekvédelmi ügy lesz belőle, külön incidens-azonosítóra vált. A szabály helye: `Gyermekvédelem – release gate.md` §4.2. |
| **Utólagos ellenőrzés (vétó/QA)** | a Memuna. |
| **Jóváhagyó** | Memuna (gyermekvédelmi felelős) |
| **Blokkol** | learner-facing safety instrukciók véglegesítése és M7 R4/Q14 helyi megfelelése |
| **Implementáció a döntés után** | a `Gyermekvédelem – release gate.md` egyetlen szabálymezője frissül; a tananyag nem másolja szét, csak erre hivatkozik. |

### HUM-SAFE-03 — A madrih saját érintettsége és kiskorú madrih státusza — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

| Mező | Tartalom |
|---|---|
| **Kérdés** | Kihez fordulhat bizalmasan a 15–17 éves madrih, hogyan maradhat ki érzékeny gyakorlatból, és milyen felnőtt felügyelet kötelező számára terepen? |
| **Miért szükséges** | A tananyag bántalmazást, önsértést, identitást és határhelyzeteket érint. A résztvevő maga is lehet érintett és kiskorú. |
| **Javasolt szakmai minimum** | szégyenítés nélküli `passz`/alternatív feladat; érzékeny feltárásnál nem marad egyedül; a 18 év alatti madrih nem kap egyedüli felnőtt felelősséget. |
| **Mit kell még eldönteni** | konkrét bizalmas kontakt, szülő/gondviselő bevonásának helyi folyamata, felnőtt:madrih felügyeleti arány |
| **Projektgazdai döntés (2026-10-02)** | A 15–17 éves madrih vezethet peulát, de soha nem ő az egyetlen felelős felnőtt. Minden éles terepi alkalmon jelen van egy jóváhagyott, felkészített, 18 év feletti felnőtt – fizikailag ott van, vagy ugyanazon a helyszínen azonnal elérhető –, és a gyermekvédelmi felelősség az övé. Érzékeny gyakorlatból bárki indoklás nélkül passzolhat. Felkavart kiskorút nem küldünk ki egyedül: kijelölt biztonságos hely és egy felnőtt van vele. |
| **A nyitott pontok döntése (projektgazdai döntés, 2026-10-02)** | Bizalmas kontakt: a mentor vagy a Somer gyermekvédelmi kontaktja (a Memuna), a „ha téged is érint” blokk szerint. Gondviselő: kiskorúnál bevonjuk, kivéve, ha ez növelheti a veszélyt, vagy maga a gondviselő érintett a feltételezett problémában; ilyenkor a Memuna a biztonságos külső utat választja. Felügyelet: minden éles terepi alkalmon legalább egy jelen lévő (vagy a helyszínen azonnal elérhető), felkészített, 18 év feletti felnőtt. Az egységes „ha téged is érint” blokk szövege a `Gyermekvédelem – release gate.md` §4.3-ban él, és a tananyag szó szerint ezt használja. Érintett források: M0.1, M0.2, M1.1–M1.4, M2.A, M2.4, M3.3, M3.4, M3.B, M4.1, M4.2, Z.2, Z.3, Z.A, a Z hub 5. szakasza, `Terepgyakorlat – 2. félév.md`, LMS-Z-03, M4.A, M6.A, M7.B (a blokk szó szerint: M0.1, M0.2, M1.1–M1.4, M2.A, M2.4, M3.3, M3.4, M3.B, M4.1, M4.2, Z.2, Z.A). |
| **Utólagos ellenőrzés (vétó/QA)** | a Memuna és a programvezető. |
| **Jóváhagyó** | Memuna (gyermekvédelmi felelős) + programvezető |
| **Blokkol** | éles learner-facing safety tájékoztató és terepgyakorlat |
| **Implementáció a döntés után** | rövid, azonos szövegű „ha téged is érint” blokk a releváns modulokban és a kurzus elején. |

### HUM-SAFE-04 — Alkohol- és dohányzási szabály — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A konkrét helyi szabályt nem a tananyag találja ki. **Jóváhagyó:** szervezeti vezetés + Memuna (gyermekvédelmi felelős). **Blokkol:** csak azokat a learner-facing példákat, amelyek konkrét helyi tiltást vagy korhatárt állítanak. **Implementáció:** az M3.4 a szabály lényegét tanítja, és a szervezeti szabályra hivatkozik; a szabályt nem másolja le teljes egészében.

**Projektgazdai döntés (2026-10-02)**: kiskorúaknak szóló programon nulla alkohol, dohány, e-cigaretta (vape) és nikotintermék; 18 év alatt ezek egyike sem. Felelős felnőtt szolgálat alatt nem fogyaszt alkoholt, és nem lehet befolyásolt állapotban. Dohányozni csak szolgálaton kívül, kijelölt helyen, a gyerekektől elkülönítve lehet. A törvény minimumként tiltja az alkohol és a dohány kiszolgálását 18 év alatt; a szervezet ennél szigorúbb szabályt alkalmaz.

**Utólagos ellenőrzés (vétó/QA)**: a szervezeti vezetés és a Memuna.

### HUM-SAFE-05 — Stáb-alkalmasság és gyermekvédelmi felkészítés — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

| Mező | Tartalom |
|---|---|
| **Kérdés** | Milyen alkalmassági/vetting ellenőrzés és milyen dokumentált gyermekvédelmi felkészítés kell a programban dolgozó 18 év feletti képzőknek, mentoroknak és önkénteseknek, illetve a 15–17 éves madrihoknak? |
| **Miért szükséges** | A program kiskorúakkal dolgozik, de a repository nem nevezhet meg automatikusan egy konkrét hatósági ellenőrzést vagy dokumentumtípust minden szerepre. |
| **Szakmai minimum** | a stáb ismeri a jóváhagyott gyermekvédelmi láncot, az összeférhetetlenségi utat, a feltárás kezelését és a safer-working szabályt; a kiskorú madrih nem kap egyedüli felnőtt felelősséget. |
| **Mit kell eldönteni** | szerepkörönként szükséges alkalmassági ellenőrzés; felkészítés tartalma; nyilvántartás; megújítás/felülvizsgálat |
| **Projektgazdai döntés (2026-10-02)** | Szerepkör-alapú alkalmassági rend. 18 év feletti képző, mentor és rendszeresen gyerekekkel dolgozó önkéntes: személyazonosság-ellenőrzés, a szerephez szükséges erkölcsi bizonyítvány, a Gyermekvédelmi működési standard v1.0 (`Gyermekvédelem – release gate.md` §5.1) elfogadása, gyermekvédelmi + safer-working + adatvédelmi képzés; évente rövid megújító képzés és nyilatkozat; új szerepkörnél új ellenőrzés. 15–17 éves madrih: képzés + magatartási kódex + felnőtt felügyelet. |
| **Erkölcsi bizonyítvány (projektgazdai döntés, 2026-10-02)** | 18 év feletti képző, mentor és rendszeresen, közvetlenül gyermekekkel dolgozó önkéntes: hatósági erkölcsi bizonyítvány, amely igazolja, hogy (a) büntetlen előéletű, és (b) nem áll foglalkozástól vagy tevékenységtől eltiltás hatálya alatt. Belépéskor legfeljebb 90 napos dokumentum, majd kétévente új, közben éves önnyilatkozat (háttér: a bűnügyi nyilvántartási rendszerről szóló 2009. évi XLVII. törvény). A régi, elérhetetlen Child Protection Policy helyett a Gyermekvédelmi működési standard v1.0 az irányadó (HUM-SAFE-01). |
| **Utólagos ellenőrzés (vétó/QA)** | a szervezeti vezetés és a Memuna; jogi kérdésben jogi szakértő. |
| **Jóváhagyó** | szervezeti vezetés + Memuna (gyermekvédelmi felelős), jogszabályi alkalmassági kérdésnél jogi szakértő |
| **Blokkol** | valódi résztvevőkkel futó program indítása, nem a zárt Moodle-staging |
| **Implementáció** | stáb-checklist, jóváhagyási bizonyíték és felkészítési nyilvántartás; a tananyag csak a jóváhagyott eljárásra hivatkozik. |

---

## 2. Adatvédelem

### HUM-PRIV-01 — Moodle-adatkezelési mátrix — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

| Mező | Tartalom |
|---|---|
| **Kérdés** | Activitynként mi a cél, jogalap, hozzáférés, megőrzés, törlés/export és harmadik fél? |
| **Miért szükséges** | A kurzus reflexiókat, Assignmenteket, kvízeredményt és részben identitáshoz kötődő szöveget kezel. |
| **Jogi keret** | A GDPR 8. cikk nem általános „minden kiskorú adatához szülői hozzájárulás” szabály. A jogalapot adatkezelési célonként kell meghatározni. |
| **Javasolt alapértelmezés** | adatminimalizálás; személyes/érzékeny történet ne legyen kötelező; mentor csak azt lássa, amihez pedagógiai vagy biztonsági feladata van. A konkrét jogalap és megőrzés nem található ki. |
| **Projektgazdai döntés (2026-10-02)** | Egyetlen activity-szintű adatkezelési mátrix a kánon (`Adatvédelem – tanulói adatok és AI.md` §3 + az activity manifest privacy-osztályai). Mindenhez a legszűkebb szükséges hozzáférés: zárt kvíz pontszáma – az értékelő; szabad szöveg, reflexió – csak a kijelölt mentor/értékelő, és csak ha ténylegesen szükséges; a gyermekvédelmi feltárás nem normál tanulási rekord, hanem külön gyermekvédelmi nyilvántartásba kerül; mentori jegyzet csak minimális fejlődéstámogató adat, „árnyékdosszié” nincs; Google-sablon csak szervezeti fiókban, korlátozott megosztással; politikai, vallási vagy világnézeti válasz nem lehet fiókhoz kötött szavazás. A Program terv §4 és §7 ütközésében a szigorúbb, kisebb hozzáférést engedő szabály érvényes. Indoklás: a Somer adatkezelési tájékoztatója és a GDPR 5. cikke (célhoz kötöttség, adattakarékosság, korlátozott tárolás). |
| **Jogalap és megőrzés (projektgazdai döntés, 2026-10-02)** | A rögzített jogalap- és megőrzési mátrix az `Adatvédelem – tanulói adatok és AI.md` §3-ában él (pl. Moodle-fiók és végső completion: a képzés vége + 24 hónap; nyers kvízpróbálkozások: a végső megerősítés + 90 nap; szabad szöveges reflexió: a képzés vége + 90 nap; gyermekvédelmi incidens: külön rendszerben, az érintett 25. születésnapjáig vagy a lezárás + 7 évig, amelyik később jár le). Politikai, vallási, egészségügyi vagy más különleges adat normál tanulási activityben nem gyűjthető; ha feltáráskor mégis megjelenik, kikerül a Moodle-ből, és az incidensfolyamatba kerül. |
| **Utólagos ellenőrzés (vétó/QA)** | a DPO/jogi felelős. |
| **Jóváhagyó** | adatkezelő privacy/DPO/jogi felelőse |
| **Blokkol** | éles learner release minden személyes adatot tároló activitynél |
| **Implementáció a döntés után** | az activity manifest privacy-osztályai szerinti beállítás + learner-facing adatvédelmi tájékoztató + törlési folyamat. |

### HUM-PRIV-02 — Fotó, videó, hang és kézírás — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A szervezet dönti el a felvétel célját, jogalapját, hozzáférését, tárhelyét, megőrzését és törlését, továbbá azt, hogy az **M0.A kézírásos plakát fotózásánál** a beazonosítható tartalom eltávolítása önmagában elegendő-e az adott célhoz. A tananyag alapértelmezése: **ne gyűjts felvételt, ha ugyanaz a pedagógiai cél elérhető nélküle; személyes telefon/felhő nem alapfolyamat.**

**Jóváhagyó:** privacy/DPO/jogi felelős. **Implementáció:** központi média-/felvételi szabály, amelyre minden médiaaktivitás hivatkozik (pl. M0.A, M1.A, M4.A–M4.B, M5.A, M6, Z.A, a Z.4 videós útja).

**Projektgazdai döntés (2026-10-02)**: alapértelmezés: nincs fotó, videó vagy hangfelvétel, csak indokolt célból; minden médiaaktivitásnál rögzíteni kell a célt, a jogalapot, a hozzáférést, a megőrzést és a törlést. A kézírásos plakátot lehetőleg fizikailag őrizzük meg. Ha fotó kell: előbb a nevek és azonosítók eltávolítása, a háttérben ne legyen gyerek, feltöltés ellenőrzött tárhelyre, majd törlés a saját eszközről. Tanulói szelfi vagy videó opcionális, kivéve, ha szakmailag ténylegesen nélkülözhetetlen.

Jogalap és megőrzés (projektgazdai döntés, 2026-10-02): fotó, videó és hang csak külön, önkéntes hozzájárulással, a cél teljesüléséig, legfeljebb 90 napig, hacsak nincs külön archiválási hozzájárulás (`Adatvédelem – tanulói adatok és AI.md` §3).

**Utólagos ellenőrzés (vétó/QA)**: a DPO/jogi felelős.

### HUM-PRIV-03 — Z.4 visszajelzés anonimitási szintje — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A core Moodle Feedback `Record user names` = `Anonymous` beállítása **név nélkül jeleníti meg a válaszokat**, de a Moodle saját dokumentációja szerint ez nem GDPR-értelemben vett teljes anonimitás; az activity completion is felhasználói fiókhoz kötődhet.

**Döntés:** ez a név nélküli működés megfelel-e a szervezeti célnak, vagy külön technikai anonimitás kell.

**Javasolt alapértelmezés:** learner-facing szövegben csak „név nélkül jelenik meg” állítás maradjon, amíg erősebb anonimitás nincs bizonyítva.  
**Jóváhagyó:** adatvédelmi/DPO felelős + programvezető. **Implementáció:** Z.4 Moodle Feedback-beállítás és adatvédelmi tájékoztató.

**Projektgazdai döntés (2026-10-02)**: a Z.4 képzési visszajelzés maradhat kötelező, de nem nevezhető anonimnak. A tanulói szöveg: **„A válaszok név nélkül jelennek meg a feldolgozásban.”** A Moodle Feedback `Anonymous` beállításánál a név nem jelenik meg a felületen, de a felhasználó azonosítója az adatbázisban marad, és a completion követhető (Moodle Docs, Feedback FAQ). Valódi anonimitáshoz a visszajelzést le kellene választani a fiókhoz kötött completionről.

**Utólagos ellenőrzés (vétó/QA)**: a DPO és a programvezető. A Z visszajelzés nyers válaszai 90 napig maradnak meg, utána csak összesítve (`Adatvédelem` §3).

### HUM-PRIV-04 — Külső generatív AI tanulói használata — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

**Döntés:** mely szolgáltató használható a madrihoknak, milyen életkori/guardian feltételekkel, milyen fiókkal és adatvédelmi beállítással.\
**Nem alku tárgya a tananyagban:** az `Adatvédelem – tanulói adatok és AI.md` §7 listája. Ez az egyetlen kanonikus promptkizárási lista; ez a dokumentum csak hivatkozik rá, nem másolja.

**Jóváhagyó:** privacy/DPO/jogi felelős + programvezető. **Implementáció:** a lenti megvalósítás (szervezeti végpont, nincs madrih-fiók); a tananyag a szolgáltatót nem reklámozza, az általános „jóváhagyott AI-eszköz” megfogalmazás maradhat, és minden AI-feladat mellett teljes értékű no-AI alternatíva áll.

**Projektgazdai döntés (2026-10-02)**: az AI használata mindig opcionális, a feladat nélküle is teljesíthető. A kurzus kiskorútól nem kér saját külső AI-fiókot: a használatot a szervezet közvetíti, a madrih nem regisztrál szolgáltatói fiókot (a megvalósítást lásd lent). A tanulói szöveg: „Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.”

Megvalósítás (projektgazdai döntés, 2026-10-02): `Moodle → a Somer szerveroldali végpontja → OpenAI Responses API`. A madrih nem regisztrál szolgáltatói fiókot; a promptot a képző vagy a szervezeti backend küldi (`/v1/responses`, `store=false`, nincs Conversations API, nincs tartós fájlfeltöltés; nincs személyes adat, nincs valódi hanih-eset, nincs gyermekvédelmi történet). Ha a szervezet számára elérhető, a ZDR (zero data retention) be van kapcsolva. A kurzus alkalmazó (deployer) szerepben jár el; a kezelők AI-jártassági felkészítést kapnak (AI Act 4. cikk), és az M7.2 elején 15 perces AI-jártassági blokk áll.

**Utólagos ellenőrzés (vétó/QA)**: a DPO/jogi felelős és a programvezető.

---

## 3. Programüzemeltetés

### HUM-OPS-01 — Központi ütemezés — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A repository **nem talál ki naptári dátumot**. Egyetlen program-szintű ütemezésből kell származtatni minden Moodle availability/due date értéket.

Kötelező döntések:
- program kezdete és a modulhetek tényleges dátumai;
- az offline peulák időpontjai;
- Assignment/Quiz határidők;
- **M7 v1 → M7.B visszajelzés/átdolgozás → v2** konkrét dátumai úgy, hogy v1 és v2 ne essen ugyanarra a napra, és a kettő között tényleges köztes visszajelzés + külön átdolgozási szakasz legyen;
- Z sorrend: Z.1–Z.3 → Z.A → Z.4.

**Jóváhagyó:** programvezető.  
**Implementáció:** az LMS-agent egy központi schedule-táblából tölti ki a dátumokat, nem egyes fájlok `KITÖLTENDŐ` mezőiből.

**Projektgazdai döntés (2026-10-02)**:
- A kapu eredményét legkésőbb 24 órával a következő fix alkalom előtt meg kell erősíteni. Pénteki A-peulánál: beadás szerda 18:00-ig, első értékelés csütörtök délután, megerősítés legkésőbb csütörtök 18:00-ig. A függőben lévő eredmény nem bukás.
- Az F-peula a nem teljesült kapu utáni, facilitált javítási alkalom, nem általános pótlás; a puszta lemaradásra a „Csendes pótlás” szolgál.
- A Peula v1-re a kijelölt mentor rubrikára épülő visszajelzést ad a v2 előtt.
- Az M0 sávja 60–80 perc, a Z online része 40–65 perc; a terepgyakorlat ettől külön.
- Időkeretek: a bottom-up összeg nyer (az M3 180–225 perc, vagyis 3–3,75 óra; az M1, M4 és M6 sávja is a saját összetevőiből adódik, a Program terv sávja ehhez igazodik); az M7.3 és az M7.4 H5P-ideje a pilotmérésig 15–20 perc; a Z.A 75 perces változat; az M5.F részlépés-sora 20–25 perces alsávot kap; az M5.3 késleltetett felidézése 72 órával az M5.3 teljesítése után nyílik, kötelező, de nem kapuzza a következő modult.

Naptár és időkeretek (projektgazdai döntés, 2026-10-02): indulás 2026-11-06 (péntek), zárás 2027-03-05 (péntek) **[SUPERSEDED: a naptári dátumokat a 11. szakasz (2026-10-05, pilot-ütemezés) felülírja]**; a teljes központi naptár (péntekek, kapu-beadások szerda 18:00, megerősítések csütörtök 18:00, téli szünet) az `LMS – activity manifest.md` központi ütemezési táblájában él. A V1 tervezési időkeretek (M0 2–2,5 óra, M1 2–3, M2 2,5–3,5, M3 3–3,75, M4 2,5–3,5, M5 3,5, M6 2,5–3, M7 4–5,5 óra; a Z online része 40–65 perc, a terepi rész külön; M7.3 és M7.4 15–20 perc/lecke) a hubokban és a `Program terv.md`-ben állnak. A pilot későbbi mérés, nem nyitott döntés és nem release-kapu. Az F-peula éles kapu sikertelensége után kötelező, puha kapunál ajánlott.

**Utólagos ellenőrzés (vétó/QA)**: a programvezető.

### HUM-OPS-02 — Támogatási kontaktok és mentori kapacitás — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

**Döntés:** technikai support csatorna, tanulási/mentor kontakt, valamint a tényleges mentor:madrih kapacitás.\
**Jóváhagyó:** programvezető.  
**Blokkol:** learner-facing support szöveg véglegesítése, nem a belső staging build.  
**Implementáció:** egy központi kurzusoldal „Segítség és kapcsolatok” blokkjából hivatkozik minden modul.

**Projektgazdai döntés (2026-10-02)**: a „Segítség és kapcsolatok” blokk négy, szerep szerinti kontaktot ad: technikai segítség, tanulási/programkontakt, a kijelölt mentor, és ettől külön a Memuna (gyermekvédelem). Nincs „mentor / felelős / vezető” típusú lánc. Mentor:madrih kapacitás: javasolt kiinduló plafon 1:8, legfeljebb 1:10.

Kapacitás (projektgazdai döntés, 2026-10-02): **kemény plafon 1:8** — egy mentor legfeljebb 8 aktív madrihot visz; az 1:10 tartalék kikerült (például 17 résztvevőhöz legalább 3 mentor kell). A gyermekvédelmi kontakt: lásd HUM-SAFE-01.

**Utólagos ellenőrzés (vétó/QA)**: a programvezető.

### HUM-A11Y-01 — Hozzáférhetőségi jóváhagyó szerepkör — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A szervezet nevezze meg, ki írja alá a kapus elemek pre-flight ellenőrzését. A specifikációban addig **szerepkör**, nem kitalált személynév szerepel.  
**Jóváhagyó:** programvezető. **Blokkol:** learner-facing release, nem a staging.

**Projektgazdai döntés (2026-10-02)**: hivatalos szerep a hozzáférhetőségi felelős. A szerző nem hagyja jóvá a saját munkáját; kis szervezetben a programvezető lehet a végső felelős, de az élesítés előtti ellenőrzést egy másik, a WCAG- és H5P-követelményeket ismerő személy végzi.

A szerep betöltése (projektgazdai döntés, 2026-10-02): a felelős (accountable) hozzáférhetőségi gazda a **Ros Hinuh** (jelenleg Lili); a független, élesítés előtti második ellenőrző **Marci**. A szerző nem hagyja jóvá a saját anyagát.

**Utólagos ellenőrzés (vétó/QA)**: a programvezető.

### HUM-PED-01 — Az M4 szakmai lektorálása — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

Az M4 hub, az M4.1–M4.4 leckék és az M4.A–M4.B peulák élesítés előtt emberi szakmai lektorálást írnak elő: a kvízitemek és disztraktorok, a sablonok, valamint az önfeltárást, kiállást kérő érzékeny gyakorlatok átnézését, a gyermekvédelmi és érzékeny tartalom külön felülvizsgálatával. A tananyag nem nevez meg lektort, és nem rögzít dátumot vagy verziót; ezek a `Program terv.md` 9.3. pontja szerinti release-jegyzőkönyvbe tartoznak.

**Jóváhagyó:** a szervezet által kijelölt szakmai lektor (kvíz, rubrika, sablonok); az önfeltáró és érzékeny gyakorlatoknál a Memuna (gyermekvédelmi felelős). **Blokkol:** az M4 élesítése valódi madrihoknak, nem a staging.

**Projektgazdai döntés (2026-10-02)**: az M4 éles release csak szakmai és gyermekvédelmi felülvizsgálat után történhet: a szakmai lektor felel a kvízért, a rubrikáért és a sablonokért, a Memuna az önfeltáró és érzékeny gyakorlatokért.

A felülvizsgálat (projektgazdai döntés, 2026-10-02): **elvégezve, az M4 szakmailag elfogadva**, négy kötelező korrekcióval: (1) az M4.2-ben a „ha komolynak érzed a helyzetet” helyett: „Ha a helyzet veszélyre, bántalmazásra, önsértésre vagy más gyermekvédelmi kockázatra utal, nem neked kell eldöntened, hogy elég súlyos-e: a jóváhagyott jelzési utat követed.”; (2) minden produktum-visszajelzés Megfigyelés → Hatás → Következő lépés, SBI csak megfigyelhető viselkedésre; (3) az M4.A-n nincs kötelező felvétel, a mini-színpad élő gyakorlat; (4) az M4.A és az M4.B előtt 24 órával Moodle-értesítő, az M4.B-re a résztvevő hozza vagy nyissa meg az M4.4 vázlatát, a képzőnek legyen nyomtatott tartalék sablonja. A modulcím marad.

**Utólagos ellenőrzés (vétó/QA)**: a szakmai lektor és a Memuna.

### HUM-GOV-01 — Terepgyakorlat rubrika ↔ KPI megfeleltetés — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

**Állapot:** lezárva (projektgazdai döntés, 2026-10-02): a 0–2 skála és a lenti KPI-képlet marad, a kalibrációs szabállyal kiegészítve.

**Javasolt (bevezetett) megoldás:** a terepgyakorlati rubrika **0–2-es skálán marad**. Az intake `≥4/5` célját skálafüggetlen normalizált százalékként riportoljuk:

`normalizált eredmény = (rubrikaátlag / 2) × 100`

Így **4/5 = 80% = 1,6/2**. A javasolt terepgyakorlati KPI tehát **≥80%**, illetve az aktuális 0–2-es rubrikán **átlag ≥1,6/2**. A megoldás nem módosítja a rubrika szintleírásait, és nem kényszeríti egységes skálára az M1–M7 modulrubrikákat.

**Döntés:** vagy 5 fokozatúra változik a terepgyakorlati rubrika, vagy a KPI-t definiálja újra a szervezet a 0–2 skálán. **Jóváhagyó:** programvezető + módszertani felelős. **Blokkol:** KPI-riport, nem a Moodle-staging.

**Projektgazdai döntés (2026-10-02)**: nem váltunk ötfokú skálára, a 0–2 marad: 0 = Még nem, 1 = Rendben (a minimum teljesül), 2 = Erős. A KPI: átlag ≥ 1,6, és minden biztonságkritikus soron legalább 1; a biztonsági sorok egymást nem kompenzálják. A pontozó a kijelölt mentor; a minták egy részét második értékelő kalibrálja.

Kalibráció (projektgazdai döntés, 2026-10-02): a minták **20%-át, de kohorszonként legalább 3 terepi értékelést**, valamint **minden biztonságkritikus bukó vagy határesetet (100%)** második értékelő is pontoz. Ha bármely soron 1 pontnál nagyobb az eltérés, vagy a minősítés eltér, az adott kohorsz mintája 40%-ra emelkedik, újrakalibrálással.

**Utólagos ellenőrzés (vétó/QA)**: a programvezető és a módszertani felelős.

**Implementáció:** `Terepgyakorlat – 2. félév.md` ezt az egyetlen képletet használja a KPI-riporthoz.

---

## 4. Mozgalmi tartalom

### HUM-SOMER-01 — Izrael/cionizmus és béke/palesztin dimenzió helyi megfogalmazása — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A repository nem alkot mozgalmi állásfoglalást. A helyi Somer/ken erősítse meg az M2-ben használt pontos megfogalmazást.  
**Jóváhagyó:** helyi mozgalmi/ideológiai felelős. **Blokkol:** az érintett M2-rész learner-facing véglegesítése.

**Projektgazdai döntés (2026-10-02)**: nem alkotunk új ideológiát: a helyi Ideológiai Kézikönyv a kánon (a könyv szerint a cionizmushoz hasonló eszméknél „a someres álláspontot” írja le). Az Izrael/palesztin dimenzió tanulói szövege a béke, az emberi jogok, az aktív felelősségvállalás és a vitán alapuló párbeszéd értékeiből épül (a projektgazda szerint a jelenlegi stratégia ezeket nevezi meg), és nem tesz úgy, mintha a tananyag önállóan politikai állásfoglalást hozna.

A végleges tanulói szöveg (projektgazdai döntés, 2026-10-02): „A Hasomer Hacair cionista mozgalom. Saját ideológiai kézikönyve szerint Izraelt a zsidó önmeghatározás kifejeződésének tekinti. A magyar Somer oktatásában ugyanakkor a béke, az emberi jogok, az egyenlőség, az aktív felelősségvállalás és a vitán alapuló párbeszéd alapértékek. A képzés nem várja el, hogy a résztvevők ugyanazt az aktuálpolitikai véleményt képviseljék. Izraelről, a palesztinokról és a konfliktusról ellenőrizhető tényekből, több nézőpont megismerésével és minden érintett emberi méltóságának tiszteletével beszélünk. Antiszemita, arab- vagy palesztinellenes általánosítás nem elfogadható. A madrih feladata nem egy politikai válasz megtanítása, hanem olyan beszélgetés vezetése, amelyben lehet kérdezni, vitatkozni, forrásokat vizsgálni és árnyalt álláspontot kialakítani.” Ez a Somer saját, dokumentált keretének összefoglalása, nem új politikai állásfoglalás; helye az M2 érintett része.

**Utólagos ellenőrzés (vétó/QA)**: a helyi ideológiai felelős.

### HUM-SOMER-02 — Kvuca-korosztályok — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

**Állapot:** lezárva (projektgazdai döntés, 2026-10-02): a háromcsoportos felosztás marad, a lenti verziózott forrással.

**Javasolt 2025/26-os felosztás:** **Parparim 6–9, Kivsza 10–12, Leviatán 13–17**.

**Forrás (verziózott hivatkozás):** „Oktatási terv 2025/2026 – Hasomer Hacair Magyarország” (Google Docs; a Somer „A Hasomer Hacair Ideológiai Kézikönyve” oldaláról „25/26 Oktatási terv” néven linkelve: https://docs.google.com/document/d/1L1zJJv0EcQxsOF9eaxwARrmS5Qh3XbUA1wla0A08hZE ; megtekintve 2026-10-02). A bevezető szerint: „Parparim (6-9)”, „Kivsza (10-12)”, „Leviatán (13-17)”. A repó csak hivatkozik rá, másolatot nem tárol. A korábbi `Zorea 16+` külön csoport a repo történeti maradványa; a tananyag a háromcsoportos modellt használja.

**Projektgazdai döntés (2026-10-02)**: a háromcsoportos modell marad (Parparim 6–9, Kivsza 10–12, Leviatán 13–17), a fenti verziózott forrással.

Írásmód (projektgazdai döntés, 2026-10-02): a magyar Somer first-party alakjai a kánon — **Leviatán**, továbbá madrih, hanih, hágsámá, dugma isit; a teljes tanulói korpusz egyszeri, gépi migrációt kap, a belső azonosítók nem változnak.

**Utólagos ellenőrzés (vétó/QA)**: a ken-vezető / mozgalmi felelős.

**Jóváhagyó:** ken-vezető / mozgalmi felelős. **Blokkol:** a korosztályprofilok hivatalosként való kommunikálása.

**Implementáció:** a glosszárium, M3 korosztálymodul, az ezekre épülő M6/M7 hivatkozások és a kapcsolódó média-specifikációk ezt a háromcsoportos modellt használják.

### HUM-SOMER-03 — Hágsámá helyi megfogalmazása — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A pontos helyi jelentés és tananyagbeli megfogalmazás mozgalmi döntés. **Jóváhagyó:** mozgalmi/ideológiai felelős.

**Projektgazdai döntés (2026-10-02)**: a Somer–Magyar szótár szerint: „Hágsámá – Jelentése: a someres önmegvalósítás. Az a folyamat, ami során elérjük a somer által kitűzött célokat, megvalósítjuk a számunkra ideális világképet.” A tanulói mondat: „A *hágsámá* a someres értékek gyakorlati megvalósítása: nemcsak beszélünk arról, milyen világot szeretnénk, hanem személyesen és közösségként teszünk is érte.”

Írásmód (projektgazdai döntés, 2026-10-02): **hágsámá** (a Somer–Magyar szótár alakja), lásd HUM-SOMER-02.

**Utólagos ellenőrzés (vétó/QA)**: a mozgalmi/ideológiai felelős.

---

## 5. Média és szolgáltatók

A részletes gyártási alternatívák a `Média-assetek/PRODUCTION-DECISIONS.md` fájlban vannak. Ez a döntési csomag csak azokat a pontokat tartja nyilván, amelyek emberi jóváhagyás nélkül nem zárhatók.

**Projektgazdai döntés a médiakapuk release-hatásáról (2026-10-02):** a jogi és gyermekvédelmi médiakapuk blokkolják az általuk érintett tanulói asset release-ét. A teljes release csak akkor `READY`, ha minden release-hatókörű médiakapu zárt, vagy az érintett assetet eltávolították, illetve helyettesítették. Lehet külön `CONTENT_READY / MEDIA_PENDING` állapot, de a „specifikáció zárt” állítás nem igaz, amíg kötelező asset nyitott jogi kapun áll. **Utólagos ellenőrzés (vétó/QA)**: a release owner és a jogi/adatvédelmi felelős.

### HUM-MEDIA-01 — Vizuális rendszer — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A márka/stílus végleges választása a `PRODUCTION-DECISIONS.md` **D1** döntése. **Jóváhagyó:** projekt kreatív/márkafelelős.

**Projektgazdai döntés (2026-10-02):** a D1 lezárva. D1-a igen: a hivatalos Somer-paletta; D1-b igen: a 2022-es arculati kézikönyv és a hivatalos SVG színgenerációja a kánon; D1-c: a B változat (Source Sans 3 + produkciós semleges skála); D1-d igen: a szín szemantikája modulhatókörű, az elsődleges jel a forma és a felirat; D1-e: a `#2B2523` csak a logón belül. Kanonikus paletta: `#D84C15`, `#F2BC00`, `#87B027`, `#369D37`, `#08A0CA`, `#82CDE9`. A részletes produkciós értékek a `Média-assetek/PRODUCTION-DECISIONS.md` D1-ében és a `PRODUCTION-STYLE-TOKEN.md` B változatában állnak. Az R5 nyitott értéke ezzel kitöltve.

**Utólagos ellenőrzés (vétó/QA)**: a kreatív/márkafelelős.

### HUM-MEDIA-02 — Hangjogosultság és ElevenLabs-hang létrehozása — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A két forrásbeszélő hangjához dokumentált jogosultság kell. A konkrét klónozási módot csak az aktuális ElevenLabs-feltételek szerint szabad választani. **Professional Voice Clone esetén a szolgáltató jelenlegi szabálya szerint a beszélő a saját hangját maga hozza létre és hitelesíti, majd privát módon oszthatja meg; más személy PVC-jét a projektfiók nem hozhatja létre helyette.**  
**Jóváhagyó:** jogi/privacy felelős + a hang tulajdonosa. **Implementáció:** a `VOICE-BIBLE.md` csak a ténylegesen létrehozott, jogosult voice ID-t kapja meg.

**Projektgazdai döntés (2026-10-02)**: a J1, J2, V1 és V3 médiakapu kanonikus felelős- és bizonyíték-mezőt kap, a HUM-MEDIA-02 alkapuiként (`Média-assetek/RIGHTS-EVIDENCE.md`). A forrás-beszélők a repóban álnéven szerepelnek (`VOICE-SRC-01`, `VOICE-SRC-02`); a valódi név, a szerződés vagy hozzájárulás, a hatókör és a dátum a korlátozott hozzáférésű jogosultsági nyilvántartásba kerül. A D11 a hangjogosultsági bizonyítékig blokkolt; az E-9 jogi felülvizsgálatra vár (`LEGAL_REVIEW_REQUIRED`).

**Projektgazdai döntés (2026-10-03, VO 2. fázis; bizonyíték: `01 Fejlesztés/04 Audit/2026-10-03 Projektgazdai döntések – VO 2. fázis.md`)**: a két ElevenLabs-hang (a kanonikus narrátorhang és a második hang) létezik; a hanghasználati jog tisztázott, a hang tulajdonosai kifejezetten hozzájárultak (VO D-01). Az elsődleges narrátor a kanonikus narrátorhang; a második hang jogtisztázott (VO D-14). A formális bizonyíték — a `VOICE-RIGHTS-REGISTER` nem személyes hivatkozása és a jogi/privacy jóváhagyó minősítése — bizonyíték-kapu (megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő). A két forrás-beszélő nagykorú (projektgazdai tényközlés, 2026-10-03, K5); a korlátozott hozzáférésű jogosultsági nyilvántartás ezt „nagykorúság ellenőrizve” bejegyzésként rögzíti, életkor, születési dátum és igazolvány-adat nélkül (kiegészítő döntés, 2026-10-03, K6; bizonyíték: `01 Fejlesztés/04 Audit/2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`); a bejegyzés és a jóváhagyói minősítés bizonyíték-kapu; utólagos ellenőrzés (vétó/QA): DPO. A voice-ID nem nyilvános: csak a VO QA-repó gyártási konfigurációjában él, a `VOICE-BIBLE.md`-be sem kerül; ez a fenti „Implementáció” sort felváltja (kiegészítő döntés, 2026-10-03, K3). A D11 dialógushangjait az első gyártási körre a VO D-14 és a kiegészítő döntés (2026-10-03, K4; bizonyíték: `01 Fejlesztés/04 Audit/2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`) rendezte (Madrih A: a kanonikus narrátorhang, Madrih B: a második hang a kalibrálása után, beszélőnként szegmentálva); a szájszinkronos gyártási út nyitott.

Nyilvántartás és előzmények (projektgazdai döntés, 2026-10-02): a korlátozott hozzáférésű hangjogosultsági nyilvántartás helye Google Workspace Shared Drive → `Restricted / Rights / Voice`, fájl: `VOICE-RIGHTS-REGISTER`; szerkesztheti Marci és Lili, a producer csak az álneveket látja. Kötelező mezők: álnév, valódi név, hozzájárulás/szerződés hivatkozása, engedélyezett felhasználás, modell/szolgáltató, terület, időtartam, visszavonás, aláírás dátuma, a bizonyíték helye/hash-e, valamint a nagykorúság ellenőrzése (igen/nem, dátum, az ellenőrző szerepe; életkor, születési dátum és igazolvány-adat nélkül — kiegészítő döntés, 2026-10-03, K6). Valódi név nem kerül a Gitbe; a git-előzményekben maradt neveket a repo tulajdonosa egyszeri `git filter-repo` tisztítással cseréli álnévre (a régi clone-ok és forkok nem garantáltan törölhetők). A D11 a hangjogosultsági bizonyítékig blokkolt; az E-9 jogi felülvizsgálaton.

**Utólagos ellenőrzés (vétó/QA)**: a jogi/adatvédelmi felelős és a hang tulajdonosai.

### HUM-MEDIA-03 — HeyGen/avatar és média-jogok — LEZÁRVA

**Lezárva:** 2026-10-02

**Jóváhagyta:** projektgazda

**Bizonyíték:** `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md` (a projektgazda 1. és 2. válasza, szó szerint)

A választott HeyGen-folyamathoz szükséges személy-, hang-, képmás- és szolgáltatói jogosultságokat a `RIGHTS-EVIDENCE.md` szerint kell lezárni. **Jóváhagyó:** jogi/privacy felelős + érintett jogosult(ak); gyermekvédelmi tartalomnál a Memuna is.

**Projektgazdai döntés (2026-10-02)**: gyermekvédelmi vagy krízis-HOOK-ban nem használunk készlet-AI-beszélőfejet: az M2.4, az M3.3 és az M3.4 HOOK-ja hangalámondás + tipográfia/grafika. Ha mégis beszélőfej kell, csak egyedi, nagykorú avatar, kifejezett hozzájárulással, jogi/adatvédelmi és gyermekvédelmi felülvizsgálattal.

**Utólagos ellenőrzés (vétó/QA)**: a jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna. A többi HOOK készlet-avatarjának képmás-licencét a gyártás előtt dokumentálni kell (R2).

---

## 6. Nem emberi döntés, ezért nem marad itt nyitott kapuként

- M0 belépőkvíz: a jelenlegi kánon szerint diagnosztikus completion-jelző, nem éles kapu.
- H5P szabad szöveg: technikai megvalósítási/acceptance-kérdés, nem szervezeti döntés.
- Moodle activity-ID-k: build-kimenetek; a staging build után automatikusan rögzítendők.
- Moodle/H5P verziók: célkörnyezetből kiolvasható tények.
- Gyártási becslések: projekttervezési adat, nem learner-facing release-kapu.
- Fájlnév-stílusok: szerkesztői karbantartás, nem release-gate.

---

## 7. Dokumentált, elfogadott reziduumok

- A súlyos M3-es eseteket harmadik személyű esetelemzéssel dolgozzuk fel; traumatikus szerepjáték nincs.
- A Z.4 hivatalos reflektív produktuma **Moodle Assignment**.
- Az M0-kvíz completion-alapú diagnosztikus jelző.
- Az M7 kétlépcsős produktumfolyam invariánsa: **v1 → köztes visszajelzés/átdolgozás → v2**.
- A pedagógiai alapelv: **kevesebb gépezet, több mozgalom**.

---

## 8. Projektgazdai döntések HUM-azonosító nélkül (2026-10-02)

Ezek szerzői, értékelési és szerkesztési döntések. A tananyag ezeket alkalmazza; a jobb oldali szerep utólagos ellenőrzése vétó / minőségellenőrzés (QA). Release-kaput nem nyitnak és nem zárnak.

| Téma | Projektgazdai döntés | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|
| Próbálkozások, melyik eredmény számít | 1 normál + 1 javító próbálkozás; éles kapunál a javító próbálkozás a kötelező F-peula után nyílik (a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele, 3. kör), puha kapunál automatikus; további a képző által; a legjobb megerősített eredmény számít, a teljesítés nem romolhat vissza | programvezető + értékelési felelős |
| Puha és éles kapu | puha kapu: formatív, nem blokkol; éles kapu: a minimumfeltétel és a szükséges emberi megerősítés nélkül nincs következő kapuzott tartalom (`Program terv.md` §5) | programvezető + értékelési felelős |
| Üres sablon | completion csak tényleges, minimálisan értelmezhető tartalommal; a fájlfeltöltés önmagában nem completion | értékelési felelős |
| Az M7 kvíz helye | a Peula v2 előtt, felkészültségi kapuként; a v2 az alkalmazás bizonyítéka | programvezető + értékelési felelős |
| Az M1 rubrikahorgonyai | 0 = Még nem, 1 = Rendben, 2 = Erős | modulgazda / módszertani lektor |
| Produktum-visszajelzés | Megfigyelés → Hatás → Következő lépés; az SBI viselkedésre való | módszertani felelős |
| A Peula v2 kvucája | valós kvucára csak nem azonosító, csoportszintű információval; különben kitalált profil | DPO + programvezető |
| Esetalapú kapuproduktum | csak kitalált, életszerű eset; valós eset névtelenítve sem | Memuna + DPO |
| Kritikus követelmények, A/B sarok | a kritikus követelményeket megnevezzük, a kvíz kulcsát nem; az M3 A/B sarka törölve (nincs saját pedagógiai funkciója) | értékelési felelős + Memuna |
| Program-teljesítés, eredménycímkék | Online félév teljesítve ÉS Terepgyakorlat teljesítve; „Teljesítve” / „Még nem teljesítve” – minden kapukimenet ugyanezt a címkepárt használja (3. kör) | programvezető + módszertani felelős |
| Időkeretek | bottom-up sávok (lásd HUM-OPS-01) | programvezető |
| Az M2 sorrendje | a manifest a sorrendforrás; az M2.F szövege igazodik | modulgazda |
| Csendes pótlás és F-peula | két külön fogalom; a „felzárkóztató műhely” nem kanonikus név | programvezető |
| Videók hozzáférhetőségi besorolása | egyenként: a beszélőfej képi sávja lehet dekoratív; a jelentést hordozó jelenetvideóhoz hangalámondásos képleírás kell (WCAG 2.2 SC 1.2.5, AA), mellette szöveges alternatíva is (SC 1.2.3) | hozzáférhetőségi felelős + médiafelelős |
| Írásmód | „Nemcsak játék, hanem peula”, „egyválaszos”, „Moodle-ben”, „lépéstérkép” (végrehajtva, a fájlnevekkel együtt) | tananyagfelelős |
| Storming és kortárs bántalmazás | külön tanítjuk; veszélyben lévő gyereknél nincs „normális storming” | Memuna + modulgazda |
| Segélyvonalak | 116-111, 116-000 és 112 leírása a `Gyermekvédelem – release gate.md` §3.3 szerint | Memuna |
| dugma isit, HÉTKÖZNAPOK | egy forma a Glosszárium szerint (az írásmódot a HUM-SOMER-02 projektgazdai döntése rögzíti); az M5 harmadik kategóriájának címkéje HÉTKÖZNAPOK | tananyagfelelős |
| Új kvíztételek | M3: a helyes választ eláruló „jóváhagyott” szó nélkül, valódi tévképzetre épülő disztraktorokkal; M5: transzfer- és szcenárió-tételek; az M0 belépőkvíz hét tétele (köztük a biztonsági tételek) a projektgazda szövegével megírva | értékelési felelős; az M3-nál a Memuna is |

## 9. Projektgazdai döntések – harmadik kör (2026-10-02)

A „Második jóváhagyói kör” oldal 12 maradék kérdésére a projektgazda mind a 12 esetben ezt válaszolta: „Ajánlás szerint.” A döntés tartalma tehát a közzétett ajánlás (szó szerint: `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md`, 3. válasz). A tételek a kapcsolódó HUM-tételek részei, ezért azok lezárt állapota nem változik; a jobb oldali szerep utólagos ellenőrzése vétó / minőségellenőrzés (QA).

| Kérdés | Projektgazdai döntés (2026-10-02) | Kapcsolódó tétel | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| A Memuna átnézése élesítés előtt | élesítés előtti QA-lépés marad a gyermekvédelmi tartalmakra (M3.3, M3.B, M3-kapu, az M7 gyermekvédelmi részei) **[a felsorolás példálózó; a kánoni hatókör a `Gyermekvédelem – release gate.md` §2 — 2026-10-05, 11. szakasz]**: egyszeri, írásos „átnéztem” a release-jegyzőkönyvben; ez a kész anyag ellenőrzése, nem a policy újradöntése | HUM-SAFE-01; RELEASE-READINESS G1 | a Memuna |
| Kötelező F-peula és a javító próbálkozás | éles kapunál (M1, M3, M5, M6, M7) a javító próbálkozás az F-peula után nyílik: a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele; puha kapunál és a Z-nél automatikus marad | HUM-OPS-01 | programvezető + értékelési felelős |
| Hiányzó naptári pontok | **[SUPERSEDED: a naptári dátumokat a 11. szakasz (2026-10-05, pilot-ütemezés) felülírja]** kurzus-hozzáférés 2026-11-02; F-peula a megerősítés utáni hétfőn 18:00-tól, javító határidő a rákövetkező szerda 18:00; az M3 helyzetleírás határideje 2027-01-04 18:00; az M6/M7 javítás a Z utáni hétre csúszhat, a programteljesítés bevárja (activity manifest §7) | HUM-OPS-01 | programvezető |
| Kiskorú fotó/videó/hang hozzájárulása | 18 év alatt a résztvevő és a gondviselő együtt adja | HUM-PRIV-02 | DPO |
| Három megőrzési sor | mentori fejlesztési jegyzet = a mentori 1:1 meta-napló sora (utolsó mentorálás + 6 hónap); név nélküli papír munkalap: összesítés, majd 30 napon belül megsemmisítés; a Z.4 beadandó = szabad szöveges reflexió (képzés vége + 90 nap) | HUM-PRIV-01 | DPO |
| Moodle-on kívüli adatfolyamok | hanih-visszajelzés név nélkül, papíron vagy szervezeti űrlapon, 90 nap; terepi megfigyelési jegyzet = a mentori jegyzet sora; incidens programmutatóként csak összesített darabszám, azonosító nélkül | HUM-PRIV-01 | DPO |
| Az M2.1 identitás-kör kérdése | a válasz nem kerül tárolásra: önellenőrző, nem rögzített elem (H5P-próbálkozás rögzítése kikapcsolva) | HUM-PRIV-01 | DPO |
| Az AI az M7.1-ben | az M7.1 mini AI-blokkja elé háromsoros „Mielőtt használod” doboz, mutatóval az M7.2 AI-jártassági blokkjára | HUM-PRIV-04 | DPO/jogi felelős + programvezető |
| Kipróbálási vállalás kitalált kvucánál | kitalált profilnál a vállalás a terepgyakorlat első alkalmára szól | – | modulgazda |
| Kapueredmény-címkék | egy címkepár mindenhol: „Teljesítve” / „Még nem teljesítve” | – | értékelési felelős |
| Terepgyakorlati rubrika | mind a hat alkalom számít; a KPI programmutató; egyéni feltétel a biztonságkritikus sorok ≥ 1-e; biztonságkritikus: a „biztonság és határtartás” sor; a soronkénti szintleírásokat a módszertani felelős írja meg | HUM-GOV-01 | módszertani felelős |
| Az M3.A 4.3 blokk | a közös átbeszélés 3–4 helyett 3 kártyával fut | – | modulgazda |

## 10. Projektgazdai döntések – release-modell és médiafázisok (2026-10-04)

A 2026-10-04-i döntések átvezetése a kánoni döntési helyre. Szó szerint: a Q-REL-1…4 és a Q-MED-1
`01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – összesítő 24 kérdése.md`, az RM-D1…D6
`01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – release-modell.md`, a BS-D1…D6 és a BS-D8
`01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – BSPEC-01…04 maradék.md`, a BSPEC-02 leltár D-1…D-6 döntése
`01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – BSPEC-02 leltár D-1…D-3.md` (BS-D7 azonosító nincs: a Moodle
4.5–5.2 kutatási tartomány, nem döntés; a pontos célverzió a célkörnyezetből származó G3-bizonyíték). A modell részletei:
`01 Fejlesztés/04 Audit/2026-10-04 Release-modell v2 – Moodle build és learner release.md`. A tételek release-kaput nem
zárnak; a jobb oldali szerep utólagos ellenőrzése vétó / minőségellenőrzés (QA).

| Téma | Projektgazdai döntés (2026-10-04) | Forrás | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| Két verdikt | `MOODLE-BUILD-VERDICT`: `NOT_READY` / `READY_FOR_STAGING_BUILD`. `LEARNER-RELEASE-VERDICT`: `NO-GO` / `CONTENT_READY / MEDIA_PENDING` / `READY_FOR_CONTROLLED_PILOT`. Csupasz `READY` állapot nincs. A régi `RELEASE-VERDICT` egy release-ciklusig kompatibilitási alias. A korábbi döntésekben (pl. az 5. szakasz 2026-10-02-i médiadöntése) a `READY` a `READY_FOR_CONTROLLED_PILOT`-ot jelenti. | RM-D3 | programvezető |
| A build-readiness alapelve | A Moodle-build readiness-t soha nem blokkolja olyan bizonyíték, amely csak a build vagy a runtime során keletkezhet (`BUILD_OUTPUT`, `RUNTIME_OUTPUT`, runtime a11y-teszt, végső Memuna/DPO/a11y QA, program-transzfer, go-live sign-off). A buildet meghatározó specnek viszont késznek kell lennie: implementálható activity-definíciók, célkörnyezeti paraméterek, buildet érintő safeguarding-, privacy- és a11y-szabályok, és minden release-kötelező médiához asset vagy elfogadott fallback. | RM, 1. pont | programvezető |
| Életciklus | `INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`. A kontrollált pilot az első valódi tanulói release. A `GENERAL_RELEASE` életciklus-fázis, nem repo-verdikt: a pilot-findingok javítása, újratesztelése és a go/no-go döntés után. A 6 valós terepi peula + mentori ciklus nem learner-release kapu, hanem release utáni programvalidáció. | Q-REL-1; RM-D1; RM-D3 | programvezető |
| Bukott éles kapu után | Nincs pufferhét. A következő modul tanulási része megnyílhat, de a következő éles kapu lezárása és minden, a hiányzó kompetenciára épülő magas tétű előrehaladás blokkolt marad. Az F-peula a megerősítés utáni hétfőn, a javító határidő szerda 18:00. | Q-REL-2 | programvezető + értékelési felelős |
| Döntési és QA-lánc | A `LEZÁRVA` állapot felbontandó. Kötelező release-lánc: `OWNER_DECIDED → IMPLEMENTED → RUNTIME_VERIFIED → FINAL_RELEASE_QA → RELEASE_APPROVED`; mellette `PROPOSED`, `SUPERSEDED`, `REOPENED`. Az `OWNER_DECIDED` nem release-ready állapot. Két QA-fogalom: a `SPEC_QA` korai vétó vagy tanácsadó ellenőrzés, nem build-kapu; a `FINAL_RELEASE_QA` a kész, runtime-ellenőrzött rendszer szakértői ellenőrzése, release-kapu: ide tartozik a Memuna végső átnézése, a DPO release-ellenőrzése és a független a11y pre-flight. Amíg a fejlécek nincsenek átállítva, a `LEZÁRVA` az `OWNER_DECIDED`-nak felel meg. | Q-REL-3; RM-D2 | programvezető |
| Kezdési idő | A kanonikus kezdési idő péntek 18:00, Europe/Budapest. | Q-REL-4 | programvezető |
| Média-MVP fázisai | A fázis, release-kötelező: tanulói szöveg, natív H5P, szükséges segédlet, pedagógiai diagram/grafika és minden szükséges alt- vagy szöveges ekvivalens. B fázis: csak pedagógiailag indokolt narráció, mindig a szükséges leirattal/felirattal. C fázis: videó, avatar, karakterjelenet, márkás polish csak bizonyított tanulási funkcióval; a C fázis jogfüggő eleménél A/B-s statikus vagy szöveges fallback. Nem a 415 asset vagy a 903 deliverable teljes legyártása a release-feltétel. A manifeszt `release_phase: A/B/C` mezőt kap, és az lesz a scope-freeze. A médiakapu asset-szintű, fallbackkel. | Q-MED-1; RM-D4 | médiafelelős + programvezető |
| LMS-M5-07 (késleltetett felidézés) | Elsődleges út a „Restriction by relative date” plugin (a site admin telepíti); ha nincs telepítve, a pont az M5-03 után látható, és a lecke kéri a 72 órás várakozást. A build nem vár a pluginra. | RM-D6 | LMS-gazda / site admin |
| A kapu-checkpoint tartalékútja (BSPEC-01) | A Group-alapú tartalékút elvetve, nem nyitott implementációs opció. A HUM-PRIV-01 nem változik meg azért, hogy egy tartalékút működjön: a tanulók nem láthatják egymás kapuállapotát vagy csoporttagságát. Ha nincs biztonságos tartalékút, és a primary `GATE_CONFIRMED` út core Moodle, determinisztikus, a kutatási tartományban támogatott, pontosan specifikált és runtime-teszttel igazolható, a „nincs tartalékút” elfogadható eredmény, de bizonyítani és dokumentálni kell. Alternatív tartalékutat csak azért nem gyártunk, hogy legyen. | BS-D1 | DPO/jogi felelős (a HUM-PRIV-01 utólagos ellenőrzője) |
| A Q-REL-2 értelmezése | Nem új döntés. Bukott kapu után a következő modul első tanulási leckéje megnyílhat; a sikeres kapueredményhez kötött downstream activity a siker előtt nem nyílhat meg. A „downstream feloldás előtt” szövegezést minden érintett helyen egyértelművé kell tenni. | BS-D2 | programvezető + értékelési felelős (a Q-REL-2 szerint) |
| Bukott M7-kapu | Az `LMS-M7-08` állapota „Még nem teljesítve”. Ez nem pass és nem M7-teljesítés. A Q-REL-2 szerinti következő tanulási rész megnyílhat, de a végleges program- és kurzusteljesítés blokkolva marad, amíg az M7 javítása sikeresen le nem zárul. | BS-D3 | programvezető + értékelési felelős (a Q-REL-2 szerint) |
| „Nem üres” ≠ „minimálisan értelmezhető” | A pusztán nem üres válasz nem bizonyítja a Program terv §5 szerinti „minimálisan értelmezhető tartalmat”. Mezőnként kell vizsgálni, mi kényszeríthető ki strukturálisan Moodle-ban; ahol ez nem automatizálható megbízhatóan, ott automatikus szemantikai validációt nem állítunk, hanem jelöljük a szükséges emberi ellenőrzést, különösen a Z.3 biztonsági lépésénél. | BS-D4 | — (a döntési jegyzőkönyv nem nevez meg utólagos ellenőrzőt) |
| Az M0 belépőkvíz 4. iteme | A D) disztraktort javítani kell, mert a Q-REL-2 után részben igaz; a helyes válasz és az answer key nem változik, csak a hibás disztraktor szövege, olyanra, amely a Q-REL-2 mellett is egyértelműen téves. | BS-D5 | értékelési felelős (az M0 belépőkvíz utólagos ellenőrzője) |
| Az LMS-Z-06 megőrzése | Maradjon DPO-döntés; a repository nem találgatja, hogy a megőrzés 90 nap („Szabad szöveges reflexió”) vagy 12 hónap („Assignment / peulatervek”). | BS-D6 | — (nyitott DPO-döntés; gazdája a DPO) |
| A Z.3 biztonsági lépésének teljesítése | A beküldés és a tartalmi elfogadás külön. A beküldés kötelező, a technikai input privacy-safe és fájlmentes; a nem üres válasz nem jelenti a „minimálisan értelmezhető tartalom” teljesülését. A beküldés után a tanuló továbbhaladhat: a mentori átnézés nem blokkolja az azonnali downstream tanulási tartalmat. Külön mentor által átnézett / elfogadott állapot van, ez a végső modul- és kurzusteljesítés feltétele; el nem fogadásnál korrekció és újraellenőrzés kell. Automatikus szemantikai validációt nem találunk ki. A Memuna gyermekvédelmi vétójoga megmarad. | BS-D8 | Memuna (gyermekvédelmi vétó, a döntés szövege szerint) |
| Az M1.3 5. diája (BSPEC-02 leltár) | Az 5. dia vezetett S/B/I-mondata nem önálló completion-feltétel és nem tárolandó tanulói produktum (`REQUIRED_BUT_LEARNER_LOCAL`), külön manifest-sort nem kap. A 6. dia saját mini-SBI-je kötelező és tárolt: LMS-M1-07, három mezővel (S, B, I). | D-1 | DPO/jogi felelős (a privacy-megoldásra) |
| A Z.1 SLIDE 5 (BSPEC-02 leltár) | „Az én félévem fénypontjai” kötelező pedagógiai gyakorlat, de tanuló-lokális: nincs mentor által látható tárolt válasz és nincs új TEXT-C sor, a lecke completionje nem a reflexió tartalmának eltárolásától függ. A tanuló saját jegyzetet használhat; a szükséges záró produktumot a Z.4-ben adja be. | D-2 | DPO/jogi felelős (a privacy-megoldásra) |
| A Z.2 SLIDE 5–7 (BSPEC-02 leltár) | A „Saját tanulási pillanatom”, a „Nehéz modul / ellenállás” és a háromszavas check kötelező pedagógiai reflexió, de tanuló-lokális: nem tároljuk név szerinti szabad szöveges válaszként, nincs új TEXT-C sor, a lecke completionje a lecke elvégzésére épül. A Z.4 marad a formális, tárolt záró reflektív produktum, nem gyengül. | D-3 | DPO/jogi felelős (a privacy-megoldásra) |
| Vázlat- és önreflexiós mezők (BSPEC-02 leltár) | Az M0.1 SLIDE 6, az M0.2 SLIDE 6, az M5.2 SLIDE 9, az M5.4 SLIDE 4–5 és az M7.4 SLIDE 3 kötelező tanulási lépése `REQUIRED_BUT_LEARNER_LOCAL`: nem tárolt, nem completion-feltétel, nincs TEXT-C sor. A tárolt változatot az LMS-M5-05 (M5.2, M5.4), illetve az LMS-M7-05 és az LMS-M7-10 (M7.4) gyűjti; az M0.1 és az M0.2 mezőjéhez tárolási cél nincs megnevezve. | D-4 | DPO/jogi felelős (a privacy-megoldásra) |
| Az M6 gyakorló szöveges válaszai (BSPEC-02 leltár) | Az M6.1–M6.4 gyakorló szöveges válaszai (kockázat-válaszok, nyitott és kerülendő kérdések, „mit tanít” és variáció, az M6.4 záró kvuca-vázlata) `REQUIRED_BUT_LEARNER_LOCAL`. A Program terv §4 zárójeles felsorolása a választós itemekre szűkül, az akadálymentesítési minimum változatlan. | D-5 | DPO/jogi felelős (a privacy-megoldásra) |
| Az M0.3 segítségkérő mezője és az M5.1 opcionális mezője (BSPEC-02 leltár) | Az M0.3 SLIDE 7 segítségkérése opcionális, tanuló-lokális lépés: nem tároljuk, a tanuló a „Segítség és kapcsolatok” csatornára viszi (HUM-OPS-02). Az M5.1 opcionális mezője ugyanígy tanuló-lokális, sor nélkül. | D-6; H-6 | DPO/jogi felelős (a privacy-megoldásra) |

## 11. Projektgazdai döntések – pilot-ütemezés, build-blocker leltár, completion és M3.3 (2026-10-05)

A 2026-10-05-i döntések átvezetése a kánoni döntési helyre. Szó szerint: a pilot-ütemezés, a PILOT-1…PILOT-4 és a
scope-korrekció `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – pilot-ütemezés és M0+M1 freeze.md`, a D-a…D-d
`01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, a D-e…D-j, az M33-IMPL-6, a
SAFE-1, a SAFE-4 és a SAFE-7 kezelése `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – MAN completion és
mentor-láthatóság D-e…D-j.md` (1., 4., 5., 6., 7., 7.1. és 7.2. szakasz). A pilot-ütemezés **felülírja** a HUM-OPS-01
2026-10-02-i naptári értékeit (fent, HUM-OPS-01; 9. szakasz, „Hiányzó naptári pontok”); a 2026-10-02-i audit trail
történeti rekord marad. A tételek release-kaput nem zárnak; ahol a jobb oldali oszlop szerepet nevez, annak utólagos
ellenőrzése vétó / minőségellenőrzés (QA).

**Státusz-szemantika** (a pilot-ütemezési jegyzőkönyv 5. szakasza, 3. pont): egy projektgazdai döntés lezárt lehet,
miközben a hozzá tartozó későbbi QA- vagy bizonyíték-kapu nyitva marad. Egy datált döntés-szakasz ezért önmagában nem
jelenti, hogy a benne álló minden QA- vagy bizonyíték-sor lezárt: a SAFE-7 sora nyitott QA-tétel (`Gyermekvédelem –
release gate.md` §6), nem lezárt döntés.

| Téma | Projektgazdai döntés (2026-10-05) | Forrás | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| Pilot-ütemezés | A korábbi 2026-11-02 / 2026-11-06 indulási naptár elavult. Authoring/build: 2026-10-06; az első valódi cohort (az első, kontrollált tesztkurzus / pilot) indulása: 2026-10-10; 2026 októberében a cohort az M0 és az M1 modullal foglalkozik. A régi konkrét november–márciusi dátumok superseded; a későbbi dátumokat nem találjuk ki: `SCHEDULE_TO_RESYNC`, programvezetői új ütemezés szükséges. | pilot-ütemezés | — (a döntési jegyzőkönyv nem nevez meg utólagos ellenőrzőt) |
| A pilot hatóköre és GO/NO-GO | A 2026-10-10-i controlled pilot hatóköre első körben M0+M1. A teljes kurzus gépi `LEARNER-RELEASE-VERDICT`-je maradhat `NO-GO` az M2–Z nyitott tételei miatt; ezt nem értelmezzük át, és nem állítjuk, hogy a teljes kurzus READY. A pilot GO/NO-GO külön, explicit M0+M1 evidence list alapján kerül rögzítésre. A release-report tool nem kap modul-scope támogatást. | PILOT-1 | — |
| Ismeretlen dátumok | Nem ismert még: az M0.A pontos dátuma/időpontja; az M1 konkrét kapu-beadás, megerősítés, F-peula és javító dátumai; az M2–Z új dátumai. Hiányuk nem blokkolja az M0+M1 authoring freeze-t. A build-specben `SCHEDULE_TO_RESYNC`; tanulói nézetben placeholder nem jelenhet meg; amely Moodle activity konkrét ismeretlen dátumtól függ, felépíthető, de valódi tanulónak nem nyitható meg, amíg a dátum nincs konfigurálva. Az LMS-M0-03 elve változatlan: „M0.A után nyílik dátummal”; az M0.A dátuma nem következtethető a 2026-10-10-i cohort-startból; M1 kapu-dátumot sem találunk ki. | PILOT-2 | — |
| „Segítség és kapcsolatok” | A technikai support és a tanulási/programkontakt konkrét elérhetősége még nincs megadva: ez Anna 2026-10-06-i authoringját nem blokkolja, a learner-facing pilot release-t viszont blokkolja, amíg a tényleges csatornák nincsenek kitöltve. A blokk szerkezete négy szereppel specifikálandó: technikai segítség, tanulási/programkontakt, assigned mentor, Memuna / safeguarding; a Memuna/safeguarding adatai a meglévő kánoni adatok. Technikai vagy programkontaktot nem találunk ki; belső build-jelölő stagingben megengedett, learner-facing nézetben nem. | PILOT-3 | — |
| M0/M1 média | Az M0+M1 controlled pilot nem függ videó vagy narráció elkészültétől: a videó/karaktervideó, a narráció és a díszítő illusztráció opcionális; az információhordozó vizuálhoz strukturált HTML/szöveges fallback tartozik; a tanulási célnak média nélkül is teljesülnie kell; elkészült és jogilag/technikailag használható média később hozzáadható (a `Média-assetek/RELEASE-MEDIA-STATUS.md` M0/M1 besorolása szerint). | PILOT-4 | — |
| A 2026-10-05-i lezárási scope | M0 és M1 az első prioritás, mert 2026-10-06-tól Moodle-authoringhoz kell a stabil forrás; 2026-10-05 végéig viszont a teljes M0–Z repó/spec hardeninget le kell zárni, amennyire repóban, runtime nélkül determinisztikusan lezárható. M2–Z repo-fixable vagy build-spec munka nem kerül `POST-PILOT` státuszba; post-build / release-evidence / final-QA állapotban csak az maradhat, ami Moodle runtime-ot, renderelt felületet, cmid-et vagy még meg nem adott emberi jóváhagyást igényel. A cél: `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`; a `LEARNER-RELEASE-VERDICT` maradhat `NO-GO`, amíg a runtime és a final-QA bizonyítékok nincsenek meg. | scope-korrekció | — |
| A 38 checklist-tétel besorolása | A 2026-10-05-i build-blocker leltár besorolása elfogadva; build-tétel: PR-01, PR-02, A11Y-07, A11Y-17; a többi a leltár szerinti human-qa / signoff / runtime / environment / post-build / learner-release kategóriában marad. | D-a | — |
| BSPEC-05 és BSPEC-06 | Regisztrálandó: BSPEC-05 — Branching Scenario completion/fallback; BSPEC-06 — a standard Moodle H5P activity completion-profilja. | D-b | — |
| A média-manifest sémája | A `release_phase` / `fallback` / `fallback_final` sémamunka a `fix/moodle-build-hardening` ágon készül, ugyanannak a build-hardening körnek a részeként. | D-c | — |
| Az M7.4 SLIDE 4 fókuszválasztása | A nem pontozott fókuszválasztás nem önálló completion-elem: pedagógiai interakció marad, de a válasz megléte önmagában nem gate-eli a lecke completionjét, és nem igényel külön Moodle completion-szabályt. | D-d | — |
| Az M6.4 szcenárió-lánca | Az M6.4 egyetlen Branching Scenario activity marad; a három kötelező szcenárió fix sorrendben A → B → D, a C opcionális bónuszgyakorlás. Flow: START → A → B → választópont: „Kihagyom a plusz helyzetet” → D → FINAL, vagy „Megnézek még egy plusz helyzetet” → C → D → FINAL. Az A, a B és a D kihagyhatatlan; a FINAL csak a D után érhető el; a C nem completion-követelmény, és kihagyása nem blokkolhat; minden szcenárión belüli módszerválasztási ág a következő determinisztikus pontra konvergál; a B kapu-item kapcsolata és a D biztonsági tartalma minden tanulónak kötelező. Külön Moodle activity, stáb-checkpoint vagy kerülő tartalékút kizárva; a „legalább 3 külön szcenárió” követelmény nem gyengíthető. A „legalább 3, a negyedik opcionális” tanulói szöveg a fix flow-hoz igazítandó úgy, hogy ne sugallja: a módszerválasztásban egyetlen helyes válasz van. | D-e (a jegyzőkönyv 1., 4. és 5. szakasza; az 5. szakasz a 4. szakasz topológiáját felülírja) | — |
| BSPEC-07 | Jóváhagyva. Hatókör: azok a Moodle Assignment-alapú utak, ahol a beadás és a mentori/stáb-megerősítés két külön, Moodle-ban kódolandó állapot, és a manifest nem specifikálja a megerősítő checkpointot. | D-f | — |
| A BS-D1 alkalmazása a BSPEC-05-re | Az LMS-M2-04, LMS-M3-03, LMS-M5-02 és LMS-M6-04 sorra a BS-D1 szerinti „nincs független tartalékút” megoldás jóváhagyva, ha a soronkénti pontozott Branching Scenario + Moodle „Receive a grade” elsődleges út determinisztikusan teljesíti a lecke completion-szemantikáját. A sorok spec-szinten `BUILD_SPEC_RESOLVED`-ra zárhatók, ha a determinisztikus build-konfiguráció teljesen rögzítve van; a célverziós runtime-bizonyíték külön staging/release evidence gate, a hiánya önmagában nem tartja nyitva a sort. Ha az előírt negatív runtime-teszt a célverzión elbukik, az érintett mechanizmus ismét build blocker (a BSPEC-05 újranyitása vagy regisztrált regresszió/build defect). Group-, kézi vagy más kerülő tartalékút nincs; a pedagógiai/completion-követelmény nem gyengíthető. Az M3.3-nál a teljes, mind a négy szcenáriót lefedő flow-t külön ellenőrizni kell. A SAFE-1 strukturális változása miatt az LMS-M3-03 BSPEC-05-része újranyitottnak tekintendő addig, amíg a passz-csomóponttérkép és a completion-szemantika nincs determinisztikusan rögzítve; ugyanabban a BSPEC-05 fixkörben visszazárható. | D-g (a jegyzőkönyv 1. és 4. szakasz; az LMS-M3-03-ra: 7. szakasza: (a) változat) | — |
| Az Assignment kétállapotú mintája (BSPEC-07) | `SUBMITTED`: a Moodle Assignment beadási completionje; azt a downstream activityt nyithatja, amelyhez a kánon szerint pusztán a leadás szükséges. `CONFIRMED`: külön stáb-checkpoint; azt a downstream / magas tétű / completion-állapotot vezérli, amelyhez mentori/stáb-megerősítés szükséges. A két állapot nem mosható össze; a soronkénti unlock a kánonból vezetendő le, nem feltételezhető, hogy minden Assignment ugyanazt nyitja. | D-h | — |
| További pontozatlan választók | A D-d elve kiterjed: az M0.3 SLIDE 7 és az M2.2 értékválasztása nem önálló completion-elem; pedagógiai/reflektív interakció lehet, de a választás önmagában nem gate-elheti a Moodle lecke-completiont. | D-i | — |
| Az M2.3 pillér-ág tárolása | A pillér-ág választásának tanulói fiókhoz kötött tartós tárolása nem pedagógiai követelmény, és nem kívánt adat; a completion az ág identitását nem használja; jelentésben és manifestben nem állítjuk, hogy a konkrét pillér-választás megőrzése szükséges. Ha a core H5P attempt tracking technikailag mégis felhasználónként eltárolja, annak adatvédelmi elfogadhatósága DPO/jogi QA marad; feltételezéssel nem oldható meg. | D-j | DPO/jogi felelős (a tárolás adatvédelmi elfogadhatóságára, a döntés szövege szerint) |
| Az M3.3 S1-K1 C) ága (M33-IMPL-6) | Új tanulói áthidaló mondat nem kerül a C ág után; a meglévő gyermekvédelmi szöveg változatlan, csak a flow-csomópont kapcsolata változhat. | M33-IMPL-6 döntés (a jegyzőkönyv 6. szakasza) | — |
| Passz, szünet és completion az M3.3-ban | A HUM-SAFE-03 passzolási joga kötelező, és elsőbbséget élvez az M3.3 „mind a négy szcenáriót végigviszi” megfogalmazásával szemben; a passz nem a D-g által tiltott tartalékút, hanem ugyanazon elsődleges Branching Scenario tanulóbiztonsági útvonala. Minden érzékeny szcenárió előtt elérhető a „Passzolom ezt a helyzetet” út, indoklás nélkül; passz esetén a szcenárió tartalma kihagyható, és a flow a következő szcenárióra/checkpointra megy. Completion-szemantika: S1 (completed OR passed) AND S2 (completed OR passed) AND S3 (completed OR passed) AND S4 (completed OR passed) → post-scenario tartalom → FINAL; Moodle completion csak az egyetlen FINAL/grade-emissionnél. A tanuló bármikor szünetet tarthat vagy kiléphet; a félbehagyott M3.3 nem complete, büntetés nincs; visszatéréskor a célverzió ténylegesen támogatott resume-viselkedése érvényes, megbízható resume hiányában a tanuló újraindíthatja az activityt, és használhatja a passz-utakat (stagingben tesztelendő). Egyenértékű alternatíva a HUM-SAFE-03 szerint továbbra is kérhető; ez nem technikai completion-tartalékút, külön Moodle-kapu nem kell hozzá, új érzékeny alternatív tanulói tartalom most nem készül; ha a program/Memuna külön pedagógiai alternatívát kér, az külön tartalmi QA-t kap. Az M3.3 második személyű döntési keretezése fikciós „helper-role case analysis”, nem szerepjáték: a tanuló nem játszik sértettet vagy elkövetőt, saját történetet nem kell felidéznie vagy megosztania, a szituáció fikciós, a feladat a madrih következő lépésének elemzése. | SAFE-1 (a jegyzőkönyv 7. szakasza) | a Memuna és a DPO (release-QA/vétó, a döntés szövege szerint) |
| Az M3.3 pass-choice csomópontja és pontozása | Minden S1–S4 szcenárió előtt ugyanaz a pass-choice csomópont: kérdés „Mit szeretnél tenni ezzel a helyzettel?”, opciók „Végigmegyek ezen a helyzeten” és „Passzolom ezt a helyzetet”; indoklás, megerősítő kérdés és „biztos vagy benne?” modal nincs; egyik opció sem preferált vizuálisan vagy nyelvileg. A passzolt szcenárió utáni biztonsági csomópont az útvonalon marad (pl. S1 PASS → S1 SAFETY NODE → S2 PASS-CHOICE), S1–S4-re egységesen: választ nem kér, nem pontozott, személyes reflexiót nem kér, a passzolt narratívát nem ismétli, kizárólag a meglévő safety-box tartalmat használja. A két opció pontozási hatása azonos: egyik választása sem növelheti vagy csökkentheti a tanuló grade-jét a másikhoz képest; a scenario-válaszok helyessége nem mastery-gate; a csupa ❌-es és a csupa passzolt út egyaránt eléri a FINAL-t, és ott nem üres Moodle-grade keletkezik; a lecke nem válhat tanulónak látható teljesítménypontszámmá. Ha ezek együtt a célverzión nem teljesíthetők, a megvalósítás megáll. | SAFE-1 (a jegyzőkönyv 7.1. és 7.2. szakasza) | a Memuna (QA/vétó a kész staging activityre, a döntés szövege szerint) |
| Az M3.3 S1-K1 C) ágának iránya | Az S1-K1 C válasza a meglévő visszajelzés után közvetlenül az S1-K2-re megy; új áthidaló mondat nincs, visszavezetés az S1-K1-re nincs; a tanulónak nem kell addig újraválasztania, amíg „helyes” választ nem ad; a csupa ❌-es út eléri a FINAL-t és nem üres grade-et; a narratív átmenet fennmaradó QA-kockázata a Memuna átnézésének része. | SAFE-4 (a jegyzőkönyv 7. szakasza) | a Memuna (a narratív átmenet QA-ja, a döntés szövege szerint) |
| Az M3.3 S1 csatornája (SAFE-7) — nyitott | Nem projektgazdai döntéssel zárul. A jelenlegi answer key a staging buildben változatlan; a Memuna release előtt explicit QA-zza, hogy a 23:15-ös bejövő privát üzenet és a ✅ első válasz megfelel-e a HUM-SAFE-02-nek. Addig a ✅ nem változik, és a SAFE-7 nem jelölhető megoldottnak; learner release előtt kötelező lezárni, a Moodle staging buildet önmagában nem blokkolja. | SAFE-7 (a jegyzőkönyv 7. szakasza) | a Memuna (HUM-SAFE-02) |
| Az A11Y-15 és az A11Y-18 besorolása | A D-a besorolása marad mérvadó: RELEASE-EVIDENCE. A 2026-10-05-i scope-korrekció időzítési és hatóköri szabály volt, nem taxonómiai változás. Ha valamelyik tételnek statikus, repóban javítható előfeltétele van, azt még aznap be kell fejezni; a runtime/renderelt bizonyíték RELEASE-EVIDENCE marad. A két tétel ezért release-evidence jelölést kap, nem BUILD-et, és nem marad besorolatlan. | pilot-ütemezés, 5. szakasz 1. pont | — |
| A pilot hétköznapja | A 2026-10-10 (szombat) a pilot hiteles első tanulói/kurzusnapja. A régi pénteki alkalmakra épülő feltevések erre a pilotra nem érvényesek automatikusan, és ahol ütköznek, felülírtak. A tanulói kurzus-hozzáférés dátuma 2026-10-10; hozzáférési időpontot nem találunk ki. Az M0.A pontos dátuma/időpontja és az M1 konkrét kapu-, megerősítési, F-peula- és javító dátumai `SCHEDULE_TO_RESYNC`. | pilot-ütemezés, 5. szakasz 2. pont | — |
| A SAFE-7 és a státusz-szemantika | A SAFE-7 nyitott marad, FINAL_RELEASE_QA / learner-release tétel, a staging buildet nem blokkolja; nyitott QA-tételként szerepel a `Gyermekvédelem – release gate.md` §6-ban. Egy projektgazdai döntés lezárt lehet, miközben a későbbi QA-/bizonyíték-kapuja nyitva marad; egy datált döntés-szakasz ezért önmagában nem jelenti, hogy a benne álló minden QA-/bizonyíték-sor lezárt. A SAFE-7 nem jelölhető megoldottnak. | pilot-ütemezés, 5. szakasz 3. pont | — |
| A Memuna-átnézés hatóköre | A 9. szakasz 2026-10-02-i felsorolása („A Memuna átnézése élesítés előtt”) példálózó, nem kimerítő. A kánoni hatókör a `Gyermekvédelem – release gate.md` §2 tágabb megfogalmazása (az R-11 szerint átvezetve). A történeti szöveg marad, a hatóköre jelöléssel pontosítva. | pilot-ütemezés, 5. szakasz 4. pont | — |
| Az M3.4 → M4 mondat | Nem új szabályozási döntés: a meglévő Q-REL-2 / BSPEC-04 az irányadó. Az a tanulói mondat, amely szerint az M4 csak a megerősített sikeres teljesítés után nyílik meg, hibás, ha megerősített bukás után blokkolja az M4 tanulási részét. Az M3.4 a kánoni megkülönböztetéshez igazítandó: a következő tanulási rész a megerősített eredmény után nyílhat, „Még nem teljesítve” esetén is; csak a sikerhez kötött downstream/kapus elemek maradnak zárva. | pilot-ütemezés, 5. szakasz 5. pont | — |
| Az A11Y-07 iframe-címe (G5a/G5b) | Az A11Y-07 a G5a/G5b modell szerint kettéválik. G5a (build, repó- és spec-szint): minden tanulói Moodle H5P-iframe-nek beszédes magyar `title` attribútuma van, amelynek értéke a kanonikus H5P-/activity-cím; Moodle core fájl nem módosul; a megvalósítás karbantartott, theme-szintű JS/AMD-kiegészítés, renderer- vagy kontextusbővítés, illetve egyenértékű, karbantartott local/plugin megoldás lehet; Mustache-felülírás csak akkor elfogadható, ha a megvalósítás a címet a sablon kontextusába is átadja; a pontos megvalósítást a cél-Moodle-környezetben kell igazolni; ha egyik mechanizmus sem telepíthető, TARGET-ENVIRONMENT blokkolót kell rögzíteni, és a követelmény nem gyengül. A követelmény rögzítésével a G5a repó- és spec-része lezárható. G5b (post-build): a renderelt DOM-nak és a képernyőolvasó bejelentésének kell igazolnia; ez nem jelölhető `RUNTIME_VERIFIED`-nek, amíg nem fut. Ez nem felmentés a hozzáférhetőségi követelmény alól, és nem állítja, hogy a core Moodle teljesíti. | `01 Fejlesztés/04 Audit/2026-10-05 Fix pack – Command 6 – PR-01, PR-02, A11Y-07, A11Y-17 és konzisztencia.md`, 0. szakasz (második és harmadik üzenet) | — (a döntés nem nevez meg utólagos ellenőrzőt) |
| Az RT-P0-15 mentor-láthatósági tesztfeltételei | Projektgazdai megvalósítási döntés: a TEXT-C mentor-láthatósági mechanizmusát (`Adatvédelem – tanulói adatok és AI.md` §3, „Activity-szintű adatleltár – build-rész”) az RT-P0-15 stagingtesztje legalább két mentorral és két elkülönített tanulói csoporttal igazolja: az A mentor csak az A csoport válaszait látja; a B mentor csak a B csoport válaszait látja; egyik mentor sem jut közvetlen URL-lel más csoport tanulójának válaszához; a tanuló nem látja más tanuló válaszát. A feltételek jelentése azonos a D-a…D-d jegyzőkönyv 1. szakaszának 2. pontjával. A mechanizmus csak a mentor szerepkört szűkíti; a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés DPO-kérdés marad (BIZT-2). A teszt futtatása post-build bizonyíték (G2): ez a sor runtime-igazolást nem állít. | `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont és 2. szakasz; `01 Fejlesztés/04 Audit/2026-10-05 Fix pack – Command 6 utolsó takarítás (C6U2).md`, 0. szakasz | a DPO (QA) |
