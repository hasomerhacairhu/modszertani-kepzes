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
| **Érintett források** | `Gyermekvédelem – release gate.md`, M0.2, M0.4, M0.A, M1.A, M2.A, M2.4, M2-kapu, M3.3, M3.B, M3-kapu, M4.2, M4.3, M4.A, M4.B, M5.2, M6.2, M6.3, M6.4, M6.A, M6.B, M6-kapu, M7.2, M7.3, M7.4, M7.B, M7-kapu, Z.3, Z.A |
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

**Projektgazdai döntés (2026-10-02)**: a „Segítség és kapcsolatok” blokk négy, szerep szerinti kontaktot ad: technikai segítség, tanulási/programkontakt, a kijelölt mentor, és ettől külön a Memuna (gyermekvédelem). Nincs „mentor / felelős / vezető” típusú lánc. **[SUPERSEDED (csak a kapacitás-mondat): a következő bekezdés kemény 1:8-as plafonja; az 1:10 tartalék kikerült]** Mentor:madrih kapacitás: javasolt kiinduló plafon 1:8, legfeljebb 1:10.

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

A 2026-10-04-i döntések átvezetése a kánoni döntési helyre. Szó szerint: a Q-REL-1…4, a Q-MED-1, a Q-MED-2 és a Q-PED-4
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
| Narrációk besorolása (animáció hangsávja vagy önálló dia-narráció) | **Besorolás:** `M1.1-NAR-03` = animáció hangsávja; `M1.2-NAR-02` = animáció hangsávja; `M1.2-NAR-03` = storyboard/animáció hangsávja; `M3.1-NAR-02` = animált Tuckman-ábra hangsávja. Ezekhez **felirat + leirat** kell. `M4.1-NAR-02` a jelenlegi spec alapján **önálló slide-narráció**, nincs időzítési/szinkron-kontraktusa az animált DIA-01-gyel, ezért VO D-19 szerint mellette látható leirat kell. Ha később ténylegesen az animációhoz szinkronizáljuk, akkor átkerül a hangsáv kategóriába. | Q-MED-2 | hozzáférhetőségi felelős |
| Az M3.1 „szemüveg, nem menetrend” mondata | **Igen.** Kerüljön be: „**A modell szemüveg, nem menetrend: egy valódi csoport visszaléphet, átugorhat szakaszt, és egy helyzet többféleképpen is olvasható.**” | Q-PED-4 | módszertani felelős |
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

## 12. Projektgazdai döntés – az M1.1 SLIDE 5 önreflexiója (N-M1-04, 2026-10-10)

A 2026-10-10-i döntés átvezetése a kánoni döntési helyre. Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md` (1. és 2. szakasz). A
kánoni átvezetést a projektgazda P0 adatvédelmi freeze-kivételként hagyta jóvá. A státusz-szemantika a 11. szakasz
szerinti: a döntés lezárt, a hozzá tartozó runtime-bizonyíték és DPO QA nyitott bizonyíték-kapu.

| Téma | Projektgazdai döntés (2026-10-10) | Forrás | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| Az M1.1 SLIDE 5 személyes önreflexiója | Opcionális, kizárólag tanuló-lokális, nem tárolódhat Moodle/H5P oldalon, és nem lehet completion-feltétel. Alapértelmezés: saját jegyzetben vagy fejben végiggondolt reflexió; nem szükséges szöveget beküldeni vagy megosztani. Interaktív beviteli elem kizárólag igazoltan adatmentes runtime-működéssel engedélyezett; a próbálkozás-riport, a mentett állapot és a tanári/mentori hozzáférés vizsgálata kötelező. Átvezetve: M1.1 3. szakasz (runtime-követelmény és SLIDE 5); `LMS – activity manifest.md` LMS-M1-01 és BSPEC-02; `LMS – H5P runtime acceptance.md` 24. pont. | N-M1-04 (a jegyzőkönyv 1. és 2. szakasza) | a DPO (QA, a döntés szövege szerint) |
| Az N-M1-04 bizonyíték-kapuja — nyitott | Nem projektgazdai döntéssel zárul. A DPO jóváhagyása és a Moodle runtime-ellenőrzése (RT-P0-24 az LMS-M1-01-re: próbálkozás-riport, mentett állapot, tanári és mentori hozzáférés) nyitott bizonyíték-kapu (`RELEASE-READINESS.md` G2, G3b). Amíg az RT-P0-24 nem igazol adatmentes beviteli elemet, a SLIDE 5 beviteli elem nélkül, a saját jegyzetes úton nyílik meg. | N-M1-04 (a jegyzőkönyv 1. és 2. szakasza) | a DPO |

## 13. Projektgazdai döntések – az M0.1 SLIDE 5 kérdésének finomítása (CC-04) és a Moodle-összevetés (CC-06) (2026-10-10)

A 2026-10-10-i döntések átvezetése a kánoni döntési helyre. Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md`
(1. szakasz, 2. és 3. pont). A státusz-szemantika a 11. szakasz szerinti.

| Téma | Projektgazdai döntés (2026-10-10) | Forrás | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| Az M0.1 SLIDE 5 kérdésének finomítása (kíváncsiság ↔ félelem) | „CC-04: POST-PILOT. Az M0+M1 freeze maradjon érvényben. Az M0.1 kérdésének finomítását a pilot visszajelzéseivel együtt kezeljük. Freeze-kivételt csak tényleges P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy a tanulói előrehaladást blokkoló hiba indokolhat.” | CC-04 (a jegyzőkönyv 1. szakasza, 2. pont) | — (a döntési jegyzőkönyv nem nevez meg utólagos ellenőrzőt) |
| A Moodle-ben felépített tartalom és a repó-forrás összevetése | „a Moodle összevetését most ne kezeld blokkolóként. A Moodle MCP a jóváhagyott, aktuális GitHub-forrásból fogja felépíteni a képzést. A pontos SHA, az implementált szöveg és a tényleges működés ellenőrzését külön build/runtime feladatként kezeljük. A média hiánya önmagában nem bizonyít elavult tartalmat.” | CC-06 (a jegyzőkönyv 1. szakasza, 3. pont) | — (a döntési jegyzőkönyv nem nevez meg utólagos ellenőrzőt) |

## 14. Projektgazdai döntések – a next-version döntési csomag 125 döntése (2026-10-12)

