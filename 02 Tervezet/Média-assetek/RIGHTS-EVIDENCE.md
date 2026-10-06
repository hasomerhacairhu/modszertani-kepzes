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

> **Személyes adat ebbe a fájlba nem kerül.** Név, e-mail, telefonszám, a résztvevő vagy
> a gondviselő hozzájáruló nyilatkozata vagy annak másolata **nem** a repositoryban él.
> Ide csak a *létezés* ténye és egy nem-személyes hivatkozás (ügyszám, dosszié-azonosító) kerülhet.
>
> A két forrás-beszélő ezért álnéven szerepel (`VOICE-SRC-01`, `VOICE-SRC-02`): a valódi
> név, a szerződés vagy hozzájárulás, a hatókör és a dátum a korlátozott hozzáférésű
> jogosultsági nyilvántartásba tartozik, nem a repositoryba. *(Projektgazdai döntés,
> 2026-10-02, `HUM-MEDIA-02`; utólagos ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős és a
> hang tulajdonosai.)*
>
> **A nyilvántartás** (projektgazdai döntés, 2026-10-02): Google Workspace Shared Drive →
> `Restricted / Rights / Voice`, fájl: `VOICE-RIGHTS-REGISTER`. A projektgazda által név
> szerint kijelölt két személy szerkesztheti (a nevük az `Emberi jóváhagyás szükséges.md`
> `HUM-MEDIA-02` tételében áll, ebbe a fájlba nem kerül); a producer csak az álneveket
> (`VOICE-SRC-01`, `VOICE-SRC-02`) látja. Kötelező mezők: álnév, valódi név, hozzájárulás vagy
> szerződés hivatkozása, engedélyezett felhasználás, modell/szolgáltató, terület, időtartam,
> visszavonás, aláírás dátuma, a bizonyíték helye vagy hash-e, valamint a nagykorúság ellenőrzése (igen/nem,
> dátum, az ellenőrző szerepe; életkor, születési dátum és igazolvány-adat nélkül — kiegészítő projektgazdai
> döntés, 2026-10-03, K6). A forrás-beszélők valódi neve
> semmilyen formában nem kerül a Gitbe.
>
> **A git-előzmények** (projektgazdai döntés, 2026-10-02): a korábbi commitokban maradt
> valódi neveket a repository tulajdonosa egyszeri `git filter-repo` tisztítással
> `VOICE-SRC-01/02` álnévre cseréli, majd force-pusht végez. A régi clone-ok és forkok nem
> garantáltan törölhetők.

---

## 1. R2 — AI-avatar és AI-hang

**A szabály szövege** (`produkcios-szabalyok.json`): „Minden AI-avatar és AI-hang
assethez dokumentálandó: a használt generátor neve, a kereskedelmi/oktatási felhasználást
engedő licenc, és a voice-talent release.”

**Jelenlegi hatálya a manifesztben: 118 asset** — 29 vizuális asset és 89 hang-asset (88 narráció és az `M1.3-NAR-08` hangalámondásos képleírás) (lásd
a „Fontos következmény” bekezdést). A hatály 2026-08-27-én eldőlt (A opció,
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) lezárt döntések): a szigorúbb
olvasat marad érvényben, hacsak egy későbbi jogi review kifejezetten nem szűkíti.
**Ami nyitva maradt, az maga a bizonyíték** — az alábbi hat sor.

| Osztály | Assetek | Miért tartozik ide |
|---|---:|---|
| **AI beszélőfej-videó** | 18 | szintetikus emberi persona, aki a tananyag nevében beszél |
| **Hangalámondásos HOOK-videó (`explainer`)** | 3 | `M2.4-VID-01`, `M3.3-VID-01`, `M3.4-VID-01` — korábban beszélőfej; a `HUM-MEDIA-03` óta hangalámondás + tipográfia/grafika, a szintetikus hang miatt R2 alatt |
| **AI karakter-jelenet (teljes alakos)** | 5 | `M1.3-VID-01`, `M4.1-VID-02/03/04/05` — AI-generált emberi alak, szintetikus narrációval |
| **AI karakter-B-roll** | 1 | `M1.1-VID-02` — AI-generált kvuca-jelenetek emberi alakokkal; a saját jegyzete szerint AI karakter-anyag |
| **Karakter-freeze-frame** | 2 | `M4.1-FOTO-01/02` — a fenti videókból kivett állókép |
| **Szintetikus narráció** | 89 | a felmondás 2026-08-28 óta szintetikus (ElevenLabs) — az R2 „AI-hang” ága, lásd a „Fontos következmény” bekezdést |
| **Hétköznapi AI-illusztráció, ikon, diagram** | 0 | **NEM tartozik ide:** az R2 avatar- és hangjog, nem általános AI-tartalom kapu. Ezekre az R1 (AI-jelölés) vonatkozik. |

