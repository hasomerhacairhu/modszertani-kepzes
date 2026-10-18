# Forrás-hibaregiszter – builder-bizonyíték és célzott QA (AP-2026-10-18-01)

> **Audit trail, nem kánon.** Egyetlen, deduplikált regiszter: a builder (heymarcell/mk-coursebuild `bd00920`) forrásra
> vonatkozó tételei a kurzusforrás jelenlegi állapotával egybevetve, valamint a blokkoló-diff célzott QA-ja. A nyers
> kivonatok: `2026-10-18 Builder-bizonyíték – nyers kivonatok, AP-2026-10-18-01.md` (A–D); a QA-tételek tömörített szövege
> ugyanott, az F. szakaszban. Bázis: `c354f17` + HUM 20. szakasz (`f96ce43`). Javító commitok: `709423b` (M5–M7 blokkolók),
> `73f30ca` (M0, HUM 20), `b2c0c6d` (manifest, runtime acceptance), `139bc24` (egyéb tanulói szöveg + pin), `62eb098`
> (média). Ez a regiszter nem runtime-, szerepköri vagy release-bizonyíték.
>
> **Osztályok:** JAVÍTVA (objektív, a forrásban bizonyítva javítva) · MÁR JAVÍTVA (a hiba a bázisban sincs meg) ·
> NEM HIBA / ELAVULT · DUPLIKÁTUM · MOODLE-ONLY (a forrás helyes, build-oldali) · EMBERI DÖNTÉS (mit, kitől) ·
> BIZONYÍTÉK-KAPU (szerep, G-kapu) · BUILD-SPEC NYITOTT (BSPEC, javaslattal).

## A. A négy forrás-blokkolt activity

| Activity | Ami blokkolt (builder) | Állapot | Mit oldott fel a javítás | Ami nyitva marad | Commit |
|---|---|---|---|---|---|
| **LMS-M5-01** (M5.1) | M51-A SLIDE 2 kulcs hiányzik; M51-B visszajelzés-sablon; M51-C completion-sor | **JAVÍTVA** | A) Suli, B) Somer, C) hétköznapok – az M5.A kulcsolt párhuzamai (≈:248–250) és szabálya (:266) szerint; a B-helyzet a madrih szerepét kimondja (az M5.A kártyájával egyezően); válaszonkénti, a kulcsnak megfelelő visszajelzés, amely kimondja, hogy nem a helyszín dönt, és hogy a puszta videónézés még nem tanulás; meta completion-sor (ERT-1, HUM 20 szűkítésével); SLIDE 4 5. helyzet szára és indoklása igazítva. QA: assessment-reviewer (kulcs egyértelmű), pedagogy-, Hungarian-reviewer | M51-D: a SLIDE 4 1. és 4. helyzetének visszajelzése (PRG-15 b: szakmai lektor); QA-PED-3: az S2 B és az S4 5. helyzetének hasonlósága (módszertani lektor) | `709423b` |
| **LMS-M5-05** (M5.4) | M55-A feladatleírás hiányzik; M55-B/C pontleképezés, Grade type, Max grade; M55-D értékelői szöveg az R4 cellában | **JAVÍTVA** (leírás, R4-cella) + **BUILD-SPEC NYITOTT** (számok) | M5.4 4.1 teljes tanulói feladatleírás (feladat, mezők, minimum, mintasor, gyakori hiba, leadás, akadálymentes út, határidő, adatkezelési tájékoztató a §3 mátrix szerint, értékelési szempontok, kapuszabály, javítási út, újraértékelés, továbblépés); 4.2 beállítások; az M5 KAPU R4 Alapszint és Erős cellájából az értékelői útmutatás a kalibrációs mintamondatok közé került, a szint jelentése nem változott | BSPEC-08 (`PROPOSED`: 1/2/3, max. 12, lockzeropoints, szintpont rejtve; döntés: értékelési felelős + LMS-gazda; a végső pont rejtése: projektgazda, vétó DPO + jogi); BSPEC-09 (beküldésgomb) | `709423b`, `b2c0c6d` |
| **LMS-M6-05** (M6 Játéklap) | M65-A tanulói feladatleírás hiányzik | **JAVÍTVA** | M6 KAPU (E1) teljes leírás az M6.B-MUNK-01 rovatai és a (B) rubrika „Oké”-ellenőrzőlistája szerint (egyéni beadás, eszköztípus, cél, kvuca, menet, biztonság, inkluzivitás, variációk, „még nem elég / már jó” példák, leadási utak, határidő, kapuszabály, a blokkoló sorok döntéshozója, javítási út); (E2) beállítások; a rubrika, a pont (15) és a rejtés változatlan | BSPEC-09; a „pontszámot nem” tagmondat az X-16 visszaellenőrzésétől függ (QA-IMPL-3, RT-P0-28) | `709423b` |
| **LMS-M7-06** (Peula v2) | M76-A tanulói leírás hiányzik; M76-B v2-sablon mezőlistája (IMPL-18-1) | **JAVÍTVA** | M7 KAPU (D1) teljes leírás (v1 ↔ v2 különbség, portfólió-átkötés, adatkezelési tájékoztató, öt fő rész + két kísérő mező, a 11 pont és a 3–4 részletes pont, R4 0. szintje tanulói nyelven, öt checklist-terület mint nem külön kapu, AI-út és no-AI egyenértékűség, nyitási feltételek, ≥17/24 + R1/R4/R5/R6, javítási út); (D2) egyetlen sablon-specifikáció és `M7-HUB-MUNK-02` asset; (D3) beállítások; a mezőlistát a projektgazda 2026-10-18-i utasítása alapján ez a szakasz rögzíti (vétó/QA: értékelési felelős) | QA-PED-1 b: a sablon és a leírás elérhetősége a nyitás előtt (LMS-gazda + értékelési felelős); BSPEC-09; Memuna írásos átnézése az M7 gyermekvédelmi részeire (X-1) | `709423b` |

