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
| R2-4 | A hanggeneráló eszköz **neve és verziója** | minden szintetikus hang | **RÉSZBEN MEGVAN** — a szolgáltató **ElevenLabs** (felhasználói döntés, 2026-08-28); a **modell-azonosító és a voice-ID még hiányzik** | a szolgáltató és a modell-javaslat: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13. szakasz |
| R2-5 | **Hang-jogosultság**: a felhasznált egyedi hang használatának joga | a kiválasztott kanonikus hangra | **HIÁNYZIK** | KUTATVA — a szolgáltató feltételei és a hangtípusonkénti következmény: 1/A.0. |
| R2-6 | Emberi felmondó esetén felhasználási szerződés | — | **NEM ALKALMAZHATÓ** — a felmondás 2026-08-28 óta szintetikus | — |

> **Fontos következmény.** Ha a D2 válasza **szintetikus hang**, az R2 „AI-hang” ága
> nemcsak a 28 videóra, hanem **mind a 90 narráció-assetre** is kiterjed. Ha emberi
> felmondó lesz, akkor az R2-5 helyére az R2-6 lép, és a narrációk nem kerülnek az R2
> hatálya alá. **Ez a döntés következménye, nem külön kérdés** — de a bizonyíték-listát
> a válasz után újra kell futtatni.

---

## 1/A. Szolgáltató-kutatás (2026-08-27, kiegészítve 2026-08-28) — a bizonyíték-igény konkrétummá tétele

> **A 28 asset R2-blokkolója változatlanul a helyén marad.** A fenti hat sorból négy
> továbbra is **HIÁNYZIK**; az R2-4 a szolgáltatói döntés után **RÉSZBEN MEGVAN**, az
> R2-6 pedig **NEM ALKALMAZHATÓ** lett (a felmondás szintetikus). **Egyik sem jelent
> feloldást:** a hiányzó rész — voice-ID, modell, licenc-igazolás, hang-jogosultság —
> mind megvan még.** Ez a szakasz csak annyit tesz, hogy a „⟬generátor neve⟭” absztrakt
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
| `ACCOUNT_EVIDENCE_REQUIRED` | csak élő, fizetős fiókból igazolható (pl. voice-ID, hangtípus, tényleges nyelvi minőség, export, vízjel) |
| `CONSENT_EVIDENCE_REQUIRED` | a szolgáltató nem ír elő bizonyíték-formát; a szervezetnek kell hozzájárulást tartania |
| `LEGAL_REVIEW_REQUIRED` | van szövegszerű bizonyíték, de a jelentése jogi minősítést igényel |
| `NOT_APPLICABLE` | a szabály vagy a jelölt erre az esetre nem alkalmazható |

**Ez a szótár a lap egészére érvényes**, az 1. szakasz `HIÁNYZIK` / `MEGVAN` /
`NEM ALKALMAZHATÓ` hármasával együtt (az 1. szakasz a *bizonyíték meglétét* követi, ez a
szakasz a *bizonyíték jellegét*).

**Nem használunk `SAFE` vagy `LEGAL` állapotot.** Ez a lap nem hoz jogi következtetést.

### 1/A.0. ElevenLabs egyedi hangok — a kanonikus narrátor jelöltjei

