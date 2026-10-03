# 🎙️ Narrátor hang-bible

Az R3 produkciós szabály végrehajtási lapja: minden, ami a **jelenlegi tananyagból
objektíven levezethető** a felmondásról. Ami nyitva maradt, azt a lap kimondja, és a
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D2 pontjára mutat — ott van
egyetlen helyen az összes megválaszolandó érték.

**Hatókör:** 89 hang-asset (88 narráció és az `M1.3-NAR-08` hangalámondásos képleírás), 18
beszélőfej-videó, 3 hangalámondásos HOOK-videó (`explainer`) és 6 karakter- és jelenetvideó —
összesen 116 tétel. Az `M1.1-VID-02` néma B-roll kivételével mind szó szerinti forrásblokkal;
nincs szkript nélküli beszélt asset.

> **A szolgáltató 2026-08-28-án eldőlt: a felmondás szintetikus, a motor az ElevenLabs.**
> **2026-10-03 óta (projektgazdai döntés, VO 2. fázis):** mindkét ElevenLabs-hang — a **kanonikus narrátorhang**
> és a **második hang** — létezik; a hanghasználati jog tisztázott, a hang tulajdonosai kifejezetten
> hozzájárultak (VO D-01). Az **elsődleges narrátor a kanonikus narrátorhang**; a második hang
> jogtisztázott; az első gyártási körben csak az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után — a többi
> tételnek ez nem feltétele (VO D-14; K4). A modell, a
> beállítások és a kiejtési szótár rögzítve: 12. szakasz. A formális jogosultsági bizonyíték (a
> nem személyes hivatkozás és a jóváhagyói minősítés) függő —
> [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5. A hangok és a VOICE-SRC-álnevek
> megfeleltetését ez a lap nem rögzíti.
>
> A két forrás-beszélő álnéven szerepel: a valódi név, a szerződés vagy hozzájárulás, a
> hatókör és a dátum a korlátozott hozzáférésű jogosultsági nyilvántartásba tartozik, nem a
> repositoryba (projektgazdai döntés, 2026-10-02, `HUM-MEDIA-02`). A nyilvántartás: Google
> Workspace Shared Drive → `Restricted / Rights / Voice`, fájl: `VOICE-RIGHTS-REGISTER`; a
> projektgazda által név szerint kijelölt két személy szerkesztheti (`Emberi jóváhagyás
> szükséges.md`, `HUM-MEDIA-02`), a producer csak az álneveket látja. Kötelező mezők:
> álnév, valódi név, hozzájárulás vagy szerződés hivatkozása, engedélyezett felhasználás,
> modell/szolgáltató, terület, időtartam, visszavonás, aláírás dátuma, a bizonyíték helye
> vagy hash-e. A git-előzmények kezelése: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).
> Utólagos ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős és a hang tulajdonosai.
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

A hallgató **madrih, jellemzően 15+**, aki maga is kiskorú lehet. Ebből következik:

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

**A hang mért tempója (2026-10-03, VO 2. fázis).** A kanonikus narrátorhang természetes tempója
`eleven_v4`-en, a 12. szakasz beállításaival, a 24 renderelt blokkon **107–164 szó/perc,
medián ≈ 131**. A v4-en nincs tempó-vezérlés (`speed`), ezért ez adottság, nem beállítható
érték (projektgazdai döntés, 2026-10-03, VO D-02).

**A korábbi céltempó nem elfogadási feltétel.** A 100–120 szó/perces cél a leckék
2026-08-27-i keret–szöveg arányából jött, és ezen a hangon nem érhető el. Az időkeret a mért
természetes hosszhoz igazodik (VO D-17): ahol a szöveg hosszabb a keretnél, **a keretet kell
tágítani, nem a hangot gyorsítani**, és nem a védett mondatot vágni. Időnyújtás (time-stretch)
nem fő megoldás; legfeljebb ≤ 5%-os, hallhatóan ártalmatlan utómunkás igazítás jöhet szóba,
ha az alaphossz már a keretben van.

**Ahol a hang rövidebb a keretnél** (jellemzően a csak-hang felvezetőknél), ott a keretet nem
töltjük fel szöveggel. Ha a keret a tanuló gondolkodási idejét is tartalmazza, a címke ezt
kimondja: elöl a hang hossza, utána a gondolkodási idő (VO D-17.3), például „hang kb. 6–8 mp,
utána gondolkodási idő (a szakasz összesen 20–30 mp)”.

## 5. Szünet és hangsúly

- **A szünetet a központozás adja.** Az `eleven_v4` a forrás sortörését és üres sorát nem
  veszi szünetnek (mérve: a sor- és bekezdéstöréses változat azonos seeddel ±0,02 mp-en belül
  ugyanazt adja), SSML-szünet nincs. A soronkénti tördelés a forrás olvashatóságát szolgálja.