## B. Completion és mastery (builder: completion-register, D2, CB-C-0036)

| ID | Hely | Hiba | Osztály | Döntés / alap | Commit |
|---|---|---|---|---|---|
| CB-C-0036 / HUM 20 | M0.1 :10, :13, intro; M0.2 :10, :13, :56, :514; M0 hub :70, :79, :169; MAN LMS-M0-01, -02, új LMS-M0-07, §4 M0; RA 9, új 31. pont, RT-P0-31 | a lezárt döntés nem volt átvezetve | **JAVÍTVA** | HUM 20. szakasz (D-039, D-040); a kérdések, opciók, kulcs és visszajelzés szövege változatlan | `73f30ca`, `b2c0c6d` |
| CB-C-0036 nyitott oszlop | M0.1 S4 passzválasz; M0.2 SLIDE 4 teljesítés utáni elérhetősége (M02-P); M0 hub belépőkvíz „lásd: M0.2, 2./4. dia” | szerzői / Memuna / DPO jóváhagyás | **EMBERI DÖNTÉS** + **BIZONYÍTÉK-KAPU** | a passzválasz a projektgazda szövegjavaslata (D-041 §4), szerzői jóváhagyásig valódi tanulóval nem használható; M02-P: szerző + Memuna; DPO: Feedback- és Lesson-válaszok | — |
| CB-C-0018 (P0) | MAN §1 GATE-CP; RA 8 | bukott kapu is teljesíthette a kurzust | **JAVÍTVA** | elsődleges forrás: `MOODLE_405_STABLE`/`500_STABLE` `completion/classes/api.php` 154–156; vétólista | `b2c0c6d` |
| QA-IMPL-1 (P1) | MAN §4; RA 8 | javító próbálkozás megnyitása visszazárta volna a megnyílt tartalmat | **JAVÍTVA** | RA 19 kánoni tartalékszabálya; `mod/assign/locallib.php` `update_grade()`; vétólista | `b2c0c6d` |
| CB-C-0017 / -0029 | MAN §1 ASSIGN-S; HUM:455 | az automatikus újranyitás leadás-completiont visszaállít | **EMBERI DÖNTÉS** | projektgazda: újranyitási mód (Manual / untilpass / elfogadás); az LMS-M7-07 is az LMS-M7-05 SUBMITTED-hez kötött | — |
| CB-C-0024 | Z.2, Z.3, M2.4, M5.3 | nulla pontos H5P-sorok | **MÁR JAVÍTVA** (forrás); runtime: RA 9 | — | bázis |
| CB-C-0025 | IB-k | IB az első oldalon teljesít | **MOODLE-ONLY** | a kánon CP-t ír; konverzió leckénként projektgazdai döntés (HUM 20) | — |
| CB-C-0026 | M0.2 / egyoldalas H5P | üres ellenőrzés válasznak számít | M0.2-rész **DUPLIKÁTUM** (= CB-C-0036); többi **MOODLE-ONLY** | — | — |
| D2 osztott leckék | M0.3, M1.2, M1.3, M3.1, M3.2, M3.4, M7.1, M7.2, M7.4 | builder-konstrukció (több könyv) | CP-ként **MOODLE-ONLY**; M1.2 :34, M1.3 :80 ↔ ERT-1: **EMBERI DÖNTÉS** (projektgazda: D-046 kánonba vétele vagy a mondat átírása); M3.4 S4 státusza: szerző + Memuna | ERT-1, HUM 20 („Más lecke konverziója ebből nem következik”) | — |
| Véleményválasztók „minden válasz helyes” | M3.1 :108, :539; M3.2 :102, :522; M3.4 :83, :87, :164; M7.1 :304; M7.2 :295 | pontozott vélemény (ADV-4, RA 14) | **EMBERI DÖNTÉS** (build-spec gazda: technika; DPO, ha tárolt) | LMS-6/D-i precedens: interakció nélküli lista | — |
| M7.4 SLIDE 3 | M7.4 :455 | „minden opció helyes” MC, ellentmond a saját SLIDE 4 LMS-6 megjegyzésének | **JAVÍTVA** | LMS-6, ADV-4, ERT-2 | `709423b` |
| LMS-Z-02, -Z-03 | MAN :111, :112 | feladatelem nélküli CP | **EMBERI DÖNTÉS** (build-spec gazda: completion-alap) | MAN §1 tartalékklauzula | — |
| LMS-M5-07 | MAN :89 | végleges profil | **BIZONYÍTÉK-KAPU** (LMS-3, RA 4) | — | — |
| LMS-M0-06 (B5) | MAN :47 | üres próbálkozás teljesít | **EMBERI DÖNTÉS** (projektgazda: B5-opció) + runtime | — | — |
| QUIZ-M M3 review | M3 KAPU | M3 Review-options mátrix hiányzik | **EMBERI DÖNTÉS** (build-spec gazda + értékelési felelős, a D-23 mintájára) | ERT-5 | — |