A 2026-10-12-i döntés átvezetése a kánoni döntési helyre. Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md`
(a projektgazda szó szerinti elfogadása) és az elfogadott dokumentum,
`01 Fejlesztés/04 Audit/2026-10-12 Döntési javaslat – M0–Z 125 döntés, kutatással megalapozva.md`. A kérdések:
`01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`. A státusz-szemantika
a 11. szakasz szerinti.

- **Lezárt döntés:** az alábbi táblázat mind a 125 sora. A döntés szövege szó szerint a javaslat azonos azonosítójú sora; eltérés csak kettő, jelentésváltozás nélkül: a modulazonosító előtti névelő javítása „az”-ra az ERT-7, ERT-20, ERT-23, ERT-35 és LMS-6 sorában, valamint a TECH-1 sorában a gépi gyermekvédelmi őr által tiltott egybeírt alak helyett körülírás (a szó szerinti eredeti az elfogadott dokumentumban áll).
  - `A` = alapjavaslat.
  - `F` = feltételes javaslat. A sorban megnevezett feltétel a döntés része: amíg nem teljesül, a sorban megnevezett óvatos alapértelmezés érvényes.
- **Vétó/QA:** a jobb oldali oszlop a döntési csomagban bejegyzésenként megnevezett szerepeket adja; ellenőrzésük utólagos vétó/QA. Vétónál az érintett sor `REOPENED`.
- **Eltérés a csomag ajánlásától:** ahol a javaslat eltér a döntési csomag ajánlásától (a javaslat „Lényeges eltérések” szakasza: TECH-1, LMS-6, GYV-4/GYV-14, ERT-40, ADV-11), a javaslat érvényes.
- **PRG-17:** a döntés a CC-04 szerinti halasztás (13. szakasz).
- **Amit a szakasz nem zár le:**
  - a táblázat alatti 16 bizonyíték- és aláírás-bejegyzést: ezek a `RELEASE-READINESS.md` G1–G8 kapuinak nyitott bizonyíték-kapui;
  - a futó pilotot: a `main@213a4c5` és az M0+M1 freeze (CC-04) változatlan;
  - a tananyag átírását: ez külön, engedélyezett javítási körben történik.
- **Release:** a szakasz nem release-jóváhagyás.

| Azonosító | Projektgazdai döntés (2026-10-12; szó szerint a javaslatból) | Forrás | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| GYV-1 | `F` — Az LMS-M2-09 szabad reflexiót ne kezeljük folyamatosan figyelt gyermekvédelmi bejelentőcsatornaként, és töröljük a garantálhatatlan „mentorod azonnal bevonja” ígéretet. Az LMS-M2-05 kapubeadványon csak akkor maradjon határidős átnézés, ha tényleges szolgálati rend, értesítés, helyettesítés és SLA bizonyított; egyébként ott is világos, külön akut jelzési út legyen. Memuna + DPO ellenőrzése kell. | javaslat GYV-1; kérdés: döntési csomag GYV-1 | Memuna (HUM-SAFE-01); vétó/QA: DPO / jogi felelős. |
| GYV-2 | `F` — Érzékeny krízis-/önfeltárási gyakorlatnál biztosítsunk valódi passzt és nem személyes, fiktív alternatívát; a teljesítés nem függhet önfeltárástól. Ha a feladat biztonsági kompetenciát mér, a passzhoz ekvivalens tudásdemonstráció járjon, ne automatikus kapuátengedés. M2.4 kötelező mezője így biztosan módosítandó; M3/M4-es kör Memuna- és completion-QA. | javaslat GYV-2; kérdés: döntési csomag GYV-2 | Memuna + programvezető (HUM-SAFE-03); kapus belépő: értékelési felelős; MAN:57 és az M3.3 §7.1: projektgazda (build-spec gazda), QA: Memuna. |
| GYV-3 | `F` — Terjesszük ki a SAFE-7 helyenkénti felülvizsgálatát valamennyi 1:1-es kockázati helyzetre, a kritikus itemek kulcsának érintetlenül hagyásával. A 7 helyre külön Memuna-verdict szükséges; addig az egyéni privát kapcsolattartást ne tanítsuk automatikus helyes eljárásként. | javaslat GYV-3; kérdés: döntési csomag GYV-3 | Memuna (HUM-SAFE-02); az ITEM 4 kulcsa: projektgazda. |
| GYV-4 | `F` — Egységes, szerepnév-alapú krízisút legyen a veszélyt bemutató dobozokban: kijelölt Memuna/helyettes, tényleges elérhetőség; közvetlen veszélyben 112, érzelmi támogatásra 116 111. FONTOS: a 116 000 elsődlegesen az eltűnt gyermekek forróvonala, nem általános segélyhívó; a tananyagban szolgáltatás és címzett szerint pontosítani kell, és a Memuna kiadáskor ellenőrizze a számokat és az órákat. | javaslat GYV-4; kérdés: döntési csomag GYV-4 | Memuna (HUM-SAFE-01; vétó/QA: a Memuna és a helyettese). |
| GYV-5 | `F` — Érzékeny, potenciálisan felkavaró peulán előzetesen legyen legalább két rendelkezésre álló, felkészített 18+ felelős, vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben; felkavart kiskorú nem maradhat egyedül. Végleges létszámnorma a Memuna és programvezető hatásköre. | javaslat GYV-5; kérdés: döntési csomag GYV-5 | Memuna + programvezető (HUM-SAFE-03; GK §5:120). |
| GYV-6 | `A` — A meglévő GK §4:63–64 védelmi minimum szerepeljen röviden minden releváns peula képzői instrukciójában; a Z.A-nál előbb nyugodt meghallgatás és biztonság, gyermekvédelmi jelzés esetén azonnal Memuna. A szereplési szorongás nem automatikusan gyermekvédelmi krízis, de legyen szabad megállni és passzolni; a Memuna hagyja jóvá a küszöböt. | javaslat GYV-6; kérdés: döntési csomag GYV-6 | Memuna + programvezető (HUM-SAFE-03). |
| GYV-7 | `F` — Kétlépcsős küszöb: zaklatás, feltárás, önsértés vagy más veszélyeztetettség gyanújánál azonnali Memuna-jelzés; pusztán nem veszélyeztető nehéz érzelemnél támogató mentorálás, választási lehetőséggel. A csoportchatbántalmazás M0-specifikus küszöbét a Memuna külön ellenőrizze; a kvízkulcs nem módosul vélelmezésből. | javaslat GYV-7; kérdés: döntési csomag GYV-7 | Memuna (HUM-SAFE-01/03); az M5-nél a programvezetővel. |
| GYV-8 | `F` — Terepi veszélynél a helyszíni 18+ felelős cselekszik azonnal, és a szervezeti Memuna-jelzés külön megtörténik; ez nem két alternatív, egymást helyettesítő címzett. Pusztán hiányzó felnőtt felügyelet operatív ügyét a képző/programvezető rendezi, akut kockázatnál Memuna is. Jóváhagyás: Memuna + programvezető. | javaslat GYV-8; kérdés: döntési csomag GYV-8 | Memuna + programvezető. |
| GYV-9 | `F` — Az M7 blokkoló R4-rubrika minimumába és a mintatáblába kerüljön a felelős 18+ felnőtt megnevezése, de csak a rubrikahorgony és a már tanított Q9/(C) szabály összehangolt, formális jóváhagyásával; a hallgató nem bukhat előzetesen nem közölt követelményen. | javaslat GYV-9; kérdés: döntési csomag GYV-9 | Memuna + értékelési felelős; rubrikaszint: projektgazda. |
| GYV-10 | `F` — Tanulók, különösen kiskorúak számára ne nyissunk szabad beszélgetéses AI-segédet addig, amíg nincs igazolt adatkezelési és kríziskezelési út. Ideiglenes alap: AI-segéd kikapcsolva, no-AI út teljes értékű. Később előre meghatározott krízisválasz, külön jelzési csatorna és kontrollált, szükséges metaadat lehet; automatikus veszélyszűrés nem helyettesíti az embert. | javaslat GYV-10; kérdés: döntési csomag GYV-10 | Memuna + DPO/jogi felelős + programvezető. |
| GYV-11 | `F` — Tárolt beadandóba kerülő gyermekvédelmi feltárásnál ne legyen az LMS az incidens elsődleges nyilvántartása. Dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás/helyesbítés és adatvédelmileg jóváhagyott törlés/megőrzés kell; a tanuló kapjon biztonságos, feltárásmentes pótlási utat, a kapueredmény ne függjön a feltárástól. Ne töröljünk bizonyítékot automatikusan jogi megőrzési felülvizsgálat nélkül. | javaslat GYV-11; kérdés: döntési csomag GYV-11 | Memuna + DPO; kapueredmény: értékelési felelős; N-9: értékelési felelős + programvezető, Memuna-vétóval. |
| GYV-12 | `A` — M1-ben a szabad szöveghez az ADV §11 már elfogadott, adattakarékos mondata kerüljön az önfeltárást sugalló egyedi felszólítás helyére; M2-ben a meglévő biztonsági blokk legyen közvetlenül elérhető az érintett mezőnél. Ne hozzunk létre új, önkéntelen disclosure-ra ösztönző képeslap-szöveget; Memuna QA. | javaslat GYV-12; kérdés: döntési csomag GYV-12 | Memuna (a HUM-SAFE-03 szerint a programvezetővel). |
| GYV-13 | `A` — Az érzékeny, valódi helyzeteknél a meglévő rövid „azonnal vond be a Memunát” formula egységesen szerepeljen; a személyes reflexiós feladatoknál ne sugalljunk kötelező jelentést a puszta érzelmi megosztás miatt. A Memuna erősítse meg a konkrét helyeket és a poszterek rövid változatát. | javaslat GYV-13; kérdés: döntési csomag GYV-13 | Memuna; az M3.1-nél a modulgazdával (HUM:470). |
| GYV-14 | `F` — Kiadás előtt a Kék Vonal és az NMHH aktuális szolgáltatásleírása alapján javítsuk a hívószámok célcsoportját: 116 111 gyermek- és ifjúsági lelkisegély, 116 000 eltűnt gyermekek vonala; 112 közvetlen veszély. Ha a kánon félrevezető, a Memuna formálisan nyissa újra a konkrét tájékoztató sort; ne változtassunk telefonszámot igazolás nélkül. | javaslat GYV-14; kérdés: döntési csomag GYV-14 | Memuna (vétó a HUM:471 soron). |
| GYV-15 | `F` — A semleges „a Memuna és – ahol indokolt – a hivatalos szervek feladata” megfogalmazást ajánlom az önsértési eseteknél; a tanuló nem nyomoz, nem konfrontál. Hogy mely szerveknek, mikor kell külső jelzés, azt a jogász/JOG-1 és a Memuna határozza meg. | javaslat GYV-15; kérdés: döntési csomag GYV-15 | Memuna; jogi kérdésben jogi szakértő (lásd X-15). |
| GYV-16 | `F` — Kirekesztést nem demonstrálunk valódi kirekesztett/kirekesztő szerep kiosztásával; fiktív harmadik személyű esetelemzés és választásos feldolgozás legyen az alap. Az M3.A csoportszobor csak önkéntes, nem megbélyegző, passzolható formában maradjon, explicit debrief-fel. Memuna szakmai döntés. | javaslat GYV-16; kérdés: döntési csomag GYV-16 | Memuna; az M3.A-nál az M3 modulgazdájával. |
| GYV-17 | `A` — Az M6.A tiltott zónái legyenek rövid, kötelezően kimondott biztonsági keretek a gyakorlat előtt; a kiskorúakra, identitásra, kirekesztésre és önfeltárásra is térjen ki. Ne kerüljenek olyan állítások a kapukvízbe, amelyeket az élő peulán opcionálisan hall a résztvevő. | javaslat GYV-17; kérdés: döntési csomag GYV-17 | Memuna + a peula tartalomfelelőse. |
| GYV-18 | `F` — A 12. item „friss seb” provokatív keretezése helyett fiktív, szereplőközpontú kérdés és biztonságos válasz legyen; a „nálatok” önfeltáró kérdés opcionális és passzolható. A megváltozott disztraktor/✅ szöveg értékelési felelős + Memuna jóváhagyását igényli. | javaslat GYV-18; kérdés: döntési csomag GYV-18 | Memuna + értékelési felelős; kulcs: projektgazda. |
| GYV-19 | `A` — Mind az M2.A, mind az M4.3 gyakorlat-instrukciója kapjon egy rövid, kánoni határmondatot: aggasztó feltárásnál meghallgatni lehet, részleteket kikérdezni/nyomozni nem; a képzőnek és a Memunának a kijelölt úton jelezni kell. | javaslat GYV-19; kérdés: döntési csomag GYV-19 | Memuna. |
| GYV-20 | `F` — A zsidósághoz, családi viszonyhoz és személyes különbözőséghez kötődő identitás-vonal ne követeljen nyilvános kiállást. Privát, papíros vagy fejben végzett út, passz és nem érzékeny közös reflexió legyen a default; Memuna/DPO review után lehet az önkéntes nyilvános változatot mérlegelni. | javaslat GYV-20; kérdés: döntési csomag GYV-20 | Memuna + DPO. |
| GYV-21 | `A` — A „név nélkül” nem egyenlő anonim jelleggel egy kis kvucában. Gyermekvédelmi és érzékeny példából csak fiktív, illetve ténylegesen nem visszaazonosítható, általánosított változatot kérjünk szóban is. Valós esetet sem szóban, sem beadandóban nem tehetünk alapkövetelménnyé. | javaslat GYV-21; kérdés: döntési csomag GYV-21 | Memuna + DPO. |
| GYV-22 | `A` — Az M1.1 önfeltárásához kerüljön az M1.A mintájára világos határmondat: a személyes történet megosztása nem elvárás és nem feltétele a jó madrihságnak; lehet általános/fiktív példát választani. Memuna és lektor ellenőrizze. | javaslat GYV-22; kérdés: döntési csomag GYV-22 | Memuna + szakmai lektor. |
| GYV-23 | `F` — Első körben csoportszintű, nem megbélyegző korrekciót és a biztonsági 1–2. item nyilvános visszajelzését ajánlom. Egyéni mentoros utánkövetés csak indokolt pedagógiai cél, célhoz kötött válaszhozzáférés és DPO-jóváhagyás mellett; a kvíz diagnosztikus marad. | javaslat GYV-23; kérdés: döntési csomag GYV-23 | programvezető + Memuna; adatkör: DPO. |
| ADV-1 | `F` — Vegyes (c) hozzáférési modell: mentor csak saját csoportjának lássa a beadást; admin/editor jogosultság szűk, név szerint kiosztott, auditálható, de technikai admin teljes hozzáférését ne tagadja a tájékoztató. A „csak mentorod látja” ígéretet a tényleges RBAC-hoz kell igazítani a staging role-matrix után. | javaslat ADV-1; kérdés: döntési csomag ADV-1 | DPO / jogi felelős (a HUM-PRIV-01 „Jóváhagyó” sora szerint); a szerepkiosztást az LMS-gazda rögzíti. |
| ADV-2 | `F` — Alapértelmezés: kijelölt értékelő olvas, második/fellebbezési értékelő csak konkrét eljárásnál, Memuna szükség esetén, F-peula képzője csak aggregált vagy minimális hiánylistát lát. Az F-peula szereposztást és a vészhozzáférést dokumentálni kell; csoport-hozzáférés ténylegesen tesztelendő. | javaslat ADV-2; kérdés: döntési csomag ADV-2 | DPO / jogi felelős az LMS-gazdával; az F-peulák beosztásáról a programvezető; a Memuna szerepéről a Memuna. |
| ADV-3 | `F` — Alapértelmezés az N-M1-04 mintája: opcionális reflexió saját jegyzetben, beviteli elem és completion nélkül. Az M4 már tárolt TEXT-C-ként deklarált helyein csak formális completion-/build-spec döntéssel lehet adatmentesre átállni; ha pedagógiai bizonyíték nélkül tárolt marad, a tanulói ígéret legyen igaz és a DPO írja alá az adatkört. | javaslat ADV-3; kérdés: döntési csomag ADV-3 | projektgazda (pedagógiai szükség, completion, build-spec); vétó: DPO / jogi felelős (HUM-PRIV-01). Az ILO 2 átírása: lásd X-10; a kötelező/opcionális besorolás: lásd X-6. |
| ADV-4 | `F` — Érzelmi önjelzést, passzt és véleményt ne pontozzunk, és lehetőleg ne rögzítsük a követett H5P próbálkozásban. M1.1-ben a szöveg + Tovább út az alap; M3 SAFE-1 ágnál a konkrét H5P verzió, próbálkozás-riport, xAPI/LRS, mentett állapot és szerepkörök visszaolvasása után dönthető el a tárolásmentes technika. | javaslat ADV-4; kérdés: döntési csomag ADV-4 | DPO / jogi felelős; az M3-tételeknél a Memuna is. A completion-rész: lásd X-6 (M0:ERT-3). |
| ADV-5 | `F` — Különleges vagy érzékeny világnézeti információként kezeljük azt a névhez köthető válaszmintát, amely vallási/ideológiai meggyőződésre következtetni enged. Ne legyen kötelező azonosítható vallási önbesorolás; engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül. GDPR 9. cikk szerinti minősítés és kivétel csak jogi/DPO jóváhagyással. | javaslat ADV-5; kérdés: döntési csomag ADV-5 | DPO / jogi felelős; someres vonatkozásban a projektgazda (QA: helyi ideológiai felelős, HUM-SOMER-01). |
| ADV-6 | `F` — A FORUM-C bemutatkozó fórum maradjon valódi tanulóknak zárva, amíg nincs dokumentált cél, hozzáférési kör, DPO által elfogadott megőrzési idő és életkornak megfelelő tájékoztató. A „képzés vége + 90 nap” nem automatikus jogszerű alapérték. Addig szóbeli/nem rögzített bemutatkozás a biztonságos alternatíva. | javaslat ADV-6; kérdés: döntési csomag ADV-6 | DPO / jogi felelős; a tájékoztató szövegének freeze-kivételét a projektgazda. |
| ADV-7 | `A` — Közös papírszabály: személyes önfeltáró cetli a résztvevőnél marad vagy hozzá visszakerül; névvel nem függesztjük ki és nem gyűjtjük, fotózás alapból nincs. Szükséges csoportproduktum fotója csak előre rögzített céllal, hozzáféréssel, tájékoztatással és HUM-PRIV-02 szerinti engedéllyel; saját telefon ne legyen kötelező. | javaslat ADV-7; kérdés: döntési csomag ADV-7 | DPO / jogi felelős; az M5-nél a modulgazdával. |
| ADV-8 | `F` — Visszaazonosítható kis csoportos produktumot ne minősítsünk anonimnak. Elsődlegesen visszaadás, szóbeli összegzés vagy ténylegesen deidentifikált csoportos aggregálás; ha a mentor személyhez kapcsolja a feljegyzést, azt személyes adatként a megfelelő mentori adatkörhöz kell sorolni. Ne találjunk ki univerzális „anonim X fő fölött” küszöböt. | javaslat ADV-8; kérdés: döntési csomag ADV-8 | DPO / jogi felelős és értékelési felelős. |
| ADV-9 | `A` — A Peula v2 minimális csoportszintű kvuca-adatszabályát alkalmazzuk az M4/M5/M6 produktumokra is: korosztály, hozzávetőleges létszám, általános energia/hangulat igen; név, diagnózis, konkrét azonosítható eset nem. Kis csoportban az egyedi élethelyzet is visszaazonosítható lehet, ezért DPO QA. | javaslat ADV-9; kérdés: döntési csomag ADV-9 | DPO és programvezető (a HUM :461 QA-szerepei). |
| ADV-10 | `F` — Moodle és papír legyen az alap. Külső Google-sablon csak szervezeti fiókkal, adatfeldolgozói és hozzáférési felülvizsgálattal; nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladat. A szolgáltató, adatkör, megőrzés és harmadik fél tényleges ismeretéig ne engedjük az opcionális külső eszközt. | javaslat ADV-10; kérdés: döntési csomag ADV-10 | DPO / jogi felelős és programvezető (a fiók kérdésében); az M7-nél az LMS-gazdával; a GK §4.2-t érintő részben a Memuna. |
| ADV-11 | `F` — Egységes közös eszköz-protokoll: jelszómentés és személyes munkapéldány tilos; kijelentkezés, munkamenet-ellenőrzés, letöltési törlés és adatmentes papír/saját eszköz alternatíva. Kivételt csak LMS-biztonsági és DPO teszt után, szükséges esetben engedjünk. | javaslat ADV-11; kérdés: döntési csomag ADV-11 | LMS-gazda és DPO. |
| ADV-12 | `F` — Az AI-végponton a tartalom naplózása legyen kikapcsolva alapból; csak feltétlenül szükséges technikai metaadat, rövid, dokumentált megőrzéssel. Előbb mérjük fel a provider-, proxy-, hibalog-, backup- és admincsatornákat; ha nem garantálható az adatkizárás, a közvetlen tanulói AI-hozzáférés maradjon inaktív. „store=false” önmagában nem bizonyít teljes naplózásmentességet. | javaslat ADV-12; kérdés: döntési csomag ADV-12 | DPO / jogi felelős (QA: programvezető, HUM-PRIV-04). |
| ADV-13 | `A` — Az LMS-M2-09 szabad szövegeit ne olvassuk újra pusztán programanalitika miatt. A tanulási folyamatból jogszerűen rendelkezésre álló aggregált mutató használható, különben a „2–3 konkrét szabály” KPI kerüljön ki vagy helyettesítse completion/önértékelési mutató; nem keletkezik új monitoringcél. | javaslat ADV-13; kérdés: döntési csomag ADV-13 | DPO; az N-3 miatt a Memunával. |
| ADV-14 | `F` — A Z.4 videóopció legyen alapból kikapcsolva, amíg nincs hozzájárulás- és jogosultsági folyamat, visszavonási/törlési út és feltöltés előtti ellenőrzés. A fő szöveges/beadandós út teljesen egyenértékű. Ha később bevezetjük a videót, a fotóra vonatkozó szigorúbb szabályokat is alkalmazzuk rá; a kiskorú jogalapját jogász/DPO ellenőrzi. | javaslat ADV-14; kérdés: döntési csomag ADV-14 | DPO és jogi felelős. |
| ADV-15 | `A` — Z.4 Feedback: „Show analysis page” = No, „Enable notification of submissions” = No. A résztvevő ne lássa a kis kohorsz válaszmintáját, automatikus e-mailben ne terjesszünk válaszokat. Külön vizsgáljuk az anonim mód és az adminisztratív back-end hozzáférés tényleges működését. | javaslat ADV-15; kérdés: döntési csomag ADV-15 | DPO és programvezető (HUM-PRIV-03). |
| JOG-1 | `F` — Ideiglenes szervezeti rend: madrih azonnal a kijelölt Memunának/helyettesnek jelez; a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne. A Gyvt. 17. § konkrét címzettjeit/időhatárait jogász ellenőrizze; a Btk. 209/A. § nem valamennyi jelzéskésés általános büntetőszabálya, hanem a Gyvt. 17. § (4a)–(4c) szerinti speciális kötelezettségekhez kötődik. Ne állítsunk általános három munkanapos büntetőjogi határidőt jogi vélemény nélkül. | javaslat JOG-1; kérdés: döntési csomag JOG-1 | jogi szakértő; jóváhagyás: Memuna (GK §5); a nyilvántartás helyéről a projektgazda. |
| TERM-1 | `F` — A „dugma isit” fogalom példamutató magatartást jelölő alakja legyen következetes („dugma isitként viselkedik / példát mutat”), ne antropomorf címke („dugma isit vagy”). Az átnevezés a csatolt fájlokra és jóváhagyott kvíztörzsekre is kihat, ezért a helyi mozgalmi terminológiagazda megerősítése kell. | javaslat TERM-1; kérdés: döntési csomag TERM-1 | projektgazda; QA: ken-vezető / mozgalmi felelős. |
| TERM-2 | `A` — Az SBI S elemének kánoni magyar neve „helyzet”, az első előfordulásnál elfogadható a „szituáció” szinonima. A rubrikacím is ehhez igazodjon úgy, hogy az értékelt kompetencia és a pontozás ne változzon. | javaslat TERM-2; kérdés: döntési csomag TERM-2 | M1 modulgazda és értékelési felelős, a Glosszárium gazdájával. |
| TERM-3 | `A` — Az M2.4 két gyermekvédelmi szabálymondatában „transzparens” helyett „átlátható” legyen a szó, a GK szóhasználatával egyezően; tartalmi szabályt nem módosít. | javaslat TERM-3; kérdés: döntési csomag TERM-3 | projektgazda, a Memuna vétójával. |
| TERM-4 | `F` — Az M3.4 tanulói címe legyen természetes magyar („Mit tegyél, mit ne tegyél madrihként?”), míg a belső LMS-azonosító stabil marad; a fájlnév-átnevezés, manifest és hivatkozások együtt, ellenőrzött diffben mozogjanak. A tényleges szerzői cím az M3 modulgazdájának döntése. | javaslat TERM-4; kérdés: döntési csomag TERM-4 | M3 modulgazda; a link-címkénél az értékelési felelős és a Glosszárium gazdája. |
| TERM-5 | `A` — Az LMS-M3-05 tanulói elnevezése legyen következetesen „M3 – Helyzetleírás” (ha indokolt: „red flag és első lépések” alcímmel); ez illeszkedik a gyermekvédelmi kánon helyzetleírás fogalmához, a kód marad változatlan. | javaslat TERM-5; kérdés: döntési csomag TERM-5 | M3 modulgazda / implementációs felelős. |
| TERM-6 | `F` — Ha a 3. kártya a tizenéves kvuca állapotáról szól, „Leviatán – év eleji kvuca” legyen, ne „stáb”; a „stáb” a képzői csapatot jelöli. Csak akkor maradjon a stáb, ha a modulgazda konkrét mozgalmi értelemben igazolja a szándékát. | javaslat TERM-6; kérdés: döntési csomag TERM-6 | M3 modulgazda; someres olvasatnál a helyi ideológiai/mozgalmi felelős. |
| TERM-7 | `F` — M2-ben a személyes ideológiai viszonyulás legyen nem pontozott reflektív cél, ne névhez kötött véleménymérés. Az M5-ben a tanulási elvek saját szavas magyarázatát rövid, formatív demonstrációval lehet ellenőrizni; ha nincs erre idő/hely, a hub célmegfogalmazását szűkítsük. Modulgazdai/értékelői jóváhagyás. | javaslat TERM-7; kérdés: döntési csomag TERM-7 | projektgazda; QA: helyi ideológiai felelős és DPO (M2), értékelési felelős (M5). |
| TERM-8 | `F` — A „someres érték” értékelését a helyi Ideológiai Kézikönyvhez kössük, de ne követeljünk személyes világnézeti vallomást. A rubrika nyitott, leírt kritérium alapján fogadja el az érték és hangulat közti különbséget; a top 3-ban hiányzó someres értékre előre rögzített támogatás legyen, ne utólagos, önkényes bukás. Helyi ideológiai és értékelési QA. | javaslat TERM-8; kérdés: döntési csomag TERM-8 | projektgazda, értékelési felelős, helyi ideológiai felelős; az ERT-G3-1 (b)-nél a modulgazda. |
| ERT-1 | `A` — A H5P Course Presentation completionje a kánoni BSPEC-06 szerint az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését. Csak olyan CP kapjon erre épülő completiont, amelynek valóban van összefoglaló diája; az üres/kihagyott interakciós negatív teszt kötelező. | javaslat ERT-1; kérdés: döntési csomag ERT-1 | projektgazda (build-spec gazda); QA: értékelési felelős. |
| ERT-2 | `A` — A pontozatlan vélemény- és önjelző választó általánosan ne legyen önálló completion-elem, és ne legyen hamis „hibás” visszajelzése. A leckéket a megtekintés/összefoglaló vagy más legitim aktivitás teljesítse; M0.1-nél ezt kifejezetten rögzítsük, nehogy a completion feltétel nélkül megszűnjön. | javaslat ERT-2; kérdés: döntési csomag ERT-2 | projektgazda; QA: értékelési felelős. |
| ERT-3 | `F` — Diagnosztikus M5 QUIZ-D: a beküldés ténye elegendő completionhez, tartalmi bukás nélkül. Kötelező Z.4 Feedback: legalább egy nem érzékeny, értelmezhető Required válasz, a személyes kérdéseknél passz és egyenértékű alternatíva. A „kiürítés” valós működését stagingben tesztelni kell. | javaslat ERT-3; kérdés: döntési csomag ERT-3 | projektgazda (QUIZ-D, build-spec); értékelési felelős (Z.4); vétó/QA: DPO + programvezető (Z.4). |
| ERT-4 | `F` — Csak a tananyagban ténylegesen megígért formatív kvíz legyen külön Moodle-activity és manifest-sor; szerzői itempoolhoz ne hozzunk létre új tárolt aktivitást pusztán azért, mert a kánon „itembank”-nak nevezi. Az M1 nyitott szöveges itemjei maradjanak szerzői pool, az M2 zárt formatív gyakorló csak akkor activity, ha a tanulói út követeli és DPO által elfogadott. | javaslat ERT-4; kérdés: döntési csomag ERT-4 | projektgazda + értékelési felelős; DPO, ha activity. |
| ERT-5 | `A` — Éles kapun első próbálkozás után pontszám és a hibázott kompetencia/kritikus követelmény látszódjon, de ne jelenjen meg a helyes kulcs és a teljes opció-visszajelzés a javító lezárása előtt. Az M3/M7 kritikus itemekhez a mentor szabályosan adjon javítási útmutatást; az eltérő Moodle Review options-t célverzión vissza kell olvasni. | javaslat ERT-5; kérdés: döntési csomag ERT-5 | értékelési felelős; kritikus slotnál és a kulcs megjelenítésénél a Memuna is (M3). |
| ERT-6 | `A` — Diagnosztikus jelzéshez az első, visszajelzés előtti próbálkozás a mérvadó; a későbbi próbálkozások gyakorlásra szolgálnak, nem írják felül a korai szükségletet. M5-ben 3 próbálkozást javaslok (2 helyett is elérhető gyakorlás), M6-ban maradjon a jelenlegi korlátlan formatív út. A gradebook és az analitika e két szerepét el kell választani. | javaslat ERT-6; kérdés: döntési csomag ERT-6 | értékelési felelős + projektgazda (M5); a beállítást az LMS-gazda rögzíti. |
| ERT-7 | `A` — A valódi tévképzetre épülő, kulcsot nem eláruló disztraktor-követelményt az M5/M6 kánonban már előírt item-bankokra és a gyermekvédelmi leckeitemekre terjesszük ki; minden alacsony tétű ellenőrző kötelező újraírását nem indokolja bizonyíték. | javaslat ERT-7; kérdés: döntési csomag ERT-7 | értékelési felelős; gyermekvédelmi itemeknél a Memuna is. |
| ERT-8 | `A` — Puha kapunál a gyenge, de értelmezhető munka formatív F-peula-javaslatot váltson ki, ne „nem teljesült” bukást. A „Még nem teljesítve” státusz az üres/értelmezhetetlen beadásé marad; a rubrika szerinti fejlődési cél külön, nem kapuzó jelzés. Az értékelés helyét és hozzáférését dokumentálni kell. | javaslat ERT-8; kérdés: döntési csomag ERT-8 | projektgazda; QA: értékelési felelős, programvezető; az adatkörről DPO. |
| ERT-9 | `A` — ASSIGN-M saját completion = SUBMITTED (beküldte); a tényleges szakmai CONFIRMED állapot külön GATE-CP-n álljon be. Egy „Receive a passing grade” kipipálása az Assignmenten nem helyettesíti a kritikus rubrikasorok és a mentor-konfirmáció összetett feltételeit. A korábbi pontküszöb nem változik. | javaslat ERT-9; kérdés: döntési csomag ERT-9 | projektgazda / build-spec gazda. |
| ERT-10 | `F` — Az M3 kritikus itemsor módosításához egyszerre kell írásos projektgazdai kapudöntés és Memuna-jóváhagyás; az értékelési felelős kalibrál. Az ITEM 10-et addig ne emeljük kritikusnak, amíg nincs küszöbhatás-vizsgálat és Memuna szakmai állásfoglalás; megmaradhat fontos, de nem automatikusan blokkoló lefedettségi tételként. | javaslat ERT-10; kérdés: döntési csomag ERT-10 | projektgazda + Memuna; QA: értékelési felelős. |
| ERT-11 | `A` — A belépőkvíz nyilvánvaló nyelvi hibái („completion-állapot”, alanyegyeztetés) javíthatók a kérdések helyességének és a ✅ elhelyezésének változtatása nélkül; értékelési QA a SIG-1 körében. | javaslat ERT-11; kérdés: döntési csomag ERT-11 | projektgazda; QA: értékelési felelős. |
| ERT-12 | `A` — Tárolt, névhez kötött M1.3 mini-SBI-ben kizárólag fiktív helyzet legyen. Az M1.4-es precedens, a HUM:462 és az adatminimalizálás ezt támogatja; a leckeszöveg, HUB, MAN és érintett NAR-spec egy fix packban igazodik. DPO-vétó és szükséges hanggyártás külön. | javaslat ERT-12; kérdés: döntési csomag ERT-12 | projektgazda; vétó: DPO. |
| ERT-13 | `A` — SBI rövid válaszának kánoni hossza 2–3 mondat legyen a Program terv és a rubrika jelenlegi, többségi mintája alapján. A mondatszám csak instrukció, ne váljon pontozott küszöbbé. | javaslat ERT-13; kérdés: döntési csomag ERT-13 | projektgazda / modulgazda + értékelési felelős. |
| ERT-14 | `A` — Az M1 KAPU tartalmazzon kimondott értékelői szabályt a mintaválasz szó szerinti visszaadására: az adaptációt és helyzetre szabást értékeljük, a bemásolás önmagában nem kompetencia. A kapuval azonos példát cseréljük független, nem kulcsolt mintára, de a rubrikát az értékelési felelősnek kell jóváhagynia. | javaslat ERT-14; kérdés: döntési csomag ERT-14 | értékelési felelős; QA: módszertani lektor. |
| ERT-15 | `F` — Ugyanazért az enyhe minősítő szóért csak egyszer járjon levonás. A viselkedést objektíven leíró B-sor hordozza az adott tartalmi hibát, a hangnem külön csak önállóan igazolt kommunikációs hibánál módosulhat. A két horgony értékelői példáit egységesíteni és kalibrálni kell. | javaslat ERT-15; kérdés: döntési csomag ERT-15 | értékelési felelős + módszertani lektor. |
| ERT-16 | `F` — Az S („helyzet”) jó teljesítésének egyértelmű olvasata: idő VAGY hely (mindkettő lehet) ÉS a helyzet releváns szakasza. Kerüljön zárójelezett, pontozói példákkal megadott szabály a rubrikába; a bizonyítottan eltérő konstruktumválasztást csak az értékelési felelős hagyhatja jóvá. | javaslat ERT-16; kérdés: döntési csomag ERT-16 | értékelési felelős. |
| ERT-17 | `A` — A „megtartható kapcsolatban” zárójel magyarázó cél legyen, ne új, előre nem tanított külön pontozási dimenzió. Az értékelő a viselkedésre, nem a személy minősítésére adott visszajelzést méri, a kapcsolat megőrzése ennek pedagógiai oka. | javaslat ERT-17; kérdés: döntési csomag ERT-17 | értékelési felelős / modulgazda. |
| ERT-18 | `F` — Az M2.4 pontozatlan önbevalló polljai maradjanak követésmentesek; ne generáljanak fantom „grade”-et. A továbblépést külön igazolt, nem érzékeny completion-jelhez vagy a megtekintéshez kell kötni. A (2a) egyszerű út az első választás, ha a manifest lánca megőrzi a tanulási célt; cél-Moodle runtime próba nélkül ez nem kész. | javaslat ERT-18; kérdés: döntési csomag ERT-18 | projektgazda (build-spec gazda); a tárolásról DPO. |
| ERT-19 | `F` — Az M2 identitáskör-módszertanában az „ÉN” a középpont, a „legalább 3 kör” ezért három további rétegként értelmezendő; viszont ez a jelenlegi rubrika szigorítását okozhatja. A módosított követelményt előre kommunikálni és a modulgazda/értékelési felelős által aláíratni kell, meglévő beadást visszamenőleg nem büntetünk. | javaslat ERT-19; kérdés: döntési csomag ERT-19 | értékelési felelős. |
| ERT-20 | `F` — Ha a DPO nem engedélyezi a szabad szöveg rendszeres olvasását, az M2:244 mutató szűnjön meg; ne erőltessük a „2 vagy 3” számot adatkezelési kényszerrel. Ha marad, a programvezető válasszon előre rögzített, legalább 2-es formatív célértéket, és csak jogszerű aggregátumból számoljon. | javaslat ERT-20; kérdés: döntési csomag ERT-20 | modulgazda + értékelési felelős. |
| ERT-21 | `F` — Az M3 R1 fogadjon el a kánoni értelemben releváns biztonsági/határhelyzetet, ne csak erőszakos krízist; R2-t az olyan helyzetekben, ahol nincs feltárás vagy titoktartási ígéret, ne büntető mechanikával alkalmazzuk. A rubrika ne buktassa meg a saját sablonját követő résztvevőt; kalibráció Memuna + értékelési felelős. | javaslat ERT-21; kérdés: döntési csomag ERT-21 | értékelési felelős + Memuna; rubrikaszint: projektgazda. |
| ERT-22 | `A` — Az M3 blokkoló R4 sorban csak gyermekvédelmi eljárási kritérium (nem nyomoz, nem konfrontál, megfelelő jelzés) legyen. Az életszerűség kerüljön egy nem blokkoló minőségi sorba, mert az irreális, de biztonságos válasz nem azonos veszélyes eljárással. | javaslat ERT-22; kérdés: döntési csomag ERT-22 | projektgazda (rubrikaszint); QA: értékelési felelős + Memuna. |
| ERT-23 | `F` — Többértelmű kvuca-jelenetnél dokumentáltan több helyes párosítás legyen elfogadható; egyetlen kulcs csak akkor maradjon, ha a megfigyelhető jelek azt egyértelműen alátámasztják. A módosítást az M3 modulgazda és az értékelési felelős itemenként validálja. | javaslat ERT-23; kérdés: döntési csomag ERT-23 | értékelési felelős + M3 modulgazda. |
| ERT-24 | `F` — M4 Kapu 1 alacsony teljesítményét ne állítsuk be önkényes P/F küszöbként. Addig személyre nem szabott, összesített téma-visszajelzés legyen; ha a programvezető egyéni felzárkóztatási jelzést kíván, előbb rögzített feladatszerkezet, validált értékhatár, hozzáférés és Moodle runtime teszt kell. | javaslat ERT-24; kérdés: döntési csomag ERT-24 | értékelési felelős + projektgazda. |
| ERT-25 | `F` — Az M4.3 K3 kérdésszárát és a kulcsolt opciókat egy szakmai értelmezés körül tegyük egyértelművé; elsőként a kérdésszár pontosítása és a meglévő helyes válasz megtartása preferált. Ha szakmailag másik válasz helyes, a ✅ változása külön explicit lektori és projektgazdai döntés legyen. | javaslat ERT-25; kérdés: döntési csomag ERT-25 | az M4 szerzője / projektgazda; QA: szakmai lektor (HUM-PED-01). |
| ERT-26 | `A` — Az M5 kapu elsődleges pontozási egysége a rubrikakritérium a teljes táblázat alapján, nem minden táblázatcellára külön kötelező mikropont; a PT és HUB ugyanezt írja. Soronként legyen látható módszertani indok, de egy tanulástani eszköz nem feltétlenül kell minden sorba. Értékelési kalibráció. | javaslat ERT-26; kérdés: döntési csomag ERT-26 | értékelési felelős + projektgazda; QA: módszertani lektor. |
| ERT-27 | `A` — Az M5 R4 gyakorlásfogalma maradjon a Glosszárium tágabb, meglévő definícióján; a felidézés és az elosztott gyakorlás fontos példák, de önkényesen ne szűkítsük erre a rubrikát. | javaslat ERT-27; kérdés: döntési csomag ERT-27 | értékelési felelős + módszertani lektor. |
| ERT-28 | `F` — Az M5.2 SLIDE 8 helyes opciója a „feladat–kvuca–módszer–cél” logikát kövesse úgy, hogy a kiválasztás valóban a tanított döntési utat méri. A ✅ pozíció csak akkor maradhat, ha a szemantika ténylegesen helyes; ellenkező esetben explicit új itemdöntés, nem kozmetikai szövegezés. | javaslat ERT-28; kérdés: döntési csomag ERT-28 | M5 szerzője + értékelési felelős. |
| ERT-29 | `A` — Az M5.4 SLIDE 6 „Igaz rám / Még nem” önbevallás ne legyen pontozott helyes–hibás kérdés. Mindkét válasz legitim önellenőrzési állapot, a completion a lecke megtekintésén vagy más semleges eseményen alapuljon. | javaslat ERT-29; kérdés: döntési csomag ERT-29 | értékelési felelős, a projektgazdával. |
| ERT-30 | `F` — Az M5 KAPU Q12 opciói ugyanabból az ágensnézőpontból szóljanak; a ✅ C jelentése változatlan legyen. Elsőként csak a C mondatot igazítanám az egyes szám első személyű kontextushoz, a szakmai szerző/értékelő jóváhagyásával. | javaslat ERT-30; kérdés: döntési csomag ERT-30 | értékelési felelős + modulgazda. |
| ERT-31 | `A` — Az M6 diagnosztikus szcenárió-kvíz beküldése legyen kötelező completion, de az eredmény ne blokkolja az elsődleges éles játéklapkaput. Az önellenőrzés hibáira lehessen újrapróbálni, az „ajánlott 80%” ne váljon át rejtett bukási szabállyá. | javaslat ERT-31; kérdés: döntési csomag ERT-31 | projektgazda; QA: értékelési felelős + programvezető. |
| ERT-32 | `F` — A biztonságkritikus R4 „Oké” horgonya az adott eszköztípus tanított kötelező minimumait kérje (kontaktjátéknál akadálymentes tér, stop-jelzés, tempó, kísérés; szenzitív helyzetnél passz és felnőtt). Ez rubrikaváltozás, ezért ne implementáljuk értékelési/Memuna kalibráció nélkül. | javaslat ERT-32; kérdés: döntési csomag ERT-32 | értékelési felelős; rubrikaszint: projektgazda. |
| ERT-33 | `A` — Az M6.B társas visszajelzése maradjon formatív, pontozás nélküli („ma nem pontozunk”); a végső rubrikával a képző értékel, a stáb egymás között kalibrál. A HUB/PT „társas pontozás” kifejezéseit a tényleges folyamatra pontosítsuk a projektgazda engedélyével. | javaslat ERT-33; kérdés: döntési csomag ERT-33 | értékelési felelős + projektgazda. |
| ERT-34 | `F` — A 2. item tartalmi duplikációja helyére készítsünk azonos nehézségű Kivsza-korú, korosztályi illesztést mérő új itemet, és előzetesen validáljuk; addig a meglévő kvízt ne hirdessük teljes korosztályi lefedettségűnek. Az itemszám és küszöb csak jóváhagyással változhat. | javaslat ERT-34; kérdés: döntési csomag ERT-34 | értékelési felelős. |
| ERT-35 | `A` — Az M6 4. diagnosztikus kvízitem egyedüli helyes elvének legalább minimális változata kerüljön az összes tanuló által garantáltan látott kötelező forrásba. Az opcionális Branching Scenario ág nem lehet az értékelt ismeret egyetlen tanítási helye. | javaslat ERT-35; kérdés: döntési csomag ERT-35 | projektgazda; QA: értékelési felelős. |
| ERT-36 | `F` — Az M6 11–12. tétel azonos gondolkodási elvet más, fiktív helyzeten kérjen számon, ne szó szerinti leckememóriát. A 12. item érzékeny, önfeltárást hívó megfogalmazása csak GYV-18 döntése után javítható; biztonsági veto megtartandó. | javaslat ERT-36; kérdés: döntési csomag ERT-36 | értékelési felelős + Memuna. |
| ERT-37 | `A` — Az M6.B közös páros munka lehet formatív vázlat, de az éles LMS-M6-05 kapun minden résztvevő önállóan véglegesít és nyújt be egyéni játéklapot. A társproduktum önmagában nem bizonyít egyéni kompetenciát. | javaslat ERT-37; kérdés: döntési csomag ERT-37 | értékelési felelős + M6 modulgazda. |
| ERT-38 | `A` — Z.4 „Teljesítve”: a tartalom legyen minimálisan értelmezhető, tényleges beadás, de a három részes ideális reflektív szerkezet legyen formatív útmutató, ne új, rejtett bukási küszöb. Az adatvédelmi szempontból szenzitív részek passzolhatók, a tanulói követelmény előre ismert. | javaslat ERT-38; kérdés: döntési csomag ERT-38 | értékelési felelős; vétó/QA: programvezető. |
| ERT-39 | `A` — Z.A záró peula legyen ajánlott, értékes közösségi esemény, ne a Moodle program completion kötelező feltétele; ezt a PT és MAN jelenlegi kritériumai alátámasztják. Hiányzó jelenlét ne akadályozzon minden egyéb kaput teljesítő tanulót. | javaslat ERT-39; kérdés: döntési csomag ERT-39 | programvezető + értékelési felelős. |
| ERT-40 | `F` — M7 Q11/Q14 Multi-Select: a kapuküszöb darabszám-alapú (legalább 12 teljesen helyes item / 14), ne átszámított részpontszázalék. Ha van validált minden-vagy-semmit Moodle kérdéstípus, használjuk; egyébként manual GATE-CP megerősítés, negatív teszttel 11 teljes + 2 részleges esetére. Ne engedjen át „Grade to pass 12” önmagában. | javaslat ERT-40; kérdés: döntési csomag ERT-40 | értékelési felelős; QA: programvezető; plugin: LMS-gazda (X-11). |
| ERT-41 | `A` — A hiányzó M7 kipróbálási vállalás/AI-megjegyzés esetén kérjünk kitöltési pótlást és értelmezhető, nem értékelői visszajelzést, de ne buktassuk a kaput és ne tiltsuk a szakmai v2 értékelését. Így összeegyeztethető a „figyelembe vesszük” és a „nem blokkol” kánon. | javaslat ERT-41; kérdés: döntési csomag ERT-41 | értékelési felelős; QA: programvezető, az AI-megjegyzésnél a HUM-PRIV-04 vétó/QA-szerepei (DPO/jogi felelős + programvezető). |
| ERT-42 | `F` — Az M7 R8-ban különítsük el az AI-másolat pedagógiai problémáját és a harmadik személy azonosítható adatának biztonsági/adatvédelmi kockázatát. Az utóbbinál a beadás ne legyen automatikusan elfogadott magas összpont mellett sem; legyen DPO-jóváhagyott korlátozás, incidensértékelés, adateltávolítás és javító leadás. Rubrika és kapuhatás formális döntést igényel. | javaslat ERT-42; kérdés: döntési csomag ERT-42 | értékelési felelős + DPO; QA: DPO + programvezető. |
| ERT-43 | `F` — SMART R1 2-es szinten legyen valóban ellenőrizhető jel/kimenet, ne csupán határidő: különben a mérhetőség tanított elemét nem értékeljük. A követelmény értékelési szigorítás, ezért csak előzetes egyértelmű tanulói tájékoztatóval és projektgazdai jóváhagyással léphet hatályba. | javaslat ERT-43; kérdés: döntési csomag ERT-43 | értékelési felelős; QA: módszertani lektor. |
| ERT-44 | `F` — Az M7 R3 egyetlen konstruktuma a peula koherens belső íve legyen; a három fázis a strukturáltság megfigyelhető bizonyítéka, ne külön még egyszer pontozott dimenzió. Ha a szerző két kompetenciát akar mérni, az már külön rubrikafejlesztés és kalibráció. | javaslat ERT-44; kérdés: döntési csomag ERT-44 | értékelési felelős + modulgazda. |
| ERT-45 | `A` — Az M7 Peula v2-re ne találjunk ki univerzális 45 percet: a valódi célcsoport és helyzet szerint tervezett időkeret betarthatóságát pontozzuk; a 45 perc csak példa lehet. A PT-ben szereplő 60–90 perces programkeretekkel így nincs ellentmondás. | javaslat ERT-45; kérdés: döntési csomag ERT-45 | értékelési felelős. |
| ERT-46 | `F` — M7.1 Fill in the Blanks numerikus helyein csak akkor pontozzunk, ha cél- és kontextusfüggően meghatározható, előre publikált elfogadott válaszhalmaz vagy tartomány. Ha a „reális” szabad mérlegelést jelent, legyen pontozatlan, formatív visszajelzéses feladat; semmilyen numerikus varázsküszöböt ne gyártsunk. | javaslat ERT-46; kérdés: döntési csomag ERT-46 | leckegazda + értékelési felelős. |
| ERT-47 | `A` — Az M7 (C) „átláthatóság” kifejezést bontsuk két ellenőrizhető alpontra: ki tud a felügyeletről/kockázatról, és hogyan közlik a helyszín, sötétedés és hazajutás feltételeit a résztvevőkkel/szükséges felelőssel. Csak a már tanított követelmény legyen pontozott; Memuna ellenőrzés. | javaslat ERT-47; kérdés: döntési csomag ERT-47 | értékelési felelős; vétó/QA: Memuna. |
| ERT-48 | `A` — Az M7 AI-jártassági gyakorló kérdése legyen Page-be vagy CP-be ágyazott, lehetőleg nem követett, nem külön pontozott H5P; a kötelező tanulási tartalom megtekintését a befogadó activity completionje jelölje. No-AI azonos teljesítési út; külön H5P gradebook-nyom ne keletkezzen csak a szemléltető gyakorlatért. | javaslat ERT-48; kérdés: döntési csomag ERT-48 | projektgazda (build-spec) + értékelési felelős + LMS-gazda (LMS-rész X-11); QA: a HUM-PRIV-04 szerepei. |
| ERT-49 | `A` — Az M7 (C) kritériumából vegyük ki az „eltérő létszám” olyan elvárását, amely nincs megtanítva, és az M7.3/SLIDE5 itemekben sincs következetesen szerepeltetve. Alternatíva csak új kötelező tanulói tartalommal és jóváhagyott assessment-módosítással; a legkisebb helyes változás a rubrika szűkítése. | javaslat ERT-49; kérdés: döntési csomag ERT-49 | értékelési felelős. |
| ERT-50 | `A` — Az M7 v1 operációs táblájának minimális terjedelme 3 értelmes sor legyen; 4 sor ajánlott, de nem kötelező. A kétértelmű „min. 3–4” helyett egyetlen világos szám szerepeljen az M7.4-ben és a KAPU-ban. | javaslat ERT-50; kérdés: döntési csomag ERT-50 | értékelési felelős + modulgazda. |
| PRG-1 | `A` — Az ütemezett 45 perces peulablokkok és a központi naptár maradjanak; a modulgazdák tételes vágási tervvel csökkentsék a túlcsorduló lépéseket, a védett biztonsági/reflexiós és kötelező feldolgozó lépések rövidítése nélkül. M5.1-nél a 15–20 perc és a 9–13 percre összegződő részidők tényleges újrabecslése vagy a metaszám visszaigazítása kell, nem kitalált „átmeneti” percek. | javaslat PRG-1; kérdés: döntési csomag PRG-1 | az elvet a programvezető (HUM-OPS-01 jóváhagyó és vétó/QA); a vágási tervet az adott modulgazda (M3.B-nél a Memuna bevonásával), vétó/QA: programvezető. |
| PRG-2 | `A` — Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük; ahol nincs ilyen, inkább szűkítsük a hub-ígéretet (C opció, alap A), mint hogy minden hiányra új activityt építsünk. Új tartalom csak tételesen bizonyított nevelési szükség és PRG-4 szerzői jóváhagyás esetén. | javaslat PRG-2; kérdés: döntési csomag PRG-2 | projektgazda (célkitűzés), a modulgazdával; QA: értékelési felelős (`M3:ERT-G2-5`, M6), M6-nál a tartalomfelelős; M3-nál Memuna; M1-nél DPO, ha tárolt. |
| PRG-3 | `A` — A tényleges peulafájlban végrehajtható, időbe férő lépés legyen a részletes igazságforrás; a hub/meta/kártya-spec azzal egyezzen. Ha egy fontos, korábban ígért tanulási cél elveszne, azt a modulgazda kifejezetten PRG-4 fejlesztésre jelölheti, nem automatikus bővítésre. | javaslat PRG-3; kérdés: döntési csomag PRG-3 | a szabályt a programvezető; tételenként az adott modulgazda (az M1-poszternél és az M2-diagramnál a médiafelelőssel), vétó/QA: programvezető. |
| PRG-4 | `F` — Egy összefogott, célzott /course-develop csomag készüljön a kötelező, hiányzó feedback- és akadálymentesítési tartalomra, majd szakaszos szakmai QA. Nem kell egyszerre minden opcionális új játékot megírni. Új biztonsági/értékelési item csak Memuna/értékelési gazda által jóváhagyott tervből; az RA 125 visszajelzési minimumát ne gyengítsük. | javaslat PRG-4; kérdés: döntési csomag PRG-4 | a csomagtervet a projektgazda; szerző: a modulgazda / tartalomfelelős (M4: szerző); QA: Memuna (M3.3, M3.4, M7), szakmai lektor (M4), értékelési felelős (kulcsközeli szöveg). |
| PRG-5 | `F` — Minden kötelező F-peulához legyen 1–5 főre előre leírt, azonos kompetenciát fejlesztő változat. Hiányzásnál dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út legyen, mindig a javító próbálkozás előtt; 1:1 kiskorúval csak a meglévő HUM-SAFE-02 kivétel szerint. A programvezető rögzítse a kapacitást és a pótlási felelőst. | javaslat PRG-5; kérdés: döntési csomag PRG-5 | programvezető + értékelési felelős (HUM 8–9 vétó/QA); a változat szövege: modulgazda; 1:1: Memuna. |
| PRG-6 | `F` — Az M0 diagnosztikus belépőkvíz ne kapjon kitalált formális megerősítési kaput. M7-nél a függőben lévő kvízeredmény ne szorítsa ki a v2 határidejét: indokolt egyéni hosszabbítás és meglévő F-peula utáni 1+1 javítás. Z-nél a mentor jelölje ki a javító időpontját, a teljesítés várja be az eredményt; a Z.3 v1-út azoknak is működjön, akiknek az M7 v2-je még nincs kész. Konkrét dátumot csak a tényleges naptárból írjunk. | javaslat PRG-6; kérdés: döntési csomag PRG-6 | programvezető (HUM-OPS-01 jóváhagyó); c) és e): + értékelési felelős; e): + modulgazda. |
| PRG-7 | `A` — Az M5/M6 diagnosztikus eredményből a mentor kapjon támogató, nem kötelező beavatkozási ajánlást; a hallgatót ne büntesse alacsony diagnosztikus pont. A programvezető a meglévő tananyagból ismétlést vagy beszélgetést rendelhet, új tanulási modult ne építsünk automatikusan. | javaslat PRG-7; kérdés: döntési csomag PRG-7 | programvezető + értékelési felelős. |
| PRG-8 | `A` — A peulák szerepeljenek a Moodle-kurzusban tanulói felkészítő leíróelemként, de a képzői forgatókönyv ne legyen résztvevői anyag; az F-peulák külön látható, releváns szakaszt és szükség esetén kézi, megalapozott részvételi jelölést kapjanak. A manifest ennek megfelelően bővüljön az új verzióhoz, nem a pilotba visszamenőleg. | javaslat PRG-8; kérdés: döntési csomag PRG-8 | programvezető + build-felelős. |
| PRG-9 | `F` — M1.2 SLIDE 5 Drag & Drop: nem szükséges, legyen csak húzásmentes, rádió-/kattintásos út. M2.1 identitáskör: maradjon a CP-ben integrált, nem követett reflexió, tényleges tárolás-ellenőrzéssel. M3.3 négy illusztrációja csak akkor épüljön be az elágazás UTÁN, ha bizonyított pedagógiai szerepe van, különben maradjon ki (SAFE-1 és passzjog előtt vizuális kitettség sem lehet). | javaslat PRG-9; kérdés: döntési csomag PRG-9 | a) szerző/modulgazda, indok híján a hozzáférhetőségi gazda (HUM-A11Y-01); b) build-/LMS-gazda + M2 modulgazda (DPO nem kell); c) projektgazda (build-spec gazda), QA: Memuna, hozzáférhetőségi gazda. |
| PRG-10 | `A` — M4.B feedbackben az SBI forma legyen opcionális, de Megfigyelés → Hatás → Következő lépés szerkezet kötelező. M5 produktumnál a valós kvuca-adat nem kötelező: fiktív profil egyenértékű. Zárókörben mindenki kapjon lehetőséget megszólalni, de a passz ugyanúgy teljes értékű részvétel. | javaslat PRG-10; kérdés: döntési csomag PRG-10 | M4: modulgazda, QA: szakmai lektor; `M5:ERT-G2-9`: modulgazda + értékelési felelős, a DPO-val egyeztetve; `M5:NYELV-G2-14`: modulgazda. |
| PRG-11 | `A` — Egységes skálázási szabály: 8–20 főnél alapból 3–5 fős csoportokat képezzünk, a csoportszámot és kártyakészletet a létszámhoz igazítva. Minden peula-specbe kerüljön az adott célhoz ténylegesen szükséges eset-/kártyadarabszám és az egyenlő részvétel ellenőrzése. Ez működési alapjavaslat, nem új kánoni létszámkorlát. | javaslat PRG-11; kérdés: döntési csomag PRG-11 | az adott modulgazda (M3.B: + Memuna; M0: modulgazda / projektgazda). |
| PRG-12 | `F` — Az M3.B 4. esetkártyáját használjuk előre megírt fiktív példaanyagként, és a felnőtt-gyanúsítottas eset kulcskülönbségét a képző akkor is mondja el, ha egy időhiányos lépés kimarad. Ne rögtönözzünk valós gyermekvédelmi történetet. Memuna review szükséges a konkrét forgatókönyvre. | javaslat PRG-12; kérdés: döntési csomag PRG-12 | M3 modulgazda + Memuna (tartalmi QA). |
| PRG-13 | `A` — Az M5.A és M6.A sarokjátékokhoz legyen mozgás nélküli, helyben jelzős/kártyás egyenértékű részvétel, a passzjoggal. A cél a vélemény és megértés kifejezése, nem a fizikai sarokba állás; a modulokban már van ehhez mintaszöveg. | javaslat PRG-13; kérdés: döntési csomag PRG-13 | modulgazda + hozzáférhetőségi gazda. |
| PRG-14 | `F` — Generatív AI eredetet csak szerzői/provenance bizonyíték alapján jelöljünk, soha ne tippeljünk. Az M7.1 no-AI alternatíva legyen ugyanabban az online leckében letölthető/nyomtatható promptkártya, azonos fejlesztési céllal és completionnel. A tényleges médiaeredetet a szerző vagy médiafelelős igazolja. | javaslat PRG-14; kérdés: döntési csomag PRG-14 | a) tananyagfelelős / szerző; b) programvezető vagy modulgazda, vétó: DPO/jogi felelős. |
| PRG-15 | `F` — M2.B 3. helyzetének lezárását meglévő kánoni példából és önkéntes reflektáló kérdéssel készítsük el; M5.1 SLIDE4 1./4. kulcsát csak a formális–nonformális–informális definícióval egybevetett szakmai lektor döntése után módosítsuk; M7.B A/B sarokjátéka maradhat nem pontozott, tanári összegzéssel, amíg nincs validált, egyértelmű helyes kulcs. | javaslat PRG-15; kérdés: döntési csomag PRG-15 | a) modulgazda / módszertani felelős, a Memuna bevonásával; b) M5 szerzője / modulgazda; c) modulgazda. |
| PRG-16 | `F` — A kilenc szerzői jelentéskérdésre a legkisebb értelmező javítás: M1 SBI-S határozói sablon; M1.A-n új cetli csak önkéntesen; M2 „megtartás” = támogató figyelem, nem titoktartási ígéret; M3.A a képző választ 3 kártyát; M4.4 „puha” = nem blokkoló fejlesztő visszajelzés; M6 nem valódi veszélyhelyzet eljátszása, hanem fiktív eset; M7.4 v1-ben a megfelelő meglévő szakaszba emelés; M7.B „átjárás” egyértelmű részvételi/álláspontváltási instrukció; Z.3 „túl kicsi” csak akkor hibapélda, ha konkrétan megmagyarázott. A szerző szándékát megerősítő rövid QA kell, nem új teljes review. | javaslat PRG-16; kérdés: döntési csomag PRG-16 | az adott modulgazda (M2 bizalmas olvasatnál Memuna; M6: a hub tartalomfelelőse; Z: modulgazda vagy projektgazda). |
| PRG-17 | `F` — Az M0.1 SLIDE 5 kíváncsiság/félelem, illetve „1–2/2–3 modul” kérdését most ne döntsük el puszta ízlésből. CC-04 szerint tényleges pilot-visszajelzéssel együtt kell választani; addig a változat izolált, nem módosítjuk a futó pilot tananyagát. | javaslat PRG-17; kérdés: döntési csomag PRG-17 | projektgazda / modulgazda. |
| LMS-1 | `F` — Az egyenértékű online szöveges és fájlfeltöltéses út maradjon. Elfogadott fájltípusok a tényleges akadálymentes sablonhoz igazítva (például .docx, .odt, .pdf), alapból legfeljebb 1 fájl; képfeltöltés/screenshot ne legyen szükséges vagy ösztönzött. A Z.4 videó csak külön, DPO által engedélyezett profilon szerepelhet. Cél-Moodle beállítás- és a11y-ellenőrzés kell. | javaslat LMS-1; kérdés: döntési csomag LMS-1 | LMS-gazda + DPO + hozzáférhetőségi gazda (X-11; HUM-A11Y-01). |
| LMS-2 | `A` — Az M3.2/M3.4 Drag & Drop mellékutakat hagyjuk el, ha a húzásmentes kártyás/rádiógombos út ugyanazt a tanulási célt és visszajelzést adja. A WCAG 2.2 AA 2.5.7 szerint húzásnál egyetlen mutatóval, húzás nélküli alternatíva kell; a felesleges kétféle implementáció csak növeli az eltérés kockázatát. | javaslat LMS-2; kérdés: döntési csomag LMS-2 | M3 modulgazda; vétó/QA: hozzáférhetőségi gazda. Rokon, másik kapun: `M1:IMPL-G1-8` (X-10, az M1.2 SLIDE 5 D&D-indoklása, ugyanaz az A11Y:33-kérdés). |
| LMS-3 | `F` — M5.3 késleltetett felidézéshez rövid, adatminimalista CP/PAGE út javasolt: a személyes felidézés a tanuló saját jegyzetében történik, külön pontozott önellenőrző itemekkel csak akkor egészítjük ki, ha erre van jóváhagyott tartalom. Üres CP-t ne állítsunk be hamis „Receive grade” completionnek; a valós H5P és az LMS-M5-07 manifest tesztje dönti el, kell-e más profil. | javaslat LMS-3; kérdés: döntési csomag LMS-3 | LMS-gazda + módszertani lektor/tananyagfelelős; az önellenőrző lépésről a modulgazda. |
| LMS-4 | `F` — Az M6 játéklap kapu megállapítását a rubrikasorok szemantikai értékelése és a GATE-CP hordozza, ne puszta Moodle-normalizált összpont. Ha megőrizzük az 1/2/3 pontokat, a Grade type / Maximum grade / rubrikaminimum és a 10 pontos „csupa Oké” negatív/pozitív teszt legyen dokumentálva. A rubrikapontértéket értékelői döntés nélkül nem vetítjük át 0/1/2-re. | javaslat LMS-4; kérdés: döntési csomag LMS-4 | LMS-gazda + értékelési felelős. |
| LMS-5 | `F` — Az M7.3 Zmán Kvucá-checklistet inkább Moodle core Page/CP + letölthető munkalap formában, tanuló-lokálisan építsük, külön tárolt komment és plugin nélkül; a completiont a befogadó tanulási szakasz viszi. Ha a checklist maga kötelező és minden pipát strukturáltan kell ellenőrizni, új manifest/activity/DPObizonyíték kell, de a „szabad pipa nélkül hagyni” szabályt nem sértheti. | javaslat LMS-5; kérdés: döntési csomag LMS-5 | projektgazda + LMS-gazda/Moodle-adminisztrátor + DPO; a completionről értékelési felelős. |
| LMS-6 | `A` — Az M7.4 3–4 terület kijelölése legyen pontozatlan, saját jegyzetes lista, nem minden választ „helyessé” programozó H5P Multiple Choice. Nincs pedagógiai helyes válasz; a Completiont az oldal vagy összefoglaló dia biztosítja, ne a véleménykiválasztás. | javaslat LMS-6; kérdés: döntési csomag LMS-6 | LMS-gazda. |
| LMS-7 | `F` — Elsőként a Program terv kánoni M7.2-DIA-01 alt-szövegét használjuk, de csak akkor, ha a diagram lényegi információját ténylegesen közvetíti. Az akadálymentességi felelős ellenőrizze, hogy a rövid alt és a látható kísérőszöveg együttesen teljes értékű-e; nem az alt hossza, hanem a funkciója a döntő. | javaslat LMS-7; kérdés: döntési csomag LMS-7 | projektgazda; vétó: hozzáférhetőségi gazda. |
| LMS-8 | `F` — Az AI-segédet kezdetben képző által közvetített, opcionális, személyes adat nélküli útban engedném (C). Közvetlen tanulói chatbot/plugin csak krízis-, adatkezelési, jogosultsági és no-AI parity review után. A H5P/Moodle course completion ne függjön az AI használatától. | javaslat LMS-8; kérdés: döntési csomag LMS-8 | programvezető + Moodle-adminisztrátor; vétó/QA: DPO/jogi felelős. |
| VO-1 | `F` — Egyetlen VO-fix pack legyen; a valóban kimondott szöveget módosító 6 blokkot újra kell renderelni és meghallgatni. A további 9 írásmódi/typográfiai blokkot csak dokumentált kiejtési azonosság, source hash és VO-gazda ellenőrzés után lehet régi hanggal tartani; kétség esetén újrarender. A két videó feliratát és leiratát külön hang–szöveg egyezésre ellenőrizzük. | javaslat VO-1; kérdés: döntési csomag VO-1 | médiafelelős / VO-gazda (X-17); a kurzusoldali alkalmazást a felhasználó kéri. |
| TECH-1 | `A` — A jelenlegi gyermekvédelmi tiltóőrt (az egybeírt alak tilalma, X-18) nem lazítanám globálisan. A legkisebb biztonságos megoldás elsőre az (A): a már működő „mini-jelenet” formát hagyjuk, a P2 helyesírási hibát dokumentált kivételként. Ha szerkesztői egység miatt mégis javítanánk, inkább „rövid jelenet” (D) három fájlban, mint széles fájl-szintű security-exemption; kizárólag tételes regression-test után. | javaslat TECH-1; kérdés: döntési csomag TECH-1 | projektgazda (eszköz- és governance-változás); gyermekvédelmi vonatkozásban a GK:23 vétójoga (Memuna, DPO) érintetlen. |
| TECH-2 | `F` — Az M6.1/M6.2 két címbeli/fájlnévi javítását elvégezném külön, review-olható change setként, az összes hivatkozás, két gépi útvonalkulcs, baseline-rename mapping, pin és generált média együttmozgásával. A git mv-t a tulajdonos futtassa a saját termináljában, a hookot nem kerülve meg; utána célzott selftest, invariáns és külön media commit. | javaslat TECH-2; kérdés: döntési csomag TECH-2 | a felhasználó (az átnevezési commit futtatása) + projektgazda (a `tools/` két sora és a baseline-sor). |

**Bizonyíték- és aláírás-bejegyzések — nyitott bizonyíték-kapuk, nem projektgazdai döntések.** A szükséges bizonyíték és az igazoló a javaslat szerint. Egyik sem zárul ezzel a szakasszal.

| Bejegyzés | Szükséges bizonyíték | Igazoló | Állapot |
|---|---|---|---|
| GYV-24 | Egyazon végleges SHA-ra szóló, datált „átnéztem” G1; SAFE-7 és valamennyi 1:1-kulcs explicit verdikt; akut út/segélyvonal friss ellenőrzése; tracker #1 lezárása linkkel | Memuna | nyitott bizonyíték-kapu |
| ADV-E1 | Activitynkénti DPO G2 QA: pontos adatmezők, hozzáférési szerepek (mentor/editor/manager/admin), megőrzés, export, xAPI/LRS, saved-state, backup, esetenkénti tartalékút. M0/M1-re prioritás | DPO/jogi felelős | nyitott bizonyíték-kapu |
| ADV-E2 | Teljes activity-szintű adatleltár, külső Google/papír/mentori jegyzet folyamatokkal, adatfeldolgozói és törlési renddel, „külön review” helyek rögzítése | DPO/jogi és programvezető | nyitott bizonyíték-kapu |
| ADV-E3 | HUM-PRIV-04 AI-kapcsolat tényellenőrzése: API, közvetítő, provider, naplózás, retention, hozzáférés, továbbítás, no-AI egyenértékű út; formális QA | DPO/jogi | nyitott bizonyíték-kapu |
| SIG-1 | M0 hét belépőkvíz-itemjének független értékelési QA-ja; az 1–2. itemnél gyermekvédelmi kontroll, dátummal és SHA-val | Értékelési felelős, 1–2.: Memuna | nyitott bizonyíték-kapu |
| SIG-2 | M3 ≥10/12 és kritikus Q2/Q4/Q7/Q9, M7 Q13 szakértői item- és küszöbmegállapítás (korábbi Q-PED-6 Angoff-elv átvezetése); 1–2 közös referenciaminta; kétszemes blokkoló döntési rend | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél | nyitott bizonyíték-kapu |
| SIG-3 | M3.4 kritikus követelmény megnevezése kulcsfelfedés nélkül; szöveg és valós tanulói review-options QA | Értékelési felelős + Memuna | nyitott bizonyíték-kapu |
| SIG-4 | M4 kvíz/rubrika/sablon és M5 kapu független lektori QA-ja az összes függő döntés alkalmazása után | Kijelölt szakmai lektor; M5 assessment QA | nyitott bizonyíték-kapu |
| SIG-5 | M5 AI-generált media assetenkénti emberi szakmai és eredetjelölési ellenőrzés; release-record referencia | Szakmai lektor | nyitott bizonyíték-kapu |
| SIG-6 | M6 média jogosultságok: J3, H-11, AI Act minősítés, J2, V1, V3/E-8, R2/R3 és minden releváns RIGHTS-EVIDENCE kontroll; az érintett asset addig fallbacken | Jogi jogosult, Memuna, DPO, szerző | nyitott bizonyíték-kapu |
| RT-1 | Valódi technikai/program/mentor/Memuna kontakt, ügyfél- és tanulói nézetben helyesen megjelenik; nyitvatartás, szerepcímke, elérhetőség | LMS-gazda + programvezető | nyitott bizonyíték-kapu |
| RT-2 | M0/M1 completion/unlock/attempt/GATE_CP, védett és hibás negatív esetek; N-M1-04 saját jegyzetes/no-input alapút; H5P saved-state, xAPI/LRS és jogosultsági visszaolvasás a célverzión | Moodle/LMS-gazda, a11y szerep, DPO a saját részén | nyitott bizonyíték-kapu |
| RT-3 | M4 kész kapu/completion/a11y és notification teszt; tényleges M4_ASSIGN dátum és az elkülönített learner-scope | LMS-gazda + programvezető + a11y | nyitott bizonyíték-kapu |
| RT-4 | M6.4 Branching Scenario A → B → opcionális C → D → 6D → ZÁRÓ valós bejárása; kizárólag végponti completion, passz és érintés/húzásmentes működés | LMS-gazda + a11y | nyitott bizonyíték-kapu |
| RT-5 | M7 AI „store=false” és esetleges proxy/provider naplózások auditja, API és ZDR jogcím; no-AI út feladat-, grade- és completion-paritása | LMS-gazda + DPO | nyitott bizonyíték-kapu |
| RT-6 | M7.2/M7.3 minden párosítás billentyűzettel és egyérintéses kattintás/koppintás útján egyenértékű, azonos visszajelzéssel; mobil portrait teszt | LMS-gazda + független hozzáférhetőségi QA | nyitott bizonyíték-kapu |

## 15. Projektgazdai döntések és irányok – a D-01…D-23 csomagok (2026-10-13)

A 2026-10-13-i projektgazdai irányok átvezetése a kánoni döntési helyre. Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai felhatalmazás és irányok – D-01…D-23, AP-2026-10-13-01.md`. A csomagok
(kérdések, opciók, kutatás): `01 Fejlesztés/04 Audit/2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`.
A státusz-szemantika a 11. szakasz szerinti.