- **Bekezdés-szünet utómunkában.** Ahol a lehallgatás a bekezdéshatárt kevésnek találja, az
  utómunka kb. 0,6–1,0 mp szünetet illeszt be, a felirat-időzítéssel együtt. Bekezdésenként
  külön TTS-kérés csak a szünet kedvéért nem készül (projektgazdai döntés, 2026-10-03, VO D-10).
- **A `**félkövér**` nem hangsúlyjel.** A leckék ezzel jelölik a fogalmi kulcsszót
  (`**neked beszél**`, `**végignéz**`, `**más pillanatok**`), és a megjelenített szövegben, a
  feliratban és a leiratban meg is marad. A v4-nek nincs hangsúlyjelölő eszköze, és a CSUPA
  NAGYBETŰ sem megbízható kiemelés: a jelentést hordozó hangsúlyt a mondatszerkezet adja. Ahol
  ez nem elég, szerkesztői szövegcsere jöhet szóba — a felirattal együtt, saját findinggal.
  Az elfogadási feltétel: **a jelentést hordozó hangsúly nem sérül (fülre)** (projektgazdai
  döntés, 2026-10-03, VO D-11).
- A kérdőmondatok **valódi kérdésként** szólnak — a legtöbb HOOK kérdéssel indít.
- Az emoji a forrásszövegben (pl. 😅) **hangulatjelölő, nem felmondandó**.

## 6. Kiejtés — someres és héber szavak

A tananyag írásmódja **magyar-fonetikus és szándékos**; a
`Glosszárium – someres és pedagógiai fogalmak.md` ezt kánoni referenciaként rögzíti.
Ebből következik a felmondás is: **a leírt alakot magyarul kell olvasni** — kivéve, ahol a
VO QA-repó B4-regisztere (a kiejtési döntések kanonikus forrása, VO D-13) fülre más
hangzást rögzített: ott a kanonikus kiejtési szótár (12. szakasz) aliasa adja a hangot, az
írott alak, a felirat és a leirat pedig nem változik (projektgazdai döntés, 2026-10-03, VO D-03–D-06).

| Írott alak | Kiejtés | Forrás / megjegyzés |
|---|---|---|
| `kvuca` | „kvuca” — a **c** = /ts/ | a glosszárium kifejezetten kimondja: „a magyar »c« = /ts/ adja vissza a héber צ hangot”; **nem** „kvutza”, **nem** „kvuka” |
| `Somer`, `someres` | „somer” — az **s** = /ʃ/ | tulajdonnév, nagybetűs; **nem** „shomer” |
| `Hasomer Hacair` | „hasomer hacair” | magyar-fonetikus; **nem** „Hashomer Hatzair” |
| `peula`, `peulák` | „peula” | köznév, kisbetű |
| `madrih`, `madrihok`, `madrihot` | **„mádrih”** [maːdrix] — nem kerekített első magánhangzó, első szótagos hangsúly, szóvégi [x]; a szótár aliasa „mádrih” + rag (B4; VO D-04). A nyers olvasat (kerekített [mɔdrix]) fülre elvetve | a hibrid „madrihák” alak a tananyagban tiltott |
| `hanih`, `hanihok` | **[xanix]** — a szótár héber írású aliasa adja, a magyar rag kötőjel után (B4; VO D-04). A nyers olvasat (kerekített, lágy „honih”) fülre elvetve | egy helyen (M0.2) szándékosan héber többes: „hanihim” |
| `dugma isit` | [duɡma iʃit] — a szótár héber írású aliasa, kötőjeles raggal; jóváhagyott (B4), a fülpróba lezárva (VO D-06) | köznév, kisbetű; a „Dugma Isit” személynévi alak kerülendő |
| `ken` | „ken” | rövid e, nem „kén” |
| `Zmán Kvucá` | [zman kvutsa] — a szótár héber írású aliasa, kötőjeles raggal; jóváhagyott (B4), a fülpróba lezárva (VO D-06). Az írott hosszú á-k a hangban nem hosszúak | a `c` itt is /ts/ |
| `Parparim` | „parparim” | pillangók, 6–9 |
| `Kivsza` | „kivsza” | bárány, 10–12 |
| `Leviatán` | **„Leviatan”** [leviotɒn] — rövid a-val, a fülre jóváhagyott hangzás; a szótár aliasa Leviatán → Leviatan, Leviatánnál → Leviatannál (B4; VO D-05). A szóvégi hosszú á nem produkciós kiejtés | 13–17; a first-party „Leviatán” alak a kánon (projektgazdai döntés, 2026-10-02) — az írott alak és a felirat nem változik |
| `hágsámá`, `bogrim`, `mazkirut` | magyar olvasat | ritkábban fordulnak elő |

