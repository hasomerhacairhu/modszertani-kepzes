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

A „Kutatás” oszlop azt mutatja, hogy a **jelöltek** feltételei ismertek-e. Ettől a
bizonyíték állapota **nem változik**: az R2 a *ténylegesen használt produkciós fiókra*
kér igazolást, nem egy nyilvános feltétel-oldal létezésére.

| # | Bizonyíték | Mire kell | Állapot | Kutatás |
|---|---|---|---|---|
| R2-1 | A képgeneráló eszköz / szolgáltató **neve és verziója** | mind a 28 | **HIÁNYZIK** | KUTATVA — jelöltek és verziók: 1/A.1., 1/A.2. |
| R2-2 | A szolgáltató **kereskedelmi-oktatási felhasználást engedő** licencfeltétele (a felhasznált verzióra érvényes szövegváltozat) | mind a 28 | **HIÁNYZIK** — a fiókhoz és a választott csomaghoz kötött szövegváltozat kell | KUTATVA — a jelöltek nyilvános záradékai idézve: 1/A.1., 1/A.2. |
| R2-3 | **Avatar- / képmás-jogosultság**: az avatar nem valós, azonosítható személy hasonmása, vagy van rá engedély | 26 videó + 2 állókép | **HIÁNYZIK** | KUTATVA — a jelöltek hozzájárulási feltételei idézve; a **J2 kiskorú-kérdés** nyitva: 1/A.3. |
| R2-4 | A hanggeneráló eszköz **neve és verziója** | minden szintetikus hang | **HIÁNYZIK** — a D2 dönti el, hogy egyáltalán lesz-e | KUTATVA — jelöltek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13. szakasz |
| R2-5 | **Voice-talent release** vagy hangklónozási engedély | csak szintetikus hangnál | **HIÁNYZIK** — a D2-től függ | a jelölt stackek **készlet-hangot** használnának, klónozás nélkül; a záradékok a hang-bible 13. szakaszában |
| R2-6 | Emberi felmondó esetén **felhasználási szerződés** | csak emberi felmondónál | **HIÁNYZIK** — a D2-től függ | KUTATVA — a szerződés-szerkezet kockázata (51-szeres árkülönbség) a hang-bible 13.4. pontjában |

> **Fontos következmény.** Ha a D2 válasza **szintetikus hang**, az R2 „AI-hang” ága
> nemcsak a 28 videóra, hanem **mind a 90 narráció-assetre** is kiterjed. Ha emberi
> felmondó lesz, akkor az R2-5 helyére az R2-6 lép, és a narrációk nem kerülnek az R2
> hatálya alá. **Ez a döntés következménye, nem külön kérdés** — de a bizonyíték-listát
> a válasz után újra kell futtatni.

---

## 1/A. Szolgáltató-kutatás (2026-08-27) — a bizonyíték-igény konkrétummá tétele

> **A fenti hat sor állapota változatlanul HIÁNYZIK, és a 28 asset R2-blokkolója a
> helyén marad.** Ez a szakasz csak annyit tesz, hogy a „⟬generátor neve⟭” absztrakt
> mezőt lecseréli **megnevezett jelöltekre és a hozzájuk tényleg tartozó, idézhető
> feltételekre** — hogy a jogi jóváhagyó ne nulláról induljon.
>
> **A nyilvános szolgáltatási feltétel nem azonos a produkciós fiók bizonyítékával.**
> Fiókot nem hoztunk létre, próbaidőszakot nem indítottunk, generálást nem futtattunk.

Állapotjelölés ebben a szakaszban:

| | |
|---|---|
| `EVIDENCE_FOUND` | a kérdéses feltétel a szolgáltató saját oldalán megtalálható és idézhető |
| `EVIDENCE_INCOMPLETE` | egy része megvan, más része nem volt lekérdezhető |
| `USER_ACCOUNT_PROOF_REQUIRED` | csak élő, fizetős fiókból igazolható (pl. tényleges nyelvi minőség, export) |
| `LEGAL_REVIEW_REQUIRED` | van szövegszerű bizonyíték, de a jelentése jogi minősítést igényel |
| `NOT_APPLICABLE` | a jelölt kiesett |

**Nem használunk `SAFE` vagy `LEGAL` állapotot.** Ez a lap nem hoz jogi következtetést.

### 1/A.1. Beszélőfej-videó (21 asset)

| Jelölt | Kereskedelmi használat | Kimenet-tulajdon | Képmás / avatar feltétel | Provenance | Állapot |
|---|---|---|---|---|---|
| **Synthesia** | fizetős előfizetés | „Customer will own all Customer Data” | egyedi avatarnál: az érintett „over the applicable statutory legal age and has provided free and informed consent” | fizetős szinten EU AI Act 50. cikk szerinti jelölés; az AUP **tiltja** a provenance-jelölés eltávolítását | **EVIDENCE_FOUND** — de a magyar szájszinkron, a felirat-export és a felbontás → `USER_ACCOUNT_PROOF_REQUIRED` |
| **HeyGen** | fizetős csomagon igen; ingyenesen **nem kereskedelmi** | „you own all rights in your User Input or User Output” | tiltja mások képének feltöltését „without their consent”; avatar-hozzájáruláshoz beszélt nyilatkozat, szemantikusan ellenőrizve | nem ellenőrzött | **EVIDENCE_INCOMPLETE** |
| **BytePlus OmniHuman 1.5** | igen | „you own the Output generated in response to your Input” | az AUP megköveteli a hozzájárulást, de **technikai korlát nincs** — a felelősség a felhasználóé | **nincs C2PA**, nincs felirat-kimenet | **EVIDENCE_INCOMPLETE** — az általános AUP hatálybalépési dátuma jövőbeli (2026-09-28) |

