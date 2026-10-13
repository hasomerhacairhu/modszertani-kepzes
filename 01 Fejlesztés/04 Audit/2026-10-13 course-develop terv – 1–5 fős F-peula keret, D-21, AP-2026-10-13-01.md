# /course-develop terv – közös, 1–5 fős F-peula keret (D-21, AP-2026-10-13-01)

> **Audit trail, nem kánon.** TERVEZET a projektgazda elfogadására (HUM 14 PRG-4: „a csomagtervet a projektgazda”; a
> projektgazda 2026-10-13-i iránya, D-21: „Készíts hozzá konkrét `/course-develop` tervet. A terv külön projektgazdai
> elfogadásáig ne indíts új tartalomgyártást.”). Tartalom nem készült: ez csak a terv. A `/course-develop` skillt kizárólag
> a felhasználó indíthatja; a javasolt indító argumentum a terv elején áll. A modulspecifikus betéteket az adott
> modulgazda, az 1:1 és a biztonsági részt a Memuna, a kapacitást a programvezető hagyja jóvá (PRG-5).

## Elfogadás

- **Projektgazda:** ELFOGADOM / MÓDOSÍTOM: … / ELUTASÍTOM a tervet (a 6a és 6b átszervezéssel, az E7 opcióval együtt).
- Elfogadás után: a felhasználó indítja a `/course-develop`-ot ezzel a tervvel; a skill review-kapui (pedagógia, nyelv,
  értékelés, biztonság, implementáció, verifier) a megírt fájlon futnak; utána szerepköri jóváhagyás.
- A terv E1–E7 pontja nyitott szerepköri kérdés; a tartalom ezek nélkül nem véglegesíthető.

### D-21: `/course-develop` terv a közös, 1–5 fős F-peula-változathoz (TERVEZET, projektgazdai jóváhagyásra)


### 0. Tényállás: a kötelező F-peulák

| F-peula | Státusz | Időtartam és blokkok | Létszám | Kapuelem | Létszámfüggő lépés | PRG-5 hiányzási mondata |
|---|---|---|---|---|---|---|
| M1.F | kötelező, éles (M1.4 SBI), :64 | 45’: 0–5 / 5–25 / 25–40 / 40–45 (:115–118) | 6–20 (:47) | S, B, I, hangnem (:53) | offline B-terv „párban” (:265); Blokk 3: „kis létszámnál … a 2. opció az alap” (:307) | :66, **a kapacitásról szóló mondat hiányzik** |
| M3.F | kötelező, éles (:43) | 45’ (:20, :106–112) | kb. 6–20 (:24) | helyzetleírás R1–R4, valamint a kvíz pontszáma és kötelező biztonsági helyzetei (:30, :93) | 2–3 fős előhívás (:376); név nélküli lapgyűjtés (:388) | :45, teljes |
| M5.F | kötelező, éles (:18) | **50–55’** (:17; HUM :224), 0–5 / 5–25 / 25–50 / 50–55 | 6–20 (:23) | R1–R4, „Hiányos” szempontok (:29) | 2–3 fős (:290); a név nélküli mód csak akkor, ha a lap senkihez sem köthető (:302) | :20, teljes |
| M6.F | kötelező, éles (:40) | 45’ (:150–153) | kb. 6–20 (:20) | R1–R5; az R4 és az R5 blokkoló (:26, :40) | 2–3 fős (:389); offline „párban” (:330) | :42, teljes |
| M7.F | kötelező, éles (:35) | 45’ (:96–99) | 6–20 (:20) | kvíz, Peula v2 + Zmán Kvucá, operációs tábla (:26, :30) | 2–3 fős (:272); név nélküli lapgyűjtés (:282) | :36, teljes |

Az M2.F és az M4.F puha kapus, ezért **ajánlott** (M2.F:20, M4.F:37, Glosszárium :194). A PRG-5 („minden kötelező F-peulához”) rájuk nem vonatkozik.

Mindegyik F-peula csak azoknak szól, akiknek a kapuja nem teljesült. Egy 6–20 fős kohorszban ez jellemzően 1–5 fő, vagyis a gyakorlatban a kis létszámú változat lesz a megszokott eset.

### A. Terv a SKILL A.1–12 pontja szerint

