# `_legacy/` — a nyugdíjazott v1 média-pipeline

**Ebben a mappában semmi sem kánoni, és semmit nem szabad lefuttatni.**

A jelenlegi rendszer: a `02 Tervezet/` alatti leckefájlok rejtett `@asset` és
`@source` deklarációi → `tools/media_manifest.py` → generált regiszter.
Lásd: [`../README.md`](../README.md).

## Mi van itt

| Fájl | Mi ez |
|---|---|
| `media-merged.json` | A v1 leltár **befagyasztott** végállapota: 747 sor, 35 dedup-csoport, 61 audit-megállapítás, R1–R8 produkciós konvenciók. |
| `dedup.csv` | A 35 dedup-csoport renderelt nézete (a v1 modellből). |
| `audit.csv` | A 61 v1 audit-megállapítás diszpozícióval. |
| `wf-media.js`, `wf-media-supp.js`, `merge-patch.py` | Az eredeti AI-alapú kinyerő workflow és összefésülője. |
| `wf-verbatim.js`, `gen-verbatim-wf.py`, `merge-verbatim.py` | A `verbatim` oszlop egyszeri előállításának lánca. |
| `build-data.py`, `format-media.js` | A v1 renderelők (JSON → XLSX/CSV/MD). |

## Miért maradt meg

Két okból:

1. **Forenzikus bizonyíték.** A `media-merged.json` a 747 történeti sor
   egyeztetésének bemenete: a `python3 tools/media_manifest.py reconcile` ebből
   olvassa ki, mely régi sor melyik v2 assetté vagy deliverable-lé vált. Ha ez a
   fájl eltűnik, a migráció visszaellenőrizhetetlenné válik.
2. **Dokumentáció.** A szkriptek megmutatják, hogyan készült a v1 leltár — és
   azt is, miért nem futtatható újra: a bedrótozott fájllistájuk a 2026-06 előtti
   könyvtárszerkezetre (`MODULOK/`, `Mx_ONLINE_LECKE/`) hivatkozik.

## Miért nem futtatható

A `build-data.py` és a `format-media.js` **rá is írna** a v2 generált
kimeneteire (`assetek.csv`, `Média-asset regiszter.md`, `.xlsx`), és
visszaállítaná bennük a 2026-06-os szöveg-pillanatképet a jelenlegi
tananyagszöveg helyett. Pontosan ezt a driftet szünteti meg a v2.

A kinyerő workflow-k (`wf-*.js`, `merge-patch.py`) ezen felül AI-hívásokra és már
nem létező `/tmp` bemenetekre épültek.

## Mit örökölt a v2 ebből

* **A leltárt** — mind a 747 sor kapott diszpozíciót, lásd
  [`../asset-migration-map.csv`](../asset-migration-map.csv) és
  [`../ASSET-MANIFEST-V2-MIGRATION.md`](../ASSET-MANIFEST-V2-MIGRATION.md).
* **A dedup-elemzést** — a v2 explicit `mode: reuse` + `reuse_of` párként
  kódolja, nem utólagos hasonlóság-elemzésként.
* **Az R1–R8 produkciós konvenciókat** — a v2 assetek `production_rules` /
  `blockers` mezőből hivatkoznak rájuk, a szövegük innen származik.

## Mit NEM örökölt

A `verbatim` és a `lineRef` oszlopokat. Ezek a kinyerés pillanatának
pillanatképei voltak, és minden későbbi tananyag-szerkesztéssel csúsztak. A v2-ben
a felmondandó szöveg és az alt-szöveg **minden buildnél élőben** a leckefájl
`@source` blokkjából jön.