**Egyedül a Synthesia ad kártalanítást a megrendelő felé** a készlet-avatar képmás- és
személyiségi jogi igényeire; a HeyGen feltételeiben a felhasználó kártalanítja a
szolgáltatót.

### 1/A.2. AI karakter-jelenet (5 asset + 1 B-roll) és freeze-frame (2 asset)

| Jelölt | Kereskedelmi használat | Kimenet-tulajdon | Tanítás a bemeneten | Provenance | Állapot |
|---|---|---|---|---|---|
| **Google Veo 3.1 GA (Vertex AI)** | fizetős Vertex | „Google does not assert any ownership rights in any new intellectual property created in the Generated Output” | „Google will not use Customer Data to train or fine-tune any AI/ML models without Customer's prior permission” | SynthID + C2PA | **LEGAL_REVIEW_REQUIRED** — lásd az 1/A.3. korhatár-záradékot |
| **Runway Gen-4.5** | „does not restrict your commercial use of your Outputs”, szintkorlát nélkül | „does not claim ownership of any of your Inputs or Outputs” | **igen** — „Inputs and Outputs may be used by the Company to train and improve its AI models” | C2PA | **EVIDENCE_FOUND** |
| **Kling 3.0 Omni** | az alap-ToS 4.6 **tiltja** engedély nélkül; csak fizetős tagsági kedvezményként oldódik fel | 4.4 szerint a tiéd | van, e-mailes leiratkozással | a vízjel eltávolítása fizetős kedvezmény | **LEGAL_REVIEW_REQUIRED** |
| **OpenAI Sora 2** | — | — | — | — | **NOT_APPLICABLE** — az API-ból 2026-09-24-én kivezetik, és emberi hasonmást ábrázoló karakter-feltöltést blokkol |

A karakter rögzítéséhez vizsgált képgenerátor (`gemini-3-pro-image`, „Nano Banana Pro”)
a dokumentációja szerint karakter-konzisztenciához
**legfeljebb 5 referenciakép** adható meg („Up to 5 images of characters to maintain
character consistency”), és kimondja, hogy „All generated images include a SynthID
watermark”.

### 1/A.3. Két kérdés, amit ez a lap NEM dönt el — emberi kapu

| # | Kérdés | Bizonyíték | Kihez tartozik |
|---|---|---|---|
| **J1** | A Google Cloud Service Specific Terms §20(d) szerint az ügyfél nem használhat generatív AI-szolgáltatást olyan online szolgáltatás részeként, amely „directed towards or is likely to be accessed by individuals under the age of 18”. A tananyag célközönsége **15+**, és a madrich maga is lehet kiskorú. Hogy az **offline legyártott, majd Moodle-ön kiszolgált** asset ebbe a mondatba esik-e, jogi olvasat. | idézve fent | **jogi jóváhagyó** — ez a javasolt karakter-jelenet stacket kizárhatja |
| **J2** | A Synthesia AUP tiltja kiskorúak avatarral való ábrázolását, az egyedi avatar feltétele a nagykorúság, a Veo EU-ban `allow_adult` személy-generálást enged. Ebből az következik, hogy **a beszélőfej és a karakter felnőttnek kell hogy látsszon** — miközben a tananyag szerint a madrich maga is lehet kiskorú, és a jelenetek „madrichot” ábrázolnak. | idézve fent | **gyermekvédelmi felelős + szerzői döntés** — ez tananyagi és gyermekvédelmi kérdés, nem eszközválasztás. A kánoni hely: `Gyermekvédelem – release gate.md` és `Emberi jóváhagyás szükséges.md`. |

> **A J2 nem oldható meg produkciós oldalról.** Ez a lap rögzíti, hogy a kérdés
> felmerült, és megáll.

### 1/A.4. Ami a kutatásból hiányzik

- **A Synthesia és a HeyGen magyar szájszinkronja és felirat-exportja nem ellenőrzött** —
  pedig ez pass/fail feltétel. Csak élő fiókkal, illetve a pilot legyártásával dönthető el.
- D-ID, Colossyan, Elai.io, Creatify, Argil: nem vizsgálva.
- Adobe Firefly: a jogi és árazási oldalak nem voltak elérhetők. A „commercially safe”
  marketingszöveg **nem** kártalanítási vállalás.
- Midjourney: a dokumentáció és a jogi oldal HTTP 403-at adott.
- MiniMax/Hailuo és Pika jogi feltételei: JS-renderelt oldalak, szöveg nem nyerhető ki.
- Az Azure és a Google **kimenet-tulajdonlási** záradéka a hang oldalán (R2-4)
  nem lett lekérdezve.

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
