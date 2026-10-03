---
name: release-check
description: Objektív, gépi release-ellenőrzés a tananyagon — content_integrity, media-manifest validáció és regressziós tesztek, whitespace, relatív linkek, placeholderek, answer-key és küszöbváltozások a diffen, szemantikus azonosítók, saját diff visszaolvasása. Nem módosít semmit, de ellenőrző parancsokat futtat (Bash). Futtasd tartalmi módosítás után és release előtt.
argument-hint: [scope, pl. M3 vagy üres = teljes repo]
disallowed-tools: Edit, Write, NotebookEdit
allowed-tools:
  - Bash(python3 tools/content_integrity.py*)
  - Bash(python3 tools/media_manifest.py --selftest)
  - Bash(python3 tools/media_manifest.py validate)
  - Bash(python3 tools/media_manifest.py check)
  - Bash(python3 tools/media_manifest.py reconcile)
  - Bash(python3 tools/media_manifest.py lint *)
  - Bash(python3 tools/media_manifest.py stats)
  - Bash(python3 -m unittest tools.test_media_manifest*)
  - Bash(python3 -m py_compile*)
  - Bash(python3 -m json.tool .claude/settings.json*)
  - Bash(bash -n .claude/hooks/guard-repo-safety.sh)
  - Bash(bash .claude/hooks/guard-repo-safety.sh --selftest)
  - Bash(bash .github/read-only-workflows.sh)
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
> tartósan read-only-k (`tools:` allowlist). A `/course-review` skill csak az indító
> körében nem kap `Bash`/`Edit`/`Write` eszközt (a `disallowed-tools` a következő
> felhasználói üzenettel megszűnik), ezért a review egyetlen körben fut le.
>
> A `media_manifest.py build` **nincs** az engedélyezett parancsok között: az generált
> kimenetet ír, ezért nem része ennek a nem mutáló skillnek.

Semmit nem javít — a hibákat felsorolja, és megnevezi, melyik skill javítja.
A repository két kánoni objektív ellenőrzési réteget tart fenn:
`tools/content_integrity.py` a statikus tartalmi/repo-integritásra, míg
`tools/media_manifest.py` + `tools/test_media_manifest.py` a média-manifest
determinista fordítására és regresszióira. Ne írj ezek mellé harmadik, párhuzamos lintert.

Scope: `$ARGUMENTS` (üres = teljes repository)

## 1. Kánoni checker

```bash
python3 tools/content_integrity.py --selftest
python3 tools/content_integrity.py --release-report
```

- `Objective integrity errors: 0` **kötelező**. Bármely `ERROR:` sor blokkoló.
- A `BLOCKER:` sorok szemantikus **learner-release** kapuk: nyitott vagy vétóval
  újranyílt HUM-tétel (`HUMAN-DECISIONS`), tanulói `KITÖLTENDŐ` (`MODULE-PLACEHOLDERS`),
  LMS `BUILD_OUTPUT`, runtime `RUNTIME_OUTPUT`, valamint a gyermekvédelmi, adatvédelmi,
  hozzáférhetőségi és program-transzfer checklistek nyitott pontjai. A HUM-tételek
  2026-10-02 óta lezártak; a megnevezett szerepek írásos bizonyítéka **bizonyíték-kapu**,
  nem nyitott döntés. A puszta dokumentációs `KITÖLTENDŐ` szóelőfordulás nem blocker.
- A `PRODUCTION:` sorok média-produkciós kapuk. Az `ERROR`-számot nem növelik, de a
  verdiktbe beszámítanak: `NO-GO` (van BLOCKER) → `CONTENT_READY / MEDIA_PENDING`
  (csak PRODUCTION maradt) → `READY`. A `--strict-release` csak `READY`-nél ad 0-s
  kilépési kódot. A `GOVERNANCE:` sorok szervezeti tételek, nem release-kapuk.
- A jelentésben a `RELEASE-VERDICT` sort **szó szerint** idézd.
- A valódi nyitott értékeket **nem töltjük ki találgatásból**, jelentendők.

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
- Ha a `check` elcsúszást jelez, a javítás `python3 tools/media_manifest.py build`, külön
  `chore(media)` commitban — ezt nem ez a skill futtatja, csak megnevezi.
- A `test_only_approved_edits_changed_learner_visible_text` bukása azt jelenti, hogy
  látható szöveg változott pin nélkül: a teljes diff visszaolvasása után
  `python3 tools/test_media_manifest.py --pin-visible "<finding-/HUM-ID-k>: <miért>"`
  (a felhasználó jóváhagyásával). Az elavult pin is bukás.
- A GitHub CI telepíti a Pandocot, ezért ott a render-parity tesztnek is futnia kell:
  a végső CI-ben **0 skip** az elvárt állapot. Lokális futásnál Pandoc hiányában az egyetlen
  opcionális render-parity skip elfogadható, de ezt a jelentésben explicit jelezni kell;
  a dependency-free strukturális guardnak mindig futnia kell.

## 3. Git-higiénia

```bash
python3 -m py_compile tools/*.py
git diff --check              # nem commitolt whitespace-hiba, sorvégi szóköz
git diff --check origin/main...HEAD  # a CI a teljes PR-tartományt nézi (merge-base óta; új fájlnál előbb git add -N)
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

## 5. Ecosystem-konfiguráció (ha `.claude/**` vagy `.github/**` változott)

```bash
python3 -m json.tool .claude/settings.json > /dev/null   # csendes = érvényes JSON
bash -n .claude/hooks/guard-repo-safety.sh                # csendes = szintaxis OK
bash .claude/hooks/guard-repo-safety.sh --selftest
bash .github/read-only-workflows.sh                       # a CI „Workflows stay read-only” lépése
```

## 6. Jelentés

Add meg: mi futott, mi az eredménye **szó szerint**, mi blokkoló, mi emberi döntés,
és mi a következő lépés. Ha valami nem futott le, **mondd ki.**

**Nincs hamis készjelentés.** A `0 error` azt jelenti, hogy a gépi invariánsok rendben —
nem azt, hogy a tananyag jó. Pedagógiai, nyelvi és biztonsági minőségre `/course-review` kell.
