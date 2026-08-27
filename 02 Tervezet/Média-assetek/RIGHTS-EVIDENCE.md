# 📄 Jogi bizonyíték-nyilvántartás (R2 / R8)

**Ez a lap nem hoz jogi következtetést.** Nyilvántartás: rögzíti, milyen bizonyítéknak
kell léteznie egy asset-osztály élesítése előtt, és hogy az a bizonyíték **megvan-e**.
A „megfelel-e” kérdésre a jogi, adatvédelmi és gyermekvédelmi jóváhagyó válaszol, nem ez
a fájl és nem a fordító.

Állapotjelölés:

| | |
|---|---|
| **HIÁNYZIK** | a bizonyíték nincs meg; az asset-osztály nem élesíthető |
| **MEGVAN** | a bizonyíték létezik, hivatkozással; a jóváhagyó minősítette |
| **NEM ALKALMAZHATÓ** | a szabály szövege nem terjed ki erre az osztályra — az indoklással együtt |

> **Személyes adat ebbe a fájlba nem kerül.** Név, e-mail, telefonszám, szülői
> hozzájáruló nyilatkozat vagy annak másolata **nem** a repositoryban él. Ide csak a
> *létezés* ténye és egy nem-személyes hivatkozás (ügyszám, dosszié-azonosító) kerülhet.

---

## 1. R2 — AI-avatar és AI-hang

**A szabály szövege** (`produkcios-szabalyok.json`): „Minden AI-avatar és AI-hang
assethez dokumentálandó: a használt generátor neve, a kereskedelmi/oktatási felhasználást
engedő licenc, és a voice-talent release.”

**Jelenlegi hatálya a manifesztben: 28 asset.** A hatály 2026-08-27-én eldőlt (A opció,
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) lezárt döntések): a szigorúbb
olvasat marad érvényben, hacsak egy későbbi jogi review kifejezetten nem szűkíti.
**Ami nyitva maradt, az maga a bizonyíték** — az alábbi hat sor.

| Osztály | Assetek | Miért tartozik ide |
|---|---:|---|
| **AI beszélőfej-videó** | 21 | szintetikus emberi persona, aki a tananyag nevében beszél |
| **AI karakter-jelenet (teljes alakos)** | 5 | `M1.3-VID-01`, `M4.1-VID-02/03/04/05` — AI-generált emberi alak, szintetikus narrációval |
| **Karakter-freeze-frame** | 2 | `M4.1-FOTO-01/02` — a fenti videókból kivett állókép |
| **Hétköznapi AI-illusztráció, ikon, diagram** | 0 | **NEM tartozik ide:** az R2 avatar- és hangjog, nem általános AI-tartalom kapu. Ezekre az R1 (AI-jelölés) vonatkozik. |

### Szükséges bizonyítékok

| # | Bizonyíték | Mire kell | Állapot | Hivatkozás |
|---|---|---|---|---|
| R2-1 | A képgeneráló eszköz / szolgáltató **neve és verziója** | mind a 28 | **HIÁNYZIK** | — |
| R2-2 | A szolgáltató **kereskedelmi-oktatási felhasználást engedő** licencfeltétele (a felhasznált verzióra érvényes szövegváltozat) | mind a 28 | **HIÁNYZIK** | — |
| R2-3 | **Avatar- / képmás-jogosultság**: az avatar nem valós, azonosítható személy hasonmása, vagy van rá engedély | 26 videó + 2 állókép | **HIÁNYZIK** | — |
| R2-4 | A hanggeneráló eszköz **neve és verziója** | minden szintetikus hang | **HIÁNYZIK** — a D2 dönti el, hogy egyáltalán lesz-e | — |
| R2-5 | **Voice-talent release** vagy hangklónozási engedély | csak szintetikus hangnál | **HIÁNYZIK** — a D2-től függ | — |
| R2-6 | Emberi felmondó esetén **felhasználási szerződés** | csak emberi felmondónál | **HIÁNYZIK** — a D2-től függ | — |