> **Projektgazdai döntés (2026-10-02, `HUM-MEDIA-03`):** gyermekvédelmi vagy
> krízis-HOOK-ban nem használunk készlet-AI-beszélőfejet. Az `M2.4-VID-01`, az
> `M3.3-VID-01` és az `M3.4-VID-01` ezért hangalámondás + tipográfia/grafika (`explainer`):
> a szintetikus hang miatt az R2 és az R3 rajtuk marad, és az R5 produkciós szabály is
> vonatkozik rájuk. Utólagos ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős, az érintett
> jogosultak és a Memuna.

### Szükséges bizonyítékok

A „Kutatás” oszlop azt mutatja, hogy a **jelöltek** feltételei ismertek-e. Ettől a
bizonyíték állapota **nem változik**: az R2 a *ténylegesen használt produkciós fiókra*
kér igazolást, nem egy nyilvános feltétel-oldal létezésére.

| # | Bizonyíték | Mire kell | Állapot | Kutatás |
|---|---|---|---|---|
| R2-1 | A képgeneráló eszköz / szolgáltató **neve és verziója** | mind a 29 vizuális asset | **HIÁNYZIK** | KUTATVA — jelöltek és verziók: 1/A.1., 1/A.2. |
| R2-2 | A szolgáltató **kereskedelmi-oktatási felhasználást engedő** licencfeltétele (a felhasznált verzióra érvényes szövegváltozat) | mind a 118 | **HIÁNYZIK** — a fiókhoz és a választott csomaghoz kötött szövegváltozat kell | KUTATVA — a jelöltek nyilvános záradékai idézve: 1/A.1., 1/A.2. |
| R2-3 | **Avatar- / képmás-jogosultság**: az avatar nem valós, azonosítható személy hasonmása, vagy van rá engedély | 27 videó + 2 állókép | **HIÁNYZIK** | KUTATVA — a jelöltek hozzájárulási feltételei idézve; a készlet-avatar képmás-licence dokumentálandó (H-3, `HUM-MEDIA-03`); a **J2 kiskorú-kérdés** nyitva: 1/A.3., 1/A.5. |
| R2-4 | A hanggeneráló eszköz **neve és verziója** | minden szintetikus hang | **RÉSZBEN MEGVAN** — a szolgáltató **ElevenLabs** (felhasználói döntés, 2026-08-28), a modell `eleven_v4` (projektgazdai döntés, 2026-10-03, VO D-02); a voice-ID nem nyilvános, a VO QA-repó gyártási konfigurációjában él (kiegészítő döntés, 2026-10-03, K3); jóváhagyói minősítés nincs | a szolgáltató és a modell-javaslat: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13. szakasz |
| R2-5 | **Hang-jogosultság**: a felhasznált egyedi hang használatának joga | a kanonikus narrátorhangra és a második hangra | **RÉSZBEN MEGVAN** — projektgazdai tényközlés (2026-10-03, VO D-01): mindkét hang létezik, a hanghasználati jog tisztázott, a hang tulajdonosai kifejezetten hozzájárultak; a két forrás-beszélő nagykorú (projektgazdai tényközlés, 2026-10-03, K5; a nyilvántartás „nagykorúság ellenőrizve” bejegyzésként rögzíti, K6; a bejegyzés és a jóváhagyói minősítés bizonyíték-kapu, VO D-08). A nem személyes hivatkozás (`VOICE-RIGHTS-REGISTER`) és a jogi jóváhagyó minősítése a repóban nincs: a formális bizonyíték függő | KUTATVA — a szolgáltató feltételei és a hangtípusonkénti következmény: 1/A.0. |
| R2-6 | Emberi felmondó esetén felhasználási szerződés | — | **NEM ALKALMAZHATÓ** — a felmondás 2026-08-28 óta szintetikus | — |