- **A 14. szakasz nem nyílik újra.** Ez a szakasz a 14. szakasz döntéseinek alkalmazását rögzíti ott, ahol a döntés a
  projektgazda hatáskörében marad.
- **Lezárt döntés:** az első táblázat sorai. Projektgazdai hatáskör: a 14. szakasz érintett sorában nincs más szerepnek
  fenntartott jóváhagyás, és a független ellenőrzés (verifier) a tételt nem sorolta a szerepköri döntések közé. A jobb oldali
  oszlop utólagos vétó/QA; vétónál a sor `REOPENED`.
- **Nyitott, szerepköri döntésre vár:** a második táblázat sorai. A projektgazda iránya ezeknél **nem döntés**, és nem
  helyettesíti a megnevezett szerep döntését vagy írásos jóváhagyását; a sorok kifejezetten `nyitott` jelölésűek. A
  kitöltött elfogadási javaslatok: az `01 Fejlesztés/04 Audit/` 2026-10-13-i jóváhagyási csomagjai.
- **Amit a szakasz nem zár le:** a 14. szakasz bizonyíték- és aláírás-bejegyzéseit (G1–G8), a runtime-bizonyítékot, a
  futó pilotot (`main@213a4c5`, CC-04) és a release-t. A szakasz nem release-jóváhagyás.
