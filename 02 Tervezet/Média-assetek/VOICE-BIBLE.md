# 🎙️ Narrátor hang-bible

Az R3 produkciós szabály végrehajtási lapja: minden, ami a **jelenlegi tananyagból
objektíven levezethető** a felmondásról. Ami nyitva maradt, azt a lap kimondja, és a
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D2 pontjára mutat — ott van
egyetlen helyen az összes megválaszolandó érték.

**Hatókör:** 90 narráció-asset, 21 beszélőfej-videó, 6 karakter- és jelenetvideó — összesen
117 tétel, mind szó szerinti forrásblokkal. Nincs többé szkript nélküli beszélt asset.

> **Ez a lap nem választ szolgáltatót.** A motor, a voice-ID és a felmondó személye
> szervezeti és jogi döntés (D2, D3). A többi mező viszont **most is érvényes**, és a
> pilot-felvétel elkészíthető belőle, amint a hang eldőlt.

---

## 1. Nyelv

Magyar, minden tételnél. A narrációk technikai jegyzeteinek túlnyomó része kiírja a
„magyar” kikötést, a többinél a forrásszöveg maga magyar. Nincs idegen nyelvű narráció a
tananyagban.

Idegen szó a szövegben csak héber/someres szakszóként és néhány pedagógiai
terminusként fordul elő (lásd 6. szakasz) — ezeket **magyar hangzással**, magyar
toldalékolással kell mondani, nem angolosan.

## 2. Regiszter

**Tegező, barátságos, egyenrangú.** Az R3 szövege ezt kötelezővé teszi, és a korpusz
egyöntetűen ezt követi: a narráció-forrásokban **egyetlen** magázó alak („Ön”) sincs,
és a többségükben kifejezett egyes szám második személyű megszólítás áll („neked”,
„nézd meg”, „képzeld el”, „mennyire éreznéd”).

A hallgató **madrich, jellemzően 15+**, aki maga is kiskorú lehet. Ebből következik:

- **nem gyerekhang és nem gyereknek szóló hangsúlyozás** — a hallgató vezetői szerepre
  készül;
- **nem tanári számonkérés** — a szövegek kérdeznek, nem kioktatnak;
- **nem hivatalos-bürokratikus** — a leckék hétköznapi mondatokat használnak
  („Mi van?! Csak próbáltam feldobni a hangulatot…”), ezeket természetesen kell mondani.

## 3. Hangulat és érzelmi sáv

A tananyag három tipikus narráció-helyzete:

| Helyzet | Példa | Hangvétel |
|---|---|---|
| **HOOK / bevonás** | „Mondtak már rólad mást?”, „Volt már olyan, hogy nem ült a játék?” | közvetlen, kicsit játékos, kérdező; nem drámai |
| **INPUT / magyarázat** | modell- és fogalommagyarázatok | nyugodt, tagolt, magyarázó; a kulcsszó kap hangsúlyt |
| **Érzékeny tartalom** | M3 gyermekvédelem, red flag, titoktartás | **visszafogott, tényszerű, nem ijesztő** — a peula saját instrukciója szerint „nem azért csináljuk, hogy bárkit ijesztgessünk” |

Az érzelmi sáv **szűk**: nincs kiabálás, nincs reklámhang, nincs túljátszott lelkesedés.
Az M6.2 lecke „fagyott csend” és az M3 „késő esti üzenet” jeleneteinél a szöveg
önmagában hordozza a feszültséget — a felmondás ne tegyen rá.

## 4. Tempó

A korpusz méri magát: 114 olyan tétel van, amelynél a lecke megadja a hosszt **és** a szó
szerinti szöveget is.

| | szó/perc |
|---|---:|
| medián | **103** |
| átlag | 108 |
| alsó kvartilis | 87 |
| felső kvartilis | 127 |

**Céltempó: 100–120 szó/perc**, azaz a magyar hírolvasó-tempónál lassabb, beszélgetős
ritmus. Ez nem véletlen: a szövegek soronként tördeltek a leckében, és a sortörések
lélegzetvételi helyek.