> **Fontos következmény.** A D2 válasza (2026-08-28): **szintetikus hang**. Ezért az R2
> „AI-hang” ága nemcsak a vizuális R2-assetekre, hanem **mind a 89 hang-assetre** is
> kiterjed: a manifesztben mind a 89 hang-asset `blockers` mezője viszi az R2-t, az R2-6
> (emberi felmondó) pedig nem alkalmazható. **Ez a döntés következménye, nem külön
> kérdés.**

---

## 1/A. Szolgáltató-kutatás (2026-08-27, kiegészítve 2026-08-28) — a bizonyíték-igény konkrétummá tétele

> **A 28 asset R2-blokkolója változatlanul a helyén marad.** *(Azóta: 118 asset — lásd
> az 1. szakaszt.)* A fenti hat sorból három
> továbbra is **HIÁNYZIK**; az R2-4 a szolgáltatói döntés után, az R2-5 2026-10-03 óta **RÉSZBEN MEGVAN**, az
> R2-6 pedig **NEM ALKALMAZHATÓ** lett (a felmondás szintetikus). **Egyik sem jelent
> feloldást:** a hiányzó részek — az R2-4 jóváhagyói minősítése, a licenc-igazolás és a hang-jogosultság formális bizonyítéka —
> mind nyitottak még. *(2026-10-03: a modell eldőlt, a hanghasználati jog tartalmilag tisztázott — R2-4, R2-5 RÉSZBEN MEGVAN; a voice-ID nem nyilvános, a helye a VO QA-repó gyártási konfigurációja (K3); a formális bizonyíték és a licenc-igazolás hiányzik.)* Ez a szakasz csak annyit tesz, hogy a „⟬generátor neve⟭” absztrakt
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

A szolgáltató **eldőlt** (felhasználói döntés, 2026-08-28). A hangok azóta elkészültek, és a
szerepük is eldőlt: az egyik a **kanonikus narrátorhang**, a másik a jogtisztázott **második hang** (projektgazdai
döntés, 2026-10-03, VO D-01, D-14). Az alábbi tábla fiókbizonyítékot igénylő mezői ettől nem
zárulnak le.

