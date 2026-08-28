# 🎙️ Narrátor hang-bible

Az R3 produkciós szabály végrehajtási lapja: minden, ami a **jelenlegi tananyagból
objektíven levezethető** a felmondásról. Ami nyitva maradt, azt a lap kimondja, és a
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D2 pontjára mutat — ott van
egyetlen helyen az összes megválaszolandó érték.

**Hatókör:** 90 narráció-asset, 21 beszélőfej-videó, 6 karakter- és jelenetvideó — összesen
117 tétel, mind szó szerinti forrásblokkal. Nincs többé szkript nélküli beszélt asset.

> **A szolgáltató 2026-08-28-án eldőlt: a felmondás szintetikus, a motor az ElevenLabs.**
> Ami még nyitva van, az a **kanonikus hang** — a felhasználó két meglévő egyedi hangja,
> a **Dombi Miksa** és a **Budai Enn** közül —, valamint a hozzá tartozó voice-ID, modell,
> beállítás és jogosultsági bizonyíték. Részletek a 12–13. szakaszban; a hangválasztás
> végrehajtható terve: [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md).
>
> Az 1–11. szakasz mindezektől függetlenül érvényes: ezek a tananyagból következnek, nem
> a szolgáltatóból.

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
rögzítendők. Javaslat a pilothoz: mono, beszédre normalizálva, azonos csúcsértékkel
minden fájlban.

> A szolgáltató kiválasztása után ezek **eldönthetővé váltak**: a formátum-lista és a
> csomaghoz kötött korlátok a 13.7. szakaszban állnak. Röviden: veszteségmentes
> 44,1 kHz-es WAV-mesterhez Pro-csomag kell; Creator-on a legjobb elérhető mester a
> 192 kbps MP3. **A választás a csomagon múlik, és még nem történt meg.**

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

## 12. Motor és hang — a szolgáltató ELDŐLT, a hang még nem

**Felhasználói döntés, 2026-08-28.**

| Mező | Állapot |
|---|---|
| Szintetikus vagy emberi felmondó | ✅ **SZINTETIKUS** — eldőlt |
| Motor / szolgáltató | ✅ **ElevenLabs** — eldőlt |
| Modell | 🔎 **javaslat: `eleven_flash_v2_5`**, `language_code: "hu"` — a meghallgatás erősíti meg (13.2.) |
| Hangjelöltek | ✅ a felhasználó **két meglévő egyedi hangja**: **Dombi Miksa** és **Budai Enn** |
| Kanonikus narrátor | ⛔ **NYITOTT — meghallgatásos döntés** (13.3., [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md)) |
| Voice-ID | ⛔ **NEM ELLENŐRZÖTT — fióklekérdezés szükséges** (13.4.) |
| Hangtípus (klón / tervezett / stb.) | ⛔ **NEM ELLENŐRZÖTT — fióklekérdezés szükséges** (13.4.) |
| Hangbeállítások és seed | ⛔ nyitott — a pilot rögzíti (13.6.) |
| Kiejtési szótár | ⛔ nyitott — a meghallgatás mondja meg, mire kell (13.5.) |
| Hang-jogosultság igazolása | ⛔ nyitott → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |

> **Az R3 ettől NEM zárul le.** A szolgáltató kiválasztása a kérdésnek csak az egyik fele.
> Amíg nincs kanonikus hang, ellenőrzött voice-ID, rögzített modell és beállítás-készlet,
> a felvétel **nem reprodukálható** — az R3 blokkoló ezért mind a 117 tételen a helyén
> marad.

---

## 13. ElevenLabs — produkciós kutatás (2026-08-28)

Minden állítás a szolgáltató saját dokumentációjából, 2026-08-28-án lekérdezve. Fizetős
API-t nem hívtunk, fiókot nem hoztunk létre, hangot nem generáltunk és nem klónoztunk.

### 13.1. Az első megállapítás, ami a modellválasztást eldönti