1. **Kontextus.** Program terv §6:309 (F-peula), §6:308 (1:1 kivételek), §6:311 (stábkapacitás, 1:8). Glosszárium :188, :193–194. Manifest §7:248–263: az F-peula hétfőn 18:00-kor van, a javítás határideje szerda 18:00, a manifestben nincs F-peula-activity (:251). GK §4:56–67 és §4.2:91–99. ADV §3:68–69 és §5:151–152. HUM 14: PRG-1, -4, -5, GYV-5, ADV-2. Formátumban a meglévő öt F-peulához illeszkedik.
2. **Célcsoport.** 15+ képzős madrihok, köztük kiskorúak. A kis létszám növeli a láthatóságot és a megszólalási nyomást, ezért a választási lehetőség (szóban vagy írásban) és a passz minden blokkban megmarad.
3. **Prerekvizit.** Ugyanaz, mint a modul F-peulájánál: megvan a kapun kapott visszajelzés (Megfigyelés → Hatás → Következő lépés), és a beadott munka elérhető. Forrás: az adott modul kapuja (M1.4, M3 KAPU, M5.4, M6 játéklap, M7 KAPU).
4. **Tanulási cél.** **Nincs új cél.** A modul F-peulájának „Fő célok” szakasza változatlanul érvényes. Ez teszi az „azonos kompetenciát fejlesztő” követelményt szerkezetileg teljesíthetővé.
5. **Konstruktív illeszkedés.** A cél a nem teljesült kapuelem javítása, a tevékenység a csendes javítás, a felidézés és a tisztázás, a mérés pedig a modul javító próbálkozása a meglévő rubrikával vagy kvízzel. A keret egyiket sem változtatja meg, csak a létszámtól függő szervezést.
6. **Élmény és tevékenység.** Blokkonkénti csere, lásd a B szakasz 3–4. pontját. Két érdemi változás van a meglévő lépésekhez képest, mindkettő meglévő lépés átszervezése, nem új tevékenység:
   - (a) a 2. blokkban rövid egyéni ránézés a javítási tervre;
   - (b) a 3. blokkban a résztvevők maguk töltik ki a buborékokat.

   Ezt a kettőt külön jóváhagyásra jelölöm.
7. **Gyakorlás.** A csendes munka közben a képző 2–3 percben formatív visszajelzést ad a javítási tervre, még a javító próbálkozás előtt. Korlát: kérdez, nem diktál szöveget, és nem mondja meg, hogy „így átmegy-e”. Ezt az értékelési felelősnek kell QA-znia.
8. **Értékelés.** Nincs új item, rubrika, kulcs, küszöb vagy completion. A javító próbálkozás nyitása és határideje a modul F-peulája és a manifest §7 szerint marad.
9. **Ív és terhelés.** Új fogalom nincs. Az időtartam és a blokkhatárok a moduléi (45’, az M5.F-nél 50–55’); a D-20 vágási tervét a keret hivatkozással követi, nem előzi meg. Időellenőrzés a leírt lépésekből:
   - 1. blokk: 5 fő × kb. 30 mp halk egyeztetés ≤ 2,5’.
   - 2. blokk: a 10 perces csendes munkában 5 fő × 2’ ránézés = 10’ (3 főig 3’/fő).
   - 3. blokk: a modul lépésidői.
   - 4. blokk: 5 × 30 mp mondatbefejezés + 1–2’ zárás.

   Ha a 3. blokk hamarabb véget ér, a maradék idő a résztvevők saját kérdéseire jut. A záró üzenet nem maradhat el.
10. **Akadálymentesítés.** A modul F-peulájának eszközei, és wifi-kiesésnél az offline leckeváltozat (`LMS – hozzáférhetőségi sztenderd.md` §5; a :116 az F-peulát már „egyéni/kiscsoportos támogató tér”-nek nevezi). A szóban vagy írásban válaszolás kétirányú választás. A fogalomtérkép-alaplap közelről, asztalon is olvasható.
11. **Gyermek- és adatvédelem.** Lásd a B szakasz 6–7. pontját.
    - Új adat nem keletkezik.
    - Kis létszámnál a név nélküliség nem garantálható, ezért nincs lapgyűjtés és nincs témakérő fal (az M1.F:307 és az M5.F:302 mintájára).
    - A képző csak minimális hiánylistát lát, privát módon (ADV-2).
    - A mentoros út naplója az ADV §3:68 „Mentori 1:1 meta-napló” sora szerint készül.
    - A keret alapból nem 1:1: egy résztvevő és egy képző 45 percig 1:1 helyzet volna, a GK §4.2:99 kivételei pedig legfeljebb 30 percet engednek.
    - A GYV-5 (GK §4:65) kis létszámnál is érvényes.
    - Önfeltárási kényszer nincs.
