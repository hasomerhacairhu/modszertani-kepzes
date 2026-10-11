# 2026-10-11 Validált findingok – Z, AP-2026-10-11-01

> **Audit trail — nem kánon, nem tanulói tartalom.** Read-only `/course-review Z --lens all --run AP-2026-10-11-01`
> (`next-version` autopilot-futás). A tananyag a review alatt nem változott.
>
> - **Scope:** a teljes Z modul (6 fájl: hub, Z.1–Z.4, Z.A), egy fájlcsoportban (G1). Korábbi validált Z-riport: nincs.
> - **Lencsék:** pedagogy, assessment, language, safety, implementation (`--lens all`). **Run-ID:** AP-2026-10-11-01.
> - **Review-bázis:** `378d820` (a `02 Tervezet/` tartalma azonos a `main@213a4c5`-tel); nem commitolt változás a scope-ban: nincs.
> - **Read-only bizonyíték (kezdet):** `git diff HEAD -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`;
>   `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`.
> - **Hipotézisforrás:** a 2026-10-10-i Anna-megfeleltetési mátrix Z-sorai — audit trail, nem kánon; a lencsék a jelenlegi
>   szövegen ellenőrizték.
> - **Állapot:** VALIDÁLT — minden ID-nak verdiktje van (57/57, V1–V4); read-only bizonyíték a mentés előtt: mindkét érték `da39a3ee5e6b4b0d3255bfef95601890afd80709` (változatlan); a köztes, átfedéses M0/M1-javítások (`df2792d`, `69c2017`, `1d9d15f`, `e16a4e1`, `ed4f52d`, `506fa78`) a Z scope-ját nem érintik.
> - **Szerkezet:** I. riport · A. verifier-kontextus · B. verdiktek · C. nyers lencse-kimenetek (szó szerint; a helyi
>   abszolút útvonal-előtag repó-relatívra rövidítve, sorvégi szóközök törölve).

---

# I. Z – validált riport (2026-10-11)

> Read-only review. Tananyag nem változott. Nyers findingok: C. melléklet (57 = egyetlen fájlcsoport, G1: hub,
> Z.1, Z.2, Z.3, Z.4, Z.A) PED-G1-1…10, ERT-G1-1…8, IMPL-G1-1…11, BIZT-G1-1…10, NYELV-G1-1…18; verdiktek: B.
> melléklet (4 verifier, V1–V4, 57/57). Git-history a reviewereknél és a verifiereknél nem állt rendelkezésre: a
> baseline kérdésre mindenhol „baseline ismeretlen”, a súlyosság emiatt sehol nem emelkedett ezen az alapon.

## 1. Scope és futtatott lencsék

- **Scope:** a teljes Z modul (6 fájl: hub, Z.1–Z.4, Z.A), egy fájlcsoportban (G1). A Z **puha, nem kapuzó záró
  modul** (PT §5, PT:259: „Puha kapuk: M0, M2, M4, Z” — formatív, nem blokkol; PT:113: „nincs éles kapu,
  completion-alapú”). A Z teljesítése: Z.1–Z.4 (a Z.3-nál az LMS-Z-06 beküldésével, a Z.4-nél az LMS-Z-04
  leadásával és az LMS-Z-08 = „Teljesítve” értékkel) + a Z.3 mentori elfogadása (LMS-Z-07 = „Teljesítve”) +
  Moodle Feedback → online félév teljesítve (MAN:163).
- **Ténylegesen lefutott lencsék:** `pedagogy`, `assessment`, `implementation`, `safety`, `language` — mind teljes;
  hiányos lencse nincs.
- **A biztonság-jog lencse kötelező triggerje** (Grep mind a 6 Z-fájlon, kis- és nagybetű nélkül): `gyermekvédel`
  szókezdet 31 sorban, mind a 6 fájlban; `adatvéd` szókezdet 10 sorban; `kiskorú` szókezdet 1 sorban (Z.3:293:
  „miközben te magad is lehetsz még kiskorú, hiszen a képzés 15 éves kortól szól”); `feltárás` szótő 4 sorban;
  `önfeltár` szótő 1 sorban (Z.2:307: „A teljesítéshez nem kell érzékeny önfeltárás”); önálló `AI` szó 22 helyen,
  de `@asset`-blokkokon kívül csak fájlnév-hivatkozásként (`Adatvédelem – tanulói adatok és AI.md`) — tartalmi
  AI-provenance jegyzet (`provenance_note: "AI-generált"`) a 6 fájlban kizárólag `@asset`-blokkban áll. Tartalmi
  trigger: a Memuna-bevonás eszkalációs sorrendje (Z.3, Z.A), a Feedback-ág gyermekvédelmi feltárása (Z.4), a
  videós hozzájárulás és a mentorjegyzet megőrzése (Z.4), a kiskorú madrih szerepköre (Z.3).
- **Korábbi validált riport:** a Z-re nincs; újrahasznosítás (REUSED) nincs.
- **Read-only bizonyíték:** a kezdő és a mentés előtti `git diff HEAD -- "02 Tervezet" | shasum` és
  `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` egyaránt ``da39a3ee5e6b4b0d3255bfef95601890afd80709`` (a fejléc két sora,
  `head.md`). A review alatt a hat Z-fájl nem változott (`git diff --stat 378d820 HEAD -- "02 Tervezet/Modulok/Z"` üres); a
  köztes `02 Tervezet/`-változás csak a projektgazda 2026-10-11-i gyorsítási döntése szerinti M0- és M1-javítás
  (`df2792d`, `69c2017`, `1d9d15f`, `e16a4e1`, `ed4f52d`, `506fa78`), a Z fájljait egyik sem érinti.
- **Fájlkulcsok:** HUB = a Z modulhub (`Z – Zárás & híd a terepre.md`) · Z.1–Z.4 = az online leckék · Z.A = a záró
  kvuca-peula · MAN = `LMS – activity manifest` · RA = `LMS – H5P runtime acceptance` · A11Y = `LMS –
  hozzáférhetőségi sztenderd` · ADV = `Adatvédelem – tanulói adatok és AI` · GK = `Gyermekvédelem – release gate`
  · HUM = `Emberi jóváhagyás szükséges` · PT = `Program terv` · RR = `RELEASE-READINESS` · GL = a Glosszárium ·
  DÖNT = a 2026-10-02-i döntési jegyzőkönyv · TEREP = `Terepgyakorlat`.

**Számok (a verdiktsorokból, duplikátumokkal; 59 sor = 57 nyers finding + 2 objektív alpont):**
MEGERŐSÍTVE + objektív 26 (ebből 3 duplikátum) · MEGERŐSÍTVE + bizonyíték-kapu 1 (0 duplikátum, 3 kapura mutat) ·
EMBERI DÖNTÉS 23 (ebből 9 duplikátum, közülük 6 más modul kapujába: `M0:ERT-3`, `M0:IMPL-3`×1, `M2:BIZT-G2-3`×2,
`M2:BIZT-G3-2`, `M1:IMPL-G2-10`) · ELVETVE 9 — összesen 59, ebből 12 duplikátum. **Megtartott:** 21 objektív OPEN
finding (3 P1: `ERT-G1-2`, `PED-G1-1`, `BIZT-G1-3`; 18 P2) + 2 objektív alpont emberi döntésű tételből
(`BIZT-G1-2.obj` P1, `BIZT-G1-9.obj` P2) = 23 OPEN sor; 1 bizonyíték-kapu (P1, `BIZT-G1-10`, három kapura); 14
emberi döntés (6 P1: `BIZT-G1-1`, `BIZT-G1-2`, `ERT-G1-1`, `ERT-G1-3`, `ERT-G1-4`, `IMPL-G1-3`; 8 P2).

**Súly- és típusmódosítás a verifiernél:** P1 → P2: `IMPL-G1-2` (a lencse P1-et adott; a lánc ép, completion nem
sérül). Típusváltozás: `IMPL-G1-8` a lencse szerinti bizonyíték-kapu helyett emberi-döntés (ADV:139; a megvalósítási
döntést a projektgazda jóváhagyta, a hiányzó formális bizonyíték nem azonos a nyitott DPO-kérdéssel).

## 2. Validált objektív findingek (23: 4 P1, 19 P2)

Javítási út: `/course-fix` vagy `/hungarian-edit` (6. szakasz). `@asset`-mező csak `media_manifest.py build` úton,
külön `chore(media)` commitban; `@source` csak hanggyártási fix packon át, újrarenderelés mellett. Answer key,
küszöb, rubrikaszint, completion-logika és kötelező/opcionális besorolás egyik tételnél sem változik. A két `.obj`
sor emberi döntésű tétel döntéstől független objektív alpontja (a fő tétel: 3. szakasz). Közös kánoni fájlt
(`LMS – activity manifest.md`, HUM, Glosszárium, Program terv, ADV, GK, RA) saját szerkesztési célként érintő
javítás nincs a megtartott tételek között — mindegyik a Z modul saját fájljait (HUB, Z.1–Z.4, Z.A) módosítja, a
kánoni fájlok csak hivatkozási forrásként szolgálnak. Az `M0:NYELV-G2-18` Z.A-helyei (induló-szavak: Z.A:55, :423,
:440, :458) egy M0-tétel részei (a ledgerben IN_PROGRESS), itt csak említés; a `NYELV-G1-7` ezeket kizárja.

### P1 (4)

| ID | Hely | Probléma | Javítás és korlát |
|---|---|---|---|
| ERT-G1-2 (= IMPL-G1-1 (a)–(c); duplikátum: K1) | HUB:199; Z.4:341, :343 ↔ MAN:19, :25, :110–111, :163 | állapotmodell és skálasorrend: az LMS-Z-08 0 találat a Z-ben, a Z.4:343 kézi megerősítés útja és a Z.4:341 skálasorrendje ellentmond a BSPEC-07/D-h-nak és a GATE-CP kézi felülírási tilalmának | a MAN négy helyének szó szerinti átvezetése; a „Teljesítve” tartalmi mércéjéhez (ERT-G1-1), a címkepárhoz, az 1+1 beadáshoz és a puha kapu jellegéhez nem nyúl; egy szerkesztésben a HUB §5 3. pontjával |
| PED-G1-1 | HUB:33 ↔ MAN:247, Q-REL-2 (HUM:510), BS-D3 (HUM:517) | a Z nyitási mondata („Mivel a Z az M7 megerősített teljesítése után nyílik”) hamis a javítási úton lévő madrihnál; a Z.3:215 feltételes mondata leadott Peula v2-t feltételez | csere a MAN:247 szövegére, egy szerkesztésben az ERT-G1-7-tel (HUB:33); a Z.3 feltételes mondata csak v1-re és a nem validált M7.B:563-ra mutathat; a :237 mintaszöveg az NYELV-G1-2 verdiktjétől függ (sorrend) |
| BIZT-G1-3 | Z.3:61 ↔ MAN:108 (BS-D6) | a lecke állítása („a megőrzési időt a 3. szakasz mátrixa rögzíti”) hamis: a BS-D6 szerint az LMS-Z-06 megőrzése nyitott DPO-döntés | a MAN:108 BS-D6-mondata szó szerint át; megőrzési sort a javítás nem választ; a HUM-PRIV-01 és a Program terv §4 nyitási feltétele marad |
| BIZT-G1-2.obj (a BIZT-G1-2 alpontja) | Z.4:201 | a „(ugyanaz, mint az M3.3-ban)” hivatkozás objektíven pontatlan: az M3.3:859 szövege más, olvasói/mentori bevonási kötelezettség nélkül | a hivatkozás pontosítása vagy elhagyása; a szabály szövegéhez, a 112-höz és a „nem ígérünk teljes titoktartást” mondathoz nem nyúl; a BIZT-G1-2 fő, emberi döntésű tétele (a Feedback-ág kezelési útja) külön marad a 3. szakaszban |

### P2 (19)

**Pedagógia**

| ID | Hely | Probléma | Javítás és korlát |
|---|---|---|---|
| PED-G1-6 | Z.A:212 ↔ :213, DÖNT:67 (12. pont) | a felolvasandó utasítás (3–4 perc) ellentmond a képzői sornak és a lezárt „3 perc/fő” döntésnek | csak a :212 értéke „kb. 3 perc”-re; a PED-G1-7 (ELVETVE) tilalma a :81/:403-ra szól, ide nem |
| PED-G1-9 | Z.A:32 ↔ :312 | az eszközlista csak A4-et ad a posztermunkához, a 4.3/1. lépés kiscsoportonként flipchart/A3-at oszt; a Z.A-MUNK-01 notes mezője (:291) téves | szűkítés: új tétel a :32 alá („kiscsoportonként 1 flipchart lap vagy A3, Z.A-MUNK-01 sablon”); az A4-sor marad; a :516 „Papírok” és az `@asset` mező nem változik |

**Implementáció**

| ID | Hely | Probléma | Javítás és korlát |
|---|---|---|---|
| IMPL-G1-2 (megtartandó, PED-G1-2 ide olvad; duplikátum: K3) | Z.3:236, :298, :302, :318, :348 | a szöveges válaszok helye és ideje nincs megmondva a tanulónak; a Z.3:236 mintaszöveg Moodle Feedback „Longer text answer”-ben nem valósítható meg (`textarea_form.php`) | (a)–(b) útbaigazítás a 4./7. dián; (c) csak a kérdéscímke-rész (TEXT-C); a „MAN:108 Megjegyzés”-rész kimarad (M2-mintájú redundancia); a mintaszöveg előbb a NYELV-G1-2 verdiktjét várja; a :300 szabálymondat (BIZT-G1-1) érintetlen |
| IMPL-G1-5 (megtartandó, ERT-G1-5 ide olvad; duplikátum: K8) | Z.1:13, :335, :382 | a Single Choice Set típusnév ellentmond a Z.1 kérdésenkénti visszajelzésének; a :382 maga mondja ki a hiányt | típusnév h5p-multi-choice-ra (egyválaszos); a :382 szűkítve; felülírja az NYELV-G1-8 „Single Choice Set” megtartását, egy sorban; a ✅-ok, opciók és a SLIDE 4 completion-szerepe nem változnak |
| IMPL-G1-6 | Z.1:266, :531 ↔ VO D-19/D-21 | a kötelező a11y-utasítás „(vagy adj hozzá magyar feliratot)” alternatívája ellentmond a lezárt döntésnek (H5P Audio-tól feliratsáv nem várható) | csak a zárójeles alternatíva cseréje a VO D-19/D-21 fordulatára; `@source`/`@asset` nem változik; látható szöveg, pin kell; a NYELV-G1-6 Z.1:271-es javítása csak VO-újrarenderrel kerülhet be egyszerre |
| IMPL-G1-10 (duplikátum: K9; (a) → NYELV-G1-4) | HUB:195; Z.1:59 | (a) activity-név eltérés → NYELV-G1-4; (b) HUB:195 „érdemes” unlock-szöveg, holott a MAN:110/:112 kötelezővé teszi; (c) Z.1:59 a D-2 óta nem létező mezőkre hivatkozik | (b) a HUB:195 szerkesztése; (c) minta: Z.2:65; a (d) alpont (HUB:171↔PT:307) kiesik, szükségtelen módosítás (2026-10-10, 5. pont) |

**Biztonság-jog**

| ID | Hely | Probléma | Javítás és korlát |
|---|---|---|---|
| BIZT-G1-9.obj (a BIZT-G1-9 alpontja) | Z.A | hiányzik a HUM-PRIV-02-re és az ADV §6-ra mutató képzői hivatkozás a Z.A médiaaktivitásainál | az M1:BIZT-G3-8.obj mintájára átvezetve, legfeljebb a HUM:151 szó szerinti alapértelmezésével; a papírok (plakát, cetlik, poszterek) sorsáról nem állít semmit — az a BIZT-G1-9 fő, emberi döntésű tételének kérdése |

**Nyelv**

| ID | Hely | Probléma | Javítás és korlát |
|---|---|---|---|
| NYELV-G1-1 | Z.3:368 ↔ :381, :315 | „Zmán Kvucával” ↔ „Zmán Kvucára” esetrag-eltérés | csak az esetrag; az opciók és a ✅ (M7) maradnak; a K8 típusdöntésétől független |
| NYELV-G1-2 | Z.3:237, :222 | a mintaszöveg két helyhatározót tesz egymás mellé; a :222 MIKOR-példát is igazítani kell | a „A következő 3 Zmán Kvucámon…” nyitás betűre marad; sorrend: előbb ez, utána IMPL-G1-2 (c); a PED-G1-1 korlátjával ütközik — ez a verdikt irányadó |
| NYELV-G1-4 (megtartandó, IMPL-G1-10 (a) ide olvad) | HUB:190, :46; Z.A:24 | a Moodle-activity neve eltér a manifest „Név” értékétől (Feedback, Assignment) | a lecke/hub veszi át a MAN „Név” értékét; fájlnév és link nem változik |
| NYELV-G1-6 | HUB:109; Z.4:61 (két hely), :137, :190, :198, :233, :320; Z.A:23 | hiányzó névelő az azonosító előtt, teljes mondatos helyeken | csak a teljes mondatos helyek; a zárójeles/távirati helyek kimaradnak; a Z.1:271 `@source` csak VO-újrarenderrel (korlát: IMPL-G1-6); pin |
| NYELV-G1-7 | Z.A (10+ hely), HUB:91, :92, :165, Z.2:107, Z.4:191–192 | kötőjeles, illetve különírt köznévi összetételek egységesítése | az M0:NYELV-G2-18 Z.A induló-szó-helyei kizárva; héber tagú összetételek és tulajdonnevek kimaradnak; a Z.A:291/:480 csak build úton, `chore(media)` commitban; a :343 a NYELV-G1-17-tel egy szerkesztésben |
| NYELV-G1-8 | Z.1:321; Z.4:383, :385; Z.1:57, Z.3:59 | „Multi Choice”/„Single Choice” nem létező H5P/Moodle típusnév | a dia-címkékkel egy menetben; a „Single Choice Set” megtartása nem akadályozhatja a K8 (IMPL-G1-5) döntését; ✅ nem változik |
| NYELV-G1-9 | Z.A:11 | „madrihok (15+)” a Glosszárium:72 „/ madrihot” alakja nélkül | csak a „/ madrihot” kerül be, a „15+” marad |
| NYELV-G1-10 | Z.A:206 | a felolvasandó blokkban mondaton belüli személyváltás | csak a Z.A:206-ra szűkítve; a Z.1:34, a Z.4:53, a Z.A:405–406 és az „M0.1–M0.2 online leckében” egyes száma elvetve (riport I.5) |
| NYELV-G1-12 | Z.A:403 | „45'-ben kihagyható” (= opcionális) ↔ a percbontás szerint a névhúzás kimarad, nem választható | csak a szó cserélődik; a percek és a 75'-es 6 perc marad; a PED-G1-7 elvetésével nem tárgytalan |
| NYELV-G1-13 | Z.A:459 | „írj rá 1 szót… Lehet… mondat” ellentmond a négy „1 szó” helynek (:414, :452, :460, HUB:140) | csak a „mondat” szó törlődik; a BIZT-G1-9 :459-es helyei nem változnak |
| NYELV-G1-17 | Z.A:343 | „75' verzió” a mértékjelölő -es képző nélkül | csak „75'-es verzió”; egy szerkesztésben a NYELV-G1-7 „elismerés-kör” javításával |
| NYELV-G1-18 | Z.2:18; Z.A:105; HUB:124 | hiányzó vessző a mellérendelt függő kérdések között (AkH) | csak a vessző; az ERT-G1-8 elvetésével nincs összefésülési ütközés |

## 3. Emberi döntést igénylő tételek — javasolt szöveg nélkül

P1 → P2 sorrendben (P1: az első 6; P2: a következő 8). A Külső kapuk hozzárendelése: az `AUTOPILOT-LEDGER.md`
Külső kapuk táblája (a ledger-sorok `(X-n)` hivatkozásai; a javasolt kiegészítések a kivonat `z-gates.md` fájljában).

| ID | Kérdés | Ki dönt |
|---|---|---|
| ERT-G1-1 | a Z.4 „Teljesítve” tartalmi mércéje: a HUB hármas minimuma ↔ MAN:111/:173 „tényleges, minimálisan értelmezhető tartalom” ↔ Z.4:347/:353 tanácsjellege; valódi küszöbdöntés, a kánonból nem dönthető el | értékelési felelős; vétó/QA: programvezető (X-6) |
| BIZT-G1-1 | a Z.3:300 kötelező, mentor által elfogadandó eszkalációs mondata (kiskorú madrihnak „nem vezetek éles foglalkozást, hanem jelzem a képzőnek”) a kánonban máshol nincs rögzítve; a jelzés címzettje és a már jelen lévő hanihok esete | Memuna, programvezetővel (X-5) |
| BIZT-G1-2 | a Z.4 Feedback-ágán a gyermekvédelmi feltárásnak nincs kezelési útja; a tanulói mondat iránya (:201/:370); objektív alpont: BIZT-G1-2.obj | Memuna + DPO (X-5, X-4) |
| ERT-G1-3 | a HUB:198 a Z.A-t a „Minimális teljesítés” 2. pontjaként sorolja, a PT:211–213/MAN:163/:165 nem; a hiányzóknak nincs pótlási útja | programvezető + értékelési felelős (X-6) |
| ERT-G1-4 | a Z.4 Feedback egyik kérdése sem „Required”, az üres beküldés is teljesít (:403 „mark as complete when submitted”); a HUM:457 „Üres sablon” szabály kiterjedjen-e a Feedbackre | értékelési felelős; vétó/QA: DPO + programvezető (X-6) |
| IMPL-G1-3 | a Z.3 SLIDE 5 (:11, :260–263) beágyazott szöveges mezője tanuló-lokális vagy negyedik LMS-Z-06 kérdés-e (a D-2/D-3 mintájára); a PED-G1-2 3. pontja ide tartozik | projektgazda mint build-spec gazda; DPO/jogi QA (X-4) |
| BIZT-G1-5 | a Z.4 opcionális videós útja: hol rögzül kiskorúnál a résztvevő és a gondviselő együttes hozzájárulása, ki ellenőrzi a feltöltés előtt, vonatkozik-e rá az ADV §6 fotószabálya | DPO + jogi felelős (X-4) |
| BIZT-G1-7 | a Z.4:398 Feedback „Show analysis page” és az IMPL-G1-11 „Enable notification of submissions” értékét a HUM-PRIV-03 gazdája rögzíti; a kódbeli alapérték „No” | DPO + programvezető (X-4) |
| BIZT-G1-8 | (b) az érzelmi önbevallás (Z.2:236–240, Z.3:121–127) fiókhoz kötött tárolása és tanári láthatósága elfogadható-e (ADV:150, a D-j mintájára) | DPO (X-4); az (a) alpont = M0:ERT-3 duplikátum (X-6) |
| BIZT-G1-9 | a Z.A papíralapú anyagainak (plakát, képzői idézetek, névcetlik, poszterek, szófelhő) sorsa és fotózhatósága; objektív alpont: BIZT-G1-9.obj | DPO (X-4) |
| ERT-G1-7 | a Z saját javító útjának és az LMS-Z-07 mentori megerősítésének időpontja: a MAN:249 csak a puha M2/M4-re rendezi, a Z-re nem; az LMS-Z-07 határideje „—” | programvezető, HUM-OPS-01 (X-10) |
| NYELV-G1-14 | a Z.A:53 (előbb Memuna-bevonás, aztán odalépés) ↔ :226 (odalépés, Memuna nélkül) két eltérő sorrend egy gyermekvédelmi eljárásban | a Memuna eljárási kérdése (X-5) |
| NYELV-G1-15 (= PED-G1-10) | a Z.3:147 cím („Ha túl kicsit, túl általánosat:”) ↔ a :148 példa (csak az általánosságot mutatja) széttartása; a „túl kicsi” hibatípus szándékos-e | modulgazda vagy projektgazda (X-10) |
| PED-G1-4 | a HUB:92 a Z.3-ba általánosító lépést ír elő, a Z.3-ban nincs ilyen lépés és Z.2-hivatkozás sincs; a megoldás egyik ága új tartalom | modulgazda (X-10) |

- **Más modul nyitott kapujába olvadt:** `BIZT-G1-4` = `M2:BIZT-G2-3` (X-4; Z.4:98/:329/:307 „csak a kijelölt
  mentorod”, videós úttal együtt) · `IMPL-G1-4` = `M2:BIZT-G2-3` (X-4; ugyanaz a tényállás, Z-többlet nélkül;
  mindkettő közvetlenül a végső kulcsra mutat) · `BIZT-G1-6` = `M2:BIZT-G3-2` (X-5; második felnőtt a Z.A peulán)
  · `ERT-G1-6` = `M0:ERT-3` (X-6; a Z.1–Z.3 választók D-d/D-i-kiterjesztése) · `IMPL-G1-7` = `M0:IMPL-3` (X-6;
  `cp.js` összefoglaló dia) · `IMPL-G1-9` = `M1:IMPL-G2-10` (X-11; Z.4:336 „Accepted file types” hiánya) ·
  `BIZT-G1-8` (a) alkérdése = `M0:ERT-3` (X-6).
- **Egy csomagban kérdezendő (nem duplikátum, de ugyanaz a döntési kör):** `BIZT-G1-6` és `NYELV-G1-14` (X-5;
  ugyanaz a Z.A biztonsági eljárás, két külön kérdés — a sorrend és a második felnőtt) · `ERT-G1-1`, `ERT-G1-3`,
  `ERT-G1-4` (X-6; mindhárom „mi számít Teljesítve-nek” jellegű kérdés, külön activity) · `BIZT-G1-5` és
  `BIZT-G1-9` (X-4; a Z.A/Z.4 médiaanyagok DPO-kérdései, külön tényállás).
- **Emberi döntésű tétel objektív alpontja:** `BIZT-G1-2.obj`, `BIZT-G1-9.obj` — saját kulccsal, a 2. szakaszban.

## 4. Bizonyíték-kapuk

| ID | Szerep | G-kapu |
|---|---|---|
| BIZT-G1-10 | Memuna: a D-2, D-3, BS-D8, HUM-SAFE-02/03 G1-es, írásos „átnéztem” bizonyítéka hiányzik · DPO: a HUM-PRIV-01–03 G2-es írásos jóváhagyása, az ADV:214/:216 videós release-evidence is ide tartozik · LMS-gazda: az RTA RT-P0-03/-12/-15/-16/-24 sorai `IMPLEMENTATION_TEST_REQUIRED` | Memuna G1 (X-7), DPO G2 (X-12), G3b runtime (X-8) |

A tananyagban nem jelölhető megoldottnak; „átnéztem”, jóváhagyó, dátum és verzió nem írható be. Objektív alpont a
bizonyíték-kapuk között nincs.

## 5. Elvetve (9)

ERT-G1-8 (a Z.2:307/:309 alternatívája és a passzjog eloszlatja a cél↔feladat ellentmondás gyanúját; a javaslat
jelentősen hosszabbítaná a mikrocélt, 2026-10-10, 5. pont; a :18 vesszőjét a NYELV-G1-18 adja) · NYELV-G1-3 (a Z.4
„cél”/„következő lépés” a Z-ben egymás megfelelője, bizonyított félreértés nincs; Anna-szöveg, E-Z-029/030/031
RETAIN, átírása ütközne a 2026-10-10-i döntéssel) · NYELV-G1-5 (a „blokk” és a „szakasz” két külön, a lecke által
megfeleltetett fogalom, bizonyított terminológiai hiba nincs, a csere preferencia) · NYELV-G1-11 (a Z.3:176
„Ezekben közös, hogy:” szabályos szerkezet; a Z.A:319 „nonformális” a képzői forgatókönyv távirati
kulcsszó-listájában áll, nem hiba) · NYELV-G1-16 (az „adatminimalizált” csere regiszterpreferencia: a mondat a
TEREP:15 kánoni szabály szó szerinti átvétele) · PED-G1-3 (a „nincs megvalósítva” állítás túloz: a Z.4:23/:283 és
a Z.A:531–534 ellenőrző pontja rögzíti a sorrendet; a javaslat didaktikai kiegészítés, preferencia, 2026-10-10,
5. pont) · PED-G1-5 (a mikrocélnak nem kell felsorolnia minden elfogadási elemet; a támogató személy köre nem
bizonyítottan ellentmondó, a :279/:283/HUB:96/:287/MAN:109 összhangban áll; gyermekvédelmi szabályt nem érint,
HUM-SAFE-03 külön rendezi) · PED-G1-7 (a Z.A:81 pufferi tanácsa összhangban a HUM:224/DÖNT:67-tel és az
Anna-mátrix E-Z-036 RETAIN sorával; a HUB:32 „péntek 2. sáv” szerint nincs bizonyított blokkhatár-sértés; a „6
perc alultervezett” becslés bizonyíték nélküli) · PED-G1-8 (a Z.2/Z.3 időtúllépése mérés és kánoni számítási norma
nélküli becslés; a lépések tanuló-lokálisak, D-3, a :211 gyermekvédelmi bekezdés nem rövidíthető; a le nem
vezethető időt pilotmérés adja, nem repóbeli javítás).

**Részben elvetett részek a megerősített tételeken belül:** NYELV-G1-10 négy helye (Z.1:34, Z.4:53, Z.A:405–406,
az „M0.1–M0.2 online leckében” egyes száma) — csak a Z.A:206 marad · IMPL-G1-10 (d) alpontja (HUB:171 ↔ PT:307,
a parafrázis jelentése azonos, szükségtelen módosítás, 2026-10-10, 5. pont) · IMPL-G1-2 (c) „MAN:108 Megjegyzés”
fele (az M2:IMPL-G2-7-ben redundanciaként már elvetve) és (d) alpontja (a Z.3:327 maga kéri a magadnak-feljegyzést,
a Z.4:207 nem hibás).

## 6. Következő lépés

**`/course-fix` fájlonként:**

- **HUB** (a modulhub): `ERT-G1-2` (§5 3. pontja, :199), `PED-G1-1` (:33), `IMPL-G1-10` (b) (:195).
- **Z.1**: `IMPL-G1-5` (:13, :335, :382), `IMPL-G1-6` (:266, :531), `IMPL-G1-10` (c) (:59).
- **Z.3**: `BIZT-G1-3` (:61), `PED-G1-1` (:215, feltételes mondat), `IMPL-G1-2` (:236, :298, :302, :318, :348).
- **Z.4**: `ERT-G1-2` (:341, :343), `BIZT-G1-2.obj` (:201).
- **Z.A**: `PED-G1-6` (:212), `PED-G1-9` (:32), `BIZT-G1-9.obj` (képzői hivatkozás a HUM-PRIV-02-re/ADV §6-ra).

**`/hungarian-edit` fájlonként** (pusztán nyelvi tételek):

- **HUB**: `NYELV-G1-4` (:190, :46), `NYELV-G1-6` (:109), `NYELV-G1-7` (:91, :92, :165), `NYELV-G1-18` (:124).
- **Z.1**: `NYELV-G1-8` (:321, :57).
- **Z.2**: `NYELV-G1-7` (:107), `NYELV-G1-18` (:18).
- **Z.3**: `NYELV-G1-1` (:368), `NYELV-G1-2` (:237, :222), `NYELV-G1-8` (:59).
- **Z.4**: `NYELV-G1-6` (:61 két hely, :137, :190, :198, :233, :320), `NYELV-G1-7` (:191–192), `NYELV-G1-8` (:383,
  :385).
- **Z.A**: `NYELV-G1-4` (:24), `NYELV-G1-6` (:23), `NYELV-G1-7` (tíz+ hely, a :291/:480 kivételével), `NYELV-G1-9`
  (:11), `NYELV-G1-10` (:206), `NYELV-G1-12` (:403), `NYELV-G1-13` (:459), `NYELV-G1-17` (:343), `NYELV-G1-18`
  (:105).

**Egy menetben javítandó és sorrendi függések** (a B. melléklet kifejezett kérése):

- **Z.3:222–237** — `NYELV-G1-2` (mintaszöveg-javítás) **előbb**, csak utána `IMPL-G1-2` (c) (a mintaszöveg a
  kérdéscímkébe kerül); a `PED-G1-1` korlátja („a :237 nem változik”) a NYELV-G1-2 verdiktjének enged.
- **HUB §5 „Minimális teljesítés” listája** (:193–200) — `ERT-G1-2` (3. pont, most javítható) és `PED-G1-1`
  (:33, a nyitási mondat, ugyanazon §5-ön kívül) egy szerkesztésben; a 2. és a 4. pont (`ERT-G1-3`, `ERT-G1-4`,
  emberi döntés) ugyanabba a listába tartozik, de a döntés előtt nem módosítható — a mostani szerkesztés a listát
  ne bontsa meg.