**Az `eleven_multilingual_v2` nem támogatja a magyart.** A dokumentált nyelvlistája 29
nyelv, és a `hu` nincs köztük. Ez azért fontos, mert épp ezt a modellt jelöli a
szolgáltató úgy, hogy „Most stable on long-form generations”. A magyar nyelv tehát
**leszorít a stabilitási zászlóshajóról**, és a valódi választás két modell között marad:

| Modell | Magyar | Egyedi hang | Kiejtés-vezérlés | Tempó-vezérlés | Ár / 1000 karakter |
|---|---|---|---|---|---|
| **`eleven_flash_v2_5`** | ✅ `hu` | ✅ teljes | **csak alias-szabály** (a fonéma-címkéket kihagyja) | ✅ `speed` 0,7–1,2 | **0,05 $** |
| `eleven_v3` | ✅ „Hungarian (hun)” | IVC igen; **PVC-re „not fully optimized”** | ✅ IPA is (**az egyetlen nem angol IPA-út**) | ❌ **nincs** | 0,10 $ |
| `eleven_multilingual_v2` | ❌ **nincs** | ✅ | alias | ✅ | 0,10 $ |
| `eleven_flash_v2` | ❌ csak angol | ✅ | fonéma-címke (angol) | ✅ | 0,05 $ |
| `eleven_turbo_v2_5` | ✅, de **nyugdíjazott** | ✅ | alias | ✅ | — |

**A karakterkorlát nálunk nem szempont:** a leghosszabb tételünk is bőven egyetlen kérésbe
fér, tehát darabolásra és összefűzésre nincs szükség.

### 13.2. Modell-javaslat: `eleven_flash_v2_5`

**Öt tárgyi ok, és mind a reprodukálhatóságról szól:**

1. **A v3-nak nincs tempó-vezérlése.** Szó szerint: „Speed is not available for the Eleven
   v3 model.” A 4. szakasz céltempója (100–120 szó/perc) **kötött produkciós előírás** —
   a v3-on nem lenne rá szabályozó, csak a szöveg átírása. Ez önmagában közel kizáró.
2. **A v3 két további rögzíthető paramétert is elvesz:** „Similarity is not available for
   the Eleven v3 model.” és „Speaker Boost is not available for the Eleven v3 model.”
   Kevesebb rögzíthető paraméter = gyengébb reprodukálhatóság fél év múlva.
3. **A szolgáltató maga mondja a v3-ról:** „more variable consistency”.
4. **A v3 ronthatja is a hangot:** „Professional Voice Clones (PVCs) are currently not
   fully optimized for Eleven v3, resulting in potentially lower clone quality.”
5. **Az expresszivitás itt nem előny, hanem kockázat.** A v3 egész ajánlata az érzelmi
   tartomány és az audio-tagek; a 3. szakasz viszont **szűk érzelmi sávot** ír elő, benne
   érzékeny gyermekvédelmi tartalommal. A dupla árat azért fizetnénk, hogy utána
   elnyomjuk, amit vettünk.

Ráadásul a `flash_v2_5` **fele annyiba kerül**, és elfogadja az SSML szünet-jelölést,
amit a v3 elutasít — ez a nyugodt magyarázó ritmus tisztább eszköze.

**Amit a v3 tud és a flash nem:** „If you want to use IPA and CMU pronunciations in
languages other than English, you will have to switch to the `eleven_v3` model.” A nem
angol IPA kizárólag v3-on érhető el.

**Miért valószínű, hogy ez minket nem üt meg.** A someres szavaink **már magyar fonetikus
írásmódban állnak**: a magyar helyesírásban az `s` = /ʃ/ és a `c` = /ts/, tehát a `Somer`
és a `kvuca` a leírt alakból helyesen kellene hogy szóljon — **feltéve, hogy a modell
magyarként kezeli a szöveget**. Épp ezért kötelező a `language_code: "hu"` megadása. A
valódi kockázat nem a magyar helyesírás, hanem az, hogy a modell angol vagy héber
olvasatra vált.

