# 2026-10-11 Célzott újraellenőrzés – M1 NEEDS_RECHECK, AP-2026-10-11-01

> **Audit trail — nem kánon.** A `/course-autopilot` 6. pontja szerinti egyszeri, célzott újraellenőrzés (verifier, read-only)
> az M1 ledger-tételeire, amelyek `NEEDS_RECHECK` állapotba kerültek: ERT-G1-1 és IMPL-G1-2 (az N-M1-04 javítása után
> változott helyek, `ebf311e`, `96996e2`), PED-G1-8.obj és BIZT-G3-8.obj (a 2026-10-10-i riport 3. szakaszában „objektív
> rész”-ként nevezett, saját sor nélküli tételek), valamint a lencsék által levágott, verdikt nélküli nyolc P2.
> Forrás: `2026-10-10 Validált findingok – M1 course-review, B sáv.md`. Review-bázis: `a16eb4b` (a `02 Tervezet/`
> tartalma azonos a `main@213a4c5`-tel). Read-only bizonyíték: `git diff HEAD -- "02 Tervezet" | shasum` =
> `da39a3ee5e6b4b0d3255bfef95601890afd80709` (kezdet és mentés). Az alábbi verifier-kimenet szó szerint (a helyi abszolút
> útvonal-előtag repó-relatívra rövidítve).
>
> **Eredmény:** MEGERŐSÍTVE 4 (ERT-G1-1: javítva; IMPL-G1-2: az N-M1-04 rész javítva, a CC-04/CC-06 HUM-átvezetés = M0
> ERT-8; PED-G1-8.obj és BIZT-G3-8.obj: fennáll, önállóan javítható), ELVETVE 8, EMBERI DÖNTÉS 0.


## VERIFIER — 12 NEEDS_RECHECK tétel

ERT-G1-1 · MEGERŐSÍTVE (a 2026-10-10-i szövegen valós volt) · objektív · P0 · JAVÍTVA: a 2. szakasz összes hiba-eleme rendben van. M1.1:98 már nem ír Moodle-oldali tárolós tartalékutat („Moodle-oldali mező és tartalékút nem épül hozzá”). Az :699 notes és a :763 alapértelmezése: nincs beviteli elem. A :768 szövege „a saját jegyzetedbe … Nem kell beküldened” (a jegyzőkönyv 4. szakasza engedélyezte). A :792 előírja a teljes RT-P0-24-feltételt. A :794-ből eltűnt a „lehetőleg” és a mentor-mellékmondat; a „kizárólag tanuló-lokális” szó szerint a 2026-10-11-i döntésszöveg (jegyzőkönyv 2. szakasz), nem parafrázis. A MAN:45 LMS-M1-01 javítva. A MAN:308 BSPEC-02 datált kiegészítést kapott, és az állapota változatlanul `BUILD_SPEC_RESOLVED`. Az RA 24. pontjának listájában (ma :105) szerepel az LMS-M1-01, a pont saját LMS-M1-01-mondatot is kapott. A HUM 12. szakasza megvan · A döntés nem tiltja az igazoltan adatmentes beviteli elemet, és ez a szöveg sem tiltja (a verifier korlátja teljesül) · Nyitva maradt, de nem ennek a findingnak a része: a BIZT-G1-3 bizonyíték-kapu (RT-P0-24, DPO QA, BIZT-QA-1), valamint az M1.1-NAR-05 „gépelni” VO-függősége, amelyet a jegyzőkönyv 4.1 pontja rögzít. Javítási teendő nincs.

IMPL-G1-2 · MEGERŐSÍTVE (a 2026-10-10-i szövegen valós volt) · objektív · P1 · RÉSZBEN JAVÍTVA. Az N-M1-04 rész kész: megvan a HUM 12. szakasz (:576–586) a döntéssor és a külön „bizonyíték-kapuja — nyitott” sor, továbbá a `04 Audit` jegyzőkönyv a két 2026-10-10-i és a 2026-10-11-i szöveggel, szó szerint; a mátrixot nem írták át. Ami maradt: a CC-04 és a CC-06 HUM-átvezetése még mindig fennáll, a HUM-fájlban nincs rájuk találat. A jegyzőkönyv 3. szakasza kifejezetten külön tételnek mondja („HUM-fájlba való átvezetésük külön tétel (M0 ERT-8)”) · Ez a rész az M0 ERT-8 nyitott tételéhez tartozik, itt nem kell javítani.

