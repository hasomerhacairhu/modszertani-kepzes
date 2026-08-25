---
name: hungarian-edit
description: Szűk hatókörű magyar nyelvi szerkesztés egy fájlon vagy leckén — természetes magyar, nyelvtan, helyesírás, tipográfia, terminológia. Jelentésmegőrző. Nem pedagógiai redesign, nem policy-átírás, nem új tartalom.
argument-hint: <M4.A | "02 Tervezet/.../fájl.md">
disable-model-invocation: true
---

# Magyar nyelvi szerkesztés

**Csak nyelv.** Nem pedagógia, nem policy, nem új tartalom, nem szerkezet.
A norma: `.claude/rules/hungarian-editorial.md` — azt kövesd, ne írj újat.

Cél: `$ARGUMENTS` — egy fájl vagy egy lecke. Ha több fájl kellene, **egyesével**.

## Menet

### 1. Olvasd el a teljes fájlt
Egészben, mielőtt bármit szerkesztesz. Értsd meg, mit tanít, kinek szól, és melyik
rész tanulói, melyik képzői szöveg — a regiszter különbözik.

### 2. Jelöld ki, mihez nyúlsz
Írd fel magadnak a konkrét mondatokat, amik javítandók, és **miért** (melyik szabály).
Ha egy mondathoz nincs megnevezhető szabály, **hagyd békén.**

### 3. Szerkessz mondatonként
Minden szerkesztésnél: **a jelentés nem változhat.** Sem szűkebb, sem tágabb,
sem „világosabb, ezért kicsit más" nem lehet.

Nem nyúlsz hozzá: answer key, számok, küszöbök, szemantikus azonosítók (`M3.2`, `Z.4`),
terméknevek és H5P/Moodle UI-elemek, WCAG-hivatkozások, gyermekvédelmi és adatvédelmi
kikötések tartalma, fájlnevek és linkek.

### 4. A két tiltott lépés

- **Kitalált racionalizálás.** Ha nem érted, mit akart mondani az eredeti mondat,
  **ne írj helyette hihetőt.** Hagyd, és tedd a riportba findingként.
- **Tömeges átírás.** A jó mondat marad. Ha egy bekezdésben minden mondatot
  átírnál, valószínűleg túllépted a hatóköröd — állj meg és kérdezz.

### 5. Olvasd vissza
A `git diff`-et sorról sorra. Menj végig a `.claude/rules/hungarian-editorial.md`
**mind a 10 regressziós mintáján** — az a lista a kánoni, ne fejből dolgozz.

Ha a fájl érdemben rövidült: nézd meg soronként, mi veszett el.

### 6. Ellenőrizd
```bash
python3 tools/content_integrity.py
git diff --check
```
Ha a fájl tanulói szöveget tartalmaz, kérj második szemet: `hungarian-editorial-reviewer`
agent a **módosított** fájlra.

## Jelentés

Mit javítottál (minta szerint csoportosítva, konkrét helyekkel), mit hagytál szándékosan,
és mi az, amit nem értettél és findingként adsz vissza.

**Ez a skill nem commitol és nem pushol** — a commit/push szabály kánoni helye a
CLAUDE.md „Git-biztonság" szakasza.
