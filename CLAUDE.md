# Módszertani képzés — Claude Code munkarend

## Mi ez a repository

A Hasomer Hacair blended madrihképzésének (ifjúsági vezetőképzés) módszertani specifikációja:
**M0–M7 + Z** modul, mastery learning, Moodle/H5P célplatform.

- `02 Tervezet/` — **az aktív tananyag.** Minden más ezt szolgálja.
- `01 Fejlesztés/04 Audit/` — audit trail, nem kánon; hivatkozott forrás belőle a
  `DEEP-AUDIT-RUBRIC.md`, a döntési jegyzőkönyvek, a validált riportok és az `AUTOPILOT-LEDGER.md`.
- Gépi ellenőrzés: `tools/content_integrity.py` (integritás, release-verdikt), `tools/media_manifest.py`
  + `tools/test_media_manifest.py` (média, látható-szöveg pinek), `tools/autopilot_ledger.py`.
  Más lintert nem építünk.
- A korpusz AFFiNE-ból exportált: a természetellenes magyar mondatok nagy része export- és
  gépifordítás-maradvány, nem szerzői stílus.
- A hanggyártás külön, privát VO QA-repóban él; az ide szóló javításait fix packként adja át.

## Kánon és döntések

1. `02 Tervezet/Program terv.md` — program-architektúra
2. `02 Tervezet/Modulok/` — modul-, lecke-, peula- és kapuspecifikáció
3. `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md` — terminológia
4. `02 Tervezet/Emberi jóváhagyás szükséges.md` + a release-gate dokumentumok

Ha 1–4 ellentmond egymásnak, az finding; ne válassz közülük magadtól. Egy **lezárt
projektgazdai döntés** az 1–3. fölött áll: ha egy forrás ellentmond neki, a forrás javítandó.
Döntések: `Emberi jóváhagyás szükséges.md` (`LEZÁRVA` tételek és a 8. szakasztól a datált
szakaszok), média és hang: `02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md`; bizonyítékuk a
`04 Audit` döntési jegyzőkönyveiben. Mi számít lezárt döntésnek és mi bizonyíték-kapunak:
egyetlen definíció, `.claude/rules/safety-and-human-gates.md` „Lezárt döntések”. Lezárt döntést
követsz és átvezetsz, nem nyitsz újra.

**Írásmód** (HUM-SOMER-02): `madrih`, `hanih`, `hágsámá`, `dugma isit`, `Leviatán`.
**Nyilvános repó** (projektgazdai döntés, 2026-10-03): a hangok szerepnéven szerepelnek
(„kanonikus narrátorhang”, „második hang”), a forrás-beszélők `VOICE-SRC-01/02` álnéven; a hangok
saját neve és a privát VO QA-repó neve nem kerülhet commitba, üzenetbe, PR-be.

## Tananyag-invariánsok (részletek: `.claude/rules/`)

- A jelentés nem változhat véletlenül: amit nem tudsz hibásnak bizonyítani, nem írod át.
- Answer key, küszöb, ponthatár, időtartam, rubrikaszint, kapu-típus, completion-feltétel és a
  kötelező/opcionális besorolás csak bizonyított objektív hibánál vagy lezárt döntés alapján
  változik, a bizonyítékkal, a vétólistán jelentve.
- Gyermekvédelmi, adatvédelmi, AI- és akadálymentesítési kikötés nem törölhető. A madrih maga is
  lehet kiskorú: nem ő az egyedüli felelős felnőtt, és nem kap hatósági vagy jogi döntési szerepet.
- Szemantikus azonosító (`M3.2`, `Z.4`) nem sorszám; fájlnév és a rá mutató link együtt mozog
  (átnevezés, kemény sortörés: `.claude/rules/course-content.md`).
- A `02 Tervezet/Média-assetek/` generált kimeneteit csak a `python3 tools/media_manifest.py
  build` írja (külön `chore(media)` commitban); a `tools/approved-visible-text.json`-t csak a
  `--pin-visible`.
