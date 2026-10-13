# 2026-10-12 Célzott QA – M4 átvezetés, nyelvi lencse és verifier, AP-2026-10-12-01

- **Kiegészítés ehhez:** `2026-10-12 Célzott QA – M4 átvezetés (dd64825), AP-2026-10-12-01.md` (ott az I. riport és a biztonság-jog, valamint az értékelés + LMS lencse nyers kimenete).
- **Tartalom:** B. a verifier verdiktjei mind a 23 ID-ra (szó szerint); C. a nyelvi lencse nyers kimenete (szó szerint).

## B. Verifier-verdiktek (szó szerint)

<!-- agent a82706ffbb301fb44 -->

M4 célzott QA, adverzális második kör (AP-2026-10-12-01, next-version ág, dd64825 utáni állapot). Mind a 23 ID-t a mostani fájlokon néztem vissza, és mindegyik kapott verdiktet.

Formátum: ID | verdikt | típus | súly | indok | javítás

**A klaszter**
- M4:QA-BIZT-1 | RÉSZBEN | bizonyíték-kapu | P1 | A probléma valós: az öt 🔒 doboz (M4.1:1206, M4.2:896, M4.3:650, M4.4:704, :737) „csak a kijelölt mentorod” + admin névsora ellentmond az ADV:105–106, :117–118 szerkesztő tanári és menedzseri hozzáférésének. Új emberi döntés viszont nincs: az ADV-1 (F) lezárta a modellt, az „admin/editor szűk, név szerint” hozzáférést elfogadta, és az ígéret igazítását kifejezetten a staging role-matrix utánra tette. | Most nincs szövegjavítás. A mentor-mondat se nem erősödik, se nem íródik át, az admin-betoldás marad. A ledgerben EXTERNAL: staging role-matrix (LMS-gazda) és DPO-bizonyíték; a BIZT-2/BIZT-5 ADV-sorok a kánoni körben frissülnek.
- M4:QA-NYELV-1 | ELVETVE | — | — | Az „azonban”/„de” a rendszergazdát teszi az egyetlen kivétellé, ezzel megerősíti a kimerítő „csak a mentorod” olvasatot, amelyet a BIZT-1 éppen kánonellenesnek mutat. Ez a tiltott „mentor-mondat erősítése”. Az M4.4 vesszője kötőszó nélkül is szabályos mellérendelés, az M1.4:510 és az M5.4:45/:324 sem használ kötőszót. | Nincs javítás. A mondat az ADV-1 RBAC-igazításával együtt íródik át. Duplikátum: a BIZT-1-et kell megtartani.