- **Pontosítások a korábbi szövegekhez:** a D-08 (b) sorban a 11. szakasz és az M3.3 §7.1 „ugyanaz a passz-választó”
  szabálya a kérdésre és a két opcióra vonatkozik (a szitu címe a 16. szakasz szerint külön előnézeti csomóponton áll); a D-15 (e) sor a PRG-9 b
  átvezetése, ezért az M2.1 identitás-kör kérdésénél a HUM-PRIV-01 zárójeles mechanizmusa helyett az interakció nélküli,
  nem rögzítő dia érvényes (a HUM-PRIV-01 célja – a válasz nem kerül tárolásra – változatlan); a D-22 sor a PRG-16
  „átjárás”-olvasatát az M7.B-re pontosítja.

| Azonosító | Projektgazdai döntés (2026-10-13) | Alap (14. szakasz) | Utólagos ellenőrzés (vétó/QA) |
|---|---|---|---|
| D-02 | A GYV-17 „a kiskorúakra is térjen ki” fordulata alkalmazási kört jelent: a tiltott zónák keretét kiskorú résztvevőkkel is mindig ki kell mondani. Az M6.A meglévő, kötelező kerete ezt teljesíti; további szöveg nem kell. | GYV-17 | Memuna + a peula tartalomfelelőse. |
| D-03 | Az M3.A és az M3.B kártya- és esetkészlete a meglévő kártyák duplikálásával igazodik a létszámhoz (8–20 főnél 3–5 fős csoportok; négy csoporttól a 8 kártyás szett második példánya, illetve az 1–3. eset két példányban, visszahozás esetről esetre); az M3.B 4. esetkártyája a 4.3.3 előre megírt, fiktív esete marad, a lépés címéből kikerül az „új”. Új eset nem készül. | PRG-11, PRG-12 | M3 modulgazda + Memuna; a 4. esetkártya forgatókönyvének Memuna-reviewja (PRG-12) nyitott bizonyíték. |
| D-06 | A JOG-1 jogászi ellenőrzésének elsődleges nyilvántartása a G1 tracker-issue (#1); a `RELEASE-READINESS.md` és a `Gyermekvédelem – release gate.md` erre hivatkozik. Az issue nyilvános: személyes adat nem kerül bele. | JOG-1 („a nyilvántartás helyéről a projektgazda”) | jogi szakértő; jóváhagyás: Memuna (GK §5). |
| D-08 (b) | Az M3.3 P1–P4 passz-választóin a soron következő szitu meglévő címe előzetes témajelzésként megjelenik (build-spec; a megjelenítés módját a 16. szakasz határozza meg, és az felváltja a `showContentTitle` megoldást); a megjelenést stagingben igazolni kell. | GYV-2 (MAN:57 és az M3.3 §7.1: projektgazda mint build-spec gazda) | Memuna (QA: a cím megterhelő-e). |
| D-11 | Az ADV-1 csoportszűkítése kiterjed a H5P-C, a QUIZ-D/QUIZ-M, az ASSIGN-S/ASSIGN-M és a GATE-CP mentori nézetére. A csoportmód önmagában nem elegendő: „Separate groups” az activityken és a kurzuson (a pontkönyv miatt; „Force group mode”: „No”), a mentor szerepe csak csoportba sorolás után, csoportokon átnyúló jogosultság a mentor szerepén nincs, a szélesebb szerepek szűken, név szerint, auditálhatóan; második értékelő és F-peula-képző az ADV-2 szerint; az M0 belépőkvíz egyéni válaszai a GYV-23 szerint. Negatív hozzáférési tesztek a runtime acceptance 15. pontjában. | ADV-1 (ADV §3: „a döntés kiterjedéséről a projektgazda dönt”), ADV-2, GYV-23 | DPO / jogi felelős; a szerepkiosztást az LMS-gazda rögzíti; runtime: RT-P0-15. |
| D-12 | A GYV-23 „a biztonsági 1–2. item nyilvános visszajelzése”: a két item helyes válasza és magyarázata név és egyéni eredmény nélkül, csoportszinten, mindenkinek. | GYV-23 | programvezető + Memuna; adatkör: DPO. |
| D-13 (a), (e) | (a) Az ADV-11 közös eszköz-protokollja minden közös vagy tartalék eszközre vonatkozik, az M0.A technikai segítségpontjára is. (e) Az M2 kapubeadvány külön névmezője megszűnik; a beadást a Moodle-fiók azonosítja. Megőrzési időt ez a sor nem rögzít. | ADV-11, ADV-1 | (a) LMS-gazda + DPO; (e) DPO / jogi felelős. |
| D-15 | A hat build-spec javaslat: (a) az M3 kapukvíz a helyzetleírás megerősített rubrikájának külön GATE-CP-je (LMS-M3-08) után nyílik, határ nélküli Grade-feltétellel (ERT-9); (b) a Z.3 5. dia célmondata kötelező, tanuló-lokális lépés beviteli elem és completion nélkül (ADV-3); (c) az M4 fejlesztő rubrikája az LMS-M4-05-ön rögzül (ERT-8); (d) az LMS-M6-05 pontozása a rubrika nyers összege, a tanuló elől rejtve, a rubrikapontértékek változatlanok (LMS-4); (e) az M2.1 SLIDE 4 a követett CP interakció nélküli reflexiós diája (PRG-9 b); (f) a fórum feltétele csak a megnyitás után induló kohorszban él, zárt állapotban egyetlen feltétel sem hivatkozik rá (ADV-6). Mindegyik külön tesztelendő. | ERT-9, ADV-3, ERT-8, LMS-4, PRG-9 b, ADV-6 | (a) projektgazda / build-spec gazda, QA: értékelési felelős; (b) DPO / jogi felelős; (c) értékelési felelős, programvezető, adatkör: DPO; (d) LMS-gazda + értékelési felelős; (e) build-/LMS-gazda + M2 modulgazda; (f) DPO / jogi felelős. |
| D-17 (d) | A v2 R1 változatlan: a semleges vagy kitalált someres érték teljesíti (ADV-5). | ADV-5 (someres vonatkozásban a projektgazda) | DPO / jogi felelős; QA: helyi ideológiai felelős (HUM-SOMER-01). |
| D-19 (b) | Az M4.1 ILO 2 a ténylegesen mért szintre (felismerés) szűkül. | PRG-2, ADV-3 | M4 modulgazda; QA: értékelési felelős. |
| D-22 | Az M7.B „átjárás” szava logisztikai értelmű: átvonulás másik helyszínre. A PRG-16 részvételi olvasata erre a helyre nem vonatkozik. | PRG-16 | M7 modulgazda. |
| D-23 | Az M7 kapukvízen a helyes válasz és a megoldókulcsot felfedő visszajelzés egyik automatikus review-ablakban sem jelenik meg, a lezárás után sem; nincs automatikus kvízszintű zárás. A hibázott kompetenciát vagy kritikus követelményt a mentor közli a GATE-CP-n (LMS-M7-09), a kulcs felfedése nélkül. A beállítást cél-Moodle-ben tesztelni kell (RT-P0-19, RT-P0-08). Az M3 kapukvíz rendje nem változik. | ERT-5 (a `3b160fc`-ben átvezetett rész nem nyílik újra) | értékelési felelős. |

**Nyitott – szerepköri döntésre vagy jóváhagyásra vár (a projektgazda iránya rögzítve, nem döntés).**

| Azonosító | Projektgazdai irány (2026-10-13) | Ki dönt / hagyja jóvá | Állapot |
|---|---|---|---|
| D-01 | Egységes peula-megállítási protokoll, helyszíni helyettesítés, érzékeny foglalkozásoknál két felkészített 18+ felelős. | Memuna + programvezető (GYV-5: a létszámnorma az ő hatáskörük) | nyitott |
| D-04 | A meglévő kétlépcsős eszkaláció alkalmazása, egyértelmű címzettekkel és közvetlen veszélynél azonnali biztonsági intézkedéssel (a Z.3 veszélydoboz 112-mondatával együtt). | Memuna; a GYV-8 részeknél + programvezető; az M6.4 6D/ZÁRÓ küszöbét zároló M6-NY-D27 a Memuna szakmai reviewja céljára feloldva (16. szakasz), a küszöb módosítása nincs előre jóváhagyva | nyitott |
| D-05 | A 116-111 és a 116-000 félrevezető leírásának javítása aktuális elsődleges forrás alapján. | Memuna (GYV-14: formális újranyitás) | nyitott, sürgős |
| D-07 | Biztonságkritikus rubrikák és itemek közös szakértői kalibrációja, előzetesen nem közölt bukási feltétel nélkül. | értékelési felelős + Memuna; rubrikaszint és kulcs: projektgazda | nyitott |
| D-08 (a) | Valódi passzjog az M2.4-ben, egyenértékű fiktív tudásdemonstrációval. | Memuna + programvezető (HUM-SAFE-03) | nyitott |
| D-09 | A 24 órás kapuértékelési határidő elkülönítése a gyermekvédelmi bejelentésektől; a határidő csak az illetékesek döntésével változhat. | Memuna + DPO (GYV-1 feltétele) | nyitott |
| D-10 | Incidensnyilvántartás, hozzáférés-korlátozás, dokumentált megőrzés/törlés, feltárásmentes pótlási út. | Memuna + DPO; pótlás: értékelési felelős + programvezető | nyitott |
| D-13 (b), (c), (d) | Adattakarékosság (az M4 fókuszmondat-kártya és a Z.A szófelhő-cetli besorolása; az M2.A csoportnormájának kiterjesztése a felismerhető részletre). | (b), (c) DPO / jogi felelős; (d) Memuna + DPO | nyitott |
| D-14 | A nem igazolt AI-adatfolyam inaktív marad; a no-AI út egyenértékű; a naplózás, a megőrzés, az adattovábbítás és a képző által közvetített AI-használat dokumentálandó. | DPO / jogi felelős; programvezető + Moodle-adminisztrátor | nyitott (az inaktív alapállapot a GYV-10 és az ADV-12 szerint már érvényes) |
| D-17 (a)–(c) | Rubrikakalibráció indokolatlan küszöbemelés nélkül; a pedagógiai pontozás és az adatvédelmi stop külön. | értékelési felelős (+ DPO az ERT-42-nél); az ERT-43 elvét a projektgazda elfogadta (16. szakasz), hatályba az értékelési felelős és a lektor QA-ja és előzetes tanulói tájékoztató után lép, visszamenőleges hatás nélkül | nyitott |
| D-18 | Az itemkulcsok a ténylegesen tanított tartalomhoz igazodnak; kulcs csak szakmai jóváhagyással változik. | értékelési felelős + modulgazda / M5 szerző / szakmai lektor | nyitott |
| D-19 (a), (c) | A kimenetek ne ígérjenek magasabb szintet, mint amit a tananyag gyakoroltat és mér. | modulgazda / értékelési felelős (TERM-7) | nyitott |
| D-20 | Modulonkénti, lépésszintű vágási terv a védett lépések megtartásával. | az adott modulgazda (M3.B: + Memuna) és a programvezető jóváhagyása tervenként (16. szakasz); a B-változatok belső blokkhatár-eltolása a teljes időkeret és a védett lépések megtartásával engedélyezett (16. szakasz) | nyitott |
| D-21 | Közös 1–5 fős F-peula keret modulspecifikus kiegészítéssel; konkrét `/course-develop` terv, tartalomgyártás a terv projektgazdai elfogadásáig nincs. | a tervet a projektgazda elfogadta (16. szakasz; E7: igen); a tartalom külön `/course-develop` futásban készül; nyitott az E1–E6 (a terv E pontja szerint: Memuna, programvezető, LMS-gazda, értékelési felelős, DPO); Memuna (1:1, a terv 6–7. pontja); modulgazdák (betétek) | nyitott (E1–E6 és a megírt tartalom jóváhagyása) |
| D-16 | A Z.4 „Teljesítve” mércéje a beadás egészének minimális értelmezhetősége; a háromrészes szerkezet formatív útmutató, a szenzitív részek passzolhatók. Az ERT-3 „kiürítés” szava az üres kötelező beküldés negatív tesztjét jelenti; a válaszok törlése külön megőrzési kérdés (DPO). | értékelési felelős (ERT-38; ERT-3, Z.4); vétó/QA: programvezető, a Z.4-nél DPO + programvezető | nyitott: szakmai jóváhagyásra vár (16. szakasz); a meglévő implementáció (`8bb4d7d`, `9788c05`) marad |

## 16. Projektgazdai döntések – az AP-2026-10-13-01 záró jelentésének nyolc kérdése (2026-10-13)

A projektgazda 2026-10-13-i válasza a záró jelentés nyolc kérdésére. Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai döntések – a záró jelentés nyolc kérdése, AP-2026-10-13-02.md`. A
státusz-szemantika a 11. szakasz szerinti.

- **Lezárt döntés:** az alábbi táblázat projektgazdai döntés-oszlopa. A jobb oldali oszlopban álló szerepköri döntés,
  QA és bizonyíték nyitott marad; a szakasz ezeket nem zárja le, és nem release-jóváhagyás.
- **Viszony a 15. szakaszhoz:** a D-16 sor a 15. szakasz lezárt táblájából a nyitott táblába került (szakmai
  jóváhagyásra vár); a D-08 (b) sor megjelenítési módját ez a szakasz határozza meg; a D-04, D-17, D-20 és D-21 nyitott
  sora erre a szakaszra hivatkozik. A 15. szakasz többi sora nem változik.

| Azonosító | Projektgazdai döntés (2026-10-13) | Érintett hely | Nyitva marad (ki dönt / milyen bizonyíték) |
|---|---|---|---|
| D-21 | A közös 1–5 fős F-peula keret `/course-develop` terve (`01 Fejlesztés/04 Audit/2026-10-13 course-develop terv – 1–5 fős F-peula keret, D-21, AP-2026-10-13-01.md`) elfogadva, a benne foglalt 6a és 6b tervezési változással. E7: igen – az M2.F és az M4.F csak opcionális hivatkozást kap (ajánlott F-peula, nem PRG-5-kötelezettség). Az új tananyag külön `/course-develop` futásban készül. | 15. szakasz D-21 sora | az E1–E6 szerepköri döntés a terv E és F pontja szerint: E1 Memuna + programvezető; E2 Memuna; E3 programvezető; E4 programvezető, illetve LMS-gazda; E5 programvezető + értékelési felelős; E6 DPO + programvezető; a terv 6–7. pontja: Memuna; a modulspecifikus betétek: a modulgazdák; a megírt tartalom review-kapui és szerepköri jóváhagyása. |
| D-20 | A vágási tervek B-változataiban a belső blokkhatár eltolható, ha a teljes időkeret (a 45 perces peulablokk és a központi naptár, PRG-1) és a védett lépések változatlanok. | 15. szakasz D-20 sora; `01 Fejlesztés/04 Audit/2026-10-13 Jóváhagyási csomag – modulgazdák, D-20 vágási tervek, AP-2026-10-13-01.md` | modulgazdai (M3.B: + Memuna) és programvezetői jóváhagyás tervenként. |
| ERT-43 | Az M7 R1 2-es szintjének új horgonya elvben elfogadva. Hatályba csak az értékelési felelős és a lektor QA-ja, valamint előzetes tanulói tájékoztató után lép; visszamenőleges hatása nincs. | M7 KAPU R1 (a szöveg addig változatlan) | értékelési felelős és lektor QA-ja; az előzetes tanulói tájékoztató. |
| M6-NY-D27 | Az M6-NY-D27 zárolása (a D1 kiváltó feltétele és a Memuna bevonásának küszöbe nem változik) a Memuna szakmai reviewja céljára feloldva. A küszöb módosítása nincs előre jóváhagyva. | M6.4 6D és ZÁRÓ (D-04) | a Memuna szakmai döntése; a küszöb bármely módosításához külön jóváhagyás kell; addig a mai szöveg érvényes. |
| D-08 (b) | A passz-választás előtt (M3.3 P1–P4) a soron következő szitu meglévő címe külön, semleges előnézeti csomóponton jelenik meg, a történet feltárása nélkül; a passz-választó eredeti kérdése és két opciója marad. Ez felváltja a 15. szakasz D-08 (b) sorának `showContentTitle` megoldását, amely a h5p-branching-scenario forrása szerint passz-választó csomópontnál nem jeleníti meg a címet (M3:QA17-IMPL-1). | M3.3 3. szakasz; manifest BSPEC-05; runtime acceptance 11. pont | Memuna-QA (a cím megterhelő-e); runtime-teszt (11. pont). |
| LMS-M4-05 | Az M4 fejlesztő rubrikája egyetlen holisztikus kritérium a meglévő három szinttel; szintpont: 0 (Még nem éri el), 1 (Alapszint / rendben), 2 (Fejlettebb); Grade type: Point; Maximum grade: 2; Grade to pass: üres. A numerikus érték a tanuló elől rejtett, a szöveges értékelés látható. A három szint szövege nem változik. | manifest LMS-M4-05; runtime acceptance 26. pont | értékelési QA; Moodle-visszaolvasás a célverzión; a végső pontszám rejtésének módja (projektgazda mint build-spec gazda + LMS-gazda; manifest LMS-M4-05). |
| D-16 | A 15. szakasz D-16 sora nem végleges lezárt döntés, hanem szakmai jóváhagyásra vár. A meglévő implementáció marad, automatikusan nem vonjuk vissza. | 15. szakasz: a D-16 sor a nyitott táblában | értékelési felelős; vétó/QA: programvezető, a Z.4-nél DPO + programvezető. |
| JOG-1 | A JOG-1 nyilvántartására előkészített komment közzétéve a G1 tracker-issue-ban (#1), személyes adat nélkül. | G1 tracker-issue (#1) | a jogász írásos ellenőrzése és a Memuna jóváhagyása (G1). |

## 17. Projektgazdai döntés – X-16 staging-validációra (2026-10-13)

A projektgazda 2026-10-13-i döntése a rubrikás Assignmentek numerikus összpontjáról (X-16). Szó szerint:
`01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai döntés – X-16 staging-validációra és staging-előkészítés, AP-2026-10-13-04.md`.
A státusz-szemantika a 11. szakasz szerinti.

- **Hatókör:** staging-tesztelési jóváhagyás, nem végleges X-16 release-elfogadás. A végleges elfogadás a runtime-teszt
  (runtime acceptance 28. és 29. pont) és a lenti nyitott kérdések rendezése után külön döntés.
- **Nyitott (release-kapu):** ha a tanuló a `graderaw` vagy más út révén a numerikus pontszámhoz hozzáfér, a rejtés nem
  teljesült. A Moodle 4.5 forrása szerint a hivatalos mobil-webszolgáltatás két függvénye (`gradereport_user_get_grade_items`:
  `graderaw`; `mod_assign_get_submission_status`: `feedback.grade`) a nyers pontot visszaadja; a lezárás módjáról a
  projektgazda, az LMS-gazda és a site-adminisztrátor dönt (manifest LMS-M4-05); a site-szintű letiltás nem
  engedélyezett (19. szakasz, X-16-WS).
- **Nyitott (adatvédelmi kérdés):** a tanuló saját adatexportja („Data requests” – „Export all of my personal data”) is
  tartalmazza a nyers Assignment-pontot. Arról, hogy a rejtés release-feltétele erre az útra is vonatkozik-e, a DPO, a jogi
  felelős és a projektgazda dönt; a build ezt az utat nem korlátozza (manifest LMS-M4-05). A projektgazda javaslata: 18.
  szakasz, X-16-PRIV (PROPOSED); hatóköre: 19. szakasz, X-16-PRIV-HATÓKÖR.

| Azonosító | Projektgazdai döntés (2026-10-13) | Érintett hely | Nyitva marad |
|---|---|---|---|
| X-16 | A Moodle „Grade letter” megoldás staging-validációra elfogadva: egységes címke „Szöveges értékelés”, 0 %-os alsó határral; az LMS-M2-05, LMS-M4-05 és LMS-M6-05 rubrikáján `showscorestudent` = No, a grade itemen „Grade display type” = „Letter”, a grade item látható; a javasolt tanulói pontkönyv-beállítások érvényesek, „Show average” = No, „Show grades” = Yes, „Show feedback” = Yes; a „Course total” rejtett. A rubrikaszintek, a pontértékek, a küszöbök, a completion és a GATE-CP változatlanok. A kurzusszintű mellékhatásokat külön regressziós teszt ellenőrzi. | manifest LMS-M4-05 (LMS-M2-05, LMS-M6-05 mutatóval); runtime acceptance 28., 29. pont | a runtime-teszt (RT-P0-28, RT-P0-29); a webszolgáltatás-út lezárása; az adatexport-út adatvédelmi kérdése; a végleges release-elfogadás. |

## 18. Projektgazdai döntés – X-16 tesztkiegészítés, csonk-activityk és QA-elkülönítés (2026-10-13)

A projektgazda 2026-10-13-i döntése a staging build-terv két nyitott tesztkiegészítéséről és a QA-elemek elkülönítéséről.
Szó szerint: `01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai döntés – X-16 tesztkiegészítés, RA 8 és 29 csonk-activityk,
QA-elkülönítés, AP-2026-10-13-05.md`. A státusz-szemantika a 11. szakasz szerinti. A deploymentre ez a döntés nem ad
engedélyt; runtime-teszt ettől nem igazolt.

| Azonosító | Projektgazdai döntés (2026-10-13) | Érintett hely | Nyitva marad |
|---|---|---|---|
| X-16-TESZT | Az X-16 tesztkiegészítés (a) változata: az LMS-M2-05, LMS-M4-05 és LMS-M6-05 Assignment, valamint a hozzájuk tartozó három GATE-CP sor (LMS-M2-10, LMS-M4-10, LMS-M6-07) tesztcélú, előfeltétel nélküli példányként készül el a zárt staging QA-környezetben. A tényleges rubrika, pontozás, szintek és GATE-CP-szemantika változatlan; a kanonikus sorok valódi unlock-szabályai nem változnak. | manifest §8; runtime acceptance 28. pont, 29. pont (a), (f), 30. pont | a runtime-teszt (RT-P0-28, RT-P0-29, RT-P0-30); a QA-másolat eredményének érvénye és a kanonikus visszaellenőrzés: eldöntve, 19. szakasz, X-16-KANON. |
| RA8-29-CSONK | A runtime acceptance 8. és 29. pontjához két tesztcélú csonk-activity: a valódi, LMS-M1-06-ra épülő Grade-alapú hozzáférési feltételt modellezik („M1 megerősítve”, „M1 complete”); a negatív és a pozitív próbához mindkét szükséges állapot előállítható. Az eredmény kizárólag az adott mechanizmust igazolja, nem a teljes M2–Z end-to-end működést. | manifest §8; runtime acceptance 8., 29., 30. pont | a runtime-teszt (RT-P0-08, RT-P0-29, RT-P0-30). |
| STG-QA | QA-elkülönítés: a 13 kanonikus M0+M1 activity önálló, változatlan build-szelet; a hat X-16 tesztelem és a két csonk kizárólag belső QA-elem ugyanabban a zárt staging-kurzusban, elkülönített tesztszakaszban; egyértelmű tesztazonosítót kapnak, nem kerülnek a kanonikus completion-követelményekbe és a tanulói release-be; a release előtt eltávolítandók, és a valódi előfeltétel-lánc külön tesztelendő; a manifestben a kanonikus build-ID-k és a teszt-only azonosítók elkülönülnek. | manifest §8, §6; runtime acceptance 30. pont; `RELEASE-READINESS.md` Staging-szabály 6. | az eltávolítás és a valódi lánc tesztje (RT-P0-30). |
| X-16-PRIV | **PROPOSED – projektgazdai javaslat, nem lezárt döntés.** A numerikus értékelés ne jelenjen meg a normál tanulói Assignment-, Grades-, Quiz- vagy mobilos tanulási felületen. A GDPR szerinti, jogosult sajátadat-hozzáférést és adatexportot ettől külön kell kezelni. A nyers értékelési adat pusztán a felületi rejtés érdekében nem tartható vissza automatikusan. | 17. szakasz („Nyitott (adatvédelmi kérdés)”); manifest LMS-M4-05 | nyitott: a DPO és a jogi felelős döntési kapuja; a javaslat hatóköre: 19. szakasz, X-16-PRIV-HATÓKÖR. |
| X-16-WS | **Nyitott – nincs jóváhagyva:** a mobil-webszolgáltatások letiltása. A site-szintű hatásokat, a már kiadott tokeneket és az alternatív jogosultságkorlátozást a site-adminisztrátorral kell tisztázni. | 17. szakasz („Nyitott (release-kapu)”); manifest LMS-M4-05 | nyitott: a webszolgáltatás-út lezárása (projektgazda + LMS-gazda + site-adminisztrátor); folytatás: 19. szakasz, X-16-WS. |

## 19. Projektgazdai döntés – X-16 kanonikus visszaellenőrzés és az X-16-PRIV hatóköre (2026-10-13)

A projektgazda 2026-10-13-i döntése a 18. szakasz két nyitva maradt kérdéséről (az RT-P0-28 bizonyítéka, az X-16-PRIV
hatóköre) és az X-16-WS helyzetéről. Szó szerint: `01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai döntés – X-16
kanonikus visszaellenőrzés, X-16-PRIV hatókör, X-16-WS, AP-2026-10-13-06.md`. A státusz-szemantika a 11. szakasz szerinti.
Új tesztelem vagy activity nem készül; deploymentre ez a döntés nem ad engedélyt; runtime-teszt ettől nem igazolt.

| Azonosító | Projektgazdai döntés (2026-10-13) | Érintett hely | Nyitva marad |
|---|---|---|---|
| X-16-KANON | A hat QA-X16 tesztelemen végzett RT-P0-28 és RT-P0-29 (a), (f) vizsgálat előzetes, mechanizmusszintű runtime-bizonyíték. A végleges `RUNTIME_VERIFIED`-hez a kanonikus LMS-M2-05, LMS-M4-05 és LMS-M6-05 elemen célzott visszaellenőrzés kell; a QA-másolaton ugyanabban a Moodle-környezetben sikeresen lefuttatott negatív és pozitív esetek teljes megismétlése nem szükséges, ha bizonyított: (1) a kanonikus activity és QA-másolata releváns beállításai ténylegesen azonosak, az eltérések dokumentálva; (2) mindhárom kanonikus Assignmentnél tanulói tesztfiókkal ellenőrzött a numerikus összpont rejtése, a szöveges rubrikaszint és a mentori komment láthatósága; (3) az értékelői munkafolyamat, a GATE-CP, a rubrikapontok, a completion és a kapuküszöbök nem változtak; (4) az RT-P0-29 (a), (f) kanonikus megjelenítési eredménye dokumentált; (5) a kapcsolódó, külön nyitott API-, mobil- és adatvédelmi kapuk státusza változatlanul, valós bizonyíték alapján kezelt. Amíg a kanonikus elemek nincsenek megépítve és ellenőrizve, a QA-másolat eredménye a meglévő bizonyítékjelöléssel rögzül (a sor állapota `IMPLEMENTATION_TEST_REQUIRED` marad, a Bizonyíték oszlopban mechanizmus-bizonyíték); új státusz nem készül. Az RT-P0-28 nem nyilvánítható sikeresnek, ha valamelyik kötelező negatív eset ténylegesen megbukott; az RT-P0-29 egészét az (a) és az (f) eset eredménye önmagában nem zárja le. | runtime acceptance 28., 29., 30. pont, Teszt-állapot; 18. szakasz, X-16-TESZT | a runtime-teszt és a kanonikus visszaellenőrzés (RT-P0-28, RT-P0-29, RT-P0-30). |
| X-16-PRIV-HATÓKÖR | A 18. szakasz X-16-PRIV javaslatának hatóköre kizárólag az LMS-M2-05, LMS-M4-05 és LMS-M6-05 Assignment numerikus összpontja; nem vonatkozik a kvízpontszámok általános elrejtésére. Az ERT-5 szerinti M7 kapukvíz első próbálkozás utáni pontszám-megjelenítése a megoldókulcs és a helyes válaszok védelmével együtt változatlan; a többi kvíz jóváhagyott review-beállítása sem változik. A kurzusszintű „Grade letters” és a tanulói pontkönyv-beállítások regresszióját külön kell igazolni; a „Szöveges értékelés” címke kizárólag a három kijelölt Assignmentre alkalmazható, más activityre nem terjedhet át. A normál tanulói felületre vonatkozó rejtés elkülönül a GDPR szerinti sajátadat-hozzáféréstől és adatexporttól. | 18. szakasz, X-16-PRIV; manifest LMS-M4-05; runtime acceptance 29. pont | nyitott: a DPO és a jogi felelős jóváhagyása; az adatexport-út projektgazdai döntéssel nem zárható le. |
| X-16-WS | **Nyitott.** A mobil-webszolgáltatás site-szintű letiltását a projektgazda nem engedélyezi. Az LMS-gazda és a site-adminisztrátor rövid, döntésre alkalmas összehasonlítást készít a technikailag megvalósítható korlátozásokról, különös tekintettel a már kiadott tokenekre, a többi felhasználóra és a meglévő mobilfunkciókra. Olyan jogosultsági korlátozás nem állítható be, amelynek hatása a cél-Moodle-ben nem bizonyított. | 17. szakasz („Nyitott (release-kapu)”); 18. szakasz, X-16-WS; manifest LMS-M4-05 | nyitott: az összehasonlítás (LMS-gazda + site-adminisztrátor) és a webszolgáltatás-út lezárása (projektgazda + LMS-gazda + site-adminisztrátor). |