> ✅ **Írásmód — projektgazdai döntés (2026-10-02).** A magyar Somer first-party alakjai a
> kánon: madrih, hanih, hágsámá, dugma isit, Leviatán. A tanulói korpusz — és vele a fenti
> tábla „Írott alak” oszlopa — egyszeri gépi migrációt kapott; a belső azonosítók nem
> változtak. **A hangzást a kiejtési szótár köti a fülre hozott döntésekhez:** a kanonikus
> szótár szabályai a migrált írott alakokra illeszkednek, a hangzás a B4-ben jóváhagyott
> maradt (VO D-04, D-23). A pilot ezt produkciós környezetben ellenőrzi, nem dönti el újra
> (11.2.; VO D-13). Utólagos ellenőrzés (vétó/QA): a ken-vezető / mozgalmi felelős.

## 7. Számok, betűszók, rövidítések

- **Korosztályok:** a 2025/2026-os Oktatási terv szerinti felosztás (`HUM-SOMER-02`; projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a ken-vezető / mozgalmi felelős): `Parparim 6–9`, `Kivsza 10–12`, `Leviatán 13–17`; felmondva „hat–kilenc éves”, „tíz–tizenkét éves”, „tizenhárom–tizenhét éves”. A `13–17` a hang bemenetében (tts_text) kiírva szerepel („tizenhárom–tizenhét”), mert számjeggyel a hang „tizenháromtól tizenhét”-et mond; a felirat számjegyes marad (VO D-09, D-23).
- **SBI:** betűzve, „es-bé-í”, és a modell elemei magyarul: Situation–Behavior–Impact →
  a leckék „S”, „B”, „I” betűjelet használnak, ezeket betűként kell mondani.
- **Tuckman és a Tuckman-szakaszok:** „Takmen”, a teljes név „Brúsz Takmen”, a társszerző
  „Méri En Dzsenszen”; a szakaszok „fórming, sztórming, nórming, perfórming, edzsörning”
  (B4, fülre jóváhagyva; VO D-04). A szótár aliasa adja, az írott alak nem változik.
- **Johari:** a hang saját, magyaros olvasata — szabály nélkül, elfogadva (VO D-23).
- **Angol szakszavak:** `energizer` → „enerdzsájzer”, `red flag` → „rett fleg”, `checklist` →
  „csekliszt” (B4; VO D-23), a szótár aliasával.
- **Kódok:** `M0`–`M7` „em nulla” … „em hét”, a pont „pont”; az „.A” végű kód „pont á”
  (`M2.A` → „em kettő pont á”), mert a puszta „a” névelőnek hallatszik. Ez a hang bemenetében
  (tts_text) történik, a felirat `M2.A` marad (VO D-23).
- **Csupa nagybetűs szó:** a hang bemenetében az „ÉN” helyett „én” áll („az ÉN” → „az én”;
  VO D-23, 5. szakasz).
- **Időtartamok:** `45’` = „negyvenöt perc”, `45 mp` = „negyvenöt másodperc”.
- **Segélyvonalak** (112, 116-111, 116-123) narrációban **nem** hangzanak el — képzői
  kártyán szerepelnek (`M3.B-KART-02`). Ha valaha narrációba kerülnek, számjegyenként
  kell mondani őket. **Kivétel: a 112** az `M3.3-NAR-01-VO` gyermekvédelmi lépéssorában
  elhangzik. A 112 kiejtése — a fenti számjegyenkénti szabálytól eltérően — mindig „száztizenkettő”, soha nem „egy-egy-kettő”; az írott szöveg és a felirat „112” marad, a kimondott
  alakot a hang bemenete (tts_text) rögzíti (projektgazdai döntés, 2026-10-03, VO D-07;
  utólagos ellenőrzés (vétó/QA): a Memuna). A 116-os vonalakra a fenti szabály változatlan.

## 8. Karakter- és dialógushangok

A tananyagban **két** jelenet hordoz szereplői beszédet. Az első gyártási körben az `M4.1`-jelenetek narrációját
a kanonikus narrátorhang mondja, az `M1.3-VID-01` párbeszédét a két hang együtt szólaltatja meg:

- `M1.3-VID-01` — két madrih (A és B) beszélget, ugyanaz a helyzet kétféle
  visszajelzéssel. A szkriptet a szerző 2026-08-27-én jóváhagyta; a szó szerinti dialóg a
  leckében, `M1.3-VID-01-VO` forrásblokkban él. **Első gyártási kör (projektgazdai döntés,
  2026-10-03, VO D-14; kiegészítő döntés K4):** Madrih A szerepét a kanonikus narrátorhang, Madrih B szerepét a
  második hang mondja, **beszélőnként külön szegmensben** — a replikák nem fűződnek egyetlen
  névtelen TTS-folyammá, a beszélő azonosítója a szerkezetben megmarad, és a felirat minden
  replikánál megnevezi a beszélőt. A második hangot ehhez előbb kalibrálni kell (VO QA-repó);
  az `M1.3-VID-01` hanganyaga addig nem készülhet el, a többi tételt ez nem blokkolja. A kétszereplős, szájszinkronos gyártási út nyitott
  ([`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D11).
- `M4.1-VID-03/04/05` — a karakter **nem beszél** a hangsávban: a jelenetek némán
  készülnek, és a narrátor beszél róla harmadik személyben („Nézd meg ezt a madrihot…”). A
  3. jelenet mondatát („Sziasztok, ma arról fogunk beszélni, hogy…”) **a narrátor idézi** az
  `M4.1-NAR-05-VO` forrásblokk szerint; a szereplőnek nincs saját hangsávja, és külön
  karakterhang nem készül (projektgazdai döntés, 2026-10-03, VO D-15). A 2. jelenet „gyorsan
  beszél” utasítása a néma képen szájmozgásként jelenik meg; ezt a generálásnál
  visszafogottan kell tartani.

Minden más narráció **egyetlen, azonos narrátorhang** — ezt az R3 első mondata írja elő
(„EGYETLEN konzisztens narrátor-hang az egész tananyagban, tegező + barátságos
regiszterben — a Z-záró és az M4 modulokat is beleértve”).

## 9. Kapcsolat a felirattal és a leirattal

Ez nem stílus, hanem akadálymentesítési követelmény
(`LMS – hozzáférhetőségi sztenderd.md`):

- **Szinkronizált videó → felirat kötelező** (WCAG 2.2 SC 1.2.2), és a teljes leirat
  **nem helyettesíti**.
- **Csak hang → a dián vagy a médiaelem mellett látható teljes leirat a szöveges ekvivalens**
  (SC 1.2.1); első sora a kanonikus AI-címke (PRODUCTION-STYLE-TOKEN.md 7.3.). A H5P Audio
  elemhez nem írunk elő feliratsávot; a `.vtt` legfeljebb archivált derivatíva (projektgazdai
  döntés, 2026-10-03, VO D-19, D-21).
- **A felirat szó szerint fedje le az elhangzottakat.** Ezért a felmondás **nem
  improvizál**: amit a `@source` blokk tartalmaz, azt kell mondani. Ha a szöveg
  változik, a leckében kell változnia — a felirat és a leirat onnan generálódik.
- **Megjelenített szöveg és hangbemenet külön.** A felirat és a leirat a `@source` szövegét
  adja a jelölők nélkül (`**`, `*`, a blokk külső „ ” idézőjele, emoji, sor eleji listajel),
  minden szóval, a kanonikus írásmóddal. A kiejtési szótár aliasa és a hang bemenetének
  (tts_text) célzott, naplózott cseréi — `M2.A` → „em kettő pont á”, `13–17` →
  „tizenhárom–tizenhét”, `az ÉN` → „az én”, `112` → „száztizenkettő” — **csak a hangban**
  élnek, a feliratba és a leiratba nem kerülnek (projektgazdai döntés, 2026-10-03, VO D-09 és
  a döntéscsomag 3. pontja). A kanonikus megvalósítás a VO QA-repó szövegkinyerője
  (display_text / tts_text).
- **Párbeszéd:** a felirat minden replikánál kiírja a beszélő nevét a cue szövegében (pl. „Madrih A: …”);
  a WebVTT `<v>` hangjelölés a megjelenített feliratban nem látszik, ezért legfeljebb kiegészítés. A
  beszélő- és a verziócímke a párbeszédben nem hangzik el; a verziócímkét a hangalámondásos
  képleírás (`M1.3-NAR-08-VO`) mondja el (VO D-14, D-18).
- Az Interactive Videónál (`M1.3-VID-01`, `M4.1-VID-02`) **egy** felirat-sáv és **egy**
  leirat tartozik a teljes videóhoz; az `M4.1-VID-02` szövege a három jelenet
  narrációjának sorrendi összefűzése. Az `M1.3-VID-01` hangalámondásos
  képleírása külön forrásblokk (`M1.3-NAR-08-VO`), amely a párbeszéd szüneteiben szól (VO D-18).

**Gyakorlati következmény a felvételre:** minden narrációról tudni kell, melyik
`@source` blokkból készült, és a felvétel eltérése a szövegtől **hiba**, nem szabadság.

## 10. Kimenet és mastering

A leckék technikai jegyzeteiből:

- **Formátum:** MP3 vagy WAV (a jegyzetek 19 helyen kiírják; néhány helyen MP3/AAC a
  H5P Course Presentation audio miatt).
- **Tartalom:** „tiszta beszéd, háttérzaj nélkül” — a leckék kifejezetten így fogalmaznak.
- **Hossz:** tételenként a lecke adja meg (10–15 mp-től kb. 70–90 mp-ig); a leggyakoribb
  a 20–40 mp.
- **Egy asset = egy fájl.** A narráció-assetek nem darabolódnak tovább.

**Mester (projektgazdai döntés, 2026-10-03, VO D-12):** 48 kHz / 16 bit / mono WAV, a
`pcm_48000` API-kimenetből, átmintavételezés nélkül — a fiók valódi 48 kHz-es PCM-et ad
(mérve, 2026-10-03). A hangmodell saját sávszélessége kb. 16 kHz-nél véget ér, tehát a 48 kHz
nem hordoz több hangtartalmat, mint egy 44,1 kHz-es kimenet; azért ez a mester, mert valódi
API-mester, és egyezik a [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 6. szakaszával. A
szállítási MP3 a mesterből készül. A kérésben ténylegesen elküldött formátumot és a
mintavételt a kísérőadat rögzíti.

Nyitott: a hangerő-normalizálás célértéke és a csúcsérték — a pilot-felvétel jóváhagyásakor
rögzítendő. Javaslat a pilothoz: beszédre normalizálva, azonos csúcsértékkel minden fájlban.

## 11. Konzisztencia-szabályok

1. **Egy narrátorhang mindenre.** A narrációt — az `M4.1`-jelenetekét is — a kanonikus narrátorhang
   mondja (VO D-15); egyetlen kivétel az `M1.3-VID-01` Madrih B szerepe, amelyet a második hang
   mond (VO D-14; K4).
2. **A pilot ellenőriz, nem dönt újra.** A kiejtés kanonikus döntési forrása a
   VO QA-repó B4-regisztere (fülre hozott, kötelező döntések). A P1–P3 szkript
   ([`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md)) és a P-NAR ezeket produkciós
   környezetben ellenőrzi, nem nyitja újra őket (projektgazdai döntés, 2026-10-03, VO D-13).
   A P-NAR az `M4.2-NAR-03` ([`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) P-NAR);
   a generált terv narráció-pilotja (`MEDIA-PRODUCTION-PLAN.md` 5. szakasz) a fordító
   szabálya szerinti javaslat, és eltérhet tőle. A pilot a hangszínt, a szünetkezelést és a
   mért hosszt hagyja jóvá, és minden további R3-tétel ehhez igazodik. Ha egy jóváhagyott
   kiejtés a produkcióban hallhatóan eltér a próbától, az regresszió, nem új döntési kérdés
   (VO D-23).
3. **A kiejtési táblát (6. szakasz) minden felvételnél újra kell futtatni** — ez a
   leggyakoribb elcsúszási pont egy több hónapos gyártásban.
4. **Nincs verziószám a hangban.** Ha a lecke szövege változik, a fájl újra készül; a
   manifeszt `source_hash` mezője mutatja, melyik szövegverzióhoz készült.

## 12. Motor, hang és gyártási konfiguráció

**Felhasználói döntés, 2026-08-28; a hang és a konfiguráció: projektgazdai döntés, 2026-10-03 (VO 2. fázis).**

| Mező | Állapot |
|---|---|
| Szintetikus vagy emberi felmondó | ✅ **SZINTETIKUS** — eldőlt |
| Motor / szolgáltató | ✅ **ElevenLabs** — eldőlt |
| Modell | ✅ **`eleven_v4`**, `language_code: "hu"` — projektgazdai döntés, 2026-10-03 (VO D-02); a fülre hozott kiejtési döntések ezen a modellen születtek |
| Hangok | ✅ a **kanonikus narrátorhang** és a **második hang** — mindkét ElevenLabs-hang létezik; a hanghasználati jog tisztázott, a hang tulajdonosai kifejezetten hozzájárultak (VO D-01). A hangok és a **VOICE-SRC-01/02** álnevek megfeleltetését ez a lap nem rögzíti |
| Hang-létrehozás (módszer: IVC / PVC / egyéb) | a hangok elkészültek; a módszerről és a fiókhoz kötött tényekről (hangtípus, fióktulajdon, tanítási kimaradás) csak valós bizonyítékból rögzíthető adat → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.0 |
| Kanonikus narrátor | ✅ a **kanonikus narrátorhang** — az első teljes gyártási kör narrátorhangja; a **második hang** jogtisztázott, és az első körben csak az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után (VO D-14; K4) |
| Voice-ID | nem nyilvános: csak a VO QA-repó gyártási konfigurációjában él, a kurzusrepóba nem kerül (kiegészítő projektgazdai döntés, 2026-10-03, K3; ez a `HUM-MEDIA-02` „Implementáció” sorát felváltja) |
| Hangtípus (klón / tervezett / stb.) | fiókbizonyítékból rögzítendő (13.4.) — nem találjuk ki |
| Hangbeállítások és seed | ✅ `stability` **0,35**, `similarity_boost` **0,75** — a v4-en csak ez a kettő hat; `speed` és `style` nincs, nem is küldjük (VO D-02). Seed: rögzített (260930). A ténylegesen elküldött értékeket minden kérés kísérőadata rögzíti |
| Szövegnormalizálás | ✅ `apply_text_normalization: auto`, plusz a hang bemenetének (tts_text) célzott, naplózott cseréi (VO D-09; mérve: az `off` nem jobb) |
| Mesterformátum | ✅ `pcm_48000` → 48 kHz / 16 bit / mono WAV (10. szakasz; VO D-12) |
| Kiejtési szótár | ✅ a kanonikus gyártási kiejtési szótár — azonosító `ulYxuUbd8aSRJ89Pv2Q8`, verzió `VFpQiiOF789b08uzsooM`, 267 szabály; a forrása a VO QA-repó PLS-fájlja és konfigurációja, és minden gyártási konfiguráció a verziót rögzíti (VO D-03). Szótár nélküli gyártás nincs (13.5.) |
| Hang-jogosultság igazolása | tartalmilag tisztázott (VO D-01); a formális bizonyíték függő → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5 |

> **Az R3 tartalmilag kitöltve, a kapu még nem zárult le.** A kanonikus hang, a modell, a
> beállítások és a szótár rögzítve, a voice-ID helye kijelölve (fent; K3); nyitott a P-NAR
> pilot (`M4.2-NAR-03`) fülre jóváhagyása produkciós környezetben (11.2.; VO D-13) és a második
> hang kalibrálása az `M1.3-VID-01`-hez (8. szakasz; K4). Az R3
> blokkoló ezért a tételeken a helyén marad; a levétele a manifesztben külön, tömeges
> módosítás ([`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D2).

---

## 13. ElevenLabs — produkciós kutatás (2026-08-28)

> **Történeti kutatás (2026-08-28) — a hatályos konfiguráció a 12. szakaszban áll.** A
> 13.1–13.7. pont a `flash_v2_5` és a `v3` közti választás idején készült. A gyártás modellje az
> `eleven_v4` (projektgazdai döntés, 2026-10-03, VO D-02): ezen csak a `stability` és a
> `similarity_boost` hat; `speed`, `style` és SSML-szünet nincs; a szögletes zárójeles
> audio-taget a modell előadja, ezért szögletes zárójel nem kerülhet a hang bemenetébe; az
> IPA-fonémaszabály működik, de az alias az elsődleges eszköz. Az alábbi `speed`-, `style`- és
> modellajánlások ezért **nem használhatók**: a tempót a szöveg és az időkeret adja (4.
> szakasz), a mesterformátum a 10. szakaszban áll. Érvényes marad a 13.5. toldalékolási
> csapdája, a 13.6. „minden kérésben explicit beállítás” szabálya és a determinizmus plafonja.

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

A két jelölt a két forrás-beszélő felvételeiből létrehozandó egyedi hang volt (2026-08-28-i állapot; azóta mindkét hang elkészült, és a kanonikus narrátorhang is ki van jelölve — 12. szakasz):

| | |
|---|---|
| **A) VOICE-SRC-01** | jelölt a kanonikus narrátor szerepre |
| **B) VOICE-SRC-02** | jelölt a kanonikus narrátor szerepre |

