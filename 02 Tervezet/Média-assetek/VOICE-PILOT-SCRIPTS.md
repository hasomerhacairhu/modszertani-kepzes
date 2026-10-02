# 🎧 Hang-pilot szkriptek — a narrátor-döntés (D2) tesztanyaga

Ez a lap **három meglévő narrációt** jelöl ki a tananyagból, amelyeken a hangjelöltek
összehasonlíthatók. A szövegek **másolatok, nem kánon**: a kánoni forrás továbbra is a
leckében álló `@source` blokk, és a felvétel mindig onnan készül.

> ⚠️ **Ez a lap nem hoz létre új narrációt, és nem írja felül a meglévőt.** Ha egy
> forrásszöveg megváltozik a leckében, ez a lap **elavul** — a `Forrás-hash` oszlop
> ezért van itt. Ellenőrzés: `python3 tools/media_manifest.py check`.

**Miért kell pilot:** a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 11. szakasza kimondja, hogy
„a pilot dönt” — a tempót, a hangszínt, a szünetkezelést és a someres szavak kiejtését
egyetlen jóváhagyott felvételen kell rögzíteni, és a többi tétel ehhez igazodik. A hang
90 narráció-assetre és 27 videó hangsávjára hat; egy rossz választás 117 tételen kerül
vissza.

**Mit NEM dönt el ez a lap:** magát a hangot. Ez a lap a **tesztanyagot** jelöli ki; a
végrehajtható összehasonlítás — beállítások, kiejtési figyelőlista, pontozólap —
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md).

> ✅ **2026-08-28: a szolgáltatói kérdés lezárult.** A felmondás **szintetikus**, a motor
> az **ElevenLabs**, és a jelöltek a két forrás-beszélő — **VOICE-SRC-01** és
> **VOICE-SRC-02** — felvételeiből **létrehozandó** egyedi hangok; **a hangok még nem készültek el**.
> Az itt kijelölt három szkript ezért már nem „motorválasztási” tesztanyag, hanem a
> **két hang összehasonlításának** anyaga — hatmintás mátrixban, a hangok létrehozása után.

---

## 1. A három szkript és amit mérnek

| # | Asset | Forrásblokk | Szó | Lecke-időkeret | Mit tesztel elsősorban |
|---|---|---|---:|---|---|
| **P1** | `M3.1-NAR-02` | `M3.1-NAR-02-VO` | 136 | 60–75 mp | hosszú magyarázó ív, hangsúlykezelés, angol szakszavak magyar mondatban |
| **P2** | `M6.2-NAR-04` | `M6.2-NAR-04-VO` | 71 | 40–50 mp | visszafogott érzelmi sáv, párbeszéd-idézet, mozgalmi köznevek |
| **P3** | `M3.1-NAR-05` | `M3.1-NAR-05-VO` | 40 | 15–20 mp | kiejtés — mind a három aktuális kvuca-tulajdonnév egyetlen mondatban |

Együtt kb. **247 szó ≈ 2 perc** kész hang. Ennyi elég a döntéshez, és nem terheli meg a
próba-keretet.

### Mit fed le a három szkript a hang-bible 6. szakaszának kiejtési táblájából

| Lefedett | Hol |
|---|---|
| `kvuca` / `kvucá-` (c = /ts/) | P1, P2, P3 |
| `Somer` / `someres` (s = /ʃ/) | P1, P3 |
| `madrih`, `madrihhoz` (szóvégi torokhang) | P2 |
| `hanih` (szóeleji **és** szóvégi torokhang) | P2 |
| `peula` | P2 |
| `Parparim`, `Kivsza`, `Leviatán` | P3 |
| `Tuckman` (szerzőnév, kiejtés rögzítendő) | P1 |
| évszám felmondása (`1977`) | P1 |

