# 2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), AP-2026-10-12-01

- **Scope:** az M1 modul HUM 14. szakasz szerinti átvezetésének diffje (`eb4fa6d`), csak a módosított sorok és közvetlen környezetük. Nem teljes új audit.
- **Lencsék (ténylegesen lefutott):** biztonság-jog (`safety-policy-reviewer`), értékelés + LMS (`assessment-reviewer`), nyelv (`hungarian-editorial-reviewer`). Adverzális második kör: `verifier`, mind a 24 ID-ra.
- **Run-ID:** AP-2026-10-12-01 · **Review-bázis:** `eb4fa6d` · **Javítás:** `7a69b9d`, media `7de9164`.
- **Állapot:** VALIDÁLT.

## I. Riport

### 1. Validált objektív findingok — javítva (`7a69b9d`)

| ID | Súly | Hely | Javítás |
|---|---|---|---|
| M1:QA-BIZT-2 (GYV-12; GK §4.3:102) | P2 | M1.4 (a terv 39. blokkja) | az ad hoc „ha nagyon nehéz, válassz enyhébb szituációt” sorok kikerültek; a Memuna-mondat és a §4.3 blokk marad |
| M1:QA-BIZT-4 (RÉSZBEN; ADV-7) | P2 | M1.A §5 ellenőrző lista | a Johari-cetli szabálya szó szerint (:145) a listában is |
| M1:QA-ERT-2 (RÉSZBEN; ERT-13) | P2 | M1.4:450 | „(a mondatszám csak útmutatás, nem pontozzuk)”; példa, formátum, rubrika változatlan |
| M1:QA-NYELV-5 (+ QA-ERT-1 M1.A-része; ERT-13) | P2 | M1.A:541 | „1–2 ilyen visszajelzést írni” |
| M1:QA-ERT-5 (RÉSZBEN; ERT-15) | P2 | M1.4:628 | a „Nincs kettős levonás” bekezdés a KAPU:83 szerint; szintleírások változatlanok |
| M1:QA-ERT-6 (ERT-16) | P2 | M1.3:1027, KAPU:201, HUB:117 | az S-elem: „mikor vagy hol (vagy mindkettő), és a helyzet melyik szakaszában” |
| M1:QA-ERT-7 (+ QA-NYELV-6; ERT-4) | P2 | KAPU:132 | „(formatív szerzői itempool – NEM a kapu)” |
| M1:QA-NYELV-1 (+ QA-BIZT-3; ADV-2) | P2 | M1.F:159 | a tanuló látja a kiindulópontját, a képző csak a haladást és a minimális hiánylistát |
| M1:QA-NYELV-4 (ADV-2) | P2 | M1.F:161 | egy megnevezés: „minimális hiánylista” |
| M1:QA-NYELV-2 (RÉSZBEN; GYV-6) | P2 | M1.A:509, M1.B:392, M1.F:109 | „(a tanulói „Ha ez a téma téged is érint” blokk: `Gyermekvédelem – release gate.md` §4.3)” |
| M1:QA-NYELV-7 (GYV-21) | P2 | M1.A:374 | a zárójel-a-zárójelben feloldva; a tartalom és a korlát változatlan |
| M1:QA-NYELV-9 | P2 | M1.3:938 (`@asset`) | szám-egyeztetés („ezt viszi tovább”); build külön `chore(media)` commitban |

### 2. Emberi döntést igénylő tételek

| ID | Mit kell eldönteni | Kitől |
|---|---|---|
| M1:QA-BIZT-5 (GYV-11) | a jogosult Memuna-eljárás, a korlátozás/helyesbítés módja, a törlés és a megőrzés; a feltárásmentes pótlási út mechanikája és a próbálkozás beszámítása (a követelmény maga a kánoni körben az ADV §5-be kerül) | Memuna + DPO; a kapueredményre az értékelési felelős |

### 3. Bizonyíték-kapu

- M1:QA-BIZT-6 — a HUM 14. szakasz 16 bizonyíték- és aláírás-bejegyzése (Memuna, DPO/jogi felelős, LMS-gazda, programvezető, értékelési felelős): RELEASE-READINESS G1–G3 és a tracker. Megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő.
- M1:QA-ERT-3 — az ERT-14 rubrikájának értékelési felelősi jóváhagyása (QA: módszertani lektor).

### 4. Külső függőség (VO fix pack)

- M1:QA-BIZT-1 (RÉSZBEN) — a NAR-05 `@source` „Gondolj egy helyzetre, ami eszedbe jut” mondata ütközik a :885-tel (ERT-12). A `@source`-hoz nem nyúlunk: csak a VO fix pack javítja; a ledgerben nyitott release-blokkolóként áll. A MAN:48-rész a kánoni körbe tartozik.

### 5. Elvetve

- M1:QA-ERT-4 — a példa nem a commit része, a baseline ismeretlen; rubrikahorgony cseréje új alkalmazási eset (ERT-15 kalibrációja nyitott).
- M1:QA-NYELV-3 — az M1.F:66 a PRG-5 szó szerinti átvezetése; a javaslat más szabályt írna be.
- M1:QA-NYELV-8 — az ERT-14 szó szerinti szövege; ízlésbeli átírás.
- M1:QA-NYELV-10 — a súgó kérdése, nem a tanuló szövege; a PRG-16 nyitott QA-jú sablonját érintené.
- M1:QA-NYELV-11 — a „személyes munkapéldány” az ADV-11 szó szerinti kifejezése.

## B. Verifier-verdiktek (szó szerint)

<!-- agent a5b4b1256838a8024 -->

M1 célzott QA (AP-2026-10-12-01, eb4fa6d): adverzális második kör, 24 ID. Read-only voltam, semmit nem szerkesztettem.

**Formátum:** ID | verdikt | típus | súly | indok | javítás

QA-BIZT-1 | RÉSZBEN | objektív (VO fix pack; most nem javítható) | P1 | A NAR-05 `@source` (M1.3:901) „Gondolj egy helyzetre, ami eszedbe jut” mondata valóban ütközik a :885-tel (ERT-12). Ez a terv VO_PACK sora (plan:1461), a plan:1525 viszont a BIZT-G2-1-et FIXED-nek jelöli. A MAN:48-rész közös kánoni fájl, ezért nem M1-finding. | Korlát: a `@source`-hoz nem nyúlunk, csak a VO fix pack javítja (plan:1461). A ledgerben a NAR-05 nyitott release-blokkolóként álljon, ne FIXED-ként.

QA-BIZT-2 | MEGERŐSÍTVE | objektív | P2 | A GK §4.3:102 lezárt döntése (2026-10-02) szó szerint előírja: „ad hoc »ha nehéz« … támogató blokk helyére ez kerül”. A §4.3 blokk ott van (:518), a GYV-12 HUM-sora pedig „M1-ben a szabad szöveghez” szól, nem csak az M1.3-ra. Ráadásul a „személyes helyzet → enyhébb szituáció” ellentmond a :465-nek és a HUM:462-nek. Ez tehát nem új alkalmazási eset. | A plan Block 39-e. OLD „> Ha nagyon nehéz vagy személyes helyzet jut eszedbe, nyugodtan válassz\n> egy **enyhébb, egyszerűbb szituációt**.\n> Ha valódi gyermekvédelmi aggály jut eszedbe” → NEW „> Ha valódi gyermekvédelmi aggály jut eszedbe”. A :516 és a :518 marad. Utána `--pin-visible`, és a MUNK-01 név szerint követi.