- Tananyagot és governance-fájlt csak `Edit`/`Write` eszközzel szerkesztesz: a `.claude/rules/`
  path-szabályai csak így töltődnek be, és a sandbox a Bash-írást a repóba OS-szinten tiltja.
- A `02 Tervezet/` alá nem kerül governance- vagy folyamatdokumentum; egyetlen kivétel a
  `02 Tervezet/Média-assetek/` produkciós területe.

## Végrehajtási osztályok

Egy kifejezetten engedélyezett feladaton belül (pl. „/course-autopilot M0-Z”, „javítsd a validált
M3 findingokat”) minden lépés három osztály egyikébe esik.

| Osztály | Mi tartozik ide | Mit teszel |
|---|---|---|
| **AUTONÓM** | olvasás; specialista review, verifikáció, deduplikálás; validált objektív finding és lezárt projektgazdai döntés javítása a scope-on belül, a közvetlen következmény-frissítésekkel; helyi tesztek és média-validáció; engedélyezett generált output (`build`, `--pin-visible` finding-ID-kkel); audit-napló, ledger, helyi commit munkaágon; továbblépés a következő független tételre | kérdés nélkül végzed, és bizonyítékot rögzítesz |
| **EMBERI / KÜLSŐ KAPU** | új gyermekvédelmi, eszkalációs vagy szakértői szabály; a kiskorú madrih szerepét érintő új szabály; új jogi, GDPR-, AI Act- vagy szolgáltatási értelmezés; DPO-döntés (adatkör, megőrzés, hozzáférés); nyitott helyi someres ideológiai vagy terminológiai kérdés; valódi küszöb-, kompetencia- vagy értékelési döntés; új pedagógiai tartalom; hiányzó szerepköri jóváhagyás (bizonyíték-kapu); valós Moodle-runtime bizonyíték | a tételt a pontos bizonyítékkal és döntési igénnyel (mit, kitől) rögzíted, **nem implementálod**, és **folytatod** a tőle független munkát |
| **VÉDETT MŰVELET** | `git push`, PR nyitása vagy mergelése, írás a mainre, force push és history-átírás, éles telepítés, valódi tanulói hozzáférés, érzékeny vagy személyes adat közzététele, a scope-on kívüli külső művelet, governance-fájl módosítása | csak kifejezett, erre a műveletre szóló felhatalmazással; a platform rákérdezése ilyenkor is megjelenik |

Ha nem tudod eldönteni, AUTONÓM-e egy tétel: EMBERI KAPU. Egy hiányzó jóváhagyás rögzítése nem a
jóváhagyás megadása; runtime-, QA- vagy release-bizonyítékot nem gyártasz és nem következtetsz ki.
Kánonból bizonyítható javításhoz nem kérsz jóváhagyást; rutinkérdéssel nem állítod meg a munkát.

## Skillek és delegálás

| Skill | Mire | Ki indítja |
|---|---|---|
| `/course-autopilot <M0-Z \| modulok \| resume>` | a teljes PREFLIGHT → … → REPORT lánc, tartós ledgerrel | felhasználó vagy Claude |
| `/course-review <scope> [--lens …]` | read-only, többlencsés review + adverzális verifikáció → validált riport az `04 Audit`-ban | felhasználó vagy Claude |
| `/course-fix <riport + ID-k \| findingok \| fix pack>` | validált objektív finding és lezárt döntés sebészi javítása | felhasználó vagy Claude |
| `/hungarian-edit <fájl>` | egyfájlos, jelentésmegőrző nyelvi szerkesztés | felhasználó vagy Claude |
| `/release-check` | független, read-only gépi ellenőrzés (CI-paritás) | felhasználó vagy Claude |
| `/course-develop <feladat>` | új lecke vagy peula — a tervet a projektgazda hagyja jóvá | csak a felhasználó |