**Önálló biztonság-jog findingok**
- M4:QA-BIZT-2 | MEGERŐSÍTVE | objektív | P2 | A döntési csomag az M4.F:267-et ADV-1-helyként sorolja (plan:993), az admin-betoldás mégis csak öt helyre került be. Itt egy kizárólagos „csak a kijelölt mentor láthatja” mondat maradt. | OLD „ezeket csak a kijelölt mentor láthatja (a HUM-PRIV-01 projektgazdai döntés legszűkebb hozzáférés elvéből).” → NEW „ezeket csak a kijelölt mentor láthatja (a HUM-PRIV-01 projektgazdai döntés legszűkebb hozzáférés elvéből); technikai okból a Moodle rendszergazdája is hozzáférhet.” A mentor-részhez nem nyúlunk (BIZT-1).
- M4:QA-BIZT-3 | MEGERŐSÍTVE | emberi-döntés | P2 | A GYV-19 szó szerint „a képzőnek és a Memunának” kér jelzést, az M4.3:360 viszont csak a Memunát nevezi meg. A GK:81 (HUM-SAFE-01) szerint a címzett mindig a Memuna. Két lezárt gyermekvédelmi döntés áll szemben egymással, és az M4.3 hanih-helyzetére a képző alkalmazása új alkalmazási eset. P2-re vettem, mert a Memuna-út és a nyomozási tilalom megvan, a védelem nem gyengült. | Memuna és projektgazda dönt. A GK §4.1 nem gyengíthető. Az `M4:BIZT-G1-6` nem lehet FIXED.
- M4:QA-BIZT-4 | MEGERŐSÍTVE | objektív | P2 | Az M4.1:1199 és az M4.3:644 `@source`-ában még ott a „Most írd le magadnak…”, miközben a látható szövegből a „magadnak” az ADV-3 miatt kikerült. Ez megegyezik a plan:1054 VO_PACK tételével. | Kurzusoldalon nincs javítás: csak VO fix packkal és újrarendereléssel módosul. A ledgerben VO_PACK/nyitott, nem FIXED.
- M4:QA-BIZT-5 | MEGERŐSÍTVE | emberi-döntés | P2 | Az M4.A:381 név nélküli, önkéntes boríték- vagy falopciója csak akkor sérti az ADV-7-et, ha a fókuszkártya „személyes önfeltáró cetli”. Ezt a besorolást a döntés nem mondja ki, tehát új alkalmazási eset, és adatvédelmi kétségnél emberi kapu. | A DPO / jogi felelős dönt, Memuna-QA-val. Addig a szöveg nem változik.
- M4:QA-BIZT-6 | RÉSZBEN | objektív | P2 | Az M4.A:292-ből tényleg hiányzik az ADV-7 „tájékoztatással és HUM-PRIV-02 szerinti engedéllyel” feltétele, pedig a terv erre a helyre építi az ADV-7 fotós részét. A kiegészítés csak szigorít. A javasolt NEW viszont nyelvtanilag sántít, és a „gondviselő is hozzájárul” állítás a HUM-PRIV-02 általam olvasott szövegében (:139–153) nem szerepel, ezért nem kerülhet be. | OLD „…a hozzáférést, a megőrzést és a törlést;” → NEW „…a hozzáférést, a megőrzést és a törlést, tájékoztatták a résztvevőket, és megvan a HUM-PRIV-02 szerinti engedély;”. Gondviselői kitétel nem kerül be.

**B klaszter**
- M4:QA-BIZT-7 | MEGERŐSÍTVE | objektív | P2 | Az M4.A:58, az M4.B:63 és az M4.F:80 olyan blokkra hivatkozik, amely egyik peulafájlban sincs meg. A GYV-6 szerint ide a GK §4:63 kerül, amely „tanulói … blokk: §4.3” alakban hivatkozik, így a betoldásból elveszett egy minősítő. | Mindhárom helyen: OLD „(a „Ha ez a téma téged is érint” blokk)” → NEW „(a tanulói „Ha ez a téma téged is érint” blokk: `Gyermekvédelem – release gate.md` §4.3)”. Ez megtartandó a NYELV-9 helyett. Ugyanez a minta él az M1.A/M1.B/M1.F-ben is: ez kereszt-modul, nem M4-finding.
- M4:QA-NYELV-9 | RÉSZBEN | objektív | P2 | Ugyanaz, mint a BIZT-7. A „lásd M4.1, M4.2” hivatkozás gyengébb, mint a kánoni §4.3. Az M4.F „nem küldünk ki” alakja a GK:64 szó szerinti szövege, ezért nem írandó át. | Duplikátum: a BIZT-7 javítása az irányadó. A személyváltás nem javítandó.

**C klaszter**
- M4:QA-ERT-4 | RÉSZBEN | objektív | P2 | Csak az M4.3:53-ban kétértelmű, mert ugyanez a doboz a kvízt „kapukvíz”-nek hívja. A javasolt „(Kapu 2)” címke viszont az M4.3 tanulói szövegében sehol nem szerepel, ezért nem jó választás. | Csak az M4.3:53-ban: OLD „Ha a kapunál akadsz el, ez nem zsákutca: ha a modul végén leadott peulabemutató-vázlatodban a mentorod visszajelzése szerint még hiányzik vagy nem érthető valamelyik elem, az” → NEW „Ha a modul végén leadott peulabemutató-vázlatodnál akadsz el, ez nem zsákutca: ha a mentorod visszajelzése szerint még hiányzik belőle vagy nem érthető valamelyik elem, az”. Ez megtartandó a NYELV-2 helyett.
- M4:QA-NYELV-2 | RÉSZBEN | objektív | P2 | Az M4.3-as rész valós, és az ERT-4-be olvad. Az M4.1, M4.2 és M4.4 a PT:242 modulközi „Ha a kapunál akadsz el” formuláját őrzi, ott nincs bizonyított hiba: ez a kánoni kör tétele. | Duplikátum: az M4.3 az ERT-4 szerint javul, a másik három hely nem változik.

