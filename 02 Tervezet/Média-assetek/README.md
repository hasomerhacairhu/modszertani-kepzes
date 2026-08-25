# 🎬 Média-asset regiszter

Ez a mappa a `02 Tervezet/` tananyaghoz **legyártandó média-assetek** teljes leltárát tartalmazza: narráció, AI beszélő-fej videó, animált diagram, illusztráció, ikon, fotó/illusztráció, hang + a hozzájuk tartozó **szöveges ekvivalensek** (felirat, leirat, alt-szöveg) és **print/fizikai** anyagok.

## Fájlok

| Fájl | Mire való |
|---|---|
| **`Média-asset regiszter.xlsx`** | **Elsődleges, data-driven formátum.** 6 munkalap: Összesítő · Assetek (szűrhető, fagyasztott fejléc) · Dedup-térkép · Audit · Médiamentes fájlok · Produkciós konvenciók |
| `assetek.csv` | A teljes asset-tábla (748 sor × 21 oszlop), gépi feldolgozáshoz |
| `audit.csv` | A 61 audit-megállapítás diszpozícióval |
| `dedup.csv` | A 35 dedup-csoport (újrahasznosítások) |
| `Média-asset regiszter.md` | Ember-olvasható kísérő (ugyanaz, markdownban) |
| `_build/` | A reprodukciós pipeline (lásd lent) |

## „Felmondandó / generálandó szöveg" oszlop

Az **Assetek** munkalap (és az `assetek.csv`) tartalmazza a **szó szerinti, gyártásra kész szöveget** — nem kell a forrásfájlokban keresgélni. A `Felmondandó / generálandó szöveg (verbatim)` oszlopban:
- **narráció** → a teljes felmondandó/TTS-be tölthető szkript szó szerint;
- **felirat / leirat** → ugyanaz a szöveg (a felirat a narrációt szó szerint közli);
- **alt-szöveg** → a kész alt-szöveg (a dekoratív elemeknél szándékosan üres).

462 szöveg-asset kitöltve a forrásból; szűrd az `Asset-típus = narráció` sorokra, ha csak a felmondandó szövegek kellenek.

## Számok

- **748 asset-sor**, ~712 ténylegesen legyártandó (35 dedup-csoport újrahasznosítás)
- **74 / 74 forrásfájl lefedve** (65 assetekkel + 9 ellenőrzötten médiamentes)
- **61 audit-megállapítás mind diszpozícionálva** (16 blokkoló, 23 fontos, 22 javasolt)
- **8 produkciós konvenció (R1–R8):** AI-jelölés · avatar/hang IP · narrátor hang-bible · védjegy-semlegesség · ikon/karakter-batch · szín-szótár · függőségek · GDPR/képmás

## Ami még emberi/szervezeti döntésre vár (⟬KITÖLTENDŐ⟭)

- **R2** AI-avatar/hang licenc-igazolás (generátor, kereskedelmi licenc, voice-talent release)
- **R3** konkrét TTS-motor / voice-ID (vagy emberi felmondó)
- **R5** someres hex-paletta
- **J19** M4 HOOK-formátum szerzői megerősítése

## Reprodukció (`_build/`)

**A kánoni adat a `_build/media-merged.json`.** Ebből a regiszter minden kimenete bármikor újragenerálható.

**Élő, futtatható lépések:**

1. **`format-media.js`** `media-merged.json` → `Média-asset regiszter.md`
2. **`build-data.py`** `media-merged.json` → `.xlsx` + 3 `.csv` (openpyxl szükséges)

Mindkettő **determinisztikus**: kétszeri futtatásra a `.md` és a három `.csv` bitre azonos. (Az `.xlsx` egyetlen belső mezője, a `docProps/core.xml` időbélyege futásonként eltér — a munkalapok tartalma azonos.)

> A `.csv`-k a több soros idézett mezőkben szándékosan CRLF-et tartalmaznak, mert a generátor ezt írja. A repo `.gitattributes`-ban `*.csv -text`, hogy ezt semmi ne normalizálja — különben minden regenerálás ál-diffet okoz.

**Történeti, már NEM futtatható lépések** (a `media-merged.json` ezek kifagyasztott eredménye; megőrzésük dokumentációs célú):

* **`wf-media.js` + `wf-media-supp.js`** — az eredeti kinyerő workflow-k. A bennük bedrótozott fájllista a **2026-06 előtti** könyvtárszerkezetre hivatkozik (`MODULOK/`, `Mx_ONLINE_LECKE/`), ezért a jelenlegi korpusz ellen nem futnak.
* **`merge-patch.py`** — a workflow-outputokat fésülte össze; efemer `/tmp` bemenetekből dolgozott, amelyek már nincsenek meg.
* **`wf-verbatim.js`, `gen-verbatim-wf.py`, `merge-verbatim.py`** — a verbatim-oszlop előállításának egyszeri lánca.

Ha a kinyerést valaha újra kell futtatni, a fájllistát a jelenlegi `02 Tervezet/Modulok/` szerkezetre kell átírni.

Gyors újra-render a meglévő `media-merged.json`-ból (a `Média-assetek/` mappából futtatva):

```bash
node "_build/format-media.js" "Média-asset regiszter.md" "_build/media-merged.json"
python3 "_build/build-data.py" "_build/media-merged.json"
```