QA-BIZT-3 | MEGERŐSÍTVE (duplikátum → QA-NYELV-1 a megtartandó) | objektív | P2 | Az M1.F:159 szerint a képző a kapun kapott visszajelzést látja. Ez ütközik az ADV-2-vel („F-peula képzője csak aggregált vagy minimális hiánylistát lát”) és a :161-gyel. A javasolt NEW elliptikus „mindketten … lássa” alakja számbeli egyeztetési hiba. | A QA-NYELV-1 NEW-ja használandó.

QA-BIZT-4 | RÉSZBEN | objektív | P2 | Az ADV-7 szabálya csak az Eszközök listájában áll (:145). A §5 ellenőrző listájában és a folyamatban nincs rá emlékeztető, miközben a cetlik a táblára kerülnek (:278, :442). A javasolt NEW elhagyja a „résztvevőnél marad” alternatívát, így nem szó szerinti. | A §5 2. pontjába, a „(opcionális) doboz a kilépőkártyáknak.” sor után új sor, a :145 szó szerint: „* Johari-cetlik: a személyes cetli a résztvevőnél marad, vagy a peula végén visszakerül hozzá; névvel nem tesszük ki, és nem gyűjtjük be.” Új szabály, időbontás és megsemmisítési szöveg nem kerül be.

QA-BIZT-5 | MEGERŐSÍTVE | emberi-döntés | P2 | Ezek a GYV-11 (F) elemei a döntésen túlmenő végrehajtási kérdések: a jogosult Memuna-eljárás, a korlátozás vagy helyesbítés módja, a törlés és a megőrzés, a pótlási út mechanikája és a próbálkozás beszámítása. Gazdáik: Memuna + DPO, a kapueredményre az értékelési felelős. A követelmény maga a kánoni körben az ADV §5-be kerül (plan Block 37). | Korlát: a KAPU-ba nem kerül kitalált eljárás. Döntési igény: Memuna + DPO (korlátozás, törlés/megőrzés), értékelési felelős (pótlási út, beszámít-e a próbálkozás).

QA-BIZT-6 | MEGERŐSÍTVE | bizonyíték-kapu | P1 | A HUM:617 kimondja: a 16 bizonyíték- és aláírás-bejegyzés nyitott G1–G8 kapu. A felsorolt szerepek (Memuna, DPO/jogi felelős, LMS-gazda, programvezető, értékelési felelős) írásos bizonyítéka hiányzik. | Nem javítható: RELEASE-READINESS G1/G2/G3 és a tracker. „Megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő.”

QA-ERT-1 | RÉSZBEN (az M1.A-rész duplikátum → QA-NYELV-5 a megtartandó) | objektív | P2 | Az M1.A:541 a régi 1–2 mondatos hossz maradványa, ez valós. Az M1.B:22 és a HUB:159 viszont nem hibás: az „SBI-mondat” az M1.B és a KAPU bevett neve egy SBI-ra (M1.B:155, :210, :350, :479, :510; KAPU:177, :219), és a :350/:359 szerint egy „SBI-mondat” 2–3 mondat. A két hely önálló cseréje terminológiai széttartást okozna. | Csak az M1.A:541, a QA-NYELV-5 szerint. Az M1.B:22-höz és a HUB:159-hez nem nyúlunk.

QA-ERT-2 | RÉSZBEN | objektív | P2 | Az ERT-13 csere után az M1.4:450 „2–3 mondatos”, a formátumváz és a példa (:478–484) viszont egymondatos. Ez a 7. regressziós minta. A döntés második mondata („a mondatszám csak instrukció”) csak a KAPU:21-ben áll. Az M1.3 SLIDE 5 vezetett egymondatos váz, és a terv szándékosan nem változtatja: az a rész nem kell. | M1.4:450: OLD „fogalmazol meg egy konkrét helyzetre.” → NEW „fogalmazol meg egy konkrét helyzetre (a mondatszám csak útmutatás, nem pontozzuk).” A példához, a formátumhoz, a rubrikához és a KAPU 4.1-hez nem nyúlunk; az M1.3-hoz sem. Utána `--pin-visible`.

QA-ERT-3 | MEGERŐSÍTVE | bizonyíték-kapu | P2 | Az ERT-14 sora szó szerint: „de a rubrikát az értékelési felelősnek kell jóváhagynia” (QA: módszertani lektor). A jóváhagyás írásos bizonyítéka nincs meg. A BIZT-6 ezt a szerepet az ERT-14-re nem sorolja fel, ezért nem duplikátum. | Nem javítható, és pontozási szabály nem kerül be. RELEASE-READINESS G-kapu és a tracker.

QA-ERT-4 | ELVETVE | — | — | Az M1.4:608 példáját az eb4fa6d nem érintette, a baseline ismeretlen. Az ERT-14 a mintaválaszra szól. Rubrikahorgony cseréje új alkalmazási eset volna (az ERT-15 szerint a horgonykalibráció nyitott). A kár sem bizonyított: a H5P-kvíz ✅ opciója (M1.4:341) a B-helyzetre már kész B-részt mutat. | Nincs.

QA-ERT-5 | RÉSZBEN | objektív | P2 | Az eb4fa6d az ERT-16-ot mindkét rubrikapéldányba átvezette, az ERT-15 „Nincs kettős levonás” bekezdését csak a KAPU:83-ba. Így az M1.4:628 azonos magyarázó doboza eltér. A szintleírás (KAPU:88, M1.4:634) és a §5 Moodle-leírás módosítása viszont az ERT-15 (F) nyitott kalibrációja: értékelési felelős + módszertani lektor. | A M1.4:628 blokkidézet után új sorok, a KAPU:83 szó szerint: „>\n> **Nincs kettős levonás:** ugyanazért az enyhe minősítő szóért csak egyszer vonj le. Ha a minősítés a viselkedés leírásába csúszik be, azt a 2. sor (B) viseli; a hangnem-sor emiatt csak akkor kerül „Erős” alá, ha a szövegben ettől független, önállóan igazolható kommunikációs hiba is van.” Tilos: a szintleírások, a horgonypéldák és a §5.

QA-ERT-6 | MEGERŐSÍTVE | objektív | P2 | Az ERT-16 olvasata: idő VAGY hely ÉS szakasz. Ehhez képest az M1.3:1027 és a KAPU:201 „konkrét hely és idő”-t kér, szakaszt nem, a HUB:117 pedig „van-e hely és idő”-t. A KAPU:202 erre „kapuérett”-et mond. | M1.3:1027 és KAPU:201: OLD „Van benne **konkrét hely és idő** (S)?” → NEW „Kiderül, **mikor vagy hol** (vagy mindkettő), és **a helyzet melyik szakaszában** történt (S)?”. HUB:117: OLD „van-e hely és idő” → NEW „kiderül-e, mikor vagy hol, és a helyzet melyik szakaszában”. A másik három ponthoz nem nyúlunk. Utána `--pin-visible`.