**Amit a három szkript NEM fed le** — ezeket a köteg-jóváhagyáskor külön kell
ellenőrizni, nem a piloton: `ken`, `Zmán Kvucá`, `dugma isit`, `hágsámá`, `bogrim`,
`mazkirut`, `Hasomer Hacair`, `Johari`, `SBI` betűzés, korosztály-tartományok
(`6–9`, `13–17`), időtartamok (`45’`, `45 mp`).

---

## 2. P1 — Nyugodt magyarázó narráció

- **Asset:** `M3.1-NAR-02` — *INPUT 1 narráció – Tuckman 4+1 szakasz*
- **Forrás:** `02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md`, `@source` blokk `M3.1-NAR-02-VO` (deklaráció: 254. sor, törzs: 255–275. sor)
- **Forrás-hash:** `92d86f7be3c403a5`
- **Lecke-időkeret:** kb. 60–75 mp · **136 szó** → 109–136 szó/perc
- **Céltempó szerint:** 110 szó/percen **74 mp** — a keretben marad.

### Miért ez a reprezentatív magyarázó szkript

- A korpusz **leghosszabb egybefüggő INPUT-narrációja**. Ha egy hang egy percen át
  megtartja a figyelmet monotónia nélkül, a 20–40 mp-es többségen is meg fogja.
- **Kilenc félkövér kiemelés** van benne — a hang-bible 5. szakasza szerint ezek
  hangsúlyos szavak. Ez a legsűrűbb hangsúly-teszt a tananyagban.
- **Öt `👉` emoji** áll sorkezdeten. A hang-bible szerint az emoji **hangulatjelölő, nem
  felmondandó** — ez egyben csővezeték-teszt: a szintézis bemenetéből az emojit ki kell
  szűrni, különben a motor felolvassa vagy megbotlik rajta.
- Öt **angol szakszó** (`forming`, `storming`, `norming`, `performing`, `adjourning`)
  áll magyar mondatban, az egyik magyar toldalékkal (`adjourning`-ot). Ez a magyar TTS
  tipikus töréspontja.
- Egy **évszám** (`1977`) és két **szerzőnév** (Bruce Tuckman, Mary Ann Jensen).


### A szó szerinti szöveg — **másolat, nem kánon**

> „Bruce Tuckman egy csoportkutató volt, aki azt mondta:
>
> **a legtöbb csoport négy fő szakaszon megy át**, mielőtt igazán jól működne (plusz van egy ötödik, a lezárás).
>
> 👉 Az első a **forming**, vagyis az alakulás.
> Ilyenkor mindenki kicsit bizonytalan, udvarias, figyeli a többieket.
>
> 👉 A második a **storming**, amikor jönnek a viták, beszólások, klikkek.
> Ez fárasztó lehet, de **nem hiba**, hanem a fejlődés része.
> Figyelj: a storming kölcsönös vita – a célzott bántás már nem storming.
>
> 👉 A harmadik a **norming**, amikor megszületnek a közös szabályok.
> Már jobban figyelnek egymásra, és elkezd kialakulni a bizalom.
>
> 👉 A negyedik a **performing**.
> Itt a kvuca már tényleg **együtt dolgozik**, saját ötleteket hoz, és felelősséget vállal.
>
> 👉 Tuckman 1977-ben, Mary Ann Jensennel közösen tett hozzá egy ötödiket, az **adjourning**-ot, vagyis a **lezárást**.
> Ez a kvuca búcsúja: amikor egy someres ciklus véget ér, és szépen elköszöntök egymástól.”

*A kánoni példány a leckében áll; ez a másolat a `92d86f7be3c403a5` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `kvuca` (2×) | „kvuca”, c = /ts/ | glosszárium, hang-bible 6. |
| `someres` | „someres”, s = /ʃ/ | glosszárium, hang-bible 6. |
| `Tuckman` (2×) | **a pilot rögzíti** — a leckék nem adnak kiejtési előírást; a jóváhagyott változatot utána következetesen kell tartani | hang-bible 7. |
| `Mary Ann Jensen` | angol személynév | — |
| `1977-ben` | „ezerkilencszázhetvenhét-ben”, nem számjegyenként | hang-bible 7. |
| `forming` / `storming` / `norming` / `performing` / `adjourning` | angol olvasat, magyar mondatritmusban; az `adjourning`-ot toldalékkal | — |

