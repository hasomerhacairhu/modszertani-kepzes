# 🧪 Pilot-produkciós csomag

Családonként **egy** tétel készül el először, és azt kell jóváhagyni, mielőtt a testvérei
elindulnak. Ez a lap minden pilothoz megadja, amit a gyártáshoz tudni kell: a pontos
forrást, a stílusfüggéseket, a promptot vagy elrendezés-briefet, a fájlnevet, valamint az
**elfogadási és bukási feltételt**.

> ⚠️ **A csomag írásakor (2026-08-28) egyik pilot sem volt gyártható:** mind a kilencen
> nyitott kapu ült. Ez a lap **elő van készítve** a jóváhagyás utáni pillanatra — nem
> gyártási engedély. A kapu-állapotokat a 2. szakasz tételesen kimondja.
>
> **2026-10-02:** a hat vizuális és nyomtatott pilot (P-DIA, P-IKO, P-ILL, P-MUN, P-POS,
> P-KRT) egyetlen kapuja a D1 volt, amely projektgazdai döntéssel lezárult; náluk már csak
> az asset-szintű R5-blokkoló kivezetése van hátra a manifesztben. A P-NAR, a P-VID és a
> P-KAR előtt továbbra is nyitott kapu áll.

Kapcsolódó: [`MEDIA-PRODUCTION-PLAN.md`](./MEDIA-PRODUCTION-PLAN.md) (a generált
köteg-terv és pilot-táblázat) · [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md)
· [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) ·
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md)

---

## 1. A kilenc pilot

| # | Család | Pilot | Család mérete | Köteg | Kapuk | Eredet |
|---|---|---|---:|---|---|---|
| P-NAR | narráció / hang | `M4.2-NAR-03` | 89 | B3 | R2, R3 | a terv 2026-08-28-i javaslata; a 2026-10-03-i projektgazdai döntés (VO D-13) megerősítette |
| P-VID | AI beszélőfej | `M5.1-VID-01` | 18 | B3 | R2, R3 | a terv 2026-08-28-i javaslata |
| P-KAR | AI karakter-jelenet | `M4.1-VID-03` | 6 | B3 | R2, R3, R5 | **eltérés** — indoklás lent |
| P-DIA | diagram | `M0.2-DIA-01` | 39 | B0 | R5 | a terv 2026-08-28-i javaslata |
| P-IKO | ikon-készlet | `M1.3-IKO-01` | 40 | B0 | R5 | **eltérés** — indoklás lent |
| P-ILL | illusztráció | `M4.2-ILL-01` | 46 | B0 | R5 | a terv 2026-08-28-i javaslata |
| P-MUN | munkalap / nyomtatvány | `M6.A-MUNK-02` | 66 | B0 | R5 | a terv 2026-08-28-i javaslata |
| P-POS | poszter | `M7.B-POSZ-01` | 36 | B0 | R5 | a terv 2026-08-28-i javaslata |
| P-KRT | kártyaszett | `M5.A-KART-01` | 23 | B0 | R5 | **kiegészítés** — indoklás lent |

Az „Eredet” oszlop — és a „Kapuk” oszlop, valamint a pilotonkénti „Státusz · kapuk” sor —
a csomag írásakori (2026-08-28) állapotot rögzíti; az R5 a D1 2026-10-02-i lezárásával
kikerül a kapuk közül, az aktuális állapot a generált tervben áll. A generált terv a
pilotot minden buildnél a saját szabálya szerint újraszámolja, ezért a mostani
terv-pilot ettől eltérhet — az aktuális ID-k a
[`MEDIA-PRODUCTION-PLAN.md`](./MEDIA-PRODUCTION-PLAN.md) 5. szakaszában vannak. Ez a lap a
briefjeit a fenti ID-kre írta.

A „család mérete” a terv számolásmódját követi: az újrahasznosított (`reuse`) és az
élő/runtime tételek nélkül. A terv a posztert és a kártyaszettet **egyetlen, 59 tételes
családként** kezeli (36 + 23) — itt azért bontjuk ketté, mert a produkciós módszerük
eltér (lásd 1.1.). A kártyaszettek közül a `Z.A-KART-04` élő/runtime tétel — azt a képző
hozza létre a peulán —, ezért nincs benne a 23-ban.

A generált terv ezeken felül még három családra jelöl pilotot: a **H5P-interakció /
Moodle-elem** és a **beszerzendő fizikai eszköz** családra — ezek a BATCH 0-ban állnak,
**már ma gyárthatók**, és nincs szükségük külön briefre —, valamint a **fotó /
képernyőkép** családra. Az aktuális ID-k a terv 5. szakaszában vannak; a
fotó/képernyőkép-családhoz ez a lap nem ad briefet.

> **A gyermekvédelmi és krízis-HOOK-ok nincsenek a P-VID családjában.** A projektgazdai
> döntés szerint (`HUM-MEDIA-03`, 2026-10-02; utólagos ellenőrzés (vétó/QA): a
> jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna) az `M2.4-VID-01`, az
> `M3.3-VID-01` és az `M3.4-VID-01` nem beszélőfej, hanem hangalámondás + tipográfia/grafika (`explainer`). A P-KAR sem méri őket — a generált terv
> az `explainer` altípust a karakter-/jelenetvideó családba sorolja —, és ez a lap nem ad
> hozzájuk briefet.

### 1.1. Miért tért el három tétel a terv 2026-08-28-i javaslatától

A terv szabálya — „a legkevesebb nyitott kapuval bíró tételek közül a medián hosszúságú
specifikációjú” — **kapu-optimalizál**. Egy pilotnak viszont a **legnehezebb** dolgot kell
bizonyítania a családban, különben a jóváhagyás nem mond semmit a testvérekről.

| Eltérés | A terv akkori választása | Amit ez a lap választ | Miért |
|---|---|---|---|
| **P-KAR** | `M1.1-VID-02` (B-roll klipek) | **`M4.1-VID-03`** | Az `M1.1-VID-02` néma B-roll **szkript nélkül** (`source_ref` üres) és visszatérő karakter nélkül — a család legnehezebb problémáját, a **karakter-azonosságot**, egyáltalán nem méri. Az `M4.1-VID-03` viszont szó szerinti jóváhagyott narrációhoz kötött (`M4.1-NAR-03-VO`), és a háromjelenetes sorozat első darabja, amelyből az `M4.1-FOTO-01` freeze-frame-je készül — annak specifikációja szó szerint **„ugyanaz a madrih”**. Ez teszi a karakter-azonosságot bizonyítható elfogadási feltétellé. **Ára: egy kapuval több (R2 is ül rajta).** *(Azóta az `M1.1-VID-02` is R2 alatt áll, így a kapuszám azonos.)* |
| **P-IKO** | `M0.1-IKO-01` (egyetlen ikon) | **`M1.3-IKO-01`** (SBI 3-elemű készlet) | Az `M0.1-IKO-01` **egy darab** ikon; a család neve viszont *ikon-készlet*, és a stílus-token igazi kérdései (készlet-konzisztencia, vonalvastagság, szemantikus szín + forma-redundancia, az R6 ütközés) egy magányos ikonon nem jelennek meg. Az `M1.3-IKO-01` mindhármat egyszerre méri, ráadásul **visszatérő asset**: az `M1.4-IKO-01` `reuse_of`-fal rá mutat, és az `M1.3-DIA-01/02/03` is használja. Azonos kapuszám (R5). Az `M0.1-IKO-01` **kísérő-tételként** ugyanabban a körben legyártható, közel nulla többletköltséggel. |
| **P-KRT** | *(a terv a posztert és a kártyaszettet egy családként kezeli)* | **`M5.A-KART-01`** *(kiegészítés, nem csere)* | Az `M7.B-POSZ-01` flipchart-sablon: se kétoldalas nyomtatást, se vágóívet, se az AI-címkét nem teszteli (a `provenance` mezője `human`). A kártyaszett-alcsalád **23 asset**, és a saját produkciós nehézsége — 12 kártya, A4-enként 2–4 db, kétoldalas illesztés — sehol máshol nem jelenik meg. |

