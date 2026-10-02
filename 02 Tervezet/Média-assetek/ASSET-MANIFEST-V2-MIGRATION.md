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
| Produkciós deliverable | **901** |
| ebből legyártandó | 403 |
| ebből újrahasznosítás | 8 |
| ebből külső forrás | 6 |
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
| `REUSE` | 11 | explicit újrahasznosítás egy kanonikus assetre |
| `NO_LONGER_REQUIRED` | 3 | a jelenlegi tananyag már nem igényli |
| `CURRENTLY_UNMAPPED_ERROR` | 0 | **hiba** — egyetlen sor sem maradhat itt |

**Összesen: 747 / 747 sor diszpozícionálva.**
Nem egyeztetett (hiba): **0**.

A soronkénti leképezés gépi formában: `asset-migration-map.csv`.

## 6. Nyitott produkciós döntések

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M1.3-VID-01` | 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | Nyitott (PRODUCTION-DECISIONS.md D11): a két madrich dialógushangja, a hangok jogosultsága (R2, V2) és a kétszereplős, szájszinkronos gyártási út. A jóváhagyott HOOK-szkriptet (D6) ez a döntés nem nyitja újra. |
| `M2.3-EGY-02` | 02 Tervezet/Modulok/M2/Online leckék/M2.3 – Somer 3 pillére – mini-kapszula.md | Nyitott mozgalmi döntések az `Emberi jóváhagyás szükséges.md` szerint: HUM-SOMER-01 (Izrael/cionizmus és béke/palesztin dimenzió – a KERET-dia és a C-ág megfogalmazása) és HUM-SOMER-03 (a hagshama helyi megfogalmazása – a ZÁRÓ OLDAL). Amíg nincsenek lezárva, az asset learner-facing szövege nem véglegesíthető. Jóváhagyó: helyi mozgalmi/ideológiai felelős (HUM-SOMER-01), mozgalmi/ideológiai felelős (HUM-SOMER-03). |
| `M2.3-NAR-02` | 02 Tervezet/Modulok/M2/Online leckék/M2.3 – Somer 3 pillére – mini-kapszula.md | Nyitott mozgalmi döntés az `Emberi jóváhagyás szükséges.md` szerint: HUM-SOMER-01 (Izrael/cionizmus és béke/palesztin dimenzió – a narráció cionizmus-mondata: „kritikus, békét kereső gondolkodásunk”). Amíg nincs lezárva, a narráció nem véglegesíthető. Jóváhagyó: helyi mozgalmi/ideológiai felelős. |
| `M2.3-VID-02` | 02 Tervezet/Modulok/M2/Online leckék/M2.3 – Somer 3 pillére – mini-kapszula.md | Nyitott mozgalmi döntés az `Emberi jóváhagyás szükséges.md` szerint: HUM-SOMER-03 (a hagshama helyi megfogalmazása – az outro a hagshama-gondolatra épül). Amíg nincs lezárva, az asset nem véglegesíthető. Jóváhagyó: mozgalmi/ideológiai felelős. |
| `M2.B-POSZ-01` | 02 Tervezet/Modulok/M2/Peulák/M2.B – Somer-értékek a gyakorlatban – döntések, amelyek tanítanak.md | Nyitott mozgalmi döntés az `Emberi jóváhagyás szükséges.md` szerint: HUM-SOMER-01 (Izrael/cionizmus és béke/palesztin dimenzió – a Cionizmus-poszter opcionális kulcsszavas emlékeztetője: „a zsidó–palesztin békés együttélés keresésével is”). Amíg nincs lezárva, az asset learner-facing szövege nem véglegesíthető. Jóváhagyó: helyi mozgalmi/ideológiai felelős. |
| `M3-HUB-POSZ-02` | 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md | Az A/B sarok nem része a kanonikus M3.B peulának (az M3.B egyszavas körrel nyit, passzolási lehetőséggel). Ha a gyakorlat marad, az M3.B-be jóváhagyott állításkészlet és időkeret kell, a biztonsági keret és a passz lehetőségének kimondása után; ha nem, az asset kivezethető. A döntés nyitott; jóváhagyója még nincs rögzítve. |
| `M3.4-DIA-01` | 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md | A 3C („Dohány & alkohol – ken kontra magánélet”) tartalom a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és dohányzási szabályzatától függ. A lecke maga mondja ki: „Ennek hiányában ez a tartalmi rész nem élesíthető.” A kódex a kánoni `Emberi jóváhagyás szükséges.md` szerint nyitott szervezeti tétel (HUM-SAFE-04). Amíg nincs meg, ez az asset nem véglegesíthető — a többi témablokk (3A, 3B) tartalma kész. Dönt: a HUM-SAFE-04 jóváhagyói (Emberi jóváhagyás szükséges.md); hogy a szabály a ken vagy a szervezet szintjén születik, maga is nyitott kérdés. |
| `M3.4-EGY-03` | 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md | A 3C („Dohány & alkohol – ken kontra magánélet”) tartalom a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és dohányzási szabályzatától függ. A lecke maga mondja ki: „Ennek hiányában ez a tartalmi rész nem élesíthető.” A kódex a kánoni `Emberi jóváhagyás szükséges.md` szerint nyitott szervezeti tétel (HUM-SAFE-04). Amíg nincs meg, ez az asset nem véglegesíthető — a kártyakészletből a 6–8. kártya és a hozzájuk tartozó visszajelzés függ a kódextől. Dönt: a HUM-SAFE-04 jóváhagyói (Emberi jóváhagyás szükséges.md); hogy a szabály a ken vagy a szervezet szintjén születik, maga is nyitott kérdés. |

Hivatkozott produkciós szabályok / blokkolók:

- **R5** — 258 asset
- **R2** — 119 asset
- **R3** — 117 asset
- **R8** — 2 asset
- **R7** — 1 asset