**D klaszter**
- M4:QA-NYELV-8 | RÉSZBEN | objektív | P2 | Az „ellenőrizni kell” cselekvője nem levezethető. Az ADV-11 nem mondja meg, ki ellenőriz, és a gyakorlat megoszlik: az M0.A:604 és az M1.F:80 a képzőre bízza, az M5.F:56 és az M6.F:96 a résztvevőre. Ezért a „mindenki” beírása tartalmi választás lenne, a finding ezen része elvetendő. Az M4.F:52 viszont gyengíti az ADV-11-et: a „se maradjon rajta” csak az ott hagyást tiltja, a „tilos” pedig azt jelenti, hogy munkapéldány nem is készül (az M5-ös verifier-olvasat). Ráadásul a „(letöltött … fájl)” zárójel összemossa a munkapéldányt a külön törlendő letöltésekkel. | OLD „és személyes munkapéldány (letöltött vagy helyben mentett fájl) se maradjon rajta:” → NEW „és személyes munkapéldány (helyben mentett fájl) se készüljön rajta:”. Az „ellenőrizni kell” marad.

**E klaszter**
- M4:QA-IMPL-1 | MEGERŐSÍTVE | objektív | P2 | Az LMS-1 (F) szerint a fájltípus „a tényleges akadálymentes sablonhoz igazítva” kell. A sablon az M4.4:771 szerint .docx, a :759, :766 és :768 mégis „doc”-ot ír. A :767 purpose-mezője ráadásul szó szerinti idézetként adja vissza a :759 már megváltozott sorát, így pontatlan. | :759 → „* Fájlfeltöltés: legfeljebb 1 fájl (1 oldalas .docx vagy .pdf), a letölthető sablon alapján.”; a :767 idézete ugyanígy; a :766 „(doc)” → „(.docx)”; a :768 „doc formátumban” → „.docx formátumban”. Utána `media_manifest.py build` és a látható szöveg újrapinelése. .odt nem kerül be; a végleges típuslistát az LMS-gazda rögzíti (EXTERNAL, RT-3).
- M4:QA-NYELV-10 | MEGERŐSÍTVE | objektív | P2 | Többelemű tulajdonnév + köznév kötőjelet kér; a terv maga is „Google Doc-változat”-ot írt (plan:952). | M4.4:771: „Google Doc változat” → „Google Doc-változat”. Utána `media_manifest.py build`, külön `chore(media)` commitban.

**Értékelés**
- M4:QA-ERT-1 | MEGERŐSÍTVE | objektív | P2 | A HUB:138 első fele nem frissült az ERT-8 átvezetésével, így a be nem adott vázlatot is M4.F-kiváltónak teszi. Ez ellentmond a §5:108-nak („leadott … vázlata”), a §5:110 lemaradás-szabályának és a §7 két átírt pontjának. | OLD „ha nincs beadva vagy nagyon hiányos (a „még nem éri el” szint) → mentori jelzés, finomító kör” → NEW „ha nincs beadva → mentori jelzés; ha a leadott peulabemutató a „még nem éri el” szinten van → mentori jelzés, finomító kör”. A sor többi része, a küszöb, a szintek, az 1+1 beadás és a zárójeles megjegyzés nem változik.
- M4:QA-ERT-2 | ELVETVE | — | — | A szárat az ERT-25 (F) szerint most pontosították, és a ✅-tal való tartalmi egyezés szükséges az „egy szakmai értelmezés” egyértelműségéhez. A maradék szóvisszhang itemminőségi ítélet, amely a HUM-PED-01 lektori QA-jára tartozik, nem bizonyított hiba. A javasolt új szár is visszhangoz („világos” ↔ „Érthető”, „peula célja”). | Nincs javítás.
- M4:QA-ERT-3 | ELVETVE | — | — | Az M4.B 3. köre (:214–217) nem mondja meg, ki kérdez, így a „csak válaszoló” hézag nem bizonyított. Ha mégis valós, a lezárt PRG-2 alapértelmezése (szűkítés, nem új activity) megválaszolja, tehát nem nyitott emberi döntés. | Nincs javítás.

