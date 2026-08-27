# 🎬 Média-asset regiszter — v2

A teljes produkciós leltár: narráció, videó, animáció, illusztráció, ikon, fotó,
hang, a hozzájuk tartozó **szöveges ekvivalensek** (felirat, leirat, alt-szöveg),
valamint a **nyomtatható és letölthető** anyagok.

## Mi a kánoni forrás?

**A jelenlegi leckefájlok.** Az asset-igényeket a `02 Tervezet/` alatti Markdown
tartalmazza, rejtett HTML-kommentekben:

* `<!-- @asset { … } -->` — egy szemantikus asset-követelmény;
* `<!-- @source { … } --> … <!-- @endsource -->` — a szó szerint legyártandó
  szöveg (narráció, alt-szöveg) ott, ahol a leckében áll;
* `<!-- @asset-free { "reason": … } -->` — „ebben a fájlban nincs legyártandó
  anyag”, indoklással.

Ezek a deklarációk **nem látszanak** a renderelt Markdownban, viszont a leckével
együtt mozognak, és a fordító minden buildnél **élőben** olvassa ki belőlük a
szöveget. Ha egy narráció megváltozik a leckében, a következő build automatikusan
az új szöveget viszi a regiszterbe — nincs többé kifagyasztott pillanatkép.

## Mi generált?

Ezek a fájlok **kézzel nem szerkeszthetők**:

| Fájl | Mire való |
|---|---|
| `_build/media-manifest.v2.json` | A kánoni gépi manifeszt: minden asset, forrásszöveg, hash, deliverable. |
| `assetek.csv` | Szemantikus assetek — amit a szerző megfogalmaz. |
| `deliverable-ek.csv` | Produkciós deliverable-ek — amit ténylegesen le kell gyártani. |
| `ujrahasznositas.csv` | Explicit újrahasznosítások (`mode: reuse`). |
| `Média-asset regiszter.md` | Ember-olvasható áttekintő. |
| `Média-asset regiszter.xlsx` | Produkciós munkafüzet (7 munkalap, szűrhető). |
| `asset-migration-map.csv` | A 747 történeti sor soronkénti diszpozíciója. |
| `ASSET-MANIFEST-V2-MIGRATION.md` | A migráció összefoglalója. |

## Parancsok

```bash
python3 tools/media_manifest.py build      # minden generált kimenet újraépítése
python3 tools/media_manifest.py validate   # séma, hivatkozások, akadálymentesítés
python3 tools/media_manifest.py check      # elcsúszott generált kimenet keresése (CI)
python3 tools/media_manifest.py lint       # lehetséges deklarálatlan asset
python3 tools/media_manifest.py stats      # jelenlegi darabszámok
python3 tools/media_manifest.py reconcile  # a 747 történeti sor egyeztetése
python3 tools/media_manifest.py diff main  # mi változott egy git ref óta
```

A build **offline és determinisztikus**: nincs benne hálózat, AI-hívás vagy
dátum. Ugyanaz a Git-fa mindig bitre azonos kimenetet ad.

## Hogyan csinálom…?

Részletes, másolható példák: [`ASSET-AUTHORING.md`](./ASSET-AUTHORING.md).

**Új assetet veszek fel** → beírsz egy `@asset` blokkot abba a leckefájlba, ahol
az asset megjelenik, majd `build`.

**Megváltoztatom a felmondandó szöveget** → a leckében szerkeszted a `@source`
blokk **belsejét** (a rendes tananyagszöveget), majd `build`. Sehol máshol nem
kell hozzányúlni: a felirat, a leirat és a hang deliverable ugyanabból a
forrásból jön.

**Alt-szöveget adok vagy módosítok** → a leckében írod meg, `@source` blokkban
(`"kind": "alt-text"`), és `a11y.alt_source_ref`-fel hivatkozol rá. Ha egy
blokkban több alt van, a hivatkozás `#1`, `#2`… sorszámmal választ közülük.

**Újrahasznosítok egy assetet** → `"mode": "reuse"` és `"reuse_of": "<másik ID>"`.
Az újrahasznosított asset **nem gyárt új deliverable-t**.

**Új leckét adok hozzá** → csak leteszed az `.md` fájlt a `02 Tervezet/` alá.
A felderítés automatikus, nincs bedrótozott fájllista.

**Ellenőrzöm commit előtt** → `python3 tools/media_manifest.py check`. Ha
elcsúszott, futtass `build`-et, és commitold a generált fájlokat is.