---

## 2. Kapu-mátrix — mit kell jóváhagyni, mielőtt egy pilot elindul

**Ez a lap legfontosabb táblázata.** Egyetlen pilot sem gyártható „most”, kivéve ha itt
üres a jobb oldal.

| Pilot | Mire vár | Ki oldja fel |
|---|---|---|
| P-DIA, P-IKO, P-ILL, P-MUN, P-POS, P-KRT | **D1** (stílus-token + paletta) — **lezárva** (projektgazdai döntés, 2026-10-02); hátravan az asset-szintű R5-blokkoló kivezetése | a projektgazda döntött; utólagos ellenőrzés (vétó/QA): a kreatív/márkafelelős |
| P-NAR | a **D2 lezárult** (projektgazdai döntés, 2026-10-03): a kanonikus narrátorhang, a modell, a beállítások és a kiejtési szótár rögzítve ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12.). Mellette **D3/R2**: a hanghasználati jog tartalmilag tisztázott (VO D-01), a formális bizonyíték (R2-4/R2-5) függő. A tömeges gyártás előtt a QA-láncnak (kiejtés-regresszió, időkeret-ellenőrzés) zöldnek kell lennie | a P-NAR jóváhagyása fülre: magyar anyanyelvű, someres szóhasználatot ismerő jóváhagyó; a formális hangjog-bizonyítékról a jogi jóváhagyó és a hang jogosultja |
| P-VID | a **kész ElevenLabs hangmester** (tehát P-NAR) → **D3/R2** (a fiók jogi bizonyítéka) — és a **J2/J3** emberi kapuk | + jogi jóváhagyó; a J2-nél a Memuna (gyermekvédelmi felelős) és a szerző — felelős és bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. |
| P-KAR | **D1** (karakter-lock; a stílus 2026-10-02 óta eldőlt, a referencia-karakter és a seed rögzítése a gyártás első lépése) + **D3/R2** — és a **J1/J2** emberi kapuk. A **D2** csak az utómunkához kell, a képi generáláshoz nem (lásd 2.1.) | + jogi jóváhagyó (J1), a Memuna (gyermekvédelmi felelős) és a szerző (J2) — felelős és bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. |

> **A szolgáltatói kérdések lezárultak.** Hang: **ElevenLabs**. Beszélőfej: **HeyGen**.
> Ami maradt, az a jogi bizonyíték (a kanonikus narrátorhang 2026-10-03 óta ki van jelölve, VO D-14) — nem
> szolgáltatóválasztás.

### 2.1. Sorrendi kényszer, ami eddig nem látszott

A két videós pilot **más ponton** függ a hangtól, és ezt érdemes külön tartani:

- **P-VID — generáláskor.** A javasolt beszélőfej-útvonal **feltöltött hangsávval**
  dolgozik: az avatar a mi hangunkra szinkronizál, tehát a hangnak **a generálás előtt**
  készen kell lennie.
- **P-KAR — csak összeállításkor.** A jelenet **némán** generálódik
  (`generateAudio: false`), a karakter nem beszél, szájszinkron nincs. A képi anyag tehát
  **a hangdöntés előtt is legyártható**; a narráció csak az utómunkában kerül alá. Ha a
  hang később változik, **elég a hangsávot cserélni** — a videót nem kell újragenerálni.

Ebből:

```
D1 ──► P-DIA · P-IKO · P-ILL · P-MUN · P-POS · P-KRT   (párhuzamosan)

D2 ──► P-NAR ──► [elfogadott hang] ──► P-VID           (a generáláshoz kell a hang)
                                   └─► P-KAR utómunka   (csak a muxoláshoz kell)

P-KAR képi generálás: D1 karakter-lock + R2 + J1/J2 — a hangtól FÜGGETLEN
```

Ez jó hír a költség szempontjából: a beszélőfej-köteg — a drágább, 18 tételes ág — addig
nem indul el, amíg a hang nincs elfogadva, tehát nem kell újragenerálni, ha a hang
változik. A karakter-jelenet képi része viszont párhuzamosítható.

---

## 3. Közös elfogadási feltételek

Minden pilotra érvényes, a családspecifikus feltételeken **felül**.

- [ ] a legyártott anyag **szó szerint** fedi a manifeszt `spec` mezőjét — se több, se kevesebb;
- [ ] beszélt assetnél a hang **szó szerint** a `@source` blokk szövege, és a `source_hash` fel van jegyezve;
- [ ] a kötelező derivatívák elkészültek (`derivatives` mező: felirat / leirat / alt-szöveg / nyomtatható PDF);
- [ ] az akadálymentesítési feltételek teljesülnek (9. szakasz a [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md)-ben);
- [ ] ahol az asset `production_rules` mezőjében szerepel az **R1**, ott a tanulónak látható AI-címke **az LMS-ben, szövegként** jelenik meg — nem a képbe égetve; csak hangot tartalmazó narrációnál a leirat első sora és a lecke alján egy sor (projektgazdai döntés, 2026-10-03, VO D-21). *(A kilenc pilotból nyolcra vonatkozik; az `M7.B-POSZ-01` `provenance` mezője `human`, a szabálylistája nem tartalmazza az R1-et — oda **nem** kerül címke.)*
- [ ] ahol a generátor gépi provenance-jelölést ad, az az exportban **megmaradt** (ellenőrizve, nem feltételezve);
- [ ] a fájlnév a 7. szakasz konvencióját követi;
- [ ] a fekete-fehér nyomtatás olvasható marad (minden nyomtatványra és minden szemantikus vizuálra).

### 3.1. Közös bukási feltételek

Bármelyik teljesülése esetén a pilot **elutasítva**, és a testvér-köteg **nem indul**:

- a szöveg eltér a forrástól (akár egy szóban);
- a jelentés kizárólag színnel van jelölve;
- a magyar ékezet hibás vagy hiányzik (`ő`, `ű`, `í` — generált képben ez a leggyakoribb);
- égetett AI-címke vagy égetett felirat;
- a gépi provenance-jelölés eltűnt az exportból;
- valós, azonosítható személyre hasonlító alak;
- kiskorúnak látszó szereplő (lásd a **J2** emberi kaput);
- a kontraszt bármely szöveg–háttér páron 4,5:1 alatt (nagy szövegnél 3:1 alatt).

---

## 4. P-NAR — narráció · `M4.2-NAR-03`

| | |
|---|---|
| **Cím** | Slide 3 narráció – Dialog Cards felvezetés |
| **Modul / egység** | M4 / M4.2 |
| **Státusz · kapuk** | `jogtisztázás alatt` · **R2, R3** |
| **Forrás** | `M4.2-NAR-03-VO`, `02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md` (deklaráció: 513. sor) · hash `ce6604de9226b73d` |
| **Cél** | bevezeti és keretezi a Dialog Cards aktivitást |
| **Közönség** | madrih, jellemzően 15+ |
| **Hossz** | kb. 17–22 mp · **43 szó**; a kanonikus narrátorhang mért természetes hossza 18,9 mp (≈ 137 szó/perc) — a keretben (VO D-13: a várható hossz a mért természetes hossz) |
| **Deriváltak** | `::CAPTIONS` (felirat), `::TRANSCRIPT` (leirat) |
| **Stílusfüggés** | nincs |
| **Hangfüggés** | a kanonikus narrátorhang (VO D-14); a pilot a produkciós konfigurációt ellenőrzi |
| **Jogi függés** | **R2** (R2-4/R2-5) — a felmondás 2026-08-28 óta szintetikus, ezért az R2 a narrációra is kiterjed ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1. szakasz) |

