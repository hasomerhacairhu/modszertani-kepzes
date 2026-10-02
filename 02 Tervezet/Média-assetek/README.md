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
együtt mozognak. Amit `@source` blokk köt — a felmondandó narráció és a
forráshoz kötött alt-szöveg —, azt a fordító **minden buildnél élőben** olvassa
ki a leckéből: ha a szöveg megváltozik, a következő build automatikusan az újat
viszi a regiszterbe, és a `check` megbukik, amíg nem építed újra. Nincs többé
kifagyasztott pillanatkép.

Két dokumentált kivétel-osztály marad:

* **Nincs még szkript.** Ha egy beszélt asset nem old fel `source_ref`-et, a
  státusza `blokkolt` (`MISSING_SPOKEN_SOURCE`), és a felirat/leirat
  deliverable-je is az — ezt egyetlen produkciós szabály feloldása és kézzel
  beírt `status` sem írja felül.
* **Nem fogható forrásblokkba.** Ha az alt pontos körbezárása megváltoztatná a
  renderelt Markdown szerkezetét (például kettévágna egy bekezdést), az asset
  `a11y.alt_note`-tal tartja meg az alt-követelményt. Ilyenkor az alt **továbbra
  is kötelező deliverable**, de a szövege nem esik az élő elcsúszás-ellenőrzés
  alá — a mező kimondja, hogy melyik altról van szó és miért.

Ezek kivételek, nem a szabály: az architektúra alapja továbbra is az, hogy a
szöveg egy helyen, a leckében él.

## Mi generált?

Ezek a fájlok **kézzel nem szerkeszthetők**:

| Fájl | Mire való |
|---|---|
| `_build/media-manifest.v2.json` | A kánoni gépi manifeszt: minden asset, forrásszöveg, hash, deliverable. |
| `assetek.csv` | Szemantikus assetek — amit a szerző megfogalmaz. |
| `deliverable-ek.csv` | Produkciós deliverable-ek — amit ténylegesen le kell gyártani. |
| `ujrahasznositas.csv` | Explicit újrahasznosítások (`mode: reuse`). |
| `Média-asset regiszter.md` | Ember-olvasható áttekintő. |
| `Média-asset regiszter.xlsx` | Produkciós munkafüzet (9 munkalap, szűrhető): *Összesítő · Assetek · Deliverable-ek · Újrahasznosítás · **Emberi döntések** · **Blokkolt assetek** · Migráció · Produkciós konvenciók · Asset nélküli fájlok*. |
| `asset-migration-map.csv` | A 747 történeti sor soronkénti diszpozíciója. |
| `MEDIA-PRODUCTION-PLAN.md` | Produkciós köteg-terv: mi gyártható most, mi mire vár, milyen sorrendben éri meg haladni, és családonként melyik a pilot. |
| `media-production-plan.csv` | Ugyanaz soronként, deliverable-szinten — ez a produkciós munkalista. |
| `ASSET-MANIFEST-V2-MIGRATION.md` | A migráció összefoglalója. |

### Kánoni bemenet, nem generált

