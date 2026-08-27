# 🎛️ Produkciós stílus-token — a D1 döntés előkészítése

Ez a lap az R5 vizuális rendszer **legkisebb végrehajtható lockja**: annyit rögzít,
amennyi az első kötegek legyártásához kell, és nem többet. Nem arculati kézikönyv — a
mozgalomnak **van sajátja**, és ez a lap arra épül.

**Státusz: NYITOTT — FELHASZNÁLÓI DÖNTÉS SZÜKSÉGES.** Ez a lap **javaslatot** tesz, nem
zár le kaput. Az R5 blokkolók a 257 asseten változatlanul állnak, amíg a jóváhagyó nem
válaszol a 9. szakasz kérdéseire.

Kapcsolódó lapok: [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) (mi
következik a tananyagból), [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) (D1
kérdésszöveg), [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) (a teljes gyártási stack).

---

## 0. A kutatás egyetlen legfontosabb eredménye

**Létezik hivatalos arculati kézikönyv, és nyilvánosan elérhető.** A
`VISUAL-SYSTEM-DECISION.md` 1. szakasza azt állapította meg, hogy „a repositoryban nulla
hexadecimális színérték van” — ez továbbra is igaz, de **nem azt jelenti, hogy a
paletta nem létezik**: a repositoryn kívül, a mozgalom saját felületén létezik, deklarált
HEX / RGB / CMYK / Pantone értékekkel.

Ezért a D1 kérdése megváltozik:

| Korábbi kérdés | Mostani kérdés |
|---|---|
| Milyen legyen a someres paletta? | Átvesszük-e a **meglévő hivatalos palettát**, és mit teszünk hozzá ott, ahol a kézikönyv nem mond semmit? |

Ez lényegesen kisebb és olcsóbb döntés.

### Bizonyíték-lánc

| # | Forrás | Mit igazol | Osztály |
|---|---|---|---|
| B1 | `https://somer.hu/arculat/` — `<title>Arculat - Hasomer Hacair Magyarország</title>` (lekérdezve 2026-08-27) | a mozgalom saját arculati oldala; szövege: „Arculati kézikönyvünk itt érhető el.” | **HITELES** (first-party) |
| B2 | `https://docs.google.com/document/d/1nOgsJApcmQIC4CtPVMWQpsDf-5FY3D-rB6g0y6id_Vs/` — a B1-ről hivatkozott kézikönyv (lekérdezve 2026-08-27) | teljes színtábla HEX/RGB/CMYK/Pantone értékekkel, betűtípus, logóhasználati és ábrázolási szabályok | **HITELES** (first-party) |
| B3 | `https://somer.fra1.digitaloceanspaces.com/somer.hu/uploads/2022/01/07134759/somer-semel.zip` — logócsomag a `somer.hu` **saját feltöltés-tárában**; letöltve, SHA-256 `307c2533b7466c8f…`. *(A B1 oldal a fájlneveket egy hivatalos Drive-mappára linkeli — `drive.google.com/drive/folders/1Uf8bsmb_o88X2Lsfn61H07bw2At9RtKE` —, a ZIP-re közvetlenül nem mutat; ugyanazokat a változatokat tartalmazza.)* | 7 jóváhagyott logóváltozat SVG/PDF/PNG-ben + `.ai` mester; a `viewBox` `0 0 198.43 198.43` | **HITELES** (first-party) |
| B4 | `somer-semel-color-with-transparent-bg.svg` (B3-ból), `<style>` blokk | **független megerősítés**: a kézikönyv mind a hat alapszíne szó szerint benne áll a hivatalos vektorban | **HITELES** (first-party) |
| B5 | `https://adobe-fonts.github.io/source-sans` + `adobe-fonts/source-sans` `LICENSE.md` (lekérdezve 2026-08-27) | a javasolt helyettesítő betűtípus licence SIL OFL 1.1 | **HITELES** (kiadói) |
| B6 | `SourceSans3-Regular.otf` 3.052R, `cmap` tábla ellenőrizve | mind a **18** magyar ékezetes glif megvan (`á Á é É í Í ó Ó ö Ö ő Ő ú Ú ü Ü ű Ű`), továbbá `·` (U+00B7), `„`, `”`, `–`, `—`, `✓`, `☐` | **HITELES** (mért) |
| B7 | `somer.hu` Divi CSS, `@font-face "Myriad Pro Regular/Bold Italic/Bold Condensed Italic"` | az élő oldal ténylegesen Myriad Pro-t tölt be | **ALÁTÁMASZTÓ** (megvalósítás, nem szabály) |
| B8 | `hashomer-hatzair.org` (a világmozgalom oldala) és `/wp-json/wp/v2/media` | **nincs** nyilvános nemzetközi arculati csomag, sem hex/Pantone/betűtípus-előírás | **NEM HITELES** forrásként — a hiány ténye viszont rögzítendő |