- **Z.A:343** — `NYELV-G1-17` („75'-es verzió”) + `NYELV-G1-7` („elismerés-kör”): egy szerkesztésben, ugyanazon
  a zárójelen.
- **Z.1:13/:335/:382** — `IMPL-G1-5` (típuscsere) felülírja az `NYELV-G1-8` „Single Choice Set” megtartását; egy
  szerkesztésben, ugyanazon a soron.
- **Z.1:266–275, :531–539** — `IMPL-G1-6` (zárójeles alternatíva csere) és a `NYELV-G1-6` korlátja (:271 `@source`
  csak VO-újrarenderrel): a két javítás ne kerüljön össze egyetlen szerkesztésbe újrarenderelés nélkül, mert a
  szó szerinti leirat eltérne a hangtól.

**`media_manifest.py build` (külön `chore(media)` commit):** `NYELV-G1-7` Z.A:291, :480 (`@asset`-sorok).

**`--pin-visible`:** a teljes diff visszaolvasása után, változtatáskészletenként egyszer, a validált
finding-ID-kkal. A verifier kifejezetten pint kért: `NYELV-G1-6`, `IMPL-G1-6`; ezen felül minden más látható
szövegváltozás (a 2. szakasz többi OPEN tétele) után a `test_media_manifest` dönt.

**Kánoni közös fájlt érintő javítás:** nincs a megtartott tételek között (lásd 2. szakasz bevezetője).

Az emberi döntések és a bizonyíték-kapu a ledger Külső kapuinál (`AUTOPILOT-LEDGER.md` Külső kapuk: X-4, X-5, X-6,
X-7, X-8, X-10, X-12; a javasolt kiegészítések a kivonat `z-gates.md` fájljában).

---

# A. melléklet – verifier-kontextus

# A. Verifier-kontextus (klaszter-térkép)

## Z — verifier-kontextus és klaszter-térkép (fő munkamenet, 2026-10-11)

Findinglista: a riport C. melléklete — 57 nyers finding, egyetlen fájlcsoport. G1 (hub, Z.1, Z.2, Z.3, Z.4, Z.A): PED-G1-1…10, ERT-G1-1…8, IMPL-G1-1…11, BIZT-G1-1…10, NYELV-G1-1…18.

**Szabályok:** `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” (szó szerint a promptban); a `next-version` felhatalmazás (2026-10-11): validált objektív hiba javítható, új szakpolitikai/gyermekvédelmi/adatvédelmi/értékelési döntés és új pedagógiai tartalom emberi döntés; 2026-10-05 scope-korrekció (M2–Z repo-fixable munka nem POST-PILOT); a 2026-10-10-i döntés 4. pontja (külső kutatási hivatkozás nem igazolt bizonyíték) és 5. pontja (szükségtelen módosítás, redundancia, Anna-szövegezés romlása kerülendő → preferencia = ELVETVE); answer key / küszöb / rubrikaszint csak bizonyított objektív hibánál; `@asset` csak build úton, `@source` csak hanggyártási úton (a finding attól valós lehet); a lezárt döntések: HUM 8–12. szakasz (köztük D-j, D-i, BIZT-R5 nyitott, SAFE-7 nyitott), HUM-SAFE-01…05, HUM-PRIV-01…04, HUM-SOMER-01…03, BSPEC-01…07. Git-history nincs a verifiernél: „baseline ismeretlen”. A Z-ben ezen felül: **a Z nem kapuzó záró modul** (PT §5, PT:259: „Puha kapuk: M0, M2, M4, Z” — formatív, nem blokkol; PT:113: „nincs éles kapu, completion-alapú”; PT:213; HUM:456); `GATE_CONFIRMED_<module>` checkpointot a MAN §4 „Fontos” bekezdése csak az M1, M3, M5, M6, M7-re ír elő (MAN:167), a Z.3 mentori elfogadása és a Z.4 megerősítése mégis GATE-CP profillal készül (MAN:25). **A Z teljesítése és a kurzusteljesítés** (MAN §4 Z-sor, MAN:163): Z.1–Z.4 (a Z.3-nál az LMS-Z-06 beküldésével; a Z.4-nél az LMS-Z-04 leadásával és az LMS-Z-08 = „Teljesítve” értékkel, BSPEC-07) + a Z.3 mentori elfogadása (LMS-Z-07 = „Teljesítve”; BS-D8) + Moodle Feedback → online félév teljesítve (ha az M7 complete és az LMS-M5-07 is teljesült; az M6 és az M7 javítását bevárja); Program teljesítve = Online félév teljesítve ÉS Terepgyakorlat teljesítve (MAN:163; HUM:464). A Moodle-leképezés (MAN:165, a §4 alatt): course completion, „Condition requires” = All, minden „Kötelező = igen” §2-sor, köztük az LMS-Z-04, az LMS-Z-05, az LMS-Z-07 és az LMS-Z-08; a GATE-CP sort csak a „complete, pass” teljesíti. **Az LMS-Z-sorok** (MAN:105–112): LMS-Z-01 (H5P-C; unlock „M7 megerősítve”, Q-REL-2; a SLIDE 5–6 tanuló-lokális, D-2), LMS-Z-02 (unlock LMS-Z-01; a SLIDE 5–7 tanuló-lokális, D-3), LMS-Z-03 (unlock LMS-Z-02; a Megjegyzés-cella üres), LMS-Z-06 (TEXT-C, unlock LMS-Z-03; három „Required” kérdés: a 4. és a 6. dia mezője + a biztonsági lépés; a beküldés után a tanuló továbbhaladhat; „a lecke opcionális mezői nem ide tartoznak”; a megőrzési sor DPO-döntés, BS-D6, addig valódi madrihnak nem nyitható meg), LMS-Z-07 (GATE-CP; „Teljesítve” = a kijelölt mentor az LMS-Z-06 legutóbb beküldött válaszait, kiemelten a biztonsági lépést, tartalmilag elfogadta, a mezőnkénti elemekkel; el nem fogadásnál „Még nem teljesítve” + visszajelzés, javítás, újrabeküldés; a Z és az online félév feltétele, a következő tanulási tartalom nyitásáé nem; a Memuna vétójoga megmarad; határidő-cella: „—”), LMS-Z-04 (ASSIGN-S; „Z.A után, a §7 szerinti dátummal”; SUBMITTED = `completionsubmit`, CONFIRMED = LMS-Z-08; 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel; a videó csak opcionális, az alapértelmezés az írásos reflexió, HUM-PRIV-02), LMS-Z-08 (GATE-CP; „Teljesítve” = az LMS-Z-04 legutóbb leadott reflexiójának előírt mezőiben tényleges, minimálisan értelmezhető tartalom; „completion, nem vizsga”; automatikus szemantikai ellenőrzés nincs, BS-D4), LMS-Z-05 (FEEDBACK-N; „Z.A után”; completion „kitöltve”; HUM-PRIV-03). **BSPEC-07 / D-h** (MAN:19, :313; HUM:558, :560): a SUBMITTED és a CONFIRMED két külön állapot, nem vonható össze. **A GATE-CP skála** (MAN:25): egyedi skála pontosan két elemmel, ebben a sorrendben: 1. „Még nem teljesítve”, 2. „Teljesítve”; Grade to pass = 2; a checkpoint completion-állapotát a stáb kézzel nem írja felül; az egyedi skála kézi létrehozás, „a címkéket a Z.4 adja” (MAN:191); egy címkepár mindenhol (HUM:464, :490). „Üres sablon”: completion csak tényleges, minimálisan értelmezhető tartalommal (HUM:457; PT:261; MAN:173). **Q-REL-2** (HUM:510) és **BS-D3** (HUM:517; BS-D2: HUM:516): a Z az M7 megerősített kapueredményével nyílik, „Még nem teljesítve” esetén is (MAN:162, :247); a végleges program- és kurzusteljesítés a sikeres M7-javításig blokkolt; a javítási úton lévő madrih Peula v2-határideje az M7 javító határideje, a Z-határidejét a képző egyénileg ütemezi (MAN:247); a kipróbálási kötelezettségvállalás a v2 leadása mellé kerül (MAN:103, LMS-M7-06); kitalált kvucánál a vállalás a terepgyakorlat első alkalmára szól (HUM:489). A javító beadás puha kapunál és a Z-nél automatikus (HUM:482); a javító beadás idejét a MAN:249 csak a puha kapukra (M2, M4) rendezi („a képző jelöli ki”); a Z completion határideje `SCHEDULE_TO_RESYNC` 18:00 (MAN:229, :295); tanulói nézetben placeholder nem jelenhet meg (HUM:549); a pénteki ritmusra épülő feltevések a pilotra nem érvényesek automatikusan (HUM:569). **A Z.3 mentori elfogadása:** BS-D8 (HUM:521: a beküldés és a tartalmi elfogadás külön; a mentori átnézés nem blokkolja a downstream tanulási tartalmat; automatikus szemantikai validációt nem találunk ki; a Memuna gyermekvédelmi vétójoga megmarad), BS-D4 (HUM:518), **BS-D6** (HUM:520: az LMS-Z-06 megőrzése nyitott DPO-döntés, a repó nem találgatja; ADV:90; a `DPO_RETENTION_TO_CONFIRM` placeholder nyitott, ADV:237; RR:25, G2). **D-2 / D-3** (HUM:523, :524): a Z.1 SLIDE 5 és a Z.2 SLIDE 5–7 szöveges lépése kötelező, de tanuló-lokális (nem tárolt, nincs TEXT-C sor, nem completion-feltétel); a BSPEC-02 leltár tanuló-lokális listája a Z-ből csak a Z.1 SLIDE 5–6-ot és a Z.2 SLIDE 5–7-et tartalmazza (MAN:308); visszaolvasás: RT-P0-24. **D-d / D-i** (HUM:556, :561; MAN:16): a pontozatlan választó nem önálló completion-elem — név szerint az M7.4 SLIDE 4, az M0.3 SLIDE 7 és az M2.2 értékválasztása; a Z.1–Z.3-ra kiterjesztése új alkalmazási eset (ledger: M0:ERT-3, X-6); a **D-j** (HUM:562) az M2.3 pillér-ágára szól; **BSPEC-06** (MAN:16): H5P-C completion kizárólag „Receive a grade”, „Hide summary slide” = No — a CP-completion jelentése az M0:IMPL-3 nyitott döntése (X-6). **HUM-PRIV-01:** legszűkebb hozzáférés; az ASSIGN-S értékelői nézetét a Moodle-alapbeállításban a nem szerkesztő tanár, a szerkesztő tanár és a menedzser látja, a csoportszűkítés nincs rögzítve (ADV:117, BIZT-5), a szélesebb kör elfogadhatósága DPO-kérdés (ADV:109, BIZT-2); a kanonikus „Ki látja?” mondat: ADV:245; a Z.4 beadandó megőrzési sora: szabad szöveges reflexió, képzés vége + 90 nap (HUM:485). **HUM-PRIV-02** (HUM:139–155): alapértelmezés: nincs fotó, videó vagy hangfelvétel; tanulói videó opcionális (HUM:151); jogalap: külön, önkéntes hozzájárulás, a cél teljesüléséig, legfeljebb 90 nap (HUM:153); a központi felvételi szabályra minden médiaaktivitás hivatkozik, név szerint a Z.A és a Z.4 videós útja is (HUM:149); kiskorúnál a résztvevő és a gondviselő együtt adja (HUM:484; ADV:171: a gondviselői folyamat is a HUM-PRIV-02-höz tartozik); a fotószabály (nevek és azonosítók eltávolítása, a háttérben ne legyen gyerek, törlés a saját eszközről) a HUM:151 / ADV:163 szövege szerint fotóra szól; a release-evidence tétel nyitott (ADV:214). **HUM-PRIV-03** (HUM:157–174): a Z.4 Feedback kötelező, de nem nevezhető anonimnak; a tanulói szöveg szó szerint: „A válaszok név nélkül jelennek meg a feldolgozásban.”; a felhasználó azonosítója az adatbázisban marad (HUM:172; MAN:22); vétó/QA: a DPO és a programvezető, a nyers válaszok 90 napig (HUM:174); a Feedback mentori hozzáférése DPO-kérdés (ADV:119, BIZT-6). **Gyermekvédelem (HUM-SAFE-01…05):** a madrih maga is lehet kiskorú — a 15–17 éves madrih vezethet peulát, de soha nem ő az egyetlen felelős felnőtt; minden éles terepi alkalmon jelen van (vagy a helyszínen azonnal elérhető) egy jóváhagyott, felkészített, 18 év feletti felnőtt, a gyermekvédelmi felelősség az övé; érzékeny gyakorlatból bárki indoklás nélkül passzolhat; felkavart kiskorút nem küldünk ki egyedül (HUM:72); az egységes „ha téged is érint” blokk szövege a GK §4.3-ban él, új blokk máshol nem kerül be (HUM:73; GK:100); a madrih nem kap hatósági vagy jogi döntési szerepet (`.claude/rules/safety-and-human-gates.md` „Emberi kapu jelei”); a kanonikus tanulói mondat valós gyermekvédelmi helyzetre: „…azt ne egy tanulási feladatban tedd: azonnal vond be a kijelölt Memunát” (ADV:241). **HUM-OPS-01** (HUM:199–231): a Z sorrendje Z.1–Z.3 → Z.A → Z.4 (HUM:214); a Z online része 40–65 perc (HUM:223); „a Z.A 75 perces változat” (HUM:224); időkeretek: bottom-up sávok, vétó/QA: programvezető (HUM:465); a hub szerint a Z.A „péntek 2. sáv”, 45–75’ (HUB:32); a PT:13 a 2×45’ peulát az M1–M7 modulokra írja; a 45’-es Z.A-változat blokkhatárát a HUM-OPS-01 szó szerint nem rögzíti. **A 2026-10-02-i döntések Z-sorai:** DÖNT 12. pont (`01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md`:67): „Ne hívd 60 percesnek. … legyen 75 perces változat … A „3–3–3 perc/fő” helyett legyen egyszerűen 3 perc/fő.” — a HUM:224 a 75 perces változatot átvezette, a „3 perc/fő” a HUM-fájlban szó szerint nem szerepel (0 találat); a HUM-OPS-01 bizonyítéka ez a jegyzőkönyv (HUM:205); HUM-PRIV-03 (DÖNT:34). **VO D-19** (PRODUCTION-DECISIONS:507): csak hangot tartalmazó narrációnál a dián vagy a médiaelem mellett látható leirat a szöveges ekvivalens; a H5P Audio elemtől feliratsáv nem várható. **Nyitott kapuk (ledger, „Külső kapuk”; itt nem dőlnek el):** X-4 (DPO: adatkör, megőrzés, hozzáférés — köztük a „csak a mentorod látja” mögötti BIZT-2/BIZT-5, M1:BIZT-G2-4, M2:BIZT-G2-3), X-5 (Memuna: gyermekvédelmi szabály-alkalmazás — köztük a második felnőtt a peulákon, M2:BIZT-G3-2, M0:BIZT-9), X-6 (completion- és értékelési jelentés: M0:IMPL-3, M0:ERT-3, M2:IMPL-G2-1), X-7 (a Memuna írásos „átnéztem” bejegyzése, G1), X-8 (célkörnyezeti Moodle-visszaolvasás, G3b), X-10 (programszerkezet és időkeret — köztük a lépésidők a rögzített blokkokon belül, M2:PED-G3-1), X-11 (LMS-konfiguráció — köztük az „Accepted file types”, M1:IMPL-G2-10), X-12 (a DPO írásos jóváhagyása, G2); a BS-D6 (az LMS-Z-06 megőrzése) a ledger X-kapui között nem szerepel, a HUM:520 és az RR:25 nyitottként tartja. Az M0:NYELV-G2-18 Z.A-helyei (induló-szavak: Z.A:55, :423, :440, :458) a ledgerben az M0-tétel részei (IN_PROGRESS: „a Z.A négy helye a Z-javítással egy menetben”); a NYELV-G1-7 ezeket kizárja.

**Klaszterek (egy tényállás, több finding — ugyanabban a hívásban; mindegyik ID kap verdiktet, jelöld a megtartandót):**

| Klaszter | Findingok | Tárgy | Hívás |
|---|---|---|---|
| K1 | ERT-G1-1, ERT-G1-2, IMPL-G1-1 | a Z.4 záró reflexió megerősítése (LMS-Z-04 → LMS-Z-08) a Z.4 §4-ben és a hub §5–§6-ban. (a) Állapotmodell és skálasorrend: a Z mappában az LMS-Z-08 0 találat (visszaolvasva); a HUB:199 3. pontja csak „leadott” reflexiót kér ↔ MAN:163 (LMS-Z-04 leadva + LMS-Z-08 = „Teljesítve”); a Z.4:343 két kódolási alternatívája („értékeléshez kötött completion vagy kézi megerősítés”) ↔ BSPEC-07 / D-h (MAN:19, :110–111; HUM:560) és a GATE-CP kézi felülírási tilalma (MAN:25); a Z.4:341 skálasorrendje („Teljesítve / Még nem teljesítve”) ↔ MAN:25, a címkéket a Z.4 adja (MAN:191). ERT-G1-2 = IMPL-G1-1 duplikátum-gyanú (mindkettő objektív, a MAN szó szerinti átvezetése). Csak az IMPL-G1-1-ben: (d) a Z.4:338 zárójeles hivatkozása a MAN:19 puha kapus mondatára, és hogy az „Automatically until pass” újranyitáshoz az LMS-Z-04-et is értékelni kell (a mentor kétszer ír be) — ha ez új munkafolyamat: EMBERI DÖNTÉS (build-spec gazda); az ERT-G1-2 az Assignment saját skálájának (Z.4:340) megtartását a javításon kívüli implementációs kérdésnek tartja: itt a két javaslat eltér. (b) A „Teljesítve” mércéje (ERT-G1-1, EMBERI DÖNTÉS: értékelési felelős; vétó/QA: programvezető): a HUB:185–189 és a Z.4:345 címe a hármas minimumot teszi feltétellé ↔ MAN:111 és Z.4:343 „tényleges, minimálisan értelmezhető tartalom” (HUM:457) ↔ Z.4:347 „érdemes szem előtt tartani”, :353 „nagyon hiányos / alibi”; az ERT-G1-1 szerint a MAN:173 a Z rubrikaküszöbét nem mondja ki formatívnak, a kérdés a kánonból nem dönthető el. Függés: az IMPL-G1-1 (a) „a tartalmi minimummal” fordulata és az ERT-G1-2 javítása nem előlegezheti meg az ERT-G1-1 döntését (mindkét nyers kimenet így korlátoz). Korlát: a címkepár, az 1+1 beadás, a puha kapu és a BSPEC-07 nem változik | V1 |
| K2 | PED-G1-1, ERT-G1-7 | a javítási úton lévő madrih és a Z; a HUB:33 egy mondata, két hiba. (a) PED-G1-1 (objektív, P1): a HUB:33 „Mivel a Z az M7 megerősített teljesítése után nyílik” ↔ MAN:247 („Még nem teljesítve” esetén is), MAN:162, Q-REL-2 (HUM:510), BS-D3 (HUM:517); a Z.3 4. és 6. diája (Z.3:213, :215, :227, :237, :275, :283) leadott Peula v2-t és mellé leadott kipróbálási szándékot feltételez (vö. MAN:103), ami az M7-kvíz javítási útján lévőnek a Z hetében még nincs (MAN:247); javaslat: a HUB:33 a MAN:247 szerint + feltételes mondat a Z.3:215 után (a v1-re és az M7.B:563 kipróbálási szándékára építve — az M7-riport nem validált). (b) ERT-G1-7 (EMBERI DÖNTÉS, programvezető, HUM-OPS-01): a Z saját javító útjának nincs időpontja — a Z.4 javító beadása automatikusan nyílik (Z.4:338; HUM:482), a megerősítés a határidő utáni napon van (Z.4:339); a MAN:249 a javító beadás idejét csak a puha M2/M4-re rendezi; az LMS-Z-07 határideje „—”, az újrabeküldésnek nincs határideje; a HUB:33 csak az M6 és az M7 javítását várja be. Az ERT-G1-7 a HUB:33 nyitási mondatát szándékosan nem ismétli (a PED-G1-1-re hagyja). A verifier nézze meg, a MAN:247 „a javítási úton lévő madrih Z-határidejét … a képző egyénileg ütemezi” mondata mennyit fed le a (b)-ből (az M7 javítási útjára szól). Korlát: dátumot nem találunk ki (`SCHEDULE_TO_RESYNC`, HUM:549); az LMS-Z-06/07 kötelező státusza, a MAN:109 kritériumai, a BS-D8 lánc és a Z.3:211 gyermekvédelmi bekezdése nem változik | V1 |
| K3 | PED-G1-2, IMPL-G1-2, IMPL-G1-3 | a Z.3 szöveges lépései: hová és mikor ír a tanuló. (a) A három kötelező válasz helye az LMS-Z-06 (TEXT-C), amely csak a Z.3 CP-completionje, vagyis az összefoglaló dia után nyílik (MAN:108, :16); a 7. dia önellenőrzése (:318, :327, :348 „Nyugodtan lépj vissza 1–2 diát…”) így a beírás előtt fut; a tanulói szöveg sehol nem mondja meg, hová és mikor írja a választ; a biztonsági lépés „a 4. és a 6. dián írtakat” említi (:302); a Z.4:207 a SLIDE 4 mondatát „magadnak elmentett”-nek mondja. PED-G1-2 = IMPL-G1-2 duplikátum-gyanú (mindkettő objektív; a PED-G1-2 a jegyzetre, az IMPL-G1-2 a manifest nevére — „Z.3 – Szöveges válaszok” — utalna). Csak az IMPL-G1-2-ben: (c) a „Mezőben megjelenő mintaszöveg” (Z.3:236) Feedback „Longer text answer”-ben nem valósítható meg (placeholder-mező nincs, `textarea_form.php`), ezért szó szerint a kérdéscímkébe vagy egy előtte álló Label-elembe és a MAN:108 Megjegyzésébe kerülne (M2:IMPL-G2-7 minta — lásd Rokon); ha az önellenőrzés a beírás után legyen (az LMS-Z-06 a CP-vel párhuzamosan nyílik): a MAN:108 unlock-cellája, EMBERI DÖNTÉS (build-spec gazda). (b) A SLIDE 5 „A következő hónapban…” beágyazott rövid szöveges kérdése (Z.3:11, :241–263) és a SLIDE 7 opcionális mini szöveges válasza (:350): a Z.3:57 szerint CP-dián szabad szöveges mező nem feltételezhető; nem tartozik az LMS-Z-06 három kérdése közé (MAN:108), nincs a BSPEC-02 leltárban (MAN:308), mégis a 7. dia és a Z.4:207 erre épít. IMPL-G1-3 EMBERI DÖNTÉS (projektgazda mint build-spec gazda; tárolt útnál a DPO is): kötelező vagy opcionális tanuló-lokális (a D-2/D-3 mintája), vagy negyedik LMS-Z-06 kérdés (akkor BS-D6); a PED-G1-2 3. pontja ugyanezt a tényállást írja le, de a javításából kiveszi (az M3:IMPL-G2-6 szerinti külön döntés). Közös korlát: a három kötelező kérdés, a Required-státusz, a beküldés → mentori elfogadás lánc (LMS-Z-07, BS-D8) és az LMS-Z-06 nyitási feltétele döntés nélkül nem változik | V1 |
| K4 | BIZT-G1-4, IMPL-G1-4 | a Z.4 „A beadásodat csak a kijelölt mentorod vagy értékelőd látja” ígérete (Z.4:98, :329; fejlesztői feltétel :307) ↔ ADV:117 (ASSIGN-S értékelői nézet: nem szerkesztő tanár, szerkesztő tanár, menedzser; csoportszűkítés nincs rögzítve, BIZT-5), ADV:109 (BIZT-2), ADV:245 („Ki látja?”); az RA 15 (RT-P0-15) még nem futott. Duplikátum-gyanú: BIZT-G1-4 = IMPL-G1-4; mindkettő EMBERI DÖNTÉS (DPO, az LMS-gazdával), meglévő kapu: M1:BIZT-G2-4 / M2:BIZT-G2-3 (X-4), új döntés nem nyílik; a BIZT-G1-4 Z-többlete: a videó (arc, hang) ugyanebbe a körbe esik. Korlát: a tanulói mondat a HUM-PRIV-01 policy-mondata, a döntésig nem írható át; a Z.4:201 titoktartási kivétele marad | V2 |
| K5 | BIZT-G1-5, IMPL-G1-8, IMPL-G1-9 | a Z.4 opcionális videós útja (Z.4:117, :278, :307, :310, :336 „File submissions: ON, max 1 file, max size 100–200 MB”; HUB:184). Egy tényállás, három besorolás: (a) BIZT-G1-5 EMBERI DÖNTÉS (DPO/jogi felelős, HUM-PRIV-02): hol és hogyan rögzül kiskorúnál a résztvevő és a gondviselő együttes hozzájárulása (HUM:484; ADV:171: a gondviselői folyamat a HUM-PRIV-02-höz tartozik), ki ellenőrzi a feltöltés előtt, a feltöltés csak rögzített hozzájárulás után nyíljon-e; vonatkozik-e a videóra az ADV §6 fotószabálya (más ne szerepeljen, törlés a saját eszközről; ADV:163 / HUM:151 fotóra szól). (b) IMPL-G1-8 bizonyíték-kapu (G2, tracker #2): a megvalósítási döntést a projektgazda jóváhagyta (HUM-PRIV-02), a DPO formális bizonyítéka és a folyamat lezárása függő (ADV:214 kipipálatlan); a videó legfeljebb 90 napos sora (HUM:153) külön áll a szöveges beadás „képzés vége + 90 nap” sorától (HUM:485); az RR:83 mintája szerint addig valódi madrihnak nem nyitható. Típus-ütközés: ugyanarra a hiányra a BIZT emberi döntést, az IMPL bizonyíték-kaput mond. (c) IMPL-G1-9 objektív: az „Accepted file types” nincs megadva (üresen minden típus), a méret tartomány, nem érték, a kurzus- és site-limit nincs a G3a-paraméterek között; javaslat: a Moodle „video” csoportja + egyetlen „Maximum submission size” az LMS-gazdától (lásd Rokon: M1:IMPL-G2-10, X-11). Korlát: az írásos alapút, a hozzájárulási mondatok és a 2–3 perc maradnak; hozzájárulási vagy tárolási folyamatot nem írunk be | V2 |
| K6 | BIZT-G1-7, IMPL-G1-11, ERT-G1-4 | a kötelező LMS-Z-05 Moodle Feedback rögzítetlen beállításai (Z.4:372–403; MAN:22 FEEDBACK-N, :112; RA 16 / RT-P0-16). (a) „Show analysis page” (Z.4:398): a Z.4 az értéket a HUM-PRIV-03 gazdájára bízza; „Yes” esetén a tanulók az elemzőoldalon a többiek szabad szöveges válaszát szó szerint látják (a 2. kérdés kísérő mezője, az 5–7. kérdés); a kódbeli alapérték „No” (`selectyesno`, `setDefault` nélkül). Erre a beállításra BIZT-G1-7 = IMPL-G1-11 duplikátum-gyanú; csak az IMPL-G1-11-ben: az „Enable notification of submissions” is, a TEXT-C profil ugyanezt a két beállítást rögzíti (MAN:24), és egy döntéstől független objektív lépés (a tétel nyitottként a G2 nyitott DPO-tételei közé, RR:25, és a MAN:22 / :112 megjegyzésébe; a döntés után az érték a FEEDBACK-N profilba és az RA 16 visszaolvasási listájába). A gazda eltér: BIZT-G1-7: DPO + programvezető; IMPL-G1-11: a projektgazda mint build-spec gazda, vétó/QA: DPO + programvezető (a HUM-PRIV-03-ban ők utólagos ellenőrzők, HUM:174). (b) ERT-G1-4 (EMBERI DÖNTÉS, értékelési felelős; vétó/QA: DPO + programvezető): egyik kérdés sem „Required”, a completion „mark as complete when submitted” (Z.4:403), így az üres beküldés is teljesít; a MAN:24 a „Required”-kikötést csak a TEXT-C-nél mondja ki; ha az üres beküldés is elég, a HUB:62 (a hub 5. kompetenciája: „kitölti a visszajelző űrlapot”) és a HUB:200 pontosítandó. Korlát mindháromnál: a „Record user names” = „Anonymous”, a kötelező kitöltés, az egyszeri beküldés, a 90 napos megőrzés és a tanulói mondat („A válaszok név nélkül jelennek meg a feldolgozásban.”) nem változik; értéket a repó nem választ | V2 |
| K7 | BIZT-G1-8, ERT-G1-6, IMPL-G1-7 | a Z.1–Z.3 helyes válasz nélküli, reflektív választóinak completion-szerepe. Helyek: Z.1:13 (SLIDE 1 és 3), Z.2:13 (SLIDE 1, 3, 4 — a Z.2 completionje kizárólag ilyenekből áll), Z.3 (nincs „Completion (lecke)” sor, :5–23; választók: SLIDE 1, 3, 7), Z.1:57, Z.2:63, Z.3:59; az LMS-Z-03 Megjegyzése üres (MAN:107) ↔ D-d (HUM:556), D-i (HUM:561: csak az M0.3 SLIDE 7 és az M2.2), MAN:16 (BSPEC-06: „Receive a grade”, „Hide summary slide” = No); az ERT-G1-6 szerint a BSPEC-06 hatóköri besorolása a Z-01…03-at „pontozott interakciókkal” sorolja be (forrás: `2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`:54–56). Mindhárom EMBERI DÖNTÉS, meglévő kapu (X-6: M0:IMPL-3, M0:ERT-3, M2:IMPL-G2-1); a Z.1–Z.3-ra kiterjesztés a lezárt döntés új alkalmazási esete; az ERT-G1-6 és az IMPL-G1-7 a döntés utánra objektív lépést nevez (a Z.3 completion-sort kap, az LMS-Z-03 Megjegyzése kitöltődik). Csak az IMPL-G1-7-ben: a `cp.js` szerint összefoglaló dia csak feladatelem esetén keletkezik — ha az RA 14 nem feladat típusú megoldást választ, nincs grade, az LMS-Z-02/-03 sosem teljesül (a Z és az online félév blokkolt). Csak a BIZT-G1-8-ban: a DPO-kérdés a D-j mintájára — elfogadható-e az érzelmi önbevallás („kudarc”, Z.2:236–240; „félek bármit ígérni”, Z.3:121–127) fiókhoz kötött tárolása és tanári láthatósága (ADV:150; X-4). A dia-listák eltérnek (BIZT-G1-8: Z.3 SLIDE 1 és 7; ERT-G1-6, IMPL-G1-7: Z.3 SLIDE 1, 3, 7). Korlát: a választók, az opciók, a visszajelzések, a D-2/D-3, a Z.1 SLIDE 4 szerepe, a „Hide summary slide” és az RA 14 szerinti típusválasztás döntés nélkül nem változik; completion-sor most nem írható be | V1 |
| K8 | ERT-G1-5, IMPL-G1-5 | a Z.1 SLIDE 4 (a lecke egyetlen pontozott eleme): Single Choice Setként előírva (Z.1:13, :335), miközben kérdésenkénti rossz-válasz-visszajelzést ír (:374–381), és a lecke maga elismeri, hogy az SCS-nek nincs ilyen mezője (:382); az RA 14 csak tesztel, típust nem választ (RA:81). Duplikátum-gyanú, mindkettő objektív. Javaslat-eltérés: ERT-G1-5: Multiple Choice egyválaszos módban, kérdésenként, „Randomize answers” bekapcsolva; tartalékként, ha az SCS marad, az M4.3:398 fejlesztői megjegyzése szó szerint a :382 helyére ↔ IMPL-G1-5: csak a típusnév változik (h5p-multi-choice `chosenFeedback`), a :382 szűkíthető; ha az SCS marad: „Auto continue” = ki (A11Y:83; WCAG 2.2 SC 2.2.1), és a kérdésenkénti szöveg nem ígérhető. A precedens vegyes (Rokon: M2:ERT-G2-3, M3:IMPL-G2-9 ↔ M4:IMPL-G1-3, M5:IMPL-G2-3). Korlát: a kérdések, az opciók, a ✅-ok, a visszajelzés-szövegek és a SLIDE 4 completion-szerepe nem változik | V3 |
| K9 | IMPL-G1-10, NYELV-G1-4 | activity-nevek ↔ manifest „Név”: a Z.4 Assignment „Záró reflexiós ív” (Z.4:27, :73, :77) és „„Záró reflexió + képzési visszajelzés” Assignment” (Z.A:24) ↔ „Záró reflexió + következő lépés” (Z.4:293, :302; HUB:105, :183; MAN:110); a Feedback „Képzés-értékelés” (HUB:190) ↔ „Képzési visszajelzés – név nélkül” (Z.4:365; MAN:112). Azonos irány (a manifest neve áll; a „záró reflexiós ív” köznévként, idézőjel nélkül a sablonra maradhat), mindkettő objektív; az IMPL-G1-10 (a) csak az Assignmentet, a NYELV-G1-4 a Feedbacket és a Z.A:24-et is. Az IMPL-G1-10 további, független alpontjai: (b) a HUB:195 „érdemes … restrict access” ↔ a MAN:110/:112 kötelező unlockja (átfedés: K10); (c) a Z.1:59 tájékoztató-feltétele a D-2 óta nem létező mezőkre vonatkozik (minta: Z.2:65); (d) a HUB:171 a PT:307-et nem szó szerint idézi. Korlát: a lecke címe, a fájlnevek, a linkek, a `SCHEDULE_TO_RESYNC` dátumok és a „reflektív, NEM értékelő” mondat nem változik | V3 |
| K10 | PED-G1-3, ERT-G1-3 | a Z.A ↔ Z.4 kapcsolat és a Z.A szerepe a Z teljesítésében. PED-G1-3 (objektív): a HUB:36 és a Z.A:24 azzal indokolja a Z.4 Z.A utáni nyitását, hogy a Z.4 „a peulán megfogalmazott gondolatokból dolgozik” ↔ a Z.4:158 felidéző utasítása csak a Z.1–Z.2-re mutat, a Z.A-ban nincs a képzőnek kiírt átvezető mondat (csak a :531–534 ellenőrző kérdés), a Z.4:283 („a Z.A záró peulán volt”) a hiányzóra hamis; javaslat: a Z.4:158 rámutat a Z.A meglévő elemeire, a Z.A 4.4.2/3. lépése kap egy képzői mondatot. ERT-G1-3 (EMBERI DÖNTÉS, programvezető + értékelési felelős): a HUB:193–198 a Z.A-részvételt a „Minimális teljesítés” 2. pontjaként sorolja ↔ PT:211–213, MAN:163, :165 (a Z.A nem completion-elem; jelenléti checkpoint nincs, az LMS-Z-04 dátummal nyílik, MAN:110); a hiányzóknak nincs pótlási útja. Kölcsönös hivatkozás: az ERT-G1-3 a hiányzók Z.4-es felidéző útját a PED-G1-3-ra hagyja, a PED-G1-3 a hiányzók alternatív útját külön döntésre. Korlát: a Z.4 és a Feedback Z.A utáni, dátumos nyitása (MAN:110, :112) és a HUM-OPS-01 sorrendje (HUM:214) nem változik; új feladat vagy írásos lépés a peulán nem kerül be | V1 |
| K11 | ERT-G1-8, NYELV-G1-18 | a Z.2:18 mikrocél-mondata. ERT-G1-8 (objektív): a „volt-e olyan modul, amit nehéznek éltél meg és mit mond ez rólad” önfeltárást tesz céllá ↔ Z.2:307 („A teljesítéshez nem kell érzékeny önfeltárás”), HUB:83, a SLIDE 4 harmadik opciója (:240); javaslat: a :307 alternatívája szó szerint a :18-ba. NYELV-G1-18 (objektív): ugyanitt hiányzik a vessző az „és” előtt (a „mit mond ez rólad” nyelvtanilag az „amit” mellékmondathoz kapcsolódik); további helyei: Z.A:105, HUB:124. Egy mondat, két javítás: az ERT-G1-8 mintamondata a vesszőt nem tartalmazza, egy szerkesztésben kell összefésülni. Korlát: a SLIDE 6 szövege, a HUB:83 és a mikrocél másik két eleme nem változik; a NYELV-G1-18-ban egyetlen szó sem változik | V3 |
| K12 | PED-G1-10, NYELV-G1-15 | Z.3:147 „Ha túl kicsit, túl általánosat:” ↔ a példa (:148 „Jobb madrih leszek.” — homályos, nem kicsi) és a lecke üzenete (:117 „kicsi, konkrét lépések”; :142, :153). Típus-ütközés: PED-G1-10 objektív (a „túl kicsit,” törlése) ↔ NYELV-G1-15 EMBERI DÖNTÉS (modulgazda vagy projektgazda: szándékos második hibatípus-e; bizalom: alacsony). Korlát: a :148 példamondata és a :150–153 kritériumlista (benne a „kicsit kihívó is”) nem változik | V3 |
| K13 | PED-G1-6, PED-G1-7, NYELV-G1-12, NYELV-G1-17 | a Z.A időkeretei és két változata (75’ / 45’) a DÖNT 12. pont (DÖNT:67) és a HUM:224 („a Z.A 75 perces változat”) alapján. PED-G1-6 (objektív): a felolvasandó utasítás „fejenként kb. 3–4 perc” (Z.A:212) ↔ a képzői sor „kb. 3 perc/fő” (:213) és a DÖNT 12. pont „3 perc/fő” (a HUM-fájlba szó szerint nincs átvezetve, lásd Szabályok). PED-G1-7 (EMBERI DÖNTÉS, programvezető; HUM-OPS-01): a Z.A:81 a 75’-es változatra 75–85’, a 45’-esre 45–50’ tervezést ír ↔ HUM:224 és a DÖNT 12. pont („Ne hívd 60 percesnek…”); a 45’-es változat a „péntek 2. sáv” blokkhatárát lépi túl (HUB:32); a névhúzásos kör (Z.A:403) „kb. 6 perc” 8–20 főnél alultervezett; a lépésidők átosztása az M2:PED-G3-1 mintájára (X-10); „a `/course-fix` ne nyúljon percekhez”. NYELV-G1-12 (objektív): Z.A:403 „45’-ben kihagyható” ↔ a percbontás (:77 „kimarad”; :72, :344) → „45’-ben kimarad”. NYELV-G1-17 (objektív): Z.A:343 „75’ verzió” → „75’-es verzió”. Közös tényállás: a 75’/45’ blokkszerkezet (Z.A:72–84, :343–344, :403); ha a PED-G1-7 döntése a 45’-es változatot vagy a percbontást átírja, a NYELV-G1-12 tárgytalan lehet. Feszültség: a PED-G1-6 egy percértéket ír át (lezárt döntés átvezetéseként) ↔ a PED-G1-7 tilalma; a Z.A:81 „75–85’” fordulatát az Anna-mátrix E-Z-036 a DÖNT 12. pont és a HUM:224 szerinti percszám-változásként rögzíti (audit trail, nem kánon; lásd Rokon). Korlát: a 75’-es 6 perc, a HUM-OPS-01 blokkhatárai és a vágási sorrend (Z.A:82–84) döntés nélkül nem változik | V3 |
| K14 | BIZT-G1-6, NYELV-G1-14 | a Z.A biztonsági kerete egy képzővel (2.2 Tér, 2.3, 4.2). BIZT-G1-6 (EMBERI DÖNTÉS, Memuna + programvezető): a keret második felelős felnőttet feltételez — felkavart résztvevő mellett „ott is egy felnőtt van vele” (Z.A:45), 1:1 „egy másik felelős tudtával” (:53), feltárás (:54), facilitátori tipp (:226), „Ha van ken-vezető / felelős jelen” (:412), ellenőrző lista (:522) —, miközben a peula 8–20 főre egy képzőt ír elő; HUM-SAFE-02/-03 (HUM:72; GK §4:64, §4.2); meglévő kapu: M2:BIZT-G3-2 (X-5), új döntést nem nyit. NYELV-G1-14 (EMBERI DÖNTÉS, modulgazda + Memuna): ugyanebben az eljárásban (:53) az „Utána” nem mutat egyértelmű előzményre — a képző előbb a résztvevőhöz lép oda, vagy előbb a mentort / a Memunát vonja be; a :226 csak a „peula után” odalépést írja le. Egy eljárás, egy döntési kör (Memuna): ha a BIZT-G1-6 döntése az egy képzős utat írja le, az „Utána” sorrendje is abból következhet. Korlát: a 2.2, a 2.3 és a 4.2 biztonsági mondatai, a safer-working kikötések és az ötlépéses jelzési út szó szerint maradnak, nem gyengíthetők; egyik lencse sem javasol szöveget | V2 |

**Átfedő helyek (nem klaszter: ugyanaz a mondat vagy elem, más hiba; a verifier jelezze, ha két javaslat ütközik):** Z.4:340–353 és HUB:185–199 — K1-en belül a sorrend számít: az ERT-G1-2 / IMPL-G1-1 objektív átvezetése (két állapot, skálasorrend) nem dönthet az ERT-G1-1 mércéjéről (V1) ↔ NYELV-G1-3 (a Z.4 3. vezető kérdése :62, :140, :212, :322, a :234 ellenőrző lista és a :35 mikrocél a HUB:110 szerint; korlátja a HUB:189 / Z.4:351 minimum, amelynek „Teljesítve”-feltétel jellege az ERT-G1-1 kérdése, V4); HUB §5 „Minimális teljesítés” (HUB:193–200) — a 2. pont K10 (ERT-G1-3), a 3. pont K1 (ERT-G1-2, IMPL-G1-1), a :195 bevezető K10 (PED-G1-3, ERT-G1-3) (V1) ↔ a 4. pont és a HUB:62 K6 (ERT-G1-4, V2) ↔ a :195 „érdemes” K9 (IMPL-G1-10 (b), V3): egy lista, egy szerkesztés; Z.4:338–339 — K1 (IMPL-G1-1 (d): a zárójeles hivatkozás a MAN:19-re) ↔ K2 (ERT-G1-7: a javító beadás és a megerősítés időpontja) (V1); HUB:33 — K2-n belül egy mondat: a PED-G1-1 nyitási része és az ERT-G1-7 „csak az M6 és az M7 javítását várja be” része egy szerkesztésben (V1); Z.3 4. dia (:207–237) — K2 (PED-G1-1: feltételes mondat a :215 után; korlátja: „a :237 mintaszöveg … nem változik”) ↔ K3 (IMPL-G1-2 (a) útbaigazítás, (c) a mintaszöveg szó szerint az LMS-Z-06 kérdéscímkéjébe) (V1) ↔ NYELV-G1-2 (a :237 és a :227 mintaszöveg átírása; korlátja: a „A következő 3 Zmán Kvucámon…” nyitás betűre marad, mert a Z.3:219, :318 és a Z.4:207 erre hivatkozik, V4) ↔ PED-G1-8 (a :207–211 áttekintő külön Input-diára, V3) ↔ NYELV-G1-16 (:207 „adatminimalizált”, V4): a PED-G1-1 korlátja és a NYELV-G1-2 javaslata ütközik; ha a mintaszöveg az LMS-Z-06 címkéjébe kerül, előbb a NYELV-G1-2 verdiktje kell; ha a PED-G1-8 áthelyezi a :207–211-et, a NYELV-G1-16 helye vándorol, a szövege nem; Z.3 6. dia (:275–287) — PED-G1-5 (a támogató személy köre: :279 ↔ :283, HUB:96 ↔ :287, MAN:109) ↔ K3 (IMPL-G1-2: útbaigazítás a SLIDE 6-on) ↔ K2 (PED-G1-1: :275, :283) (V1); Z.3 biztonsági lépés (:295–306) — BIZT-G1-1 (a :300 kánonon kívüli szabálya és a jelzés címzettje; új eszkalációs szöveg és gyengítés tilos, V2) ↔ K3 (IMPL-G1-2 (a)–(b): útbaigazítás, a :302 igeideje; PED-G1-2: :298, :302) ↔ PED-G1-5 ((a): a mikrocél a Z.3:295–296 szövegéből kap tagmondatot; :306) (V1) ↔ BIZT-G1-10 (a Memuna BS-D8-vétója és QA-ja, V2): a K3 útbaigazítása a :300 szabálymondatához nem nyúlhat; a PED-G1-5 tagmondata a BIZT-G1-1 (b) döntésétől (kinek jelez) függhet; Z.3 7. dia (:318–350) — K3 ↔ K7 (a SLIDE 7 választója) (V1); Z.3 fejlesztői meta (:5–23, :11, :57, :59, :61) — K7 (a hiányzó „Completion (lecke)” sor, :59) ↔ K3 (IMPL-G1-3: :11, :57) (V1) ↔ BIZT-G1-3 (:61 → a MAN:108 BS-D6-mondata szó szerint) ↔ BIZT-G1-10 (:57, BS-D8) (V2) ↔ NYELV-G1-8 (:11, :59 „Multi Choice”, V4): ha az IMPL-G1-3 döntése negyedik LMS-Z-06 kérdést hoz, az is a BIZT-G1-3 BS-D6-mondata alá esik; Z.4:207 — K3 (mindhárom, V1) ↔ a NYELV-G1-2 korlátja (V4); Z.1:13 completion-sor — K7 (SLIDE 1, 3, V1) ↔ K8 (a SLIDE 4 típusa, V3) ↔ NYELV-G1-8 („Multi Choice” → „Multiple Choice”; korlátja: a „Single Choice Set” címke marad, V4): egy sor, három változtatás; a NYELV-G1-8 korlátja a K8 típuscseréjével ütközik; Z.1:57, Z.2:63, Z.3:59 — K7 (V1) ↔ NYELV-G1-8 (Z.1:57, Z.3:59, V4); ezek a validált M2:IMPL-G2-2 és M4:IMPL-G1-3 javításának mintamondatai (Rokon): átírásuk a minták szövegét is érinti; Z.1 SLIDE 4 (:335–382) — K8 (V3) ↔ NYELV-G1-1 (a 4. kérdés szára, :368 „Zmán Kvucával” ↔ :381; korlátja: az opciók és a ✅ maradnak, V4); Z.1 SLIDE 6 narrációja — IMPL-G1-6 (:266, :531: szó szerinti leirat a VO D-19 szerint, V3) ↔ NYELV-G1-6 (:271 `@source`, csak hanggyártási úton; :195 `@asset`, V4): ha a leirat szó szerint a hangot követi, a :271 szövegjavítása újrarenderelés nélkül eltérést okoz — a verifier nézze meg, ugyanarról a narrációról van-e szó; Z.2 SLIDE 4 (:236–240) — K7 (BIZT-G1-8: a „kudarc” választó tárolása, V1) ↔ K11 (ERT-G1-8: a harmadik opció mint alternatíva, V3); Z.4:201, :357–359, :370 — BIZT-G1-2 (V2) ↔ K4 (IMPL-G1-4: a :201 titoktartási kivétele nem változik) ↔ K6 (BIZT-G1-7: az elemzőoldalon feltárás is lehet) (V2): a :370 első mondata a HUM-PRIV-03 kanonikus mondata, mindegyikben szó szerint marad; a BIZT-G1-2 döntéstől független objektív alpontja (a hibás „(ugyanaz, mint az M3.3-ban)” hivatkozás pontosítása vagy elhagyása) a szabály szövegéhez nem nyúlhat; Z.4:307, :336 — K4 (BIZT-G1-4: :307) ↔ K5 (V2); Z.4:365–403 (Feedback) — K6 (V2) ↔ NYELV-G1-8 (:383, :385: H5P-nevek helyett Moodle-nevek, V4) ↔ K9 (NYELV-G1-4: a :365 név, V3); Z.4:152–158 — K10 (PED-G1-3: a :158 kiegészítése, V1) ↔ NYELV-G1-5 (:156 „1. blokk” → „1. szakasz”) és NYELV-G1-6 (:152 fejlesztői sor) (V4); Z.4:61–62, :137, :140, :198, :233, :234, :320 — NYELV-G1-3 ↔ NYELV-G1-6 (V4, egy hívásban): ugyanazok a vezető kérdések; a :62, :137, :140, :234 Anna-mátrixbeli helyek (Rokon: E-Z-029, E-Z-030, E-Z-031); Z.A:23–24 — K9 (NYELV-G1-4: az Assignment neve, V3) ↔ K10 (PED-G1-3, V1) ↔ NYELV-G1-6 (Z.A:23, V4); Z.A:529–534 — K10 (PED-G1-3: képzői mondat az 5/6. pont tartalmából, V1) ↔ NYELV-G1-7 (:529, :530 „elismerés-kör”, „poszter-bemutató”, V4); Z.A 4.2 (:204–213) — K13 (PED-G1-6: :212, V3) ↔ NYELV-G1-10 (:206 felolvasandó szöveg, V4) ↔ BIZT-G1-9 (:204 kifüggesztés, V2); Z.A 4.4.1 névhúzás (:400–406) — K13 (PED-G1-7: a 6 perc; NYELV-G1-12: :403, V3) ↔ BIZT-G1-9 (:405 névcetlik sorsa, V2) ↔ NYELV-G1-10 (:405–406 szám/személy, V4): négy finding egy blokkban; ha a PED-G1-7 döntése a 45’-es változatot átírja, a NYELV-G1-12 tárgytalan lehet; a passz- és a cetli-szabályok tartalma nem változik; Z.A:72–84, :343–344 — K13 (NYELV-G1-17: :343; PED-G1-7: :81, V3) ↔ NYELV-G1-7 (:343, :72, :75, :77, :83, :84 „elismerés-kör”, „poszter-idő”, „szófelhő rituálé”, V4): a :343 zárójelben két javítás; Z.A:457–462 szófelhő — BIZT-G1-9 (V2) ↔ NYELV-G1-13 (:459 „1 szó” ↔ „mondat”; HUB:140; Rokon: E-Z-040) ↔ NYELV-G1-7 (:457 „Szó-írás”, :83 „szófelhő rituálé”) (V4); Z.A:32, :35, :312–316, :516–522 — PED-G1-9 (eszközlista, ellenőrző lista, a MUNK-01 notes mezője, V3) ↔ K14 (BIZT-G1-6: :522, V2) ↔ BIZT-G1-9 (:316 posztermunka, V2) ↔ NYELV-G1-7 (:313 „Poszter-keret”, :43, :520 „poszter-állomás”, V4); Z.A:55 — BIZT-G1-9 (az M0.A plakát és a képzői idézetek, V2) ↔ az M0:NYELV-G2-18 Z.A-helye (a ledgerben M0-tétel); HUB:92 — PED-G1-4 (V3) ↔ NYELV-G1-7 („esemény-specifikus”; HUB:91 „sablon mondatokkal”, V4): ha a PED-G1-4 döntése a HUB:92-t a mai Z.3-hoz igazítja, a NYELV-G1-7 e helye tárgytalan lehet; HUB:140 — BIZT-G1-9 (V2) ↔ NYELV-G1-13 (V4); HUB:184 — K5 (V2); HUB:170, :207–208 — BIZT-G1-10 (V2); HUB:171 — K9 (IMPL-G1-10 (d), V3); HUB:206 — a NYELV-G1-16 szerint stábszöveg, marad (V4); bizonyíték-kapuk — BIZT-G1-10 (Memuna G1, DPO G2, RT-P0-03/-12/-15/-16/-24 G3b) ↔ K5 (IMPL-G1-8, G2) ↔ K4 (RT-P0-15) ↔ K6 (RT-P0-16) (V2): külön kapuk, külön bizonyíték; answer key-védelem: K8 (✅-ok), NYELV-G1-1 (a ✅ M7), K12 (a :148 példa és a kritériumlista). Lencsén kívüli megerősítés (nem finding, nem klaszter): az ERT-G1 lencse kulcsellenőrzése szerint a Z.1 SLIDE 4 négy kulcsa helyes, és a Z.4 űrlap „3 ígéret” tétele egyezik a PT:221 M0.1-es ígéreteivel.

**Rokon, más modulban már rögzített tételek** (ha a verdikt ugyanaz a kérdés, a megtartandó a korábbi, és emberi döntésnél ugyanahhoz a kapuhoz tartozik; a kulcsokat a ledger Findingok táblájában ellenőriztük — ott M0–M5-sorok vannak; az M6- és az M7-riport állapota 2026-10-11-én: NYERS (M6: RAW_SAVED, M7: REVIEWING), nem VALIDÁLT, ledger-soruk nincs; a nyers Z-kimenetek M6- vagy M7-kulcsot nem idéznek, az M7-re csak helyhivatkozással utalnak: PED-G1-1 — M7.B:563, K2 — az M7 javítási útja): M4:ERT-G1-2 (MEGERŐSÍTVE, objektív, OPEN: a MAN:78 / BSPEC-07 mondata szó szerint; P1 → P2) — K1 (az ERT-G1-2 mintája); a nyers kimenet nem idézi, de azonos minta: M2:IMPL-G1-5 (MEGERŐSÍTVE, P1, OPEN: a MAN:61 / BSPEC-07 szó szerinti átvezetése) — K1; M1:IMPL-G2-4 (bizonyíték-kapu, EVIDENCE_GATE, X-8: RT-P0-08/-19, „Allowed attempts”) — az IMPL-G1-1 rokon mintája; M2:IMPL-G2-7 (ledger: EMBERI DÖNTÉS, BLOCKED_HUMAN, X-5: a biztonsági doboz az LMS-M2-09 mezőnél; az M2-riport B. melléklete szerint a „címke-rész”, vagyis a lecke promptjának rögzítése a manifest Megjegyzésében, ELVETVE: redundancia, mert a TEXT-C profil szerint „a kérdés(ek) szövege a mező címkéje”) — K3: a PED-G1-2 tényállás-forrása („A TEXT-C activity csak a H5P teljesítése után nyílik meg” — az M2-finding Probléma-mezője) és az IMPL-G1-2 (c) mintája; a verifier nézze meg, a (c) „kérdéscímkébe + MAN:108 Megjegyzés” javaslata nem az M2-ben elvetett rész-e (a placeholder-hiány Z-többlet); M3:IMPL-G2-6 (EMBERI DÖNTÉS, X-4: opcionális reflexió tanuló-lokális vagy tárolt) és M2:IMPL-G1-1 (MEGERŐSÍTVE, objektív, P1, OPEN) — K3 (IMPL-G1-3 és a PED-G1-2 5. dia-része); M1:BIZT-G2-4, M2:BIZT-G2-3 (EMBERI DÖNTÉS, X-4: BIZT-2/BIZT-5 a „csak a mentorod látja” mögött) és M2:BIZT-G1-6 (EMBERI DÖNTÉS, X-4; = az M1:BIZT-G2-4 kapuja) — K4; M1:IMPL-G2-10 (EMBERI DÖNTÉS, X-11: az „Accepted file types” és a fájlszám, „korpusz-szintű hiány”; LMS-gazda + DPO + hozzáférhetőségi gazda; a nyers kimenet nem idézi) — K5: a verifier döntse el, az IMPL-G1-9 „video” csoportja objektív-e, vagy ennek a kapunak a része; M0:IMPL-3, M0:ERT-3 (EMBERI DÖNTÉS, X-6), M2:IMPL-G2-1 (EMBERI DÖNTÉS, X-6; DPO-rész X-4) és M3:IMPL-G2-1 (DUPLICATE = M0:IMPL-3) — K7; M2:ERT-G2-3 (MEGERŐSÍTVE, objektív, OPEN: az SCS-ág és a „Single Choice Setben a helyes opciót kell elsőként felvenni” mondat törlése, M2-riport I.2), M3:IMPL-G2-9 (MEGERŐSÍTVE: a típusnév Multiple Choice, egyválaszos), M4:IMPL-G1-3 (= M4:ERT-G1-7; MEGERŐSÍTVE, P1: SCS-kizáró fejlesztői megjegyzés, típuscsere nélkül, „M4.3:497 / Z.1:57” minta) és M5:IMPL-G2-3 (MEGERŐSÍTVE: a típusnév marad, M4-precedens szerinti megjegyzés) — K8: a precedens vegyes; az ERT-G1-5 tartalék útja az M4-es, a két fő javaslat az M3-as utat követi; M0:IMPL-7 (FIXED: a manifest „Név” oszlopa szerint), M4:IMPL-G1-8 és M5:IMPL-G1-5 (MEGERŐSÍTVE: a lecke veszi át a MAN „Név” értékét; H1, fájlnév marad) — K9 (a nyers kimenet nem idézi; azonos irány); M2:PED-G3-1 (EMBERI DÖNTÉS, X-10: lépésidők a rögzített blokkokon belül; HUM-OPS-01) — K13 (PED-G1-7); M2:BIZT-G3-2 (EMBERI DÖNTÉS, X-5: második felnőtt a peulákon; rokon: M0:BIZT-9, M1:BIZT-G3-2) — K14 (BIZT-G1-6); M2:BIZT-G1-1 (EMBERI DÖNTÉS, X-5: a KAPU §D „azonnal bevonja a Memunát” ígérete és határideje) — BIZT-G1-2 (a nyers kimenet rokon mintának nevezi; a Feedback-ág Z-többlet); M1:BIZT-G3-8 (EMBERI DÖNTÉS, X-4: a Johari-cetlik sorsa, a tábla fotózása) és M1:BIZT-G3-8.obj (MEGERŐSÍTVE, objektív, OPEN: a HUM-PRIV-02-re mutató képzői hivatkozás átvezetése, a cetlik sorsáról semmit nem állítva) — BIZT-G1-9: az M1-ben a HUM:149-hivatkozás átvezetése külön, a döntéstől függetlenül javítható objektív tétel lett, a BIZT-G1-9 a döntés utánra teszi — a verifier nézze meg, ugyanaz a felosztás áll-e; X-7 (Memuna, G1), X-12 (DPO, G2), X-8 (G3b) — BIZT-G1-10, IMPL-G1-8; nyelv: M0:NYELV-G1-13 (FIXED) és M2:NYELV-G1-9 (OPEN: névelő a modulazonosító előtt) — NYELV-G1-6; M0:NYELV-G2-18 (IN_PROGRESS: a Z.A négy helye a Z-javítással egy menetben), M2:NYELV-G1-17 (OPEN: „identitás-térkép”) és M2:NYELV-G3-13 (OPEN: „Blokk-leírások” → „Blokkleírások”; „a többi 17 fájl a saját scope-ja”) — NYELV-G1-7; M2:NYELV-G2-10 (OPEN: „Multi Choice” → „Multiple Choice”) — NYELV-G1-8; M2:NYELV-G3-17 (OPEN: „/ madrihot”) — NYELV-G1-9; az Anna-mátrix (`2026-10-10 Anna-kommitok és szakmai javaslatok – teljes megfeleltetési mátrix.md`; audit trail, nem kánon): E-Z-029 (MEGERŐSÍTVE, VALID_IMPROVEMENT: „Az „M0-hoz képest” alak a Z.4 :61, :198, :233, :320 sorában és a hubban is így áll: következetesség, nem rontás.”) — a NYELV-G1-6 ugyanezeken a helyeken névelőt kér: a verifier mérlegelje a 2026-10-10-i döntés 5. pontjával és az M0/M2 névelő-precedenssel; E-Z-030 (RETAIN: Z.4 LÉPÉS 4, :62) és E-Z-031 (PRESERVED / RETAIN: a Z.4:234 Anna-szövege + „(legalább az egyik határidős)”) — NYELV-G1-3; E-Z-036 (PRESERVED / RETAIN, MEGERŐSÍTVE: Z.A:81 „a 75’-es verziónál gondolkodj inkább 75–85’-ben”; „csak a percszámok változtak, a lezárt döntés szerint”, PGD-1002:67, EJSz:224) — K13 (PED-G1-7); E-Z-025 (RETAIN: a Z.3 SLIDE 4 „A következő 3 Zmán Kvucámon…”) — NYELV-G1-2; E-Z-040 (RETAIN: a 4.4.2 „1 szó, amit magammal viszek” rituálé) — NYELV-G1-13; N-Z-03 (EMBERI DÖNTÉS: a Zmán Kvucá helyi valóságtartalma, programvezető + ken-vezető) — K2, K3 és NYELV-G1-2 kontextusa, itt nem nyílik; N-Z-07 (NOT_IMPLEMENTED; Z.4:191–194, :206–208) és N-Z-09 (EMBERI DÖNTÉS: AI-emlékeztető nem AI-feladatú reflexiónál) — egyik lencse sem vette fel findingnak; N-Z-02 (NOT_APPLICABLE: a Z.1 SLIDE 4 a lecke egyetlen helyes válaszos interakciója) — K8 kontextusa; N-Z-04 (NOT_APPLICABLE) — a PED-G1 szerint már tárgyalt.

**Hívások:**
- V1 (14 ID): ERT-G1-1, ERT-G1-2, IMPL-G1-1, PED-G1-1, ERT-G1-7, PED-G1-2, IMPL-G1-2, IMPL-G1-3, BIZT-G1-8, ERT-G1-6, IMPL-G1-7, PED-G1-3, ERT-G1-3, PED-G1-5
- V2 (15 ID): BIZT-G1-4, IMPL-G1-4, BIZT-G1-5, IMPL-G1-8, IMPL-G1-9, BIZT-G1-7, IMPL-G1-11, ERT-G1-4, BIZT-G1-6, NYELV-G1-14, BIZT-G1-1, BIZT-G1-2, BIZT-G1-3, BIZT-G1-9, BIZT-G1-10
- V3 (16 ID): ERT-G1-5, IMPL-G1-5, IMPL-G1-10, NYELV-G1-4, ERT-G1-8, NYELV-G1-18, PED-G1-10, NYELV-G1-15, PED-G1-6, PED-G1-7, NYELV-G1-12, NYELV-G1-17, PED-G1-4, PED-G1-8, PED-G1-9, IMPL-G1-6
- V4 (12 ID): NYELV-G1-1, NYELV-G1-2, NYELV-G1-3, NYELV-G1-5, NYELV-G1-6, NYELV-G1-7, NYELV-G1-8, NYELV-G1-9, NYELV-G1-10, NYELV-G1-11, NYELV-G1-13, NYELV-G1-16

**Összesen: 57 ID, 4 hívás.**

**Hívás-témák:** V1 completion és teljesítés: a Z.4 megerősítése (LMS-Z-08, BSPEC-07, skálasorrend, a „Teljesítve” mércéje), a javítási út és a HUB:33, a Z.3 szöveges lépései és mentori elfogadása (LMS-Z-06/-07, a támogató személy köre), a reflektív választók completionje (X-6), a Z.A ↔ Z.4 kapcsolat és a Z.A szerepe a teljesítésben · V2 adatvédelem és gyermekvédelem: a Z.4 olvasói köre, a videós út (hozzájárulás, bizonyíték, fájlparaméterek), a Feedback beállításai (elemzőoldal, értesítés, „Required”), a Z.A biztonsági kerete egy képzővel, a Z.3 biztonsági lépése és megőrzési mondata, a Z.4 feltárás-mondatai, a Z.A papíralapú anyagai, szerepköri és runtime-bizonyíték · V3 H5P, nevek, pedagógia és időkeretek: a Z.1 SLIDE 4 Single Choice Setje, activity-nevek és hub–manifest eltérések, a Z.2 mikrocélja, a Z.3 „túl kicsi” vállalása és általánosító lépése, leckeidők és kognitív terhelés, a Z.A időkeretei és eszközlistája, a VO D-19 szerinti leirat · V4 nyelv: esetrag, mintaszöveg, vezető kérdés, blokk/szakasz, névelő, összetételek, típusnevek, Korosztály, szám és személy, alaptag, „1 szó”, compliance-regiszter.

**Mit kérünk minden findingnál:** verdikt (MEGERŐSÍTVE / ELVETVE / EMBERI DÖNTÉS) és típus; a súly helyes-e; duplikátumnál a megtartandó; a javasolt javítás nem ront-e (kánoni mondat, answer key, regressziós minták), és ha a javítás új pedagógiai tartalmat írna, vagy a lezárt döntés új alkalmazási esete: EMBERI DÖNTÉS.

---

# B. melléklet – verifier-verdiktek

## V4 — nyelv (12 ID)

V4 verdiktek: Z, AP-2026-10-11-01 (nyelv). Minden hivatkozott helyet a jelenlegi fájlokban olvastam vissza. Baseline mindenhol ismeretlen.

NYELV-G1-1 · MEGERŐSÍTVE · objektív · P2 · A Z.1:368 kérdés így szól: „Peula v2-t Zmán Kvucával”. Ugyanebben a leckében a :381 és a :315 „Zmán Kvucára” alakot ír, így a kérdés és a visszajelzés vonzata eltér (7-es minta). · duplikátum: nincs · korlát: csak az esetrag változik. Az opciók és a ✅ (M7) maradnak. A K8 típusdöntése ettől független.

NYELV-G1-2 · MEGERŐSÍTVE · objektív · P2 · A :237 mintaszöveg két helyhatározót tesz egymás mellé: „A következő 3 Zmán Kvucámon a ... Zmán Kvucámon futtatom le”. A nyitással összeolvasva a :227 példa is ezt adja („…a 2. Zmán Kvucámon futtatom le”). Ez nyelvtanilag hibás. · duplikátum: nincs · korlát:
- A „A következő 3 Zmán Kvucámon…” nyitás betűre marad (:219, :318, Z.4:207, E-Z-025 RETAIN).
- A javasolt „mégpedig a ... alkalommal” rés a :222 MIKOR-példával („a következő 3 Zmán Kvucám közül a másodikon”) már nem olvasható össze. A :222 példát egy menetben a réshez kell igazítani, vagy olyan rést kell választani, amelybe a :222 példa változatlanul beillik.
- A három kötelező elem nem változik.
- A PED-G1-1 korlátja („a :237 nem változik”) csak a PED-G1-1 saját javítására szól. A sorrend: előbb ez a javítás, utána az IMPL-G1-2 (c), amely a mintaszöveget a címkébe viszi.

NYELV-G1-3 · ELVETVE · objektív · P2 · A Z.4 mondata („Írj le 1–2 konkrét célt a következő lépésekhez a terepre”) nyelvtanilag helyes. A Z-ben a „cél” és a „következő lépés” egymás megfelelőjeként áll (Z.3:15 „1–2 konkrét következő lépésed, célod”; Z.4:216 „Legalább az egyik célodnál … határidőt”), így félreértés nem bizonyított. A hely Anna-szöveg (E-Z-029 VALID_IMPROVEMENT, E-Z-030 és E-Z-031 RETAIN), átírása ütközne a 2026-10-10-i döntés 5. pontjával. A „Teljesítve”-mérce kérdése az ERT-G1-1-é. · duplikátum: nincs · korlát: —

NYELV-G1-5 · ELVETVE · objektív · P2 · A „blokk” (a lépés csoportja) és a „szakasz” (a sablon része) két külön fogalom, és a lecke kifejezetten megfelelteti őket. A :182 szerint „Az íven ez két külön szakasz (a / b)”, a :203 és a :218 pedig így ír: „Az ív 2. szakasza … a rész”, „3. szakasza … b rész”. A tanuló a szakaszcímeket másolja, nem a blokkcímeket. Bizonyított terminológiai hiba nincs, a „2–3. szakasz” csere preferencia. · duplikátum: nincs · korlát: —

NYELV-G1-6 · MEGERŐSÍTVE · objektív · P2 · Teljes mondatban hiányzik a névelő az azonosító előtt. Ugyanabban az idézetben a helyes alak is áll: Z.4:198 „M0-hoz képest? … amit az M0-ban”, Z.4:61 „M0-hoz … M0-ban”. A precedensek ugyanígy döntöttek: M0:NYELV-G1-13 FIXED, M2:NYELV-G1-9, M5:NYELV-G2-13. Az E-Z-029 szerint Anna eredeti szövege „az M0 modulhoz képest” volt, a névelő tehát nem rontja Anna szövegezését. · duplikátum: nincs (új Z-helyek, az M2:NYELV-G1-9 mintája) · korlát:
- Csak a teljes mondatos helyekre szól: HUB:109; Z.4:61 (két hely), :137, :190, :198, :233, :320; Z.A:23.
- Kimarad a zárójeles és a távirati hely: HUB:132 „(kulcsszavak M0–M7-ből)”, Z.4:152 (fejlesztői „Cél:” sor), Z.A:192 „(építve Z.2-re)”.
- A Z.1:271 `@source` csak hanggyártási fix packon át, újrarendereléssel változhat, mert a leiratnak szó szerint követnie kell a hangot (VO D-19; ütközik az IMPL-G1-6-tal). A Z.1:195 `@asset` csak build úton. Pin kell.

NYELV-G1-7 · MEGERŐSÍTVE · objektív · P2 · A felsorolt helyeken a kötőjeles, illetve különírt köznévi összetételek mind ott vannak: Z.A:88, :43, :64–84, :313, :329, :343, :346, :392, :457, :520, :529–530; HUB:91, :92, :165; Z.2:107; Z.4:191–192. A kéttagú összetételt egybeírjuk, a „szófelhő-rituálé” 3 tagú és 7 szótagú, ezért kötőjeles. A hub saját „köszönéskör” alakja is ezt támasztja alá. Az egybeírás precedense: M2:NYELV-G3-13, M2:NYELV-G1-17. · duplikátum: nincs (az M0:NYELV-G2-18 Z.A-helyei kizárva) · korlát:
- Az „AkH 6:3” hivatkozás nem pontos, de a javaslat helyes.
- A héber tagú összetételek, az „Időkapszula-” és a „Félév-emojik” név, valamint az induló-szavak helyei (:55, :423, :440, :458) kimaradnak.
- A :291 és a :480 `@asset` csak build úton, külön `chore(media)` commitban.
- A :343 zárójelben a NYELV-G1-17-tel együtt kell szerkeszteni. A HUB:92 tárgytalan lehet, ha a PED-G1-4 átírja.

NYELV-G1-8 · MEGERŐSÍTVE · objektív · P2 · A Z.1:321 „H5P **Multi Choice**” nem létező típusnevet ad (a runtime acceptance „Multiple Choice”-t ír). A Z.4:383 „Multi Choice” és a :385 „Single Choice” Moodle Feedback-környezetben áll, holott a :376 a „Multiple choice” nevet használja, és a Feedbackben nincs „Single Choice” típus. A precedens az M2:NYELV-G2-10. · duplikátum: nincs · korlát:
- A Z.1:57 és a Z.3:59 a címkéket kifejezetten pedagógiai jelölésnek mondja. Az idézett „Multi Choice” címkét ott a dia-címkékkel egy menetben kell átírni, a mondat többi része nem változik.
- A „Single Choice Set” megtartása a K8 típusdöntését nem akadályozhatja.
- A ✅ nem változik.

NYELV-G1-9 · MEGERŐSÍTVE · objektív · P2 · A Z.A:11 szövege: „képzős madrihok (15+)”. A Glosszárium:72 szerint „Egységesen `madrihok / madrihot` … (a „Korosztály” fejlécekben is)”. A precedens az M2:NYELV-G3-17 és az M5:NYELV-G2-10. · duplikátum: nincs · korlát: csak a „/ madrihot” kerül be, a „15+” marad.

NYELV-G1-10 · MEGERŐSÍTVE · objektív · P2 · Csak a Z.A:206-ra szűkítve. A felolvasandó blokkban egy mondaton belül vált a személy: „Aki … elmentette magának … most idézze fel … – ez is lehet az egyik tanulási pillanatod … idézd fel”. Ez valós egyeztetési hiba. · duplikátum: nincs · korlát:
- Az „M0.1–M0.2 online leckében” egyes száma helyes: tartomány után a magyar egyes számot használ. Ez az alpont elvetve.
- Elvetve a Z.1:34 is: a „honnan indultunk / hova jutottál” közös utat és egyéni eredményt állít szembe, hiba nem bizonyított.
- Elvetve a Z.4:53 is: a „csinálunk / Végigmész” bevett utasítási regiszter.
- Elvetve a Z.A:405–406 is: a képzői forgatókönyv távirati stílusa nem hiba.
- A passz- és a cetliszabályok tartalma nem változik.

NYELV-G1-11 · ELVETVE · objektív · P2 · A Z.3:176 „Ezekben közös, hogy:” a „közös bennük, hogy…” szerkezet szabályos változata, nem hiányos mondat. A Z.A:319 „nonformális” a képzői forgatókönyv zárójeles, távirati kulcsszó-listájában áll, ez nem hiba (prompt). Bizonyított nyelvtani hiba nincs. · duplikátum: nincs · korlát: —

NYELV-G1-13 · MEGERŐSÍTVE · objektív · P2 · A Z.A:459 ezt mondja: „írj rá **1 szót** … Lehet érzés, érték, gyakorlat, mondat”. Ez ellentmond a címnek (:414 „1 szó”), a :452, a :460 („Mindenki felír egy szót”) és a HUB:140 szövegének (cím–instrukció széttartás, 7-es minta). A „mondat” kihúzásával a szöveg a négy egyező helyhez igazodik, és az E-Z-040 szerint megtartott „1 szó” rituálé változatlan marad. · duplikátum: nincs · korlát: csak a „mondat” szó törlődik. Ha a szerző rövid kifejezést akart megengedni, az tartalmi döntés: akkor minden „1 szó” hely együtt változik. A BIZT-G1-9 helyei (:459 „Nem kell nevet írni rá”) nem változnak.

NYELV-G1-16 · ELVETVE · objektív · P2 · Az „adatminimalizált” helyett más szót kérni regiszterpreferencia: a kettőspont utáni rész („hanih érzékeny adata nélkül”) maga kifejti a jelentést. A mondat a TEREP:15 kánoni szabályának szó szerinti átvétele, és a HUB:206 is így írja. A csere ugyanannak az adattakarékossági szabálynak eltérő megfogalmazását hozná létre, és a javasolt „csak a szükséges adatokat” értelmezést is beírna. Bizalom: alacsony. · duplikátum: nincs · korlát: —

Összesítés: 8 MEGERŐSÍTVE (NYELV-G1-1, -2, -6, -7, -8, -9, -10 szűkítve, -13), 4 ELVETVE (NYELV-G1-3, -5, -11, -16), 0 EMBERI DÖNTÉS. Ebből 0 bizonyíték-kapu. Duplikátum a 12 között nincs, más modul validált kulcsára sem duplikátum egyik sem: a -6, a -7, a -8 és a -9 korábbi precedensek mintáját követi új Z-helyeken. A -7 az M0:NYELV-G2-18 Z.A-helyeit kizárja.

Ütközések, amelyekre a javításnál figyelni kell:
- NYELV-G1-2 ↔ PED-G1-1 korlátja és IMPL-G1-2 (c): sorrend kell, a :222 példát is igazítani kell.
- NYELV-G1-6 Z.1:271 ↔ IMPL-G1-6: csak VO-újrarenderrel.
- NYELV-G1-8 ↔ K8.
- NYELV-G1-7 :343 ↔ NYELV-G1-17: egy szerkesztésben.

Vizsgált fájlok:
- 02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md
- 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md
- 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md
- 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md
- 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md
- 01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md
- 01 Fejlesztés/04 Audit/2026-10-10 Anna-kommitok és szakmai javaslatok – teljes megfeleltetési mátrix.md

## V3 — H5P, nevek, pedagógia, időkeretek (16 ID)

ERT-G1-5 · MEGERŐSÍTVE · objektív · P2 · Z.1:335 „Egyszerű **Single Choice Set**” és Z.1:13 típusneve ellentmond a Z.1:377–381 kérdésenkénti visszajelzésének, a Z.1:382 maga mondja ki, hogy az SCS-ben „nincs kérdésenkénti visszajelző mező”, az RA:81 pedig csak tesztel, típust nem választ; a korpuszminta (M5.1:192, :424, M5.3:355, M1.2:183, M7.2:152) és a DÖNT:77 („a H5P MultiChoice `Single Choice (Radio Buttons)` módja erre alkalmas”) is ezt támasztja alá; baseline ismeretlen · → IMPL-G1-5 · a „Randomize answers” a DÖNT:77 szerint megengedett többlet, nem kötelező; a ✅-ok, az opciók, a visszajelzés-szövegek és a SLIDE 4 completion-szerepe nem változik.
IMPL-G1-5 · MEGERŐSÍTVE · objektív · P2 · ugyanaz a tényállás, mint az ERT-G1-5-é (a hely visszaolvasva), ráadásul a h5p-semantics és az A11Y:83 („Auto continue” ki) pontos hivatkozásával; a típusnév egyválaszos Multiple Choice-ra cserélése a lecke saját visszajelzés-szövegeit teszi megvalósíthatóvá · megtartandó (K8) · csak a :13 és a :335 típusneve változik, a :382 szűkítése a :13 / :335 cserével együtt történik (a „Single Choice Set” címkének az NYELV-G1-8 korlátjában rögzített megtartását ez a csere felülírja: egy sor, egy szerkesztés); az M3:IMPL-G2-9 utat követi, az M4-es tartalékút csak akkor kell, ha a build-gazda mégis az SCS-t tartja meg.
IMPL-G1-10 · MEGERŐSÍTVE · objektív · P2 · (a) Z.4:27, :73, :77 „Záró reflexiós ív” ↔ Z.4:302 / MAN:110 „Záró reflexió + következő lépés”; (b) HUB:195 „érdemes a **Z.4-et `restrict access`-szel…**” ↔ MAN:110 / :112 kötelező unlock („Z.A után”); (c) a Z.1:59 „minden szabad szöveges mezője előtt” a D-2 óta nem létező mezőkre szól, a Z.2:65 már a javított minta; baseline ismeretlen · az (a) alpont → NYELV-G1-4 · a (d) alpont (HUB:171 ↔ PT:307) kiesik: a parafrázis jelentése azonos a PT szövegével, a javítás szükségtelen (2026-10-10, 5. pont); a HUB:195 szerkesztése egy menetben a K10-zel; a „reflektív, NEM értékelő” mondat és a `SCHEDULE_TO_RESYNC` marad.
NYELV-G1-4 · MEGERŐSÍTVE · objektív · P2 · HUB:190 „Moodle Feedback – „Képzés-értékelés”” ↔ Z.4:365 / MAN:112 „Képzési visszajelzés – név nélkül”; Z.4:27, :73, :77 „Záró reflexiós ív” ↔ Z.4:302 / MAN:110; az irány megegyezik a validált M0:IMPL-7, M4:IMPL-G1-8 és M5:IMPL-G1-5 mintájával (a manifest „Név” oszlopa áll) · megtartandó (K9 névrész) · a Z.A:24-en a Z.4 lecke címe áll („Z.4 – „Záró reflexió + képzési visszajelzés””): ez a cím marad, csak az Assignment neve változzon a manifest szerintire (pl. „a Z.4 „Záró reflexió + következő lépés” Assignmentje”); a Z.4:77 címsora is a §4 nevét kapja; fájlnév és link nem változik.
ERT-G1-8 · ELVETVE · — · — · A Z.2:18 egy képességet nevez meg („meg tudod nevezni…”). A :307 alternatívája csak a SLIDE 6 négy részkérdéséből a harmadikat váltja ki, a passzjogot a :307 és a :309 kifejezetten biztosítja, és a lépés tanuló-lokális, nem completion-feltétel (D-3), ezért bizonyított cél ↔ értékelés ellentmondás nincs. A javaslat a mikrocélt jelentősen hosszabbítaná (2026-10-10, 5. pont) · — · a Z.2:18 csak az NYELV-G1-18 vesszőjét kapja.
NYELV-G1-18 · MEGERŐSÍTVE · objektív · P2 · Z.2:18 „amit nehéznek éltél meg és mit mond ez rólad”: a két mellérendelt függő kérdés közé, az „és” elé vessző kell (AkH, tagmondatokat kapcsoló „és”); ugyanígy a Z.A:105 és a HUB:124 „melyik lenne az és miért?” (hiányos tagmondat); baseline ismeretlen · — · csak vessző kerül be, egyetlen szó sem változik; az ERT-G1-8 elvetésével nincs összefésülési ütközés.
PED-G1-10 · EMBERI DÖNTÉS · emberi-döntés · P2 · A Z.3:147 „Ha túl kicsit, túl általánosat:” és a :148 példa tényleg széttart (a példa csak az általánosságot mutatja), de a „túl kicsi” mint második hibatípus párhuzamos a :144 „túl nagyot” fordulattal, és összhangban van a :153 „de kicsit kihívó is” kritériummal. A szerzői szándék nem bizonyítható, ezért az objektív besorolás nem tartható; egy tényállás, egy verdikt-típus · → NYELV-G1-15 · a javasolt törlés („túl kicsit,”) nem használható: ha a hibatípus szándékos, a törlés megváltoztatná a lecke jelentését; a :148 és a :150–153 marad.
NYELV-G1-15 · EMBERI DÖNTÉS · emberi-döntés · P2 · cím ↔ példa széttartás (a regressziós szabálylista 7. mintája) a Z.3:147–148-on; a „túl kicsi” hibatípus szándékos is lehet (:144 ↔ :147 párhuzam, :153), ezért az irányt a modulgazda vagy a projektgazda dönti el: a „túl kicsit,” maradvány, és törlendő, vagy szándékos, és akkor új példa kell (az már új tartalom) · megtartandó (K12) · szöveget a repó nem választ; a :148 példa és a :150–153 kritériumlista döntés nélkül nem változik.
PED-G1-6 · MEGERŐSÍTVE · objektív · P2 · Ugyanabban a lépésben a Z.A:212 „Idő: fejenként kb. 3–4 perc.” ellentmond a Z.A:213 „kb. 3 perc/fő” sorának, és a DÖNT:67 (12. pont: „legyen egyszerűen **3 perc/fő**”) is 3 percet ír elő. Ez a HUM-OPS-01 bizonyítéka (HUM:205), a HUM:224-be ez a fél mondat nincs átvezetve, és ugyanezt rögzíti az Anna-mátrix :1107 sora. Baseline ismeretlen · — · csak a :212 értéke változik („kb. 3 perc”); a „hármasokban percekkel túlcsúszik” hatás túlzó (3×4 perc belefér a 10–12 perces keretbe), de ez a javítást nem érinti; a PED-G1-7 tilalma a :81-re és a :403-ra szól, ide nem.
PED-G1-7 · ELVETVE · — · — · A Z.A:81 pufferre vonatkozó tanácsa („a 75’-es verziónál gondolkodj inkább 75–85’-ben”) nem nevezi át a változatot. Összhangban van a HUM:224-gyel („a Z.A 75 perces változat”) és a DÖNT:67-tel, és az Anna-mátrix E-Z-036 sora (RETAIN, MEGERŐSÍTVE) ezt a sort kifejezetten a döntés megvalósításaként rögzíti. A HUB:32 a Z.A-nak „péntek 2. sáv (45–75’)” sávot ad, a 2×45’-et a PT:13 csak az M1–M7-re írja, ezért nincs bizonyított blokkhatár-sértés. A névhúzás „6 perc alultervezett” állítása bizonyíték nélküli becslés, és a fájl a csúszásra már ad vágási utat (:84, :408) · — · —.
NYELV-G1-12 · MEGERŐSÍTVE · objektív · P2 · Z.A:403 „45’-ben kihagyható” (= opcionális) ↔ :72 „névhúzás nélkül”, :77 „kimarad”, :344 „névhúzás nélkül”: a percbontás szerint a 45’-es változatban a névhúzás nem választható, hanem kimarad; egyértelműségi hiba; baseline ismeretlen; a PED-G1-7 elvetésével nem tárgytalan · — · csak a szó változik; a percek, a 75’-es 6 perc és a :408 „hagyd ki” (75’-es csúszás) marad.
NYELV-G1-17 · MEGERŐSÍTVE · objektív · P2 · Z.A:343 „75’ verzió”: minőségjelzőként a mértékjelölő szó -es képzőt kér, és ugyanebben a zárójelben (:344 „45’-es peulánál”) és a fájl más helyein (:77, :81, :403 „75’-es”) is a képzős alak áll; ez nyelvtani és következetességi hiba, nem távirati stílus · — · csak „75’-es verzió”; a percértékek és a zárójel többi „20’ elismerés-kör” típusú mennyiségjelölése marad; a :343 egy szerkesztésben az NYELV-G1-7 „elismerés-kör” javításával.
PED-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P2 · A HUB:92 a Z.3-ba általánosító lépést ír elő („fogalmazz meg a Z.2-ben felidézett pillanatból **1 általános elvet**”), a Z.3-ban viszont nincs ilyen lépés, és Z.2-hivatkozás sincs benne (0 találat). A Z.2:342 „Ezek a sztorik fognak segíteni a **Z.3-ban** is” ígérete ezt a hiányt erősíti. Ez két kánoni forrás (hub és lecke) ellentmondása, és az egyik megoldás új tartalom, ezért a modulgazda dönt · — · a `/course-fix` nem választhat; ha a hub igazodik a Z.3-hoz, az NYELV-G1-7 HUB:92-es „esemény-specifikus” helye tárgytalanná válhat.
PED-G1-8 · ELVETVE · — · — · A Z.2 és a Z.3 időtúllépése a lencse saját becslése („Becslésem szerint ez 15–20 perc”), mérés és kánoni számítási norma nélkül. A szöveges lépések tanuló-lokálisak, minimális karakterszám nélkül (D-3), a Z.3 4. diájának tagolása didaktikai preferencia, a :211 gyermekvédelmi bekezdése pedig nem rövidíthető. A le nem vezethető időt a DÖNT:58 (3. pont) mintájára pilotmérés adja, nem repóbeli javítás · — · —.
PED-G1-9 · MEGERŐSÍTVE · objektív · P2 · Az eszközlista a posztermunkához csak A4-et ad (Z.A:32 „A4-es lapok (min. 3–4 db kiscsoportonként) – a „Híd a terepre” poszterhez”; a :35-ös flipchart a felhőhöz kell), a 4.3/1. lépés viszont kiscsoportonként „1 nagy lapot (flipchart / A3)” oszt ki (:312). A Z.A-MUNK-01 notes mezője (:291) azt állítja, hogy a flipchart/A3 benne van a listában, holott nincs; ez belső ellentmondás. Baseline ismeretlen · — · szűkítés: a :32 alá egy új tétel kerüljön („kiscsoportonként 1 flipchart lap vagy A3 (Z.A-MUNK-01 sablon)”), az A4-sor maradjon (a notes mindkettőt felsorolja; ha a sort cserélnénk, az tartalomvesztés volna); a :516 „Papírok” már lefedi, nem kell hozzányúlni; az `@asset` mező nem változik.
IMPL-G1-6 · MEGERŐSÍTVE · objektív · P2 · A Z.1:266 és a :531 kötelező a11y-utasítása „(vagy adj hozzá magyar feliratot)” alternatívát ad. Ez ellentmond a lezárt VO D-19-nek (PRODUCTION-DECISIONS „Lezárt döntések”, :507: csak hangos narrációnál a látható leirat a szöveges ekvivalens, „a H5P Audio elemtől feliratsáv nem várható”), a K2-nek (:513) és a fájl saját a11y-jegyzetének (:203, :477). A lezárt döntés szó szerinti átvezetése objektív javítás; baseline ismeretlen · — · csak a zárójeles alternatíva cserélődik a VO D-19 / VO D-21 fordulatára; a „szó szerint” és az „Új tartalom nem hangozhat el” kikötés, a `@source` (:268–275, :533–539) és az `@asset` mezők nem változnak. Látható szöveg, ezért pin kell. A NYELV-G1-6 :271-es VO-javítása más szöveg, de ha újrarenderelés nélkül kerülne be, a szó szerinti leirat eltérne a hangtól: ez a NYELV-G1-6 korlátja.

Összesítés (16 ID): MEGERŐSÍTVE 10 (ERT-G1-5, IMPL-G1-5, IMPL-G1-10, NYELV-G1-4, NYELV-G1-18, PED-G1-6, NYELV-G1-12, NYELV-G1-17, PED-G1-9, IMPL-G1-6); ELVETVE 3 (ERT-G1-8, PED-G1-7, PED-G1-8); EMBERI DÖNTÉS 3 (PED-G1-10, NYELV-G1-15, PED-G1-4). Bizonyíték-kapu: 0. Duplikátumok: ERT-G1-5 → IMPL-G1-5 (K8); az IMPL-G1-10 (a) alpontja → NYELV-G1-4 (K9; az IMPL-G1-10 a (b) és a (c) alponttal önállóan megmarad, a (d) kiesik); PED-G1-10 → NYELV-G1-15 (K12, egy verdikt-típus: EMBERI DÖNTÉS). A K11-ben az ERT-G1-8 elvetésével csak az NYELV-G1-18 marad; a K13-ban a PED-G1-7 elvetésével az NYELV-G1-12 nem tárgytalan.

## V1 — completion és teljesítés (14 ID)

ERT-G1-1 · EMBERI DÖNTÉS · emberi-döntés · P1 · A Z.4 „Teljesítve” értékére három mérce vonatkozik, és mindhárom ott van a fájlokban. (1) A hármas minimum: HUB:186–189, illetve a Z.4:345 címe: „Minimum elvárás a „Teljesítve”-hez”. (2) A MAN:111: „tényleges, minimálisan értelmezhető tartalom”. (3) A Z.4:347 ugyanezt a minimumot tanácsnak nevezi („érdemes szem előtt tartani”), a :353 pedig „nagyon hiányos / alibi”. A MAN:173 csak az M2 és az M4 küszöbét mondja formatívnak. A MAN:19 „a forrás minimuma alatt javítás” mondata kétértelmű. A HUM:457 csak alsó határ. Lezárt döntés nem válaszolja meg, ez valódi küszöbdöntés: értékelési felelős, vétó/QA: programvezető · — · Ahogy a finding írja: a döntésig a minimum szövege, a címkepár és az 1+1 beadás nem változik. Az ERT-G1-2 és az IMPL-G1-1 nem előlegezheti meg a döntést, és a NYELV-G1-3 korlátja (HUB:189 / Z.4:351) is ehhez kötött.

ERT-G1-2 · MEGERŐSÍTVE · objektív · P1 · A Z mappában az „LMS-Z-08” 0 találat. A HUB:199 („Z.4 leadott záró reflexió”) ellentmond a MAN:163-nak (leadás ÉS LMS-Z-08 = „Teljesítve”). A Z.4:343 „kézi megerősítés” útja ellentmond a MAN:25 tilalmának („a stáb kézzel nem írja felül”). A Z.4:341 sorrendje („`Teljesítve / Még nem teljesítve`”) fordítottja a MAN:25 kötött sorrendjének, miközben a MAN:191 szerint „a címkéket a Z.4 adja”. Ez hamis completion kockázata. A BSPEC-07 / D-h (HUM:560) lezárt, ezért a MAN szó szerinti átvezetése objektív. Ez a megtartandó a K1-ből · megtartandó (IMPL-G1-1 ide olvad) · Csak a MAN:19, :25, :110–111 és :163 szó szerinti szövege kerülhet át. A „Teljesítve” tartalmi mércéjéhez (ERT-G1-1), a címkepárhoz, az 1+1 beadáshoz és az Assignment saját skálájához (Z.4:340) nem nyúl. Ugyanebben a szerkesztésben átveheti az IMPL-G1-1 (d) objektív első felét (lásd ott).

IMPL-G1-1 · MEGERŐSÍTVE · objektív · P1 · Az (a)–(c) pont ugyanaz a tényállás, mint az ERT-G1-2: Z.4:343 ↔ MAN:110, Z.4:341 ↔ MAN:25. A Moodle-forrást megnyitottam: a docs.moodle.org/405 Assignment settings szövege szerint „Automatically until pass (after grading, until the student achieves the passing grade)”. Egyedül a (d) pont többlet. A Z.4:338 zárójeles mondata („A manifest ASSIGN-S profilja szerint újrabeadás engedett”) a MAN:19 Peula v1-re szóló fordulatát idézi, nem a „puha kapus beadásoknál (… LMS-Z-04) 1 normál + 1 javító beadás automatikusan” mondatot. Ez objektív hiba · → ERT-G1-2 · Az (a) pont „a tartalmi minimummal” fordulata csak a MAN:110–111 szövegét jelentheti, a HUB / Z.4:349–351 minimumát nem (ERT-G1-1). A (d) második fele (az LMS-Z-04-et is értékelni kell, a mentor kétszer ír be) LMS-konfigurációs és runtime-kérdés. Most nem implementálandó: a meglévő RT-P0-19 / RA 3 bizonyítéki kapuhoz (M1:IMPL-G2-4) és az X-11-hez tartozik.

PED-G1-1 · MEGERŐSÍTVE · objektív · P1 · A HUB:33 „Mivel a Z az M7 megerősített teljesítése után nyílik” mondata ellentmond a lezárt Q-REL-2-nek (HUM:510) és a BS-D3-nak (HUM:517), valamint a MAN:247 szövegének: „(„Még nem teljesítve” esetén is”. A Z.3:215 („Az M7-ben a Peula v2-d mellé már leadtál egy kipróbálási szándékot”) a javítási úton lévő madrihra hamis, mert a v2 leadása az LMS-M7-09-ig zárva marad (MAN:162). Az M7.B:563-ban a kipróbálási szándék valóban rögzítve van · — · A HUB:33-ba csak a MAN:247 szövege kerülhet, egy szerkesztésben az ERT-G1-7 részével, új dátum nélkül. A Z.3 feltételes mondata csak a v1-re és a meglévő M7.B:563-ra mutathat; az M7-riport nem validált. Nem változik: az LMS-Z-07 kritériumai, a :211 gyermekvédelmi bekezdés és a :237 mintaszöveg. A :237 a NYELV-G1-2 (V4) javaslatával ütközik: annak verdiktje az irányadó.

ERT-G1-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · A Z.4:339 szerint a megerősítés „a következő napon” van. A MAN:249 a javító beadás idejét csak a „Puha kapunál (M2, M4)” rendezi, a MAN:149 pedig külön kezeli a „puha kapunál (M2, M4) és a Z-nél” esetet. Az LMS-Z-07 határideje „—”. A MAN:247 csak az M7 javítási útján lévő madrih Z-határidejét fedi le, a Z saját javító útját (a Z.4 javító beadását, a Z.3 újrabeküldését) nem. Gazda: programvezető, HUM-OPS-01 (X-10) · — · Dátumot nem találunk ki (`SCHEDULE_TO_RESYNC`). A HUB:33 a PED-G1-1-gyel egy szerkesztésben változik. A BS-D8 lánc és az 1+1 beadás nem változik.

PED-G1-2 · MEGERŐSÍTVE · objektív · P2 · Ugyanaz a tényállás, mint az IMPL-G1-2: az LMS-Z-06 csak az LMS-Z-03 után nyílik (MAN:108, :16), a Z.3:348 („Nyugodtan lépj vissza 1–2 diát…”) pedig a beírás előtt fut. A 3. pont (az 5. dia mezője) az IMPL-G1-3 tárgya · → IMPL-G1-2 · A „jegyzetbe írja” fordulat beolvasztható az IMPL-G1-2 útbaigazításába.

IMPL-G1-2 · MEGERŐSÍTVE · objektív · P2 (a lencse P1-et adott; a lánc ép, completion nem sérül) · A tanulói szöveg sehol nem mondja meg, hová és mikor kerül a válasz. A :302 „a 4. és a 6. dián írtakat” említi, a SLIDE 7 önellenőrzése pedig a beküldés előtt fut. A Z.3:236 „Mezőben megjelenő mintaszöveg” Feedback „Longer text answer”-ben nem valósítható meg. Ezt a forrásban ellenőriztem: a MOODLE_405_STABLE `textarea_form.php` mezői csak `required`, `name`, `label`, `itemwidth`, `itemheight` · megtartandó (PED-G1-2 ide olvad) · Az (a)–(b) maradhat. A (c)-ből csak a kérdéscímke-rész maradhat: a TEXT-C szerint „a kérdés(ek) szövege a mező címkéje”. A „MAN:108 Megjegyzés” rész kimarad: az M2:IMPL-G2-7-ben ugyanezt redundanciaként ELVETETTÉK. A mintaszöveg előbb a NYELV-G1-2 verdiktjét várja, az „A következő 3 Zmán Kvucámon…” nyitás betűre marad. A (d) kimarad: a Z.3:327 maga kéri, hogy a tanuló írja fel magának a két mondatot, így a Z.4:207 „magadnak elmentett” fordulata nem hibás. Az unlock-cella nem változik. A :300 szabálymondata (BIZT-G1-1) érintetlen.

IMPL-G1-3 · EMBERI DÖNTÉS · emberi-döntés · P1 · A Z.3:260–263 beágyazott rövid szöveges mezőt ír elő mintaszöveggel, a Z.3:57 szerint viszont CP-dián ilyen mező nem feltételezhető. A MAN:108 szerint „a lecke opcionális mezői nem ide tartoznak”. A MAN:308 leltára a Z-ből csak a Z.1 SLIDE 5–6-ot és a Z.2 SLIDE 5–7-et tartalmazza. A D-2/D-3 a Z.3 SLIDE 5-öt és 7-et nem nevezi meg, ezért ez új alkalmazási eset. Gazda: projektgazda mint build-spec gazda; DPO/jogi QA a D-2/D-3 mintájára; tárolt útnál a BS-D6 is. Rokon: M3:IMPL-G2-6 (X-4), de más elemekről szól · megtartandó (a PED-G1-2 3. pontja ide tartozik) · A döntésig a :11 és a :260–263 nem változik, és completion- vagy TEXT-C-sor sem kerül be.

BIZT-G1-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · A Z.2:13 completion-sora ellenőrizve. A Z.2:233–240 („kudarcélmény”, „nem szeretnék most erre gondolni”) és a Z.3:121–127 („félek bármit ígérni”) ellentmond az ADV:150-nek: „saját önreflexió: ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség”. Az (a) pont, hogy a D-d/D-i kiterjed-e a Z-re, az M0:ERT-3 kérdése (X-6). A (b) pont önálló DPO-kérdés: ezeknek a válaszoknak a fiókhoz kötött tárolása, a D-j mintájára (X-4) · (a) → M0:ERT-3; (b) megtartandó · A választók, a completion-listák és az RA 14 szerinti típusválasztás nem változik. A dialista hiányos: a Z.3 SLIDE 3 kimaradt, az ERT-G1-6 és az IMPL-G1-7 listája szerint pótlandó.

ERT-G1-6 · EMBERI DÖNTÉS · emberi-döntés · P2 · A Z.1:13 és a Z.2:13 helyes válasz nélküli választókra épül. A Z.3 metájában nincs „Completion (lecke)” sor. A HUM:561 a D-i elvét név szerint csak az M0.3-ra és az M2.2-re terjeszti ki. A 2026-10-05-i riport :54–55 sora valóban a „pontozott interakciókkal” osztályba sorolja a „Z-01…03”-at. A Z-re való kiterjesztés új alkalmazási eset, a meglévő X-6 kapu része · → M0:ERT-3 · A döntésig a választók, az opciók, a D-2/D-3, a „Hide summary slide” és a Z.1 SLIDE 4 nem változik.

IMPL-G1-7 · EMBERI DÖNTÉS · emberi-döntés · P1 · A tényállás ugyanaz, mint az ERT-G1-6. A `cp.js`-t ellenőriztem: az összefoglaló dia a `slidesWithSolutions` / `hasAnswerElements` függvényében keletkezik. Ez a CP-completion jelentése, az M0:IMPL-3 nyitott kérdése (X-6), új döntést nem nyit · → M0:IMPL-3 · A döntés utáni lépés (a Z.3 completion-sora, az LMS-Z-03 Megjegyzése) a döntési csomaggal megy. Most completion-sor nem írható be.

PED-G1-3 · ELVETVE · — · — · A „nincs megvalósítva” állítás túloz. A Z.4:23 a „Z.A élő lezárás → Z.4” sorrendet rögzíti, a Z.4:283 kimondja: „ez az ív arra épít”, a Z.A:531–534 ellenőrző pontja pedig a képzőtől elvárja az online folytatás bejelentését. A felidéző rámutatás és az új képzői mondat didaktikai kiegészítés, a 2026-10-10-i döntés 5. pontja szerint preferencia. A Z.A-ról hiányzók Z.4:283-as helyzete az ERT-G1-3 döntésének része · — · Nincs.

ERT-G1-3 · EMBERI DÖNTÉS · emberi-döntés · P1 · A HUB:198 („2. Z.A záró peula (offline).”) a „Minimális teljesítés (a Z modul teljesítése)” alatt áll. A PT:213, a MAN:163 és a MAN:165 a Z.A-t nem sorolja a teljesítési feltételek közé, jelenléti elem sincs, az LMS-Z-04 dátummal nyílik (MAN:110). A kánon 1. és 2. forrása ellentmond egymásnak, és lezárt döntés nem rendezi; a CLAUDE.md szerint ilyenkor nem választunk. Gazda: programvezető + értékelési felelős · — · A Z.4 és a Feedback Z.A utáni, dátumos nyitása és a HUM:214 sorrendje nem változik. A HUB §5 listája egy szerkesztésben változik a K1-gyel (HUB:199), a K6-tal (:200) és a K9-cel (:195).

PED-G1-5 · ELVETVE · — · — · Az (a) pont didaktikai preferencia: a mikrocélnak nem kell felsorolnia minden elfogadási elemet. A (b) pontban nincs bizonyított ellentmondás. A :279 egy ötletgyűjtő kérdés („Ki tud ebben neked támasz lenni?”), a :283 sablonja és a HUB:96 a vállalás címzettjét szűkíti, a :287 és a MAN:109 („kinek mondja el”) pedig összhangban van egymással. A mentorok egyenetlen döntése feltételezés. Gyermekvédelmi szabályt nem érint, mert a felügyeletet a HUM-SAFE-03 külön rendezi · — · Nincs.

Összesítés: 5 MEGERŐSÍTVE (ERT-G1-2, IMPL-G1-1, PED-G1-1, PED-G1-2, IMPL-G1-2), 2 ELVETVE (PED-G1-3, PED-G1-5), 7 EMBERI DÖNTÉS (ERT-G1-1, ERT-G1-7, IMPL-G1-3, BIZT-G1-8, ERT-G1-6, IMPL-G1-7, ERT-G1-3). Ebből bizonyíték-kapu: 0. Az IMPL-G1-1 (d) runtime-része a meglévő RT-P0-19 / M1:IMPL-G2-4 kapuhoz tartozik, új kaput nem nyit.

Duplikátumok: IMPL-G1-1 → ERT-G1-2; PED-G1-2 → IMPL-G1-2; ERT-G1-6 → M0:ERT-3; IMPL-G1-7 → M0:IMPL-3; BIZT-G1-8 (a) → M0:ERT-3, a (b) DPO-része megtartandó (X-4).

Baseline: mind a 14-nél ismeretlen, a súlyosság emiatt nem emelkedett.

## V2 — adatvédelem és gyermekvédelem (15 ID)

BIZT-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.4:98 és a :329 szövege „A beadásodat csak a kijelölt mentorod vagy értékelőd látja”, az ADV:117 szerint viszont az ASSIGN-S értékelői nézetét a nem szerkesztő tanár, a szerkesztő tanár és a menedzser is látja, „nincs rögzítve (BIZT-5)”, az ADV:109 (BIZT-2) és az ADV:230 pedig DPO-kérdésnek tartja; ez meglévő X-4-kapu, baseline ismeretlen. · → M2:BIZT-G2-3 (az M4:BIZT-G2-2 és az M5:BIZT-G2-2 precedense szerint; új helyek: Z.4:98, :329, :307, és a videós út ugyanebbe a körbe esik; a K4 megtartandó Z-sora ez) · A tanulói mondat a HUM-PRIV-01 policy-mondata (HUM:132), a DPO-döntésig nem írható át; a Z.4:201 titoktartási kivétele marad.
IMPL-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P1 · Ugyanaz a tényállás és ugyanazok az idézetek (Z.4:98 ↔ ADV:117), ugyanaz a DPO-kapu (BIZT-5/BIZT-2, RT-P0-15), Z-többlet nélkül. · → BIZT-G1-4 → M2:BIZT-G2-3 · Mint a BIZT-G1-4-nél.
BIZT-G1-5 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.4:336 szerint „File submissions: ON” mindenkinek, a hozzájárulás rögzítését, ellenőrzését és a feltöltés feltételét pedig sehol nem írja le. Az ADV:139 kimondja: „A szülői/gondviselői tájékoztatás vagy engedélyezés helyi folyamata ezért emberi és jogi döntés”, az ADV:171 szerint a folyamat a HUM-PRIV-02-höz tartozik. A fotószabály (HUM:151, ADV:163: „a háttérben ne legyen gyerek … törlés a saját eszközről”) fotóra szól, videóra alkalmazása új alkalmazási eset. · — (a K5 megtartandó tétele) · Az írásos alapút, a hozzájárulási mondatok (Z.4:117, :310; HUB:184) és a 2–3 perc maradnak; hozzájárulási vagy tárolási folyamat nem írható be.
IMPL-G1-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · A tényállás valós (Z.4:336; ADV:214 „[ ] fotó/videó/hang folyamat HUM-PRIV-02 szerint lezárva”), de a bizonyíték-kapu besorolás nem tartható: a hozzájárulás folyamatát a kánon (ADV:139) nyitott emberi és jogi döntésnek mondja, nem lezárt döntés hiányzó szerepköri bizonyítékának. A videó legfeljebb 90 napos megőrzése és a szöveg „képzés vége + 90 nap” sora már külön áll a Z.4:307-ben; a törlés bizonyítéka (ADV:211, :214, release-evidence) a G2-höz tartozik, ezt a BIZT-G1-10 G2-sora fedi. · → BIZT-G1-5 · Az RR:83-ra épített „addig valódi madrihnak nem nyitható” mondat a lezárt döntés új alkalmazási esete, objektív szövegként nem használható.
IMPL-G1-9 · EMBERI DÖNTÉS · emberi-döntés · P2 · Valós és forrással igazolt (docs.moodle.org/405 Assignment settings: „Leaving the field blank will allow all file types.” / „It cannot be larger than the limit in the Course settings.”), és a Z.4:336 „100–200 MB” tartomány, nem érték. Az „Accepted file types” hiányát a ledger korpusz-szintű LMS-konfigurációs döntésként már az X-11-be sorolta, és az egyetlen méretérték az LMS-gazda választása, nem a kánonból következik. · → M1:IMPL-G2-10 (X-11; a Z.4:336 új hely) · Az opcionális videó, az írásos alapértelmezés és a 2–3 perc nem változik; értéket a repó nem választ.
BIZT-G1-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · Valós: a Z.4:398 a `Show analysis page` értékét „a HUM-PRIV-03 gazdája (adatvédelmi/DPO felelős + programvezető)” döntésére bízza, a FEEDBACK-N sor (MAN:22, ADV:119) pedig nem rögzíti. Elsődleges forrásból ellenőrizve: a `mod_form.php`-ban a `publish_stats` `selectyesno`, `setDefault` nélkül, a textarea `print_analysed` minden `$value->value`-t szó szerint kiír, a docs szerint pedig „Choose whether to show students the analyis page or only show to teachers.” A gazda (HUM:170 Jóváhagyó: DPO + programvezető) helyes. · — (a K6 (a) megtartandó tétele; az IMPL-G1-11 „Enable notification of submissions” fele ide olvad) · Értéket a repó nem választ; a „Record user names” = „Anonymous”, a kötelező kitöltés, az egyszeri beküldés, a 90 nap és a HUM-PRIV-03 tanulói mondata szó szerint marad.
IMPL-G1-11 · EMBERI DÖNTÉS · emberi-döntés · P2 · Ugyanaz a Z.4:398-sor (a két beállítás), a kódbeli bizonyíték azonos és igazolt. A finding premisszája részben hibás: a HUM:170 a DPO-t és a programvezetőt a HUM-PRIV-03 „Jóváhagyó”-jaként is megnevezi, nem csak utólagos ellenőrzőként, ezért a Z.4:398 delegálása nem ellentmondás. · → BIZT-G1-7 · A „döntéstől független objektív lépés” (új nyitott DPO-tétel az RR:25-be, a MAN:22/:112-be) nem javítás, hanem kapukövetés: a ledger X-4-ben vezetendő, a kánoni release-dokumentumba a döntés előtt nem írandó.
ERT-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.4:374–392 egyik kérdést sem jelöli „Required”-nek, a :382 kísérő kérdése kifejezetten „opcionális”, a :403 szerint pedig „mark as complete when submitted”. A MAN:24 a „Required”-et csak a TEXT-C-nél köti az üres beküldés kizárásához. A HUB:62/:200 („csak a kitöltés ténye számít”) és a lezárt „Üres sablon” szabály (HUM:457: „completion csak tényleges, minimálisan értelmezhető tartalommal”) között feszültség van, és a szabály kiterjesztése a Feedbackre új alkalmazási eset. Az üres beküldés runtime-viselkedése az RA 16-ban igazolandó. · — · A kérdések szövege, a név nélküli megjelenítés, a HUM-PRIV-03 tanulói mondata és a kötelező státusz nem változik.
BIZT-G1-6 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.A:45 szerint „felkavart résztvevőt nem küldünk ki egyedül, ott is egy felnőtt van vele”, a :53 és a :226 1:1 helyzetet „egy másik felelős tudtával” enged, a :522 ellenőrző lista ugyanezt kérdezi, a :412 szerint viszont „Ha van ken-vezető / felelős jelen”. A peula 8–20 főre (:12) képzőt ír elő (egyes számban; :410 „képző(k)”), második felnőtt nincs előírva. Ez az X-5 meglévő kérdése. · → M2:BIZT-G3-2 (a Z.A új helyként, az M3:BIZT-G3-2 mintájára) · A 2.2, a 2.3 és a 4.2 biztonsági mondatai, a safer-working kikötések és az ötlépéses jelzési út szó szerint maradnak.
NYELV-G1-14 · EMBERI DÖNTÉS · emberi-döntés · P2 · Valós: a Z.A:53 „…a kijelölt Memunához (…). Utána diszkréten, de átlátható helyzetben lép oda a résztvevőhöz” sorrendje (előbb bevonás, aztán odalépés) ellentétben áll a :226-tal („a peula után finoman odamehetsz hozzá”, mentor vagy Memuna nélkül). Ugyanarra a helyzetre két sorrend szól egy gyermekvédelmi eljárásban; a sorrend eldöntése a Memuna eljárási kérdése, nem nyelvi javítás. · — (nem duplikátum; ugyanabban az X-5-ös döntési körben a BIZT-G1-6-tal / M2:BIZT-G3-2-vel) · Szöveg nem javasolható; a safer-working kikötések és a jelzési út szó szerint maradnak.
BIZT-G1-1 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.3:300 kötelező, mentor által elfogadandó mondata („…nem vezetek éles foglalkozást, hanem jelzem a képzőnek.”) a repóban csak itt fordul elő (Grep), és a HUM:72–73, a GYV:60 és a Terepgyakorlat:24 nem rögzíti sem a lépést, sem a „képző” címzettet, sem a már jelen lévő hanihok esetét. Ez új eszkalációs és felügyeleti szabály a kiskorú madrihnak (X-5). · — · A biztonsági lépés és a HUM-SAFE-03 mondatai nem törölhetők és nem gyengíthetők; új eszkalációs szöveg nem írható be; a K3/PED-G1-5 javításai a :300 szabálymondatához nem nyúlhatnak.
BIZT-G1-2 · EMBERI DÖNTÉS · emberi-döntés · P1 · Valós: a Z.4:201 és a :370 „ne csak ebbe az ívbe/űrlapba írd”, az ADV:241 kanonikus mondata viszont „azt ne egy tanulási feladatban tedd”. A Z.4:201 „(ugyanaz, mint az M3.3-ban)” hivatkozása objektíven pontatlan: az M3.3:859 szövege „azt ne a reflexióba írd”, olvasó és mentori bevonási kötelezettség nélkül. A név nélküli Feedback-feltárásnak nincs kezelési útja; a §4 eljárása (Z.4:357–359) csak az Assignmentre szól. A tanulói mondat iránya és a Feedback-ág gyermekvédelmi/DPO-döntés (X-5, X-4). · — (rokon M2:BIZT-G1-1, nem azonos tényállás) · A döntéstől független objektív alpont csak a „(ugyanaz, mint az M3.3-ban)” hivatkozás pontosítása vagy elhagyása, a szabály szövegéhez nyúlás nélkül. A :370 első mondata (HUM-PRIV-03), a 112 és a „nem ígérünk teljes titoktartást” marad; új „ha téged is érint” blokk nem kerülhet be.
BIZT-G1-3 · MEGERŐSÍTVE · objektív · P1 · Valós és kánonnal ütközik: a Z.3:61 szerint „a megőrzési időt az … 3. szakaszának mátrixa rögzíti (projektgazdai döntés, 2026-10-02)”, a lecke egyetlen tárolt szöveges activityjére (LMS-Z-06) viszont a MAN:108, az ADV:90 és a HUM:520 (BS-D6, lezárt döntés: „Maradjon DPO-döntés; a repository nem találgatja”) szerint a megőrzési sor nyitott, és addig az activity „valódi madrihnak nem nyitható meg”. A BS-D6 át nem vezetése objektív hiba; baseline ismeretlen. · — · A MAN:108 BS-D6-os mondata szó szerint kerüljön át; megőrzési sort választani tilos; a HUM-PRIV-01 és a Program terv §4 nyitási feltétele marad. Ha az IMPL-G1-3 döntése negyedik LMS-Z-06 kérdést hoz, az is e mondat alá esik.
BIZT-G1-9 · EMBERI DÖNTÉS · emberi-döntés · P2 · Valós: a HUM:149 a Z.A-t név szerint a központi felvételi szabályra hivatkozó médiaaktivitások közé sorolja, a Z.A-ban viszont nincs HUM-PRIV-02- vagy ADV §6-hivatkozás (Grep: 0 találat). Az M0.A plakát, a képzői idézetek (:55), a névcetlik (:405), a poszterek és a szófelhő sorsa, és az, hogy szabad-e őket lefotózni, a DPO kérdése (X-4; rokon M1:BIZT-G3-8). · — (rokon M1:BIZT-G3-8 / M1:BIZT-G3-8.obj, más peula) · A javaslat időzítése nem használható: az M1-precedens szerint a HUM-PRIV-02-re és az ADV §6-ra mutató képzői hivatkozás, legfeljebb a HUM:151 szó szerinti alapértelmezésével, már most, a döntéstől függetlenül objektív alpont, és a papírok sorsáról semmit nem állíthat. A 2.3 kitakarási kikötése marad; tárolási szabályt nem írunk be.
BIZT-G1-10 · MEGERŐSÍTVE · bizonyíték-kapu · P1 · Valós: a lezárt döntésekhez (D-2, D-3, BS-D8, HUM-SAFE-02/03, HUM-PRIV-01–03) hiányzik a megnevezett szerepek írásos bizonyítéka. Az RTA:132, :141, :144, :145 és :153 sorai (RT-P0-03/-12/-15/-16/-24) `IMPLEMENTATION_TEST_REQUIRED` állapotúak, az ADV:216 „[ ] privacy/DPO/jogi signoff bizonyítéka rögzítve.”, a Z.1:453 pedig a DPO-t és a Memunát nevezi meg vétó/QA-szerepként. · — (a ledger X-7 (G1, Memuna), X-12 (G2, DPO) és X-8 (G3b) kapuihoz csatolandó; az ADV:214 videós release-evidence része is ide tartozik) · Nem javítható: „megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő”; semmi nem jelölhető megoldottnak.

Összesítés: MEGERŐSÍTVE 2 (BIZT-G1-3 objektív; BIZT-G1-10 bizonyíték-kapu), ELVETVE 0, EMBERI DÖNTÉS 13 (BIZT-G1-4, IMPL-G1-4, BIZT-G1-5, IMPL-G1-8, IMPL-G1-9, BIZT-G1-7, IMPL-G1-11, ERT-G1-4, BIZT-G1-6, NYELV-G1-14, BIZT-G1-1, BIZT-G1-2, BIZT-G1-9); ebből bizonyíték-kapu: 1 (BIZT-G1-10). Súlyváltozás nincs. Típusváltozás: az IMPL-G1-8 a lencse szerinti bizonyíték-kapu helyett emberi-döntés (ADV:139).

Duplikátumok:
- IMPL-G1-4 → BIZT-G1-4 → M2:BIZT-G2-3 (X-4)
- IMPL-G1-8 → BIZT-G1-5
- IMPL-G1-11 → BIZT-G1-7
- IMPL-G1-9 → M1:IMPL-G2-10 (X-11)
- BIZT-G1-6 → M2:BIZT-G3-2 (X-5)

Hivatkozott fájlok: 01 Fejlesztés/04 Audit/2026-10-11 Validált findingok – Z, AP-2026-10-11-01.md; 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md; 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md; 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md; 02 Tervezet/Adatvédelem – tanulói adatok és AI.md; 02 Tervezet/Emberi jóváhagyás szükséges.md; 01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md

---

# C. melléklet – nyers lencse-kimenetek (szó szerint)

## PED-G1 — pedagógia, hub, Z.1–Z.4, Z.A

Pedagógiai lencse, Z modul, G1 csoport (hub, Z.1–Z.4, Z.A). 10 findingot találtam. Közülük 1 P1, a többi P2. Típus szerint 7 objektív és 3 emberi döntés.

Fájlrövidítések (mind a `02 Tervezet/` alatt):
- HUB = `Modulok/Z/Z – Zárás & híd a terepre.md`
- Z.1 = `Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md`
- Z.2 = `Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md`
- Z.3 = `Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md`
- Z.4 = `Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md`
- Z.A = `Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md`
- MAN = `LMS – activity manifest.md`
- HUM = `Emberi jóváhagyás szükséges.md`
- DÖNT = `01 Fejlesztés/04 Audit/2026-10-02 Projektgazdai döntések.md`

---

**PED-G1-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:**
  - Z.3:213, :215, :227, :237, :275, :283 (4. és 6. dia, LMS-Z-06 1–2. kérdés)
  - HUB:33
  - ↔ MAN:162, :247, :259
- **Probléma:** A Z.3 kötelező, mentor által elfogadott első mezője leadott Peula v2-t és mellé leadott kipróbálási szándékot feltételez. Annak, akinek az M7-kvíz első próbálkozása nem sikerült, a Z hetében még nincs leadott v2-je: az ő v2-határideje az M7 javító határideje, az M7.F pedig a Z utáni héten van. A HUB:33 közben azt állítja, hogy a Z csak az M7 sikeres teljesítése után nyílik, ami ellentmond a manifestnek és a lezárt Q-REL-2 / BS-D3 döntésnek.
- **Bizonyíték:**
  - Z.3:215 „M7-ben a Peula v2-d mellé már leadtál egy kipróbálási szándékot” · HUB:33 „Mivel a Z az M7 megerősített teljesítése után nyílik”
  - MAN:247 „A Z az M7 megerősített kapueredményével nyílik („Még nem teljesítve” esetén is” · „az ő Peula v2-jének határideje is az M7 javító határideje”
- **Hatás:**
  - A javítási úton lévő madrih (már egy bukott kapu után) olyan anyag „elővételére” kap utasítást, ami nincs meg.
  - A kötelező mezőt nem tudja a leírt módon kitölteni.
  - A mentor nem tudja, mihez mérje az elfogadást.
- **Javaslat:**
  - (1) HUB:33: a „megerősített teljesítése után nyílik” helyére a MAN:247 megfogalmazása kerüljön (Q-REL-2, BS-D3).
  - (2) Z.3:215 után jöjjön egy feltételes mondat: ha a Peula v2 még nincs leadva (M7 javítási út), a tanuló a v1-ére és az M7.B-n rögzített kipróbálási szándékára építsen (M7.B:563).
  - Javítási korlát:
    - Az LMS-Z-06/07 kötelező státusza, a mentori elfogadás kritériumai (MAN:109), a :237 mintaszöveg és a :211 gyermekvédelmi bekezdés nem változik.
    - Új előírás (például a terv frissítése a v2 után) nem kerül be.
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:**
  - Z.3:217–221, :249–263, :298, :302, :318, :327, :348, :350
  - ↔ MAN:108
  - Minta: M2 IMPL-G2-7 (és M3 IMPL-G2-6 az 5. diára)
- **Probléma:**
  - A három kötelező válasz helye az LMS-Z-06, ami csak a Z.3 H5P teljesítése után nyílik. A 7. dia önellenőrzése így a beírás előtt fut le, a „Nem” ág pedig lehetetlen lépést kér: a diasorban nincs mit „átírni”.
  - A tanulói szöveg sehol nem mondja meg, hová és mikor írja a választ.
  - Az 5. dia „A következő hónapban…” mondatához mező van előírva („Mezőben megjelenő mintaszöveg”). Ez nincs az LMS-Z-06-ban, és a diasoron belüli mező a :57 szerint nem feltételezhető, így a helye meghatározatlan. Mégis erre épít a 7. dia és a Z.4:207.
- **Bizonyíték:**
  - Z.3:348 „Nyugodtan lépj vissza 1–2 diát, és írd át úgy, hogy”
  - MAN:108 „Z.3 – Szöveges válaszok | TEXT-C | igen | … | LMS-Z-03”. Az M2 IMPL-G2-7 validált tényállása: „A TEXT-C activity csak a H5P teljesítése után nyílik meg”.
- **Hatás:**
  - A mentori elfogadás előtti egyetlen önellenőrzés hatástalan.
  - A tanuló a diasort „kész”-ként zárja le, mielőtt bármit leírt volna.
  - A Z.4 egy meghatározatlan helyű mondatra hivatkozik.
- **Javaslat:**
  - A 4. dián (:217 környékén) és a biztonsági lépésnél (:298) jelenjen meg egy tanulói mondat: a választ a lecke után megnyíló szövegmezőben küldi be, addig a jegyzetébe írja.
  - A :318 és a :348 a jegyzetre hivatkozzon („írd át a jegyzetedben, mielőtt beküldöd”).
  - Javítási korlát:
    - A kötelező státusz, a beküldés → mentori elfogadás lánc és az LMS-Z-06 nyitási feltétele nem változik.
    - Az 5. dia mezőjének státusza (tanuló-lokális vagy tárolt) az M3 IMPL-G2-6 szerinti külön emberi döntés, nem része ennek a javításnak.
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:**
  - HUB:36, :195
  - Z.A:24, :531–534 (5/6. pont)
  - Z.4:152, :158, :283
- **Probléma:** A hub és a Z.A azzal indokolja, hogy a Z.4 a Z.A után jön (restrict access), hogy a Z.4 „a peulán megfogalmazott gondolatokból dolgozik”. Ez egyik oldalon sincs megvalósítva:
  - A Z.4 felidéző utasítása csak a Z.1–Z.2-re mutat.
  - A Z.A egyetlen blokkjában sincs a képzőnek kiírt mondat, amely a Z.4-hez vezetne. Csak az ellenőrző lista kérdezi: „Tudod, mit fogsz mondani…”.
  - A peulán egyéni, megtartott kimenet nem keletkezik.
- **Bizonyíték:**
  - HUB:36 „a peulán megfogalmazott gondolatokból dolgozik”
  - Z.4:158 „Gondolj vissza arra, amit a Z.1–Z.2-ben már elkezdtél:”
- **Hatás:**
  - A szándékolt térközös felidézés (peula → egyéni reflexió) elmarad, és a sorrendkényszer tartalmilag üres.
  - A Z.A-ról hiányzónak a Z.4:283 („a Z.A záró peulán volt”) hamis.
- **Javaslat:**
  - A Z.4:158 egészüljön ki egy rámutatással a Z.A meglévő elemeire (Időkapszula-pillanat, poszter, a szó, amit magával visz).
  - A Z.A 4.4.2/3. lépése kapjon egy képzői mondatot az 5/6. pont tartalmából (a folyamat online folytatódik: Z.4 és visszajelzés).
  - Javítási korlát:
    - Új feladat és új írásos lépés a peulán nem kerül be.
    - A hiányzók alternatív útja külön döntés, nem része ennek a javításnak.
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:**
  - HUB:92
  - Z.2:342–343
  - ↔ Z.3:33 és a 4–6. dia
- **Probléma:** A hub a Z.3-ba általánosító lépést ír elő: a Z.2-ben felidézett pillanatból egy általános elv, és a következő lépés ehhez kötődik. A Z.2 záró szövege is azt ígéri, hogy a „sztorik” a Z.3-ban segítenek. A Z.3 egyetlen diáján sincs ilyen lépés, és a Z.2 pillanataira sem hivatkozik. A hub és a lecke specifikációja ellentmond egymásnak.
- **Bizonyíték:**
  - HUB:92 „fogalmazz meg a Z.2-ben felidézett pillanatból”
  - Z.2:342 „Ezek a sztorik fognak segíteni a”
- **Hatás:**
  - A hub szerint a terepi átvitelt ez a lépés biztosítaná („ne maradjon esemény-specifikus”), de nem valósul meg.
  - A Z.2 ígérete üres marad.
  - A képző a hub alapján olyan elemre számít, ami a leckében nincs meg.
- **Javaslat:** EMBERI DÖNTÉS (modulgazda): az általánosító lépés kerüljön-e be a Z.3-ba (ez új dia vagy lépés, tehát új tartalom), vagy a HUB:92 és a Z.2:342 igazodjon a mai Z.3-hoz. A `/course-fix` ne válasszon.
- **Típus:** emberi-döntés
- **Verdikt:** —

**PED-G1-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:**
  - Z.3:15–17 (mikrocél), :279, :283, :287, :306
  - ↔ HUB:59–60 (4. kompetencia), :96; MAN:109
- **Probléma:** A cél, a kötelező mezők és a mentori elfogadás csak részben illeszkedik:
  - (a) A Z.3 mikrocélja csak az 1–2 célt és az első lépést nevezi meg. A mentor viszont „kiemelten” a biztonsági lépést és a támogató személyt fogadja el, ezek a hub 4. kompetenciájából jönnek.
  - (b) A támogató személy köre ellentmondásos. A :279 tág listát ad, a :283 sablon és a HUB:96 a mentorra vagy kijelölt tapasztalt madrihra szűkít, a :287 mezőleírás és a MAN:109 kritériuma pedig csak annyit mond: „kinek mondja el”.
- **Bizonyíték:**
  - Z.3:279 „(mentor, madrih-társ, ken-vezető…)”
  - Z.3:283 „(a mentorom vagy egy kijelölt tapasztalt madrih neve)”
- **Hatás:**
  - A tanuló nem tudja a célból, mi az elfogadás kulcsa.
  - Aki (akár 15 éves) madrih-társat nevez meg, attól függően kap „Még nem teljesítve”-t, hogy a mentor melyik szöveget követi. Az elfogadás így egyenetlen lesz.
- **Javaslat:**
  - (a) A mikrocél kapjon egy tagmondatot a HUB:59–60 és a Z.3:295–296 meglévő szövegéből (kitől kér segítséget, kinek jelez gyermekvédelmi aggálynál).
  - (b) A :287 mezőleírás nevezze meg a HUB:96 és a :283 szerinti kört.
  - Javítási korlát:
    - A :279 ötletlistája maradhat.
    - A MAN:109 kritériumai és a kötelező státusz nem változik.
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:** Z.A:212 ↔ :213; DÖNT:67 (12. pont)
- **Probléma:** A résztvevőknek felolvasott utasítás fejenként 3–4 percet ad. A következő sor képzői időtartása és a projektgazda 12. pontbeli döntése 3 perc/fő.
- **Bizonyíték:**
  - Z.A:212 „Idő: fejenként kb. 3–4 perc.” · Z.A:213 „Képző figyel az időre, kb. 3 perc/fő.”
  - DÖNT:67 „A „3–3–3 perc/fő” helyett legyen egyszerűen **3 perc/fő**.”
- **Hatás:**
  - Hármasokban a blokk percekkel túlcsúszik.
  - A képző a saját instrukciójával ellentétesen szakítja félbe a beszélőt.
- **Javaslat:**
  - Z.A:212: „fejenként kb. 3–4 perc” → „fejenként kb. 3 perc”.
  - Javítási korlát: semmi más nem változik.
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:**
  - Z.A:81, :403
  - HUB:32
  - ↔ HUM:224
  - DÖNT:67
  - Minta: M2 PED-G3-1
- **Probléma:**
  - A Z.A a 75 perces változatra 75–85, a 45 percesre 45–50 perc tervezését írja elő. A lezárt döntés szerint a Z.A 75 perces változat, a projektgazda indoklása szerint a megadott idő egyezzen a tartalommal („Ne hívd 60 percesnek…”). A 45 perces változat a pénteki blokkhatárt lépi túl (a többi modul „péntek 2. sáv” = 45’).
  - A névhúzásos kör „kb. 6 perc” 8–20 főnél (cetliírás, húzás, újrahúzás, fejenként egy mondat) szintén alultervezett.
- **Bizonyíték:**
  - Z.A:81 „a 75’-es verziónál gondolkodj inkább” … „és inkább a felső sávval kalkulálj”
  - HUM:224 „a Z.A 75 perces változat”
- **Hatás:** A képző 85 percre tervez egy 75 percre (illetve 45 percre) ütemezett alkalmat, így a központi naptár és a blokkhatár sérül.
- **Javaslat:** EMBERI DÖNTÉS (programvezető; HUM-OPS-01 vétó/QA): törlődjön-e a „75–85’ / 45–50’” tervezési tanács a meglévő vágási sorrend (Z.A:82–84) javára, vagy módosuljon a Z.A idősávja. A lépésidők átosztása az M2 PED-G3-1 mintájára szintén a modulgazdáé. A `/course-fix` ne nyúljon percekhez.
- **Típus:** emberi-döntés
- **Verdikt:** —

**PED-G1-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:**
  - Z.2:7, :264, :300
  - Z.3:7, :207–230 (4. dia), :232–306
  - HUM:465
- **Probléma:**
  - A Z.2 10–15 perce mellett két, egyenként 5–8 mondatos, kézzel írt reflexió áll, ráadásul négy input-dia, három választós kérdés és a 7. dia. Becslésem szerint ez 15–20 perc.
  - A Z.3 10–15 percébe három kötelező írásos válasz, az M7-beadás előkeresése és egyetlen mobil dián kb. 480 szavas szöveg fér (terepgyakorlati szabályok, felügyeleti szabály, majd a feladat).
- **Bizonyíték:**
  - Z.2:7 „**Időtartam:** 10–15 perc” · Z.2:264 „Írj **5–8 mondatot**” · Z.2:300 „Írj róla **5–8 mondatot**:”
- **Hatás:**
  - A záró hét (a Z.4 40–65 percével együtt) alultervezett.
  - A Z.3 4. diáján a kötelező feladat elvész a szabálylista mögött (kognitív túlterhelés mobilon).
- **Javaslat:** EMBERI DÖNTÉS (modulgazda; vétó/QA: programvezető, „Időkeretek: bottom-up sávok”, HUM:465):
  - Z.2: csökkenjen-e a mondatszám (például 3–5), vagy igazodjon a leckeidő.
  - Z.3: kerüljön-e a :207–211 áttekintő külön Input-diára.
  - Javítási korlát:
    - A :211 gyermekvédelmi bekezdés nem rövidíthető.
    - A Z teljes online idejének új összege a 2026-10-03-i külső audit 8. pontja szerint projektgazdai kérdés, ezt a finding nem nyitja újra.
- **Típus:** emberi-döntés
- **Verdikt:** —

**PED-G1-9**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia
- **Hely:**
  - Z.A:32, :35, :312, :516
  - a Z.A-MUNK-01 `@asset` notes mezője
- **Probléma:** Az eszközlista és a képzői ellenőrző lista nem tartalmazza a kiscsoportos poszterekhez kiosztandó nagy lapot. Az eszközlista A4-es lapokat ad, a 4.3/1. lépés kiscsoportonként egy flipchart- vagy A3-lapot. A Z.A-MUNK-01 notes mezője azt állítja, hogy a flipchart/A3 benne van a listában.
- **Bizonyíték:**
  - Z.A:32 „A4-es lapok (min. 3–4 db kiscsoportonként) – a „Híd a terepre” poszterhez”
  - Z.A:312 „Mindegyik kapjon 1 nagy lapot (flipchart / A3).”
- **Hatás:** A lista alapján készülő képző csak egy flipchartot hoz (a felhőhöz), a 2–4 kiscsoport plakátjához pedig nem lesz megfelelő lap.
- **Javaslat:**
  - Z.A:32 (és :516): „kiscsoportonként 1 flipchart lap vagy A3 (Z.A-MUNK-01 sablon)” a :312 és a Z.A-MUNK-01 asset szerint.
  - Javítási korlát: az `@asset` mező nem változik (a javítás után a notes mező állítása igaz lesz).
- **Típus:** objektív
- **Verdikt:** —

**PED-G1-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia
- **Hely:** Z.3:147–148 ↔ :103, :117, :142
- **Probléma:** A célkitűzést tanító input-dia a „túl kicsi” vállalást hibaként mutatja be. A példája („Jobb madrih leszek.”) azonban nem kicsi, hanem homályos, és a lecke központi üzenete éppen az, hogy a kis lépés a jó.
- **Bizonyíték:**
  - Z.3:147 „Ha túl kicsit, túl általánosat:”
  - Z.3:117 „**kicsi, konkrét lépések**, amik reálisak”
- **Hatás:** Pont a tanítandó fogalomnál zavaros a kontraszt (nagy ↔ homályos helyett nagy ↔ kicsi): a tanuló azt értheti, hogy a kis lépés is hiba.
- **Javaslat:**
  - Z.3:147: „Ha túl kicsit, túl általánosat:” → „Ha túl általánosat:”.
  - Javítási korlát: a :148 példamondata és a :150–153 kritériumlista (benne a „kicsit kihívó is”) nem változik.
- **Típus:** objektív
- **Verdikt:** —

---

Az Anna-mátrix hipotéziseiből egyiket sem vettem fel pedagógiai findingnak:
- **N-Z-07:** Az M0.1:411 és az M0.2:501 csak ajánlja a mondatok elmentését, ezért a Z.4:194/:208 tartalékútja pedagógiailag indokolt.
- **N-Z-03:** A Program terv :17 a Zmán Kvucát „a kvuca fix, rendszeres foglalkozás-idősávja”-ként definiálja, a Z.3 ezzel nem ellentétes.
- **N-Z-09:** A biztonság-jog lencse dimenziója (D8), azt nem vizsgáltam.
- Az M0 NYELV-G2-18 Z.A-helyeit nem ismételtem.

Neuromítoszt vagy túláltalánosított kutatási állítást (D9) nem találtam. Az appreciative inquiry hivatkozást (Z.A:386) az N-Z-04 már tárgyalta. A „nonformal-education.eu” forrást nem tudtam ellenőrizni, mert nincs webeszközöm, ezért nem jelentem.

## BIZT-G1 — biztonság-jog, hub, Z.1–Z.4, Z.A

## BIZT-G1: biztonság-jog lencse, Z modul, G1 (hub, Z.1–Z.4, Z.A), AP-2026-10-11-01, next-version

Csak olvastam, a D6, D7 és D8 dimenziót vizsgáltam. Fájlkulcsok:
- HUB = `02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md`
- Z.1 / Z.2 / Z.3 / Z.4 = `02 Tervezet/Modulok/Z/Online leckék/…`
- Z.A = `02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md`
- Kereszthivatkozások: MAN = `LMS – activity manifest.md`, HUM = `Emberi jóváhagyás szükséges.md`, ADV = `Adatvédelem – tanulói adatok és AI.md`, GYV = `Gyermekvédelem – release gate.md`, RTA = `LMS – H5P runtime acceptance.md`

**Kötelező triggerek:**
- **Gyermekvédelmi:** érintett a Z.3 biztonsági lépése, a Z.4 feltárás-mondatai és a Z.A biztonsági kerete.
- **Adatvédelmi:** érintett a Z.3 TEXT-C, a Z.4 Assignment és videó, a Z.4 Feedback, valamint a Z.A plakátjai és cetlijei.
- **AI-tartalom:** a scope-ban nincs AI-feladat. Csak a Z.1 visszatekintése említi az AI-t.

**Források:**
- A Moodle-állításokat elsődleges forrásból olvastam: a `moodle/moodle` repó `MOODLE_405_STABLE` ágának forráskódjából és a docs.moodle.org oldalról.
- Segélyvonal-számot nem ellenőriztem: a Z csak a 112-t említi.

---

**BIZT-G1-1**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.3:300 (biztonsági lépés, kötelező mintamondat), Z.3:306 (LMS-Z-06, 3. kérdés). Fájlközi: MAN:109 (LMS-Z-07, a mentor elfogadja), HUM:72–73 (HUM-SAFE-03), GYV §4:60.
- **Probléma:**
  - A kötelező, mentor által elfogadandó mondat új operatív szabályt tanít a kiskorú madrihnak. Ha nincs jelen a 18 év feletti felnőtt, vagy a Memuna adatai nem egyértelműek, „nem vezetek éles foglalkozást, hanem jelzem a képzőnek”.
  - Ez a szabály a kánonban sehol máshol nem szerepel: sem a HUM-SAFE-03-ban, sem a GYV-ben, sem a döntési jegyzőkönyvekben.
  - Nyitva hagyja, mi történik a már megérkezett hanihokkal. Így éppen az a helyzet áll elő, amelyet a HUM-SAFE-03 tilt: a kiskorú madrih a gyerekekkel egyedül marad, és ő dönt.
  - A jelzés címzettje (a „képző”) sincs kánonban rögzítve.
- **Osztály:** a felügyeleti szabály PROJEKT-DÖNTÉS (HUM-SAFE-03). Hogy a mondat a kánonban sehol nem szerepel, az TÉNY. A teendő, ha a felnőtt hiányzik, és a jelzés címzettje EMBERI JÓVÁHAGYÁS KELL.
- **Bizonyíték:**
  - Z.3:300: „vagy egy éles alkalmon a felkészített, 18 év feletti felelős felnőtt nincs jelen, és a helyszínen sem érhető el azonnal, nem vezetek éles foglalkozást, hanem jelzem a képzőnek.”
  - HUM:72: „A 15–17 éves madrih vezethet peulát, de soha nem ő az egyetlen felelős felnőtt.”
- **Hatás:**
  - A mentor egy kánonon kívüli szabályt fogad el teljesítési feltételként.
  - Ha a felnőtt hiányzik és a gyerekek már ott vannak, a 15–17 éves madrihnak nincs megtanult lépése. Felnőtt helyett ő dönt a helyszínen.
- **Javaslat:** EMBERI DÖNTÉS, a HUM-SAFE-03 gazdáinak: a Memunának és a programvezetőnek. Három kérdés:
  - (a) Elfogadják-e a „nem vezetek éles foglalkozást” szabályt.
  - (b) Kinek jelez a madrih: a képzőnek, a ken-vezetőnek vagy a programvezetőnek.
  - (c) Mi a teendő, ha a hanihok már a helyszínen vannak.

  Javítási korlát: a biztonsági lépés és a HUM-SAFE-03 mondatai nem törölhetők és nem gyengíthetők. Új eszkalációs szöveget nem szabad kitalálni.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-2**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.4:201 (LÉPÉS 4a), Z.4:370 (a Feedback leírása), Z.4:357–359 (feltárás-kezelés, csak az Assignmentre). Fájlközi: ADV §11:241, M3.3:859, Z.1:451, Z.2:44, HUM:172.
- **Probléma:**
  - A Z.4 két helyen azt mondja: „ne **csak** ebbe … írd”. A kanonikus tanulói mondat (ADV §11) viszont azt, hogy valós gyermekvédelmi helyzetet „ne egy tanulási feladatban” jelezzen a tanuló.
  - A Z.4:201 a saját szabályát „ugyanaz, mint az M3.3-ban” megjelöléssel vezeti be. Az M3.3 mai szabálya azonban „azt ne a reflexióba írd”, olvasó nélkül.
  - A név nélkül megjelenő Feedbackhez nincs feltárás-kezelési utasítás. A §4 eljárása csak az Assignmentre szól.
  - Nyitott, hogy egy Feedback-válaszban megjelenő feltárásnál szabad-e és ki által az adatbázisban megmaradó felhasználói azonosítóból (HUM:172) azonosítani a beküldőt.
  - Rokon minta: M2 BIZT-G1-1. A Feedback-ág Z-specifikus többlet.
- **Osztály:** TÉNY: a két szöveg eltér, a hivatkozott M3.3-mondat más. PROJEKT-DÖNTÉS: HUM-SAFE-01 és HUM-PRIV-03. EMBERI JÓVÁHAGYÁS KELL: a tanulói mondat iránya és a Feedback-feltárás kezelése.
- **Bizonyíték:**
  - Z.4:370: „A válaszok név nélkül jelennek meg a feldolgozásban. Ha veszélyről van szó, azt ne csak ebbe az űrlapba írd: azonnal vond be a Memunát.”
  - ADV:241: „Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd: azonnal vond be a kijelölt Memunát”
- **Hatás:**
  - A „ne csak” megengedi, hogy a tanuló az űrlapba írja a feltárást. Ott a feldolgozó nem tudja, kitől jött, és eljárási utasítása sincs. A jelzés elakadhat.
  - A Z.4 és a Z.1/Z.2 két eltérő szabályt tanít ugyanarra a helyzetre.
- **Javaslat:** EMBERI DÖNTÉS. Kérdések:
  - (a) A Memunától (HUM-SAFE-01): a Z.4:201 és a :370 átveszi-e szó szerint az ADV §11 mondatát.
  - (b) A Memunától és a DPO-tól (HUM-PRIV-03): mi a Feedback-feldolgozó teendője, ha egy név nélküli válaszban feltárás jelenik meg. Szabad-e a beküldőt azonosítani, és ki teheti meg.

  Ezek döntés nélkül is objektívek: a hibás „(ugyanaz, mint az M3.3-ban)” hivatkozás pontosítható vagy elhagyható, a szabály szövegéhez nyúlás nélkül.

  Javítási korlát: a 112 és a „nem ígérünk teljes titoktartást” mondat marad. Új „ha téged is érint” blokk nem kerülhet be (GYV §4.3).
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-3**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** Z.3:61 (fejlesztői feltétel, adatkezelési tájékoztató). Fájlközi: MAN:108 (LMS-Z-06), ADV:90, ADV §11:237 (`DPO_RETENTION_TO_CONFIRM`), HUM:520 (BS-D6).
- **Probléma:**
  - A Z.3 szerint a szabad szöveges mezők megőrzési idejét az ADV §3 mátrixa rögzíti, projektgazdai döntésként.
  - A Z.3 egyetlen tárolt szöveges activityjénél, az LMS-Z-06-nál ez nem igaz. A megőrzési sor ott nyitott DPO-döntés (BS-D6): 90 nap vagy 12 hónap.
  - A manifest ehhez a nyitás tilalmát is hozzáköti. Ez a Z.3-ba nincs átvezetve.
- **Osztály:** TÉNY: a Z.3 állítása ellentmond a MAN-nak és az ADV-nek. PROJEKT-DÖNTÉS: BS-D6, vagyis maradjon DPO-döntés.
- **Bizonyíték:**
  - Z.3:61: „a megőrzési időt az `Adatvédelem – tanulói adatok és AI.md` 3. szakaszának mátrixa rögzíti (projektgazdai döntés, 2026-10-02)”
  - MAN:108: „a válaszok megőrzési sora („Szabad szöveges reflexió” vagy „Assignment / peulatervek”) DPO-döntés (BS-D6), addig az activity valódi madrihnak nem nyitható meg”
- **Hatás:** A Z.3-ból építő fejlesztő a mátrixból választ megőrzési sort, és a just-in-time tájékoztatóba bizonyítatlan időtartamot írhat. Az activity a DPO-döntés előtt is megnyílhat.
- **Javaslat:** A Z.3:61 vegye át szó szerint az LMS-Z-06 BS-D6-os mondatát (MAN:108). Javítási korlát: megőrzési sort választani tilos. A Program terv §4 nyitási feltétele marad. A DPO-döntés maga meglévő nyitott kapu (BS-D6), ez a finding nem nyit újat.
- **Típus:** objektív · **Verdikt:** —

**BIZT-G1-4**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.4:98 (LÉPÉS 1), Z.4:329 (leírás), Z.4:307 (fejlesztői feltétel). Fájlközi: ADV §3 build-rész:117 (ASSIGN-S sor), ADV:109 (BIZT-2), ADV §11:245.
- **Probléma:**
  - A Z.4 kétszer abszolút ígéretet tesz: „csak a kijelölt mentorod vagy értékelőd látja”. Ez az írott reflexióra és a videóra is vonatkozik.
  - Az ASSIGN-S profilban a Moodle-alapértelmezés szerint a nem szerkesztő tanár, a szerkesztő tanár és a menedzser csoporttól függetlenül látja a beadványt.
  - A szűkítés (BIZT-5) és a szélesebb kör elfogadhatósága (BIZT-2) nyitott DPO-kérdés.
  - Rokon minta: M2 BIZT-G1-6. A Z-többlet: a videó (arc, hang) ugyanebbe a körbe esik. A megőrzés itt eldöntött (HUM 9. szakasz: 90 nap).
- **Osztály:** PROJEKT-DÖNTÉS: HUM-PRIV-01, legszűkebb hozzáférés. EMBERI JÓVÁHAGYÁS KELL: BIZT-2 és BIZT-5.
- **Bizonyíték:**
  - Z.4:98: „A beadásodat csak a kijelölt mentorod vagy értékelőd látja, aki a visszajelzést adja.”
  - ADV:117: „| ASSIGN-S, ASSIGN-M, GATE-CP | … nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) |”
- **Hatás:** A kiskorú tanuló a kapott biztosíték alapján ír vagy vesz fel videót a változásáról és a határairól, miközben a tényleges olvasói kör szélesebb lehet.
- **Javaslat:** EMBERI DÖNTÉS (DPO, az LMS-gazdával): mi a BIZT-5 és a BIZT-2 válasza az LMS-Z-04-re, a videós utat is beleértve. A tanulói ígéret a HUM-PRIV-01 policy-mondata, ezért addig nem írandó át. Ha a DPO szűkítés nélkül elfogadja a szélesebb kört, a mondatot az ADV §11 „Ki látja?” szövegéhez kell igazítani. Ez meglévő nyitott kapu, új döntést nem nyit.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-5**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.4:117 és :310 (hozzájárulás), Z.4:336 (File submissions: ON), Z.4:278 (beadás), HUB:184. Fájlközi: ADV §6:163 és :171, ADV §9:214.
- **Probléma:** A videós út feltétele, hogy kiskorúnál a tanuló és a gondviselő együtt hozzájáruljon. A Z.4 azonban sehol nem mondja meg:
  - hol és hogyan rögzül ez a hozzájárulás;
  - ki ellenőrzi a feltöltés előtt;
  - kell-e hozzá egyáltalán file-beadás, holott a fájlfeltöltés mindenkinek be van kapcsolva.

  Hiányzik az a kikötés is, hogy a felvételen más ne szerepeljen, főleg gyerek. Hiányzik az is, hogy a saját eszközön maradt példányt törölni kell. Az ADV §6 ezeket a fotóra rögzíti, videóra nem. A gondviselői folyamat a HUM-PRIV-02-höz tartozik, az ADV §9 szerint lezáratlan.
- **Osztály:** PROJEKT-DÖNTÉS: HUM-PRIV-02, vagyis a hozzájárulás adója és a 90 nap. TÉNY: a beállítás mindenkinek megnyitja a feltöltést. EMBERI JÓVÁHAGYÁS KELL: a hozzájárulás folyamata és a fotószabály alkalmazása videóra.
- **Bizonyíték:**
  - Z.4:336: „File submissions: **ON**, max 1 file, max size 100–200 MB (opcionális videós út).”
  - ADV:171: „A gondviselői hozzájárulás folyamata is a **HUM-PRIV-02**-höz tartozik.”
- **Hatás:** Egy 15–17 éves tanuló videója hozzájárulás nélkül is a Moodle-be kerülhet, akár más személlyel a képen. A saját telefonján maradt példány megőrzése szabályozatlan.
- **Javaslat:** EMBERI DÖNTÉS (DPO/jogi felelős, HUM-PRIV-02). Kérdések:
  - (a) A hozzájárulás rögzítésének helye és módja; hogy a feltöltés csak rögzített hozzájárulás után nyílik-e.
  - (b) Vonatkozik-e a videóra az ADV §6 fotószabálya: senki más a felvételen, törlés a saját eszközről.

  Javítási korlát: az írásos alapút és a hozzájárulási mondatok maradnak. Új tárolási vagy hozzájárulási folyamatot nem szabad kitalálni.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-6**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.A:45 (2.2 Tér), Z.A:53 (2.3, 1:1), Z.A:54 (feltárás), Z.A:226 (facilitátori tipp), Z.A:412 („Ha van ken-vezető / felelős jelen”), Z.A:522 (ellenőrző lista). Fájlközi: GYV §4:64, §4.2.
- **Probléma:**
  - A Z.A biztonsági kerete második felelős felnőttet feltételez. A felkavart résztvevő mellett „ott is egy felnőtt van”, a 1:1 beszélgetés „egy másik felelős tudtával” jöhet létre.
  - A peula viszont csak egy képzőt ír elő, 8–20 fő mellett. A ken-vezető jelenléte feltételes.
  - Rokon minta: M2 BIZT-G3-2 (második felnőtt a peulákon), ezért új döntést nem nyit.
- **Osztály:** PROJEKT-DÖNTÉS: HUM-SAFE-02 és -03. EMBERI JÓVÁHAGYÁS KELL: a peulai felnőttlétszám.
- **Bizonyíték:**
  - Z.A:45: „felkavart résztvevőt nem küldünk ki egyedül, ott is egy felnőtt van vele.”
  - Z.A:412: „Ha van ken-vezető / felelős jelen, ő is mondhat 1–2 mondatot”
- **Hatás:** Egyetlen képzőnél a felkavart résztvevő kísérése vagy egy feltárás kezelése felügyelet nélkül hagyja a kvucát. Ha a képző marad, a résztvevő marad egyedül.
- **Javaslat:** EMBERI DÖNTÉS (a Memuna és a programvezető, az M2 BIZT-G3-2-vel együtt): kötelező-e a második felnőtt a Z.A-n. Ha nem, mi a felkavart résztvevő és a feltárás útja egy képzővel. Javítási korlát: a 2.2, a 2.3 és a 4.2 biztonsági mondatai nem gyengíthetők.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-7**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** Z.4:398 (`Show analysis page`). Fájlközi: ADV §3 build-rész:119 (FEEDBACK-N sor), HUM:170 (HUM-PRIV-03, implementáció).
- **Probléma:**
  - A Z.4 a `Show analysis page` értékét a HUM-PRIV-03 gazdájára bízza, a kockázatot viszont nem nevezi meg.
  - Ha az érték „Yes”, a tanulók az elemzőoldalon minden más résztvevő szabad szöveges válaszát szó szerint látják: a 2. kérdés kísérő mezőjét és az 5–7. kérdést.
  - Az ADV FEEDBACK-N sora a tanulói láthatóságot nem rögzíti. Elsődleges forrás: a Moodle kódja. Az alapérték „No”, mert `selectyesno`, és `setDefault` nincs.
- **Osztály:** TÉNY: a Moodle kódja. PROJEKT-DÖNTÉS: HUM-PRIV-03. EMBERI JÓVÁHAGYÁS KELL: a beállítás értéke.
- **Bizonyíték:**
  - Moodle `MOODLE_405_STABLE`, `mod/feedback/item/textarea/lib.php` (`print_analysed`): „foreach ($values as $value) { … echo str_replace("\n", '<br />', $value->value);”
  - docs.moodle.org, Feedback settings: „Choose whether to show students the analyis page or only show to teachers.”
- **Hatás:** Egy kiskorú tanuló „legnehezebb rész” válasza a teljes képzős csoport elé kerülhet. Ebben feltárás is lehet (lásd BIZT-G1-2).
- **Javaslat:** EMBERI DÖNTÉS (DPO és programvezető, HUM-PRIV-03): a `Show analysis page` értéke. Ha „Yes”, kell-e ehhez tanulói tájékoztató mondat. Javítási korlát: az értéket a repó nem választja meg. A kanonikus „név nélkül jelennek meg” mondat nem változik.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:**
  - Z.1:13 (completion: a SLIDE 1 és a SLIDE 3 reflektív választója);
  - Z.2:13 (completion: a SLIDE 1, 3 és 4); Z.2:236–240 (kudarcélmény, „nem szeretnék most erre gondolni”);
  - Z.3:121–127 („félek bármit ígérni”), Z.3:333.

  Fájlközi: ADV §5:150, ADV build-rész:115 (H5P-C), HUM:556, :561, :562 (D-d, D-i, D-j).
- **Probléma:**
  - A Z.1 és a Z.2 completion-elemként sorolja fel a helyes válasz nélküli, érzelmi állapotot rögzítő választókat. Emiatt ezek követéssel, fiókhoz kötve tárolódnak, és a tanári szerepek próbálkozás-riportjában látszanak.
  - Az ADV §5 a saját önreflexiót csak konkrét pedagógiai szükségnél engedi mentor-láthatóvá tenni.
  - A D-d és a D-i elvét („pontozatlan választó nem completion-elem”) a projektgazda csak megnevezett elemekre terjesztette ki. A Z.1–Z.3 nincs köztük.
  - Lehetséges átfedés az implementációs lencse completion-findingjával; itt az adatvédelmi oldal a többlet.
- **Osztály:** TÉNY: a completion-listák. PROJEKT-DÖNTÉS: ADV §5, D-d, D-i, D-j. EMBERI JÓVÁHAGYÁS KELL: a kiterjesztés a Z-re.
- **Bizonyíték:**
  - Z.2:13: „a választós interakciók érdemi megválaszolása (az LMS-Z-02 H5P-C profilja): SLIDE 1, SLIDE 3 és SLIDE 4 Single Choice.”
  - ADV:150: „**saját önreflexió:** ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség.”
- **Hatás:** Kiskorú tanulók érzelmi önbevallása („kudarc”, „félek”) név szerint tárolódik és látható, olyan cél nélkül, amelyet a kánon megnevezne.
- **Javaslat:** EMBERI DÖNTÉS. Kérdések:
  - (a) A projektgazdától: kiterjed-e a D-d/D-i elve a Z.1 SLIDE 1 és 3, a Z.2 SLIDE 1, 3 és 4, valamint a Z.3 SLIDE 1 és 7 választóira.
  - (b) A DPO-tól, a D-j mintájára: elfogadható-e e válaszok fiókhoz kötött tárolása.

  Javítási korlát: a completion-listák és az RA 14. pont szerinti típusválasztás a döntésig nem változik.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** Z.A:55 (az M0.A plakát és az idézetek), Z.A:204 (kifüggesztés), Z.A:405 (névhúzás: névcetlik), Z.A:459–462 (szófelhő), Z.A:316 (posztermunka). HUB:140. Fájlközi: HUM:149 és :151 (HUM-PRIV-02), ADV §3:67, M0.A:366.
- **Probléma:**
  - A HUM-PRIV-02 implementációs sora a Z.A-t név szerint a központi felvételi és kézírás-szabályra hivatkozó activityk közé sorolja. A Z.A-ban ilyen hivatkozás nincs.
  - A Z.A nem mondja meg, mi lesz a peula után:
    - az egész féléven át őrzött M0.A „mitől félek” plakáttal;
    - a képző saját jegyzetéből készült idézetekkel;
    - a névcetlikkel, a poszterekkel és a szófelhővel.
  - Arról sem szól, szabad-e őket lefotózni.
  - A Z.A a megőrzés kijelölt célpontja; a cél itt teljesül. Rokon minta: M1 BIZT-G3-8.
- **Osztály:** TÉNY: a hivatkozás hiányzik. PROJEKT-DÖNTÉS: HUM-PRIV-02. EMBERI JÓVÁHAGYÁS KELL: melyik megőrzési sor vonatkozik a plakátokra és a cetlikre.
- **Bizonyíték:**
  - HUM:149: „központi média-/felvételi szabály, amelyre minden médiaaktivitás hivatkozik (pl. M0.A, M1.A, M4.A–M4.B, M5.A, M6, Z.A, a Z.4 videós útja)”
  - Z.A:405: „Mindenki nevét írjátok fel külön kis cetlire, tegyétek egy tálba / kalapba”
- **Hatás:** Kézírásos, félelmeket és neveket tartalmazó papírok a cél teljesülése után határidő nélkül a stáb-dossziéban maradhatnak, vagy egy résztvevő telefonjára kerülhetnek.
- **Javaslat:** EMBERI DÖNTÉS (DPO/jogi felelős, HUM-PRIV-02): a Z.A után az M0.A plakátra, a képzői idézetekre, a névcetlikre és a Z.A plakátjaira a „kézírásos plakát” sor, a „név nélküli papír munkalap” sor (30 napon belüli megsemmisítés) vagy visszaadás vonatkozik-e. A döntés után a HUM-PRIV-02 hivatkozás és a sor átvezetése a Z.A-ba objektív. Javítási korlát: a 2.3 kitakarási kikötése marad. Új tárolási szabályt nem szabad kitalálni.
- **Típus:** emberi-döntés · **Verdikt:** —

**BIZT-G1-10**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** Z.1:453 és Z.2:46 (vétó/QA: a DPO és a Memuna), Z.3:57 (BS-D8, a Memuna vétója), HUB:170, :207–208, Z.A 4.2 (HUM-SAFE-02/03), Z.4:402 (HUM-PRIV-03). Fájlközi: HUM:73 (HUM-SAFE-03: Z.2, Z.3, Z.A, a Z hub 5. szakasza), RTA:132, :141, :144, :145, :153, ADV:216, GYV §6:151, RELEASE-READINESS G1, G2, G3b.
- **Probléma:**
  - A Z biztonsági és adatvédelmi megoldásai lezárt döntéseken alapulnak: D-2, D-3, BS-D8, HUM-SAFE-02/03, HUM-PRIV-01–03.
  - A megnevezett szerepek írásos bizonyítéka hiányzik:
    - a DPO QA-ja a D-2-re és a D-3-ra;
    - a Memuna QA-ja a Z.1/Z.2 veszély-dobozára, a Z.3 biztonsági lépésére (BS-D8-vétó) és a Z-beli HUM-SAFE-03-implementációkra;
    - a DPO, jogi signoff.
  - Az RT-P0-03, -12, -15, -16 és -24 állapota `IMPLEMENTATION_TEST_REQUIRED`.
- **Osztály:** PROJEKT-DÖNTÉS: a megvalósítási döntések. A szerepköri bizonyíték hiánya TÉNY.
- **Bizonyíték:**
  - RTA:153: „| RT-P0-24 | `IMPLEMENTATION_TEST_REQUIRED` | 24. Tanuló-lokális szöveges lépések |”
  - ADV:216: „- [ ] privacy/DPO/jogi signoff bizonyítéka rögzítve.”
- **Hatás:** Élesben bizonyítatlan marad, hogy a Z.1/Z.2 szöveges lépései nem tárolódnak, hogy a Feedback név nélkül jelenik meg, és hogy a mentor-láthatóság a tervezett.
- **Javaslat:** Nem javítható. Megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő. A kapuk:
  - G1 (#1): a Memuna;
  - G2 (#2): a DPO;
  - G3b (#3): az RT-P0-03, -12, -15, -16 és -24 a célverzión.

  Semmit ne jelölj megoldottnak.
- **Típus:** bizonyíték-kapu · **Verdikt:** —

---

**Hipotézisek, biztonsági szemmel:**
- **N-Z-07:** nem biztonsági-jogi kérdés. A tartalékút a tanuló-lokális M0-mondat miatt indokolt; a pedagógiai lencse dönti el.
- **N-Z-03:** a Z.3 szövege nem ellentétes a kánonnal; biztonsági finding nincs.
- **N-Z-09:** nem jelentem. A Z szövegében nincs AI-feladat, és nincs olyan mondat, amely AI-használatra utalna a mentor által olvasott szövegnél. Az ADV §7 és §11 kurzusszintű AI-szabálya érvényes. Szövegszerű kétség nélkül nem nyitok új döntést.

NINCS TÖBB (10 finding, a cap pontosan kitelt; LEVÁGVA-sor nincs, mert ennél több findingom nincs).

Sources:
- [Moodle source, MOODLE_405_STABLE: mod/feedback/item/textarea/lib.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/feedback/item/textarea/lib.php) (elsődleges)
- [Moodle source, MOODLE_405_STABLE: mod/feedback/mod_form.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/feedback/mod_form.php) (elsődleges)
- [MoodleDocs 4.5: Feedback settings](https://docs.moodle.org/405/en/Feedback_settings) (elsődleges)

## ERT-G1 — értékelés, hub, Z.1–Z.4, Z.A

Értékelési lencse (D1, D3), Z modul, G1 csoport (hub, Z.1–Z.4, Z.A). 8 findingot találtam: 4 P1 és 4 P2. Típus szerint 3 objektív és 5 emberi döntés. A tananyaghoz nem nyúltam.

Fájlrövidítések:
- HUB = `02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md`
- Z.1 = `02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md`
- Z.2 = `02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md`
- Z.3 = `02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md`
- Z.4 = `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md`
- Z.A = `02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md`
- MAN = `02 Tervezet/LMS – activity manifest.md`
- PT = `02 Tervezet/Program terv.md`
- HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`
- RA = `02 Tervezet/LMS – H5P runtime acceptance.md`

---

**ERT-G1-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés (D1, D3)
- **Hely:**
  - HUB:185–189 (Minimum elvárás), :217, :219 (§6)
  - Z.4:343, :345, :347, :353
  - ↔ MAN:111 (LMS-Z-08), :19 (ASSIGN-S „Grade / pass”), :173
  - ↔ HUM:457 („Üres sablon”); PT:259
- **Probléma:** A Z.4 „Teljesítve” döntésére három különböző mérce szól, és ezek nem egyeztethetők össze:
  - (a) A HUB:185–189 és a Z.4:345 címe a hármas minimumot teszi a „Teljesítve” feltételévé: legalább 3 pillanat, mindegyiknél az, hogy miért fontos; 2–3 mondat a szemléletváltozásról; legalább egy határidős lépés, és hogy kinek mondja el.
  - (b) A MAN:111 és a Z.4:343 csak „tényleges, minimálisan értelmezhető tartalmat” kér. A HUM:457 ezt alsó határként rögzíti, nem a minimum helyett.
  - (c) A Z.4:347 ugyanezt a minimumot tanácsnak minősíti („érdemes szem előtt tartani”), a :353 pedig harmadik, megfigyelhető kritérium nélküli küszöböt vezet be („nagyon hiányos / alibi”). A HUB §6 a hiányos produktumot elemzési jelzésként kezeli, nem „Még nem teljesítve” értékként.
  - A MAN:173 csak az M2 és az M4 rubrikaküszöbét mondja ki formatívnak, a Z-ét nem, ezért a kérdés a kánonból nem dönthető el.
- **Bizonyíték:**
  - Z.4:345/:347 „Minimum elvárás a „Teljesítve”-hez” · „de ezeket érdemes szem előtt tartani:”
  - MAN:111 „„Teljesítve” = az LMS-Z-04 legutóbb leadott reflexiójának előírt mezőiben tényleges, minimálisan értelmezhető tartalom van”
- **Hatás:**
  - Ugyanaz a beadás (például 1 pillanat, határidő nélküli lépés) az egyik mentornál „Teljesítve”, a másiknál „Még nem teljesítve” lesz.
  - A K1 („legalább 3 pillanat”) és a K3 („időben behatárolt” lépés) egyetlen mérése a Z.4. A MAN szerinti mércével ezek elsajátítás nélkül is teljesülnek.
  - Az LMS-Z-08 a kurzusteljesítés kritériuma (MAN:165), ezért az egyenetlenség az online félév teljesítését is érinti.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős; vétó/QA: programvezető) a két lehetőség közül:
  - (a) A HUB/Z.4 minimuma az LMS-Z-08 „Teljesítve” feltétele. Ekkor a MAN:111 és a Z.4:343/:347/:353 igazodik hozzá, a „Még nem teljesítve” pedig a hiányzó minimumelemhez kötődik.
  - (b) A minimum formatív visszajelzés, mint az M2-nél és az M4-nél (MAN:173). Ekkor a HUB:185–189 és a Z.4:345 címe igazodik, és a „Még nem teljesítve” csak üres vagy értelmezhetetlen beadásnál jár.
  - Javítási korlát: a döntésig a minimum szövege, a címkepár és az 1 normál + 1 javító beadás nem változik; a `/course-fix` ne válasszon. Az ERT-G1-2 javítása ezt a döntést nem előlegezheti meg.
