# Release Readiness – kötelező Go / No-Go kapuk

**Állapot:** NO-GO, amíg az alábbi P0 kapuk nincsenek bizonyítékkal lezárva.

A tananyag minősége és a release-érettség két külön kérdés. A repository erős pedagógiai specifikáció, de éles kurzusnak csak a tényleges szervezeti, adatvédelmi és LMS-implementációval együtt minősíthető.

## Globális kapuk – minden modul élesítését blokkolják

- [ ] **G1 Gyermekvédelem:** kijelölt felelős, helyi jelzési/escalation protokoll, alternatív út összeférhetetlenség esetére, M3 és kapcsolódó safety tartalmak szakértői aláírása. Lásd `Gyermekvédelem – release gate.md`.
- [ ] **G2 Adatvédelem és kiskorúak:** adatleltár, jogalapok, szerepkörök/hozzáférés, megőrzés/törlés, fotó/videó, érzékeny reflexiók, AI-szolgáltatások és kiskorú hozzáférés jóváhagyva. Lásd `Adatvédelem – tanulói adatok és AI.md`.
- [ ] **G3 LMS/H5P célkörnyezet:** Moodle-verzió és minden H5P content type verziója rögzítve; a kritikus completion, branching, draft/resume és accessibility tesztek átmentek. Lásd `LMS – H5P runtime acceptance.md`.
- [ ] **G4 Learner-facing placeholder = 0:** tanulói útvonalon nincs `KITÖLTENDŐ`, névtelen kontakt, bizonytalan határidő vagy nem létező link.
- [ ] **G5 Accessibility:** mobil + billentyűzet + screen reader + zoom/reflow + captions teszt a tényleges Moodle-renderen.
- [ ] **G6 Terminológia és korosztály:** a helyi Somer megerősítette a 2026-os kánoni alakokat és a 3/4 kvuca-architektúrát; a glosszárium és tananyag ennek megfelelő.
- [ ] **G7 Release regression:** `tools/content_integrity.py` 0 ERROR; link-check 0 broken local link; nincs kánoni duplikátum.

## Modul-specifikus kapuk

Egy modul tartalmi jóváhagyása lehet moduláris **csak akkor**, ha G1–G7 globális kapuk már zártak. Egy modul saját szakmai/ideológiai lektorálása blokkolhatja csak azt a modult, de globális safety/privacy/infrastruktúra hiányában **semmilyen modul nem élesíthető tanulóknak**.

## Program-transzfer

- [ ] A félév végi `Peula v2` nem a program végső teljesítménymutatója: működik a `Terepgyakorlat – 2. félév.md` szerinti hat valós, 60–90 perces peula + mentorfeedback ciklus.
- [ ] Pilot megtörtént kis csoporttal, findingek javítva és újratesztelve.
- [ ] Média-regiszter a tartalmi freeze **után** újragenerálva és auditálva.

## Merge ≠ release

A GitHub merge technikai esemény. Élesítéshez külön, dátummal és felelősökkel rögzített Go/No-Go review kell. A release bizonyítékai linkelhetők ebbe a dokumentumba vagy a kapcsolódó issue-kba.
