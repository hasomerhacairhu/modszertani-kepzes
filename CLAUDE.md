# Módszertani képzés — Claude Code munkarend

## Mi ez a repository

A Hasomer Hacair blended madrihképzésének (ifjúsági vezetőképzés) teljes módszertani
fejlesztési és implementációs specifikációja. Moduláris felépítés: **M0–M7 + Z**,
mastery learning alapon, Moodle/H5P célplatformra.

- `02 Tervezet/` — **ez az aktív tananyag.** Minden más ezt szolgálja.
- `01 Fejlesztés/04 Audit/` — **audit trail, nem tanulói tartalom, nem aktuális kánon.**
  Az auditnaplók a múltat rögzítik; egy ottani mondat nem specifikáció. Két kivétel, mert
  hivatkozott forrás: a `DEEP-AUDIT-RUBRIC.md` (a reviewerek dimenziólistája) és a
  projektgazdai döntési jegyzőkönyvek (a HUM-tételek bizonyítéka).
- `tools/content_integrity.py` — központi statikus tartalmi integritás-ellenőrző.
- `tools/media_manifest.py` + `tools/test_media_manifest.py` — a média-manifest
  fordító/validátor és regressziós tesztréteg; a CI ezt külön, teljes historyval futtatja.
- A korpusz **AFFiNE-ból exportált**: a természetellenes magyar mondatok jelentős része
  export- és gépifordítás-maradvány, nem szándékos szerzői stílus.
- A hanggyártás (kanonikus narrátorhang, kiejtési szótár, renderelés) egy külön, privát VO
  QA-repóban él; az ide szóló javításait fix packként adja át, amit a `/course-fix` visz be.

## Kánoni forrás-sorrend és a döntések helye

1. `02 Tervezet/Program terv.md` — program-architektúra
2. `02 Tervezet/Modulok/` — modul-, lecke-, peula- és kapuspecifikáció
3. `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md` — terminológia
4. `02 Tervezet/Emberi jóváhagyás szükséges.md` + a release-gate dokumentumok
5. `01 Fejlesztés/04 Audit/` — előzmény, nem kánon (a fenti két kivétellel)

Ha 1–4 ellentmond egymásnak, az **finding**; ne válassz közülük magadtól. **Kivétel:** egy
lezárt projektgazdai döntés az 1–3. források fölött áll — ha egy forrás ellentmond neki, az
a forrás javítandó.

**Hol élnek a döntések:** projektgazdai döntések → `Emberi jóváhagyás szükséges.md` (a
`LEZÁRVA` tételek és a 8–9. szakasz); bizonyítékuk → `01 Fejlesztés/04 Audit/` döntési
jegyzőkönyvei; média- és hangdöntések → `02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md`;
release-kapuk → `RELEASE-READINESS.md`. A release-állapotot **kizárólag** a
`python3 tools/content_integrity.py --release-report` `RELEASE-VERDICT` sora mondja meg; egy
HUM-tétel lezárása nem release-jóváhagyás.

## Emberi döntési határok

Ezekben Claude **nem dönt és nem talál ki választ** — findingot ír, és megáll:

- **kiskorúak szerepe**: a madrih maga is lehet kiskorú, nem ő az egyedüli felelős
  felnőtt, és nem kaphat önálló hatósági vagy jogi döntéshozói szerepet
- gyermekvédelmi szakpolitika, eszkalációs szabály, szakértői gate
- jogi álláspont, GDPR-jogalap, AI Act-besorolás, szolgáltatási feltétel
- adatvédelmi (DPO) döntés: adatkör, megőrzés, hozzáférés
- helyi someres ideológiai vagy terminológiai döntés
- szervezeti jóváhagyás, release sign-off

A határok az **új**, illetve a lezárt döntésen túlmenő kérdésekre érvényesek. Lezárt
projektgazdai döntést követsz és átvezetsz, nem nyitsz újra; a megnevezett szerepek írásos
bizonyítéka **bizonyíték-kapu**, nem nyitott döntés — nem írod be és nem feltételezed. A
definíció egyetlen helye: `.claude/rules/safety-and-human-gates.md` „Lezárt döntések”.

**Írásmód** (HUM-SOMER-02): `madrih`, `hanih`, `hágsámá`, `dugma isit`, `Leviatán`.
**Nyilvános repó** (projektgazdai döntés, 2026-10-03): a hangok szerepnéven szerepelnek
(„kanonikus narrátorhang”, „második hang”), a forrás-beszélők `VOICE-SRC-01/02` álnéven;
a hangok saját neve és a privát VO QA-repó neve nem kerülhet commitba, üzenetbe sem.

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

