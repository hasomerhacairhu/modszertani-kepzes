# Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02

Ez a dokumentum a projektgazdának és a szerepköri jóváhagyóknak szól. Összevont, kutatott javaslatot ad azokra a kérdésekre, amelyeket a futás nem zárhatott le magától: a célzott QA 40 új döntés-tételére, a HUM 14 részleges átvezetéseinek maradékára és az M7 kapukvíz válaszszivárgására (ERT-5). **Státusza: javaslat, nem döntés.** A 2026-10-12-én elfogadott 125 döntés (`02 Tervezet/Emberi jóváhagyás szükséges.md` 14. szakasz) nem nyílik újra; minden csomag egy már elfogadott döntés alkalmazásáról, feltételéről vagy szerepköri bemenetéről kérdez. A javaslatok elfogadása sem release-jóváhagyás: a `MOODLE-BUILD-VERDICT` és a `LEARNER-RELEASE-VERDICT` csak a `content_integrity.py --release-report` sorából, illetve a G1–G8 kapuk bizonyítékából és a go/no-go döntésből következik. Bázis: a `next-version/AP-2026-10-11-01` ág, futás `AP-2026-10-12-02`. A kutatás a `10b5d76` állapoton készült; a futásban implementált javítások: `3b160fc`, `958bced`, `16a9ad9`, `11a89b4`, `93da996` (média: `4b188cc`, `0b695a0`, `87c08c1`).

