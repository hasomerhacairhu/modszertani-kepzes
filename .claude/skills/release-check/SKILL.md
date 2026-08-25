---
name: release-check
description: Objektív, gépi release-ellenőrzés a tananyagon — content_integrity.py, whitespace, relatív linkek, placeholderek, answer-key és küszöbváltozások a diffen, szemantikus azonosítók, saját diff visszaolvasása. Nem módosít semmit, de ellenőrző parancsokat futtat (Bash). Futtasd tartalmi módosítás után és release előtt.
argument-hint: [scope, pl. M3 vagy üres = teljes repo]
disallowed-tools: Edit, Write, NotebookEdit
allowed-tools:
  - Bash(python3 tools/content_integrity.py*)
  - Bash(python3 -c *)
  - Bash(bash -n .claude/hooks/*)
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
Ez a repository **egyetlen** kánoni objektív checkere: `tools/content_integrity.py`.
Ne írj mellé második lintert.

Scope: `$ARGUMENTS` (üres = teljes repository)

## 1. Kánoni checker

```bash
python3 tools/content_integrity.py --release-report
```

- `Objective integrity errors: 0` **kötelező**. Bármely `ERROR:` sor blokkoló.
- A `BLOCKER:` sorok release-kapuk (`KITÖLTENDŐ`, nyitott checklist) — ezeket
  **nem töltjük ki találgatásból**, jelentendők.

## 2. Git-higiénia

```bash
git diff --check      # whitespace-hibák, sorvégi szóköz
git status --short
git diff --stat
```

## 3. Célzott ellenőrzések a diffen

Ha van módosítás, **olvasd vissza a teljes saját diffedet** (`git diff`), és külön nézd meg:

- **answer key**: változott-e `✅` vagy más helyesmegoldás-jelölés helye/darabszáma
- **számok**: küszöb, százalék, ponthatár, időtartam, próbálkozásszám módosult-e
- **szemantikus azonosítók**: `M3.2`, `Z.4`, `M1.B` átírása vagy átszámozása
- **relatív linkek és fájlnevek**: átnevezés esetén a hivatkozó helyek is követték-e
- **félbehagyott szöveg**: mondat közepén véget érő sor, `TODO`, `…`, üres listaelem,
  duplikált bekezdés, elárvult címsor
- **tartalomvesztés**: `git diff --stat` szerint hol csökkent jelentősen a méret,
  és ott tényleg szándékos volt-e
- **ismert regressziók**: a checker `ACTIVE_SPEC_RULES` és `M3_ROLEPLAY_PHRASES`
  listái a `tools/content_integrity.py`-ban — ha új invariáns kell, azt ott bővítsd,
  de **csak objektív invariánst**. „Ez rossz magyar" soha nem lehet regex-szabály.

## 4. Ecosystem-konfiguráció (ha `.claude/**` változott)

```bash
python3 -c "import json,sys; json.load(open('.claude/settings.json')); print('settings.json OK')"
bash -n .claude/hooks/guard-repo-safety.sh && echo "hook szintaxis OK"
```

## 5. Jelentés

Add meg: mi futott, mi az eredménye **szó szerint**, mi blokkoló, mi emberi döntés,
és mi a következő lépés. Ha valami nem futott le, **mondd ki.**

**Nincs hamis készjelentés.** A `0 error` azt jelenti, hogy a gépi invariánsok rendben —
nem azt, hogy a tananyag jó. Pedagógiai, nyelvi és biztonsági minőségre `/course-review` kell.