> **Tartalék: `eleven_v3`.** Csak akkor váltunk rá, ha a meghallgatás azt mutatja, hogy a
> maradék hibák alias-szabállyal és átírással nem javíthatók. A csere ára: nincs
> tempó-vezérlés, nincs similarity- és speaker-boost-rögzítés, PVC-nél minőségromlás,
> dupla költség és bevallottan ingadozóbb konzisztencia — cserébe olyan IPA-ért, amelyet a
> szolgáltató maga „80–90% pronunciation consistency”-ként ír le.
>
> **Döntési sorrend:** előbb a hangtípust kell megállapítani (13.4.). Ha bármelyik hang
> **PVC**, a v3 gyakorlatilag kiesik, és a `flash_v2_5` a válasz.

### 13.3. A hangválasztás — dokumentációból nem eldönthető

A két jelölt a felhasználó két meglévő egyedi hangja:

| | |
|---|---|
| **A) Dombi Miksa** | jelölt a kanonikus narrátor szerepre |
| **B) Budai Enn** | jelölt a kanonikus narrátor szerepre |

**Ajánlás: nincs — MEGHALLGATÁS SZÜKSÉGES.** Két hang közül dokumentáció alapján
választani nem lehet; a magyar természetesség, a melegség és a someres szavak kiejtése
csak hallgatással dönthető el. A hatpárosos összehasonlítás végrehajtható terve:
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md).

**Egy hang lesz a kanonikus narrátor**, ahogy az R3 első mondata előírja. A másik hang
sorsa (tartalék, dialógus- vagy karakterhang) **külön, későbbi döntés** — ez a lap nem
osztja ki neki egyik szerepet sem.

### 13.4. A két hang azonosítása — fióklekérdezés szükséges

> ⛔ **Ebben a környezetben nincs ElevenLabs hitelesítő adat** — sem környezeti változó,
> sem konfigurációs fájl, sem kulcstartó-bejegyzés, sem MCP-kapcsolat. A voice-ID-t és a
> hangtípust ezért **nem tudtuk lekérdezni, és nem is találjuk ki.**

**Amit a felhasználónak ki kell nyernie — webes út (a leggyorsabb):**

1. **My Voices** oldal (`elevenlabs.io/app/voice-lab`).
2. A hang neve melletti **típusikon** megmondja a hangtípust — a dokumentált jelmagyarázat:
   **sárga pipa** = Professional Voice Clone · **fekete pipa** = Studio Quality PVC ·
   **villám** = Instant Voice Clone · **nincs ikon** = Voice Design (tervezett hang).
3. Ugyanott látszik, **milyen nyelvre tanították** — ellenőrizendő, hogy magyar.
4. A három pont menüben: **Copy voice ID**.

**Hitelesített, csak olvasó API-út** (generálás és költés nélkül):

```
GET /v2/voices?search=Dombi%20Miksa&voice_type=personal
GET /v2/voices?search=Budai%20Enn&voice_type=personal
GET /v1/voices/{voice_id}
GET /v1/voices/{voice_id}/settings
GET /v1/models
```

**Amit a válaszból rögzíteni kell:**

| Mező | Mit mond meg |
|---|---|
| `voice_id` | maga az azonosító — a dokumentáció példáiban **20 karakter**, vegyes kis- és nagybetű + számjegy |
| `category` | a hangtípus: `cloned` (IVC) · `professional` (PVC) · `high_quality` (stúdió-PVC) · `generated` (Voice Design) · `premade` · `famous` |
| `fine_tuning.state` | **PVC-nél ez a modell-kompatibilitás válasza** — melyik modellre van betanítva |
| `verified_languages[]` (`language`, `model_id`, `accent`) | igazolt-e a **magyar**, és melyik modellen |
| `voice_verification.is_verified` | PVC-hitelesítés állapota |
| `settings` | a tárolt `stability`, `similarity_boost`, `style`, `use_speaker_boost`, `speed` |
| `is_owner`, `sharing.status` | tulajdon és megosztási állapot |