- **Típus:** emberi-döntés
- **Verdikt:** —

**ERT-G1-2**
- **Súlyosság:** P1
- **Bizalom:** magas (a skálasorrend-kockázatnál közepes)
- **Lencse:** értékelés (D3)
- **Hely:**
  - HUB:199 (§5, 3. pont)
  - Z.4:340–341, :343
  - ↔ MAN:110–111 (LMS-Z-04, LMS-Z-08), :163, :165, :25 (GATE-CP), :191
  - Minta: M4 ERT-G1-2 (objektív)
- **Probléma:** A Z egyetlen fájlja sem említi az LMS-Z-08 megerősítő checkpointot (Grep: 0 találat a Z mappában a „Z-08”-ra). Ebből három hiba következik:
  - (a) A HUB §5 3. pontja szerint a Z-hez elég a „leadott” reflexió, holott a MAN:163 a leadás mellett az LMS-Z-08 = „Teljesítve” értéket is megköveteli (BSPEC-07, D-h).
  - (b) A Z.4:343 elavult kódolási alternatívákat ad. A „kézi megerősítés” éppen az, amit a GATE-CP tilt, mert így a bukó érték a kurzusteljesítésben teljesítettnek számítana.
  - (c) A Z.4:341 a skálát „Teljesítve / Még nem teljesítve” sorrendben adja meg, a GATE-CP viszont kötött sorrendet ír elő (1. „Még nem teljesítve”, 2. „Teljesítve”). A MAN:191 szerint a skála címkéit a Z.4 adja.