### Miért ez a pilot

A generált terv 2026-08-28-i választása: az akkori narráció-család **medián esete** —
közepes hossz, tiszta instrukciós regiszter, egyetlen félkövér kiemeléssel, mozgalmi
szakszóval (`hanih`). Aki ezt jól mondja fel, a 89-ből 80-at jól mond fel.

> **Fontos:** a P-NAR a **családi** pilot, és a 2026-10-03-i projektgazdai döntés szerint is ez
> marad (VO D-13), akkor is, ha a generált terv narráció-pilotja más. A kiejtés kanonikus döntési
> forrása a VO QA-repó B4-regisztere; a P1–P3 ([`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md))
> és a P-NAR ezeket produkciós környezetben ellenőrzi, nem dönt újra. Hangválasztás nincs: a
> narrációt a kanonikus narrátorhang mondja (VO D-14). Sorrend: **zöld QA-lánc → P1–P3 és P-NAR a kanonikus narrátorhanggal →
> a narrációs köteg.**

### Gyártási brief — **ElevenLabs**, a 2026-10-03-i konfiguráció

- **Motor:** `eleven_v4`, `language_code: "hu"` (projektgazdai döntés, 2026-10-03, VO D-02) —
  a magyar olvasat kikényszerítése kötelező, enélkül a someres szavak angol vagy héber
  fonetikát kaphatnak.
- **Hang:** a **kanonikus narrátorhang** (VO D-14). A voice-ID nem nyilvános: a VO QA-repó
  gyártási konfigurációjában él, a kurzusrepóban nincs (K3).
- **Bemenet:** a `@source` blokk szövege **tisztítva** — a `„ ”` határoló idézőjel nélkül, a
  `**…**` jelölés eltávolítva, emoji nélkül, szögletes zárójel nélkül; a kiejtés célzott
  cseréi (tts_text) csak a hang bemenetében élnek ([`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) 2.1.).
- **Tempó:** a v4-en nincs `speed`; a hossz a mért természetes hossz (kb. 17–22 mp). A szünetet
  a központozás adja; a sortörés és az üres sor nem szünetvezérlő, a bekezdéshatáron szükség
  szerint az utómunka tesz kb. 0,6–1,0 mp-et (VO D-10).
- **Beállítások:** minden kérésben **explicit** `stability` 0,35 és `similarity_boost` 0,75,
  plusz rögzített `seed`; `style`, `use_speaker_boost` és `speed` nincs (VO D-02). A tárolt
  beállításra hagyatkozni tilos; a ténylegesen elküldött értékeket a kísérőadat rögzíti.
- **Kiejtés:** a kanonikus kiejtési szótár rögzített verziójával (`ulYxuUbd8aSRJ89Pv2Q8` /
  `VFpQiiOF789b08uzsooM`, VO D-03): `hanih` → [xanix], a B4 szerint
  ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 6.).
- **Export:** `pcm_48000` → 48 kHz / 16 bit / mono WAV-mester (VO D-12) → MP3 derivatíva a
  Moodle/H5P-hez.
- **Felirat-időzítés:** érdemes a szolgáltató **karakterszintű időbélyeget** adó
  végpontját kipróbálni. A felirat **szövege így is a lecke marad** — a végpont csak az
  időzítést adja.

### Elfogadási feltétel

- [ ] a felmondás szó szerint a forrásszöveg;
- [ ] hossz kb. 17–22 mp között, gyorsítás és időnyújtás nélkül (VO D-13, D-17);
- [ ] `hanih` a B4 szerinti [xanix] hangzással (VO D-04);
- [ ] a jelentést hordozó hangsúly nem sérül (fülre) (VO D-11);
- [ ] tegező, egyenrangú, nem tanáros;
- [ ] tiszta beszéd, háttérzaj nélkül;
- [ ] a `.vtt` (archivált derivatíva, VO D-19) időzítése a hanghoz igazítva, szövege a forrással azonos;
- [ ] a leirat első sora a kanonikus AI-címke, és a lecke alján ugyanez áll egy sorban (VO D-21);
- [ ] a leirat a dián vagy a médiaelem mellett látható szövegként illeszthető be (VO D-19;
      a Course Presentation diáinak nincs jegyzetmezője — `LMS – hozzáférhetőségi sztenderd.md`); a billentyűzetes és
      képernyőolvasós elérhetőséget az `LMS – H5P runtime acceptance.md` szerinti teszt igazolja;
- [ ] a hang nem indul el magától: a lejátszást a tanuló indítja (H5P Audio: „Enable autoplay” kikapcsolva; projektgazdai döntés 2026-10-03-B, IMPL-34).

### Bukási feltétel

Bármely szóeltérés a forrástól · a 22 mp túllépése gyorsítással vagy időnyújtással kompenzálva ·
a B4-ben elvetett `hanih`-olvasat (kerekített „honih”) · magázó vagy gyerekhangú felmondás · hallható zaj, szuszogás, vágásnyom.

---

## 5. P-VID — AI beszélőfej · `M5.1-VID-01`

| | |
|---|---|
| **Cím** | nyitó beszélő fej – suli / Somer / hétköznapok |
| **Modul / egység** | M5 / M5.1 |
| **Státusz · kapuk** | `jogtisztázás alatt` · **R2, R3** |
| **Forrás** | `M5.1-VID-01-VO`, `02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md` (deklaráció: 151. sor) · hash `a461ce6828fbc62c` |
| **Cél** | azonnali érzelmi bevonás; a három tanulási kategória ráhangoló bevezetése |
| **Arány / hossz** | **16:9**, max. 40 mp · **63 szó** → 110 szó/percen 34,4 mp |
| **Deriváltak** | `::VOICEOVER`, `::CAPTIONS`, `::TRANSCRIPT` |
| **Alt-szöveg** | csak a **képi sáv** (beszélő fej) dekoratív: hangalámondás nem kell (WCAG 2.2 SC 1.2.5), mert a narrációt a felirat és a leirat szó szerint lefedi; a videóelemet a dián látható, leíró videócímke azonosítja (SC 1.1.1), a lejátszó nem rejtett a segédtechnológia elől |
| **Kísérő asset** | `M5.1-EGY-01` — a tanulónak látható R1-címke, **LMS-szövegként** |

### Miért ez a pilot

A 18 beszélőfej **modális esete**: HOOK-videó, közepes hossz, egy szereplő, kamerába
beszél. A generált terv 2026-08-28-i választása. A testvér-köteg a gyermekvédelmi és
krízis-HOOK-okat nem tartalmazza (1. szakasz): ezekhez a projektgazdai döntés szerint
készlet-AI-beszélőfej nem készül.

### Gyártási brief — **HeyGen** (felhasználói döntés, 2026-08-28)

A hang **nem itt készül**: a kanonikus hangmestert az ElevenLabs állítja elő a lecke
`@source` szövegéből, a HeyGen csak a képi/szájszinkron fázist végzi.

