# Projektgazdai döntési csomag — next-version M0–Z (AP-2026-10-11-01)

> **Állapot: DÖNTÉSRE VÁR.** A csomag a lezárt autopilot-futás nyitott tételeit rendezi döntésekbe. Jóváhagyást, runtime- vagy szerepköri bizonyítékot nem tartalmaz és nem állít: egy hiányzó jóváhagyás rögzítése nem a jóváhagyás megadása, és egy ajánlás nem döntés. Új review nem futott; új gyermekvédelmi, adatvédelmi, jogi, értékelési vagy pedagógiai szabályt a csomag nem vezet be.

- **Futás:** AP-2026-10-11-01 (`next-version`), ledger: `01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md` (TERMINAL, `AUTOPILOT-RESULT: OPEN_ITEMS_REMAIN`).
- **Ág és bázis:** `next-version/AP-2026-10-11-01`, bázis `main@213a4c5` (a futó pilot forrása); a csomag a `1d7b58d` állapotán készült.
- **Bemenet:** a ledger 299 `BLOCKED_HUMAN` és 31 `EVIDENCE_GATE` sora (330 kulcs), a 16 nyitott külső kapu (X-4 … X-19), a validált és a célzott QA-riportok, a lezárt döntések (`Emberi jóváhagyás szükséges.md`, `PRODUCTION-DECISIONS.md`, a `04 Audit` döntési jegyzőkönyvei) és a `RELEASE-READINESS.md` G1–G8 kapui.
- **Módszer:** öt read-only részvázlat szerepkörönként; a fő session összefésülte őket, és szkripttel ellenőrizte, hogy mind a 330 kulcs **pontosan egy** bejegyzéshez tartozik (A. függelék). Ha egy tétel több kapura hivatkozik, az elsődleges kapu a ledger-sor szövegében elsőként megnevezett kapu; a többi rész kereszthivatkozás.
- **Sorszámok:** a kánoni fájlok (GK, HUM, ADV, RR, PT, MAN, RA) sorszámai a `1d7b58d` állapotra vonatkoznak; a lecke- és kapufájl-sorszámok a findingok review-bázisára, azóta elcsúszhattak (a pontos helyet a validált riport adja).
- **Olvasási útmutató:** a döntési lista a 0–2. szakasz (összefoglaló, sorrend, egysoros áttekintő táblázat); a 3–13. szakasz bejegyzésenként a hét mezőt adja (döntés, érintett findingok és kánoni források, opciók, ajánlás, következmények, mit blokkol, ki hagyja jóvá) — ezt csak az épp tárgyalt döntéshez kell elővenni; az A. függelék a kulcsonkénti visszakereshetőség.

## 0. Összefoglaló

- **330 nyitott tétel → 141 bejegyzés:** **125 valódi döntés** és **16 szükséges bizonyíték vagy aláírás** (ezek nem nyitott kérdések: azt írják le, milyen írásos vagy runtime-bizonyíték kell kitől).
- **„Már lezárt / átvezetendő”: 0 tétel.** Egyik tételt sem fedi le szó szerint és teljesen egy lezárt döntés; a csoportok végén a részben szűkítő, újra nem nyitható lezárt korlátok szerepelnek.
- **Staging build:** a gépi `MOODLE-BUILD-VERDICT` a `5fcabea`-n ezekkel a tételekkel együtt `READY_FOR_STAGING_BUILD`; a bejegyzések a kontrollált pilotot (M0+M1 csak freeze-kivétellel), a learner release-t (G1–G8) vagy csak a későbbi fejlesztést blokkolják — bejegyzésenként a „Mit blokkol” mező.
- **Két technikai kivétel** (TECH-1: X-18, TECH-2: X-19) felhasználói lépést igényel, a pontos lépésekkel.

| Szerepkör / csoport | Döntés | Bizonyíték / aláírás | Tétel | ebből P0 | ebből P1 |
|---|---:|---:|---:|---:|---:|
| Gyermekvédelem — Memuna | 23 | 1 | 66 | 3 | 33 |
| Adatvédelem — DPO | 15 | 3 | 52 | 2 | 18 |
| Jogi értelmezés — jogi szakértő | 1 | 0 | 2 | 0 | 1 |
| Mozgalmi terminológia és ideológia — helyi felelős | 8 | 0 | 10 | 0 | 2 |
| Értékelés és completion — értékelési felelős / projektgazda | 50 | 0 | 74 | 1 | 22 |
| Szerepköri jóváhagyások (signoff) | 0 | 6 | 5 | 0 | 3 |
| Tantervi architektúra — programvezető / modulgazda | 17 | 0 | 85 | 0 | 18 |
| LMS-megvalósítás és akadálymentesség — LMS-gazda / hozzáférhetőségi gazda | 8 | 0 | 10 | 0 | 3 |
| Runtime-bizonyíték — build-felelős (G3) | 0 | 6 | 8 | 1 | 5 |
| Hang- és VO-gyártás — médiafelelős | 1 | 0 | 11 | 0 | 0 |
| Technikai kivételek | 2 | 0 | 7 | 0 | 0 |
| **Összesen** | **125** | **16** | **330** | **7** | **105** |

## 1. Javasolt döntési sorrend

1. **P0-t tartalmazó bejegyzések** (learner-release- vagy pilot-blokkoló biztonsági, adatvédelmi tételek): GYV-1, GYV-2, GYV-24, ADV-6, ADV-E1, ERT-12, RT-2.
2. **P1-et tartalmazó bejegyzések:** GYV-3, GYV-4, GYV-5, GYV-7, GYV-8, GYV-9, GYV-10, GYV-11, GYV-12, GYV-14, GYV-16, GYV-17, GYV-23, ADV-1, ADV-2, ADV-3, ADV-4, ADV-5, ADV-12, ADV-E3, JOG-1, TERM-7, TERM-8, ERT-1, ERT-2, ERT-3, ERT-9, ERT-13, ERT-14, ERT-15, ERT-18, ERT-21, ERT-24, ERT-25, ERT-26, ERT-31, ERT-32, ERT-33, ERT-38, ERT-39, ERT-40, ERT-42, ERT-43, ERT-48, SIG-1, SIG-2, SIG-6, PRG-1, PRG-2, PRG-3, PRG-4, PRG-6, PRG-8, PRG-9, PRG-12, LMS-2, LMS-3, LMS-5, RT-1, RT-4, RT-6.
3. A többi döntés szerepkörönként, egy-egy ülésben (ahol van, a csoport elején a javasolt menet).
4. A döntések átvezetése új, külön engedélyezett `/course-fix`-körben ezen az ágon; a lezárt döntések a `Emberi jóváhagyás szükséges.md` datált szakaszába kerülnek. Új tartalom: `/course-develop` (PRG-4), a terv projektgazdai jóváhagyásával.
5. A bizonyíték- és aláírás-bejegyzések (ADV-E, GYV-24, SIG, RT) a döntések átvezetése **után**, a végleges változaton; az RT-csomagok a staging buildon.

## 2. Áttekintő táblázat (egy sor = egy bejegyzés)

Az „Ajánlás” oszlop: *van* = kánonból, lezárt döntésből vagy elsődleges forrásból levezetett ajánlás; *részleges*; *nincs* = szakértői, jogi, DPO- vagy szerzői ítélet kell; *—* = bizonyíték-bejegyzés. A jóváhagyó oszlop rövidített; a teljes szerepkör a részletes bejegyzésben.

| ID | Kérdés / bizonyíték | Tétel | Max. súly | Ajánlás | Jóváhagyó (röviden) |
|---|---|---:|:---:|:---:|---|
| GYV-1 | N-3: a „mentorod azonnal bevonja a Memunát” ígéret és a mentori átnézés | 2 | P0 | részleges | Memuna (HUM-SAFE-01) |
| GYV-2 | Passzjog: érzékeny-e a gyakorlat, és mi a passz-út | 4 | P0 | részleges | Memuna + programvezető (HUM-SAFE-03) |
| GYV-3 | 1:1 helyzetek és a SAFE-7 hatóköre (HUM-SAFE-02-megfelelés) | 7 | P1 | részleges | Memuna (HUM-SAFE-02) |
| GYV-4 | Elérhetetlenségi (munkaidőn kívüli) út a krízisdobozokban | 3 | P1 | van | Memuna (HUM-SAFE-01) |
| GYV-5 | Második, 18 év feletti felkészített felnőtt a peulákon | 2 | P1 | nincs | Memuna + programvezető (HUM-SAFE-03) |
| GYV-6 | Képzői in-the-moment protokoll a peulákban | 3 | P2 | van | Memuna + programvezető (HUM-SAFE-03) |
| GYV-7 | Jelzési küszöb és címzett: Memuna vagy mentor | 4 | P1 | részleges | Memuna (HUM-SAFE-01/03) |
| GYV-8 | Terepi jelzési címzett: a helyszíni 18+ felnőtt és a képző | 2 | P1 | nincs | Memuna + programvezető |
| GYV-9 | A 18+ felelős felnőtt a peulatervben és a rubrikában (M7) | 2 | P1 | nincs | Memuna + értékelési felelős |
| GYV-10 | Kiskorú feltárása vagy krízise a kurzus AI-segédjében | 1 | P1 | nincs | Memuna + DPO/jogi felelős + programvezető |
| GYV-11 | Feltárás tárolt beadványban vagy visszajelzésben: kezelési út | 2 | P1 | részleges | Memuna + DPO |
| GYV-12 | Támogató és adattakarékossági szöveg a tárolt mezőknél és önjelző válaszoknál | 4 | P1 | van | Memuna (a HUM-SAFE-03 szerint a programvezetővel) |
| GYV-13 | Rövid Memuna-utalás: helye és formája | 5 | P2 | van | Memuna |
| GYV-14 | A 116-000 leírása (GK §3.3, §4.1) | 1 | P1 | részleges | Memuna (vétó a HUM:471 soron) |
| GYV-15 | „A részletek kiderítése a Memuna és a hatóság dolga” | 1 | P2 | nincs | Memuna |
| GYV-16 | Kirekesztés-szimuláció és szerepjáték határa | 3 | P1 | nincs | Memuna |
| GYV-17 | Tiltott zóna kimondása az M6.A-n | 1 | P1 | nincs | Memuna + a peula tartalomfelelőse |
| GYV-18 | Saját párhuzamot hívó kérdésforma az M6-ban (KAPU 12) | 2 | P2 | nincs | Memuna + értékelési felelős |
| GYV-19 | „Ne nyomozz, ne kérdezz tovább” a gyakorlat-instrukciókban | 2 | P2 | van | Memuna |
| GYV-20 | Nyilvános pozicionálás az M2.A identitás-vonalán | 1 | P2 | nincs | Memuna + DPO |
| GYV-21 | Anonimizálási korlát a szóbeli és a valós példákra | 2 | P2 | nincs | Memuna + DPO |
| GYV-22 | A kiskorú madrih önfeltárásának határa (M1.1) | 1 | P2 | van | Memuna + szakmai lektor |
| GYV-23 | Egyéni utánkövetés a belépőkvíz 1–2 | 1 | P1 | nincs | programvezető + Memuna |
| GYV-24 | G1: a Memuna írásos „átnéztem” bejegyzése (bizonyíték-kapu, X-7) | 10 | P0 | — | kizárólag a Memuna (GK §5:120) |
| ADV-1 | Szerkesztő tanári/menedzseri hozzáférés és csoportszűkítés a „csak a kijelölt mentorod látja” ígéret mögött | 3 | P1 | nincs | DPO / jogi felelős (a HUM-PRIV-01 „Jóváhagyó” sora szerint) |
| ADV-2 | Ki tartozik a „kijelölt értékelő/mentor” olvasói körbe (második és fellebbezési képző, Memuna, F-peula …) | 3 | P1 | nincs | DPO / jogi felelős az LMS-gazdával |
| ADV-3 | Önreflexiós és opcionális szabad szöveges mezők: tanuló-lokális vagy tárolt (az N-M1-04 új alkalmazási esetei) | 7 | P1 | van | projektgazda (pedagógiai szükség, completion, build-spec) |
| ADV-4 | Pontozatlan önbevallás, passz- és önjelző választás rögzítése követett H5P-ben | 6 | P1 | van | DPO / jogi felelős |
| ADV-5 | BIZT-R5: someres vagy identitás-tartalom név szerint tárolt, kötelező mezőben | 4 | P1 | nincs | DPO / jogi felelős |
| ADV-6 | A bemutatkozó fórum (FORUM-C) megőrzése, a „Bemutatkozó fal” review-ja és a pilot-tájékoztató | 1 | P0 | nincs | DPO / jogi felelős |
| ADV-7 | A peulák papír- és fizikai produktumai, fotó és személyes telefon (a HUM-PRIV-02 alkalmazása) | 5 | P2 | van | DPO / jogi felelős |
| ADV-8 | „Név nélküli” begyűjtés, ha visszaazonosítható (kis létszám, a képző ismeri a sorokat) | 2 | P2 | nincs | DPO / jogi felelős és értékelési felelős |
| ADV-9 | Valós kvuca adata a produktumokban: a Peula v2 szabályának kiterjesztése és egységes adatmondat | 4 | P2 | van | DPO és programvezető (a HUM :461 QA-szerepei) |
| ADV-10 | Moodle-on kívüli digitális eszközök: Google-sablon, közös digitális fal, QR-kódos kilépőkártya | 3 | P2 | részleges | DPO / jogi felelős és programvezető (a fiók kérdésében) |
| ADV-11 | Közös vagy tartalék eszköz kezelése az F-peulákon | 2 | P2 | nincs | LMS-gazda és DPO |
| ADV-12 | A Somer AI-végpontjának naplózása, megőrzése és hozzáférése | 1 | P1 | nincs | DPO / jogi felelős (QA: programvezető, HUM-PRIV-04) |
| ADV-13 | A hub-analitika célhoz kötöttsége (az LMS-M2-09 szabad szövegeinek átolvasása) | 1 | P2 | van | DPO |
| ADV-14 | A Z.4 videós útja: a hozzájárulás rögzítése és ellenőrzése | 1 | P2 | nincs | DPO és jogi felelős |
| ADV-15 | A Z.4 Feedback „Show analysis page” és beküldési értesítése | 1 | P2 | van | DPO és programvezető (HUM-PRIV-03) |
| ADV-E1 | A DPO írásos release-QA-ja a lezárt adatkezelési megoldásokra, activitynként (bizonyíték-kapu, G2) | 3 | P0 | — | DPO / jogi felelős (G2, tracker #2) |
| ADV-E2 | Az activity-szintű adatleltár többi mezője és a „Külön review” sorok (bizonyíték-kapu, G2 release-evidence) | 4 | P2 | — | az LMS-gazda és a privacy felelős tölti ki |
| ADV-E3 | A HUM-PRIV-04 (külső AI) írásos DPO/jogi QA-ja (bizonyíték-kapu, G2) | 1 | P1 | — | DPO / jogi felelős és programvezető (tracker #2) |
| JOG-1 | Ki tesz külső jelzést és milyen határidővel (Gyvt) | 2 | P1 | nincs | jogi szakértő |
| TERM-1 | dugma isit: kiterjed-e a Glosszárium „kerüld” szabálya a kisbetűs, megszemélyesítő alakra | 1 | P2 | nincs | projektgazda |
| TERM-2 | Az SBI „S” elemének kánoni neve: „helyzet” vagy „szituáció” | 1 | P2 | nincs | M1 modulgazda és értékelési felelős, a Glosszárium gazdájával |
| TERM-3 | „transzparens” → „átlátható” az M2.4 gyermekvédelmi szabálymondataiban | 1 | P2 | van | projektgazda, a Memuna vétójával |
| TERM-4 | Az M3.4 kánoni leckecíme (és a HUB:288 link-címkéje) | 2 | P2 | nincs | M3 modulgazda |
| TERM-5 | Az LMS-M3-05 tanulói neve | 1 | P2 | van | M3 modulgazda / implementációs felelős |
| TERM-6 | A „Leviatán – év eleji stáb” kártyacímke jelentése | 1 | P2 | nincs | M3 modulgazda |
| TERM-7 | A nem mért „saját szavaival elmondja / elmagyarázza” kompetencia: kimeneti vagy reflektív cél | 2 | P1 | részleges | projektgazda |
| TERM-8 | Mi számít „someres értéknek” az M2-kapu R2-sorában | 1 | P1 | részleges | projektgazda, értékelési felelős, helyi ideológiai felelős |
| ERT-1 | A H5P Course Presentation completionjének jelentése | 3 | P1 | van | projektgazda (build-spec gazda) |
| ERT-2 | A pontozatlan választók completion-elve: általános vagy tételes | 1 | P1 | van | projektgazda |
| ERT-3 | Üres beküldés a kötelező, nem pontozott activityknél (a HUM:457 kiterjesztése) | 2 | P1 | van | projektgazda (QUIZ-D, build-spec) |
| ERT-4 | A KAPU item-bankja / fogalmi kvíze: tanulói activity vagy szerzői pool | 2 | P2 | nincs | projektgazda + értékelési felelős |
| ERT-5 | Az éles kapukvízek Review options-e és a bukás indoklása | 2 | P2 | van | értékelési felelős |
| ERT-6 | A diagnosztikus kvízek jelzése, próbálkozásszáma és Review options-e | 4 | P2 | van | értékelési felelős + projektgazda (M5) |
| ERT-7 | A disztraktor-elv kiterjesztése a lecke-checkekre és a diagnosztikus item-bankokra | 4 | P2 | van | értékelési felelős |
| ERT-8 | Puha kapuk (M2, M4): mi váltja ki az F-peula-ajánlást, mit jelent a „kapu nem teljesült” | 2 | P2 | részleges | projektgazda |
| ERT-9 | Az éles kapus Assignment (ASSIGN-M) saját completionje: a D-h minta kiterjesztése | 1 | P1 | van | projektgazda / build-spec gazda |
| ERT-10 | Az M3 kritikus itemkörének bővítése: jóváhagyói rend és az ITEM 10 | 2 | P2 | van | projektgazda + Memuna |
| ERT-11 | M0: a belépőkvíz projektgazdai itemszövegének nyelvi javítása | 1 | P2 | van | projektgazda |
| ERT-12 | M1: valós vagy csak kitalált helyzet az LMS-M1-07 mini-SBI-ben (N-1) | 1 | P0 | van | projektgazda |
| ERT-13 | M1: az SBI kánoni hossza | 1 | P1 | van | projektgazda / modulgazda + értékelési felelős |
| ERT-14 | M1: a kész minta-SBI visszaadásának értékelői szabálya | 1 | P1 | van | értékelési felelős |
| ERT-15 | M1: B-sor ↔ hangnem-sor, kettős levonás | 1 | P1 | részleges | értékelési felelős + módszertani lektor |
| ERT-16 | M1: a KAPU:55 S-„Erős” horgonyának olvasata | 2 | P2 | nincs | értékelési felelős |
| ERT-17 | M1: a KAPU:79 zárójelének jelentése | 1 | P2 | nincs | értékelési felelős / modulgazda |
| ERT-18 | M2: mi adja az LMS-M2-03 (M2.4 H5P-C) grade-jét | 1 | P1 | részleges | projektgazda (build-spec gazda) |
| ERT-19 | M2: beleszámít-e az „ÉN” az R1 „legalább 3 kör” feltételébe | 1 | P2 | nincs | értékelési felelős |
| ERT-20 | M2: a HUB:244 határszabály-mutatójának alsó határa | 1 | P2 | részleges | modulgazda + értékelési felelős |
| ERT-21 | M3: R1 és R2 feltárás nélküli helyzetben | 2 | P1 | nincs | értékelési felelős + Memuna |
| ERT-22 | M3: az életszerűség a blokkoló R4-ben | 1 | P2 | van | projektgazda (rubrikaszint) |
| ERT-23 | M3: az M3.2 párosító kulcsa | 1 | P2 | nincs | értékelési felelős + M3 modulgazda |
| ERT-24 | M4: a Kapu 1 jelzése és a „gyenge eredmény” határa | 1 | P1 | nincs | értékelési felelős + projektgazda |
| ERT-25 | M4: az M4.3 K3 kulcsa | 1 | P1 | nincs | az M4 szerzője / projektgazda |
| ERT-26 | M5: a kapu pontozási egysége (táblázatsor vagy rubrikasor) | 3 | P1 | van | értékelési felelős + projektgazda |
| ERT-27 | M5: az R4 „gyakorlás”-horgonya ↔ GL:197 | 3 | P2 | van | értékelési felelős + módszertani lektor |
| ERT-28 | M5: az M5.2 SLIDE 8 kulcsolt opciójának szövege | 1 | P2 | nincs | M5 szerzője + értékelési felelős |
| ERT-29 | M5: az M5.4 SLIDE 6 pontozatlan önellenőrzéssé váljon-e | 2 | P2 | van | értékelési felelős, a projektgazdával |
| ERT-30 | M5: KAPU Q12 nézőpont ↔ kulcs | 1 | P2 | nincs | értékelési felelős + modulgazda |
| ERT-31 | M6: a szcenárió-kvíz kötelező completion-elem-e | 1 | P1 | nincs | projektgazda |
| ERT-32 | M6: az R4 „Oké” horgonya és a tanított minimum | 2 | P1 | nincs | értékelési felelős |
| ERT-33 | M6: társas pontozás ↔ „Ma nem pontozunk” | 1 | P1 | nincs | értékelési felelős + projektgazda |
| ERT-34 | M6: a KAPU 2 | 1 | P2 | nincs | értékelési felelős |
| ERT-35 | M6: a KAPU 4 | 1 | P2 | van | projektgazda |
| ERT-36 | M6: a KAPU 11–12 | 1 | P2 | nincs | értékelési felelős + Memuna |
| ERT-37 | M6: páros közös lap ↔ egyéni LMS-M6-05 leadás | 1 | P2 | van | értékelési felelős + M6 modulgazda |
| ERT-38 | Z: a Z.4 „Teljesítve” tartalmi mércéje | 1 | P1 | nincs | értékelési felelős |
| ERT-39 | Z: a Z.A a „Minimális teljesítés” része-e | 1 | P1 | van | programvezető + értékelési felelős |
| ERT-40 | M7: a Q11/Q14 Multi-Select részpontja és az egyetlen döntő formula | 1 | P1 | van | értékelési felelős |
| ERT-41 | M7: a hiányzó kipróbálási vállalás és AI-megjegyzés következménye (K4) | 4 | P2 | van | értékelési felelős |
| ERT-42 | M7: az R8 0-s szintje (AI-másolat és beazonosítható hanih-adat egy pontban) | 1 | P1 | nincs | értékelési felelős + DPO |
| ERT-43 | M7: az R1 2-es szintje („mérhető jel VAGY időkeret”) | 1 | P1 | nincs | értékelési felelős |
| ERT-44 | M7: mit mér az R3 | 1 | P2 | nincs | értékelési felelős + modulgazda |
| ERT-45 | M7: az R7 fix 45 perce | 1 | P2 | van | értékelési felelős |
| ERT-46 | M7: az M7.1 SLIDE 4 Fill in the Blanks elfogadott tartománya | 1 | P2 | nincs | leckegazda + értékelési felelős |
| ERT-47 | M7: a (C)-cella „átláthatóság” szava | 1 | P2 | nincs | értékelési felelős |
| ERT-48 | M7: az AI-jártassági blokk beágyazása és completion-szerepe | 1 | P1 | van | projektgazda (build-spec) + értékelési felelős + LMS-gazda (LMS-rész …) |
| ERT-49 | M7: a (C) 2 | 1 | P2 | van | értékelési felelős |
| ERT-50 | M7: a v1 operációs táblájának minimuma | 1 | P2 | nincs | értékelési felelős + modulgazda |
| SIG-1 | M0: a belépőkvíz itemszövegének utólagos értékelési QA-ja | 1 | P1 | — | értékelési felelős |
| SIG-2 | M3 és M7: a biztonságkritikus küszöb szakértői megállapítása, kalibráció, kétszemes rend | 1 | P1 | — | az item-szintű becslést a Memuna és a módszertani lektor végzi |
| SIG-3 | M3: a HUM:463 szerinti QA az M3.4:834 kritikus-téma megnevezésére | 0 | — | — | értékelési felelős + Memuna (a HUM:463 utólagos ellenőrzői) |
| SIG-4 | Szakmai lektor modul-QA-ja: M4 (HUM-PED-01) és M5 KAPU (PT §9.2 1.) | 1 | P2 | — | a szervezet által kijelölt szakmai lektor |
| SIG-5 | M5: az AI-generált médiaelemek emberi szakmai lektorálása | 1 | P2 | — | szakmai lektor |
| SIG-6 | M6: az M6.1 VID-01 és NAR-02…07 jogi és jogosultsági blokkolói (HUM-MEDIA-02) | 1 | P1 | — | jogi jóváhagyó, Memuna, DPO, szerző — nem a szakmai lektor |
| PRG-1 | Lépésidők a rögzített blokkhatárokon belül | 14 | P1 | van | az elvet a programvezető (HUM-OPS-01 jóváhagyó és vétó/QA) |
| PRG-2 | Kimondott cél/kompetencia ↔ gyakorlás és mérés | 11 | P1 | van | projektgazda (célkitűzés), a modulgazdával |
| PRG-3 | Ígéret ↔ leírt lépés a modulon belül (hub, meta, kártya-spec) | 11 | P1 | van | a szabályt a programvezető |
| PRG-4 | Egyetlen `/course-develop` csomag az új tartalomra | 9 | P1 | van | a csomagtervet a projektgazda |
| PRG-5 | Az F-peula kis létszámnál és hiányzásnál | 3 | P2 | van | programvezető + értékelési felelős (HUM 8–9 vétó/QA) |
| PRG-6 | A központi naptár szerkezeti pontjai a `SCHEDULE_TO_RESYNC`-ben | 5 | P1 | részleges | programvezető (HUM-OPS-01 jóváhagyó) |
| PRG-7 | Kohorsz- és célzott beavatkozás a diagnosztikus jelzés után | 2 | P2 | van | programvezető + értékelési felelős |
| PRG-8 | Peulák és F-peula a Moodle-kurzusban (PT:219 ↔ MAN) | 2 | P1 | van | programvezető + build-felelős |
| PRG-9 | Lecke-szintű build- és interakció-elhelyezés (három független alpont) | 3 | P1 | részleges | a) szerző/modulgazda, indok híján a hozzáférhetőségi gazda … |
| PRG-10 | Kötelező vagy opcionális | 3 | P2 | részleges | M4: modulgazda, QA: szakmai lektor |
| PRG-11 | Létszám-skálázás a peulákban | 3 | P2 | nincs | az adott modulgazda (M3.B: + Memuna) |
| PRG-12 | Az M3.B esetanyaga (fiktív esetmondat, kimaradó 4) | 2 | P1 | van | M3 modulgazda + Memuna (tartalmi QA) |
| PRG-13 | Mozgás nélküli részvétel a sarokjátékokban | 2 | P2 | van | modulgazda + hozzáférhetőségi gazda |
| PRG-14 | AI-eredetjelölés és no-AI eszköz (két független alpont) | 2 | P2 | részleges | a) tananyagfelelős / szerző |
| PRG-15 | Peula- és leckekulcsok, lezárások (három független alpont) | 3 | P2 | nincs | a) modulgazda / módszertani felelős, a Memuna bevonásával |
| PRG-16 | Szerzői szándék-megerősítések (jelentéskérdések) | 9 | P2 | részleges | az adott modulgazda (M2 bizalmas olvasatnál Memuna) |
| PRG-17 | Az M0.1 SLIDE 5 kérdése (CC-04) | 1 | P2 | nincs | projektgazda / modulgazda |
| LMS-1 | Fájlos beadási utak: elfogadott fájltípus és fájlszám (korpusz-szinten) | 1 | P2 | nincs | LMS-gazda + DPO + hozzáférhetőségi gazda (X-11) |
| LMS-2 | Az M3 Drag and Drop mellékútja | 1 | P1 | van | M3 modulgazda |
| LMS-3 | Az M5.3 késleltetett felidézési pontjának H5P-típusa és önellenőrzése (N-M5-08) | 2 | P1 | nincs | LMS-gazda + módszertani lektor/tananyagfelelős |
| LMS-4 | Az M6 játéklap 1/2/3 szintű rubrikájának Moodle-normalizálása | 1 | P2 | nincs | LMS-gazda + értékelési felelős |
| LMS-5 | Az M7.3 Checklist-aktivitás formája, completionje és tárolása (K18) | 2 | P1 | nincs | projektgazda + LMS-gazda/Moodle-adminisztrátor + DPO |
| LMS-6 | Az M7.4 SLIDE 4 pontozatlan fókuszválasztójának H5P-útja | 1 | P2 | nincs | LMS-gazda |
| LMS-7 | Az M7.2-DIA-01 alt-szövege: a PT:221 rövid vagy a lecke részletes változata | 1 | P2 | van | projektgazda |
| LMS-8 | A kurzus AI-segédjének Moodle-formája, helye és hozzáférési feltétele | 1 | P2 | nincs | programvezető + Moodle-adminisztrátor |
| RT-1 | „Segítség és kapcsolatok” blokk: kitöltés és megjelenés | 1 | P1 | — | LMS-gazda (megjelenés) |
| RT-2 | M0+M1: completion, unlock, kapumechanika, próbálkozások, a SLIDE 5 adatmentessége | 3 | P0 | — | LMS-gazda / build-felelős (G3b) |
| RT-3 | M4 célverziós tesztcsomag | 1 | P2 | — | LMS-gazda (G3b), hozzáférhetőségi gazda (G5b) |
| RT-4 | M6.4 Branching Scenario | 1 | P1 | — | LMS-gazda (G3b), hozzáférhetőségi gazda (G5b) |
| RT-5 | Az AI-segéd adatkezelése és a no-AI completion (M7) | 1 | P2 | — | LMS-gazda (G3b) |
| RT-6 | Az M7 párosításainak húzásmentessége | 1 | P1 | — | LMS-gazda |
| VO-1 | 3 | 11 | P2 | van | médiafelelős / VO-gazda (X-17) |
| TECH-1 | A „minijelenet” gépi őr hatóköre (X-18) | 3 | P2 | van | projektgazda (eszköz- és governance-változás) |
| TECH-2 | Az M6.1 és az M6.2 átnevezése a `tools/` útvonalkulcsaival (X-19) | 4 | P2 | van | a felhasználó (az átnevezési commit futtatása) + projektgazda (a …) |

## 3. Gyermekvédelem — Memuna

> Forrás: `AUTOPILOT-LEDGER.md` (1d7b58d, AP-2026-10-11-01), a validált riportok 3–4. szakasza és a célzott
> QA-riportok. Új review nem futott, jóváhagyást vagy bizonyítékot ez a szakasz nem állít. Rövidítések: GK =
> `Gyermekvédelem – release gate.md`, HUM = `Emberi jóváhagyás szükséges.md`, ADV = `Adatvédelem – tanulói adatok és
> AI.md`, RR = `RELEASE-READINESS.md`, PT = `Program terv.md`. A kánoni sorszámok a mai HEAD-re vonatkoznak, a lecke-
> és KAPU-sorszámok a findingok review-bázisára (azóta elcsúszhattak; pl. Z.3:300 ma :306).
>
> **Mit blokkol – közös keret:** a `MOODLE-BUILD-VERDICT` READY_FOR_STAGING_BUILD; **egyik tétel sem blokkolja a staging
> buildet** (GK §2:21, HUM:569). „Learner release” = az érintett modul megnyitása valódi madrihoknak (kontrollált pilot
> vagy később) a G1 FINAL_RELEASE_QA-n át: a Memuna végső átnézése (GYV-24) a döntések nélkül nem zárható le értelmesen.
> P0/P1: a riportok szerint learner-release-blokkoló; P2: a G1-átnézés bemenete, önálló blokkolónak a kánon nem jelöli.
> A madrih maga is lehet kiskorú: egyik opció sem adhat neki egyedüli felelősséget vagy hatósági szerepet (GK §4:59–60).

**Javasolt menet:** (1) egy Memuna-ülés a GYV-1…GYV-23-ra, társdöntőkkel: programvezető (GYV-2, 5, 6, 7, 8, 23),
DPO (GYV-1 vétó, 10, 11, 20, 21, 23), értékelési felelős (GYV-2, 9, 11, 18), szakmai lektor (GYV-22), projektgazda
(GYV-2 build-spec, GYV-3 ITEM 4 kulcsa, GYV-9 rubrikaszint, GYV-18 kulcs); (2) átvezetés `/course-fix`-szel; (3) GYV-24:
a Memuna „átnéztem”-je a végső verzióra. Elsőként: a két P0 (GYV-1, GYV-2), utána a SAFE-7 (GYV-3) és az
elérhetetlenségi csomag (GYV-4).

### GYV-1 — N-3: a „mentorod azonnal bevonja a Memunát” ígéret és a mentori átnézés
- **Döntés:** Kötelező-e (és milyen határidővel) az M2 tárolt szabad szöveges válaszainak mentori átolvasása (LMS-M2-09; a KAPU §D sablonja, LMS-M2-05), és maradhat-e az M2.4:37 és a KAPU §D:201 „a mentorod azonnal bevonja a Memunát” ígérete a KAPU:24 megerősítési határideje mellett?
- **Érintett findingok:** M2:BIZT-G2-1 (P0), M2:BIZT-G1-1 (P1). **Kánon:** GK §4.1:84 (eset nem kerül beadandóba); ADV §11:241 („Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd…”; a szöveges válaszokat „csak akkor nézi meg, ha ténylegesen szükséges”); GK §4:56; HUM-SAFE-01 (HUM:29–31).
- **Opciók:** (a) kötelező, határidős mentori átnézés, beküldési értesítéssel; az ígéret időkorláttal marad; (b) nincs kötelező átnézés: az „azonnal bevonja” ígéret kikerül, a mező mellé az ADV §11:241 mondata kerül; (c) átnézés csak a KAPU-beadványnál (LMS-M2-05), az LMS-M2-09-nél a (b). A „nem jelent feltétel nélküli titoktartást” védelem mindegyikben marad.
- **Ajánlás:** a kánon iránya a (b) vagy a (c): az ADV §11:241 és a GK §4.1:84 a valós jelzést a tanulási feladaton kívülre tereli, az ADV §11 csak „ha ténylegesen szükséges” olvasást ígér, így az „azonnal” kötelező, határidős átnézés nélkül nem tartható. A választás és az (a) határideje a Memuna döntése, DPO-vétóval.
- **Következmények:** biztonság: a mai ígéret hamis biztonságérzetet ad (P0); adatvédelem: az (a) új, rendszeres olvasási célt nyit (rokon: M2:BIZT-G1-8, X-4); megvalósítás: értesítési beállítás, mentori kapacitás (1:8).
- **Mit blokkol:** az M2 learner release-ét (P0).
- **Ki hagyja jóvá:** Memuna (HUM-SAFE-01); vétó/QA: DPO / jogi felelős.

### GYV-2 — Passzjog: érzékeny-e a gyakorlat, és mi a passz-út
- **Döntés:** Érzékeny gyakorlat-e a GK §4:61 / HUM-SAFE-03 értelmében az alábbi négy elem, és ha igen, milyen passz- vagy alternatív út kell, hogyan hat a kötelező mezőre, a completionre és a kapus belépőre?
- **Érintett findingok:** M2:BIZT-G2-2 (P0; M2.4 SLIDE 5 kötelező krízis-esetválasza, az M2.4:39 „Mondhatsz passzt”, MAN:57 nyitott); M3:PED-G2-1 (P1; M3.4 SLIDE 4 és 6, a SLIDE 4 kapus belépő); M3:IMPL-G2-5 (P1; látszódjon-e a szcenárió címe a P1–P4 passz-választón); M4:BIZT-G2-10 (P2; M4.B 4.1, 4.2, 4.4/1, csak a :326 mondata vehető át). **Kánon:** GK §4:61–62, §4.3:104; HUM-SAFE-03 (HUM:72); SAFE-1 (HUM:566–567, csak az M3.3-ra).
- **Opciók:** (a) nem érzékeny, nincs passz-út; (b) érzékeny: passz a meglévő elemen belül (pl. elfogadott „passz” válasz a Required mezőben, completion-semlegesen, a SAFE-1 elveinek mintájára); (c) érzékeny: egyenértékű, nem személyes alternatív feladat; (d) a mező opcionális lesz (completion-változás, build-spec).
- **Ajánlás:** részben kánonból. Az M2.4 SLIDE 5 maga ígér passzt (M2.4:39, HUM-SAFE-03 blokk), ezért a „Required, passz nélkül” állapot nem maradhat; a (b)/(c)/(d) közti választás a Memuna és a programvezető döntése. Az M3:IMPL-G2-5-nél igen: a passzjog tájékozott választást feltételez, a cím meglévő szöveg, a §7.1 nem változik (QA: a cím maga ne legyen megterhelő). Az M3.4 és az M4.B érzékenységéről ajánlás nincs, az a Memuna ítélete.
- **Következmények:** értékelés: a passz nem ronthatja a kapus belépőt (M3.4 SLIDE 4), MAN:57 completion-szemantikája; biztonság: a P0 tétel kötelező krízisválaszt kényszerít ki; megvalósítás: H5P „Show content title”, Required-beállítás.
- **Mit blokkol:** M2 (P0) és M3 (P1) learner release; az M4.B a G1 bemenete.
- **Ki hagyja jóvá:** Memuna + programvezető (HUM-SAFE-03); kapus belépő: értékelési felelős; MAN:57 és az M3.3 §7.1: projektgazda (build-spec gazda), QA: Memuna.

### GYV-3 — 1:1 helyzetek és a SAFE-7 hatóköre (HUM-SAFE-02-megfelelés)
- **Döntés:** Kiterjed-e a Memuna SAFE-7 QA-ja (ma: az M3.3 S1 23:15-ös bejövő privát üzenete és a ✅ első válasz) a többi 1:1 helyre, és helyenként megfelel-e a szöveg és a kulcs a HUM-SAFE-02-nek, a (a)–(c) kivételeknek és a kiskorú madrih szerephatárának?
- **Érintett findingok:** M0:BIZT-3 (M0.4 SLIDE 3 2. helyzet); M2:BIZT-G2-4 (M2.4:193, :206–209, :653); M3:BIZT-G1-1 (KAPU ITEM 4: (a) SAFE-7, (b) a „Nem hagyom egyedül” a kiskorú madrih szerepén belül van-e; a (c) a GYV-4-ben); M3:BIZT-G2-3 (M3.3:548–552 akut doboza ↔ a (b) kivétel); M3:BIZT-G3-4 (M3.B 1. esetkártya, a megoldójegyzet csatornája, MUNK-03); M3:BIZT-G2-8 (M3.4:363, :590 ↔ :358); M4:BIZT-G2-1 (M4.A:437–442, MUNK-02: képzői 1:1 erős szorongásnál). **Kánon:** GK §4.2:94, :97, :98; §4:59–60, :65–66; §6:152–153; HUM-SAFE-02 (HUM:51–53); SAFE-7 (HUM:569, :572).
- **Opciók:** (a) a QA kiterjed mind a hét helyre, egy körben, helyenkénti verdikttel; (b) csak az M3.3 S1; (c) kiterjesztés, és a nem megfelelő helyek javítása a Memuna szövegével.
- **Ajánlás:** a hatókörre az (a), mert a GK §6:152 (human-qa) eleve „a négyszemközti (1:1) helyzetek tananyagát és kvízkulcsait” kéri a HUM-SAFE-02-vel egyeztetni, nem csak az M3.3 S1-et. A helyenkénti megfelelésről ajánlás nincs, az a Memuna ítélete. Addig a ✅ és a kulcs nem változik (HUM:569).
- **Következmények:** értékelés: az M3 KAPU ITEM 4 kritikus item, kulcsa csak projektgazdai döntéssel változhat; biztonság: kiskorúnak küldött személyes privát üzenet soha nem „helyes” válasz (GK §4.2:97); megvalósítás: M0-szövegváltozás a futó pilotban csak freeze-kivétellel.
- **Mit blokkol:** learner release (HUM:569: „learner release előtt kötelező lezárni”); az M0-hely a futó M0+M1 pilotban feltételes pilot-blokkoló.
- **Ki hagyja jóvá:** Memuna (HUM-SAFE-02); az ITEM 4 kulcsa: projektgazda.

### GYV-4 — Elérhetetlenségi (munkaidőn kívüli) út a krízisdobozokban
- **Döntés:** Bekerüljön-e szerepnévvel a GK §4.1 tartalék útja (helyettes: Ros Hinuh; ha egyikük sem elérhető vagy munkaidőn kívül: 116-111 / 116-000, közvetlen veszélyben 112) a megnevezett krízisdobozokba és visszajelzésekbe?
- **Érintett findingok:** M2:BIZT-G2-5 (M2.4 SLIDE 1/5); M2:BIZT-G1-2 (M2 KAPU 5. item visszajelzése, :113; a ✅ és az opciók nem változnak); M3:BIZT-G2-4 (M3.3 SLIDE 2, :309 ← M3.3:751). Ide futó alkérdések: M3:BIZT-G1-1 (c), M6:BIZT-G1-1 (b), M7:BIZT-G3-4 (DUPLICATE; M7.F:35, :87, :305, M7.B:93, :632). **Kánon:** GK §4.1:86–88, §3.3:43–49; HUM-SAFE-01 (HUM:30).
- **Opciók:** (a) egységes, rövid, szerepnevű mondat minden felsorolt helyre, mutatóval a „Segítség és kapcsolatok” blokkra; (b) csak a blokkra mutató utalás (mai állapot); (c) csak a munkaidőn kívül releváns helyekre (23:15-ös helyzet, M7.F hétfő 18:00).
- **Ajánlás:** az (a). A tartalom lezárt (HUM-SAFE-01 kontaktdöntés, HUM:30), a GK §4.1:87 szerint a központi szám hétköznap 10–18 él, és „munkaidőn kívül és közvetlen veszélyben a 112, illetve a Kék Vonal az út”; név és telefonszám nélkül (GK §4.1:88). A helyeket a Memuna hagyja jóvá.
- **Következmények:** biztonság: enélkül munkaidőn kívül a tanuló egyetlen útja egy nem elérhető kontakt; megvalósítás: VO-t érintő helyen hanggyártási úton (X-17); a ✅-ok nem változnak.
- **Mit blokkol:** M2 és M3 learner release (P1); az M6/M7-helyek a G1 bemenetei.
- **Ki hagyja jóvá:** Memuna (HUM-SAFE-01; vétó/QA: a Memuna és a helyettese).

### GYV-5 — Második, 18 év feletti felkészített felnőtt a peulákon
- **Döntés:** Kötelező-e második, 18 év feletti felkészített felnőtt a képzés peuláin (M0.A, M2.A/B/F, M3.B/F, M4.A, M6.A, M7.F, Z.A), vagy mi az egyképzős út, ha egy felkavart kiskorú mellé felnőtt kell (GK §4:64), és közben a kör folytatódik?
- **Érintett findingok:** M0:BIZT-9, M2:BIZT-G3-2. Ide olvadt: M3:BIZT-G3-2, M6:BIZT-G3-1, Z:BIZT-G1-6, az M7:BIZT-G3-2 második felnőttes része és az M4:BIZT-G2-9 „ki a felnőtt” alkérdése. **Kánon:** GK §4:60, :64; HUM-SAFE-03 (HUM:72–73: „legalább egy” felnőtt); HUM-SAFE-05 (HUM:107).
- **Opciók:** (a) minden peulán kötelező; (b) csak az érzékeny peulákon (M0.A, M2.A, M3.B, M6.A, Z.A); (c) egyképzős út: a helyszínen azonnal elérhető második felelős (a GK §4:60 mintájára) és a kör felfüggesztése; (d) egy képző marad, a képzőképzés (HUM-SAFE-05) kezeli.
- **Ajánlás:** nincs, ez a Memuna és a programvezető ítélete: személyzeti szabály, a HUM-SAFE-03 legalább egy felnőttet ír elő, kettőt nem. Kockázat: egy képzővel a GK §4:64 minimuma és a kör folytatása (M0.A:132–133, M2.A:280) egyszerre nem teljesíthető.
- **Következmények:** megvalósítás: stábigény, HUM-OPS-02 kapacitás; a (c) új tartalmi lépést kér; biztonság.
- **Mit blokkol:** a peulák élesítését (P1). Az M0.A-ra a személyzeti döntés operatívan most is meghozható (M0 riport §3).
- **Ki hagyja jóvá:** Memuna + programvezető (HUM-SAFE-03; GK §5:120).

### GYV-6 — Képzői in-the-moment protokoll a peulákban
- **Döntés:** Szó szerint bekerüljön-e a peulák képzői utasításaiba a HUM-SAFE-03 facilitátori minimuma (GK §4:63–64), „felkavart” állapot-e a szereplési szorongás, és mi a Z.A helyes lépéssorrendje?
- **Érintett findingok:** M1:BIZT-G3-2 (M1.A:503–505, M1.B:389–391, M1.F:107; ide olvadt: M3:BIZT-G3-3 az M3.A:111, :561 és M3.F:99, :552 helyekkel, és M7:BIZT-G3-2 az M7.A:56, :518, M7.B:93 helyekkel); M4:BIZT-G2-9 (M4.A:58, :390); Z:NYELV-G1-14 (Z.A:53: előbb a Memuna, aztán odalépés ↔ :226: odalépés, Memuna nélkül). **Kánon:** GK §4:63–64, §4.1:74–78; HUM-SAFE-03 (HUM:72), HUM-SAFE-05.
- **Opciók:** (a) a GK §4:63–64 két mondata szó szerint minden peula képzői utasításába (az M2.F:73 már így van); (b) elég a képzőképzés, a peulaszöveg marad; (c) az (a), és a szereplési szorongás látható jele is „felkavart”. Z.A: (i) a GK §4.1 sorrendje (meghallgatás, majd gyermekvédelmi aggálynál azonnal a Memuna), (ii) a :53 változat, (iii) a :226 változat.
- **Ajánlás:** az (a), a Z.A-nál az (i): kánoni szöveg és kánoni sorrend, új szabály nélkül, az M2.F:73 mintája megvan. A szereplési szorongás besorolása a Memuna ítélete.
- **Következmények:** biztonság; megvalósítás: több peula képzői sora, a spec-helyeken build; a „ki a felnőtt” kérdés a GYV-5.
- **Mit blokkol:** a G1 bemenete (P2).
- **Ki hagyja jóvá:** Memuna + programvezető (HUM-SAFE-03).

### GYV-7 — Jelzési küszöb és címzett: Memuna vagy mentor
- **Döntés:** A nem egyértelműen gyermekvédelmi helyzetekben (csoportchat-szívatás, mély szorongás, veszélyeztetettség nélküli gyász, saját érintettség) kötelező-e a Memuna bevonása, vagy a mentor marad a címzett (GK §4.1:81)?
- **Érintett findingok:** M0:BIZT-5 (M0.2:265 mindig Memuna ↔ M0.4:307 és hub:241 „szükség esetén”); M5:BIZT-G1-1 (M5.2:313 szorongás-beszélgetés passz nélkül, automatikus Memuna mély szorongásnál; a passz-rész a GYV-2 elve szerint); M6:BIZT-G2-4 (M6.2:777–779); M7:BIZT-G3-1 (M7.F:390 és MUNK-02 „a Memunát vonom be” ↔ M7.F:87, M7.B:93, :632). **Kánon:** GK §4.1:80–81, §4:63, §4.3:104; HUM-SAFE-03 (HUM:73: bizalmas kontakt a mentor vagy a Memuna); M6-NY-D1 (2026-10-04: „A jelzési utat a feltárás indítja. A kibillenést a meglévő M0.A mini-protokoll kezeli.”), M6-NY-D27.
- **Opciók:** (a) mindenhol kettős szerkezet: feltárás vagy veszélyeztetettség esetén azonnal a Memuna, egyéb érzelmi nehézségnél a mentor (M0.A mini-protokoll), a Memuna választható kontakt; (b) alacsony küszöb, minden ilyen helyzet Memuna-jelzés; (c) helyenként külön küszöb.
- **Ajánlás:** az M5-, M6- és M7-helyeken az (a): ezt adja a lezárt M6-NY-D1 elve és a HUM-SAFE-03 választási joga; a túleszkaláció a tanuló tudta nélkül jelzéssé tenné a saját érintettséget. A D1 kiterjesztése új alkalmazás, a Memuna hagyja jóvá. Az M0:BIZT-5-nél (zaklatás, kortárs bántalmazás küszöbe) ajánlás nincs, az a Memuna ítélete: a GK §4.1:80 a zaklatást a Memuna körébe sorolja.
- **Következmények:** biztonság (túl- vagy aluleszkaláció); adatvédelem (a jelzés adattovábbítás); értékelés: az M0 belépőkvíz kulcsa döntés nélkül nem változik.
- **Mit blokkol:** az M5 learner release-ét (P1); a többi a G1 bemenete (P2).
- **Ki hagyja jóvá:** Memuna (HUM-SAFE-01/03); az M5-nél a programvezetővel.

### GYV-8 — Terepi jelzési címzett: a helyszíni 18+ felnőtt és a képző
- **Döntés:** Megnevezheti-e a tananyag terepi címzettként a helyszíni, 18 év feletti felelős felnőttet (M6 KAPU:352 P1, M6.B játéklap „kit hívsz”) és a képzőt (Z.3:300, kiskorú madrih: „nem vezetek éles foglalkozást, hanem jelzem a képzőnek”) a Memuna mellett vagy előtt?
- **Érintett findingok:** M6:BIZT-G1-1 (ide olvadt: M6:BIZT-G3-4; a küszöb lezárt: M6-NY-D3, D27; a (b) a GYV-4-ben, a (c) a GYV-24-ben); Z:BIZT-G1-1. **Kánon:** GK §4:60 (a gyermekvédelmi felelősség a helyszíni 18+ felnőtté), §4.1:81 (a címzett mindig a Memuna, „nem »egy felnőtt«”), §4.1:77; HUM-SAFE-03 (HUM:72–73).
- **Opciók:** (a) kettős: azonnal a helyszíni 18+ felnőtt, és a 4. lépés szerint a Memuna; (b) csak a Memuna; (c) a Z.3-nál: a felügyeleti hiány (nincs jelen 18+ felnőtt) nem gyermekvédelmi ügy, címzettje a képző vagy a programvezető, és ez a kánonba kerül.
- **Ajánlás:** nincs, ez a Memuna és a programvezető ítélete. A GK §4:60 és §4.1:81 között a kánonban nincs feloldás; a Z.3:300 a HUM-SAFE-03 felügyeleti szabályának betartatását írja le, nem ügyjelzést.
- **Következmények:** biztonság (késlekedő vagy rossz címzett); megvalósítás: a KAPU P1 és a játéklap egy döntéssel változik.
- **Mit blokkol:** az M6 és a Z learner release-ét (P1).
- **Ki hagyja jóvá:** Memuna + programvezető.

### GYV-9 — A 18+ felelős felnőtt a peulatervben és a rubrikában (M7)
- **Döntés:** Kérje-e az M7 KAPU R4 2–3. szintje (KAPU:311–312) a 18 év feletti felelős felnőtt megnevezését, és kerüljön-e erről mondat az M7.4 operációs mintatáblája alá (:769–778)?
- **Érintett findingok:** M7:BIZT-G1-2 (P1), M7:PED-G2-4 (P2; ide olvadt: M7:BIZT-G2-8). **Kánon:** HUM-SAFE-03 (HUM:72); GK §4:60; az M7 KAPU (C) 5. sora (:386) és a Q9 (:164, :171) már kéri; a MUNK-01 spec (:808) új szöveget kizár.
- **Opciók:** (a) R4 2–3. szint és mintatábla-mondat (spec-módosítás, build); (b) csak a mintatábla-mondat; (c) marad, a (C) sor és a Q9 lefedi.
- **Ajánlás:** nincs, ez a Memuna és az értékelési felelős ítélete: blokkoló rubrikasorról van szó, a rubrikaszint csak döntéssel változik. Tény: a KAPU ma belsőleg eltér (a (C) sor és a Q9 kéri, az R4 nem).
- **Következmények:** értékelés (blokkoló sor); biztonság; megvalósítás (MUNK-01 spec, build).
- **Mit blokkol:** az M7 learner release-ét (P1).
- **Ki hagyja jóvá:** Memuna + értékelési felelős; rubrikaszint: projektgazda.

### GYV-10 — Kiskorú feltárása vagy krízise a kurzus AI-segédjében
- **Döntés:** Ha egy (akár kiskorú) madrih feltárást, krízist vagy red flaget ír a kurzus AI-segédjébe, kell-e szerveroldali szűrés, rögzített válaszút (Memuna, „Segítség és kapcsolatok”, 112), eszkaláció és monitorozás?
- **Érintett findingok:** M7:BIZT-G1-4 (ide olvadt: M7:BIZT-G2-1; M7.2:24, :107, :988, M7.4:869–871). **Kánon:** ADV §7:187–188 (csak a delegálást tiltja); HUM-PRIV-04 (HUM:176); GK §4.1, §3.3.
- **Opciók:** (a) szűrés és rögzített válaszút, monitorozás nélkül; (b) az (a), eszkalációval és monitorozással (ez maga is adatkezelés); (c) ilyen bevitelre az AI-segéd letilt, vagy kiskorúnak nem érhető el; (d) marad a „ne AI-t kérdezz” mondat.
- **Ajánlás:** nincs, ez a Memuna, a DPO/jogi felelős és a programvezető együttes ítélete. A „ne AI-t kérdezz” mondat nem törölhető. Kockázat: rögzített válaszút nélkül a modell rögtönöz egy krízisbevitelre.
- **Következmények:** adatvédelem (monitorozás, naplózás: rokon M7:BIZT-G2-3, X-4); megvalósítás: az AI-segéd formája az M7:IMPL-G3-8 (X-11).
- **Mit blokkol:** az M7 AI-segédjét és az M7 learner release-ét (P1); a DPO-rész az X-4/X-12-ben.
- **Ki hagyja jóvá:** Memuna + DPO/jogi felelős + programvezető.

### GYV-11 — Feltárás tárolt beadványban vagy visszajelzésben: kezelési út
- **Döntés:** Ha egy tárolt kapubeadvány (M1 KAPU:27; M3-többlet: KAPU:309, N-9) vagy a Z.4 Feedback-ága (Z.4:201, :370) gyermekvédelmi feltárást tartalmaz, ki veszi ki és hová, mi lesz a kapueredménnyel, és mi az alternatív beadási út?
- **Érintett findingok:** M1:BIZT-G2-6 (ide olvadt: M3:BIZT-G1-3); Z:BIZT-G1-2 (objektív része, a Z:BIZT-G1-2.obj, FIXED). **Kánon:** GK §4.1:84–85 (az ügy dokumentációja nem Moodle-ben, hanem a korlátozott incidensnyilvántartásban); ADV §11:241, ADV:75; HUM-PRIV-03 (Z.4 anonimitás).
- **Opciók:** (a) a Memuna vagy a helyettes azonnal kiveszi és az incidensnyilvántartásba viszi, a tanuló feltárásmentes változatot ad be, a kapueredmény addig függő; (b) a beadvány marad, csak megjelölik, az értékelés a feltárásos részt figyelmen kívül hagyja; (c) az anonim Z.4 Feedbacknél: kánoni mondat a beküldés előtt, összesített olvasás azonosítás nélkül.
- **Ajánlás:** részben kánonból: az eset nem maradhat Moodle-dokumentációként (GK §4.1:84–85). A kivétel módjáról, a megőrzésről és törlésről, valamint a kapueredményről ajánlás nincs, az a Memuna, a DPO és az értékelési felelős ítélete.
- **Következmények:** adatvédelem (törlés, megőrzés, hozzáférés); értékelés (kapueredmény, N-9 alternatív út); biztonság.
- **Mit blokkol:** a Z learner release-ét (P1); az M1/M3-rész a G1 bemenete.
- **Ki hagyja jóvá:** Memuna + DPO; kapueredmény: értékelési felelős; N-9: értékelési felelős + programvezető, Memuna-vétóval.

### GYV-12 — Támogató és adattakarékossági szöveg a tárolt mezőknél és önjelző válaszoknál
- **Döntés:** Mi álljon a tárolt mezők és az önjelző kérdések mellett: az egyedi „ha nagyon nehéz helyzet” szöveg, a HUM-SAFE-03 blokk, az ADV §11:241 mondata vagy a meglévő biztonsági doboz, új blokk nélkül (GK §4.3:102)?
- **Érintett findingok:** M1:BIZT-G2-10 (M1.3:913–915, M1.4:514; az M1.4:516 Memuna-mondata nem törölhető); M1:BIZT-G2-3 (objektív, kész blokk: az ADV §11:241 mondata az M1.3-ba, az N-1 (M1:BIZT-G2-1, X-6) és a BIZT-G2-10 döntésével egy lépésben); M2:IMPL-G2-7 (az M2.4 SLIDE 5 ⚠️/🆘 doboza az LMS-M2-09 mezőhöz); M2:PED-G2-7 (támogató visszajelzés az M2.4:340 „túl sok” válaszra; ide tartozik az M2:BIZT-G2-7 Memuna-alkérdése). **Kánon:** GK §4.3:102, :104; §4.1:84; ADV §11:241; HUM-SAFE-03 (HUM:73).
- **Opciók:** M1: (a) az egyedi szöveg helyére az ADV §11:241 mondata (feladatszintű adattakarékosság); (b) az egyedi szöveg kikerül, és a már ott álló §4.3 blokk marad egyedül (M1.3:917, M1.4:518); (c) marad. M2: (a) a meglévő doboz szó szerint a mezőhöz; (b) csak mutató a meglévő blokkra vagy a „Segítség és kapcsolatok” blokkra; (c) új támogató visszajelzés.
- **Ajánlás:** M1-nél az (a), az N-1 (X-6) után egy szerkesztésben: a §4.3 blokk már a mező mellett áll, a GK §4.3:102 ad hoc támogató szöveget nem hagy mellette, a „finomíthatsz” forma pedig a nehéz helyzet beírására biztat. M2:IMPL-G2-7-nél az (a), meglévő szöveggel. M2:PED-G2-7-nél a (b), mert a GK §4.3:102 szerint máshol nem kerül be új blokk. A Memuna hagyja jóvá.
- **Következmények:** adatvédelem (kevesebb azonosítható beírt eset); biztonság; megvalósítás: egy szerkesztési kör az N-1 után, a spec-helyeken build.
- **Mit blokkol:** az M1:BIZT-G2-3 (P1) az M1 learner release-ét; a többi a G1 bemenete.
- **Ki hagyja jóvá:** Memuna (a HUM-SAFE-03 szerint a programvezetővel).

### GYV-13 — Rövid Memuna-utalás: helye és formája
- **Döntés:** Kerüljön-e a GK §4.1:82 rövid utalása („azonnal vond be a Memunát”) a HUM-SAFE-01 forráslistáján kívüli helyekre, és kötelező-e benne az „azonnal” és a GK §4.1:80 első előfordulási formulája?
- **Érintett findingok:** M1:BIZT-G1-4 (M1.1 SLIDE 5, az írás előtt, a Z.2:307 mintájára; „csak nálad marad” az RT-P0-24-ig tilos, HUM:587–588); M1:BIZT-G3-9 (M1.B 4.4.2 terepi SBI-vállalás; az M1.4:516 kimondja); M3:BIZT-G1-10 (M3.1:280 doboz, mert az M3.3 csak az M3.A után nyílik); M7:BIZT-G3-3 (M7.A :56, :518; utána csak az M7.B:93 szó szerint); M2:QA-BIZT-1 (M2.A:176 és a :122 spec „ilyenkor a Memunát vonjuk be”, = M2:BIZT-G3-1 (b)). Ide futó alkérdés: M2:BIZT-G3-5 (b). **Kánon:** GK §4.1:77, :80–82; §4.3:102; HUM-SAFE-01 forráslista (HUM:34); HUM 8. „Storming…” sor (HUM:470).
- **Opciók:** (a) a GK §4.1:82 utalása szó szerint mind a négy helyre (az M1.1-nél a Z.2:307 mondata), az M2.A-ban „ilyenkor azonnal bevonjuk a Memunát”; (b) csak a terepi, valós kvucás helyekre (M1.B, M7.A); (c) marad.
- **Ajánlás:** az (a): kánoni rövid forma, új szabály és új „ha téged is érint” blokk nélkül; a 4. lépés kulcsszava az „azonnal” (GK §4.1:77). Hogy a GK §4.1:80 formulája kötelező-e a poszter műfajában, azt a Memuna dönti el.
- **Következmények:** biztonság (a jelzési út mindenhol látszik); megvalósítás: kis szövegváltozások, az M2.A-ban spec és build.
- **Mit blokkol:** a G1 bemenete (mind P2).
- **Ki hagyja jóvá:** Memuna; az M3.1-nél a modulgazdával (HUM:470).

### GYV-14 — A 116-000 leírása (GK §3.3, §4.1)
- **Döntés:** Módosuljon-e a GK §3.3:47 és §4.1 116-000-leírása („nem általános »szülői vonal«”) a szolgáltató saját, aktuális leírása szerint (vétónál a HUM 8. szakasz „Segélyvonalak” sora REOPENED)?
- **Érintett findingok:** M3:BIZT-G2-2 (utána az M3.3:860, a KAPU:365 és az M3:IMPL-G3-3 követi). **Kánon:** GK §3.3:45–50, §6:150, §7:164; HUM:471.
- **Opciók:** (a) marad, a HUM:471 sor él; (b) a Memuna vétója után REOPENED, a GK leírása a Kék Vonal aktuális szövegéhez igazodik, a tananyag követi.
- **Ajánlás:** a Memuna a release-napi segélyvonal-ellenőrzéssel (GK §6:150) egy lépésben döntsön, a Kék Vonal saját aktuális leírásából. A GK §3.3:45 maga a „jelenlegi szolgáltatásleírást” teszi mércévé, ezért eltérés esetén a (b). A tartalmi ítélet a Memunáé.
- **Következmények:** biztonság (helyes vonal a helyes helyzethez); megvalósítás: három hely és az IMPL-G3-3 egy lépésben.
- **Mit blokkol:** az M3 learner release-ét (P1; GK §6:150 release-evidence).
- **Ki hagyja jóvá:** Memuna (vétó a HUM:471 soron).

### GYV-15 — „A részletek kiderítése a Memuna és a hatóság dolga”
- **Döntés:** Maradhat-e ez a fordulat (M3.3:697, :698, :705; KAPU:243, :248) az önsértés-esetnél is, amíg a jogi minősítés nyitott?
- **Érintett findingok:** M3:BIZT-G2-9. **Kánon:** GK §3.1:33 (nyitott jogi alkalmazási kérdés), §3.2:39, §4:57–58. A „Meghallgatni szabad – kihallgatni nem” és a „nem a tiéd” marad.
- **Opciók:** (a) marad; (b) „a Memuna dolga”, a hatóság kimarad; (c) „a Memuna és – ha szükséges – a hivatalos szervek dolga”.
- **Ajánlás:** nincs, ez a Memuna ítélete; a jogi rész a jogi szakértőé (X-15).
- **Következmények:** biztonság és jogi pontosság; az S3-SAFE doboz a SAFE-1 miatt döntés nélkül nem változik.
- **Mit blokkol:** a G1 bemenete (P2).
- **Ki hagyja jóvá:** Memuna; jogi kérdésben jogi szakértő (lásd X-15).

### GYV-16 — Kirekesztés-szimuláció és szerepjáték határa
- **Döntés:** Kiterjed-e a kirekesztés-szimuláció tilalma (az M6 biztonsági minimuma: nincs kirekesztés-szimuláció, nincs kirekesztett vagy kirekesztő szerep) az M6.4:772 „szerepjáték társadalmi helyzetekkel” opcióra (és az 5D-J-re), valamint az M3.A csoportszobrának „Van-e valaki külön?” pozíciójára?
- **Érintett findingok:** M6:BIZT-G2-2 (P1); M6:BIZT-G2-1 (a második betoldás az M6:BIZT-G2-2 szövegével; az objektív rész FIXED, M6.4:811); M3:BIZT-G3-7 (M3.A:271, :281). **Kánon:** GK §2:23 (harmadik személyű esetelemzés, nem traumatikus szerepjáték); HUM 7. szakasz (HUM:441); az M6.1:1066–1067 modulminimuma.
- **Opciók:** (a) kurzusszintű tilalom, mindkét elem kikerül vagy átalakul; (b) az M6-on belül igen (M6.4-opció), az M3.A-ban keretezve (önkéntes, nincs kiosztott kirekesztett szerep, passz, átbeszélés); (c) mindkettő marad, keretezve.
- **Ajánlás:** nincs, ez a Memuna ítélete. A GK §2:23 a súlyos helyzetek traumatikus szerepjátékát zárja ki; a kirekesztés-élmény hatásának megítélése szakmai kérdés.
- **Következmények:** biztonság; tanulás (a szobor és az opció pedagógiai funkciója); megvalósítás: az M6.4 második betoldása csak ezután.
- **Mit blokkol:** az M6 learner release-ét (P1); az M3.A a G1 bemenete.
- **Ki hagyja jóvá:** Memuna; az M3.A-nál az M3 modulgazdájával.

### GYV-17 — Tiltott zóna kimondása az M6.A-n
- **Döntés:** Legyen-e kötelező (és identitás-témákkal bővített) in-the-moment lépés kiskorú résztvevőkkel az M6.A:459 ma opcionális tiltott-zóna kimondása, amelyet a KAPU:230 és az A:574 kapuzott szabályként kezel?
- **Érintett findingok:** M6:BIZT-G3-2. **Kánon:** GK §4 (szakmai minimum), HUM-SAFE-03; ütközhet az M6:IMPL-G3-7 (K10) szárával.
- **Opciók:** (a) kötelező és bővített; (b) kötelező, a KAPU:230 szövegével; (c) marad opcionális.
- **Ajánlás:** nincs, ez a Memuna és a peula tartalomfelelősének ítélete.
- **Következmények:** biztonság; értékelés: a KAPU:230-hoz igazítás és a K10-ütközés; megvalósítás: peulaszöveg.
- **Mit blokkol:** az M6 learner release-ét (P1).
- **Ki hagyja jóvá:** Memuna + a peula tartalomfelelőse.

### GYV-18 — Saját párhuzamot hívó kérdésforma az M6-ban (KAPU 12. item)
- **Döntés:** Maradhat-e a „friss seb” a KAPU 12. itemének szárában (KAPU:325), és kérhet-e saját párhuzamot passz nélkül a ✅ (:328), illetve az M6.2:602 „nálatok” mintakérdése?
- **Érintett findingok:** M6:PED-G1-8, M6:BIZT-G2-6; társkapu: M6:ERT-G2-8 (X-6). **Kánon:** GK §4:61–62; HUM-SAFE-03; M6.4:443–444, M6.2:609 (részben alátámasztja).
- **Opciók:** (a) a „friss seb” kikerül a szárból, a ✅ szereplőközpontú lesz (a lecke :651 mintájára); (b) friss-seb-függő elosztó (az ERT-G2-8 útja); (c) a „nálatok” kérdés passz-formulát kap. Az (a) és a (b) ütközik.
- **Ajánlás:** nincs, ez a Memuna és az értékelési felelős ítélete. A 12. itemről egy döntés szülessen, az X-6 ERT-G2-8-cal együtt; kulcs csak projektgazdai döntéssel változik.
- **Következmények:** értékelés (kapu-item, elosztó, kulcs); biztonság (saját seb feltárása kapuhelyzetben).
- **Mit blokkol:** a G1 bemenete (P2); a kapu-item az X-6 értékelési döntésén is múlik.
- **Ki hagyja jóvá:** Memuna + értékelési felelős; kulcs: projektgazda.

### GYV-19 — „Ne nyomozz, ne kérdezz tovább” a gyakorlat-instrukciókban
- **Döntés:** Bekerüljön-e a GK §4:57 elve (a madrih nem nyomoz, nem folytat rávezető kérdésekkel „kihallgatást”) a páros megosztás és a kérdezéstechnika instrukciójába?
- **Érintett findingok:** M2:BIZT-G3-9 (M2.A:360 „kérdezz rá, és segítsd a másikat”: aggasztó tartalomnál a társ ne kérdezzen tovább, és azonnal jelezzen); M4:BIZT-G1-6 (az M4.3:360 mellé a GK:57 félmondata a :352 „Jól értem, hogy…?” formája miatt; a :360 nem gyengíthető). **Kánon:** GK §4:57, §4.1:76, :83.
- **Opciók:** (a) a GK §4:57 félmondata szó szerint mindkét helyre (az M2.A-ban és „azonnal szólj a képzőnek”); (b) csak az M4.3; (c) marad.
- **Ajánlás:** az (a): kánoni safeguarding-minimum szó szerint, új szabály nélkül. A Memuna hagyja jóvá.
- **Következmények:** biztonság (a begyakorolt kérdezéstechnika nem csúszik kihallgatásba); megvalósítás: két mondat.
- **Mit blokkol:** a G1 bemenete (P2).
- **Ki hagyja jóvá:** Memuna.

### GYV-20 — Nyilvános pozicionálás az M2.A identitás-vonalán
- **Döntés:** Maradjanak-e nyilvános pozicionálásként az identitás-vonal 3–5. állításai (zsidósághoz fűződő viszony, család hatása, nehézségek, különbözőség; M2.A:257–259), vagy papíron, illetve fejben végiggondolt formába kerüljenek?
- **Érintett findingok:** M2:BIZT-G3-3 (DPO-rész: X-4). **Kánon:** GK §4:61–62; ADV (különleges adat); BIZT-R5 (MAN:59).
- **Opciók:** (a) nyilvános marad, passzal; (b) a 3–5. állítás privát (papír vagy fejben); (c) csere kevésbé érzékeny állításra (új tartalom).
- **Ajánlás:** nincs, ez a Memuna és a DPO ítélete.
- **Következmények:** biztonság és adatvédelem (vallási, családi hovatartozás a csoport előtt, kiskorúak között); tanulás: a gyakorlat célja.
- **Mit blokkol:** a G1/G2 bemenete (P2).
- **Ki hagyja jóvá:** Memuna + DPO.

### GYV-21 — Anonimizálási korlát a szóbeli és a valós példákra
- **Döntés:** Kiterjed-e a „név és felismerhető részlet nélkül” / „csak kitalált eset” korlát (GK §2:23) a peulák szóbeli példáira (M1.A:372 „a saját kvucádra szabva”, M1.B:157) és az M2.B:368 valós (Somer-)vezetői helyzetére?
- **Érintett findingok:** M1:BIZT-G3-5, M2:BIZT-G3-5 (az (a) az M1:BIZT-G3-5 kapuja, a (b) a GYV-13-ban). **Kánon:** GK §2:23; HUM:462 (Memuna + DPO); ADV §11:241 (fiktív vagy általánosított példa).
- **Opciók:** (a) igen, minden szóbeli példára; (b) csak gyermekvédelmi tartalmú példára (a GK §2:23 szerint); (c) nem, elég a képzői útmutatás.
- **Ajánlás:** nincs, ez a Memuna és a DPO ítélete.
- **Következmények:** adatvédelem (kis közösségben visszaazonosítható eset); tanulás (életszerűség).
- **Mit blokkol:** a G1/G2 bemenete (P2).
- **Ki hagyja jóvá:** Memuna + DPO.

### GYV-22 — A kiskorú madrih önfeltárásának határa (M1.1)
- **Döntés:** Kapjon-e határ-mondatot az M1.A:282 mintájára az M1.1:926, amely a (kiskorú) madrih önfeltárását a kvucához való közelség eszközeként keretezi?
- **Érintett findingok:** M1:BIZT-G1-7. **Kánon:** GK §4:62; HUM-SAFE-03. Az M1 nincs a GK §2 G1-hatókörében (GK:17).
- **Opciók:** (a) határ-mondat az M1.A:282 meglévő szövegéből; (b) marad; (c) új keretezés (új tartalom).
- **Ajánlás:** az (a): modulon belüli, meglévő szöveg, új szabály nélkül. A Memuna és a szakmai lektor hagyja jóvá.
- **Következmények:** biztonság (a kiskorú madrih nem érez nyomást saját érzékeny történet megosztására); tanulás.
- **Mit blokkol:** csak későbbi fejlesztés (P2; az M1 nincs a G1-hatókörben).
- **Ki hagyja jóvá:** Memuna + szakmai lektor.

### GYV-23 — Egyéni utánkövetés a belépőkvíz 1–2. itemén
- **Döntés:** Kapjon-e egyéni, támogató utánkövetést, aki a belépőkvíz 1–2. (biztonsági) itemét elsőre tévesen válaszolja meg, és ki láthatja ehhez az egyéni válaszokat?
- **Érintett findingok:** M0:PED-8 (DPO-rész: X-4). **Kánon:** HUM 6–7. szakasz (az M0-kvíz diagnosztikus completion-jelző); HUM:473 (a hét item a projektgazda szövegével); ADV §3; HUB:148, :174.
- **Opciók:** (a) igen, a mentor egyénileg megkeresi (egyéni válasz-hozzáférés kell); (b) csak csoportszintű megerősítés az M0.A-n, összesítés alapján; (c) marad a kvíz saját visszajelzése.
- **Ajánlás:** nincs, ez a programvezető és a Memuna ítélete, az adatkör a DPO-é. Az answer key nem változik.
- **Következmények:** adatvédelem (egyéni kvízválaszok olvasása); tanulás (biztonsági tévképzet korai javítása); megvalósítás: mentori kapacitás.
- **Mit blokkol:** az M0 G1-átnézésének bemenete (P1; az M0 riport szerint POST-PILOT).
- **Ki hagyja jóvá:** programvezető + Memuna; adatkör: DPO.

### GYV-24 — G1: a Memuna írásos „átnéztem” bejegyzése (bizonyíték-kapu, X-7)
- **Döntés:** nem döntés, hanem bizonyíték: a Memuna egyszeri, írásos „átnéztem” bejegyzése a release-jegyzőkönyvben (PT §9.3) a GK §2 teljes hatókörére. Nem írható be, és nem feltételezhető.
- **Érintett findingok:** M0:BIZT-1, M2:ERT-G1-7, M2:BIZT-G2-8, M3:BIZT-G1-2, M3:BIZT-G2-10, M3:IMPL-G3-4, M4:PED-G1-7, M6:BIZT-G2-3, M7:BIZT-G1-5, Z:BIZT-G1-10. Ide olvadt vagy része: M3:BIZT-G2-1, M4:NYELV-G1-2, M4:NYELV-G1-9, M4:IMPL-G1-3, M6:BIZT-G2-7, M7:BIZT-G2-6, M7:ERT-G2-5, az M6:IMPL-G2-2 G1-alpontja, az M7:IMPL-G2-10 Memuna-része, és az M3:IMPL-G2-11, M7:IMPL-G2-5 új visszajelzés-szövegeinek QA-ja. **Kánon:** GK §2:17–19, §6:145, :150, :152–153; HUM:481, :573; RR:24, :39–40, :85; tracker #1 (RR:60, :69).
- **Milyen írásos bizonyíték kell, kitől (az „Opciók” helyett):** a Memunától, a release-jegyzőkönyvben: (1) „átnéztem” nyilatkozat dátummal, az átnézett verzióval (commit-SHA) és az alábbi hatókörrel; (2) a SAFE-7 kifejezett verdiktje (GK §6:153, HUM:569) és a GYV-3 helyeinek 1:1 kvízkulcs-QA-ja (GK §6:152); (3) a segélyvonalak és az akut út review-napi ellenőrzése dátummal és forrással (GK §6:150); (4) a tracker #1 lezárása a bejegyzés linkjével (RR:69). Ha a bejegyzés a repón kívül már megvan, elég rá hivatkozni. **Hatókör:** M0: M0.2 SLIDE 3–4, M0.4 SLIDE 2–4, belépőkvíz 1–2., M0.A mini-protokoll · M2: KAPU 5. item (:106–113), §D (:201), §E (:265); M2.4 :37–39, :206–210, SLIDE 5 · M3: hub, KAPU (:14), kritikus slotváltozatok (:38); M3.3–M3.4 (SAFE-1/SAFE-4 QA, a GK §6 sorai; LMS-M3-04: a MAN:65 jelölése kész); M3.B, KART-01/-02/-03, MUNK-03; M3.F · M4: M4.2 SLIDE 5 K2 (:720–737), M4.3:360 és a javított szövegek · M6: M6.2:779, M6.3:745, M6.4:930–938, :1022 (6D/ZÁRÓ); hatóköri kérdés: a KAPU P1 és az M6.A 4.3.2/B (M6:BIZT-G1-1 (c)) · M7: KAPU Q13, Q14, R4, (C) 5. sor; HUB:380–387; M7.3 SLIDE 4–5 és a Checklist 5. területe; M7.4 SLIDE 4, :778, :790; M7.B, M7.F · Z: D-2, D-3, BS-D8 (HUM:523), a HUM-SAFE-02/03 alkalmazásai.
- **Ajánlás:** a GYV-1…GYV-23 szövegváltozásai előbb kerüljenek be, az „átnéztem” a kész, végső verzióra szóljon (GK §2:19: „a kész anyagot”). Az M0-rész a futó pilot miatt most kell.
- **Következmények:** biztonság: e nélkül a GK §2 hatókörébe eső elem nem nyitható meg valódi madrihoknak (GK §2:17); megvalósítás: a jelöléseket („még nincs rögzítve”, MAN:65) csak a bejegyzés után lehet frissíteni.
- **Mit blokkol:** learner release (G1 FINAL_RELEASE_QA); az M0-rész a futó M0+M1 pilot blokkolója (M0 riport §4). Staging nem (GK §2:21).
- **Ki hagyja jóvá:** kizárólag a Memuna (GK §5:120; RR:39). Társ-bizonyítékok más kapukon: értékelési QA (X-9: M3:BIZT-G1-2, M3:BIZT-G2-10), LMS-gazda runtime (X-8: M2:BIZT-G2-8, M3:BIZT-G2-10, Z:BIZT-G1-10), DPO (X-12: Z:BIZT-G1-10), szakmai lektor (X-16: M4:PED-G1-7).

### Lezárt korlátok és „már lezárt / átvezetendő” tételek

Nincs olyan tétel, amelyet egy lezárt projektgazdai döntés szövege szó szerint megválaszol. A legközelebbi lezárt döntések
csak az opciókat szűkítik, a kérdést nem zárják le:
- HUM-SAFE-01 kontaktdöntés (HUM:30) · a GYV-4 tartalma lezárt, a helyek nem.
- HUM-SAFE-03 passzjog (HUM:72) · a GYV-2-ben a passzjog lezárt, a mechanizmus és az érzékenység nem; a HUM:73 „legalább egy” felnőttje a GYV-5-ben kettőt nem ír elő.
- SAFE-1 (HUM:566–567) · csak az M3.3-ra szól (GYV-2, GYV-3).
- M6-NY-D1, D27 · csak az M6.4 kibillenésére szól (GYV-7); az M6-NY-D3, D27 a GYV-8 küszöbét zárja, a címzettet nem.
- HUM 8. „Segélyvonalak” (HUM:471) · lezárt; a GYV-14 csak Memuna-vétóval nyithatja újra.
- HUM 12. (N-M1-04, HUM:587–588) · az M1.1 SLIDE 5 tanuló-lokalitása lezárt, a GYV-13 Memuna-mondata nem.

## 4. Adatvédelem — DPO

> Részvázlat a döntési csomaghoz. Nem kánon, és nem jóváhagyás. Forrás: `AUTOPILOT-LEDGER.md` (Külső kapuk, Findingok)
> és a validált riportok 3–4. szakasza (M0/M1 2026-10-10 és nyelvi lencse, M2–M7, Z, az M6 célzott QA).
> Rövidítések: ADV = `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`, HUM = `Emberi jóváhagyás szükséges.md`,
> GK = `Gyermekvédelem – release gate.md`, RR = `RELEASE-READINESS.md`, MAN = `LMS – activity manifest.md`,
> PT = `Program terv.md`, GL = Glosszárium, RA = `LMS – H5P runtime acceptance.md`, HUB/KAPU = az adott modul hubja, illetve kapufájlja.
> A sorszámok a findingok és a HEAD szerintiek.
>
> **Elsődleges kapu:** a ledger-sor saját szövegében elsőként hivatkozott kapu (`(X-a, X-b)` → X-a). Ha egy tétel elsődlegesen
> másik kapué, itt csak hivatkozás áll rá („lásd X-n”). **Közös bizonyíték-kapuk:** az M1:BIZT-G1-3, az M1:BIZT-G2-2, az
> M4:IMPL-G2-12, az M6:IMPL-G2-2 (elsődleges: X-8) és a Z:BIZT-G1-10 (elsődleges: X-7) DPO-része is az X-12-höz tartozik.
> Itt nincsenek beszámolva, de a DPO teendőjeként az ADV-E1 felsorolja őket. Ugyanígy a jogi alkérdés: M3:BIZT-G2-9 (X-5) → JOG-1.

### ADV-1 — Szerkesztő tanári/menedzseri hozzáférés és csoportszűkítés a „csak a kijelölt mentorod látja” ígéret mögött
- **Döntés:** Elfogadható-e a szerkesztő tanár, a menedzser és a rendszergazda csoporttól független hozzáférése (BIZT-2)? Szűkíteni kell-e csoport szerint a mentor hozzáférését a nem TEXT-C profilokon (ASSIGN-S/M, GATE-CP, H5P-C, QUIZ; BIZT-5)? Vagy inkább a tanulói ígéret és az ADV §11 „Ki látja?” szakasza bővüljön?
- **Érintett findingok:** M1:BIZT-G2-4 (M1.4:502, ASSIGN-M), M2:BIZT-G2-3 (M2.2:499, M2.4:37), M2:BIZT-G1-6 (az LMS-M2-05 hozzáférése; alkérdés: a megőrzési sor és a „Név (vagy becenév)” mező). Ide olvadt: M4:BIZT-G2-2, M5:BIZT-G2-2, Z:BIZT-G1-4, Z:IMPL-G1-4 (M4.4:704, :737, M4.F:267, M5.4:45/:323, Z.4:98/:307/:329), továbbá az M3:BIZT-G1-5/-G2-5/-G2-7/-G3-8, az M5:BIZT-G1-4 és az M6:BIZT-G1-7 BIZT-5/BIZT-2 alkérdése. **Kánon:** ADV §3:104–109 („a szűkítés DPO-kérdés: BIZT-5”; BIZT-2: „ez a szakasz nem dönti el”), :115, :117; §5:148; §11:230, :245; HUM 11. szakasz :576 (az RT-P0-15 csak a mentort szűkíti); HUM-PRIV-01 :132 (legszűkebb szükséges hozzáférés).
- **Opciók:** (a) Szűkítés: szerkesztő tanári és menedzseri szerep csak névre szóló, indokolt kiosztással. A mentor csoportmódja minden P2-profilon él, és ezt stagingben visszaolvassák. (b) A hozzáférés marad; a tanulói ígéret és a §11 „Ki látja?” megnevezi az adminisztratív szerepeket. (c) Vegyes megoldás: a mentorokat csoport szerint szűkítik, az adminisztratív hozzáférés korlátozott és dokumentált, és a tájékoztató jelöli.
- **Ajánlás:** ajánlás nincs — a DPO ítélete; a kánon két helyen kifejezetten nyitva hagyja. Kockázat: Moodle-alapértelmezés mellett a mai tanulói mondat nem igaz. Bármelyik opciónál a §11:245 mondatát a döntéshez kell igazítani.
- **Következmények:** Adatvédelem: a tájékoztató valóságtartalma. Megvalósítás: csoportmód és szerepkiosztás a buildben, az RT-P0-15 kiterjesztése a nem TEXT-C profilokra. Tanulásra és értékelésre nincs hatása.
- **Mit blokkol:** A stagingot nem. Kontrollált pilot (M0+M1): az M1-riport POST-PILOT döntésnek sorolta. Az M1-Assignment ugyanakkor csak jóváhagyott adatkezeléssel nyitható meg (RR:83; a bizonyíték az M1:BIZT-G2-2, X-8/ADV-E1). Learner release: igen (G2), minden P2-adatot tároló activitynél.
- **Ki hagyja jóvá:** DPO / jogi felelős (a HUM-PRIV-01 „Jóváhagyó” sora szerint); a szerepkiosztást az LMS-gazda rögzíti.

### ADV-2 — Ki tartozik a „kijelölt értékelő/mentor” olvasói körbe (második és fellebbezési képző, Memuna, F-peula képzője)
- **Döntés:** A „kijelölt mentor/értékelő” körbe tartozik-e a második és a fellebbezési képző, a Memuna (M3-kapu) és a nem mentor F-peula-képző? Ha nem, hogyan kapja meg az F-peula képzője a kapuvisszajelzésből képzett hiánylistát?
- **Érintett findingok:** M3:BIZT-G2-5 (LMS-M3-05; M3.4:64, KAPU:317 ↔ MAN:66, PT:290), M3:BIZT-G3-8 (M3.F:3, :183), M7:IMPL-G3-7 (M7.F:79). **Kánon:** ADV §5:148 (P2-adatot csak a kijelölt értékelő/mentor lát, és csak ha szükséges); ADV §3:87 (az F-peulák nem Moodle-ben vezetett mentori jegyzete: külön review); §11:245; M3 KAPU:317 (kétszemes rend); GK:23.
- **Opciók:** (a) A kör kifejezett bővítése: a második és a fellebbezési képző, valamint a Memuna csak kétszemes, fellebbezési vagy gyermekvédelmi okból olvas; az F-peula képzője kohorszonként kijelölt értékelő. A §5 és a §11 ennek megfelelően kiegészül. (b) Szűk kör: csak a kijelölt mentor olvas; a második és a fellebbezési képző csak fellebbezéskor; az F-peula képzője csak név nélküli, összesített hiánylistát kap. (c) Az F-peulát mindig a kijelölt mentor vezeti.
- **Ajánlás:** ajánlás nincs — a DPO és a programvezető ítélete. Minden opciónál kötelező: a kétszemes rend, a Memuna-mondat, a „valós eset névtelenítve sem” szabály (GK:23) és az M7.F:79 „név nélkül” kikötése nem gyengül.
- **Következmények:** Értékelés: a kétszemes rend és a fellebbezés működése. Adatvédelem: a §11 „Ki látja?” szövege. Megvalósítás: Moodle-csoport és szerep a második képzőnek. Programszervezés: az F-peulák beosztása.
- **Mit blokkol:** Learner release (G2) az M3- és az M7-kapunál. A stagingot és az M0+M1 pilotot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős az LMS-gazdával; az F-peulák beosztásáról a programvezető; a Memuna szerepéről a Memuna.

### ADV-3 — Önreflexiós és opcionális szabad szöveges mezők: tanuló-lokális vagy tárolt (az N-M1-04 új alkalmazási esetei)
- **Döntés:** Az alábbi szöveges mezők tanuló-lokálisak legyenek (nem tároltak, nem completion-feltételek, az N-M1-04 és a D-2…D-6 mintájára)? Vagy tárolt TEXT-C-mezők legyenek, saját manifest- és ADV §3-sorral? (Az M7.B:29-nél a törlés is opció.)
- **Érintett findingok:** M3:IMPL-G2-6 (M3.1 SLIDE 5, M3.2 7A: a 🔒 tárolást ígér, de TEXT-C sor nincs, MAN:308), M4:BIZT-G1-2 (M4.1:1203 „magadnak írod”, M4.3:643, :649 ↔ MAN:24, :70, :74: LMS-M4-06/-08, TEXT-C), M4:IMPL-G1-2 (függő tétel: a tanulói mondatok a BIZT-G1-2 után), M4:ERT-G1-10 (M4.1 IV Free Text, :831–836; a válasz az xAPI-ban rögzül), M7:IMPL-G2-3 (M7.2:913; nincs TEXT-C sora, és nincs a BSPEC-02 és az RA 24 listáján), M7:BIZT-G3-6 (M7.B:29), Z:IMPL-G1-3 (Z.3 SLIDE 5: tanuló-lokális, vagy az LMS-Z-06 negyedik kérdése). **Kánon:** ADV §2:29 (alapértelmezés: az önreflexió a madrihnál marad), §5:150; HUM 12. szakasz :587–588 (N-M1-04); HUM 10. szakasz :524–529 (D-1…D-6); ADV §3:65; RA 24. pont.
- **Opciók:** (a) Tanuló-lokális: nem tárolt, nem completion-feltétel. Beviteli elem csak igazoltan adatmentes runtime mellett lehet (RA 24); addig a saját jegyzetes út él. (b) Tárolt: TEXT-C sor, ADV §3 „Szabad szöveges reflexió” sor, RT-P0-15, és a tanulói ígéret ehhez igazodik. (c) Az M7.B:29-nél a kérdés törlése.
- **Ajánlás:** (a), ha a projektgazda nem nevez meg konkrét pedagógiai vagy értékelési szükséget. Ezt az ADV §2:29 és §5:150 lezárt alapértelmezése és a következetes precedens (N-M1-04, D-2…D-6) adja. Kivétel: az M4.1-ben és az M4.3-ban a manifest ma tárolt TEXT-C-t ír (LMS-M4-06/-08). Ott az (a) completion-változás, amelyet a projektgazdának kifejezetten jóvá kell hagynia; ha nem hagyja jóvá, a (b) marad, és a „magadnak írod” mondatot kell igazítani.
- **Következmények:** Tanulásra nincs hatása: az opcionális, önreflexiós jelleg marad. Értékelés: az M4 completion-feltétele változhat (lásd X-6). Adatvédelem: kevesebb tárolt P2-szöveg. Megvalósítás: a „nem tároljuk” mondat csak az RA 24 sikeres visszaolvasása után írható be (X-8); a VO-forrásszöveg csak hanggyártási úton változik (X-17).
- **Mit blokkol:** A stagingot nem: a build a mai állapotot követi (nem completion-elem, a 🔒 nem törlődik). Learner release (G2) az M3, M4, M7 és Z érintett leckéinél. Az M0+M1 pilotot nem.
- **Ki hagyja jóvá:** projektgazda (pedagógiai szükség, completion, build-spec); vétó: DPO / jogi felelős (HUM-PRIV-01). Az ILO 2 átírása: lásd X-10; a kötelező/opcionális besorolás: lásd X-6.

### ADV-4 — Pontozatlan önbevallás, passz- és önjelző választás rögzítése követett H5P-ben
- **Döntés:** Elfogadható-e, hogy a követett H5P (CP vagy Branching Scenario) próbálkozás-riportja tanulónként rögzíti a pontozatlan érzelmi önbevallást, az önjelzést és a passz-választást, és ezt a tanári szerepek látják (ADV §3:115)? Vagy ezek rögzítésmentes útra kerüljenek?
- **Érintett findingok:** M1:IMPL-G1-5 (M1.1 SLIDE 1–2, választós tartalékút), M3:BIZT-G1-5 (M3.3 P1–P4 passz-választás; csak összesített-e a hub §7 elemzése, HUB:268–271), M3:BIZT-G2-7 (M3.4:188 „Nagyon, ez most nagyon aktuális nekem.”), M5:BIZT-G2-4 (M5.4 SLIDE 6), M6:BIZT-G1-4 (M6.1–M6.3 SLIDE 1), Z:BIZT-G1-8 (b) (Z.2:236–240, Z.3:121–127). **Kánon:** ADV §3:81 és HUM 9. szakasz :487 (M2.1 identitás-kör: nem rögzített elem, kikapcsolt követéssel vagy tartalombankos beágyazással); HUM 11. szakasz :564 (D-j: a választás tárolása nem kívánt adat; ha mégis tárolódik, DPO/jogi QA kell), :558/:563 (D-d/D-i: nem completion-elem), :566–567 (SAFE-1 passz-csomópont); ADV §5:150.
- **Opciók:** (a) A rögzítés elfogadása: ADV §3-sor (pl. „Nyers kvízpróbálkozások”, a megerősítés + 90 nap) és a tájékoztató kiegészítése. (b) Rögzítésmentes út az M2.1 mintájára (kikapcsolt követés, tartalombankos beágyazás, vagy szöveg + Tovább), ahol a completion nem erre az elemre épül. (c) A választó elhagyása, a szöveges kérdés marad (az M1.1-ben ez a forrás elsődleges útja).
- **Ajánlás:** a (b), az M1.1-nél a (c). A lezárt M2.1-precedens (HUM :487), a D-j és az ADV §5:150 ebbe az irányba mutat, és a D-d/D-i szerint egyik elem sem completion-feltétel. Az M3.3 passz-választásánál ajánlás nincs: a SAFE-1 csomópont szerkezete a Branching Scenarióban nem változhat, ezért a DPO és a Memuna ítél a célverziós visszaolvasás (X-8) után. A hub §7 elemzése csak összesített adatból készülhet (ADV §11:243).
- **Következmények:** Biztonság: ha a passz vagy az önjelzés egyénileg látható, az nyomást kelthet (a HUM-SAFE-03 passzjoga). Adatvédelem: kevesebb érzékeny próbálkozás-adat. Megvalósítás: a CP szerkezete és completion-profilja (M0:IMPL-3, X-6).
- **Mit blokkol:** A stagingot nem: az M1.1 buildje a nem rögzítő „szöveg + Tovább” utat követi. Az M0+M1 pilotot nem (POST-PILOT). Learner release (G2) az M3, M5, M6 és Z érintett leckéinél.
- **Ki hagyja jóvá:** DPO / jogi felelős; az M3-tételeknél a Memuna is. A completion-rész: lásd X-6 (M0:ERT-3).

### ADV-5 — BIZT-R5: someres vagy identitás-tartalom név szerint tárolt, kötelező mezőben
- **Döntés:** Különleges (vallási vagy világnézeti) adat gyűjtésének minősül-e, ha egy név szerint tárolt, kötelező mező a zsidóság-kör megnevezését, a választott pillért vagy egy someres értéket kéri? Alkalmazható-e kivétel? Vagy a promptnak kör- és pillér-semlegesnek kell lennie, és a megnevezésnek pontlevonás nélkül kihagyhatónak?
- **Érintett findingok:** M2:BIZT-G1-3 (LMS-M2-06, M2.1:487; KAPU D. 1. blokk, :217), M2:PED-G1-5 (KAPU D. „Választott pillér”, :235; R3 ≥ 1), M2:BIZT-G2-6 (az LMS-M2-07 promptja, M2.3:910), M7:BIZT-G1-6 (LMS-M7-10, M7.1:529; R1). **Kánon:** ADV §3:54, :75 (különleges adat normál activityben nem gyűjthető), :81; HUM-PRIV-01 :132–133; HUM 11. szakasz :564 (D-j); MAN:59 (a BIZT-R5 nyitott); RR G2 :25 (nyitott DPO-döntésként nevesítve).
- **Opciók:** (a) Nem különleges adat (a someres értékrend pedagógiai tartalma): a mező tárolt marad, mező melletti adatvédelmi megjegyzéssel. (b) Különleges vagy világnézeti adat: a prompt kör- és pillér-semleges, a megnevezés kihagyható, pontlevonás nélkül. (c) Különleges adat, de a GDPR 9. cikk (2) bekezdésének valamelyik kivétele alkalmazható (jogi minősítés kell, dokumentált jogalappal).
- **Ajánlás:** ajánlás nincs — a DPO/jogi felelős minősít, someres vonatkozásban a projektgazda. Kockázat: ha a minősítés (b), a kánon (ADV §3:75) a ma kötelező, név szerinti mezőket nem engedi. Ekkor a KAPU D. R3/A.1 feltételeinek értékelési igazítása következik (X-6).
- **Következmények:** Értékelés: a KAPU D. R3 ≥ 1 feltétele és a pontlevonás. Tanulás: a pillér-kötődés továbbra is rögzítés nélküli önreflexió (HUM-PRIV-01). Adatvédelem: a különleges adat kockázata. Megvalósítás: a manifest-sorok privacy-megjegyzése.
- **Mit blokkol:** Learner release (G2) az M2 és az M7 érintett activityjeinél; az RR G2 kifejezetten nyitott DPO-döntésnek írja. A stagingot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős; someres vonatkozásban a projektgazda (QA: helyi ideológiai felelős, HUM-SOMER-01).

### ADV-6 — A bemutatkozó fórum (FORUM-C) megőrzése, a „Bemutatkozó fal” review-ja és a pilot-tájékoztató
- **Döntés:** Mennyi ideig őrizzük meg a bemutatkozó fórumposztot és -választ, és melyik ADV §3-sor vonatkozik rá? Mi a „Bemutatkozó fal” külön review-jának eredménye? Megnyitható-e a fórum a pilotban megőrzési tájékoztató nélkül?
- **Érintett findingok:** M0:BIZT-7 (P0). **Kánon:** ADV §3:79 (külön review: az M0 Bemutatkozó fal), :120 (FORUM-C); a §3 mátrixában (:60–73) fórumposztra nincs sor; PT:228 („Ha egy adatot gyűjtő aktivitásra ez nincs rögzítve, az nem nyitható meg valódi madrihnak.”); ADV §1:7 (a repó nem választ megőrzési időt); §11:247–256.
- **Opciók:** (a) Meglévő sor hozzárendelése (pl. „Szabad szöveges reflexió”: a képzés vége + 90 nap). (b) Új, fórumra szabott megőrzési sor, a DPO rögzíti. (c) A pilotban a fórum nem nyílik meg, vagy rögzítés nélküli bemutatkozás váltja (szóban, az M0.A-n).
- **Ajánlás:** ajánlás nincs — a DPO ítélete (a megőrzési időt a repó nem választja meg).
- **Következmények:** Adatvédelem: a megőrzés közlése. Tanulás: a bemutatkozás formája. Megvalósítás: a §11 „Meddig őrizzük meg?” listája és a fórum bevezetőjének szövege; ehhez a freeze alatt projektgazdai kivétel kell (CC-04-szabály).
- **Mit blokkol:** A kontrollált pilotot (M0 PILOT-BLOCKER, PT:228) és a learner release-t (G2). A stagingot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős; a tájékoztató szövegének freeze-kivételét a projektgazda.

### ADV-7 — A peulák papír- és fizikai produktumai, fotó és személyes telefon (a HUM-PRIV-02 alkalmazása)
- **Döntés:** Mi lesz a peula után az önfeltáró cetlikkel, a névvel aláírható kártyákkal, a plakátokkal és a poszterekkel (visszaadás, név nélküli begyűjtés, fizikai megőrzés, kifüggesztés)? Fotózhatók-e? Maradhat-e a „telefonon megmutatjuk” út?
- **Érintett findingok:** M1:BIZT-G3-8 (M1.A Johari-cetlik, a tábla fotója; a HUM:149-hivatkozás átvezetése objektív: .obj), M4:BIZT-G2-5 (M4.A:381: névvel aláírható kártya borítékba vagy falra; MUNK-01, POSZ-01), M4:BIZT-G2-4 (függő tétel: a kártya ADV-utalása; objektív rész: .obj), M5:BIZT-G2-1 (M5.A:437 „vagy a telefonján mutatjuk meg”), Z:BIZT-G1-9 (Z.A: plakát, képzői idézetek, névcetlik, poszterek, szófelhő; objektív rész: .obj). **Kánon:** HUM-PRIV-02 :147, :151 (alapból nincs felvétel; a kézírásos plakátot fizikailag őrizzük; a fotó lépései; a személyes telefon nem alapfolyamat); ADV §6:161–169; ADV §2:29; ADV §3:67 (név nélküli papír munkalap: összesítés, majd 30 napon belül megsemmisítés); ADV §9:214.
- **Opciók:** (a) Egységes peula-papírszabály: az önfeltáró cetli és kártya a madrihnál marad, vagy visszakerül hozzá; névvel nem gyűjtünk és nem függesztünk ki; a név nélküli lapokra az ADV §3:67 vonatkozik; a plakátot fizikailag őrizzük; fotó csak megnevezett céllal, a HUM-PRIV-02 lépései szerint készül; a telefonos út csak ezekkel a lépésekkel maradhat, vagy kimarad. (b) Tételenkénti döntés. (c) A névvel aláírt kártya begyűjthető, új ADV §3-sorral és tájékoztatóval.
- **Ajánlás:** (a). A HUM-PRIV-02 (lezárt döntés), az ADV §2:29 alapértelmezése és az ADV §3:67 sora ezt adja ki. Ami ezen túlmegy (például a névvel begyűjtött lap megőrzési ideje), azt csak a DPO rögzítheti.
- **Következmények:** Tanulás: az M4-ben a kártya visszaadása (az M4:PED-G2-9 (a) útja, X-10, ettől függ). Adatvédelem: nem marad névvel gyűjtött papír. Megvalósítás: a MUNK- és POSZ-assetek csak build úton változnak.
- **Mit blokkol:** Learner release (G2; az ADV §9:214 release-evidence-sora) az M1.A, M4.A, M5.A és Z.A peulánál; az M1-riport POST-PILOT-nak sorolta. A stagingot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős; az M5-nél a modulgazdával.

### ADV-8 — „Név nélküli” begyűjtés, ha visszaazonosítható (kis létszám, a képző ismeri a sorokat)
- **Döntés:** Teljesíti-e az ADV §3:67 „név nélkül begyűjtött” sorát, ha a táblára írt hiány kis létszámnál visszaazonosítható, vagy ha a képző név szerint ismeri a név nélkül begyűjtött játéklap-sorokat? Ha nem, milyen sor vagy módszer kell?
- **Érintett findingok:** M5:BIZT-G2-5 (M5.F:305; a MUNK-01 digitális megfelelőjének nincs §3-sora), M6:BIZT-G3-5 (M6.F:331/:333 ↔ :223). **Kánon:** ADV §3:67, :69 (mentori fejlesztési jegyzet); §2:29; §5:151.
- **Opciók:** (a) Ha visszaazonosítható, a mentori fejlesztési jegyzet sora vonatkozik rá (az utolsó mentorálás + 6 hónap), minimális adattal. (b) Név nélkülinek számít, ha csak összesítve kerül ki, a DPO által megadott létszámküszöb felett. (c) Módszerváltás (szóbeli összesítés vagy egyéni visszaadás).
- **Ajánlás:** ajánlás nincs — a DPO és az értékelési felelős ítélete. Létszámküszöb a repóból nem vezethető le.
- **Következmények:** Értékelés: a hiánylistára épülő F-peula és felzárkóztatás. Adatvédelem: a „név nélküli” ígéret valóságtartalma. Megvalósítás: a MUNK-01 digitális változata.
- **Mit blokkol:** Learner release (G2) az M5.F és az M6.F peulánál. A stagingot és az M0+M1 pilotot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős és értékelési felelős.

### ADV-9 — Valós kvuca adata a produktumokban: a Peula v2 szabályának kiterjesztése és egységes adatmondat
- **Döntés:** Kiterjed-e a Peula v2 kvuca-szabálya (valós kvuca csak nem azonosító, csoportszintű információval, nevek, egyéni érzékeny történetek és diagnózisok nélkül) az M4 peulabemutatóra, az M5 kapuproduktumra és az M6 játéklapra? Belefér-e a csoportszintbe a „nevesített korosztály/élethelyzet” és a „néhányan visszahúzódók”? Mindenhol a bővebb adatmondat álljon?
- **Érintett findingok:** M4:BIZT-G1-5 (HUB:133; ADV:83), M5:BIZT-G1-5 (KAPU:293 R2, HUB:20; ADV:84), M5:NYELV-G2-12 (függő tétel: az M5.B:312 a K5 és az M5:ERT-G2-9 (X-10) után; a HOLD-blokk kész), M6:QA-BIZT-2 (KAPU:384, HUB:10, :208, M6.B:244, :32 ↔ M4.4:737, M7.B:439). **Kánon:** HUM 8. szakasz :461 („A Peula v2 kvucája”, QA: DPO + programvezető); ADV §3:86, :83–84; ADV §2:29.
- **Opciók:** (a) A HUM :461 / ADV :86 szabályának szó szerinti kiterjesztése mindhárom produktumra, a bővebb adatmondattal az M6 mind az öt helyén. (b) A mai modulmondatok maradnak; a DPO csak a vitatott példák csoportszintűségéről dönt. (c) Az M4-ben és az M5-ben csak kitalált profil használható.
- **Ajánlás:** (a), a DPO és a programvezető megerősítésével. A szabály már szerepel a kánonban, az M4.4:737 és az M7.B:439 is használja, és a kiterjesztés csak szigorít (ADV §2). Hogy a „nevesített korosztály/élethelyzet” csoportszintű-e, az DPO-ítélet.
- **Következmények:** Értékelés: az M5 R2-kritériuma és a valós kvuca-sor kötelezősége (lásd X-10, M5:ERT-G2-9). Adatvédelem: egységes kizárási lista. Megvalósítás: a HUB:10 és az M6.B:244 csak build úton változik.
- **Mit blokkol:** Learner release (G2; az ADV:83/:84 külön review-ja, ADV-E2) az M4, M5 és M6 kapuproduktumánál. A stagingot nem.
- **Ki hagyja jóvá:** DPO és programvezető (a HUM :461 QA-szerepei).

### ADV-10 — Moodle-on kívüli digitális eszközök: Google-sablon, közös digitális fal, QR-kódos kilépőkártya
- **Döntés:** Van-e a tanulóknak szervezeti Google-fiókja? Használható-e a közös digitális fal (M6.3) és a QR-kódos digitális kilépőkártya (M7 hub), és ha igen, milyen eszközzel, fiókkal, láthatósággal és ADV §3-sorral? Melyik megőrzési sor vonatkozik az LMS-M7-10-re?
- **Érintett findingok:** M2:BIZT-G1-7 (M2-HUB-MUNK-01, HUB:203), M6:BIZT-G2-5 (M6.3:546, Kivsza-példa; GK §4.2), M7:BIZT-G1-7 (HUB:86, :90, :420; (c) az LMS-M7-10 megőrzése, M7.1:520). **Kánon:** HUM-PRIV-01 :132 és ADV §3:53 (Google-sablon csak szervezeti fiókban, korlátozott megosztással); ADV §3:87; ADV §9:207; GK §4.2 (digitális 1:1 helyzetek, online szobák).
- **Opciók:** (a) Csak Moodle, és ha van, szervezeti Google-fiók; a digitális fal és a QR-kártya helyett papíros vagy Moodle-változat. (b) A külső eszköz engedélyezett, ADV §3-sorral, szervezeti fiókkal és tájékoztatóval. (c) Eszközönként vegyes megoldás.
- **Ajánlás:** részleges. A Google-út feltétele lezárt: szervezeti fiók nélkül a Google-sablon nem használható (HUM-PRIV-01 szó szerint). A fiók megléte ténykérdés, a programvezető válaszolja meg. A digitális falra, a QR-kártyára és az LMS-M7-10 megőrzési sorára ajánlás nincs — a DPO dönt, a BS-D6 mintájára.
- **Következmények:** Tanulás: saját példány vagy papíros változat. Adatvédelem: harmadik fél, fiók, láthatóság. Megvalósítás: ha a QR-kártya marad, manifest-sort kap.
- **Mit blokkol:** Learner release (G2) az M2, M6 és M7 érintett elemeinél. A stagingot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős és programvezető (a fiók kérdésében); az M7-nél az LMS-gazdával; a GK §4.2-t érintő részben a Memuna.

### ADV-11 — Közös vagy tartalék eszköz kezelése az F-peulákon
- **Döntés:** Milyen további szabály vonatkozik a közös vagy tartalék eszközre (jelszómentés tilalma, a letöltött jegyzet törlése)? Készülhet-e rajta Moodle-on kívüli munkapéldány? Egységesen minden F-peulába bekerüljön-e a szabály?
- **Érintett findingok:** M2:BIZT-G3-10 (M2.F; a kijelentkezés objektív tétel, M2:IMPL-G3-1), M6:QA-BIZT-1 (M6.F:323 „a közös eszközön nem”). Ide olvadt: M6:IMPL-G3-1 (jelszómentés). **Kánon:** A11Y:55, :57 (saját fiók, kijelentkezés); ADV §6:166 (személyes eszköz vagy felhő nem alapértelmezett tároló — analógia, nem lefedés).
- **Opciók:** (a) Egységes szabály minden F-peulán: nincs jelszómentés, nincs helyi munkapéldány a közös eszközön (papír vagy saját eszköz helyette), kijelentkezés és a letöltések törlése. (b) Munkapéldány engedélyezett, kötelező törlési lépéssel. (c) Modulonkénti szabály.
- **Ajánlás:** ajánlás nincs — az LMS-gazda és a DPO ítélete. A döntésig az M6.F:323 tilalma marad (a törlése gyengítés volna).
- **Következmények:** Adatvédelem: maradványadat a közös eszközön. Hozzáférhetőség: hogyan jut a résztvevő eszközhöz (A11Y:55). Megvalósítás: az F-peulák utasításainak egységesítése.
- **Mit blokkol:** Learner release (G2) az F-peulák eszközös útján. A stagingot nem.
- **Ki hagyja jóvá:** LMS-gazda és DPO.

### ADV-12 — A Somer AI-végpontjának naplózása, megőrzése és hozzáférése
- **Döntés:** Naplóz-e a Somer szerveroldali AI-végpontja (prompt, válasz, metaadat)? Mennyi ideig őrzi meg, ki fér hozzá, és milyen csatornán küldi a képző a promptot?
- **Érintett findingok:** M7:BIZT-G2-3 (M7.2:24). **Kánon:** HUM-PRIV-04 :189–191 és ADV §7:179 (`store=false`, nincs személyes adat, ZDR, ha elérhető), :186 (promptkizárási lista), :188 (a szervezet dokumentálja a beállításokat); az ADV §3-ban nincs AI-sor; :86 (az M7 AI-promptjai: külön review); §11:262 (a tájékoztató megőrzésről nem szól).
- **Opciók:** (a) Tartalmat nem naplóz, csak technikai metaadatot, rövid megőrzéssel. (b) Visszaélés- és biztonsági célból tartalmat is naplóz, rögzített megőrzéssel és szűk hozzáféréssel (kapcsolódik: M7:BIZT-G1-4, X-5; a monitorozás maga is adatkezelés). (c) Csak a képző által közvetített használat, naplózás a szervezeti oldalon.
- **Ajánlás:** ajánlás nincs — a DPO ítélete. A tájékoztató (§11:262) bővítése csak ezután jön.
- **Következmények:** Adatvédelem: új ADV §3-sor. Biztonság: a krízist jelző bevitel kezelése (X-5). Megvalósítás: a végpont konfigurációja, RT-P0-20 (X-8).
- **Mit blokkol:** Learner release (G2) az M7 AI-segédjére. A no-AI út teljes értékű marad (HUM-PRIV-04), ezért az M7 teljesíthetőségét nem blokkolja. A stagingot nem.
- **Ki hagyja jóvá:** DPO / jogi felelős (QA: programvezető, HUM-PRIV-04).

### ADV-13 — A hub-analitika célhoz kötöttsége (az LMS-M2-09 szabad szövegeinek átolvasása)
- **Döntés:** Igazolja-e a HUB:244 analitikai mutatója („legalább 2–3 konkrét … szabály”), hogy az LMS-M2-09 szabad szöveges válaszait rendszeresen átolvassák?
- **Érintett findingok:** M2:BIZT-G1-8 (HUB:244); tőle függ az M2:NYELV-G1-13 (X-6); kapcsolódik az M2:BIZT-G2-1 (N-3, X-5). **Kánon:** ADV §11:243 és PT:227 („a program fejlesztéséhez csak összesített, beazonosíthatatlan adatot használunk”); ADV §2:20–27; §5:148.
- **Opciók:** (a) A mutató csak olyan adatból számolható, összesítve, amelyet más jogos célból (pl. az N-3 szerinti mentori átnézés során) már láttak; önálló átolvasást nem igazol. (b) A mutató kikerül, vagy teljesítési arány váltja. (c) Rendszeres átolvasás analitikai célra, a tájékoztató módosításával.
- **Ajánlás:** az (a) vagy a (b). A (c) ellentmondana az ADV §11:243 és a PT:227 kánoni mondatának. A kettő közül a DPO választ, az N-3 döntésével (X-5) összhangban.
- **Következmények:** Adatvédelem: célhoz kötöttség. Értékelés: a HUB:244 mutatójának alsó határa (X-6) ettől függ. Megvalósítás: nincs új tárolás.
- **Mit blokkol:** Learner release (G2) az M2-nél. A stagingot nem.
- **Ki hagyja jóvá:** DPO; az N-3 miatt a Memunával.

### ADV-14 — A Z.4 videós útja: a hozzájárulás rögzítése és ellenőrzése
- **Döntés:** Kiskorúnál hol rögzül a résztvevő és a gondviselő együttes hozzájárulása a Z.4 opcionális videójához? Ki ellenőrzi feltöltés előtt? Vonatkoznak-e a videóra az ADV §6 fotólépései?
- **Érintett findingok:** Z:BIZT-G1-5; ide olvadt: Z:IMPL-G1-8. **Kánon:** lezárt rész — a hozzájárulás adója (HUM 9. szakasz :484; ADV §4:141, §6:171: „a tanuló saját videójára is”). Nyitott rész — a folyamat (ADV §6:159, :171: „a gondviselői hozzájárulás folyamata is a HUM-PRIV-02-höz tartozik”; §9:214).
- **Opciók:** (a) A hozzájárulás Moodle-on kívüli, korlátozott hozzáférésű szervezeti nyilvántartásba kerül; a videós út csak a rögzítése után nyílik meg; a mentor ellenőriz; a fotólépések a videóra is vonatkoznak. (b) A videós út kimarad (a hivatalos produktum a Moodle Assignment, HUM 7. szakasz). (c) Videós út csak 18 év felettieknek.
- **Ajánlás:** ajánlás nincs — a DPO és a jogi felelős folyamatdöntése. A hozzájárulás adóját nem kell újra eldönteni.
- **Következmények:** Adatvédelem: a gondviselői hozzájárulás kezelése. Megvalósítás: Assignment-beállítás (a fájltípusokról lásd X-11, M1:IMPL-G2-10). Hozzáférhetőség: a videó opcionális marad.
- **Mit blokkol:** Learner release (G2; ADV §9:214) a Z.4 videós útjára. A stagingot nem.
- **Ki hagyja jóvá:** DPO és jogi felelős.

### ADV-15 — A Z.4 Feedback „Show analysis page” és beküldési értesítése
- **Döntés:** Mi legyen a Z.4 Feedback „Show analysis page” beállítása és az „Enable notification of submissions” értéke?
- **Érintett findingok:** Z:BIZT-G1-7 (Z.4:398); ide olvadt: Z:IMPL-G1-11. **Kánon:** HUM-PRIV-03 :172 (a válaszok név nélkül jelennek meg, de a visszajelzés nem anonim); ADV §8; ADV §3:119 (FEEDBACK-N; a mentor hozzáférése DPO-kérdés, BIZT-6), :131 (TEXT-C: az értesítés „No”, BIZT-11).
- **Opciók:** (a) Mindkettő „No” (ez a kódbeli alapérték). (b) „Show analysis page” = Yes, csak összesítve, létszámküszöb felett. (c) Az értesítés „Yes”, a név nélküli megjelenítés mellett.
- **Ajánlás:** (a). Ezt az ADV §2 adatminimalizálása és a TEXT-C-re rögzített BIZT-11 mintája (ADV:131) adja; kis csoportban az elemzőoldal visszaazonosíthat (vö. ADV-8). A DPO és a programvezető, a HUM-PRIV-03 gazdái erősítsék meg.
- **Következmények:** Adatvédelem: a „név nélkül jelennek meg” ígéret tartható. Megvalósítás: Feedback-beállítás. Tanulásra nincs hatása.
- **Mit blokkol:** Learner release (G2) a Z.4-nél. A stagingot nem: a kódbeli „No” felépíthető.
- **Ki hagyja jóvá:** DPO és programvezető (HUM-PRIV-03).

### ADV-E1 — A DPO írásos release-QA-ja a lezárt adatkezelési megoldásokra, activitynként (bizonyíték-kapu, G2)
- **Szükséges bizonyíték (nem nyitott döntés):** a DPO/jogi felelős írásos jóváhagyása (ADV §9:216, „privacy/DPO/jogi signoff”; RR G2 FINAL_RELEASE_QA) arról, hogy a lezárt megoldások a megvalósításban teljesülnek. Ezek: a HUM-PRIV-01 az LMS-M2-01/-05/-06-nál (az M2.1 SLIDE 4 nem tárolt elem), a HUM-PRIV-01 és a D-j az LMS-M2-07/-08/-09-en és az M2.2–M2.4 H5P-C adatfolyamain. A megvalósítást a projektgazda jóváhagyta; a szerepköri bizonyíték még nincs meg.
- **Érintett findingok:** M2:BIZT-G1-9, M2:BIZT-G2-9. Ugyanez a DPO-bizonyíték kell ezekhez is (elsődleges kapujuk másik, ott vannak beszámolva): M1:BIZT-G1-3 (N-M1-04, BIZT-QA-1; X-8), M1:BIZT-G2-2 (LMS-M1-05/-07, ADV:230; itt elsődleges, runtime-része: RT-2), M4:IMPL-G2-12 és M6:IMPL-G2-2 (D-5; X-8), Z:BIZT-G1-10 (D-2, D-3, BS-D8, HUM-PRIV-01–03, ADV:214/:216; X-7). **Kánon:** ADV §1:5, §9:216, §11:230; HUM 12. szakasz :588; HUM 10. szakasz :524–528; RR G2 :25.
- **Opciók / ajánlás:** nem döntés. Sorrend: előbb az M0+M1 pilot DPO-része (N-M1-04, LMS-M1-05/-07: PILOT-BLOCKER), utána modulonként.
- **Következmények:** A DPO-QA bemenete a runtime-visszaolvasás (RT-P0-15, -21, -24; X-8). Vétó esetén az érintett lezárt döntés `REOPENED` lesz.
- **Mit blokkol:** A kontrollált pilotot (az M1-részeknél) és a learner release-t (G2 FINAL_RELEASE_QA) minden érintett modulnál. A stagingot nem.
- **Kitől:** DPO / jogi felelős (G2, tracker #2); a runtime-részt az LMS-gazda adja (X-8).

### ADV-E2 — Az activity-szintű adatleltár többi mezője és a „Külön review” sorok (bizonyíték-kapu, G2 release-evidence)
- **Szükséges bizonyíték (nem nyitott döntés):** kitöltött activity-leltár (adatmező, cél, jogalap- és megőrzési sor, törlés, export, harmadik fél, kiskorúakra vonatkozó szabály; ADV §9:207), a nem Moodle-ben vezetett mentori jegyzettel (F-peulák, hubok) és a Google-sablonokkal együtt. Emellett az ADV §3 „Külön review” sorainak írásos eredménye: az M4 peulabemutató (:83), az M5/M6 produktumok (:84), az F-peulák mentori jegyzete, az M5.4 és az M6 Google-sablonja (:87), a TEXT-C mezők (:89). Tárolót és hozzáférési szabályt a repóba nem írunk.
- **Érintett findingok:** M2:BIZT-G3-7 (M2.F:3, :137), M4:BIZT-G2-7, M5:BIZT-G1-4 (ide olvadt: M5:BIZT-G2-9), M6:BIZT-G1-7 (M6.F:3, :223, HUB:14, M6.B:31; ide olvadt: M6:BIZT-G3-6). Beolvadt bizonyíték: M7:BIZT-G3-7 (= M2:BIZT-G3-7; M7.F:3, :138). **Kánon:** ADV §3:33–47, :77–91; §5:151; §9:207, :211.
- **Opciók / ajánlás:** nem döntés. A csoportszűkítés (BIZT-5) és a szervezeti fiók kérdése nem ide tartozik: lásd ADV-1, ADV-10.
- **Következmények:** A leltár a §11 „Meddig őrizzük meg?” listájának és a törlési folyamatnak (§9:211) az alapja.
- **Mit blokkol:** Learner release (G2 RELEASE-EVIDENCE) az M2, M4, M5, M6 és M7 érintett elemeinél. A stagingot nem.
- **Kitől:** az LMS-gazda és a privacy felelős tölti ki; vétó/QA: DPO (tracker #2).

### ADV-E3 — A HUM-PRIV-04 (külső AI) írásos DPO/jogi QA-ja (bizonyíték-kapu, G2)
- **Szükséges bizonyíték (nem nyitott döntés):**
  - a DPO/jogi felelős és a programvezető írásos vétó/QA-ja a HUM-PRIV-04-re (HUM :193);
  - a szervezet ADV §7:188 szerinti szolgáltatói dokumentációja (korhatár, gondviselői feltételek, adatkezelési és tanítási beállítás, admin kontroll, szerződéses/adatfeldolgozói helyzet, a jóváhagyás dátuma);
  - annak igazolása, hogy a „ZDR, ha elérhető” megfelel-e a szolgáltató 18 év alattiakra vonatkozó feltételeinek;
  - a deployer-besorolás jogi QA-ja;
  - a képzők AI-jártassági felkészítésének bizonyítéka (AI Act 4. cikk).
- **Érintett findingok:** M7:BIZT-G1-3; ide olvadt: M7:BIZT-G2-2, M7:BIZT-G2-4. **Kánon:** HUM-PRIV-04 :176–193; ADV §7:177–192; RR G2.
- **Opciók / ajánlás:** nem döntés. A csak másodlagos forrásból ismert „2026/1744”-es állítás a kánonba nem kerülhet (M7-riport).
- **Következmények:** A végpont naplózásáról szóló döntés (ADV-12) és a krízist jelző bevitel kezelése (X-5, M7:BIZT-G1-4) ezt egészíti ki.
- **Mit blokkol:** Learner release (G2) az M7 AI-segédjére; a no-AI utat nem. A stagingot nem.
- **Kitől:** DPO / jogi felelős és programvezető (tracker #2).

## 5. Jogi értelmezés — jogi szakértő

### JOG-1 — Ki tesz külső jelzést és milyen határidővel (Gyvt. 17. §), és mire vonatkozik a hub „büntetőjogi relevancia” mondata (Btk. 209/A. §)
- **Döntés:** Hogyan alkalmazandó a Gyvt. 17. § jelzési és kezdeményezési kötelezettsége a képzést működtető szervezeti jogalanyra és szerepeire (Memuna, helyettes, képző, mentor, 15–17 éves madrih)? Ki tesz külső jelzést, milyen határidővel, és hol a nyilvántartás? Melyik cselekményre vonatkozik a HUB:41 mondata („a haladéktalan, legkésőbb három munkanapon belüli továbblépésnek büntetőjogi relevanciája is lehet”), és a mulasztáshoz kötődik-e?
- **Érintett findingok:** M3:BIZT-G1-8 (HUB:40–43), M3:NYELV-G1-3 (HUB:41 ↔ KAPU:359). Jogi alkérdés más kapuban: M3:BIZT-G2-9 („a Memuna és a hatóság dolga”; lásd X-5). **Kánon:** GK §3.1:29–33 („Nyitott jogi alkalmazási kérdés … a repository nem minősíti önállóan”); §3.2:35–39 (a 209/A. § a 17. § (4a)–(4c) bekezdésében előírt kötelezettség megszegésére épül; automatikus büntetőjogi következményt nem állítunk); §5:121 (jogi szakértő csak a jogi minősítésnél); HUM-SAFE-01 :29–32 (ötlépéses út, incidensnyilvántartás); M3 HUB:42 („az éles használat előtt rögzíteni kell, és a Memunának jóvá kell hagynia”).
- **Opciók:** (a) A külső jelzést a Memuna (vagy a helyettese) teszi a szervezet nevében, a jogász által megadott határidővel; a madrih és a képző belső jelzést tesz. (b) A jogi szakértő szerepenként eltérő kötelezettséget állapít meg (pl. a nagykorú képző vagy mentor személyes kötelezettségét). (c) A HUB:41 mondatát a jogi vélemény szerint pontosítani kell, vagy a KAPU:359 és a GK §3.2 megfogalmazására szűkíteni.
- **Ajánlás:** ajánlás nincs — a jogi szakértő ítélete. Minden opciónál kötött: a madrihra külső jelzési feladat nem írható, a hub mondata nem törölhető, és az ötlépéses út (HUM-SAFE-01) nem változik. Kockázat: a mai HUB:41 megenged olyan olvasatot, amely közel esik a GK §3.2 tilalmához (automatikus büntetőjogi következmény).
- **Következmények:** Biztonság: a jelzési lánc vége (ki és mikor fordul hatósághoz). Tanulás: a HUB:41 mondata. Megvalósítás: a nyilvántartás helye (a G1 tracker #1 vagy új HUM-sor).
- **Mit blokkol:** Learner release (M3): a HUB:42 maga írja elő, hogy éles használat előtt rögzíteni kell (G1, tracker #1). A stagingot és az M0+M1 pilotot nem.
- **Ki hagyja jóvá:** jogi szakértő; jóváhagyás: Memuna (GK §5); a nyilvántartás helyéről a projektgazda.

## 6. Mozgalmi terminológia és ideológia — helyi felelős

### TERM-1 — dugma isit: kiterjed-e a Glosszárium „kerüld” szabálya a kisbetűs, megszemélyesítő alakra
- **Döntés:** A GL:27 szabálya („A megszemélyesített »Dugma Isitnek lenni« formát kerüld”) és a GL:219 nagybetűs tilalma kiterjed-e a kisbetűs „dugma isit vagy / dugma isit madrih” alakra?
- **Érintett findingok:** M0:NYELV-G2-11 (M0.2:26, :417; M0.4:25, :154, :248, :293, :296, :486; HUB:144, :238; M0.4-ILL-03; a HUB:235 projektgazdai itemtörzse). Ide olvadt: M2:NYELV-G1-14 (HUB:53, :83, :260; KAPU:42, :104; az M2.4 fájlneve és címe; Program terv). **Kánon:** GL:25–28, :219; HUM 8. szakasz :472 („egy forma a Glosszárium szerint”), :473 (a belépőkvíz itemjei a projektgazda szövegével); HUM-SOMER-02 :347.
- **Opciók:** (a) Igen, kiterjed: a kisbetűs megszemélyesítés is „dugma isitként viselkedni / személyes példát mutatni” alakra változik. Ez az M2.4 fájlnevét, a linkeket és a HUB:235 itemszövegét is érinti; az átnevezés külön commitban történik. (b) Nem: a szabály csak a nagybetűs, főnévi megszemélyesítésre szól, és a GL:27 pontosítandó. (c) Vegyes: a tanulói címekben marad, a folyószövegben igazodik.
- **Ajánlás:** ajánlás nincs — a projektgazda ítélete (QA: ken-vezető / mozgalmi felelős). Két kánoni forrás ütközik: a GL és a modulok, köztük a projektgazda saját itemtörzse.
- **Következmények:** Tanulásra nincs hatása. Megvalósítás: az (a) esetén fájl-átnevezés (M2.4), valamint a linkek, a PT és a médiaregiszter frissítése; a VO-szöveg csak hanggyártási úton változik. Értékelés: a belépőkvíz itemszövege változik, az answer key nem.
- **Mit blokkol:** Release-kaput nem (a G6 lezárt); csak a szöveg egységessége a tét. Átnevezésnél külön commit kell (az X-19 mintájára).
- **Ki hagyja jóvá:** projektgazda; QA: ken-vezető / mozgalmi felelős.

### TERM-2 — Az SBI „S” elemének kánoni neve: „helyzet” vagy „szituáció”
- **Döntés:** Mi az SBI „S” elemének kánoni magyar neve az M1-ben és a Glosszáriumban: „helyzet” vagy „szituáció”?
- **Érintett findingok:** M1:NYELV-G1-14 (= NYELV-G3-19): „helyzet” áll a GL:138-ban és a HUB:33, :231-ben; „szituáció” a HUB:241-ben, a KAPU:47 rubrikasor nevében, az M1.2:936-ban, az M1.4:482-ben, az M1.A:534-ben és az M1.B:181-ben. **Kánon:** GL:137–138 („Helyzet → Viselkedés → Hatás”); a CLAUDE.md kánonsorrendje (2. modulok ↔ 3. Glosszárium; az ütközés finding, automatikus elsőbbség nincs).
- **Opciók:** (a) „helyzet” mindenhol, a KAPU:47 rubrikasor nevével együtt (a horgonyok nem változnak). (b) „szituáció” mindenhol, a Glosszárium igazodik. (c) Az egyik a fő név, a másik zárójeles szinonima, az első előfordulásnál.
- **Ajánlás:** ajánlás nincs — a modulgazda és az értékelési felelős ítélete, a Glosszárium gazdájával. Szempontok: a terminológia forrása a GL, és az „egy fogalomra egy megnevezés” szabály egységet kér; a rubrikasor nevének változásához az értékelési felelős jóváhagyása kell.
- **Következmények:** Értékelés: a KAPU:47 sor neve változhat, a pontozás nem. Tanulás: egységes terminus.
- **Mit blokkol:** Release-kaput nem; csak a szöveg egységessége a tét.
- **Ki hagyja jóvá:** M1 modulgazda és értékelési felelős, a Glosszárium gazdájával.

### TERM-3 — „transzparens” → „átlátható” az M2.4 gyermekvédelmi szabálymondataiban
- **Döntés:** Az M2.4:208 és :653 szabálymondatában a „transzparens” helyére kerülhet-e a HUM-SAFE-02 / GK §4.2 szava, az „átlátható”?
- **Érintett findingok:** M2:NYELV-G2-3. **Kánon:** GK §4.2:92 (a szabály egyetlen helye; a tananyag „értelemszerűen rövidítve használja”), :94 („indokolt esetben, átlátható módon”), :96 („diszkrét, de átlátható”); HUM-SAFE-02 :49–51. Az M2.4:208 ugyanabban a mondatban már „átlátható módon”-t is használ.
- **Opciók:** (a) „átlátható” mindkét helyen. (b) Marad a „transzparens”.
- **Ajánlás:** (a). Ez a lezárt szabály szóhasználata (GK §4.2:94, :96), és a :208 mondatban ma két szó áll ugyanarra a fogalomra. A szabály tartalma nem változik; a Memuna vétójoga megmarad.
- **Következmények:** Biztonság: egységes szabályszöveg. Tanulásra nincs hatása. Megvalósítás: a látható szöveg változik, ezért pin kell.
- **Mit blokkol:** Release-kaput nem; a Memuna M2.4-átnézése (G1, X-7) ugyanezt a szöveget érinti.
- **Ki hagyja jóvá:** projektgazda, a Memuna vétójával.

### TERM-4 — Az M3.4 kánoni leckecíme (és a HUB:288 link-címkéje)
- **Döntés:** Melyik az M3.4 kánoni címe: a H1-ben álló „Mit tegyél / mit ne tegyél madrihként”, vagy a fájlnévben, a hubban és a MAN-ban álló „Do / Don’t madrihként”? Átnevezés esetén a linkek is vele mozognak.
- **Érintett findingok:** M3:IMPL-G2-15 (H1 ↔ fájlnév ↔ HUB:122, :288, M3.B:151, M3.F:16, MAN:65), M3:NYELV-G1-2 (függő tétel: a HUB:288 „red flag-ek” címkéje a döntéssel együtt változik; objektív rész: .obj). **Kánon:** MAN:65; a tananyag-invariáns: a fájlnév és a rá mutató link együtt mozog, az átnevezés külön commit.
- **Opciók:** (a) A magyar H1 a kánon; a fájlnév, a MAN:65, a hub és a linkek igazodnak (külön `git mv` commit). (b) A „Do / Don’t” marad, a H1 igazodik. (c) Vegyes: a tanulói cím magyar, a belső azonosító és a fájlnév marad.
- **Ajánlás:** ajánlás nincs — az M3 modulgazda dönt. A Do/Don’t írásmódokat a döntéssel egy lépésben kell egységesíteni; a VISUAL-SYSTEM-DECISION zöld/piros színszemantikája marad.
- **Következmények:** Megvalósítás: átnevezésnél külön commit (az X-19 mintájára), a médiaregiszter útvonala és build. Tanulásra nincs hatása.
- **Mit blokkol:** Release-kaput nem.
- **Ki hagyja jóvá:** M3 modulgazda; a link-címkénél az értékelési felelős és a Glosszárium gazdája.

### TERM-5 — Az LMS-M3-05 tanulói neve
- **Döntés:** Mi legyen az LMS-M3-05 tanulói neve? Jelenleg három alak él: M3.4:784 „M3 – modulproduktum: kvuca-helyzet és red flag”, MAN:66 „M3 – Helyzetelemzés”, EGY-07 és :696 „Helyzetleírás red flagekkel”.
- **Érintett findingok:** M3:NYELV-G2-3 (= IMPL-G2-10). **Kánon:** MAN:66; GK:23 („az M3 helyzetleírásába”); a validált finding a „helyzetleírás” terminust jelöli kánoninak; a verifier korlátja szerint a „Helyzetelemzés” nem emelhető a leckébe.
- **Opciók:** (a) „Helyzetleírás”-alapú név, egyszerre a MAN:66-ban, az M3.4:784-ben és az EGY-07-ben. (b) A lecke mai neve marad, a MAN:66 és az EGY-07 igazodik.
- **Ajánlás:** (a), mert a GK:23 és a validált finding a „helyzetleírás” terminust nevezi kánoninak. A pontos megnevezés a modulgazdáé.
- **Következmények:** Tanulás: egységes produktumnév. Megvalósítás: a MAN, a lecke és az EGY-07 együtt változik, az utóbbi build úton.
- **Mit blokkol:** Release-kaput nem.
- **Ki hagyja jóvá:** M3 modulgazda / implementációs felelős.

### TERM-6 — A „Leviatán – év eleji stáb” kártyacímke jelentése
- **Döntés:** Mit jelent a 3. kártya „Leviatán – év eleji stáb” címkéje? A korpuszban a „stáb” képzőket és mentorokat jelent. Ha someres szóhasználat, mi a helyes megnevezés?
- **Érintett findingok:** M3:PED-G3-13 (M3.A:411, :431, KART-02 spec); someres olvasatnál X-14. **Kánon:** HUM-SOMER-02 :341–347 (Leviatán: 13–17); a kulcs (Leviatán / Norming) nem változik.
- **Opciók:** (a) A címke a kvuca saját év eleji szakaszára utal: a „stáb” szó a három helyen cserélendő. (b) Someres szóhasználat: marad, magyarázattal. (c) A címke kimarad, csak a korosztály és a szakasz marad.
- **Ajánlás:** ajánlás nincs — a modulgazda szerzői szándékáról van szó; ha someres szóhasználat, a helyi mozgalmi felelős dönt.
- **Következmények:** Tanulás: a kártya egyértelműsége. Megvalósítás: a KART-02 csak build úton változik. Értékelésre nincs hatása (a kulcs marad).
- **Mit blokkol:** Release-kaput nem.
- **Ki hagyja jóvá:** M3 modulgazda; someres olvasatnál a helyi ideológiai/mozgalmi felelős.

### TERM-7 — A nem mért „saját szavaival elmondja / elmagyarázza” kompetencia: kimeneti vagy reflektív cél
- **Döntés:** Mért kimeneti kompetencia maradjon-e az M2 hub 3. kompetenciájának első pontja („Röviden elmondja, mit jelent számára a cionizmus, szocializmus, humanista zsidóság”, HUB:33) és az M5 „saját szavaival el tudja magyarázni” kompetenciája (HUB:18, :33)? Vagy legyen nem mért, reflektív cél, illetve kapjon mérést?
- **Érintett findingok:** M2:ERT-G1-5 (= PED-G1-6), M5:PED-G1-10 (= ERT-G1-10 (a)). Rokon tétel más kapuban: M4:ERT-G1-5 (X-10). **Kánon:** HUM-PRIV-01 :132 (világnézeti válasz nem lehet fiókhoz kötött szavazás); ADV §3:54, :75; HUM-SOMER-01 :325, :327 (a helyi Ideológiai Kézikönyv a kánon; a képzés nem várja el, hogy mindenki ugyanazt a véleményt képviselje).
- **Opciók:** (a) Nem mért, reflektív cél; a hub-kompetencia átfogalmazva. (b) Mért, de tárolás nélkül (szóbeli vagy peulás formatív megfigyelés), vagy nem személyes tudásként (a pillérek someres jelentése). (c) Új mérőelem (M5: nyílt magyarázó feladat).
- **Ajánlás:** M2: az (a) vagy a (b). A személyes ideológiai jelentés tárolt mérése a kánon szerint nem vezethető be (HUM-PRIV-01, ADV §3:75); a kettő közül a projektgazda választ. M5 (nem ideológiai tartalom: gyakorlás, aktív felidézés): ajánlás nincs — a projektgazda és az értékelési felelős dönt.
- **Következmények:** Értékelés: a kompetencia és a mérés illeszkedése (hub §6). Adatvédelem: az M2-ben nem keletkezik új tárolt ideológiai válasz. Tanulás: a (c) új tartalmat jelent.
- **Mit blokkol:** Release-kaput nem; csak a kompetencia és a mérés illeszkedését, ami későbbi fejlesztés.
- **Ki hagyja jóvá:** projektgazda; QA: helyi ideológiai felelős és DPO (M2), értékelési felelős (M5).

### TERM-8 — Mi számít „someres értéknek” az M2-kapu R2-sorában
- **Döntés:** Mi számít someres értéknek az R2-nél (KAPU:38, :183), és mi az érték és a hangulat határa? Mi a teendő, ha a top 3-ban nincs ilyen? Tanítsa-e az M2.2 a különbséget? Melyik az elsődleges: az M2.B „mai értéke” vagy az M2.2:703 „kiemelt értéke”?
- **Érintett findingok:** M2:PED-G2-2; ide olvadt: M2:ERT-G1-4, M2:ERT-G3-1 (b). **Kánon:** HUM-SOMER-01 :325 (a helyi Ideológiai Kézikönyv a kánon), :327 (alapértékek: béke, emberi jogok, egyenlőség, aktív felelősségvállalás, vitán alapuló párbeszéd); HUM-SOMER-03 :365 (hágsámá); PT:93 (a „kapu lazít” út csak a PT módosításával); M2.2:515.
- **Opciók:** (a) Zárt lista a helyi Ideológiai Kézikönyvből és a HUM-SOMER-01 alapértékeiből; az M2.2 tanítja az érték és a hangulat különbségét. (b) Nyitott definíció, kritériummal (értékítélet, nem hangulat) és értékelői kalibrációval. (c) Az R2 bármely, az M2.2-ben kiemelt értéket elfogad; a „kapu lazít” út csak a PT:93 módosításával járható.
- **Ajánlás:** részleges. A lezárt HUM-SOMER-01 szerint a forrás a helyi Ideológiai Kézikönyv: a lista vagy a kritérium onnan veendő. A rubrika-következményre (ha a top 3-ban nincs ilyen) és a tanítási lépésre ajánlás nincs — az értékelési felelős és a helyi ideológiai felelős dönt.
- **Következmények:** Értékelés: az R2 egyértelmű pontozása (az M2 puha kapu). Tanulás: az M2.2-ben esetleg új lépés, ami új tartalom.
- **Mit blokkol:** RR-kaput nem; a gyakorlatban az M2-kapu értékelői kalibrációja előtt kell.
- **Ki hagyja jóvá:** projektgazda, értékelési felelős, helyi ideológiai felelős; az ERT-G3-1 (b)-nél a modulgazda.

### Lezárt korlátok és „már lezárt / átvezetendő” tételek

Olyan tétel nincs, amelyet egy lezárt projektgazdai döntés szövege szó szerint, teljesen lefedne. A ledger és a verifier
ezeket a lezárt döntések vizsgálata után hagyta BLOCKED_HUMAN, illetve EVIDENCE_GATE állapotban. Részben lefedett tételek: a
lefedett rész átvezetendő, a maradék döntés nyitott, ezért nincsenek beszámolva:

- M2:BIZT-G1-7 · „szervezeti fiók nélkül nincs Google-sablon”: HUM-PRIV-01 (HUM :132; ADV §3:53). Nyitott: van-e fiók (ADV-10).
- Z:BIZT-G1-5 · a hozzájárulás adója kiskorúnál (a résztvevő és a gondviselő együtt, a saját videóra is): HUM 9. szakasz :484; ADV §4:141, §6:171. Nyitott: a folyamat (ADV-14).
- M1:BIZT-G3-8, M5:BIZT-G2-1, Z:BIZT-G1-9 · a fotó lépései és a „személyes telefon nem alapfolyamat”: HUM-PRIV-02 (HUM :147, :151; ADV §6:163–166). Nyitott: a produktumok sorsa, és hogy indokolt-e a fotó (ADV-7).
- M2:NYELV-G2-3 · az „átlátható” kánoni szó: GK §4.2:94, :96. A verifier-korlát szerint a cseréhez a projektgazda döntése és a Memuna vétójoga kell (TERM-3).

## 7. Értékelés és completion — értékelési felelős / projektgazda

> Részvázlat az AP-2026-10-11-01 döntési csomagjához. Forrás: `AUTOPILOT-LEDGER.md` (X-6, X-9, X-16) és a validált
> riportok; új review nem futott, jóváhagyás vagy bizonyíték nincs beírva. A „Mit blokkol” mező a learner release-re
> vonatkozik: a ledger záró QA-sora szerint (Futás, `5fcabea`; nem újraellenőrizve) a futás e tételek nyitva hagyásával
> `READY_FOR_STAGING_BUILD` verdiktet adott, ezért egyik itteni döntés sem staging-build-blokkoló. A „kontrollált pilot”
> csak az M0+M1-re érvényes (PILOT-1); a többi modulnál a learner release ma is `NO-GO`.
>
> **Rövidítések:** PT = `Program terv.md` · HUM = `Emberi jóváhagyás szükséges.md` · MAN = `LMS – activity manifest.md` ·
> RA = `LMS – H5P runtime acceptance.md` · GK = `Gyermekvédelem – release gate.md` · ADV = `Adatvédelem – tanulói adatok
> és AI.md` · GL = Glosszárium · RR = `RELEASE-READINESS.md` · Mx HUB / Mx KAPU = a modul hubja / kapufájlja · Mx.y =
> lecke. VF-Mx = `2026-10-11 Validált findingok – Mx, AP-2026-10-11-01.md` (az M0/M1-nél a 2026-10-10-i B sávos és a
> 2026-10-11-i nyelvi riport). A sorszámok a validált riportok szerintiek; a javító commitok után eltolódhattak.
>
> **Javasolt sorrend (függőségek):** ERT-1 → M3:NYELV-G1-11, M5:IMPL-G1-12 · ERT-26/27/29 → az M5 HOLD-blokkjai ·
> ERT-6 + ERT-34 + X-10 (M6:PED-G1-9) → M6:NYELV-G1-10 · ERT-41 → az M7.4:780–781 HOLD-részei · X-4 (M2:BIZT-G1-8) → ERT-20 ·
> X-10 (M7:PED-G1-8) → ERT-46 · X-5 (M6:PED-G1-8) ↔ ERT-36 · ERT-10 → SIG-2 (M3) · a kulcs- és rubrikadöntések → SIG-4.

**A. Programszintű döntések (több modulra egy döntés)**

### ERT-1 — A H5P Course Presentation completionjének jelentése
- **Döntés:** a H5P-C (Course Presentation) completion azt jelenti-e, hogy a tanuló elérte az összefoglaló diát, vagy a megválaszolást ténylegesen ki kell kényszeríteni?
- **Érintett findingok:** M0:IMPL-3; a döntéssel egy szerkesztésben: M3:NYELV-G1-11 (HUB:252), M5:IMPL-G1-12 (M5.1 „mikor kész”); CP-része: M5:ERT-G1-1; ide olvadt 14 kulcs (lásd Lefedettség). Források: MAN:16 (BSPEC-06: „Receive a grade”, „Hide summary slide” = No; „puszta megtekintés nem elég, ha a lecke választ kér”); `summary-slide.js` (a completion megválaszolás-ellenőrzés nélkül megy, VF-M0 B sáv :135); RA:71 (9. pont); M0.1:13, M0.2:13, M0.3:14, M0.4:14; M3.1:576, M3.2:679, M3.4:9, :509; M4.3:20, M4.4:26, MAN:73, :75; M5 HUB:185, :187; M6 HUB:224, M6.1–M6.3:9; M7.4:14; Z `cp.js` (összefoglaló dia csak feladatelemnél).
- **Opciók:** (a) completion = az összefoglaló dia elérése; a profil és a leckék Completion-sorai ehhez igazodnak; (b) a megválaszolás kikényszerítése szerkezeti átépítéssel (core CP-ben nincs rá beállítás). Mindkét úton: RA 9 negatív eset (összefoglaló dia megválaszolatlan interakciókkal) — az M0:ERT-2 objektív tétele.
- **Ajánlás:** (a). A lezárt BSPEC-06 (D-b) éppen ezt a mechanizmust rögzíti, és nem nyitható újra; a (b) minden CP-sor (M0–Z) átépítését kívánná; az eltérés megengedő irányú (senkit nem blokkol tévesen, adatot nem tesz ki — VF-M0 B sáv). Feltétel: soronként ellenőrizni, hogy van-e feladatelem, különben nincs összefoglaló dia, és a sor sosem teljesül (Z:IMPL-G1-7).
- **Következmények:** a biztonsági reflexet gyakorló dia (pl. M0.2 SLIDE 3) megválaszolás nélkül is teljesít — ezt a QA-nak tudatosan el kell fogadnia; a „befejezte”-analitika a dia elérését jelenti; a fent felsorolt Completion-sorok átírása.
- **Mit blokkol:** M0+M1 pilot: POST-PILOT (VF-M0 B sáv); learner release: a Completion-mondatok és az RA 9 negatív teszt (G3b).
- **Ki hagyja jóvá:** projektgazda (build-spec gazda); QA: értékelési felelős.

### ERT-2 — A pontozatlan választók completion-elve: általános vagy tételes
- **Döntés:** a D-d/D-i elve („a pontozatlan választó nem önálló completion-elem”) általános szabály, vagy csak a felsorolt tételekre (M7.4 SLIDE 4, M0.3 SLIDE 7, M2.2) szól?
- **Érintett findingok:** M0:ERT-3; ide olvadt Z:ERT-G1-6; alkérdésként: Z:BIZT-G1-8 (a), M6:BIZT-G1-4 completion-része, M7:ERT-G2-4 / M7:IMPL-G2-4 (2). Források: MAN:16 (általános mondat); HUM 11. szakasz D-d, D-i; M0.1:13, M0.3:14, M0.4:14; RA:83; Z.1–Z.3 választói; M6.1–M6.3 SLIDE 1; M7.4 SLIDE 3.
- **Opciók:** (a) általános: az M0.1, M0.3 SLIDE 1, M0.4, Z.1–Z.3, M6.1–M6.3 SLIDE 1 és M7.4 SLIDE 3 completion-sorai újradefiniálódnak (az M0.1-nek nem marad választós completion-eleme); (b) tételes: a MAN:16 mondata a D-d/D-i tételeire szűkül.
- **Ajánlás:** (a). A MAN:16 már általános szabályként fogalmaz; a projektgazda két körben (D-d, D-i) ugyanezt az elvet alkalmazta; pontozott véleménykérdés őszinte választ jelölhet hibásnak (RA:83); a D-j a választás tárolását sem kívánja. Feltétel: az M0.1 completion-alapját ugyanebben a döntésben ki kell mondani (az ERT-1-gyel összhangban).
- **Következmények:** completion-sorok átírása négy modulban; a tárolási kérdés (Z:BIZT-G1-8 b, M6:BIZT-G1-4) a DPO-nál marad (X-4). Korlát: a D-d, a D-i és a BSPEC-06 nem nyílik újra.
- **Mit blokkol:** M0+M1 pilot: POST-PILOT, de PILOT-BLOCKER, ha az M0.1 completion a pilotban nem áll be (VF-M0 B sáv); learner release: RA 9 (b).
- **Ki hagyja jóvá:** projektgazda; QA: értékelési felelős.

### ERT-3 — Üres beküldés a kötelező, nem pontozott activityknél (a HUM:457 kiterjesztése)
- **Döntés:** teljesítheti-e a completiont az üres beküldés az M5 diagnosztikus kvíznél (QUIZ-D „attempt submitted”) és a Z.4 Feedbacknél (egyik kérdés sem „Required”)?
- **Érintett findingok:** M5:ERT-G1-1 (QUIZ-D-rész; a CP-rész = ERT-1), Z:ERT-G1-4. Források: M5 HUB:185, :187 („érdemi kitöltéssel”) ↔ MAN:17, :84; Z.4:372–393, :403; Z HUB:62, :200; MAN:22, :24, :112; RA:86 (16. pont); HUM:457 („Üres sablon”); BS-D4 (HUM 10.); HUM-PRIV-03.
- **Opciók:** (a) igen, a tanulói szöveg pontosul („a beküldés ténye számít”); (b) nem: a Z.4-nél legalább egy „Required” kérdés, a QUIZ-D-nél az érdemi kitöltés kikényszerítése vagy emberi ellenőrzése; (c) activitynként eltérő.
- **Ajánlás:** (c): a QUIZ-D-nél (a), a Z.4-nél (b). A QUIZ-D diagnosztikus, nem kapuzó (PT:273), a profilja (MAN:17) a beküldést rögzíti, elég a hub mondatát igazítani; a Z.4 Feedback a program kötelező záró eleme (HUM-PRIV-03), és a BS-D4 szerint ahol a nem-üresség strukturálisan kikényszeríthető, ott ezt kell vizsgálni — a „Required” ilyen.
- **Következmények:** Z.4: a név nélküli megjelenítés és a HUM-PRIV-03 mondata nem változik, de a válaszadás kötelezővé válik (DPO/programvezető QA); RA 16. pont tesztje.
- **Mit blokkol:** learner release (M5, Z); G3b (RA 16.).
- **Ki hagyja jóvá:** projektgazda (QUIZ-D, build-spec); értékelési felelős (Z.4); vétó/QA: DPO + programvezető (Z.4).

### ERT-4 — A KAPU item-bankja / fogalmi kvíze: tanulói activity vagy szerzői pool
- **Döntés:** a kapufájlban leírt item-bank, illetve fogalmi kvíz tanulói Moodle-activity legyen saját manifest-sorral, vagy szerzői itempool maradjon (és a szöveg ne ígérjen activityt)?
- **Érintett findingok:** M1:ERT-G2-4 (M1 KAPU §3, szabad szöveges Item 5–6), M2:PED-G1-9 (M2 KAPU B., 10 item). Források: M1 KAPU:11, :28, :186–200, :308; MAN:35, :45–51; M1 HUB:248; PT:271 · M2 KAPU:26, :54–56; M2 HUB:179; minta: LMS-M5-06, LMS-M6-06 (QUIZ-D).
- **Opciók:** (a) activity: új §2-sor (profil, completion, „Kötelező” = nem, privacy; az M1 szabad szöveges itemeire DPO-besorolás); (b) szerzői pool: a KAPU/HUB „LMS” sorai és ígéretei igazodnak; (c) vegyes: az M2 zárt kvíze activity, az M1 pool.
- **Ajánlás:** nincs — projektgazda + értékelési felelős ítélete (formatív gyakorlás ↔ új build- és adatkör). Kockázat: az (a) az M1-nél új, tárolt szabad szöveges adatkört nyit (DPO, X-4); a (b)-nél a hub formatív ígérete kiesik.
- **Következmények:** (a) manifest-sor és RA-teszt; (b) csak szövegigazítás.
- **Mit blokkol:** learner release (M1, M2); M0+M1 pilot: POST-PILOT („sor nélkül a pilot-build nem hozza létre”).
- **Ki hagyja jóvá:** projektgazda + értékelési felelős; DPO, ha activity.

### ERT-5 — Az éles kapukvízek Review options-e és a bukás indoklása
- **Döntés:** mit lásson a madrih az M3 és az M7 kapukvízének első és javító próbálkozása után (pontszám, helyes válasz, opciószintű visszajelzés, a bukás oka), és kell-e az M3-ban slotonként validált itemváltozat?
- **Érintett findingok:** M3:ERT-G1-11 (= PED-G1-6, IMPL-G1-11, ERT-G3-1, az IMPL-G3-7 emberi része), M7:IMPL-G1-9. Források: M3 KAPU:38 (a javító ugyanazt a 12 itemet kapja), :140; MAN:18 (QUIZ-M); M3 HUB:234–236; M3.F:30, :187 · M7 KAPU:50–53, :411; M7.F:142, :207 · HUM:463 („a kritikus követelményeket megnevezzük, a kvíz kulcsát nem”); docs.moodle.org/405 (a „Right answer” felfedi a helyes választ).
- **Opciók:** (a) beküldés után pontszám és a hibázott kritikus követelmény / téma megnevezése, a „Right answer” és az opciószintű visszajelzés csak a javító próbálkozás lezárása után; (b) azonnali teljes visszanézés; (c) slotonkénti, validált itemváltozat (M3), amellyel a kulcs felfedése nem rontja a javítót.
- **Ajánlás:** (a). A javító próbálkozás ugyanazt a 12 itemet kapja (M3 KAPU:38), így az első után felfedett kulcs a második próbálkozást érvénytelen bizonyítékká tenné; a HUM:463 a kritikus követelmény megnevezését előírja, a kulcsét kizárja (a próbálkozás utáni nézetre ez új alkalmazás, ezért döntés). A (c) új itemtartalom és Memuna-jóváhagyás (KAPU:38).
- **Következmények:** a bukás oka témaszinten látszik, az F-peula erre épít (M3.F, M7.F igazodik); a QUIZ-M profil és a KAPU §0 rögzíti; kulcs, küszöb, próbálkozásszám nem változik.
- **Mit blokkol:** learner release (M3, M7 éles kapu); G3a beállítás, G3b teszt.
- **Ki hagyja jóvá:** értékelési felelős; kritikus slotnál és a kulcs megjelenítésénél a Memuna is (M3).

### ERT-6 — A diagnosztikus kvízek jelzése, próbálkozásszáma és Review options-e
- **Döntés:** az M5 fogalomkvíznél és az M6 szcenárió-kvíznél melyik próbálkozás adja a tanulói és a stáb-jelzést, hány próbálkozás legyen az M5-ben (2 vagy 3), mi a Review options, és legyen-e fogalomcsaládonkénti jelzés (M5)?
- **Érintett findingok:** M5:ERT-G1-4 (= IMPL-G1-8), M6:ERT-G1-7, M6:IMPL-G1-3 (Review options-sor, HOLD #25), M6:NYELV-G1-10 (KAPU:437 egybeírás a végszövegen, HOLD #57; az ERT-34-től és az X-10 M6:PED-G1-9-től is függ). Források: M5 KAPU:24, :30, :313–314; M5 HUB:180–181, :205–208; MAN:17 („a forrás szerinti, egyébként 2–3”), :84; PT:265 · M6 KAPU:23, :38, :48, :71, :346, :437; M6 HUB:202, :242, :247; MAN:92; precedens: MAN:44 (M0).
- **Opciók:** (a) az első próbálkozás adja a jelzést, a többi gyakorlás; (b) a legjobb vagy az utolsó próbálkozás; mellette: M5 „Attempts allowed” 2 vagy 3; fogalomcsaládonkénti jelzés igen/nem; Review options: „Immediately after the attempt” → „Whether correct”, „Specific feedback”, „General feedback” = Yes (a döntéssel együtt beírható objektív alpont).
- **Ajánlás:** (a) az első próbálkozás: ez a manifest saját M0-mintája (MAN:44), és diagnosztikus értéke csak a visszajelzés előtti próbálkozásnak van. A próbálkozásszám és a családonkénti jelzés: értékelési felelős ítélete (a kánon csak 2–3-as sávot ad).
- **Következmények:** a kvízek formatívak maradnak (≥10/12 jelzőküszöb, itemek, kulcsok, az M6 korlátlan próbálkozása változatlan); a pool bővítése (N-M6-18) külön döntés.
- **Mit blokkol:** learner release (M5, M6); G3a beállítás.
- **Ki hagyja jóvá:** értékelési felelős + projektgazda (M5); a beállítást az LMS-gazda rögzíti.

### ERT-7 — A disztraktor-elv kiterjesztése a lecke-checkekre és a diagnosztikus item-bankokra
- **Döntés:** kiterjed-e a HUM 8. „Új kvíztételek” elve (valódi tévképzetre épülő, a kulcsot el nem áruló elosztó) a lecke-checkekre és a diagnosztikus item-bankokra; ha igen, a szerző cseréli az elosztót, a ✅ változatlan?
- **Érintett findingok:** M3:ERT-G2-7 (+ builder félkövér-tilalom), M5:ERT-G2-8, M6:ERT-G2-7, M6:ERT-G1-10 (alternatíva: a KAPU:72 szűkítése; a 12. item B-opciója az ERT-36-tal). Források: HUM:473; M3.3:326–329, :931–934, :962–965; M3.4:650–653; M3 KAPU:93, :95 · M5.3:557, :591, :606; M5 KAPU:32 · M6.2:965; M6.3:802–805, :1151–1154; M6.4:984–987; M6 KAPU:72, :306–309; M6.1:1417–1420; M6-NY-D8 (nem tiltja).
- **Opciók:** (a) teljes kiterjesztés minden checkre és item-bankra; (b) csak a modul saját disztraktor-elve alá eső item-bankokra (M5 KAPU:32, M6 KAPU:72) és a gyermekvédelmi tartalmú lecke-itemekre; (c) nincs kiterjesztés, a checkek formatív gyakorlásként maradnak (az M6 KAPU:72 szűkül).
- **Ajánlás:** (b). Az M5 KAPU:32 és az M6 KAPU:72 a modul saját szabálya, ezt az item-bank itemjeinek teljesíteniük kell; a gyermekvédelmi lecke-itemeknél (M3.3/M3.4) a téves reflex rögzülése indokolja; a többi check tétje kicsi (nincs pass-küszöb), és a futás korlátja a szükségtelen módosítás kerülése (ledger, Futás, „Korlátok” 2).
- **Következmények:** új elosztószöveg szerzői úton, értékelési QA-val (gyermekvédelmi itemnél Memuna); a ✅ és a kérdésszöveg nem változik.
- **Mit blokkol:** learner release-t formálisan nem (nem kapuzó itemek); az M6 diagnosztikus item-bank a saját szabálya miatt a release előtt javítandó.
- **Ki hagyja jóvá:** értékelési felelős; gyermekvédelmi itemeknél a Memuna is.

### ERT-8 — Puha kapuk (M2, M4): mi váltja ki az F-peula-ajánlást, mit jelent a „kapu nem teljesült”
- **Döntés:** a puha kapuknál mi váltja ki az F-peula-ajánlást, mit jelentenek a tanulói „ha a kapu nem teljesült” mondatok, és hol rögzül az M4 rubrikaszintje?
- **Érintett findingok:** M2:QA-PED-1 (M2.F:205, KAPU:253, a helylista: HUB:161; M2.F:20, :37, :207, :368; M2.B:383; grep-pel: KAPU:48, M2.1:46, M2.2:59, M2.3:95, M2.4:45, HUB:39, :229), M4:ERT-G2-4 (= IMPL-G2-9). Előzmény: M2:IMPL-G1-5 FIXED (`cee9849`). Források: MAN:61 („a puha kapu rubrika-küszöbe formatív, nem feltétel”), :78, :173; M2 KAPU:24; GL:186, :188, :194; M4 HUB:128, :138; M4.F:26–27, :166, :265; HUM:456 („Puha és éles kapu”), HUM 9. „Kapueredmény-címkék”.
- **Opciók:** (a) az F-ajánlást a formatív rubrika-küszöb alatti eredmény váltja ki (az M4-nél a Kapu 1 gyenge eredménye is, ERT-24), a „kapu nem teljesült” helyére „a rubrika-küszöb alatt maradtál, az F-peula ajánlott” kerül, a „Még nem teljesítve” az üres vagy értelmezhetetlen beadásé marad (MAN:61, :78); (b) F-ajánlás csak „Még nem teljesítve” esetén; (c) mindkettő, külön mondattal. Az M4 rubrikaszintje: LMS-M4-05 rubrika vagy LMS-M4-10 „Feedback comments”.
- **Ajánlás:** a kiváltásra (a): a lezárt HUM:456 (a puha kapu formatív, nem blokkol) és a HUM 9. egyetlen címkepárja mellett a „kapu nem teljesült” csak a „Még nem teljesítve” lehet, ami a MAN:61/:78 szerint az üres vázlaté; a gyenge, de nem üres munka támogatása így csak a formatív küszöbhöz köthető. A rubrikaszint helyére ajánlás nincs — build-spec gazda.
- **Következmények:** a helylista tanulói mondatainak és a GL:186-nak az átfogalmazása; küszöbszám, kaputípus, 1+1 beadás nem változik; a mentori visszajelzés helye adatkör (DPO).
- **Mit blokkol:** learner release (M2, M4).
- **Ki hagyja jóvá:** projektgazda; QA: értékelési felelős, programvezető; az adatkörről DPO.

### ERT-9 — Az éles kapus Assignment (ASSIGN-M) saját completionje: a D-h minta kiterjesztése
- **Döntés:** az ASSIGN-M sorok (LMS-M1-05 és az M3/M5/M6/M7 megfelelői) saját completionje kövesse-e a D-h kétállapotú mintáját: SUBMITTED = leadás, CONFIRMED = a GATE-CP sor?
- **Érintett findingok:** M1:IMPL-G2-2. Források: MAN:20 (ASSIGN-M profil), :25, :50, :51 (LMS-M1-06 GATE-CP), :165, :167 („Fontos”); M1 KAPU:297–301, :306; M1.4:542–553; HUM 11. D-f (szó szerint nem fedi: ott a manifest nem ad checkpointot), D-h.
- **Opciók:** (a) igen: „Make a submission” (`completionsubmit`), jegyalapú completion kikapcsolva, a megerősítés a GATE-CP-n; (b) „Receive a passing grade” az Assignmenten, a GATE-CP mellett; (c) marad a profil beállítás nélkül (ez a nyitott állapot).
- **Ajánlás:** (a). A D-h szerint a két állapot nem mosható össze; a megerősítést a BSPEC-01 óta a GATE-CP hordozza (MAN §4, LMS-M1-06), a downstream unlock is ahhoz kötődik, így az Assignment saját completionje a SUBMITTED-állapot lehet. Korlát: Grade to pass = 5, Maximum grade = 8 és a konjunkciós küszöb nem változik.
- **Következmények:** egységes beállítás öt modulban; RA 8. pont állapotmátrixa; az „Mx complete” a GATE-CP-hez kötődik.
- **Mit blokkol:** M0+M1 pilot: POST-PILOT (az M2 nyitása az LMS-M1-06-hoz kötött); learner release: G3a beállítás, G3b teszt.
- **Ki hagyja jóvá:** projektgazda / build-spec gazda.

### ERT-10 — Az M3 kritikus itemkörének bővítése: jóváhagyói rend és az ITEM 10
- **Döntés:** ki hagyja jóvá az M3 gyermekvédelmi kapu kritikus itemkörének bővítését, és legyen-e kritikus item az ITEM 10 (madrih–hanih párkapcsolat)?
- **Érintett findingok:** M3:QA-BIZT-1 (jóváhagyói rend), M3:BIZT-G1-7 (ITEM 10; az objektív szerepjavítás M3:ERT-G1-7 FIXED, `3ae0c09`). Források: M3 KAPU:74–78 (a :78 ma: „projektgazdai döntés; QA: értékelési felelős + Memuna”), :38; PT:272 (kritikus itemek: 2, 4, 7, 9); GK:120 („A gyermekvédelmi jóváhagyás egyetlen felelőse a Memuna”); RR:39; HUM:473, :481.
- **Opciók:** jóváhagyói rend: (a) projektgazdai döntés Memuna-vétóval (KAPU:78); (b) Memuna-jóváhagyás (GK:120); (c) mindkettő: Memuna írásos jóváhagyása és projektgazdai döntés (PT:272 módosítása). ITEM 10: (i) kritikussá válik (ötelemű konjunkció); (ii) lefedettségi item marad.
- **Ajánlás:** a rendre (c): a kritikus itemkör egyszerre gyermekvédelmi tartalom (GK:120, RR:39: egyetlen jóváhagyó a Memuna) és a PT:272-ben rögzített kapufeltétel (kánoni sorrend 1., projektgazdai hatáskör). Az ITEM 10-re ajánlás nincs — Memuna + értékelési felelős ítélete; kockázat: (i) szigorítja a kaput, (ii) mellett az ITEM 10 rossz válasza ≥10/12-vel átmehet (KAPU:78).
- **Következmények:** (i) esetén a PT:272, a KAPU §1.2, a kézi kritikus-item-ellenőrzés (KAPU:76) és az RA-teszt bővül; a ≥10/12 nem változik.
- **Mit blokkol:** learner release (M3 éles kapu); a SIG-2 küszöb-megállapítása az itemkör ismeretében teljes.
- **Ki hagyja jóvá:** projektgazda + Memuna; QA: értékelési felelős.

**B. Modulszintű döntések**

### ERT-11 — M0: a belépőkvíz projektgazdai itemszövegének nyelvi javítása
- **Döntés:** javítható-e nyelvileg a belépőkvíz projektgazdai itemszövege (7. item „a completion állapotát” különírása, a 4. item alanya), a kulcs és a tartalom változatlanul?
- **Érintett findingok:** M0:NYELV-G1-14. Források: M0 HUB:180 (projektgazdai szöveg, 2026-10-02), :223–230 (4. item), :254, :258, :260 (7. item, a ✅ C opció is); HUM:473; BS-D5 (HUM 10.: a 4. item D) disztraktora projektgazdai döntéssel javítva, kulcs változatlan).
- **Opciók:** (a) igen, csak nyelvi javítás (egy alak: „completion-állapot”; egyértelmű alany), a ✅ szövegében is; (b) nem, a szöveg szó szerint marad.
- **Ajánlás:** (a). A verifier szerint a „completion állapotát” valós helyesírási hiba; a szöveg gazdája a projektgazda, és a BS-D5 mutatja, hogy a kulcs érintetlenül hagyásával módosíthatja; a QA a SIG-1-gyel egy menetben elvégezhető.
- **Következmények:** látható szöveg változik (`--pin-visible`); kulcs és disztraktortartalom nem.
- **Mit blokkol:** csak későbbi fejlesztés (next-version); a futó pilotot nem.
- **Ki hagyja jóvá:** projektgazda; QA: értékelési felelős.

### ERT-12 — M1: valós vagy csak kitalált helyzet az LMS-M1-07 mini-SBI-ben (N-1)
- **Döntés:** kerülhet-e az LMS-M1-07 (M1.3 saját mini-SBI; tárolt, névhez kötött TEXT-C) mezőbe valós, névtelenített helyzet, vagy — mint az M1.4-ben — csak kitalált?
- **Érintett findingok:** M1:BIZT-G2-1 (P0; + PED-G2-12); ráépül az M1:BIZT-G2-3 (lásd X-5). Források: M1.3:886, :902 (NAR-05), :1059 (NAR-06); M1 HUB:117; MAN:48 („nyitott”); M1.4:457; a D-a…D-d jegyzőkönyv :85 („Változatlanul nyitva … N-1”); BSPEC-02 leltár :244, :278; ADV §2:29, §3:82; HUM:462 („Esetalapú kapuproduktum”: közeli, de a kapuproduktumra szól, nem fedi).
- **Opciók:** (a) valós, névtelenített helyzet (DPO-jóváhagyott adatkör, megőrzés, hozzáférés; tájékoztató: „név és felismerhető részlet nélkül”); (b) csak kitalált helyzet (szövegigazítás: M1.3:886, NAR-05/06, HUB:117, MAN:48).
- **Ajánlás:** (b), a DPO vétójának fenntartásával. Ugyanennek a tanulónak az M1.4 kapuja csak kitalált helyzetet enged, és a HUM:462 a kapuproduktumra kimondja: „valós eset névtelenítve sem”; tárolt, névhez kötött mezőben ez az adattakarékos út. Ez a lezárt döntés új alkalmazása, ezért kell a döntés.
- **Következmények:** nem kerül tárolásra harmadik személyre vonatkozó valós adat; (b)-nél szöveg + VO (NAR-05/06 hanggyártási úton).
- **Mit blokkol:** kontrollált pilot (M0+M1): az LMS-M1-07 megnyitása (PILOT-BLOCKER); learner release (G2).
- **Ki hagyja jóvá:** projektgazda; vétó: DPO.

### ERT-13 — M1: az SBI kánoni hossza
- **Döntés:** az SBI kánoni hossza 2–3 vagy 1–2 mondat?
- **Érintett findingok:** M1:PED-G2-1 (= ERT-G1-4, ERT-G2-3, ERT-G3-7). Források: PT:106, :138, :142; M1 HUB:33, :39, :125, :132; M1 KAPU:21, :197, :200, :260 ↔ M1.3:45, :801; M1.4:10, :426, :450, :461, :491; M1.B:359; KAPU 4.1 minta.
- **Opciók:** (a) 2–3 mondat; (b) 1–2 mondat.
- **Ajánlás:** (a). A kánoni sorrendben első Program terv háromszor, a hub és a KAPU-előírás is 2–3 mondatot ír; a rubrika a hosszt nem pontozza, így a döntés csak a tanulói útmutatást igazítja. (A verifier szerint ezt önhatalmúlag nem lehet választani: projektgazdai döntés kell.)
- **Következmények:** lecke- és peulahelyek egységesítése, az M1.4-ben „SBI-mondat” helyett „SBI”, a KAPU 4.1 minta igazítása; VO (M1.4:434) hanggyártási úton; értékelési hatás nincs.
- **Mit blokkol:** M0+M1 pilot: POST-PILOT; learner release (tanulói szöveg).
- **Ki hagyja jóvá:** projektgazda / modulgazda + értékelési felelős.

### ERT-14 — M1: a kész minta-SBI visszaadásának értékelői szabálya
- **Döntés:** kapjon-e a M1 KAPU §5 értékelői szabályt arra az esetre, ha a beadás az M1.4:475–476 kész minta-SBI-t (a B kapuhelyzetre) szó szerint vagy közel szó szerint visszaadja, és cserélődjön-e a példa?
- **Érintett findingok:** M1:ERT-G2-1 (= PED-G2-2). Források: M1.4:290–292, :456, :457, :473–476; M1 KAPU §1, §5, :21.
- **Opciók:** (a) értékelői szabály a §5-ben; (b) a példa cseréje kapuhelyzeten kívüli kánoni példára (M1.4:290–292); (c) mindkettő.
- **Ajánlás:** (c), de legalább (a): a verifier szerint „a példacsere önmagában nem elég” (a saját helyzetes út, M1.4:457, bármely mintát átengedi), értékelői szabály kell; a szabály tartalma az értékelési felelős ítélete.
- **Következmények:** a hamis átengedés kizárása; a küszöb (soronként ≥1 ÉS ≥5/8), a szintek és a ✅ változatlan.
- **Mit blokkol:** M0+M1 pilot: POST-PILOT (a pilot alatt repón kívüli értékelői utasítással kezelhető); learner release (M1 kapu).
- **Ki hagyja jóvá:** értékelési felelős; QA: módszertani lektor.

### ERT-15 — M1: B-sor ↔ hangnem-sor, kettős levonás
- **Döntés:** a B-sor („becsúszik egy ítélkező szó”) és a hangnem-sor („enyhe minősítés”) ugyanazt az enyhe minősítést vonja-e le, és a KAPU 4.1 határeset-mintájának melyik indoklása érvényes?
- **Érintett findingok:** M1:ERT-G2-2 (= PED-G2-7). Források: M1 KAPU:25, :36, :64, :81, :86, :126 („nincs kettős súlyozás”), 4.1 (:265–269); HUM:459 (csak a szintneveket zárja le).
- **Opciók:** (a) csak a B-sor vonja le; (b) csak a hangnem-sor; (c) szándékos kettős levonás (ekkor a KAPU:81 és :126 javítandó); mellette: hová tartozik a „sokat beszéltél bele” típus.
- **Ajánlás:** részleges: (a) vagy (b) — a KAPU:126 saját elve kizárja a (c)-t; hogy melyik sor, az értékelési felelős + módszertani lektor ítélete.
- **Következmények:** a 4.1 minta indoklása és verdiktje igazodik; szintnevek, 4 sor, küszöb változatlan; a pilot alatt kalibrációs egyeztetés kell (téves bukásnál második értékelő, KAPU:25).
- **Mit blokkol:** M0+M1 pilot: POST-PILOT; learner release (M1 kapu).
- **Ki hagyja jóvá:** értékelési felelős + módszertani lektor.

### ERT-16 — M1: a KAPU:55 S-„Erős” horgonyának olvasata
- **Döntés:** a M1 KAPU:55 S-„Erős” horgonyának („idő ÉS/VAGY hely ÉS a helyzet szakasza”) melyik olvasata érvényes?
- **Érintett findingok:** M1:NYELV-G2-4; ráépül az M1:ERT-G2-5 S-sora (M1.4:482, :585; az objektív rész `M1:ERT-G2-5.obj` FIXED, `ed4f52d`). Források: M1 KAPU:36, :55, :67, :75, :264; M1.4:482, :586.
- **Opciók:** (a) (idő vagy hely, vagy mindkettő) ÉS a helyzet szakasza; (b) idő, vagy (hely ÉS a helyzet szakasza).
- **Ajánlás:** nincs — értékelési felelős ítélete (a 4.1–4.2 minta nem dönti el; rubrikaszint jelentése).
- **Következmények:** az M1.4 S-sora utána igazodik (`--pin-visible`); szintnevek, pontok, küszöb változatlan.
- **Mit blokkol:** learner release (M1 kapu); a pilotot nem (POST-PILOT).
- **Ki hagyja jóvá:** értékelési felelős.

### ERT-17 — M1: a KAPU:79 zárójelének jelentése
- **Döntés:** a M1 KAPU:79 4. rubrikasor vezérkérdésének „(megtartható kapcsolatban)” zárójele külön szempont (a kapcsolat megőrzése) vagy magyarázat?
- **Érintett findingok:** M1:NYELV-G2-8. Forrás: M1 KAPU:79.
- **Opciók:** (a) külön, pontozott szempont; (b) magyarázat.
- **Ajánlás:** nincs — értékelési felelős / modulgazda ítélete; a viselkedés ↔ személy logika semmiképp nem változik.
- **Következmények:** (a)-nál a szintleírások pontosítása; (b)-nél csak nyelvi átírás.
- **Mit blokkol:** learner release (M1 kapu).
- **Ki hagyja jóvá:** értékelési felelős / modulgazda.

### ERT-18 — M2: mi adja az LMS-M2-03 (M2.4 H5P-C) grade-jét
- **Döntés:** mi adja az LMS-M2-03 grade-jét és completionjét, ha a MAN:56 szerint a pollok „rögzítés nélküliek”, a H5P-C profil viszont „Receive a grade”?
- **Érintett findingok:** M2:IMPL-G2-1 (= PED-G2-6, ERT-G2-1, BIZT-G2-7). Források: M2.4:3–19, :55, :189–204, :331–342; MAN:16, :56–58; RA:72; M2 HUB:178; HUM 9. „Az M2.1 identitás-kör kérdése” (rögzítés kikapcsolva); D-i; D-j.
- **Opciók:** (1) a pollok követett feladatok (minden opció helyes), a MAN:56 a DPO jóváhagyásával igazodik — a SLIDE 1-en ütközik a GK §4.2 kulcsával (Memuna); (2) a pollok rögzítés nélküli szövegelemek, új completion-bázissal: (2a) az LMS-M2-09 unlockja nem a H5P-re épül, (2b) BSPEC-06-kivétel, (2c) nem érzékeny, pontozott ellenőrző elem (új tartalom).
- **Ajánlás:** a (2) irány; a completion-bázis (2a vagy 2b) a build-spec gazda döntése. A MAN:56, a HUM 9. M2.1-es döntése, a D-i és a D-j egy irányba mutat (önbevallás nem tárolt és nem completion-elem); az (1) adatkört nyit és Memuna-kérdést vet fel.
- **Következmények:** nincs tárolt poll-válasz; BSPEC-06-eltérés vagy unlock-átkötés; a (2c) csak szerzői úton.
- **Mit blokkol:** learner release (M2); G3a, G3b; a DPO-rész X-4.
- **Ki hagyja jóvá:** projektgazda (build-spec gazda); a tárolásról DPO.

### ERT-19 — M2: beleszámít-e az „ÉN” az R1 „legalább 3 kör” feltételébe
- **Döntés:** beleszámít-e az „ÉN” a M2 KAPU R1 és A.1 „legalább 3 kör” feltételébe?
- **Érintett findingok:** M2:PED-G1-11. Források: M2 KAPU:37, :182, :214–215; M2 HUB:25; M2.1:261, :263–267, :473–475.
- **Opciók:** (a) igen, az ÉN is kör (a KAPU mai olvasata); (b) nem, az ÉN a középpont (az M2.1 modellje), 3 további kör kell.
- **Ajánlás:** nincs — értékelési felelős ítélete. Kockázat: (a) a lecke modelljével ütközik, (b) szigorítja az R1-et.
- **Következmények:** a KAPU A.1, a D. sablon, a HUB:25 és a NYELV-G1-4 példája igazodik; küszöbszám nem változik.
- **Mit blokkol:** learner release (M2 puha kapu).
- **Ki hagyja jóvá:** értékelési felelős.

### ERT-20 — M2: a HUB:244 határszabály-mutatójának alsó határa
- **Döntés:** ≥2 vagy ≥3 legyen a M2 HUB:244 „legalább 2–3” mutatójának alsó határa?
- **Érintett findingok:** M2:NYELV-G1-13. Források: M2 HUB:37, :90, :183, :190, :244; LMS-M2-09.
- **Opciók:** (a) ≥2; (b) ≥3; (c) tárgytalan, ha a DPO szerint a mutató kikerül (M2:BIZT-G1-8, X-4).
- **Ajánlás:** előbb az X-4 (M2:BIZT-G1-8) döntése; ha a mutató marad, ajánlás nincs — modulgazda + értékelési felelős.
- **Következmények:** programanalitika; a completion és a kompetencia szövege nem változik.
- **Mit blokkol:** csak későbbi fejlesztés (programanalitika).
- **Ki hagyja jóvá:** modulgazda + értékelési felelős.

### ERT-21 — M3: R1 és R2 feltárás nélküli helyzetben
- **Döntés:** elfogadja-e az M3 R1 sora a határproblémákat (ken-szabálysértés, „kedvenc hanih”), mi teljesíti az R2-t feltárás nélküli helyzetben, és vonatkozik-e rá az R2 „meg sem említi” blokkoló szintje?
- **Érintett findingok:** M3:ERT-G2-2 (= PED-G2-2), M3:ERT-G3-8. Források: M3.4:465, :487–488, :824–830, :834; M3 KAPU:315, :323–325; M3.3:973; M3.B:404, :511.
- **Opciók:** (a) az R1 elfogadja a határproblémát, és feltárás nélküli helyzetben a „meg sem említi” szint nem alkalmazandó (KAPU §2.1 kalibrációs megjegyzés); (b) az R1 csak „valódi red flag” (KAPU:323), az R2 mindig alkalmazandó — a sablon példái és az M3.B 4. kártyája titoktartási elemet kap; (c) vegyes.
- **Ajánlás:** nincs — értékelési felelős + Memuna ítélete (gyermekvédelmi rubrikaszint). Kockázat: a sablon saját példáját követő tanuló ma elbukhat az éles kapun (P1).
- **Következmények:** utána legfeljebb a :825–827 példalista két címkézett sorra bontása, új példa nélkül; szintek, blokkoló R2/R4, küszöb változatlan.
- **Mit blokkol:** learner release (M3 éles kapu); a SIG-2 kalibrációja erre épül.
- **Ki hagyja jóvá:** értékelési felelős + Memuna; rubrikaszint: projektgazda.

### ERT-22 — M3: az életszerűség a blokkoló R4-ben
- **Döntés:** maradjon-e az életszerűség a blokkoló R4 sorban, vagy kerüljön más sorba, és kapjon-e saját sablonsort?
- **Érintett findingok:** M3:ERT-G1-5 (= PED-G1-7). Források: M3 KAPU:34, :308, :315, :317, :326, :340; PT:272 („R4 (nem nyomoz / nem konfrontál) blokkoló”); M3 HUB:253.
- **Opciók:** (a) marad az R4-ben, saját sablonsorral és egységes megnevezéssel; (b) másik, nem blokkoló sorba kerül.
- **Ajánlás:** (b): a kánoni sorrendben első PT:272 az R4-et a „nem nyomoz / nem konfrontál” biztonsági mérce miatt teszi blokkolóvá; az életszerűség nem biztonsági mérce, blokkoló soron téves biztonsági bukást okozhat. (Rubrikaszint-módosítás, ezért projektgazdai döntés.)
- **Következmények:** (a) új sablonszöveg szerzői úton; (b) rubrika-átrendezés, a pontsáv és a blokkoló logika egyébként változatlan.
- **Mit blokkol:** learner release (M3 éles kapu).
- **Ki hagyja jóvá:** projektgazda (rubrikaszint); QA: értékelési felelős + Memuna.

### ERT-23 — M3: az M3.2 párosító kulcsa
- **Döntés:** az M3.2 párosító kulcsa szigorú legyen, vagy jelenetenként felsorolt elfogadott kvucákkal, mindkét formában azonos kulccsal?
- **Érintett findingok:** M3:IMPL-G2-14 (= ERT-G2-6, a PED-G2-4 kulcs-része). Források: M3.2:599 (EGY-01), :628 (EGY-02), :662–668 (kulcs), :670 (a fejlesztőre bízza).
- **Opciók:** (1) szigorú kulcs, a :670 törlődik; (2) jelenetenként felsorolt elfogadott kvucák.
- **Ajánlás:** nincs — értékelési felelős + M3 modulgazda (tartalmi ítélet: mely jelenetek többértelműek).
- **Következmények:** a két H5P-forma azonos kulcsot kap; a :670 törlése nem objektív javítás.
- **Mit blokkol:** csak későbbi fejlesztés (az M3.2 nem kapus elem).
- **Ki hagyja jóvá:** értékelési felelős + M3 modulgazda.

### ERT-24 — M4: a Kapu 1 jelzése és a „gyenge eredmény” határa
- **Döntés:** mi az M4 Kapu 1 (M4.3 kapukvíz) jelzése, és hol a „gyenge eredmény” határa?
- **Érintett findingok:** M4:PED-G1-2 (= ERT-G1-8; a `PED-G1-2.obj` FIXED: `4119d16`, `b429420`). Források: M4 HUB:125–128, :165, :171; M4.3:20, :186–191, :398, :440, :497; MAN:73; PT:109, :246, :259, :273–274.
- **Opciók:** (a) a CP pontozott interakcióinak eredménye, rögzített határral; (b) a SLIDE 5 itemjei a próbálkozás-riportban, kimondott mentori teendővel; (c) egyéni küszöb nélküli analitikai jelzés.
- **Ajánlás:** nincs — értékelési felelős + projektgazda (valódi küszöbdöntés); az (a) határa az ERT-8 F-ajánlásához kötődik.
- **Következmények:** a completion, a Grade to pass, a puha kapu és a „kapukvíz” megnevezés nem változik.
- **Mit blokkol:** learner release (M4); utána SIG-4.
- **Ki hagyja jóvá:** értékelési felelős + projektgazda.

### ERT-25 — M4: az M4.3 K3 kulcsa
- **Döntés:** az M4.3 SLIDE 5 K3 (Kapu 1) kulcsa: új opció, pontosított kérdésszár, vagy a ✅ áthelyezése?
- **Érintett findingok:** M4:ERT-G1-1 (= PED-G1-1, NYELV-G1-1, NYELV-G1-4). Források: M4.3:186–198, :540–555 (:549 ✅ „Érthető volt, hogy mire akartunk ma kilyukadni?”), :641; M4 HUB:75, :149; M4.F:79, :370.
- **Opciók:** (a) a 3. opció helyére a SLIDE 1-gyel összhangban álló új opció; (b) a kérdésszár pontosítása (a :554–555 visszajelzés és a NYELV-G1-1/-4 vele mozog); (c) a ✅ áthelyezése, csak lektori ítélettel.
- **Ajánlás:** nincs — kulcsdöntés lektori ítélettel (a verifier szerint egyik opció sem egyértelműen helyes).
- **Következmények:** answer key-változás (vétólista); a K1, a K2 és a SLIDE 1 ✅ marad; az M4:ERT-G1-6 K3-visszajelzése (X-10) csak utána.
- **Mit blokkol:** learner release (M4: a HUM-PED-01 szerint az élesítés a lektori QA-hoz kötött, SIG-4).
- **Ki hagyja jóvá:** az M4 szerzője / projektgazda; QA: szakmai lektor (HUM-PED-01).

### ERT-26 — M5: a kapu pontozási egysége (táblázatsor vagy rubrikasor)
- **Döntés:** az M5 kapu egysége a táblázatsor (minden sor mind a 4 kritériumon) vagy a rubrikasor (kritériumonként a táblázat egésze), és kötelező-e tanulástan-elem minden táblázatsorban?
- **Érintett findingok:** M5:PED-G1-1 (= ERT-G1-2); egy menetben: M5:NYELV-G1-2 (HUB:176, KAPU:26, :288), M5:NYELV-G1-9 (HUB:211); az M5:ERT-G2-1 „1 sor / minden sor” része. Források: M5 KAPU:26, :283–288, :295; M5 HUB:35, :176, :186, :211; M5.4:163, :203, :213, :254; PT:273; MAN:83.
- **Opciók:** (a) táblázatsor × kritérium (KAPU:286); (b) rubrikasor (HUB:176/:186, KAPU:26, PT:273); mellette: soronként kötelező tanulástan-elem igen/nem; a Moodle-oldali rögzítés helye (rubrika vagy `GATE_CONFIRMED_M5`).
- **Ajánlás:** (b): a kánoni sorrendben első PT:273 („az M5.4 táblázat minden rubrikasora ≥ Alapszint”), a KAPU:26 és a HUB:176 is rubrikasort mond, egyedül a KAPU:286 tér el. A soronkénti tanulástan-elem: értékelési felelős ítélete. A „3 vagy 4 sor” nem nyílik újra.
- **Következmények:** a KAPU:286, :288 és a HUB:211 igazodik; küszöb, szintek, az R4 kritikus státusza változatlan.
- **Mit blokkol:** learner release (M5 éles kapu); utána SIG-4.
- **Ki hagyja jóvá:** értékelési felelős + projektgazda; QA: módszertani lektor.

### ERT-27 — M5: az R4 „gyakorlás”-horgonya ↔ GL:197
- **Döntés:** szűküljön-e az M5 R4 „gyakorlás”-horgonya az aktív felidézésre és az elosztott gyakorlásra, vagy marad a GL:197 tág definíciója?
- **Érintett findingok:** M5:PED-G1-2 (= ERT-G1-2 (c), PED-G2-7); egy menetben: M5:NYELV-G1-12 (KAPU:300), M5:NYELV-G1-14 (KAPU:299). Források: M5 KAPU:295, :297–300; M5.3:174–180, :248–254; M5.4:124; GL:197.
- **Opciók:** (a) szűkebb horgony, a GL:197 módosításával; (b) marad a GL:197, a kalibrációs példák legfeljebb kiegészülnek.
- **Ajánlás:** (b): a verifier szerint a rubrika ma összhangban van a kánonnal (GL:197, kánon 3.); a szűkítés a Glosszárium-definíció megváltoztatása volna, amelyhez a findingok nem bizonyítanak hibát.
- **Következmények:** (a) Glosszárium-változás és az R4 kritikus sor újrakalibrálása; (b) csak a KAPU:299–300 nyelvi javításai.
- **Mit blokkol:** learner release (M5 éles kapu, R4 kritikus).
- **Ki hagyja jóvá:** értékelési felelős + módszertani lektor.

### ERT-28 — M5: az M5.2 SLIDE 8 kulcsolt opciójának szövege
- **Döntés:** igazodjon-e az M5.2 SLIDE 8 kulcsolt opciója („Először a nevelési célt találom ki…”, :558) a SLIDE 7 „a feladatból indulunk” elvéhez és a négytagú lánchoz?
- **Érintett findingok:** M5:ERT-G1-9 (= PED-G1-9). Források: M5.2:13–15, :529, :534, :557–560; M5 HUB:56, :207; M5 KAPU:165, :312.
- **Opciók:** (a) a ✅ opció szövege a lánchoz igazodik (a ✅ helye és a disztraktorok maradnak); (b) marad.
- **Ajánlás:** nincs — az M5 szerzője + értékelési felelős (kulcsolt opció; mindhárom disztraktor is a cél elhanyagolásáról szól).
- **Következmények:** a HUB:207 és a KAPU:312 csak utána igazodhat.
- **Mit blokkol:** learner release (M5; lecke-check, nem kapuz).
- **Ki hagyja jóvá:** M5 szerzője + értékelési felelős.

### ERT-29 — M5: az M5.4 SLIDE 6 pontozatlan önellenőrzéssé váljon-e
- **Döntés:** az M5.4 SLIDE 6 „✅ Igaz rám / ☐ Még nem…” eleme pontozatlan önellenőrzéssé váljon-e (a D-d/D-i új alkalmazási esete)?
- **Érintett findingok:** M5:ERT-G2-3 (= IMPL-G2-4); egy menetben: M5:ERT-G2-1 (SLIDE 6 4. állítás :254, zárószöveg :259–260; az objektív rész `.obj` FIXED, `0932de3`). Források: M5.4:246–255; MAN:16; HUM 11. D-d, D-i; rokon: M5:BIZT-G2-4 (DPO, X-4).
- **Opciók:** (a) pontozatlan önellenőrzés, a zárószöveg igazodik; (b) marad kulcsolt.
- **Ajánlás:** (a): önbevallásos állításnak nincs helyes válasza; a pontozás az őszinte „Még nem”-et hibásnak jelölné (RA:83 ugyanezt a kockázatot írja le); a D-d/D-i elve és az ERT-2 ajánlása ide mutat.
- **Következmények:** answer key-változás (vétólista); a DPO-kérdés (M5:BIZT-G2-4) részben tárgytalanná válhat.
- **Mit blokkol:** learner release (M5).
- **Ki hagyja jóvá:** értékelési felelős, a projektgazdával.

### ERT-30 — M5: KAPU Q12 nézőpont ↔ kulcs
- **Döntés:** az M5 KAPU Q12 disztraktorai első személyűek, a ✅ C harmadik személyű: a kulcs nézőpontja igazodjon a disztraktorokhoz, vagy fordítva?
- **Érintett findingok:** M5:NYELV-G1-11. Források: M5 KAPU:267–270, :274–275, :277; HUM:473.
- **Opciók:** (a) a C nézőpontja igazodik (ágensváltás nélkül); (b) a disztraktorok igazodnak; (c) marad.
- **Ajánlás:** nincs — értékelési felelős + modulgazda (itemírási kérdés; a nyers javaslat ágenst váltana, nem vehető át).
- **Következmények:** a ✅ a C-n marad; a :277 visszajelzés döntés nélkül nem változik.
- **Mit blokkol:** learner release (M5 kapu).
- **Ki hagyja jóvá:** értékelési felelős + modulgazda.

### ERT-31 — M6: a szcenárió-kvíz kötelező completion-elem-e
- **Döntés:** az M6 szcenárió-kvíz kitöltése kötelező completion-elem-e?
- **Érintett findingok:** M6:ERT-G1-1 (= PED-G1-1, IMPL-G1-1). Források: M6 HUB:194, :222, :226; M6 KAPU:23, :38, :409 ↔ MAN:92 (LMS-M6-06 „Kötelező” = igen), :94, :161, :165, :169, :310 (BSPEC-04, nem dönti el); PT:111, :274.
- **Opciók:** (a) kötelező kitölteni, de nem kapuz (az M5 hub §6 mintája; a HUB és a KAPU igazodik); (b) nem completion-elem (LMS-M6-06 „Kötelező” = nem, kikerül a MAN:161-ből).
- **Ajánlás:** nincs — projektgazda (build-spec gazda) ítélete: a manifest és a modulfájlok ütköznek, a PT csak a „nem kapuz”-t rögzíti.
- **Következmények:** a formatív státusz, a ≥10/12 és a korlátlan próbálkozás nem változik; a HUB:222–226 az ERT-1-gyel egy szerkesztésben.
- **Mit blokkol:** learner release (M6); G3a (course completion).
- **Ki hagyja jóvá:** projektgazda; QA: értékelési felelős + programvezető.

### ERT-32 — M6: az R4 „Oké” horgonya és a tanított minimum
- **Döntés:** az M6 R4 „Oké” horgonya (egyetlen biztonsági megjegyzés bármely eszköznél) kapjon-e kategóriaspecifikus minimumot (bizalom- és kontaktjátéknál az M6.1 négyelemes minimuma), és mit jelent az M6.B:219 „minimum”-mezőlistája az „Oké”-listához képest?
- **Érintett findingok:** M6:ERT-G1-2, M6:ERT-G3-4. Források: M6 KAPU:169–186 (5. item), :395–396, :405–406, :409; M6.1:876–893; M6 HUB:44, :57, :152; M6.B:41–53, :139, :208–226; M6.F:319, :328; PT:111.
- **Opciók:** (a) kategóriaspecifikus „Oké”-horgony (rubrikaváltozás), a variáció és a „mikor állsz le, kit hívsz” az „Oké” része; (b) marad az egymondatos küszöb, a KAPU kimondja, hogy a kategória-minimumot az értékelő visszajelzésben kéri, és az M6.B:219, HUB:44, :152 „minimum” szava a KAPU „Oké”-listájához igazodik.
- **Ajánlás:** nincs — értékelési felelős, rubrikánál projektgazda; a biztonsági horgony miatt Memuna-QA javasolt. Kockázat: a (b) mellett a tanított négyelemes minimum hiánya a blokkoló soron sem buktat.
- **Következmények:** az R4 szintjei, a blokkoló státusz, a „minden sor ≥2” és az M6.1 minimuma a döntésig változatlan; a HUB:228 példaforrása (NYELV-G1-1) és a B:216 mező (BIZT-G3-4, NYELV-G3-9) sorrendben követi.
- **Mit blokkol:** learner release (M6 éles kapu).
- **Ki hagyja jóvá:** értékelési felelős; rubrikaszint: projektgazda.

### ERT-33 — M6: társas pontozás ↔ „Ma nem pontozunk”
- **Döntés:** az M6 KAPU, a HUB:218 és a PT:288 társas pontozása és társ–stáb kalibrációja hogyan viszonyul az M6.B:227 „Ma nem pontozunk” menetéhez?
- **Érintett findingok:** M6:ERT-G3-1 (= PED-G3-3; c) alpont: MUNK-02 „Oké”-lista az M6.F 2.1-be). Források: M6 KAPU:387, :389, :399, :421; M6 HUB:218; PT:288; M6.B:24, :139, :227, :375, :472; M6-NY-D24.
- **Opciók:** (a) a KAPU, a HUB:218 és a PT:288 a tényleges menetet írja le: a társas visszajelzés fejlesztő, nem pontoz, a kalibráció a képzők között zajlik (PT-módosítás); (b) az M6.B-be társas besorolási lépés kerül az „Oké”-ellenőrzőlistával (új tartalom).
- **Ajánlás:** nincs — értékelési felelős + projektgazda. Az (a) a PT:288-at módosítja, amelyet az M6-NY-D24 (Workshop-összefüggésben) érintetlennek kért: ezt csak a projektgazda engedheti; Moodle Workshop egyik úton sem lesz.
- **Következmények:** az R4/R5 végső pontja a képzőé / mentoré marad.
- **Mit blokkol:** learner release (M6 éles kapu).
- **Ki hagyja jóvá:** értékelési felelős + projektgazda.

### ERT-34 — M6: a KAPU 2. iteme a 6.-at duplikálja
- **Döntés:** az M6 KAPU 2. iteme a 6.-at duplikálja, Kivsza-korú item nincs: átsorolás vagy új item?
- **Érintett findingok:** M6:ERT-G1-6 (= PED-G1-3). Források: M6 KAPU:50, :60–61, :86, :100–118, :190–208, :373, :437; M6 HUB:54.
- **Opciók:** (a) a 2. item a biztonsági témába kerül, a „4 / 3 / 3 / 2” beosztás igazodik; (b) új korosztály-illesztési item a 2. helyre (az N-M6-18 pool-bővítéssel).
- **Ajánlás:** nincs — értékelési felelős ítélete. Kockázat: (a) mellett a HUB:54 korosztályi lefedettsége hiányos marad; (b) új itemtartalom.
- **Következmények:** az itemek, a kulcsok, a 12-es darabszám és a ≥10/12 nem változik; (b)-nél az ERT-G2-4 és a NYELV-G1-4 2. itemre vonatkozó része tárgytalan.
- **Mit blokkol:** learner release (M6; diagnosztikus, nem kapuz).
- **Ki hagyja jóvá:** értékelési felelős.

### ERT-35 — M6: a KAPU 4. itemének elve a kötelező szcenárió ágoldalain
- **Döntés:** kiterjed-e a 2026-10-05-i döntés (opcionális tartalom nem lehet kvízitem egyetlen tanítási forrása) a kötelező szcenárió ágoldalaira, vagyis kerüljön-e a 4. item elve egy minimális mondatban kötelező forrásba?
- **Érintett findingok:** M6:ERT-G2-5. Források: M6 KAPU:157, :162; M6.4:794–797 (5D-J), :838–843 (5D-T); M6.2:287–289; `2026-10-05 Projektgazdai döntés – M6.4 elfogadás és Command 5 hatókör.md` :35–39, :141.
- **Opciók:** (a) igen: a meglévő M6.4-elv szó szerint, egy mondatban kötelező forrásba kerül; (b) nem: a 4. item az ágoldalakra támaszkodik.
- **Ajánlás:** (a): a 2026-10-05-i döntés indoka (kapuitem nem épülhet olyan tartalomra, amelyet nem minden tanuló lát) az ágoldalra is áll, mert a választástól függ, ki látja; az átvezetés a döntés mintáját követi, új szabályt nem ír. (Új alkalmazási eset, ezért döntés.)
- **Következmények:** a ✅, a szár és a küszöb változatlan; nem állítható, hogy az M6.1 vagy az M6.2 tanítja, ami nincs benne.
- **Mit blokkol:** learner release (M6).
- **Ki hagyja jóvá:** projektgazda; QA: értékelési felelős.

### ERT-36 — M6: a KAPU 11–12. iteme az M6.2 itemjeinek ismétlése
- **Döntés:** az M6 KAPU 11–12. iteme az M6.2 gyakorló itemjeit ismétli: izomorf változat, friss-seb-függő elosztó, vagy tudatos visszakérdezés?
- **Érintett findingok:** M6:ERT-G2-8 (= PED-G2-5); a 12. itemről egy döntés az M6:PED-G1-8-cal (lásd X-5) és az ERT-7 M6:ERT-G1-10 B-opciójával. Források: M6 KAPU:64, :300–310, :322–337 (:325 „friss seb”); M6.2:646–653, :818–838.
- **Opciók:** (a) izomorf változat (új értékelési tartalom); (b) friss-seb-függő elosztó a 12. itembe; (c) tudatos visszakérdezés marad, a visszajelzés kimondja.
- **Ajánlás:** nincs — értékelési felelős a Memuna bevonásával; a 12. itemnél előbb az X-5 (M6:PED-G1-8) döntése, mert a két javaslat ütközik.
- **Következmények:** a ✅, a szár és a küszöb a döntésig változatlan.
- **Mit blokkol:** learner release (M6; diagnosztikus kvíz).
- **Ki hagyja jóvá:** értékelési felelős + Memuna.

### ERT-37 — M6: páros közös lap ↔ egyéni LMS-M6-05 leadás
- **Döntés:** hogyan lesz az M6.B páros közös lapjából egyéni, mentor által kapuzott LMS-M6-05 leadás?
- **Érintett findingok:** M6:PED-G3-8. Források: M6.B:21, :261, :348; MAN:91 (LMS-M6-05).
- **Opciók:** (a) közös vázlat, egyéni véglegesítés és leadás; (b) közös leadás mindkét névvel.
- **Ajánlás:** (a): az LMS-M6-05 egyéni, mentor által kapuzott Assignment (MAN:91), a profilja és az R1–R5 a finding korlátja szerint nem változik; a (b) ezzel ütközne.
- **Következmények:** egy instrukciós mondat az M6.B:348-on (a BIZT-G1-3 G3-helye is érinti).
- **Mit blokkol:** learner release (M6 éles kapu).
- **Ki hagyja jóvá:** értékelési felelős + M6 modulgazda.

### ERT-38 — Z: a Z.4 „Teljesítve” tartalmi mércéje
- **Döntés:** mi a Z.4 „Teljesítve” (LMS-Z-08) mércéje: a HUB/Z.4 hármas minimuma, vagy a „tényleges, minimálisan értelmezhető tartalom” (HUM:457), a minimum formatív visszajelzésként?
- **Érintett findingok:** Z:ERT-G1-1. Források: Z HUB:185–189, :217, :219; Z.4:343–353; MAN:19, :111, :173; HUM:457; PT:259.
- **Opciók:** (a) a hármas minimum a „Teljesítve” feltétele; (b) a minimum formatív (mint az M2/M4-nél, MAN:173), a „Teljesítve” a HUM:457 alsó határa.
- **Ajánlás:** nincs — valódi küszöbdöntés (verifier).
- **Következmények:** (a) szigorúbb mentori elfogadás, el nem fogadásnál javítás; a minimum szövege, a címkepár és az 1+1 beadás változatlan.
- **Mit blokkol:** learner release (Z; program-teljesítés).
- **Ki hagyja jóvá:** értékelési felelős; vétó/QA: programvezető.

### ERT-39 — Z: a Z.A a „Minimális teljesítés” része-e
- **Döntés:** a Z.A peula a „Minimális teljesítés” eleme-e (HUB:198), vagy ajánlott lépés (PT:211–213, MAN:163/:165)?
- **Érintett findingok:** Z:ERT-G1-3. Források: Z HUB:193, :195–199; MAN:110, :133, :163, :165; PT:211–213.
- **Opciók:** (a) completion-feltétel jelenléti elemmel és pótlási úttal; (b) ajánlott lépés, a HUB:195–199 átfogalmazódik.
- **Ajánlás:** (b): a kánoni sorrendben első PT:211–213 és a course completion kritériumai (MAN:163/:165) nem sorolják a Z.A-t; az (a)-hoz pótlási út kellene, amely a kánonban nincs.
- **Következmények:** a HUB §5 a többi Z-javítással egy szerkesztésben; a dátumos nyitás és a sorrend nem változik.
- **Mit blokkol:** learner release (Z; program-teljesítés).
- **Ki hagyja jóvá:** programvezető + értékelési felelős.

### ERT-40 — M7: a Q11/Q14 Multi-Select részpontja és az egyetlen döntő formula
- **Döntés:** jár-e részpont az M7 kapukvíz Q11/Q14 Multi-Select itemjeinél, és mi az egyetlen döntő formula a „≥80%” ↔ „≥12/14” helyett?
- **Érintett findingok:** M7:IMPL-G1-3 (= ERT-G1-1). Források: M7 KAPU:21, :48, :52, :199, :242, :411; M7 HUB:382; MAN:101–102; HUM:456.
- **Opciók:** (a) mindent-vagy-semmit pontozás pluginnal (`qtype_multichoiceset`, G3a, X-11); (b) core részpontozás, de az LMS-M7-09 megerősítésekor csak a teljes pontú item számít jónak (kézi ellenőrzés); (c) arányos részpont „Grade to pass = 12,00”-val — 11 teljes + 2 részleges itemmel is átenged.
- **Ajánlás:** (a), ha a plugin a célkörnyezetben elérhető, különben (b). A „≥12/14” itemszámot jelent, a (c) ezt csendben lazítaná (küszöbváltozás); a (b) az M3 KAPU:76 bevett mintája (kézi ellenőrzés a megerősítés előtt, ha a konfiguráció nem kényszerít).
- **Következmények:** szám nem változik (12/14, 80%, Q13-szabály, ✅); a KAPU:48/:411 rögzíti a formulát.
- **Mit blokkol:** learner release (M7 éles kapu); G3a (plugin), G3b.
- **Ki hagyja jóvá:** értékelési felelős; QA: programvezető; plugin: LMS-gazda (X-11).

### ERT-41 — M7: a hiányzó kipróbálási vállalás és AI-megjegyzés következménye (K4)
- **Döntés:** mi a következménye a hiányzó vagy üres kipróbálási vállalásnak és AI-használat-megjegyzésnek, amelyet a KAPU „completion-szinten figyelembe vesz, de nem blokkol”?
- **Érintett findingok:** M7:ERT-G1-11 (= PED-G1-12, IMPL-G1-10, ERT-G2-11); a döntés utáni végszövegen: M7:NYELV-G1-4, M7:NYELV-G2-5, M7:NYELV-G2-11 b) (M7.4:780–781; a c) rész lásd X-17). Források: M7 KAPU:249, :254–262, :422–423; MAN:20, :103, :104; M7.4:780–781; M7 HUB:282; M7.B:102, :146–147, :163, :562–568; HUM 9. „Kipróbálási vállalás kitalált kvucánál” (a tartalmat rendezi, a hiány következményét nem); HUM-PRIV-04.
- **Opciók:** (a) nincs következmény; (b) pótlási kérés kapuhatás nélkül; (c) completion-feltétel.
- **Ajánlás:** (b): ez az egyetlen olvasat, amely a kánoni mondat mindkét felével összefér — az (a) ellentmond a „figyelembe vesz”-nek, a (c) a „nem blokkol”-nak (a PED-G1-12 verdiktje szerint a D-d/D-i szellemének is).
- **Következmények:** a 24 pont és a „nem pontozott” státusz nem változik; a befagyasztott fordulat (KAPU:255–262, :422–423, MAN:103, M7.4:780–781) a döntés szerint íródik át.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős; QA: programvezető, az AI-megjegyzésnél a HUM-PRIV-04 vétó/QA-szerepei (DPO/jogi felelős + programvezető).

### ERT-42 — M7: az R8 0-s szintje (AI-másolat és beazonosítható hanih-adat egy pontban)
- **Döntés:** van-e kapuhatása az R8 0-s szintjének, váljon-e kétfelé az AI-másolat és a beazonosítható hanih-adat mércéje, és mi lesz a már leadott beazonosító adattal?
- **Érintett findingok:** M7:BIZT-G1-1 (= ERT-G1-3). Források: M7 KAPU:249, :252, :268, :357, :366–368; M7 HUB:358, :377; ADV §3:66, :86; HUM:461 (a kapuhatásról nem dönt).
- **Opciók:** (a) kettéválik, a beazonosító adat visszaküldést vagy blokkolást von maga után; (b) együtt marad, a kapuhatás kimondva; mellette DPO: ki és hogyan távolítja el a leadott adatot, incidens-e, ki a jelzés címzettje.
- **Ajánlás:** nincs — értékelési felelős + DPO ítélete (a DPO-rész X-4). Kockázat: az R8 ma nem kritikus, így 21 ≥ 17 ponttal beazonosító hanih-adattal is „Teljesítve” lehet.
- **Következmények:** a KAPU:357 incidensmondata és az R8 gyermekvédelmi ága nem törölhető.
- **Mit blokkol:** learner release (M7 éles kapu); G2.
- **Ki hagyja jóvá:** értékelési felelős + DPO; QA: DPO + programvezető.

### ERT-43 — M7: az R1 2-es szintje („mérhető jel VAGY időkeret”)
- **Döntés:** kötelező-e a mérhető jel az M7 R1 2-es szintjén (KAPU:278), vagy a Q3 visszajelzése és az M7.1 igazodik a rubrikához?
- **Érintett findingok:** M7:PED-G1-1 (= ERT-G1-4). Források: M7 KAPU:86–93, :277–278; M7.1:316–320; M7.A:215, :349–352.
- **Opciók:** (a) a mérhető jel kötelező (az időkeret mellette maradhat); (b) marad a VAGY, a Q3 visszajelzése és az M7.1 igazodik.
- **Ajánlás:** nincs — értékelési felelős (konstruktum-ütközés); az M7:BIZT-G1-6 (X-4) R1-korlátjával egyeztetendő.
- **Következmények:** a Q3 kulcsa (B), az R1 ≥2 és a 17/24 nem változik.
- **Mit blokkol:** learner release (M7 éles kapu; az R1 blokkoló, PT:288).
- **Ki hagyja jóvá:** értékelési felelős; QA: módszertani lektor.

### ERT-44 — M7: mit mér az R3
- **Döntés:** mit mér az M7 R3: a 11 pont három fázisát, a peula belső ívét, vagy mindkettőt külön szempontként?
- **Érintett findingok:** M7:PED-G1-10 (= NYELV-G1-12). Források: M7 KAPU:99, :110, :299–300; M7 HUB:160.
- **Opciók:** (a) a fázisok jelenléte; (b) a belső ív; (c) mindkettő külön.
- **Ajánlás:** nincs — értékelési felelős + modulgazda (rubrikaszint).
- **Következmények:** az 1-es szint példája és a HUB:160 címke igazodik; a 0–3 skála, a nem kritikus státusz és a Q4–Q6 kulcs változatlan.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős + modulgazda.

### ERT-45 — M7: az R7 fix 45 perce
- **Döntés:** legyen a v2 kötelező hossza 45 perc, vagy az R7 1-es szintje a tervezett időkeret túllépését mérje?
- **Érintett findingok:** M7:ERT-G1-12. Források: M7 KAPU:114, :164, :210, :347; M7 HUB:132; M7.2:708; PT:441.
- **Opciók:** (a) a v2 kötelező hossza 45 perc, a feladatleírás kimondja; (b) az R7 a saját tervezett időkeret túllépését méri, a 45 perc csak példa.
- **Ajánlás:** (b): a v2 hossza sehol nincs rögzítve, a KAPU saját példái (60’) és a PT:441 (60–90’) ellentmondana az (a)-nak; a (b) egyiket sem írja felül.
- **Következmények:** az R7 nem kritikus marad, a küszöb nem változik; az ERT-50 külön döntés.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős.

### ERT-46 — M7: az M7.1 SLIDE 4 Fill in the Blanks elfogadott tartománya
- **Döntés:** mi az M7.1 SLIDE 4 Fill in the Blanks elfogadott válaszainak tartománya („az összes reális szám”, :333)?
- **Érintett findingok:** M7:IMPL-G1-7. Források: M7.1:333, :340, :347, :356; RA:42.
- **Opciók:** (a) mezőnként rögzített tartomány, szó szerint a leckében; (b) pontozás nélküli út (RA 6. pont (b)), csak célverzión igazolt működés után.
- **Ajánlás:** nincs — leckegazda + értékelési felelős; előbb az M7:PED-G1-8 (X-10) döntése.
- **Következmények:** a mondatok és a visszajelzések a döntésig nem változnak.
- **Mit blokkol:** learner release (M7; lecke, nem kapuz).
- **Ki hagyja jóvá:** leckegazda + értékelési felelős.

### ERT-47 — M7: a (C)-cella „átláthatóság” szava
- **Döntés:** mit kell megnevezni az M7 KAPU:382 (C)-cellájában („Pontos kezdés–zárás + helyszín + átláthatóság (sötétedés, hazaút) megnevezve”) az „átláthatóság” alatt?
- **Érintett findingok:** M7:NYELV-G1-16. Források: M7 KAPU:218, :240, :382; HUM-SAFE-02 („átlátható módon”).
- **Opciók:** (a) safer-working értelemben vett átláthatóság (ki tud a helyzetről); (b) a körülmények (sötétedés, hazaút) közlése a résztvevőkkel és a szülőkkel; (c) mindkettő, külön felsorolva.
- **Ajánlás:** nincs — értékelési felelős; vétó/QA: Memuna (a cella biztonsági szempontot pontoz).
- **Következmények:** a 0–2 skála, az 5 terület és az R4/R7-kötés változatlan.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős; vétó/QA: Memuna.

### ERT-48 — M7: az AI-jártassági blokk beágyazása és completion-szerepe
- **Döntés:** hogyan ágyazódik be az M7.2 kötelező AI-jártassági blokkja (beágyazott H5P, HUB:199 ↔ „külön H5P-activity”, M7.2:130), és szerepe van-e a lecke completionjében?
- **Érintett findingok:** M7:IMPL-G2-2 (= ERT-G2-2). Források: M7.2:8, :31, :87, :89, :130, :132–152, :989; M7 HUB:199; MAN:96; HUM:191 (HUM-PRIV-04); a blokk 2026-10-02 óta kötelező.
- **Opciók:** (a) Page-be ágyazott, tartalombankos H5P, rögzítés nélkül, nem completion-elem (a kötelezőséget a befogadó oldal completionje hordozza); (b) külön H5P activity saját §2-sorral (profil, completion, privacy); mellette: a Page vagy a kérdés feltétele-e az LMS-M7-02 nyitásának.
- **Ajánlás:** (a): a HUB:199 beágyazott H5P-t ír, a blokk „formatív” (:87), és a rögzítés nélküli út adattakarékosabb (a HUM-PRIV-04 keretében); a (b) új manifest-sort és adatkört nyitna. A completion-elem kijelölése a build-spec gazdáé.
- **Következmények:** a blokk szövege, a §7 tiltólista, a kérdés, a ✅ és a „formatív” besorolás nem változik; az M7.2 metájába lecke-completion sor kerül.
- **Mit blokkol:** learner release (M7); G3a.
- **Ki hagyja jóvá:** projektgazda (build-spec) + értékelési felelős + LMS-gazda (LMS-rész X-11); QA: a HUM-PRIV-04 szerepei.

### ERT-49 — M7: a (C) 2. sor „eltérő létszám” szempontja
- **Döntés:** a (C) 2. sorának „mi van eltérő létszámnál” szempontját (KAPU:383) az M7.3 nem tanítja, a SLIDE 5 Q1 kulcsa pedig a létszámot nem hiányosnak kulcsolja: új tartalom, vagy a (C) szintleírása módosul?
- **Érintett findingok:** M7:ERT-G2-10. Források: M7 KAPU:376, :383, :388, :419; M7.3:623, :698, :703, :706–710, :847–848.
- **Opciók:** (a) az M7.3 tanítja (új tartalom, a modulgazda írja); (b) a szempont kimarad a (C) 2. területének 2-es szintjéből.
- **Ajánlás:** (b): a kapu nem mérhet olyat, amit a tananyag nem tanít (konstruktív illeszkedés), a Q1 kulcsa semmiképp nem változik, így ez a kisebb beavatkozás; az (a) új pedagógiai tartalom.
- **Következmények:** a (C) skálája és a küszöb változatlan.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős.

### ERT-50 — M7: a v1 operációs táblájának minimuma
- **Döntés:** a v1 operációs táblájának minimuma 3 vagy 4 sor („min. 3–4 sor”, M7.4:767, KAPU:348)?
- **Érintett findingok:** M7:NYELV-G2-8. Források: M7.4:72, :607–608, :761–762, :767, :808 (`@asset`); M7 KAPU:348.
- **Opciók:** (a) minimum 3, a 4 ajánlott; (b) minimum 4.
- **Ajánlás:** nincs — értékelési felelős + modulgazda (számszerű minimum).
- **Következmények:** utána a :808 build úton, a KAPU:348 egy menetben; az ERT-45 külön döntés.
- **Mit blokkol:** learner release (M7).
- **Ki hagyja jóvá:** értékelési felelős + modulgazda.

## 8. Szerepköri jóváhagyások (signoff)

> Ezek nem nyitott döntések: a megvalósítást a projektgazda jóváhagyta, a formális szerepköri bizonyíték függő. Semmi
> nem írható be helyettük („átnéztem”, jóváhagyó, dátum, verzió, MEGVAN); vétónál az érintett tétel `REOPENED`.

### SIG-1 — M0: a belépőkvíz itemszövegének utólagos értékelési QA-ja
- **Mit kell aláírni:** írásos QA-bejegyzés arról, hogy a belépőkvíz hét itemének projektgazdai szövegét (M0 HUB:180) átnézték; QA-megfigyelés: az 1., a 2. és az 5. item kulcsa hossz alapján kitalálható, a 2. item kulcsa a „jóváhagyott” szót tartalmazza (a HUM:473 ezt az M3-ra zárja ki). Answer key-módosítást a riport nem javasol; vétónál a tétel a projektgazdához megy.
- **Érintett findingok:** M0:ERT-4. Források: M0 HUB:180, :187–243, :205; HUM:473; BS-D5 (az M0 belépőkvíz utólagos ellenőrzője az értékelési felelős).
- **Ki írja alá:** értékelési felelős; az 1–2. itemnél a Memuna is (átfed az M0:BIZT-1-gyel, X-7).
- **Hol rögzül:** a PT §9.3 release-jegyzőkönyvben (a kiadott modul jóváhagyásai között).
- **Mit blokkol:** G-kaput nem (HUM 8.: a vétó/QA release-kaput nem nyit és nem zár); POST-PILOT (VF-M0 B sáv). Az ERT-11-gyel egy menetben célszerű.

### SIG-2 — M3 és M7: a biztonságkritikus küszöb szakértői megállapítása, kalibráció, kétszemes rend
- **Mit kell aláírni:** (1) az M3 kvízküszöbének (≥10/12 + kritikus itemek) és az M7 Q13 gyermekvédelmi itemének szakértői küszöb-megállapítása (PT:277; §9.2 1.); (2) a kapu-szezon előtti értékelői kalibráció (1–2 referenciaminta közös pontozása) és a kétszemes blokkoló döntési rend dokumentálása (PT:288; §9.2 4.): M3-nál mentor + második képző + Memuna, M7-nél mentor + második képző.
- **Érintett findingok:** M3:BIZT-G1-2 (értékelési része; = ERT-G1-3), M7:ERT-G1-5. Források: PT:277, :288, :391, :394; M3 KAPU:30, :74, :317; M7 KAPU:21, :27, :48, :370, :409–424; RR:22–35.
- **Ki írja alá:** az item-szintű becslést a Memuna és a módszertani lektor végzi; a küszöb jóváhagyása a PT:277 szerint a §9.2 1. pont szerinti szakmai lektor feladata; a kalibráció és a kétszemes rend dokumentálása az értékelési szerepé.
- **Hol rögzül:** PT §9.3 release-jegyzőkönyv; a KAPU QA-listája legfeljebb szó szerint hivatkozhat a PT:277-re és a :288-ra.
- **Mit blokkol:** az M3 és az M7 éles kapujának learner release-ét (PT:288: a két kapu csak akkor élesedhet, ha a kalibráció és a kétszemes rend dokumentált). A Memuna „átnéztem” bejegyzése nem azonos a küszöb-jóváhagyással (VF-M7). Az M3-nál az ERT-10 (kritikus itemkör) eredménye előfeltétel. Társkapu: X-7 (az M3 Memuna-része: KAPU:14 „átnéztem”, a kritikus slotváltozatok, KAPU:38, a segélyvonalak a review napján).
- **Megjegyzés:** a Q-PED-6 (2026-10-04, `OWNER_DECIDED`: „strukturált szakértői küszöb-megállapítás (Angoff-elemekkel)”, utólagos kalibráció a pilot itemadataiból) a PT:277-be és a HUM 10. szakaszába nincs átvezetve; az átvezetés objektív tétel, nem döntés.

### SIG-3 — M3: a HUM:463 szerinti QA az M3.4:834 kritikus-téma megnevezésére
- **Mit kell aláírni:** hogy az M3.4:834 a kritikus követelményeket megnevezi, a kvíz kulcsát nem árulja el (HUM:463).
- **Érintett findingok:** M3:BIZT-G2-10 (értékelési része; = PED-G2-10, ERT-G2-8, IMPL-G2-7). Források: M3.4:834; HUM:463; M3.3:9–10.
- **Ki írja alá:** értékelési felelős + Memuna (a HUM:463 utólagos ellenőrzői).
- **Hol rögzül:** PT §9.3 release-jegyzőkönyv.
- **Mit blokkol:** az M3 learner release-ét (a G1-Memuna-résszel együtt). Társkapuk: X-7 (Memuna „átnéztem” az M3.3–M3.4-re, a SAFE-7 nyitott FINAL_RELEASE_QA, GK §6), X-8 (RT-P0-09, -11, -13, -14, -22, -24, RT-A11Y-01…12). A ✅ és a SAFE-7 nem jelölhető megoldottnak.

### SIG-4 — Szakmai lektor modul-QA-ja: M4 (HUM-PED-01) és M5 KAPU (PT §9.2 1.)
- **Mit kell aláírni:** M4: a kvízitemek, disztraktorok, a rubrika és a sablonok utólagos lektori QA-ja (HUM-PED-01), benne a 2026-10-02 óta módosult elemek: M4:PED-G2-3 új elosztója (FIXED, `4119d16`) és a döntések után az ERT-25, ERT-24, illetve az M4:ERT-G1-6, M4:ERT-G1-9, M4:PED-G2-4 (X-10) új szövegei (PT §9.3: módosított kvíz és rubrika csak újraellenőrzéssel élesíthető). M5: a KAPU (item-bank + rubrika) szakmai lektorálása (PT:277, §9.2 1.), mellette az értékelési felelős QA-bejegyzése; az ERT-26/27/28/30 döntései után.
- **Érintett findingok:** M4:PED-G1-7 (lektori része; = BIZT-G1-3, IMPL-G1-9), M5:ERT-G1-11. Források: HUM:274, :276, :280, :282; PT:277, :391, §9.3; RR:39; M5 KAPU:11–13; M5 HUB:193, :233.
- **Ki írja alá:** a szervezet által kijelölt szakmai lektor; az M5-nél QA: értékelési felelős.
- **Hol rögzül:** a jóváhagyó neve, dátuma és verziója a PT §9.3 release-jegyzőkönyvben (HUM:274), nem a G1 alatt (a G1 egyetlen jóváhagyója a Memuna, RR:39).
- **Mit blokkol:** az M4 élesítését valódi madrihoknak, nem a staginget (HUM:276); az M5 modul élesítését (PT §9.2 1.); a pilot Go/No-Go-ját az érintett modulra. Társkapu: X-7 (az M4 Memuna-része: M4.2 SLIDE 5 K2, M4.3:360). A 2026-10-02-i projektgazdai felülvizsgálat (HUM:280) a lektori utólagos QA-t nem helyettesíti (HUM:282).

### SIG-5 — M5: az AI-generált médiaelemek emberi szakmai lektorálása
- **Mit kell aláírni:** az M5.1 VID-01, NAR-02, VID-02, az M5.3 ILL-01, IKO-01, ILL-02 és az M5.4 ILL-01 emberi szakmai lektorálását; enélkül az „AI-generált médiaelem · emberi lektorálással.” címke (PT:224) nem igaz.
- **Érintett findingok:** M5:BIZT-G1-6 (ide olvadt M5:BIZT-G2-10). Források: PT:224, §9.2 3.; M5.1:22, :145, :322, :566; M5.3:59, :137, :211; M5.4:85; PRODUCTION-DECISIONS D3 (ma egy sincs meg).
- **Ki írja alá:** szakmai lektor.
- **Hol rögzül:** PT §9.3 release-jegyzőkönyv; a címke, a blokkolók és az `@asset` nem változik.
- **Mit blokkol:** az érintett assetek tanulói megjelenítését; a B/C fázisú elemeknél (narráció, videó) a Q-MED-1 szerinti fallbackkel a modul learner release-e nem áll meg.

### SIG-6 — M6: az M6.1 VID-01 és NAR-02…07 jogi és jogosultsági blokkolói (HUM-MEDIA-02)
- **Mit kell aláírni:** a RIGHTS-EVIDENCE hiányzó sorait: J3, H-11 és az AI Act 50. cikk (4) minősítése (jogi jóváhagyó); J2 (Memuna + szerző); V1 (Memuna + DPO); V3/E-8 (Memuna + jogi jóváhagyó); R2-3.
- **Érintett findingok:** M6:BIZT-G1-6. Források: M6.1:105–155, :136–139 (`"blockers": ["R2","R3"]`), a NAR-02…07 helyei; RIGHTS-EVIDENCE:83, :189, :290–292; PRODUCTION-DECISIONS:502 (VO D-08); GK:25.
- **Ki írja alá:** jogi jóváhagyó, Memuna, DPO, szerző — nem a szakmai lektor.
- **Hol rögzül:** RIGHTS-EVIDENCE 1/A.5 nem személyes hivatkozással; a valódi név és a szerződés a korlátozott hozzáférésű jogosultsági nyilvántartásba. MEGVAN nem írható be; a blokkolók, az R1-címke és a provider/deployer-bekezdés nem törölhető.
- **Mit blokkol:** az érintett tanulói asseteket (GK:25; RR Médiakapuk); videó/narráció lévén fallbackkel a modul release-e nem áll meg (Q-MED-1).
- **Megjegyzés:** a tétel ideiglenesen áll az X-16-on (szakmai lektor); a validált riport „X-17”-et javasolt, de az X-17 azóta a hanggyártási fix pack. Javasolt: saját médiajog-signoff sor (a csomag összefésülőjének döntése).

### Lezárt korlátok és „már lezárt / átvezetendő” tételek
- Nincs olyan tétel, amelyet lezárt projektgazdai döntés szó szerint lefed. A közeli lezárt döntések (BSPEC-06/D-b, D-d, D-i,
  D-f, D-h, BS-D4, BS-D5, HUM:456, :457, :461, :462, :463, :473, a 2026-10-05-i M6.4-döntés, M6-NY-D8, M6-NY-D24) a
  verifierek szerint keretet adnak, de nem válaszolják meg a kérdést (új alkalmazási eset), ezért a fenti döntésekben
  korlátként és az ajánlás indokaként szerepelnek.
- Részben érintett, át nem vezetett lezárt döntés (tételt nem zár le): Q-PED-6 (2026-10-04) → PT:277 elnevezése; lásd SIG-2.

## 9. Tantervi architektúra — programvezető / modulgazda

> **Read-only döntési vázlat, nem kánon, nem jóváhagyás.** Forrás: `AUTOPILOT-LEDGER.md` (AP-2026-10-11-01, TERMINAL,
> `1d7b58d`), Külső kapuk X-10; `gate_X-10.tsv` (87 tétel); a validált riportok 3. szakasza (M0/M1 2026-10-10, M0/M1
> nyelvi, M2–M7, Z 2026-10-11), a célzott QA-riportok (M5, Z) és a verifier-verdiktek; lezárt döntések: `Emberi
> jóváhagyás szükséges.md` (HUM) 3. és 6.–13. szakasz, a 2026-10-04-i M6-NY-, a 2026-10-05-i M6.4- és a 2026-10-10-i
> projektgazdai jegyzőkönyv.
>
> **Rövidítések:** HUB = a modul hubfájlja · KAPU = a modul kapufájlja · Mx.y = lecke · Mx.A/B/F = peula · PT = `Program
> terv.md` · MAN = `LMS – activity manifest.md` · RA = `LMS – H5P runtime acceptance.md` · A11Y = `LMS – hozzáférhetőségi
> sztenderd.md` · GK = `Gyermekvédelem – release gate.md` · RR = `RELEASE-READINESS.md` · HUM = `Emberi jóváhagyás
> szükséges.md` · „10-10/5” = a 2026-10-10-i projektgazdai jegyzőkönyv 5. pontja („ne egy újraírt, bonyolultabb képzés
> legyen … kerüld a szükségtelen módosításokat”). A sorszámok a ledger és a riportok szerintiek: végrehajtáskor újra
> bizonyítandók.
>
> **Közös „Mit blokkol” alap:** a staging buildet egyik tétel sem blokkolja (a gépi `MOODLE-BUILD-VERDICT` az `5fcabea`-n
> ezekkel együtt `READY_FOR_STAGING_BUILD`); a futó M0+M1 kontrollált pilotot (main) egyik sem érinti (next-version ág).
> Ahol alább G-kapu áll, az a next-version learner release-ét érinti; ahol „nem G-kapu”, ott a tétel a next-version
> tartalmi véglegesítését (az előkészített HOLD-blokkokat) tartja vissza.

### PRG-1 — Lépésidők a rögzített blokkhatárokon belül

- **Döntés:** Ahol a lépésidők összege túllépi a rögzített blokk- (vagy lecke-) keretet, mi a közös szabály, és
  peulánként melyik lépés rövidül?
- **Érintett findingok:** `M0:PED-5`, `M0:NYELV-G2-1` (függő), `M2:PED-G3-1`, `M3:PED-G3-1` (ide olvadt `M3:ERT-G3-9`),
  `M4:PED-G2-2`, `M4:NYELV-G2-6` (a :326 „ha belefér az idő”), `M4:NYELV-G2-5`, `M4:NYELV-G2-12` a), `M4:NYELV-G2-10`
  (függő; a :205 a PRG-2, a :278 a PRG-10 után is), `M5:PED-G2-6`, `M5:QA-PED-2`, `M6:PED-G3-1`, `M7:PED-G3-1` (ide olvadt
  `M7:ERT-G3-9`), `M7:NYELV-G3-14` (függő). Túlfutás: M0.A Blokk 2–3 (16–21′, 13–18′ a 15′-ben; a 45′-es változat
  vágási terv nélkül); M2.A Blokk 3 (20–25′ a 15′-ben), M2.B Blokk 4; M3.A 4.2–4.3, M3.B 4.2–4.3, M3.F 4.4 és Blokk 3;
  M4.A 4.3–4.5, M4.B 4.3–4.4; M5.A 4.1–4.2, M5.B 4.2.1, 4.3.1–2, M5.F 4.4; M6.A 4.2–4.4, M6.F 4.3; M7.A 4.2–4.5, M7.B
  4.2–4.4, M7.F Blokk 1; M5.1:651–655 („15–20 perc” ↔ részidők 9–13). **Kánon:** HUM-OPS-01 (HUM:224 időkeretek,
  :228 vétó/QA); HUM 8 „Időkeretek” (:465); HUM 9 „Az M3.A 4.3 blokk … 3 kártyával” (:492); a riportok verifier-korlátja
  (M2–M7 §3: „a 45’ és a blokkhatárok (HUM-OPS-01) nem változnak”); M3.A:309, M4.A:254 („belefér”).
- **Opciók:** (A) a 45′ és a blokkhatárok maradnak; a modulgazda peulánként vágási tervet ír (mi rövidül, mi kerül „ha
  az idő engedi” tartalékba), védett lépéslistával; a „belefér”-mondatok és a függő nyelvi tételek ezzel egy menetben ·
  (B) a bottom-up elv peulaszinten: a peula hossza a lépések összegére nő (időtartam-invariáns és központi naptár
  változik) · (C) vegyes: A, de ahol az alsó sávértékek összege is túlfut (M0.A, M2.A Blokk 3), ott B.
- **Ajánlás:** (A). Indok: a hat riport egybehangzó korlátja; a B a HUM-OPS-01 központi ütemezését nyitná újra; 10-10/5.
  A vágás helye modulgazdai ítélet. Védett, nem vágható: M0.A Blokk 3 3. lépése („madrih, nem terapeuta”), az M2 védett
  páros megosztása, az M3.A 3 kártyás átbeszélése (HUM 9), az M6.A 4.3.2/B, a zárókör és az M6.F 20 perces csendes
  pótlása, az M5.F 20–25 perces alsávja (HUM-OPS-01). M5.1: a meta (:7), a HUB:7, :41 és a 3,5 óra nem változik, csak a
  részidők újrabecslése vagy a sor meta-hivatkozása között lehet választani.
- **Következmények:** képzői végrehajthatóság (ma a képző rögtönöz); a vágás védett biztonsági lépést nem érinthet; az
  M4.B-nél előbb a PRG-2 `M4:PED-G2-1` (szerepcsere) kell; M3.B-nél a PRG-12 esetanyagával egy menetben.
- **Mit blokkol:** nem G-kapu; a next-version peulaszövegeit és a HOLD-blokkokat (pl. M4.B:324, M7.F :93/:102).
- **Ki hagyja jóvá:** az elvet a programvezető (HUM-OPS-01 jóváhagyó és vétó/QA); a vágási tervet az adott modulgazda
  (M3.B-nél a Memuna bevonásával), vétó/QA: programvezető.

### PRG-2 — Kimondott cél/kompetencia ↔ gyakorlás és mérés

- **Döntés:** Ahol a hub vagy a lecke olyan kompetenciát ígér, amelyet egyetlen feladat sem gyakoroltat vagy mér, a cél
  szűküljön a meglévőhöz, vagy készüljön új gyakorló/mérő elem?
- **Érintett findingok:** `M1:ERT-G1-3` (a HUB 4. kompetenciájának „záróreflexiós produktuma”), `M1:PED-G1-8` (HUB:93
  „4/5”, :97/:99 visszacsatolás), `M3:PED-G1-4` (HUB:27–29, M3.1:12) + függő `M3:NYELV-G1-12`, `M3:ERT-G2-5` (M3.2:12 ↔
  :29), `M4:ERT-G1-5` (HUB:46), `M4:PED-G2-1` (M4.B:19 ↔ :206), `M6:ERT-G2-3` (HUB:53/:62/:65, M6.2:15 ↔ :908, M6.3,
  M6.4:55–56; ide olvadt `M6:PED-G1-4`, `M6:PED-G2-2`, `M6:PED-G2-3`), `M6:PED-G1-2` (M6.1, HUB:84), `M7:PED-G1-8`
  (HUB:157, M7.1:15, :320), `Z:PED-G1-4` (HUB:92 ↔ Z.3). Az objektív alpontok (`.obj`) külön kulcsok.
- **Opciók:** (A) szűkítés: a cél, a hub vagy a címke a meglévő gyakorláshoz és méréshez igazodik (követő `/course-fix`)
  · (B) új gyakorló/mérő elem a PRG-4 `/course-develop` csomagban · (C) tételenként: alapértelmezés A, a projektgazda
  által kijelölt tételek B.
- **Ajánlás:** (C), alapértelmezett A-val. Indok: 10-10/5; HUM 7 (:445) „kevesebb gépezet, több mozgalom”. Kényszerítő
  korlátok az A felé: `M6:ERT-G2-3` M6.4-része (2026-10-05: „No new M6.4 round”); `M6:PED-G1-2` (a riport maga a 10-10/5-re
  hivatkozik); `M1:ERT-G1-3` B ága tárolt produktumként új adatkör volna (HUM-PRIV-01, DPO), a program mintája a
  tanuló-lokális reflexió (HUM 12 N-M1-04; HUM 10 D-2/D-3: a tárolt záró reflexió a Z.4); `M4:PED-G2-1`-nél időátosztásra
  nincs hely, mert az M4.B blokkjai már túlfutnak (PRG-1). `M3:PED-G1-4`: ajánlás nincs — projektgazda ítélete (Memuna
  QA); kockázat: a szűkítés nem törölheti a HUM 8 (:470) „Storming és kortárs bántalmazás: külön tanítjuk” tartalmát.
- **Következmények:** A esetén kapu-item és ✅ nem változik; B formatív elem, kapuhatás nélkül; M1-nél tárolás → DPO
  (X-4); M3 bántalmazási elem → Memuna-QA (G1).
- **Mit blokkol:** nem G-kapu; a B ágon G1 (M3) és G2 (M1, ha tárolt).
- **Ki hagyja jóvá:** projektgazda (célkitűzés), a modulgazdával; QA: értékelési felelős (`M3:ERT-G2-5`, M6), M6-nál a
  tartalomfelelős; M3-nál Memuna; M1-nél DPO, ha tárolt.

### PRG-3 — Ígéret ↔ leírt lépés a modulon belül (hub, meta, kártya-spec)

- **Döntés:** Ha a hub, a peula metája/célja vagy egy spec mást ígér, mint amit a részletes lépés ténylegesen leír, melyik
  az irányadó?
- **Érintett findingok** (zárójelben, mit adna az A szabály): `M1:PED-G3-9` (M1.A percbontás HUB:147–151, M1.F poszter és
  „cél 4” HUB:172–203, :221–222, M1.B-végi kérdés HUB:275–278 → a peulafájl), `M2:IMPL-G3-7` (M2-HUB-DIA-01, HUB:129, :149
  → a hub purpose/notes igazodik), `M3:PED-G3-4` (HUB:240 ↔ M3.F:111, :469 → M3.F) + függő `M3:NYELV-G3-2`,
  `M3:PED-G3-9` (M3.A kártyahátlap :87, :403, :425, KART-02/MUNK-01 ↔ a 4.3 lépései → kulcs a képzőnél), `M4:PED-G2-9`
  (M4.A:304 visszautalás ↔ :381 leadott kártya → az ígéret kikerül; a kártya-visszaadás az X-4 `M4:BIZT-G2-5`-től függ),
  `M7:ERT-G3-10` (HUB:418–422 kilépőkártya ↔ M7.A/M7.F nincs, M7.B:571 más → a hub szűkül), `M7:PED-G2-2` (HUB:225 ↔
  M7.3:868–869 → a hub igazodik), `M7:PED-G3-2` (M7.B:419, HUB:278 ↔ :14, :18, :564, :574; ide olvadt `M7:ERT-G3-8`,
  `M7:NYELV-G3-11` → a meta és a zárás a csoportos műhelyhez igazodik) + függő `M7:NYELV-G3-10`, `M7:NYELV-G3-17`.
- **Opciók:** (A) általános szabály: a ténylegesen leírt lépés az irányadó, az ígéret (hub, meta, cél, spec) igazodik —
  követő `/course-fix` · (B) az ígéret az irányadó, a lépés bővül (új tartalom → PRG-4; időigény → PRG-1) · (C) szabály
  nélkül, tételenként.
- **Ajánlás:** (A), a modulgazda tételenkénti kivételkérésével (B → PRG-4). Indok: a hubok peula-szakasza „Rövid
  percbontás-vázlat” (M1 HUB:146, :162, :218; M3 HUB:155, :206, :232), és a részleteket a peulafájlra bízza (M1 HUB:196
  „Részletek az M1.F peula-fájlban.”); a B a már túlfutó blokkokba tenne új lépést (PRG-1; pl. kilépőkártya mindhárom M7
  peulába); 10-10/5. `M7:PED-G3-2`: az A nem sérti a HUM 7 (:444) „v1 → köztes visszajelzés/átdolgozás → v2”
  invariánsát, mert a saját v1-re a kijelölt mentor ad visszajelzést (HUM-OPS-01 :222, PT:203) — ezt a programvezető
  erősítse meg. `M3:PED-G3-9`: ha a modulgazda az önellenőrzést választja, az egymondatos új instrukció (B).
- **Következmények:** hub-, meta- és `@asset`-szövegek (build, pin), a függő nyelvi tételek egy menetben; a QR-kilépőkártya
  (X-4 `M7:BIZT-G1-7`) és a névvel leadott kártya (X-4 `M4:BIZT-G2-5`) DPO-kérdés marad.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** a szabályt a programvezető; tételenként az adott modulgazda (az M1-poszternél és az M2-diagramnál a
  médiafelelőssel), vétó/QA: programvezető.

### PRG-4 — Egyetlen `/course-develop` csomag az új tartalomra

- **Döntés:** A kánon által előírt, de meg nem írt tanulói tartalom, valamint a PRG-2, -3, -5, -12, -13 és -15 „új
  tartalom” ágai egyetlen `/course-develop` csomagban készüljenek-e, ki írja és ki QA-zza?
- **Érintett findingok:** hibásválasz-visszajelzés: `M3:IMPL-G2-11` (M3.2–M3.4; ide olvadt `M3:ERT-G2-3`),
  `M4:ERT-G1-6` (M4.3 SLIDE 1 :200, SLIDE 5 K1 :513; a K3 az X-6 `M4:ERT-G1-1` után), `M5:PED-G1-4` (M5.1 SLIDE 4, M5.2
  B–D), `M6:IMPL-G1-5` (M6.1 SLIDE 8 K2, :1436–1437), `M7:IMPL-G2-5` (M7.3/M7.4, hét hely; ide olvadt `M7:ERT-G2-3`);
  pozitív visszajelzés: `M6:IMPL-G2-7` b) (M6.4:996); darabszám: `M4:ERT-G1-9` (M4.3 SLIDE 4: 12–15 előírva, 8 megírva,
  :429, :440, :473), `M7:ERT-G2-7` (M7.2 SLIDE 6 „min. 7”, négy leírás nélküli „Ha elfér”, :873–885, N-M7-02; ide olvadt
  `M7:PED-G2-7`), `M7:PED-G3-11` c) (M7.A KART-01 „10–12” ↔ 5 mondat). **Kánon:** RA:125 („hibás válasz után értelmes,
  nem csak »rossz« visszajelzés”), RA:170 (RT-A11Y-12); HUM-PED-01 (HUM:276–282); CLAUDE.md (a `/course-develop` tervét a
  projektgazda hagyja jóvá). Az objektív alpontok (`.obj`: semleges meglévő szöveg) külön kulcsok.
- **Opciók:** (A) egy csomag: a visszajelzések kötelezően, a darabszám-tételek és a többi PRG „új tartalom” ága a
  projektgazda kijelölése szerint · (B) most csak a kötelező visszajelzések, a többi a következő verzióban · (C) a
  visszajelzés-követelmény szűkítése (egységes semleges szöveg minden opcióra).
- **Ajánlás:** (A) a visszajelzésekre: az RA:125 kánoni követelmény, és akadálymentesítési követelmény nem gyengíthető,
  ezért a (C) csak ott jöhet szóba, ahol a meglévő semleges szöveg a `.obj` szerint elég. A darabszám-tételekre ajánlás
  nincs — szerző + szakmai lektor (M4), illetve modulgazda + értékelési felelős (M7) ítélete: megírás vagy a szám
  igazítása a megírt készlethez. Az `M6:IMPL-G2-7` b)-re az RA:125 nem vonatkozik (helyes válasz), az utasítás elhagyása is
  védhető.
- **Következmények:** ✅ és elosztó nem változik; az új gyermekvédelmi visszajelzés-szövegek a Memuna G1-átnézésébe esnek
  (X-7); M4-nél HUM-PED-01 lektor-QA (X-16); build és pin; a `/course-develop`-ot csak a felhasználó indítja.
- **Mit blokkol:** learner release: G5b (RT-A11Y-12), G1 (M3/M7 új szövegek), az M4 éles release-e (HUM-PED-01).
- **Ki hagyja jóvá:** a csomagtervet a projektgazda; szerző: a modulgazda / tartalomfelelős (M4: szerző); QA: Memuna
  (M3.3, M3.4, M7), szakmai lektor (M4), értékelési felelős (kulcsközeli szöveg).

### PRG-5 — Az F-peula kis létszámnál és hiányzásnál

- **Döntés:** Kapjanak-e a kapus F-peulák kis létszámú (1–5 fős) változatot, és mi a javító út annak, aki a kötelező
  F-peulán nem tud részt venni?
- **Érintett findingok:** `M1:PED-G3-8` (M1.F:47 „6–20 fő” ↔ KAPU:24, HUB:258), `M2:PED-G3-11` (M2.F:19; 1–3 főnél a név
  nélküli lapgyűjtés nem név nélküli), `M3:ERT-G3-10` (M3.F:43–44; programszintű: M1, M3, M5, M6, M7). **Kánon:** PT:286
  („F-peula … egyéni vagy kiscsoportos támogatással”; 1:1 csak a GK §4.2 kivételeként); HUM-OPS-01 (:221); HUM 8 (:455)
  és HUM 9 (:482): a javító próbálkozás az F-peula után nyílik; MAN:245, :248 (F-peula-activity nincs, a képző nyit
  felülbírálással); GK:98 (1:1 kivételek, legfeljebb 30 perc).
- **Opciók:** (a) kis létszám: (A1) minden kapus F-peulához kis létszámú változat · (A2) több modul közös F-peulája · (A3)
  a létszámsor marad, a képző rögtönöz. (b) hiányzás: (B1) pót-F-peula · (B2) az (a) szerinti változat pótidőpontban ·
  (B3) a képző egyéni egyeztetés után nyitja a javító próbálkozást (MAN:248).
- **Ajánlás:** (a) A1: a PT:286 kifejezetten egyéni vagy kiscsoportos F-peulát ír, és a HUM-OPS-01 szerint csak a kaput
  nem teljesítők vesznek részt, tehát a kis létszám a várható eset. (b) ajánlás nincs — programvezető + értékelési felelős
  ítélete; a sorrend (F-peula → javító próbálkozás) egyik opcióban sem változhat. Kockázat: egyéni (1:1) F-peula csak a
  GK:98 kivételeinek egyikeként (legfeljebb 30 perc, előre egyeztetett mentorbeszélgetés); ha nem illik, Memuna (X-5).
- **Következmények:** a javítás kis létszámnál is elérhető; kis létszámnál a „név nélküli” gyűjtés visszaazonosít
  (X-4 rokon); a változat szövege a PRG-4 csomagba; a pótidőpont szabálya a PRG-6 resynchez.
- **Mit blokkol:** learner release a kapus modulokra (a kötelező F-peula végrehajthatósága); G8 (a hiányzási út
  naptárszabály).
- **Ki hagyja jóvá:** programvezető + értékelési felelős (HUM 8–9 vétó/QA); a változat szövege: modulgazda; 1:1: Memuna.

### PRG-6 — A központi naptár szerkezeti pontjai a `SCHEDULE_TO_RESYNC`-ben

- **Döntés:** A programvezetői új ütemezés (HUM 11, pilot-ütemezés, PILOT-2) milyen szerkezeti szabállyal zárja az
  M0-megerősítés, az M7 kvíz ↔ v2 és a Z javító útjának réseit?
- **Érintett findingok:** `M0:IMPL-5` (MAN:220 ↔ a HUM-OPS-01 naptársora, `2026-10-02 Projektgazdai döntések.md` :188,
  :199), `M7:ERT-G1-2` (MAN:102; utána KAPU §0, HUB:144, M7.4 SLIDE 6), `M7:IMPL-G3-2` (M7.F:35 „1+1” ↔ MAN:20, :245,
  :247; második M7.F nincs), `Z:ERT-G1-7` (MAN:249 csak M2/M4; az LMS-Z-07 határideje „—”; utána a FIXED `Z:PED-G1-1`
  HUB:33 mondata újraszerkesztendő), `Z:QA-NYELV-1` (Z.3:217 ↔ :219, :241, SLIDE 6).
- **Opciók és ajánlás alpontonként:**
  - a) M0 „Megerősítés”: nincs / marad. **Ajánlás: nincs** — az M0-kvíz diagnosztikus jelző, nem kapu (HUM 6 :430, HUM 7
    :443), a 24 órás megerősítés kapueredményre szól (HUM-OPS-01 :220), az M0 határideje célidő (MAN:267).
  - b) M7 kvíz-megerősítés: kvízhatáridő a v2 elé, megerősítési ablakkal / a v2 határideje tolódik. **Ajánlás a
    kicsúszásra:** a madrih nem kerülhet hátrányba, a v2 határideje egyénileg tolódik (HUM-OPS-01 :220 „A függőben lévő
    eredmény nem bukás”; MAN:247 felülbírálási minta); a dátum a programvezetőé.
  - c) A kvízen bukott v2-jének javító helye: második M7.F / az egy M7.F fedi mindkettőt, a v2 javítóját a képző
    egyénileg ütemezi / más. **Ajánlás nincs** — korlát: 1+1 (HUM 8 :455), éles kapunál javító csak F-peula után (HUM 9
    :482).
  - d) Z javító útja. **Ajánlás (analógia):** a Z javítója automatikus (HUM 9 :482), a határidőt a képző jelöli ki
    (MAN:249 mintája), a programteljesítés bevárja (MAN:247); az LMS-Z-07 megerősítése a mentoré (BS-D8).
  - e) A Z.3 v1-útja. **Ajánlás:** kiterjed a :219, :241 és a SLIDE 6 szövegére — a Z „Még nem teljesítve” M7-eredménnyel
    is nyílik (MAN:247, Q-REL-2), így a javítási úton lévőnek a Z.3-kor nincs v2-je; az LMS-Z-07 kritériumai (MAN:109) a
    v2-t nem nevezik meg.
- **Következmények:** próbálkozásszám és küszöb nem változik; MAN §7, KAPU §0, HUB:144, M7.4 SLIDE 6 és Z HUB:33 egy
  menetben; dátumot a repó nem talál ki (PILOT-2).
- **Mit blokkol:** G8 — a naptár szabályai BUILD-besorolásúak (RR:34; a gépi verdikt ezt nem méri), a dátumok
  RELEASE-EVIDENCE; learner release az M7-re és a Z-re.
- **Ki hagyja jóvá:** programvezető (HUM-OPS-01 jóváhagyó); c) és e): + értékelési felelős; e): + modulgazda.

### PRG-7 — Kohorsz- és célzott beavatkozás a diagnosztikus jelzés után

- **Döntés:** Ki, mikor és mit tesz, ha a diagnosztikus kvíz kohorsz- vagy egyéni szinten gyenge eredményt jelez (M5
  „célzott felzárkóztatás”, M6 „extra online ismétlés / célzott támogatás”)?
- **Érintett findingok:** `M5:PED-G1-6` (M5 HUB:208), `M6:PED-G1-9` (M6 HUB:242, :247, KAPU:437; a „pár próbálkozás”
  az X-6 `M6:ERT-G1-7`-é); függő: `M6:NYELV-G1-10` → lásd X-6. **Kánon:** M6-NY-D7 (2026-10-04, M6 KAPU :38: „A stábnak
  kötelező figyelembe vennie az eredményt; a célzott ismétlés és a mentori egyeztetés ajánlott.”); HUM 8 (:467): a csendes
  pótlás és az F-peula két külön fogalom, a „felzárkóztató műhely” nem kanonikus név.
- **Opciók:** (A) felelős, forma és időpont kijelölése (pl. mentor vagy módszertani felelős, ismétlés a meglévő anyagból)
  · (B) a hub-ígéretek az M6-NY-D7 mintájára szűkülnek (kötelező figyelembevétel, ajánlott ismétlés és egyeztetés) · (C)
  új ismétlő anyag (PRG-4).
- **Ajánlás:** (B). Indok: ugyanannak a modulnak a kapujára a projektgazda már így döntött (M6-NY-D7); a hubra és az M5-re
  ez analógia, ezért megerősítés kell; nem hoz új kötelezettséget, és nem keveri a csendes pótlást az F-peulával.
- **Következmények:** a formatív, nem blokkoló státusz nem változik; M5 HUB:208, M6 HUB:242/:247 és a KAPU:437 (az X-6
  K6/K7 után) igazodik.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** programvezető + értékelési felelős.

### PRG-8 — Peulák és F-peula a Moodle-kurzusban (PT:219 ↔ MAN)

- **Döntés:** A PT:219 szerinti „Peulák” és „Extra / F-peula” blokk bekerüljön-e a manifestbe, vagy a PT pontosodjon?
- **Érintett findingok:** `M1:IMPL-G3-8` (PT:219 ↔ MAN:114, :248), `M0:IMPL-2` (ugyanaz a hiány; M0.3:159, :177).
  **Kánon:** PT:219; MAN:8, :114–133, :248; HUM 8 „Új kvíztételek” (:473: az M0 belépőkvíz tételei a projektgazda
  szövegével) — a 7. item ✅ C-je és visszajelzése (M0 HUB:254–260): „a peulákat a Moodle-kurzusban találod”.
  Kapcsolódó, ledger-kulcs nélküli nyitott kérdés: N-M4-07 (egységes 24 órás peula-értesítő; Anna-mátrix: UNRESOLVED).
- **Opciók:** (A) MAN-bővítés: modulonként „Peulák” leíróelem (nem activity, cmid és completion nélkül) és „Extra /
  F-peula” szakasz (jelenlét kézi completionnel opcionális, MAN:248); képzői peulaszöveg tanulói nézetbe nem kerül · (B)
  PT-pontosítás: a peulák nem jelennek meg a kurzusban.
- **Ajánlás:** (A). Indok: a lezárt projektgazdai kvízszöveg szerint a peulák a Moodle-kurzusban vannak; a lezárt döntés a
  kánon 1–3. forrásai fölött áll, a B ezzel ütközne. A leíróelem tartalma („mire készülj”) az N-M4-07-től függ.
- **Következmények:** az M0.3 ígérete teljesül; új adatkör nincs (nem activity); MAN „Kurzusszintű elemek” bővül.
- **Mit blokkol:** nem G-kapu a gépi verdikt szerint; a next-version build-specjének teljessége (G3a jellegű).
- **Ki hagyja jóvá:** programvezető + build-felelős.

### PRG-9 — Lecke-szintű build- és interakció-elhelyezés (három független alpont)

- **Döntés:** a) megmaradjon-e az M1.2 SLIDE 5 Drag & Drop; b) hol legyen az M2.1 SLIDE 4 a tanulói úton; c)
  Image-csomópont kerüljön-e az M3.3 passz-választó után, vagy maradjanak ki az ILL-01…04?
- **Érintett findingok:** a) `M1:IMPL-G1-8` (M1.2:797, :803; A11Y:32–33); b) `M2:IMPL-G1-3` (HUM 9 :487: az M2.1
  identitás-kör kérdése nem rögzített elem; RT-P0-21); c) `M3:IMPL-G2-4` (M3.3:421–672 ↔ :53–74 csomóponttérkép; a BQ
  kérdésmezője nem fogad képet; a lezárt BSPEC-05 térkép; HUM 11 SAFE-1).
- **Opciók és ajánlás:**
  - a) (1) indoklás a fejlesztői megjegyzésben + kötelező húzásmentes út / (2) a D&D kikerül, a rádiógombos út az egyetlen.
    **Ajánlás: (2)**, ha a szerző nem ad indokot — A11Y:32 „A Drag & Drop kerülendő ennél a mobil-first
    célközönségnél”, :33 indoklási kötelezettség.
  - b) CP-leírásba ágyazva / külön, nem követett activity előtte vagy utána / a CP kettébontása. **Ajánlás nincs** —
    build-/LMS-gazda ítélete; feltétel: a válasz nem rögzül (HUM 9 :487).
  - c) (1) H5P.Image-csomópont a „Végigmegyek” ág és az Sx-K1 közé, soha nem a passz-választó elé, saját alt-tal / (2) a
    négy illusztráció kimarad. **Ajánlás (gyenge): (2)**, ha a projektgazda nem lát bennük bizonyított tanulási funkciót:
    a szcenárió szövege a kérdésmezőben teljes, a Q-MED-1 szerint az illusztratív jelenet nem A-fázisú release-kötelező
    (HUM 10 :513), és a lezárt BSPEC-05 térkép nem nyílik újra.
- **Következmények:** a) és c) hozzáférhetőség (G5a); c) a passz előtti képi expozíció tilos (HUM-SAFE-03, SAFE-1); b)
  adat: nem rögzített elem marad.
- **Mit blokkol:** G5a/G3a jellegű build-spec a next-version buildje előtt (a gépi verdikt nem blokkolja); c) G1
  (Memuna-QA az elhelyezésre).
- **Ki hagyja jóvá:** a) szerző/modulgazda, indok híján a hozzáférhetőségi gazda (HUM-A11Y-01); b) build-/LMS-gazda + M2
  modulgazda (DPO nem kell); c) projektgazda (build-spec gazda), QA: Memuna, hozzáférhetőségi gazda.

### PRG-10 — Kötelező vagy opcionális; részvételi minimum

- **Döntés:** Kötelező-e az SBI a peula-visszajelzésben (M4.B), kötelező-e a valós kvuca-sor (M5), és mi az M5.A
  zárókörének minimuma?
- **Érintett findingok:** `M4:PED-G2-4` (M4.B:278 „add” ↔ HUB:138 „opcionálisan”), `M5:ERT-G2-9` (M5.4:146 „legyen” ↔
  HUB:20 „lehet” ↔ M5.B:312 „akár”; társ: X-4 `M5:BIZT-G1-5`) — függő: `M5:NYELV-G2-12` → lásd X-4; `M5:NYELV-G2-14`
  (M5.A:524 ↔ :496 passzjog, HUM-SAFE-03; vö. M5.B:478 „2–3 ember”).
- **Opciók:** kötelező / opcionális; a zárókörnél: mindenki sorra kerül, passzjoggal / néhány önkéntes.
- **Ajánlás:** `M4:PED-G2-4` → opcionális: a lezárt HUM-PED-01 (2) (HUM:280) és a HUM 8 „Produktum-visszajelzés”
  (:460) a Megfigyelés → Hatás → Következő lépés vázat teszi kötelezővé, az SBI-t csak megfigyelhető viselkedésre
  engedi; a HUB:138 is opcionálisnak írja. `M5:ERT-G2-9` → opcionális, egyenértékű kitalált profillal: a HUM 8 :461
  („A Peula v2 kvucája”: valós kvucára csak csoportszintű adattal, különben kitalált profil) mintája és az adattakarékosság
  alapján — az M5-re analógia, a DPO-ítélet (X-4) felülírhatja. `M5:NYELV-G2-14` → ajánlás nincs — modulgazda ítélete; a
  passzjog mindkét olvasatban érintetlen.
- **Következmények:** a kötelező/opcionális besorolás invariáns, csak e döntéssel változik; a rubrika a kvuca-sort nem
  méri; az M4.B:289–290 mintamondatai utána igazodnak.
- **Mit blokkol:** nem G-kapu; M4-nél a HUM-PED-01 lektor-QA (X-16).
- **Ki hagyja jóvá:** M4: modulgazda, QA: szakmai lektor; `M5:ERT-G2-9`: modulgazda + értékelési felelős, a DPO-val
  egyeztetve; `M5:NYELV-G2-14`: modulgazda.

### PRG-11 — Létszám-skálázás a peulákban

- **Döntés:** A 8–20 fős sávban hány csoport, hány fővel és hány kártyával/esettel dolgozzon a peula, ahol a csoportbontás
  nem fedi le a teljes sávot?
- **Érintett findingok:** `M2:IMPL-G3-6` (M2.B:331: 3 csoport × 3–5 fő csak 9–15 főt fed), `M3:IMPL-G3-9` (M3.A 2.2 ↔
  4.3, fix 8 kártya; M3.B 3–4 csoport, 4 eset, tartalék nincs; 8 és 16+ fő), `M0:NYELV-G2-22` (M0.A:347 „vagy páratlan a
  létszám” ↔ :344 „3–5 fős csoportok”; alacsony tét, „akár”).
- **Opciók:** (A) peulánkénti skálázási sor (létszám → csoportszám, csoportméret, darabszám) · (B) egységes programszabály
  (3–5 fős csoportok, a csoportszám a létszámból adódik, anyag a maximumra) peulánkénti kivételekkel · (C) a létszámsáv
  szűkül a lefedett tartományra.
- **Ajánlás:** nincs — modulgazda ítélete (a létszám és a darabszám számszerű invariáns, kánoni érték nincs). Hatékonysági
  megjegyzés: a B egy sablonnal mindhárom tételt lefedi.
- **Következmények:** a KART-01/-02 technical darabszáma build úton; M3.B esetkártyáinál gyermekvédelmi tartalom.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** az adott modulgazda (M3.B: + Memuna; M0: modulgazda / projektgazda).

### PRG-12 — Az M3.B esetanyaga (fiktív esetmondat, kimaradó 4. esetkártya)

- **Döntés:** Mi kerüljön az M3.B 4.3.3 „új, rövid, fiktív esetmondatának” helyére, és kimaradhat-e alapból az egyetlen
  felnőtt-gyanúsítottas (4.) esetkártya?
- **Érintett findingok:** `M3:PED-G3-2` (M3.B 4.3.3; ide olvadt `M3:IMPL-G3-8`), `M3:ERT-G3-2` (M3.B:186, :350, :406).
  **Kánon:** HUM 7 (:441: harmadik személyű esetelemzés), HUM 8 (:462: csak kitalált eset); a KAPU item-bank helyzetei
  tilosak (kapuszivárgás); GK §2 (az M3.B a Memuna G1-hatókörében).
- **Opciók:** (a) 2–4 előre megírt, harmadik személyű esetmondat (új tartalom → PRG-4) · (b) meglévő anyag: a kimaradó
  4. esetkártya vagy az M3.3 szcenáriói · (c) a :406 „Fontos különbség” doboz mindig elhangzik, akkor is, ha a 4.3.3 az
  első vágás.
- **Ajánlás:** (b) a 4. esetkártyával a 4.3.3-ban, + (c). Indok: csak meglévő kánoni anyag (új gyermekvédelmi szöveg
  nincs), és a felnőtt-gyanúsítottas eset kulcsüzenete akkor is elhangzik, ha a 4.3.3 időhiány miatt kiesik (PRG-1). A
  Memuna jóváhagyásával.
- **Következmények:** KAPU-helyzet nem kerülhet be; a megoldójegyzetek nem változnak; a PRG-1 M3.B-vágásával egy menetben.
- **Mit blokkol:** learner release: G1 (a Memuna M3.B-átnézése, X-7).
- **Ki hagyja jóvá:** M3 modulgazda + Memuna (tartalmi QA).

### PRG-13 — Mozgás nélküli részvétel a sarokjátékokban

- **Döntés:** Kapjon-e az M5.A 3 sarok játéka és az M6.A sarokszavazása mozgás nélküli részvételi módot?
- **Érintett findingok:** `M5:PED-G2-14` (M5.A:240; a galériasétán van: :437), `M6:PED-G3-9` (M6.A:377–378, :536–538; a
  :455 kézjeles alternatívája itt nincs). Minta: M6.A:455, M3.A:285, M5.A:437; a kánon mozgásos játékra nem ír elő
  alternatívát.
- **Opciók:** (A) a modulban már meglévő alternatíva (kézjel, helyben jelzés) átvétele a sarokjátékokhoz, rövid új
  résztvevői instrukcióként · (B) nem kerül be.
- **Ajánlás:** (A): ugyanazon peulák más pontján már van ilyen út (M6.A:455, M5.A:437), így a következetesség
  helyreáll, az M6 témája pedig az inkluzivitás. Új szakpolitikai szabály nem keletkezik; a mondat a meglévő mintájára
  készül.
- **Következmények:** offline peula, a G5 (H5P/Moodle) nem fedi; a játék célja nem változik.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** modulgazda + hozzáférhetőségi gazda.

### PRG-14 — AI-eredetjelölés és no-AI eszköz (két független alpont)

- **Döntés:** a) mely M4.3-itemek készültek generatív AI-val; b) milyen no-AI eszköz érhető el az M7.1 online leckében?
- **Érintett findingok:** a) `M4:BIZT-G1-7` (M4.3:22; PT:224; kiindulás: az M4.2 asset-notes „AI-asszisztált” jelölései,
  :95, :435, :601); b) `M7:NYELV-G1-14` (M7.1:413 „a promptkártya” ↔ nyomtatott promptkártya, M7.2:24, M7.B:480;
  HUM-PRIV-04; HUM 9 :488).
- **Opciók:** a) itemenkénti ténynyilatkozat → jelölés a lecke alján (PT:224), vagy ha nincs AI-item, a feltételes ígéret
  (:22) kikerül · b) (1) a dia saját promptkártyája / (2) nyomtatott promptkártya az online leckében is elérhetővé téve.
- **Ajánlás:** a) nincs — a szerző ténybeli nyilatkozata kell; címkét feltételezésből kitenni vagy elhagyni tilos. b)
  nincs — programvezető/modulgazda, DPO/jogi vétóval; korlát: a no-AI alternatíva nem törölhető és nem szűkíthető.
- **Következmények:** PT:224: az ember által olvasható eredetjelölés alapelv; b) HUM-PRIV-04 lánca nem változik.
- **Mit blokkol:** learner release: a) az M4.3 AI-jelölése (PT:224, nem önálló G-kapu); b) a HUM-PRIV-04 DPO/jogi QA-ja
  (G2-kör).
- **Ki hagyja jóvá:** a) tananyagfelelős / szerző; b) programvezető vagy modulgazda, vétó: DPO/jogi felelős.

### PRG-15 — Peula- és leckekulcsok, lezárások (három független alpont)

- **Döntés:** a) kapjon-e lezárást az M2.B érték-szigetek 3. helyzete; b) marad-e az M5.1 SLIDE 4 1./4. helyzetének
  „formális” kulcsa; c) kapjon-e kulcsot és összegző mondatot az M7.B A/B sarokkvíz 4–5. állítása?
- **Érintett findingok:** a) `M2:ERT-G3-4` (M2.B:208–209; KAPU B4/B10; ide olvadt `M2:PED-G3-6`); b) `M5:PED-G1-3`
  (M5.1 SLIDE 4 ↔ a lecke „kívül vagy mellett” definíciója és az M5.A:259 határesete; ide olvadt `M5:ERT-G1-6`,
  `M5:PED-G2-10` a)); c) `M7:ERT-G3-6` (M7.B:268–271; kánoni mondatok: KAPU:138, :186, M7.F:300; ide olvadt
  `M7:PED-G3-9`).
- **Opciók:** a) lezárás a KAPU B4/B10 elvével / a zárókérdés átírása (mindkettő új szöveg → PRG-4); b) a kulcs marad, a
  definíció és a határeset pontosodik / a kulcs igazodik a definícióhoz; c) kulcs + összegző mondat a kánoni mondatokból /
  kulcs nélküli játék marad („középen is maradhatsz”).
- **Ajánlás:** nincs — modulgazdai/szerzői ítélet (a: Memuna bevonásával; b: elsődleges forrás nincs, answer
  key-védelem; c: kulcsdöntés). c)-hez: ha kulcs kerül be, csak a megnevezett kánoni mondatokból.
- **Következmények:** ✅ csak e döntéssel változik; b) az M5.A:259 szándékos határesete érintett; c) EGY-01 build úton.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** a) modulgazda / módszertani felelős, a Memuna bevonásával; b) M5 szerzője / modulgazda; c)
  modulgazda.

### PRG-16 — Szerzői szándék-megerősítések (jelentéskérdések)

- **Döntés:** A modulgazda egy-egy mondatban megerősíti az alábbi helyek szándékolt jelentését; utána a nyelvi javítás
  objektív (`/hungarian-edit` vagy `/course-fix`).
- **Érintett findingok, opciók, ajánlás:**

  | Kulcs | Hely | Kérdés (olvasatok) | Ajánlás |
  |---|---|---|---|
  | `M1:NYELV-G2-9` | M1.3:803–805, :889–893; M1.4:470–471; MUNK-01 spec | az SBI-sablon S-rése határozói vagy tagmondatos | határozói: a sablon igazodjon a kánoni példákhoz (M1.3:428, M1.4:475, KAPU:87); QA: értékelési felelős |
  | `M1:NYELV-G3-16` | M1.A:277 | „tedd meg nyugodtan”: új cetlire írás, ha a 3 elfogyott? | nincs; a :282 önkéntessége nem gyengülhet |
  | `M2:NYELV-G1-12` | M2 HUB:103 | „egymás történeteinek megtartása”: megtartó figyelem vagy bizalmas kezelés | megtartó figyelem: a HUB:103 a kérdezés és a tükrözés mellett sorolja (M2.A:18), a bizalmas olvasat a teljes titoktartás tilalmába ütközne (KAPU:265, HUM-SAFE-01); bizalmas olvasatnál Memuna |
  | `M3:NYELV-G3-6` (csak b) | M3.A:462 | ki választja ki a 3 kártyát (T/2 ↔ E/2 képzői megszólítás) | nincs; a lépés és az időkeret nem változik (HUM 9 :492) |
  | `M4:NYELV-G2-2` | M4.4:62 | „pont ezért van … puha, formáló visszajelzés”: mire utal, marad-e | nincs; a horgony a `37472dc` után újra bizonyítandó, találgatott pótlás tilos |
  | `M6:NYELV-G1-1` | M6 HUB:228 | „nem valós szerepet játszunk le”: a tagadás hatóköre | nincs; az M6.1:1066–1068 minimuma nem gyengülhet, új példa nem kerül be |
  | `M7:NYELV-G2-15` | M7.4:308 | melyik v1-részbe kerüljön a beemelt anyag (nem létező mezők) | nincs |
  | `M7:NYELV-G3-12` | M7.B:433, MUNK-01 :291 | az „átjárás” szándéka | nincs |
  | `Z:NYELV-G1-15` | Z.3:147 ↔ :148 | szándékos-e a „túl kicsi” hibatípus (ide olvadt `Z:PED-G1-10`) | nincs |

- **Következmények:** jelentés-tisztázás; tartalmi szabály nem változik.
- **Mit blokkol:** nem G-kapu.
- **Ki hagyja jóvá:** az adott modulgazda (M2 bizalmas olvasatnál Memuna; M6: a hub tartalomfelelőse; Z: modulgazda vagy
  projektgazda).

### PRG-17 — Az M0.1 SLIDE 5 kérdése (CC-04)

- **Döntés:** Egy konstruktumot (kíváncsiság) vagy két kérdést (kíváncsiság + félelem) kérdezzen az M0.1 SLIDE 5, „1–2”
  vagy „2–3” modulra?
- **Érintett findingok:** `M0:ERT-8` (M0.1:330–351; objektív rész: `M0:ERT-8.obj`). **Kánon:** HUM 13 (:598), CC-04.
- **Opciók:** (a) egy konstruktum, „1–2” · (b) két kérdés, „2–3” · (c) a pilot-visszajelzésből adódó más forma.
- **Ajánlás:** nincs — a lezárt CC-04 szerint a tartalom a pilot-visszajelzéssel dől el; addig nem nyitandó.
- **Következmények:** a dia visszajelzése csak a választott konstruktumra reagáljon.
- **Mit blokkol:** csak későbbi fejlesztés (pilot után).
- **Ki hagyja jóvá:** projektgazda / modulgazda.

### Lezárt korlátok és „már lezárt / átvezetendő” tételek

Nincs olyan X-10 tétel, amelyet egy lezárt projektgazdai döntés szövege szó szerint, teljesen megválaszolna. Részben
lezárt korlátok (nem nyílnak újra, a döntés ezeken belül mozog):

| Kulcs | Lezárt rész | Helye |
|---|---|---|
| `Z:ERT-G1-7` | a Z javító próbálkozása automatikus | HUM 9 (:482) |
| `M7:ERT-G1-2` | a függőben lévő eredmény nem bukás | HUM-OPS-01 (HUM:220) |
| `M6:ERT-G2-3` | az M6.4-ben nincs új kör, új mérés nem kerülhet be | `2026-10-05 Projektgazdai döntés – M6.4 elfogadás…` |
| `M0:ERT-8` | a tartalom a pilot-visszajelzéssel dől el | HUM 13 (:598), CC-04 |
| `M3:PED-G1-4` | a storming és a kortárs bántalmazás külön tanítandó | HUM 8 (:470) |
| `M3:PED-G3-1`, `M3:NYELV-G3-6` | az M3.A 4.3 közös átbeszélése 3 kártyával fut | HUM 9 (:492) |
| `M7:PED-G3-2` | v1 → köztes visszajelzés/átdolgozás → v2 | HUM 7 (:444), HUM-OPS-01 (:222) |

## 10. LMS-megvalósítás és akadálymentesség — LMS-gazda / hozzáférhetőségi gazda

> Read-only vázlat a ledgerből (`AUTOPILOT-LEDGER.md`) és a validált riportokból; a repóban semmi nem változott. A
> sorszámok a HEAD `1d7b58d`-n visszaolvasva (ahol a ledger régebbi sort ad, zárójelben). Rövidítések: MAN = `LMS –
> activity manifest.md`, RA = `LMS – H5P runtime acceptance.md`, RR = `RELEASE-READINESS.md`, HUM = `Emberi jóváhagyás
> szükséges.md`, ADV = `Adatvédelem – tanulói adatok és AI.md`, GK = `Gyermekvédelem – release gate.md`, A11Y = `LMS –
> hozzáférhetőségi sztenderd.md`, PT = `Program terv.md`, VPS = `Média-assetek/VOICE-PILOT-SCRIPTS.md`, HUB/KAPU = a modul
> hubja/kapufájlja. **Elsődleges kapu:** a ledger-sor első megnevezett szerepe, illetve a kapusor „fő kapu” jelölése; a
> többi kapu csak hivatkozás. **Gépi állapot (5fcabea):** `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`,
> `LEARNER-RELEASE-VERDICT: NO-GO`. A „Mit blokkol” mezőben a kontrollált pilot az első valódi tanulói release
> (`READY_FOR_CONTROLLED_PILOT`), a learner release a `GENERAL_RELEASE` (HUM:509).

### LMS-1 — Fájlos beadási utak: elfogadott fájltípus és fájlszám (korpusz-szinten)
- **Döntés:** Milyen „Accepted file types” és „Maximum number of uploaded files” beállítást kapjanak az Assignment fájlos útjai, és mi legyen az online szövegszerkesztő kép-/fájlbeszúrásával, a „két egyenértékű út” megtartásával?
- **Érintett findingok:** `M1:IMPL-G2-10` (ide olvadt: `Z:IMPL-G1-9`). **Források:** M1 KAPU:297; M1.4:552, :465 (csak kitalált helyzet); MAN:24 (BIZT-1: az online szöveg szerkesztője fájlt fogad); Z.4:303, :336 (videós út: max. 1 fájl, 100–200 MB); M3.4:706; M4.4:731; HUM:457 (fájlfeltöltés önmagában nem completion); Moodle Docs 4.5 (üres mező = minden típus; M1-riport :622).
- **Opciók:** (A) sablonos utak dokumentumformátumokra szűkítve (a hozzáférhető sablon formátumai), max. 1 fájl, a szerkesztő kép-/fájlbeszúrása korlátozva; a Z.4 videós útja külön profil (videóformátum, max. 1). (B) csak fájlszám-korlát, üres típusmező, tanulói instrukcióval. (C) a fájlos út megszűnik — a PT §5 / KAPU:297 „két egyenértékű út” kánonját módosítaná, csak projektgazdai kánonmódosítással.
- **Ajánlás:** nincs — a DPO (adattakarékosság) és a hozzáférhetőségi gazda (a formátum akadálymentessége, M1.4-MUNK-01) ítélete. Kockázat ma: bármilyen fájl, így kiskorúról készült kép vagy valós beszélgetés képernyőképe is feltölthető, holott a kapuba csak kitalált eset kerülhet (GK:23).
- **Következmények:** adatvédelem: a feltölthető adatkör szűkül; a11y: a szűkítés nem zárhatja ki az akadálymentes formátumot; megvalósítás: a KAPU §5-ök és a MAN ASSIGN-sorai rögzítik; rubrika, küszöb, completion nem változik. A Z.4 videós út hozzájárulása külön kérdés (`Z:BIZT-G1-5`, X-4).
- **Mit blokkol:** staging buildet nem; az M1-review (2026-10-10) POST-PILOT-nak sorolta → learner release előtt, a G2/G5 FINAL_RELEASE_QA tárgya.
- **Ki hagyja jóvá:** LMS-gazda + DPO + hozzáférhetőségi gazda (X-11; HUM-A11Y-01).

### LMS-2 — Az M3 Drag and Drop mellékútja
- **Döntés:** Megmarad-e az M3.4 SLIDE 4 és az M3.2 7B Drag and Drop-ja mellékútként a húzásmentes alapút mellett?
- **Érintett findingok:** `M3:IMPL-G2-2` (objektív része `M3:IMPL-G2-2.obj` FIXED, 3ae0c09: az M3.2 koppintásos alaputja a jelenetenkénti MC). **Források:** M3.4:410–417 (EGY-03, D&D), :442–454 (EGY-05, MC), :467, :512; M3.2:592–599; A11Y:32–33 („Drag & Drop kerülendő”; ha mégis, a fejlesztői megjegyzésben indokolni kell); h5p-drag-question `semantics.json` (kártyánkénti visszajelző mező nincs; M3-riport :806); RA 13. pont (:81).
- **Opciók:** (A) a D&D elhagyása, egyetlen húzásmentes út kártyánkénti visszajelzéssel. (B) a D&D marad, indoklással (A11Y:33), a „per-kártya visszajelzés ugyanaz” mondatok igazításával (a D&D-n csak célzónás visszajelzés). (C) a D&D marad eltérő visszajelzéssel, a tanulói szöveg jelzi a különbséget.
- **Ajánlás:** (A) — az A11Y §3 alapértelmezése, indoklás egyik leckében sincs, és a D&D a leckében ígért kártyánkénti visszajelzést technikailag nem tudja (`semantics.json`). A hozzáférhetőségi gazda vétója érvényes.
- **Következmények:** tanulás: egy út, azonos visszajelzés; a11y: az SC 2.5.7 egyszerűbben igazolható; megvalósítás: az EGY-03 kivezetése build úton; kártyák, kulcs, ✅ nem változik. Az `M3:IMPL-G2-11` (X-10) új visszajelzés-szövege csak a megmaradó úton jelenhet meg: egy menetben.
- **Mit blokkol:** staging buildet nem; G5b + független a11y pre-flight (FINAL_RELEASE_QA) → kontrollált pilot (M3).
- **Ki hagyja jóvá:** M3 modulgazda; vétó/QA: hozzáférhetőségi gazda. Rokon, másik kapun: `M1:IMPL-G1-8` (X-10, az M1.2 SLIDE 5 D&D-indoklása, ugyanaz az A11Y:33-kérdés).

### LMS-3 — Az M5.3 késleltetett felidézési pontjának H5P-típusa és önellenőrzése (N-M5-08)
- **Döntés:** Melyik grade-et adó, szabad szöveget nem tároló H5P-elem valósítsa meg az LMS-M5-07-et, és kap-e a felidézés után önellenőrző lépést?
- **Érintett findingok:** `M5:IMPL-G2-2`, `M5:PED-G2-11` (egy döntési pont; `M5:IMPL-G2-2.obj` FIXED, b429420: „Moodle Label /” törölve, MAN:85). **Források:** M5.3:522–547 (:530 „rövid H5P”, :543 a helyességtől független nyugtázás); MAN:85 (H5P-C), MAN:16 (BSPEC-06 „Receive a grade”), MAN:165 (az online félév feltétele); RA 4. pont (:40); HUM:516 (RM-D6); GL:198.
- **Opciók:** (A) rövid Course Presentation összefoglaló diával: a két fejben végzett felidézés után pontozott önellenőrző itemek visszajelzéssel; a grade az összefoglaló diáról jön, és ez adja a PED-G2-11 önellenőrzését (új tanulói tartalom). (B) rövid CP pontozott elem nélkül, a mai nyugtázással: a grade az összefoglaló dia elérésén múlik (az `M0:IMPL-3` nyitott kérdése, X-6), önellenőrzés nincs. (C) más, szabad szöveget nem tároló pontozott típus az LMS-gazda választásával. Kizárt: Free Text, Essay.
- **Ajánlás:** nincs — az LMS-gazda és a módszertani lektor/tananyagfelelős (típus), valamint a modulgazda (önellenőrzés) ítélete; igazodjon az `M0:IMPL-3` (X-6) döntéséhez.
- **Következmények:** tanulás: önellenőrzés nélkül a felidézés helyessége nem derül ki (GL:198); a 72 óra, a kötelező státusz, a completion és az értesítési tilalom nem nyílik újra; megvalósítás: a MAN:85 típusmezője és az M5.3:530 igazodik.
- **Mit blokkol:** staging build: az LMS-M5-07 típus nélkül nem konfigurálható a BSPEC-06 szerint (a gépi verdikt ezt nem méri); kontrollált pilot: az online félév feltétele (MAN:165), RT-P0-04.
- **Ki hagyja jóvá:** LMS-gazda + módszertani lektor/tananyagfelelős; az önellenőrző lépésről a modulgazda.

### LMS-4 — Az M6 játéklap 1/2/3 szintű rubrikájának Moodle-normalizálása
- **Döntés:** Milyen Grade type, Maximum grade és rubrika-minimum beállítással fusson az LMS-M6-05, ha a Moodle a rubrikapontot a minimumtól normalizálja?
- **Érintett findingok:** `M6:IMPL-G1-7`. **Források:** M6 KAPU:385–386 (1/2/3 szint, minden sor ≥2, R4/R5 blokkoló); MAN:91 (Grade type és Maximum grade hiányzik; vö. MAN:50, :66, :103), MAN:93 (LMS-M6-07 GATE-CP); RA 1. pont (:37), 8. pont M6 negatív esete (:55); Moodle Docs Rubrics, G = Σ(gᵢ−minᵢ)/Σ(maxᵢ−minᵢ) (M6-riport :528).
- **Opciók:** (A) Point, Maximum grade = 15, 1/2/3 szintpont, a „minimum 0” beállítás rögzítve; a nyers szám tájékoztató, a kapudöntést a GATE-CP hordozza. (B) a szintpontok 0/1/2-re vetítése (az M1/M3/M7 mintája) — értékelési döntés, a küszöb és a szintleírás átírásával. (C) az (A), a rubrika-pontszám tanulói megjelenítésének rögzítésével.
- **Ajánlás:** nincs — az LMS-gazda és az értékelési felelős ítélete. Kockázat: rögzítés nélkül a csupa „Oké” lap (10) kisebb nyers számot kaphat, mint az RA bukó esete (11).
- **Következmények:** értékelés: (A)/(C) mellett szintpont, küszöb, blokkoló logika nem változik; a továbblépés a GATE-CP-n múlik (MAN:93); megvalósítás: a MAN:91 kiegészül, RT-P0-01 visszaolvasás.
- **Mit blokkol:** staging build: az LMS-M6-05 grade-beállítása (gépi verdikt nem méri); kontrollált pilot: RT-P0-01, -08.
- **Ki hagyja jóvá:** LMS-gazda + értékelési felelős.

### LMS-5 — Az M7.3 Checklist-aktivitás formája, completionje és tárolása (K18)
- **Döntés:** Plugin- vagy core úton, milyen manifest-sorral, completionnel és visszajelzéssel épüljön a „Zmán Kvucá-checklist – péntek esti mintaprogram”, és tárolódik-e a tanulói komment és a „Záró nyitott kérdés” válasza?
- **Érintett findingok:** `M7:IMPL-G2-1` (ide olvadt: `M7:IMPL-G1-1`, `M7:PED-G2-1`, `M7:ERT-G2-1`, `M7:BIZT-G2-5`), `M7:NYELV-G1-5` (HUB:116, a döntéssel egy menetben; `.obj` FIXED). **Források:** M7.3:7–8, :796, :818, :823–884 (:831 „hagyd pipa nélkül”, :866 „Záró nyitott kérdés”); HUB:116, :217; MAN:97 (csak LMS-M7-03), MAN:35; RR G3a; mod_checklist `lang/en/checklist.php`, `lib.php` (completion csak százalékos/darabszámos; `studentcomments` létezik; M7-riport :778).
- **Opciók:** (A) mod_checklist (G3a pluginlista), saját manifest-sor; completion nincs vagy kézi (a százalékos ütközik a „hagyd pipa nélkül” szabállyal); tanulói komment kikapcsolva és a záró kérdés tanuló-lokális, vagy bekapcsolva ADV §3-sorral és tájékoztatóval. (B) core út: a checklist az LMS-M7-03 H5P-C-ben, tanuló-lokális, nem tárolt elemként (a D-4 mintája), külön aktivitás nélkül; a HUB:116, :217 és az M7.3:7–8, :818 igazodik. (C) letölthető checklist (File/Page), completion nélkül.
- **Ajánlás:** nincs — projektgazda (build-spec), LMS-gazda (plugin vagy core), DPO (szabad szöveg tárolása, az `M3:IMPL-G2-6` csomag elve, X-4) és értékelési felelős (kötelezőség, completion) ítélete.
- **Következmények:** a 12 tétel, az 5 terület, a „csak azt pipáld” szabály, a SLIDE 5 kulcsa és a „Záró nyitott kérdés” nem változik és nem törölhető; tárolt komment = új adatkör (G2); a HUB:116 HOLD-blokkja (fix-terv #100) a döntés után; az `M7:PED-G2-2` (X-10, a záró kérdés tárgya) külön döntés.
- **Mit blokkol:** staging build: az M7.3 aktivitás manifest-sor nélkül nem építhető (gépi verdikt nem méri); plugin esetén G3a; kontrollált pilot (M7): G2, ha tárol.
- **Ki hagyja jóvá:** projektgazda + LMS-gazda/Moodle-adminisztrátor + DPO; a completionről értékelési felelős.

### LMS-6 — Az M7.4 SLIDE 4 pontozatlan fókuszválasztójának H5P-útja
- **Döntés:** Milyen H5P-elemmel valósuljon meg a 3–4 terület kijelölését kérő, helyes válasz nélküli fókuszválasztó?
- **Érintett findingok:** `M7:IMPL-G2-7`. **Források:** M7.4:505–543 (:522–525 „3–4 terület”, :543 „ne pontozott Multiple Choice legyen”), :455 (SLIDE 3 precedens: MC, minden opció helyes); HUM:558 (D-d: nem completion-elem); RA 14. pont 3. alpont (:85); h5p-multi-choice `semantics.json` (`singlePoint` + `passPercentage`: bármely kijelölés 1/1; M7-riport :761); A11Y §3 (következetes interakció a modulon belül).
- **Opciók:** (A) Multiple Choice többválaszos, minden opció helyes, `singlePoint` + alacsony `passPercentage`; a :543 mondata igazodik. (B) interakció nélküli lista, tanuló-lokális jegyzettel. (C) más pontozatlan elem, ha a célverzión igazolható.
- **Ajánlás:** nincs — LMS-gazda ítélete. A lecke saját SLIDE 3-mintája az (A) felé mutat, de a :543 ma kizárja; a próbája az RA 14. pont 3. alpontja.
- **Következmények:** a hét fókuszterület és a D-d nem változik; a :544 terjedelem-javítását nem blokkolja; a :543 fejlesztői mondata a döntést követi.
- **Mit blokkol:** staging build: az LMS-M7-04 egy diájának konfigurációja (gépi verdikt nem méri); kontrollált pilot: RT-P0-14.
- **Ki hagyja jóvá:** LMS-gazda.

### LMS-7 — Az M7.2-DIA-01 alt-szövege: a PT:221 rövid vagy a lecke részletes változata
- **Döntés:** A Program terv :221 (a) altja kerüljön az M7.2-DIA-01-hez, vagy a lecke mai, részletes altja marad, és a PT igazodik?
- **Érintett findingok:** `M7:IMPL-G2-12` (a) (a (b)–(d) `.obj` FIXED, 729342a: PT:221 szó szerint). **Források:** PT:221 (a); M7.2:307–321 (asset), :400–405 (DIA-01-ALT; a :404 szerint a dián a lista a diagram teljes szöveges ekvivalense); A11Y §2 (:26–27); kánoni sorrend (CLAUDE.md: PT = 1.).
- **Opciók:** (A) PT:221 (a) szó szerint. (B) a részletes alt marad, a PT:221 (a) módosul (projektgazdai kánonmódosítás).
- **Ajánlás:** (A) — a PT a kánoni sorrend első forrása, a (b)–(d) ugyanígy, szó szerint került át, a teljes tartalom pedig élő szövegként a dián áll. A hozzáférhetőségi gazda vétója érvényes, ha a rövidebb altot kevésnek tartja.
- **Következmények:** a11y: rövid alt + élő szöveges ekvivalens; megvalósítás: build úton, `chore(media)`.
- **Mit blokkol:** egyiket sem (mindkét változatban van alt); a G5b/a11y pre-flight előtt célszerű lezárni.
- **Ki hagyja jóvá:** projektgazda; vétó: hozzáférhetőségi gazda.

### LMS-8 — A kurzus AI-segédjének Moodle-formája, helye és hozzáférési feltétele
- **Döntés:** Milyen Moodle-formában, hol és milyen feltétellel érhető el az opcionális AI-segéd a lezárt HUM-PRIV-04 láncán?
- **Érintett findingok:** `M7:IMPL-G3-8` (ide olvadt: `M7:BIZT-G1-4` (b)). **Források:** M7.B:627 (csoportonkénti hozzáférés), :75, :478; MAN:119 (csak felsorolja), :94, :96, :98; HUM:189–191 (HUM-PRIV-04: `Moodle → Somer szerveroldali végpont → OpenAI Responses API`, saját fiók nélkül, a promptot a képző vagy a backend küldi); RA 20. pont (:97–102); ADV §7.
- **Opciók:** (A) kurzusszintű blokk/plugin a Somer végpontjára (G3a). (B) külön Moodle-aktivitás (pl. külső eszköz) az M7-ben, csoportos hozzáférési feltétellel. (C) tanulói Moodle-felület nélkül: a képző küldi a promptot (HUM-PRIV-04, M7.B:478 megengedi); a „kurzus AI-segédje” mondatok igazodnak.
- **Ajánlás:** nincs — a programvezető és a Moodle-adminisztrátor ítélete, DPO/jogi vétóval. Kockázat: forma nélkül az RT-P0-20 (RT-5) nem futtatható.
- **Következmények:** a HUM-PRIV-04 lánca, a tanulói mondat és a kötelező no-AI út nem változik; kapcsolódó, másik kapun: naplózás/megőrzés `M7:BIZT-G2-3` (X-4), magas kockázatú bevitel `M7:BIZT-G1-4` (X-5), DPO QA `M7:BIZT-G1-3` (X-12).
- **Mit blokkol:** staging build: plugin esetén G3a; kontrollált pilot: közvetve, az RT-P0-20-on át.
- **Ki hagyja jóvá:** programvezető + Moodle-adminisztrátor; vétó/QA: DPO/jogi felelős.

## 11. Runtime-bizonyíték — build-felelős (G3)

Nem döntések: staging-tesztek tesztfiókkal, dátummal és pontos verzióval; `RUNTIME_VERIFIED` csak tényleges eredménnyel
írható (RA:31; RR staging-szabály 5.). Eredmény, „átnéztem” vagy dátum a tananyagba nem írható be. Javasolt sorrend:
RT-1, RT-2 (M0+M1, a legkisebb staging-szelet, PILOT-1), majd RT-3…RT-6.

### RT-1 — „Segítség és kapcsolatok” blokk: kitöltés és megjelenés
- **Bizonyíték-igény:** a négy szerep szerinti kontakt (technikai, tanulási/program, kijelölt mentor, Memuna) kitöltve, és tanulói tesztfiókkal láthatóan visszaolvasva.
- **Érintett findingok:** `M0:IMPL-9`. **Források:** HUM:552 (PILOT-3), HUM:243 (HUM-OPS-02); M0.2:473; RR G8 (:34); RA 17. pont (:88).
- **RT-sor:** RT-P0-17; G4b staging visszaaudit (RR :112).
- **Ki igazolja:** LMS-gazda (megjelenés); a valódi technikai és programkontakt: programvezető (HUM-OPS-02 jóváhagyója, RELEASE-EVIDENCE); a Memuna-adat a HUM-SAFE-01-ből.
- **Kapu, blokkol:** G4b, G8 → az M0+M1 kontrollált pilot (PILOT-3: kitöltetlen csatornával learner-facing pilot nem indul).
- **Runtime-rész itt, elsődleges kapu máshol:** `M2:BIZT-G2-8` (RT 17. pont; lásd X-7).

### RT-2 — M0+M1: completion, unlock, kapumechanika, próbálkozások, a SLIDE 5 adatmentessége
- **Bizonyíték-igény:** célverziós visszaolvasás tanulói, képzői és mentori tesztfiókkal.
- **Érintett findingok:** `M1:BIZT-G1-3` (RT-P0-24 az LMS-M1-01-re; ide olvadt: IMPL-G1-4, PED-G1-2, az ERT-G1-2 SLIDE 5-része), `M1:ERT-G1-2` (RT-P0-09 üres SLIDE 5-tel, -13 az M1.2 húzásmentes útja, -14 a SLIDE 1–2 pontozatlan választói), `M1:IMPL-G2-4` (RT-P0-01 Max grade 8 / Grade to pass 5, -08 a 0/1/2/2 negatív eset és a GATE-CP állapotmátrix, -09 az LMS-M1-03 → -07 → -04 → -05 lánc, -19; ide olvadt IMPL-G3-2). **Források:** RA 1., 8., 9., 13., 14., 19., 24. pont (:33–37, :50–71, :72, :81, :82–85, :90–96, :106); MAN:16, :45–51; HUM:587–588 (N-M1-04); M1.4:496–500; M1 KAPU:303–306.
- **Nem nyitott ledger-sor, de a kapusor része (kánoni tesztpont kész, runtime nyitott):** `M0:ERT-2` → RT-P0-25 (LMS-M0-06 üres beküldés, HUB:181 működő ága); `M1:QA-IMPL-3`, `M1:ERT-G2-6` → RT-P0-26 (LMS-M1-05 rubrika-előnézet, MAN:50); `M1:QA-IMPL-2` → RT-P0-19 (KAPU:306 „Grant attempts” = „Manually”, „Allowed attempts” = „Unlimited”); `Z:IMPL-G1-1` (d) → RT-P0-03/-19 (LMS-Z-04 újranyitás után a mentor újra dönt).
- **Ki igazolja:** LMS-gazda / build-felelős (G3b); az M1.2 húzásmentes útját a G5b-ben a hozzáférhetőségi gazda pre-flightja is.
- **Kapu, blokkol:** G3b, G5b (POST-BUILD) → az M0+M1 kontrollált pilot GO (PILOT-1; a 2026-10-10-i M1-review PILOT-BLOCKER-nek sorolta).
- **Megjegyzés:** az RT-P0-24 sikeréig az M1.1 SLIDE 5 beviteli elem nélkül, saját jegyzetes úton nyílik (HUM:588); beviteli elem nélkül ezt kell rögzíteni (RA:106). DPO-rész (BIZT-QA-1): lásd X-12. Runtime-rész itt, elsődleges kapu máshol: `M1:BIZT-G2-2` (RT-P0-15 két mentorral, két csoporttal, HUM:576; lásd X-12).

### RT-3 — M4 célverziós tesztcsomag
- **Bizonyíték-igény:** az M4 kapu-, completion-, láthatósági, média- és a11y-tesztjei; az értesítő és az `M4_ASSIGN` dátuma.
- **Érintett findingok:** `M4:IMPL-G2-12`. **Források:** M4-riport :183; RA:133–170; MAN:239 (értesítő), :280 (`M4_ASSIGN`: `SCHEDULE_TO_RESYNC`).
- **RT-sorok:** RT-P0-01, -06, -08, -09, -14, -15, -19, -22, -23; RT-A11Y-01…12. Az RA 9. pont negatív esete az `M0:IMPL-3` csomagja (X-6).
- **Ki igazolja:** LMS-gazda (G3b), hozzáférhetőségi gazda (G5b); a dátumokat a programvezető állítja be (G8 RELEASE-EVIDENCE; PILOT-2: dátum nélkül felépíthető, tanulónak nem nyitható). DPO-rész (G2): lásd X-12.
- **Kapu, blokkol:** G3b, G5b, G8 → kontrollált pilot (M4).

### RT-4 — M6.4 Branching Scenario
- **Bizonyíték-igény:** a D-e szerinti fix lánc (A → B → opcionális C → D → 6D → ZÁRÓ) determinisztikus a célverzión, és csak a végképernyő ad completiont.
- **Érintett findingok:** `M6:IMPL-G2-2`. **Források:** M6-riport :257; MAN:90 („runtime bizonyítandó”); HUM:559 (D-e), :561 (D-g); RA 2., 5. pont (:38, :41).
- **RT-sorok:** RT-P0-02, -05, -09, -14, -22, -23, -24; RT-A11Y-01…12. Ha egy negatív eset elbukik, a BSPEC-05 újranyílik (HUM:561).
- **Ki igazolja:** LMS-gazda (G3b), hozzáférhetőségi gazda (G5b). DPO-rész (D-5, G2): lásd X-12; G1-alpont: `M6:BIZT-G2-3` (X-7).
- **Kapu, blokkol:** G3b, G5b → kontrollált pilot (M6).

### RT-5 — Az AI-segéd adatkezelése és a no-AI completion (M7)
- **Bizonyíték-igény:** `/v1/responses` `store=false`, Conversations API és tartós fájlfeltöltés nélkül; ZDR állapota rögzítve; személyes adat nem megy át; az LMS-M7-01/-02/-04 no-AI úton is teljesül.
- **Érintett findingok:** `M7:IMPL-G1-11` (ide olvadt az `M7:IMPL-G2-10` AI-része). **Források:** RA 20. pont (:97–102), :152; HUM:191; M7.1:412, HUB:133, :280, M7.2:68, :114, M7.4:80, M7.B:75, :477, :587, :627.
- **RT-sor:** RT-P0-20.
- **Ki igazolja:** LMS-gazda (G3b); a DPO/jogi QA a HUM-PRIV-04-re: `M7:BIZT-G1-3`, lásd X-12.
- **Kapu, blokkol:** G3b → kontrollált pilot (M7). **Előfeltétel:** az LMS-8 döntése és megvalósítása.

### RT-6 — Az M7 párosításainak húzásmentessége
- **Bizonyíték-igény:** az M7.2 SLIDE 6 (:862) és az M7.3 SLIDE 4 párosítása a renderen egy kattintással/koppintással is végigvihető, azonos visszajelzéssel és completionnel; célméret mobil portrait nézetben.
- **Érintett findingok:** `M7:IMPL-G2-10` (csak az RT-P0-13 maradéka; a Memuna-rész = `M7:BIZT-G1-5`, X-7). **Források:** RA 13. pont (:81), :145; A11Y §3.
- **RT-sor:** RT-P0-13.
- **Ki igazolja:** LMS-gazda; a G5b-ben a hozzáférhetőségi gazda és a független pre-flight.
- **Kapu, blokkol:** G5b → kontrollált pilot (M7).

**Runtime-részük itt van, de az elsődleges kapujuk máshol (első megnevezett szerep):** `M1:BIZT-G2-2` → X-12 (RT-P0-15);
`M2:BIZT-G1-9` → X-12 (RT-P0-21); `M2:BIZT-G2-9` → X-12 (RT-P0-15); `M2:BIZT-G2-8` → X-7 (RT-P0-17);
`M3:BIZT-G2-10` → X-7 (RT-P0-09, -11, -13, -14, -22, -24, RT-A11Y; értékelési QA: X-9); `Z:BIZT-G1-10` → X-7 (RT-P0-03,
-12, -15, -16, -24; DPO: X-12); `M3:BIZT-G1-5` → X-4 (a passz-adat célverziós visszaolvasása: RT-P0-11).

## 12. Hang- és VO-gyártás — médiafelelős

### VO-1 — 3. hanggyártási fix pack: 15 `@source`-blokk javítása
- **Döntés:** Készüljön-e most egy fix pack a privát VO QA-repóban az alábbi `@source`-javításokkal (a kurzusoldalon `/course-fix`, utána build), és mely blokkoknál kell újrarender?
- **Érintett findingok:** `M1:BIZT-G2-7`, `M1:NYELV-G1-6`, `M1:NYELV-G2-5`, `M3:NYELV-G1-13`, `M3:NYELV-G2-15`, `M4:NYELV-G1-12`, `M6:NYELV-G1-7`, `M6:NYELV-G2-1`, `Z:NYELV-G1-6`, `M7:NYELV-G2-9`, `M7:NYELV-G2-11` c) (a b) része: lásd X-6, K4 = `M7:ERT-G1-11`), `M7:NYELV-G2-13` a); rész: `M6:NYELV-G1-11` (kulcsa: TECH-2). Az objektív `.obj` részek mind FIXED. **Források:** `Média-assetek/README.md` :100–103 (a felmondandó szöveg a `@source`-ban változik, utána build); VOICE-BIBLE §9 (:213–233: a felvétel eltérése a szövegtől hiba), 13.6 (:515–516: újragyártásnál a teljes tétel újravétele); a riportok VO-korlátja (pl. M3-riport :1154, Z-riport :312); HUM:524 (D-1).
- **Helyek** (`fájl:sor` — blokk — csere; * = változik a kimondott szöveg):
  - M1.3:813 — M1.3-NAR-04-VO — „beírni” → „leírni”*; + spec :749 „írja be” → „írja le” (D-1)
  - M1.2:640 — M1.2-NAR-04-VO — „szóra vagy kifejezésre” → „szóra”*; + spec :573 „szóra/kifejezésre” → „szóra”
  - M1.3:1058 — M1.3-NAR-06-VO — „az Assignmentben” → „a beadandóban”*; + spec :940
  - M6.1:485 — M6.1-NAR-03-VO — „bizalom- vagy kontaktjátékok” → „bizalom- és kontaktjátékok”* (az :454, :857 alakja)
  - M6.3:974, :976 — M6.3-NAR-05-VO — „Tanít közös döntést:” → „Közös döntésre tanít:”, „Tanít felelősséget:” → „Felelősségre tanít:”*
  - Z.1:271 — Z.1-NAR-01-VO — „M0-ban … M7-re” → „az M0-ban … az M7-re”*; + spec :195 (fix-terv #42)
  - M3.1:279 (NAR-02-VO), :523, :526, :533 (NAR-03-VO) — „**adjourning**-ot”, „**forming**-ban”, „**storming**-nál”, „**performing**-ban” → közvetlen toldalék (a :286/:785 „stormingként” mintája)
  - M3.3:996 — M3.3-NAR-03-VO — „egy alap térképed” → „egy alaptérképed”
  - M4.1:826 — M4.1-NAR-05-VO (az M4.1-VID-05 is erre hivatkozik) — „hogy…’.”” → „hogy…’””
  - M7.2:735 — M7.2-NAR-04-VO — „élmény-fázis” → „élményfázis”; M7.2:846 — NAR-05-VO — „red flag-ek” → „red flagek”; M7.3:649 — NAR-04-VO — „red flag-et” → „red flaget”
  - M7.3:153 — M7.3-VID-01-VO — beágyazott „…” → ‘…’ (az M4:NYELV-G2-11 mintája)
  - M6.1:202 — M6.1-VID-01-VO — „játék-kategóriákban” → „játékkategóriákban” (rész; kulcs: TECH-2)
- **Opciók:** (A) egy pack, mind a 15 blokk újrarenderelve és meghallgatva. (B) egy pack; újrarender a 6 kimondottszöveg-változásos blokknál (*), a 9 írásmód-/tipográfiai blokknál a VO-gazda a kiejtési szótár aliasai (VO D-03, D-04) és a forrás-hash alapján igazolja, hogy a meglévő hang változatlanul érvényes, különben újrarender. (C) halasztás a következő gyártási körig: a `@source` és a hang változatlan, a hibák a leiratban is maradnak.
- **Ajánlás:** (B) — a VOICE-BIBLE §9 a kimondott szöveg és a felvétel egyezését követeli meg, ez a 9 írásmód-blokknál újrarender nélkül is fennállhat; a két videó (M7.3-VID-01, M6.1-VID-01) így csak felirat-/leiratjavítást kap. Az M1.3-NAR-04 a lezárt D-1 átvezetése, ezért a halasztás (C) nem ajánlott.
- **Következmények:** tanulás: a leirat és a felirat a `@source`-ból készül, a hibák addig tanulói szövegként is látszanak; megvalósítás: a pack a kurzusrepóba szerepnéven érkezik, a `/course-fix` csak akkor alkalmazza, ha a felhasználó a saját üzenetében kéri (course-fix SKILL, „Külső findinglista”); utána build (`chore(media)`) és egy `--pin-visible`; a hangok neve sehol nem szerepelhet (2026-10-03-A).
- **Mit blokkol:** egyik verdiktet sem: a narráció B fázis, a videó C fázis, mindkettő fallbackkel jár (HUM:513, Q-MED-1), az M0/M1 pilotban a narráció opcionális (HUM:553, PILOT-4). A már gyártott M1.3-NAR-04 (D-1-ellentmondás) a pack előtt ne kerüljön tanulói felületre.
- **Ki hagyja jóvá:** médiafelelős / VO-gazda (X-17); a kurzusoldali alkalmazást a felhasználó kéri.

## 13. Technikai kivételek

### TECH-1 — A „minijelenet” gépi őr hatóköre (X-18)
- **Döntés:** Szűkül-e a `tools/content_integrity.py` globális „minijelenet” tiltása úgy, hogy a nem gyermekvédelmi, videós/peula „minijelenet” az AkH 139. szerint egybeírható legyen, vagy marad a „mini-jelenet” alak?
- **Érintett findingok:** `M4:NYELV-G1-8` c), `M5:NYELV-G1-1` e), `M5:NYELV-G2-11` (ILL-02); az objektív részek FIXED. **Források:** content_integrity.py:201–211 (ACTIVE_SPEC_RULES, :205 'minijelenet', globálisan, :451–467 `check_active_spec`), :267–276 (M3_ROLEPLAY_PHRASES, :270 M3-ra szűkített SAFEGUARDING); GK:23 (lezárt, repo-szintű: súlyos helyzet harmadik személyű esetelemzéssel, nem szerepjátékkal; vétó: Memuna, DPO); HUM:441; a 4119d16 előtti futás 2 SPEC-DRIFT ERROR-ja (ledger :1514). **Helyek ma:** M4.1:546, :549 (VID-02 title/spec), :631, :675, :719 (VID-03…05 notes), :735, :841; M5.2:510 (tanulói opciószöveg); M5.3:210 (ILL-02 title).
- **Opciók:** (A) status quo: a „mini-jelenet” marad, a három alpont lezárva „gépi őr miatt nem javítjuk”, tools változatlan. (B) a globális tiltás marad, a három nem gyermekvédelmi fájlra fájl-szintű kivétel. (C) a :205 törlése, csak az M3-őr (:270) marad. (D) szinonima („rövid jelenet”) a 9 helyen, tools nélkül — új nyelvi döntés, nem a validált javítás.
- **Ajánlás:** (B) — az AkH 139. az egybeírást kéri, a GK:23 lezárt döntése viszont az M3-on kívül is érvényes (M7 gyermekvédelmi részei, GK §2), ezért a (C) gyengítené a gépi védelmet; a (B) mindkettőt megtartja. Ha a projektgazda nem vállal tools-módosítást: (A).
- **Lépések (B):** 0) a projektgazda kifejezett felhatalmazása a `tools/` módosítására (eddig a futás felhatalmazásán kívül esett). 1) commit `tools(content_integrity)`: az ACTIVE_SPEC_RULES (:201–211) változatlan; új állandó :211 után, pl. `ACTIVE_SPEC_PATH_EXEMPTIONS = {('minijelenet', <M4.1 útvonal>), ('minijelenet', <M5.2 útvonal>), ('minijelenet', <M5.3 útvonal>)}` indoklással (X-18); a `check_active_spec` (:463–464) kihagyja a kivételes (fájl, kifejezés) párt; önteszt: a kivétel csak e három, M3-on kívüli fájlra érvényes. Ellenőrzés: `py_compile`, `python3 tools/content_integrity.py --selftest`, `python3 tools/content_integrity.py` (0 ERROR). 2) commit `fix(M4,M5)` `/course-fix`-szel: a fenti 9 hely „minijelenet…” alakra; `content_integrity` 0 ERROR; `python3 tools/test_media_manifest.py --pin-visible "M4:NYELV-G1-8, M5:NYELV-G1-1, M5:NYELV-G2-11: minijelenet (AkH 139.), X-18"`. 3) commit `chore(media)`: `python3 tools/media_manifest.py build`, `check`, `reconcile`, unittest (az `@asset` title/spec/notes mezők változnak). Sorrend kötött: az 1) nélkül a 2) SPEC-DRIFT ERROR-t ad, és a Stop-hook nem enged befejezni. A `tools/media_migrate_v2.py:116` (egyszeri migrációs eszköz, a buildben és a tesztekben nem fut) nem kell. (C)-nél az 1) lépés egyetlen sor: a :205 törlése.
- **Mit blokkol:** egyiket sem (P2 írásmód); csak későbbi fejlesztés.
- **Ki hagyja jóvá:** projektgazda (eszköz- és governance-változás); gyermekvédelmi vonatkozásban a GK:23 vétójoga (Memuna, DPO) érintetlen.

### TECH-2 — Az M6.1 és az M6.2 átnevezése a `tools/` útvonalkulcsaival (X-19)
- **Döntés:** Végrehajtható-e a validált, 2026-10-04 óta halasztott két átnevezés (`M6.1 – Játékkategóriák 3 aktuális kvucára.md`, `M6.2 – Történet mint tükör.md`) a hozzá kötött `tools/` útvonalkulcsok módosításával?
- **Érintett findingok:** `M6:NYELV-G1-11` (NYELV-109/302/203, course-fix napló 2026-10-04 :266–267), `M6:IMPL-G2-5` (M6.2:22–23 „Cím a kurzusban”), `M6:NYELV-G3-3` (b) (A:40, :59; B:8, :9; F:11, :12, :106, :195, :228, :229, :254 — riportsorok), `M6:QA-IMPL-5` (VPS:135). **Források:** M6-riport :157 (teljes helylista); `.claude/rules/course-content.md` (külön `git mv` commit, fájlnév és link együtt mozog); a hook: „git mv: nincs az engedélyezett git-alparancsok között — a felhasználó futtassa”; HUM:435 (fájlnév-stílus nem release-gate).
- **Opciók:** (A) átnevezés most, az alábbi négy committal. (B) halasztás; a címek és a fájlnevek addig maradnak (az M6.2 kurzusbeli címe vesszővel tér el a MAN:88 „Név”-től).
- **Ajánlás:** (A) — validált objektív javítás, a halasztás oka csak technikai volt, és a `tools/` két sora miatt a kulcsokat ugyanabban a change setben kell mozgatni.
- **Lépések (A):** 1) a felhasználó normál terminálban, a repó gyökeréből: `git mv "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md" "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játékkategóriák 3 aktuális kvucára.md"`, `git mv "02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md" "02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet mint tükör.md"`, majd `git commit` (csak az átnevezés, tartalmi szerkesztés nélkül). 2) commit `tools` (projektgazdai felhatalmazással): `tools/content_integrity.py:152` FILE_FORBIDDEN_PHRASES-kulcs az új M6.1 útvonalra (különben a `check_file_scoped_regressions` hiányzó útnál csendben kihagyja az M6.1-őrt); `tools/test_media_manifest.py:62` kulcs az új M6.1 útvonalra (a :63 baseline-érték marad); új baseline-sor: új M6.2 útvonal → `…/M6.2 – Történet, mint tükör.md` (a `a8629732` baseline-commitban ezen a néven létezik), új szótárban, a :102 `BASELINE_RENAMES` összefésülésébe felvéve; a precedens szerint (2026-10-02) a két régi útvonal a LEGACY_PATHS-ba (:44–80) — nem kötelező. 3) commit `fix(M6)` `/course-fix`-szel: HUB:252, :254 link-cél és címke, HUB:79, :91 cím; az M6.1/M6.2 cím- és szöveghelyei (M6.1:1, :6, :25 stb.; M6.2:1, :6, :23, :549, :556), a G3-helyek (`M6:NYELV-G3-3` (b)), MAN:87 (a MAN:88 már egyezik), VPS:135 útvonal és sorszám a végállapotra (ma deklaráció 497., törzs 498–517.); az M6.1 `@asset` specjei build úton; nem nyúl: M6.1:202 (`@source`, VO-1), `asset-migration-map.csv`, `_legacy/`. Utána `content_integrity` 0 ERROR és egy `--pin-visible "M6:NYELV-G1-11, M6:IMPL-G2-5, M6:NYELV-G3-3, M6:QA-IMPL-5: az M6.1/M6.2 átnevezése (NYELV-109/302/203), X-19"` (ez írja a `tools/approved-visible-text.json` :239, :243 kulcsait is; kézzel nem). 4) commit `chore(media)`: build ×2, `check`, `reconcile`, unittest. A PR merge commitja megőrzi az átnevezés-commitot (PR #12 precedens); a merge módját a felhasználó választja.
- **Mit blokkol:** egyiket sem (HUM:435); csak későbbi fejlesztés. A VO-1-gyel nincs kötött sorrend; ha a TECH-2 fut előbb, a pack az új útvonalra hivatkozik.
- **Ki hagyja jóvá:** a felhasználó (az átnevezési commit futtatása) + projektgazda (a `tools/` két sora és a baseline-sor).

### Lezárt korlátok és „már lezárt / átvezetendő” tételek

Nincs olyan tétel, amelyet egy lezárt döntés szövege teljesen megválaszolna. Részben lefedett, de nyitott maradékkal:
`M1:BIZT-G2-7` · a tartalmat a D-1 (HUM:524) adja, a hanggyártás nyitott (VO-1) · `M1:BIZT-G1-3` · N-M1-04 (HUM:587–588),
a bizonyíték-kapu kifejezetten nyitott (RT-2, X-12) · `M7:IMPL-G3-8` · a lánc a HUM-PRIV-04 (HUM:189–191), a Moodle-forma
nyitott (LMS-8) · `M7:IMPL-G2-7` · a completion-szerep a D-d (HUM:558), a H5P-út nyitott (LMS-6) · `M5:IMPL-G2-2` · az
elérési út az RM-D6 (HUM:516), a típus nyitott (LMS-3).

## A. függelék — Lefedettség: mind a 330 nyitott kulcs

Minden kulcs pontosan egy bejegyzéshez tartozik. A „Kapcsolódó” oszlop a részvázlatok kereszthivatkozásait tartalmazza (más kapu része, társjóváhagyó).

| Kulcs | Súly | Állapot | Bejegyzés | Kapcsolódó |
|---|:---:|---|---|---|
| `M0:BIZT-1` | P0 | EVIDENCE_GATE | GYV-24 | — |
| `M0:BIZT-3` | P1 | BLOCKED_HUMAN | GYV-3 | — |
| `M0:BIZT-5` | P2 | BLOCKED_HUMAN | GYV-7 | — |
| `M0:BIZT-7` | P0 | BLOCKED_HUMAN | ADV-6 | — |
| `M0:BIZT-9` | P1 | BLOCKED_HUMAN | GYV-5 | — |
| `M0:ERT-3` | P1 | BLOCKED_HUMAN | ERT-2 | lásd X-6 |
| `M0:ERT-4` | P1 | EVIDENCE_GATE | SIG-1 | — |
| `M0:ERT-8` | P2 | BLOCKED_HUMAN | PRG-17 | — |
| `M0:IMPL-2` | P1 | BLOCKED_HUMAN | PRG-8 | — |
| `M0:IMPL-3` | P1 | BLOCKED_HUMAN | ERT-1 | — |
| `M0:IMPL-5` | P1 | BLOCKED_HUMAN | PRG-6 | — |
| `M0:IMPL-9` | P1 | EVIDENCE_GATE | RT-1 | — |
| `M0:NYELV-G1-14` | P2 | BLOCKED_HUMAN | ERT-11 | — |
| `M0:NYELV-G2-1` | P2 | BLOCKED_HUMAN | PRG-1 | — |
| `M0:NYELV-G2-11` | P2 | BLOCKED_HUMAN | TERM-1 | — |
| `M0:NYELV-G2-22` | P2 | BLOCKED_HUMAN | PRG-11 | — |
| `M0:PED-5` | P2 | BLOCKED_HUMAN | PRG-1 | — |
| `M0:PED-8` | P1 | BLOCKED_HUMAN | GYV-23 | lásd X-5 (adatkör: DPO-rész) |
| `M1:BIZT-G1-3` | P0 | EVIDENCE_GATE | RT-2 | DPO-rész: X-12 |
| `M1:BIZT-G1-4` | P2 | BLOCKED_HUMAN | GYV-13 | — |
| `M1:BIZT-G1-7` | P2 | BLOCKED_HUMAN | GYV-22 | — |
| `M1:BIZT-G2-1` | P0 | BLOCKED_HUMAN | ERT-12 | lásd X-6 (DPO-vétó) |
| `M1:BIZT-G2-10` | P2 | BLOCKED_HUMAN | GYV-12 | — |
| `M1:BIZT-G2-2` | P0 | EVIDENCE_GATE | ADV-E1 | a ledger-sor első szerepe a DPO, G2 |
| `M1:BIZT-G2-3` | P1 | BLOCKED_HUMAN | GYV-12 | lásd X-5 (az ERT-12-vel egy lépésben) |
| `M1:BIZT-G2-4` | P1 | BLOCKED_HUMAN | ADV-1 | — |
| `M1:BIZT-G2-6` | P2 | BLOCKED_HUMAN | GYV-11 | lásd X-5 (DPO-rész) |
| `M1:BIZT-G2-7` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M1:BIZT-G3-2` | P2 | BLOCKED_HUMAN | GYV-6 | — |
| `M1:BIZT-G3-5` | P2 | BLOCKED_HUMAN | GYV-21 | lásd X-5 (DPO-rész) |
| `M1:BIZT-G3-8` | P2 | BLOCKED_HUMAN | ADV-7 | — |
| `M1:BIZT-G3-9` | P2 | BLOCKED_HUMAN | GYV-13 | — |
| `M1:ERT-G1-2` | P1 | EVIDENCE_GATE | RT-2 | — |
| `M1:ERT-G1-3` | P1 | BLOCKED_HUMAN | PRG-2 | lásd X-10 (DPO, ha tárolt) |
| `M1:ERT-G2-1` | P1 | BLOCKED_HUMAN | ERT-14 | — |
| `M1:ERT-G2-2` | P1 | BLOCKED_HUMAN | ERT-15 | — |
| `M1:ERT-G2-4` | P2 | BLOCKED_HUMAN | ERT-4 | lásd X-6 (DPO, ha activity) |
| `M1:ERT-G2-5` | P2 | BLOCKED_HUMAN | ERT-16 | — |
| `M1:IMPL-G1-5` | P2 | BLOCKED_HUMAN | ADV-4 | — |
| `M1:IMPL-G1-8` | P2 | BLOCKED_HUMAN | PRG-9 | — |
| `M1:IMPL-G2-10` | P2 | BLOCKED_HUMAN | LMS-1 | lásd X-11 |
| `M1:IMPL-G2-2` | P1 | BLOCKED_HUMAN | ERT-9 | — |
| `M1:IMPL-G2-4` | P1 | EVIDENCE_GATE | RT-2 | — |
| `M1:IMPL-G3-8` | P2 | BLOCKED_HUMAN | PRG-8 | — |
| `M1:NYELV-G1-14` | P2 | BLOCKED_HUMAN | TERM-2 | — |
| `M1:NYELV-G1-6` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M1:NYELV-G2-4` | P2 | BLOCKED_HUMAN | ERT-16 | — |
| `M1:NYELV-G2-5` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M1:NYELV-G2-8` | P2 | BLOCKED_HUMAN | ERT-17 | — |
| `M1:NYELV-G2-9` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M1:NYELV-G3-16` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M1:PED-G1-8` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M1:PED-G2-1` | P1 | BLOCKED_HUMAN | ERT-13 | — |
| `M1:PED-G3-8` | P2 | BLOCKED_HUMAN | PRG-5 | — |
| `M1:PED-G3-9` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M2:BIZT-G1-1` | P1 | BLOCKED_HUMAN | GYV-1 | — |
| `M2:BIZT-G1-2` | P1 | BLOCKED_HUMAN | GYV-4 | — |
| `M2:BIZT-G1-3` | P1 | BLOCKED_HUMAN | ADV-5 | — |
| `M2:BIZT-G1-6` | P1 | BLOCKED_HUMAN | ADV-1 | — |
| `M2:BIZT-G1-7` | P2 | BLOCKED_HUMAN | ADV-10 | — |
| `M2:BIZT-G1-8` | P2 | BLOCKED_HUMAN | ADV-13 | — |
| `M2:BIZT-G1-9` | P1 | EVIDENCE_GATE | ADV-E1 | lásd X-12 (runtime-rész: RT-P0-21) |
| `M2:BIZT-G2-1` | P0 | BLOCKED_HUMAN | GYV-1 | — |
| `M2:BIZT-G2-2` | P0 | BLOCKED_HUMAN | GYV-2 | — |
| `M2:BIZT-G2-3` | P1 | BLOCKED_HUMAN | ADV-1 | — |
| `M2:BIZT-G2-4` | P1 | BLOCKED_HUMAN | GYV-3 | — |
| `M2:BIZT-G2-5` | P1 | BLOCKED_HUMAN | GYV-4 | — |
| `M2:BIZT-G2-6` | P1 | BLOCKED_HUMAN | ADV-5 | — |
| `M2:BIZT-G2-8` | P1 | EVIDENCE_GATE | GYV-24 | lásd X-7 (runtime-rész: RT-P0-17, RT-1) |
| `M2:BIZT-G2-9` | P1 | EVIDENCE_GATE | ADV-E1 | lásd X-12 (runtime-rész: RT-P0-15) |
| `M2:BIZT-G3-10` | P2 | BLOCKED_HUMAN | ADV-11 | — |
| `M2:BIZT-G3-2` | P1 | BLOCKED_HUMAN | GYV-5 | — |
| `M2:BIZT-G3-3` | P2 | BLOCKED_HUMAN | GYV-20 | lásd X-5 (DPO-rész) |
| `M2:BIZT-G3-5` | P2 | BLOCKED_HUMAN | GYV-21 | lásd X-5 (DPO-rész) |
| `M2:BIZT-G3-7` | P2 | EVIDENCE_GATE | ADV-E2 | — |
| `M2:BIZT-G3-9` | P2 | BLOCKED_HUMAN | GYV-19 | — |
| `M2:ERT-G1-5` | P1 | BLOCKED_HUMAN | TERM-7 | — |
| `M2:ERT-G1-7` | P1 | EVIDENCE_GATE | GYV-24 | — |
| `M2:ERT-G3-4` | P2 | BLOCKED_HUMAN | PRG-15 | — |
| `M2:IMPL-G1-3` | P2 | BLOCKED_HUMAN | PRG-9 | — |
| `M2:IMPL-G2-1` | P1 | BLOCKED_HUMAN | ERT-18 | lásd X-6 (tárolás: DPO-rész) |
| `M2:IMPL-G2-7` | P2 | BLOCKED_HUMAN | GYV-12 | — |
| `M2:IMPL-G3-6` | P2 | BLOCKED_HUMAN | PRG-11 | — |
| `M2:IMPL-G3-7` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M2:NYELV-G1-12` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M2:NYELV-G1-13` | P2 | BLOCKED_HUMAN | ERT-20 | — |
| `M2:NYELV-G2-3` | P2 | BLOCKED_HUMAN | TERM-3 | — |
| `M2:PED-G1-11` | P2 | BLOCKED_HUMAN | ERT-19 | — |
| `M2:PED-G1-5` | P1 | BLOCKED_HUMAN | ADV-5 | — |
| `M2:PED-G1-9` | P2 | BLOCKED_HUMAN | ERT-4 | — |
| `M2:PED-G2-2` | P1 | BLOCKED_HUMAN | TERM-8 | — |
| `M2:PED-G2-7` | P2 | BLOCKED_HUMAN | GYV-12 | — |
| `M2:PED-G3-1` | P1 | BLOCKED_HUMAN | PRG-1 | — |
| `M2:PED-G3-11` | P2 | BLOCKED_HUMAN | PRG-5 | — |
| `M2:QA-BIZT-1` | P2 | BLOCKED_HUMAN | GYV-13 | — |
| `M2:QA-PED-1` | P2 | BLOCKED_HUMAN | ERT-8 | — |
| `M3:BIZT-G1-1` | P1 | BLOCKED_HUMAN | GYV-3 | — |
| `M3:BIZT-G1-10` | P2 | BLOCKED_HUMAN | GYV-13 | — |
| `M3:BIZT-G1-2` | P1 | EVIDENCE_GATE | GYV-24 | elsődleges: X-7, Memuna |
| `M3:BIZT-G1-5` | P1 | BLOCKED_HUMAN | ADV-4 | lásd X-4 (runtime-rész: RT-P0-11) |
| `M3:BIZT-G1-7` | P2 | BLOCKED_HUMAN | ERT-10 | — |
| `M3:BIZT-G1-8` | P1 | BLOCKED_HUMAN | JOG-1 | — |
| `M3:BIZT-G2-10` | P1 | EVIDENCE_GATE | GYV-24 | elsődleges: X-7, Memuna |
| `M3:BIZT-G2-2` | P1 | BLOCKED_HUMAN | GYV-14 | — |
| `M3:BIZT-G2-3` | P1 | BLOCKED_HUMAN | GYV-3 | — |
| `M3:BIZT-G2-4` | P1 | BLOCKED_HUMAN | GYV-4 | — |
| `M3:BIZT-G2-5` | P1 | BLOCKED_HUMAN | ADV-2 | — |
| `M3:BIZT-G2-7` | P1 | BLOCKED_HUMAN | ADV-4 | — |
| `M3:BIZT-G2-8` | P2 | BLOCKED_HUMAN | GYV-3 | — |
| `M3:BIZT-G2-9` | P2 | BLOCKED_HUMAN | GYV-15 | lásd X-5 (jogi alkérdés: JOG-1) |
| `M3:BIZT-G3-4` | P2 | BLOCKED_HUMAN | GYV-3 | — |
| `M3:BIZT-G3-7` | P2 | BLOCKED_HUMAN | GYV-16 | — |
| `M3:BIZT-G3-8` | P2 | BLOCKED_HUMAN | ADV-2 | — |
| `M3:ERT-G1-11` | P2 | BLOCKED_HUMAN | ERT-5 | — |
| `M3:ERT-G1-5` | P2 | BLOCKED_HUMAN | ERT-22 | — |
| `M3:ERT-G2-2` | P1 | BLOCKED_HUMAN | ERT-21 | — |
| `M3:ERT-G2-5` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M3:ERT-G2-7` | P2 | BLOCKED_HUMAN | ERT-7 | — |
| `M3:ERT-G3-10` | P2 | BLOCKED_HUMAN | PRG-5 | — |
| `M3:ERT-G3-2` | P2 | BLOCKED_HUMAN | PRG-12 | — |
| `M3:ERT-G3-8` | P2 | BLOCKED_HUMAN | ERT-21 | — |
| `M3:IMPL-G2-11` | P1 | BLOCKED_HUMAN | PRG-4 | társ-kapu: X-7, Memuna-QA |
| `M3:IMPL-G2-14` | P2 | BLOCKED_HUMAN | ERT-23 | — |
| `M3:IMPL-G2-15` | P2 | BLOCKED_HUMAN | TERM-4 | — |
| `M3:IMPL-G2-2` | P1 | BLOCKED_HUMAN | LMS-2 | — |
| `M3:IMPL-G2-4` | P1 | BLOCKED_HUMAN | PRG-9 | lásd X-10 (az X-11 csak az alt-rész) |
| `M3:IMPL-G2-5` | P1 | BLOCKED_HUMAN | GYV-2 | — |
| `M3:IMPL-G2-6` | P1 | BLOCKED_HUMAN | ADV-3 | — |
| `M3:IMPL-G3-4` | P1 | EVIDENCE_GATE | GYV-24 | — |
| `M3:IMPL-G3-9` | P2 | BLOCKED_HUMAN | PRG-11 | — |
| `M3:NYELV-G1-11` | P2 | BLOCKED_HUMAN | ERT-1 | — |
| `M3:NYELV-G1-12` | P2 | BLOCKED_HUMAN | PRG-2 | függő |
| `M3:NYELV-G1-13` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M3:NYELV-G1-2` | P2 | BLOCKED_HUMAN | TERM-4 | — |
| `M3:NYELV-G1-3` | P2 | BLOCKED_HUMAN | JOG-1 | — |
| `M3:NYELV-G2-15` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M3:NYELV-G2-3` | P2 | BLOCKED_HUMAN | TERM-5 | — |
| `M3:NYELV-G3-2` | P2 | BLOCKED_HUMAN | PRG-3 | függő |
| `M3:NYELV-G3-6` | P3 | BLOCKED_HUMAN | PRG-16 | — |
| `M3:PED-G1-4` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M3:PED-G2-1` | P1 | BLOCKED_HUMAN | GYV-2 | lásd X-5 (kapusor-tag) |
| `M3:PED-G3-1` | P1 | BLOCKED_HUMAN | PRG-1 | — |
| `M3:PED-G3-13` | P2 | BLOCKED_HUMAN | TERM-6 | — |
| `M3:PED-G3-2` | P1 | BLOCKED_HUMAN | PRG-12 | — |
| `M3:PED-G3-4` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M3:PED-G3-9` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M3:QA-BIZT-1` | P2 | BLOCKED_HUMAN | ERT-10 | — |
| `M4:BIZT-G1-2` | P1 | BLOCKED_HUMAN | ADV-3 | lásd X-4 (kapusor-tag) |
| `M4:BIZT-G1-5` | P2 | BLOCKED_HUMAN | ADV-9 | — |
| `M4:BIZT-G1-6` | P2 | BLOCKED_HUMAN | GYV-19 | — |
| `M4:BIZT-G1-7` | P2 | BLOCKED_HUMAN | PRG-14 | — |
| `M4:BIZT-G2-1` | P1 | BLOCKED_HUMAN | GYV-3 | — |
| `M4:BIZT-G2-10` | P2 | BLOCKED_HUMAN | GYV-2 | — |
| `M4:BIZT-G2-4` | P2 | BLOCKED_HUMAN | ADV-7 | — |
| `M4:BIZT-G2-5` | P2 | BLOCKED_HUMAN | ADV-7 | — |
| `M4:BIZT-G2-7` | P2 | EVIDENCE_GATE | ADV-E2 | — |
| `M4:BIZT-G2-9` | P2 | BLOCKED_HUMAN | GYV-6 | — |
| `M4:ERT-G1-1` | P1 | BLOCKED_HUMAN | ERT-25 | — |
| `M4:ERT-G1-10` | P2 | BLOCKED_HUMAN | ADV-3 | lásd X-4 (kapusor-tag) |
| `M4:ERT-G1-5` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M4:ERT-G1-6` | P2 | BLOCKED_HUMAN | PRG-4 | QA: X-16 |
| `M4:ERT-G1-9` | P2 | BLOCKED_HUMAN | PRG-4 | QA: X-16 |
| `M4:ERT-G2-4` | P2 | BLOCKED_HUMAN | ERT-8 | lásd X-6 (adatkör: DPO) |
| `M4:IMPL-G1-2` | P1 | BLOCKED_HUMAN | ADV-3 | — |
| `M4:IMPL-G2-12` | P2 | EVIDENCE_GATE | RT-3 | DPO-rész: X-12 |
| `M4:NYELV-G1-12` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M4:NYELV-G1-8` | P2 | BLOCKED_HUMAN | TECH-1 | — |
| `M4:NYELV-G2-10` | P2 | BLOCKED_HUMAN | PRG-1 | függő |
| `M4:NYELV-G2-12` | P2 | BLOCKED_HUMAN | PRG-1 | függő |
| `M4:NYELV-G2-2` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M4:NYELV-G2-5` | P2 | BLOCKED_HUMAN | PRG-1 | függő |
| `M4:NYELV-G2-6` | P2 | BLOCKED_HUMAN | PRG-1 | — |
| `M4:PED-G1-2` | P1 | BLOCKED_HUMAN | ERT-24 | — |
| `M4:PED-G1-7` | P1 | EVIDENCE_GATE | GYV-24 | elsődleges: X-7, Memuna |
| `M4:PED-G2-1` | P1 | BLOCKED_HUMAN | PRG-2 | — |
| `M4:PED-G2-2` | P1 | BLOCKED_HUMAN | PRG-1 | — |
| `M4:PED-G2-4` | P2 | BLOCKED_HUMAN | PRG-10 | QA: X-16 |
| `M4:PED-G2-9` | P2 | BLOCKED_HUMAN | PRG-3 | lásd X-10 ((a) út: ADV-7 után) |
| `M5:BIZT-G1-1` | P1 | BLOCKED_HUMAN | GYV-7 | — |
| `M5:BIZT-G1-4` | P2 | EVIDENCE_GATE | ADV-E2 | — |
| `M5:BIZT-G1-5` | P2 | BLOCKED_HUMAN | ADV-9 | — |
| `M5:BIZT-G1-6` | P2 | EVIDENCE_GATE | SIG-5 | — |
| `M5:BIZT-G2-1` | P2 | BLOCKED_HUMAN | ADV-7 | — |
| `M5:BIZT-G2-4` | P2 | BLOCKED_HUMAN | ADV-4 | — |
| `M5:BIZT-G2-5` | P2 | BLOCKED_HUMAN | ADV-8 | — |
| `M5:ERT-G1-1` | P1 | BLOCKED_HUMAN | ERT-3 | CP-rész: ERT-1 |
| `M5:ERT-G1-11` | P2 | EVIDENCE_GATE | SIG-4 | — |
| `M5:ERT-G1-4` | P2 | BLOCKED_HUMAN | ERT-6 | — |
| `M5:ERT-G1-9` | P2 | BLOCKED_HUMAN | ERT-28 | — |
| `M5:ERT-G2-1` | P2 | BLOCKED_HUMAN | ERT-29 | — |
| `M5:ERT-G2-3` | P2 | BLOCKED_HUMAN | ERT-29 | — |
| `M5:ERT-G2-8` | P2 | BLOCKED_HUMAN | ERT-7 | — |
| `M5:ERT-G2-9` | P2 | BLOCKED_HUMAN | PRG-10 | — |
| `M5:IMPL-G1-12` | P2 | BLOCKED_HUMAN | ERT-1 | — |
| `M5:IMPL-G2-2` | P1 | BLOCKED_HUMAN | LMS-3 | — |
| `M5:NYELV-G1-1` | P2 | BLOCKED_HUMAN | TECH-1 | — |
| `M5:NYELV-G1-11` | P2 | BLOCKED_HUMAN | ERT-30 | — |
| `M5:NYELV-G1-12` | P2 | BLOCKED_HUMAN | ERT-27 | — |
| `M5:NYELV-G1-14` | P2 | BLOCKED_HUMAN | ERT-27 | — |
| `M5:NYELV-G1-2` | P2 | BLOCKED_HUMAN | ERT-26 | — |
| `M5:NYELV-G1-9` | P2 | BLOCKED_HUMAN | ERT-26 | — |
| `M5:NYELV-G2-11` | P2 | BLOCKED_HUMAN | TECH-1 | — |
| `M5:NYELV-G2-12` | P2 | BLOCKED_HUMAN | ADV-9 | lásd X-4 (függő) |
| `M5:NYELV-G2-14` | P2 | BLOCKED_HUMAN | PRG-10 | — |
| `M5:PED-G1-1` | P1 | BLOCKED_HUMAN | ERT-26 | — |
| `M5:PED-G1-10` | P2 | BLOCKED_HUMAN | TERM-7 | — |
| `M5:PED-G1-2` | P2 | BLOCKED_HUMAN | ERT-27 | — |
| `M5:PED-G1-3` | P2 | BLOCKED_HUMAN | PRG-15 | — |
| `M5:PED-G1-4` | P2 | BLOCKED_HUMAN | PRG-4 | — |
| `M5:PED-G1-6` | P2 | BLOCKED_HUMAN | PRG-7 | — |
| `M5:PED-G2-11` | P2 | BLOCKED_HUMAN | LMS-3 | — |
| `M5:PED-G2-14` | P2 | BLOCKED_HUMAN | PRG-13 | — |
| `M5:PED-G2-6` | P2 | BLOCKED_HUMAN | PRG-1 | — |
| `M5:QA-PED-2` | P2 | BLOCKED_HUMAN | PRG-1 | — |
| `M6:BIZT-G1-1` | P1 | BLOCKED_HUMAN | GYV-8 | — |
| `M6:BIZT-G1-4` | P2 | BLOCKED_HUMAN | ADV-4 | lásd X-4 (kapusor-tag) |
| `M6:BIZT-G1-6` | P1 | EVIDENCE_GATE | SIG-6 | — |
| `M6:BIZT-G1-7` | P2 | EVIDENCE_GATE | ADV-E2 | — |
| `M6:BIZT-G2-1` | P2 | BLOCKED_HUMAN | GYV-16 | — |
| `M6:BIZT-G2-2` | P1 | BLOCKED_HUMAN | GYV-16 | — |
| `M6:BIZT-G2-3` | P1 | EVIDENCE_GATE | GYV-24 | — |
| `M6:BIZT-G2-4` | P2 | BLOCKED_HUMAN | GYV-7 | — |
| `M6:BIZT-G2-5` | P2 | BLOCKED_HUMAN | ADV-10 | — |
| `M6:BIZT-G2-6` | P2 | BLOCKED_HUMAN | GYV-18 | — |
| `M6:BIZT-G3-2` | P1 | BLOCKED_HUMAN | GYV-17 | — |
| `M6:BIZT-G3-5` | P2 | BLOCKED_HUMAN | ADV-8 | — |
| `M6:ERT-G1-1` | P1 | BLOCKED_HUMAN | ERT-31 | — |
| `M6:ERT-G1-10` | P2 | BLOCKED_HUMAN | ERT-7 | — |
| `M6:ERT-G1-2` | P1 | BLOCKED_HUMAN | ERT-32 | — |
| `M6:ERT-G1-6` | P2 | BLOCKED_HUMAN | ERT-34 | — |
| `M6:ERT-G1-7` | P2 | BLOCKED_HUMAN | ERT-6 | — |
| `M6:ERT-G2-3` | P1 | BLOCKED_HUMAN | PRG-2 | — |
| `M6:ERT-G2-5` | P2 | BLOCKED_HUMAN | ERT-35 | — |
| `M6:ERT-G2-7` | P2 | BLOCKED_HUMAN | ERT-7 | — |
| `M6:ERT-G2-8` | P2 | BLOCKED_HUMAN | ERT-36 | — |
| `M6:ERT-G3-1` | P1 | BLOCKED_HUMAN | ERT-33 | — |
| `M6:ERT-G3-4` | P2 | BLOCKED_HUMAN | ERT-32 | — |
| `M6:IMPL-G1-3` | P2 | BLOCKED_HUMAN | ERT-6 | — |
| `M6:IMPL-G1-5` | P1 | BLOCKED_HUMAN | PRG-4 | — |
| `M6:IMPL-G1-7` | P2 | BLOCKED_HUMAN | LMS-4 | — |
| `M6:IMPL-G2-2` | P1 | EVIDENCE_GATE | RT-4 | DPO-rész: X-12 |
| `M6:IMPL-G2-5` | P2 | BLOCKED_HUMAN | TECH-2 | — |
| `M6:IMPL-G2-7` | P2 | BLOCKED_HUMAN | PRG-4 | — |
| `M6:NYELV-G1-1` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M6:NYELV-G1-10` | P2 | BLOCKED_HUMAN | ERT-6 | lásd X-6 (függő) |
| `M6:NYELV-G1-11` | P2 | BLOCKED_HUMAN | TECH-2 | az M6.1:202 VO-része: VO-1 |
| `M6:NYELV-G1-7` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M6:NYELV-G2-1` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M6:NYELV-G3-3` | P2 | BLOCKED_HUMAN | TECH-2 | — |
| `M6:PED-G1-2` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M6:PED-G1-8` | P2 | BLOCKED_HUMAN | GYV-18 | lásd X-5 (kapusor-tag) |
| `M6:PED-G1-9` | P2 | BLOCKED_HUMAN | PRG-7 | lásd X-10 (kapusor-tag) |
| `M6:PED-G3-1` | P1 | BLOCKED_HUMAN | PRG-1 | — |
| `M6:PED-G3-8` | P2 | BLOCKED_HUMAN | ERT-37 | — |
| `M6:PED-G3-9` | P2 | BLOCKED_HUMAN | PRG-13 | — |
| `M6:QA-BIZT-1` | P2 | BLOCKED_HUMAN | ADV-11 | — |
| `M6:QA-BIZT-2` | P2 | BLOCKED_HUMAN | ADV-9 | — |
| `M6:QA-IMPL-5` | P2 | BLOCKED_HUMAN | TECH-2 | — |
| `M7:BIZT-G1-1` | P1 | BLOCKED_HUMAN | ERT-42 | lásd X-6 (DPO-rész) |
| `M7:BIZT-G1-2` | P1 | BLOCKED_HUMAN | GYV-9 | — |
| `M7:BIZT-G1-3` | P1 | EVIDENCE_GATE | ADV-E3 | — |
| `M7:BIZT-G1-4` | P1 | BLOCKED_HUMAN | GYV-10 | lásd X-5 (DPO-rész) |
| `M7:BIZT-G1-5` | P1 | EVIDENCE_GATE | GYV-24 | — |
| `M7:BIZT-G1-6` | P2 | BLOCKED_HUMAN | ADV-5 | — |
| `M7:BIZT-G1-7` | P2 | BLOCKED_HUMAN | ADV-10 | — |
| `M7:BIZT-G2-3` | P1 | BLOCKED_HUMAN | ADV-12 | — |
| `M7:BIZT-G3-1` | P2 | BLOCKED_HUMAN | GYV-7 | — |
| `M7:BIZT-G3-3` | P2 | BLOCKED_HUMAN | GYV-13 | — |
| `M7:BIZT-G3-6` | P2 | BLOCKED_HUMAN | ADV-3 | — |
| `M7:ERT-G1-11` | P2 | BLOCKED_HUMAN | ERT-41 | — |
| `M7:ERT-G1-12` | P2 | BLOCKED_HUMAN | ERT-45 | — |
| `M7:ERT-G1-2` | P1 | BLOCKED_HUMAN | PRG-6 | — |
| `M7:ERT-G1-5` | P1 | EVIDENCE_GATE | SIG-2 | — |
| `M7:ERT-G2-10` | P2 | BLOCKED_HUMAN | ERT-49 | — |
| `M7:ERT-G2-7` | P2 | BLOCKED_HUMAN | PRG-4 | lásd X-10 (kapusor-tag) |
| `M7:ERT-G3-10` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M7:ERT-G3-6` | P2 | BLOCKED_HUMAN | PRG-15 | — |
| `M7:IMPL-G1-11` | P2 | EVIDENCE_GATE | RT-5 | — |
| `M7:IMPL-G1-3` | P1 | BLOCKED_HUMAN | ERT-40 | lásd X-6 (értékelési felelős) |
| `M7:IMPL-G1-7` | P2 | BLOCKED_HUMAN | ERT-46 | — |
| `M7:IMPL-G1-9` | P2 | BLOCKED_HUMAN | ERT-5 | — |
| `M7:IMPL-G2-1` | P1 | BLOCKED_HUMAN | LMS-5 | lásd X-11 (szabad szöveg: DPO-rész) |
| `M7:IMPL-G2-10` | P1 | EVIDENCE_GATE | RT-6 | — |
| `M7:IMPL-G2-12` | P2 | BLOCKED_HUMAN | LMS-7 | — |
| `M7:IMPL-G2-2` | P1 | BLOCKED_HUMAN | ERT-48 | lásd X-6 (az X-11 csak a beágyazási rész) |
| `M7:IMPL-G2-3` | P1 | BLOCKED_HUMAN | ADV-3 | — |
| `M7:IMPL-G2-5` | P1 | BLOCKED_HUMAN | PRG-4 | társ-kapu: X-7, Memuna-QA |
| `M7:IMPL-G2-7` | P2 | BLOCKED_HUMAN | LMS-6 | — |
| `M7:IMPL-G3-2` | P1 | BLOCKED_HUMAN | PRG-6 | — |
| `M7:IMPL-G3-7` | P2 | BLOCKED_HUMAN | ADV-2 | — |
| `M7:IMPL-G3-8` | P2 | BLOCKED_HUMAN | LMS-8 | — |
| `M7:NYELV-G1-14` | P2 | BLOCKED_HUMAN | PRG-14 | — |
| `M7:NYELV-G1-16` | P2 | BLOCKED_HUMAN | ERT-47 | — |
| `M7:NYELV-G1-4` | P2 | BLOCKED_HUMAN | ERT-41 | — |
| `M7:NYELV-G1-5` | P2 | BLOCKED_HUMAN | LMS-5 | — |
| `M7:NYELV-G2-11` | P2 | BLOCKED_HUMAN | ERT-41 | elsődleges: X-6, a b) rész |
| `M7:NYELV-G2-13` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M7:NYELV-G2-15` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M7:NYELV-G2-5` | P2 | BLOCKED_HUMAN | ERT-41 | — |
| `M7:NYELV-G2-8` | P2 | BLOCKED_HUMAN | ERT-50 | — |
| `M7:NYELV-G2-9` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `M7:NYELV-G3-10` | P2 | BLOCKED_HUMAN | PRG-3 | függő |
| `M7:NYELV-G3-12` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `M7:NYELV-G3-14` | P2 | BLOCKED_HUMAN | PRG-1 | függő |
| `M7:NYELV-G3-17` | P2 | BLOCKED_HUMAN | PRG-3 | függő |
| `M7:PED-G1-1` | P1 | BLOCKED_HUMAN | ERT-43 | — |
| `M7:PED-G1-10` | P2 | BLOCKED_HUMAN | ERT-44 | — |
| `M7:PED-G1-8` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `M7:PED-G2-2` | P2 | BLOCKED_HUMAN | PRG-3 | — |
| `M7:PED-G2-4` | P2 | BLOCKED_HUMAN | GYV-9 | — |
| `M7:PED-G3-1` | P1 | BLOCKED_HUMAN | PRG-1 | — |
| `M7:PED-G3-11` | P2 | BLOCKED_HUMAN | PRG-4 | — |
| `M7:PED-G3-2` | P1 | BLOCKED_HUMAN | PRG-3 | — |
| `Z:BIZT-G1-1` | P1 | BLOCKED_HUMAN | GYV-8 | — |
| `Z:BIZT-G1-10` | P1 | EVIDENCE_GATE | GYV-24 | lásd X-7 (DPO G2-rész: ADV-E1) |
| `Z:BIZT-G1-2` | P1 | BLOCKED_HUMAN | GYV-11 | lásd X-5 (DPO-rész) |
| `Z:BIZT-G1-5` | P2 | BLOCKED_HUMAN | ADV-14 | — |
| `Z:BIZT-G1-7` | P2 | BLOCKED_HUMAN | ADV-15 | — |
| `Z:BIZT-G1-8` | P2 | BLOCKED_HUMAN | ADV-4 | lásd X-4 ((a) alpontja = ERT-2) |
| `Z:BIZT-G1-9` | P2 | BLOCKED_HUMAN | ADV-7 | — |
| `Z:ERT-G1-1` | P1 | BLOCKED_HUMAN | ERT-38 | — |
| `Z:ERT-G1-3` | P1 | BLOCKED_HUMAN | ERT-39 | — |
| `Z:ERT-G1-4` | P1 | BLOCKED_HUMAN | ERT-3 | — |
| `Z:ERT-G1-7` | P2 | BLOCKED_HUMAN | PRG-6 | — |
| `Z:IMPL-G1-3` | P1 | BLOCKED_HUMAN | ADV-3 | — |
| `Z:NYELV-G1-14` | P2 | BLOCKED_HUMAN | GYV-6 | — |
| `Z:NYELV-G1-15` | P2 | BLOCKED_HUMAN | PRG-16 | — |
| `Z:NYELV-G1-6` | P2 | BLOCKED_HUMAN | VO-1 | — |
| `Z:PED-G1-4` | P2 | BLOCKED_HUMAN | PRG-2 | — |
| `Z:QA-NYELV-1` | P2 | BLOCKED_HUMAN | PRG-6 | — |

## B. függelék — Összefésülési döntések (fő session)

- `M1:BIZT-G2-2`: két részvázlat is csak hivatkozott rá (X-8 ↔ X-12). A ledger-sor első szerepe a DPO (G2) → ADV-E1; a runtime-rész (RT-P0-15) az RT-2-ben.
- `M3:BIZT-G1-2`, `M3:BIZT-G2-10`, `M4:PED-G1-7`: két vázlat is sajátjának számolta. Az első megnevezett kapu az X-7 (Memuna) → GYV-24; az értékelési/lektori rész a SIG-2, SIG-3, SIG-4 bejegyzésben marad (a SIG-3-nak így nincs saját elsődleges kulcsa, de szükséges aláírás).
- `M7:NYELV-G2-11`: az első megnevezett kapu az X-6 → ERT-41; a c) hanggyártási rész a VO-1-ben.
- A részvázlatok saját „Lefedettség” táblái és összesítő sorai helyett az A. függelék érvényes.
