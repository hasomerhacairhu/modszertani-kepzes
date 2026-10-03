---
name: hungarian-edit
description: Szűk hatókörű magyar nyelvi szerkesztés egy fájlon vagy leckén — természetes magyar, nyelvtan, helyesírás, tipográfia, terminológia. Jelentésmegőrző. Nem pedagógiai redesign, nem policy-átírás, nem új tartalom.
argument-hint: <M4.A | "02 Tervezet/.../fájl.md">
disable-model-invocation: true
---

# Magyar nyelvi szerkesztés

**Csak nyelv.** Nem pedagógia, nem policy, nem új tartalom, nem szerkezet.
A norma: `.claude/rules/hungarian-editorial.md` — azt kövesd, ne írj újat.

Cél: `$ARGUMENTS` — egy fájl. Azonosítónál (`M4.A`, `Z.4`) Glob-bal keresd meg a fájlt a
modulon belül; ha nem egyértelmű, kérdezz. Több fájl **egyesével**, külön futásban.

## Menet

### 1. Olvasd el a teljes fájlt
Egészben, mielőtt bármit szerkesztesz. Értsd meg, mit tanít, kinek szól, és melyik
rész tanulói, melyik képzői szöveg — a regiszter különbözik.

### 2. Jelöld ki, mihez nyúlsz
Írd fel magadnak a konkrét mondatokat, amik javítandók, és **miért** (melyik szabály).
Ha egy mondathoz nincs megnevezhető szabály, **hagyd békén.**

### 3. Szerkessz mondatonként (`Edit` eszközzel)
Minden szerkesztésnél: **a jelentés nem változhat.** Sem szűkebb, sem tágabb,
sem „világosabb, ezért kicsit más" nem lehet.

Nem nyúlsz hozzá: answer key, számok, küszöbök, szemantikus azonosítók (`M3.2`, `Z.4`),
terméknevek és H5P/Moodle UI-elemek, WCAG-hivatkozások, gyermekvédelmi és adatvédelmi
kikötések tartalma, fájlnevek és linkek.

**Metaadat-blokkok:**
- `<!-- @asset {…} -->`: csak JSON-szöveg értékét javíthatod; kulcs, szerkezet, ID nem
  változik, és az érték belsejébe nem kerülhet nyers `"` (a magyar `„…”` idézőjel rendben van).
- `<!-- @source … -->` narráció: nyelvi javítás megengedett, de a forrás-hash és a kész
  hangfelvétel ezzel elavul — a jelentésben sorold fel az érintett asset-ID-kat
  („újrarenderelés kell”).

### 4. A két tiltott lépés

- **Kitalált racionalizálás.** Ha nem érted, mit akart mondani az eredeti mondat,
  **ne írj helyette hihetőt.** Hagyd, és tedd a riportba findingként.
- **Tömeges átírás.** A jó mondat marad. Ha egy bekezdésben minden mondatot
  átírnál, valószínűleg túllépted a hatóköröd — állj meg és kérdezz.

### 5. Olvasd vissza
A `git diff`-et sorról sorra. Menj végig a `.claude/rules/hungarian-editorial.md`
**mind a 10 regressziós mintáján** — az a lista a kánoni, ne fejből dolgozz.
Ha a fájl érdemben rövidült: nézd meg soronként, mi veszett el.

### 6. Második szem, majd lezárás — ebben a sorrendben
1. Tanulói szövegnél: `hungarian-editorial-reviewer` a **diff-hunkokra** (a promptban kapja
   meg őket; csak a módosított sorokat nézze). A megerősített észrevételeket javítsd.
2. `python3 tools/content_integrity.py` és `git diff --check`.
3. A teljes `git diff` visszaolvasása.
4. Látható szöveg változott → egyszer `python3 tools/test_media_manifest.py --pin-visible
   "<fájl-ID>: nyelvi javítás"` (rákérdez); az `approved-visible-text.json`-t kézzel soha ne
   szerkeszd.
5. `@asset`/`@source` változott → `python3 tools/media_manifest.py build`, majd `check`.
6. `/release-check` — utolsóként.

## Jelentés

Mit javítottál (minta szerint csoportosítva, konkrét helyekkel), mit hagytál szándékosan,
melyik asset-ID-t kell újrarenderelni, és mi az, amit nem értettél és findingként adsz vissza
(a `.claude/finding-format.md` szerint).

**Ez a skill nem commitol és nem pushol** — a commit/push szabály kánoni helye a
CLAUDE.md „Git-biztonság" szakasza.