| Fájl | Mire való |
|---|---|
| `produkcios-szabalyok.json` | Az R1–R8 produkciós konvenciók szövege. **Kézzel karbantartott:** amikor egy szervezeti vagy jogi döntés megszületik, itt kell kivezetni a `⟬KITÖLTENDŐ⟭` jelölést. A fordító ebből dolgozik, nem a befagyasztott v1 pillanatképből. |
| [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) | A gyártás elindításához hiányzó **emberi döntések** — egy helyen, döntésenként egy kérdéssel, opciókkal és hatásszámmal. Kézzel karbantartott. |
| [`RELEASE-MEDIA-STATUS.md`](./RELEASE-MEDIA-STATUS.md) | A release-szükségesség és a gyártási blokkoltság külön kezelése; az M0+M1 staging média-fallbackjei. |
| [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) | Az R3 végrehajtási lapja: nyelv, regiszter, tempó, kiejtés, felirat-viszony, kimenet. A szintetikus út és az ElevenLabs már eldőlt; a konkrét voice-ID, modell, reprodukciós beállítások és kiejtési szótár maradt nyitva. |
| [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) | Az R5 lock-lapja: mi kötelező már most, mi következetes de nem hivatalos, és mi hiányzott. A D1 2026-10-02-án projektgazdai döntéssel lezárult; a mezők kitöltve. |
| [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) | R2/R8 bizonyíték-nyilvántartás, a `HUM-MEDIA-02` alkapuinak (J1, J2, V1, V3) felelős- és bizonyíték-mezőjével. Nem hoz jogi következtetést, és személyes adatot nem tartalmaz. |
| [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) | A D1 előkészítése: a mozgalom **hivatalos arculati kézikönyvéből** kinyert paletta és szabályok, számított WCAG-kontrasztokkal, és két jóváhagyható változat. A D1 2026-10-02-án a **B változattal** lezárult (projektgazdai döntés); ez a lap a tananyag-produkció stílus-tokenje. |
| [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) | A teljes gyártási stack előkészítése: vizuális rendszer, hang, beszélőfej, karakter-jelenet, formátumok, elnevezés, provenance, akadálymentesítés, jogi bizonyíték, nyitott döntések. |
| [`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md) | A D2 tesztanyaga: három meglévő narráció, amelyen a hangjelöltek összemérhetők. Másolat, nem kánon. |
| [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) | A D2 utolsó kérdésének végrehajtható terve: **VOICE-SRC-01 vs. VOICE-SRC-02**, hat minta, beállítások, kiejtési figyelőlista, pontozólap. **A két ElevenLabs hang még nincs létrehozva** (a két név forrás-beszélőt jelöl), ezért a teszt még nem futtatható. |
| [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) | Családonként egy pilot-brief: pontos forrás, promptok, elfogadási és bukási feltételek, fájlelnevezés. **A hat vizuális és nyomtatott pilot kapuja a D1 volt, amely 2026-10-02-án lezárult; a hangos és videós pilotokon (P-NAR, P-VID, P-KAR) továbbra is nyitott kapu ül.** |

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

A `build` a köteg-tervet is előállítja: [`MEDIA-PRODUCTION-PLAN.md`](./MEDIA-PRODUCTION-PLAN.md)
és `media-production-plan.csv`. A terv **nem második igazság**: minden száma a
jelenlegi manifesztből származik, a kötegek pedig abból, hogy melyik asseten
milyen kapu ül.

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
(`"kind": "alt-text"`), és `a11y.alt_source_ref`-fel hivatkozol rá. Minden alt
kapja meg a **saját blokkját**, abban **pontosan egy** `„…”` idézettel; a
hivatkozás mindig `#1`. Két idézet egy blokkban validációs hiba — a fordító nem
választ helyetted. Ha az alt nem zárható körbe a renderelt szerkezet
megváltoztatása nélkül, `a11y.alt_note`-ot használsz; a részleteket lásd az
[`ASSET-AUTHORING.md`](./ASSET-AUTHORING.md) 2.4 pontjában.

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

## Mi blokkolja még a produkciót?

A regiszter naprakész — a **gyártás** viszont nem indulhat, amíg ezek nyitva
vannak. Az érintett assetek a `blockers` mezőben hivatkoznak rájuk, és a
munkafüzet *Blokkolt assetek* lapján is megjelennek. A szabályok teljes szövege a
munkafüzet *Produkciós konvenciók* lapján olvasható.

| Kapu | Mi hiányzik | Mit blokkol |
|---|---|---|
| **R2** — AI-avatar / AI-hang IP-megfelelőség | a generátor neve, a kereskedelmi licenc és a voice-talent release igazolása | a 21 beszélőfej-videó, az 5 AI karakter-jelenet és a belőlük kivett 2 állókép, az AI karakter-B-roll (`M1.1-VID-02`), valamint — mivel a felmondás szintetikus — mind a 90 narráció; összesen 119 asset (29 vizuális + 90 narráció) |
| **R3** — Narrátor hang-bible | a konkrét ElevenLabs voice-ID, modell-azonosító, reprodukciós beállítások és kiejtési szótár | minden narráció, hang és videó |
| **R5** — Ikon- és karakter-batch + lock | **nincs — a D1 2026-10-02-án lezárult** (projektgazdai döntés: a hivatalos someres hex-paletta és a B változat, [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D1); az asset-szintű R5-blokkolók kivezetése a manifesztben külön lépés | a kivezetésig: minden tervezett vizuál és nyomtatott anyag, valamint az AI karakter-jelenetek |
| **R7** — Produkciós függőségek | a véglegesített Moodle-felület | a kurzusfelületet ábrázoló képernyőkép |
| **R8** — GDPR / képmás-védelem | valós fotón/képernyőképen minden azonosítható személy és kézírás anonimizálása vagy kikeretezése; **felismerhető kiskorúnál előre dokumentált szülői hozzájárulás**; képernyőképen nincs valós felhasználónév, arc vagy licenc-korlátos harmadik felas elem | a tananyag **két** valós felvétele: a Moodle-képernyőkép és a kvuca-plakátok archív fotói |

Az R8 hatálya a szabály saját szövegét követi („valós fotó/screenshot esetén”):
AI-generált képre és beszerzendő fizikai eszközre nem terjed ki — az indoklás
tételenként a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 2. szakaszában áll.

> **Projektgazdai döntés (2026-10-02, `HUM-MEDIA-03`):** gyermekvédelmi vagy
> krízis-HOOK-ban nem használunk készlet-AI-beszélőfejet. Az `M2.4-VID-01`, az
> `M3.3-VID-01` és az `M3.4-VID-01` hangalámondás + tipográfia/grafika (`explainer`): az R2
> és az R3 rajtuk marad, és az R5 produkciós szabály is vonatkozik rájuk. Utólagos
> ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna.

**Mit kell eldönteni ahhoz, hogy induljon a gyártás?** Egy helyen, döntésenként
egy kérdéssel, opciókkal és hatásszámmal:
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md). Ami már most tudható a
hangról és a vizuális rendszerről: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md),
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md).

