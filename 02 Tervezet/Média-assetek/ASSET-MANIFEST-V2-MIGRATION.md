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
| Szemantikus asset | **417** |
| Produkciós deliverable | **903** |
| ebből legyártandó | 403 |
| ebből újrahasznosítás | 7 |
| ebből külső forrás | 6 |
| ebből emberi döntés kell | 1 |
| Forrásblokk | 124 |
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
| `PRESERVED` | 405 | azonos azonosítóval megmaradt szemantikus asset |
| `CHANGED` | 4 | megmaradt, de a v2 egység-névtérben új azonosítót kapott |
| `DERIVED_NOW` | 318 | a v2-ben egy szülő asset derivatívája (felirat / leirat / alt / hang) |
| `MERGED_INTO_PARENT` | 6 | a szülő asset deklarációjába olvadt, nincs külön deliverable |
| `REUSE` | 10 | explicit újrahasznosítás egy kanonikus assetre |
| `NO_LONGER_REQUIRED` | 3 | a jelenlegi tananyag már nem igényli |
| `AMBIGUOUS` | 1 | emberi döntés kell a besoroláshoz |
| `CURRENTLY_UNMAPPED_ERROR` | 0 | **hiba** — egyetlen sor sem maradhat itt |

**Összesen: 747 / 747 sor diszpozícionálva.**
Nem egyeztetett (hiba): **0**.

A soronkénti leképezés gépi formában: `asset-migration-map.csv`.

## 6. Nyitott produkciós döntések

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M3-HUB-POSZ-01` | 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md | GYERMEKVÉDELMI FELELŐS DÖNTÉSE. A kérdés nem az, hány lépés „szebb”, hanem hogy ez a poszter ugyanaz az anyag-e, mint a peula kanonikus sablonja. A peulában a lépés-térkép ÖT csomópontos, és a 2. csomópont a nem alkudható instrukció: „Meghallgatom röviden, biztonságosan (nem ígérek 100% titoktartást)” (M3.B-MUNK-01 spec; M3.B 4.3.2). Ugyanez a tiltás a modul kompetenciasorában (§2, 36. sor), a hub operatív szabályában (41. sor), az M3.3 és M3.4 feedbackjeiben, és a KAPU-rubrika BLOKKOLÓ R2 (titoktartás) sorában is szerepel. A hub itt viszont NÉGY lépést ír le (észreveszem → jelzek → nem maradok egyedül → kit vonok be, 250. sor), amiből a titoktartás-lépés és az utánkövetés hiányzik. Eldöntendő: (A) ez a poszter a peula ÖT csomópontos sablonjának a megjelenése, tehát `reuse_of: M3.B-MUNK-01`, és a hub 250. sorának összefoglaló mondatát ehhez kell igazítani; vagy (B) valóban két külön anyag kell, és akkor le kell írni, milyen gyermekvédelmi tartalommal áll a négylépéses változat. Claude nem dönt helyette: a hub látható gyermekvédelmi mondatának átírása szakpolitikai döntés. Részletek: Média-assetek/PRODUCTION-DECISIONS.md, D5. |
| `M3.4-DIA-01` | 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md | A 3C („Dohány & alkohol – ken vs. magánélet”) tartalom a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és dohányzási szabályzatától függ. A lecke maga mondja ki: „Ennek hiányában ez a tartalmi rész nem élesíthető.” A kódex a kánoni `Emberi jóváhagyás szükséges.md` szerint nyitott szervezeti tétel. Amíg nincs meg, ez az asset nem véglegesíthető — a többi témablokk (3A, 3B) tartalma kész. Dönt: a ken vezetése / a képzésért felelős. |
| `M3.4-EGY-03` | 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md | A 3C („Dohány & alkohol – ken vs. magánélet”) tartalom a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és dohányzási szabályzatától függ. A lecke maga mondja ki: „Ennek hiányában ez a tartalmi rész nem élesíthető.” A kódex a kánoni `Emberi jóváhagyás szükséges.md` szerint nyitott szervezeti tétel. Amíg nincs meg, ez az asset nem véglegesíthető — a többi témablokk (3A, 3B) tartalma kész. Dönt: a ken vezetése / a képzésért felelős. |

Hivatkozott produkciós szabályok / blokkolók:

- **R5** — 258 asset
- **R3** — 117 asset
- **R2** — 28 asset
- **R8** — 2 asset
- **R7** — 1 asset

