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
| Szemantikus asset | **418** |
| Produkciós deliverable | **890** |
| ebből legyártandó | 400 |
| ebből újrahasznosítás | 11 |
| ebből külső forrás | 6 |
| ebből emberi döntés kell | 1 |
| Forrásblokk | 121 |
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
| `PRESERVED` | 402 | azonos azonosítóval megmaradt szemantikus asset |
| `CHANGED` | 4 | megmaradt, de a v2 egység-névtérben új azonosítót kapott |
| `DERIVED_NOW` | 315 | a v2-ben egy szülő asset derivatívája (felirat / leirat / alt / hang) |
| `MERGED_INTO_PARENT` | 11 | a szülő asset deklarációjába olvadt, nincs külön deliverable |
| `REUSE` | 14 | explicit újrahasznosítás egy kanonikus assetre |
| `AMBIGUOUS` | 1 | emberi döntés kell a besoroláshoz |
| `CURRENTLY_UNMAPPED_ERROR` | 0 | **hiba** — egyetlen sor sem maradhat itt |

**Összesen: 747 / 747 sor diszpozícionálva.**
Nem egyeztetett (hiba): **0**.

A soronkénti leképezés gépi formában: `asset-migration-map.csv`.

## 5. Nyitott produkciós döntések

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M3.B-KART-03` | 02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md | A v1 leltárban szereplő spec olyan foglalkozásformára épült, amit a jelenlegi tananyag már nem tartalmaz, és a jelenlegi peula-szöveg nem hivatkozik erre a segédanyagra. Emberi döntés kell arról, hogy szükség van-e rá, és ha igen, milyen tartalommal — a témáért felelős szakmai/gyermekvédelmi jóváhagyóval. Az eredeti v1 megfogalmazás a befagyasztott leltárban változatlanul megvan (M3.B-KART-03). |

Hivatkozott produkciós szabályok / blokkolók:

- **R5** — 244 asset
- **R3** — 118 asset
- **R2** — 21 asset
- **R8** — 11 asset
- **R7** — 1 asset