Ahol a mért érték kilóg (leggyorsabb: `M7.1-NAR-02` ≈ 271 szó/perc, `M2.4-NAR-04`
≈ 214 szó/perc), ott **a lecke időkerete a szűk, nem a szöveg hosszú** — ilyenkor a
felvételnél a hosszt kell tágítani, nem a szöveget hadarni. Ellenkező irányban
(`M3.2-NAR-04` ≈ 43 szó/perc) bőven van hely a szüneteknek.

## 5. Szünet és hangsúly

- **Sortörés a forrásban = rövid levegő.** A szkriptek szándékosan soronként tördeltek.
- **Üres sor = bekezdés-szünet** (0,6–1 mp).
- **`**félkövér**` a forrásban = hangsúlyos szó.** A leckék ezzel jelölik a fogalmi
  kulcsszót (`**neked beszél**`, `**végignéz**`, `**más pillanatok**`). A hangsúly
  a kiemelt szón van, nem az egész mondaton.
- A kérdőmondatok **valódi kérdésként** szólnak — a legtöbb HOOK kérdéssel indít.
- Az emoji a forrásszövegben (pl. 😅) **hangulatjelölő, nem felmondandó**.

## 6. Kiejtés — someres és héber szavak

A tananyag írásmódja **magyar-fonetikus és szándékos**; a
`Glosszárium – someres és pedagógiai fogalmak.md` ezt kánoni referenciaként rögzíti.
Ebből következik a felmondás is: **a leírt alakot magyarul kell olvasni.**

| Írott alak | Kiejtés | Forrás / megjegyzés |
|---|---|---|
| `kvuca` | „kvuca” — a **c** = /ts/ | a glosszárium kifejezetten kimondja: „a magyar »c« = /ts/ adja vissza a héber צ hangot”; **nem** „kvutza”, **nem** „kvuka” |
| `Somer`, `someres` | „somer” — az **s** = /ʃ/ | tulajdonnév, nagybetűs; **nem** „shomer” |
| `Hasomer Hacair` | „hasomer hacair” | magyar-fonetikus; **nem** „Hashomer Hatzair” |
| `peula`, `peulák` | „peula” | köznév, kisbetű |
| `madrich`, `madrichok`, `madrichot` | a szóvégi **ch** torokhang, nem /cs/ és nem /k/ | a hibrid „madrichák” alak a tananyagban tiltott |
| `chanich`, `chanichok` | a **ch** ugyanaz a torokhang, szó elején is | egy helyen (M0.2) szándékosan héber többes: „chanichim” |
| `dugma ishit` | „dugma isit” | köznév, kisbetű; a „Dugma Ishit” személynévi alak kerülendő |
| `ken` | „ken” | rövid e, nem „kén” |
| `Zmán Kvucá` | „zmán kvucá” — mindkét ékezet hosszú | a `c` itt is /ts/ |
| `Parparim` | „parparim” | pillangók, 6–10 |
| `Kivsza` | „kivsza” | bárány, 11–13 |
| `Leviatan` | „leviatan” — **ékezet nélkül** | a glosszárium kifejezetten tiltja a „Leviatán” alakot; toldalékoltan a tő miatt lehet ékezet |
| `Zorea` | „zorea” | magvető, 16+; toldalékolva „Zoreánál” |
| `hagshama`, `bogrim`, `mazkirut` | magyar olvasat | ritkábban fordulnak elő |

> ⚠️ **Nyitott terminológiai kapu.** A glosszárium 2026-08-25-i figyelmeztetése szerint a
> `madrich` / `chanich` alakok mellett a mozgalom nyilvános felületein `madrih` és
> `hánih` szerepel; a house style-t a helyi ken-/országos felelősnek kell jóváhagynia.
> **A hangfelvételt ez érinti**, mert a szóvégi hang eltér. Amíg nincs döntés, a
> felvétel a glosszárium jelenlegi kánoni alakját követi — de a pilot-hangmintát ezekkel
> a szavakkal kell jóváhagyatni, hogy egy későbbi terminológiai migráció ne 91 fájlt
> mondasson újra.