**Többi nyelvi finding**
- M4:QA-NYELV-3 | RÉSZBEN | objektív | P2 | Az M4.1:1182 „A két választ” a dd64825-ben jött be. A dián egyetlen kérés áll, a narráció pedig „2 dolgot” mond, ezért a két válasz összekeverhető. Az M4.3:628-ban a „két mondat” előzménye a kétrészes kérdésből (több/kevesebb) kikövetkeztethető, ott nincs bizonyított hiba. | Csak az M4.1:1182: OLD „A két választ a lecke után következő” → NEW „A válaszaidat a lecke után következő”. Az M4.3 nem változik. Látható szöveg, tehát `--pin-visible`.
- M4:QA-NYELV-4 | RÉSZBEN | objektív | P2 | Az (a) rész valós: a dd64825 a régi „A hiányzó completion” alanyt „ez”-re cserélte, amely a „jelzés”-re is visszautalhat (3. regressziós minta). A (b) rész nem hiba: a hub vegyes képzői és fejlesztői specifikáció (BSPEC, LMS-azonosítók), a feltétellista pedig az ERT-24 átvezetése. | (a) OLD „jelzés a mentornak / stábnak: ez lemaradás, a résztvevő csendes pótlással pótolja.” → NEW „jelzés a mentornak / stábnak. A hiányzó completion lemaradás: a résztvevő csendes pótlással pótolja.” A (b) mondat marad.
- M4:QA-NYELV-5 | ELVETVE | — | — | A „szerkezet” a PRG-10 döntés szó szerinti szava (HUM:730), és a korpuszban mindkét alak él (PT: „modell”; M1/M6/M7 kapuk: „szerkezet”). A cseréje a GL kánoni körének terminológiai döntése, nem M4-hiba. | Nincs javítás.
- M4:QA-NYELV-6 | ELVETVE | — | — | A HUB:137 nem állítja, hogy a társas visszajelzés nem strukturált: a formáló/strukturált pár időzítést és funkciót különít el. A javasolt átcímkézés pedagógiai tartalmat változtatna. | Nincs javítás.
- M4:QA-NYELV-7 | ELVETVE | — | — | A félreolvasás sem torzít jelentést: a GL szerint formatív = nem blokkol, és a PRG-16 „puha = nem blokkoló” glosszája a mondatban megvan. A jelzőtorlódás stílus kérdése. | Nincs javítás.

**BIZT-8**
- M4:QA-BIZT-8 | MEGERŐSÍTVE | bizonyíték-kapu | P2 | A felsorolt lezárt döntések (ADV-3, ADV-7, ADV-9, ADV-11, GYV-3, GYV-6, GYV-19) szövegszinten át vannak vezetve, de a döntésekben megnevezett szerepek írásos bizonyítéka (DPO, Memuna, LMS-gazda) nincs meg. | Nem javítható. A `RELEASE-READINESS.md` G-kapuihoz rendelendő: „megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő”. Az `M4:BIZT-G1-2` és az `M4:BIZT-G2-1` EXTERNAL marad.