A `GET /v1/models` válaszából modellenként érdemes: `model_id`, `languages`,
`serves_pro_voices` (kiszolgálja-e a PVC-ket), `can_use_style`, `can_use_speaker_boost`.

**Mit jelent a három lehetséges típus nálunk:**

| Típus | Következmény |
|---|---|
| **PVC** (`professional` / `high_quality`) | a legstabilabb választás 117 tételre; **csak saját hang klónozható** — „Even with their consent, you cannot clone someone else's voice”; a szolgáltató szerint a PVC automatikusan a Flash v2.5 / Turbo v2.5 / Multilingual v2 modellekre tanul — **a v3 nincs ebben a listában**; Creator-csomag vagy feljebb kell hozzá |
| **IVC** (`cloned`) | a v3 nyitva marad; kevésbé stabil; a hangsúly a forrásfelvételtől függ — ellenőrizendő, hogy **magyar** anyagra tanult, mert „if you use a voice that is not native to the language, it might retain its native accent” |
| **Voice Design** (`generated`) | teljesen szintetikus: **nincs valós személyhez kötött jogosultsági kérdés** — ez a legegyszerűbb jogi helyzet |

> ⚠️ **PVC-nél egy külön kapcsolót is rögzíteni kell.** A kérés `use_pvc_as_ivc` mezője
> (alapérték `false`) eldönti, hogy a PVC- vagy az IVC-változat szólal-e meg — ugyanahhoz
> a hanghoz **két különböző renderelés** tartozik. Ha nincs explicit megadva, egy későbbi
> klip csendben a másikból jöhet.

### 13.5. Kiejtés — mi működik a `flash_v2_5`-ön

| Eszköz | `flash_v2_5` | `v3` |
|---|---|---|
| Szótár **alias**-szabály | ✅ | ✅ |
| Szótár **fonéma**-szabály (IPA/CMU) | ❌ kihagyja | ✅ |
| Soron belüli IPA | ❌ | ✅ |
| Nem angol IPA | ❌ | ✅ **csak itt** |

Szó szerint: „Pronunciation dictionary phoneme tags only work with eleven_flash_v2 and
eleven_v3 models. Other models skip dictionary phoneme tags and use the default
pronunciation. For other models, **use alias tags instead**.”

**A javasolt eljárás — és ez szándékosan a legkevesebb beavatkozás:**

1. `language_code: "hu"`, **szótár nélkül** legyártani a hat mintát.
2. **Meghallgatással** megállapítani, melyik szó romlik el ténylegesen. A várható
   töréspont a `madrich` és a `chanich` (a `ch` = /x/ digráf nem magyar helyesírási elem),
   valamint a `Leviatan` (megnyúló *á* kockázata).
3. **Csak a tényleges hibákat** javítani alias-szabállyal — például `madrich → madrih`,
   mert a magyarban nincs fonemikus /x/, és a /h/ a természetes realizáció.
   **Minden aliast meghallgatással kell megerősíteni.**
4. Az IPA marad tartaléknak; ez az egyetlen ok, ami a v3-ra váltást indokolná.

> ⚠️ **Magyar toldalékolási csapda — ez a szakasz legfontosabb gyakorlati tudnivalója.**
> A szótárszabályok `case_sensitive` és `word_boundaries` kapcsolója egyaránt
> **alapértelmezetten igaz**. Szóhatárral egy `Somer` szabály **nem fog illeszkedni** a
> `someres`, `Somert`, `Somerek` alakokra. A magyar toldalékolás miatt tehát **a ténylegesen
> előforduló összes alakot fel kell sorolni** (`kvuca / kvucát / kvucában / kvucák`,
> `peula / peulát / peulák`, `madrich / madrichok / madrichhoz` …), vagy tudatosan ki kell
> kapcsolni a szóhatárt és vállalni a részszó-illeszkedést. **A szabálylistát a tényleges
> szkriptekből kell építeni, nem szótári alapalakokból.**