**Ajánlás: nincs — MEGHALLGATÁS SZÜKSÉGES.** Két hang közül dokumentáció alapján
választani nem lehet; a magyar természetesség, a melegség és a someres szavak kiejtése
csak hallgatással dönthető el. A hatpárosos összehasonlítás végrehajtható terve:
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md).

**Egy hang lesz a kanonikus narrátor**, ahogy az R3 első mondata előírja. A másik hang
sorsa (tartalék, dialógus- vagy karakterhang) **külön, későbbi döntés** — ez a lap nem
osztja ki neki egyik szerepet sem. Az `M1.3-VID-01` dialógushangjainak kérdése:
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D11.

### 13.4. A két hang azonosítása — a létrehozás után

> ✅ **A hangok léteznek (projektgazdai tényközlés, 2026-10-03, VO D-01).** A 2026-08-28-i
> kutatáskor még nem voltak meg. Ebben a repositoryban **nincs ElevenLabs hitelesítő adat**, és
> a voice-ID-t, a hangtípust **nem rögzítjük és nem találjuk ki**: az alábbi menet a
> fiókbizonyíték kinyerésére szolgál.

**Amit a felhasználónak ki kell nyernie — webes út (a leggyorsabb):**

1. **My Voices** oldal (`elevenlabs.io/app/voice-lab`).
2. A hang neve melletti **típusikon** megmondja a hangtípust — a dokumentált jelmagyarázat:
   **sárga pipa** = Professional Voice Clone · **fekete pipa** = Studio Quality PVC ·
   **villám** = Instant Voice Clone · **nincs ikon** = Voice Design (tervezett hang).