- **Bizonyíték:**
  - HUB:199 „3. Z.4 leadott záró reflexió + benne a következő lépés(ek)” · Z.4:343 „(értékeléshez kötött completion vagy kézi megerősítés)”
  - MAN:25 „egyedi skála pontosan két elemmel, ebben a sorrendben: 1. „Még nem teljesítve”, 2. „Teljesítve”” ↔ Z.4:341 „`Teljesítve / Még nem teljesítve`”
- **Hatás:**
  - A Z.4 szerint dolgozó mentor csak az Assignmentet értékeli, így az LMS-Z-08 üres marad, és az online félév teljesítése (MAN:165) senkinél nem áll be. Ha pedig kézzel állítja „complete”-re, kijátssza a GATE-CP védelmét.
  - Ha a skála a Z.4 sorrendjével készül, a „Grade to pass = 2” mellett a „Még nem teljesítve” lesz „complete, pass”. Ez hamis completion.
- **Javaslat:** A MAN szövegének szó szerinti átvezetése (BSPEC-07, D-h):
  - HUB:199: egészüljön ki a MAN:163 fordulatával: „az LMS-Z-04 leadásával és az LMS-Z-08 = „Teljesítve” értékkel (BSPEC-07)”.
  - Z.4:343 második mondata: két külön állapot. A leadás (SUBMITTED) a `completionsubmit`; a megerősítést (CONFIRMED) a kijelölt mentor/értékelő az LMS-Z-08-ba írja „Teljesítve” vagy „Még nem teljesítve” értékkel; a checkpoint completionjét kézzel nem írja felül (MAN §1 GATE-CP).
  - Z.4:341: a címkesorrend a MAN:25 szerint, alacsonytól a magasig: „Még nem teljesítve”, „Teljesítve”.
  - Javítási korlát: a „Teljesítve” tartalmi feltétele (ERT-G1-1), a címkepár és az 1+1 beadás nem változik. Az Assignment saját skálájának (Z.4:340) megtartása implementációs kérdés, nem része ennek a javításnak.
