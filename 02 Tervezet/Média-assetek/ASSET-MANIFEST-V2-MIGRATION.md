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
| Produkciós deliverable | **906** |
| ebből legyártandó | 404 |
| ebből újrahasznosítás | 7 |
| ebből külső forrás | 6 |
| ebből emberi döntés kell | 1 |
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
| `PRESERVED` | 406 | azonos azonosítóval megmaradt szemantikus asset |
| `CHANGED` | 4 | megmaradt, de a v2 egység-névtérben új azonosítót kapott |
| `DERIVED_NOW` | 320 | a v2-ben egy szülő asset derivatívája (felirat / leirat / alt / hang) |
| `MERGED_INTO_PARENT` | 6 | a szülő asset deklarációjába olvadt, nincs külön deliverable |
| `REUSE` | 10 | explicit újrahasznosítás egy kanonikus assetre |
| `AMBIGUOUS` | 1 | emberi döntés kell a besoroláshoz |
| `CURRENTLY_UNMAPPED_ERROR` | 0 | **hiba** — egyetlen sor sem maradhat itt |

**Összesen: 747 / 747 sor diszpozícionálva.**
Nem egyeztetett (hiba): **0**.

A soronkénti leképezés gépi formában: `asset-migration-map.csv`.

## 5. Felirat/leirat forrásszöveg nélkül

Ezeknél a beszélt asseteknél a jelenlegi lecke nem tartalmaz olyan
összefüggő, idézett szkriptet, amit `@source` blokkba lehetett volna fogni,
ezért a felirat- és leirat-deliverable **szöveg nélkül** áll. A produkció
nem indulhat el rajtuk, amíg a szkript be nem kerül a leckébe — utána a
`@source` blokk és a `source_ref` felvételével a szöveg automatikusan
bekerül a regiszterbe.

| ID | Fájl | Derivatívák |
|---|---|---|
| `M1.3-VID-01` | 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | captions, transcript |
| `M3.2-NAR-02` | 02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md | captions, transcript |

## 6. Nyitott produkciós döntések

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M1.3-VID-01` | 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | A HOOK-dialóg felmondható, VÉGLEGES szövege szerzői jóváhagyást igényel. A lecke a négy mondatot kiírja (SLIDE 1 „Mit látunk?”), de a „Mit hallunk?” sor kifejezetten úgy fogalmaz, hogy „Nagyjából a fenti mondatok” (201. sor) — ez implementációs szabadság, nem jóváhagyott szkript. Amíg a szerző nem hagyja jóvá a szó szerinti szöveget és az nem kerül `@source` blokkba, a felirat és a leirat nem gyártható. Javasolt, a lecke mondataiból összeállított szövegváltozat: Média-assetek/PRODUCTION-DECISIONS.md, D6. |
| `M3-HUB-POSZ-01` | 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md | GYERMEKVÉDELMI FELELŐS DÖNTÉSE. A kérdés nem az, hány lépés „szebb”, hanem hogy ez a poszter ugyanaz az anyag-e, mint a peula kanonikus sablonja. A peulában a lépés-térkép ÖT csomópontos, és a 2. csomópont a nem alkudható instrukció: „Meghallgatom röviden, biztonságosan (nem ígérek 100% titoktartást)” (M3.B-MUNK-01 spec; M3.B 4.3.2). Ugyanez a tiltás a modul kompetenciasorában (§2, 36. sor), a hub operatív szabályában (41. sor), az M3.3 és M3.4 feedbackjeiben, és a KAPU-rubrika BLOKKOLÓ R2 (titoktartás) sorában is szerepel. A hub itt viszont NÉGY lépést ír le (észreveszem → jelzek → nem maradok egyedül → kit vonok be, 250. sor), amiből a titoktartás-lépés és az utánkövetés hiányzik. Eldöntendő: (A) ez a poszter a peula ÖT csomópontos sablonjának a megjelenése, tehát `reuse_of: M3.B-MUNK-01`, és a hub 250. sorának összefoglaló mondatát ehhez kell igazítani; vagy (B) valóban két külön anyag kell, és akkor le kell írni, milyen gyermekvédelmi tartalommal áll a négylépéses változat. Claude nem dönt helyette: a hub látható gyermekvédelmi mondatának átírása szakpolitikai döntés. Részletek: Média-assetek/PRODUCTION-DECISIONS.md, D5. |
| `M3.2-NAR-02` | 02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md | Nincs jóváhagyott narráció-szöveg. A lecke a SLIDE „Input 1” diaszövegét adja meg (a négy kvuca-profil fókuszszavai, az „ugyanúgy peulázol” következménye és a „fejprofil” zárómondat), de kimondottan csak opcionális narrációt jelez, verbatim szkript nélkül. A szöveg megírása és jóváhagyása szerzői feladat; amíg nem kerül `@source` blokkba, a hang, a felirat és a leirat nem gyártható. Javasolt, kizárólag a jelenlegi diaszövegből összeállított szövegváltozat: Média-assetek/PRODUCTION-DECISIONS.md, D7. |
| `M4.2-ILL-01` | 02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md | ⟬SZERZŐI DÖNTÉS⟭ M4 HOOK-formátum. Az M4.1 beszélőfej-videóval nyit, az M4.2/M4.3/M4.4 statikus illusztrációval + narrációval. A korpusz azt mutatja, hogy ez NEM M4-specifikus anomália, hanem a tananyag általános mintája: 17 lecke nyit beszélőfejjel (M1.1, M1.2, M2.1–M2.4, M3.1–M3.4, M4.1, M5.1, M6.1, M6.2, M7.2–M7.4), 15 pedig statikus vizuállal vagy interaktív videóval (M0.1, M0.2, M0.4, M1.3, M1.4, M4.2–M4.4, M5.2, M5.3, M6.3, M7.1, Z.1–Z.3) — az M1, M5, M6 és M7 modulon BELÜL is vegyesen. Eldöntendő: (A) a jelenlegi vegyes nyitás megerősítése (nincs új gyártás, ez az asset R5 alá kerül), vagy (B) M4-en belüli egységesítés, ami három új beszélőfej-videót és három új szkriptet jelent (M4.2/M4.3/M4.4). Részletek: Média-assetek/PRODUCTION-DECISIONS.md, D4. |

Hivatkozott produkciós szabályok / blokkolók:

- **R5** — 258 asset
- **R3** — 118 asset
- **R2** — 28 asset
- **R8** — 2 asset
- **R7** — 1 asset

