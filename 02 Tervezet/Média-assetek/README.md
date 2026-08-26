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

## „Felmondandó / generálandó szöveg" oszlop — ⚠️ kifagyasztott pillanatkép

Az **Assetek** munkalap (és az `assetek.csv`) `Felmondandó / generálandó szöveg (verbatim)` oszlopa **a kinyerés pillanatában** rögzített, szó szerinti szöveget tartalmaz:
- **narráció** → a teljes felmondandó/TTS-be tölthető szkript;
- **felirat / leirat** → ugyanaz a szöveg (a felirat a narrációt szó szerint közli);
- **alt-szöveg** → az akkori alt-szöveg (a dekoratív elemeknél szándékosan üres).

**Olvasd el, mielőtt bármit legyártanál:**

1. A `verbatim` (és a `lineRef`) **egy történeti időpont pillanatképe**, nem élő hivatkozás a leckére.
2. A kinyerő pipeline **nyugdíjazott** (lásd lent), ezért **a naprakészsége nincs garantálva** — minden azóta történt tananyag-szerkesztés elcsúsztathatta.
3. Ezért **nem használható végleges narráció-, felirat- vagy alt-szöveg-forrásként** anélkül, hogy a **jelenlegi leckefájlhoz visszaellenőriznéd**. A „nem kell a forrásfájlokban keresgélni" **nem érvényes** erre az oszlopra.
4. **Ütközés esetén a jelenlegi leckefájl az irányadó**, nem a pillanatkép.
5. **A szöveget hordozó assetek végleges/kötegelt legyártása addig blokkolt**, amíg az érintett pillanatkép-szöveget újra nem származtatták vagy egyenként vissza nem ellenőrizték a jelenlegi forráshoz. Az ismert, visszaellenőrzött driftpéldák lent szerepelnek — **a lista nem teljes**.

462 szöveg-asset kitöltve a kinyeréskori forrásból; szűrd az `Asset-típus = narráció` sorokra, ha a felmondandó szövegek kellenek — de az 1–5. pont ezekre is áll.

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

**A kánoni adat a `_build/media-merged.json`** — az **asset-leltárra** nézve: azonosítók, típus, hatókör, dedup, darabszámok, produkciós könyvelés. Ebből a regiszter minden kimenete bármikor újragenerálható.

**A jelenlegi tananyagszövegre viszont a leckefájl a kánon**, nem ez a JSON: a narráció szó szerinti szövege, az akadálymentesítési és runtime-előírás, valamint a pedagógiai megfogalmazás **mindig a `02 Tervezet/Modulok/` alatti aktuális lecke szerint érvényes** (lásd a „Felmondandó / generálandó szöveg" és az „Ismert kinyerési drift" szakaszt). A leltár érvényessége és a benne lévő szöveg naprakészsége **két külön kérdés** — az előbbi áll, az utóbbi nem garantált.

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

## ⚠️ Ismert kinyerési drift (frozen snapshot)

A `_build/media-merged.json` a **kifagyasztott, kánoni produkciós adathalmaz**, és a renderelt kimenetek
determinisztikusan ebből állnak elő. A kinyerő pipeline viszont **nyugdíjazott** (lásd fent), ezért a
sorokban tárolt **forráshely- és idézet-mezők** (`lineRef`, `verbatim`) **elcsúszhatnak**, amikor a
tananyag prózája változik: ezek a mezők a kinyerés pillanatának pillanatképei, nem élő hivatkozások.
Minden tananyag-szerkesztés — sorbeszúrás is — növeli ezt a driftet.

**Ütközés esetén a jelenlegi tananyagfájl az irányadó**, nem a pillanatkép — a pedagógiai,
akadálymentesítési és runtime-szabályokra nézve egyaránt. A drift **nem javítható kézzel**; akkor kell
újraszármaztatni, amikor a kinyerő pipeline-t újraépítik a jelenlegi `02 Tervezet/Modulok/` szerkezetre.

Jelenleg ellenőrzött példák (2026-08-26) — a lista nem teljes, csak a visszaellenőrzött eseteket sorolja:

| Hol | Pillanatkép | Jelenlegi forrás |
|---|---|---|
| `M3.4-IKO-02.lineRef`, `M3.4-EGY-06.lineRef`, `M6.1-EGY-05.lineRef` + `.verbatim`, `M6.1-EGY-08.verbatim` | „H5P Short Answer” / „H5P Essay / Short Answer” | a leckékben már nincs „Short Answer”; a szabad szöveges mezők megvalósítás-semlegesek (`LMS – H5P runtime acceptance.md` 6. pont) |
| `M2.3-EGY-02.lineRef` | „559–564 (záró **Short-answer** mező)” | az M2.3 záró mezője „1 rövid szabad szöveges mező” |
| `M1.1-IKO-02`, `M2.4-DIA-02`, `M2.4-ILL-02`, `M4.1-NAR-07`, `M4.2-EGY-05`, `M4.2-ILL-03`, `M4.4-ALT-05`, `M4.4-DIA-05`, `M4.4-NAR-05`, `M6.1-EGY-11`, `Z.1-IKO-01` (leíró mezők) | „H5P Essay” / „Essay mező” | ezek a leckék már **nem** neveznek meg content type-ot: a Course Presentation dián belüli szabad szöveg nem feltételezhető, a megvalósítást a runtime acceptance 6. pontja dönti el |
| M4.1 feliratsor idézete | „kapcsolható magyar felirat **vagy** a slide-szöveg fedje le szó szerint… WCAG 1.2.2” | az M4.1 elkülöníti a **csak hangot** (WCAG 2.2 SC 1.2.1) a **hangos videótól**, ahol a **felirat kötelező** (SC 1.2.2) — a leirat nem váltja ki |
| `M5.1-NAR-02`, `M5.1-FEL-02`, `M5.1-LEI-02` (`.verbatim`) | „a nonformális **és** az informális tanulás is **önkéntes**” | az M5.1 SLIDE 3 narrációja javítva: az önkéntesség a **someres részvétel** helyi jellemzője, nem az informális tanulás ismertetőjegye; a választóvonal a **tudatos nevelési cél** (Cedefop) |
| `M5.1-ALT-02` (`.verbatim`) | „közép – nonformális tanulás / Somer (szervezett, **önkéntes**, nevelési cél…); jobb – informális tanulás / random élet (spontán, nincs tervezett nevelési cél)” | az M5.1 alt-szövege javítva: a nonformálisnál a **nevelési cél** a definiáló jegy (az önkéntesség Somer-specifikus), az informálisnál kiegészült azzal, hogy **sokszor észre sem veszed, hogy tanultál** |

> A `check_active_spec` szándékosan kihagyja a `Média-assetek/` mappát, ezért a checker ezt a driftet
> nem is jelezheti — a fenti szabály (a tananyagfájl az irányadó) tudatos, dokumentált megállás.

Gyors újra-render a meglévő `media-merged.json`-ból (a `Média-assetek/` mappából futtatva):

```bash
node "_build/format-media.js" "Média-asset regiszter.md" "_build/media-merged.json"
python3 "_build/build-data.py" "_build/media-merged.json"
```