12. **Implementáció.**
    - Nincs új Moodle-activity és nincs új H5P (a PRG-8 szerint a képzői forgatókönyv nem résztvevői anyag), új `@asset` sem kell: a meglévő anyagok fejenként számoltak (pl. M3.F:131, M1.F:232).
    - **Hely:** `02 Tervezet/Felzárkóztató peula – kis létszámú változat (1–5 fő).md`. Indok: programszintű tananyag a `Terepgyakorlat – 2. félév.md` mintájára. A `02 Tervezet/Modulok/` gyökere nem jó hely, mert a `tools/media_manifest.py:444–453` `file_identity` függvénye a fájlnevet modulnévként, „HUB”-ként sorolná be.
    - A fájlba nem kerülhet `⟬KITÖLTENDŐ⟭`: a `content_integrity.py:522, :705–708, :783–785, :850` szerint ez a `MOODLE-BUILD-VERDICT`-et `NOT_READY`-ra állítja, ha `Modulok/` alatt van, és a gyökérben sem kívánatos.
    - Személynév nem kerül a fájlba (a repó nyilvános).

**EMBERI DÖNTÉS, a terven belül:**
- E1: Melyik F-peula „érzékeny” a GYV-5 szerint (jelölt: M3.F, M7.F). Kis létszámnál kell-e második 18+ felelős? Dönt: Memuna + programvezető.
- E2: Az egy résztvevős eset, és hogy a nagykorú egyetlen résztvevőre ugyanez vonatkozik-e (ez szigorúbb a kánonnál, tehát új szabály volna). Dönt: Memuna.
- E3: Ki hagyja jóvá a rövid egyéni mentoros utat. Dönt: programvezető.
- E4: Hol rögzül a kapacitás és a pótlás felelőse (a manifest §7 új oszlopa `SCHEDULE_TO_RESYNC` értékkel, vagy repón kívüli operatív naptár). Dönt: programvezető, illetve az LMS-gazda.
- E5: Mi történik, ha a pótidőpont nem fér el a javító határidő (szerda 18:00) előtt. A határidőt a keret nem módosítja. Dönt: programvezető + értékelési felelős.
- E6: Ki tarthatja az F-peulát, és ki férhet hozzá a kapueredményhez (BIZT-G3-8, nyitott). Dönt: DPO + programvezető.
- E7: Az M2.F és az M4.F hivatkozzon-e a keretre (opcionális, nem PRG-5-kötelezettség). Dönt: projektgazda.

### B. A keretfájl szerkezete (vázlat a megíráshoz)

0. **Bevezető idézetblokk.** A modul F-peulájának adatvédelmi bevezetője érvényes, kiegészítve: „Kis létszámnál a név nélküliség nem biztosítható: a jegyzetlapokat nem gyűjtjük be, témakérés-cetli nem kerül a táblára, a kérdések szóban vagy a saját lapon maradnak.”
1. **Meta és mikor használjátok.**
   - Használat: (a) 1–5 résztvevő van egy kötelező F-peulán; (b) dokumentált pótidőpont hiányzás miatt (PRG-5).
   - Nem csendes pótlás, nem második F-peula, és nem online változat.
   - Időtartam: a modul F-peulájáé. Létszám: 2–5 fő egy képzővel; 1 főre lásd a 6. pontot.
   - **Megtartási előfeltételek, név nélkül, a programvezető rögzíti:**
     - az időpont a javító határidő előtt van;
     - ki tartja (a pótlás felelőse, szerepnéven);
     - a második 18+ felelős vagy az azonnal elérhető helyettes, ha az E1 szerint kell, vagy ha egy résztvevő van;
     - a mentoros út jóváhagyója (E3);
     - az F-peula szereposztása és a vészhozzáférés (ADV-2).