Nem blokkoló, de minden vizuális munkára érvényes konvenció: **R1** (egységes
AI-jelölés — a tanulónak látható címke jóváhagyott szövege: „AI-generált médiaelem · emberi lektorálással.”), **R4**
(védjegy-semlegesség), **R6** (szín-szótár — 2026-10-02 óta modulhatókörű: a jelentést
mindig felirat, forma vagy betűjel hordozza).

**Nyitott emberi döntés.** Egy nem üres `decision` mező önálló készültségi kapu:
amíg ott áll, az asset státusza `emberi döntésre vár`, a produkciós szabályokból
levezetett státusz és a kézzel beírt `status` előtt. Ehhez **nem kell**
`mode: human-decision` — egy egyébként `legyártandó` asset is hordozhat nyitott
döntést (a mód azt mondja meg, *hogyan* készül, a státusz azt, hogy
*elkészíthető-e már*). Ha ugyanazon az asseten strukturális akadály is van
(például `MISSING_SPOKEN_SOURCE`), a státusz `blokkolt` marad — a nyitott döntés
attól még külön látszik a `readiness_issues` mezőben és a *Blokkolt assetek*
lapon.

A nyitott döntések teljes listája a munkafüzet *Emberi döntések* lapján és az
[`ASSET-MANIFEST-V2-MIGRATION.md`](./ASSET-MANIFEST-V2-MIGRATION.md) 6.
szakaszában van; a regiszterben az *⛔ Készültségi akadályok* és az *⚖️ Emberi
döntésre váró tételek* szakasz mutatja őket.

> ⚠️ **Emberi döntés:** az R8 szövegében — az R2/R3/R5-tel ellentétben — nincs
> `⟬KITÖLTENDŐ⟭` jelölés. Hogy ez betartandó szabály-e (és így nem kapu), vagy
> önálló jóváhagyást igényel a fotó/képernyőkép-assetek élesítése előtt, a
> Memunának (gyermekvédelmi felelős) és az adatvédelmi felelősnek kell tisztáznia
> ([`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md), D8). A felvételek adatkezelésére
> projektgazdai döntés van (`HUM-PRIV-02`, 2026-10-02): alapértelmezésben nincs fotó, videó
> vagy hangfelvétel, csak indokolt célból; a jogalap külön, önkéntes hozzájárulás, a
> megőrzés a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási
> hozzájárulás (`Adatvédelem – tanulói adatok és AI.md` 3. szakasz). Az R8 státuszáról (D8)
> a döntés nem szól.

> ✅ **Az M4 HOOK-formátum szerzői döntése 2026-08-27-én megszületett.** A v1 README ezt
> `J19` néven említette; ilyen azonosító sehol nincs a befagyasztott adathalmazban, a
> döntés viszont az `M4.2-ILL-01` assethez volt kötve. A válasz: a korpuszban a vegyes
> HOOK-formátum az általános minta, ezért az M4.2–M4.4 marad statikus illusztráció +
> narráció, új beszélőfej-videó nem készül. Az asset `decision` mezője kiürült, és a
> szokásos R5 alatt gyártandó. Részletek:
> [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md), lezárt döntések.

Ezek **szervezeti és jogi döntések**. A fordító csak nyilvántartja őket; nem old
fel egyet sem.

> A `content_integrity.py` `check_active_spec` ellenőrzése szándékosan kihagyja
> ezt a mappát, mert generált kimeneteket tartalmaz. A leckefájlokba írt
> deklarációkra viszont **teljes mértékben érvényes** — a migráció ezért nem
> vitte tovább a v1 spec-mezőkből a visszavont megfogalmazásokat.