## ID-konvenció

`<egység>-<TÍPUS>-<sorszám>`, például `M5.1-VID-01`.

Az **egység** a fájl útvonalából származik, és a fordító ellenőrzi:

| Fájl | Egység |
|---|---|
| `Modulok/M5/Online leckék/M5.1 – …md` | `M5.1` |
| `Modulok/M5/Peulák/M5.A – …md` | `M5.A` |
| `Modulok/M5/M5 – …md` (modul-áttekintő) | `M5-HUB` |
| `Modulok/M5/M5 – Kapu – …md` | `M5-KAPU` |

Ez oldja fel a v1 ismert **ID-ütközését**: a modul-áttekintőben szereplő
`M1.1-VID-01` korábban ugyanazt az azonosítót viselte, mint a lecke saját sora,
pedig más sorról volt szó. Most `M1-HUB-…`, és ha ugyanaz a média, akkor
explicit `reuse_of`.

A **deliverable-ek** azonosítója az assetből származik: `M5.1-VID-01`,
`M5.1-VID-01::CAPTIONS`, `M5.1-VID-01::TRANSCRIPT`. Az asset-ID nem tartalmazhat
`::`-t, így nem ütközhetnek.

## Mi a `_legacy/`?

A nyugdíjazott v1 pipeline és a befagyasztott `media-merged.json`. **Nem kánoni,
és nem futtatható** — a részletek: [`_legacy/README.md`](./_legacy/README.md).
Megőrizzük, mert a 747 történeti sor egyeztetése ebből dolgozik.

## Mi blokkolja még a produkciót? (⟬KITÖLTENDŐ⟭)

A regiszter naprakész — a **gyártás** viszont nem indulhat, amíg ezek nyitva
vannak. Az érintett assetek a `blockers` mezőben hivatkoznak rájuk, és a
munkafüzet *Nyitott döntések* lapján is megjelennek. A szabályok teljes szövege a
munkafüzet *Produkciós konvenciók* lapján olvasható.

| Kapu | Mi hiányzik | Mit blokkol |
|---|---|---|
| **R2** — AI-avatar / AI-hang IP-megfelelőség | a generátor neve, a kereskedelmi licenc és a voice-talent release igazolása | a beszélőfej- és karaktervideók |
| **R3** — Narrátor hang-bible | a konkrét TTS-motor / voice-ID, vagy az emberi felmondó | minden narráció, hang és videó |
| **R5** — Ikon- és karakter-batch + lock | a rögzített **someres hex-paletta** (a szabály ezen belül tartja nyitva) | minden tervezett vizuál és nyomtatott anyag |
| **R7** — Produkciós függőségek | a véglegesített Moodle-felület | a kurzusfelületet ábrázoló képernyőkép |
| **R8** — GDPR / képmás-védelem | felhasználási jogcím, attribúció, anonimizálás | a fotó- és stock-assetek |

Nem blokkoló, de minden vizuális munkára érvényes konvenció: **R1** (egységes
AI-jelölés), **R4** (védjegy-semlegesség), **R6** (szín-szótár).

Egy asset **emberi döntésre vár** (`mode: human-decision`) — lásd a *Nyitott
döntések* munkalapot és az [`ASSET-MANIFEST-V2-MIGRATION.md`](./ASSET-MANIFEST-V2-MIGRATION.md)
5. szakaszát.

> ⚠️ **Tisztázandó a v1 README-ből:** az korábbi olvasat egy `J19` hivatkozást is
> nyitott kapuként sorolt fel („az M4 HOOK-formátum szerzői megerősítése”).
> Ilyen azonosító **nincs** a befagyasztott adathalmazban (sem a 8 produkciós
> szabály, sem a 61 audit-megállapítás között), ezért a v2 nem hivatkozik rá.
> Ha a kapu valós, szerzői megerősítés kell hozzá — ez nem gépi kérdés.

Ezek **szervezeti és jogi döntések**. A fordító csak nyilvántartja őket; nem old
fel egyet sem.

> A `content_integrity.py` `check_active_spec` ellenőrzése szándékosan kihagyja
> ezt a mappát, mert generált kimeneteket tartalmaz. A leckefájlokba írt
> deklarációkra viszont **teljes mértékben érvényes** — a migráció ezért nem
> vitte tovább a v1 spec-mezőkből a visszavont megfogalmazásokat.