## C. Tanulói szöveg, értékelés, nyelv (CB-C és review-package)

| ID | Hely | Hiba | Osztály | Commit |
|---|---|---|---|---|
| CB-C-0016 | M2 KAPU :178, :266; M2 hub :221 | a formatív küszöb „elfogadva” | **JAVÍTVA** | `139bc24` |
| CB-C-0035 | M7.3 | ígért munkalap asset nélkül | **JAVÍTVA** (M7.3-MUNK-01) | `139bc24`, `62eb098` |
| CB-C-0035 / A8 VO | M7.3 :796 „Moodle Checklistben” | narráció; újrarenderelés kell | **EMBERI DÖNTÉS** (VO fix pack, X-6): „…a Zmán Kvucá-checklist munkalapján…” | — |
| CB-C-0012 | Z.4 :384 | modullista forrása | **JAVÍTVA** (az M0.1 SLIDE 5 listája); a Likert-horgonyok: **EMBERI DÖNTÉS** (szerző) | `139bc24` |
| CB-C-0004 | MAN §5 | MCP-képességmátrix elavult (Core 1.0 → v1.3.0) | **NYITOTT, objektív** (P2; a builder adataival javítható) | — |
| CB-C-0034 | MAN :54, :72, :90, :97, :109 | `GATE_CONFIRMED_Mx` a névben | **NYITOTT, objektív** (egy MAN-mondat); a tanulói leírások: forrás-szerzés | — |
| CB-C-0033 | Glosszárium :26, :34, :168, fájltérkép | belső metaadat a tanulói oldalon | **NYITOTT** (megjelenítési szabály; a :168-nál Memuna-QA) | — |
| CB-C-0007, -0009, -0020, -0021, -0027, -0032 | Z.4; M0.1; M0.2; X-16 | DPO-, szerzői, Memuna-, X-16-tételek | **EMBERI DÖNTÉS / BIZONYÍTÉK-KAPU** (a sor szerinti szerep) | — |
| CB-C-0001, -0002, -0008, -0011, -0022, -0023, -0029, -0030, -0031 | — | — | **NEM HIBA / DUPLIKÁTUM / ELAVULT** (builder-verifier elvetette) | — |
| CB-C-0010, -0013, -0014, -0015 | M3 KAPU; Z.4; M0.4; M1.4 | — | **MÁR JAVÍTVA** | bázis |
| CB-C-0019 | M0.1 S5 | „1–2” ↔ „max. 2–3” | **EMBERI DÖNTÉS** (PRG-17: pilot-visszajelzéssel; X-9) | — |
| CB-C-0028 | M1.1 :80 | Lesson-konstrukciótól függ | **MOODLE-ONLY** (kánon: CP) | — |
| A1 húzás | M4.2 :623; M4.3 :427, :444 | csak a húzásos útnak volt instrukciója | **JAVÍTVA** | `139bc24` |
| A3 | M3.4 :444 | „Sorold be” rádiógombnál | **JAVÍTVA** | `139bc24` |
| A4 | M1.3 :885 | „írd le magadnak” ↔ „szövegmezőbe írd be” | **JAVÍTVA** | `139bc24` |
| A5 | M0.2 :369, :464 | „ne írj ide” mező nélkül | **JAVÍTVA** | `73f30ca` |
| A6, A9, A10 | M1.1 :784; M1.4 :434 (ERT-13: 2–3 mondat); M1.2 :41 | narráció | **EMBERI DÖNTÉS** (VO fix pack, X-6; szövegjavaslat a nyers kivonat D. szakaszában) | — |
| A7 | M5.4 :193, :214; M6.3 ×4; Z.2 :300 | hiányzó „hova írd” | **JAVÍTVA** | `139bc24` |
| A11 | Z.4 videós mondatok | — | **NEM HIBA** (minden mondat feltételes) | — |
| A12 | M7.4 :532, :557; M3.2 :803; M7.4 :792, M7.B :569 | belső kód / fejlesztői fájl a tanulói szövegben | **JAVÍTVA** | `709423b`, `139bc24` |
| A13 | Z.1 :318; Z.3 :183 | kérdés ↔ vezérlő | **JAVÍTVA**; M5.3 :106 „és miért?”: **NEM HIBA** (gondolkodtató felvezetés) | `139bc24` |
| A14, A15 | dia-hivatkozások, offline PDF | — | **MOODLE-ONLY** / **EMBERI DÖNTÉS** (D-5: projektgazda / szerző) | — |
| B: M4.3 | M4.3 S1 :200, S4 :477 | hiányzó korrekciós visszajelzés; „+1–1 extra” kártya | **JAVÍTVA** (a SLIDE 3 indoklásaiból; 4 kártya, 4 célzóna-visszajelzés) | `139bc24` |
| B: M3.2 S6/S7, M3.4 kártyák 1–4, 9 | M3.2 :668, :759; M3.4 :469–481 | válaszonkénti visszajelzés hiányzik | **NYITOTT, forrás-szerzés** (M3.2: a kulcs még validálandó; M3.4: Memuna) | — |
| B: vélemény-keret kulcsolt itemen | M4.2 :626; M7.1 :104; M7.4 :211 | „nincs tökéletes válasz” ↔ ✅ | **EMBERI DÖNTÉS** (szerző + értékelési felelős; D-14) | — |
| B: kvíz-bevezetők | LMS-M0-06, M5-06, M6-06, M7-07 | hiányzó tanulói bevezető | **NYITOTT, forrás-szerzés** | — |
| C: Glosszárium :81 ↔ GYV §4.1 | Glosszárium :81 | ellentmondó névszabály | **JAVÍTVA** | `139bc24` |
| C: M3.3 :45 | M3.3 | törött félkövér | **JAVÍTVA** | `139bc24` |
| C: „Assignment” a tanulói szövegben | ≈40 hely, 21 fájl | angol Moodle-szó | **NYITOTT** (egy terminológiai szabály; a magyar Moodle-felület: „Feladat”) | — |
| D1 „Segítség és kapcsolatok” blokk | MAN :121 | a blokk tanulói szövege sehol | **NYITOTT, objektív** (GYV §4.1 szerint); HUM-OPS-02 csatornák: programvezető | — |
| D3 25 opcionális Feedback | builder D-045/D-046 | tárolt véleményválaszok | **EMBERI DÖNTÉS** (projektgazda + DPO; a forrás nem igazítható a buildhez döntés nélkül) | — |
| D5 TEXT-C tájékoztató | MAN :25; 11 űrlap | ötpontos „just-in-time” tájékoztató szövege | **NYITOTT, objektív** (a lezárt értékekből; „Kihez”: DPO) | — |
| D2, D6–D9 | ADAT | kapcsolattartó, megőrzési sorok, csoport-láthatóság | **EMBERI DÖNTÉS / BIZONYÍTÉK-KAPU** (DPO; runtime RA 15) | — |