Szótár-mechanika: a szabályok `add-from-rules` hívással hozhatók létre, a kéréshez
`pronunciation_dictionary_locators` mezőben csatolhatók (**legfeljebb 3**), és minden
szerkesztés **új `version_id`-t** hoz létre. **A `version_id`-t explicit rögzíteni kell**,
különben a szótár csendben elcsúszik.

### 13.6. Beállítások és reprodukálhatóság

| Paraméter | Alapérték | Tartomány | Megjegyzés |
|---|---|---|---|
| `stability` | 0,5 | 0–1 | alacsonyabb = szélesebb érzelmi sáv; **a mi szűk sávunkhoz magasabb** (~0,6–0,75) |
| `similarity_boost` | 0,75 | 0–1 | **v3-on nincs** |
| `style` | 0,0 | 0–1 | a szolgáltató ajánlása: „keep this setting at 0 at all times”; emeli az instabilitást |
| `use_speaker_boost` | `true` | logikai | **v3-on nincs** |
| `speed` | 1,0 | **0,7–1,2** | **v3-on nincs** — ez a 100–120 szó/perc szabályozója |

> **A kérésben küldött beállítás felülírja a hangon tároltat, de csak arra a kérésre.**
> Ebből egy kemény produkciós szabály következik: **minden kérésnél explicit el kell
> küldeni a teljes beállítás-készletet.** Ha a tárolt beállításra hagyatkozunk, elég, ha
> valaki hónapok múlva a felületen hozzányúl a hanghoz, és a kimenet csendben megváltozik.

**Az őszinte plafon.** A szolgáltató kimondja: „The models are nondeterministic. For
consistency, use the optional seed parameter, though **subtle differences may still
occur**.” A `seed` leírása is óvatos: „our system will make a best effort to sample
deterministically… **Determinism is not guaranteed**.”

Ebből következik: egy fél év múlva újragyártott klip **hasonló lesz, nem bitre azonos**.
Produkciós válasz: minden újragyártásnál meghallgatás, és **inkább a teljes tétel
újravétele**, mint egy javított mondat beillesztése a régi felvételbe.

### 13.7. Kimeneti formátumok

A formátum-azonosító alakja `kodek_mintavétel_bitráta`. A csomag-kötöttség szó szerint:
„MP3 with 192kbps bitrate requires you to be subscribed to **Creator tier or above**. PCM
and WAV formats with 44.1kHz sample rate requires you to be subscribed to **Pro tier or
above**.”

| Szerep | Formátum | Csomag |
|---|---|---|
| **Archív mester (ideális)** | `wav_48000` — **48 kHz** / 16 bit, veszteségmentes. A formátum-listában létezik (ellenőrizve); a 10. szakasz és a produkciós stack 6. szakasza is 48 kHz-et ír elő, tehát **nincs leminősítés** | a 44,1 kHz-re a szolgáltató kimondottan **Pro**-t követel; a **48 kHz csomag-kapuját a dokumentáció nem mondja ki** — a fiókban ellenőrizendő |
| **Archív mester (Creator-on ez a maximum)** | `mp3_44100_192` | **Creator** |
| **Videó-vágás bemenete** | a fenti mester, egyszer importálva | — |
| **Moodle/H5P lejátszás** | `mp3_44100_128` | bármely |

> **Ez valódi minőségi döntés.** Creator-csomagon **minden mester veszteséges**, és minden
> belőle készülő derivatíva másodgenerációs tömörítés. A veszteségmentes mesterhez Pro
> kell. A 10. szakasz nyitott mastering-értékei ezzel eldönthetővé válnak.

