# 🧪 Pilot-produkciós csomag

Családonként **egy** tétel készül el először, és azt kell jóváhagyni, mielőtt a testvérei
elindulnak. Ez a lap minden pilothoz megadja, amit a gyártáshoz tudni kell: a pontos
forrást, a stílusfüggéseket, a promptot vagy elrendezés-briefet, a fájlnevet, valamint az
**elfogadási és bukási feltételt**.

> ⚠️ **Egyik pilot sem gyártható ma.** Mind a kilencen nyitott kapu ül. Ez a lap
> **elő van készítve** a jóváhagyás utáni pillanatra — nem gyártási engedély. A
> kapu-állapotokat a 2. szakasz tételesen kimondja.

Kapcsolódó: [`MEDIA-PRODUCTION-PLAN.md`](./MEDIA-PRODUCTION-PLAN.md) (a generált
köteg-terv és pilot-táblázat) · [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md)
· [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) ·
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md)

---

## 1. A kilenc pilot

| # | Család | Pilot | Család mérete | Köteg | Kapuk | Eredet |
|---|---|---|---:|---|---|---|
| P-NAR | narráció / hang | `M4.2-NAR-03` | 90 | B2 | R3 | a terv javaslata |
| P-VID | AI beszélőfej | `M5.1-VID-01` | 21 | B3 | R2, R3 | a terv javaslata |
| P-KAR | AI karakter-jelenet | `M4.1-VID-03` | 6 | B3 | R2, R3, R5 | **eltérés** — indoklás lent |
| P-DIA | diagram | `M0.2-DIA-01` | 39 | B1 | R5 | a terv javaslata |
| P-IKO | ikon-készlet | `M1.3-IKO-01` | 40 | B1 | R5 | **eltérés** — indoklás lent |
| P-ILL | illusztráció | `M4.2-ILL-01` | 46 | B1 | R5 | a terv javaslata |
| P-MUN | munkalap / nyomtatvány | `M6.A-MUNK-02` | 61 | B1 | R5 | a terv javaslata |
| P-POS | poszter | `M7.B-POSZ-01` | 37 | B1 | R5 | a terv javaslata |
| P-KRT | kártyaszett | `M5.A-KART-01` | 24 | B1 | R5 | **kiegészítés** — indoklás lent |

A „család mérete” a terv számolásmódját követi: **`mode: generate`** assetek, az
újrahasznosítottak nélkül. A terv a posztert és a kártyaszettet **egyetlen, 61 tételes
családként** kezeli (37 + 24) — itt azért bontjuk ketté, mert a produkciós módszerük
eltér (lásd 1.1.). A 24 kártyaszettből egy (`Z.A-KART-04`) élő/runtime tétel, tehát
központilag 23 gyártható elő.

A generált terv további két pilotot jelöl, amelyek **már ma gyárthatók**, és nincs
szükségük külön briefre: `M4.2-EGY-04` (H5P mini-kvíz) és `M3.F-EGY-01` (beszerzendő
irodaszer). Ezek a BATCH 0-ban állnak.

### 1.1. Miért tér el három tétel a generált tervtől

A terv szabálya — „a legkevesebb nyitott kapuval bíró tételek közül a medián hosszúságú
specifikációjú” — **kapu-optimalizál**. Egy pilotnak viszont a **legnehezebb** dolgot kell
bizonyítania a családban, különben a jóváhagyás nem mond semmit a testvérekről.