- Munkarend: előbb értsd meg → tervezz → módosíts → tesztelj → olvasd vissza a diffet.
- Review-, audit- vagy „nézd át” kérésre `/course-review`; tananyag-javításra `/course-fix` vagy
  `/hungarian-edit`; több modulra vagy a kurzus véglegesítésére `/course-autopilot`. Ezeket a
  Skill eszközzel indítod, és a szabályaik kötnek; ad hoc, skill nélkül csak a felhasználó által
  konkrétan megnevezett, egyetlen apró javítást végzel.
- A review és a javítás külön fázis: review közben nem szerkesztesz tananyagot (a lencse-reviewerek
  és a `verifier` read-only: `Read`, `Grep`, `Glob`, néhol web), javítás közben nem indítasz
  teljes új auditot — a javítás után célzott, diffre szabott ellenőrzés jön. Két szándékos
  kivétel, egy fájlon belül: a `/hungarian-edit` maga jelöli ki a nyelvi hibákat (tartalmit
  soha), a `/course-develop` a saját, most írt fájlján futtatja a review-kapukat és javít.
- Egy scope egyszerre; teljes korpuszt „biztos, ami biztos” nem olvasol be. Nagy átolvasás
  subagentbe megy, nem a fő contextbe; párhuzamosan csak read-only ügynökök futnak (egyszerre
  legfeljebb 8); tananyagot csak a fő session ír, sorban.
- Finding-formátum: `.claude/finding-format.md`; review-dimenziók: `01 Fejlesztés/04 Audit/DEEP-AUDIT-RUBRIC.md`.

## Git-biztonság

- A brancheken lehetnek pusholatlan felhasználói commitok és nem commitolt munka: **semmit ne dobj
  el.** Tilos: `reset --hard` és `reset <commit>` (`--soft` is), `clean -f`, `checkout -- <út>`,
  `restore` (working tree), `rebase`, `commit --amend`, force push, bármilyen history-átírás — a
  rövidített opcióalakok is.
- Három réteg. (1) **Sandbox** (`.claude/settings.json`): a Bash a repóba, a `.git`-et is
  beleértve, nem ír; ideiglenes fájl a `$TMPDIR`-be kerül. Sandboxon kívül csak az a hívás fut,
  amelynek **minden része** szó szerint `git …` (a repó gyökeréből, `-C` nélkül), `gh …`,
  `python3 tools/media_manifest.py build`, a `--pin-visible`, vagy a
  `python3 tools/audit_import.py <forrás.md> "<fájlnév.md>"` (kész `.md` a munkamenet ideiglenes
  területéről, csak az `01 Fejlesztés/04 Audit/`-ba, követett fájl felülírása nélkül, a
  névellenőrzés után). Egy `cd`, `git -C`, `| head`, `; echo` vagy átirányítás a teljes hívást
  sandboxban tartja — a git-írás ezért mindig önálló hívás. A sandbox parancsból nem kapcsolható
  ki; a privát VO QA-repóba ebből a sessionből semmi nem írható. (2) **Hook**
  (`.claude/hooks/guard-repo-safety.sh`): a sandboxon kívüli git/gh hívások engedélylistája, fail
  closed. (3) **Settings** deny/ask szabályai — az ask minden módban, auto módban is rákérdez.
- Commit: egy engedélyezett feladaton belül, helyi munkaágon AUTONÓM (`git commit -F
  <$TMPDIR-fájl>`, csak a saját útvonalaid). A mainre nem commitolsz; felhasználói commitot nem
  amendelsz és nem írsz felül.