| | |
|---|---|
| **Szolgáltató** | **HeyGen** — a választás lezárva, nem tárgya ennek a briefnek |
| **Hang** | **feltöltött ElevenLabs hangmester, a kanonikus narrátorhanggal** (VO D-20). A HeyGen saját TTS-e **nincs használatban** — a séma ezt kikényszeríti: a `script` és az `audio_url` / `audio_asset_id` mező **kölcsönösen kizárja egymást** |
| **Avatar** | **egyetlen nyilvános készlet-avatar** (`studio_avatar`, `ownership=public`), amely minden beszélőfej-videóban visszatér. A készlet-avatar **képmás-licencét a szolgáltató feltételei szerint dokumentálni kell** (`HUM-MEDIA-03`, R2-3; [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) H-3). Egyedi „digital twin” avatarhoz hozzájárulási lánc kell, és annak API-s létrehozása enterprise-szintű |
| **Megjelenés** | **egyértelműen felnőtt** — ez nem stílus, hanem szabály: a szolgáltató moderációs politikája tiltja a 18 év alattinak látszó avatart (lásd a J2 kaput). Semleges, hétköznapi öltözet; nem tanáros, nem céges |
| **Keretezés** | mellkép, tekintet a kamerába; a fej a felső harmadban, a cím-biztonságos zónán belül |
| **Háttér** | egyszínű felület a palettából, vagy semleges világos háttér. **Védjegy-semlegesség (R4):** nem utánozhatja a Messenger / WhatsApp / Discord / Insta / Moodle vizuális nyelvét |
| **Felirat** | **nem égetett.** A `.vtt` felirat a lecke `@source` szövegéből készül, **nem** a szolgáltatóétól. A videógenerálás felirat-beállítása amúgy is **csak SRT-t** ad (a formátum-felsorolásban egyetlen érték szerepel), és beszédfelismerésből származik — a szolgáltatói felirat legfeljebb keresztellenőrzés. *(A szolgáltató máshol, a videó-fordítás funkciójában ad VTT-t is; az viszont nem ez az útvonal.)* |
| **Export** | MP4, **16:9**, 1080p. Az arányt **explicit** kell megadni, mert az `auto` az avatar forrásképéből vezeti le |

#### A gyártási lánc — három lépés

```
1.  hangmester feltöltése         → asset-azonosító (MP3 vagy WAV, ≤ 32 MB)
2.  videó létrehozása             → az avatar-azonosító + a feltöltött hang azonosítója
                                    (a szöveges szkript-mező üresen marad!)
                                    arány = 16:9, felbontás = 1080p, motor explicit
3.  állapot lekérdezése           → kész videó letöltése és ARCHIVÁLÁSA
```

A letöltési link **ideiglenes** — a kész MP4-et azonnal a saját tárolóba kell menteni.
A szolgáltató nem archívum.

> ⚠️ **Nem dokumentált, ezért a pilotnak kell eldöntenie:** hogy a kimeneti MP4 a
> feltöltött hangot **változatlanul** viszi-e tovább, vagy újrakódolja. A szolgáltatói
> dokumentáció erről hallgat. A pilot elfogadásának ez mérhető feltétele (lásd lent).

### Negatív megkötések

Nincs égetett szöveg · nincs égetett AI-címke · nincs zenei aláfestés · nincs
márkázott UI-elem · nincs valós személyre hasonlító arc · nincs kiskorúnak látszó
szereplő · nincs kameramozgás vagy zoom-effekt.

### Elfogadási feltétel

Az első hét pont **a pilot négy nem dokumentált kérdését méri** — ezekre a szolgáltatói
dokumentáció nem ad választ, csak egy tényleges renderelés.

- [ ] a **magyar szájszinkron** a feltöltött hangra hihető — a szolgáltató a
      szájszinkront a hanghullámból vezeti, nyelvi listája ehhez nincs; *ez a pilot
      elsődleges kérdése*;
- [ ] **a kimeneti hang a feltöltött ElevenLabs mester** — mérve, nem feltételezve:
      a kimenetből kinyert hangsáv kodekje és mintavétele rögzítve, és a mesterrel
      null-teszttel összevetve. Ha újrakódolás történik, azt **dokumentálni kell**, és el
      kell dönteni, elfogadható-e;
- [ ] **gépi provenance:** a kész MP4-et meg kell vizsgálni, van-e benne
      C2PA / Content Credentials jelölés. A szolgáltató dokumentációja **sehol nem állítja,
      hogy beágyaz ilyet** — csak egy szabványügyi kezdeményezésben való tagságot említ.
      Ha nincs jelölés, az R1 gépi ága itt tárgytalan; ha van, az exportnak meg kell
      tartania. **Feltételezni egyiket sem szabad;**
- [ ] **nincs vízjel** a fizetős renderen — a dokumentáció a vízjelmentességet a fizetős
      csomaghoz köti, de kifejezetten nem mondja ki; ellenőrizendő;
- [ ] 16:9 és 1080p, ≤ 40 mp, 25 fps;
- [ ] az avatar újrahasználható a további 17 videóhoz **ugyanazzal az azonosítóval**;
- [ ] a moderáció **átengedi** a tananyag hangvételét — a szolgáltató automatikus
      moderációt futtat, és a politikai tartalom tiltott kategória; egy mozgalmi-ideológiai
      keretezésű HOOK elakadhat rajta. Ezt is a pilot deríti ki;
- [ ] a `.vtt` felirat **a lecke `@source` szövegéből** készült, nem a szolgáltató
      SRT-kimenetéből;
- [ ] az alsó 15%-ban nincs grafika;
- [ ] az R1-címke az LMS-ben, szövegként jelenik meg (`M5.1-EGY-01`);
- [ ] a videó nem indul el magától: a lejátszást a tanuló indítja („Auto-play video” kikapcsolva; projektgazdai döntés 2026-10-03-B, IMPL-34).

### Bukási feltétel

Rossz vagy „idegen nyelvű” szájmozgás · a szolgáltató saját TTS-e szólal meg a feltöltött
hang helyett · a hangmester felismerhetően romlik az újrakódolástól · égetett felirat vagy
címke · watermarkos kimenet · az avatar nem rögzíthető újrafelhasználásra · a moderáció
elutasítja a tartalmat.

> ⚠️ **Reprodukálhatósági kockázat, amit a pilot nem old meg.** A szolgáltató
> avatar-leíró rekordjában **nincs verzió-mező**: az avatar megjelenése nem rögzíthető
> egy adott változatra, és a szolgáltató a motorok viselkedését menet közben változtatja.
> Ebből következő produkciós szabály: **a 18 beszélőfej-videót egyetlen szűk időablakban
> kell legyártani**, nem hónapokra elosztva, és minden kész MP4-et archiválni kell.
> Egy év múlva egyetlen klip újragyártására nincs garancia, hogy ugyanaz az arc jön
> vissza.

---

## 6. P-KAR — AI karakter-jelenet · `M4.1-VID-03`

| | |
|---|---|
| **Cím** | Jelenet 1 karaktervideó – „Jegyzetbe bújó madrih” |
| **Modul / egység** | M4 / M4.1 |
| **Státusz · kapuk** | `jogtisztázás alatt` · **R2, R3, R5** |
| **Forrás** | `M4.1-NAR-03-VO`, `02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md` (deklaráció: 748. sor) · hash `a251aced0d05df02` |
| **Hossz** | 20–25 mp, teljes alakos jelenet |
| **Konténer** | beágyazva az `M4.1-VID-02` H5P Interactive Videóba (`composed_of`) — a felirat és a leirat **a konténeré**, nem ezé |
| **Származék máshol** | az `M4.1-FOTO-01` freeze-frame-je ebből és az `M4.1-VID-05`-ből készül |
| **Akadálymentesítés** | jelenetvideó: a testbeszéd hordozza a jelentést, ezért a képi sáv nem dekoratív, és hangalámondásos képleírás, mellette szöveges alternatíva kell (projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a hozzáférhetőségi felelős és a médiafelelős). A formáját a lecke `a11y` mezője rögzíti |