**Felirat-időzítés — külön nyeremény.** A szolgáltatónak van olyan végpontja, amely a
hanggal együtt **karakterszintű időbélyegeket** ad vissza. Ez pontosabb, mint bármilyen
utólagos illesztés, és **a felirat forrásszövege így is a lecke marad** — a végpont csak
az időzítést adja, a szöveget nem. Ezt a P-NAR pilotnál érdemes kipróbálni.

### 13.8. Jog, adatkezelés, provenance

Magyar szervezetnek az **EGT-s** feltételszöveg az irányadó (lekérdezve 2026-08-28).

| Tárgy | A szolgáltató szövege | Következmény |
|---|---|---|
| **Kereskedelmi használat** | ingyenes szinten „only use the Services for non-commercial purposes”; fizetős előfizetéssel „may use the Services for commercial purposes” | **fizetős csomag kötelező** |
| **Kimenet-tulajdon** | „you retain all rights in and to your Output” | rendben |
| **Licenc a feltöltött tartalomra** | „perpetual and irrevocable… nonexclusive… royalty-free… worldwide and sub-licensable” licenc a szolgáltatás fejlesztésére | lásd a tanítási kimaradást |
| **Tanítás a bemeneten — kimaradás** | „you may opt out of our use of your Content for training at any time… **does not affect any uses… prior to that date**” | **a kimaradást ELŐRE kell bekapcsolni**, nem utólag |
| **Klónozás** | PVC: „Even with their consent, you cannot clone someone else's voice”; IVC: önbevalló jelölőnégyzet | a szolgáltató **nem ír elő bizonyíték-formát** — ez a mi oldalunkon emberi döntés |
| **Megőrzés** | a hangról generált adatot „not… longer than 3 years after your last interaction” | rögzítendő |
| **Közlési kötelezettség** | a kifejezett kötelezettség **AI-ügynökökre** szól („must clearly and prominently disclose… they are interacting with AI rather than a human”), nem előre renderelt narrációra | **a narrációra nincs szolgáltatói közlési előírás** |

> **Ez nem gyengíti az R1-et.** A tananyag AI-címkéje **projektszabály**, nem szolgáltatói
> követelmény — és attól, hogy a szolgáltató nem írja elő, változatlanul kötelező marad.
> A tiltó oldal viszont érvényes: a szolgáltató politikája tiltja az AI-eredet
> megtévesztő elhallgatását.

**Provenance — a projekt „ne távolítsd el” szabálya szempontjából ez a legfontosabb.**

- A szolgáltató **hallhatatlan hangvízjelet** ágyaz a generált hangba
  („imperceptible digital watermarks”, „completely inaudible”). Mivel ez a hullámformában
  él, nem metaadatban, elvben túléli az átkódolást — **de a szolgáltató nem publikál
  robusztussági leírást, tehát ez nem ellenőrizhető.**
- A bevezetés **nem befejezett**: a leírás szerint a lefedettség 2026 júliusa folyamán
  terjedt ki a fizetős szintekre, és a lap nem mondja ki, hogy ez lezárult. Hogy a
  **mi** fizetős kimenetünk ma vízjelezett-e, nyilvános oldalról **nem állapítható meg**.
- **A beszéd-kimeneten nincs C2PA.** A C2PA-aláírás kapcsolója a szolgáltató API-jában
  kizárólag a zenei végponton létezik, a szöveg-beszéd kérésben nincs ilyen mező.
- **Gyakorlati következmény:** a hang oldalán **nincs olyan gépi provenance-jelölés, amit
  csatolni, ellenőrizni vagy megőrizni tudnánk**. Az R1 gépi ága itt nem értelmezhető —
  a kötelezettséget a **saját manifeszt-fegyelmünk** és a tanulónak látható címke viszi.
  Ezt ki kell mondani, nem elhallgatni.

### 13.9. Költség