QA-ERT-7 | MEGERŐSÍTVE (QA-NYELV-6 a duplikátuma; ez a megtartandó) | objektív | P2 | A KAPU:132 cím „completion”-t ígér, miközben az ERT-4 (F) után a :28 és a :134 szerint nincs activity és nincs manifest-sor. A címre horgonylink nem mutat (grep). | KAPU:132: OLD „(formatív / completion – NEM a kapu)” → NEW „(formatív szerzői itempool – NEM a kapu)”. A :30-hoz, az itemekhez és a ✅-okhoz nem nyúlunk.

QA-NYELV-1 | MEGERŐSÍTVE (megtartandó; a QA-BIZT-3 ide olvad) | objektív | P2 | Lásd a QA-BIZT-3-at. Ez a NEW szám szerint egyeztet, a :161 „haladás” szavát használja, és az ADV-2 „csak … minimális hiánylista” fordulatát. | M1.F:159: OLD „a tanuló és a képző lássa a kiindulópontot – a kapun kapott visszajelzést és a leckék állását –” → NEW „a tanuló lássa a kiindulópontját (a kapun kapott visszajelzést és a leckék állását), a képző pedig csak a haladást és a minimális hiánylistát –”. A „**nyilvános státuszjelölés nélkül**” változatlan.

QA-NYELV-2 | RÉSZBEN | objektív | P2 | A három peulában nincs meg a blokk. A GK:63 (GYV-6 forrás) „tanulói … blokk: §4.3” minősítője az átvezetéskor kiesett. A javasolt NEW-ból hiányzik a §4.3-mutató; a kánoni alak az M4-precedens (M4.F:80). | M1.A:509, M1.B:392: OLD „(a „Ha ez a téma téged is érint” blokk szerint)” → NEW „(a tanulói „Ha ez a téma téged is érint” blokk: `Gyermekvédelem – release gate.md` §4.3)”. M1.F:109 ugyanígy, a pontosvessző előtt.

QA-NYELV-3 | ELVETVE | — | — | Az M1.F:66 a PRG-5 döntés szó szerinti átvezetése („1:1 kiskorúval csak a meglévő HUM-SAFE-02 kivétel szerint”). A javasolt NEW (KAPU:24, az általános szabály) más szabály, mint a HUM-SAFE-02 előre meghatározott kivétellistája (GK:115). Gyermekvédelmi jelentést változtatna. | Korlát: a NEW nem használható, a döntési szöveg marad.

QA-NYELV-4 | MEGERŐSÍTVE | objektív | P2 | Ugyanaz a lista az eb4fa6d-ben két néven került be: :101 „minimális hiánylista”, :161 „a nem teljesült kapufeltételek minimális listája”. Ez sérti az „egy fogalomra egy megnevezés” szabályt. | M1.F:161: OLD „a nem teljesült kapufeltételek minimális listáját” → NEW „a résztvevők minimális hiánylistáját (melyik kapufeltétel nem teljesült)”.

QA-NYELV-5 | MEGERŐSÍTVE (megtartandó; a QA-ERT-1 M1.A-része ide olvad) | objektív | P2 | Az M1.A:541 a régi 1–2 mondatos hosszt ígéri, az ERT-13 kánoni hossza 2–3 mondat. A darabszám (min. 1, max. 2 SBI, M1.4:469) megmarad. | M1.A:541: OLD „1–2 ilyen visszajelző mondatot írni.” → NEW „1–2 ilyen visszajelzést írni.”

QA-NYELV-6 | MEGERŐSÍTVE (duplikátum → QA-ERT-7) | objektív | P2 | Ugyanaz, mint a QA-ERT-7. | A QA-ERT-7 javítása.

QA-NYELV-7 | MEGERŐSÍTVE | objektív | P2 | A GYV-21 betoldás (eb4fa6d) zárójelet tett zárójelbe, és az „azokat” névmás messze került az előzményétől. Ez regresszió. A NEW a tartalmat és a korlátot megtartja. | M1.A:374, a javasolt NEW szerint: „…Írj mellé 1–2 újat is, lehetőleg a saját kvucádra szabva, és azokat is olvasd fel. Az új mondatok kitalált vagy általánosított helyzetről szóljanak, amelyről senkire nem lehet ráismerni: egy kis közösségben név nélkül is könnyen kiderül, kiről van szó.)*”

QA-NYELV-8 | ELVETVE | — | — | Az „önmagában nem kompetencia” az ERT-14 döntés szó szerinti szövege. A finding maga mondja, hogy „a jelentés nem torzul”. Ízlésbeli átírás. | Nincs.

QA-NYELV-9 | MEGERŐSÍTVE | objektív | P2 | Szám-egyeztetési hiba („SBI-váza van, és ezt viszik tovább”) az eb4fa6d által módosított `@asset` spec-sorban. A hiba eredetileg is ott volt, a commit átvitte. | M1.3:938: OLD „és ezt viszik tovább” → NEW „és ezt viszi tovább”. Utána `media_manifest.py build`, külön `chore(media)` commitban.

QA-NYELV-10 | ELVETVE | — | — | A „voltunk” eredetileg is ott volt, és nem a tanuló másolja be: ez a súgó kérdése. A töredékes kitöltés feltételezés (bizalom: alacsony). A változtatás a PRG-16 nyitott QA-jú sablonját és a MUNK-01-et is érintené. | Nincs.

QA-NYELV-11 | ELVETVE | — | — | A „személyes munkapéldány” az ADV-11 döntés szó szerinti kifejezése. A precedens (M6:QA-NYELV-5) szerint az értelmezése nem nyitott emberi döntés. | Nincs.

**Összesítés:**
- **Verdiktek:** 13 MEGERŐSÍTVE, 6 RÉSZBEN, 5 ELVETVE.
  - MEGERŐSÍTVE: BIZT-2, BIZT-3, BIZT-5, BIZT-6, ERT-3, ERT-6, ERT-7, NYELV-1, NYELV-4, NYELV-5, NYELV-6, NYELV-7, NYELV-9.
  - RÉSZBEN: BIZT-1, BIZT-4, ERT-1, ERT-2, ERT-5, NYELV-2.
  - ELVETVE: ERT-4, NYELV-3, NYELV-8, NYELV-10, NYELV-11.
- **Típus:** 1 emberi-döntés (BIZT-5), ebből 0 bizonyíték-kapu; 2 bizonyíték-kapu (BIZT-6, ERT-3). A többi megerősített vagy részben megerősített finding objektív.
- **Duplikátumok:**
  - QA-BIZT-3 ↔ QA-NYELV-1: a NYELV-1 marad.
  - QA-ERT-1 (M1.A-rész) ↔ QA-NYELV-5: a NYELV-5 marad.
  - QA-ERT-7 ↔ QA-NYELV-6: az ERT-7 marad.

Hivatkozott fájlok:
- 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- 02 Tervezet/Gyermekvédelem – release gate.md (:63, :102, :115)
- 02 Tervezet/Emberi jóváhagyás szükséges.md (14. szakasz: :617, :634–686, :725)
- 02 Tervezet/Modulok/M4/Peulák/M4.F – Felzárkóztató peula – Test, hang, kérdések & peulabemutató (Study Lab).md:80 (precedens)

## C. Nyers lencse-kimenetek (szó szerint)

<!-- agent aa09d6adbe52aa146 -->

M1 célzott QA, biztonság-jog lencse (eb4fa6d, AP-2026-10-12-01). Read-only voltam, semmit nem szerkesztettem.