> ⚠️ **Két figyelmeztetés, amit a jóváhagyónak látnia kell.**
>
> **1. Két, egymással nem egyező színgeneráció van forgalomban.** A kézikönyv és a 2022-es
> logócsomag a lenti hat értéket adja; a `somer.hu` élő oldala, a favicon és a
> háromnyelvű lockup viszont még a **2021-es** változatot szállítja (`#DC5727 #F1BA18
> #82B441 #36A549 #0FA2C8 #70CCE7`). **Az élő oldalról vagy a faviconból mintavett szín
> tehát rossz lesz.** A kézikönyv + SVG értékei az irányadók — ezt a jóváhagyónak
> meg kell erősítenie.
>
> **2. A kézikönyv szerkeszthető Google Doc, verzió-, dátum- és jóváhagyás-bélyeg
> nélkül.** First-party, de nem datált. Hogy ez a hatályos változat-e, **szervezeti
> megerősítés kérdése**, nem levezethető.

---

## 1. Palette — HITELES MÁRKAÉRTÉK

Minden érték szó szerint a kézikönyvből (B2), és minden alapszín **byte-azonosan
megerősítve** a hivatalos SVG-ből (B4). Ezeket **nem találtuk ki, és nem módosítjuk.**

### 1.1. Alapszínek

| Kézikönyvi név | HEX | RGB | Pantone | SVG-ben |
|---|---|---|---|---|
| piros | `#D84C15` | 216, 76, 21 | 173 C | ✅ `.cls-4` |
| sárga | `#F2BC00` | 242, 188, 0 | 7408 C | ✅ `.cls-3` |
| zöld | `#87B027` | 135, 176, 39 | 2301 C | ✅ `.cls-2` |
| sötét zöld | `#369D37` | 54, 157, 55 | 7739 C | ✅ `.cls-1` |
| sötét kék | `#08A0CA` | 8, 160, 202 | 2200 C | ✅ `.cls-7` |
| kék | `#82CDE9` | 130, 205, 233 | 636 C | ✅ `.cls-8` |

CMYK-értéket a kézikönyv mindegyikhez ad (pl. piros: `C 9,38% M 80,47% Y 100% K 1,17%`).

### 1.2. Árnyalatok — szintén deklaráltak

| Alap | 1 | 2 | 3 |
|---|---|---|---|
| piros | `#E1733C` | `#E9986A` | `#F1BC9B` |
| sárga | `#FFCE1F` | `#FFD439` | `#FFDA53` |
| zöld | `#A3BE53` | `#BCCE82` | `#D4DFAE` |
| sötét zöld | `#6FAE58` | `#9AC182` | `#BFD6AD` |
| kék | `#A1D7EE` | `#BCE2F3` | `#D4ECF8` |
| sötét kék | `#65B2D5` | `#95C5E0` | `#BCD8EA` |

*(A sárga három árnyalatához a kézikönyv csak HEX-et ad, RGB/CMYK/Pantone nélkül.)*

### 1.3. Két további érték a hivatalos csomagból — deklarálatlan

A logócsomag SVG-i tartalmazzák, a kézikönyv színtáblái **nem**:

| HEX | Hol | Mi ez |
|---|---|---|
| `#1D1D1B` | a `black-*` és `white-with-black-bg` változatok egyetlen színe | a hivatalos **monokróm fekete** — nem `#000000` |
| `#2B2523` | a színes szemel egyetlen útvonala (`.cls-5`) | deklarálatlan sötét részletszín |

**Ez fontos:** a mozgalom saját monokróm változata `#1D1D1B`-t használ, nem tiszta
feketét. A tananyag alapszövegszínének ez a természetes választása — hivatalos érték,
és 16,88:1 kontrasztot ad fehéren.

---

## 2. Számított akadálymentesítés — ez dönti el, hogyan használható a paletta

A kontrasztokat **kiszámoltuk**, nem becsültük (WCAG 2.2 relatív luminancia-képlet;
ellenőrizve a W3C ismert értékein: fekete/fehér = 21,00:1, `#777777`/fehér = 4,48:1).
A követelmények forrása: `LMS – hozzáférhetőségi sztenderd.md`, a **„KAPUS H5P
»pre-flight« checklist”** kontraszt-sora — szöveg **≥ 4,5:1** (nagy szöveg 3:1),
jelentéshordozó nem-szöveges elem **≥ 3:1**. Ugyanott áll egy **nem normatív
projekt-cél a minimum felett**: „a kapus elemeknél a lényeges UI-kontrasztot is
igyekszünk 4,5:1-re hozni, mert a madrichok jellemzően olcsó kijelzőn, gyenge fényben,
mozgás közben használják.” A 2.4. pont szerint önmagában megálló három márkaszín
(`#D84C15` 4,23 · `#369D37` 3,48 · `#08A0CA` 3,05) a **szabványt teljesíti, ezt a
projekt-célt nem** — kapus elem ikonjánál ezért a `#1D1D1B` körvonalas változatot kell
használni.