> ⚠️ **A szolgáltató két árazási felülete nem mond ugyanazt, ezért itt nem adunk egyetlen
> pontos számot.** Az API-árazási oldal karakteralapú dollárárat közöl (`flash_v2_5`
> 0,05 $ / 1000 karakter, `v3` 0,10 $ / 1000). A fő árazási oldal viszont **kredit**-alapon
> számol, és a saját GYIK-je a Flash/Turbo-ra „0,5 és 1 kredit karakterenként” **sávot** ad,
> nem rögzített 0,5-et — ebből az olvasatból lényegesen magasabb, kb. 0,165–0,20 $ / 1000
> karakter jön ki. **Ez a szolgáltató belső ellentmondása, nem a mi bizonytalanságunk.**
> Alább ezért mindkét olvasat szerepel.

| Tétel | Karakter | Alsó becslés (API-oldal) | Felső becslés (kredit-olvasat) |
|---|---:|---|---|
| **Hatmintás meghallgatás** (mérve) | 3 066 | **≈ 0,15 $** | **≈ 0,61 $** |
| Teljes tananyag, kész hang | 50–82 ezer | 2,50 – 4,10 $ | 10 – 16 $ |
| Teljes tananyag, **3× nyers** | 150–225 ezer | **7,50 – 11,25 $** | **30 – 45 $** |

*(A `v3` mindkét olvasatban nagyjából a kétszerese.)*

**A lényeg a bizonytalanság ellenére is áll:** a teljes tananyag hangja **tíz–ötven dollár
nagyságrend**, a hatmintás teszt pedig **kevesebb, mint egy dollár**. A csomagot ezért ne a
karakterár döntse el, hanem a **kimeneti formátum és a hangtípus**: Creator elég a
kereskedelmi használathoz és a 192 kbps MP3-hoz, Pro csak a veszteségmentes WAV-mesterhez
kell. **A tényleges elszámolást a fiókban kell ellenőrizni** az első köteg után.

### 13.10. Amit ez a lap NEM dönt el — emberi kapuk

| # | Kérdés | Kihez tartozik |
|---|---|---|
| **V1** | *(korábbi, Microsoft-specifikus tétel — **tárgytalan**, mert nem az a szolgáltató lett kiválasztva.)* Helyette: a választott szolgáltató **nem ír elő** közlési kötelezettséget előre renderelt narrációra. A tananyag R1-címkéje tehát **saját projektdöntés**, és az is marad. Hogy kiskorú tanulók esetén a **szülő/gondviselő** felé kell-e külön tájékoztatás, továbbra is nyitott — de ez a **tananyag** kérdése, nem a szolgáltatóé. | gyermekvédelmi felelős + DPO; a kánoni hely a `Gyermekvédelem – release gate.md` és az `Adatvédelem – tanulói adatok és AI.md` |
| **V2** | A hang **jogosultsági bizonyítéka**. Ha a kiválasztott hang valós személy klónja, a szolgáltató önbevalláson túl **semmilyen bizonyíték-formát nem ír elő** — a szervezetnek magának kell eldöntenie, milyen hozzájárulást tart, milyen formában és meddig. | jogi jóváhagyó + a hang jogosultja → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |
| **V3** | A szolgáltató feltételei szerint 18 év alatti nem használhatja a szolgáltatást, és kiskorú hangadata nem tölthető fel; a tiltólista viszont 13–18 közötti használatot szülői hozzájárulással elképzelhetőnek tart. **A saját dokumentumaik nem mondanak ugyanazt.** A tananyagban a madrich maga is lehet kiskorú. Kiskorú hangjának klónozása egyértelműen tiltott; hogy kiskorú kezelheti-e a fiókot, nyitott. | gyermekvédelmi felelős |
| **V4** | A **tanítási kimaradást** be kell kapcsolni, **mielőtt** bármit feltöltünk — visszamenőleg nem hat. Ez üzemeltetési lépés, de felelőst kíván. | a fiók gazdája |

> A kutatás **szűkíti** a döntést, nem helyettesíti. A kanonikus hang kiválasztása
> meghallgatásos emberi döntés marad.