**Mi rendben van:** a következő döntések szó szerint vagy a döntés szövegével kerültek át, és védelem nem gyengült: GYV-12 (M1.3), GYV-13, GYV-21, GYV-22, GYV-6, ADV-4, ADV-8, ADV-11, PRG-5, valamint az M1.4:510-be betoldott ADV-1 mondat.
- GYV-12: az M1.3:913 mondata betűre egyezik az ADV §11:241 utolsó mondatával. A döntési csomag 212. sora pontosan ezt a mondatot nevezi meg.
- Az M1.3-ból kikerült „enyhébb, fiktív verzió” helyett erősebb védelem áll: a mező most már csak kitalált helyzetet enged, és a HUM-SAFE-03 blokk (:915) megmaradt.
- Az M1 tanulói szövegében nincs olyan mondat, amely tagadná az admin hozzáférését (rákerestem: „csak … látja”, „senki más”, „csak nálad”).

---

**M1:QA-BIZT-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md:900–905` (NAR-05 `@source`); a mező előtti tájékoztató előírása: `02 Tervezet/LMS – activity manifest.md:48`
- **Probléma:** Az ERT-12 átvezetése félkész. A tárolt, névhez kötött mini-SBI-hez két tanulói felület még mindig valós helyzetre hív, ellentétben az új :885-ös utasítással.
- **Bizonyíték:**
  - M1.3:901: „Gondolj egy helyzetre, ami eszedbe jut – vagy találj ki egy egyszerű, kisebb sztorit.”
  - MAN:48: „…a lecke kikötése: „név és felismerhető részlet nélkül”; … nyitott: kerülhet-e ide valós, névtelenített helyzet”
- **Hatás:** A tanuló egymásnak ellentmondó utasítást hall és lát. A build a mező elé a régi, valós helyzetet megengedő kikötést írná. Így névhez kötött, visszaazonosítható adat kerülhet a Moodle-be.
- **Javaslat:** Hangszöveget nem szabad ad hoc szerkeszteni. A NAR-05 a VO-fix packkal változik (a terv VO_PACK sora: „Találj ki egy egyszerű, kisebb sztorit.”), a MAN:48 a kánoni körben (terv #13). Amíg mindkettő nincs kész, az M1 learner release blokkolt. A ledgerben ez a két tétel nyitott release-blokkolóként szerepeljen.
- **Típus:** objektív (a döntés lezárt PROJEKT-DÖNTÉS, az ellentmondás a fájlokból bizonyítható)

**M1:QA-BIZT-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:514–515`
- **Probléma:** A #39 kihagyása után az M1.4-ben megmaradt az egyedi „ha nehéz” mondat. Ez ellentmond a GK §4.3:102 lezárt, 2026-10-02-i döntésének: „Minden meglévő, ad hoc „ha nehéz / ha téged is érint / ha felkavar” típusú támogató blokk helyére ez kerül”. A mondat „személyes” szava ráadásul az enyhébb valós helyzet beírását sugallja, szemben a :465-tel és a HUM:462-vel.
- **Bizonyíték:** „Ha nagyon nehéz vagy személyes helyzet jut eszedbe, nyugodtan válassz / egy **enyhébb, egyszerűbb szituációt**.”
- **Hatás:** Az M1.3 és az M1.4 kétféle biztonsági üzenetet ad. A MUNK-01 sablon spec szerint szó szerint átveszi ezt a blokkot, így a hiba a letölthető sablonba is továbbmegy.
- **Javaslat:** A kihagyás indoka (a GYV-12 csak az M1.3-at nevezi meg) a GK §4.3:102-re nem érvényes. Ennek alapján a két sor törölhető. A :516-os Memuna-mondat és a :518-as §4.3 blokk marad. Ha a verifier új alkalmazási esetnek látja: EMBERI DÖNTÉS: a Memuna (a programvezetővel) döntse el, vonatkozik-e a GK §4.3:102 az M1.4:514–515-re.
- **Típus:** objektív

**M1:QA-BIZT-3**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md:159`
- **Probléma:** Az ADV-2 átvezetése (:100, :161) után ugyanennek a blokknak a „Cél” sora még azt mondja, hogy a képző a teljes kapus visszajelzést látja. Ez ellentmond a közvetlenül utána álló :161-nek.
- **Bizonyíték:** „**Cél:** a tanuló és a képző lássa a kiindulópontot – a kapun kapott visszajelzést és a leckék állását”
- **Hatás:** Az F-peula képzője ellentmondó utasítást kap arról, mennyi adatot nézhet meg.
- **Javaslat:** OLD: „a tanuló és a képző lássa a kiindulópontot – a kapun kapott visszajelzést és a leckék állását –” → NEW: „a tanuló lássa a kapun kapott visszajelzését, a képző a nem teljesült kapufeltételek minimális listáját, és mindketten a leckék állását –”. A NEW csak a :161 meglévő szóhasználatát veszi át (ADV-2).
- **Típus:** objektív

**M1:QA-BIZT-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md:145` (a szabály); a folyamat: :278, :442, 4.4.2 (:511–555), §5 (:559–)
- **Probléma:** Az ADV-7 szabálya csak az Eszközök listájában áll. A folyamatban a cetlik a táblára kerülnek (a Rejtett mezőbe is), a képző leemel közülük. Sem a zárásban, sem a képzői ellenőrző listában nincs olyan lépés, amely a cetliket visszajuttatná.
- **Bizonyíték:**
  - :145: „a személyes cetli a résztvevőnél marad, vagy a peula végén visszakerül hozzá”
  - :442: „A képző **leemel néhány cetlit**”
- **Hatás:** A szabály végrehajtatlan marad. Kézírással visszaazonosítható, önfeltáró cetlik maradhatnak a táblán vagy a képzőnél.
- **Javaslat:** A §5 „Megvannak-e az eszközök?” pontjába vagy a 4.4.2 végére kerüljön be ugyanez a szabály szó szerint, például: „Johari-cetlik: a peula végén visszakerülnek a résztvevőkhöz; névvel nem tesszük ki, és nem gyűjtjük be (ADV-7).” Ez közvetlen következmény-frissítés, új szabály nélkül. A megsemmisítésről ne írj semmit.
- **Típus:** objektív