## D. A célzott QA (blokkoló-diff) tételei

Reviewerek: `assessment-reviewer` (QA-ERT-1…7), `hungarian-editorial-reviewer` (QA-NYELV-1…21), `safety-policy-reviewer`
(QA-BIZT-1…9), `implementation-reviewer` (QA-IMPL-1…8, Moodle 4.5 forráskóddal), `pedagogy-reviewer` (QA-PED-1…10).
Bemenet: a `709423b` előtti diff (`02 Tervezet/`).

| Tétel | Osztály | Hogyan zárult | Commit |
|---|---|---|---|
| QA-ERT-1, -2, -3, -4, -5, -7 | objektív | javítva (R4-alapszint és önellenőrzés szövege; M6 „Erős”; M7 R4 0. szint tanulói nyelven; (D2) segédszöveg és ⚠️ mondat; BSPEC-09; hub-hivatkozás és a kapu két részének megnevezése) | `709423b`, `b2c0c6d` |
| QA-ERT-6 | objektív (döntési igény rögzítése) | BSPEC-08 „Döntés” mezője megnevezi a végső pont rejtésének döntéshozóját | `b2c0c6d` |
| QA-BIZT-1, -2, -3, -5, -9 | objektív | javítva (címzettek az ADAT §5/§11 szerint; R4 0. szint; GYV-11 az értékelői jegyzetben; kapcsolattartó-mondat; egyedi szöveg mondata az ADAT §11 szerint) | `709423b` |
| QA-BIZT-4 | emberi döntés | DPO: a rubrikakitöltés és az értékelői visszajelzés megőrzési sora | — |
| QA-BIZT-6, -7, -8 | bizonyíték-kapu | DPO (tájékoztató, RT-15), Memuna (az M7 (D)), ADV-E3/D-14 (AI-út) | — |
| QA-NYELV-1…3, -6…13, -15…18, -20, -21 | objektív | javítva | `709423b` |
| QA-NYELV-4 | emberi döntés | DPO: a 24 hónap kezdőpontja (a tanulói mondat a kánoni ADAT §11 sorrendjét követi) | — |
| QA-NYELV-5 | (biztonsági kétség) | a mondat az AI-tartalomra szűkítve („az a te szakmai döntésed”); a gyermekvédelmi felelősség mondata változatlan | `709423b` |
| QA-NYELV-14, -19 | objektív | a QA-PED-1 a) és a QA-IMPL-6 javításával zárult | `709423b` |
| QA-IMPL-1, -2, -4…8 | objektív | javítva (§4 nyitási logika; v2 nyitási feltételek és sablonígéret; „Mi jön utána?”; BSPEC-09; szintnév a rubrikában; „Grading method”) | `709423b`, `b2c0c6d` |
| QA-IMPL-3 | bizonyíték-kapu | X-16 kanonikus visszaellenőrzés (RT-P0-28, RA 30, X-16-WS); függőségi mondat az (E2)-ben | `709423b` |
| QA-PED-1 a), -2, -4…8, -10 | objektív | javítva | `709423b` |
| QA-PED-1 b) | emberi döntés | LMS-gazda + értékelési felelős: a v2-sablon és -leírás elérhetősége a nyitás előtt | — |
| QA-PED-3 | emberi döntés | módszertani lektor: az M5.1 S2 B ↔ S4 5. helyzet | — |
| QA-PED-9 | emberi döntés | programvezető + értékelési felelős (+ LMS-gazda): az újraértékelés kérésének csatornája; hol látja a tanuló a kapueredményt | — |