2. **Előkészítés.**
   - Eszközök: a modul 2.1. listája; kis létszámnál nem kell témakérés-sáv és cetli, a fogalomtérkép-alaplap asztalon is használható.
   - Tér: egyetlen átlátható tér, külön szoba nélkül.
   - Képző: a modul 2.3. pontja, valamint a minimális hiánylista privát átnézése.
3. **Percbontás.** Hivatkozással a modul 3. szakaszára (45’: 0–5 / 5–25 / 25–40 / 40–45; M5.F: 0–5 / 5–25 / 25–50 / 50–55), mellette a kis létszámú csere oszlopa.
4. **Blokkonkénti csere.**
   - 1. blokk: a modul instrukciója; a témakérés szóban vagy a saját lapra; a képző körbejár, és halkan megkérdezi, mivel kezd a résztvevő.
   - 2. blokk: a 20 perc védett idő („szent idő”) marad; a csendes munka 10 percében egyéni ránézés a közös térben, a 7. pont korlátaival. Az offline „párban” lépés 1 főnél: egyedül a lappal, a képző kérdésével.
   - 3. blokk:
     - előhívás: 1 fő írásban, fejből; 2–3 fő egy csoport; 4–5 fő két csoport (2+2 vagy 2+3);
     - kérdésgyűjtés nyílt módban; a képző a modul „tipikus félreértés” kérdéseivel nyithat, így senkinek nem kell a sajátját kimondania;
     - a buborékokat a résztvevők töltik ki, az összekötő kérdések a modulból jönnek.
   - 4. blokk: a modul mondatbefejezése szóban vagy írásban (nem kell felolvasni), passzal; a híd és a határidő a modulé.
5. **Modulspecifikus betétek.** Csak meglévő elemek, új item nélkül.
   - **M1.F:** javított SBI-vázlat (S, B, I, hangnem). A 3. blokk három rövid magyarázatból és mini-összegzésből áll (:288–345), az Opció 2 az alap (:307). Lehetőség: a magyarázat előtt a résztvevő a saját szavaival mondja el a fogalmat. A vakfoltra nem kérünk saját életből vett példát.
   - **M3.F:** papíron írt javítási terv; a peula alatt Moodle-szerkesztés nincs (M3.F:263). A 3. blokk az :370–445 lépései az M3.F-POSZ-02 alaplappal. A kérdésekre adott válasz a GK §4.1 öt lépését követi szó szerint. A helyzetleírás kitalált eset marad. GYV-5 (E1).
   - **M5.F:** a „Hiányos” szempontok átírása (R1–R4). A 3. blokk 20–25’ (:240–356). A lapgyűjtés tilalma már a :302-ben is benne van.
   - **M6.F:** papíron a játéklap javítása, az R4 és az R5 blokkoló. A 3. blokk a :339–437 lépései; az offline „párban” (:330) 1 fő esetén átalakul. Kirekesztés-szimuláció nincs.
   - **M7.F:** a peulaterv javítása (kvíz, illetve Peula v2). A 3. blokk a :224–316 lépései. A keret nem ír elő AI-használatot; a :308 AI-korlátja marad. Időzítés: a Z utáni hét. GYV-5 (E1).
6. **Egy résztvevő (TERVEZET, Memuna hagyja jóvá).**
   - „Egy résztvevővel és egy képzővel a 45 perces alkalom 1:1 helyzet volna, a safer-working szabály kivételei pedig legfeljebb 30 percet engednek (`Gyermekvédelem – release gate.md` §4.2).”
   - Ezért két út van: (1) jelen van egy második felkészített 18+ felelős, és az alkalom a keret szerint zajlik; (2) jóváhagyott, rövid egyéni mentoros út a §4.2 (a) kivétele szerint (legfeljebb 30 perc, hivatalos csatornán vagy átlátható térben, egy másik felelős tudtával, csak meta-naplóval).
   - A mentoros út javasolt menete: 0–5’ a visszajelzés és az első lépés; 5–20’ a javítási terv a „Következő lépés” szerint (a résztvevő mondja el, a mentor kérdez); 20–25’ fejből 2–3 kulcsfogalom a modul fogalomtérképéről; 25–30’ híd. A hiányzó leckét csendes pótlással pótolja.