### 2.1. Márkaszín mint SZÖVEG fehéren

| Szín | HEX | Arány | Törzsszöveg (4,5) | Nagy szöveg (3,0) | Nem-szöveges (3,0) |
|---|---|---:|---|---|---|
| piros | `#D84C15` | **4,23:1** | ❌ | ✅ | ✅ |
| sötét zöld | `#369D37` | **3,48:1** | ❌ | ✅ | ✅ |
| sötét kék | `#08A0CA` | **3,05:1** | ❌ | ✅ | ✅ |
| zöld | `#87B027` | **2,54:1** | ❌ | ❌ | ❌ |
| kék | `#82CDE9` | **1,77:1** | ❌ | ❌ | ❌ |
| sárga | `#F2BC00` | **1,75:1** | ❌ | ❌ | ❌ |

> **Egyetlen márkaszín sem alkalmas törzsszövegnek fehéren.** Három közülük
> (`#F2BC00`, `#87B027`, `#82CDE9`) a **3:1 nem-szöveges küszöböt sem éri el** — vagyis
> önmagában vékony vonalként vagy jelentéshordozó grafikai elemként fehér alapon nem
> használható.

### 2.2. Fehér szöveg márkaszínen

| Szín | Arány | Törzsszöveg | Nagy szöveg |
|---|---:|---|---|
| piros `#D84C15` | 4,23:1 | ❌ | ✅ |
| sötét zöld `#369D37` | 3,48:1 | ❌ | ✅ |
| sötét kék `#08A0CA` | 3,05:1 | ❌ | ✅ |
| zöld `#87B027` | 2,54:1 | ❌ | ❌ |
| kék `#82CDE9` | 1,77:1 | ❌ | ❌ |
| sárga `#F2BC00` | 1,75:1 | ❌ | ❌ |

**Fehér szöveg márkaszínen sehol nem éri el a törzsszöveg-küszöböt.**

### 2.3. `#1D1D1B` szöveg márkaszínen — ez viszont működik

| Alap | Arány | Törzsszöveg |
|---|---:|---|
| sárga `#F2BC00` | **9,62:1** | ✅ |
| kék `#82CDE9` | **9,53:1** | ✅ |
| zöld `#87B027` | **6,65:1** | ✅ |
| sötét kék `#08A0CA` | **5,54:1** | ✅ |
| sötét zöld `#369D37` | **4,85:1** | ✅ |
| piros `#D84C15` | 3,99:1 | ❌ (nagy szövegre ✅) |

Az árnyalatokon (1.2.) `#1D1D1B` szöveggel **mind a 18 árnyalat teljesíti az AA
küszöböt** (4,5:1); a sáv 5,40:1 – 13,79:1. **Kettő marad az AAA (7:1) alatt:**
`#E1733C` (5,40:1) és `#6FAE58` (6,33:1) — ezek AA-ra jók, AAA-ra nem. A többi
tizenhat AAA.

### 2.4. A levezetett szabály

> **A márkaszínek felületszínek, nem tintaszínek.**
> Szöveg alattuk `#1D1D1B`-vel áll, nem fehérrel. Fehér alapon vékony, jelentéshordozó
> vonalként csak `#D84C15`, `#369D37` és `#08A0CA` állhat meg önmagában; a világos három
> (`#F2BC00`, `#87B027`, `#82CDE9`) **`#1D1D1B` körvonalat igényel** — akkor a határvonal
> hordozza az 1.4.11 szerinti információt (körvonal a papírhoz 16,88:1, a kitöltéshez
> 6,65–9,62:1).

### 2.5. Az R6 szín-ütközés — mért válasz

Kiszámoltuk minden márkaszín-pár egymáshoz mért kontrasztját:

| Legjobb pár | Legrosszabb pár |
|---|---|
| sárga / piros = **2,41:1** | sárga / kék = **1,01:1** |

**A tizenöt pár közül egyetlen sem éri el a 3:1-et.** Ezen belül a szemantikus családok
belső elválása is gyenge:

| Család | Legrosszabb belső pár | Arány |
|---|---|---:|
| SBI (S/B/I) | S(sötét kék) / B(sötét zöld) | 1,14:1 |
| Kérdéstípusok (kék=`#82CDE9`) | zárt / tisztázó | **1,01:1** |
| Do / Don't | DO / DON'T | 1,22:1 |
| M6.4 jelölők | előny / inkluzivitás | 1,14:1 |
| 3 pillér | cionizmus / hum. zsidóság | 1,43:1 |

**Ebből objektív következtetés adódik, nem ízlés:** ebben a palettában a szín
**egyáltalán nem képes** két jelentést elválasztani — sem gyengénlátónak, sem
színtévesztőnek, sem fekete-fehér nyomtatásban. A tananyag már ma is előírja, hogy „a
szín soha nem egyedüli információhordozó”; a mérés azt mutatja, hogy ez a szabály nem
ráadás, hanem **teherhordó**.