**Összesítés**
- 23 ID: MEGERŐSÍTVE 10 (BIZT-2, -3, -4, -5, -7, -8, ERT-1, IMPL-1, NYELV-10; ebből emberi-döntés a BIZT-3 és a BIZT-5, bizonyíték-kapu a BIZT-8), RÉSZBEN 8 (BIZT-1 bizonyíték-kapuként, BIZT-6, ERT-4, NYELV-2, NYELV-3, NYELV-4, NYELV-8, NYELV-9), ELVETVE 6 (ERT-2, ERT-3, NYELV-1, NYELV-5, NYELV-6, NYELV-7).
- Bizonyíték-kapu: 2 (BIZT-1, BIZT-8).
- Duplikátumok:
  - NYELV-1 → BIZT-1 marad;
  - NYELV-9 → BIZT-7 marad;
  - NYELV-2 → ERT-4 marad (csak az M4.3);
  - a D klaszterben az ADV-11 „munkapéldány”-javítása a NYELV-8 sorában szerepel.
- Látható szöveg változik: BIZT-2, BIZT-6, BIZT-7, ERT-1, ERT-4, NYELV-3, NYELV-4, NYELV-8, IMPL-1 → változtatáskészletenként egy `--pin-visible`.
- Asset-mezők változnak: IMPL-1, NYELV-10 → `media_manifest.py build`, külön `chore(media)` commitban.

Fájlok:
- 02 Tervezet/Modulok/M4/
- 02 Tervezet/Emberi jóváhagyás szükséges.md (14. szakasz)
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md


## C. Nyers lencse-kimenet – nyelv (szó szerint)

<!-- agent a36c7ed70e987bb4b -->

## M4 — célzott nyelvi QA (HUM 14., dd64825, AP-2026-10-12-01)

Ez read-only ellenőrzés volt. Csak a diff hunkjait és a közvetlen környezetüket néztem, a döntések tartalmát nem vitatom. Régi Somer-írásmód nincs a diffben, a 10. regressziós minta (azonosítók) nem sérült.

**Fájlok (az alábbi rövidítésekkel):**
- HUB = `02 Tervezet/Modulok/M4/M4 – Hallható és érthető vagyok – Kiállás, kapcsolódás & kérdezéstechnika.md`
- M4.1–M4.4 = `02 Tervezet/Modulok/M4/Online leckék/M4.x – …md`
- M4.A, M4.B, M4.F = `02 Tervezet/Modulok/M4/Peulák/M4.x – …md`
- GK = `02 Tervezet/Gyermekvédelem – release gate.md`

---

**M4:QA-NYELV-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M4.1:1206; M4.2:896; M4.3:650; M4.4:704; M4.4:737
- **Probléma:** Az ADV-1 betoldása kötőszó nélkül követi a „csak a kijelölt mentorod láthatja / látja” mondatot. Így a „csak … is” ellentmondásnak olvasható. Az M4.4 két helyén vessző köti a két főmondatot kötőszó nélkül, a többi három helyen pontosvessző: az öt hely írásjele sem egységes.
- **Bizonyíték:** M4.4:704 „A vázlatodat csak a kijelölt mentorod (értékelőd) látja, technikai okból a Moodle rendszergazdája is hozzáférhet;” · M4.1:1206 „…ha ténylegesen szükséges; technikai okból a Moodle rendszergazdája is hozzáférhet.”
- **Hatás:** Az adatvédelmi ígéret két fele ütközni látszik, a tanuló nem tudja, melyik igaz.
- **Javaslat:** A kivételt kötőszó jelölje. M4.1, M4.2, M4.3: „; technikai okból a Moodle rendszergazdája is hozzáférhet.” → „; technikai okból azonban a Moodle rendszergazdája is hozzáférhet.” M4.4:704 és :737: „látja, technikai okból a Moodle rendszergazdája is hozzáférhet;” → „látja, de technikai okból a Moodle rendszergazdája is hozzáférhet;”. A „csak” és a „csak akkor, ha ténylegesen szükséges” feltétel nem törölhető. Az M5.4:45 és :324 azonos betoldása scope-on kívül esik: a fő session döntse el, egységesíti-e.
- **Típus:** objektív