**M1:QA-BIZT-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:27`
- **Probléma:** A GYV-11 óvatos alapértelmezéséből csak a megőrzési oldal került a KAPU-ba („nem törlünk automatikusan”). A döntésben ugyanígy előírt „szükség szerinti korlátozás” nem került be. A KAPU által hivatkozott ADV §5 („kikerül a Moodle-ből”) és az új mondat viszonyát sem tisztázza a szöveg. A „feltárásmentes pótlási út” mechanikája sincs leírva, pedig a Próbálkozás-szabály szerint a javító próbálkozás csak az F-peula után nyílik.
- **Bizonyíték:** „a tanuló biztonságos, feltárásmentes pótlási utat kap. Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan.” A döntés (HUM:634): „szükség szerinti korlátozás/helyesbítés és adatvédelmileg jóváhagyott törlés/megőrzés kell”.
- **Hatás:** Az értékelő úgy olvashatja, hogy a feltárást tartalmazó beadás korlátozás nélkül a Moodle-ben marad (a mentor, a második képző és az admin is látja). Ekkor az LMS de facto nyilvántartássá válik. Az sem világos, hogy a feltárást tartalmazó próbálkozás elhasználja-e a normál próbálkozást.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna és a DPO döntsön a jogosult eljárásról, a beadás korlátozásáról és a törlés vagy megőrzés módjáról. Az értékelési felelős döntsön a pótlási útról és arról, beszámít-e a feltárást tartalmazó próbálkozás. Bizonyíték: a GYV-11 sor. Addig a KAPU-ba ne kerüljön kitalált eljárás.
- **Típus:** emberi-döntés

**M1:QA-BIZT-6**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md:601–725` (14. szakasz, „Utólagos ellenőrzés (vétó/QA)” oszlop), az M1-ben átvezetett sorok
- **Probléma:** Az átvezetett döntésekhez hiányzik a megnevezett szerepek írásos bizonyítéka:
  - Memuna: GYV-6, GYV-12, GYV-13, GYV-21, GYV-22 és a szereplési szorongás küszöbe;
  - DPO / jogi felelős: ADV-1, ADV-2, ADV-4, ADV-7, ADV-8, ADV-11, ERT-12 vétó, GYV-11, GYV-21;
  - LMS-gazda: az ADV-1 staging role-matrixa (addig az M1.4:510 felsorolása, a szerkesztő tanár, a menedzser és a Memuna nélkül, csak feltételes), az ADV-2 csoport-hozzáférés teszt és az F-peula szereposztása / vészhozzáférése, valamint az ADV-11 kivételteszt;
  - programvezető: a PRG-5 kapacitás és pótlási felelős;
  - értékelési felelős: a GYV-11 kapueredmény-része.
- **Bizonyíték:** „Amit a szakasz nem zár le: … a táblázat alatti 16 bizonyíték- és aláírás-bejegyzést” (HUM:617). Az ADV-1 sor: „A „csak mentorod látja” ígéretet a tényleges RBAC-hoz kell igazítani a staging role-matrix után.”
- **Hatás:** Megvalósítási döntés: a projektgazda jóváhagyta; a formális szerepköri bizonyíték függő. Amíg nincs meg, az M1 nem kiadható tanulóknak.
- **Javaslat:** Nem javítható. A `RELEASE-READINESS.md` G1 (Memuna), G2 (DPO) és G3 (LMS / runtime) kapuihoz és a tracker-issue-hoz tartozik. Ne írd be és ne feltételezd.
- **Típus:** bizonyíték-kapu

---

**Állítás-besorolás:**
- PROJEKT-DÖNTÉS: a HUM 14. szakasz sorai és a GK §4.3:102.
- TÉNY (fájlból): az idézett ellentmondások.
- EMBERI JÓVÁHAGYÁS KELL: a QA-BIZT-5 tárgya, és a QA-BIZT-2, ha a verifier új alkalmazási esetnek látja.

Webkutatást nem végeztem. Egyik finding sem igényelt új tárgyi jogi vagy szolgáltatási tényt.

**Fájlok (abszolút úttal):**
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md

<!-- agent a5dd4e152e264e974 -->

## M1 célzott QA, értékelési és LMS-lencse: a HUM 14. szakasz átvezetése (eb4fa6d)

7 findingot találtam, mind P2. Hat objektív, egy bizonyíték-kapu; IMPL-finding nincs. Nem szerkesztettem semmit.

Fájlrövidítések (a teljes utak a lista végén): KAPU, HUB, M1.3, M1.4, M1.A, M1.B.

---

**M1:QA-ERT-1**
- **Súlyosság:** P2
- **Bizalom:** magas (M1.A); közepes (M1.B, HUB)
- **Lencse:** értékelés
- **Hely:** M1.A:540–541; M1.B:22 (vö. M1.B:359); HUB:159
- **Probléma:** Az ERT-13 után is maradt „1–2 … mondat” a modulban.
  - Az M1.A hídja tanulóknak szóló szövegben 1–2 visszajelző mondatot ígér, közvetlenül a TERM-2 miatt módosított :536-os sor mellett.
  - Az M1.B célja „1–2 … SBI-mondat”, miközben ugyanennek a fájlnak a :359-es sora már „2–3 mondatban”-t ír.
- **Bizonyíték:**
  - M1.A:540–541: „Ott konkrétan meg fogod tanulni, hogyan lehet / 1–2 ilyen visszajelző mondatot írni.”
  - M1.B:22: „Tud legalább **1–2 rövid, használható SBI-mondatot** megfogalmazni” ↔ M1.B:359: „Megpróbál **2–3 mondatban**”
- **Hatás:** A peulán 1–2 mondat, az M1.3–M1.4-ben 2–3 mondat a cél. Az „SBI-mondat” kétértelmű: darabszámot vagy mondatszámot jelent. Az M1.4-ben épp ezért cserélték „SBI”-re.
- **Javaslat:**
  - M1.A:541: „1–2 ilyen visszajelző mondatot írni” → „1–2 ilyen visszajelzést írni”.
  - M1.B:22: „1–2 rövid, használható SBI-mondatot” → „1–2 rövid, használható SBI-t”.
  - HUB:159: „legalább 1–2 használható SBI-mondatot” → „legalább 1–2 használható SBI-t”.
  - Ez a csomag M1.4-es „SBI-mondat → SBI” mintája.
  - Tilos: a darabszám (1–2) és az időkeret.
  - Az M1.4:434 (NAR-03 hangszöveg) a hangcsomag útján javul, a tervben nyilvántartva.
- **Típus:** objektív

**M1:QA-ERT-2**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.4:450 ↔ :476–484; mellékesen M1.3:45 ↔ :799–804, :1019
- **Probléma:** A feladatszöveg 1–2 mondatról 2–3-ra változott. A közvetlenül alatta álló „Formátum – javaslat” és „Például” egy mondat maradt. A döntés második mondata („a mondatszám csak instrukció”) csak a KAPU:21-ben áll, a tanulói leírásban nem.
- **Bizonyíték:**
  - M1.4:450: „Ebben a feladatban **2–3 mondatos SBI-visszajelzést** fogalmazol meg”
  - M1.4:483–484: „„Amikor ma a játék közben háromszor félbeszakítottad a többieket, / nagyon nehéz volt megtartani a figyelmüket.”” (egy mondat)
- **Hatás:** Cím és példa szétválik (a hungarian-editorial 7. regressziós mintája). A tanuló nem tudja, elég-e egy mondat. Az értékelő a leírásból mondatszám-követelményt olvashat ki, vagyis éppen az ERT-13 által tiltott pontozott küszöböt.
- **Javaslat:**
  - Az M1.4:450 végére a KAPU:21 kikötése, tanulói nyelven: „… egy konkrét helyzetre (a mondatszám csak útmutatás, nem pontozzuk).”
  - Tilos: a példa, a formátum, a rubrika és a KAPU 4.1 egymondatos átmenő mintája.
  - Az M1.3 SLIDE 5 „Kötelező sablon (1 mondat)” és a SLIDE 7 „Ellenőrizd a saját mondatod!” ugyanígy egy mondatot gyakoroltat a „2–3 mondatos” mikrocél mellett. Ha kell, oda is ugyanez a zárójel.
- **Típus:** objektív