**Javaslat az R6-ra (nem döntés):**

1. **Az elsődleges megkülönböztető mindig a forma és a betűjel/felirat.** Ez már ma is
   kötelező (S/B/I betűk, ikonalak, „szín + forma” kikötések).
2. **A szín-szótár modul-hatókörű, nem globális.** Ugyanaz a márkaszín más modulban más
   szerepet vihet, mert (a) a jelentések soha nem jelennek meg egy képernyőn,
   (b) mindegyiket külön forma/betű jelöli, (c) a paletta hat színnel öt szemantikus
   családot szolgál ki. Ezt az R6 „explicit jelölés” ága megengedi — de **ki kell
   mondani**, különben a kék véletlenül globális jelentést kap.
3. **Ahol egy család négy színt kér, luminancia szerint válaszd őket.** A
   kérdéstípusoknál a `kék #82CDE9` és a `sárga #F2BC00` **1,01:1** — gyakorlatilag
   azonos világosság. Ha a család mégis színnel is akar elválni, a „zárt”-hoz a
   `sötét kék #08A0CA` javasolt (`#08A0CA`/`#F2BC00` = 1,74:1). Ez a lecke szövegét
   **nem érinti**: a leckék hue-nevet írnak („kék”), nem hex-et.
4. **A négy kvuca-piktogram maradjon szín-semleges** (forma + emoji-metafora), mert
   négy, egymástól luminanciában is elváló márkaszín nincs.

---

## 3. Tipográfia

### 3.1. Amit a kézikönyv kimond — HITELES

> „Kétféle betűtípust használunk. Az egyik a **Myriad Pro** amit a szövegekhez a másik
> pedig a **Dock11** amit az SMR felirathoz használunk. Mindkettő betűtípus megtalálható
> a Font mappában OTF kiterjesztésben…”

### 3.2. Amit a kézikönyv NEM mond ki — és ez blokkoló

A kézikönyv „címsorok” szakasza minden szinten szó szerint ezt írja:

> `Cím: kifejtésre vár` · `Alcím: kifejtésre vár` · `Heading 1: kifejtésre vár` ·
> `Heading 2: kifejtésre vár` · `Bekezdes: kifejtésre vár`

**Betűméret-skála tehát nincs — sem a szervezetnél, sem a repositoryban.** Ezt a
tananyagnak akkor is meg kell alkotnia, ha a Myriad Pro marad. A 3.4. pont javaslata
ezért **PRODUKCIÓS AJÁNLÁS** minden változatban.

### 3.3. Két nyitott kockázat a betűtípus körül

| # | Kockázat | Miért számít |
|---|---|---|
| T1 | **A Myriad Pro Adobe kereskedelmi betűtípus.** A `somer.hu` nyers `.otf`-ként szolgálja ki. Hogy a szervezet licence kiterjed-e Moodle/H5P webes beágyazásra és PDF-embedelésre, **jogi kérdés**, és a repositoryból nem eldönthető. | 247 R5-asset PDF-je és SVG-je ettől függ. Ha az embedelés nem fedett, minden nyomtatvány újraszedendő. |
| T2 | **A Dock11 fájl nem található a nyilvános asset-mappában.** A kézikönyv „Font mappát” említ; a hivatkozott Drive-mappában nincs ilyen. SMR-feliratos grafika sem található. | Az SMR szóvédjegyet nem tudjuk reprodukálni. A tananyagnak viszont nincs is szüksége rá — a szemel vektorban áll, a betűi görbék. |

### 3.4. Betűméret-skála — PRODUKCIÓS AJÁNLÁS

Nem márkaérték. A `LMS – hozzáférhetőségi sztenderd.md` premisszájából vezetve („olcsó
kijelző, gyenge fény, mozgás közben”) és az A4-es próbanyomatból visszamérve:

| Szerep | A4 nyomtatvány | A6/A5 kártya | A3–A1 poszter |
|---|---|---|---|
| Cím | 17–20 pt, félkövér | 12–14 pt, félkövér | A3: ≥ 36 pt · A2: ≥ 48 pt · A1: ≥ 60 pt |
| Szekciócím | 11–13 pt, félkövér | 10–11 pt | ≥ 24 pt |
| Törzs | **10,5 pt / 1,38 sorköz** | **≥ 12 pt** (teremben felolvasva) | A3: ≥ 18 pt |
| Másodlagos / jegyzet | 8,5–9 pt | 9 pt | ≥ 14 pt |
| Élőláb / meta | 7–7,5 pt | 7 pt | — |

- **Abszolút alsó határ nyomtatványon: 8 pt.** Tanulónak szóló instrukció **soha nem
  kisebb 10 pt-nél**.
- **SVG-ábra képernyőn:** a legkisebb szöveg effektív mérete ≥ 14 px 1× rendereléskor, és
  az ábrának 320 px széles nézetben is olvashatónak kell lennie (mobile-first kikötés).