> **Fontos következmény.** Ha a D2 válasza **szintetikus hang**, az R2 „AI-hang” ága
> nemcsak a 28 videóra, hanem **mind a 90 narráció-assetre** is kiterjed. Ha emberi
> felmondó lesz, akkor az R2-5 helyére az R2-6 lép, és a narrációk nem kerülnek az R2
> hatálya alá. **Ez a döntés következménye, nem külön kérdés** — de a bizonyíték-listát
> a válasz után újra kell futtatni.

### Amit ez a lap NEM állít

- Nem mondja ki, hogy bármelyik szolgáltató „kereskedelmileg biztonságos”.
- Nem minősít licencszöveget.
- Nem dönti el az EU AI Act szerinti szerepbesorolást. Az R1 szövege erről már rögzíti,
  hogy az 50. cikk (2) gépi jelölési kötelezettsége a szintetikus tartalmat előállító
  rendszer **szolgáltatóját** terheli, nem az oktatási médiát készítő szervezetet, és hogy
  az 50. cikk (4) deployer-oldali eseteinek alkalmazhatóságát **jogi review** minősítse.
  Ez a lap ezt átveszi, nem értelmezi tovább.

---

## 2. R8 — GDPR és képmás valós felvételen

**A szabály szövege:** „Valós fotó/screenshot esetén minden azonosítható
személyt/kézírást anonimizálni vagy kikeretezni kell; felismerhető kiskorúnál
dokumentált szülői hozzájárulás ELŐRE kötelező. Screenshotnál nincs valós
felhasználónév/arc és nincs licenc-korlátos 3rd-party elem.”

**Jelenlegi hatálya: 2 asset.** Mindkettő valós felvétel; a tananyagban több nincs.

| Asset | Mi ez | Miért R8 | Osztály |
|---|---|---|---|
| `M0.3-FOTO-01` | Moodle kurzus-főoldal képernyőkép | valós képernyőkép: felhasználónév, arc, harmadik felas elem kerülhet rá | **ADATVÉDELMI ÁTALAKÍTÁS KELL** |
| `M0.A-FOTO-01` | a képző által készített fotók a kitöltött kvuca-plakátokról | valós felvétel **kézírásról**, kiskorúak által írt tartalommal | **EMBERI POLICY-DÖNTÉS KELL** — egyben élő/runtime tétel: a képző a peula után készíti, nem központi előgyártás |

### Szükséges bizonyítékok és teendők

| # | Tétel | Mit kell tenni / igazolni | Állapot |
|---|---|---|---|
| R8-1 | `M0.3-FOTO-01` | a képernyőkép **teszt-fiókkal** készüljön: nincs valós felhasználónév, nincs arc, nincs licenc-korlátos harmadik felas elem | **HIÁNYZIK** (a felület sem áll még — R7) |
| R8-2 | `M0.A-FOTO-01` | a plakátfotó **kézírást** rögzít: eldöntendő, hogy anonimizálás (nevek kitakarása) elég-e, vagy előzetes írásos hozzájárulás kell | **HIÁNYZIK** → D8 |
| R8-3 | `M0.A-FOTO-01` | ha felismerhető kiskorú kerülhet a képre: **előzetes, dokumentált szülői hozzájárulás** | **HIÁNYZIK** → D8; a nyilatkozatok NEM ebben a repositoryban élnek |
| R8-4 | `M0.A-FOTO-01` | megőrzési idő és hozzáférési kör az archívumra (a fotó a Z.A peuláig áll) | **HIÁNYZIK** — adatvédelmi (DPO) hatáskör |

### Ahol az R8 NEM alkalmazható — és miért

Ezek a tételek korábban R8 alatt álltak; a besorolás a szabály szövegével ütközött.
A kivezetés indoka minden esetben az asset saját deklarációjából következik:

| Asset(ek) | Korábbi állapot | Miért nem alkalmazható |
|---|---|---|
| `M3.F-EGY-01`, `M3.F-EGY-02`, `M4.F-EGY-01`, `M4.F-EGY-02`, `M5-HUB-EGY-01`, `M6.F-EGY-01` | R8 | Beszerzendő fizikai irodaszer (post-it, matrica, filc, marker). Nem fotó, nem képernyőkép, **nincs képi tartalma**; a saját specifikációjuk is kimondja, hogy „nem grafikai gyártás”. Az R8-nak nincs rájuk alkalmazható kikötése. |
| `M2.3-FOTO-01` | R8 | AI-generált háttérvizuál. A lecke „someres/kvuca-vizuál” hátteret ír elő, nem valós fotót; az asset eredete `ai`. Helyette **R5** (vizuális rendszer) + R1 (AI-jelölés). |
| `M4.1-FOTO-01`, `M4.1-FOTO-02` | R8 | Az AI-generált karakterjelenetekből (`M4.1-VID-03/04/05`) kivett freeze-frame; nem valós személy felvétele. Helyette **R2** (AI-karakter jogtisztaság) + **R5** (karakter-lock) — az R5 szövege maga mondja ki, hogy „a freeze-frame-ek a videó-gyártás részeként” készülnek. |

> A hat beszerzési tétel ezzel `specifikáció kész` állapotba került. Ez **nem** jogi
> engedély semmire: azt állítja, hogy egy doboz filc megvásárlásának nincs képmásvédelmi
> feltétele.

### Ami már megtörtént kockázatcsökkentés

Az M6.3 leckében a projekt korábban **fotóról illusztrációra** váltott, kimondottan a
GDPR-kockázat elkerüléséért („DÖNTÉS: illusztráció (GDPR-kockázat elkerülése),
FOTO→ILL”). Ennek eredménye, hogy a 417 assetből ma **kettő** épül valós felvételre.
Ez a lap ezt a döntést rögzíti, nem bírálja felül — és nem is használható arra, hogy egy
**kötelezően valós** felvételt (a Moodle-képernyőképet) illusztrációra cseréljünk.

---

## 3. R1 — AI-provenance (nem kapu, de nyilvántartandó)

Az R1 **kötelező projektszabály**, nem nyitott kapu: minden `provenance=ai` asseten
egyetlen kanonikus, ember-olvasható AI-címke kell. Ez 280 assetet érint.

| # | Tétel | Állapot |
|---|---|---|
| R1-1 | A címke **egységes szövege** | **MEGVAN** — 2026-08-27-én jóváhagyva, szó szerint: **AI-generált médiaelem · emberi lektorálással.** Rögzítve a `produkcios-szabalyok.json` R1 szabályában (`human_label` mező), és kivezetve a tananyag mind a 21 aktív előfordulására; a korábbi négy változat megszűnt. Regressziós teszt őrzi (`TestApprovedDecisions`). |
| R1-2 | A címke vizuális formája és elhelyezése | **HIÁNYZIK** → D1 első lépcső / [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md). A szöveg eldőlt, a megjelenés nem. |
| R1-3 | Gépi provenance-jelölés (C2PA / Content Credentials / vízjel) megmaradása az exportban | **HIÁNYZIK** — a generátor kiválasztása után ellenőrizendő (R2-1) |

---

## 4. Mit kell tenni, ha egy bizonyíték megérkezik

1. Írd be a fenti táblába a **hivatkozást** (ügyszám, dosszié-azonosító, szerződés
   megnevezése — **nem** személyes adatot), és állítsd az állapotot **MEGVAN**-ra.
2. Ha ezzel egy teljes kapu lezárul, vezesd ki a nyitott-érték jelölést a
   `produkcios-szabalyok.json` megfelelő szabályából és a
   [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) döntéséből.
3. Futtasd: `python3 tools/media_manifest.py build`.
4. A köteg-terv (`MEDIA-PRODUCTION-PLAN.md`) automatikusan
   átsorolja az érintett asseteket.
