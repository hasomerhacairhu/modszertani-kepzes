---
name: course-autopilot
description: Autonóm kurzusvéglegesítés a teljes vagy megadott modulkörre (M0–M7 + Z) — PREFLIGHT → INVENTORY → REVIEW → VERIFY → TRIAGE → FIX → REGRESSION → FINAL QA → REPORT, tartós ledgerrel (01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md), megszakítás és tömörítés után folytatható. A meglévő skilleket hívja (/course-review, /course-fix, /hungarian-edit, /release-check); emberi döntést nem hoz, hanem pontosan rögzít, és a független munkával folytatja. Használd több modul vagy a teljes tananyag véglegesítésénél, és egy félbeszakadt autopilot-futás folytatásánál (resume).
argument-hint: <M0-Z | M2,M5 | resume> [--lens pedagogy,assessment,language,safety,implementation|all] [--review-only]
---

# Course autopilot

Feladat: `$ARGUMENTS` (alapértelmezett lencsék: `pedagogy,assessment,implementation,safety`;
`--review-only`: nincs javítás).

## Állandó szabályok — a futás végéig, tömörítés után is

1. **Az állapot a ledgerben él, nem a contextben:** `01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md`
   (formátum és állapotgép: `${CLAUDE_SKILL_DIR}/ledger.md`). Tömörítés, megszakítás vagy új
   session után olvasd újra ezt a fájlt és a ledgert, futtasd a
   `python3 tools/autopilot_ledger.py next`-et, és onnan folytasd. A ledgert minden lezárt lépés
   után `Edit`-tel frissíted, mielőtt továbblépsz; a ledger nem bizonyíték, csak sorrend.
2. **Végrehajtási osztályok** (CLAUDE.md): az AUTONÓM munkát kérdés nélkül végzed. Az EMBERI /
   KÜLSŐ KAPU tételt a pontos bizonyítékkal és döntési igénnyel rögzíted (`BLOCKED_HUMAN`,
   `EVIDENCE_GATE`, Külső kapuk), **nem implementálod, és a tőle független munkával folytatod**.
   VÉDETT műveletet (push, PR, merge, governance-módosítás) csak akkor végzel, ha az indító üzenet
   kifejezetten engedi.
3. **Specialista utasítást nem duplikálsz:** a review a `/course-review`, a javítás a
   `/course-fix` (pusztán nyelvi tétel: `/hungarian-edit`), az ellenőrzés a `/release-check`
   eljárása — a Skill eszközzel hívod őket, és az ő szabályaik kötnek.
4. **Review közben nem szerkesztesz tananyagot.** Csak `MEGERŐSÍTVE` + `objektív` finding vagy
   lezárt projektgazdai döntés javítható; lezárt döntést nem nyitsz újra, újat nem hozol.
5. **Egy kézben, sorban írsz:** tananyagot csak a fő session ír, modulonként. Párhuzamosan csak
   read-only ügynökök futnak, egyszerre legfeljebb 8; az értesítésükre vársz, várakozásként nem
   keresgélsz.
6. **Nincs kitalált bizonyíték:** runtime-, szerepköri vagy release-jóváhagyást nem írsz be és nem
   következtetsz ki. Egy állapot csak a fájl, a diff vagy a parancskimenet visszaolvasása után
   kerül a ledgerbe.
7. **Nem dobsz el munkát:** idegen, nem commitolt változáshoz nem nyúlsz; a git-író hívás mindig
   önálló `git …` parancs (CLAUDE.md „Git-biztonság”); a mainre nem commitolsz.

## 1. PREFLIGHT

1. `git status --short`, `git branch --show-current`, `git log --oneline -3`. Idegen, nem
   commitolt változás → `PRECONDITION` kapu a ledgerben, jelentés, és megállsz (nem viszed át, nem
   dobod el).
2. `python3 tools/autopilot_ledger.py next`:
   - `ACTIVE` futás (`resume` vagy azonos scope) → a kiírt lépésnél folytatod;
   - `NONE` / `FINISHED` → új futás (a régi ledger a git-historyban marad): Futás tábla (Run-ID
     `AP-<ÉÉÉÉ-HH-NN>-<nn>`, scope, lencsék, a felhatalmazás az indító üzenetből szó szerint,
     munkaág, bázis-commit, dátum, korlátok), Modulok tábla a scope-ra, és a Külső kapuk
     újraellenőrizve: `PRECONDITION` csak az, ami ennek a scope-nak a futását blokkolja; a scope-on
     kívüli nyitott tétel `HUMAN_DECISION`-ként marad. Nyitott `PRECONDITION` mellett a futás nem
     indul: jelentés, megállás.