- **Igazítás:** a kézikönyv szerint „a szöveg legyen balra vagy jobbra zárt. Ne legyen
  középre igazított vagy sorkizárt.” → a tananyagban **egységesen balra zárt**, sehol
  sorkizárt. Ez egyszerre márkaszabály és olvashatósági előny.

### 3.5. Fallback-lánc

```
Myriad Pro  →  Source Sans 3  →  Segoe UI  →  Helvetica Neue  →  Arial  →  sans-serif
```

A lánc mindkét változatban ugyanez; csak az **elsődleges** tag különbözik (lásd 8.).

---

## 4. Elrendezés

Amit a kézikönyv kimond (**HITELES**):

- **Flat design**: rács-stílus, aszimmetrikus elrendezés, talpatlan betűk, hangsúlyos
  tipográfia, világos hierarchia.
- **Szövegdoboz**: négyzetes vagy a bekezdés formáját követő; csak párhuzamosok és
  merőlegesek, **görbe vonal nincs**; a derékszögek **5 pont sugárral lekerekítve**,
  arányosan skálázva; egyszínű, homogén kitöltés; a háttérhez képest kontrasztos —
  lehet a háttér domináns színe, ha az a kép ≥ 60%-át kitölti.
- **Árnyék**: kerülendő. Nagyobb geometrikus alakzat és szövegdoboz kaphat **lágy,
  halvány** árnyékot; **szövegdobozon belül soha**.
- **Képek**: előnyben a someres szimbólumot és a mozgalom résztvevőit ábrázoló képek;
  a csillapító overlay (egyszínű vagy színátmenetes) színei **csak a palettából**.

**PRODUKCIÓS AJÁNLÁS** (a kézikönyv ezekről hallgat):

- **A4 álló, 190 mm szedéstükör**, margók 14 mm fent/balra/jobbra, 12 mm lent; a
  nyomtatók nem-nyomtatható sávja miatt semmi nem mehet 10 mm-nél közelebb a széphez.
- **12 oszlopos rács** 4 mm csatornával az A4-en (aszimmetrikus elhelyezés megengedett,
  a kézikönyv szerint kifejezetten kívánatos).
- **Függőleges ritmus** 4,4 mm alapegység; szekcióközök ennek többszörösei.
- **Címhely:** a cím a lap tetején, fölötte egy soros, verzálissal szedett „kicker”
  (modul + asset-osztály), alatta egy vastag (1,2 pt `#1D1D1B`) vonal. Ez adja a
  „hangsúlyos tipográfia + világos hierarchia” kikötést szín nélkül is.
- **Kártyaív:** A4-enként 2–4 kártya, szaggatott `--rule` vágóvonallal; kétoldalas
  szettnél a hátoldal oszlopsorrendje **tükrözött**, hogy a hosszú élű duplex illesszen.

---

## 5. Ikonrendszer — PRODUKCIÓS AJÁNLÁS

A kézikönyv ikonokról nem rendelkezik; a flat design kikötés és a 2.4. mérés viszont
együtt kijelöli a választ.

| Paraméter | Érték | Miért ez |
|---|---|---|
| Stílus | **vonalas (outline), nem kitöltött** | a világos márkaszínek kitöltésként nem érik el a 3:1-et fehéren; a `#1D1D1B` körvonal mindig 16,88:1 — a vonalas rendszer **konstrukcióból** akadálymentes |
| Tervezőrács | 24 × 24 egység | ipari szabvány, osztható 64 / 128 / 256 px-re |
| Vonalvastagság | **2/24 az ikondoboz éléhez képest** (64 px-en ≈ 5,3 px) | vastag vonal olcsó kijelzőn, gyenge fényben is megáll |
| Végződés / csatlakozás | lekerekített (`round` cap és join) | illeszkedik a kézikönyv 5 pt-os lekerekítés-elvéhez |
| Sarok-lekerekítés | sugár = vonalvastagság | „arányaiban apró és szolid” (kézikönyv) |
| Szín | körvonal `#1D1D1B`; opcionális márkaszín-kitöltés **mögötte** | a jelentést a forma viszi, a szín kíséri |
| Sűrűség | ikononként **legfeljebb 3** önálló elem | 64 px-en ennél több összefolyik |
| Szöveg az ikonban | **nincs** — kivéve a szemantikus betűjelet (`S` / `B` / `I`) | a betűjel kötelező redundancia, nem dekoráció |
| Formátum | SVG (elsődleges), PNG átlátszó háttérrel (tartalék), min. 64 × 64 px | a leckék technikai jegyzeteiből |

**Kötelező redundancia:** minden szemantikus ikon egyedi **sziluettel** azonosítható a
színe nélkül is. Ellenőrzés: az ikoncsalád 100%-ban szürkeárnyalatosra konvertálva is
megkülönböztethető kell legyen — a 2.5. mérés miatt ez nem opcionális.

---

