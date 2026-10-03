# Nagy findingcsomag (kb. 20+ tétel) — eljárás

A `SKILL.md` szabályai változatlanul érvényesek; ez a fájl csak azt teszi hozzá, ami egy hosszú
futást megszakíthatatlanná és folytathatóvá tesz. Egy 100+ tételes csomag közben szinte biztos a
context-tömörítés, és a scratchpad újraindításkor törlődik: az állapot ezért **fájlban** él, nem a
beszélgetésben.

## 1. Indulás

1. Olvasd be a csomag fejlécét: döntési forrás, bázis-commit, **alkalmazási sorrend**, ellenőrzési
   parancsok. A tételeket a csomag sorrendjében dolgozd fel (a függőségek miatt), fájlcsoportonként.
2. Hozd létre a **naplót**: `01 Fejlesztés/04 Audit/<ÉÉÉÉ-HH-NN> course-fix napló – <csomag>.md`,
   egy sor tételenként: `| ID | fájl | állapot | megjegyzés |`, kezdetben `várakozik`.
3. Kérdezd meg egyszer a felhasználót: kér-e **ellenőrzőpont-commitot fájlcsoportonként**
   (`fix(copy): <csomag> CF-xx…CF-yy`). Igen nélkül nem commitolsz.

## 2. Tételenként (a SKILL.md 1–5. lépése), plusz

- **Idempotencia:** ha a javítás szövege már a fájlban van, és a bizonyíték már nincs, a tétel
  `már alkalmazva` — nem szerkeszted újra. Ha egyik sincs meg, `kihagyva: a fájl eltér`, és jelzed.
- **Új fájl vagy új blokk** (pl. új `@source`, a csomag által előírt új dokumentum): csak ha a finding
  kifejezetten előírja, pontosan a megadott tartalommal (`Write`, illetve `Edit`). Ha a csomag
  ellenőrzőösszeget ad (sha256), egyeztesd.
- A naplót **fájlcsoportonként** frissítsd (`Edit`): `alkalmazva` / `már alkalmazva` /
  `kihagyva: <ok>` / `megállva: emberi döntés`.

## 3. Fájlcsoport végén

```bash
python3 tools/content_integrity.py
git diff --check
```

Ha `@asset`/`@source` változott: `python3 tools/media_manifest.py build`, majd `check`. Ha a felhasználó
kért ellenőrzőpontot, most commitolj (a generált kimenet külön `chore(media)` commitba).

## 4. Folytatás megszakítás után

Olvasd be a naplót és a `git diff --stat`-ot; az első nem lezárt tételnél folytasd. Minden tételt
újra bizonyítasz (2. lépés) — a napló csak a sorrendet adja, nem bizonyíték.

## 5. A csomag végén (a SKILL.md „A végén” lépései helyett ebben a sorrendben)

1. A teljes `git diff` visszaolvasása; látható szöveg változásakor **egyetlen**
   `python3 tools/test_media_manifest.py --pin-visible "<csomag> <ID-tartomány>: <miért>"`.
2. Célzott újraellenőrzés lencsénként, **csak a módosított fájlokra**: a finding ID-jének lencséje
   szerint (`NYELV` → `hungarian-editorial-reviewer`, `IMPL` → `implementation-reviewer`, `PED` →
   `pedagogy-reviewer`, `BIZT` → `safety-policy-reviewer`, `ERT` → `assessment-reviewer`); lencsénként
   egy futás a hozzá tartozó fájlokra. Lencse-ID nélküli tételnél a fájl dönt: tanulói lecke →
   `hungarian-editorial-reviewer` (+ `pedagogy-reviewer`, ha idő vagy feladat változott); `Média-assetek/`,
   LMS- és release-dokumentum → `implementation-reviewer`; gyermekvédelmi vagy adatvédelmi szöveg →
   `safety-policy-reviewer`; teszt- és eszközfájl → a tesztek futása. Nem teljes audit, és nem a `verifier`.
3. `/release-check`.
4. Jelentés: a napló összesítése (darabszám állapotonként), a kihagyott és megállított tételek
   indokkal, a vétólista, és ami emberi döntésre vár (finding-formátumban).