7. **Biztonsági minimum.** Csak hivatkozás, új szabály nincs: GK §4:61–67 (passz; nincs kötelező megosztás; saját érintettség; felkavart kiskorú nem marad egyedül; GYV-5 és megállítási protokoll, ennek egységesítése a D-01; nincs automatikus félrevonulás; a diszkrét beszélgetés is átlátható). A kis létszámra jellemző kockázat: ha a képző egy felkavart résztvevővel marad, a többiek ne maradjanak felnőtt nélkül, ezért szerepel az előfeltételek között a második felelős vagy a helyettes.
8. **Rövid képzői ellenőrző lista**, a modul §5 listája mellé.

### C. Tervezett szerkesztések

### D21-01 — Új keretfájl
- Fájl: `02 Tervezet/Felzárkóztató peula – kis létszámú változat (1–5 fő).md` (új)
- Alap: HUM 14 PRG-5, PRG-4; D-21 projektgazdai irány; M3:ERT-G3-10
- Hatáskör: SZEREP. A tervet a projektgazda hagyja jóvá (PRG-4). Az 5. pont betétjeit az adott modulgazda, a 6–7. pontot a Memuna, az 1. pont előfeltételeit a programvezető, a 4. pont 2. blokkját és az 5. pont kapuelem-hivatkozásait az értékelési felelős. Vétó/QA: programvezető + értékelési felelős.
- OLD: — (új fájl)
- NEW: a B szakasz szerkezete; H1: `# Felzárkóztató peula (F-peula) – kis létszámú változat (1–5 fő)`
- Együtt mozgó helyek: D21-02…D21-12; `tools/approved-visible-text.json` (csak `--pin-visible`); a média `check`, és ha elcsúszik, `build` külön `chore(media)` commitban; HUM 15. szakasz D-21-sora (fő session)
- Címkék: LÁTHATÓ SZÖVEG; nem VÉTÓLISTÁS, nem VO-PACK, nem BUILD-INPUT
- Indoklás: a D-21 (b) opciója egyetlen szerzői körrel teljesíti a PRG-5-öt. A gyökérbeli hely a `media_manifest.py:444–461` szerint „program-doc” besorolást kap.

### D21-02 — M1.F, Létszám
- Fájl: `02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md:47`
- Alap: PRG-5; D-21
- Hatáskör: PROJEKTGAZDA (vétó/QA: programvezető + értékelési felelős; a szöveg: M1 modulgazda)
- OLD: `**Létszám:** 6–20 fő`
- NEW: ``**Létszám:** 6–20 fő; 1–5 résztvevőnél a kis létszámú változat szerint (`Felzárkóztató peula – kis létszámú változat (1–5 fő).md`)``
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: a PRG-5 szerinti hivatkozás azon a helyen, ahol a képző a létszámot nézi.

### D21-03 — M3.F, Létszám
- Fájl: `…/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md:24`
- Alap, hatáskör: mint a D21-02-nél (M3 modulgazda; a biztonsági részhez Memuna)
- OLD: `**Létszám:** kb. 6–20 fő`
- NEW: ``**Létszám:** kb. 6–20 fő; 1–5 résztvevőnél a kis létszámú változat szerint (`Felzárkóztató peula – kis létszámú változat (1–5 fő).md`)``
- Együtt mozgó helyek: D21-01. Az M3.F:131 „(6–20 fő)” `@asset`-jegyzet fejenként számolt, nem kell módosítani.
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: a D-21 „Addig” záradékát (az M3.F:24 marad) az elfogadás oldja fel.

### D21-04 — M5.F, Létszám
- Fájl: `…/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md:23`
- Alap, hatáskör: mint a D21-02-nél (M5 modulgazda)
- OLD: `**Létszám:** 6–20 fő`
- NEW: mint a D21-02-nél
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: mint a D21-02-nél. Az időtartam (50–55’) nem változik.

### D21-05 — M6.F, Létszám
- Fájl: `…/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:20`
- Alap, hatáskör: mint a D21-02-nél (M6 modulgazda)
- OLD: `**Létszám:** kb. 6–20 fő`
- NEW: mint a D21-03-nál
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: mint a D21-02-nél.