- **Típus:** objektív
- **Verdikt:** —

**ERT-G1-3**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés (D3)
- **Hely:**
  - HUB:193, :198 (§5 „Minimális teljesítés”, 2. pont)
  - ↔ MAN:163, :165, :110, :133
  - ↔ PT:211–213
- **Probléma:** A hub a Z.A záró peulán való részvételt a Z teljesítésének feltételei közé sorolja. A Program terv Z-sora, a manifest §4 Z-sora és a kurzusteljesítés kritériumai között viszont nincs ott. Jelenléti checkpoint sem létezik: az LMS-Z-04 a Z.A után dátummal nyílik, nem jelenléttel. A hiányzóknak nincs pótlási útja.
- **Bizonyíték:**
  - HUB:198 „2. Z.A záró peula (offline).” (a :193 „Minimális teljesítés (a Z modul teljesítése)” alatt)
  - MAN:163 „Z | Z.1–Z.4 (… az LMS-Z-04 leadásával és az LMS-Z-08 = „Teljesítve” értékkel …) + a Z.3 mentori elfogadása … + Moodle Feedback”
- **Hatás:**
  - A hub szerint dolgozó képző a Z.A-ról hiányzót teljesítetlennek tekinti, a Moodle viszont teljesítettnek jelzi. Vagy fordítva: a hub feltétele csendben kiesik.
  - A programteljesítés feltétele dokumentumonként más.