### A szó szerinti narráció (másolat, nem kánon)

> „Nézd meg ezt a madrihot.
> A papírra koncentrál, a válla kicsit beesik,
> a tekintete szinte végig lefelé van.
>
> Ha hanih lennél,
> mennyire éreznéd azt, hogy **neked beszél**,
> és mennyire azt, hogy inkább a lapja mögé próbál bújni?”

A karakter **nem beszél** — a narrátor beszél róla harmadik személyben. Ez a jelenet
teljes hangfeladata.

### Miért ez a pilot

Mert ez a család **egyetlen valódi nehézsége**: a három jelenetben ugyanannak az embernek
kell látszania, és az `M4.1-FOTO-01` specifikációja ezt szó szerint kimondja
(„ugyanaz a madrih karba tett kézzel vs. nyitott kézzel”). Egy pilot, amely nem méri a
karakter-azonosságot, nem mond semmit a testvéreiről.

### Gyártási brief — javasolt stack

**1. lépés — karakter-lock (a videó előtt).** Referenciakép-készlet generálása
képgenerátorral; a dokumentáció **legfeljebb 5 referenciaképet** enged a
karakter-konzisztenciához:

```
CONTENT      Egyetlen fiatal felnőtt ifjúsági vezető alakja, semleges álló
             testtartásban, semleges hétköznapi öltözetben (egyszerű póló, farmer).
             Teljes alak, majd mellkép, majd háromnegyedes profil — ugyanaz a személy.
COMPOSITION  Semleges világos háttér, egyenletes megvilágítás, a teljes alak látszik,
             a kéz és a váll pozíciója tisztán kivehető.
STYLE        Lapos vektoros illusztráció, egyszerűsített arc, egyenletes kontúr.
             Nem fotorealisztikus, nem 3D-render, nem festői.
BRAND        Háttér és ruházat kizárólag a jóváhagyott palettából; kontúr #1D1D1B.
TEXT         Nincs szöveg a képen.
A11Y         A testtartás a kontúrból is kiolvasható legyen, szín nélkül.
NEGATIVE     Nincs valós, azonosítható személyre hasonlítás. Nincs kiskorúnak látszó
             alak. Nincs vallási öltözet. Nincs márkajelzés, logó, felirat.
             Nincs színátmenet, nincs árnyékhatás, nincs textúra.
OUTPUT       PNG, min. 2048 px hosszabb él, átlátszó vagy egyszínű háttér.
```

A referenciakészlet **verziókövetve** kerül a `media/source/` alá, mert a többi öt jelenet
ugyanebből dolgozik.

**2. lépés — jelenet-generálás.**

| Paraméter | Érték |
|---|---|
| Bemenet | a rögzített referenciakép **első képkockaként** + legfeljebb 3 referenciakép |
| Hang | **`generateAudio: false`** — néma generálás; a narráció utómunkában kerül alá |
| Seed | rögzített; a prompt-átíró funkció **kikapcsolva** (különben a seed nem determinál) |
| Kameraállás | statikus, szemmagasság, teljes alak; nincs kameramozgás |
| Mozgás | minimális: a válltartás előreesik, a tekintet lefelé, a papírt tartó kéz kissé megemelkedik. **A testbeszéd a tartalom** — nem díszlet |
| Fény | egyenletes, lágy, nem drámai |
| Arány / felbontás | **16:9, 1920 × 1080** — azonos a beszélőfej-pilottal, hogy a H5P Interactive Video konténerben ne váltson formátumot |
| Klipek | **3 db 8 mp-es felvétel**, egymás után vágva → 24 mp, ami a 20–25 mp-es keretbe esik. Illesztés kemény vágással, áttűnés nélkül; a kameraállás mindhárom klipben azonos, hogy a vágás ne olvasódjon jelenetváltásnak |

**3. lépés — utómunka.** A P-NAR-ban elfogadott hanggal felmondott `M4.1-NAR-03-VO`
narráció a néma jelenet alá; a felirat és a leirat **az `M4.1-VID-02` konténerhez**
készül, nem ehhez a jelenethez. A freeze-frame-et képkocka-kivétellel vesszük ki.

### Elfogadási feltétel

- [ ] a karakter felismerhetően **ugyanaz**, mint a referenciakészleten;
- [ ] a jelenet **három párja** (`M4.1-VID-03/04/05`) egymás mellé téve ugyanazt az embert mutatja — *ez a család valódi próbája*;
- [ ] a testbeszéd egyértelműen olvasható: előreeső váll, lefelé néző tekintet, papír mögé bújás;
- [ ] a videó **néma**;
- [ ] a narráció alámuxolva, szinkronban;
- [ ] a referenciakép, a prompt és a seed rögzítve és verziókövetve;
- [ ] a freeze-frame kivehető, és a képpár testtartás-kontrasztja látszik;
- [ ] a képi sáv hangalámondásos képleírása és szöveges alternatívája a lecke `a11y` mezője szerint elkészült;
- [ ] a gépi provenance-jelölés megmaradt.

### Bukási feltétel

A karakter jeleneteként más ember · kiskorúnak látszó alak · a modell kitalált nyelven
beszélő szájmozgást ad · nem reprodukálható a seed/referencia rögzítése után · valós
személyre hasonlítás · a testtartás nem olvasható ki a képből.

> ⚠️ **EMBERI DÖNTÉS — nyitott szerzői hiány, amit ez a brief nem tölt ki.** Az
> `M4.1-FOTO-01` specifikációja **karba tett kezet** kér („ugyanaz a madrih karba tett
> kézzel vs. nyitott kézzel/felsőtesttel”), de ezt a testtartást **egyik
> jelenet-specifikáció sem tartalmazza**: az `M4.1-VID-03` „előreeső vállak, papírba
> mélyed”, az `M4.1-VID-04` „lábról lábra billeg”, az `M4.1-VID-05` „laza vállak”. A
> freeze-frame maga sem nevez meg jelenetet, csak annyit, hogy „az IV-videókból”.
> **A szerzőnek kell megmondania, melyik jelenet viszi a karba tett kezet — vagy hogy a
> képpár másik testtartás-kontrasztra épül.** Amíg ez nyitva van, a P-KAR jóváhagyható,
> az `M4.1-FOTO-01` viszont nem gyártható le.