PED-G1-8.obj · MEGERŐSÍTVE · objektív · P2 · FENNÁLL: a HUB:102 szövege „Check: 3 rövid záró kérdés … (besorolás, nem átírás)”, pedig az M1.2:866 Q1 besorolás, a :885 Q2 egy állítás igaz/hamis megítélése, a :906 Q3 fogalmi kérdés · Ugyanaz a hibaosztály, mint a HUB:86-é, amelyet a riport objektívnek validált (ERT-G1-3 obj.). A PED-G1-8 emberi döntése a :93 („4/5”) és a :97/:99 (visszacsatolás, Johari-felidézés) irányáról szól, a :102 tényállítására nem hat. Önállóan javítható · Javítási korlát: csak a :102 zárójele változhat; a legkisebb beavatkozás a „besorolás, ” törlése, a „nem átírás” marad, vagy a lecke saját tagolásának leírása új tartalom nélkül. A :93/:97/:99 és az M1.2 Check-je (kérdések, ✅) érintetlen. A PED-G1-8 döntése utáni hub-szerkesztéssel összevonható, de nem függ tőle.

BIZT-G3-8.obj · MEGERŐSÍTVE · objektív (HUM-PRIV-02, LEZÁRVA, Jóváhagyta: projektgazda) · P2 · FENNÁLL: a HUM:149 szerint „központi média-/felvételi szabály, amelyre minden médiaaktivitás hivatkozik (pl. M0.A, M1.A, …)”, az M1.A-ban viszont nincs ilyen hivatkozás (a „HUM-PRIV-02|fotó|felvétel|megsemmis|Adatvédelem” keresésnek nincs releváns találata) · A lezárt tétel maga nevezi meg az M1.A-t, ezért a hivatkozás átvezetése nem új alkalmazási eset. A DPO-döntéstől csak a cetlik sorsa függ · Javítási korlát: egyetlen képzői megjegyzés az M1.A-ba (4.2.3 vagy az előkészítés), amely a HUM-PRIV-02-re és az `Adatvédelem – tanulói adatok és AI.md` 6. szakaszára (:163) hivatkozik, legfeljebb a szó szerinti alapértelmezéssel: „nincs fotó, videó vagy hangfelvétel, csak indokolt célból”. Tilos bármit állítani a cetlik megőrzéséről, visszaadásáról vagy megsemmisítéséről; tilos a „kézírásos plakát fizikai megőrzése” sort vagy a 30 napos munkalap-szabályt a cetlikre alkalmazni (ez a BIZT-G3-8 nyitott DPO-kérdése); tilos fotót engedni. A cetli-önkéntesség mondatai (M1.A:276–282) érintetlenek.

ERT-G1-11 · ELVETVE · — · P2 · — · Az M1.1:655 állításának lényege igaz („nem azt jelenti, hogy baj van velem”). A „hasznos információ arról, hogy mások hogyan látnak” laza, de nem hamis: a vakfolt tartalma éppen az, amit mások látnak rólam (:665). Bizonyított kulcshiba nincs, ugyanezt a T/F itemet a PED-G1-7 már elvetette, egy answer-key-item átírása pedig item-írási preferencia.

ERT-G2-12 · ELVETVE · — · P2 · — · Az M1.4:491–492 nem mond ellent a KAPU:300 értékelői utasításának, csak nem ismétli meg. A szabály a tanulónak kedvez, a kár nem bizonyított; az „elvesző soronkénti visszajelzés” a KAPU szándékos megoldása (:300, :307). Szükségtelen módosítás a 2026-10-10-i döntés 5. pontja szerint.