## 7. Számok, betűszók, rövidítések

- **Korosztályok:** a szövegek `6–10`, `11–13`, `14–16`, `16+` alakban írják; felmondva
  „hat–tíz éves”, „tizenegy–tizenhárom éves”, „tizenhat plusz” helyett „tizenhat év
  felett”.
- **SBI:** betűzve, „es-bé-í”, és a modell elemei magyarul: Situation–Behavior–Impact →
  a leckék „S”, „B”, „I” betűjelet használnak, ezeket betűként kell mondani.
- **Johari, Tuckman:** magyaros olvasat („johari”, „takmen” helyett „tuckman” magyar
  betűzéssel) — ezek szerzőnevek, a leckék nem adnak kiejtési előírást, ezért a
  pilot-felvételnél kell rögzíteni, és utána következetesen tartani.
- **Időtartamok:** `45’` = „negyvenöt perc”, `45 mp` = „negyvenöt másodperc”.
- **Segélyvonalak** (112, 116-111, 116-123) narrációban **nem** hangzanak el — képzői
  kártyán szerepelnek (`M3.B-KART-02`). Ha valaha narrációba kerülnek, számjegyenként
  kell mondani őket.

## 8. Karakter- és dialógushangok

A tananyagban **két** dialógusos jelenet van, és ezek nem a narrátor hangjai:

- `M1.3-VID-01` — két madrich (A és B) beszélget, ugyanaz a helyzet kétféle
  visszajelzéssel. **Két megkülönböztethető hang kell**, hogy a felirat nélkül is
  követhető legyen, ki beszél. A szkriptet a szerző 2026-08-27-én jóváhagyta; a szó
  szerinti dialóg a leckében, `M1.3-VID-01-VO` forrásblokkban él.
- `M4.1-VID-03/04/05` — a karakter **nem beszél**, a narrátor beszél róla harmadik
  személyben („Nézd meg ezt a madrichot…”). Egyetlen kivétel a 3. jelenet, ahol a
  karakter egy mondatot mond: „Sziasztok, ma arról fogunk beszélni, hogy…”. Ez a mondat
  a jelenetben hangzik el, nem a narrátor sávján.

Minden más narráció **egyetlen, azonos narrátorhang** — ezt az R3 első mondata írja elő
(„EGYETLEN konzisztens narrátor-hang az egész tananyagban, tegező + barátságos
regiszterben — a Z-záró és az M4 modulokat is beleértve”).

## 9. Kapcsolat a felirattal és a leirattal

Ez nem stílus, hanem akadálymentesítési követelmény
(`LMS – hozzáférhetőségi sztenderd.md`):

- **Szinkronizált videó → felirat kötelező** (WCAG 2.2 SC 1.2.2), és a teljes leirat
  **nem helyettesíti**.
- **Csak hang → teljes szöveges átirat elegendő** (SC 1.2.1).
- **A felirat szó szerint fedje le az elhangzottakat.** Ezért a felmondás **nem
  improvizál**: amit a `@source` blokk tartalmaz, azt kell mondani. Ha a szöveg
  változik, a leckében kell változnia — a felirat és a leirat onnan generálódik.
- Az Interactive Videónál (`M1.3-VID-01`, `M4.1-VID-02`) **egy** felirat-sáv és **egy**
  leirat tartozik a teljes videóhoz; az `M4.1-VID-02` szövege a három jelenet
  narrációjának sorrendi összefűzése.

**Gyakorlati következmény a felvételre:** minden narrációról tudni kell, melyik
`@source` blokkból készült, és a felvétel eltérése a szövegtől **hiba**, nem szabadság.

## 10. Kimenet és mastering

A leckék technikai jegyzeteiből:

- **Formátum:** MP3 vagy WAV (a jegyzetek 19 helyen kiírják; néhány helyen MP3/AAC a
  H5P Course Presentation audio miatt).
- **Tartalom:** „tiszta beszéd, háttérzaj nélkül” — a leckék kifejezetten így fogalmaznak.
- **Hossz:** tételenként a lecke adja meg (10–15 mp-től 45–60 mp-ig); a leggyakoribb
  a 20–40 mp.
- **Egy asset = egy fájl.** A narráció-assetek nem darabolódnak tovább.

Nyitott, mert a repository nem rögzíti: mintavételi frekvencia, bitmélység, csatorna
(mono/sztereó), hangerő-normalizálás célértéke. Ezek a pilot-felvétel jóváhagyásakor
rögzítendők — nem szolgáltatófüggőek, de nincs rájuk jelenlegi forrás, ezért nem
találjuk ki őket. Javaslat a pilothoz: mono, beszédre normalizálva, azonos csúcsértékkel
minden fájlban.

## 11. Konzisztencia-szabályok

1. **Egy hang mindenre** (a 8. szakasz két dialógusos kivételével).
2. **A pilot dönt.** A `M4.2-NAR-03` a kijelölt narráció-pilot
   (`MEDIA-PRODUCTION-PLAN.md` 5. szakasz): a tempót,
   a hangszínt, a szünetkezelést és a someres szavak kiejtését ezen kell jóváhagyni,
   és a többi 90 tétel ehhez igazodik.
3. **A kiejtési táblát (6. szakasz) minden felvételnél újra kell futtatni** — ez a
   leggyakoribb elcsúszási pont egy több hónapos gyártásban.
4. **Nincs verziószám a hangban.** Ha a lecke szövege változik, a fájl újra készül; a
   manifeszt `source_hash` mezője mutatja, melyik szövegverzióhoz készült.

## 12. Motor és hang — NYITOTT (D2), de már kutatott