> ⚠️ **A P-KAR nem indítható a `J1` és a `J2` emberi kapu megválaszolása előtt** —
> [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.3.; a felelős és a bizonyíték: 1/A.5.

> ⚠️ **A P-KAR elfogadása két testvérre nem vihető át.** Az `M1.3-VID-01` kétszereplős,
> képernyőn zajló párbeszéd: a „videó néma” feltétel és a néma generálás rá nem
> alkalmazható; a hangja az első gyártási körben Madrih A-nál a kanonikus narrátorhang, Madrih B-nél a
> második hang (a kalibrálása után), beszélőnként szegmentálva (VO D-14, K4), a szájszinkronos gyártási útja nyitott döntés
> ([`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D11). Az `M1.1-VID-02` B-roll
> („körben ülő fiatalok”) a 3.1. „kiskorúnak látszó szereplő” bukási feltételébe ütközhet;
> az ábrázolás módja a `J2` emberi döntése.

---

## 7. P-DIA — diagram · `M0.2-DIA-01`

| | |
|---|---|
| **Cím** | SLIDE 4 jelzési folyamatábra: az ötlépéses jelzési út (észreveszem → meghallgatom → nem nyomozok → bevonom a Memunát → közvetlen veszélynél 112) |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Cél** | a „madrih, nem terapeuta” logika egyetlen lineáris jelzési útvonalként; megerősíti, hogy a madrih nem egyedül old meg, hanem jelez |
| **Deriváltak** | `::ALTTEXT` |

### Miért ez a pilot

A terv 2026-08-28-i választása: a 39 diagram **modális szerkezete** (lineáris, számozott
lépéssor), és ráadásul gyermekvédelmi tartalmú — a legláthatóbb hely, ahol az olvashatóság
számít.

### Gyártási brief — **determinisztikus SVG, nem generatív**

Öt csomópont, nyilakkal — az ötlépéses jelzési út (`HUM-SAFE-01`; projektgazdai döntés,
2026-10-02; utólagos ellenőrzés (vétó/QA): a Memuna), a lecke SLIDE 4 szövegével:
**1)** Észreveszem, és komolyan veszem · **2)** Meghallgatom, és nem ígérek teljes
titoktartást · **3)** Nem nyomozok, nem konfrontálok, és nem próbálom egyedül megoldani ·
**4)** Azonnal bevonom a kijelölt Memunát (összeférhetetlenség esetén a név szerint
kijelölt helyettesét) · **5)** Közvetlen veszélynél előbb a biztonság és a 112, utána a
belső jelzés.

| | |
|---|---|
| **Elrendezés** | balról jobbra; **mobilon felülről lefelé** |
| **Két arány-változat** | `__master-wide.svg` (asztali) és `__master-tall.svg` (mobil) — egy deliverable, két export |
| **Tipográfia** | csomópont-cím ≥ 17 px, alcím ≥ 14 px effektív méret 1× renderelésen; 320 px széles nézetben is olvasható |
| **Szín** | doboz-kontúr és szöveg `#1D1D1B`; opcionális márkaszín-felület a doboz mögött; a sorszám a szín nélkül is jelöli a sorrendet |
| **Forma** | derékszögű doboz, 5 pt-nek megfelelő arányos sarok-lekerekítés; görbe vonal nincs |
| **Animáció** | **opcionális** — a statikus változat önmagában megfelel |
| **Akadálymentesítés az SVG-ben** | `<title>` és `<desc>` elem; a `::ALTTEXT` deliverable a lépések sorrendjét mondja el |

### Elfogadási feltétel

- [ ] az öt csomópont szövege szó szerint a lecke SLIDE 4 szakaszának lépéseivel (a **„Vizualitás”** folyamatábra és a **„Szöveg a dián”** 1–5. pontja) egyezik;
- [ ] a sorrend a számozásból is kiolvasható, nem csak a nyilakból;
- [ ] 320 px széles nézetben olvasható;
- [ ] fekete-fehérben nyomtatva minden információ megmarad;
- [ ] `<title>` és `<desc>` kitöltve;
- [ ] a két arány-változat ugyanazt a tartalmat viszi.

### Bukási feltétel

A gyermekvédelmi lépéssor bármely eleme kimarad vagy sorrendet cserél · a jelentés csak a
nyilak irányából olvasható · a mobil változat vízszintes görgetést kíván · a szöveg képbe
égetett raszter.

---

## 8. P-IKO — ikon-készlet · `M1.3-IKO-01`

| | |
|---|---|
| **Cím** | SBI vizuális kód ikon-készlet (S / B / I) |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Kísérő-tétel ugyanebben a körben** | `M0.1-IKO-01` (a terv 2026-08-28-i pilotja) — egyetlen ikon, közel nulla többletköltség |
| **Deriváltak** | `::ALTTEXT` |

### Miért ez a pilot

Ez az egyetlen tétel, amely **egyszerre** méri a készlet-konzisztenciát, a szemantikus
szín + forma redundanciát és az R6 ütközést. Ráadásul **visszatérő asset**: az
`M1.4-IKO-01` `reuse_of`-fal rá mutat, és az `M1.3-DIA-01/02/03` grafikái, valamint az
`M1.3-VID-01` ikon-overlay-ei is ezt használják — egyetlen jóváhagyás a legtöbb
downstream tételt oldja fel.

### Gyártási brief

Három elem, a lecke által rögzített szerepekkel:

| Elem | Szerep | Ikonmetafora (a lecke szerint) | Javasolt márkaszín |
|---|---|---|---|
| **S** | Situation | óra + helyszín(pin) | sötét kék `#08A0CA` |
| **B** | Behavior | szem / fül | sötét zöld `#369D37` |
| **I** | Impact | szív / hullám | piros `#D84C15` |

| | |
|---|---|
| **Stílus** | vonalas (outline), 24 × 24 tervezőrács, vonalvastagság 2/24, lekerekített végződés és csatlakozás |
| **Kontúr** | `#1D1D1B` — a márkaszín a kontúr **mögötti** felület, nem maga a vonal |
| **Kötelező redundancia** | mindhárom ikonon ott az `S` / `B` / `I` betűjel, és mindhárom sziluettje eltér |
| **Formátum** | SVG mester; PNG derivatíva átlátszó háttérrel, ≥ 64 × 64 px, retina-méret |
| **Készlet-konzisztencia** | azonos optikai súly, azonos rácsigazítás, azonos margó a 24-es dobozon belül |

**Produkciós mód.** Az asset `provenance` mezője `ai` — az ikon-koncepció AI-generált
alapból indul, a **legyártott fájl viszont tisztított, rácsra igazított SVG**. Ez azért
kell, mert három ikonnak azonos vonalvastagságúnak és optikai súlyúnak kell lennie, amit
generálás önmagában nem ad. **Ha a jóváhagyó úgy dönt, hogy a készlet teljesen kézzel
rajzolt, az a `provenance` mező megváltoztatását jelentené** — az önálló, tudatos
manifeszt-művelet, nem ennek a pilotnak a hatásköre.

### Elfogadási feltétel

- [ ] mindhárom ikon felismerhető **64 × 64 px-en**;
- [ ] **100%-ban szürkeárnyalatosra konvertálva is megkülönböztethetők** — a mért paletta miatt ez nem opcionális;
- [ ] az `S` / `B` / `I` betűjel mindegyiken ott van;
- [ ] azonos vonalvastagság és optikai súly;
- [ ] átlátszó háttér, SVG mester;
- [ ] a `::ALTTEXT` mindhárom ikonhoz megnevezi a szerepet **és** a formát (pl. „S – óra és helyszín ikon”).

### Bukási feltétel

Az ikonok csak színben térnek el · eltérő vonalvastagság a készleten belül · 64 px-en
összefolyik · hiányzó betűjel · nem átlátszó háttér.

---

## 9. P-ILL — illusztráció · `M4.2-ILL-01`

| | |
|---|---|
| **Cím** | Hook chat-buborék: ideges peula-mondat |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Cél** | beránt egy ismerős helyzettel; érzelmileg azonnal bekapcsol |
| **Arány** | **4:5 álló** (1638 × 2048 px), mobilnézetre, középre helyezve |
| **Deriváltak** | `::ALTTEXT` |

### Miért ez a pilot

A terv 2026-08-28-i választása — de van egy külön érdeme: **ez az egyetlen illusztráció-pilot,
amelynek a tartalma egy magyar mondat**. Ezért ez méri a leggyakoribb generatív hibát
(elrontott ékezet) **és** a javasolt megoldást egyszerre.

### Gyártási brief — kétrétegű, ez a lényeg

**A generátor a jelenetet rajzolja, a szöveget nem.**

```
CONTENT      Egy telefonképernyő-szerű, semleges üzenetbuborék egy egyszerű asztali
             jelenetben: telefon, egy kéz, esti hangulat. A buborék ÜRES.
COMPOSITION  Álló arány, mobilnézetre. A buborék a kép közepén, körülötte levegő,
             hogy a szövegréteg utólag beleférjen.
STYLE        Lapos vektoros illusztráció, egyszerűsített formák, egyenletes kontúr.
             Hangulat: ismerős, hétköznapi feszültség — nem drámai, nem vicces.
BRAND        Felületszínek a jóváhagyott palettából; kontúr és részletek #1D1D1B.
             Színátmenet nincs.
TEXT         SEMMILYEN SZÖVEG A KÉPEN. A buborék üresen marad.
A11Y         A buborék belseje egyszínű, hogy a ráhelyezett szöveg elérje a 4,5:1-et.
NEGATIVE     Nincs Messenger / WhatsApp / Discord / Insta / Moodle felületmásolat (R4).
             Nincs márkajelzés, nincs valós alkalmazás-ikon, nincs olvasható arc.
             Nincs generált betű, számjegy vagy írásjel sehol a képen.
OUTPUT       PNG, min. 2048 px hosszabb él, 4:5 álló arány (1638 × 2048).
```

**Szövegréteg — determinisztikusan, SVG-ben:**

> „Nagyon ideges vagyok, hogy holnap peulát kell tartanom…”

| | |
|---|---|
| **Szedés** | a jóváhagyott törzsbetűtípus (Source Sans 3 — D1, B változat), balra zárt, a buborékon belül keskeny margóval |
| **Kontraszt** | a mondat és a buborék-felület között **≥ 4,5:1** — mérve, nem becsülve |
| **Kimenet** | a végleges mester **SVG**, amelybe a generált PNG-alap `<image>` elemként ágyazódik, a mondat pedig `<text>` rétegként kerül rá. Így a fájlnév-táblázat `__master.svg` bejegyzése teljesül, és a szöveg **vektoros marad** |

### Elfogadási feltétel

- [ ] a buborék szövege **szó szerint** a lecke mondata, helyes ékezetekkel;
- [ ] a szöveg **vektoros réteg**, nem generált képpont;
- [ ] szöveg–háttér kontraszt ≥ 4,5:1, kiszámolva;
- [ ] nincs védjegyzett felületre emlékeztető elem (R4);
- [ ] a `::ALTTEXT` leírja a buborék tartalmát és a kontextust;
- [ ] az R1-címke az LMS-ben, szövegként.

### Bukási feltétel

Generált betű a képen · hibás vagy hiányzó `ő`/`á` · felismerhető platform-UI · olvasható
arc · a szöveg beleégetve a generált rétegbe.

---

## 10. P-MUN — munkalap · `M6.A-MUNK-02`

| | |
|---|---|
| **Cím** | Képzői ellenőrző lista – „Játék-labor 3 aktuális kvucára” (1 oldalas gyorssegédlet) |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Formátum** | **A4 álló, pontosan 1 oldal**, pipálható checklist |
| **Deriváltak** | `::PRINTPDF` |

### Miért ez a pilot

A terv 2026-08-28-i választása: a 61 nyomtatványos tétel **legszigorúbb formai kényszerével**
(„1 oldalra”), ami a tipográfiai skálát azonnal próbára teszi.

### Gyártási brief — determinisztikus HTML/CSS → PDF

Tartalom: a forrás 5. szekciójának öt pontja — **1)** Meta tiszta · **2)** Játékok
kiválasztva · **3)** Eszközök & tér · **4)** Biztonsági keret a fejben · **5)** Híd az M6.B
játéklaphoz.

