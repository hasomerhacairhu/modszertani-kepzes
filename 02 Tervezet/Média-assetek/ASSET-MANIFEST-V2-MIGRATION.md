# Asset Manifest v2 — migrációs és egyeztetési jelentés

> **Generált fájl.** `python3 tools/media_manifest.py build` állítja elő a
> jelenlegi leckefájlok `@asset`/`@source` deklarációiból és a befagyasztott
> történeti leltárból. Ne szerkeszd kézzel.

## 1. Mi változott az architektúrában

| | Régi (v1) | Új (v2) |
|---|---|---|
| Kánoni forrás | befagyasztott `media-merged.json` | a jelenlegi Markdown `@asset`/`@source` deklarációi |
| Szövegek | kinyeréskori pillanatkép (`verbatim`) | minden buildnél élőben a leckéből |
| Helyhivatkozás | sorszám-pillanatkép (`lineRef`) | stabil forrásblokk-ID |
| Kinyerés | AI-workflow (nyugdíjazott) | determinisztikus fordító, hálózat és AI nélkül |
| Újrahasznosítás | utólagos dedup-elemzés | explicit `mode: reuse` + `reuse_of` |
| Elcsúszás észlelése | nincs | `media_manifest.py check` a CI-ban |

## 2. Történeti alap

- **747 sor** a befagyasztott leltárban
- ebből **733 legyártandó** és **14 újrahasznosítás** (a régi `Legyártandó?` besorolás szerint)
- **35 dedup-csoport**

## 3. Jelenlegi v2 leltár

| Mutató | Érték |
|---|--:|
| Szemantikus asset | **415** |
| Produkciós deliverable | **903** |
| ebből legyártandó | 401 |
| ebből újrahasznosítás | 8 |
| ebből külső forrás | 6 |
| Forrásblokk | 123 |
| Feldolgozott fájl | 84 |
| Assetet tartalmazó fájl | 65 |

A két szám **nem összemérhető közvetlenül**: a régi leltár egy táblában
keverte a szemantikus követelményt és a belőle származó akadálymentesítési
deliverable-t (felirat, leirat, alt-szöveg külön sorként). A v2 ezeket
derivatívaként a szülő assethez köti, ezért kevesebb *asset* és külön
számolt *deliverable* keletkezik.

## 4. A 747 történeti sor egyeztetése

| Diszpozíció | Db | Jelentése |
|---|--:|---|
| `PRESERVED` | 403 | azonos azonosítóval megmaradt szemantikus asset |
| `CHANGED` | 3 | megmaradt, de a v2 egység-névtérben új azonosítót kapott |
| `DERIVED_NOW` | 314 | a v2-ben egy szülő asset derivatívája (felirat / leirat / alt / hang) |
| `MERGED_INTO_PARENT` | 6 | a szülő asset deklarációjába olvadt, nincs külön deliverable |
| `REUSE` | 11 | explicit újrahasznosítás egy kanonikus assetre |
| `NO_LONGER_REQUIRED` | 10 | a jelenlegi tananyag már nem igényli |
| `CURRENTLY_UNMAPPED_ERROR` | 0 | **hiba** — egyetlen sor sem maradhat itt |

**Összesen: 747 / 747 sor diszpozícionálva.**
Nem egyeztetett (hiba): **0**.

A soronkénti leképezés gépi formában: `asset-migration-map.csv`.

## 6. Nyitott produkciós döntések

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M1.3-VID-01` | 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | Nyitott (PRODUCTION-DECISIONS.md D11): a kétszereplős, szájszinkronos gyártási út. A dialógushangot az első gyártási körre a projektgazda eldöntötte (2026-10-03, VO D-14: a kanonikus narrátorhang mindkét szerepre, beszélőnként külön szegmensben, a feliratban beszélőjelöléssel); a hangok jogosultsága tartalmilag tisztázott (VO D-01), a formális bizonyíték (R2, V2) függő. A jóváhagyott HOOK-szkriptet (D6) ez a döntés nem nyitja újra. |

Hivatkozott produkciós szabályok / blokkolók:

- **R2** — 118 asset
- **R3** — 116 asset
- **R8** — 2 asset
- **R7** — 1 asset