### D21-06 — M7.F, Létszám
- Fájl: `…/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md:20`
- Alap, hatáskör: mint a D21-02-nél (M7 modulgazda; a biztonsági részhez Memuna)
- OLD: `**Létszám:** 6–20 fő`
- NEW: mint a D21-02-nél
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: mint a D21-02-nél.

### D21-07 — M1.F, a PRG-5 kapacitásmondatának átvezetése (a D-21 elfogadásától független, most is elvégezhető)
- Fájl: `…/M1/Peulák/M1.F – … (45’).md:66`
- Alap: HUM 14 PRG-5, utolsó mondat: „A programvezető rögzítse a kapacitást és a pótlási felelőst.”
- Hatáskör: PROJEKTGAZDA (lezárt döntés; vétó/QA: programvezető + értékelési felelős)
- OLD: `kiskorúval 1:1 csak a safer-working szabály meglévő kivételei szerint (HUM-SAFE-02);` (egyszer szerepel)
- NEW: `kiskorúval 1:1 csak a safer-working szabály meglévő kivételei szerint (HUM-SAFE-02); a kapacitást és a pótlás felelősét a programvezető rögzíti;`
- Együtt mozgó helyek: nincs
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: az M3.F:45, M5.F:20, M6.F:42 és M7.F:36 tartalmazza ezt a mondatot, az M1.F nem. A D-21-dokumentum :486 sora („az M1.F … már tartalmazta”) erre a mondatra nem igaz.

### D21-08 — M1.F, hivatkozás a pótidőponthoz (a D21-07 utáni állapotra)
- Fájl: M1.F:66
- Alap, hatáskör: mint a D21-02-nél; az 1:1-es rész miatt a Memuna is
- OLD: `a kapacitást és a pótlás felelősét a programvezető rögzíti;` (csak a D21-07 után létezik)
- NEW: ``a kapacitást és a pótlás felelősét a programvezető rögzíti; a pótidőpont és a rövid egyéni mentoros út a kis létszámú változat szerint zajlik (`Felzárkóztató peula – kis létszámú változat (1–5 fő).md`);``
- Együtt mozgó helyek: D21-01, 6. pont
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: a PRG-5 két hiányzási útja egy leírt formát kap.

### D21-09…D21-12 — M3.F:45, M5.F:20, M6.F:42, M7.F:36, hivatkozás a pótidőponthoz
- Fájl: a négy fájl a fenti sorokon (a négy fájl mindegyikében egyszer szerepel; Greppel ellenőriztem)
- Alap, hatáskör: mint a D21-08-nál
- OLD: `A kapacitást és a pótlás felelősét a programvezető rögzíti.`
- NEW: ``A kapacitást és a pótlás felelősét a programvezető rögzíti. A pótidőpont és a rövid egyéni mentoros út a kis létszámú változat szerint zajlik (`Felzárkóztató peula – kis létszámú változat (1–5 fő).md`).``
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: mint a D21-08-nál.

### D21-13 — Program terv §6, programszintű hivatkozás
- Fájl: `02 Tervezet/Program terv.md:309`
- Alap: PRG-5; D-21
- Hatáskör: PROJEKTGAZDA (vétó/QA: programvezető + értékelési felelős)
- OLD: `A **csendes pótlás** önálló elmaradás-pótlás annak, aki lemaradt egy leckéről vagy peuláról.` (egyszer szerepel)
- NEW: ``A **csendes pótlás** önálló elmaradás-pótlás annak, aki lemaradt egy leckéről vagy peuláról. Ha egy kötelező F-peulára 1–5 résztvevő jut, vagy hiányzás miatt dokumentált pótidőpont kell, az F-peula a közös kis létszámú változat szerint zajlik (`Felzárkóztató peula – kis létszámú változat (1–5 fő).md`); a kapacitást és a pótlás felelősét a programvezető rögzíti (HUM 14. szakasz, PRG-5).``
- Együtt mozgó helyek: D21-01
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: a SKILL B pontja szerint a hivatkozást programszinten is fel kell venni.