## 6. Illusztráció- és karakterrendszer — PRODUKCIÓS AJÁNLÁS

| Paraméter | Érték |
|---|---|
| Stilizáltság | **lapos vektoros illusztráció**; nem fotorealisztikus, nem 3D-render, nem festői |
| Háttér | egyszínű márkaszín vagy fehér; illusztráción **színátmenet nincs** (a kézikönyv a gradienst csak fotó-overlayre engedi) |
| Kontúr | ha van, `#1D1D1B`, az ikonrendszerrel azonos vastagsági logikával |
| Emberi karakter | egyszerűsített arc, konzisztens testarány; **rögzített referenciakészletből** (lásd `PRODUCTION-STACK.md`) |
| Sokféleség | az életkor, nemi megjelenés, testalkat, hajviselet, szemüveg és segédeszköz **a teljes készleten belül** változzon természetesen — ne „egy sokszínű szereplő” képenként. Egyetlen vizuális jegy se legyen egy szerep azonosítója. |
| Vallási megjelenítés | a mozgalom harmadik pillére a glosszárium szerint **„világi (szekuláris) humanista zsidóság”** — ezért vallási öltözet nem használható a zsidóság vizuális rövidítéseként. Bármely ezen túlmutató ábrázolási kérdés **helyi someres döntés**, nem produkciós. |
| Valós személy | AI-illusztráció **nem mintázhat** azonosítható valós személyt (R2/R8) |
| Szöveg a képben | **nincs generált szöveg a képben.** Minden magyar szöveg utólag, determinisztikus tipográfiával kerül rá. Indok: a generatív modellek a magyar ékezeteket (ő, ű) rendszeresen elrontják; a szöveg a leckéből származik és változhat; az alt-szövegnek szó szerint egyeznie kell. |

**Az egyetlen látszólagos kivétel** (`M4.2-ILL-01` — chat-buborék magyar mondattal)
valójában ezt a szabályt igazolja: a generátor a buborékot és a jelenetet rajzolja meg
**szöveg nélkül**, a mondat SVG-ben kerül bele. A pilot-brief így írja le.

---

## 7. Nyomtatvány-, videó- és jelölésrendszer

### 7.1. Nyomtatvány — **PRODUKCIÓS AJÁNLÁS**, a méret- és B/W-kikötések kivételével

A lapméretek és a fekete-fehér nyomtathatóság a leckék technikai jegyzeteiből jönnek
(✅ kötelező); az élőláb, a margóértékek, a vonalvastagságok és a mezőméretek **javaslatok**.

- **A4 álló** az alap; A5 / fél A4 a cédula; A3 / A2 / A1 a flipchart és a fali poszter.
- **Fekete-fehér kompatibilitás kötelező, nem opció.** A szerkezetet vonalvastagság és
  tipográfia hordozza; a szín kizárólag ráadás. A 2.5. mérés miatt ez a **teljes**
  nyomtatvány-családra igaz, nem csak arra a 26 tételre, amelyik a saját jegyzetében
  fekete-fehérként szerepel.
- **Kézírásos mező:** sorköz ≥ 8 mm, alávonás `--rule` 0,6 pt; jelölőnégyzet 4 × 4 mm,
  1 pt `#1D1D1B` kerettel, 0,7 mm sarokkerekítéssel.
- **Élőláb minden nyomtatványon:** `<asset-id> · v<verzió> · <rövid cím>` balra,
  oldalszám jobbra, 7 pt `--ink-muted`. Ez teszi a kinyomtatott lapot visszakereshetővé.

### 7.2. Videó-grafika — a 16:9 kötelező, a többi **PRODUKCIÓS AJÁNLÁS**

A 16:9 arány a leckék jegyzeteiből kötelező. Az 1920 × 1080-as mester, a biztonsági
zónák és az overlay-szabály **nem szerepel a repositoryban** — ezek javaslatok.

- **16:9, 1920 × 1080 mester.**
- **Cím-biztonságos zóna:** a keret belső 90%-a (5% behúzás minden oldalon = 96 px
  vízszintesen, 54 px függőlegesen 1080p-n).
- **Felirat-biztonságos zóna:** az alsó **15%** égetett grafikától mentes marad — a
  H5P/Moodle ide rendereli a feliratot.
- **Overlay:** csak palettaszín, lapos; grafikán színátmenet nincs.
- **Égetett felirat nincs** — a felirat külön `.vtt` deliverable.

### 7.3. Az AI-jelölés vizuális kezelése (R1)

A **szöveg kötött, és nem módosul**:

> **AI-generált médiaelem · emberi lektorálással.**

A megjelenítésből **egy dolog objektíven eldőlt**, a többi nem:

| Kérdés | Válasz | Bizonyíték |
|---|---|---|
| Beleégetve vagy az LMS jeleníti meg? | **az LMS/H5P jeleníti meg, valódi szövegként** | `M5.1-EGY-01` a11y: „Valódi kijelölhető szöveg legyen, ne képbe égetve.”; `M6.1-EGY-01` a11y: „Olvasható szövegként jelenik meg (nem képbe égetve).” |
| Hol? | **NYITOTT — a D1 dönti el.** A két meglévő hordozó nem egyezik: `M5.1-EGY-01` „a beszélő fej videók alá”, `M6.1-EGY-01` „a lecke alján/dián”. A kánoni R1 szabály maga is kimondja, hogy „a címke vizuális megjelenése **és elhelyezése** a vizuális rendszer (R5 stílus-token) hatásköre”. | `produkcios-szabalyok.json` R1; a két asset spec-mezője |
| A gépi jelölés hol van? | magában az exportált fájlban (C2PA / Content Credentials / vízjel), és az export **nem távolíthatja el** | R1 szabályszöveg; `M6.1-VID-01` jegyzet |

**PRODUKCIÓS AJÁNLÁS a megjelenésre** (ezt a részt kell jóváhagyni):

- szín `--ink-muted` `#5C5C5B` a lap háttérszínén — **6,69:1**, tehát kis méretben is AA;
- méret a törzsszöveg **0,875-szöröse**, de képernyőn soha nem kevesebb 12 px effektív
  méretnél, nyomtatványon 8 pt-nél;
- egy sor, tördelés nélkül, a médiaelem bal széléhez igazítva;
- a `·` U+00B7 középpont — a betűkészletben ellenőrizve (B6);
- **soha** képként, soha rövidítve, soha lefordítva, soha ikonra cserélve;
- nyomtatható, AI-eredetű letölthető anyagon az élőlábban, szövegként.

---

## 8. A két változat — ez a tényleges döntés

Mindkettő **azonos márkaszíneket** és **azonos logóhasználatot** használ. A különbség
két helyen van: a **betűtípus** és a **semleges (szürke) skála**.

### A változat — MÁRKA-SZIGORÚ

| | |
|---|---|
| **Paletta** | a 6 alapszín + 18 árnyalat + `#FFFFFF` + `#1D1D1B`. **Semmi más.** |
| **Betűtípus** | Myriad Pro (törzs), Dock11 (csak SMR-felirat, a tananyagban nem fordul elő) |
| **Semleges skála** | nincs; a hierarchiát tipográfia és márkaszín-felület adja |
| **Ikon / illusztráció / nyomtatvány / videó / AI-jelölés** | az 5–7. szakasz szerint — **de** a 7.1. `--rule` és `--ink-muted` tokenjei helyett `#1D1D1B` gyengített vonalvastagsággal |
| **Előny** | nulla kitalált érték; minden hex visszavezethető a kézikönyvre; a legkisebb jóváhagyási súrlódás |
| **Kockázat** | **T1** (Myriad Pro embedelési licenc, lásd 3.3.) — ha nem fedett, mind a 247 R5-asset újraszedendő. **T2** (Dock11 fájl nem elérhető). Táblázatvonalhoz és másodlagos szöveghez nincs szürke: marad a `#1D1D1B` gyengített vonalvastagsággal vagy egy márkaszín — mindkettő rosszabb. |
| **Újragyártási kockázat** | **MAGAS**, és nem tőlünk függ (jogi válasz) |
| **Hány asset építhet rá az R5 lezárása után** | 247 (a teljes B1 köteg) — de csak akkor, ha a betűtípus-licenc kérdése addigra megválaszolt. Amíg nincs válasz: **0**. |

### B változat — MÁRKAHŰ + PRODUKCIÓS RÉTEG *(ajánlott)*

| | |
|---|---|
| **Paletta** | **változatlanul** a 6 alapszín + 18 árnyalat + `#FFFFFF` + `#1D1D1B` — plusz egy semleges skála, amely a hivatalos `#1D1D1B`-ből származik, és **PRODUKCIÓS AJÁNLÁSKÉNT** van megjelölve, nem márkaértékként |
| **Betűtípus** | **Source Sans 3** (SIL OFL 1.1, Adobe — B5) a tananyag-produkcióhoz; a Myriad Pro marad mindenütt, ahol a szervezet maga készít anyagot |
| **Semleges skála** | lásd lent |
| **Ikon / illusztráció / nyomtatvány / videó / AI-jelölés** | az 5–7. szakasz szerint, azonosan |
| **Előny** | nincs licencfüggés: a Source Sans 3 PDF-be és H5P-be szabadon beágyazható. Mérve: mind a **18** magyar ékezetes glif megvan, a `·`, `„`, `”`, `–`, `—`, `✓`, `☐` is (B6). A szürke skála megoldja a táblázat-, elválasztó- és másodlagosszöveg-problémát. A márkaszínek és a logó **érintetlenek**. |
| **Kockázat** | a tananyag betűképe eltér a szervezet egyéb anyagaitól. A Source Sans 3 az Adobe saját, humanista talpatlan nyílt betűtípusa, tehát a Myriad Pro-hoz karakterében közel áll — de **nem azonos**, és ezt a márkatulajdonosnak jóvá kell hagynia. |
| **Újragyártási kockázat** | **ALACSONY** |
| **Hány asset építhet rá az R5 lezárása után** | 247 (a teljes B1 köteg), jogi válaszra várás nélkül |