A szolgáltató **eldőlt** (felhasználói döntés, 2026-08-28). A hang **nem**: a két
forrás-beszélő — Dombi Miksa és Budai Enn — felvételeiből előbb **létre kell hozni** a
két egyedi hangot (a módszer nyitott, V2 hozzájárulás-bizonyíték a feltöltés előtt
kötelező), és utána lehet választani, meghallgatással
([`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md)).

> ⛔ **A hangok még nem léteznek** — voice-ID és hangtípus a létrehozás után rögzíthető.
> Ebben a környezetben ráadásul **nincs ElevenLabs hitelesítő adat**, ezért semmit **nem
> kérdeztünk le, és nem találtunk ki.** A létrehozás utáni azonosítás menete:
> [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.4.

| Mező | Dombi Miksa | Budai Enn |
|---|---|---|
| Hang (voice-objektum) létezik? | `MÉG NEM — LÉTREHOZANDÓ` | `MÉG NEM — LÉTREHOZANDÓ` |
| `voice_id` | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| `voice_type` (`category`) | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Fióktulajdon / kontextus | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Létrehozás forrása (mire tanult) | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Magyar nyelvre igazolt-e | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| **Hozzájárulás / felhasználási jog** | `CONSENT_EVIDENCE_REQUIRED` | `CONSENT_EVIDENCE_REQUIRED` |
| Kereskedelmi / oktatási használat | `EVIDENCE_FOUND` — fizetős csomag esetén | `EVIDENCE_FOUND` — fizetős csomag esetén |

**A név nem bizonyíték.** Az, hogy egy hangot „Dombi Miksa”-nak vagy „Budai Enn”-nek
hívnak, **önmagában semmit nem igazol** arról, hogy van-e jog egy valós személy hangját
használni. A hangtípus dönti el, mit kell igazolni:

| Ha a hang típusa… | …akkor a jogosultsági helyzet |
|---|---|
| **Professional Voice Clone** | a szolgáltató szerint **csak saját hang** klónozható — „Even with their consent, you cannot clone someone else's voice”. Igazolandó: hogy a fiók tulajdonosa és a hang tulajdonosa ugyanaz |
| **Instant Voice Clone** | a szolgáltató **önbevalló jelölőnégyzettel** intézi, és **semmilyen bizonyíték-formát nem ír elő**. Hogy a szervezet milyen hozzájárulást tart, milyen formában és meddig, **a mi döntésünk** — `CONSENT_EVIDENCE_REQUIRED` |
| **Voice Design (tervezett, szintetikus)** | a hang nem azonosított természetes személyről készült, tehát a klónozási hozzájárulás kérdése **nem merül fel ugyanabban a formában** → `LEGAL_REVIEW_REQUIRED`, azzal az indoklással, hogy nincs azonosított érintett. **Ez a lap nem mondja ki, hogy „nincs jogi kérdés"** — azt a jóváhagyó állapítja meg |

**A szolgáltató feltételeiből idézve:**

| # | Tárgy | Szöveg | Állapot |
|---|---|---|---|
| E-1 | Kereskedelmi használat | ingyenes szinten „only use the Services for non-commercial purposes”; fizetős előfizetéssel „may use the Services for commercial purposes” | `EVIDENCE_FOUND` — **fizetős csomag kötelező** |
| E-2 | Kimenet-tulajdon | „you retain all rights in and to your Output” | `EVIDENCE_FOUND` |
| E-3 | Klónozási feltétel | „your voice or a voice you are authorized to share with us”; tiltott más hangjának replikálása „without consent or legal right” | `CONSENT_EVIDENCE_REQUIRED` — **bizonyíték-formát a szolgáltató nem ír elő** |
| E-4 | Tanítás a bemeneten | a kimaradás bármikor bekapcsolható, de „**does not affect any uses… prior to that date**” | `EVIDENCE_FOUND` — **a kimaradást ELŐRE kell bekapcsolni** |
| E-5 | Megőrzés | a hangról generált adatot „not… longer than 3 years after your last interaction” | `EVIDENCE_FOUND` |
| E-6 | Gépi provenance | hallhatatlan hangvízjel; **a beszéd-kimeneten nincs C2PA**; robusztussági leírás nincs; a lefedettséget nem nyilvánították befejezettnek | `EVIDENCE_INCOMPLETE` — az R1 gépi ága a hangon **nem értelmezhető** |
| E-7 | Közlési kötelezettség | a kifejezett előírás **AI-ügynökökre** szól, nem előre renderelt narrációra | `NOT_APPLICABLE` — az R1-címke **projektszabály**, és az is marad |
| E-8 | Kiskorúak | a feltételek szerint 18 alatti nem használhatja a szolgáltatást és kiskorú hangadata nem tölthető fel; a tiltólista viszont 13–18 közötti használatot szülői hozzájárulással elképzelhetőnek tart — **a saját dokumentumaik nem mondanak ugyanazt** | `LEGAL_REVIEW_REQUIRED` — lásd V3 |

### 1/A.1. Beszélőfej-videó (21 asset) — a szolgáltató **HeyGen** (felhasználói döntés, 2026-08-28)

A szolgáltató-választás lezárult; ez a szakasz már nem hasonlít össze jelölteket, hanem a
**választott** szolgáltató feltételeit rögzíti. A korábban vizsgált, **nem választott**
alternatívák (Synthesia, BytePlus OmniHuman) csak nyomon követhetőségért maradnak
megemlítve — a jelenlegi gyártási útvonalnak nem részei.

Minden idézet a szolgáltató saját feltételeiből, lekérdezve 2026-08-28.

| # | Feltétel | Bizonyíték | Állapot |
|---|---|---|---|
| H-1 | **Kereskedelmi használat és kimenet-tulajdon** | „As between HeyGen and you, **you own all rights in your User Input or User Output**, and does not restrict your ability to use User Output for your own purposes (**including for commercial purposes**)… we hereby **assign to you all right, title and interest**” | `EVIDENCE_FOUND` |
| H-2 | **Az ingyenes csomag kizárt** | az ingyenes szinten a kimenet „solely for personal, non-commercial, and internal evaluation purposes”, és „may not be sold, sublicensed, redistributed, monetized, or used in connection with commercial activities” | `EVIDENCE_FOUND` — **fizetős csomag kötelező** |
| H-3 | **Avatar-hozzájárulás** | „Consent applies only to **digital twin** avatars. Photo avatars… and prompt-to-avatar characters… depict no real, identifiable person and do **not** require consent.” A tervezett útvonal **nyilvános készlet-avatart** használ, tehát hozzájárulási lánc nem keletkezik | `EVIDENCE_FOUND` a készlet-avatarra |
| H-4 | **Feltöltött tartalom szavatossága** | „you represent and warrant that you have, or have obtained, **all rights, licenses, consents, permissions, power and/or authority** necessary to grant the rights granted herein for Your Content.” — ez a **feltöltött hangmesterre is vonatkozik** | `CONSENT_EVIDENCE_REQUIRED` — lásd H-5 |
| H-5 | **A feltöltött tartalomra adott licenc** | a feltöltött tartalomra a szolgáltató „a license to… modify Your Content to operate, improve, promote and provide the Services and to develop new services and products, **including to train or otherwise improve or modify our artificial intelligence and machine learning models**”-t kap, amely „royalty-free, transferable, sublicensable, worldwide and **irrevocable**”, és a szerződés megszűnését is túléli | **`LEGAL_REVIEW_REQUIRED`** — lásd a J3 kaput |
| H-6 | **AI-közlési kötelezettség** | „if you distribute your User Output to others, to the extent required by applicable law, you must **proactively disclose that such User Output was created using artificial intelligence technologies**” | `EVIDENCE_FOUND` — a tananyag R1-címkéje ezt kiszolgálja |
| H-7 | **Kiskorú megjelenésű avatar tilalma** | tiltott az olyan avatar, amely „Represent or appear in the sole discretion of HeyGen to represent **individuals under the age of 18**” | `EVIDENCE_FOUND` — lásd a J2 kaput |
| H-8 | **Gépi provenance (C2PA)** | a szolgáltató etikai lapja szó szerint a **Content Authenticity Initiative** tagságát mondja ki („We are a member of the Content Authenticity Initiative”) — **a C2PA nevet nem használja**, és sem ez a lap, sem a fejlesztői dokumentáció, sem az OpenAPI-leírás, sem a feltételek **nem állítják**, hogy Content Credentials kerülne magába a kimeneti fájlba. *(A CAI és a C2PA rokon, de nem ugyanaz.)* | `ACCOUNT_EVIDENCE_REQUIRED` — egyetlen próbarendereléssel eldönthető |
| H-8/b | **Vízjel az API-kimeneten** | a **fogyasztói** előfizetési oldal kifejezetten felsorolja a „vízjel-eltávolítást” a fizetős szinteken; az **API-útvonalra** viszont a per-másodperc árlap, a korlát-leírás és a feltételek egyaránt **hallgatnak** — sem azt nem mondják, hogy vízjelezett, sem azt, hogy nem | `ACCOUNT_EVIDENCE_REQUIRED` — a hiányból következtetni nem elég |
| H-9 | **A hangmester sértetlensége** | a dokumentáció **nem nyilatkozik** arról, hogy a feltöltött hang újrakódolás nélkül kerül-e a kimeneti MP4-be | `ACCOUNT_EVIDENCE_REQUIRED` — a pilot méri |
| H-10 | **Moderáció** | a nem engedélyezett tartalmak közt szerepel a „**Political**: Content that displays political opinions…”, és a szolgáltató automatikus moderációt futtat; érzékeny („conditional”) oktatási tartalom pedig „can be created using **custom avatars only**” | `ACCOUNT_EVIDENCE_REQUIRED` — csak beküldéssel deríthető ki, hogy ez a tananyag átmegy-e |
| H-11 | **Kártalanítás iránya** | a szolgáltató feltételei **nem** vállalnak kártalanítást a megrendelő felé a készlet-avatar képmás- vagy személyiségi jogi igényeire; a szavatosság a **feltöltő** oldalán áll („you represent and warrant that you have… all rights, licenses, consents…”). Egy korábban vizsgált, **nem választott** alternatíva ezen a ponton kedvezőbb volt — ez a különbség a szolgáltatóváltással **eltűnt**, és tudni kell róla | `LEGAL_REVIEW_REQUIRED` |

> **A H-5 a legfontosabb új tétel.** A gyártási lánc szerint a **klónozott egyedi hang
> hangmesterét** töltjük fel a szolgáltatóhoz. A fenti záradék szerint ezzel a
> szolgáltató visszavonhatatlan, továbbadható licencet kap arra, hogy ezen a hangon
> **modelljeit tanítsa**. Ha a hang valós személy hangjának klónja, ez **nem csak a
> szervezet döntése, hanem az érintett személyé is**.
>
> Két pontosítás, hogy ez ne legyen túlállítva:
> 1. A záradék a feltételekben a **Creator / Pro / Business csomagok** felhasználóira van
>    címezve. Hogy az **API-s, feltöltött egyenlegű** útvonalra ugyanez vonatkozik-e, vagy
>    külön feltétel, a dokumentumból **nem állapítható meg** — a feltételek szövege az
>    API-csomagot meg sem említi.
> 2. A szolgáltató saját etikai nyilatkozata azt írja, hogy felhasználói adatot
>    „only with consent” használ modelljavításra. A két szöveg **nem mond ugyanazt**; a
>    feltételek a frissebbek.
>
> **Ez a lap nem dönti el, melyik az irányadó.** → `J3`, 1/A.3.

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

### 1/A.3. Három kérdés, amit ez a lap NEM dönt el — emberi kapu

| # | Kérdés | Bizonyíték | Kihez tartozik |
|---|---|---|---|
| **J1** | A Google Cloud Service Specific Terms §20(d) szerint az ügyfél nem használhat generatív AI-szolgáltatást olyan online szolgáltatás részeként, amely „directed towards or is likely to be accessed by individuals under the age of 18”. A tananyag célközönsége **15+**, és a madrich maga is lehet kiskorú. Hogy az **offline legyártott, majd Moodle-ön kiszolgált** asset ebbe a mondatba esik-e, jogi olvasat. | idézve fent | **jogi jóváhagyó** — ez a javasolt karakter-jelenet stacket kizárhatja |
| **J2** | A **választott beszélőfej-szolgáltató** moderációs politikája tiltja az olyan avatart, amely „Represent or appear in the sole discretion of HeyGen to represent **individuals under the age of 18**”; a karakter-jelenet szolgáltatója pedig EU-ban felnőttre korlátozott személy-generálást enged. Ebből az következik, hogy **a beszélőfej és a karakter felnőttnek kell hogy látsszon** — miközben a tananyag szerint a madrich maga is lehet kiskorú, és a jelenetek „madrichot” ábrázolnak. | idézve a H-7 sorban | **gyermekvédelmi felelős + szerzői döntés** — ez tananyagi és gyermekvédelmi kérdés, nem eszközválasztás. A kánoni hely: `Gyermekvédelem – release gate.md` és `Emberi jóváhagyás szükséges.md`. |
| **J3** | A beszélőfej-szolgáltató a **feltöltött tartalomra** visszavonhatatlan, továbbadható licencet kér, amely kiterjed a **modelljei tanítására** is (H-5). A gyártási lánc szerint épp a **klónozott egyedi hang** hangmesterét töltenénk fel. Ha a hang valós személy hangjának klónja, ez az érintett személy döntése is. Nyitva marad az is, hogy a záradék az API-s útvonalra egyáltalán vonatkozik-e. | idézve a H-5 sorban | **jogi jóváhagyó + a hang jogosultja** — a szervezet nem adhat egyoldalúan tanítási jogot más hangjára |

> **Egyik J-kapu sem oldható meg produkciós oldalról.** Ez a lap rögzíti, hogy a kérdés
> felmerült, és megáll.
>
> **A J3-nak van egy olcsó kikerülő útja, amit érdemes mérlegelni:** ha a beszélőfej-videók
> hangját nem töltjük fel, hanem a videót **néma** vagy elvetett hanggal generáljuk és a
> hangmestert **utómunkában** illesztjük alá, a feltöltési licenc a hangra nem keletkezik.
> Ennek ára, hogy a szájszinkron a feltöltött hangból származik — tehát ez az út a
> beszélőfejnél **nem járható**, a karakter-jeleneteknél viszont igen, mert azok eleve
> némán készülnek. **Ez nem javaslat, csak a döntési tér pontosítása.**

### 1/A.4. Ami a kutatásból hiányzik

- **A magyar szájszinkron minősége nem ellenőrzött** — pedig ez pass/fail feltétel. A
  szolgáltató a szájszinkront a hanghullámból vezeti, nyelvi támogatási listát ehhez nem
  közöl; csak a pilot legyártásával dönthető el. *(A szolgáltató magyar **TTS**-e ezzel
  szemben már nem kérdés: a hangot az ElevenLabs adja, a szolgáltató TTS-e nincs
  használatban.)*
- **Négy dolog, amit csak egyetlen próbarenderelés dönt el** (H-8, H-9, H-10 és a
  vízjelmentesség): beágyaz-e a kimenet gépi provenance-jelölést; sértetlen marad-e a
  feltöltött hangmester; átengedi-e a moderáció ezt a tananyagot; és tényleg vízjelmentes-e
  a fizetős render.
- **A beszélőfej-avatar nem verziózható.** A szolgáltató avatar-leíró rekordjában nincs
  verzió-mező, és a motorok viselkedése menet közben változik. Ez nem jogi, hanem
  reprodukálhatósági kockázat — a produkciós válasz: egyetlen időablakban gyártani és
  archiválni.
- A korábban vizsgált, **nem választott** beszélőfej-alternatívák (Synthesia, BytePlus
  OmniHuman, D-ID, Colossyan, Elai.io, Creatify, Argil) nyilvános feltételeit ez a lap
  már nem tartja karban.
- Adobe Firefly: a jogi és árazási oldalak nem voltak elérhetők. A „commercially safe”
  marketingszöveg **nem** kártalanítási vállalás.
- Midjourney: a dokumentáció és a jogi oldal HTTP 403-at adott.
- MiniMax/Hailuo és Pika jogi feltételei: JS-renderelt oldalak, szöveg nem nyerhető ki.
- A **hang oldalán a kimenet-tulajdonlás már ellenőrzött** („you retain all rights in and
  to your Output”), de a **hangtípus és a voice-ID nem** — fióklekérdezés kell hozzá
  (1/A.0.). A korábban vizsgált, nem választott hang-alternatívák (Azure, Google)
  feltételeit ez a lap már nem tartja karban.

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