| | |
|---|---|
| **Lapméret / margó** | A4 álló; 14 mm fent/balra/jobbra, 12 mm lent; semmi 10 mm-nél közelebb a széphez |
| **Tipográfia** | cím 17–20 pt félkövér; szekciócím 11–13 pt; törzs 10,5 pt / 1,38; jegyzet 8,5 pt; élőláb 7 pt |
| **Jelölőnégyzet** | 4 × 4 mm, 1 pt `#1D1D1B` keret, 0,7 mm sarok |
| **Kézírásos mező** | sorköz ≥ 8 mm, alávonás `--rule` 0,6 pt |
| **Élőláb** | `M6.A-MUNK-02 · v… · Játék-labor 3 aktuális kvucára` balra, oldalszám jobbra |
| **Szín** | nem szükséges. A lap **fekete-fehérben teljes értékű** |
| **Determinizmus** | a build rögzített időbélyeggel fut, hogy két futtatás azonos PDF-et adjon |

### Elfogadási feltétel

- [ ] **pontosan egy** A4 oldal, 210 × 297 mm;
- [ ] mind az öt pont és minden alpont szerepel;
- [ ] fekete-fehér lézernyomtatón teljes értékű;
- [ ] a PDF-nek **szövegrétege** van (kereshető, felolvasható), nem raszter;
- [ ] a magyar ékezetek helyesek (`ő`, `ű`, `í`);
- [ ] a jelölőnégyzetek egyértelműen pipálhatók, kézírásos mérettel;
- [ ] kétszer lefuttatva **azonos** fájl keletkezik.

### Bukási feltétel

Két oldalra csúszik · a törzsszöveg 10 pt alá szorul, hogy elférjen · hiányzó ékezet ·
raszterizált szöveg · szín nélkül értelmezhetetlen elem.

---

## 11. P-POS — poszter · `M7.B-POSZ-01`

| | |
|---|---|
| **Cím** | Flipchart-poszter: „Zmán Kvucá = …” definíció + „AI-határok” |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Provenance** | **`human`** — *nem* AI-generált, ezért **R1-címke nem tartozik hozzá** |
| **Formátum** | nagy flipchart / csomagolópapír; kézzel írt **vagy** nyomtatott-felnagyított; kifüggeszthető |
| **Deriváltak** | `::PRINTPDF` |

### Miért ez a pilot

A terv 2026-08-28-i választása: ez méri a **nagy formátumú, teremből olvasható**
tipográfiát, ami a **37 gyártandó poszter** (38 összesen; 1 `reuse`) közös kényszere.

**Amit viszont NEM mér:** az AI-címke elhelyezését (mert `human` eredetű), a kétoldalas
nyomtatást és a vágóívet. Ezért van külön kártyaszett-pilot (P-KRT), és ezért az AI-címke
elhelyezését a P-ILL és a P-MUN validálja.

### Gyártási brief

Két mező egy lapon vagy két lapon:

1. **„Zmán Kvucá = …”** — konkrét idősáv + kvuca + tér + felelősség; **nem** aznap
   kitalált spontán, cél nélküli program.
2. **„AI-határok”** — **mind a három** ponttal (a lecke 4.1. és 4.2. blokkja — az asset `spec` mezője is ezekre hivatkozik): nincs konkrét hanih-név vagy sztori;
   gyermekvédelmi ügyben a Memunához (a Somer gyermekvédelmi felelőséhez), nem AI-hoz; az
   AI csak ötletel, a felelősség a madrihé.

| | |
|---|---|
| **Leadandó (a pilotra rögzítve)** | **egy A3 álló, nyomtatható PDF**, kétmezős elrendezéssel. Az A2/A1 nagyítás és a kézzel írt flipchart-változat ugyanebből a forrásból származtatható, de **a pilot elfogadása az A3 PDF-en történik** |
| **Olvasási távolság** | a poszter a teremfalon lóg, ezért az elfogadás mércéje **3 méterről olvasható** — ez a pilot rögzítette érték, nem a tananyagból származik |
| **Tipográfia** | A3: cím ≥ 36 pt, törzs ≥ 18 pt · A2: cím ≥ 48 pt · A1: cím ≥ 60 pt |
| **Olvashatóság** | „távolról olvasható”, nagy kontrasztos betűkép — a teremfal hátuljából |
| **Szín** | nem szükséges; a két mezőt keret és tipográfia választja el, nem szín |
| **Kézírásos változat** | a sablon hagyjon kitölthető helyet, hogy a képző a helyszínen írja meg |

