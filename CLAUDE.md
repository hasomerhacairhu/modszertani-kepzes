# Módszertani képzés — Claude Code munkarend

## Mi ez a repository

A Hasomer Hacair blended madrihképzésének (ifjúsági vezetőképzés) teljes módszertani
fejlesztési és implementációs specifikációja. Moduláris felépítés: **M0–M7 + Z**,
mastery learning alapon, Moodle/H5P célplatformra.

- `02 Tervezet/` — **ez az aktív tananyag.** Minden más ezt szolgálja.
- `01 Fejlesztés/04 Audit/` — **audit trail, nem tanulói tartalom, nem aktuális kánon.**
  Az auditnaplók a múltat rögzítik; egy ottani mondat nem specifikáció.
- `tools/content_integrity.py` — központi statikus tartalmi integritás-ellenőrző.
- `tools/media_manifest.py` + `tools/test_media_manifest.py` — a média-manifest
  fordító/validátor és regressziós tesztréteg; a CI ezt külön, teljes historyval futtatja.
- A korpusz **AFFiNE-ból exportált**: a természetellenes magyar mondatok jelentős része
  export- és gépifordítás-maradvány, nem szándékos szerzői stílus.
- A hanggyártás (kanonikus narrátorhang, kiejtési szótár, renderelés) egy külön, privát VO
  QA-repóban él; az ide szóló javításait fix packként adja át, amit a `/course-fix` visz be.
  A nyilvános repóban a hangok szerepnéven szerepelnek („kanonikus narrátorhang”, „második
  hang”), a forrás-beszélők `VOICE-SRC-01/02` álnéven (projektgazdai döntés, 2026-10-03).

## Kánoni forrás-sorrend

1. `02 Tervezet/Program terv.md` — program-architektúra
2. `02 Tervezet/Modulok/` — modul-, lecke-, peula- és kapuspecifikáció
3. `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md` — terminológia
4. `02 Tervezet/Emberi jóváhagyás szükséges.md` + a release-gate dokumentumok
5. `01 Fejlesztés/04 Audit/` — előzmény, nem kánon

Ha 1–4 ellentmond egymásnak, az **finding**. Ne válassz közülük magadtól.

## Emberi döntési határok

Ezekben Claude **nem dönt és nem talál ki választ** — findingot ír, és megáll:

- **kiskorúak szerepe**: a madrih maga is lehet kiskorú, nem ő az egyedüli felelős
  felnőtt, és nem kaphat önálló hatósági vagy jogi döntéshozói szerepet
- gyermekvédelmi szakpolitika, eszkalációs szabály, szakértői gate
- jogi álláspont, GDPR-jogalap, AI Act-besorolás, szolgáltatási feltétel
- adatvédelmi (DPO) döntés: adatkör, megőrzés, hozzáférés
- helyi someres ideológiai vagy terminológiai döntés
- szervezeti jóváhagyás, release sign-off

**Lezárt döntések.** Az `Emberi jóváhagyás szükséges.md` 2026-10-02-án lezárt
(`LEZÁRVA` + `Jóváhagyta:`) tételei projektgazdai döntések: követed és átvezeted, nem
nyitod újra (részletek: `.claude/rules/safety-and-human-gates.md`). A megnevezett szerepek
(Memuna, DPO, jogi felelős) írásos bizonyítéka **bizonyíték-kapu**, nem nyitott döntés:
nem írod be és nem feltételezed. A fenti határok az új, illetve a lezárt döntésen
túlmenő kérdésekre érvényesek. A helyi írásmód is eldőlt (HUM-SOMER-02): `madrih`,
`hanih`, `hágsámá`, `dugma isit`, `Leviatán`.

## Munkarend

**Előbb értsd meg → tervezz → módosíts → tesztelj → olvasd vissza a diffet.**

Az **audit és a javítás külön művelet.** Review soha nem szerkeszt tananyagot; javítás
soha nem indít új teljes auditot. A folyamat:

`/course-review` → validált findingok → **emberi döntés** → `/course-fix` vagy
`/hungarian-edit` → `/release-check`. Új lecke vagy peula: `/course-develop`.

### Tananyagon ad hoc ne dolgozz

A fenti garanciák (read-only reviewerek, adverzális ellenőrzés, finding-formátum,
emberi kapuk) **a skillek belsejében élnek**. A `/course-review`, `/course-fix`,
`/hungarian-edit` és `/course-develop` skillt csak a felhasználó indíthatja el (a nem
mutáló `/release-check`-et Claude is futtathatja). Ezért:

- Ha a kérés review, audit vagy „nézd át" jellegű → mondd meg, hogy a belépő
  `/course-review <scope>`, és **várd meg**. Ne kezdj el a fő contextben átvizsgálni.
- Ha a kérés tananyag-javítás → `/course-fix` (tartalmi) vagy `/hungarian-edit` (nyelvi).
- Ha a kérés új tananyag → `/course-develop`.
- Egyetlen kivétel: a felhasználó által **konkrétan megnevezett, egyetlen** apró
  javítás, amit ő maga már azonosított.

**Két szándékos kivétel a review ↔ javítás szétválasztás alól**, mert mindkettő egyetlen
fájlon belül, bizonyítható hibán dolgozik: a `/hungarian-edit` maga jelöli ki a nyelvi
hibákat (tartalmi, pedagógiai vagy policy-hibát soha), a `/course-develop` pedig a
saját, most írt fájlján futtatja a review-kapukat és javít. Máshol nem.

Tananyagot csak `Edit`/`Write` eszközzel szerkessz: a `.claude/rules/` útvonalhoz kötött
szabályai csak ezeknél töltődnek be, Bash-alapú (sed, python) szerkesztésnél nem.

## Kontextus-fegyelem

- Egy jól körülhatárolt scope egyszerre: egy modul, egy fájl, egy lencse.
- Nagy kutatás és többfájlos átolvasás **specialista subagentbe** megy, nem a fő
  contextbe. A subagent rövid finding-listát ad vissza, nem fájldumpot.
- Nem összefüggő workstream között `/clear`.
- Ne olvass be teljes korpuszt „biztos, ami biztos" alapon.
- Hosszú, többügynökös futásnál a pótolhatatlan bemenetet (a projektgazda szó szerinti
  válasza, döntési csomag, validált finding-lista) azonnal tartós helyre írd
  (`01 Fejlesztés/04 Audit/` vagy commit egy munkaágon): a `/private/tmp` scratchpad
  újraindításkor törlődik.

## Git-biztonság

- A branchen **lehetnek pusholatlan felhasználói commitok. Semmit ne dobj el.**
- Tilos: `reset --hard`, `reset <commit>` (akár `--soft`), `clean -f`, `checkout -- .`,
  `restore` (working tree), `rebase`, `commit --amend`, force push, bármilyen history
  rewrite. Ezeket a `.claude/hooks/guard-repo-safety.sh` hook blokkolja is.
- `git push` és `gh pr merge` **kizárólag explicit kérésre**: a hook és a settings minden
  alakban rákérdez (a `git -C <út> push`-ra is). Távoli branch vagy ref törlése (`git push -d`,
  `:ref`, `--prune`, `gh api` DELETE a `git/refs`-en) blokkolt; a `gh pr merge|close
  --delete-branch` rákérdez. Távoli branchet a felhasználó töröl.
- **Nyilvános repó:** a hangok neve és a privát VO QA-repó neve nem kerülhet commitba — üzenetbe
  sem (projektgazdai döntés, 2026-10-03). Push előtt a VO QA-repó `tools/check-course-push.py`
  ellenőrzője átnézi a pusholandó tartományt; találatnál a branch nem pusholható.
