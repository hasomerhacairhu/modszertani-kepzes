# Deep Audit Rubric

Ez a repository **egyetlen kánoni audit-dimenziólistája**. A `/course-review` skill és a
`.claude/agents/` alatti specialista reviewerek erre hivatkoznak — ne készíts mellé
másodikat. A gépi és ügynöki audit **nem helyettesíti** a szakértői jóváhagyást.

A finding-formátumot külön fájl írja le: `.claude/finding-format.md`.

## Dimenziók

| ID | Dimenzió | Piros (P0) finding | Sárga (P1) finding |
|---|---|---|---|
| D1 | Constructive alignment | cél nincs mérve / kapu mást mér | részleges vagy homályos illeszkedés |
| D2 | Tanulási ív és terhelés | blokkoló sorrendi/prerekvizit hiba | túlterhelés, gyenge ritmus, irreális időbecslés |
| D3 | Értékelés / mastery | hamis completion, kritikus safety tudás nem kapuzott | rubrika/feedback/elosztó finomítandó |
| D4 | LMS/H5P implementálhatóság | dokumentált funkció nincs vagy nem bizonyított | verzió-/runtime-kockázat |
| D5 | Accessibility | kulcstartalom nem hozzáférhető | javítandó UX/a11y részlet |
| D6 | Someres tartalmi/ideológiai pontosság | helyi döntést AI találna ki | helyi megerősítés kell |
| D7 | Safeguarding | veszélyes instrukció, hiányzó eszkaláció, szakértői gate megkerülése | óvatosság / keretezés javítandó |
| D8 | Adatvédelem / AI | kiskorú vagy érzékeny adat kontroll nélkül | retention/access/alternatíva tisztázandó |
| D9 | Tudományos megalapozottság | bizonyítottan félrevezető / neuromítosz | túláltalánosított állítás |
| D10 | Repo-integritás | törött link, kánoni duplikátum, release-blokkoló placeholder | terminológiai/stílus inkonzisztencia |
| D11 | Magyar szerkesztői minőség | a nyelvi hiba **megváltoztatja a jelentést** vagy egy szabályt | természetellenes magyar, AI-s tónus, anglicizmus, tipográfia |
| D12 | Tanulói és képzői élmény | kötelező önfeltárás, hiányzó kilépési lehetőség, végrehajthatatlan instrukció | gyenge motiváció, hiányzó választás, nehezen felkészülhető peula |
| D13 | Modulok közti konzisztencia és transzfer | ellentmondó szabály két kánoni dokumentum között | ismétlődés, gyenge terepgyakorlati átkötés |

A táblázat a P0 és P1 küszöböt adja. **P2** = minden további érdemi, de nem blokkoló
megállapítás bármely dimenzióban; a rubrika ezeket nem sorolja fel külön.

## Lencse → dimenzió

| Lencse (`/course-review --lens`) | Dimenziók |
|---|---|
| `pedagogy` | D1, D2, D9, D12, D13 |
| `assessment` | D1, D3 |
| `language` | D11, és D10 terminológiai része |
| `safety` | D6, D7, D8 |
| `implementation` | D4, D5, D10 |

A lencse → **agent** hozzárendelés kánoni helye a `/course-review` skill, nem ez a fájl.

## Routing — mi történik egy findinggel

- **D6, D7, D8**: emberi döntés. A reviewer findingot ír, **nem javasol szakpolitikai
  szöveget**, és a javítás nem automatizálható. Lásd `.claude/rules/safety-and-human-gates.md`.
- **D9** tárgyi állítás: elsődleges forrással cáfolható vagy alátámasztható; ha nincs
  elsődleges forrás, ezt ki kell mondani.
- **Minden más**: `verifier` adverzális ellenőrzés után `/course-fix` (tartalmi) vagy
  `/hungarian-edit` (nyelvi). Javítás **csak validált findingra**, soha nem audit közben.
- **Objektív invariáns** (link, duplikátum, tiltott regressziós mondat, placeholder):
  a `tools/content_integrity.py` dolga. Szemantikus ítéletet („rossz magyar", „gyenge
  pedagógia") **soha ne tegyél regex-szabállyá.**