> ✅ **A hangok léteznek** (projektgazdai tényközlés, 2026-10-03, VO D-01). A repóban nincs
> ElevenLabs hitelesítő adat; a voice-ID-t és a hangtípust nem rögzítjük és nem találjuk ki — a
> tábla fiókbizonyítékot igénylő mezői ezért nyitottak. Az azonosítás menete:
> [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.4.

| Mező | VOICE-SRC-01 | VOICE-SRC-02 |
|---|---|---|
| Hang (voice-objektum) létezik? | `LÉTEZIK` — a két hang (a kanonikus narrátorhang és a második hang) létezik (VO D-01); hogy melyik melyik álnévhez tartozik, a repó nem rögzíti | `LÉTEZIK` — ugyanígy |
| `voice_id` | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| `voice_type` (`category`) | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Fióktulajdon / kontextus | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Létrehozás forrása (mire tanult) | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| Magyar nyelvre igazolt-e | `ACCOUNT_EVIDENCE_REQUIRED` | `ACCOUNT_EVIDENCE_REQUIRED` |
| **Hozzájárulás / felhasználási jog** | `CONSENT_EVIDENCE_REQUIRED` | `CONSENT_EVIDENCE_REQUIRED` |
| Kereskedelmi / oktatási használat | `EVIDENCE_FOUND` — fizetős csomag esetén | `EVIDENCE_FOUND` — fizetős csomag esetén |

**A név nem bizonyíték.** Az, hogy egy hangot „VOICE-SRC-01”-nek vagy „VOICE-SRC-02”-nek
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
| E-4 | Tanítás a bemeneten | a kimaradás bármikor bekapcsolható, de csak „once the request has been processed by our team” hat *(4(i), lekérdezve 2026-10-02)*, és „**does not affect any uses… prior to that date**” | `EVIDENCE_FOUND` — **a kimaradást ELŐRE kell bekapcsolni**, minden fiókban, ahová felvétel kerül; a feltöltés csak a kérés feldolgozása után jöhet |
| E-5 | Megőrzés | a hangról generált adatot „not… longer than 3 years after your last interaction” | `EVIDENCE_FOUND` |
| E-6 | Gépi provenance | hallhatatlan hangvízjel; **a beszéd-kimeneten nincs C2PA**; robusztussági leírás nincs; a lefedettséget nem nyilvánították befejezettnek | `EVIDENCE_INCOMPLETE` — az R1 gépi ága a hangon **nem értelmezhető** |
| E-7 | Közlési kötelezettség | a kifejezett előírás **AI-ügynökökre** szól, nem előre renderelt narrációra | `NOT_APPLICABLE` — az R1-címke **projektszabály**, és az is marad |
| E-8 | Kiskorúak | a feltételek szerint 18 alatti nem használhatja a szolgáltatást és kiskorú hangadata nem tölthető fel; a tiltólista viszont 13–18 közötti használatot szülői hozzájárulással elképzelhetőnek tart — **a saját dokumentumaik nem mondanak ugyanazt** | `LEGAL_REVIEW_REQUIRED` — lásd a V3 alkaput (1/A.5.) |
| E-9 | Licenc a feltöltött felvételekre | a feltöltött hangfelvétel a 4(b) szerint a 4(d) alá esik: a tartalomra — a hangra is — szóló licenc „to provide the Services…, to improve the Services, and to develop new services and products”, és „perpetual and irrevocable (which means this license cannot be withdrawn)”, „sub-licensable, through multiple tiers”; a hangot engedély nélkül önállóan nem kommercializálja („will not commercialize your voice on a standalone basis without your permission”). A 4(g) szerint csak az tölthet fel, akinek megvan „all the rights necessary to grant us the license described above”. *(EGT-s feltételek, lekérdezve 2026-10-02)* | **`LEGAL_REVIEW_REQUIRED`** — a H-5 mintájára. A kimaradás (E-4) a tanítási felhasználásra szól; hogy a licenc többi célját érinti-e, és mit kell ehhez a V2 hozzájárulásnak lefednie, jogi kérdés. A projektgazdai döntés (2026-10-02, `HUM-MEDIA-02`) szerint ez az állapot a jogi felülvizsgálatig marad, hallgatólagosan nem tekinthető elfogadottnak |

### 1/A.1. Beszélőfej-videó (18 asset) — a szolgáltató **HeyGen** (felhasználói döntés, 2026-08-28)

A szolgáltató-választás lezárult; ez a szakasz már nem hasonlít össze jelölteket, hanem a
**választott** szolgáltató feltételeit rögzíti. A korábban vizsgált, **nem választott**
alternatívák (Synthesia, BytePlus OmniHuman) csak nyomon követhetőségért maradnak
megemlítve — a jelenlegi gyártási útvonalnak nem részei.

Minden idézet a szolgáltató saját feltételeiből, lekérdezve 2026-08-28.

| # | Feltétel | Bizonyíték | Állapot |
|---|---|---|---|
| H-1 | **Kereskedelmi használat és kimenet-tulajdon** | „As between HeyGen and you, **you own all rights in your User Input or User Output**, and does not restrict your ability to use User Output for your own purposes (**including for commercial purposes**)… we hereby **assign to you all right, title and interest**” | `EVIDENCE_FOUND` |
| H-2 | **Az ingyenes csomag kizárt** | az ingyenes szinten a kimenet „solely for personal, non-commercial, and internal evaluation purposes”, és „may not be sold, sublicensed, redistributed, monetized, or used in connection with commercial activities” | `EVIDENCE_FOUND` — **fizetős csomag kötelező** |
| H-3 | **Avatar-hozzájárulás** | „Consent applies only to **digital twin** avatars. Photo avatars… and prompt-to-avatar characters… depict no real, identifiable person and do **not** require consent.” A tervezett útvonal **nyilvános készlet-avatart** használ — erre az idézet **nem terjed ki**, mert csak a digital twin, a fotó- és a prompt-avatar szerepel benne. A készlet-avatar képmás-licencét a szolgáltató feltételei szerint dokumentálni kell (`HUM-MEDIA-03`) | `EVIDENCE_INCOMPLETE` — a digital twin, fotó- és prompt-avatarra idézve; a készlet-avatar képmás-licence nincs dokumentálva → R2-3 |
| H-4 | **Feltöltött tartalom szavatossága** | „you represent and warrant that you have, or have obtained, **all rights, licenses, consents, permissions, power and/or authority** necessary to grant the rights granted herein for Your Content.” — ez a **feltöltött hangmesterre is vonatkozik** | `CONSENT_EVIDENCE_REQUIRED` — lásd H-5 |
| H-5 | **A feltöltött tartalomra adott licenc** | a feltöltött tartalomra a szolgáltató „a license to… modify Your Content to operate, improve, promote and provide the Services and to develop new services and products, **including to train or otherwise improve or modify our artificial intelligence and machine learning models**”-t kap, amely „royalty-free, transferable, sublicensable, worldwide and **irrevocable**”, és a szerződés megszűnését is túléli | **`LEGAL_REVIEW_REQUIRED`** — lásd a J3 kaput |
| H-6 | **AI-közlési kötelezettség** | „if you distribute your User Output to others, to the extent required by applicable law, you must **proactively disclose that such User Output was created using artificial intelligence technologies**” | `EVIDENCE_FOUND` — a tananyag R1-címkéje ezt kiszolgálja |
| H-7 | **Kiskorú megjelenésű avatar tilalma** | tiltott az olyan avatar, amely „Represent or appear in the sole discretion of HeyGen to represent **individuals under the age of 18**” | `EVIDENCE_FOUND` — lásd a J2 kaput |
| H-8 | **Gépi provenance (C2PA)** | a szolgáltató etikai lapja szó szerint a **Content Authenticity Initiative** tagságát mondja ki („We are a member of the Content Authenticity Initiative”) — **a C2PA nevet nem használja**, és sem ez a lap, sem a fejlesztői dokumentáció, sem az OpenAPI-leírás, sem a feltételek **nem állítják**, hogy Content Credentials kerülne magába a kimeneti fájlba. *(A CAI és a C2PA rokon, de nem ugyanaz.)* | `ACCOUNT_EVIDENCE_REQUIRED` — egyetlen próbarendereléssel eldönthető |
| H-8/b | **Vízjel az API-kimeneten** | a **fogyasztói** előfizetési oldal kifejezetten felsorolja a „vízjel-eltávolítást” a fizetős szinteken; az **API-útvonalra** viszont a per-másodperc árlap, a korlát-leírás és a feltételek egyaránt **hallgatnak** — sem azt nem mondják, hogy vízjelezett, sem azt, hogy nem | `ACCOUNT_EVIDENCE_REQUIRED` — a hiányból következtetni nem elég |
| H-9 | **A hangmester sértetlensége** | a dokumentáció **nem nyilatkozik** arról, hogy a feltöltött hang újrakódolás nélkül kerül-e a kimeneti MP4-be | `ACCOUNT_EVIDENCE_REQUIRED` — a pilot méri |
| H-10 | **Moderáció** | a nem engedélyezett tartalmak közt szerepel a „**Political**: Content that displays political opinions…”, és a szolgáltató automatikus moderációt futtat; érzékeny („conditional”) oktatási tartalom pedig „can be created using **custom avatars only**” | `ACCOUNT_EVIDENCE_REQUIRED` — csak beküldéssel deríthető ki, hogy ez a tananyag átmegy-e. A gyermekvédelmi és krízis-HOOK-ok a projektgazdai döntés szerint nem készülnek beszélőfejjel (`HUM-MEDIA-03`; lásd az 1. szakaszt) |
| H-11 | **Kártalanítás iránya** | a szolgáltató feltételei **nem** vállalnak kártalanítást a megrendelő felé a készlet-avatar képmás- vagy személyiségi jogi igényeire; a szavatosság a **feltöltő** oldalán áll („you represent and warrant that you have… all rights, licenses, consents…”). Egy korábban vizsgált, **nem választott** alternatíva ezen a ponton kedvezőbb volt — ez a különbség a szolgáltatóváltással **eltűnt**, és tudni kell róla | `LEGAL_REVIEW_REQUIRED` |

> **A H-5 a legfontosabb új tétel.** A gyártási lánc szerint a **klónozott egyedi hang
> hangmesterét** töltjük fel a szolgáltatóhoz. A fenti záradék szerint ezzel a
> szolgáltató visszavonhatatlan, továbbadható licencet kap arra, hogy ezen a hangon
> **modelljeit tanítsa**. Ha a hang valós személy hangjának klónja, ez **nemcsak a
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
watermark”. Ez is a Google generatív szolgáltatása, ezért a **J1** kérdése (1/A.3.) erre a
lépésre is kiterjed — `LEGAL_REVIEW_REQUIRED`; hogy melyik feltételszöveg és záradék
alkalmazandó rá, a jogi jóváhagyó dönti el.

### 1/A.3. Három kérdés, amit ez a lap NEM dönt el — emberi kapu

| # | Kérdés | Bizonyíték | Kihez tartozik |
|---|---|---|---|
| **J1** | A Google Cloud Service Specific Terms §20(d) szerint az ügyfél nem használhat generatív AI-szolgáltatást olyan online szolgáltatás részeként, amely „directed towards or is likely to be accessed by individuals under the age of 18”. A tananyag célközönsége **15+**, és a madrih maga is lehet kiskorú. Hogy az **offline legyártott, majd Moodle-ben kiszolgált** asset ebbe a mondatba esik-e, jogi olvasat. A kérdés a karakter-jelenet **videómodelljét** (Veo) és a karakter-lock **képgenerátorát** (`gemini-3-pro-image`) egyaránt érinti: mindkettő a Google generatív szolgáltatása. | idézve fent | **jogi jóváhagyó** — ez a javasolt karakter-jelenet stacket — a videót és a képi lépést is — kizárhatja. A `HUM-MEDIA-02` alkapuja; felelős és bizonyíték: 1/A.5. |
| **J2** | A **választott beszélőfej-szolgáltató** moderációs politikája tiltja az olyan avatart, amely „Represent or appear in the sole discretion of HeyGen to represent **individuals under the age of 18**”; a karakter-jelenet szolgáltatója pedig EU-ban felnőttre korlátozott személy-generálást enged. Ebből az következik, hogy **a beszélőfej és a karakter felnőttnek kell hogy látsszon** — miközben a tananyag szerint a madrih maga is lehet kiskorú, és a jelenetek „madrihot” ábrázolnak. | idézve a H-7 sorban | **Memuna (gyermekvédelmi felelős) + szerzői döntés** — ez tananyagi és gyermekvédelmi kérdés, nem eszközválasztás. A kánoni hely: a `HUM-MEDIA-02` alkapuja (`Emberi jóváhagyás szükséges.md`); felelős és bizonyíték: 1/A.5. |
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

### 1/A.5. A `HUM-MEDIA-02` alkapui — felelős és bizonyíték (J1, J2, V1, V3)

> **Projektgazdai döntés (2026-10-02).** A J1, a J2, a V1 és a V3 a kánoni `HUM-MEDIA-02`
> alkapuja (`Emberi jóváhagyás szükséges.md` 5. szakasz); a felelős és a bizonyíték
> kanonikus mezője ez a tábla. A felelős szerepnév, nem személynév. Egyik alkapu sem
> tekinthető hallgatólagosan lezártnak: az állapot csak a 4. szakasz szerint, nem személyes
> hivatkozással állítható **MEGVAN**-ra. A projektgazdai döntés szerint a jogi és a
> gyermekvédelmi médiakapu blokkolja az általa érintett tanulói asset release-ét. Utólagos
> ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős és a hang tulajdonosai.

| Alkapu | Kérdés | Felelős (szerep) | Bizonyíték | Állapot | Mit érint |
|---|---|---|---|---|---|
| **J1** | a Google generatív szolgáltatásainak 18 év alatti záradéka (1/A.3.) | jogi jóváhagyó | dokumentált jogi állásfoglalás a záradék alkalmazhatóságáról | **HIÁNYZIK** | a karakter-jelenet stack: a videó és a karakter-lock képi lépése |
| **J2** | felnőtt megjelenésű avatar és karakter, miközben a madrih maga is lehet kiskorú (1/A.3.) | Memuna (gyermekvédelmi felelős) + szerző | a Memuna és a szerző dokumentált döntése az ábrázolás módjáról | **HIÁNYZIK** | a beszélőfej- és a karakter-brief |
| **V1** | kell-e kiskorú tanulóknál külön szülői/gondviselői tájékoztatás a szintetikus narrációról ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.10.) | Memuna (gyermekvédelmi felelős) + DPO | a Memuna és a DPO dokumentált döntése | **HIÁNYZIK** | a hang-stack élesítése |
| **V3** | a hang-szolgáltató saját dokumentumai nem mondanak ugyanazt a 18 év alattiakról: kezelhet-e kiskorú fiókot (E-8; [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.10.) | Memuna (gyermekvédelmi felelős); az E-8 jogi kérdésében a jogi jóváhagyó | a Memuna dokumentált döntése **és** az E-8 jogi felülvizsgálata (`LEGAL_REVIEW_REQUIRED`) — ez külön lezárási feltétel: a V3 a jogi felülvizsgálat nélkül nem állítható **MEGVAN**-ra | **HIÁNYZIK** | a fiókhasználat |

### Amit ez a lap NEM állít

- Nem mondja ki, hogy bármelyik szolgáltató „kereskedelmileg biztonságos”.
- Nem minősít licencszöveget.
- Nem dönti el az EU AI Act szerinti szerepbesorolást. Az R1 szövege erről már rögzíti,
  hogy az 50. cikk (2) gépi jelölési kötelezettsége a szintetikus tartalmat előállító
  rendszer **szolgáltatóját** terheli, nem az oktatási médiát készítő szervezetet, és hogy
  az 50. cikk (4) deployer-oldali eseteinek alkalmazhatóságát **jogi review** minősítse.
  Ez a lap ezt átveszi, nem értelmezi tovább. *(2026-10-02: a projektgazda rögzítette, hogy
  a kurzus a külső AI-rendszerek használatában alkalmazóként (deployer) jár el —
  `HUM-PRIV-04`, `Adatvédelem – tanulói adatok és AI.md`; hogy ebből az 50. cikk (4) mely
  esetei érintik a médiaasseteket, továbbra is a jogi review kérdése.)*
- Nem állítja, hogy jogi, DPO- vagy Memuna-jóváhagyás született. *(2026-10-03, VO D-08: a
  konzervatív átláthatósági kezelést — a csak hangot tartalmazó narrációnál a leirat első sora és
  a lecke alján egy sor a kanonikus AI-címkével, VO D-21 — a projektgazda jóváhagyta; az 50. cikk
  (4) alkalmazhatóságának jogi minősítése és a V1 (Memuna + DPO) formális bizonyítéka függő.)*

---

## 2. R8 — GDPR és képmás valós felvételen

**A szabály szövege:** „Valós fotó/screenshot esetén minden azonosítható
személyt/kézírást anonimizálni vagy kikeretezni kell; felismerhető kiskorúnál
a résztvevő és a gondviselő együttes, dokumentált hozzájárulása ELŐRE kötelező
(projektgazdai döntés, 2026-10-02). Screenshotnál nincs valós felhasználónév/arc
és nincs licenc-korlátos 3rd-party elem.”

**Jelenlegi hatálya: 2 asset.** Mindkettő valós felvétel; a tananyagban több nincs.

| Asset | Mi ez | Miért R8 | Osztály |
|---|---|---|---|
| `M0.3-FOTO-01` | Moodle kurzus-főoldal képernyőkép | valós képernyőkép: felhasználónév, arc, harmadik felas elem kerülhet rá | **ADATVÉDELMI ÁTALAKÍTÁS KELL** |
| `M0.A-FOTO-01` | a képző által készített fotók a kitöltött kvuca-plakátokról | valós felvétel **kézírásról**, kiskorúak által írt tartalommal | **ADATVÉDELMI ÁTALAKÍTÁS ÉS HOZZÁJÁRULÁS KELL** (a policy projektgazdai döntés: `HUM-PRIV-02`, 2026-10-02) — egyben élő/runtime tétel: a képző a peula után készíti, nem központi előgyártás |

### Szükséges bizonyítékok és teendők

| # | Tétel | Mit kell tenni / igazolni | Állapot |
|---|---|---|---|
| R8-1 | `M0.3-FOTO-01` | a képernyőkép **teszt-fiókkal** készüljön: nincs valós felhasználónév, nincs arc, nincs licenc-korlátos harmadik felas elem | **HIÁNYZIK** (a felület sem áll még — R7) |
| R8-2 | `M0.A-FOTO-01` | a plakátfotó **kézírást** rögzít: előbb a nevek és azonosítók eltávolítása; a fotó jogalapja külön, önkéntes hozzájárulás, amelyet 18 év alatt a résztvevő és a gondviselő együtt ad, 18 év felett a résztvevő (`HUM-PRIV-02`, lásd lent) | **HIÁNYZIK** — a szabály eldőlt, a hozzájárulás bizonyítéka még nincs; az R8 státusza: D8 |
| R8-3 | `M0.A-FOTO-01` | ha felismerhető kiskorú kerülhet a képre: **előzetes, dokumentált hozzájárulás, amelyet a résztvevő és a gondviselő együtt ad** (a projektgazdai döntés szerint a háttérben nem lehet gyerek) | **HIÁNYZIK** → `HUM-PRIV-02`, D8; a nyilatkozatok NEM ebben a repositoryban élnek |
| R8-4 | `M0.A-FOTO-01` | megőrzési idő és hozzáférési kör az archívumra (a fotó a Z.A peuláig áll) | **RÉSZBEN MEGVAN** — a megőrzés projektgazdai döntés: a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás; a hozzáférés a legszűkebb szükséges kör (`Adatvédelem – tanulói adatok és AI.md` 3. szakasz). A 2026-10-02-i központi naptár szerint az M0.A és a Z.A között 119 nap telt volna el; a naptári dátumokat a 2026-10-05-i pilot-ütemezés felülírta (`SCHEDULE_TO_RESYNC`). A szabály változatlan: ha az M0.A és a Z.A között 90 napnál több telik el, a fotó a Z.A-ig csak külön archiválási hozzájárulással őrizhető meg — ennek bizonyítéka hiányzik |

> **Projektgazdai döntés (2026-10-02, `HUM-PRIV-02`):** alapértelmezésben nincs fotó,
> videó vagy hangfelvétel, csak indokolt célból; minden médiaaktivitásnál rögzíteni kell a
> célt, a jogalapot, a hozzáférést, a megőrzést és a törlést. A kézírásos plakátot
> lehetőleg fizikailag őrizzük meg. Ha fotó kell: előbb a nevek és azonosítók eltávolítása,
> a háttérben ne legyen gyerek, feltöltés ellenőrzött tárhelyre, majd törlés a saját
> eszközről. **Jogalap és megőrzés** (szintén projektgazdai döntés): fotó, videó és hang
> csak külön, önkéntes hozzájárulással, a cél teljesüléséig, legfeljebb 90 napig, hacsak
> nincs külön archiválási hozzájárulás (`Adatvédelem – tanulói adatok és AI.md` 3.
> szakasz). **A hozzájárulás adója** (projektgazdai döntés, 2026-10-02; utólagos
> ellenőrzés (vétó/QA): a DPO): 18 év alatt a résztvevő és a gondviselő együtt, 18 év
> felett a résztvevő (`Adatvédelem – tanulói adatok és AI.md` 4. szakasz); a fenti
> szabályszöveg ezt már így írja. Az R8-2 és az R8-3 bizonyítéka (a hozzájárulások) ettől még
> hiányzik; az R8-4 szabálya eldőlt. Utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős.

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
FOTO→ILL”). Ennek eredménye, hogy a 415 assetből ma **kettő** épül valós felvételre.
Ez a lap ezt a döntést rögzíti, nem bírálja felül — és nem is használható arra, hogy egy
**kötelezően valós** felvételt (a Moodle-képernyőképet) illusztrációra cseréljünk.