- **Javaslat:** EMBERI DÖNTÉS (programvezető + értékelési felelős):
  - (a) A Z.A-részvétel completion-feltétel. Ekkor a manifestbe jelenléti elem kell, és a hiányzóknak pótlási út (új completion-döntés).
  - (b) Ajánlott lépés. Ekkor a HUB:195–199 2. pontja a PT:213 és a MAN:163 szerint ajánlásként fogalmazódik át.
  - Javítási korlát: a Z.4 és a Feedback Z.A utáni, dátumos nyitása (MAN:110, :112) nem változik. A Z.A-ról hiányzók Z.4-es felidéző útja a PED-G1-3-hoz tartozik.
- **Típus:** emberi-döntés
- **Verdikt:** —

**ERT-G1-4**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés (D1, D3)
- **Hely:**
  - HUB:62 (K5), :200
  - Z.4:372–393, :403
  - ↔ MAN:22 (FEEDBACK-N), :24 (TEXT-C), :112
  - ↔ RA:86 (16. pont)
- **Probléma:** A képzési visszajelzés completionje a beküldés („mark as complete when submitted”), de egyik kérdés sincs „Required”-ként előírva, a kísérő szöveges kérdés pedig kifejezetten opcionális. A manifest maga mondja ki, hogy üres beküldést csak a „Required” kérdés zár ki. Így a K5 („kitölti a visszajelző űrlapot”) completionje üres űrlappal is megszerezhető. Az RA 16. pontja ezt az esetet nem teszteli.
- **Bizonyíték:**
  - Z.4:403 „**Activity completion:** mark as complete when submitted.”
  - MAN:24 „a „Required” kérdés miatt üres beküldés nem lehetséges” (a TEXT-C profilnál; a FEEDBACK-N profilnál nincs ilyen kikötés)