**M4:QA-NYELV-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M4.1:53; M4.2:57; M4.3:53; M4.4:62 („Ha elakadsz” doboz)
- **Probléma:** Az új feltétel második „ha”-mellékmondatként kerül a megmaradt „Ha a kapunál akadsz el, ez nem zsákutca:” nyitány alá, így két feltétel ágyazódik egymásba. Az M4.3-ban ugyanez a doboz a kvízt „kapukvíz”-nek hívja, ezért ott a „kapunál” a kvízre utal, a folytatás viszont a vázlatról szól: a feltétel és a következmény elválik.
- **Bizonyíték:** M4.3:53 „…nem mentődik a válaszod a kapukvízben…” · „Ha a kapunál akadsz el, ez nem zsákutca: ha a modul végén leadott peulabemutató-vázlatodban a mentorod visszajelzése szerint még hiányzik…”
- **Hatás:** Az M4.3-ban a kvízen elakadó tanulónak szóló „nem zsákutca” más helyzetre ad választ. A doboz nehezen olvasható fel.
- **Javaslat:** Mind a négy helyen azonos csere. OLD: „Ha a kapunál akadsz el, ez nem zsákutca: ha a modul végén leadott peulabemutató-vázlatodban a mentorod visszajelzése szerint még hiányzik vagy nem érthető valamelyik elem, az” → NEW: „Ha a modul végén leadott peulabemutató-vázlatodnál akadsz el, ez nem zsákutca: ha a mentorod visszajelzése szerint még hiányzik belőle vagy nem érthető valamelyik elem, az”. Az ERT-8 szerinti F-peula-kiváltó nem változik. A „Ha a kapunál akadsz el” a PT:242 modulközi formulája, amelyet a terv a kánoni körhöz rendel. Ha a fő session a nyitányt megtartja, legalább az M4.3-ban egyértelművé kell tenni, melyik kapuról van szó.
- **Típus:** objektív

**M4:QA-NYELV-3**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M4.1:1182; M4.3:628
- **Probléma:** A dia szövegében a „két válasz” és a „két mondat” előzmény nélkül áll (névmási zuhanás, cím és instrukció széttartása).
  - Az M4.1 dián egyetlen kérés van, a narráció pedig „2 dolgot” mond. Ez az 1. kérdés két eleme, nem a két válasz.
  - Az M4.3 dián csak „gondold végig” áll, a „2 rövid mondat” kérése csak a mező promptjában szerepel.
  - Az M4.2:875 mintájában az előzmény megvan.
- **Bizonyíték:** M4.1:1182 „Zárásként írd le röviden, mire figyelsz majd… A két választ a lecke után következő…” · M4.3:628 „A két mondatot a lecke után következő **„M4.3 – Reflektív kérdés”** szövegmezőbe írd be.”
- **Hatás:** A tanuló nem tudja, melyik két válaszról vagy mondatról van szó; az M4.1-ben a „2 dolog” és a „két válasz” összekeverhető.
- **Javaslat:** M4.1:1182: „A két választ a lecke után következő” → „A válaszaidat a lecke után következő” (az M4.2:55 fordulata). M4.3:628: „A két mondatot a lecke után következő **„M4.3 – Reflektív kérdés”** szövegmezőbe írd be.” → „Erről írj 2 rövid mondatot a lecke után következő **„M4.3 – Reflektív kérdés”** szövegmezőbe.” (a mező promptjának kérése).
- **Típus:** objektív

**M4:QA-NYELV-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:128 (Kapu 1, „Következmény”)
- **Probléma:** Két hiba van a sorban.
  - (a) A régi „A hiányzó completion” alany helyére „ez” került, ami a legközelebbi előzményre, a „jelzés a mentornak / stábnak”-ra mutat (3. minta, névmási zuhanás).
  - (b) A záró feltételmondat fejlesztői, compliance-regiszterű („validált értékhatár”, „Moodle runtime-teszt”) és főnévtorlódásos, pedig a mentoroknak szóló sorban áll. A hubban máshol nincs „runtime” vagy „validált”.