#### A B változat semleges skálája — PRODUKCIÓS AJÁNLÁS

`#1D1D1B` és fehér keverékei; egyik sem márkaérték.

| Token | HEX | Fehéren | Használat |
|---|---|---:|---|
| `--ink` | `#1D1D1B` | **16,88:1** | törzsszöveg, ikonkörvonal, ábravonal — *ez hivatalos érték* |
| `--ink-muted` | `#5C5C5B` | **6,69:1** | másodlagos szöveg, jegyzet, élőláb, **AI-provenance címke** |
| `--rule` | `#8E8E8D` | **3,28:1** | szerkezeti keret: táblacella, jelölőnégyzet, vágóvonal |
| `--rule-soft` | `#CDCDCD` | 1,59:1 | **csak dekoratív** hajszálvonal — jelentést nem hordozhat |
| `--surface` | `#F1F1F1` | 1,13:1 | halvány háttérsáv; `--ink` rajta **14,95:1** |

> ⚠️ **Egy különbség átszivárog az 5–7. szakaszba.** A 7.1. kézírásos mezője és élőlába,
> valamint a pilot-briefek kártya-vágóvonala a `--rule` és `--ink-muted` tokent használja,
> amelyek **csak a B változatban léteznek**. Az A változat választása esetén ezeket a
> helyeket `#1D1D1B`-re kell átírni, eltérő vonalvastagsággal — a
> [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) P-MUN és P-KRT briefjében is.

### Ami mindkettőben azonos, és nem tárgya a választásnak

- a hat alapszín és a tizennyolc árnyalat — változatlanul, a kézikönyv szerint;
- a logó: csak a hivatalos csomagból, **soha nem újrarajzolva, soha nem átszínezve**,
  nem nyújtva, nem forgatva, színátmenet és effekt nélkül;
- a jelmondat írásmódja: `Házák VeÁmác!` / `Házák!` — a kézikönyv a hibás alakokat
  tételesen felsorolja (`Hazak VeAmac`, `Házák Ve Ámác`, `házák veámác`,
  `Hazak Ve'Ematz` stb.);
- balra zárt szöveg, sorkizárás sehol;
- 5 pt-os szövegdoboz-lekerekítés, görbe vonal nélkül;
- az árnyék-korlátozás;
- az 5–7. szakasz teljes tartalma.

### Ajánlás

**B változat.** Egyetlen érdemi indoka van, és az nem esztétikai: az **A változat egy
meg nem válaszolt jogi kérdéstől teszi függővé 247 asset gyártásának indulását**, miközben
a B ugyanazt a márkaszín- és logórendszert viszi, csak a szedésben tér el — ott, ahol a
kézikönyvnek amúgy sincs előírása, mert a betűméret-skálája kitöltetlen.

> **Ez ajánlás, nem jóváhagyott szervezeti döntés.** Az R5 blokkolók a helyükön maradnak.

---

## 9. Amit a jóváhagyónak el kell döntenie

| # | Kérdés | Ajánlás |
|---|---|---|
| **D1-a** | Átvesszük-e a hivatalos arculati kézikönyv palettáját a tananyagra? | **Igen** — first-party, deklarált, a hivatalos vektorral megerősített |
| **D1-b** | A **2022-es** (kézikönyv + logócsomag) színgeneráció a hatályos, nem a `somer.hu`-n még élő 2021-es? | **Igen** — de ezt a szervezetnek meg kell erősítenie |
| **D1-c** | **A** vagy **B** változat (betűtípus + semleges skála)? | **B** |
| **D1-d** | Elfogadható-e, hogy a szín-szótár **modul-hatókörű**, és az elsődleges megkülönböztető mindig a forma/betűjel? | **Igen** — a 2.5. mérés szerint más nem is működne |
| **D1-e** | A `#2B2523` deklarálatlan részletszín használható-e, vagy maradjon a logón belül? | **Maradjon a logón belül**; a tananyag `#1D1D1B`-t használ |

Amit **nem** kérdezünk, mert a repository már eldöntötte: az AI-címke szövegét (R1, D9)
és azt, hogy a címke LMS-szöveg, nem képbe égetett elem (7.3.).

## 10. Elfogadási feltétel

A stílus-token akkor zárható, ha:

- [ ] D1-a … D1-e megválaszolva;
- [ ] a `produkcios-szabalyok.json` R5 szövegéből kivezethető a nyitott érték;
- [ ] a [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) 4. szakaszának mezői
      kitöltve;
- [ ] a családonkénti pilotok
      ([`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md)) elfogadva;
- [ ] `python3 tools/media_manifest.py build` lefutott, és a köteg-terv frissült.