- **Hatás:**
  - A részvételi cél (K5) és a Z completion visszajelzés nélkül teljesül, a „kitöltési arány” analitika (HUB:215) torz lesz.
  - Nem javaslok P0-t, mert a K5 kifejezetten részvételi cél, tartalmi mérés vagy biztonsági tudás nem épül rá.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős; vétó/QA: DPO + programvezető, HUM-PRIV-03): legyen-e legalább egy „Required” kérdés (például az 1. Likert-kérdés), vagy a „kitöltés ténye” az üres beküldést is jelenti. Utóbbi esetben a HUB:62 és a :200 pontosítandó.
  - Javítási korlát: a kérdések szövege, a név nélküli megjelenítés, a HUM-PRIV-03 tanulói mondata és a pontozás hiánya nem változik.
- **Típus:** emberi-döntés
- **Verdikt:** —

**ERT-G1-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés (D3)
- **Hely:**
  - Z.1:13, :335, :374–382 (SLIDE 4)
  - ↔ RA:81–82 (14. pont)
  - Minta: M2 ERT-G2-3 (objektív), M4.3:398
- **Probléma:** A SLIDE 4 a pontozott emlékeztető kérdéseket Single Choice Setként írja elő, közben kérdésenként tanító visszajelzést ad a téves válaszra. A lecke maga is elismeri, hogy a Single Choice Setnek nincs ilyen mezője; csak a tesztre hivatkozik, a típust nem rendezi.
- **Bizonyíték:**
  - Z.1:335 „Egyszerű **Single Choice Set** (3–5 kérdés, egymás után).”
  - Z.1:382 „A Single Choice Setben nincs kérdésenkénti visszajelző mező (csak pontsávos összesítő visszajelzés)”
- **Hatás:** Az előírt típus mellett a hibázó tanuló csak pontsávot lát. A :378–381 újratanító mondatai (például a „Johari-ablak és az SBI az M1-ben volt…”) nem jelennek meg, így a lecke egyetlen pontozott eleme visszajelzés nélküli lesz.
- **Javaslat:** Az M2 ERT-G2-3 mintája szerint a :13 és a :335 típusa: Multiple Choice egyválaszos módban, kérdésenként, „Randomize answers” bekapcsolva. Ha a build-gazda megtartja a Single Choice Setet, legalább az M4.3:398 fejlesztői megjegyzése kerüljön át szó szerint a :382 helyére.
  - Javítási korlát: a kérdések, az opciók, a ✅-ok, a visszajelzések és a SLIDE 4 completion-szerepe nem változik.
- **Típus:** objektív
- **Verdikt:** —

**ERT-G1-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés (D3)
- **Hely:**
  - Z.1:13, :57
  - Z.2:13, :63
  - Z.3:5–23 (nincs completion-sor), :59
  - ↔ MAN:16 (H5P-C), :105–107
  - ↔ HUM:556 (D-d), :561 (D-i)
  - ↔ `01 Fejlesztés/04 Audit/2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`:54–56
  - Rokon: M0 IMPL-3 (X-6)
- **Probléma:**
  - A Z.1 és a Z.2 lecke-completionje helyes válasz nélküli, reflektív választókra épül. A Z.2-é kizárólag ilyenekre (SLIDE 1, 3, 4), a Z.1-é részben (SLIDE 1 és 3).
  - A D-d/D-i elve szerint a pontozatlan választás nem gate-elheti a lecke-completiont. A D-i ezt csak az M0.3-ra és az M2.2-re terjesztette ki név szerint.
  - A Z.3-nak nincs completion-sora, holott a H5P-C profil a forrásban előírt interakciót kéri.
  - A BSPEC-06 hatóköri besorolása a Z-01…03-at „pontozott interakciókkal” sorolta be, de a Z.2-ben és a Z.3-ban nincs pontozott interakció.
- **Bizonyíték:**
  - Z.2:13 „a választós interakciók érdemi megválaszolása (az LMS-Z-02 H5P-C profilja): SLIDE 1, SLIDE 3 és SLIDE 4 Single Choice.”
  - HUM:561 „a választás önmagában nem gate-elheti a Moodle lecke-completiont”
- **Hatás:** A Z.2 és a Z.3 completionje vagy olyan elemekre épül, amelyeket egy lezárt döntés elve kizár, vagy határozatlan. A Z.1–Z.3 completion a Z és az online félév teljesítésének része.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős + projektgazda; az M0 IMPL-3 / X-6 döntési csomagjába, nem külön):
  - Kiterjed-e a D-d/D-i elve a Z.1 SLIDE 1/3, a Z.2 SLIDE 1/3/4 és a Z.3 SLIDE 1/3/7 választóira (ez a lezárt döntés új alkalmazási esete)?
  - Ha igen, mi a Z.2 és a Z.3 completion-eleme pontozott interakció nélkül? A Z.3 a döntés szerint kapjon completion-sort.
  - Javítási korlát: a választók, az opciók, a visszajelzések, a D-2/D-3, a Z.1 SLIDE 4 szerepe és a „Hide summary slide” beállítás döntés nélkül nem változik.
- **Típus:** emberi-döntés
- **Verdikt:** —

**ERT-G1-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés (D3)
- **Hely:**
  - Z.4:338–339
  - Z.3:57, :302
  - HUB:33
  - ↔ MAN:109 (LMS-Z-07, schedule „—”), :149, :229, :249
  - ↔ HUM:482
- **Probléma:** A Z javítási útjának nincs időpontja:
  - A Z.4 javító beadása a „Még nem teljesítve” után automatikusan nyílik, de a megerősítés a Z-határidő utáni napon van. A javító beadás idejét a MAN:249 csak az M2-re és az M4-re rendezi („a képző jelöli ki”).
  - A Z.3 mentori elfogadásának (LMS-Z-07) és az elutasítás utáni újrabeküldésnek nincs határideje.
  - A HUB:33 csak az M6 és az M7 javítását várja be.
- **Bizonyíték:**
  - MAN:249 „**Puha kapunál (M2, M4)** a javító beadás idejét a képző jelöli ki; ehhez nincs központi dátum.”
  - Z.4:339 „a Z completion határideje 18:00, a központi naptár szerinti napon … az eredmény megerősítése: a következő napon.”
- **Hatás:** A csütörtökön „Még nem teljesítve” értéket kapó vagy a Z.3-ban későn elutasított tanulónál a javítás a határidő után már nem kiszámítható. Az online félév teljesítésének nincs meghatározott végpontja, a javító út csak papíron létezik.
- **Javaslat:** EMBERI DÖNTÉS (programvezető, HUM-OPS-01): a MAN:249 puha kapus szabálya („a képző jelöli ki”) kiterjed-e a Z.4 javító beadására és a Z.3 újrabeküldésére, vagy központi pont kell (`SCHEDULE_TO_RESYNC`). Kell-e határidő az LMS-Z-07 mentori elfogadására?
  - Javítási korlát: az 1 normál + 1 javító, az automatikus nyitás és a BS-D8 lánc nem változik; dátumot nem találunk ki.
- **Típus:** emberi-döntés
- **Verdikt:** —

**ERT-G1-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés (D1)
- **Hely:**
  - Z.2:17–19 (mikrocél)
  - ↔ Z.2:240 (SLIDE 4 harmadik opció), :307 (SLIDE 6)
  - HUB:83
- **Probléma:** A tanulói mikrocél a „mit mond ez rólad” önfeltárást a lecke céljává teszi. A lecke maga (:307) és a hub (:83) viszont alternatív kérdést ad, és kimondja, hogy a teljesítéshez nem kell érzékeny önfeltárás. A cél és a feladat nem illeszkedik.
- **Bizonyíték:**
  - Z.2:18 „meg tudod nevezni, **volt-e olyan modul, amit nehéznek éltél meg és mit mond ez rólad**,”
  - Z.2:307 „A teljesítéshez nem kell érzékeny önfeltárás”
- **Hatás:** Aki a lecke saját, a HUM-SAFE-03 passzjogát tiszteletben tartó alternatíváját választja, a kimondott cél szerint nem érte el a célt, és a cél kötelező önfeltárást sugall.
- **Javaslat:** A :18 kapja meg a :307 alternatíváját szó szerint, például: „…és mit mond ez rólad (vagy azt, milyen támogatás vagy tanulási forma segít neked, és mit próbálsz ki legközelebb)”.
  - Javítási korlát: a SLIDE 6 szövege, a HUB:83 és a mikrocél másik két eleme nem változik.
- **Típus:** objektív
- **Verdikt:** —

---

**Egyéb megjegyzések:**
- **Átfedés a PED-G1-gyel:** nem ismételtem meg a következőket:
  - a Z.3 7. diájának „lépj vissza 1–2 diát” visszajelzését és az 5. dia mezőjét (PED-G1-2);
  - a Z.3 mentori elfogadásának támogatóköri ellentmondását (PED-G1-5);
  - a Z.A-ról hiányzók Z.4-es felidézését (PED-G1-3);
  - a HUB:33 Z-nyitási mondatát (PED-G1-1).
- **Kulcsellenőrzés:** a Z.1 SLIDE 4 négy kulcsa a modulcímek és a hub szerint helyes. A Z.4 visszajelző űrlapjának „3 ígéret” tétele egyezik a PT:221 M0.1-es ígéreteivel.
- **Anna-hipotézisek:** egyiket sem vettem fel értékelési findingnak.
  - N-Z-07: P3, nem értékelési kérdés; a tartalékút indokolt.
  - N-Z-03: nincs kánonnal ellentétes szöveg.
  - N-Z-09: D8, a biztonság-jog lencséé.
  - Az M0 NYELV-G2-18 Z.A-helyeit nem ismételtem.

## IMPL-G1 — implementáció, hub, Z.1–Z.4, Z.A (1. rész)

Implementációs lencse, Z modul, G1. Ez read-only review volt, fájlt nem szerkesztettem. A pilot-besorolást szándékosan kihagytam.

Rövidítések (abszolút utak):
- HUB = 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- Z.1 = 02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md
- Z.2 = 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md
- Z.3 = 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- Z.4 = 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md
- MAN = …/02 Tervezet/LMS – activity manifest.md
- RA = …/02 Tervezet/LMS – H5P runtime acceptance.md
- ADV = …/02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- A11Y = …/02 Tervezet/LMS – hozzáférhetőségi sztenderd.md
- PD = …/02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md
- PT = …/02 Tervezet/Program terv.md

---

**IMPL-G1-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.4:338, :340–341, :343; HUB:185, :199 ↔ MAN:19 (ASSIGN-S), :25 (GATE-CP), :110 (LMS-Z-04), :111 (LMS-Z-08), :163, :165, :191; RA:39, :92
- **Probléma:** A Z.4 és a hub még a BSPEC-07 előtti, egyállapotú modellt írja le.
  - A Z.4 szerint a leadás nem completion, a kódolást pedig két út között nyitva hagyja.
  - A lezárt BSPEC-07 szerint viszont az LMS-Z-04 saját completionje maga a leadás (SUBMITTED). A megerősítés a külön LMS-Z-08 GATE-CP sorban van (CONFIRMED).
  - Az LMS-Z-08 a Z egyik fájljában sem szerepel. A hub minimális teljesítése (:199) sem említi.
  - A skála sorrendje is fordított.
- **Bizonyíték:** Z.4:343 „a puszta leadás … önmagában nem completion. A Moodle-beli kódolást (értékeléshez kötött completion vagy kézi megerősítés) az … LMS-Z-04 sora rögzíti.” · MAN:110 „SUBMITTED: a reflexió leadva (`completionsubmit`); CONFIRMED: LMS-Z-08”
  Z.4:341 „`Teljesítve / Még nem teljesítve`” ↔ docs.moodle.org/405 Scales: „You must order the comma separated elements in increasing order of value.”
- **Hatás:**
  - Aki a Z.4 alapján épít, nem tölti ki az LMS-Z-08-at. A kurzusteljesítés kritériuma az LMS-Z-08 „complete, pass” állapota (MAN:165), így az online félév és a program teljesítése nem áll be (hamis nem-teljesítés).
  - Fordított esetben csak az LMS-Z-08 kap értéket. Ekkor a „Még nem teljesítve” utáni automatikus javító beadás (Z.4:338; MAN:149, lezárt) nem nyílik meg. Ok: docs.moodle.org/405 Assignment settings: „Automatically until pass (after grading, until the student achieves the passing grade)”.
  - Ha a skálát a Z.4:341 sorrendjében hozzák létre, a „Teljesítve” lesz a legalacsonyabb érték.
- **Javaslat:**
  - (a) A Z.4:343 helyére a MAN:110 és :111 két állapota kerül, szó szerint, a tartalmi minimummal.
  - (b) A Z.4 §4 és a HUB:199 3. pontja kimondja, hogy a mentor az LMS-Z-08-ba írja a „Teljesítve” / „Még nem teljesítve” értéket (MAN:163).
  - (c) A Z.4:341 sorrendje a GATE-CP szerint: „Még nem teljesítve”, „Teljesítve” (MAN:25).
  - (d) A Z.4:338 zárójeles hivatkozása a MAN:19 puha kapus mondatára mutasson („a puha kapus beadásoknál (… LMS-Z-04) 1 normál + 1 javító beadás automatikusan”). A mostani „újrabeadás engedett” fordulat a Peula v1-é.
  - Az automatikus újranyitáshoz az LMS-Z-04-et is értékelni kell (saját skála, „Automatically until pass”), vagyis a mentor kétszer ír be. Ha a verifier ezt új munkafolyamatnak ítéli: EMBERI DÖNTÉS, a projektgazdától mint build-spec gazdától.
  - Nem változik: az 1+1 beadás, a Z.4:349–351 minimuma, a puha kapu, a BSPEC-07.
  - Rokon minta: M1:IMPL-G2-4 („Allowed attempts”, RT-P0-19).
- **Típus:** objektív
- **Verdikt:** —

---

**IMPL-G1-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.3:217–237 (SLIDE 4), :283–287 (SLIDE 6), :300–306 (biztonsági lépés), :318, :327, :348 (SLIDE 7); Z.4:207 ↔ MAN:108 (LMS-Z-06, unlock: LMS-Z-03), :16 (H5P-C: a grade az összefoglaló dián jön létre), :24 (TEXT-C)
- **Probléma:** A három kötelező mező az LMS-Z-06 TEXT-C activityben van. Ez csak a Z.3 CP completionje, vagyis a SLIDE 7 utáni összefoglaló dia után nyílik meg. A diaszöveg mégis úgy vezet, mintha a tanuló a dián írna:
  - a SLIDE 7 önellenőrzése még meg nem írt célmondatokat nézet át, és visszalépést kér;
  - a biztonsági lépés „a 4. és a 6. dián írtakat” említi;
  - a tanulói szöveg sehol nem nevezi meg a „Z.3 – Szöveges válaszok” activityt;
  - a „Mezőben megjelenő mintaszöveg” Moodle Feedback „Longer text answer” kérdésben nem valósítható meg. A MOODLE_405_STABLE `mod/feedback/item/textarea/textarea_form.php` mezői csak: `required`, `name` (max. 255), `label`, `itemwidth`, `itemheight`; alapérték- vagy placeholder-mező nincs.
- **Bizonyíték:** Z.3:348 „Nyugodtan lépj vissza 1–2 diát, és írd át úgy, hogy **konkrétabb és reálisabb legyen**” · MAN:108 „| LMS-Z-06 | … | TEXT-C | igen | … | LMS-Z-03 |”
  Z.3:236 „Mezőben megjelenő mintaszöveg:”
- **Hatás:**
  - A SLIDE 4-en nincs mező, a SLIDE 7 önellenőrzése üres, a CP-ben való visszalépés semmit nem módosít.
  - A mintaszöveg elvész, vagy a fejlesztő maga dönti el a mezőcímkét (M2:IMPL-G2-7).
  - A Z.4:207 „magadnak elmentett” célmondata közül az első valójában az LMS-Z-06-ban beküldött válasz.
- **Javaslat:**
  - (a) A SLIDE 4, a SLIDE 6 és a biztonsági lépés diaszövegébe egy-egy rövid útbaigazítás kerül a manifest nevével: a válasz a lecke után megnyíló „Z.3 – Szöveges válaszok” activitybe kerül.
  - (b) A :348 visszalépés-mondata a mező kitöltésekor történő pontosításra cserélődik. A :318 és a :302 igeideje és utalása ugyanígy igazodik („a 4. és a 6. dián kért válaszaidat”).
  - (c) A mintaszöveg szó szerint az LMS-Z-06 kérdéscímkéjébe vagy egy előtte álló Label-elembe kerül. Kérdésenként a MAN:108 Megjegyzésében is rögzítendő (M2:IMPL-G2-7 minta).
  - (d) A Z.4:207 a SLIDE 4 mondatánál a beküldött LMS-Z-06-válaszra utal.
  - Ha a projektgazda azt akarja, hogy az önellenőrzés a beírás után legyen (az LMS-Z-06 a CP-vel párhuzamosan nyíljon): az a MAN:108 unlock-cellájának módosítása, EMBERI DÖNTÉS (build-spec gazda).
  - Nem változik: a három kötelező kérdés, a Required-státusz, az LMS-Z-07, a BS-D8.
- **Típus:** objektív
- **Verdikt:** —

---

**IMPL-G1-3**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.3:11, :241–263 (SLIDE 5), :350 (SLIDE 7, opcionális mini szöveges válasz); Z.3:318, :327; Z.4:207 ↔ Z.3:57; MAN:108 („a lecke opcionális mezői nem ide tartoznak”), :308 (BSPEC-02 leltár: tanuló-lokális csak a Z.1 SLIDE 5–6 és a Z.2 SLIDE 5–7)
- **Probléma:** A SLIDE 5 „A következő hónapban…” mondata „Beágyazott kérdés – rövid szöveges válasz” mintaszöveggel. A :11 is beágyazott típusként sorolja.
  - Ugyanez a fájl kimondja, hogy CP-dián szabad szöveges mező nem feltételezhető.
  - Nem tartozik az LMS-Z-06 három kérdése közé, nincs benne a BSPEC-02 leltárban, és nincs kötelező/opcionális besorolása.
  - A SLIDE 7 és a Z.4:207 mégis a két finomítandó célmondat egyikeként kezeli.
  - A SLIDE 7 opcionális mini szövegmezője ugyanilyen.
- **Bizonyíték:** Z.3:260–262 „**Beágyazott kérdés – rövid szöveges válasz** … Mezőben megjelenő mintaszöveg:” · Z.3:57 „**A Course Presentation dián belüli szabad szöveges mező nem feltételezhető:**”
- **Hatás:** A fejlesztő három irányba mehet, és mindegyik rossz:
  - nem támogatott CP-beli mezőt épít (Essay nem kerülhet CP-be);
  - vagy olyan Free Text-szerű elemet, amelynek szövege a próbálkozás-riportba vagy a mentett állapotba kerül (RA 24 nem fedi; megőrzési sora nincs);
  - vagy elhagyja a mezőt, és akkor a Z.4 olyan mondatra épít, amely a tanulónak nincs meg.
- **Javaslat:** EMBERI DÖNTÉS. Gazda: a projektgazda mint build-spec gazda; tárolt útnál a DPO is.
  - Eldöntendő: a SLIDE 5 (és a SLIDE 7 opcionális) szöveges lépés a BSPEC-02 melyik kategóriájába kerül: kötelező tanuló-lokális (mint a D-2/D-3), opcionális tanuló-lokális, vagy negyedik LMS-Z-06 kérdés (akkor megőrzés: BS-D6).
  - A döntés után objektív: a :11 és a :260–263 a választott minta szerint (pl. Z.1:455 „Beviteli elem nincs…”), valamint a MAN:308 leltára és az LMS-Z-03 Megjegyzése.
  - Rokon minta: M3:IMPL-G2-6, M2:IMPL-G1-1.
  - Nem változik: a 4./6./biztonsági lépés kötelező státusza, a mondatkezdés, a példák.
- **Típus:** emberi-döntés
- **Verdikt:** —

---

**IMPL-G1-4**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** Z.4:98, :329 ↔ ADV:117 (ASSIGN-S, GATE-CP), :105–107, :109; RA:85 (15. pont)
- **Probléma:** A tanulói felület azt ígéri, hogy a Z.4 beadást csak a kijelölt mentor vagy értékelő látja.
  - Az ADV §3 szerint a Moodle 4.5 alapbeállításában az értékelői nézetet a nem szerkesztő tanár, a szerkesztő tanár és a menedzser is látja.
  - A csoport szerinti szűkítés „nincs rögzítve” (BIZT-5).
  - Az RA 15. pontja még nem futott.
- **Bizonyíték:** Z.4:98 „A beadásodat csak a kijelölt mentorod vagy értékelőd látja, aki a visszajelzést adja.” · ADV:117 „nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5)”
- **Hatás:** A P2 személyes reflexiót (amelyben a Z.4:201 szerint veszélyjelzés is lehet) a kurzus minden mentora láthatja. A tanulói ígéret így hamis, és a just-in-time tájékoztató (PT §4) pontatlan.
- **Javaslat:** EMBERI DÖNTÉS: DPO. Azonos kapu: M1:BIZT-G2-4, M2:BIZT-G2-3 (BIZT-5, BIZT-2).
  - Választás: technikai szűkítés, vagy a tanulói mondat kiegészítése.
  - A döntésig a mondat nem írható át. A runtime-igazolás az RA 15 (G2, POST-BUILD).
  - Nem változik: a HUM-PRIV-01 legszűkebb hozzáférés elve, a Z.4:201 titoktartási kivétele.
- **Típus:** emberi-döntés
- **Verdikt:** —

---

**IMPL-G1-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.1:13, :335, :374–382 (SLIDE 4) ↔ RA:81 (14. pont); A11Y:83
- **Probléma:** A SLIDE 4 Single Choice Set, miközben négy kérdésenkénti rossz-válasz-visszajelzést ír meg.
  - Az SCS-nek nincs kérdés- vagy válaszonkénti visszajelző mezője, és az „Auto continue” alapértéke bekapcsolt.
  - A lecke ezt maga is elismeri, és az RA 14-re hárítja, de az RA 14 csak tesztel, típust nem választ.
- **Bizonyíték:** Z.1:382 „A Single Choice Setben nincs kérdésenkénti visszajelző mező (csak pontsávos összesítő visszajelzés)” · h5p-single-choice-set `semantics.json`: „Alternatives - first alternative is the correct one.”; autoContinue: „This needs to be turned off to make the content fully accessible when using a screen reader.”
- **Hatás:**
  - A tévesen válaszoló tanuló nem kapja meg a modulra visszavezető magyarázatot.
  - Alapbeállítással a feladat a visszajelzés elolvasása előtt továbblép (WCAG 2.2 SC 2.2.1).
- **Javaslat:**
  - Csak a típusnév változik: kérdésenként egyválaszos Multiple Choice („Single Choice (Radio Buttons)”). Ennek válaszonként van `chosenFeedback` mezője (h5p-multi-choice `semantics.json`: „Message displayed if answer is selected”). Minta: M3:IMPL-G2-9, M2:ERT-G2-3.
  - A :13 completion-sora és a :335 ezt követi; a :382 szűkíthető arra, hogy a megjelenést az RA 14 teszteli.
  - Ha mégis SCS marad: „Auto continue” = ki (A11Y:83), és a kérdésenkénti szöveg nem ígérhető.
  - Nem változik: a kérdések, az opciók, a ✅ és a visszajelzés-szövegek.
- **Típus:** objektív
- **Verdikt:** —

---

**IMPL-G1-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.1:266, :531 ↔ PD:507 (VO D-19), :513 (K2); A11Y:12; RA:103 (22. pont). A Z.1:203 és :477 `a11y.note` mezője helyes.
- **Probléma:** A kötelező akadálymentességi utasítás a csak hangos narrációnál alternatívát kínál a szó szerinti szöveges megjelenítés helyett: „(vagy adj hozzá magyar feliratot)”.
  - A lezárt VO D-19 szerint itt a látható leirat a szöveges ekvivalens, és a H5P Audiótól feliratsáv nem várható.
  - Ez a fordulat csak a Z.1-ben fordul elő.
- **Bizonyíték:** Z.1:266 „a narráció szövegét szó szerint jelenítsd meg a dián vagy a slide alatti szövegmezőben (vagy adj hozzá magyar feliratot)” · PD:507 „Csak hangot tartalmazó narrációnál a dián vagy a médiaelem mellett látható leirat a szöveges ekvivalens; … a H5P Audio elemtől feliratsáv nem várható.”
- **Hatás:** Ha a fejlesztő a feliratos utat választja, nem marad szöveges ekvivalens. A SLIDE 6 narrációja (a köszönet és a Z.2-átvezetés) máshol nincs a dián, így WCAG 2.2 SC 1.2.1 hiány keletkezik. A törzs és az asset a11y-jegyzete is ellentmond egymásnak.
- **Javaslat:**
  - Mindkét helyen törlendő a zárójeles alternatíva, helyére a VO D-19 / A11Y:12 fordulata kerül (látható leirat, első sora a kanonikus AI-címke). Ez a lezárt döntés szó szerinti átvezetése.
  - Nem változik: a „szó szerint” és az „új tartalom nem hangozhat el” kikötés, a `@source` és az `@asset` mezők.
- **Típus:** objektív
- **Verdikt:** —

---

**IMPL-G1-7**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** Z.2:13, :63; Z.3:3–23 (a metában nincs „Completion (lecke)” sor), :59; Z.1:13 ↔ MAN:16 (H5P-C, „Hide summary slide” = No), :107 (az LMS-Z-03 Megjegyzése üres); RA:72 (9. pont)
- **Probléma:** A Z.2 és a Z.3 completionje bizonytalan alapon áll.
  - A Z.2 completion-halmaza kizárólag helyes válasz nélküli, reflektív Single Choice-okból áll (SLIDE 1, 3, 4).
  - A Z.3-nak nincs completion-sora, és a választói (SLIDE 1, 3, 7) szintén mind reflektívek.
  - A H5P-C grade-et csak a CP összefoglaló diája adja. Az a CP-forrás szerint csak akkor jelenik meg, ha van feladatelem, és megválaszolás-ellenőrzés nélkül küld (M0:IMPL-3).
- **Bizonyíték:** Z.2:13 „a választós interakciók érdemi megválaszolása (az LMS-Z-02 H5P-C profilja): SLIDE 1, SLIDE 3 és SLIDE 4 Single Choice.” · h5p-course-presentation `cp.js`: „this.slidesWithSolutions.forEach(function (slide) { that.showSummarySlide = slide.length; });”
- **Hatás:**
  - Ha az RA 14 nem feladat típusú megoldást választ a helyes válasz nélküli kérdésekre, a CP-nek nincs összefoglaló diája, nincs grade. Ekkor az LMS-Z-02 vagy az LMS-Z-03 sosem teljesül, és a Z, valamint az online félév blokkolt.
  - Feladat típusú megoldásnál a completion a dia elérése, nem az „érdemi megválaszolás”.
