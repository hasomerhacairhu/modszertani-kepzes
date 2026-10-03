# Nagy findingcsomag (kb. 20+ tétel) — eljárás

A `SKILL.md` szabályai változatlanul érvényesek; ez a fájl azt teszi hozzá, ami egy hosszú
futást megszakíthatóvá és folytathatóvá tesz. Egy 100+ tételes csomag közben szinte biztos a
context-tömörítés, és a scratchpad újraindításkor törlődik: az állapot ezért **fájlban** él.
**Tömörítés vagy megszakítás után ezt a fájlt és a naplót újra beolvasod.**

## 1. Indulás

1. Olvasd be a csomag fejlécét: döntési forrás, bázis-commit, **alkalmazási sorrend**,
   ellenőrzési parancsok, várható köztes állapotok. A lépéseket ebben a sorrendben dolgozod fel.
2. Hozd létre a **naplót** (`Write`): `01 Fejlesztés/04 Audit/<ÉÉÉÉ-HH-NN> course-fix napló –
   <csomag rövid neve>.md`. Egy sor **lépésenként**: `| ID | lépés | fájl | állapot | megjegyzés |`,
   kezdetben `várakozik`. A forrást szerepnéven nevezd meg (pl. „VO QA-repó fix pack”), abszolút
   útvonal és privát repónév nem kerül bele.
3. Köztes commit nincs: a csomag köztes állapotai tervezetten lehetnek pirosak (lásd 3.). Commit
   csak a végén, és csak a felhasználó kérésére.

## 2. Lépésenként (a SKILL.md 1–6. lépése), plusz

- **Idempotencia** — mielőtt szerkesztesz. A döntés alapja a lépés **hozzáadott sorai**: a
  javítás azon nem üres sorai, amelyek a bizonyítékban nincsenek (a közös horgonysor, pl. egy
  címsor, nem hozzáadott sor). Nem a javítás teljes szövegblokkja dönt, mert két lépés
  osztozhat egy horgonyon (pl. CF-101 és CF-104: a 23. pont a 22. és a címsor közé kerül, így
  a CF-101 teljes blokkja már nem áll egyben, a hozzáadott sora viszont megvan):
  - *beszúrás* és *csere*: ha **minden** hozzáadott sor már a fájlban van (annyiszor, ahányszor a
    lépés hozzáadja) → `már alkalmazva`; ha **egyik sincs** meg, és a bizonyíték megvan →
    javítasz; ha csak **egy részük** van meg → `megállva: részben alkalmazva`, nem szerkesztesz,
    és a hiányzó sorokat jelzed; ha egyik sincs meg, és a bizonyíték sincs → `kihagyva: a fájl
    eltér`, és jelzed;
  - *csere hozzáadott sor nélkül* (a javítás csak elhagy a bizonyítékból): ha a bizonyíték
    megvan → javítasz; ha nincs meg, és a javítás szövege megvan → `már alkalmazva`; különben
    `kihagyva: a fájl eltér`;
  - *törlés*: ha a bizonyíték nincs meg, és a környező horgony megvan → `már alkalmazva`.
- Egy lépés = egy `Edit`; `replace_all` csak, ha a lépés előírja.
- A naplót **minden lépés után** frissítsd (`Edit`): `alkalmazva` / `már alkalmazva` /
  `kihagyva: <ok>` / `megállva: emberi döntés`.

## 3. Fájlcsoport végén

```bash
python3 tools/content_integrity.py
git diff --check
```

Csak ez a kettő. A `media_manifest.py check`/`reconcile` és a média-tesztek a csomag **közben**
tervezetten bukhatnak (pl. egy törölt narráció történeti sorainak diszpozíciója csak egy későbbi
lépésben érkezik, a látható szöveg pinje csak a végén frissül) — ez nem hiba, és nem javítod
el saját kútfőből. A csomag fejlécében megadott köztes állapotokat tekintsd elvártnak.

## 4. Folytatás megszakítás után

Olvasd be ezt a fájlt, a naplót és a `git diff --stat`-ot; az első nem lezárt lépésnél folytasd.
Minden lépést újra bizonyítasz (idempotencia-szabály) — a napló csak a sorrendet adja, nem
bizonyíték.

## 5. A csomag végén

A `SKILL.md` „A végén” sorrendje szerint: teljes diff → egyetlen pin → build kétszer + `check` +
`reconcile` → célzott újraellenőrzés a diff-hunkokkal, lencsénként (lencse-ID nélküli
lépésnél a fájl dönt: tanulói lecke → `hungarian-editorial-reviewer`, és `pedagogy-reviewer`, ha
idő vagy feladat változott; `Média-assetek/`, LMS- és release-dokumentum →
`implementation-reviewer`; gyermekvédelmi vagy adatvédelmi szöveg → `safety-policy-reviewer`;
teszt- és eszközfájl → a tesztek futása) → `/release-check` → jelentés a napló összesítésével
(darabszám állapotonként, kihagyott és megállított lépések indokkal, vétólista).