## E. Vétólista (answer key, küszöb, completion, rubrika, gyermekvédelmi/adatvédelmi megfogalmazás)

| Hely | Előtte → utána | Bizonyíték |
|---|---|---|
| M5.1 SLIDE 2 (A/B/C) | kulcs nélkül → A Suli ✅, B Somer ✅, C hétköznapok ✅ | M5.A ≈:248–250 kulcs, :266 szabály; owner order §5.A |
| M5.1 SLIDE 2 B-helyzet | „…mesél egy sztorit a hetéből.” → „…, a madrih pedig visszakérdez.” | M5.A kártya-változat; owner order §5.A |
| M5.1 SLIDE 4 5. helyzet | szár: „a madrih vezetésével”; a kulcs (nonformális) változatlan | a kulcs indoklása a madrihot nevezte meg |
| M5 KAPU R4 Alapszint, Erős | értékelői zárójel és Q12-utalás a cellából a kalibrációs pontokba | a szint jelentése szó szerint megmaradt |
| M7 KAPU R8 0. szint | eljárási zárójel a cellából az értékelői jegyzetbe, kiegészítve a GYV-11 mondatával | ADAT §5 GYV-11 |
| MAN §1 GATE-CP completion | „Receive a grade” → „Receive a grade” + „Receive a passing grade” | Moodle 4.5/5.0 kód; CB-C-0018 |
| MAN §4 nyitás | az éles kapu Assignmentjének completionje nem külön restrict-feltétel | RA 19 tartalékszabály; Moodle 4.5 kód |
| MAN LMS-M0-01/-02/-07 | CP → IB + kötelező Feedback; CP → natív Lesson; LMS-M0-02 nyitása LMS-M0-07 | HUM 20. szakasz |
| M0.1 S4 | + „Ezt most nem szeretném megosztani.” | HUM 20 (passzválasz), D-041 §4; szerzői jóváhagyásig nem élesíthető |
| M0.2 :369, :464 | „ne írj ide” → „ne írj le” | a lépés tanuló-lokális; a védő tartalom megmaradt |
| M4.3 S4 | +4 kártya (kategóriánként 1) és 4 célzóna-visszajelzés | a forrás „+ még 1–1 extra” előírása; SLIDE 3 indoklások |
| M5.4, M6 KAPU, M7 KAPU tájékoztatók | új tanulói tájékoztató | ADAT §3 mátrix, §5, §11; Program terv §7 |
| M7 KAPU (D1) 9. pont, kapuszabály | az R4 0. szintje tanulói nyelven | M7 KAPU R4 0. szint (:312) |
| BSPEC-08, BSPEC-09 | új `BUILD_SPEC_OPEN` sorok, `PROPOSED` értékekkel | nincs kánoni érték; a build-verdikt `NOT_READY` |
| BSPEC-10, BSPEC-11 | új `BUILD_SPEC_OPEN` sorok (`f009c9b`), `PROPOSED` értékekkel | QF-IMPL-1 (`mod/lesson/lang/en/lesson.php`, D-039); QA2-ERT-2 |
| M4.3 SLIDE 4 célzóna-visszajelzés | kártyára szóló szöveg → oszlopra szóló szöveg a húzásos úton; a kártyánkénti szöveg a húzásmentes úton marad; kulcs változatlan | h5p-drag-question `feedbackOnIncorrect`; QF-ERT-1 |
| M7 KAPU (A) bevezető | a Q13 témája tanulói nyelven, a kulcs nélkül; a Memuna-lábjegyzet törölve, mert a Q13 kulcsára utalt | QA2-ERT-5; M7 KAPU Q13 C ✅ |
| GYV §4.1 :88, Program terv :251, M3 KAPU :13 | `17905fd`: „közvetlen veszélyben a 112, munkaidőn kívül a Kék Vonal” → `f009c9b`: az eredeti mondat visszaállítva | a két olvasat közti választás a Memunáé (QF-BIZT-4, QF-NYELV-1, QF-PED-3); a Segítség-blokk addig csak a kánoni „közvetlen veszélyben hívd a 112-t” mondatot hozza (GYV :79, :105) |
| Segítség-blokk gyermekvédelmi pontja | új tanulói szöveg: előbb a biztonság és a 112; címzett a Memuna (helyettes: Ros Hinuh); „te vagy valaki más” | GYV :79, :81, :87, :105; HUM-OPS-02, HUM-SAFE-01, -03; élesítés: programvezető + Memuna |
| Adatvédelem §11.1 TEXT-C sablon | új tanulói sablon, a lezárt értékekből | §3 (90 nap), §5, §11 (Ki látja?, más célra); PT :238 (3); végső „Ki látja?”: DPO + LMS-gazda |