### Tempó és hangvétel

Nyugodt, tagolt, magyarázó. A kulcsszó kap hangsúlyt, nem az egész mondat. A négy
`👉`-cel kezdődő blokk **azonos ritmusú** legyen — ez a szakaszok listaszerűségét adja
vissza. Nincs lelkesedés, nincs tanári számonkérés.

---

## 3. P2 — Érzelmileg telítettebb, reflektív narráció

- **Asset:** `M6.2-NAR-04` — *Narráció – SLIDE 4 történet 2. rész*
- **Forrás:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md`, `@source` blokk `M6.2-NAR-04-VO` (deklaráció: 492. sor, törzs: 493–512. sor)
- **Forrás-hash:** `f78f0c8b737f2434`
- **Lecke-időkeret:** kb. 40–50 mp · **71 szó** → 85–106 szó/perc
- **Céltempó szerint:** 110 szó/percen **39 mp** — a keret alsó szélén, tehát **van hely a szüneteknek**. Ez itt szándékos.

### Miért ez a reprezentatív érzelmi szkript

- Ez a tananyag **legérzelmesebb narratív szakasza**, és pontosan az a hely, ahol a
  hang-bible 3. szakasza a **túljátszást hibának** nevezi: „a szöveg önmagában hordozza
  a feszültséget — a felmondás ne tegyen rá”. Egy reklámhangú vagy drámai TTS ezen a
  szövegen azonnal megbukik; egy generikus marketingmondaton nem bukna meg.
- **Ez az egyetlen szkript, amelyben párbeszéd-idézet van**
  (`‘Figyi, szerintünk ez nem volt oké. / Lehetett volna valamit csinálni?’`), ráadásul
  két sorra tördelve. A hangnak jeleznie kell, hogy idézet — de a 8. szakasz szerint
  **nem külön karakterhanggal**: ez narrátori idézés, nem dialógus-asset.
- Hordozza a három leggyakoribb mozgalmi köznevet (`madrih`, `hanih`, `peula`) és a
  toldalékolt `madrihhoz` / `kvucának` alakot.
- Egyetlen félkövér kiemelés zárja (`a történet tükröt tarthat a kvucának`) — a
  hangsúly a lezáró mondaton ül, nem szórva.


### A szó szerinti szöveg — **másolat, nem kánon**

> „A beszólás után Lili elhallgat.
> Lehajtja a fejét, hátradől.
>
> A madrih hallja, mi történt.
> Látszik rajta, hogy gondolkodik,
> de végül csak megköszöni Lilinek a megosztást,
> és megy tovább a kör.
>
> A peula véget ér.
> Lili szinte végig csendben marad.
>
> A végén két hanih odamegy a madrihhoz,
> és azt mondják:
> ‘Figyi, szerintünk ez nem volt oké.
> Lehetett volna valamit csinálni?’
>
> Most jön az a rész,
> ahol **a történet tükröt tarthat a kvucának**.”

*A kánoni példány a leckében áll; ez a másolat a `f78f0c8b737f2434` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `madrih`, `madrihhoz` | „madrih” — a szóvégi **h** hallható torokhang, nem /cs/, nem /k/; a toldalékolt alakban is | hang-bible 6. |
| `hanih` | „hanih” — a szó eleji és a szóvégi **h** is hallható torokhang | hang-bible 6. |
| `peula` | „peula”, kisbetűs köznév | glosszárium |
| `kvucának` | hosszú á a toldalékolt tőben | glosszárium |
| `Lili`, `Lilinek` | magyar keresztnév | — |

### Tempó és hangvétel

Visszafogott, tényszerű, meleg — **nem szomorkás és nem drámai**. A „Lili szinte végig
csendben marad.” után valódi szünet kell (üres sor = 0,6–1 mp). Az idézetnél a
regiszter enyhén vált, a hangszín nem.

---

## 4. P3 — Kiejtés-sűrű narráció

- **Asset:** `M3.1-NAR-05` — *Outro narráció – átvezetés M3.2-re*
- **Forrás:** `02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md`, `@source` blokk `M3.1-NAR-05-VO` (deklaráció: 811. sor, törzs: 812–818. sor)
- **Forrás-hash:** `17184b1a6e2cf25c`
- **Lecke-időkeret:** 15–20 mp · **40 szó** → 120–160 szó/perc

> ⚠️ **Mért eltérés, nem hiba a szkriptben.** A céltempón (110 szó/perc) ez a szöveg
> **kb. 22 mp**, azaz ~2 másodperccel túllépi a lecke 15–20 mp-es keretét. A hang-bible
> 4. szakasza erre kimondott szabályt ad: „a lecke időkerete a szűk, nem a szöveg
> hosszú — ilyenkor a felvételnél a **hosszt kell tágítani**, nem a szöveget hadarni.”
> A pilotnak ezt kell megerősítenie: a felvétel **nem** gyorsulhat 130 szó/perc fölé
> csak azért, hogy beleférjen. Ha a jóváhagyó mégis a 20 mp-es keretet tartja
> kötelezőnek, az **szerzői döntés a lecke időkeretéről**, nem hangdöntés.

### Miért ez a reprezentatív kiejtési szkript

- A tananyag **legsűrűbb someres kiejtési tesztje**: 40 szóban több kiejtés-érzékeny elem, köztük **mind a három aktuális kvuca-tulajdonnév egyetlen felsorolásban**.
- A `Leviatán` hangzóhossza: a projektgazdai döntés (2026-10-02) szerint a first-party
  „Leviatán” alak a kánon, hosszú á-val; a tananyag írott alakja gépi migrációval vált át.
  Ha egy hang ezt elrontja, az minden előfordulásnál látszani fog.
- Rövid: egy jelölt kiejtési profilja 20 másodperc alatt eldönthető, mielőtt a hosszabb
  szkriptekre költenél.


### A szó szerinti szöveg — **másolat, nem kánon**

> „Köszi, hogy végigmentél ezen a leckén.
> Most már van egy térképed arról, hogyan fejlődik egy kvuca.
> A következő részben belenagyítunk a három aktuális someres kvucába:
> Parparim, Kivsza és Leviatán –
> hogy lásd, milyen világban élnek, és te miben tudsz hozzájuk kapcsolódni.”

*A kánoni példány a leckében áll; ez a másolat az `17184b1a6e2cf25c` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `Parparim` | „parparim” | glosszárium |
| `Kivsza` | „kivsza” | glosszárium |
| `Leviatán` | „leviatán” — hosszú **á**, a first-party „Leviatán” alak szerint | projektgazdai döntés (2026-10-02); hang-bible 6. |
| `kvuca`, `kvucába` | c = /ts/; a toldalékolt tőben hosszú á | glosszárium |
| `someres` | s = /ʃ/ | glosszárium |
| `és` a felsorolás végén, `–` gondolatjel | a gondolatjel szünet, nem felmondandó | hang-bible 5. |

### Tempó és hangvétel

Lezáró, barátságos, kicsit lassuló. A négy tulajdonnév **külön-külön hallható** legyen —
ez a szkript egyetlen valódi feladata. A gondolatjel után rövid levegő.

---

## 5. Hogyan kell a pilotot futtatni

1. **Egy hang = mind a három szkript**, tehát a két jelölttel összesen **hat minta**. Egy
   szkripten nem lehet hangot választani: P1 a tempót, P2 az érzelmi sávot, P3 a kiejtést
   méri, és egy hang lehet az egyikben jó, a másikban rossz. A mátrixot és a beállításokat
   a [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) tartalmazza.
2. **A szintézis bemenete tisztított szöveg**, nem a nyers Markdown. A pontos szabályokat
   a tesztlap 2.1. szakasza rögzíti — röviden: a `**…**` jelölés **eltávolítandó** (nem
   fordítandó hangsúly-jelölésre), az emoji a mögötte álló szóközzel együtt törlendő, a
   nyitó/záró `„ ”` a forrásblokk határa, a sortörés és az üres sor viszont marad.
3. **Ugyanaz a tisztított szöveg megy mindkét hanghoz**, bájtra azonosan — különben nem
   hangot hasonlítasz össze, hanem szövegváltozatokat.
4. **A kiejtési táblát (hang-bible 6.) mindkét hangnál végig kell hallgatni** — a teszt
   **szótár nélkül, egyetlen körben** fut. A kiejtési szótár a teszt **eredménye**, nem a
   bemenete: előbb ki kell derülnie, melyik szó romlik el ténylegesen, és csak azokra
   készül alias-szabály. *(A „szótárral és anélkül is lefuttatni" kétkörös eljárás a
   motorválasztás idejéből maradt itt; a motor azóta eldőlt, és a kétkörös futtatás
   megkétszerezné a hat mintát.)*
5. **A jóváhagyó magyar anyanyelvű, someres szóhasználatot ismerő ember.** A
   `Leviatán` / `kvuca` / `hanih` alak helyességét nem lehet leírt átiratból eldönteni.

## 6. Elfogadási feltétel a hang-pilotra

- [ ] mind a három szkript elkészült ugyanazzal a hanggal;
- [ ] P1 tempója 100–125 szó/perc között marad, és a kilenc kiemelés hallható;
- [ ] P1-ben egyetlen emoji sem hangzik el;
- [ ] P2 nem játssza túl az érzelmi tartalmat, és az idézet nem külön karakterhang;
- [ ] P3-ban mind a három aktuális kvuca-név helyes, és a `Leviatán` hosszú á-val,
      „leviatán”-ként szól;
- [ ] a `madrih` / `hanih` szóvégi és szóeleji hangja a hang-bible 6. szakasza szerint
      hallható torokhang, nem /cs/ és nem /k/;
- [ ] a `kvuca` c-je /ts/, a `Somer` s-e /ʃ/;
- [ ] a hang tegező, egyenrangú, nem gyerekhang és nem hivatalos;
- [ ] a felvétel szó szerint fedi a forrásszöveget (a felirat ebből generálódik);
- [ ] tiszta beszéd, háttérzaj nélkül; a hang-bible 10. szakaszának nyitott
      mastering-értékei (mintavétel, bitmélység, csatorna, normalizálás) ekkor
      rögzíthetők.

> **Írásmód — projektgazdai döntés (2026-10-02):** a magyar Somer first-party alakjai a
> kánon (madrih, hanih, hágsámá, dugma isit, Leviatán), és a tanulói korpusz egyszeri gépi
> migrációt kapott (2026-10-02). Ezzel a P2 és a P3 forrásszövege is változott: a fenti
> másolatok és a hash-ek a migrált szöveget követik, a karakterszám az
> `ELEVENLABS-VOICE-TEST.md`-ben frissítve, a szószám nem változott. A P2 és P3 hangmintáját a migrált szöveggel, **a terminológiai
> ellenőrzővel együtt** érdemes meghallgatni (utólagos ellenőrzés (vétó/QA): a ken-vezető /
> mozgalmi felelős).
>
> **Korosztály-architektúra frissítve 2026-09-28:** a tananyag a 2025/26-os oktatási tervre
> hivatkozó három csoportot használja: **Parparim 6–9, Kivsza 10–12, Leviatán 13–17** (HUM-SOMER-02; projektgazdai döntés, 2026-10-02).
> A P3 ezért már csak ezt a három tulajdonnevet teszteli.
