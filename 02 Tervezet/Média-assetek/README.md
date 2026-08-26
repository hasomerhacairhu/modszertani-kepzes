# 🎬 Média-asset regiszter

Ez a mappa a `02 Tervezet/` tananyaghoz **legyártandó média-assetek** teljes leltárát tartalmazza: narráció, AI beszélő-fej videó, animált diagram, illusztráció, ikon, fotó/illusztráció, hang + a hozzájuk tartozó **szöveges ekvivalensek** (felirat, leirat, alt-szöveg) és **print/fizikai** anyagok.

## Fájlok

| Fájl | Mire való |
|---|---|
| **`Média-asset regiszter.xlsx`** | **Elsődleges, data-driven formátum.** 6 munkalap: Összesítő · Assetek (szűrhető, fagyasztott fejléc) · Dedup-térkép · Audit · Médiamentes fájlok · Produkciós konvenciók |
| `assetek.csv` | A teljes asset-tábla (747 sor × 21 oszlop), gépi feldolgozáshoz |
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

- **747 asset-sor**, ebből **733 ténylegesen legyártandó** és **14 újrahasznosítás** (a `Legyártandó?` oszlop besorolása)
  - a **35 dedup-csoport ≠ 35 nem gyártandó sor**: egy csoport gyakran ugyanarra az EGY assetre mutató több forráshivatkozás, ilyenkor egyetlen sor sem esik ki. Egy sor csak akkor „újrahasznosítás”, ha a csupasz ID-je eltér a csoport csupasz kanonikus ID-jétől, **és** a hivatkozó dedup-tag ugyanarra a fájl-hatókörre mutat, mint a sor (a hub és a lecke ID-tere ütközik: a hub `M1.1-ALT-01`-e más asset, mint az M1.1 lecke `M1.1-ALT-01` sora).
  - ⚠️ **Nyitott, emberi döntést igénylő maradék:** négy sor (`M3.F-MUNK-01`, `M3.F-MUNK-02`, `Z.A-POSZ-01`, `Z.A-POSZ-02`) olyan dedup-csoportban van, ahol a tag-ID-k **nem hordoznak fájl-hatókört**, a csoport `reason` szövege viszont maga figyelmeztet az ID-ütközésre az áttekintő és a részletes fájl között. Ezek besorolása gépileg nem dönthető el — szerzői döntés kell hozzá.
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

Mindkettő **determinisztikus**: kétszeri futtatásra a három `.csv` bitre azonos, és a `.md` is az, ha a generálási dátumot rögzíted:

```bash
MEDIA_BUILD_DATE=2026-08-26 node "_build/format-media.js" "Média-asset regiszter.md" "_build/media-merged.json"
```

Enélkül a `.md` fejlécében a „Generálva” dátum a mai napra frissül — ez az egyetlen, szándékos eltérés. Az `.xlsx`-nél a `docProps/core.xml` időbélyege tér el futásonként; a munkalapok tartalma azonos.

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