## F. Generatív AI-val írt tanulói szöveg (provenance, PRG-14 a))

A futás minden forrásszövegét generatív AI (Claude, Claude Code-ban) írta a projektgazda 2026-10-18-i utasítása alapján; a commitok `Co-Authored-By` sora ezt rögzíti. A PRG-14 szerint az AI-eredetet csak szerzői / provenance-bizonyíték alapján jelöljük: ez a lista az a bizonyíték, a tanulói jelölés módja és a szerzői nyilatkozat a szerzőé / tananyagfelelősé (M4:BIZT-G1-7, X-3).

- **Új tanulói feladatleírások és sablon:** M5.4 4.1 (`709423b`); M6 KAPU (E1) (`709423b`); M7 KAPU (D1), (D2), M7-HUB-MUNK-02 (`709423b`); M7.3-MUNK-01 (`139bc24`).
- **Új vagy átírt kvíz- és feladat-visszajelzés:** M5.1 SLIDE 2 válaszonkénti visszajelzés, SLIDE 4 5. helyzet (`709423b`, `f009c9b`); M4.3 SLIDE 1 két korrekciós visszajelzése, SLIDE 4 három új kártyája és célzóna-visszajelzései (`139bc24`, `f009c9b`).
- **Új tanulói bevezetők és blokkok:** a négy kvíz-bevezető (LMS-M0-06, -M5-06, -M6-06, -M7-07), a GATE-CP tanulói leírás, a „Segítség és kapcsolatok” blokk, az Adatvédelem §11.1 sablon (`17905fd`, `f009c9b`); M0.1 „Hogyan teljesíted?”, M0.2 navigációs mondatok (`73f30ca`, `f009c9b`).
- **Instrukció-javítások:** M4.2, M4.3, M3.4 húzásmentes út; M1.3, M5.4, M6.3, Z.1–Z.4 írási helyek (`139bc24`, `f009c9b`).
- A M4.2 és az M4.3 „Szakmai lektorálás” sora már jelöli, hogy a 2026-10-02-i lektorálás ezekre az elemekre nem terjed ki (`f009c9b`).