- A merge módját a felhasználó választja; atomikus átnevezést tartalmazó PR-nél a merge
  commit megőrzi az átnevezés-commitot (PR #12).
- A CI kizárólag olvasó-ellenőrző: `contents: write` jogú, tartalmat vagy generált
  kimenetet író vagy pusholó workflow tilos (2026-09-29: 43fd22a). A rebuild lokálisan,
  külön `chore(media)` commitban készül.
- Felhasználói checkpoint-commitot ne amendelj és ne írj felül.

## Kötelező ellenőrzések tartalmi módosítás után

```bash
python3 -m py_compile tools/*.py                # minden Python tool szintaktikailag érvényes
python3 tools/content_integrity.py               # 0 ERROR kötelező
python3 tools/media_manifest.py check            # elcsúszás → python3 tools/media_manifest.py build
python3 tools/media_manifest.py reconcile        # történeti sorok egyeztetve
python3 -m unittest tools.test_media_manifest    # média-regressziós tesztek + látható-szöveg pinek
git diff --check                                 # nem commitolt változás
git diff --check origin/main...HEAD              # a CI a teljes PR-tartományt nézi (merge-base óta)
git diff                                         # olvasd vissza a saját változtatásodat
```

- **Látható szöveg változott** → a teljes diff visszaolvasása után, változtatáskészletenként
  egyszer: `python3 tools/test_media_manifest.py --pin-visible "<finding-/HUM-ID-k>: <miért>"`.
  A `tools/approved-visible-text.json`-t kézzel soha ne szerkeszd.
- **Kemény sortörés** sor végi `\`-sel, nem két szóközzel: a CI a teljes PR-tartományon
  futtatja a `git diff --check`-et, és egy 50% alá eső átnevezésnél a fájl minden
  sorvégi szóközét jelzi.

A teljes, CI-paritású lista a `/release-check`; ha a CI-ba új lépés kerül, a skill is
frissül. Governance-változás (CLAUDE.md, `.claude/**`) után a felhasználó futtassa a `/doctor`
utasításfájl-ellenőrzését: hiányzó hivatkozást és egymásnak ellentmondó szabályt keres. A GitHub CI ezen felül Pandocot telepít, ezért a rejtett asset-meta
render-parity teszt sem maradhat skipelt.

## Nincs hamis készjelentés

**0 script error ≠ jó tananyag.** Ebben a repositoryban egyszer már egy futás közben
önmagát átíró automatizmus adott „0 regresszió / validated" jelentést, miközben hét
javítás félkész maradt a fájlokban. Ezért:

- Bizonyíték **kizárólag a végállapot visszaolvasása**, nem a záró riport.
- Ha egy lépés kimaradt, elbukott vagy bizonytalan, mondd ki.
- „Kész"-t csak arra írj, amit ténylegesen a fájlban ellenőriztél.
- Egy invariáns-ellenőrzés utasítás-osztályra nézzen, ne egyetlen szó szerinti mondatra.

## Ebben a repositoryban NE

- ne írj governance- vagy folyamatdokumentumot a `02 Tervezet/` alá (az tananyag).
  **Egyetlen, szűk kivétel:** a `02 Tervezet/Média-assetek/` mappa a média-produkció
  saját területe — ide tartoznak az asset-specifikációk, a produkciós szabályok, a
  döntési nyilvántartások és a generált produkciós nézetek, mert közvetlenül az aktív
  tananyagot valósítják meg. Ez **nem** ad engedélyt általános projekt-governance vagy
  folyamatdokumentum írására a `02 Tervezet/` bármely más pontján
- ne építs második linter-rendszert a `tools/content_integrity.py` mellé
- ne szerkeszd kézzel a `02 Tervezet/Média-assetek/` generált kimeneteit (CSV, XLSX,
  `_build/*.json` és a `Média-assetek/README.md` „Mi generált?” táblájában felsorolt
  Markdown-fájlok): a `python3 tools/media_manifest.py build` állítja elő őket