3. Ha a HEAD a `main`: `git switch -c autopilot/<Run-ID>` (önálló hívás).
4. **Korlátok a kánonból, minden futásnál újra:** a lezárt freeze-, pilot- és scope-döntések
   (`Emberi jóváhagyás szükséges.md` datált szakaszai, `04 Audit` döntési jegyzőkönyvek). Ma ilyen
   az M0+M1 pilot-freeze (2026-10-05; a pilot 2026-10-10 óta fut): ott csak a freeze-kivétel
   (P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy előrehaladást blokkoló hiba) javítható, a
   többi `OWNER_DEFERRED` (POST-PILOT). Ha a kánon azóta mást mond, az érvényes.
5. Kiinduló gépi állapot a Napló első sorába: `python3 tools/content_integrity.py` és a
   `--release-report` két verdikt-sora. Piros kiindulás → a javítása az első tétel.
6. Commit (`git add` a ledgerre, `git commit -F <$TMPDIR-fájl>`): `audit(autopilot): <Run-ID> start`.

## 2. INVENTORY — mi validált már, mi változott

Modulonként:
- a legutóbbi validált riport az `04 Audit`-ban (`… Validált findingok – <modul> …`) és a
  review-bázisa (a fejlécből vagy a mentő commit szülőjéből);
- `git diff --stat <bázis> HEAD -- "02 Tervezet/Modulok/<modul>"`, és a modult érintő kánoni sorok
  (manifest, HUM-tételek) változása a bázis óta;
- a riport minden ID-ja a Findingok táblába (`<modul>:<ID>`; `MEGERŐSÍTVE` + `objektív` → `OPEN`,
  `ELVETVE` → `REJECTED`, összevont → `DUPLICATE`, emberi döntés → `BLOCKED_HUMAN`,
  bizonyíték-kapu → `EVIDENCE_GATE`), a riport utáni projektgazdai döntésekkel (freeze-kivétel,
  POST-PILOT) együtt;
- Review: nincs változás a bázis óta, és a kért lencsék lefutottak → `REUSED`; csak egyes fájlok
  változtak → a `/course-review` csak azokra fut, és azok régi findingjai `NEEDS_RECHECK`; nincs
  riport vagy hiányzik egy lencse → `PENDING`.

Nagy riport kivonatolását read-only ügynökre bízhatod (kimenete: kész ledger-sorok); a beírás a te
`Edit`-ed, utána `python3 tools/autopilot_ledger.py validate`.

## 3. REVIEW + VERIFY

Minden `PENDING` modulra `/course-review <modul> --lens <a futás lencséi> --run <Run-ID>` (Skill
eszközzel). Az ügynököket, a folytatást, a verifiert és a mentést a `/course-review` szervezi; két
modul review-ja átfedhet, ha összesen sem fut 8-nál több ügynök. Állapot: `REVIEWING` →
`RAW_SAVED` (nyers kimenet mentve) → `VERIFIED` (riport mentve, minden ID-nak verdiktje van).
Commit: `audit(autopilot): <modul> validated review`.

## 4. TRIAGE

A validált findingok a ledgerbe, a 2. pont szabályai szerint, és még:
- `objektív`, de a javítása új pedagógiai tartalmat írna (új lecke, peula, feladat) →
  `BLOCKED_HUMAN` (`/course-develop`, a terv projektgazdai jóváhagyásával);
- `objektív`, de a javítási korlát egy nyitott döntéstől függ → `BLOCKED_HUMAN`, a döntési igénnyel;
- freeze alá esik, és nem freeze-kivétel → `OWNER_DEFERRED`;
- minden `BLOCKED_HUMAN` és `EVIDENCE_GATE` egy Külső kapu sorhoz tartozik (új vagy meglévő): mit
  kell eldönteni vagy bizonyítani, kinek, mely findingokat old fel.

## 5. FIX — modulonként, sorban