| Eltérés | A terv választása | Amit ez a lap választ | Miért |
|---|---|---|---|
| **P-KAR** | `M1.1-VID-02` (B-roll klipek) | **`M4.1-VID-03`** | Az `M1.1-VID-02` néma B-roll **szkript nélkül** (`source_ref` üres) és visszatérő karakter nélkül — a család legnehezebb problémáját, a **karakter-azonosságot**, egyáltalán nem méri. Az `M4.1-VID-03` viszont szó szerinti jóváhagyott narrációhoz kötött (`M4.1-NAR-03-VO`), és a háromjelenetes sorozat első darabja, amelyből az `M4.1-FOTO-01` freeze-frame-je készül — annak specifikációja szó szerint **„ugyanaz a madrich”**. Ez teszi a karakter-azonosságot bizonyítható elfogadási feltétellé. **Ára: egy kapuval több (R2 is ül rajta).** |
| **P-IKO** | `M0.1-IKO-01` (egyetlen ikon) | **`M1.3-IKO-01`** (SBI 3-elemű készlet) | Az `M0.1-IKO-01` **egy darab** ikon; a család neve viszont *ikon-készlet*, és a stílus-token igazi kérdései (készlet-konzisztencia, vonalvastagság, szemantikus szín + forma-redundancia, az R6 ütközés) egy magányos ikonon nem jelennek meg. Az `M1.3-IKO-01` mindhármat egyszerre méri, ráadásul **visszatérő asset**: az `M1.4-IKO-01` `reuse_of`-fal rá mutat, és az `M1.3-DIA-01/02/03` is használja. Azonos kapuszám (R5). Az `M0.1-IKO-01` **kísérő-tételként** ugyanabban a körben legyártható, közel nulla többletköltséggel. |
| **P-KRT** | *(a terv a posztert és a kártyaszettet egy családként kezeli)* | **`M5.A-KART-01`** *(kiegészítés, nem csere)* | A `M7.B-POSZ-01` flipchart-sablon: se kétoldalas nyomtatást, se vágóívet, se az AI-címkét nem teszteli (a `provenance` mezője `human`). A kártyaszett-alcsalád **24 asset**, és a saját produkciós nehézsége — 12 kártya, A4-enként 2–4 db, kétoldalas illesztés — sehol máshol nem jelenik meg. |

---

## 2. Kapu-mátrix — mit kell jóváhagyni, mielőtt egy pilot elindul

**Ez a lap legfontosabb táblázata.** Egyetlen pilot sem gyártható „most”, kivéve ha itt
üres a jobb oldal.

| Pilot | Mire vár | Ki oldja fel |
|---|---|---|
| P-DIA, P-IKO, P-ILL, P-MUN, P-POS, P-KRT | **D1** (stílus-token + paletta) | arculati/program-felelős |
| P-NAR | **D2** (motor és hang) | program- és költségvetési felelős |
| P-VID | **D2** *(a hangot fel kell tölteni)* → **D3/R2** (avatar-jogtisztaság) | + jogi jóváhagyó |
| P-KAR | **D1** (karakter-lock) + **D3/R2** — és a **J1/J2** emberi kapuk. A **D2** csak az utómunkához kell, a képi generáláshoz nem (lásd 2.1.) | + jogi és gyermekvédelmi jóváhagyó |

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

Ez jó hír a költség szempontjából: a beszélőfej-köteg — a drágább, 21 tételes ág — addig
nem indul el, amíg a hang nincs elfogadva, tehát nem kell újragenerálni, ha a hang
változik. A karakter-jelenet képi része viszont párhuzamosítható.

---

## 3. Közös elfogadási feltételek

Minden pilotra érvényes, a családspecifikus feltételeken **felül**.

- [ ] a legyártott anyag **szó szerint** fedi a manifeszt `spec` mezőjét — se több, se kevesebb;
- [ ] beszélt assetnél a hang **szó szerint** a `@source` blokk szövege, és a `source_hash` fel van jegyezve;
- [ ] a kötelező derivatívák elkészültek (`derivatives` mező: felirat / leirat / alt-szöveg / nyomtatható PDF);
- [ ] az akadálymentesítési feltételek teljesülnek (9. szakasz a [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md)-ben);
- [ ] ahol az asset `production_rules` mezőjében szerepel az **R1**, ott a tanulónak látható AI-címke **az LMS-ben, szövegként** jelenik meg — nem a képbe égetve. *(A kilenc pilotból nyolcra vonatkozik; a `M7.B-POSZ-01` `provenance` mezője `human`, a szabálylistája nem tartalmazza az R1-et — oda **nem** kerül címke.)*
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
| **Státusz · kapuk** | `produkciós szabályra vár` · **R3** |
| **Forrás** | `M4.2-NAR-03-VO`, `02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md` (deklaráció: 509. sor) · hash `cc5e9efdc46c9251` |
| **Cél** | bevezeti és keretezi a Dialog Cards aktivitást |
| **Közönség** | madrich, jellemzően 15+ |
| **Hossz** | 20–25 mp · **43 szó** → 103–129 szó/perc; 110 szó/percen **23,5 mp** — a keretben |
| **Deriváltak** | `::CAPTIONS` (felirat), `::TRANSCRIPT` (leirat) |
| **Stílusfüggés** | nincs |
| **Hangfüggés** | **maga a döntés tárgya** |
| **Jogi függés** | R2-4/R2-5, ha a D2 szintetikus hangot választ |