- `git push` és a GitHubra író `gh` parancsok VÉDETTEK: csak kifejezett kérésre, egyszerű, önálló
  alakban, a repó gyökeréből (`git push origin <branch>`, `gh pr create … --body-file <út>`); a
  settings minden módban rákérdez, más alakot a hook blokkol. A GitHubra kerülő szöveget a helyi
  `.git/hooks/text-name-check`, a pusht a `.git/hooks/pre-push` névellenőrzi; találatnál nincs
  push. Távoli branch törlése és GitHub API-írás blokkolt. A merge módját a felhasználó
  választja; átnevezést tartalmazó PR-nél a merge commit megőrzi az átnevezés-commitot (PR #12).
- A CI kizárólag olvasó-ellenőrző (`.github/read-only-workflows.sh`); a teljes, CI-paritású
  ellenőrzőlista a `/release-check` — ha a CI-ba új lépés kerül, a skill is frissül.

## Ellenőrzés és release

Tartalmi módosítás után, a végállapoton:

```bash
python3 -X pycache_prefix="${TMPDIR:-/tmp}/pyc" -m py_compile tools/*.py
python3 tools/content_integrity.py               # 0 ERROR kötelező
python3 tools/media_manifest.py check            # elcsúszás → build, külön chore(media) commit
python3 tools/media_manifest.py reconcile
python3 -m unittest tools.test_media_manifest    # látható szöveg változott → --pin-visible
git diff --check && git diff --check origin/main...HEAD
git diff                                         # olvasd vissza a saját változtatásodat
```

- Látható szöveg változott → a teljes diff visszaolvasása után, változtatáskészletenként egyszer
  `python3 tools/test_media_manifest.py --pin-visible "<finding-/HUM-ID-k>: <miért>"`; az
  indoklás csak validált finding- vagy döntés-azonosítót nevezhet meg.
- Logikai checkpointnál és a végén `/release-check`; közben diffre szabott, célzott ellenőrzés.
  A Stop-hook nem enged úgy befejezni egy kört, hogy a tananyag nem commitolt változásai
  `content_integrity`- vagy whitespace-hibát okoznak.
- Build- és release-állapotot csak a `python3 tools/content_integrity.py --release-report` két
  verdikt-sora ad: `MOODLE-BUILD-VERDICT` és `LEARNER-RELEASE-VERDICT` (a `RELEASE-VERDICT` egy
  ciklusig alias). Sem a `READY_FOR_STAGING_BUILD`, sem a `READY_FOR_CONTROLLED_PILOT` nem
  release-jóváhagyás: a pilothoz a G1–G8 kapuk szerepköri bizonyítéka (`FINAL_RELEASE_QA`) és a
  go/no-go döntés kell (`02 Tervezet/RELEASE-READINESS.md`); egy HUM-tétel lezárása sem az.

## Nincs hamis készjelentés

0 script error ≠ jó tananyag. Ebben a repóban egyszer már egy önmagát átíró automatizmus adott
„0 regresszió” jelentést, miközben hét javítás félkész maradt. Bizonyíték **kizárólag a
végállapot visszaolvasása** (fájl, diff, parancskimenet), nem egy riport vagy a ledger. Ami
kimaradt, elbukott vagy bizonytalan, azt kimondod; „kész”-t csak arra írsz, amit a fájlban
ellenőriztél — governance-munkánál is, ahol független ellenőrzés nélkül semmi sem „naprakész”.
Egy invariáns-ellenőrzés utasítás-osztályra nézzen, ne egyetlen szó szerinti mondatra.

## Hosszú futás, folytatás, új session

- A pótolhatatlan bemenetet (a projektgazda szó szerinti válasza, döntési csomag, validált
  finding-lista, nyers lencse-kimenet) azonnal az `01 Fejlesztés/04 Audit/`-ba írod: a scratchpad
  újraindításkor törlődik. Az autopilot állapota az `AUTOPILOT-LEDGER.md`; folytatás:
  `python3 tools/autopilot_ledger.py next`; indítás és `/goal`: a `course-autopilot` skill.
- A projekt-beállítások (hook, deny/ask, sandbox) csak a repó gyökeréből indított sessionben
  töltődnek be. Governance-változás (CLAUDE.md, `.claude/**`) után **új session** kell: a subagentek
  az induláskor betöltött szabályokat kapják. A `/doctor prompt-audit` 2.1.283-tól érhető el.