ERT-G3-11 · ELVETVE · — · P2 · — · Valós, hogy a KAPU 4. szakaszában csak átment beadványra van minta. A KAPU:255 és a :307 viszont minden próbálkozásra soronként idézett, Megfigyelés → Hatás → Következő lépés szerkezetű visszajelzést ír elő, ebből a bukott sor és a következő lépés kiolvasható (M1.F:163). Egy új bukott minta új értékelési tartalom lenne, nem bizonyított hiba. A rubrika megjelenítését a validált ERT-G2-6 fedi.

ERT-G3-12 · ELVETVE · — · P2 · — · Az M1.B:227 „Sound – hangerő” egy „ha van idő” fogalom-felidéző élő mozgásos kérdés elosztója. Bizonyított hiba nélkül elosztó nem cserélhető (course-content invariáns). Az 5. kérdés „tilos” szava maga a korrigálandó félreértés (:218). Item-írási preferencia.

IMPL-G3-12 · ELVETVE · — · P2 · — · Az M1.F:210 és :243 `review`/`notes` mezője múlt idejű történeti metaadat a v1-ről, ugyanaz a minta, mint máshol (pl. M1.1-IKO-02 `review`). Tanulói, build- vagy manifest-hatás nincs. Higiéniai preferencia, a javítása szükségtelen média-buildet vonna maga után.

IMPL-G3-13 · ELVETVE · — · P2 · — · A `human` provenance címkéje „emberi” (tools/media_manifest.py:139–141), és a kártyák kézzel írhatók vagy rajzolhatók (M1.B:128, :140). Az M1.F-MUNK-01/-02 javítása egyedi tétel volt, nem szabály. Az „emberi-felvétel” megjegyzés 18 fájlban 73-szor fordul elő, ez korpuszszintű minta. Nincs kánoni szabály, amelyhez képest az M1.B hibás volna.

PED-G3-11 · ELVETVE · — · P2 · — · Az átfedést a forrás maga deklarálja és kezeli (M1.A:372: „nagyrészt ugyanazok, mint a mikroleckében. Írj mellé 1–2 újat is”). Az N-M1-05 csak mátrix-hipotézis (audit trail, döntés nincs). Új példamondat vagy helyzetkártya új pedagógiai tartalom lenne; ez preferencia.

PED-G3-12 · ELVETVE · — · P2 (alacsony) · — · Ugyanaz a tényállás, mint a BIZT-G3-6-é (M1.B:385 ↔ M1.A:273–274, :301), amelyet a verifier elvetett: az opcionális, csak pozitív, passzolható „apró visszajelzés” fokozatos nyitás, nem megszegett ígéret · A BIZT-G3-6 elvetett tétel duplikátuma.

Összesítés: 12 tétel. MEGERŐSÍTVE 4 (ERT-G1-1, IMPL-G1-2, PED-G1-8.obj, BIZT-G3-8.obj), ELVETVE 8 (ERT-G1-11, ERT-G2-12, ERT-G3-11, ERT-G3-12, IMPL-G3-12, IMPL-G3-13, PED-G3-11, PED-G3-12), EMBERI DÖNTÉS 0. Bizonyíték-kapu: 0 új (a kapcsolódó BIZT-G1-3, BIZT-QA-1 és RT-P0-24 továbbra is nyitott bizonyíték-kapu).
Állapot a jelenlegi szövegen: ERT-G1-1 JAVÍTVA; IMPL-G1-2 RÉSZBEN JAVÍTVA (az N-M1-04 rész kész, a CC-04/CC-06 HUM-átvezetése az M0 ERT-8-ként fennáll); PED-G1-8.obj és BIZT-G3-8.obj FENNÁLL, mindkettő önállóan javítható a megadott korláttal, az emberi döntésrészük (PED-G1-8 programvezető, BIZT-G3-8 DPO) nyitva marad.
Duplikátum: PED-G3-12 = a BIZT-G3-6 (elvetett) tényállása. A 12 között nincs további duplikátum.
Fájlok:
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md
- 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