**Tananyagot és governance-fájlt csak `Edit`/`Write` eszközzel szerkessz.** A `.claude/rules/`
útvonalhoz kötött szabályai `Read`/`Edit`/`Write` eszköznél töltődnek be, Bash-nél nem; a
hook ezért blokkolja a Bash-szerkesztést (sed/perl/awk helyben, tee, átirányítás, cp/mv,
patch, inline szkript). Amit a hook nem lát (szkriptfájl, változón át megadott út), az is
tilos.

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
- **Governance-változás után új session.** A subagentek a session indulásakor betöltött
  CLAUDE.md-t és szabályokat kapják: egy CLAUDE.md- vagy `.claude/**`-commit után indíts új
  sessiont, mielőtt skillt vagy review-t futtatsz. A felhasználó ezután futtassa a `/doctor`
  utasításfájl-ellenőrzését (Claude Code 2.1.283+): hiányzó hivatkozást és egymásnak
  ellentmondó szabályt keres.
- A projekt beállításai (hook, deny/ask szabályok) csak akkor töltődnek be, ha a Claude Code
  a repó gyökeréből indul.

## Git-biztonság

- A branchen **lehetnek pusholatlan felhasználói commitok. Semmit ne dobj el.**
- Tilos: `reset --hard`, `reset <commit>` (akár `--soft`), `clean -f`, `checkout -- .` és
  `checkout <út>`, `restore` (working tree), `rebase`, `commit --amend`, force push, bármilyen
  history rewrite — a rövidített opcióalakok is (`--har`, `--amen`). A
  `.claude/hooks/guard-repo-safety.sh` hook ezeket blokkolja.
- `git push`, `gh pr merge` és `gh pr close` **kizárólag explicit kérésre**, és csak egyszerű,
  önálló alakban (`git push origin <branch>`, `git -C <út> push …`, `gh pr merge <n>`): ezekre a
  settings ask-szabálya minden módban rákérdez; minden más alakot (összetett parancs,
  `git -c … push`, `bash -c`, `gh pr --repo … merge`) a hook blokkol. Távoli branch vagy ref
  törlése és GitHub API-írás blokkolt; távoli branchet a felhasználó töröl.
- **Push előtt** a névellenőrzés: a VO QA-repó `tools/check-course-push.py --range
  origin/main..<branch>` (a helyi `.git/hooks/pre-push` is futtatja, ha telepítve van);
  találatnál a branch nem pusholható.
- A merge módját a felhasználó választja; atomikus átnevezést tartalmazó PR-nél a merge
  commit megőrzi az átnevezés-commitot (PR #12).
- A CI kizárólag olvasó-ellenőrző (`.github/read-only-workflows.sh` allowlist; 2026-09-29-én
  egy író jogú job közvetlenül a main-re pusholt). A rebuild lokálisan, külön `chore(media)`
  commitban készül.
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
  egyszer: `python3 tools/test_media_manifest.py --pin-visible "<finding-/HUM-ID-k>: <miért>"`
  (rákérdez). A `tools/approved-visible-text.json`-t kézzel soha ne szerkeszd.
- Kemény sortörés, átnevezés, generált kimenetek: `.claude/rules/course-content.md`.
- A Stop-hook nem enged úgy befejezni egy kört, hogy a tananyag nem commitolt változásai
  `content_integrity` vagy whitespace-hibát okoznak.

A teljes, CI-paritású lista a `/release-check`; ha a CI-ba új lépés kerül, a skill is frissül.
A CI Pandocot telepít, és bukik, ha bármely média-teszt skippel.

## Nincs hamis készjelentés

**0 script error ≠ jó tananyag.** Ebben a repositoryban egyszer már egy futás közben
önmagát átíró automatizmus adott „0 regresszió / validated" jelentést, miközben hét
javítás félkész maradt a fájlokban. Ezért:

- Bizonyíték **kizárólag a végállapot visszaolvasása**, nem a záró riport.
- Ha egy lépés kimaradt, elbukott vagy bizonytalan, mondd ki.
- „Kész"-t csak arra írj, amit ténylegesen a fájlban ellenőriztél — governance-munkánál is:
  egy független ellenőrzés eredménye nélkül nem „naprakész”.
- Egy invariáns-ellenőrzés utasítás-osztályra nézzen, ne egyetlen szó szerinti mondatra.

## Ebben a repositoryban NE

- ne írj governance- vagy folyamatdokumentumot a `02 Tervezet/` alá (az tananyag).
  **Egyetlen, szűk kivétel:** a `02 Tervezet/Média-assetek/` mappa a média-produkció
  saját területe — ide tartoznak az asset-specifikációk, a produkciós szabályok, a
  döntési nyilvántartások és a generált produkciós nézetek, mert közvetlenül az aktív
  tananyagot valósítják meg. Ez **nem** ad engedélyt általános projekt-governance vagy
  folyamatdokumentum írására a `02 Tervezet/` bármely más pontján
- ne építs második linter-rendszert a `tools/content_integrity.py` mellé
- ne szerkeszd kézzel a `02 Tervezet/Média-assetek/` generált kimeneteit (lista:
  `.claude/rules/course-content.md` „Generált tartalom”)