**M1:QA-ERT-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** KAPU:305 (§5) ↔ KAPU §1, a rubrikasorok (:47–89)
- **Probléma:** Az ERT-14 szabálya azt mondja, hogy az adaptációt „a rubrikával” értékeld. Egyik rubrikasor és szint sem írja le viszont az adaptációt. A sorok szövegjegyei szerint a szó szerint bemásolt leckeminta (M1.4:483–484) átmenő pontot kaphat.
- **Bizonyíték:**
  - KAPU:305: „A rubrikával azt értékeld, mennyire igazította a tanuló a mintát a saját választott helyzetéhez”
  - KAPU:36: „A rubrika **megfigyelhető szövegjegyeket** pontoz”
- **Hatás:** Két értékelő ugyanarra a bemásolt beadásra eltérő kapueredményt adhat. Így a „bemásolás nem kompetencia” elv hamis teljesítés felé csúszhat.
- **Javaslat:**
  - Az ERT-14 lezárt döntés, nem nyitom újra. A döntés szerint „a rubrikát az értékelési felelősnek kell jóváhagynia”.
  - Hiányzik az értékelési felelős írásos jóváhagyása arról, hogyan alkalmazandó a szabály a rubrikaszinteken (QA: módszertani lektor). Megfogalmazás: „megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő”.
  - Addig nem írunk be kitalált pontozási szabályt.
  - Mellékesen: a KAPU-ban a „a lecke kész mintáját” nem mondja meg, melyik leckéről van szó.
- **Típus:** bizonyíték-kapu

**M1:QA-ERT-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.4:604–608 ↔ KAPU:65 (és KAPU:104, „Ez a fájl a hivatalos rubrika.”); a kapuhelyzet: M1.4:137–138
- **Probléma:** Az ERT-14 kicserélte a kapuhelyzettel azonos mintát (:483–484). A lecke rubrikamásolatában azonban a B-sor „Erős” példája a „Kinevetés a körben” kapuhelyzet kész B-része maradt, és eltér a KAPU-horgonytól.
- **Bizonyíték:** M1.4:608: „Pl.: „Ma a kör alatt háromszor kinevetted a többieket, amikor ők beszéltek.”” ↔ KAPU:65: „„A kör alatt háromszor félbeszakítottad a többieket, amikor ők beszéltek.””
- **Hatás:** Ha a rubrikát ebből a másolatból viszik be (a tanuló előnézetben látja), a tanuló kész „Erős” B-részt kap a B kapuhelyzetre. A két rubrikaváltozat kalibrációja is eltér.
- **Javaslat:**
  - Az M1.4:608 példáját szó szerint a KAPU:65 horgonyára kell igazítani.
  - Tilos: a szintnév, a pont és a szintleírás.
  - Bizalom közepes, mert nem egyértelmű, hogy a 4.2 bekerül-e a tanulói nézetbe.
- **Típus:** objektív

**M1:QA-ERT-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** KAPU:83 ↔ :88; KAPU:301; M1.4:633–635
- **Probléma:** A „Nincs kettős levonás” szabály (ERT-15) csak a szintleírásokon kívüli magyarázó idézetblokkban áll.
  - A hangnem „Rendben” szintleírása (KAPU:88, M1.4:634) továbbra is levon az „enyhe minősítés” miatt.
  - Az M1.4 4.2 4. sorából hiányzik a szabály, holott az ERT-16-ot ugyanide átvezették.
  - A §5 szerint a Moodle-rubrikába csak a szintleírások kerülnek.
- **Bizonyíték:**
  - KAPU:88: „de van benne egy-egy éles/szúrós fordulat vagy enyhe minősítés.”
  - KAPU:301: „vidd be a fenti 4 sort, soronként 0/1/2 ponttal és a szintleírásokkal.”
- **Hatás:** A Moodle-ban pontozó értékelő ugyanazért a szóért kétszer vonhat le. Példa: 1/1/1/1 = 4/8, „Még nem” lesz a szabály szerinti 1/1/1/2 = 5/8, „Teljesítve” helyett. A tiltott kettős levonás így megfordíthatja a kapueredményt.
- **Javaslat:**
  - A hangnem „Rendben” leírásához (KAPU:88, M1.4:634) utalás: „… vagy enyhe minősítés (ha nem ugyanaz a szó, amelyet a 2. sor már levont)”.
  - Az M1.4 4.2 4. sorába a KAPU:83 mondata, szó szerint.
  - A §5-ben: a „Nincs kettős levonás” mondat a 4. kritérium Moodle-leírásába is kerüljön be.
  - Tilos: a horgonypéldák (KAPU:64, :88) egységesítése. Az a döntés szerint az értékelési felelős és a módszertani lektor kalibrációja.
- **Típus:** objektív

**M1:QA-ERT-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.3:1027; KAPU:201–202 (Item 6); HUB:117
- **Probléma:** Az ERT-16 szerint a konkrét S: idő vagy hely (mindkettő is lehet) ÉS a helyzet releváns szakasza (KAPU:55, M1.4:490, :594). A formatív önellenőrzés ehelyett hely ÉS időt kér, szakaszt pedig nem.
- **Bizonyíték:**
  - M1.3:1027: „⬜ „Van benne **konkrét hely és idő** (S)?””
  - KAPU:201–202: „1. Van benne **konkrét hely és idő** (S)? … Ha mind a 4-re „igen”, akkor kapuérett az SBI-vázad”
- **Hatás:** Két irányban félrevezet.
  - „ma, a kör második felében” a rubrika szerint Erős, a lista szerint „nem”.
  - „ma a peulán” a KAPU:55 pontozói példája szerint Rendben, a lista szerint „igen”, és az Item 6 „kapuérett”-nek nevezi.
- **Javaslat:**
  - Az M1.3:1027 és a KAPU:201 S-pontja az M1.4:490 megfogalmazásával: „Kiderül, **mikor vagy hol** (vagy mindkettő), és **a helyzet melyik szakaszában** történt (S)?”
  - HUB:117: „van-e hely és idő” → „kiderül-e, mikor vagy hol, és a helyzet melyik szakaszában”.
  - Tilos: a másik három pont és a nem pontozott megvalósítás.
  - A látható szöveg változik, ezért utána `--pin-visible` kell.
- **Típus:** objektív

**M1:QA-ERT-7**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** KAPU:132 (mellékesen :30)
- **Probléma:** Az ERT-4 után activity nincs, így completion sincs. A §3 címe mégis megtartja a kivett completion-ígéretet, közvetlenül a módosított bekezdés fölött.
- **Bizonyíték:** KAPU:132: „## 3. Kísérő item-bank (formatív / completion – NEM a kapu)” ↔ KAPU:134: „**Szerzői itempool: külön Moodle-activity és manifest-sor nem készül hozzá**”
- **Hatás:** A cím alapján a build completion-követett activityt építhet, ami ütközik az ERT-4 óvatos alapértelmezésével.
- **Javaslat:**
  - KAPU:132: „(formatív / completion – NEM a kapu)” → „(formatív szerzői itempool – NEM a kapu)”.
  - A :30 „a kvíz eredménye” fordulat nem létező kvízre utal; ez opcionális, kis súlyú.
  - Tilos: az itemek, a ✅ jelölések és a visszajelzések.
- **Típus:** objektív

---

### Összesítő megjegyzések (nem findingok)