| Mező | Állapot |
|---|---|
| Szintetikus vagy emberi felmondó | **nyitott** → D2 |
| Motor / szolgáltató neve | **nyitott** → D2 (a jelöltek kutatva, lásd 13.) |
| Voice-ID vagy felmondó személye | **nyitott** → D2 |
| Kereskedelmi-oktatási felhasználás igazolása | **nyitott** → D3, [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |
| Hang-jogosultság (voice-talent release / klónozási engedély) | **nyitott** → D3 |

**Ez a hang-bible egyetlen valódi hiányzó döntése.** Minden más mező fent ki van töltve
a jelenlegi tananyagból. Amint a D2 megszületik, a narráció-köteg
(90 asset / 267 deliverable) indulhat — a pilot jóváhagyása után. A beszélőfej- és
karaktervideók ezen felül az R2-re (és részben az R5-re) is várnak.

---

## 13. Szolgáltató-kutatás (2026-08-27) — bizonyíték, nem választás

> **Ez a szakasz nem választ szolgáltatót.** Elsődleges, szolgáltatói forrásokból
> összegyűjtött bizonyíték, hogy a D2 döntés ne feltételezésen alapuljon. Fizetős API-t
> nem hívtunk, fiókot nem hoztunk létre, hangot nem klónoztunk, próbaidőszakot nem
> indítottunk. **Az R3 blokkoló mind a 117 tételen a helyén marad.**

### 13.1. A tananyag szemszögéből egyetlen kérdés dönt: a kiejtés

A 6. szakasz kiejtési táblája **produkciós követelmény**, nem stílus. Ezért a jelölteket
elsősorban az különbözteti meg, hogy a magyar loanword-kiejtés **kikényszeríthető-e**,
vagy csak remélhető.

| Motor | Magyar támogatás (a szolgáltató saját megnevezésével) | Kiejtés-vezérlés | Verzió-rögzítés |
|---|---|---|---|
| **Azure AI Speech** | `hu-HU` locale, „Standard” típus: **2 GA hang** + 8 nyilvános előzetes (`MAI-Voice-2`) | SSML `<phoneme alphabet="ipa">` **és** egyedi kiejtési szótár (PLS) — a hu-HU-n egyik sincs letiltva | **12 hónapos leállítási értesítés** GA hangokra (előzetesre nem) — lásd a 13.2. idézetét |
| **Google Cloud TTS** | 30 db `hu-HU-Chirp3-HD-*` („Premium”) + `hu-HU-Standard-B`, `hu-HU-Wavenet-B` | `custom_pronunciations` (IPA / X-SAMPA); a Chirp3-HD SSML **előzetes**, „as is” | nincs dokumentált dátumozott rögzítés |
| **ElevenLabs** | `eleven_v3` és `eleven_flash_v2_5`; **nem** az `eleven_multilingual_v2`, és **nem** a speech-to-speech modell | kiejtési szótár; fonéma-címke csak `eleven_flash_v2` + `eleven_v3` alatt; **nem angol IPA-hoz v3 kell** | nincs; a seed „best effort”, **„Determinism is not guaranteed.”** |
| **Cartesia** | magyar listázva, `sonic-3.6` | nem ellenőrzött | dátumozott pillanatkép-verziók vannak |
| **Emberi felmondó** | anyanyelvi | teljes | szerződéses |

**Magyar nyelvet nem támogat** (ellenőrizve): Amazon Polly, Murf, Rime, Deepgram Aura,
Hume. A Speechify „hamarosan”-t jelöl. Az OpenAI TTS-nek **nincs SSML/fonéma/IPA
vezérlése** — a 6. szakasz követelménye miatt ez kizáró ok.

### 13.2. Amiért az Azure kiemelkedik — és amiért ez nem elég a döntéshez

Az Azure **dokumentál magyar IPA fonéma-készletet**, és abban benne van mind a három
hang, amit a tananyag someres szókincse igényel:

| IPA | A szolgáltató saját magyar példája | Mit old meg nálunk |
|---|---|---|
| `t͡s` | **c**íme, huszonnyol**c** | `kvuca`, `Kivsza`, `Zmán Kvucá` |
| `ʃ` | **s**aját, `fõorvos` | `Somer`, `someres`, `Hasomer` |
| `x` | **h**rabovszki, i**h**letével | a szóvégi torokhang a `madrich` / `chanich` alakban |

*(A `fõorvos` alak a forrásoldal kódolási hibája — az `ő` betűk végig `õ`-ként jelennek meg rajta. Szó szerint idézzük, nem javítjuk.)*

**A verzió-rögzítés forrása** ugyanaz a lap
(`learn.microsoft.com/azure/ai-foundry/responsible-ai/speech-service/text-to-speech/transparency-note`,
lekérdezve 2026-08-27), szó szerint:

> „Microsoft will provide customers with 12 months' notice before removing any prebuilt
> neural voices from our catalog, unless security, legal, or system performance
> considerations require an expedited removal. **This does not apply to previews.**”

A Google **fonéma-referenciája 18 locale-t sorol, és egyetlen magyar említést sem
tartalmaz** — ott az IPA-felülírás próbálgatás. Az ElevenLabs a saját dokumentációjában
a v3 IPA-támogatást „80–90% kiejtési következetességként” írja le, és kimondja, hogy az
azonos IPA-átirat is adhat eltérő kimenetet.

**Ez viszont csak a felét dönti el.** Azt, hogy egy hang *úgy szól-e*, mint egy meleg,
egyenrangú, tegező magyar madrich, dokumentációból nem lehet megállapítani. Ezért a
D2 válaszát **meghallgatásos teszthez** kell kötni:
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md).

### 13.3. Konkrét magyar hangjelöltek

**Megerősített azonosítók.** Az alábbi sztringek a szolgáltató saját, bejelentkezés
nélkül elérhető dokumentációs listáján szerepelnek, és külön ellenőrzésen is átmentek:

| Motor | Hang | Állapot | Nem (a szolgáltató jelölése) |
|---|---|---|---|
| Azure | `hu-HU-NoemiNeural` | **GA** | Female |
| Azure | `hu-HU-TamasNeural` | **GA** | Male |
| Azure | `hu-HU-Bence:MAI-Voice-2`, `-Levente:`, `-Lilla:`, `-Réka:` | nyilvános **előzetes** — a 12 hónapos garancia **nem** vonatkozik rájuk | M / M / F / F |
| Google | `hu-HU-Chirp3-HD-Charon`, `-Orus` | GA | MALE |
| Google | `hu-HU-Chirp3-HD-Kore`, `-Leda` | GA | FEMALE |

A 8. szakasz kétszereplős jelenete egyetlen motoron belül megoldható: az Azure és a
Google is ad legalább egy férfi és egy női GA magyar hangot.

> ⛔ **ElevenLabs: nincs megerősíthető voice-ID.** A szolgáltatónak **nincs bejelentkezés
> nélküli azonosító→név feloldása**: a `/v1/voices/{id}` és a szűrt `/v1/shared-voices`
> végpont egyaránt hitelesítést kér, a webes hangkönyvtár pedig bármely sztringre azonos
> oldalvázat ad vissza, tehát a HTTP 200 nem bizonyíték. **Ezért ez a lap nem közöl
> ElevenLabs voice-ID-t.** Ha a D2 erre az ágra esik, a hangot a fiókból, hitelesített
> `GET /v1/voices/{id}` hívással kell azonosítani, és a visszakapott `name` mezőt kell
> ide beírni. Egy másolt, meg nem erősített azonosító némán más beszélőt adna.

A 8. szakasz kétszereplős jelenete (`M1.3-VID-01`) egyetlen motoron belül megoldható: az
Azure és a Google is ad legalább egy férfi és egy női GA magyar hangot.

### 13.4. Emberi felmondó — indikatív piaci sáv

Több nyilvános szinkron- és e-learning-árlista, illetve piactéri árazás **összesített**
sávja, tájékoztató jelleggel; **nem ajánlat, és tételenként nincs forrásolva** — a
konkrét számokat ajánlatkéréskor kell ellenőrizni.

| | Nettó | Bruttó (27% áfával) |
|---|---|---|
| Teljes sáv ~60 perc kész hangra | 255 000 – 690 000 Ft (≈ 700–1 900 €) | 324 000 – 878 000 Ft |
| Középérték | ≈ 420 000 Ft (≈ 1 150 €) | ≈ 532 000 Ft |

Ezen felül **≈ 35 000 – 90 000 Ft** a 117 fájl darabolása és elnevezése, ha nincs benne
a csomagban.

> ⚠️ **A szerződés szerkezete többet számít, mint a napidíj.** Egy magyar árlistán a
> 117 tétel **4 095 000 Ft**, ha 117 külön „spotként” árazzák, és **80 000 Ft**, ha
> egyetlen, legfeljebb 60 perces megbízásként — **51-szeres különbség azonos munkára**.
> *(Egyetlen árlistából; a nagyságrend a lényeg, nem a pontos szám.)* Emberi felmondó esetén **egy projektként, megadott fájlszámmal**
> kell szerződni.
>
> A piactér-útvonal (Fiverr-típusú) ára szóalapon 17-szeres szórást mutat, a kereskedelmi
> felhasználást **külön felárként** árazza, és a mintában szereplő eladók
> **legfeljebb 5 fájlra** bontják a leadást — 117 fájlos, LMS-en publikált anyaghoz ez
> nem megtakarítás, hanem licencelési csapda.

### 13.5. Költség — a szintetikus ág nem költségdöntés

Alap: 60–80 perc kész hang, 100–120 szó/perc → 6 000–9 600 szó → ≈ 50 000–82 000
karakter kész; a próbákkal és újravételekkel **3× nyers ≈ 150 000–225 000 karakter**.