`--review-only` esetén az `OPEN` tételek és a modul Javítása `NOT_AUTHORIZED`. Különben:
1. A modul `OPEN` tételei: `/course-fix "<riport-fájl>" <ID-k> --run <Run-ID>`; a pusztán nyelvi
   tételek fájlonként: `/hungarian-edit <fájl> --findings <ID-k> --run <Run-ID>`. Ezek újra
   bizonyítják a hibát, minimálisan javítanak, célzottan újraellenőriznek, és tételenkénti
   állapotot adnak — azt vezeted át a ledgerbe.
2. Egy blokkolt tétel nem állítja meg a modult: a többivel folytatod.
3. Commit modulonként: a tartalmi javítás és a látható-szöveg pin (`fix(<modul>): <ID-k>`), a
   `media_manifest.py build` kimenete külön `chore(media)` commitban. A `FIXED` sorokba a tartalmi
   commit SHA-ja kerül; a modul `Javítás: DONE`, Bizonyíték: commit + a célzott ellenőrzés eredménye.

## 6. REGRESSION

- Modulonként a `/course-fix` záró lépései (integritás, whitespace, teljes diff, célzott lencse a
  diff-hunkokra). A célzott ellenőrzés új findingja `<modul>:QA-<n>` kulccsal a ledgerbe kerül, és
  ugyanígy triázsolod — nem indít teljes új auditot.
- Minden harmadik javított modul után és a FINAL QA előtt `/release-check`; piros eredménynél a
  hibát okozó modul javítása az első tétel.
- `NEEDS_RECHECK`: egyszeri célzott lencse-ellenőrzés a jelenlegi szövegre; utána `OPEN` vagy
  `REJECTED`.

## 7. FINAL QA

1. `/release-check`. Hibánál vissza a 6. ponthoz.
2. `Záró QA`: a release-check alatti commit és a két verdikt-sor szó szerint; `Állapot: FINISHED`;
   ledger-commit.
3. `python3 tools/autopilot_ledger.py check` — **csak** `AUTOPILOT-LEDGER: TERMINAL` és 0-s
   kilépési kód esetén kész; különben a kiírt okok a következő tételek.

## 8. REPORT

Rövid jelentés a ledgerre hivatkozva: modulonként review- és javítás-állapot, commitok; a
`BLOCKED_HUMAN` / `EVIDENCE_GATE` tételek és Külső kapuk döntési igényként (mit, kitől, mely
findingokat old fel); vétólista (answer key, küszöb, rubrika, gyermekvédelmi/adatvédelmi
megfogalmazás: fájl:sor, előtte/utána, bizonyíték); a két verdikt-sor és a `check` kimenete. A
`READY_FOR_STAGING_BUILD` és a `READY_FOR_CONTROLLED_PILOT` sem release-jóváhagyás.

## Indítás, `/goal`, folytatás

Új session a repó gyökeréből, auto módban (a projekt-settings `defaultMode: "auto"` értéke
terminálban nem érvényes; a flag vagy a felhasználói settings igen):

    claude --permission-mode auto

A sessionben egyetlen sor (a `/goal` minden kör után külön modellel ellenőrzi a feltételt, és amíg
nem teljesül, új kört indít; a háttérben futó ügynökök alatt az ellenőrzés vár):

    /goal Futtasd a /course-autopilot M0-Z futást, és folytasd, amíg a transzkriptben a `python3 tools/autopilot_ledger.py check` legutóbbi futása `AUTOPILOT-LEDGER: TERMINAL` sort és 0-s kilépési kódot mutat, a legutóbbi /release-check riport 0 objektív hibát jelent és mindkét verdikt-sort szó szerint idézi, és a `git status --short` üres. Közben nincs push, PR, merge vagy governance-módosítás, és emberi döntést nem implementálsz. Ha nyitott PRECONDITION miatt a futás nem indulhat, vagy ugyanaz a lépés háromszor egymás után elbukik, állj meg, és jelentsd az okát; legfeljebb 200 kör.

Folytatás: `claude --continue` (a `/goal` visszaáll), vagy új sessionben `/course-autopilot resume`.
Nem interaktív futás: `claude -p --permission-mode auto --permission-prompts none "/goal …"` — ott
minden rákérdező művelet (push, PR) automatikusan elutasítódik.
