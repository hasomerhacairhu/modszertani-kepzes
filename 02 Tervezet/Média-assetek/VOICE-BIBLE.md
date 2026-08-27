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

## 12. Motor és hang — NYITOTT (D2)

| Mező | Állapot |
|---|---|
| Szintetikus vagy emberi felmondó | nyitott → D2 |
| Motor / szolgáltató neve | nyitott → D2 |
| Voice-ID vagy felmondó személye | nyitott → D2 |
| Kereskedelmi-oktatási felhasználás igazolása | nyitott → D3, [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) |
| Hang-jogosultság (voice-talent release / klónozási engedély) | nyitott → D3 |

**Ez a hang-bible egyetlen valódi hiányzó döntése.** Minden más mező fent ki van töltve
a jelenlegi tananyagból. Amint a D2 megszületik, a narráció-köteg
(90 asset / 267 deliverable) indulhat — a pilot jóváhagyása után. A beszélőfej- és
karaktervideók ezen felül az R2-re (és részben az R5-re) is várnak.

> Szolgáltatót ez a lap nem javasol és nem nevez meg: erre a repositoryban nincs
> bizonyíték, a kitalálása pedig jogi és költségvetési kötelezettséget hamisítana.
