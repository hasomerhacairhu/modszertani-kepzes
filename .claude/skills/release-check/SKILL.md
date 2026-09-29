---
name: release-check
description: Objektív, gépi release-ellenőrzés a tananyagon — content_integrity, media-manifest validáció és regressziós tesztek, whitespace, relatív linkek, placeholderek, answer-key és küszöbváltozások a diffen, szemantikus azonosítók, saját diff visszaolvasása. Nem módosít semmit, de ellenőrző parancsokat futtat (Bash). Futtasd tartalmi módosítás után és release előtt.
argument-hint: [scope, pl. M3 vagy üres = teljes repo]
disallowed-tools: Edit, Write, NotebookEdit
allowed-tools:
  - Bash(python3 tools/content_integrity.py*)
  - Bash(python3 tools/media_manifest.py*)
  - Bash(python3 -m unittest tools.test_media_manifest*)
  - Bash(python3 -m py_compile*)
  - Bash(python3 -c *)
  - Bash(bash -n .claude/hooks/*)
  - Bash(bash .claude/hooks/*)
  - Bash(git cat-file*)
  - Bash(git diff*)
  - Bash(git status*)
---

# Release-ellenőrzés

**Operatív, nem mutáló skill — nem „hard read-only".** Az `Edit`, `Write` és
`NotebookEdit` el van véve tőle, de **`Bash`-t futtat**: enélkül nem tudná lefuttatni az
objektív ellenőrzéseket. A parancsai olvasó/ellenőrző jellegűek, és a
`.claude/hooks/guard-repo-safety.sh` + `permissions.deny` réteg alatt futnak.

> A **hard read-only** kategória ettől külön áll: a `.claude/agents/` alatti reviewerek
> és a `/course-review` skill — azoknak `Bash`, `Edit` és `Write` eszközük **sincs**.

Semmit nem javít — a hibákat felsorolja, és megnevezi, melyik skill javítja.
A repository két kánoni objektív ellenőrzési réteget tart fenn:
`tools/content_integrity.py` a statikus tartalmi/repo-integritásra, míg
`tools/media_manifest.py` + `tools/test_media_manifest.py` a média-manifest
determinista fordítására és regresszióira. Ne írj ezek mellé harmadik, párhuzamos lintert.

Scope: `$ARGUMENTS` (üres = teljes repository)

## 1. Kánoni checker

```bash
python3 tools/content_integrity.py --release-report
```

- `Objective integrity errors: 0` **kötelező**. Bármely `ERROR:` sor blokkoló.
- A `BLOCKER:` sorok szemantikus release-kapuk: nyitott `HUM-*` döntések,
  produkciós szabályok, LMS `BUILD_OUTPUT`, runtime `RUNTIME_OUTPUT` és kanonikus
  checklistek. A puszta dokumentációs `KITÖLTENDŐ` szóelőfordulás nem blocker.
  A valódi nyitott értékeket **nem töltjük ki találgatásból**, jelentendők.

## 2. Média-manifest és generált output

A release-check ugyanazt a média-invariáns réteget futtatja, mint a GitHub CI.
A történeti baseline teszt **nem maradhat csendben skipelt** sekély klón miatt:

```bash
git cat-file -e a8629732e46eb489644dc90a624e6c8466612eda^{commit}
python3 tools/media_manifest.py --selftest
python3 tools/media_manifest.py validate
python3 tools/media_manifest.py check
python3 tools/media_manifest.py reconcile
python3 tools/media_manifest.py lint --high-only
python3 -m unittest tools.test_media_manifest
```

- A baseline commit hiánya **hiba**, nem elfogadható skip.
- A `check` szerint minden generált CSV/JSON/XLSX/Markdown kimenetnek naprakésznek kell lennie.
- A `reconcile` eredménye nem rejthet el unmapped/conflict sort.
- A GitHub CI telepíti a Pandocot, ezért ott a render-parity tesztnek is futnia kell:
  a végső CI-ben **0 skip** az elvárt állapot. Lokális futásnál Pandoc hiányában az egyetlen
  opcionális render-parity skip elfogadható, de ezt a jelentésben explicit jelezni kell;
  a dependency-free strukturális guardnak mindig futnia kell.

## 3. Git-higiénia

```bash
python3 -m py_compile tools/*.py
git diff --check      # whitespace-hibák, sorvégi szóköz
git status --short
git diff --stat
```

## 4. Célzott ellenőrzések a diffen

Ha van módosítás, **olvasd vissza a teljes saját diffedet** (`git diff`), és külön nézd meg:

- **answer key**: változott-e `✅` vagy más helyesmegoldás-jelölés helye/darabszáma
- **számok**: küszöb, százalék, ponthatár, időtartam, próbálkozásszám módosult-e
- **szemantikus azonosítók**: `M3.2`, `Z.4`, `M1.B` átírása vagy átszámozása
- **relatív linkek és fájlnevek**: átnevezés esetén a hivatkozó helyek is követték-e
- **félbehagyott szöveg**: mondat közepén véget érő sor, `TODO`, `…`, üres listaelem,
  duplikált bekezdés, elárvult címsor
- **tartalomvesztés**: `git diff --stat` szerint hol csökkent jelentősen a méret,
  és ott tényleg szándékos volt-e
- **ismert regressziók**: a checker `ACTIVE_SPEC_RULES`, `FORBIDDEN_ANYWHERE`
  és `M3_ROLEPLAY_PHRASES` listái a `tools/content_integrity.py`-ban — új guard csak
  **bizonyított, már ténylegesen előfordult regresszióra** kerülhet be. Generikus
  „rossz magyar" lint tilos; egy konkrét, dokumentált mass-replace hiba (például
  `műhelyban` → `műhelyben`) viszont szűk exact guardként védhető.

## 5. Ecosystem-konfiguráció (ha `.claude/**` változott)

```bash
python3 -c "import json,sys; json.load(open('.claude/settings.json')); print('settings.json OK')"
bash -n .claude/hooks/guard-repo-safety.sh && echo "hook szintaxis OK"
bash .claude/hooks/guard-repo-safety.sh --selftest
```

## 6. Jelentés

Add meg: mi futott, mi az eredménye **szó szerint**, mi blokkoló, mi emberi döntés,
és mi a következő lépés. Ha valami nem futott le, **mondd ki.**

**Nincs hamis készjelentés.** A `0 error` azt jelenti, hogy a gépi invariánsok rendben —
nem azt, hogy a tananyag jó. Pedagógiai, nyelvi és biztonsági minőségre `/course-review` kell.