**Opcionális (E7, projektgazda):** M2.F:19 és M4.F:20 Létszám-sora a D21-02 mintájára, „ajánlott F-peula” jelzéssel. Alapjavaslat: nem kerül be a D-21 csomagba.

### D. Review-kapuk és DoD (SKILL C, ebben a sorrendben)
1. `pedagogy-reviewer`: a D21-01 és a hivatkozó mondatok. Fókusz: azonos cél, időellenőrzés, 1–5 fős lépésváltozatok.
2. `hungarian-editorial-reviewer`.
3. `assessment-reviewer` (kötelező): a 2. blokk formatív ránézése, az 5. pont kapuelem-hivatkozásai, a javító próbálkozás sorrendje és határideje érintetlen-e.
4. `safety-policy-reviewer` (kötelező): a 6–7. pont, GK §4/§4.2, GYV-5, ADV-2, a lapgyűjtés tilalma, a 2. blokk egyéni ránézése mint nem 1:1 helyzet.
5. `implementation-reviewer`: nincs új activity; a javító próbálkozás nyitása (manifest §7:251); akadálymentesítés.
6. `verifier`, majd 7. a megerősített findingok javítása, 8. a teljes diff visszaolvasása.
9. Egyszer `--pin-visible "D-21/PRG-5: F-peula kis létszámú változat + hivatkozások"`.
10. `media_manifest.py check` és `reconcile`. `@asset` nincs, de a `discover_sources` az új fájlt is olvassa; elcsúszásnál `build` kétszer, külön `chore(media)` commitban.
11. `content_integrity.py` 0 ERROR, a `--release-report` verdiktje nem romlik; `/release-check` utolsóként.

### E. Elfogadási feltételek
1. Mind az öt kötelező F-peula hivatkozik a keretre (Létszám-sor és hiányzási mondat), az M1.F-ben megvan a PRG-5 kapacitásmondata.
2. A keret nem hoz új célt, itemet, rubrikát, kulcsot, küszöböt, időtartamot, blokkhatárt, kaputípust, completiont, és nem változtat a kötelező/opcionális besoroláson.
3. Minden 2–3 fős vagy „párban” lépésnek van 1 fős és 4–5 fős változata, és a blokkonkénti percek a leírt lépésekből összeadódnak.
4. Kiskorúval nincs 30 percnél hosszabb vagy nem átlátható 1:1 helyzet. Az egy résztvevős eset csak a 6. pont két útja szerint zajlik.
5. A biztonsági pontok csak hivatkozásként szerepelnek, a GYV-5 létszámnormáját a keret nem találja ki.
6. Nincs lapgyűjtés, sem név vagy státusz a táblán, új adatkör nem keletkezik, személynév nincs a repóban.
7. Lefutott az összes D-pontbeli kapu.
8. A szerepköri jóváhagyások írásban megvannak. Ezek bizonyíték-kapuk: nem írom be és nem feltételezem őket.

### F. Jóváhagyók
- Projektgazda: a terv (PRG-4), az E7 és a két tervezési változás (6a, 6b).
- Modulgazdák (M1, M3, M5, M6, M7): a saját betétjük.
- Memuna: a 6–7. pont, az E1 (a programvezetővel), az E2.
- Programvezető: a kapacitás, a pótlás felelőse, az E3, az E4, az E5 (az értékelési felelőssel), az E6 (a DPO-val).
- Értékelési felelős: a 2. blokk és az 5. pont kapukapcsolata.
- Vétó/QA (PRG-5): programvezető + értékelési felelős.

### G. Ami nem része a tervnek
- új tevékenység (a 6a és a 6b meglévő lépés átszervezése);
- új értékelési item vagy rubrikasor;
- kulcs, küszöb, ponthatár, rubrikaszint, időtartam vagy javító határidő változása;
- completion vagy kaputípus változása, az M2.F/M4.F kötelezővé tétele;
- online vagy videohívásos változat (ehhez Memuna- és DPO-döntés kellene);
- új `@asset`, VO;
- új gyermekvédelmi szabály, a GYV-5 létszámnormája, a BIZT-G3-8 hozzáférési szabálya;
- a D-20 vágási terve;
- második F-peula.

### H. Findingok (pedagógiai lencse)