**Olvasási útmutató.**
- Azonosítók: **D-xx** = emberi döntési csomag; **BK-xx** = bizonyíték-kapu (szerepköri vagy runtime-bizonyíték, nem döntés); **KF-xx** = külső függőség (VO fix pack, SIGNOFF).
- Rövidítések: HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`; GK = `02 Tervezet/Gyermekvédelem – release gate.md`; ADV = `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`; MAN = `02 Tervezet/LMS – activity manifest.md`; RA = `02 Tervezet/LMS – H5P runtime acceptance.md`; RR = `02 Tervezet/RELEASE-READINESS.md`; PT = `02 Tervezet/Program terv.md`; A11Y = `02 Tervezet/LMS – hozzáférhetőségi sztenderd.md`; KAPU = a modul kapufájlja (`<modul> – Kapu – értékelő (item-bank + rubrika).md`); CSOMAG = `01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`.
- A sorszámok a kutatás idején (`10b5d76`) érvényesek; a későbbi commitok kissé eltolhatták őket.
- A „Vétó/QA (HUM 14)” sor a HUM 14. szakasz „Utólagos ellenőrzés (vétó/QA)” oszlopát idézi, ahogy a kutatói bemenetek tartalmazták.
- A forrásokat csak ott nevezzük meg, ahol a kutatók ténylegesen idézték őket; ahol egy kutató jelezte, hogy egy forrást nem ért el vagy nem ellenőrzött, azt kiírjuk.
- A ledger-kulcsok `<modul>:<ID>` alakúak (`01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md`). A Külső kapuk kulcsát mindig „ledger: X-n” alakban írjuk. A „régi X-n” a HUM 14 sorainak hivatkozása az AP-2026-10-11-01 futás külső kapuira (például ADV-3: „lásd X-10”, „lásd X-6”; ERT-40: „plugin: LMS-gazda (X-11)”); ezek nem azonosak a mostani ledger azonos számú kulcsaival.

---

## 1. Összefoglaló táblázat

| ID | Téma | Dönt · vétó/QA | Típus | Feloldott kulcsok | Javaslat egy sorban |
|---|---|---|---|---|---|
| D-01 | Peula-megállítási protokoll, helyettes, alacsony kockázat, létszámnorma (GYV-5) | Memuna + programvezető · ugyanők (HUM-SAFE-03; GK §5) | EMBERI DÖNTÉS | M0:QA14-BIZT-2, M2:QA14-BIZT-2, M6:QA14-BIZT-4, M2:BIZT-G3-2, M4:BIZT-G2-9 | Egy közös protokoll a GK §4-ben, meglévő elemekből; „azonnal elérhető” = ugyanazon a helyszínen; előzetes, peulánkénti besorolás; érzékeny peulán két felkészített 18+ felnőtt |
| D-02 | M6.A tiltott zóna: „a kiskorúakra is térjen ki” (GYV-17) | Memuna + a peula tartalomfelelőse · ugyanők | EMBERI DÖNTÉS (megerősítés) | M6:QA14-BIZT-5b | Alkalmazási körként olvasni; a mostani szöveg ezt teljesíti |
| D-03 | M3.A/M3.B eset- és kártyakészlet a létszámhoz; a 4.3.3 esete négy csoportnál (PRG-11, PRG-12) | M3 modulgazda + Memuna · ugyanők | EMBERI DÖNTÉS | M3:QA14-NYELV-13, M3:IMPL-G3-9 | Meglévő kártyák duplikálása; a 4. kártya marad, a címből kikerül az „új” |
| D-04 | Eszkalációs küszöb és címzett hat helyen (GYV-4, GYV-7, GYV-8, GYV-19) | Memuna (egyes részeknél + programvezető, értékelési felelős, projektgazda) · Memuna, a GYV-8-nál + programvezető | EMBERI DÖNTÉS | M6:QA14-BIZT-1, M6:QA14-BIZT-2, M7:QA14-BIZT-6, Z:QA14-BIZT-2, M4:QA14-BIZT-3, M0:BIZT-5, M6:BIZT-G1-1 | A modul saját kánoni mondatainak átvétele, új címzett nélkül |
| D-05 | Segélyvonal-tájékoztató, 116-111 / 116-000 (GYV-14) | Memuna · Memuna (vétó a HUM:471 soron) | EMBERI DÖNTÉS (P1) | M3:BIZT-G2-2 | A HUM:471 sor újranyitása a szolgáltató leírása szerint, telefonszám-változás nélkül |
| D-06 | JOG-1: a jogászi ellenőrzés és a kijelölt felnőtt nyilvántartási helye | projektgazda · jogi szakértő, Memuna | EMBERI DÖNTÉS (kicsi) | M3:BIZT-G1-8 (döntési rész) | G1 #1 tracker-issue vagy új HUM-sor; a bemenetek nem ajánlanak |
| D-07 | Biztonsági rubrika- és itemkalibráció (ERT-21, GYV-18, GYV-9, ERT-32) | értékelési felelős + Memuna; rubrikaszint, kulcs: projektgazda · ugyanők | EMBERI DÖNTÉS | M3:QA14-BIZT-2, M6:QA14-BIZT-3, M7:BIZT-G1-2, M7:PED-G2-4, M6:ERT-G1-2, M6:ERT-G3-4 | A titoktartás-kérés a feltételbe; R3 Alapszinten két címzett; új fiktív 12. item; R4-horgony két típusra, kalibrációval |
| D-08 | Passzjog: egyenértékű passz (M2.4), tájékozott passz (M3.3) (GYV-2) | Memuna + programvezető; build-spec: projektgazda · ugyanők, QA: Memuna | EMBERI DÖNTÉS | M2:QA14-BIZT-4, M3:IMPL-G2-5 | A passz-mondat a „mit nem kezdenél el” elemmel bővül; a meglévő cím megjelenik |
| D-09 | GYV-1: határidős átnézésnek számít-e az M2 kapu 24 órás megerősítése | Memuna · DPO / jogi felelős | EMBERI DÖNTÉS | M2:QA14-BIZT-5 | A kutató szerint nem; a verifier ezt nem fogadta el lezárásnak |
| D-10 | Feltárás a tárolt beadásban és a Feedback-válaszban (GYV-11, HUM-PRIV-01) | Memuna + DPO; pótlás: értékelési felelős · ugyanők | EMBERI DÖNTÉS | M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2 | Átmentés az incidensnyilvántartásba, korlátozás, kézi törlés jogi felülvizsgálat után; feltárásmentes pótlás külön próbálkozással |
| D-11 | Hozzáférési modell: az ADV-1 kiterjedése, ASSIGN-csoportmód, ADV-4 technikaválasztás | projektgazda; LMS-/build-spec gazda; DPO (+ Memuna) · DPO / jogi felelős | EMBERI DÖNTÉS | KANON:QA14-BIZT-1, M0:QA14-BIZT-3, KANON:QA16-IMPL-2, M3:BIZT-G1-5, M3:BIZT-G2-7 (döntési rész) | Szűkítés mindhárom profilra „Separate groups”-szal; a QUIZ-D-n activity-szintű override; Assignmenten csoportmód + szerep csak csoportba sorolás után |
| D-12 | M0 belépőkvíz: „a két item nyilvános visszajelzése” (GYV-23) | programvezető + Memuna; adatkör: DPO · ugyanők | EMBERI DÖNTÉS | M0:QA14-NYELV-3 | Tartalomszintű, név és eredmény nélküli visszajelzés mindenkinek |
| D-13 | Adatkör-besorolás: közös eszköz, cetlik, visszaazonosítható részlet, M2-jegyzet (ADV-11, ADV-7, GYV-21, ADV-1) | projektgazda; DPO / jogi felelős; Memuna + DPO · LMS-gazda, DPO, Memuna | EMBERI DÖNTÉS | M0:QA14-BIZT-4, M4:QA14-BIZT-5, Z:QA14-BIZT-3, M2:QA14-BIZT-7, M2:BIZT-G1-6 (megőrzés) | Öt besorolás; a javaslat mindenütt a meglévő, szigorúbb vagy azonos modulbeli mintát követi |
| D-14 | AI-út: metaadat-megőrzés és tanulói tájékoztató (ADV-12, GYV-10, LMS-8) | DPO / jogi felelős; programvezető + Moodle-adminisztrátor · DPO / jogi felelős | EMBERI DÖNTÉS | KANON:QA14-BIZT-5, KANON:QA14-BIZT-3b | Most inaktív; utána rövid, DPO által rögzített megőrzés ZDR-kérelemmel; a közvetített út kimondása a §7:194-gyel együtt |
| D-15 | Build-spec és completion: M3 kvíznyitás, Z.3 5. dia, M4 rubrika helye, M6 grade, M2.1 SLIDE 4, fórum (ERT-9, ADV-3, ERT-8, LMS-4, PRG-9, ADV-6) | projektgazda (build-spec gazda), LMS-gazda, értékelési felelős, M2 modulgazda · DPO, értékelési felelős | EMBERI DÖNTÉS | KANON:QA14-ERT-2, KANON:QA14-IMPL-7b, M4:ERT-G2-4, M6:IMPL-G1-7, M2:IMPL-G1-3, M0:QA14-ERT-1 | Hat beállítási döntés, mindegyiknél meglévő precedenssel |
| D-16 | Z.4 záró reflexió: „Teljesítve” alsó határa, passz jelzése, „kiürítés” (ERT-38, ERT-3) | értékelési felelős; „kiürítés”: projektgazda · programvezető, DPO | EMBERI DÖNTÉS | Z:QA14-NYELV-1, Z:ERT-G1-1, Z:QA14-ERT-2, Z:QA14-IMPL-3 | A beadás egészének értelmezhetősége a mérce; opcionális passz-jelölés; a „kiürítés” az üres beküldés negatív tesztje |
| D-17 | Rubrikahorgonyok és kalibrációs mondatok (ERT-26, ERT-42, ERT-43, ADV-5 R1) | értékelési felelős + projektgazda; ERT-42-nél DPO · módszertani lektor, programvezető | EMBERI DÖNTÉS | M5:QA14-ERT-1, M7:BIZT-G1-1, M7:PED-G1-1, M7:BIZT-G1-6 (b) | Kalibrációs mondat szintváltozás nélkül; az R8 pedagógiai + külön adatvédelmi stop; R1: „ellenőrizhető jel vagy kimenet” |
| D-18 | Item- és kulcsdöntések (ERT-23, ERT-28, ERT-30, PRG-15) | értékelési felelős + modulgazda, M5 szerzője, szakmai lektor · ugyanők | EMBERI DÖNTÉS | M3:IMPL-G2-14, M5:ERT-G1-9, M5:NYELV-G1-11, M5:PED-G1-3 | Itemenkénti kulcsvalidálás; a ✅ a tanított láncot követi; első személyű C opció; egyértelműen formális helyzetek |
| D-19 | Kimeneti célok illesztése (TERM-7, PRG-2, ADV-3 / régi X-10, ADV-5) | projektgazda, modulgazda, értékelési felelős · helyi ideológiai felelős, DPO | EMBERI DÖNTÉS | M5:PED-G1-10, M4:ERT-G1-10, M2:QA14-ERT-2 | „Elmagyarázza” helyett „felismeri” típusú szűkítés; a hub-cél a kitalált példát is engedi |
| D-20 | PRG-1: tételes vágási tervek | az érintett modulgazda (M3.B-nél + Memuna) · programvezető | EMBERI DÖNTÉS | M0:PED-5, M2:PED-G3-1, M3:PED-G3-1, M4:PED-G2-2, M4:NYELV-G2-6, M5:PED-G2-6, M5:QA-PED-2, M6:PED-G3-1, M7:PED-G3-1 | Modulonkénti vágás a 45’ és a blokkhatárok megtartásával; az M5.1-nél újrabecslés próbaolvasókkal |
| D-21 | PRG-5: 1–5 fős F-peula-változat, kapacitás, pótlási felelős | modulgazda (PRG-4 csomag), Memuna (1:1), programvezető · programvezető + értékelési felelős | EMBERI DÖNTÉS | M3:ERT-G3-10 | Egy közös, programszintű kis létszámú keret modulspecifikus betéttel |
| D-22 | M7.B „átjárás” szándéka (PRG-16) | M7 modulgazda · ugyanő | EMBERI DÖNTÉS | M7:NYELV-G3-12 | Logisztikai olvasat: átvonulás másik helyszínre |
| D-23 | ERT-5 D1/D2: az M7 kapukvíz Review options ablakmátrixa és zárási mechanizmusa | build-spec gazda (LMS-gazda) + értékelési felelős; dátumok: programvezető · értékelési felelős, M3-nál Memuna | EMBERI DÖNTÉS | ERT-5 maradéka (ledger: M7:G7-ERT5-2) | D1: a hibázott kompetenciát a mentor írja a GATE-CP-be; D2: nincs kvízszintű zárás, a felülbírálás zárási ideje a javító határideje |
| BK-01 | Memuna G1-verdikt (M3.4 passz, GYV-6 küszöb) + RA 9 negatív teszt | Memuna; LMS-gazda | BIZONYÍTÉK-KAPU | M3:PED-G2-1, M4:BIZT-G2-10, M4:BIZT-G2-9 (küszöb-QA) | G1, G3b |
| BK-02 | M5.3 completion-profil | LMS-gazda + módszertani lektor | BIZONYÍTÉK-KAPU | M5:IMPL-G2-2 | G3b, RA 4. pont |
| BK-03 | M4 tárolt TEXT-C adatköre | DPO / jogi felelős | BIZONYÍTÉK-KAPU | M4:BIZT-G1-2 | G2 |
| BK-04 | JOG-1 jogászi ellenőrzés és Memuna-jóváhagyás | jogi szakértő, Memuna | BIZONYÍTÉK-KAPU | M3:BIZT-G1-8 | G1 |
| BK-05 | ADV-4 runtime-visszaolvasás | LMS-gazda | BIZONYÍTÉK-KAPU | M3:BIZT-G1-5, M3:BIZT-G2-7 | G3b; utána D-11 (c) |
| BK-06 | ADV-2 / ADV-10 dokumentáció és hozzáférési teszt | programvezető, DPO, LMS-gazda, Memuna | BIZONYÍTÉK-KAPU | M3:BIZT-G2-5, M3:BIZT-G3-8 | G2, G3b |
| BK-07 | ADV-1 staging role-matrix | LMS-gazda, DPO | BIZONYÍTÉK-KAPU | M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6 (hozzáférés) | G2 POST-BUILD, RT-P0-15 |
| BK-08 | LMS-7 alt-szöveg QA | hozzáférhetőségi gazda | BIZONYÍTÉK-KAPU | M7:IMPL-G2-12 | G5a/G5b |
| BK-09 | PRG-14 provenance-nyilatkozat | szerző / tananyagfelelős, médiafelelős | BIZONYÍTÉK-KAPU | M4:BIZT-G1-7 | nincs G-sor; legközelebb G2 |
| BK-10 | ERT-5 ablakmátrix célverziós tesztje | LMS-gazda / TEST_OWNER | BIZONYÍTÉK-KAPU | ERT-5 (ledger: M7:G7-ERT5-3) | G3b, RT-P0-19, RT-P0-08 |
| BK-11 | ADV-5: GDPR 9. cikk szerinti minősítés | DPO / jogi felelős | BIZONYÍTÉK-KAPU | M7:BIZT-G1-6 (c) | G2 |
| BK-12 | PRG-12: Memuna-review az M3.B 4. esetkártyájára | Memuna | BIZONYÍTÉK-KAPU | (D-03-hoz) | G1 |
| BK-13 | Döntés utáni runtime- és szerepköri bizonyítékok | LMS-gazda, értékelési felelős, Memuna, DPO | BIZONYÍTÉK-KAPU | (D-04, D-07–D-09, D-15, D-16-hoz) | G1, G2, G3b, SIGNOFF |
| KF-01 | VO fix pack: kimondott szöveg a `@source` blokkokban | VO-gazda / médiafelelős · DPO | VO-PACK | M1:QA14-BIZT-1, M4:QA14-BIZT-4 | Újrarender a döntések szerint; addig nyitott release-blokkoló |
| KF-02 | ERT-19 hatálybalépése | modulgazda + értékelési felelős | SIGNOFF | M2:PED-G1-11 | Aláírás és előzetes tájékoztató, utána egy menetben átvezethető |

---

## 2. Emberi döntési csomagok

### D-01 – Peula-megállítási protokoll, helyettes és létszámnorma (GYV-5)

**Mit kell eldönteni?** Mi a GYV-5 „kötelező megállítási protokollja”? Mit jelent az „azonnal elérhető helyettes”? Ki és mi alapján dokumentálja az „alacsony kockázatot”, mely peulák érzékenyek, és mi a végleges létszámnorma?

**Ki dönt, ki ellenőriz:** Memuna + programvezető. Vétó/QA (HUM 14, GYV-5): Memuna + programvezető (HUM-SAFE-03; GK §5:120).

**Háttér:** A protokoll tartalma sehol nincs a kánonban; a GK §4, §4.1, §4.2 és a HUM-SAFE-03 nem ír le megállítási lépést. A modulok lépéssorai eltérnek, és kettő kifejezetten nem állítja meg a kört (M0.A:134 „a kör/feladat folytatódik mással”, M2.A:281–283). Egy képzővel a „felnőtt vele van” (GK:64) és a „kör folytatódik” egyszerre nem teljesíthető. Az `F` jelölés szerint a szó szerinti GYV-5 az óvatos alapértelmezés, de két kiskapuja tartalom nélkül áll.

**Opciók (a protokollra):**
- (a) Egy közös protokoll a GK §4-ben, csak meglévő elemekből: semleges megállító mondat (M6.A:492), a szünet felkínálása, egy felnőtt a felkavart kiskorúval a kijelölt, átlátható helyen (GK:64), a helyettes hívása, és a kör csak a második felelős érkezése után folytatódik; gyermekvédelmi aggálynál Memuna, közvetlen veszélynél előbb a biztonság és a 112 (§4.1). Előny: egységes, feloldja az ütközést. Kockázat: a GK új eleme, Memuna-szövegezés kell.
- (b) Peulánként a meglévő lépéssor a protokoll. Előny: a legolcsóbb. Kockázat: az M0.A:134 és az M2.A:281–283 ellentmondása megmarad.
- (c) Érzékeny peulán nincs protokoll-ág, két 18+ felelős kötelező. Előny: a legszigorúbb. Kockázat: kapacitásigény.

**Javaslat és indoklás (G1 kutató):**
1. Protokoll: az (a). Az M6.A-nál elég a 4.3.2/B-re hivatkozni, mert az 1. lépése már megállítja a kört, és a KAPU P1 ugyanezt kéri számon.
2. „Azonnal elérhető”: a GK:60 mintája, „ugyanazon a helyszínen azonnal elérhető”; a telefonos elérhetőség nem elég.
3. Besorolás: a Memuna és a programvezető előre, peulánként sorol be, kánoni helyen; kivételes esetre a programvezető írásos kockázatfelmérése. A képző önminősítése nem javasolt. Az önmagukat érzékenynek nevező peulák (M0.A, M2.A, M3.B, M6.A, Z.A) alapból ne legyenek egyszemélyesen vezethetők. Az M2.B és az M2.F besorolása nyitott; az M4.A-ra az ajánlás „nem érzékeny”, mert a GYV-6 szerint a szereplési szorongás nem automatikusan krízis.
4. Létszámnorma: érzékeny peulán legalább két, a HUM-SAFE-05 szerint ellenőrzött és felkészített 18+ felnőtt (képző vagy mentor), 20 főig. A 15–17 éves madrih nem számít bele (HUM-SAFE-03).
5. Az M0.A:134 és az M2.A:281–283 feltételes alakot kap (van második felelős: a kör folytatódik; nincs: megállás a protokoll szerint). A szövegezés a Memunáé.

Források: NSPCC Learning, „Recommended adult to child ratios for working with children” (https://learning.nspcc.org.uk/research-resources/briefings/recommended-adult-child-ratios-working-with-children): 13–18 év 1:10, „at least two adults present”, csak 18+ számít felnőttnek; ajánlás, nem jogszabály. Keeping Children Safe, International Child Safeguarding Standards (https://www.keepingchildrensafe.global/wp-content/uploads/2023/09/KCS-CS-Standards-ENG-200218.pdf), Standard 3: a kockázatbesorolás szervezeti folyamat. Hatályos magyar létszámnormát a kutató nem talált: a 6/2025. (II. 25.) BM rendeletet csak nem hivatalos forrásból (net.jogtar.hu) olvasta, a hivatalos NJT-oldal nem töltött be, a Gyvt.-t nem olvasta végig. A Scouting America szabályát nem tudta ellenőrizni, ezért nem támaszkodik rá.

**Addig:** a szó szerinti GYV-5 marad (M0.A:94, M2.A:65, :466, M6.A:182, :712). Protokoll-tartalom, 4.3.2/B-azonosítás és besorolás nem kerül be. A szigorúbb átmeneti olvasat („csak a kétfelnőttes ág teljesíthető”) új szűkítő szabály volna; ezt csak a döntéshozók mondhatják ki. Megfigyelés: az M0.A ellenőrzőlistájából hiányzik a GYV-5-pont; ennek felvétele új tartalom.

**Mit old fel:** M0:QA14-BIZT-2, M2:QA14-BIZT-2, M6:QA14-BIZT-4, M2:BIZT-G3-2, M4:BIZT-G2-9 (a besorolási és a „ki a felnőtt” rész; a GYV-6 küszöb-QA a BK-01-ben).

**Elfogadás után:** a protokoll a GK §4-be kerül, a peulák hivatkoznak rá; a besorolás kánoni helyre; az M0.A:134 és az M2.A:281–283 a Memuna szövegezésével feltételes alakot kap.

**Már átvezetve:** a GYV-5 zárómondata („A végleges létszámnormát a Memuna és a programvezető határozza meg.”) az M6.A:182-ben (`3b160fc`; verifier A2).

### D-02 – M6.A tiltott zóna: „a kiskorúakra is térjen ki” (GYV-17)

**Mit kell eldönteni?** Mit jelent a GYV-17-ben, hogy a tiltott zónák kerete „a kiskorúakra is térjen ki”: alkalmazási kört vagy tartalmi elemet?

**Ki dönt, ki ellenőriz:** Memuna + a peula tartalomfelelőse. Vétó/QA (HUM 14, GYV-17): ugyanők.

**Mostani állapot:** az M6.A:462–466 kötelező, a játék előtt kimondott keret; kitér az identitásra, a kirekesztésre és az önfeltárásra, és kimondja: „(Ez a keret soha nem maradhat el, kiskorú résztvevőkkel sem.)” Ez a korábbi verifier átmeneti javítása.

**Opciók:**
- (a) Alkalmazási kör: a :466 teljesíti, nincs további szöveg. Előny: nincs új tartalom. Kockázat: ha a döntéshozó tartalmi elemet értett, az hiányzik.
- (b) Tartalmi elem: a kiskorúakat, életkort érintő állítás is tiltott zóna. Előny: tágabb védelem. Kockázat: új tartalom.
- (c) Korosztályi igazítás (kivsza). A :460 erről csak a fizikai biztonság kapcsán szól. Kockázat: új tartalom.

**Javaslat és indoklás (G1 kutató):** az (a). A döntési csomag kérdése (CSOMAG :355) szó szerint arról szólt, hogy kötelező legyen-e a kimondás kiskorú résztvevőkkel. Megerősítés után a tétel MÁR RENDBEN.

**Addig:** a :462–466 marad; ez az óvatos alapértelmezés (a keret mindig kötelező). A KAPU :221 és :233 kulcsa nem változik.

**Mit old fel:** M6:QA14-BIZT-5b. **Elfogadás után:** (a) esetén nincs szerkesztés, csak ledger-lezárás; (b) vagy (c) esetén új tartalom az M6.A 4.3 keretében.

### D-03 – M3.A/M3.B eset- és kártyakészlet a létszámhoz (PRG-11, PRG-12)

**Mit kell eldönteni?** (1) Mi az M3.B 4.3.3 („Gyors alkalmazás – új eset kívülről”) esete, ha négy csoport dolgozik, és a 4. esetkártya a PRG-12 szerint a 4.3.3 fiktív esete? (2) Hogyan igazodik a kártya- és esetkészlet a 8–20 fős létszámhoz, ha a PRG-11 szerint 3–5 fős csoportok az alap?

**Ki dönt, ki ellenőriz:** M3 modulgazda + Memuna. Vétó/QA (HUM 14): PRG-12: M3 modulgazda + Memuna (tartalmi QA); PRG-11: az adott modulgazda (M3.B: + Memuna).

**Mostani állapot:** az M3.A:396 csoportonként 2–3 kártyát ad egy 8 darabos szettből; 20 főnél ez 8–21 kártyát kívánna. Az M3.B:354 „3–4 fős csoportokra … alapból 3 csoporttal” dolgozik; 20 főnél ez nem hajtható végre.

**Opciók (1):** (a) a 4. kártya marad, a címből kikerül az „új” – a PRG-12 szó szerinti olvasata; (b) ötödik, előre megírt, Memuna által átnézett eset – új tartalom; (c) négy csoportnál a lépés elmarad, a „Fontos különbség” akkor is elhangzik (:471) – nincs új tartalom.

**Opciók (2):** (a) meglévő kártyák duplikálása (M3.A: négy csoporttól a 8-as szett második példánya; M3.B: négy csoporttól az 1–3. eset duplán, visszahozás esetenként) – nincs új tartalom; (b) új esetkártyák – új gyermekvédelmi tartalom (PRG-4, Memuna); (c) három csoport marad nagyobb csoportokkal – ellentmond a PRG-11-nek.

**Javaslat és indoklás (G1, G9 kutató):** (1)(a), elfogadható alternatíva az (1)(c); (2)(a). A duplikált eset összevetése maga is tanulságos, és az M3.A közös átbeszélése a képző választotta 3 kártyán marad (PRG-16).

**Addig:** a 4.3.3 címe, az M3.B:354 és :264 marad; saját eset nem kerül be.

**Mit old fel:** M3:QA14-NYELV-13, M3:IMPL-G3-9. **Elfogadás után:** az M3.B 4.3.3 címe, a :186 spec „alapból” szava (`media_manifest.py build` úton), az M3.A/M3.B csoport- és kártyautasításai; célszerűen egy menetben a D-20 M3-as időtervével. A PRG-12 Memuna-reviewja külön bizonyíték (BK-12).

### D-04 – Eszkalációs küszöb és címzett (GYV-4, GYV-7, GYV-8, GYV-19)

**Mit kell eldönteni?** Hogyan alkalmazandó a GYV-7 kétlépcsős küszöbe, a GYV-8 helyszíni 18+ felelőse és a GYV-19 címzettje hat olyan helyen, amelyről a döntés név szerint nem szól?

**Ki dönt, ki ellenőriz:** a Memuna; a Z.3-nál és az M6 KAPU P1-nél a programvezetővel; a ✅-szöveg változásánál az értékelési felelős és a projektgazda is; az M4.3-nál a projektgazdával; az M0 belépőkvíz itemszövege a projektgazdáé (hub :180). Vétó/QA (HUM 14): GYV-4: Memuna (vétó/QA: a Memuna és a helyettese); GYV-7: Memuna (HUM-SAFE-01/03); GYV-8: Memuna + programvezető; GYV-19: Memuna.

**Részkérdések, opciók és javaslat (G2 kutató):**
- **(a) M6.3:749, M6.4 6D és ZÁRÓ (:933–934, :1028); M6.2:783** (M6:QA14-BIZT-1, -2). A „friss seb” az ötlépéses jelzési útra visz; az M6.2:783 már kétlépcsős, de nem mondja meg, ki adja a „támogató mentorálást”. Opciók: a „friss seb” kikerül, és az M6.2:783 mondata átkerül; a „friss seb” marad „veszélyeztetettséggel járó” pontosítással; status quo (túleszkaláció, feszül a GYV-13 elvével). **Javaslat:** az első, kiegészítve a kánoni M6.A:502 és M3.3:416 mondatával, hogy a kiskorú madrih ne maradjon egyedül a „nem jelzési ügy” minősítéssel. Hogy bizonytalanságnál a helyszíni 18+ felelős vagy a Memuna a konzultációs út, az új szabály: a Memuna dönti el. Korlát: a 2026-10-05-i jegyzőkönyv szerint a 6D/ZÁRÓ ismétlése Memuna-QA, és az M6-NY-D27 a küszöböt zárolja.
- **(b) M7.B:480** (M7:QA14-BIZT-6): a tanácskérési szabály a „komoly szorongást” is a Memunához küldi. Opciók: marad; a modul saját :93 szerkezete (gyermekvédelem, bántalmazás: Memuna; komoly szorongás: mentor; veszélyeztetettség gyanújánál azonnal Memuna); „a Memunától vagy a mentorodtól”. **Javaslat:** a :93 szerkezete. Az AI-tilalom egyik opcióban sem gyengülhet.
- **(c) M0 csoportchat-szívatás** (M0:BIZT-5): az M0.2:271 Memuna-jelzést, az M0.4:310 Memuna nélküli beavatkozást kulcsol. Opciók: mindig jelzés (GK §4.1:81); GYV-7-es kétlépcső; helyenként eltérő. **Javaslat:** a kétlépcső, az ismétlődő csúfolás „zaklatásnak” minősül; a minősítés a Memunáé. Utána az eltérő visszajelzés objektív átvezetés; a kvízkulcs nem változik.
- **(d) M4.3:360 terepi hanih-helyzet** (M4:QA14-BIZT-3): a GYV-19 „képző” eleme. Opciók: csak az M2.A-ra szól, az M4.3 kész; helyszíni 18+ felelős (GYV-8), képző nélkül; szó szerinti „képző”. **Javaslat:** az első: terepen nincs képző, és a GK §4.1:82 (címzett mindig a Memuna) nem gyengül.
- **(e) M6 KAPU P1 (✅ A :355, visszajelzés :367) és az M6.B játéklap „kit hívsz” rovata** (M6:BIZT-G1-1). Opciók: csak a visszajelzés kap két kánoni elemet (GK §4:60, M2.4:209 elérhetetlenségi mondat), a ✅ nem változik; a ✅ is változik; marad. **Javaslat:** az első. A GYV-4 (c) alkérdése a kutató szerint G1-bizonyíték, nem döntés (BK-13).
- **(f) Z.3:310 mintamondat és a :303 doboz** (Z:QA14-BIZT-2; nem blokkoló, a mostani szöveg teljesíti a GYV-8-at). Opciók: marad; a GK §4.1 5. lépése („Közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés.”) szó szerint a :303 dobozba; a mintamondatba (ez az LMS-Z-07 elfogadási kritériumát érintené). **Javaslat:** a doboz. Forrás a 112 működésére: https://europa.eu/youreurope/citizens/travel/security-and-emergencies/emergency/index_hu.htm.

**Addig:** minden hely változatlan. A mostani szövegek többnyire túleszkalálnak, ami védelmi szempontból óvatos. Kivétel az (e): munkaidőn kívül elérhetetlen utat tanít, de védelmi elemet nem töröl.

**Mit old fel:** M6:QA14-BIZT-1, M6:QA14-BIZT-2, M7:QA14-BIZT-6, Z:QA14-BIZT-2, M4:QA14-BIZT-3, M0:BIZT-5, M6:BIZT-G1-1.

**Elfogadás után:** a megnevezett leckék, peulák és az M6 KAPU visszajelzése a modul saját kánoni mondatainak szó szerinti átvételével igazodnak; a (d) után az `M4:BIZT-G1-6` a „képző” részig is zárható.

**Már átvezetve:** a GYV-19 az M2.A:362-ben (`3b160fc`; lásd 5.2).

### D-05 – Segélyvonal-tájékoztató, 116-111 / 116-000 (GYV-14)

**Mit kell eldönteni?** Újranyitja-e a Memuna a HUM:471 „Segélyvonalak” sort, és milyen 116-111- és 116-000-leírást hagy jóvá a GK §3.3-ba és a §4.1-be?

**Ki dönt, ki ellenőriz:** Memuna. Vétó/QA (HUM 14, GYV-14): Memuna (vétó a HUM:471 soron). Az újranyitást maga a GYV-14 írja elő („Ha a kánon félrevezető, a Memuna formálisan nyissa újra a konkrét tájékoztató sort; ne változtassunk telefonszámot igazolás nélkül.”), ezért ez nem a 125 döntés újranyitása.

**Mostani állapot:** GK:47: „116-000: … felnőttek is hívhatják; nem általános „szülői vonal””; ugyanezt követi az M3.3:709 és az M3 KAPU:367. A GK:46 és az M3.3:709 szerint a 116-111 a gyerek érdekében telefonáló felnőttet is fogadja.

**Kutatás (G2):** a Kék Vonal 116-000-oldala (kek-vonal.hu/tudastar/116-000-segelyvonal-a-bantalmazott-es-eltunt-gyerekekert-szakembereknek-is): „A 116 000 Segélyvonalon várjuk azoknak a felnőtteknek a hívásait, akik aggódnak egy gyermekért” – ezt a kutató a 2026-10-11-i verifier elsődleges forrásból készült idézetéből vette át. A kek-vonal.hu/szuloknek/116-000 oldal: „HÍVJ MINKET, ha aggódsz egy gyerekért!”; a kek-vonal.hu/fiataloknak szerint a 116-111 a gyerekek és fiatalok vonala, felnőtt hívóra a kutató megerősítést nem talált. A Kék Vonal oldalait a kutató összegző eszközön át érte el. NMHH (https://nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese): a 116000 neve „Eltűnt gyermekek felkutatására fenntartott forróvonal”, a 116111-é „Gyermekek segélyvonala”.

**Opciók:**
- (a) Nincs újranyitás. Előny: nincs változás. Kockázat: a kánon félrevezető marad.
- (b) Újranyitás a szolgáltató leírása szerint: a 116-111 a gyerekeknek és fiataloknak; a 116-000 bántalmazott és eltűnt gyerekek ügyében, a gyermekért aggódó felnőtteknek (szülőknek, szakembereknek) is; a „nem általános szülői vonal” és a 116-111 felnőtt-állítás törlése. Előny: a hívó a megfelelő vonalra jut. Kockázat: Memuna-aktus kell.
- (c) A GYV-14 saját, szűk fordulata („eltűnt gyermekek vonala”). Kockázat: szűkebb a HUM-SAFE-01-nél és a szolgáltató leírásánál, szó szerint nem vezethető át.

**Javaslat és indoklás (G2):** a (b), a release-napi ellenőrzéssel (GK §6) egy lépésben. Telefonszám nem változik.

**Addig:** a mostani szöveg marad, mert repóból nem írható át. Ez nem óvatos alapértelmezés: egy aggódó felnőttet rossz vonalra küldhet. Ezért P1.

**Mit old fel:** M3:BIZT-G2-2. **Elfogadás után:** a GK §3.3 és §4.1, az M3.3:709 📞 doboza és az M3 KAPU:367 egy változtatáskészletben, a Memuna által jóváhagyott leírással.

### D-06 – JOG-1: a jogászi ellenőrzés és a kijelölt felnőtt nyilvántartási helye

**Mit kell eldönteni?** Hol rögzüljön a JOG-1 jogászi ellenőrzése (a Gyvt. 17. § címzettjei és határidői) és a külső jelzésről döntő kijelölt felnőtt megnevezése?

**Ki dönt, ki ellenőriz:** projektgazda (a JOG-1 sora: „a nyilvántartás helyéről a projektgazda”). Vétó/QA (HUM 14, JOG-1): jogi szakértő; jóváhagyás: Memuna (GK §5).

**Opciók:** (a) a G1 #1 tracker-issue; (b) új HUM-sor. Mindkettőt a JOG-1 maga nevezi meg. Előnyüket és kockázatukat a bemenetek nem mérlegelik.

**Javaslat:** a kutatói és verifier-kimenetek nem adnak ajánlást; a verifier (C4) szerint a repóban erről nincs döntés. Kis, nem tartalmi döntés.

**Mit old fel:** M3:BIZT-G1-8 döntési része (ledger: X-14). A bizonyíték-rész a BK-04-ben. **Elfogadás után:** a választott helyen nyitott bejegyzés a jogászi és Memuna-bizonyítéknak; a hub :42 nem változik tovább.

**Már átvezetve, és amit a verifier elvetett:** a JOG-1 hozzáadó mondata a hub :42-ben, a jogászi tagmondat megtartásával (`3b160fc`; vessző: `16a9ad9`). A kutató eredeti, cserés változatát a verifier (A5) ELVETETTE, mert törölte volna a „a külső jelzés jogi kérdésében jogi szakértő dönt” tagmondatot, és ez jogi kikötést gyengített volna.

### D-07 – Biztonsági rubrika- és itemkalibráció (ERT-21, GYV-18, GYV-9, ERT-32)

**Mit kell eldönteni?** (a) Lefedi-e az M3 KAPU R2 „titoktartási ígéret” feltétele a hanih titoktartás-kérését, és mi az R3 Alapszintje határhelyzetben? (b) Mi az M6 KAPU 12. item új szára, ✅-ja és disztraktora? (c) Milyen horgonnyal kerül az M7 blokkoló R4 minimumába és a mintatáblába a felelős 18+ felnőtt, a Q9/(C) szabállyal összehangolva? (d) Hogyan erősödjön az M6 R4 „Oké”-horgonya?

**Ki dönt, ki ellenőriz:** értékelési felelős + Memuna; rubrikaszintről és kulcsról a projektgazda. Vétó/QA (HUM 14): ERT-21: értékelési felelős + Memuna, rubrikaszint: projektgazda; GYV-18: Memuna + értékelési felelős, kulcs: projektgazda; GYV-9: Memuna + értékelési felelős, rubrikaszint: projektgazda; ERT-32: értékelési felelős, rubrikaszint: projektgazda.

**(a) ERT-21 (M3:QA14-BIZT-2, G3 kutató).** A KAPU-M3:318 és :325 szerint feltárás vagy titoktartási ígéret nélküli helyzetben az R2 nem büntető. A kánon a hanih kérését központi helyzetként tanítja (M3.3:177, :187), és a sablon (M3.4:832) maga is kérdez a titoktartásra. Opciók (1): a kérés is beletartozik / csak az elhangzott ígéret. Opciók (2): Alapszinten mindig a Memuna bevonása / a helyzet típusának megfelelő felnőtt (GYV-8) / mindkettő elfogadott. **Javaslat:** (1) a kérés beletartozik, mert a sablont követő tanulót nem buktatja; (2) mindkettő elfogadott, mert sem a Memunához forduló, sem a GYV-8 szerint helyes operatív címzettet megnevező tanuló nem bűnhődik. Az öt hely együtt változna (KAPU-M3:318, :325 két cellája, M3.4:837, M3.B:513).

**(b) GYV-18 (M6:QA14-BIZT-3, G3 kutató).** A KAPU-M6:328–343 a „friss seb” mondatot tartalmazó történetre épül; a lecke diaszövege (M6.2:606) már átvezetett. Opciók: új fiktív helyzet; a mostani keret marad a „friss seb” nélkül (ütközik az ERT-36-tal, mert a ✅ szó szerint a lecke ✅-ja lenne); a ✅ marad passz-formulával (nem teljesíti a „szereplőközpontú” előírást). **Javaslat:** új fiktív helyzet, szereplőközpontú ✅-val; a disztraktorok ugyanazt a három hibatípust hordozzák (megnevezés vagy szégyenítés, álkérdés, áldozathibáztatás); a :338 és a :343 vele mozog. A G3 kutatói kimenetben illusztratív, nem implementálandó tervezet van a jóváhagyóknak. A narráció nem döntés, hanem VO fix pack (KF-01).

**(c) GYV-9 (M7:BIZT-G1-2, M7:PED-G2-4).** Ebben a futásban nem kutatott: a G3 kutató levágta. A döntés iránya adott: a felelős 18+ felnőtt megnevezése csak a rubrikahorgony és a már tanított Q9/(C) szabály összehangolt, formális jóváhagyásával kerülhet be, és a hallgató nem bukhat előzetesen nem közölt követelményen. Opciókat a bemenet nem tartalmaz. A jóváhagyóknak egyszerre kell megnézniük az M7 KAPU R4 2–3. szintjét, a (C) 5. sorát, a Q9-et, az M7.4 mintatábláját és a MUNK-01 specet; ezeket a kutató nem olvasta vissza.

**(d) ERT-32 (M6:ERT-G1-2, M6:ERT-G3-4, G9 kutató).** Az M6 KAPU:399 R4 „Oké” szintje ma egy konkrét fizikai vagy érzelmi biztonsági megjegyzést kér; a tanított minimum a KAPU:189-ben áll. Opciók: (A) teljes, eszköztípusonkénti horgony; (B) első lépésben csak a két megnevezett típusra (kontaktjáték, szenzitív helyzet), a többi a mai horgonyon; (C) a horgony marad, mentori megjegyzéssel – ez ellentmond a döntésnek. **Javaslat:** (B), kalibráció 6–10 mintalapon két értékelővel (értékelési felelős + Memuna), előzetes tájékoztatással, visszamenőleges hatás nélkül. Az M6.B:219 mezőlistáját egy menetben kell igazítani (a kutató nem olvasta vissza).

**Addig:** minden rubrika, item és kulcs változatlan. (a): a kapu kalibráció és kétszemes döntési rend nélkül úgysem élesedhet (KAPU-M3:317). (b): nem óvatos alapértelmezés, de a ✅ jóváhagyás nélkül nem érinthető, és az M6 learner release G1 nélkül amúgy is zárt. (d): a mai, enyhébb horgony biztonságkritikusan nem óvatos, de a döntés tiltja a kalibráció nélküli bevezetést.

**Mit old fel:** M3:QA14-BIZT-2, M6:QA14-BIZT-3, M7:BIZT-G1-2, M7:PED-G2-4, M6:ERT-G1-2, M6:ERT-G3-4.

**Elfogadás után:** az M3 KAPU, M3.4 és M3.B öt helye; az M6 KAPU 12. itemje a :338/:343-mal; az M7 KAPU R4-e, mintatáblája és a tanulói tájékoztató; az M6 KAPU R4-e és az M6.B:219. Látható szöveg, ezért pin kell.

### D-08 – Passzjog: egyenértékű és tájékozott passz (GYV-2)

**Mit kell eldönteni?** (a) Mi számít egyenértékű tudásdemonstrációnak az M2.4 SLIDE 5 passz-útján? (b) Megjelenjen-e a szcenárió meglévő címe az M3.3 P1–P4 passz-választóin?

**Ki dönt, ki ellenőriz:** (a) Memuna + programvezető (HUM-SAFE-03); (b) projektgazda (build-spec gazda), QA: Memuna. Vétó/QA (HUM 14, GYV-2): Memuna + programvezető (HUM-SAFE-03); kapus belépő: értékelési felelős; MAN:57 és az M3.3 §7.1: projektgazda (build-spec gazda), QA: Memuna.

**Opciók (a), M2.4:663:** marad az egy mondat a bevonandó személyről (a mező nem kapu; a titoktartás tilalmát az M3 éles kapuja méri); a passz-mondat kiegészül a 3️⃣ kérdés saját elemével („mit nem kezdenél el”); a „teljes értékű válasz” minősítés elhagyása. **Javaslat (G3):** a kiegészítés: a legkisebb lépés az „ekvivalens” felé, és személyes tartalmat nem kér. Együtt mozog a MAN:57-tel és a hub két passz-sorával (a QA szerint HUB:183, :190; a kutató ezeket nem ellenőrizte).

**Opciók (b), M3.3:58, :63, :67, :70:** a meglévő cím megjelenik, új szöveg nélkül; status quo (vak passz); téma-előjelzés az INSTR-12/34-ben (új gyermekvédelmi szöveg). **Javaslat (G3):** a meglévő cím, mert a tájékozott passz a HUM-SAFE-03 célja. A Memuna nézze meg, nem megterhelő-e maga a cím (például „vágásnyomok”). Kutatási hiány: a H5P Branching Scenario `showContentTitle` működését (melyik cím jelenik meg) a kutató nem ellenőrizte; stagingben kell igazolni (BK-13).

**Addig:** mindkettő marad. Az M2.4 nem automatikus átengedés (a mező „Required”, biztonsági mondatot kér); az M3.3-ban a passz és a biztonsági csomópontok megvannak.

**Mit old fel:** M2:QA14-BIZT-4, M3:IMPL-G2-5. **Elfogadás után:** az M2.4:663, a MAN:57 és a hub passz-sorai; az M3.3 build-specje (BSPEC-05) a cím megjelenítéséről.

### D-09 – GYV-1: az M2 kapubeadvány határidős átnézése

**Mit kell eldönteni?** Vonatkozik-e a GYV-1 („Az LMS-M2-05 kapubeadványon csak akkor maradjon határidős átnézés, ha … SLA bizonyított”) a KAPU-M2:24 24 órás mentori megerősítésére?

**Ki dönt, ki ellenőriz:** Memuna (HUM-SAFE-01); vétó/QA (HUM 14, GYV-1): DPO / jogi felelős. Ha a válasz a HUM:220 programszintű 24 órás döntését érintené, az a projektgazda hatásköre (G3 kutató).

**Ellentmondás a bemenetek között:** a G3 kutató MÁR RENDBEN-nek sorolta: a 24 órás határidő önálló, lezárt döntés (HUM:201–203, :220), kapuértékelési megerősítés, és a GYV-1 kérdése (CSOMAG:211) a biztonsági átolvasást választja szét tőle. A verifier (B7) ezt ELVETETTE: a „maradjon” egy meglévő átnézésre utal, az LMS-M2-05-nek ma egyetlen határidős átnézése a KAPU-M2:24, és a csomag kérdése is e mellett kérdez. A verifier A8 sem tartotta igazoltnak. A verifier verdiktje az erősebb, ezért ez emberi döntés.

**Opciók:**
- (a) Nem vonatkozik: a KAPU:24 kapuértékelési megerősítés, marad. Előny: a HUM:220 érintetlen. Kockázat: ha a Memuna biztonsági átnézésnek tekinti, SLA nélküli ígéret marad.
- (b) Vonatkozik: az M2-ben SLA-bizonyíték kell, vagy a KAPU:24 az M2-ben módosul. Kockázat: a HUM:220 lezárt programszintű döntését írná felül az M2-ben (projektgazdai hatáskör, vétólistás időtartam és completion).

**Javaslat:** a G3 kutató érvei az (a) mellett szólnak; a verifier szerint ez nem bizonyított, ezért a Memuna mondja ki. Az akut út (KAPU-M2:203) mindkét esetben megvan.

**Kapcsolódó megfigyelés (G4):** a Z.4:201 mondata („a beadást látó mentornak vagy értékelőnek azonnal be kell vonnia”) garancia-jellegű; a GYV-1 mintája ilyet az M2-ben tiltott. Érdemes ugyanebben a döntésben megnézni.

**Addig:** marad. A GYV-1 Memuna- és DPO-QA-ja bizonyíték (BK-13).

**Mit old fel:** M2:QA14-BIZT-5. **Elfogadás után:** (a) esetén ledger-lezárás; (b) esetén a KAPU-M2:24 és a MAN:57 projektgazdai döntéssel.

### D-10 – Feltárás a tárolt beadásban és a Feedback-válaszban (GYV-11, HUM-PRIV-01)

**Mit kell eldönteni?** (a) Ki és hogyan korlátozza vagy veszi ki a gyermekvédelmi feltárást tartalmazó tárolt beadást a Moodle-ből? (b) Mi a törlés és a megőrzés rendje? (c) Mi a feltárásmentes pótlás mechanikája, és (d) beszámít-e a feltárást tartalmazó próbálkozás? (e) Kiterjed-e a megőrzési kivétel a Z.4 Feedback nyers válaszaira, szabad-e a tárolt felhasználónévvel visszakeresni a válaszadót, és kell-e tájékoztató mondat a Z.4:370-be? (f) Mit jelent a HUM-PRIV-01 „kikerül a Moodle-ből” a GYV-11 mellett?

**Ki dönt, ki ellenőriz:** Memuna + DPO (a, b, e, f); a visszakeresésnél a jogi felelős is; értékelési felelős (c, d). Vétó/QA (HUM 14, GYV-11): Memuna + DPO; kapueredmény: értékelési felelős; N-9: értékelési felelős + programvezető, Memuna-vétóval.

**Opciók (a, b, f):**
- (1) A Memuna vagy a helyettese az incidensnyilvántartásba menti a szükséges tartalmat (GK:85–86); a Moodle-példányt kijelölt jogosult korlátozza (rejtés, az értékelői hozzáférés elvonása); a végleges törlés kézi, jogi megőrzési felülvizsgálat után. Előny: az LMS nem elsődleges nyilvántartás, nincs automatikus törlés.
- (2) A Moodle-példány a normál megőrzési sor szerint marad, megjelölve. Kockázat: érzékeny tartalom marad az LMS-ben.
- (3) Átmentés után azonnali kézi törlés. Kockázat: ütközik a GYV-11-gyel (nincs törlés jogi felülvizsgálat nélkül).

**Opciók (c, d):** (i) kézzel nyitott, külön próbálkozás, amely nem számít bele a keretbe (a Z.4:359 mintája); (ii) a próbálkozás beszámít.

**Opciók (e):** a Feedback-válasz kivétel a 90 napos összesítés alól, korlátozva / a Memuna az incidensnyilvántartásba menti, a Moodle-válasz a 90 napos sor szerint megy / átmentés után kézi törlés a `mod/feedback:deletesubmissions` jogú szereppel, dokumentáltan. Visszakeresés: tiltott / csak súlyos veszélynél, a Memuna kérésére, megnevezett adminisztrátor által, dokumentáltan.

**Javaslat és indoklás (G4 kutató):** (1) + (i); a „kikerül” korlátozásként olvasandó, amely jogi felülvizsgálat után kézi törlésbe fordul – így mindkét lezárt mondat teljesül. A Feedbacknél a második vagy a harmadik opció, mert így az ADV §3:70 változatlan maradhat (a második esetben a Z.4:401 GYV-11-tagmondata kikerülne). A visszakeresés csak súlyos veszélynél – ez jogi minősítés; ha megengedett, a tájékoztató nem tagadhatja (a HUM-PRIV-03 „név nélkül jelennek meg” mondata a megjelenítésről szól, és nem változhat).

Források: GDPR 17. cikk (3) e), 18. cikk (1) c) és (2), (38) preambulumbekezdés – a kutató másodlagos forrásból (gdpr-info.eu) idézte, mert az EUR-Lex nem töltött be; a magyar hivatalos szöveggel össze kell vetni. NAIH-iránymutatást nem nézett. Moodle 4.5: Feedback FAQ (docs.moodle.org/405) – anonim Feedbacknél a felhasználónév az adatbázisban rögzül, a képernyőn nem látszik; Viewing Feedback responses: „Individual responses may be Deleted if required.”; `mod/feedback/db/access.php`: a `mod/feedback:deletesubmissions` az editingteacher és a manager szerepé.

**Addig:** az M1 KAPU:27, a Z.4:359, :370, :401 és az ADV §5:153 marad; kitalált eljárás nem kerül be.

**Mit old fel:** M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2.

**Elfogadás után:** az ADV §3 és §5, a GK incidensnyilvántartási része, az M1 KAPU:27 pótlási útja és a Z.4 megőrzési, tájékoztató mondatai.

**Már átvezetve:** a GYV-11 dokumentálási mondata az M1 KAPU:27-ben (`3b160fc`; verifier A3), a „jogosult” minősítővel az ADV:153-ban is (`16a9ad9`; QA15-BIZT-1).

### D-11 – Hozzáférési modell: az ADV-1 kiterjedése, ASSIGN-csoportmód, ADV-4 technikaválasztás

**Mit kell eldönteni?** (a) Kiterjed-e az ADV-1 (c) csoportszűkítése a H5P-C, a QUIZ-D/M és a GATE-CP mentori nézetére, és a belépőkvízen (QUIZ-D) ki láthatja alapból a tételszintű egyéni válaszokat? (b) Milyen mechanizmus biztosítja az ASSIGN-S/M-en, hogy a mentor csak a saját csoportját lássa? (c) A runtime-visszaolvasás után melyik tárolásmentes technika legyen az M3 SAFE-1 ágnál és az M3.4 érzelmi önjelzésénél (ADV-4)?

**Ki dönt, ki ellenőriz:** (a) projektgazda, DPO-val; a beállítást az LMS-gazda rögzíti; (b) LMS-gazda / build-spec gazda; (c) DPO, az M3-nál a Memuna is, a mutatóról a Memuna. Vétó/QA (HUM 14): ADV-1: DPO / jogi felelős (a HUM-PRIV-01 „Jóváhagyó” sora szerint), a szerepkiosztást az LMS-gazda rögzíti; ADV-4: DPO / jogi felelős, az M3-tételeknél a Memuna is; GYV-23: programvezető + Memuna, adatkör: DPO. A KANON:QA16-IMPL-2-nél vétó: DPO / jogi felelős. (Ledger: X-13.)

**Háttér:** a HUM:647 csak a beadásról szól; a döntési csomag kérdése (CSOMAG:452) mind a négy profilt felsorolja, a választott (c) opció (:454) nem szűkít profilra; a GATE-CP szó szerint nem beadás (MAN:25). A kánonból nem dönthető el. A QA16-IMPL-2 szerint az új RA 15-ös ASSIGN-tesztlépés csoportmódon alapuló szűrést vár, a build-spec viszont az Assignmentre nem ír elő csoportmódot (csak a TEXT-C-re).

**Kutatás (G4, G5, QA16):** Moodle 4.5 forráskód (`MOODLE_405_STABLE`): a H5P (`mod/h5pactivity/classes/local/manager.php`) és a kvíz (`mod/quiz/classes/local/reports/report_base.php`) „Separate groups” mellett, `moodle/site:accessallgroups` nélkül szűr. Az Assignmentnél (`mod/assign/gradingtable.php`, `lib/grouplib.php`) csoportba nem sorolt mentornál az aktív csoport 0, és a kutató extra ellenőrzést nem talált; óvatos következtetése, hogy ilyen mentor minden beadást láthat – ezt runtime-ban kell eldönteni. A `moodle/site:accessallgroups` a szerkesztő tanárnál alapból engedélyezett, a nem szerkesztőnél nem (https://docs.moodle.org/405/en/Capabilities/moodle/site:accessallgroups). A `mod/quiz:viewreports` RISK_PERSONAL, alapból teacher, editingteacher és manager szerepé (`mod/quiz/db/access.php`); a Responses report soronként mutatja a válaszokat (docs.moodle.org/405/en/Quiz_responses_report). Groups FAQ: https://docs.moodle.org/503/en/Groups_FAQ. Nem ellenőrzött: a dev „Groups access control” oldal elavult; az MDL-40367 JavaScript nélkül nem töltött be; az Assignment csoport nélküli viselkedését leíró fórumszálat a QA nem olvasta; az MDL-80501 és az MSA-24-0003 csak keresési összefoglalóból ismert (403). GDPR 25. cikk (2): másodlagos forrásból.

**Opciók (a):**
- (A) Mindhárom profilra, „Separate groups” csoportmóddal. Előny: a HUM-PRIV-01 legszűkebb hozzáférése, core-ban megvalósítható. Kockázat: a kétszemes rend miatt a második képzőnek csoporton kívüli hozzáférés kell.
- (B) Csak az ASSIGN-S/M-re, a döntés betűje szerint. Kockázat: a „Ki látja?” szövegnek ki kell mondania, hogy a kvíz- és a H5P-eredményt minden tanári szerep látja.
- (C) A H5P-C-re és a QUIZ-ra igen, a GATE-CP-re nem.
- QUIZ-D-re külön (G4): Moodle-alapérték csoportmóddal / activity-szintű role override (a `mod/quiz:viewreports` elvonása a nem szerkesztő tanártól; csoportszintű korrekcióhoz összesítés; egyéni utánkövetéshez a DPO jóváhagyása után dokumentált, ideiglenes override) / csak összesítés mindenkinek (runtime-kérdés, hogy a két riport szétválasztható-e).

**Opciók (b), QA16-IMPL-2:** „Separate groups” az Assignmenteken; a mentor a nem szerkesztő tanári szerepet csak csoportba sorolás után kapja (a TEXT-C BIZT-3 mintájára); a második értékelő és az F-peula képzője dokumentált, eljáráshoz kötött hozzáférést kap (ADV-2, újraértékelés). A QA ezt a hármat egy döntésként kéri; alternatívája az, hogy a mechanizmus rögzítetlen marad, és a teszt sikere „csak remény”.

**Opciók (c):** a bemenetek technikát nem részleteznek; az ADV-4 a döntést a visszaolvasás utánra halasztja (BK-05). Korlát: a SAFE-1 csomópontjai nem változnak; az önjelző kérdés nem törölhető, és nem köthető completionhöz.

**Javaslat és indoklás:** (a) az (A), a csoport nélküli mentorral mint negatív tesztesettel (G5); a QUIZ-D-n ennél szigorúbb, activity-szintű override (G4), mert a GYV-23 célhoz kötött válaszhozzáférést és DPO-jóváhagyást ír elő. A két ajánlás összefér. (b) a három elem együtt, a TEXT-C mintájára. (c) a BK-05 bizonyítéka után.

**Addig:** az ADV §3 „nincs rögzítve; nyitott: az ADV-1 kiterjedése (BIZT-5)” cellái, az ADV:109, a HUB:283 és az ADV:116 marad. Ez óvatos alapértelmezés, mert nem ígér szűkítést.

**Mit old fel:** KANON:QA14-BIZT-1, M0:QA14-BIZT-3, KANON:QA16-IMPL-2, valamint az M3:BIZT-G1-5 és az M3:BIZT-G2-7 döntési része.

**Elfogadás után:** az ADV §3 profilsorai és a mechanizmus-szakasz (125–130. sor), a MAN ASSIGN-S/M profilsora (19–20. sor), (B) esetén a tanulói „Ki látja?” szövegek; utána a role-matrix-teszt (BK-07).

**Már átvezetve:** a H5P-C, a QUIZ és a GATE-CP cella „nyitott: az ADV-1 kiterjedése” jelölése (`958bced`, `93da996`; verifier B1, QA16-IMPL-4); az RA 15. pont ASSIGN-S/M tesztlépése a csoport nélküli mentorral és a közvetlen URL-es negatív esettel (`958bced`, `93da996`; verifier B2, QA16-BIZT-3).

### D-12 – M0 belépőkvíz: „a két item nyilvános visszajelzése” (GYV-23)

**Mit kell eldönteni?** Tartalomszintű-e a GYV-23 „nyilvános visszajelzése” (a két biztonsági item helyes válasza és magyarázata mindenkinek), vagy személyhez kötött, csoport előtti visszajelzés?

**Ki dönt, ki ellenőriz:** programvezető + Memuna; adatkör: DPO. Vétó/QA (HUM 14, GYV-23): ugyanők.

**Mostani állapot:** a HUB:283 a döntés szó szerinti átvezetése. Sem a döntés, sem a csomag (CSOMAG:411) nem magyarázza a kifejezést.

**Opciók:**
- (1) A két item helyes válasza és magyarázata név és eredmény nélkül mindenkinek, szóban az M0.A-n vagy kurzusüzenetben. Előny: adatvédelmileg semleges.
- (2) A kvíz review-beállítása a beküldés után mindenkinek megmutatja a két item helyes válaszát és általános visszajelzését. Kockázat: build-spec és runtime-teszt kell.
- (3) Személyhez kötött, csoport előtti visszajelzés. Kockázat: ütközik a „nem megbélyegző” kikötéssel, egyéni eredményt tesz közzé.

**Javaslat és indoklás (G4):** az (1), szükség esetén a (2)-vel. Csak ez fér össze a csoportszintű, nem megbélyegző korrekcióval és a célhoz kötött hozzáféréssel.

**Addig:** a szó szerinti átvezetés marad; köztes átírás nincs (a korábbi verifier szerint).

**Mit old fel:** M0:QA14-NYELV-3. **Elfogadás után:** a HUB:283 pontosítása; (2) esetén a QUIZ-D review-beállítása a MAN-ban, runtime-teszttel (összefügg a D-11 QUIZ-D-részével).

### D-13 – Adatkör-besorolás: közös eszköz, cetlik, visszaazonosítható részlet, M2-jegyzet (ADV-11, ADV-7, GYV-21, ADV-1)

**Mit kell eldönteni?** Öt besorolási kérdés:
- (a) ADV-11: vonatkozik-e a közös eszköz-protokoll a nem F-peulás tartalék eszközre (M0.A:604, technikai segítségpont)?
- (b) ADV-7: személyes, önfeltáró cetli-e az M4.A:381 és az M4.B:332–333 fókuszmondat-kártyája?
- (c) ADV-7: csoportproduktum vagy önfeltáró cetli a Z.A:464–467 egyszavas szófelhő-cetlije, és mi a sorsa a peula után?
- (d) GYV-21: kerüljön-e az M2.A:177 és :410 csoportos normájába „és felismerhető részlettel sem”?
- (e) ADV-1 alkérdés: melyik megőrzési sor vonatkozik az M2 kapu identitás-jegyzetére (az LMS-M2-05-nek nincs saját §3-sora), és kell-e a „Név (vagy becenév)” mező (M2 KAPU:214)?

**Ki dönt, ki ellenőriz:** (a) projektgazda; (b), (c) DPO / jogi felelős, a (b)-nél Memuna-QA-val; (d) Memuna + DPO; (e) DPO / jogi felelős az LMS-gazdával. Vétó/QA (HUM 14): ADV-11: LMS-gazda és DPO; ADV-7: DPO / jogi felelős; GYV-21: Memuna + DPO; ADV-1: DPO / jogi felelős.

**Opciók és javaslat (G4, G5 kutató):**
- **(a)** minden közös vagy tartalék eszközre / csak az F-peulákra / az M0-ra külön szabály. **Javaslat:** minden eszközre. A döntés szövege nem szűkít; a javaslat „Lényeges eltérések” 5. pontja („ADV-11: közös eszközön inkább adatmentes működés az alap”) általános; a HUM:614 szerint eltérésnél a javaslat érvényes; az A11Y:57 is szűkítés nélkül vezeti át. A korábbi verifier mégis új alkalmazási esetnek minősítette, ezért döntés kell.
- **(b)** nem önfeltáró, marad / önfeltáró, a boríték- és faliopció kikerül / csak a résztvevőnél marad, a képző szóban összesít. **Javaslat:** nem önfeltáró: szakmai fejlődési szándék, nem az ADV §2:29 érzékeny kategóriája; az elhelyezés önkéntes és név nélküli; a csomag (a) opciója szerint a név nélküli lapokra az ADV §3:67 vonatkozik. A legóvatosabb a második opció lenne.
- **(c)** csoportproduktum, fizikai megőrzés a HUM-PRIV-02 szerint, az időt a DPO adja / csoportproduktum, a résztvevők elviszik a szavukat, vagy az ADV §3:67 szerint megsemmisül / önfeltáró, visszakerül, a felhőről nincs fotó. **Javaslat:** a második: a Z.A:40 már csoportproduktumnak tekinti, és nem keletkezik megőrzési idő nélküli papír.
- **(d)** mindkét helyre / csak a :410-be / marad. **Javaslat:** mindkét helyre: az M2.B:370 már ezt a mércét használja, és a GYV-21 első mondata a kis kvuca visszaazonosíthatóságára figyelmeztet. A Memuna-kivétel érintetlen.
- **(e)** +90 nap a Z.4 reflektív beadandó precedense szerint (ADV :65) / +12 hónap Assignmentként / a névmező törlése (adatminimalizálás; a fiók már azonosít). **Javaslat:** +90 nap és a névmező törlése.

**Addig:** minden hely marad. Az M0.A:604 a szigorúbb alap. A „nincs fotó”, a „Nevet ne írj rá” és a saját telefonra vonatkozó tilalom egyik opcióban sem gyengülhet. Megőrzési sort nem találgatunk.

**Mit old fel:** M0:QA14-BIZT-4, M4:QA14-BIZT-5, Z:QA14-BIZT-3, M2:QA14-BIZT-7, M2:BIZT-G1-6 (a megőrzési és a névmező-rész; a hozzáférési rész a BK-07-ben).

**Elfogadás után:** az M0.A:604, az M4.A:381–382, az M4.B:332–333, a Z.A:464–467, az M2.A:177 és :410, az ADV §3 új vagy pontosított sora, az M2 KAPU:214.

### D-14 – AI-út: metaadat-megőrzés és tanulói tájékoztató (ADV-12, GYV-10, LMS-8)

**Mit kell eldönteni?** (a) Mi az AI-végpont technikai metaadatának jogalapja és megőrzési ideje az ADV §3 táblában, és hogyan jelenik meg a szolgáltató naplója harmadik félként? (b) Kimondja-e az ADV §11:264 tanulói tájékoztatója, hogy az AI-segédet egyelőre a képző kezeli?

**Ki dönt, ki ellenőriz:** (a) DPO / jogi felelős (QA: programvezető); (b) programvezető + Moodle-adminisztrátor, vétó/QA: DPO / jogi felelős. Vétó/QA (HUM 14): ADV-12: DPO / jogi felelős (QA: programvezető, HUM-PRIV-04); GYV-10: Memuna + DPO / jogi felelős + programvezető; LMS-8: programvezető + Moodle-adminisztrátor, vétó/QA: DPO / jogi felelős.

**Kutatás (G5):** OpenAI, „Data controls in the OpenAI platform” (https://developers.openai.com/api/docs/guides/your-data): a visszaélés-figyelési naplók alapból legfeljebb 30 napig maradnak; a Responses API alkalmazásállapota alapból 30 nap, vagy ha `store=true`; a ZDR előzetes jóváhagyáshoz kötött. Következmény: `store=false` mellett is maradhat tartalom a szolgáltatói naplóban, ha nincs jóváhagyott ZDR – ez alátámasztja az ADV-12 „store=false önmagában nem bizonyít” mondatát.

**Opciók (a):** jogos érdek (üzembiztonság), rövid megőrzés, például legfeljebb 30 nap / Somer-oldalon nincs naplózás, csak a szolgáltatói napló, harmadik félként dokumentálva / inaktív marad a csatornafelmérésig. **Javaslat (G5):** most inaktív, utána jogos érdek DPO által rögzített időtartammal és ZDR-kérelemmel. A kutató átmeneti, időtartam nélküli pontját az ADV „Külön review” listájába a verifier (B3) ELVETETTE: nem szó szerinti átvezetés, új besorolást tesz (a GYV-10/LMS-8 alatt a promptot a képző küldi, nem igazolt, hogy ez tanulói adat), és a lezárt ADV-12-t nyitottnak mutatná.

**Opciók (b):** a §11:264 kiegészül az M7 lezárt formulájával („Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.” – M7.4:82, M7.2:69, :115) / marad. **Javaslat (G5):** a kiegészítés. A kutató ezt LEZÁRHATÓ-nak sorolta, a verifier (B4) ELVETETTE: az M7-formulát a korábbi verifier már figyelembe vette, a QA az M7-ben validálta, nem a DPO-kapus tájékoztatóban, és a kiegészítés eltérne a §7:194 kanonikus HUM-PRIV-04-es tanulói szövegétől. Elfogadás esetén a §7:194 is vele együtt igazodik.

**Addig:** az ADV §7:183 és §11:264 marad; az ADV §1 DPO-feltétele változatlan.

**Mit old fel:** KANON:QA14-BIZT-5, KANON:QA14-BIZT-3b (az (a) része MÁR RENDBEN: az ADV:247 megegyezik a §5:148-cal; a GYV-10/LMS-8 a specben bent van: ADV §7:183, RA 20. pont, MAN:120).

**Elfogadás után:** az ADV §3 új AI-sora (jogalap, időtartam, harmadik fél), illetve a §11:264 és a §7:194 összehangolt kiegészítése.

### D-15 – Build-spec és completion (ERT-9, ADV-3 / régi X-6, ERT-8, LMS-4, PRG-9 b, ADV-6)

**Mit kell eldönteni?** Hat beállítási kérdés, amelyekre a lezárt döntés nem ad értéket.

**Ki dönt, ki ellenőriz:** a döntéshozót részkérdésenként alább adjuk meg. Vétó/QA (HUM 14): ERT-9: projektgazda / build-spec gazda; ADV-3: projektgazda, vétó: DPO / jogi felelős; ERT-8: projektgazda, QA: értékelési felelős, programvezető, az adatkörről DPO; LMS-4: LMS-gazda + értékelési felelős; PRG-9 b): build-/LMS-gazda + M2 modulgazda (DPO nem kell); ADV-6: DPO / jogi felelős, a tájékoztató freeze-kivételéről a projektgazda.

- **(a) M3 kvíznyitás (ERT-9; KANON:QA14-ERT-2).** Hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy az LMS-M3-06 kapukvíz csak a megerősített rubrika után nyíljon? Dönt: projektgazda (build-spec gazda); QA: értékelési felelős. Opciók: új GATE-CP sor az Assignment-komponens megerősített rubrikájára, a kvíz határ nélküli Grade-feltétellel nyílik (precedens: LMS-M7-09, BSPEC-01) / határ nélküli Grade-feltétel közvetlenül az LMS-M3-05-re, a marking workflow „Released” állapotával (G3b-bizonyíték kell) / M3-kivétel „Receive a grade” completionnel (ellentmond az ERT-9-nek, formális eltérési döntés kell). **Javaslat (G6):** az első: determinisztikus, és nem kell kivétel. Forrás: docs.moodle.org/405/en/Activity_completion_settings, docs.moodle.org/405/en/Restrict_access_settings (Grade-feltétel: minimum, maximum, mindkettő vagy egyik sem).
- **(b) A Z.3 5. dia célmondata (ADV-3, régi X-6; KANON:QA14-IMPL-7b).** Kötelező tanuló-lokális vagy opcionális lépés? Dönt: projektgazda. Opciók: kötelező, tanuló-lokális (precedens: Z.1 SLIDE 5–6, Z.2 SLIDE 5–7, MAN:312), a Z.3:337 és a Z.4:207 változatlan / opcionális (az ADV-3 alapértelmezése és az „1–2” mikrocél mellette szól), de akkor a „mindkét célmondatod” fordulat két helyen igazítandó. **Javaslat (G6):** kötelező, tanuló-lokális: beviteli elem és completion nélkül nem jelent kikényszerítést.
- **(c) Az M4 rubrikaszint helye (ERT-8; M4:ERT-G2-4).** Dönt: projektgazda (build-spec gazda); a hozzáférésről a DPO. Opciók: rubrika az LMS-M4-05-ön (az M2 precedense, LMS-M2-05: a tanuló a szintleírást és a kommentet látja, pontot nem) / szöveges szint az LMS-M4-10 „Feedback comments” mezőjében. **Javaslat (G6):** az első: ugyanaz a minta, mint a másik puha kapunál, és a GATE-CP értéke tisztán CONFIRMED marad. A kutató az M4-fájlokat ebben a körben nem olvasta újra.
- **(d) Az LMS-M6-05 grade-beállítása (LMS-4; M6:IMPL-G1-7).** Dönt: LMS-gazda + értékelési felelős. Opciók: Point, Maximum grade = 15, „Calculate grade based on the rubric having a minimum score of 0” bekapcsolva – a Moodle-pont a nyers rubrikaösszeg (5–15), egyezik a RA:55 jelölésével / ugyanez kikapcsolva – csupa „Oké” = 7,5, félrevezető / bármelyik, de a pont rejtve a tanuló elől (az M2-sor mintája). **Javaslat (G8):** az első, rejtett ponttal. Forrás: docs.moodle.org/405/en/Rubrics (a FAQ szerint 0 pont nélküli szintnél a minimum-beállítást be kell kapcsolni). A KAPU:388 már kimondja, hogy a nyers pont nem kapudöntés.
- **(e) Az M2.1 SLIDE 4 helye és formája (PRG-9 b; M2:IMPL-G1-3).** Dönt: build-/LMS-gazda + M2 modulgazda. Opciók: a követett CP diáján interakció nélküli reflexió, „Check” nélkül, statikus visszajelzéssel (ez az RT-P0-14 tartalékútja is) / tartalombankos elem a CP leírásában / a mai, különálló, nem követett elem (a SLIDE 5 előtti tudatosítás kimarad). **Javaslat (G8):** az első: szó szerint „CP-ben integrált reflexió”, megőrzi a 3 → 4 → 5 sorrendet, és nincs mit tárolni; ára az elvesző interakció. A követés a RA 21. pont kánoni mondata szerint activity-szintű; a részkérdésenkénti rögzítést a kutató Moodle-forrással nem tudta igazolni.
- **(f) A fórum megnyitása futó kohorszban (ADV-6; M0:QA14-ERT-1).** Dönt: projektgazda (build-spec gazda) + LMS-gazda. Opciók: csak a megnyitás után induló kohorszban feltétel / visszamenőleges, türelmi idővel (hozzáférés-elvonás és adattörlés) / a fórum véglegesen opcionális (kötelező–opcionális váltás). **Javaslat (G5):** az első; zárt állapotban az activity ne készüljön el, vagy rejtett legyen úgy, hogy egyetlen feltétel sem hivatkozik rá. Forrás (Moodle 4.5): `availability/condition/completion/classes/condition.php` – a pillanatnyi completionből számol; `lang/en/completion.php` `err_settingslocked` (https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lang/en/completion.php) – kurzus-kritérium utólag csak a teljesítési adatok törlésével adható hozzá.

**Addig:** a MAN és a leckék érintett sorai maradnak; a nyitottság a legtöbb helyen jelölve van, ez óvatos alapértelmezés. A (c)-nél a hely nincs dokumentálva; az (e)-nél a mai, nem követett elem az adatvédelmileg óvatos állapot.

**Mit old fel:** KANON:QA14-ERT-2, KANON:QA14-IMPL-7b, M4:ERT-G2-4, M6:IMPL-G1-7, M2:IMPL-G1-3, M0:QA14-ERT-1.

**Elfogadás után:** a MAN érintett sorai (LMS-M3-05/06/07, LMS-Z-03, LMS-M4-05, LMS-M6-05 a MAN:91-ben, az M2.1 SLIDE 4 sora, LMS-M0-05) és a leckék build-specje; utána runtime-bizonyíték: RT-P0-01 (RA 8. pont), RT-P0-21 (RA 21. pont), és az (a) részkérdés marking workflow-s opciójánál G3b (BK-13).

### D-16 – Z.4 záró reflexió: „Teljesítve”, passz, „kiürítés” (ERT-38, ERT-3)

**Mit kell eldönteni?** (a) Mi a „Teljesítve” alsó határa: mindhárom szakaszban értelmezhető tartalom, vagy a beadás egészének értelmezhetősége? (b) Hogyan jelzi a tanuló a passzt, és mi a mentor első lépése üres szakasznál? (c) Mit jelent az ERT-3 „kiürítés” szava?

**Ki dönt, ki ellenőriz:** (a) értékelési felelős; (b) értékelési felelős a DPO-val; (c) projektgazda build-spec gazdaként, QA: értékelési felelős. Vétó/QA (HUM 14): ERT-38: értékelési felelős, vétó/QA: programvezető; ERT-3: projektgazda (QUIZ-D, build-spec), értékelési felelős (Z.4), vétó/QA: DPO + programvezető (Z.4).

**Opciók és javaslat (G6 kutató):**
- **(a)** (i) mindhárom szakaszban (az érzékeny rész passzolható): a Completion rule (Z.4:343) és a MAN:112 marad, a Z célzott QA-riport három cseréje átvehető; mellette szól az M2/M4 precedens. (ii) a beadás egésze: a Z.4:343 zárójele és a MAN:112 „előírt mezőiben” fordulata módosul. **Javaslat:** (ii). A döntés a háromrészes szerkezetet formatív útmutatónak mondja; ugyanezt ígéri a tanulónak látható Z.4:98 és :329; az átadás tartalmát pedig a Z.3 LMS-Z-07 már mentori elfogadással méri.
- **(b)** opcionális „passz” jelölés a szakaszcím alatt, és üres szakasznál a mentor első lépése a rákérdezés vagy a Z.4:167 szerinti általánosított változat felajánlása / nincs jelölés, a :355 („Még nem teljesítve” + kiegészítés kérése) marad. **Javaslat:** az első, az (a)-val együtt döntve; a (ii) olvasatban a kérdés nagyrészt tárgytalan.
- **(c)** (1) az üres beküldés negatív tesztje: a Required 1. kérdés üresen vagy „Not selected”-del nem küldhető be, completion nem áll be; (2) törlési teszt (egyedi törlés vagy kurzus-reset). **Javaslat:** az (1) az ERT-3 alá; a (2) külön megőrzési tétel, a gazdája a DPO. Források (Moodle 4.5): `mod/feedback/item/multichoicerated/lib.php` – Required elemnél üres érték hibát ad (stagingben igazolandó); docs.moodle.org/405/en/Viewing_Feedback_responses; a kurzus-reset a `feedback_delete_all_completeds`-et hívja (`mod/feedback/lib.php`). Időzített 90 napos törlést a core Feedbackben a kutató nem talált; ez következtetés.

**Addig:** a Z.4:98, :329, :343, :347, :353, :355, a Z hub :185, a MAN:112 és az RA 16. pont nyitott zárójele marad, nyelvi alapon sem írható át. A mostani kettősség nem óvatos alapértelmezés, de a feloldása küszöbdöntés.

**Mit old fel:** Z:QA14-NYELV-1, Z:ERT-G1-1, Z:QA14-ERT-2, Z:QA14-IMPL-3.

**Elfogadás után:** a Z.4 Completion rule és tanulói mondatai, a Z hub :185, a MAN:112 (LMS-Z-08), az RA 16. pont tesztje.

### D-17 – Rubrikahorgonyok és kalibrációs mondatok (ERT-26, ERT-42, ERT-43, ADV-5 R1)

**Mit kell eldönteni?** (a) Az M5 R3-nál a „soronként látható módszertani indok” Alapszint- vagy csak Erős szintű követelmény? (b) Hogyan válik ketté az M7 R8 (pedagógiai minőség és adatszivárgás)? (c) Mi az M7 R1 2-es szintjének új horgonya? (d) Kiterjed-e az ADV-5 „válasz nélküli” útja a v2 R1 2-es szintjére?

**Ki dönt, ki ellenőriz:** értékelési felelős + projektgazda (rubrikaszint); az ERT-42-nél a DPO; az ERT-43 szövegét az értékelési felelős írja, a projektgazda hagyja jóvá. Vétó/QA (HUM 14): ERT-26: értékelési felelős + projektgazda, QA: módszertani lektor; ERT-42: értékelési felelős + DPO, QA: DPO + programvezető; ERT-43: értékelési felelős, QA: módszertani lektor; ADV-5: DPO / jogi felelős, someres vonatkozásban a projektgazda (QA: helyi ideológiai felelős, HUM-SOMER-01).

**Opciók és javaslat:**
- **(a) M5 KAPU:286, :294 (M5:QA14-ERT-1, G6):** kalibrációs mondat a KAPU:286 után, szintváltozás nélkül (Alapszinten az illeszkedés felismerhető, a kifejezett „miért” az Erős szint) / átmenéshez minden sorba indokmondat (lécemelés, ütközik a CSOMAG:963 következményével) / nincs mondat. **Javaslat:** az első: megtartja a szinteket, a küszöböt és az R4 státuszát, és nem teremt rejtett bukási feltételt.
- **(b) M7 KAPU:360 R8 (M7:BIZT-G1-1, G9):** (A) az R8 csak pedagógiai (saját hang, AI-másolat), mellette külön, nem pontozott „adatvédelmi stop”: azonosítható harmadik személyes adatnál a beadás pontszámtól függetlenül javításra megy vissza, DPO-folyamat szerint, eltávolítással; (B) az R8 0-s szintje blokkoló (két konstruktumot kever); (C) marad. **Javaslat:** (A). Nyitott részkérdés: a javító leadás ne fogyassza a javító próbálkozást, mert jogorvoslat, nem teljesítménybukás. Hogy egy beadott hanih-név incidens-e, az DPO-értékelés. A GDPR 4. cikk 12. pontját, 5. cikk (1) c) pontját és 33. cikk (1) bekezdését (https://eur-lex.europa.eu/eli/reg/2016/679/oj) a kutató élőben nem ellenőrizte.
- **(c) M7 KAPU:279 R1 (M7:PED-G1-1, G9):** (A) „legalább egy ellenőrizhető jel vagy kimenet”, az időkeret önmagában nem elég; (B) „jel ÉS időkeret” (túlmegy a döntésen); (C) marad. **Javaslat:** (A). Csak előzetes, egyértelmű tanulói tájékoztatóval és projektgazdai jóváhagyással lép hatályba; egy menetben a Q3 visszajelzésével (KAPU:93) és az M7.1:316–320-szal (ezeket a kutató nem olvasta újra).
- **(d) ADV-5 a v2 R1-nél (M7:BIZT-G1-6 (b), G5):** az R1 marad, mert a semleges vagy kitalált someres érték teljesíti, és ezt a KAPU:408 kimondja / az R1 2-es szintje elfogadja a megnevezés nélküli, a kvuca helyzetéhez kötött relevanciát / az értékkötés kikerül az R1-ből. **Javaslat:** az első, a (c)-vel egy menetben.

**Addig:** a rubrikák változatlanok; ez óvatos (nincs rejtett bukási feltétel). Az R8 gyermekvédelmi ága érintetlen.

**Mit old fel:** M5:QA14-ERT-1, M7:BIZT-G1-1, M7:PED-G1-1, M7:BIZT-G1-6 (a (b) rész).

**Elfogadás után:** az M5 KAPU:286 utáni kalibrációs mondat; az M7 KAPU R8 és R1 horgonya, a Q3 visszajelzése, az M7.1 és a tanulói tájékoztató; az ADV-ben az adatvédelmi stop eljárása.

**Már átvezetve:** az M7:BIZT-G1-6 (a) része: a semleges vagy kitalált érték mondata az M7.1:236-ban és az M7.4:488-ban, az LMS-M7-10 teljes ADV-5-átvezetése gazdával, és az LMS-M7-10 felvétele az RR G2 nyitott DPO-listájára (`958bced`, `93da996`). A verifier (B5) ezt RÉSZBEN fogadta el, mert az RR-kiegészítést akkor nem ellenőrizte; a QA16-BIZT-2 után került be. A (c) rész bizonyíték-kapu (BK-11).

### D-18 – Item- és kulcsdöntések (ERT-23, ERT-28, ERT-30, PRG-15)

**Mit kell eldönteni?** Négy item kulcsa vagy opciószövege, amelyet a lezárt döntés csak szerzői vagy értékelői jóváhagyással enged változtatni.

**Ki dönt, ki ellenőriz:** (a) értékelési felelős + M3 modulgazda; (b) M5 szerzője + értékelési felelős; (c) értékelési felelős + modulgazda; (d) szakmai lektor / M5 szerzője. Vétó/QA (HUM 14): ERT-23: értékelési felelős + M3 modulgazda; ERT-28: M5 szerzője + értékelési felelős; ERT-30: értékelési felelős + modulgazda; PRG-15 b): M5 szerzője / modulgazda.

**Opciók és javaslat (G6, G9 kutató):**
- **(a) M3.2:658–664 kulcsa (ERT-23; M3:IMPL-G2-14).** Opciók: itemenkénti validálás a kutató javaslata szerint / a mai egyetlen kulcs marad minden itemnél, „iránymutató” visszajelzéssel. **Javaslat:** az 1., 4. és 7. item egyetlen kulccsal marad (erős fejlődési, illetve szó szerinti „idősebb” jel); a 2. és 5. (bekiabálás, egymás szavába vágás) csoportdinamikai jel, ezért a Kivsza és a Leviatán is elfogadható; a 3. és 6. az M3.2 korosztálytérképe alapján döntendő (ezt a kutató nem ellenőrizte).
- **(b) M5.2 SLIDE 8 ✅ (ERT-28; M5:ERT-G1-9).** Valódi itemdöntés: a döntés sorrendje (feladat–kvuca–módszer–cél) eltér a tanított lánctól (feladat → cél → kvuca → módszer, MAN:80), a KAPU:312 pedig harmadik megfogalmazást hordoz. Opciók: a ✅ a tanított láncot követi, a döntés négy elemét meglétként olvassuk / a ✅ a döntés sorrendjét követi (nem tanított utat kulcsolna) / új item a `/course-develop` csomagban (ledger: X-8). **Javaslat:** az első; utána a HUB:207 és a KAPU:312 igazodik. A kutató az M5.2 SLIDE 7–8 mostani szövegét nem olvasta be (a ✅ a CSOMAG:977 idézete).
- **(c) M5 KAPU:269 C opciója (ERT-30; M5:NYELV-G1-11).** Opciók: első személyű „mi”-alak, a kvuca marad a felidézés ágense / a plan-M5 változata, amely ágenst vált („felidéztetem velük”). **Javaslat:** a „mi”-alak: azonos nézőpont az A és D opcióval, és nem ütközik a :274 indokkal és a :277 visszajelzéssel.
- **(d) M5.1 SLIDE 4 1. és 4. helyzete (PRG-15; M5:PED-G1-3).** Opciók: a kulcs marad, a két helyzet szövege egyértelműen formálissá válik (tanóra, tanterv, jegy) / a kulcs nonformálisra vált, a visszajelzés a :369-re hivatkozik / mindkét válasz elfogadott, határeset-visszajelzéssel. **Javaslat:** az első: a bevezető besorolás célja a tiszta elkülönítés, a határeset az M5.A élő vitájába való. Források, élőben nem ellenőrizve: a Tanács 2012. december 20-i ajánlása (2012/C 398/01, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32012H1222(01)) és az UNESCO ISCED 2011; ezek szerint a két mostani helyzet inkább nonformális, a mostani kulcs vitatható.

**Addig:** minden kulcs és opció marad; az M3.2 és az M5.1 formatív elem, kapuhatás nélkül.

**Mit old fel:** M3:IMPL-G2-14, M5:ERT-G1-9, M5:NYELV-G1-11, M5:PED-G1-3. **Elfogadás után:** az érintett itemek kulcsa, opciószövege és visszajelzése; látható szöveg, ezért pin kell; a ✅ változása vétólistás.

### D-19 – Kimeneti célok illesztése (TERM-7, PRG-2, ADV-3 / régi X-10, ADV-5)

**Mit kell eldönteni?** Három kimeneti cél többet ígér, mint amit a lecke vagy a kapu mér. Szűkül-e a cél, vagy új mérési elem kell?

**Ki dönt, ki ellenőriz:** (a) modulgazda + értékelési felelős, a célkitűzésről a projektgazda; (b) modulgazda vagy projektgazda; (c) projektgazda + értékelési felelős, someres QA: helyi ideológiai felelős (HUM-SOMER-01). Vétó/QA (HUM 14): TERM-7: projektgazda, QA: helyi ideológiai felelős és DPO (M2), értékelési felelős (M5); PRG-2: projektgazda (célkitűzés) a modulgazdával, QA: értékelési felelős; ADV-3: projektgazda, vétó: DPO / jogi felelős; ADV-5: DPO / jogi felelős, someres vonatkozásban a projektgazda.

**Opciók és javaslat:**
- **(a) M5 hub :18, :32, :33 (M5:PED-G1-10, G9).** Opciók: formatív demonstráció egy meglévő élő lépésben (M5.B 4.3.2 vagy M5.F 4.3.0; az M5.B 4.3 viszont már túlfut) / a cél szűkítése az „elmagyarázza” helyett „felismeri és alkalmazza” irányba. **Javaslat:** a szűkítés: idő nincs rá, és a PRG-2 is a szűkítést preferálja; a kapura nincs hatása. A Program terv és a MAN tükörszövegét a kutató nem ellenőrizte.
- **(b) M4.1 ILO 2 (M4:ERT-G1-10, G6).** Opciók: „felismeri” szűkítés / gyakoroltatott, nem mért cél marad / új, mért produktív elem (tárolt adatkör, DPO kell). **Javaslat:** a „felismeri”: a cél azt állítja, amit a lecke ténylegesen mér (SLIDE 3–4 Single Choice). Addig az ILO túlígér, ez nem óvatos alapértelmezés.
- **(c) M2 HUB:34 (M2:QA14-ERT-2, G6).** Opciók: a kimeneti cél a saját vagy egy kitalált madrih példáját is engedi / marad. **Javaslat:** a betoldás: cél és értékelés nem válik szét, az R3 szintjei és a küszöb nem változnak. A KAPU:239 sablonsora vele mozog. A kutató a HUB:34-et nem olvasta újra (a verifier idézete).

**Addig:** változatlan.

**Mit old fel:** M5:PED-G1-10, M4:ERT-G1-10, M2:QA14-ERT-2. **Elfogadás után:** az M5 hub :18, :32, :33, az M4.1:12 és :19, az M2 hub :34 és a KAPU:239 (build úton); a PT és a MAN tükörszövegei.

### D-20 – PRG-1: tételes vágási tervek

**Mit kell eldönteni?** Modulonként mely lépések rövidülnek, hogy a 45’ és a blokkhatárok tarthatók legyenek, védett biztonsági, reflexiós és kötelező feldolgozó lépés rövidítése nélkül? Az M5.1-nél: a 9–13 percre összegződő részidők újrabecslése vagy a 15–20 perces metaszám visszaigazítása?

**Ki dönt, ki ellenőriz:** az adott modulgazda, az M3.B-nél a Memunával; vétó/QA: programvezető. Vétó/QA (HUM 14, PRG-1): az elvet a programvezető (HUM-OPS-01 jóváhagyó és vétó/QA); a vágási tervet az adott modulgazda (M3.B-nél a Memuna bevonásával), vétó/QA: programvezető.

**Miért nem zárható le:** a döntés lépésszintű percet nem ad, a percek pedig vétólistás időtartamok.

**Opciók:** (a) a G9 kutató modulonkénti vágási javaslata kiindulópontként; (b) a modulgazda saját terve. Az M5.1-nél: (A) a részidők újrabecslése 2–3 15–17 éves próbaolvasóval a kész H5P-vázlaton, a metaszám marad, ha belefér; (B) a metaszám visszaigazítása, ekkor a HUB:7 és a 3,5 órás terhelés (HUM-OPS-01) is átszámolandó.

**Javaslat (G9), modulonként röviden:**
- **M0.A:** a Blokk 2 és 3 a meglévő sávon belül, előre kijelölt csoportokkal, rövidebb plakát- és körbenézési lépéssel; a 45’-es változat külön tervvel. A „Kihez fordulhatok?” és a „Madrih, nem terapeuta” lépés védett.
- **M2.A, M2.B, M2.F:** a Blokk 3 15’-re (a rajzolás csak frissítés, ha az M2.1-es térkép megvan); a 4.4.1 nagykör rövidítése csak a modulgazda megerősítésével; az M2.B záró üzenete a vállalás-kör része; az M2.F-en a technikai belépés érkezéskor.
- **M3.A, M3.B, M3.F:** a csoportalakítás és a bemutatás rövidül; az M3.B a Memunával, a 4.3.3 időszelep (D-03); a hamis M3.A:309 mondatot a tervvel együtt kell javítani; az M3.F lépéslistáját a kutató nem olvasta.
- **M4.A, M4.B:** a 4.3–4.5 a sávon belül; 16 fő fölött a triádút az alap. Az M4.B:326 két mondata kötelező tartalom marad, az idő csak az összevonást engedi; a szerzői szándékot meg kell erősíteni (M4:NYELV-G2-6).
- **M5.A, M5.B, M5.F, M5.1:** létszámfüggő bemutatás; az M5.B :326 „5 perces” és „1 percben” fordulata közül választani kell; az M5.1-nél az (A).
- **M6.A:** a 4.2–4.4 rövidítése, a 4.3.2/B érintetlen. A páros és a nagykör összevonása védett lépést érint, ezért kifejezetten modulgazdai döntés programvezetői vétóval.
- **M7.A, M7.B, M7.F:** alapból két önkéntes; az AI-tipp csak akkor, ha marad idő (az opcionális státusz és a nem-AI út nem változik); a belépés érkezéskor.

**Addig:** minden percszám és az M3.A:309, az M7.A:403, az M7.B:540, az M4.A:254 mondata marad. Ez nem óvatos alapértelmezés: a túlfutás a terepen a zárókört szorítaná ki. A kutató több lépéslistát nem olvasott vissza (M2.A Blokk 2, M3.F, M4.B 4.3, M6.F 4.3, M5.A/M5.B belső percei, M7.B Blokk 4); ezeket a modulgazdának kell pótolnia.

**Mit old fel:** M0:PED-5, M2:PED-G3-1, M3:PED-G3-1, M4:PED-G2-2, M4:NYELV-G2-6, M5:PED-G2-6, M5:QA-PED-2, M6:PED-G3-1, M7:PED-G3-1.

**Elfogadás után:** a peulák percbontása és a kapcsolódó mondatok modulonként, a jóváhagyott terv szerint; látható szöveg, ezért pin kell. Már rendben: az M0.A:153–157 45’-es címkéi; az M7:NYELV-G3-14 (5.1).

### D-21 – PRG-5: 1–5 fős F-peula-változat és kapacitás

**Mit kell eldönteni?** Milyen formában készüljön az 1–5 főre előre leírt, azonos kompetenciát fejlesztő F-peula-változat, és ki rögzíti a kapacitást és a pótlási felelőst?

**Ki dönt, ki ellenőriz:** a változatot a modulgazda írja a PRG-4 `/course-develop` csomagban (csak a felhasználó indíthatja, a tervet a projektgazda hagyja jóvá; ledger: X-8); az 1:1 kérdésben a Memuna; a kapacitásról a programvezető. Vétó/QA (HUM 14, PRG-5): programvezető + értékelési felelős (HUM 8–9 vétó/QA); a változat szövege: modulgazda; 1:1: Memuna.

**Opciók:**
- (a) F-peulánként külön kis létszámú változat. Előny: modulhoz szabott. Kockázat: többszörös szerzői munka, redundancia.
- (b) Egy közös, programszintű „kis létszámú F-peula” keret, amelyre minden kötelező F-peula hivatkozik, modulspecifikus tartalmi betéttel. Előny: egy szerzői kör, a döntést ugyanúgy teljesíti.

**Javaslat (G9):** a (b).

**Addig:** az M3.F:24 „6–20 fő” sora marad; kitalált változat nem kerül be. Kiskorúval 1:1 csak a HUM-SAFE-02 szerint.

**Mit old fel:** M3:ERT-G3-10. **Elfogadás után:** új keret a PRG-4 csomagban, a kötelező F-peulák hivatkozása; a programvezető kapacitás- és felelős-bejegyzése.

**Már átvezetve:** a PRG-5 hiányzási mondata az M6.F-ben és az M7.F-ben (`958bced`; verifier B6); az M1.F, az M3.F és az M5.F már tartalmazta.

### D-22 – M7.B „átjárás” szándéka (PRG-16)

**Mit kell eldönteni?** Mit jelent az M7.B:434 „Van-e átjárás másik térbe?” kérdése és a MUNK-01 spec :292 „átjárás” szava az „Idő & helyszín” sorban?

**Ki dönt, ki ellenőriz:** az M7 modulgazdája. Vétó/QA (HUM 14, PRG-16): az adott modulgazda.

**Háttér:** a PRG-16 részvételi vagy álláspontváltási instrukcióként olvasta, de ez az „Idő & helyszín” sorba nem illik, ezért új alkalmazási eset. A döntési csomag (CSOMAG:1588) csak a szándékot kérdezte.

**Opciók:** (a) logisztikai olvasat: kell-e közben átvonulni egy másik helyszínre, és hogyan oldják meg; (b) mások áthaladása a téren; (c) a döntés részvételi olvasata, amely a sarokjátékhoz tartozna, nem ide.

**Javaslat (G9):** az (a), mert logisztikai és felügyeleti pont, és illik a sorba.

**Addig:** marad; biztonsági szempontból nem félrevezető.

**Mit old fel:** M7:NYELV-G3-12. **Elfogadás után:** az M7.B:434 és a :292 `@asset` spec; build és pin kell.

### D-23 – ERT-5 D1/D2: az M7 kapukvíz Review options ablakmátrixa és zárási mechanizmusa

**Mit kell eldönteni?** D1: hogyan lássa a tanuló az első próbálkozás után a hibázott kompetenciát vagy kritikus követelményt kulcsszivárgás nélkül? D2: milyen mechanizmus biztosítja, hogy az „After the quiz is closed” ablak a javítási úton lévő tanulónál ne kezdődjön a javító határideje előtt?

**Ki dönt, ki ellenőriz:** build-spec gazda (LMS-gazda) + értékelési felelős; a dátumoknál a programvezető (HUM-OPS-01). Vétó/QA (HUM 14, ERT-5): értékelési felelős; kritikus slotnál és a kulcs megjelenítésénél a Memuna is (M3). Az ERT-40 kérdéstípusánál a plugin az LMS-gazdáé (régi X-11). (Ledger: X-12.)

**Opciók D1:**
- (a) Mentoron keresztül: az első három ablakban „The attempt” = No, a tanuló csak a „Marks” értéket (opcionálisan az Overall feedbacket) látja; a hibázott kompetenciát a kijelölt mentor a megerősítéskor a GATE-CP visszajelzés-mezőjébe írja (LMS-M7-09, az M3-nál LMS-M3-07), a kulcs nélkül. Előny: nincs szivárgás, meglévő kánoni csatorna (MAN:25; M7.F:26, :144). Kockázat: nem azonnali.
- (b) Automatikusan, itemszinten: „The attempt” + „Marks” = Yes, „Whether correct” = No. Csak akkor, ha a Q11/Q14 a célverzión validált minden-vagy-semmi kérdéstípussal épül (ERT-40); részpontos Multi-Select-nél az itemenkénti részpont részleges kulcs-információt ad.
- (c) „Whether correct” = Yes: kizárva, mert a Q11/Q14-nél bizonyos válaszmintákban a teljes kulcsot mutatja.

**Opciók D2:**
- (1) Nincs kvízszintű zárás (az M0 mintája, MAN:271); a javítóhoz készülő felhasználói felülbírálás zárási ideje a javító határideje. Előny: ha a beállítás elmarad, a kulcs soha nem jelenik meg (biztonságos irányú hiba), és a sikeresen teljesítők sem adhatják tovább.
- (2) Kvízszintű zárás `M7_V2_DUE`-ra, és minden nem teljesítő tanuló a zárás előtt felülbírálást kap. Kockázat: a felülbírálás az F-peula után készül (M7.F:399), a megerősítés a zárás után is jöhet (MAN:103) – közben a tanuló „After close” állapotban látja a kulcsot.
- (3) A kulcs egyik ablakban sem jelenik meg automatikusan; a javító után a mentor beszéli át az itemeket.

**Javaslat és indoklás (G7 kutató):** D1-nél most az (a), mert ez az óvatos út; a (b) az ERT-40 kérdéstípusának és a runtime-tesztnek az igazolása után jöhet szóba. D2-nél az (1); ha kötelező kvízzárás kell, a (3). Indoklás és források: 6. szakasz.

**Amit a verifier részben fogadott el:** a kutató LEZÁRHATÓ-javaslatából a verifier (A7) csak az általános visszajelzés elrejtését fogadta el; az ablakmátrixot, az „After close” invariánst és az RA 19. pont új alpontját D1/D2 döntésnek minősítette, mert összefonódnak, és a kutató a Moodle-viselkedést forráskódból következtette, célverzión nem igazolta.

**Addig:** a hibázott kompetencia megjelenítésének módja nincs rögzítve; ez nem óvatos alapértelmezés. A kutató átmeneti mondatot is javasolt (a D1 (a) mint alapértelmezés a KAPU:51 és a QUIZ-M végére); ez tanulói élményt érint, ezért nem került be.

**Mit old fel:** az ERT-5 maradéka (ledger: M7:G7-ERT5-2). Utána bizonyíték: BK-10. **Elfogadás után:** a KAPU:51, :415, a MAN:18 (QUIZ-M) és a MAN:102 (LMS-M7-07) kiegészítése a választott ablakmátrixszal, és az RA 19. pont új alpontja a G7 tesztterve szerint.

---

## 3. Bizonyíték-kapuk

Ezek nem nyitott döntések: a lezárt döntés tartalma adott, a megnevezett szerep írásos bizonyítéka vagy a runtime-teszt hiányzik. A G-kapuk a `02 Tervezet/RELEASE-READINESS.md` G1–G8 sorai. A bizonyítékot nem a repó állítja elő: a futás egyiket sem gyártotta és nem következtette ki.

| ID | Tétel | Kulcsok | Kinek a bizonyítéka | G-kapu | Meglévő óvatos alapértelmezés |
|---|---|---|---|---|---|
| BK-01 | Memuna-verdikt: az M3.4 SLIDE 4 és 6 érzékeny gyakorlat-e, és a „kötelező tanulási lépés” engedjen-e passzt; a GYV-6 küszöbének jóváhagyása az M4-ben; a megválaszolatlan interakció negatív tesztje (RA 9. pont) (verifier C1) | M3:PED-G2-1, M4:BIZT-G2-10, M4:BIZT-G2-9 (küszöb-QA) | Memuna (GYV-24); LMS-gazda | G1 (FINAL_RELEASE_QA); G3b | Az M3.4:12 és :63 passza, az ERT-1 szerinti completion; az M4.B:63 „bárki bármikor megállhat és passzolhat”; a GK §4:63–64 minimuma. Ha a Memuna alternatív feladatot vagy körönkénti passz-bejelentést kér, a tétel újranyílik (az M4.B:326 mondata akkor a 4.1, 4.2 és 4.4/1 instrukciójába kerül). |
| BK-02 | Az M5.3 adatminimalista útjának completion-profilja, mindkét úton tesztelve (verifier C2) | M5:IMPL-G2-2 | LMS-gazda + módszertani lektor / tananyagfelelős | G3b (RA 4. pont) | M5.3:529, :531, :544; MAN:85: „a végleges completiont a valós H5P és ennek a sornak a tesztje dönti el”. A h5p-course-presentation `cp.js` szerint feladatelem nélküli CP-nek nincs összefoglaló diája (https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/src/scripts/cp.js). |
| BK-03 | A tárolt TEXT-C adatkörének DPO-aláírása (LMS-M4-06, LMS-M4-08) (verifier C3) | M4:BIZT-G1-2 | DPO / jogi felelős (ADV-E1) | G2 | A tárolt út marad; a tanulói ígéret igaz (M4.1:1206, M4.3:650). A narrációs maradék: KF-01. |
| BK-04 | JOG-1: a Gyvt. 17. § címzettjeinek, határidőinek és a (4b) alkalmazhatóságának jogászi ellenőrzése; Memuna-jóváhagyás; a kijelölt felnőtt megnevezése (szervezeti aktus) (verifier C4) | M3:BIZT-G1-8 | jogi szakértő (írásban), Memuna; a szervezet | G1 | Hub :41 Btk.-mondata, :42 JOG-1 hozzáadó mondata a jogászi tagmondattal; a korpuszban nincs „munkanap”-határidő. A Gyvt.-t a G2 kutató másodlagos forrásból (net.jogtar.hu), összegző eszközön át olvasta; a szó szerinti idézeteket átvétel előtt az njt.hu-n újra kell olvasni. A nyilvántartási hely: D-06. |
| BK-05 | ADV-4: a H5P saved-state, xAPI/LRS, próbálkozás-riport és jogosultságok visszaolvasása a célverzión (verifier C5: RÉSZBEN) | M3:BIZT-G1-5, M3:BIZT-G2-7 | LMS-gazda (RT-2, RA 15. pont, ADV-E1) | G3b | M3.4:95: „nem pontozott, nem completion-elem, és lehetőleg nem rögzül”; a SAFE-1 csomópontjai változatlanok. A visszaolvasás után valódi technikaválasztás jön (D-11 (c)). |
| BK-06 | ADV-2 / ADV-10: az F-peula szereposztásának, a vészhozzáférésnek és a szervezeti Google-fióknak a dokumentálása; a Memuna szerepének megerősítése; DPO G2; csoport-hozzáférési teszt (verifier C6) | M3:BIZT-G2-5, M3:BIZT-G3-8 | programvezető; Memuna; DPO (ADV-E1, ADV-E2); LMS-gazda (RT-P0-15, RA 15. pont) | G2; G3b | M3.4:67, M3.F:3, :184; M3.4:772 (ADV-10). A „hozzáférhet-e nem mentor képző” kérdésre az ADV-2 felel; tartalmi döntés nem marad. |
| BK-07 | ADV-1: staging role-matrix, a mentor-láthatóság tesztje tesztfiókkal (verifier C7) | M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6 (hozzáférési rész) | LMS-gazda; DPO | G2 (POST-BUILD), RT-P0-15 | M1.4:510, M2.2:499, M2 KAPU:203: „technikai okból a Moodle rendszergazdája is hozzáférhet”; az RA 15. pont ASSIGN-tesztlépése (`958bced`, `93da996`). A teszt után a „csak a kijelölt mentorod” fordulat a tényleges szerepekhez igazodik (közvetlen következmény). A mechanizmus: D-11 (b). |
| BK-08 | LMS-7: a PT :221 rövid altja és a látható kísérőszöveg együtt teljes értékű-e az M7.2 diagramjánál (verifier C8) | M7:IMPL-G2-12 | hozzáférhetőségi gazda (HUM-A11Y-01) | G5a/G5b (FINAL_RELEASE_QA) | A részletes alt marad (M7.2:401–406); a (b)–(d) alt kész. |
| BK-09 | PRG-14 a): itemenkénti írásos provenance-nyilatkozat az AI-eredetről az M4.2–M4.4 tételeinél (verifier C9) | M4:BIZT-G1-7 | szerző / tananyagfelelős; média esetén a médiafelelős | nincs saját G-sor; a legközelebbi a G2 (tracker #2) | Feltételes ígéret (M4.3:22, M4.2:23, M4.4:29, hub :16, M4.A:14, M4.B:14), címke nincs. A nyilatkozat után a PT:224 szerinti sor csak a megnevezett itemekhez kerül ki. |
| BK-10 | ERT-5: a Review options ablakmátrix célverziós visszaolvasása; a Q11/Q14 kérdéstípusa (ERT-40) | ERT-5 (ledger: M7:G7-ERT5-3) | LMS-gazda / TEST_OWNER | G3b (RT-P0-19, RT-P0-08) | Az általános visszajelzés is rejtve a javító lezárásáig (`3b160fc`). A tesztlépés a D-23 előtt nem írható be. Részletek: 6. szakasz. |
| BK-11 | ADV-5: a GDPR 9. cikk szerinti minősítés és kivétel az M7.1 SMART cél R eleménél (LMS-M7-10) | M7:BIZT-G1-6 ((c) rész) | DPO / jogi felelős; someres vonatkozásban a projektgazda | G2 (FINAL_RELEASE_QA) | A semleges, kitalált vagy kihagyható út (`958bced`); az LMS-M7-10 az RR G2 nyitott DPO-listáján (`93da996`). |
| BK-12 | PRG-12: Memuna-review az M3.B 4. esetkártyájának konkrét forgatókönyvére | (a D-03-hoz kapcsolódik) | Memuna | G1 | A 4. kártya előre megírt fiktív eset; rögtönzött valós történet nincs. |
| BK-13 | Döntés utáni bizonyítékok: RA 8. pont / RT-P0-01 (D-15 d); RA 21. pont / RT-P0-21 (D-15 e); RA 16. pont (D-16 c); a `showContentTitle` stagingben (D-08 b); G3b a marking workflow-s útnál, ha azt választják (D-15 a); SIG-2: a kalibráció és a kétszemes döntési rend (D-07 a; KAPU-M3:317); a GYV-1 Memuna- és DPO-QA-ja (D-09); a GYV-4 (c) alkérdése (D-04 e) | – | LMS-gazda; értékelési felelős; Memuna; DPO | G3b; G1; G2; SIGNOFF | A döntésig a csomagokban leírt átmeneti állapot. |

---

## 4. Külső függőségek

### KF-01 – VO fix pack (verifier C11)

**Mi hiányzik:** a kurzusoldali szöveg kész; a régi mondat csak a narráció `@source` blokkjaiban maradt, ezért csak hanggyártási fix packkel változhat (VO-1).
- M1.3:901 (M1.3-NAR-05-VO): a „Gondolj egy helyzetre, ami eszedbe jut” fordulat valós helyzetre is biztat, és ütközik az ERT-12-vel. Javasolt irány (G8): csak a kitalált, egyszerű történetre biztató mondat.
- M4.1:1199 (M4.1-NAR-07-VO) és M4.3:644 (M4.3-NAR-03-VO): a „magadnak” szó ellentmond a tárolt TEXT-C igaz tanulói ígéretének (ADV-3). Javasolt irány (G8): a „magadnak” elhagyása.
- Kapcsolódó: az M6.2:631–632 (M6.2-NAR-05-VO) narrációja a GYV-18 előtti kérdést mondja; forrása a már átvezetett M6.2:606 diaszöveg (G3).

**Ki viszi:** a VO-gazda / médiafelelős (a hanggyártás), DPO-vétóval (ERT-12, ADV-3). A VO-1 szerint a kimondott szöveget módosító blokkot újra kell renderelni és meg kell hallgatni; a kurzusoldali alkalmazást a felhasználó kéri, fix packként.

**Állapot:** a `@source`-ból épülő leirat a pack beérkezéséig a régi mondatot mutatja, ezért ez nyitott release-blokkoló, nem FIXED. A RR-ben nincs külön VO-sor. Kulcsok: M1:QA14-BIZT-1, M4:QA14-BIZT-4 (és az M4:BIZT-G1-2, az M6:QA14-BIZT-3 narrációs része).

### KF-02 – SIGNOFF: az ERT-19 hatálybalépése (verifier C10)

**Mi hiányzik:** az ERT-19 tartalma eldőlt („az „ÉN” a középpont, a „legalább 3 kör” … három további réteg”). A hatálybalépés feltétele a modulgazda / értékelési felelős aláírása és az előzetes tanulói tájékoztató; meglévő beadást visszamenőleg nem büntetünk. Az M2 KAPU:37 ma is a régi, enyhébb szöveget hordozza.

**Ki:** modulgazda + értékelési felelős. Vétó/QA (HUM 14, ERT-19): értékelési felelős. Ez SIGNOFF, nem G1–G8-kapu; elutasításnál a tétel újranyílik.

**Elfogadás után:** egy menetben átvezethető a plan-M2:319–321 listája szerint (az A.1 példájából kikerül az ÉN; az R1 három kört kér az ÉN-en kívül; a D-sablonban az ÉN a középpont; a HUB:25 és az M2.1:477 egyeztetése). Kulcs: M2:PED-G1-11.

---

## 5. Már rendben, illetve már implementálva

### 5.1 Már rendben, nincs teendő

- **M3:QA14-BIZT-1 (GYV-15).** A GYV-15 döntési kérdése (CSOMAG:337) név szerint megnevezi az S3-SAFE dobozt (a régi :705, ma M3.3:554), és ez az önsértés-szcenárióban áll (SLIDE 5, „Vágásnyomok”, :545). A :554 ma a GYV-15 formuláját hordozza. A KAPU ITEM 9 („otthon bántják”) bántalmazási eset, a GYV-15 „önsértési eseteknél” hatókörén kívül esik, ezért a változatlansága a döntéssel összhangban van. A G2 kutató a sorszám-eltolódást git-history nélkül következtette ki; a verifier (B8) a helyeket visszaolvasva MEGERŐSÍTETTE. A lecke és a kapu egységesítése opcionális, új alkalmazás volna (Memuna, jogász); nem blokkol.
- **M7:NYELV-G3-14 (PRG-1).** Az M7.A (:65 = :385) és az M7.B (:500, :524) rendben. Az M7.F :95 nyitókérdése és :104 blokkcíme közti eltérés mind a hét F-peula közös sablonja: közös blokkcím („Hol tartok, miben kérek segítséget?”), modulonkénti nyitókérdés (M1.F–M6.F ellenőrizve). A verifier (B9) MEGERŐSÍTETTE; a validált finding M7.F-javaslata eleve használhatatlan volt.
- **Részben rendben:** a KANON:QA14-BIZT-3b (a) része (D-14); az M6:QA14-BIZT-5b objektív része (D-02); az M4:BIZT-G2-9 GYV-6-része (M4.A:58, M4.B:63, M4.F:80; D-01, BK-01).

### 5.2 Ebben a futásban implementálva (nem javasoljuk újra)

- **Teljesen lezárt kulcsok:**
  - M2:QA14-BIZT-3 (GYV-19): M2.A:362 „azonnal szólj a kijelölt úton a képzőnek és a Memunának.” (`3b160fc`; verifier A4 pontosított szövege; QA15: 0 finding).
  - M3:QA14-IMPL-1, M3:IMPL-G2-2 (LMS-2, M3.4-rész): a Drag & Drop mellékút kivezetése, a `tools/test_media_manifest.py` párcseréje, a legacy-diszpozíció (`3b160fc`, média `4b188cc`); az EGY-04 metaadata (`11a89b4`, média `87c08c1`; QA15-IMPL-1). Verifier A1.
  - M7:QA14-ERT-1b (ERT-40): M7 KAPU:53 (`3b160fc`; verifier A6 pontosított szövege); a :48 és :217 már rendben volt.
- **Részben implementált kulcsok (a többi rész nyitott):** M6:QA14-BIZT-4 (D-01), M1:QA14-BIZT-5 (D-10), M3:BIZT-G1-8 (D-06, BK-04), KANON:QA14-BIZT-1 (D-11), M1:BIZT-G2-4 és M2:BIZT-G2-3 (BK-07), M7:BIZT-G1-6 (D-17, BK-11), M3:ERT-G3-10 (D-21), ERT-5 (D-23, BK-10, 6. szakasz).
- **Nem blokkoló megfigyelések az LMS-2 körül (G8, QA15):** az M3.1 Drag & Drop-ja marad, mert az LMS-2 nem nevezi meg; az A11Y:34 modulon belüli konzisztencia-szabálya miatt a hozzáférhetőségi gazda nézze meg. A `02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md` darabszámai (420/913) eltérnek a generált tervtől (a kutatáskor 416 asset; a `87c08c1` buildje után 415 asset és 902 deliverable, mert az M3.4-EGY-03 kikerült); ezt a kánoni kör igazítsa. Ugyanott a HUM-SAFE-04 blokk még az M3.4-EGY-03-at nevezi; ez datált nyilvántartás, történetileg pontos.

---

## 6. Az M7 kapukvíz válaszszivárgása (ERT-5)

**A kockázat (G7 kutató, verifier A7).**
- Mind a 14 M7-item 4 opciós (A–D); a Q11 és a Q14 Multi-Select (3/4 helyes), a többi Single Choice. Minden itemnek egyetlen, itemszintű „Visszajelzés” bekezdése van, amely Moodle-ben General feedback lesz, és **kimondja a kulcsot** (például Q1, KAPU:72; a Q7 a három disztraktort név szerint kizárja). Opciónkénti visszajelzés (Specific feedback) egyik itemnél sincs.
- A régi szabályszöveg (KAPU:51, :415; MAN:18 QUIZ-M; MAN:102 LMS-M7-07) a nem létező opciónkénti visszajelzést tiltotta a javító lezárásáig, a ténylegesen kulcsot közlő általános visszajelzést nem. Egyik szöveg sem mondta meg, melyik Moodle-időablakban mi legyen beállítva. Az RA-ban nem volt ERT-5-tesztlépés.
- **A Review options kvízszintű, nem próbálkozásonkénti.** A `mod/quiz/mod_form.php` a visszanézési mezőket kvízszinten tárolja; a felülbírálási űrlap (`mod/quiz/classes/form/edit_override_form.php`) csak csoportot, felhasználót, jelszót, nyitást, zárást, időkorlátot és próbálkozásszámot kezel; a Quiz FAQ szerint a felülbírálás dátumot, időt és próbálkozásszámot változtat. Az „Immediately after the attempt” (a beküldés utáni 2 perc) és a „Later, while the quiz is still open” ablak beállítása ezért mindkét próbálkozás után ugyanaz.
- **Csak az „After the quiz is closed” választja szét a próbálkozásokat**, mert ezt a tanulóra érvényes, felülbírálással módosítható zárási idő indítja (`mod/quiz/classes/quiz_attempt.php`: `quiz_update_effective_access`; `mod/quiz/locallib.php`: `AFTER_CLOSE`). Csapda: ha a kvízszintű zárás `M7_V2_DUE`, és a felülbírálás csak az F-peula után készül el (M7.F:399), a bukott tanuló addig „After close” állapotban van, és látja a kulcsot.
- **A Multi-Select „Whether correct” és „Marks” részleges kulcs-információt adhat.** A `question/type/multichoice/renderer.php` a megjelölt opciókat egyenként helyesnek vagy hibásnak jelöli; ha a tanuló mind a négyet bejelölte, a teljes kulcsot látja. Részpontos Multi-Select-nél az itemenkénti „Marks” és a saját jelölés együtt részleges opció-következtetést enged (G7; a QA15 implementációs lencse ugyanezt jelezte a MoodleDocs „Whether correct” és „Marks” leírása alapján). Az Overall feedback sávos, a Q13-at név szerint nem tudja megnevezni.
- A `moodle/grade:viewhidden` jogú felhasználókra (tipikusan tanárok, adminisztrátorok) a Review options nem vonatkozik, ezért a tesztet tisztán tanulói fiókkal kell végezni.

Források, ahogy a G7 kutató megadta: Quiz settings, MoodleDocs 4.5 (https://docs.moodle.org/405/en/Quiz_settings) és 5.0 (https://docs.moodle.org/500/en/Quiz_settings); Quiz FAQ, MoodleDocs 4.5 (https://docs.moodle.org/405/en/Quiz_FAQ); `MOODLE_405_STABLE` forrás: `mod/quiz/locallib.php`, `mod/quiz/classes/quiz_attempt.php` (és `MOODLE_500_STABLE`), `mod/quiz/mod_form.php`, `mod/quiz/classes/form/edit_override_form.php`, `question/type/multichoice/renderer.php` (a raw.githubusercontent.com/moodle/moodle útvonalain). Hogy a felülbírálásban megadott zárási idő kvízszintű zárás nélkül is „After close” állapotot ad, azt a kutató forráskódból következtette; célverzión igazolni kell.

**Mi lett javítva.** A `3b160fc` mind a négy helyen kimondja, hogy az itemenkénti tanulói (általános) visszajelzés is rejtve marad a javító próbálkozás lezárásáig (KAPU:51, :415; MAN:18 QUIZ-M; MAN:102 LMS-M7-07); a `11a89b4` a MAN:102 cellájában a „látszik” igével választja el a látható és a rejtett elemeket (QA15-ERT-1). Ez szó szerint egyezik az M3 KAPU:35-tel, ezért az M3-on nem változtat; az M3 itemjei egyválaszosak, ott a „Whether correct” nem árulja el a kulcsot. A QA15 implementációs lencse szerint a szöveg nem ellentmondásos, és kulcsot nem árul el. Nem változott: kulcs, ✅, küszöb, próbálkozásszám, completion, rubrikaszint, kötelező–opcionális besorolás. Ledger: M7:G7-ERT5-1 FIXED.

**Mi maradt D1/D2 döntésnek (D-23).** A konkrét ablakmátrix (mely elem melyik ablakban Yes vagy No), az „After close” invariáns (a javítási úton lévő tanulónál nem kezdődhet a javító határideje előtt) és az RA 19. pont új alpontja. A verifier (A7) szerint ezek a D1-gyel (hogyan látszik a hibázott kompetencia; „The attempt” be vagy ki) és a D2-vel (zárási mechanizmus) összefonódnak, ezért build-spec döntések; a tesztlépés tartalma a mátrixtól függ.

**Milyen runtime-bizonyíték kell (BK-10).** RT-P0-19 (az RA 19. pont új alpontja a D-23 után) és RT-P0-08 (a Q11/Q14 kérdéstípusa, ERT-40); G3b; felelős a TEST_OWNER / LMS-gazda. A `RUNTIME_VERIFIED` állapotot csak dátummal és verzióval rögzített tényleges teszt adhatja. A G7 kutató tesztterve, javaslatként:
- tisztán tanulói szerepű tesztfiók;
- negatív esetek: az első próbálkozáson nem teljesítő fiók a beküldés után 2 percen belül, 2 perc után, egy esetleges kvízszintű zárás elmúltával (a felülbírálás előtt és után), valamint a javító beküldése után, a javító határideje előtt sem lát helyes választ, általános visszajelzést, opciószintű vagy összesítő visszajelzést, a Q11/Q14-nél opciónkénti helyes/hibás jelölést sem;
- pozitív esetek: az első próbálkozás után a pontszám és a hibázott kompetencia a választott úton látszik; a javító határideje után az „After close” ablakra beállított elemek megjelennek;
- pozitív kontroll egy tesztkvízen, ahol a „Right answer” és a „General feedback” az első ablakban Yes; enélkül a negatív eset nem bizonyító;
- a beállítás-mátrixot a Moodle- és a kérdéstípus-verzióval együtt kell rögzíteni, és változáskor meg kell ismételni.

**Megfigyelés az értékelési felelősnek:** ha a képző kézzel egy harmadik próbálkozást nyit, az már a kulcs felfedése után fut; ezt az ERT-5 nem szabályozza.

---

## 7. Lefedettségi lista

A `groups.json` minden `keys` és `old` kulcsa (93 kulcs), valamint a futásban keletkezett további kulcsok. Formátum: kulcs → csomag vagy szakasz.

**G1 – Peula-biztonsági keret: megállítási protokoll, létszám, kiskorúak (GYV-5, GYV-6, GYV-17, PRG-12)**

- M0:QA14-BIZT-2 → D-01
- M2:QA14-BIZT-2 → D-01
- M6:QA14-BIZT-4 → D-01 (kísérő javítás: 5.2)
- M6:QA14-BIZT-5b → D-02
- M3:QA14-NYELV-13 → D-03; BK-12
- M2:BIZT-G3-2 → D-01
- M4:BIZT-G2-9 → D-01 (besorolás); BK-01 (GYV-6 küszöb-QA)

**G2 – Eszkalációs út, küszöb és címzett (GYV-4, GYV-7, GYV-8, GYV-14, GYV-15, GYV-19, JOG-1)**

- M6:QA14-BIZT-1 → D-04
- M6:QA14-BIZT-2 → D-04
- M7:QA14-BIZT-6 → D-04
- Z:QA14-BIZT-2 → D-04
- M2:QA14-BIZT-3 → 5.2 (implementálva)
- M4:QA14-BIZT-3 → D-04
- M3:QA14-BIZT-1 → 5.1 (már rendben)
- M0:BIZT-5 → D-04
- M6:BIZT-G1-1 → D-04
- M3:BIZT-G2-2 → D-05
- M3:BIZT-G1-8 → D-06 (nyilvántartási hely); BK-04 (jogász, Memuna)

**G3 – Gyermekvédelmi tartalmú értékelés (ERT-21, GYV-1, GYV-2, GYV-6, GYV-9, GYV-18)**

- M3:QA14-BIZT-2 → D-07
- M2:QA14-BIZT-5 → D-09
- M2:QA14-BIZT-4 → D-08
- M6:QA14-BIZT-3 → D-07; KF-01 (narráció)
- M3:IMPL-G2-5 → D-08
- M3:PED-G2-1 → BK-01
- M4:BIZT-G2-10 → BK-01
- M7:BIZT-G1-2 → D-07
- M7:PED-G2-4 → D-07

**G4 – Tanulói adatok: láthatóság, megőrzés, önfeltárás, közös eszköz (GYV-11, GYV-21, GYV-23, ADV-2, ADV-4, ADV-7, ADV-10, ADV-11)**

- M0:QA14-BIZT-3 → D-11
- M0:QA14-NYELV-3 → D-12
- M0:QA14-BIZT-4 → D-13
- M1:QA14-BIZT-5 → D-10 (alpont: 5.2)
- Z:QA14-BIZT-1 → D-10
- KANON:QA14-BIZT-4 → D-10
- M4:QA14-BIZT-5 → D-13
- Z:QA14-BIZT-3 → D-13
- M2:QA14-BIZT-7 → D-13
- Z:BIZT-G1-2 → D-10
- M3:BIZT-G1-5 → BK-05; D-11 (technikaválasztás)
- M3:BIZT-G2-7 → BK-05; D-11 (technikaválasztás)
- M3:BIZT-G2-5 → BK-06
- M3:BIZT-G3-8 → BK-06

**G5 – Hozzáférési modell, AI-út, fórum (ADV-1, ADV-5, ADV-6, ADV-12, GYV-10, LMS-8)**

- KANON:QA14-BIZT-1 → D-11
- KANON:QA14-BIZT-5 → D-14
- KANON:QA14-BIZT-3b → D-14 ((a) rész: 5.1)
- M0:QA14-ERT-1 → D-15
- M1:BIZT-G2-4 → BK-07
- M2:BIZT-G1-6 → BK-07 (hozzáférés); D-13 (megőrzés, névmező)
- M2:BIZT-G2-3 → BK-07
- M7:BIZT-G1-6 → D-17 ((b) rész); BK-11 ((c) rész); (a) rész: 5.2

**G6 – Értékelés és build-spec (ERT-3, ERT-8, ERT-9, ERT-26, ERT-28, ERT-38, ERT-40, ADV-3, ADV-5)**

- M5:QA14-ERT-1 → D-17
- M7:QA14-ERT-1b → 5.2 (implementálva)
- Z:QA14-NYELV-1 → D-16
- Z:QA14-ERT-2 → D-16
- Z:QA14-IMPL-3 → D-16
- KANON:QA14-ERT-2 → D-15
- KANON:QA14-IMPL-7b → D-15
- M2:QA14-ERT-2 → D-19
- Z:ERT-G1-1 → D-16
- M5:ERT-G1-9 → D-18
- M4:BIZT-G1-2 → BK-03; KF-01 (narráció)
- M4:ERT-G1-10 → D-19
- M4:ERT-G2-4 → D-15

**G7 – Az M7 kapukvíz visszajelzéseinek válaszszivárgása (ERT-5; ERT-40, ERT-41):** a `groups.json`-ban nincs kulcs; a futás ledgerében az M7:G7-ERT5-1…3 kulcs áll (lent); az ERT-5 a D-23-ban, a BK-10-ben és a 6. szakaszban.

**G8 – Részleges LMS-/build-átvezetések és VO-tételek (LMS-2, LMS-3, LMS-4, LMS-7, PRG-9, PRG-14, VO-1, ERT-12)**

- M3:QA14-IMPL-1 → 5.2 (implementálva)
- M1:QA14-BIZT-1 → KF-01
- M4:QA14-BIZT-4 → KF-01
- M3:IMPL-G2-2 → 5.2 (implementálva)
- M5:IMPL-G2-2 → BK-02
- M6:IMPL-G1-7 → D-15; BK-13 (RT-P0-01)
- M7:IMPL-G2-12 → BK-08
- M2:IMPL-G1-3 → D-15; BK-13 (RT-P0-21)
- M4:BIZT-G1-7 → BK-09

**G9 – Részleges program- és értékelési átvezetések (PRG-1, PRG-2, PRG-5, PRG-11, PRG-15, PRG-16, TERM-7, ERT-19, ERT-23, ERT-30, ERT-32, ERT-42, ERT-43)**

- M0:PED-5 → D-20
- M2:PED-G3-1 → D-20
- M3:PED-G3-1 → D-20
- M4:NYELV-G2-6 → D-20
- M4:PED-G2-2 → D-20
- M5:PED-G2-6 → D-20
- M5:QA-PED-2 → D-20
- M6:PED-G3-1 → D-20
- M7:NYELV-G3-14 → 5.1 (már rendben)
- M7:PED-G3-1 → D-20
- M3:ERT-G3-10 → D-21 (hiányzási mondat: 5.2)
- M3:IMPL-G3-9 → D-03
- M5:PED-G1-3 → D-18
- M7:NYELV-G3-12 → D-22
- M5:PED-G1-10 → D-19
- M2:PED-G1-11 → KF-02 (SIGNOFF)
- M3:IMPL-G2-14 → D-18
- M5:NYELV-G1-11 → D-18
- M6:ERT-G1-2 → D-07
- M6:ERT-G3-4 → D-07
- M7:BIZT-G1-1 → D-17
- M7:PED-G1-1 → D-17

**A futásban keletkezett további kulcsok**

- KANON:QA16-IMPL-2 → D-11
- M7:G7-ERT5-1 → 6. szakasz (implementálva)
- M7:G7-ERT5-2 → D-23
- M7:G7-ERT5-3 → BK-10

**Besorolatlan kulcs:** nincs.