- **Bizonyíték:** „jelzés a mentornak / stábnak: ez lemaradás,” · „Egyéni jelzés csak rögzített feladatszerkezet, validált értékhatár, hozzáférési szabály és Moodle runtime-teszt után vezethető be.”
- **Hatás:** Bizonytalan, mi a „lemaradás” alanya. A feltételmondat fejlesztői kikötés, a stáb nem tudja végrehajtani.
- **Javaslat:**
  - (a) „jelzés a mentornak / stábnak: ez lemaradás, a résztvevő csendes pótlással pótolja.” → „jelzés a mentornak / stábnak. A hiányzó completion lemaradás: a résztvevő csendes pótlással pótolja.”
  - (b) A mondat szó szerint kerüljön fejlesztői megjegyzésbe: „*(Fejlesztői megjegyzés: egyéni jelzés csak rögzített feladatszerkezet, validált értékhatár, hozzáférési szabály és Moodle runtime-teszt után vezethető be.)*”. A feltétellista az ERT-24 miatt nem rövidíthető.
- **Típus:** objektív

**M4:QA-NYELV-5**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv (D10 terminológia)
- **Hely:** HUB:138; M4.B:278 (a „modell” szót használja: HUB:137, :138, M4.B:299, M4.4:597, :790)
- **Probléma:** Ugyanarra a sémára a két új mondat „szerkezet”-et ír, a modul többi hat helye „modell”-t, köztük ugyanaz a HUB-megjegyzés és az M4.B:299. A HUB:138-ban a „kötelezően a … szerkezetben” határozó ige nélkül lóg.
- **Bizonyíték:** HUB:138 „…lehetséges nyitó kérdés –, kötelezően a Megfigyelés → Hatás → Következő lépés szerkezetben; … a mentor a Megfigyelés → Hatás → Következő lépés modell szerint ad…”
- **Hatás:** Egy fogalomra két név jut. Az M4.B-ben a :278 és a :299 egymás alatt két külön sémának olvasható.
- **Javaslat:** HUB:138: „–, kötelezően a Megfigyelés → Hatás → Következő lépés szerkezetben;” → „–, és kötelezően a Megfigyelés → Hatás → Következő lépés modellt követi;”. M4.B:278: „a **Megfigyelés → Hatás → Következő lépés** szerkezetben add:” → „a **Megfigyelés → Hatás → Következő lépés** modell szerint add:”. A PRG-10 szerinti kötelező/opcionális besorolás nem változik.
- **Típus:** objektív

**M4:QA-NYELV-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:137 („Ajánlott folyamat”)
- **Probléma:** A változatlan mondat a társas és a mentori visszajelzést „formáló ↔ strukturált” ellentétként választja szét. A PRG-10 átvezetése óta (HUB:138, M4.B:278) a társas visszajelzés is kötelezően a Megfigyelés → Hatás → Következő lépés sémát követi, így ez a megkülönböztetés elavult (7. minta).
- **Bizonyíték:** HUB:137 „Így a társas (leadás előtti, formáló) és a mentori (leadás utáni, strukturált) visszajelzés nem mosódik össze.”
- **Hatás:** A társas visszajelzés egyszerre „nem strukturált” és kötelezően strukturált; ezt a mentor ellentmondásként olvassa.
- **Javaslat:** A különbséget a HUB:138 saját megkülönböztetése adja (élő előadás ↔ írásos vázlat): „(leadás előtti, formáló) és a mentori (leadás utáni, strukturált)” → „(leadás előtti, az élő előadásra adott) és a mentori (leadás utáni, az írásos vázlatra adott)”. Ha a „formáló / strukturált” címkét meg kell tartani, az tartalmi döntés: a modulgazdáé, a QA a szakmai lektoré.
- **Típus:** objektív

