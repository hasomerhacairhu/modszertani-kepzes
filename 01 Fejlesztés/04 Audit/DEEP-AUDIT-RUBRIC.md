# Deep Audit Rubric

Ez a rubrika a `.claude/workflows/deep-audit.js` gépi auditjának kánoni dimenziólistája. A gépi audit **nem helyettesíti** a szakértői jóváhagyást.

| ID | Dimenzió | Piros finding | Sárga finding |
|---|---|---|---|
| D1 | Constructive alignment | cél nincs mérve / kapu mást mér | részleges vagy homályos illeszkedés |
| D2 | Tanulási ív és terhelés | blokkoló sorrendi/prerekvizit hiba | túlterhelés, gyenge ritmus |
| D3 | Értékelés / mastery | hamis completion, kritikus safety tudás nem kapuzott | rubrika/feedback finomítandó |
| D4 | LMS/H5P implementálhatóság | dokumentált funkció nincs vagy nem bizonyított | verzió-/runtime-kockázat |
| D5 | Accessibility | kulcstartalom nem hozzáférhető | javítandó UX/a11y részlet |
| D6 | Someres tartalmi/ideológiai pontosság | helyi döntést AI találna ki | helyi megerősítés kell |
| D7 | Safeguarding | veszélyes instrukció, hiányzó eszkaláció, szakértői gate megkerülése | óvatosság / keretezés javítandó |
| D8 | Adatvédelem / AI | kiskorú vagy érzékeny adat kontroll nélkül | retention/access/alternatíva tisztázandó |
| D9 | Tudományos megalapozottság | bizonyítottan félrevezető / neuromítosz | túláltalánosított állítás |
| D10 | Repo-integritás | törött link, kánoni duplikátum, release-blokkoló placeholder | terminológiai/stílus inkonzisztencia |

## Routing

- **D7** → `safeguarding-review`, biztonságkritikus tartalmat ne auto-javítson éles szakpolitikai állítássá.
- **D6** → `ideology-gate-review`, helyi Somer-konvenciót ne találjon ki.
- **D8** jogalap/retention/hozzáférés → emberi privacy/DPO review.
- Architekturális programváltozás → `architecture-review`.
- Auto-fix csak akkor, ha a helyes állapot objektíven bizonyítható (pl. link, elírás, duplikátum, egyértelmű belső ellentmondás).
