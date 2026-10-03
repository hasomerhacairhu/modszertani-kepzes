---
name: release-check
description: Objektív, gépi release-ellenőrzés a teljes repón — content_integrity és release-verdikt, media-manifest validáció és regressziós tesztek, whitespace, governance-konfiguráció, answer-key és küszöbváltozások a diffen. Nem módosít semmit; külön subagentben fut, és tömör riportot ad. Futtasd tartalmi módosítás után és release előtt.
context: fork
agent: release-checker
background: false
allowed-tools:
  - Bash(python3 tools/content_integrity.py*)
  - Bash(python3 tools/media_manifest.py --selftest)
  - Bash(python3 tools/media_manifest.py validate)
  - Bash(python3 tools/media_manifest.py check)
  - Bash(python3 tools/media_manifest.py reconcile)
  - Bash(python3 tools/media_manifest.py lint *)
  - Bash(python3 tools/media_manifest.py stats)
  - Bash(python3 -m unittest tools.test_media_manifest*)
  - Bash(python3 -X pycache_prefix=* -m py_compile*)
  - Bash(python3 -m json.tool .claude/settings.json*)
  - Bash(bash -n .claude/hooks/*)
  - Bash(bash .claude/hooks/guard-repo-safety.sh --selftest)
  - Bash(bash .claude/hooks/review-agent-allowlist.sh --selftest)
  - Bash(bash .github/read-only-workflows.sh)
  - Bash(bash .github/read-only-workflows.sh --selftest)
  - Bash(bash -n .github/read-only-workflows.sh)
  - Bash(touch .sandbox-probe)
  - Bash(rm -f .sandbox-probe)
  - Bash(git fetch*)
  - Bash(git cat-file*)
  - Bash(git diff*)
  - Bash(git status*)
---

# Release-ellenőrzés

Mindig a **teljes** repót ellenőrzi; argumentuma nincs. Külön subagentben fut
(`release-checker`), így nem veszi el a hívó skill szerkesztő eszközeit, és csak a riport kerül
vissza. Semmit nem javít és nem buildel — a hibát megnevezi, és hogy melyik skill vagy parancs
javítja. Két kánoni ellenőrzési réteg van: `tools/content_integrity.py` és
`tools/media_manifest.py` + `tools/test_media_manifest.py`; harmadik linter nem kell.

## 1. Kánoni checker

```bash
python3 tools/content_integrity.py --selftest
python3 tools/content_integrity.py --release-report
```

- `Objective integrity errors: 0` **kötelező**. Bármely `ERROR:` sor blokkoló.
- A `BLOCKER:` sorok szemantikus learner-release kapuk (nyitott vagy vétóval újranyílt HUM-tétel,
  tanulói `KITÖLTENDŐ`, LMS-build, runtime, valamint a gyermekvédelmi, adatvédelmi,
  hozzáférhetőségi és program-transzfer checklistek nyitott pontjai). A megnevezett szerepek
  hiányzó írásos bizonyítéka **bizonyíték-kapu**, nem nyitott döntés.
- A `PRODUCTION:` sorok média-produkciós kapuk: az `ERROR`-számot nem növelik, de a verdiktbe
  beszámítanak (`NO-GO` → `CONTENT_READY / MEDIA_PENDING` → `READY`; a `--strict-release` csak
  `READY`-nél ad 0-s kilépési kódot). A `GOVERNANCE:` sorok nem release-kapuk.
- A `RELEASE-VERDICT` sort **szó szerint** idézd. Nyitott értéket nem töltünk ki találgatásból.

## 2. Média-manifest és generált output (a CI-vel azonos)

```bash
git cat-file -e a8629732e46eb489644dc90a624e6c8466612eda^{commit}
python3 tools/media_manifest.py --selftest
python3 tools/media_manifest.py validate
python3 tools/media_manifest.py check
python3 tools/media_manifest.py reconcile
python3 tools/media_manifest.py lint --high-only
python3 -m unittest tools.test_media_manifest
python3 tools/media_manifest.py stats
```

- A baseline commit hiánya **hiba**, nem elfogadható skip.
- A `check` elcsúszásánál a javítás `python3 tools/media_manifest.py build`, külön
  `chore(media)` commitban — megnevezed, nem futtatod.
- A `reconcile` nem rejthet el unmapped/conflict sort.
- A látható-szöveg teszt bukása: látható szöveg változott pin nélkül (vagy elavult a pin) →
  `python3 tools/test_media_manifest.py --pin-visible "<ID-k>: <miért>"`, a felhasználó
  jóváhagyásával — megnevezed, nem futtatod.
- A tesztek összegzése legyen `OK` skip nélkül; a CI egy skipre is bukik. Lokálisan Pandoc
  nélkül a render-parity skip előfordulhat — ezt jelezd.

## 3. Git-higiénia

```bash
python3 -X pycache_prefix="${TMPDIR:-/tmp}/pyc" -m py_compile tools/*.py   # a repó sandboxból nem írható
git fetch --quiet origin main
git diff --check                       # nem commitolt whitespace-hiba
git diff --check origin/main...HEAD    # a CI a teljes PR-tartományt nézi (merge-base óta)
git status --short
git diff --stat origin/main...HEAD
```

Új, még nem követett fájl a diffben nem látszik — ezt jelezd (`git status`).

## 4. Célzott ellenőrzések a diffen

Olvasd vissza a változásokat (`git diff origin/main...HEAD` és a nem commitolt `git diff`), és
nézd meg külön:

- **answer key**: változott-e `✅` vagy más helyesmegoldás-jelölés helye/darabszáma
- **számok**: küszöb, százalék, ponthatár, időtartam, próbálkozásszám
- **szemantikus azonosítók**: `M3.2`, `Z.4`, `M1.B` átírása vagy átszámozása
- **relatív linkek és fájlnevek**: átnevezésnél a hivatkozó helyek is követték-e
- **félbehagyott szöveg**: mondat közepén véget érő sor, `TODO`, üres listaelem, duplikált
  bekezdés, elárvult címsor
- **tartalomvesztés**: hol csökkent jelentősen a méret, és szándékos volt-e
- **ismert regressziók**: a checker `ACTIVE_SPEC_RULES`, `FORBIDDEN_ANYWHERE` és
  `M3_ROLEPLAY_PHRASES` listái — új guard csak bizonyított, ténylegesen előfordult
  regresszióra kerülhet be

## 5. Governance-konfiguráció (mindig, mint a CI-ben)

```bash
python3 -m json.tool .claude/settings.json > /dev/null
bash -n .claude/hooks/guard-repo-safety.sh
bash .claude/hooks/guard-repo-safety.sh --selftest
bash -n .claude/hooks/review-agent-allowlist.sh
bash .claude/hooks/review-agent-allowlist.sh --selftest
bash -n .claude/hooks/stop-checks.sh
bash .github/read-only-workflows.sh --selftest
bash .github/read-only-workflows.sh
touch .sandbox-probe                   # sandbox-próba: ennek EL KELL BUKNIA
```

A `.sandbox-probe` a `.claude/settings.json` sandbox `denyWrite` listáján van, ezért a `touch`
helyes működésnél „Operation not permitted” hibával bukik — ez a várt eredmény, így jelented:
„sandbox aktív”. Ha a `touch` **sikerül**, a Bash nem sandboxban fut (a settings nem töltődött
be, vagy a session sandbox nélkül indult): ez **blokkoló governance-hiba**; a próbafájlt
`rm -f .sandbox-probe` törli (gitignore-olt), és a riport első sora ezt mondja ki.

## 6. Jelentés

Mi futott, az eredmény **szó szerint** (döntő sorok), mi blokkoló, mi emberi döntés vagy
bizonyíték-kapu, és mi a következő lépés (melyik skill vagy parancs). Ha valami nem futott le,
**mondd ki.** A `0 error` azt jelenti, hogy a gépi invariánsok rendben — nem azt, hogy a
tananyag jó; pedagógiai, nyelvi és biztonsági minőségre `/course-review` kell.