## G. Második célzott QA (QA2) és záró regressziós QA (QF) – lezárás

Nyers kimenet: `2026-10-18 Builder-bizonyíték – nyers kivonatok, AP-2026-10-18-01.md`, G. szakasz. QA2: safety, assessment, Hungarian a `17905fd` előtti diffen. QF: pedagogy, assessment, safety, implementation, Hungarian a `f96ce43` → `17905fd` teljes diffen (34 fájl); a pedagógiai, értékelési és implementációs lencse a 60 körös korlátnál megállt, a már ellenőrzött részekből adott riportot, és megnevezte, mit nem nézett meg (lent).

| Tétel | Osztály | Hogyan zárult | Commit |
|---|---|---|---|
| QA2-BIZT-1, -2, -4, -6 (objektív rész), -7, -8, -9, -10 a) | objektív | javítva (112 előbb; „te vagy valaki más”; helyettes a vétóban; ADV-1 feltétel; kontakt tényleges elérhetőségként; teljes Z.3-mondat, LMS-M7-10; „más célra” mondat; kizárólagos kihagyási lista) | `17905fd` |
| QA2-BIZT-3, QA2-BIZT-6 (végső szöveg) | emberi döntés | KANON:QA2-BIZT-3; KANON:QF-BIZT-6 | — |
| QA2-BIZT-5, QA2-BIZT-10 b) | bizonyíték-kapu | KANON:QA2-BIZT-5; KANON:QA2-BIZT-10b | — |
| QA2-ERT-1…6, GATE-CP „ha kell” | objektív | javítva („Közvetlenül a beküldés után”; BSPEC-11; kötelező M7.F, újraértékelés; egy próbálkozásban; lábjegyzet törölve; első próbálkozás, mentornak szóló jelzés) | `17905fd`, `f009c9b` |
| QA2-NYELV-1 | — | lásd QF-BIZT-4 | `f009c9b` |
| QA2-NYELV-2…10, -12 | objektív | javítva | `17905fd` |
| QA2-NYELV-11 | emberi döntés (kis súly) | a kvíz-bevezetőben a manifest szerinti „kijelölt mentorod vagy értékelőd”; az Adatvédelem §11 „értékelőd” mondata változatlan (DPO-szöveg, KANON:QF-BIZT-6) | `f009c9b` |
| QF-BIZT-1, -3 | objektív / bizonyíték-kapu átvezetése | javítva (M0.2 just-in-time feltétel; a HUM 20 nyitott oszlopa szó szerint az M0.1-ben és az M0.2-ben) | `f009c9b` |
| QF-BIZT-2, -5, -6 | emberi döntés | M0:QF-BIZT-2; KANON:QF-BIZT-5; KANON:QF-BIZT-6 | — |
| QF-BIZT-4, QF-NYELV-1, QF-PED-3 | emberi döntés (Memuna) | a kánoni mondat visszaállítva; KANON:QF-BIZT-4 | `f009c9b` |
| QF-PED-1, -2, -4, -5, -6, -8 | objektív | javítva (könyv → kérdőív átadás; célzóna-szöveg; Lesson-a11y; RA 31 záróoldal; javítási ág ütemezése; M5.1 visszautalás) | `f009c9b` |
| QF-PED-7 | emberi döntés | M7:QF-PED-7 | — |
| QF-PED-9 | nem hiba | az M5 KAPU 307–309 ismétlése értékelői szöveg; a cellából áthelyezett eredeti mondat szó szerinti megőrzése szándékos | — |
| QF-ERT-1, -2, -3, -4 | objektív | javítva (= QF-PED-2; = QF-PED-8; G1, G2, G5b és Adatvédelem §3; RA 19 negatív eset) | `f009c9b` |
| QF-ERT-5 | emberi döntés | M0:QF-ERT-5 (a forrásban fejlesztői figyelmeztetés) | `f009c9b` |
| QF-IMPL-1 | build-spec | BSPEC-10, M0:BSPEC-10 | `f009c9b` |
| QF-IMPL-2…7, -9 | objektív | javítva (Lesson-a11y; célzóna; 4.5-ös címkék; LESSON profil, H5P-C kivétel; G2 / §3; mechanizmus-bizonyíték; teljes fájlnév) | `f009c9b` |
| QF-IMPL-8 | emberi döntés | M0:QF-IMPL-8 (az M0.1 :322 builder-javaslatként hivatkozza) | `f009c9b` |
| QF-NYELV-2…20 | objektív | javítva (a -19 a „feladatot / célt” betoldással) | `f009c9b` |
| Ledger-újraellenőrzés (161 sor) | — | 14 sor forráshely-megjegyzéssel frissítve; döntéssel lezárt 0 | ledger |

**Amit a záró QA nem nézett meg** (a lencsék saját jelentése szerint): M0.3, M0.4, M1, M2.4, Z.1–Z.4 a diffen túl; az M5.B, M6.B, M7.B teljes peulaszövege; az időbecslések újraszámolása (M4.3: 8 → 12 kártya; M0.1: plusz egy Feedback); a Lesson záró URL-je és jegyrögzítése Moodle-forrásból; az ASSIGN-S újranyitás a CB-C-0017-en túl; a hétköznapi határidők a pilot-felülírással (HUM 11) szemben; WCAG célméret és kontraszt a Lesson- és Feedback-képernyőkön. Ezek nem „rendben” állapotúak, hanem nem vizsgáltak.