**M4:QA-NYELV-7**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M4.4:62
- **Probléma:** A „vagyis nem blokkoló” magyarázat a „formáló” után áll, így azt magyarázza, nem a döntés szerinti „puha”-t. Tanulói szövegben négy jelző torlódik.
- **Bizonyíték:** „– a beadás után is tőle kapsz puha, formáló, vagyis nem blokkoló, fejlesztő visszajelzést.”
- **Hatás:** A tanuló azt érti, hogy „formáló” = „nem blokkoló”.
- **Javaslat:** → „– a beadás után is tőle kapsz formáló, fejlesztő visszajelzést; ez „puha” visszajelzés, vagyis nem blokkol.” Forrás: PRG-16 („„puha” = nem blokkoló fejlesztő visszajelzés”) és a Glosszárium („Puha kapu: formatív, **nem blokkol**”). Mind a négy jelző megmarad.
- **Típus:** objektív

**M4:QA-NYELV-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M4.F:52
- **Probléma:** Az ADV-11 betoldása személytelen „ellenőrizni kell”-lel zárul, nem derül ki, ki ellenőriz. Ugyanennek a döntésnek az M5.F:56 és az M6.F:96 szerinti megfogalmazása a résztvevőt nevezi meg („mindenki … ellenőrzi”).
- **Bizonyíték:** „a munka végén ellenőrizni kell, hogy a munkamenet lezárult, és a letöltések törlődtek.”
- **Hatás:** A képzői instrukció nem egyértelműen végrehajtható, és a három F-peula közös protokollja eltér.
- **Javaslat:** → „a munka végén mindenki ellenőrzi, hogy a munkamenet lezárult, és a letöltései törlődtek.” Ha a modulgazda a képzőnek szánta az ellenőrzést, az tartalmi döntés, nem nyelvi javítás.
- **Típus:** objektív

**M4:QA-NYELV-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M4.A:58; M4.B:63; M4.F:80
- **Probléma:** A GK:63 kánoni utalásából kiesett a „tanulói” minősítő (2. minta). A peulafájlokban nincs „Ha ez a téma téged is érint” blokk, csak az M4.1:55 és az M4.2:59 leckében, így a képző nem tudja, hol keresse. Az M4.F-ben ráadásul egy mondaton belül vált a személy: a tegező felszólítás után („tereld őt”) többes szám első személy jön („nem küldünk ki”). Ez utóbbi alacsony bizalmú.
- **Bizonyíték:** GK:63 „(a tanulói „ha téged is érint” blokk: §4.3)” ↔ M4.F:80 „…tereld őt biztonságos támogatási útra (a „Ha ez a téma téged is érint” blokk); felkavart kiskorút nem küldünk ki egyedül:”
- **Hatás:** Helyben kezelendő helyzetben a képző nem találja a hivatkozott támogatási utat.
- **Javaslat:** Mindhárom helyen: „(a „Ha ez a téma téged is érint” blokk)” → „(a tanulói „Ha ez a téma téged is érint” blokk szerint, lásd M4.1, M4.2)”. Az M4.F-ben opcionális: „felkavart kiskorút nem küldünk ki egyedül” → „felkavart kiskorút ne küldj ki egyedül”. Ez elhagyható, ha a kánoni szó szerinti alak marad. A szabály tartalma (kijelölt biztonságos hely és egy felnőtt) nem változhat.
- **Típus:** objektív

**M4:QA-NYELV-10**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M4.4:771 (`@asset` technical.note, BUILD-blokk)
- **Probléma:** Többelemű terméknév és köznév összetétele kötőjel nélkül.
- **Bizonyíték:** „Szerkeszthető dokumentum: .docx (Google Doc változat csak szervezeti fiókban…”
- **Hatás:** Helyesírási hiba kerül a generált média-leltárba (fejlesztői szöveg).
- **Javaslat:** „Google Doc változat” → „Google Doc-változat”. Utána `python3 tools/media_manifest.py build`, külön `chore(media)` commitban.
- **Típus:** objektív

---

Az ADV-1 betoldásnak egy nyelvi problémája van, a QA-NYELV-1. A mondat egyébként természetes, tegező, és az öt helyen azonos a szóhasználat.

Nincs P0/P1 finding, és nincs levágott finding.