| Motor | Kész hang | 3× nyers |
|---|---|---|
| Google Chirp3-HD | 0 $ | **0 $** — belefér az 1M karakter/hó ingyenes keretbe |
| Azure (15 $ / 1M karakter) | ≈ 0,75–1,25 $ | **≈ 2,25–3,40 $** |
| ElevenLabs v3 (0,10 $ / 1000 karakter) | ≈ 5–8 $ | **≈ 15–22,50 $** |

A bizonytalanság ±30%, döntően a magyar karakter/szó arányból. **A három szintetikus
opció között a költség nem érdemi különbség** — a döntést a magyar természetesség, a
kiejtés-kikényszeríthetőség és a hónapokkal későbbi reprodukálhatóság döntse el.
Az emberi felmondó ennek 300–1000-szerese, ami viszont **nem** teszi rossz választássá:
más kockázatprofilt vesz.

Két gyakorlati kikötés, ha a döntés az adott ágra esik:
- **Azure:** az SSML-jelölés is számlázott karakter (a `<speak>` és `<voice>` kivételével)
  — a kiejtést ezért a PLS-szótárból vezéreld, ne soronkénti `<phoneme>` címkékkel. A
  szótár karakterei nem számlázottak.
- **ElevenLabs:** a 44,1 kHz-es WAV/PCM kimenet a dokumentáció szerint **Pro-csomagot**
  igényel; az ingyenes szinten a publikált tartalom **forrásmegjelölésre kötelezett**, és
  csak fizetős csomag ad kereskedelmi licencet.

### 13.6. Ami a 10. szakasz nyitott mastering-értékeit illeti

A jelenlegi javaslat (mono, beszédre normalizálva, azonos csúcsértékkel) **változatlan**.
A pilot-felvételkor rögzítendő konkrét értékekhez annyi jött hozzá, hogy a jelölt motorok
kínálnak alkalmas kimeneti formátumot (az Azure például 48 kHz / 16 bit / mono PCM-et).
**Ez nem választás, csak annyi, hogy a 10. szakasz nyitott mezői a pilot után nem
maradnak technikailag megoldatlanok.**

### 13.7. Amit ez a lap NEM dönt el — emberi kapuk

| # | Kérdés | Kihez tartozik |
|---|---|---|
| V1 | A Microsoft átláthatósági jegyzete (URL a 13.2-ben, lekérdezve 2026-08-27) kimondja: „**Disclose the synthetic nature of voices, images, and/or videos to users** such that users are not likely to be deceived or duped…”, és külön: „**Consider proper disclosure to parents or other parties** with use cases that are designed for or may be used in situations involving minors and children. If your use case is intended for minors or children, **you'll need to ensure that your disclosure is clear and transparent so that parents or legal guardians can understand the role of synthetic media** and make an informed decision on behalf of minors or children about whether to use the experience.” A tananyag R1-címkéje a **tanulónak** szól. Hogy ez önmagában kielégíti-e a szülői tájékoztatás elvárását, **gyermekvédelmi és adatvédelmi kérdés**. | gyermekvédelmi felelős + DPO; a kánoni hely a `Gyermekvédelem – release gate.md` és az `Adatvédelem – tanulói adatok és AI.md`, **nem ez a lap** |
| V2 | Elfogadható-e, hogy egy **előzetes (preview)** hangra ne vonatkozzon a 12 hónapos garancia? Ha igen, a hang eltűnésekor 117 tétel mondandó újra. | program- és költségvetési felelős |
| V3 | A szolgáltatói kimenet-tulajdonlási záradék az Azure és a Google esetében **nem ellenőrzött** (a Microsoft Product Terms és a Google kereskedelmi feltételei nem lettek lekérdezve). | jogi jóváhagyó — [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |

> Szolgáltatót ez a lap továbbra sem választ. A fenti kutatás **szűkíti** a döntést, nem
> helyettesíti: a D2 válasza szervezeti, költségvetési és jogi döntés marad.