### Miért ez a pilot

A generált terv választása, és megáll: a narráció-család **medián esete** — közepes hossz,
tiszta instrukciós regiszter, egyetlen félkövér kiemelés nélkül, mozgalmi szakszóval
(`chanich`). Aki ezt jól mondja fel, a 90-ből 80-at jól mond fel.

> **Fontos:** a P-NAR a **családi** pilot. A **hangválasztás** viszont nem ezen dől el,
> hanem a három tesztszkripten
> ([`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md)) — azok szélesebb kiejtési és
> érzelmi felületet mérnek. Sorrend: **hangválasztás a három szkripten → a P-NAR az első
> éles felvétel az elfogadott hanggal.**

### Gyártási brief

- Bemenet: a `@source` blokk szövege **tisztítva** — a `„ ”` határoló idézőjel nélkül, a
  `**…**` jelölés hangsúlyra fordítva vagy eltávolítva, emoji nélkül.
- Tempó `<prosody rate>`-tel a 110 szó/perc közelébe; sortörés = rövid levegő, üres sor =
  0,6–1 mp.
- Kiejtés: `chanich` — szóvégi torokhang. PLS-szótárból, ne soronkénti fonéma-címkével.
- Export: WAV 48 kHz / 16 bit / mono mester → MP3 derivatíva.

### Elfogadási feltétel

- [ ] a felmondás szó szerint a forrásszöveg;
- [ ] hossz 20–25 mp között, hadarás nélkül;
- [ ] `chanich` helyesen;
- [ ] tegező, egyenrangú, nem tanáros;
- [ ] tiszta beszéd, háttérzaj nélkül;
- [ ] a `.vtt` felirat időzítése a hanghoz igazítva, szövege a forrással azonos;
- [ ] a leirat a H5P slide-jegyzetbe illeszthető.

### Bukási feltétel

Bármely szóeltérés a forrástól · a 25 mp túllépése hadarással kompenzálva · anglicizált
`chanich` · magázó vagy gyerekhangú felmondás · hallható zaj, szuszogás, vágásnyom.

---

## 5. P-VID — AI beszélőfej · `M5.1-VID-01`

| | |
|---|---|
| **Cím** | HOOK beszélő fej – suli / somer / random |
| **Modul / egység** | M5 / M5.1 |
| **Státusz · kapuk** | `jogtisztázás alatt` · **R2, R3** |
| **Forrás** | `M5.1-VID-01-VO`, `02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md` (deklaráció: 143. sor) · hash `ea1f6213d7c26f07` |
| **Cél** | azonnali érzelmi bevonás; a három tanulási kategória ráhangoló bevezetése |
| **Arány / hossz** | **16:9**, max. 40 mp · **67 szó** → 110 szó/percen 36,5 mp |
| **Deriváltak** | `::VOICEOVER`, `::CAPTIONS`, `::TRANSCRIPT` |
| **Alt-szöveg** | a videóelem **dekoratív** — a tartalmat a felirat és a leirat szó szerint lefedi |
| **Kísérő asset** | `M5.1-EGY-01` — a tanulónak látható R1-címke, **LMS-szövegként** |

### Miért ez a pilot

A 21 beszélőfej **modális esete**: HOOK-videó, közepes hossz, egy szereplő, kamerába
beszél. A generált terv választása, és megáll.

### Gyártási brief — javasolt stack (Synthesia; tartalék: HeyGen API)

| | |
|---|---|
| **Avatar** | **egyetlen készlet-avatar**, amely mind a 21 videóban visszatér. Nem egyedi avatar: így nincs valós személyhez kötött képmás-hozzájárulási lánc. |
| **Megjelenés** | felnőttnek olvasható, semleges, hétköznapi öltözet; nem tanáros, nem céges, nem korporatív háttér |
| **Hang** | **feltöltött hangsáv** a P-NAR-ban elfogadott hanggal — a szolgáltató TTS-e nincs használatban |
| **Keretezés** | mellkép, tekintet a kamerába; a fej a felső harmadban, a cím-biztonságos zónán belül |
| **Háttér** | egyszínű felület a palettából, vagy semleges világos háttér. **Védjegy-semlegesség (R4):** nem utánozhatja a Messenger / WhatsApp / Discord / Insta / Moodle vizuális nyelvét |
| **Felirat** | **nem égetett** — külön `.vtt`; az alsó 15% grafikamentes marad |
| **Export** | MP4 / H.264, 1920 × 1080, 16:9 |

### Negatív megkötések

Nincs égetett szöveg · nincs égetett AI-címke · nincs zenei aláfestés · nincs
márkázott UI-elem · nincs valós személyre hasonlító arc · nincs kiskorúnak látszó
szereplő · nincs kameramozgás vagy zoom-effekt.

### Elfogadási feltétel

- [ ] a **magyar szájszinkron** a feltöltött hangra hihető — *ez a pilot elsődleges, még nem ellenőrzött kérdése*;
- [ ] a hang a P-NAR-ban elfogadott hang, változatlanul;
- [ ] 16:9, ≤ 40 mp, 1080p;
- [ ] a `.vtt` felirat exportálható és időzítése pontos;
- [ ] az alsó 15%-ban nincs grafika;
- [ ] a gépi provenance-jelölés az exportban megmaradt;
- [ ] az R1-címke az LMS-ben, szövegként jelenik meg (`M5.1-EGY-01`);
- [ ] az avatar újrahasználható a további 20 videóhoz **ugyanazzal az azonosítóval**.

### Bukási feltétel

Rossz vagy „idegen nyelvű” szájmozgás · a szolgáltató saját TTS-e szólal meg a feltöltött
hang helyett · égetett felirat vagy címke · watermarkos kimenet · a felirat nem
exportálható · az avatar nem rögzíthető újrafelhasználásra.

---

## 6. P-KAR — AI karakter-jelenet · `M4.1-VID-03`

| | |
|---|---|
| **Cím** | Jelenet 1 karaktervideó – „Jegyzetbe bújó madrich” |
| **Modul / egység** | M4 / M4.1 |
| **Státusz · kapuk** | `jogtisztázás alatt` · **R2, R3, R5** |
| **Forrás** | `M4.1-NAR-03-VO`, `02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md` (deklaráció: 734. sor) · hash `238cf16a52679083` |
| **Hossz** | 20–25 mp, teljes alakos jelenet |
| **Konténer** | beágyazva az `M4.1-VID-02` H5P Interactive Videóba (`composed_of`) — a felirat és a leirat **a konténeré**, nem ezé |
| **Származék máshol** | az `M4.1-FOTO-01` freeze-frame-je ebből és az `M4.1-VID-05`-ből készül |

### A szó szerinti narráció (másolat, nem kánon)

> „Nézd meg ezt a madrichot.
> A papírra koncentrál, a válla kicsit beesik,
> a tekintete szinte végig lefelé van.
>
> Ha chanich lennél,
> mennyire éreznéd azt, hogy **neked beszél**,
> és mennyire azt, hogy inkább a lapja mögé próbál bújni?”

A karakter **nem beszél** — a narrátor beszél róla harmadik személyben. Ez a jelenet
teljes hangfeladata.

### Miért ez a pilot

Mert ez a család **egyetlen valódi nehézsége**: a három jelenetben ugyanannak az embernek
kell látszania, és az `M4.1-FOTO-01` specifikációja ezt szó szerint kimondja
(„ugyanaz a madrich karba tett kézzel vs. nyitott kézzel”). Egy pilot, amely nem méri a
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
- [ ] a gépi provenance-jelölés megmaradt.

### Bukási feltétel

A karakter jeleneteként más ember · kiskorúnak látszó alak · a modell kitalált nyelven
beszélő szájmozgást ad · nem reprodukálható a seed/referencia rögzítése után · valós
személyre hasonlítás · a testtartás nem olvasható ki a képből.

> ⚠️ **EMBERI DÖNTÉS — nyitott szerzői hiány, amit ez a brief nem tölt ki.** Az
> `M4.1-FOTO-01` specifikációja **karba tett kezet** kér („ugyanaz a madrich karba tett
> kézzel vs. nyitott kézzel/felsőtesttel”), de ezt a testtartást **egyik
> jelenet-specifikáció sem tartalmazza**: az `M4.1-VID-03` „előreeső vállak, papírba
> mélyed”, az `M4.1-VID-04` „lábról lábra billeg”, az `M4.1-VID-05` „laza vállak”. A
> freeze-frame maga sem nevez meg jelenetet, csak annyit, hogy „az IV-videókból”.
> **A szerzőnek kell megmondania, melyik jelenet viszi a karba tett kezet — vagy hogy a
> képpár másik testtartás-kontrasztra épül.** Amíg ez nyitva van, a P-KAR jóváhagyható,
> az `M4.1-FOTO-01` viszont nem gyártható le.

> ⚠️ **A P-KAR nem indítható a `J1` és a `J2` emberi kapu megválaszolása előtt** —
> [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.3.

---

## 7. P-DIA — diagram · `M0.2-DIA-01`

| | |
|---|---|
| **Cím** | SLIDE 4 jelzési folyamatábra: észreveszem → nem maradok egyedül → jelzek → támogatást kapunk |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Cél** | a „madrich, nem terapeuta” logika egyetlen lineáris jelzési útvonalként; megerősíti, hogy a madrich nem egyedül old meg, hanem jelez |
| **Deriváltak** | `::ALTTEXT` |

### Miért ez a pilot

A terv választása, és megáll: a 39 diagram **modális szerkezete** (lineáris, számozott
lépéssor), és ráadásul gyermekvédelmi tartalmú — a legláthatóbb hely, ahol az olvashatóság
számít.

### Gyártási brief — **determinisztikus SVG, nem generatív**

Négy csomópont, nyilakkal: **1)** Valami nem oké / Észreveszem · **2)** Nem maradok
egyedül · **3)** Jelzek *(ken-vezető · gyermekvédelmi felelős · stáb)* · **4)** Támogatást
kapunk.

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

- [ ] a négy csomópont szövege szó szerint a lecke **330. és 336–346. sorának** lépéseivel egyezik;
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
| **Kísérő-tétel ugyanebben a körben** | `M0.1-IKO-01` (a terv pilotja) — egyetlen ikon, közel nulla többletköltség |
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

A terv választása, és megáll — de van egy külön érdeme: **ez az egyetlen illusztráció-pilot,
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
| **Szedés** | a jóváhagyott törzsbetűtípus, balra zárt, a buborékon belül keskeny margóval |
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
| **Cím** | Képzői checklist – „Játék-labor 4 kvucára” (1 oldalas cheat-sheet) |
| **Státusz · kapuk** | `produkciós szabályra vár` · **R5** |
| **Formátum** | **A4 álló, pontosan 1 oldal**, pipálható checklist |
| **Deriváltak** | `::PRINTPDF` |

### Miért ez a pilot

A terv választása, és megáll: a 61 nyomtatványos tétel **legszigorúbb formai kényszerével**
(„1 oldalra”), ami a tipográfiai skálát azonnal próbára teszi.

### Gyártási brief — determinisztikus HTML/CSS → PDF

Tartalom: a forrás 5. szekciójának öt pontja — **1)** Meta tiszta · **2)** Játékok
kiválasztva · **3)** Eszközök & tér · **4)** Safety keret a fejben · **5)** Híd az M6.B
játéklaphoz.

| | |
|---|---|
| **Lapméret / margó** | A4 álló; 14 mm fent/balra/jobbra, 12 mm lent; semmi 10 mm-nél közelebb a széphez |
| **Tipográfia** | cím 17–20 pt félkövér; szekciócím 11–13 pt; törzs 10,5 pt / 1,38; jegyzet 8,5 pt; élőláb 7 pt |
| **Jelölőnégyzet** | 4 × 4 mm, 1 pt `#1D1D1B` keret, 0,7 mm sarok |
| **Kézírásos mező** | sorköz ≥ 8 mm, alávonás `--rule` 0,6 pt |
| **Élőláb** | `M6.A-MUNK-02 · v… · Játék-labor 4 kvucára` balra, oldalszám jobbra |
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

A terv választása, és megáll: ez méri a **nagy formátumú, teremből olvasható**
tipográfiát, ami a **37 gyártandó poszter** (39 összesen) közös kényszere.

**Amit viszont NEM mér:** az AI-címke elhelyezését (mert `human` eredetű), a kétoldalas
nyomtatást és a vágóívet. Ezért van külön kártyaszett-pilot (P-KRT), és ezért az AI-címke
elhelyezését a P-ILL és a P-MUN validálja.

### Gyártási brief

Két mező egy lapon vagy két lapon:

1. **„Zmán Kvucá = …”** — konkrét idősáv + kvuca + tér + felelősség; **nem** aznap
   kitalált random program.
2. **„AI-határok”** — **mind a három** ponttal (a lecke 111. és 228. sora): nincs konkrét chanich-név vagy sztori;
   gyermekvédelmi ügyben mentorhoz, nem AI-hoz; az AI csak ötletel, a felelősség a
   madriché.

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

Az AI-határok bármelyik kikötése lágyul vagy kimarad · a „gyermekvédelmi ügyben
mentorhoz, nem AI-hoz” mondat elveszti az élét · nem olvasható teremtávolságból · téves
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

Kiegészítés a poszter mellé: a kártyaszett-alcsalád **24 asset**, és a saját produkciós
nehézségét — kétoldalas illesztés, vágóív, kézbe vehető olvashatóság — semmilyen más
pilot nem méri.

### Gyártási brief — determinisztikus HTML/CSS → PDF

| | |
|---|---|
| **Előlap** | 1–3 mondatos szituáció-leírás; a szó szerinti szöveg a lecke **6. mellékletében, az 540. sortól** („## 6. Melléklet – 12 helyzetkártya – szövegek”; a tizenkét kártya kb. az 542–661. sorban). **Megjegyzés:** az asset `spec` mezője még a régi `402-518` tartományt írja — ez elavult hivatkozás a manifesztben, külön, tudatos adatjavítást igényel, és ez a lap nem végzi el. |
| **Hátlap** | képzői címke `[SULI]` / `[SOMER]` / `[RANDOM]` a fogalommal (formális / nonformális / informális) |
| **Kiosztás** | 4 kártya / A4, szaggatott vágóvonal `--rule` színnel |
| **Duplex** | a hátoldal **oszlopsorrendje tükrözött**, hogy a hosszú élű duplex illeszkedjen |
| **Tipográfia** | előlap törzs ≥ 12 pt (a képző felolvassa a teremben); hátlap-címke nagy, verzál |
| **Redundancia** | a hátlapcímke mellé **forma-glif** is kerül (pl. ▣ / ◆ / ●), hogy a három kategória szín nélkül is elváljon |
| **Védjegy-semlegesség (R4)** | ennek az assetnek a szabálylistájában az R4 is szerepel, és a kártyaszövegek említenek platformokat („buszos TikTok”, „Insta/TikTok görgetés”). A **szöveg marad változatlanul**; a kártya viszont **nem** rajzolhat felismerhető alkalmazás-ikont, logót vagy platform-felületet |
| **AI-jelölés (R1)** | az asset `provenance` mezője `mixed`, és a szabálylistája tartalmazza az R1-et → a nyomtatvány élőlábában szövegként ott a kanonikus címke |
| **Élőláb** | kártyánként `M5.A-KART-01 · v… · <sorszám>/12` |

### Elfogadási feltétel

- [ ] mind a 12 kártya szövege szó szerint a 6. mellékletből (540. sortól);
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
- **Nincs 100 tételes köteg elfogadott pilot előtt.** Ez a lap ezért létezik.
- Ha egy pilot bukik, a **családja nem indul** — de a többi család mehet tovább, mert a
  2.1. sorrendi ábra szerint csak a videós ág láncolt.

## 14. Fájlnév-konvenció a pilotokhoz

A teljes konvenció: [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 7. szakasz.

| Pilot | Mester | Derivatíva |
|---|---|---|
| P-NAR | `M4.2-NAR-03__master.wav` | `…__master.mp3` · `…__captions.hu.vtt` · `…__transcript.hu.md` |
| P-VID | `M5.1-VID-01__master.mp4` | `…__captions.hu.vtt` · `…__transcript.hu.md` |
| P-KAR | `M4.1-VID-03__master.mp4` *(néma + alámuxolt narráció)* | felirat/leirat a konténerhez: `M4.1-VID-02__captions.hu.vtt` |
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