**PED-1**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:** M1.F:66
- **Probléma:** Az M1.F-ből hiányzik a PRG-5 kapacitásra és a pótlás felelősére vonatkozó mondata. A másik négy kötelező F-peulában megvan.
- **Bizonyíték:** „kiskorúval 1:1 csak a safer-working szabály meglévő kivételei szerint (HUM-SAFE-02);” (itt a bekezdés véget ér). Vö. M3.F:45: „A kapacitást és a pótlás felelősét a programvezető rögzíti.”
- **Hatás:** az M1-pótlásnál nincs kimondott felelős, ami modulok közti inkonzisztencia (D13).
- **Javaslat:** a D21-07 szerinti szó szerinti átvezetés.
- **Típus:** objektív
- **Verdikt:** —

**PED-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:** M1.F:47, M3.F:24, M5.F:23, M6.F:20, M7.F:20
- **Probléma:** Ha egyetlen résztvevő bukik, a szöveg semmit nem mond arról, hogyan zajlik az F-peula. A 45 (M5.F: 50–55) perces alkalom egy képzővel 1:1 helyzet lenne, ami túllépi a safer-working kivételek 30 perces korlátját.
- **Bizonyíték:** M3.F:24 „**Létszám:** kb. 6–20 fő”; GK §4.2:99 „Legfeljebb **30 perc**, hivatalos csatornán vagy fizikailag átlátható térben”.
- **Hatás:** kiskorúval szabályon kívüli 1:1 helyzet jöhet létre (D12/D13).
- **Javaslat:** EMBERI DÖNTÉS: a B szakasz 6. pontjának két útja; dönt a Memuna, a mentoros út jóváhagyójáról a programvezető.
- **Típus:** emberi-döntés
- **Verdikt:** —

**PED-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:** `LMS – activity manifest.md` §7:248, :258–263
- **Probléma:** A pótidőpontnak nincs helye a naptárban, és nincs szabály arra az esetre, ha a hétfő 18:00 és a szerda 18:00 közötti ablakban nem szervezhető meg, pedig a PRG-5 „mindig a javító próbálkozás előtt” követelményt ír elő.
- **Bizonyíték:** :248 „a kötelező F-peula a kapueredmény megerősítése utáni hétfőn 18:00-tól van; a javító próbálkozás határideje a rákövetkező szerda 18:00”.
- **Hatás:** a hiányzó tanuló mastery-útja esetleges lesz.
- **Javaslat:** EMBERI DÖNTÉS: E4 és E5; dönt a programvezető az értékelési felelőssel, a naptárrészt az LMS-gazdával.
- **Típus:** emberi-döntés
- **Verdikt:** —

### (1) Amit nem ellenőriztem
- Az M5.F, M6.F és M7.F 3. blokkjának teljes lépéslistáját és lépésidejét nem olvastam végig. A „2–3 fős” előhívást és a lapgyűjtést soronként igen.
- Az M1–M7 kapufájlok rubrikasorainak szó szerinti nevét nem néztem meg; az F-peulák saját utalásaira támaszkodtam.
- Hogy a `media_manifest.py check` jelez-e elcsúszást egy `@asset` nélküli új fájlra.
- Hogy a HUM 8–9. szakasz F-peula-tétele tartalmaz-e mást a PRG-5-ön túl.

### (2) Ellentmondás a kánonban
- A D-21-dokumentum :486 sora szerint az M1.F „már tartalmazta” a hiányzási mondatot, de a kapacitásra vonatkozó rész hiányzik (PED-1).
- A feladat „45’ megtartása” kitétele nem illik az M5.F-re: az M5.F 50–55’ (:17), ami lezárt döntés (HUM :224). A keret ezért mindig a modul saját időtartamát tartja meg. Gyenge feszültség lehet a PRG-1 „45 perces peulablokkok” mondatával; ez a D-20 ügye, alacsony bizalommal.
- Ellentmondás helyett két nyitott függés van: a GYV-5 „érzékeny peula” besorolása és a BIZT-G3-8 hozzáférési kérdése. A keret egyiket sem döntheti el.

Érintett fájlok (abszolút úttal):
- 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- 02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md
- 02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md
- 02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md
- 02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md
- 02 Tervezet/Program terv.md
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/LMS – activity manifest.md
- tools/media_manifest.py
- tools/content_integrity.py
