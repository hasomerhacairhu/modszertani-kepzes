# Módszertani képzés — Claude Code munkarend

## Mi ez a repository

A Hasomer Hacair blended madrichképzésének (ifjúsági vezetőképzés) teljes módszertani
fejlesztési és implementációs specifikációja. Moduláris felépítés: **M0–M7 + Z**,
mastery learning alapon, Moodle/H5P célplatformra.

- `02 Tervezet/` — **ez az aktív tananyag.** Minden más ezt szolgálja.
- `01 Fejlesztés/04 Audit/` — **audit trail, nem tanulói tartalom, nem aktuális kánon.**
  Az auditnaplók a múltat rögzítik; egy ottani mondat nem specifikáció.
- `tools/content_integrity.py` — az egyetlen objektív, determinisztikus ellenőrző.
- A korpusz **AFFiNE-ból exportált**: a természetellenes magyar mondatok jelentős része
  export- és gépifordítás-maradvány, nem szándékos szerzői stílus.

## Kánoni forrás-sorrend

1. `02 Tervezet/Program terv.md` — program-architektúra
2. `02 Tervezet/Modulok/` — modul-, lecke-, peula- és kapuspecifikáció
3. `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md` — terminológia
4. `02 Tervezet/Emberi jóváhagyás szükséges.md` + a release-gate dokumentumok
5. `01 Fejlesztés/04 Audit/` — előzmény, nem kánon

Ha 1–4 ellentmond egymásnak, az **finding**. Ne válassz közülük magadtól.

## Emberi döntési határok

Ezekben Claude **nem dönt és nem talál ki választ** — findingot ír, és megáll:

- **kiskorúak szerepe**: a madrich maga is lehet kiskorú, nem ő az egyedüli felelős
  felnőtt, és nem kaphat önálló hatósági vagy jogi döntéshozói szerepet
- gyermekvédelmi szakpolitika, eszkalációs szabály, szakértői gate
- jogi álláspont, GDPR-jogalap, AI Act-besorolás, szolgáltatási feltétel
- adatvédelmi (DPO) döntés: adatkör, megőrzés, hozzáférés
- helyi someres ideológiai vagy terminológiai döntés
- szervezeti jóváhagyás, release sign-off

## Munkarend

**Előbb értsd meg → tervezz → módosíts → tesztelj → olvasd vissza a diffet.**

Az **audit és a javítás külön művelet.** Review soha nem szerkeszt tananyagot; javítás
soha nem indít új teljes auditot. A folyamat:

`/course-review` → validált findingok → **emberi döntés** → `/course-fix` vagy
`/hungarian-edit` → `/release-check`. Új lecke vagy peula: `/course-develop`.

### Tananyagon ad hoc ne dolgozz

A fenti garanciák (read-only reviewerek, adverzális ellenőrzés, finding-formátum,
emberi kapuk) **a skillek belsejében élnek**, és a skilleket csak a felhasználó
indíthatja el. Ezért:

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

## Kontextus-fegyelem

- Egy jól körülhatárolt scope egyszerre: egy modul, egy fájl, egy lencse.
- Nagy kutatás és többfájlos átolvasás **specialista subagentbe** megy, nem a fő
  contextbe. A subagent rövid finding-listát ad vissza, nem fájldumpot.
- Nem összefüggő workstream között `/clear`.
- Ne olvass be teljes korpuszt „biztos, ami biztos" alapon.

## Git-biztonság

- A branchen **lehetnek pusholatlan felhasználói commitok. Semmit ne dobj el.**
- Tilos: `reset --hard`, `clean -f`, `checkout -- .`, `restore` (working tree),
  `rebase`, `commit --amend`, force push, bármilyen history rewrite.
  Ezeket a `.claude/hooks/guard-repo-safety.sh` hook blokkolja is.
- `git push` **kizárólag explicit kérésre** (a settings rákérdez).
- Felhasználói checkpoint-commitot ne amendelj és ne írj felül.

## Kötelező ellenőrzések tartalmi módosítás után

```bash
python3 tools/content_integrity.py    # 0 ERROR kötelező
git diff --check                      # whitespace-hibák
git diff                              # olvasd vissza a saját változtatásodat
```

Ezt a hármat a `/release-check` skill futtatja végig, a célzott ellenőrzésekkel együtt.

## Nincs hamis készjelentés

**0 script error ≠ jó tananyag.** Ebben a repositoryban egyszer már egy futás közben
önmagát átíró automatizmus adott „0 regresszió / validated" jelentést, miközben hét
javítás félkész maradt a fájlokban. Ezért:

- Bizonyíték **kizárólag a végállapot visszaolvasása**, nem a záró riport.
- Ha egy lépés kimaradt, elbukott vagy bizonytalan, mondd ki.
- „Kész"-t csak arra írj, amit ténylegesen a fájlban ellenőriztél.
- Egy invariáns-ellenőrzés utasítás-osztályra nézzen, ne egyetlen szó szerinti mondatra.

## Ebben a repositoryban NE

- ne írj governance- vagy folyamatdokumentumot a `02 Tervezet/` alá (az tananyag)
- ne építs második linter-rendszert a `tools/content_integrity.py` mellé
- ne szerkeszd kézzel a `02 Tervezet/Média-assetek/` generált CSV/XLSX kimeneteit