- **Eltérés a manifesttől és a kánontól (a kánoni kör frissíti, a tervezett #82, #83, #35 blokk fedi):**
  - MAN:46 (LMS-M1-02) még „drag-free egyenértékű út kötelező” (PRG-9).
  - MAN:50 (LMS-M1-05): a completion még „leadva + megerősített kapueredmény”, fájlszám és fájltípus nincs megadva (ERT-9, LMS-1).
  - Az RA:81-ben még ott a „(pl. M1.2)” (PRG-9). A #83 után érdemes ellenőrizni, hogy az M1.2 SLIDE 5 rádiógombos útját (6 MC-elem egy CP-dián, mobilos skálázás, 24×24 px) más RA-pont lefedi-e.
- **Hangcsomag-maradványok (a tervben nyilvántartva):** M1.4:434 „1–2 mondatos”; M1.4:299 „elmondod a szituációt”.
- **TERM-2:** A ✅-os opciókban „szituáció” áll (KAPU:221, M1.3:1039, M1.B:224), a visszajelzés „helyzet”-et mond. Szinonimaként érthető, nem árulja el a kulcsot és nem okoz ellentmondást, ezért nem finding.
- **ERT-9:** Elsődleges forrás nélkül nem tudtam ellenőrizni, hogy a célverzión a kézi újranyitás („Grant attempts = Manually”) visszaállítja-e a `completionsubmit` állapotot gyakorló újrabeadásnál. Javaslom felvenni a G3b tanulói tesztfiókos visszaolvasásába.
- **Invariánsok:**
  - Nem változott a döntésen túl a ✅, az opciók, a küszöb (minden sor ≥1 ÉS ≥5/8), a szintnevek és pontok, a kaputípus és az időtartamok.
  - A HUB M1.A percbontása továbbra is 45 perc.
  - Az SBI-darabszám (minimum 1, maximum 2) az „SBI-mondat → SBI” csere után is változatlan.
  - A „4/5” célérték törlése a PRG-2 szerint történt.
- **Finding nélkül:** PRG-2, PRG-3, PRG-9 (a SLIDE 5 instrukciója, visszajelzései és @asset-jei egyeznek), PRG-16, LMS-1, ERT-17. Az ERT-14 új M1.4-es példája nem kapuhelyzet.
- **ERT-13, eltérés a csomagtól:** A csomag „Következmények” sora a KAPU 4.1 mintájának igazítását is említi, a terv ezt nem végezte el. A HUM-sor szövege nem írja elő, és az egymondatos átmenő minta összhangban van a „nem pontozott” mondatszámmal, ezért nem finding.

### Fájlok

- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md

<!-- agent abd92d3f6e2c75325 -->

Az M1 nyelvi QA-ja (HUM 14. szakasz, eb4fa6d) elkészült: 11 finding, 1×P1 és 10×P2. Csak a diff-hunkokat és a közvetlen környezetüket olvastam, fájlt nem szerkesztettem.

**M1:QA-NYELV-1**
- Súlyosság: P1 · Bizalom: közepes · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md:159` (vö. :101, :161)
- Probléma: A blokk „Cél” sora szerint a képző is látja a kapun kapott visszajelzést. Ez két sorral lejjebb ütközik az ADV-2 átvezetésével, amely szerint a képző csak a minimális hiánylistát nézi. A régi mondat bent maradt (7. minta: cím/cél és tartalom széttart).
- Bizonyíték: „**Cél:** a tanuló és a képző lássa a kiindulópontot – a kapun kapott visszajelzést és a leckék állását” · :161 „nézze át … a nem teljesült kapufeltételek minimális listáját”
- Hatás: A képző a célmondat alapján megnyitja a teljes kapus visszajelzést, így az adattakarékos alapértelmezés gyengül.
- Javaslat: OLD „a tanuló és a képző lássa a kiindulópontot – a kapun kapott visszajelzést és a leckék állását –” → NEW „a tanuló lássa a kiindulópontját (a kapun kapott visszajelzést és a leckék állását), a képző pedig csak a haladást és a minimális hiánylistát –”. A „**nyilvános státuszjelölés nélkül**” rész változatlan marad.
- Típus: objektív (ADV-2 következménye)

**M1:QA-NYELV-2**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `…/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md:509`; `…/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md:392`; `…/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md:109`
- Probléma: A határozott névelős „a … blokk” olyan blokkra mutat, amely egyik peulafájlban sincs meg; csak az online leckékben és a hubban áll. A kánoni forrás (GK:63) kiírja, hogy ez a tanulói blokk; az átvezetésből ez a jelző kiesett (2. minta: elveszett minősítő).
- Bizonyíték: M1.A:509 „biztonságos támogatási útra terelsz (a „Ha ez a téma téged is érint” blokk szerint)” · GK:63 „(a tanulói „ha téged is érint” blokk: §4.3)”
- Hatás: Élő peulán a képző nem tudja, melyik blokkot kövesse.
- Javaslat: Mindhárom helyen OLD „(a „Ha ez a téma téged is érint” blokk szerint)” → NEW „(a tanulói „Ha ez a téma téged is érint” blokk szerint)”. A mondat többi része változatlan marad, köztük a többes számú „nem küldünk ki”, mert az szándékosan közös felelősséget jelöl.
- Típus: objektív

**M1:QA-NYELV-3**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Peulák/M1.F – …(45’).md:66`
- Probléma: A „meglévő kivételei” fejlesztői metanyelv: a szerkesztőnek szólt, hogy ne találjon ki új kivételt. A képző ebből nem tudja meg, mik a feltételek, pedig ugyanez a fájl és a KAPU is kiírja őket.
- Bizonyíték: „kiskorúval 1:1 csak a safer-working szabály meglévő kivételei szerint (HUM-SAFE-02);”
- Hatás: A képző nem tudja végrehajtani az utasítást, mert nem derül ki belőle, mikor és hogyan szabad kettesben lenni.
- Javaslat: OLD „kiskorúval 1:1 csak a safer-working szabály meglévő kivételei szerint (HUM-SAFE-02);” → NEW „kiskorúval kettesben (1:1) csak indokolt esetben, átlátható módon és egy másik felelős tudtával (safer-working szabály, HUM-SAFE-02);”. Ez a KAPU:24 kánoni mondata szó szerint. A pótidőpont és a mentoros út nem változik.
- Típus: objektív

**M1:QA-NYELV-4**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Peulák/M1.F – …(45’).md:101` és `:161`
- Probléma: Ugyanaz a lista egy fájlon belül két néven szerepel.
- Bizonyíték: :101 „átnézi a résztvevők minimális hiánylistáját” · :161 „a nem teljesült kapufeltételek minimális listáját”
- Hatás: Két külön dokumentumnak tűnhet.
- Javaslat: :161 OLD „a nem teljesült kapufeltételek minimális listáját” → NEW „a résztvevők minimális hiánylistáját (melyik kapufeltétel nem teljesült)”. Ha a NYELV-1 javítása bekerül, abban is ez a név álljon.
- Típus: objektív

**M1:QA-NYELV-5**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Peulák/M1.A – …(45’).md:540–541` (a TERM-2 hunk közvetlen környezete)
- Probléma: Az ERT-13 után a kánoni hossz 2–3 mondat. Az M1.A hídja ennek ellenére „1–2 visszajelző mondatot” ígér. Az ERT-13 csomag ugyanezt az esetet az M1.4-ben úgy vezette át, hogy az „SBI-mondat” helyére „SBI” került (7. minta).
- Bizonyíték: „Ott konkrétan meg fogod tanulni, hogyan lehet / 1–2 ilyen visszajelző mondatot írni.”
- Hatás: A peulán más hosszt hallanak, mint ami a leckében és a kapuban áll.
- Javaslat: OLD „1–2 ilyen visszajelző mondatot írni” → NEW „1–2 ilyen visszajelzést írni”. Az 1–2-es darabszám marad (min. 1, max. 2 SBI), a mondatszám nem kerül bele.
- Típus: objektív

**M1:QA-NYELV-6**
- Súlyosság: P2 · Bizalom: magas (a fejlécre) · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:132` (továbbá :30, :134)
- Probléma: Az ERT-4 után az item-bank szerzői itempool, activity és completion nélkül. A szakaszcím ennek ellenére még „completion”-t ír (7. minta).
- Bizonyíték: :132 „## 3. Kísérő item-bank (formatív / completion – NEM a kapu)” · :28 „külön Moodle-activity és manifest-sor nem készül hozzá”
- Hatás: A cím completion-alapú kvízt ígér, ami nem készül.
- Javaslat: OLD „(formatív / completion – NEM a kapu)” → NEW „(formatív – NEM a kapu)”. Horgonylink nem mutat rá. A :30 („a kvíz eredménye”) és a :134 („a kvízbe egyik sem kerül át”) mondatához ne nyúljatok, amíg nem tisztázott, kerül-e item az itempoolból lecke-H5P-be; a kapudöntésről szóló állításuk addig is igaz.
- Típus: objektív

**M1:QA-NYELV-7**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `…/Peulák/M1.A – …(45’).md:374`
- Probléma: A GYV-21 betoldás után a képzői megjegyzésben zárójel áll zárójelen belül, egyetlen mondatban három betoldással. Az „azokat” névmás így messzire kerül az „1–2 újat” előzménytől.
- Bizonyíték: „…amelyről senkire nem lehet ráismerni (egy kis közösségben név nélkül is könnyen kiderül, kiről van szó), és azokat is olvasd fel.)*”
- Hatás: Felolvasva nehezen követhető, és az „azokat” elcsúszhat.
- Javaslat: NEW „*(Képzői megjegyzés: ezek a mondatok nagyrészt ugyanazok, mint a mikroleckében. Írj mellé 1–2 újat is, lehetőleg a saját kvucádra szabva, és azokat is olvasd fel. Az új mondatok kitalált vagy általánosított helyzetről szóljanak, amelyről senkire nem lehet ráismerni: egy kis közösségben név nélkül is könnyen kiderül, kiről van szó.)*”. A tartalom és a korlát nem változik.
- Típus: objektív

**M1:QA-NYELV-8**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/M1 – Kapu – értékelő (item-bank + rubrika).md:305`
- Probléma: Az ERT-14 szabálysorában három tükörfordítás-nyom van. A „közel szó szerinti” a „near-verbatim” mása. Az „önmagában nem kompetencia” kategóriahiba: a bemásolás nem kompetencia, hanem nem bizonyítja azt. A „saját választott helyzetéhez” jelzőhalmozás.
- Bizonyíték: „a mintaválasz szó szerinti vagy közel szó szerinti bemásolása önmagában nem kompetencia … a saját választott helyzetéhez”
- Hatás: A pontozói szabály nehezebben olvasható. Kisebb nyelvi zaj, a jelentés nem torzul.
- Javaslat: NEW „a mintaválasz szó szerinti vagy majdnem szó szerinti bemásolása önmagában még nem bizonyít kompetenciát. A rubrikával azt értékeld, mennyire igazította a tanuló a mintát az általa választott helyzethez (adaptáció, helyzetre szabás).”. Az értékelési szabály tartalma, a szint, a pont és a küszöb nem változik.
- Típus: objektív

**M1:QA-NYELV-9**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `…/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md:938` (az `M1.3-NAR-06` spec mezője; ezt a sort a commit módosította)
- Probléma: Szám-egyeztetési hiba (6. minta): az alany egyes számú („SBI-váza van”), az állítmány többes számú („viszik”).
- Bizonyíték: „akkor használható SBI-váza van, és ezt viszik tovább az M1.4 leckében és a beadandóban.”
- Hatás: A hanggyártási spec hibás mintát ad tovább.
- Javaslat: OLD „ezt viszik tovább” → NEW „ezt viszi tovább”. Ez `@asset` mező, ezért utána `media_manifest.py build` kell, külön `chore(media)` commitban.
- Típus: objektív

**M1:QA-NYELV-10**
- Súlyosság: P2 · Bizalom: alacsony · Lencse: nyelv
- Hely: M1.3:802 és :888; `…/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:478` és :531 (`M1.4-MUNK-01` spec)
- Probléma: A „, és te” elhagyása után a sablon („Amikor ___ (S) ___ (B), én / a kvuca ___ (I)”) csak határozói S-sel nyelvtanos. Az S-súgó viszont igét ad („voltunk”), és ez tagmondatos kitöltést kínál, ami összeütközik a B-réssel.
- Bizonyíték: „„**Amikor** ___ (S – mikor, hol, milyen helyzetben voltunk) / ___ (B – mit csináltál konkrétan),”” — a súgót visszhangzó kitöltéssel: „Amikor a peulán voltunk háromszor félbeszakítottad…”.
- Hatás: Egyes tanulók töredékes vagy vesszőhibás SBI-t írnak a mintára. A határozói kitöltés („ma a játék közben”) helyes mondatot ad.
- Javaslat: OLD „(S – mikor, hol, milyen helyzetben voltunk)” → NEW „(S – mikor, hol, milyen helyzetben)”. Az M1.4 szögletes zárójeles alakjában ugyanígy, a MUNK-01 specben szó szerint követve. A B- és az I-súgó, a mezőszám és a PRG-16 nyitott modulgazdai QA-ja nem változik.
- Típus: objektív

**M1:QA-NYELV-11**
- Súlyosság: P2 · Bizalom: alacsony · Lencse: nyelv
- Hely: `…/Peulák/M1.F – …(45’).md:80` (továbbá :10, :380)
- Probléma: A „személyes munkapéldány” a döntés (ADV-11) belső kifejezése. A szövegből nem derül ki, milyen konkrét tevékenység tilos; a letöltések törlését külön kimondja, tehát nem azt jelenti.
- Bizonyíték: „jelszót nem ment el, és nem hoz létre rajta személyes munkapéldányt”
- Hatás: A képző nem tudja érthetően kimondani a szabályt a résztvevőknek.
- Javaslat: EMBERI DÖNTÉS: mit jelent a gyakorlatban a „személyes munkapéldány”, hogy egyszerű szavakkal le lehessen írni. Kitől: az ADV-11 gazdái, az LMS-gazda és a DPO. Addig a szöveghez ne nyúljatok.
- Típus: emberi-döntés

Lencsén kívüli megjegyzés, nem NYELV-finding, csak ellenőrzésre. Két ponton a commit eltér a tervtől:
- Az M1.4:510 tanulói mondatához hozzákerült a „technikai okból a Moodle rendszergazdája is hozzáférhet” rész. A plan-M1 szerint ennek a mondatnak az ADV-1 alapján a staging role-matrixig változatlanul kellett volna maradnia.
- Az M1.4:514–515 „enyhébb, egyszerűbb szituációt” sora bent maradt, vagyis a GYV-12 #39-es blokkja nem került át. Ez rendben van, ha a fő session a B olvasatot választotta.