### Elfogadási feltétel

- [ ] mindkét mező tartalma szerepel, a forrás megfogalmazásához hűen;
- [ ] a definíció négy eleme (idősáv, kvuca, tér, felelősség) mind ott van;
- [ ] az AI-határok mindhárom kikötése ott van, **gyengítés nélkül**;
- [ ] A3-on 3 méterről olvasható;
- [ ] fekete-fehérben nyomtatva teljes értékű;
- [ ] **nincs rajta AI-provenance címke** (az asset `human` eredetű).

### Bukási feltétel

Az AI-határok bármelyik kikötése lágyul vagy kimarad · a „gyermekvédelmi ügyben a
Memunához, nem AI-hoz” mondat elveszti az élét · a „felelősség” elem úgy olvasható, hogy a
kvuca biztonságáért a madrih egyedül felel (a gyermekvédelmi felelősség a jelen lévő,
18 év feletti felnőtté — a lecke 4.1. blokkja) · nem olvasható teremtávolságból · téves
AI-címke a lapon.

---

## 12. P-KRT — kártyaszett · `M5.A-KART-01`

| | |
|---|---|
| **Cím** | 12 helyzetkártya – kétoldalas szett (front: sztori, hátlap: címke) |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Provenance** | `mixed` |
| **Formátum** | 12 kártya, **A4-enként 2–4 db** a vágási helyhez, **kétoldalas**; nyomtatható PDF |
| **Deriváltak** | `::PRINTPDF` |

### Miért ez a pilot

Kiegészítés a poszter mellé: a kártyaszett-alcsalád **23 asset**, és a saját produkciós
nehézségét — kétoldalas illesztés, vágóív, kézbe vehető olvashatóság — semmilyen más
pilot nem méri.

### Gyártási brief — determinisztikus HTML/CSS → PDF

| | |
|---|---|
| **Előlap** | 1–3 mondatos szituáció-leírás; a szó szerinti szöveg kánoni helye a lecke **„## 6. Melléklet – 12 helyzetkártya – szövegek”** szakasza. Az asset `spec` ugyanerre a stabil szakaszcímre hivatkozik. |
| **Hátlap** | képzői címke `[SULI]` / `[SOMER]` / `[HÉTKÖZNAPOK]` a fogalommal (formális / nonformális / informális) |
| **Kiosztás** | 4 kártya / A4, szaggatott vágóvonal `--rule` színnel |
| **Duplex** | a hátoldal **oszlopsorrendje tükrözött**, hogy a hosszú élű duplex illeszkedjen |
| **Tipográfia** | előlap törzs ≥ 12 pt (a képző felolvassa a teremben); hátlap-címke nagy, verzál |
| **Redundancia** | a hátlapcímke mellé **forma-glif** is kerül (pl. ▣ / ◆ / ●), hogy a három kategória szín nélkül is elváljon |
| **Védjegy-semlegesség (R4)** | ennek az assetnek a szabálylistájában az R4 is szerepel, és a kártyaszövegek említenek platformokat („buszos TikTok”, „Insta/TikTok görgetés”). A **szöveg marad változatlanul**; a kártya viszont **nem** rajzolhat felismerhető alkalmazás-ikont, logót vagy platform-felületet |
| **AI-jelölés (R1)** | az asset `provenance` mezője `mixed`, és a szabálylistája tartalmazza az R1-et → a nyomtatvány élőlábában szövegként ott a kanonikus címke |
| **Élőláb** | kártyánként `M5.A-KART-01 · v… · <sorszám>/12` |

### Elfogadási feltétel

- [ ] mind a 12 kártya szövege szó szerint a **„## 6. Melléklet – 12 helyzetkártya – szövegek”** szakaszból;
- [ ] kétoldalas nyomtatás után az előlap és a hátlap **ugyanazon a kártyán** van;
- [ ] a vágóvonal mentén levágva a szöveg nem sérül (≥ 3 mm belső biztonsági margó);
- [ ] a hátlapcímke szín nélkül is megkülönböztethető;
- [ ] az előlap szövege kézben tartva olvasható;
- [ ] fekete-fehérben teljes értékű;
- [ ] kétszer lefuttatva azonos fájl keletkezik.

### Bukási feltétel

Duplex után elcsúszott hátlap · a vágás beleér a szövegbe · a három kategória csak
színnel különül el · a határeset-kártyák szövege módosul (**több kártya szándékosan
határeset a vitához** — ez nem hiba, nem javítandó).

---

## 13. Jóváhagyási lánc

Nem bürokrácia: mindegyik lépés más hibát fog meg, és mindegyik **olcsóbb** most, mint
egy 100 tételes kötegen.

```
Pilot V0
  → technikai review     — formátum, méret, determinizmus, export
  → arculati review      — stílus-token, paletta, logóhasználat
  → nyelvi review        — szó szerinti egyezés, magyar tipográfia, kiejtés
  → akadálymentesítési review — kontraszt, alt, felirat, fekete-fehér, forma-redundancia
  → V1 elfogadva
  → testvér-köteg indul
```

- **Beszélt asseteknél a nyelvi review meghallgatásos**, nem átiratos.
- **Az akadálymentesítési review-t nem a szerző végzi**, hanem a hozzáférhetőségi felelős
  (accountable: a Ros Hinuh); az élesítés előtti, független második ellenőrzést a
  `HUM-A11Y-01` tételben név szerint megnevezett második ellenőrző végzi
  (`Emberi jóváhagyás szükséges.md`; projektgazdai döntés, 2026-10-02; utólagos
  ellenőrzés (vétó/QA): a programvezető).
- **Nincs 100 tételes köteg elfogadott pilot előtt.** Ez a lap ezért létezik.
- Ha egy pilot bukik, a **családja nem indul** — de a többi család mehet tovább, mert a
  2.1. sorrendi ábra szerint csak a videós ág láncolt.

## 14. Fájlnév-konvenció a pilotokhoz

A teljes konvenció: [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 7. szakasz.

| Pilot | Mester | Derivatíva |
|---|---|---|
| P-NAR | `M4.2-NAR-03__master.wav` | `…__master.mp3` · `…__captions.hu.vtt` · `…__transcript.hu.md` |
| P-VID | `M5.1-VID-01__master.mp4` | `…__voiceover.wav` · `…__captions.hu.vtt` · `…__transcript.hu.md` |
| P-KAR | `M4.1-VID-03__master.mp4` *(néma + alámuxolt narráció)* | `…__alt.txt` · felirat/leirat a konténerhez: `M4.1-VID-02__captions.hu.vtt` |
| P-DIA | `M0.2-DIA-01__master-wide.svg` · `…__master-tall.svg` | `…__master.png` · `…__alt.txt` |
| P-IKO | `M1.3-IKO-01__master.svg` | `…__master.png` · `…__alt.txt` |
| P-ILL | `M4.2-ILL-01__master.svg` | `…__master.png` · `…__alt.txt` |
| P-MUN | `M6.A-MUNK-02__master.html` | `…__print.pdf` |
| P-POS | `M7.B-POSZ-01__master.html` | `…__print.pdf` |
| P-KRT | `M5.A-KART-01__master.html` | `…__print.pdf` |

**Verziószám a mester nevében nincs** — azt a git és a `source_hash` adja. A pilot
jóváhagyási körei alatt `__v0` / `__v1` utótag használható; az elfogadott változat
utótag nélkül kerül a `masters/` alá.

**Placeholder-fájlokat nem hozunk létre előre.**