- **Javaslat:** EMBERI DÖNTÉS, de nem új döntés: az M0:IMPL-3, az M0:ERT-3 (a Z.2 completionje, akárcsak az M0.1-é, csak pontozatlan választókból áll) és az M2:IMPL-G2-1 nyitott kérdéséhez tartozik (X-6). Gazda: projektgazda; QA: értékelési felelős.
  - A döntés után objektív: a Z.3 metája kap „Completion (lecke)” sort a Z.1:13 / Z.2:13 mintájára, és kitöltődik az LMS-Z-03 Megjegyzése.
  - Most completion-sor nem írható be.
- **Típus:** emberi-döntés
- **Verdikt:** —

---

**IMPL-G1-8**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.4:307, :310, :336; HUB:184 ↔ ADV:72, :171, :214; RELEASE-READINESS G2 (:25), „Modul-specifikus élesítés” (:83)
- **Probléma:** A videós beadási út minden tanulónak nyitva van (File submissions: ON). A HUM-PRIV-02 folyamatának bizonyítéka közben hiányzik:
  - ki, hol és a feltöltés elfogadása előtt rögzíti a hozzájárulást (18 év alatt a gondviselőét is);
  - hogyan törlődik a videó legfeljebb 90 napon belül, a szöveges beadás „képzés vége + 90 nap” sorától külön.
  - Az ADV release-evidence tétele kipipálatlan.
- **Bizonyíték:** Z.4:336 „File submissions: **ON**, max 1 file, max size 100–200 MB (opcionális videós út).” · ADV:214 „- [ ] fotó/videó/hang folyamat HUM-PRIV-02 szerint lezárva; <!-- gate: release-evidence -->”
- **Hatás:** Kiskorú videója rögzített hozzájárulás nélkül kerülhet a Moodle-be. A videó megőrzése a beadás sorát követné, nem a legfeljebb 90 napos sort.
- **Javaslat:**
  - Repóban nem javítható. Megvalósítási döntés: a projektgazda jóváhagyta (HUM-PRIV-02, 2026-10-02); a DPO formális bizonyítéka és a folyamat lezárása függő → G2 (tracker #2).
  - A RELEASE-READINESS :83 mintája szerint a videós út addig valódi madrihnak nem nyitható.
  - Hozzájárulási mechanizmust nem írunk be.
- **Típus:** bizonyíték-kapu
- **Verdikt:** —

---

**IMPL-G1-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** Z.4:336, :278 ↔ docs.moodle.org/405 Assignment settings; A11Y:46–47
- **Probléma:** A videós út Assignment-paraméterei nem építhetők meg egyértelműen.
  - Az „Accepted file types” nincs megadva; üresen hagyva minden fájltípust enged.
  - A méret tartomány („100–200 MB”), nem érték, és a kurzusbeállítás korlátozza.
  - A célkörnyezeti feltöltési limit egyik G3a-paraméter között sem szerepel.
- **Bizonyíték:** Z.4:336 „max 1 file, max size 100–200 MB (opcionális videós út)” · docs.moodle.org/405 Assignment settings: „Leaving the field blank will allow all file types.” / „It cannot be larger than the limit in the Course settings.”
- **Hatás:**
  - A „videós” mezőben bármilyen fájl (kitöltött docx, fotó) leadható.
  - Alacsonyabb kurzus- vagy site-limitnél a 2–3 perces telefonos videó feltöltése a határidőn bukik el.
- **Javaslat:**
  - Z.4 §4: „Accepted file types” = videó (a Moodle „video” csoportja), ez a Z.4:278 és :336 alapján levezethető.
  - Egyetlen „Maximum submission size” érték a 100–200 MB-on belül, az LMS-gazda rögzíti. Fejlesztői megjegyzés, hogy a kurzus- és site-limit ezt engedje (G3a, RA Environment record).
  - Nem változik: a videó opcionális, a szöveg az alapértelmezés, a 2–3 perc.
- **Típus:** objektív
- **Verdikt:** —

---

**IMPL-G1-10**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** Z.4:27, :73 ↔ Z.4:302, MAN:110; HUB:195 ↔ MAN:110, :112; Z.1:59 ↔ Z.2:65; HUB:171 ↔ PT:307
- **Probléma:** Négy kisebb eltérés a build-szerződéstől vagy a kánontól:
  - (a) Az Assignment neve „Záró reflexiós ív”, a §4 és a manifest szerint „Záró reflexió + következő lépés”.
  - (b) A hub ajánlásként („érdemes”) írja a Z.4 Z.A utáni nyitását, a manifest kötelező unlockként.
  - (c) A Z.1:59 tájékoztató-feltétele a D-2 óta nem létező mezőkre vonatkozik. A Z.2:65 már javítva van.
  - (d) A hub a PT §6-ot nem szó szerint idézi.
- **Bizonyíték:** Z.4:73 „→ Moodle Assignment (Z.4 – „Záró reflexiós ív”, Online text)” · Z.4:302 „**Név:** `Záró reflexió + következő lépés`”
  HUB:195 „érdemes a **Z.4-et `restrict access`-szel a Z.A dátuma mögé tenni**” · MAN:110 „**Z.A után, a §7 szerinti dátummal**”
- **Hatás:**
  - A tanuló és a fejlesztő két néven keresi ugyanazt az activityt (A11Y Phase-0: heading az aktivitás nevével).
  - Az „érdemes” kihagyható beállítást sugall.
  - A Z.1:59 alapján fölösleges tájékoztató vagy mező épülhet.
- **Javaslat:**
  - (a) A :27 és a :73 a §4 nevét használja; a „záró reflexiós ív” köznévként a sablonra maradhat.
  - (b) A HUB:195 a MAN:110/:112 unlockját veszi át szó szerint.
  - (c) A Z.1:59 a Z.2:65 mintáját követi: „…minden adatot rögzítő mezője előtt (a D-2 szerint a Z.1 szöveges lépései nem ilyenek)…”.
  - (d) A HUB:171 idézete a PT:307 szövegét követi.
  - Nem változik: a tájékoztató tartalmi követelménye, a `SCHEDULE_TO_RESYNC` dátumok, a „reflektív, NEM értékelő” mondat.
- **Típus:** objektív
- **Verdikt:** —

---

A hipotézisekről: az N-Z-07, az N-Z-03 és az N-Z-09 a D4/D5/D10 dimenzión kívül esik, ezért ebben a lencsében nem jelentettem őket. Az M0 NYELV-G2-18 négy Z.A-helyét nem ismételtem meg.

LEVÁGVA: 1 további finding, súlyosságuk: 1×P2

## IMPL-G1 — implementáció, hub, Z.1–Z.4, Z.A (2. rész, folytatás) (folytatás 2)

Implementációs lencse, Z modul, G1 — folytatás (a korábban leadott IMPL-G1-1…10 ismétlése nélkül). Read-only, fájlt nem szerkesztettem; pilot-besorolást nem adok.

Rövidítések: Z.4 = 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md · MAN = …/02 Tervezet/LMS – activity manifest.md · RA = …/02 Tervezet/LMS – H5P runtime acceptance.md · ADV = …/02 Tervezet/Adatvédelem – tanulói adatok és AI.md · HUM = …/02 Tervezet/Emberi jóváhagyás szükséges.md · RR = …/02 Tervezet/RELEASE-READINESS.md

---

**IMPL-G1-11**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** Z.4:398 (5. szakasz, Beállítás-javaslatok); Z.4:383–392 (szöveges kérdések: 2. „Hol hiányzott…”, 5–7.) ↔ MAN:22 (FEEDBACK-N: „eredmény a HUM-PRIV-03 szerint”), MAN:112 (LMS-Z-05); HUM:157–170 (HUM-PRIV-03, LEZÁRVA); ADV:119 (BIZT-6); RR:25 (G2 nyitott DPO-tételei); RA:86 (16. pont)
- **Probléma:** A kötelező LMS-Z-05 Feedback két build-paraméterének („Show analysis page”, „Enable notification of submissions”) értéke sehol nincs rögzítve. A Z.4 a lezárt HUM-PRIV-03 jóváhagyóira hárítja őket, holott azok ott utólagos ellenőrzők (vétó/QA), és a HUM-PRIV-03 szövege ezekről nem dönt. A FEEDBACK-N profil sem rögzíti őket, és a tétel nem szerepel sem a G2 nyitott DPO-tételei, sem a BSPEC-sorok között. A TEXT-C profil ugyanezt a két beállítást kifejezetten rögzíti (MAN:24: „Show analysis page” = No; „Enable notification of submissions” = „No”).
- **Bizonyíték:** Z.4:398 „**`Show analysis page` és `Enable notification of submissions`:** az értéküket a HUM-PRIV-03 gazdája (adatvédelmi/DPO felelős + programvezető) rögzíti.” · MOODLE_405_STABLE `mod/feedback/mod_form.php`: a `publish_stats` és az `email_notification` `selectyesno` elem, `setDefault()` nélkül
- **Hatás:** Nincs rögzítve, mit kap a tanuló beküldés után. „Show analysis page” = Yes esetén a 8–20 fős csoportban a tanulók az elemzőoldalon a többiek válaszait is láthatják, köztük a szabad szöveges javaslatokat és nehézségeket (Z.4:382, :387–392). Kis csoportban ezek név nélkül is visszaazonosíthatók, ami gyengíti a „név nélkül jelennek meg a feldolgozásban” ígéretet (HUM-PRIV-03). A fejlesztő a beállítást maga választja meg, az RA 16. pont pedig ezt a két értéket nem olvassa vissza.
- **Javaslat:** EMBERI DÖNTÉS: a két beállítás értéke az LMS-Z-05-nél. Gazda: a projektgazda mint build-spec gazda; vétó/QA: DPO + programvezető (HUM-PRIV-03), a BIZT-6 mentor-hozzáféréssel együtt. A döntéstől független objektív lépés: a tétel nyitottként bekerül a G2 nyitott DPO-tételei közé (RR:25) és a MAN:22 / :112 megjegyzésébe, a döntés után pedig a választott érték a FEEDBACK-N profilba és az RA 16. pont visszaolvasási listájába. A repóban nem írunk be értéket. Nem változik: a „Record user names” = „Anonymous”, a kötelező kitöltés, az egyszeri beküldés, a 90 napos megőrzés, a tanulói mondat („A válaszok név nélkül jelennek meg a feldolgozásban.”).
- **Típus:** emberi-döntés
- **Verdikt:** —

LEVÁGVA: 0 további finding

## NYELV-G1 — nyelv, hub, Z.1–Z.4, Z.A (1. rész)

NYELV lencse: Z modul, G1 (hub, Z.1–Z.4, Z.A), AP-2026-10-11-01. Csak olvastam, fájlt nem módosítottam.

**Rövidítések (abszolút utak):**
- HUB = 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- Z.1 = 02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md
- Z.2 = 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md
- Z.3 = 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- Z.4 = 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md
- Z.A = 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md

**A hipotézisekről és a kizárásokról:**
- **N-Z-07:** a „Ha nincs meg, nem baj –” (Z.4:194, :208) természetes magyar mondat. A kibúvó kérdése pedagógiai, nem nyelvi, ezért nem jelentem.
- **N-Z-03, N-Z-09:** nem nyelvi kérdések. A szövegükben nem találtam nyelvi hibát.
- **M0:NYELV-G2-18:** a Z.A-ban validált helyeit (:55, :423, :440, :458, „induló-szavak”) nem ismétlem. A héber tagú összetételeket (madrih-, hanih-, kvuca-) a G2-18 kizárása szerint kihagytam.
- **Régi írásmód** (madrich, chanich, hagshama, dugma ishit, Leviatan, madrihák): a Z-ben 0 találat.

---

**NYELV-G1-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** Z.1:368 (SLIDE 4, 4. kérdés). Összevetve: Z.1:381 és :315.
- **Probléma:** A kvízkérdés rossz esetragot használ: „Zmán Kvucával”, holott ugyanez a lecke kétszer „Zmán Kvucára” alakot ír.
- **Bizonyíték:**
  - :368 „„Melyik modulban írtál **Peula v2-t Zmán Kvucával**?””
  - :381 „„Majdnem 🙂 – a Peula v2-t Zmán Kvucára az M7-ben írtad meg.””
- **Hatás:** A tanulói kérdés szerint a peulát a Zmán Kvucával együtt írták, nem a Zmán Kvucára. A kérdés és a visszajelzés eltér egymástól (7-es regressziós minta).
- **Javaslat:** „Peula v2-t Zmán Kvucára”. Korlát: az opciók és a ✅ (M7) nem változnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** Z.3:237 (a mező mintaszövege, LMS-Z-06, 1. kérdés) és Z.3:227 (segítő példa)
- **Probléma:** A kötelező nyitómondat („A következő 3 Zmán Kvucámon…”) és a „mikor” rész összeolvasva két helyhatározót ad egymás mellett („…Kvucámon a … Zmán Kvucámon”). Ez nem magyar mondat.
- **Bizonyíték:**
  - :237 `A következő 3 Zmán Kvucámon a ... Zmán Kvucámon futtatom le a Peula v2-met a ... kvucámmal.`
  - A helyes szerkezet ugyanebben a diában, :222: „(pl. „a következő 3 Zmán Kvucám közül a másodikon”)”
- **Hatás:** A tanuló a kötelező mezőt egy hibás minta alapján tölti ki.
- **Javaslat:**
  - :237 → `A következő 3 Zmán Kvucámon lefuttatom a Peula v2-met a ... kvucámmal, mégpedig a ... alkalommal. Ha ..., akkor ...`
  - :227 → „…lefuttatom a Peula v2-met a Leviatán-kvucámmal, mégpedig a 2. alkalommal.”
  - Korlát: a „A következő 3 Zmán Kvucámon…” nyitás betűre marad, mert a Z.3:219, :318 és a Z.4:207 erre hivatkozik. A három kötelező elem (mikor, melyik kvuca, ha–akkor) nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.4:62, :140, :212, :322 (a 3. vezető kérdés); Z.4:234 (ellenőrző lista); Z.4:35 (mikrocél). Összevetve: HUB:110, HUB:189, Z.4:351.
- **Probléma:** Ugyanaz a 3. kérdés a hubban grammatikus, a Z.4-ben elmosódott jelentésű („célt a következő lépésekhez”), pedig a teljesítési minimum következő lépést kér.
- **Bizonyíték:**
  - Z.4:62 „„Írj le **1–2 konkrét célt a következő lépésekhez** a terepre.”
  - HUB:110 „„Írj le 1–2 konkrét következő lépést, célt a terepre.”
- **Hatás:** A tanuló a lépések mögé írhat célt, miközben a „Teljesítve” feltétele az, hogy 1–2 következő lépés legyen, legalább az egyik határidős.
- **Javaslat:**
  - A négy kérdéshelyen a HUB:110 szövege szó szerint.
  - :234 → „Van 1–2 konkrét következő lépésed (célod)…”
  - :35 → „1–2 konkrét következő lépést (célt) a terepre”
  - Korlát: a „Kinek fogod elmondani…” mondat és a minimum-feltételek (HUB:189, Z.4:351) nem változnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv (D10 terminológia)
- **Hely:**
  - A Feedback neve: HUB:190 ↔ Z.4:365 és a manifest LMS-Z-05.
  - Az Assignment neve: Z.4:27, :73, :77 („Záró reflexiós ív”) és Z.A:24 („„Záró reflexió + képzési visszajelzés” Assignment”) ↔ Z.4:293, :302, HUB:105, :183 és a manifest LMS-Z-04.
- **Probléma:** Egy Moodle-aktivitás több idézőjeles néven fut: az Assignmentnek három neve van, a Feedbacknek kettő.
- **Bizonyíték:**
  - HUB:190 „**Moodle Feedback – „Képzés-értékelés”**” ↔ Z.4:365 `Képzési visszajelzés – név nélkül`
  - Z.4:73 „→ Moodle Assignment (Z.4 – „Záró reflexiós ív”, Online text)” ↔ Z.4:302 `Záró reflexió + következő lépés`
- **Hatás:** Az építő rossz néven hozhatja létre az aktivitást. A tanuló a Z.4:293 alapján más nevet keres, mint amit a Moodle-ben lát.
- **Javaslat:**
  - Mindenhol a manifest neve áll: HUB:190 → „Képzési visszajelzés – név nélkül”; Z.4:27, :73 és Z.A:24 → „Záró reflexió + következő lépés”.
  - A „záró reflexiós ív” idézőjel nélkül maradhat a sablon leírásaként.
  - Korlát: a lecke címe („Z.4 – Záró reflexió + képzési visszajelzés”), a fájlnevek és a linkek nem változnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv (D10 terminológia)
- **Hely:** Z.4:156 és :186 (lépéscímek) ↔ :130, :161 (szakasz), :203, :218 (2. és 3. szakasz), :262, :278 (háromrészes)
- **Probléma:** Az ív részeit a tanuló kétféle néven, eltérő számozással látja: két „blokk” (a 2. blokkban a/b rész) és három „szakasz”, ahol a „2. blokk” a 2. és a 3. szakaszt fedi.
- **Bizonyíték:**
  - :186 „**2. blokk – Szemléletváltozás és következő lépések**”
  - :130 „**mindhárom egy-egy szakasz ezen az íven**”
- **Hatás:** A tanuló a szakaszcímeket maga másolja a szövegébe (:81), ezért a számozás könnyen elcsúszik.
- **Javaslat:** :156 „1. blokk” → „1. szakasz”; :186 „2. blokk” → „2–3. szakasz”. Korlát: a LÉPÉS-számozás, a szakaszcímek és az a)/b) jelölés marad.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-6** (az M0:NYELV-G1-13 és az M2:NYELV-G1-9 mintája)
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:**
  - HUB:109, :132
  - Z.1:271 (VO, `@source`), Z.1:195 (`@asset` spec)
  - Z.4:61 (két hely), :137, :190, :198, :233, :320; :152 (fejlesztői sor)
  - Z.A:23, :192
- **Probléma:** A szemantikus azonosítók elől teljes mondatban hiányzik a névelő („M0-hoz”, „M0-ban”, „M7-re”, „Z.1–Z.3 leckék”, „Z.2-re”). Ugyanabban az idézetben a helyes alak is előfordul.
- **Bizonyíték:**
  - Z.4:198 „…változott a madrih-szemléleted M0-hoz képest? Mi valósult meg abból, amit az M0-ban magadnak megfogalmaztál?”
  - Z.1:271 „Látod, honnan indultunk M0-ban, és hova jutottunk el M7-re.”
- **Hatás:** Felolvasva (VO) és tanulói kérdésben is döccen. Ugyanazon a helyen kétféle alak áll.
- **Javaslat:** Mindenhol „az M0-hoz”, „az M0-ban”, „az M7-re”, „a Z.1–Z.3 leckék”, „a Z.2-re építve”, „az M0–M7-ből”. Korlát:
  - Az azonosítók nem változnak.
  - A Z.1:271 csak a hanggyártási úton javítható (újrarenderrel), a Z.1:195 build úton.
  - Pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-7** (az M0:NYELV-G2-18, az M2:NYELV-G1-17 és az M2:NYELV-G3-13 mintája, új helyekkel)
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:**
  - Z.A:88 „Blokk-leírások”
  - „elismerés-kör”: Z.A:64, :72, :75 (két hely), :77, :83, :84, :343, :346, :392, :529, :530
  - „poszter-állomás”: Z.A:43, :520
  - „poszter-bemutató/-bemutatás”: Z.A:71, :329, :529; `@asset`: :291, :480
  - Z.A:75 „poszter-idő”; Z.A:313 „Poszter-keret”; Z.A:457 „Szó-írás”
  - Z.A:83 „szófelhő rituálé” (különírva)
  - HUB:91 „sablon mondatokkal” (különírva); HUB:92 „esemény-specifikus”; HUB:165 „Támogatás-térkép”
  - Z.2:107 „érzés-szintű” (`@asset`: :76)
  - Z.4:191 „várakozás-mondatát”, :192 „ígéret-mondatát”
- **Probléma:** Magyar köznévi összetételek kötőjellel vagy különírva. Ez ellentmond az AkH 6:3-as szabályának.
- **Bizonyíték:**
  - Z.A:88 „## 4. Blokk-leírások (részletesen)”
  - Z.A:83 „a **záró szófelhő rituálé** (4.4.2)”
- **Hatás:** Helyesírási hiba a képzői és tanulói szövegben és a nyomtatott anyagok leírásában.
- **Javaslat:** blokkleírások, elismeréskör, poszterállomás, poszterbemutató/-bemutatás, poszteridő, poszterkeret, szóírás, szófelhő-rituálé (3 tag, 7 szótag), sablonmondatokkal, eseményspecifikus, támogatástérkép, érzésszintű, várakozásmondat, ígéretmondat. Korlát:
  - A héber tagú összetételek, az „Időkapszula-” és a „Félév-emojik” név, valamint a G2-18 „induló-szavak” helyei kimaradnak.
  - Az `@asset`-mezők csak build úton változnak, külön `chore(media)` commitban.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-8** (az M2:NYELV-G2-10 mintája)
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv (D10 terminológia)
- **Hely:**
  - Z.1:11, :13, :57, :321; Z.3:11, :59, :181; HUB:80 „multichoice”
  - Moodle Feedback-környezetben: Z.4:383 „Multi Choice” és :385 „Single Choice” ↔ Z.4:376 „Multiple choice”
- **Probléma:** A H5P tartalomtípus nem hivatalos „Multi Choice” alakban áll; a hivatalos név „Multiple Choice”, a runtime acceptance is így írja. A Feedback-blokkban H5P-nevek szerepelnek, miközben két sorral feljebb a Moodle-név áll.
- **Bizonyíték:**
  - Z.1:321 „H5P **Multi Choice** (pipálhat többet is – nincs jó/rossz, csak reflexió)”
  - Z.4:383 „**Hasznos modulok** – Multi Choice (több válasz jelölhető)”
- **Hatás:** Az építő nem létező típust keres. A Feedbackben nincs „Single Choice” elem.
- **Javaslat:**
  - H5P-helyeken „Multiple Choice”.
  - Z.4:383 → „Multiple choice (több válasz)”; :385 → „Multiple choice (egy válasz)”.
  - Korlát: az RA 14. pontjára hivatkozó kikötő mondatok, a „Single Choice Set” és a Z.1–Z.3 „Single Choice” címkéi maradnak; ✅ nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-9** (az M2:NYELV-G3-17 mintája)
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv (D10 terminológia)
- **Hely:** Z.A:11 ↔ Glosszárium:72
- **Probléma:** A „Korosztály” sorból hiányzik a kánoni „/ madrihot”.
- **Bizonyíték:**
  - Z.A:11 „**Korosztály:** képzős madrihok (15+)”
  - Glosszárium:72 „Egységesen `madrihok / madrihot` a teljes tananyagban (a „Korosztály” fejlécekben is).”
- **Hatás:** Eltérés a kánoni terminológiától.
- **Javaslat:** „képzős madrihok / madrihot (15+)”. Korlát: a „15+” marad.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:**
  - Erősebb helyek: Z.A:206 (felolvasandó képzői szöveg); Z.1:34
  - Gyengébb helyek: Z.4:53–56; Z.A:405–406
- **Probléma:** Szám- és személyelcsúszás (6-os regressziós minta):
  - Z.A:206: egy mondaton belül 3. személyből 2. személybe vált, és két leckére egyes számú „leckében” áll.
  - Z.1:34: „indultunk” és „jutottál” egy mondatban.
  - Z.4:53–56: „Két dolgot csinálunk:”, a pontok viszont „Végigmész”, „Kitöltesz”.
  - Z.A:405–406: a csoportnak szóló („írjátok”, „Menjetek”) és a képzőnek szóló („mondd ki”) pontok keverednek.
- **Bizonyíték:**
  - Z.A:206 „Aki az **M0.1–M0.2 online leckében** elmentette magának […] most idézze fel […] – ez is lehet az egyik tanulási pillanatod […] idézd fel körülbelül.”
  - Z.1:34 „**M0–M7** – honnan indultunk, és hova jutottál el madrihként.”
- **Hatás:** A képző felolvasás közben kénytelen javítani. Az utasításnál nem dönthető el, kinek szól.
- **Javaslat:**
  - Z.A:206 egységesen 2. személyben: „Ha az M0.1–M0.2 online leckékben elmentetted magadnak a … mondatodat, most idézd fel…”
  - Z.1:34 egy személyben, pl. „honnan indultál, és hova jutottál el madrihként”.
  - Z.4:53 → „Két dolgot csinálsz:”
  - Z.A:405–406: idézőjeles képzői szövegként, vagy „Kérd meg őket, hogy…” szerkezetben, mint a :400.
  - Korlát: a passz-szabály és a cetli-szabályok tartalma nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-11**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.A:319; Z.3:176
- **Probléma:** Hiányzik az alaptag vagy az utalószó (1-es regressziós minta):
  - Z.A:319: főnevek felsorolásában csak a „nonformális” jelző áll.
  - Z.3:176: hiányzik az „az a”.
- **Bizonyíték:**
  - Z.A:319 „(önismeret, visszajelzés, kvuca, gyermekvédelem, nonformális stb.)”
  - Z.3:176 „Ezekben közös, hogy:”
- **Hatás:** A képzői felsorolás csonka. A tanulói diaszöveg nyelvtanilag hiányos.
- **Javaslat:** „nonformális nevelés” (az M5 címe és a Z.1:258 is így írja); „Ezekben az a közös, hogy:”.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-12**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.A:403 ↔ :72, :77, :344
- **Probléma:** A 45 perces változatra a 4.4.1 „kihagyható” (opcionális) szót ír, a percbontás szerint viszont a névhúzás kimarad.
- **Bizonyíték:**
  - :403 „(kb. 6 perc, *75’-es verzióban; 45’-ben kihagyható*)”
  - :77 „(a névhúzásos nagykörös rákötés kimarad)”
- **Hatás:** A képző a 45 perces változatban is beférőnek gondolhatja a 6 perces kört, amire a 11 perces blokkban nincs idő.
- **Javaslat:** „45’-ben kimarad”. Korlát: a percek, a 75’-es 6 perc és a HUM-OPS-01 blokkhatárai nem változnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-13**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.A:459 ↔ :414 (cím), :452, :460, HUB:140
- **Probléma:** A felolvasandó instrukció egy szót kér, a következő mondat viszont mondatot is megenged.
- **Bizonyíték:** :459 „írj rá **1 szót**, amit magaddal viszel ebből a félévből. Lehet érzés, érték, gyakorlat, mondat – ami neked most igaz.”
- **Hatás:** A szófelhő-rituálé szabálya elbizonytalanodik.
- **Javaslat:** A „mondat” törlése a felsorolásból, a többi négy helyhez igazítva. Ha a szerző rövid kifejezést akart megengedni, az tartalmi döntés, és akkor minden „1 szó” hely együtt változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-14**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.A:53 ↔ :226
- **Probléma:** Biztonsági eljárásban az „Utána” nem mutat egyértelmű előzményre. Jelentheti azt, hogy a mentorhoz vagy a Memunához fordulás után, de azt is, hogy a peula után. A 4.2 tippje csak a „peula után” odalépést írja le.
- **Bizonyíték:**
  - :53 „gyermekvédelmi aggálynál pedig a kijelölt **Memunához** (…). Utána diszkréten, de átlátható helyzetben lép oda a résztvevőhöz”
  - :226 „a peula után finoman odamehetsz hozzá egy rövid „minden oké?” kérdéssel”
- **Hatás:** Nem egyértelmű, hogy a megérintett résztvevőhöz előbb a képző lép-e oda, vagy előbb a mentort vagy a Memunát vonja be.
- **Javaslat:** EMBERI DÖNTÉS: a modulgazda és a Memuna döntse el, melyik sorrendet jelenti az „Utána”, és ehhez igazodjon a :226 is. Szöveget nem javaslok. Korlát: a safer-working kikötések és az ötlépéses jelzési út szó szerint maradnak.
- **Típus:** emberi-döntés · **Verdikt:** —

**NYELV-G1-15**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** Z.3:147–148 ↔ :142, :153
- **Probléma:** A „Miért kis lépések?” dia hibaként a „túl kicsit” is megnevezi, a példa („Jobb madrih leszek”) és a magyarázat viszont csak az általánosságot mutatja.
- **Bizonyíték:**
  - :147 „Ha túl kicsit, túl általánosat:”
  - :148 „– *„Jobb madrih leszek.”* – ez szép, de **nem tudod, mikor teljesült.**”
- **Hatás:** A diaüzenet („kis lépés jó”) és a hibalista egymásnak ellentmondónak hat.
- **Javaslat:** EMBERI DÖNTÉS: a modulgazda vagy a projektgazda döntse el, hogy a „túl kicsi” vállalás szándékos második hibatípus-e (akkor a példát igazítani tartalmi döntés), vagy maradvány (akkor a „túl kicsit,” törlendő). Szöveget nem javaslok.
- **Típus:** emberi-döntés · **Verdikt:** —

LEVÁGVA: 3 további finding, súlyosságuk: 3×P2

## NYELV-G1 — nyelv, hub, Z.1–Z.4, Z.A (2. rész, folytatás) (folytatás 2)

NYELV lencse: Z modul, G1, folytatás (AP-2026-10-11-01). Ez a 3 levágott finding; a G1-1…15 nem ismétlődik. Csak olvastam, fájlt nem módosítottam.

**Rövidítések (abszolút utak):**
- HUB = 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md
- Z.2 = 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md
- Z.3 = 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md
- Z.A = 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md
- TEREP = 02 Tervezet/Terepgyakorlat – 2. félév.md

---

**NYELV-G1-16**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** Z.3:207 (SLIDE 4, tanulói diaszöveg). Forrása a TEREP:15. A HUB:206 stábszöveg, ott maradhat.
- **Probléma:** A tanulói szövegben adatvédelmi szakszó áll („adatminimalizált”). A szerkesztői norma szerint tanulói szövegben nincs compliance-regiszter.
- **Bizonyíték:**
  - Z.3:207 „A megfigyelési jegyzeted rövid és adatminimalizált legyen: hanih érzékeny adata nélkül.”
  - TEREP:15 „rövid, adatminimalizált megfigyelési jegyzet; hanih érzékeny adata nélkül.”
- **Hatás:** A 15–17 éves madrih a GDPR-szót nem feltétlenül érti, így az adattakarékossági utasítás lényege csak a kettőspont utáni részből derül ki.
- **Javaslat:** „A megfigyelési jegyzeted legyen rövid, és csak a szükséges adatokat tartalmazza: hanih érzékeny adata nélkül.” Korlát:
  - Az adattakarékossági kikötés tartalma nem gyengülhet; a „hanih érzékeny adata nélkül” rész szó szerint marad.
  - A TEREP:15 és a HUB:206 nem változik.
  - Ha a verifier a TEREP-mondatot kánoni átvételnek tekinti, a csere nem végezhető el.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-17**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** Z.A:343 ↔ :344, :81, :77, :403
- **Probléma:** A „75’ verzió” jelzőként hiányzik a képző („-es”). Ugyanebben a zárójelben és a fájl más helyein „45’-es” és „75’-es” áll.
- **Bizonyíték:**
  - :343 „*(75’ verzió: 20’ elismerés-kör [kb. 2’ keret + 7’ párcsere + …”
  - :344 „45’-es peulánál rövidíts: 11’ elismerés”
- **Hatás:** Felolvasva „hetvenöt perc verzió” lesz, ami nyelvtanilag hibás, és a fájlon belül is eltér a többi alaktól.
- **Javaslat:** „75’-es verzió”. Korlát: a percértékek nem változnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-18**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** Z.2:18 (mikrocél); Z.A:105 (felolvasandó körkérdés); HUB:124 (ugyanez a körkérdés)
- **Probléma:** Két tagmondatot összekötő „és” elől hiányzik a vessző.
  - Z.2:18: emiatt a „mit mond ez rólad” nyelvtanilag a „amit” vonatkozó mellékmondathoz kapcsolódik.
  - Z.A:105 és HUB:124: a „miért” hiányos tagmondat.
- **Bizonyíték:**
  - Z.2:18 „volt-e olyan modul, amit nehéznek éltél meg és mit mond ez rólad”
  - Z.A:105 „Ha a féléved egy emoji lenne, melyik lenne az és miért?”
- **Hatás:** Írásjelhiba a tanulói mikrocélban és a képző által felolvasott kérdésben; a Z.2:18 mondatszerkezete rosszul tagolódik.
- **Javaslat:** „…amit nehéznek éltél meg, és mit mond ez rólad”; „…melyik lenne az, és miért?” (a Z.A:105 és a HUB:124 együtt). Korlát: csak a vessző kerül be, egyetlen szó sem változik.
- **Típus:** objektív · **Verdikt:** —

LEVÁGVA: 0 további finding