3. Ugyanott látszik, **milyen nyelvre tanították** — ellenőrizendő, hogy magyar.
4. A három pont menüben: **Copy voice ID**.

**Hitelesített, csak olvasó API-út** (generálás és költés nélkül):

```
GET /v2/voices?search=VOICE-SRC-01&voice_type=personal
GET /v2/voices?search=VOICE-SRC-02&voice_type=personal
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
| **Voice Design** (`generated`) | teljesen szintetikus: nincs azonosított természetes személy, akinek a hangját klónoznánk — de ebből **nem következik, hogy nincs jogi kérdés**: a bizonyíték-nyilvántartás `LEGAL_REVIEW_REQUIRED` állapotban tartja, a minősítés a jogi jóváhagyóé ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.0.) |

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

**Az eljárás (projektgazdai döntés, 2026-10-03, VO D-03) — a 2026-08-28-i „szótár nélküli
első kör” helyett:**

1. Minden gyártási kérés a **kanonikus kiejtési szótár** rögzített azonosítójával és
   verziójával megy (12. szakasz). Szótár nélküli gyártás vagy próbakör nincs: a szótár
   nélküli olvasat a fülre már elvetett változatokat hozná vissza (a kerekített [mɔdrix]-ot, a
   lágy „honih”-ot, az angol s-sel ejtett „szomer”-t).
2. A szabályokat a VO QA-repó építi a narráció ténylegesen előforduló alakjaiból
   (minden toldalékos alakra külön szabály), PLS-ből reprodukálhatóan; a lefedettség-ellenőrzés
   hibával áll meg, ha egy kanonikus írásmódú alakra nincs szabály.
3. Új vagy módosított szabály csak próbával és fülre hozott döntéssel kerül be (B4-regiszter,
   VO D-13); a B4-ben elvetett változat nem javasolható újra.
4. Minden szótárváltozás új verziót ad; a gyártási konfiguráció a verziót rögzíti, a
   kísérőadat minden kérésnél naplózza.

> ⚠️ **Magyar toldalékolási csapda — ez a szakasz legfontosabb gyakorlati tudnivalója.**
> A szótárszabályok `case_sensitive` és `word_boundaries` kapcsolója egyaránt
> **alapértelmezetten igaz**. Szóhatárral egy `Somer` szabály **nem fog illeszkedni** a
> `someres`, `Somert`, `Somerek` alakokra. A magyar toldalékolás miatt tehát **a ténylegesen
> előforduló összes alakot fel kell sorolni** (`kvuca / kvucát / kvucában / kvucák`,
> `peula / peulát / peulák`, `madrih / madrihok / madrihhoz` …), vagy tudatosan ki kell
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
| **Archív mester (ideális)** | `wav_48000` — **48 kHz** / 16 bit, veszteségmentes. A formátum-listában létezik (ellenőrizve). A 10. szakasz a mintavételt **nyitottnak** hagyja, a produkciós stack 6. szakasza pedig csak **ajánlja** a 48 kHz-et (▫️ produkciós ajánlás); a hangteszt és a P-NAR a csomag legjobb formátumával számol (`wav_44100` / `mp3_44100_192`). Az egységes mesterformátum a nyitott csomagdöntéssel együtt rögzítendő | a 44,1 kHz-re a szolgáltató kimondottan **Pro**-t követel; a **48 kHz csomag-kapuját a dokumentáció nem mondja ki** — a fiókban ellenőrizendő |
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
| **Licenc a feltöltött tartalomra** | „perpetual and irrevocable… nonexclusive… royalty-free… worldwide and sub-licensable” licenc a szolgáltatás nyújtására és javítására, valamint „to develop new services and products” *(4(d), lekérdezve 2026-10-02)* | **nem a kimaradás oldja meg:** a kimaradás a tanítási felhasználásra szól, a licencet pedig a szolgáltató visszavonhatatlannak írja le → `LEGAL_REVIEW_REQUIRED` ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) E-9; V2) |
| **Tanítás a bemeneten — kimaradás** | „you may opt out of our use of your Content for training at any time…”; csak „once the request has been processed by our team” hat *(4(i), lekérdezve 2026-10-02)*, és „**does not affect any uses… prior to that date**” | **a kimaradást ELŐRE kell bekapcsolni**, nem utólag — minden fiókban, ahová felvétel kerül; a feltöltés csak a kérés feldolgozása után jöhet |
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
| **Hatmintás meghallgatás** (mérve) | 3 208 | **≈ 0,16 $** | **≈ 0,64 $** |
| Teljes tananyag, kész hang | 50–82 ezer | 2,50 – 4,10 $ | 10 – 16 $ |
| Teljes tananyag, **3× nyers** | 150–225 ezer | **7,50 – 11,25 $** | **30 – 45 $** |

*(A `v3` mindkét olvasatban nagyjából a kétszerese.)*

*(2026-10-03: a narráció mért terjedelme kb. 47 ezer karakter — QA-mérés, 2026-10-02: 47 070
karakter, 112 blokk; a fenti „50–82 ezer” a 2026-08-28-i becslés, és a `flash_v2_5` árával
számol. A v4-es karakterárat a fiók elszámolásából kell ellenőrizni.)*

**A lényeg a bizonytalanság ellenére is áll:** a teljes tananyag hangja **tíz–ötven dollár
nagyságrend**, a hatmintás teszt pedig **kevesebb, mint egy dollár**. A csomagot ezért ne a
karakterár döntse el, hanem a **kimeneti formátum és a hangtípus**: Creator elég a
kereskedelmi használathoz és a 192 kbps MP3-hoz, Pro csak a veszteségmentes WAV-mesterhez
kell. **A tényleges elszámolást a fiókban kell ellenőrizni** az első köteg után.

### 13.10. Amit ez a lap NEM dönt el — emberi kapuk

| # | Kérdés | Kihez tartozik |
|---|---|---|
| **V1** | *(korábbi, Microsoft-specifikus tétel — **tárgytalan**, mert nem az a szolgáltató lett kiválasztva.)* Helyette: a választott szolgáltató **nem ír elő** közlési kötelezettséget előre renderelt narrációra. A tananyag R1-címkéje tehát **saját projektdöntés**, és az is marad. Hogy kiskorú tanulók esetén a **szülő/gondviselő** felé kell-e külön tájékoztatás, továbbra is nyitott — de ez a **tananyag** kérdése, nem a szolgáltatóé. | Memuna (gyermekvédelmi felelős) + DPO; a `HUM-MEDIA-02` alkapuja — felelős és bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. |
| **V2** | A hang **jogosultsági bizonyítéka**. Ha a kiválasztott hang valós személy klónja, a szolgáltató önbevalláson túl **semmilyen bizonyíték-formát nem ír elő** — a szervezetnek magának kell eldöntenie, milyen hozzájárulást tart, milyen formában és meddig. | jogi jóváhagyó + a hang jogosultja → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |
| **V3** | A szolgáltató feltételei szerint 18 év alatti nem használhatja a szolgáltatást, és kiskorú hangadata nem tölthető fel; a tiltólista viszont 13–18 közötti használatot szülői hozzájárulással elképzelhetőnek tart. **A saját dokumentumaik nem mondanak ugyanazt.** A tananyagban a madrih maga is lehet kiskorú. Kiskorú hangjának klónozása egyértelműen tiltott; hogy kiskorú kezelheti-e a fiókot, nyitott. | Memuna (gyermekvédelmi felelős); az E-8 jogi kérdésében a jogi jóváhagyó — az E-8 jogi felülvizsgálata külön lezárási feltétel; a `HUM-MEDIA-02` alkapuja — felelős és bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. |
| **V4** | A **tanítási kimaradást** be kell kapcsolni, **mielőtt** bármit feltöltünk — visszamenőleg nem hat, és csak a kérés feldolgozása után lép életbe. Minden fiókban kell, ahová felvétel kerül. Ez üzemeltetési lépés, de felelőst kíván. | a fiók gazdája — PVC-nél a forrás-beszélő is, mert a hang az ő fiókjában jön létre (`HUM-MEDIA-02`) |

> A kutatás **szűkíti** a döntést, nem helyettesíti. A kanonikus hang kiválasztása
> meghallgatásos emberi döntés marad.