---

## 3. R1 — AI-provenance (nem kapu, de nyilvántartandó)

Az R1 **kötelező projektszabály**, nem nyitott kapu: minden `provenance=ai` asseten
egyetlen kanonikus, ember-olvasható AI-címke kell. Ez 278 assetet érint.

| # | Tétel | Állapot |
|---|---|---|
| R1-1 | A címke **egységes szövege** | **MEGVAN** — 2026-08-27-én jóváhagyva, szó szerint: **AI-generált médiaelem · emberi lektorálással.** Rögzítve a `produkcios-szabalyok.json` R1 szabályában (`human_label` mező), és kivezetve a tananyag mind a 21 aktív előfordulására; a korábbi négy változat megszűnt. Regressziós teszt őrzi (`TestApprovedDecisions`). |
| R1-2 | A címke vizuális formája és elhelyezése | **MEGVAN** — projektgazdai döntés (2026-10-02, D1 / `HUM-MEDIA-01`): élő LMS-szöveg, nem képbe égetve; a megjelenés és az elhelyezés a [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 7.3. pontja szerint (B változat; [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) 4. szakasz). Csak hangot tartalmazó narrációnál a narráció leiratának első sora és a lecke alján egy sor (projektgazdai döntés, 2026-10-03, VO D-21). |
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

> Az R2 lezárása önmagában nem zárja le az 1/A.5. alkapuit (J1, J2, V1, V3): ezek a saját
> felelősükkel és bizonyítékukkal zárulnak, és a projektgazdai döntés szerint addig az általuk
> érintett tanulói asset release-ét blokkolják (`Emberi jóváhagyás szükséges.md` 5. szakasz).
