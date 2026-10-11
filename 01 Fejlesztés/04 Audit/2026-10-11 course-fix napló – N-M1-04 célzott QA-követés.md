# course-fix napló — N-M1-04 célzott QA-követés (2026-10-11)

> **Audit trail.** A `fix/m1-privacy-learner-local` ág második `/course-fix` futása: az N-M1-04 első átvezetése
> (`ebf311e`, `c1545c3`) utáni célzott QA findingjainak javítása, a projektgazda 2026-10-11-i végrehajtási
> megbízása alapján (szó szerint: `2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md`,
> 4. szakasz). Commitok: `96996e2` (kánon, jegyzőkönyv, látható-szöveg pin) és `db35119` (`chore(media)`).
> A findingok három körből jönnek: **QA1** az első átvezetés diff-hunkjain (2026-10-11, az előző munkamenet),
> **QA2** e futás javításainak diff-hunkjain, **QA3** a QA2-javítások célzott újraellenőrzése. A nyers
> lencse-kimenetek szó szerint az A. mellékletben. Teljes modul-audit nem futott.

## 1. Tételenkénti állapot

Sorszámok a végállapotban (`db35119`). Rövidítések: M1.1 = `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak
– vakfoltjaim felismerése.md`; RA = `02 Tervezet/LMS – H5P runtime acceptance.md`; JK = a döntési jegyzőkönyv.

| ID | Kör | Állapot | Hely | Megjegyzés |
|---|---|---|---|---|
| NYELV-QA-1 | QA1 | `FIXED` | RA:105 | „ha az e pont szerinti visszaolvasás igazolja” |
| NYELV-QA-2 | QA1 | `FIXED` | M1.1:792 | „a runtime acceptance 24. pontja szerinti teszt … igazolja” |
| NYELV-QA-3 | QA1 | `FIXED` | JK:55 | „hatókörpontjai” |
| IMPL-QA-1 | QA1 | `FIXED` | M1.1:98, :700 | a SLIDE 5-re a tanuló-lokális szabály vonatkozik, nem a RA 6. pontjának általános útjai; az M1.1-IKO-02 `review` mezője igazítva, build |
| IMPL-QA-2 / BIZT-QA-2 | QA1 | `FIXED` | M1.1:768, :793 | a QA1-ben projektgazdai kérdés volt; a projektgazda 2026-10-11-én az N-M1-04 végrehajtásaként felhatalmazta (JK 4.) |
| IMPL-QA-3 | QA1 | `FIXED` | RA:11, :105 | konkrét mentett-állapot tesztlépés; `enablesavestate` és `savestatefreq` az Environment record új sorában |
| IMPL-QA-4 | QA1 | `EXTERNAL` | tracker #2, #3 | GitHub-írás, nem repó-tétel: az LMS-M1-01 a G2/G3b tracker-issue-kba a merge után kerül |
| BIZT-QA-1 | QA1 | `EVIDENCE_GATE` | JK 4.1. | DPO-értékelés: elég-e a három csatorna, vagy az xAPI/LRS, a backup és a kiemelt hozzáférés is kell |
| (ERT-megfigyelés) | QA1 | `FIXED` | M1.1:768, :793 | az IMPL-QA-2 része |
| RT-P0-24 | — | `EVIDENCE_GATE` | RA:153 | `IMPLEMENTATION_TEST_REQUIRED`, a célkörnyezeti futásig |
| NAR-05 „gépelni” | QA1 | VO-függőség | JK 4.1. | a narráció és a hang nem változott; csak a hanggyártás engedélyezett útján |
| ERT (QA2) | QA2 | nincs finding | — | a completion-logika változatlan |
| IMPL-QA2-1 / BIZT-QA2-1 | QA2 | `FIXED` | RA:11, :105 | várakozás a mentési időköznél tovább, pozitív kontroll, nincs szerkesztés a munkamenetek között |
| IMPL-QA2-2 | QA2 | `FIXED` | RA:105 | az eredmény a rögzített beállításokra és verziókra érvényes; státusz-visszaállítás és más leckékre szóló tiltás szándékosan nem került be |
| IMPL-QA2-3 / NYELV-QA2-2 | QA2 | `FIXED` | M1.1:763 | a beviteli elemes változat csak összehangolt, külön rögzített diaszöveggel |
| BIZT-QA2-2 | QA2 | `FIXED` | JK:117–121 | példálózó kiemelt hozzáférés, „ahol releváns”; a BIZT-2 forrása megnevezve |
| NYELV-QA2-1 | QA2 | `FIXED` | M1.1:98 | egyes szám, „lépés” |
| NYELV-QA2-3 | QA2 | `FIXED` | RA:11 | sorcímke: „„Save state” beállítás” |
| NYELV-QA2-4 | QA2 | `FIXED` | RA:105 | „a tanulói tesztfiókból ki kell jelentkezni” |
| NYELV-QA2-5 | QA2 | `FIXED` | JK:124–127 | „ezen az úton kívül nem módosítjuk” |
| IMPL-QA3-1 | QA3 | `FIXED` | RA:105 | „egy másik, nem az első diára átlépve”, utána várakozás |
| IMPL-QA3-2 | QA3 | `FIXED` | RA:105 | a beviteli elem H5P-könyvtárának verziója is rögzítendő; külön Environment record sor nem készült |
| NYELV-QA3-1 | QA3 | `FIXED` | RA:11, :105 | „mentési időköz” |
| NYELV-QA3-2 | QA3 | `FIXED` | RA:105 | „nem szabad szerkeszteni” |
| NYELV-QA3-3 | QA3 | `FIXED` | RA:105 | „Bekapcsolt „Save state” beállításnál” |
| NYELV-QA3-4 | QA3 | `FIXED` | JK:120–121 | „csoporttól független” |

A QA3 javításait a futás a végállapot visszaolvasásával ellenőrizte; negyedik review-kör a projektgazda utasítása
szerint („Do not … create an endless stylistic correction cycle”) nem futott. A NYELV-QA3 két nem nyelvi
megfigyeléséből az elsőt (diák nélküli activity) a „Course Presentationben” megszorítás kezeli; a másodikat (a
böngésző és az eszköz cseréje) a futás nem vezette át, mert az IMPL-QA2-2 a beállításokra és a verziókra szólt.

## 2. Vétólista (adatvédelmi és completion-megfogalmazás)

Answer key, küszöb, ponthatár, rubrikaszint és kötelező/opcionális besorolás nem változott.

| Hely | Előtte | Utána | Alap |
|---|---|---|---|
| M1.1:768 (tanulói szöveg) | „írj rá **2–3 mondatot** (ha szeretnél).” | „írj rá **2–3 mondatot** a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.” | N-M1-04; JK 4. (projektgazdai felhatalmazás) |
| M1.1:793 (completion-sor) | „az is teljesíti a leckét, aki üresen hagyja” | „az is teljesíti a leckét, aki nem ír semmit” | IMPL-QA-2; a logika változatlan (ERT QA2: nincs finding) |
| M1.1:98 (runtime-követelmény) | a megvalósítást a RA 6. pontja dönti el (Moodle-oldali mező is) | a SLIDE 5-re a tanuló-lokális szabály vonatkozik, nem a RA 6. pontjának általános útjai | IMPL-QA-1; N-M1-04 |
| M1.1:763 | — | a beviteli elemes változat csak összehangolt, külön rögzített diaszöveggel | IMPL-QA2-3 |
| RA:105 (24. pont) | „mentett állapot … sem őrzi meg”, tesztlépés nélkül | konkrét eljárás, pozitív kontroll, érvényesség a rögzített beállításokra és verziókra | IMPL-QA-3, IMPL-QA2-1/-2, IMPL-QA3-1/-2 |

„Nem tároljuk” típusú mondat nem került a leckébe; gyermekvédelmi, adatvédelmi és akadálymentesítési kikötés nem
törlődött.

## 3. Ellenőrzések (a végállapoton)

- `content_integrity.py`: 0 ERROR; `--selftest` 57/57.
- `media_manifest.py build` kétszer, azonos hash; `check`, `reconcile` OK (747/747); `validate`, `lint --high-only`
  0 HIGH; `unittest` 159/159, skip nélkül.
- `--pin-visible` a végállapoton (M1.1, RA).
- `git diff --check` a munkafán és az `origin/main...HEAD` tartományon: tiszta.
- `/release-check`: `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`, `LEARNER-RELEASE-VERDICT: NO-GO` (változatlan);
  az `ENVIRONMENT-RECORD` nyitott sorainak száma 18 → 19 (az új sor), a `RUNTIME-TESTS` 36.

## A. melléklet — nyers lencse-kimenetek, szó szerint

A reviewerek kimenete változtatás nélkül; csak a repó abszolút útvonal-előtagja és a munkamenet ideiglenes
területe (`<scratchpad>/`) van rövidítve. A kimenetek modell-kimenetek, nem projektgazdai döntések.

### A.1. QA1 — értékelési lencse (assessment-reviewer)

````text
ERT lencse (értékelés, D1/D3), célzott újraellenőrzés. **Az értékelési lencsén nincs finding.**

A három kérdésre:

1. **Nem változott semmi, amit az értékelés érint.** A completion, a pontozás, a küszöb, az answer key és a kötelező–opcionális besorolás ugyanaz maradt.
   - A manifest :45 Completion oszlopa továbbra is „profil”. A H5P-C profil (manifest :16) „a forrásban előírt interakció(k)” befejezését kéri, és a SLIDE 5-öt a :793 ebből kifejezetten kiveszi.
   - A SLIDE 6 kvízéhez nem nyúlt a javítás. A SLIDE 5 továbbra is opcionális.
   - A régi :792-ből kikerült az Essay kulcsszó-pontozásáról szóló kikötés. Ettől nem lett lazább a szabály: a „Pontozás nincs.” (:792) és a :98 mondata („nem pontozzuk automatikusan”) ugyanezt fedi le.

2. **Az új sorok nem mondanak ellent sem a :80-nak, sem a :793-nak, sem a mikrocélnak (:55).**
   - A :98, :763, :792, :794, a manifest :45 és :308, valamint a runtime acceptance :104 mind ugyanazt mondja: a lépés nem completion-feltétel, alapból nincs beviteli elem, és szöveget nem kell beküldeni.
   - A :793 mondata („az is teljesíti a leckét, aki üresen hagyja”) feltételezi, hogy van mező. Logikailag ez is igaz marad: ha van mező, az üresen hagyás nem akadály, ha nincs, a feltétel magától teljesül.
   - A mikrocél „saját példával illusztrálni” része a SLIDE 5-ben eddig sem volt mért vagy kapuzott. Ezt a javítás nem hozta létre, és az N-M1-04 szerint nem is lehet kötelezővé vagy tárolttá tenni.

3. **A :792 „Pontozás nincs.” és a :793 „Nincs pontszám.” együtt rendben van.** A kettő ugyanazt mondja, egymásnak nem mond ellent. A régi „pontozás nélkül” jelentését pontosan megtartják.

Egy megfigyelés, ami nem értékelési finding, a pedagógiai vagy implementációs lencséhez tartozhat. Két nem módosított, tanulónak szóló sor továbbra is írást vagy gépelést feltételez, holott alapból nincs beviteli elem, és nem mondja meg, hova írjon a tanuló:
- :768 „írj rá **2–3 mondatot**”
- :784 „Ha nem akarsz gépelni”

Ezek a sorok kívül estek ennek az újraellenőrzésnek a körén.

Fájlok:
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
````

### A.2. QA1 — biztonsági lencse (safety-policy-reviewer)

````text
Ez célzott, read-only újraellenőrzés volt, nem új audit. A 10 megadott helyet olvastam: M1.1 :98, :699, :763, :792–794, a tanulói szöveget :767–784 között, manifest :45 és :308, runtime acceptance :104 és :152, HUM :576–586, a jegyzőkönyvet, valamint ellenőrzésképp a HUM-PRIV-01-et (:118–131) és a `RELEASE-READINESS.md` G3b sorát.

**Eredmény:** a módosítás teljesen és torzítás nélkül vezeti át a döntést.
- A módosított sorokban nem maradt „lehetőleg”, mentor-láthatóság, sem Moodle-oldali mező vagy tartalékút.
- Nincs bennük jogalapra vagy megőrzésre vonatkozó állítás, „nem tároljuk” tanulói ígéret, runtime- vagy release-GO.
- A DPO QA és az RT-P0-24 mindenhol nyitott, az RT-P0-24 állapota `IMPLEMENTATION_TEST_REQUIRED` maradt.
- A mentor-láthatóság előzetes jelzése és a `Adatvédelem` §3 hivatkozás azért esett ki, mert a tároló út megszűnt. Ezzel nem veszett el védelmi korlát.

Két kisebb finding maradt.

**BIZT-QA-1** · P2 · Bizalom: közepes
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:104`; ugyanez a minta: `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:792`
- **Probléma:** a döntés általános „adatmentes” működést kér, és a három csatornát csak kötelező minimumként sorolja fel. Az átvezetés ezt a három csatornát elégséges feltétellé teszi. Nincs benne a Moodle-ból kifelé menő xAPI-továbbítás (pl. LRS-plugin), a mentés (backup) és a menedzseri/rendszergazdai hozzáférés. Ez utóbbit a HUM 11. szakasza DPO-kérdésként tartja nyilván (BIZT-2). Hogy ezek valóban adatot hordoznak-e, külső forrással nem ellenőriztem.
- **Bizonyíték:** „csak akkor alkalmazható, ha ez a visszaolvasás igazolja, hogy a beírt szöveg sem a próbálkozás-riportban, sem a mentett állapotban nem marad meg, és tanári vagy mentori tesztfiókkal sem érhető el”. A döntés szövege ezzel szemben: „Interaktív beviteli elem kizárólag igazoltan adatmentes runtime-működéssel engedélyezett.”
- **Javaslat:** EMBERI DÖNTÉS. A DPO-nak a G2 keretében kell eldöntenie, hogy a három csatorna elég-e az „adatmentes” igazolásához, vagy a tesztkört bővíteni kell a felsorolt csatornákkal. Bizonyíték hozzá: a célkörnyezet plugin- és log-leltára. Addig a szövegen nem kell változtatni.
- **Típus:** emberi-döntés

**BIZT-QA-2** · P2 · Bizalom: alacsony
- **Hely:** M1.1 :768 és :774 (változatlan tanulói szöveg) a :792-vel szemben
- **Probléma:** alapértelmezés szerint nincs beviteli elem, a dia mégis írásra kér. A tanuló sehol nem olvassa, hogy a saját jegyzetébe írjon, és hogy a szöveget nem kell beküldenie vagy megosztania. Ez csak a fejlesztői specifikációban szerepel.
- **Bizonyíték:** „Válassz ki **egy** kérdést, és írj rá **2–3 mondatot** (ha szeretnél).” A :792-ben: „szöveget nem kell beküldenie vagy megosztania”.
- **Javaslat:** EMBERI DÖNTÉS. A projektgazdának kell eldöntenie, hogy a freeze alatt is kapjon-e a tanuló egy rövid „saját jegyzetbe, nem kell beküldeni” útmutatást. Ez a már nyitott BIZT-G1-4-hez (a tájékoztató kérdése) kapcsolódik. „Nem tároljuk” mondat nem kerülhet be (runtime acceptance 24. pont, utolsó mondat).
- **Típus:** emberi-döntés

Más finding nincs: a 12. szakasz G2/G3b hivatkozása létező kapukra mutat, és a jegyzőkönyv a szó szerinti forrással egyezik.
````

### A.3. QA1 — nyelvi lencse (hungarian-editorial-reviewer)

````text
Lencse: nyelv. A felsorolt új mondatokban két bizonyítható nyelvi hibát és egy apró helyesírási hibát találtam. A többi sorban nincs nyelvi hiba. A „Moodle/H5P oldalon”, „tanári/mentori”, „bizonyítékkapu marad” fordulatok a projektgazda szó szerinti döntésszövegét követik, ezért nem kifogásolom őket.

**NYELV-QA-1** · P2 · közepes · objektív
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:104`
- **Probléma:** az „ez a visszaolvasás” nem mutat egyértelmű előzményre.
  - A pontban két visszaolvasás áll: a képzői fiókos és a mentett állapoté. Közvetlenül előtte viszont a „beállítás értékéről” szóló mondat van.
  - A lefektetett eljárás csak képzői tesztfiókot nevez meg, ezért a névmás olyan lépésre mutat, amely nem fedi a mentori fiókos ellenőrzést. Ez utóbbi tartalmi jelzés, javaslatot nem teszek rá.
- **Bizonyíték:** „ha ez a visszaolvasás igazolja, hogy […] és tanári vagy mentori tesztfiókkal sem érhető el”
- **Javasolt minimális javítás:** „ha az e pont szerinti visszaolvasás igazolja, hogy …”

**NYELV-QA-2** · P2 · közepes · objektív
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:792`
- **Probléma:** a mondat szerint a dokumentum egy pontja végzi az igazolást a célkörnyezetben. A teszt igazol, nem a specifikáció pontja. A 98. sor ugyanezt helyesen írja: „a célkörnyezet runtime-tesztje igazolja”.
- **Bizonyíték:** „ha a runtime acceptance 24. pontja a célkörnyezetben igazolja, hogy”
- **Javasolt minimális javítás:** „ha a runtime acceptance 24. pontja szerinti teszt a célkörnyezetben igazolja, hogy”

**NYELV-QA-3** · P2 · alacsony · objektív
- **Hely:** `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md:54`
- **Probléma:** egybeírási hiba (AkH 12, 139.): a többtagú összetételt hat szótagig egybeírjuk. A hiba a jegyzőkönyv saját szövegében van, nem idézetben.
- **Bizonyíték:** „A megbízás hatókör-pontjai közül, szó szerint:”
- **Javasolt minimális javítás:** „hatókörpontjai”

Tudatosan nem jelentett, a korpuszban megszokott alakok:
- A „bizonyíték-kapu”, „státusz-szemantika”, „próbálkozás-riport” és „pilot-” kötőjeles írása az AkH 138. szerint egybeírandó lenne. Ezek a korpuszban és a governance-ben rögzült kifejezések, a „bizonyíték-kapu” finding-típusnév is. Egyedileg javítva szétesne az egységes szóhasználat; ha kell, ez korpusz-szintű döntés.
- A HUM 586. sorában a „— nyitott” nagy gondolatjele a 567. sor mintáját követi.
````

### A.4. QA1 — implementációs lencse (implementation-reviewer)

````text
Ezeket olvastam: M1.1:98, :699–700, :763–794 (benne a változatlan dia-szöveg, :765–774); MAN:35, :45, :308; RA:41, :104, :152; HUM:576–586; az N-M1-04 jegyzőkönyv szakaszcímeit; a RELEASE-READINESS G2/G3b sorait; az Adatvédelem :115-öt. Webet nem használtam: új képességállítást nem találtam.

A kereszthivatkozások mind létező célra mutatnak (HUM 12. szakasz, RA 24. pont, LMS-M1-01, RT-P0-24, G2, G3b, jegyzőkönyv 1–2. szakasz). A MAN:308 kiegészítése datált, az állapot nem változott; az RT-P0-24 továbbra is `IMPLEMENTATION_TEST_REQUIRED`. Az RA 24 lefedi a döntés mindhárom vizsgálati elemét. A beviteli elem nélküli alapút egyértelműen építhető, a MAN:35-tel és az RA 6-tal nem ütközik.

**IMPL-QA-1** · P2 · bizalom: magas · M1.1:98, :700
Probléma: Az általános bekezdés a lecke egyetlen szabadszöveges lépésére (SLIDE 5) még Moodle-oldali mezőt kínál, és az RA 6-ra bízza a döntést. A következő mondat ugyanerre a lépésre ezt kizárja, és az RA 24-et teszi mérvadóvá. Az IKO-02 `review` mezője jelen időben szintén az RA 6-ot nevezi meg.
Bizonyíték: „A tényleges megvalósítást (Moodle-oldali szövegmező, H5P **Free Text Question** …) az `LMS – H5P runtime acceptance.md` 6. pontja dönti el” ↔ „Moodle-oldali mező és tartalékút nem épül hozzá”.
Hatás: A fejlesztő ugyanarra a mezőre két döntési pontot lát.
Javaslat: Az általános mondatot úgy kell szűkíteni, hogy a SLIDE 5-re csak az N-M1-04 és az RA 24 vonatkozzon. A `review` mezőt is ehhez kell igazítani, utána a manifestet újra kell generálni. A „Course Presentation dián belüli … nem feltételezhető” kikötés marad.
Típus: objektív

**IMPL-QA-2** · P2 · bizalom: közepes · M1.1:768, :793 (változatlan sorok), a :763/:792-vel szemben
Probléma: Az alapúton nincs beviteli elem, a dia szövege mégsem mondja meg, hová írjon a tanuló, a :793 pedig mezőt feltételez.
Bizonyíték: „Válassz ki **egy** kérdést, és írj rá **2–3 mondatot** (ha szeretnél).”; „az is teljesíti a leckét, aki üresen hagyja”.
Hatás: A tanuló olyan mezőt keres, amely az alapbuildben nincs.
Javaslat: A „saját jegyzetedbe” alapértelmezést át kell vezetni a dia szövegébe és a :793-ba. Az M1.1-NAR-05-VO változatlan marad, „nem tároljuk” típusú mondat nem kerülhet be (RA 24, utolsó mondat), a látható szöveget újra kell pinnelni. Korlát: csak akkor, ha az N-M1-04 freeze-kivétele kiterjed rá; ha nem, a freeze után.
Típus: objektív

**IMPL-QA-3** · P2 · bizalom: közepes · RA:104
Probléma: A feltételes beviteli elem elfogadási feltételének egyik része, hogy a szöveg „a mentett állapotban nem marad meg”. A pont nem rögzíti, melyik fiókkal és hogyan kell ezt visszaolvasni, a beállítás értékét pedig kifejezetten nyitva hagyja.
Bizonyíték: „képzői tesztfiókkal vissza kell olvasni, hogy … mentett állapot (… `mod_h5pactivity/enablesavestate`) sem őrzi meg a szöveget”; „A beállítás értékét a célkörnyezet adja, ez a dokumentum nem rögzíti.”
Hatás: A beviteli elemes változatra nem adható egyértelmű megfelelt/nem felelt meg ítélet. Az alaputat ez nem érinti.
Javaslat: Konkrét tesztlépés kell, például: a tanulói fiók új munkamenetben újranyitja az activityt, az `enablesavestate` értéke pedig az Environment recordba kerül. A tárolási szintű vizsgálat a DPO QA (G2) dolga, nem kell beírni.
Típus: objektív

**IMPL-QA-4** · P2 · bizalom: magas · HUM:586; RA:152
Probléma: Hiányzik az N-M1-04 runtime-bizonyítéka (RT-P0-24 az LMS-M1-01-re) és a DPO QA. A G2 sor nyitott DPO-tételei között az LMS-M1-01 nem szerepel (közepes bizalom: a sor döntéseket sorol, nem QA-t).
Bizonyíték: „| RT-P0-24 | `IMPLEMENTATION_TEST_REQUIRED` |”; „nyitott bizonyíték-kapu (`RELEASE-READINESS.md` G2, G3b)”.
Hatás: Beviteli elemes változat addig nem engedhető. A saját jegyzetes alaputat ez nem blokkolja.
Javaslat: Nem javítható. Az LMS-M1-01-et a G2/G3b tracker-issue-ban (#2, #3) kell rögzíteni, a bizonyítékot nem írjuk be.
Típus: bizonyíték-kapu

Az ellenőrzött fájlok:
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 02 Tervezet/RELEASE-READINESS.md
````

### A.5. QA2 — értékelési lencse

````text
Nincs ERT-QA2 finding. A módosított sorok nem változtatták meg a completion-logikát, a kötelező/opcionális besorolást, a pontozást, az answer key-t és a küszöböt sem.

Mit ellenőriztem:

- **Szöveg és completion összhangja.** Az írás nem feltétel, és a beküldés sem az. Ezt mondja a lecke összes érintett sora:
  - a dia új mondata (:768, „a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.”),
  - a :774-es „Ha nem akarsz írni…” sor,
  - a H5P-beállítás (:792–794),
  - a lecke meta completion-sora (:80, „a saját gondolataid leírása az 5. dián nem feltétel”).
- **A :793 „aki nem ír semmit”** ugyanazt jelenti, mint a korábbi „aki üresen hagyja”, csak a beviteli elem nélküli alapesethez igazítva.
- **A :98 szűkítés tényszerűen igaz.** Az 5. dia a lecke egyetlen szabad szöveges lépése: az 1. és 2. dián önbevallós választás van, a 3., 4. és 6. dián True/False és Single Choice. A runtime acceptance 6. pontja maga is azt írja, hogy a tanuló-lokális lépésekhez nincs Moodle-oldali mező, és ezeket a 24. pont igazolja.
- **Manifest és döntés.** Az LMS-M1-01 sor, a H5P-C completion-profil („Receive a grade”, az összefoglaló dián át) és a HUM 12. szakasz is ugyanezt mondja.
- **A runtime acceptance 24. pontjának új mondatai** (a mentett állapot kijelentkezéses tesztje, az Environment record sora, „nem írja elő”) csak a már meglévő „mentett állapot sem őrzi meg” követelményt teszik végrehajthatóvá. A „completion nem függ tőle” kitétel szövege és jelentése változatlan.

Az érintett fájlok:
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/LMS – activity manifest.md (:16, :45)
- 02 Tervezet/Emberi jóváhagyás szükséges.md (:585–586)
````

### A.6. QA2 — biztonsági lencse

````text
## Biztonsági-jogi célzott QA (QA2): N-M1-04 javítás, csak a diff-hunkok

A négy kérdésből hármat rendben találtam. Két P2 findingot írtam, P0 és P1 nincs.

**Rendben (a végállapot visszaolvasása alapján):**
- **1. A dia szövege.** Az M1.1:768 új szövege („a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.”) pontosan a jegyzőkönyv 4. szakaszában szó szerint idézett felhatalmazást vezeti át, és nem lép túl rajta.
  - Nincs benne „nem tároljuk” vagy más adatkezelési ígéret.
  - Megmaradt az opcionalitás: „ha szeretnél”, és a :774-es sor („Ha nem akarsz írni, fejben is végiggondolhatod.”).
  - A completion nem függ a beküldéstől: a :793-as sor szerint „az is teljesíti a leckét, aki nem ír semmit”.
- **2. A runtime acceptance.** A 24. pont minden korábbi ellenőrzése megmaradt (próbálkozás-riport, mentett állapot, képzői visszaolvasás, tanári és mentori tesztfiók). Az új Environment record sor `RUNTIME_OUTPUT` helyőrzőt tartalmaz, a dátum és a tesztfelelős mezője üres, vagyis nem állít teljesült bizonyítékot.
- **3. A jegyzőkönyv.** A 4.1. szakasz a BIZT-QA-1-et és az RT-P0-24-et (`IMPLEMENTATION_TEST_REQUIRED`) nyitottként rögzíti, és nem hoz új policy-döntést. Egy pontatlansága van, ez a BIZT-QA2-2.
- **4. Törlés.** Nem törlődött gyermekvédelmi, adatvédelmi vagy akadálymentesítési kikötés. Az M1.1:102 kiveszi a diát a 6. pont általános útjai alól, ezzel szűkebb lett a mozgástér, nem tágabb. Az M1.1-ben más szabad szöveges lépést nem találtam.

---

**ID:** BIZT-QA2-1
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, új „A mentett állapot tesztje…” mondat) és a :11-es Environment record sor
- **Probléma:** Az új tesztlépés a kijelentkezést közvetlenül a szöveg beírása utánra teszi, és nem köti a mentési gyakorisághoz. Ha a tesztelő az első mentés előtt kijelentkezik, a szöveg nem töltődik vissza, a teszt mégis sikeresnek látszik. Az Environment record csak a „Save state” értékét kéri, a mentési gyakoriságot (`mod_h5pactivity/savestatefreq`) nem.
- **Bizonyíték:**
  - A repó: „a szöveg beírása után a tanulói tesztfiókkal ki kell jelentkezni, majd egy új, külön munkamenetben újra be kell jelentkezni […] a teszt csak akkor sikeres, ha nem töltődik vissza.”
  - Elsődleges forrás, Moodle (`public/mod/h5pactivity/lang/en/h5pactivity.php`, `savestatefreq_help`): „How often (in seconds) that the user's current state is saved.”
  - Elsődleges forrás, Moodle (`public/mod/h5pactivity/settings.php`): a `savestatefreq` alapértéke `60`, az `enablesavestate`-é `1`.
  - Másodlagos forrás (O. Tacke, snordian.de, „How does resuming an exercise work in H5P?”), óvatosan kezelendő: „When an author edits H5P content that a user has already been working on, then all states that were saved in connection with this content will be reset.” Eszerint a két munkamenet közötti tartalomszerkesztés szintén hamis sikert adhat.
- **Hatás:** Ha egy későbbi build beviteli elemet tesz az LMS-M1-01-re vagy egy másik tanuló-lokális lépésre, a hamisan sikeres mentettállapot-teszt alapján a kiskorú tanuló személyes szövege megmaradhat a mentett állapotban. Az alapértelmezett, beviteli elem nélküli útra ez nem hat, ezért nem P0/P1.
- **Javaslat:**
  - A javítás: a 24. pont új mondata írja elő, hogy beírás után a teszt idején érvényes `savestatefreq` értékénél hosszabb ideig kell várni a kijelentkezés előtt, és hogy a két munkamenet között az activity tartalma nem szerkeszthető. A :11-es Environment record sor rögzítse a `savestatefreq` értékét is.
  - Mihez tilos nyúlni: a 24. pont meglévő ellenőrzéseihez (próbálkozás-riport, mentett állapot, tanári és mentori hozzáférés) és a „csak akkor sikeres” feltételhez.
  - Kérdés a DPO-nak, nem ennek a javításnak a része: elég-e a visszatöltési teszt, vagy a szerveroldali tárolást (xAPI-állapot) is vizsgálni kell. Ez a nyitott BIZT-QA-1 kapuhoz tartozik, ezért itt nem nyitom meg újra.
- **Típus:** objektív
- **Verdikt:**

---

**ID:** BIZT-QA2-2
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md:117-119` (4.1., „Nyitott bizonyíték-kapu — DPO (BIZT-QA-1)”)
- **Probléma:** A 4.1. a projektgazda „privileged access where relevant” fordulatát zárójeles felsorolással adja vissza: „(menedzseri, rendszergazdai)”. Ez kimerítő felsorolásként olvasható, és szűkíti a DPO vizsgálati körét (kimaradhat például a hosting-, adatbázis- vagy mentéskezelői hozzáférés). A „vö. BIZT-2” hivatkozás nem azonosítható egyértelműen: a `04 Audit` mappában több riportban is van BIZT-2 azonosítójú finding, a 4.1. pedig nem nevezi meg, melyikre gondol.
- **Bizonyíték:**
  - A jegyzőkönyv: „a mentések (backup) és a kiemelt (menedzseri, rendszergazdai) hozzáférés is a vizsgálat része (vö. BIZT-2).”
  - Ugyanebben a fájlban, szó szerint: „Keep BIZT-QA-1 open for DPO assessment, including xAPI/LRS, backups and privileged access where relevant.”
  - Ütköző BIZT-2-k: a MAN completion és mentor-láthatóság validált riportjában (2026-10-05), a BSPEC-02 leltáraiban és a BSPEC-01…04 döntésekben (2026-10-04) is szerepel ilyen azonosító.
- **Hatás:** A DPO-kapu hatóköre a projektgazda szövegénél szűkebbnek olvasható, és a hivatkozott előzmény nem visszakereshető. A kapu nyitott állapotán ez nem változtat.
- **Javaslat:**
  - A javítás: a zárójeles felsorolás legyen példálózó („például menedzseri, rendszergazdai”), vagy maradjon a projektgazda fordulata („kiemelt hozzáférés, ahol releváns”). A „vö. BIZT-2” kapja meg a riport fájlnevét. A legvalószínűbb a `2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md` BIZT-2-je, ezt a hívónak ellenőriznie kell.
  - Mihez tilos nyúlni: a 4. szakasz szó szerinti idézetei, a kapu nyitott státusza, és nem kerülhet be új hozzáférési szabály.
- **Típus:** objektív
- **Verdikt:**

Források:
- [Moodle `mod/h5pactivity` settings.php (main)](https://raw.githubusercontent.com/moodle/moodle/main/public/mod/h5pactivity/settings.php)
- [Moodle `mod/h5pactivity` nyelvi fájl (main)](https://raw.githubusercontent.com/moodle/moodle/main/public/mod/h5pactivity/lang/en/h5pactivity.php)
- [snordian.de – How does resuming an exercise work in H5P? (másodlagos)](https://snordian.de/2023/03/04/how-does-resuming-an-exercise-work-in-h5p/)
- [MDL-67789 – Moodle Tracker (a tartalma nem volt lekérhető, nem támaszkodtam rá)](https://moodle.atlassian.net/browse/MDL-67789)
````

### A.7. QA2 — nyelvi lencse

````text
Célzott nyelvi QA, nyelvi lencse. Csak a diff-hunkokat vizsgáltam (`qa2-diff.patch`), a környezetet csak a névmási referencia és az egyeztetés miatt olvastam. Öt findingot találtam, mind P2, P0 vagy P1 nincs.

A dia új mondatával („…a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.”) nyelvileg nincs gond. Természetes, tegező magyar, a „beküldened” személyragos főnévi igenév jó alak. A szövegét a projektgazda engedélyezte, ezt nem vitatom; az NYELV-QA2-2 csak a feltételes mezős úttal való ütközésről szól.

A 24. pontban az „az e pont szerinti visszaolvasás” megszünteti a korábbi „ez a visszaolvasás” névmási zuhanását. A „nem írja elő” csere feloldja a „rögzít” két jelentésének ütközését. A „Course Presentation-verzióval”, a „Moodle-, H5P- és” és a „hatókörpontjai” alak helyes.

---

**NYELV-QA2-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:98`
- **Probléma:** Az új mondat szerint a leckében egyetlen szabad szöveges lépés van, és alapértelmezésben nincs hozzá mező. A közvetlenül előtte álló, változatlan sablonmondat viszont többes számban, létező mezőkről beszél, így a bekezdés számban és állításban is ellentmond önmagának.
- **Bizonyíték:** „a lecke szabad szöveges mezőibe a tanuló **saját, előre nem ismert szövege** kerül, ezért ezek nem kötött megoldású elemek” – „A lecke egyetlen szabad szöveges lépése az 5. dia önreflexiója”
- **Hatás:** A képző vagy a build-felelős azt olvassa ki, hogy a leckében több mező van, és hogy a szöveg bekerül valahová. Ez ütközik az utána álló alapértelmezéssel, hogy beviteli elem nincs.
- **Javaslat:** Javítási korlát:
  - Csak az M1.1 első mondatát kell egyes számra és a „lépés” fogalomra igazítani: egy lépés, alapértelmezésben beviteli mező nélkül.
  - A „nem kötött megoldású” és a „nem pontozzuk automatikusan” állítás tartalma változatlan marad.
  - Ugyanennek a sablonmondatnak az M4.1, M4.2, M6.1, M6.2 és Z.1 leckében álló példányához nem kell nyúlni.
  - Olyan új szöveg nem kerülhet be, amely a kötelezőnek mutatja az írást.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA2-2**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:768`, a változatlan `:763` és `:792` sorral összevetve
- **Probléma:** Ez a szerkesztési szabály 7. regressziós mintája (a feladat szövege és a hozzá tartozó elemek széttartanak). A dia szövege most kizárólag a saját jegyzetes útra szól. A feltételes beviteli elemes út mikroszövege („Ide írj…”) viszont változatlan maradt, és sehol nincs leírva, hogy ezen az úton a dia szövegét is igazítani kell.
- **Bizonyíték:** `:768` „és írj rá **2–3 mondatot** a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.” – `:763` „Szövegmező („Ide írj, ha szeretnél. Elég 2–3 mondat.”) csak … kerülhet a diára.”
- **Hatás:** Ha a build a feltételes beviteli elemmel épül, a tanuló egyszerre két ellentmondó utasítást lát: írjon a saját jegyzetébe, és írjon ide.
- **Javaslat:** Javítási korlát:
  - A projektgazda által engedélyezett, saját jegyzetes dia-szöveg változatlan marad.
  - A `:763` vagy a `:792` sorba egy átvezető kikötés kerüljön: ha a feltételes beviteli elem épül, a „Szöveg a dián” jegyzetes része és a szövegmező mikroszövege együtt igazítandó.
  - A beviteli elemes út új tanulói mondatát a javítás most nem írja meg.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA2-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:11`, a `:105` (24. pont) sorral összevetve
- **Probléma:** Az új Environment record sor a beállítás értékét „mentett állapot … értéke” néven nevezi meg, hiányzik az alaptag („beállítás”).
  - Ugyanebben a dokumentumban a „mentett állapot” a tárolt állapotadatot jelenti („a mentett állapotot … kell visszaolvasni”, „A mentett állapot tesztje”).
  - A 24. pont a sort „A beállítás … értékét … erre szolgáló sorában” fordulattal hívja, de a sorcímkében nincs „beállítás”.
- **Bizonyíték:** `:11` „H5P mentett állapot („Save state”, `mod_h5pactivity/enablesavestate`) értéke a teszt idején” – `:105` „mentett állapot (a célverzió „Save state” beállítása, …) sem őrzi meg a szöveget”
- **Hatás:** Egy fogalomra két megnevezés jut, és egy megnevezés két fogalmat takar. A tesztelő a „mentett állapot értékét” a mentett tartalomnak is olvashatja, nem a beállítás be/ki értékének.
- **Javaslat:** A sorcímke a 24. pont megnevezését kövesse, például: „H5P „Save state” beállítás (mentett állapot, `mod_h5pactivity/enablesavestate`) értéke a teszt idején (24. pont, RT-P0-24)”. Az oszlopokhoz és a 24. pont szövegéhez nem kell nyúlni.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA2-4**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, az új tesztlépés-mondat)
- **Probléma:** A „kijelentkezik” vonzata a magyarban „valamiből”. A „tesztfiókkal kijelentkezni” szerkezetet a dokumentum „X tesztfiókkal + cselekvés” mintája hozta át. A korpuszban máshol a kijelentkezés vonzat nélkül vagy „fiókjával dolgozik” szerkezetben áll (`LMS – hozzáférhetőségi sztenderd.md:57`).
- **Bizonyíték:** „a szöveg beírása után a tanulói tesztfiókkal ki kell jelentkezni, majd egy új, külön munkamenetben újra be kell jelentkezni”
- **Hatás:** A felolvasott tesztlépés kissé idegenül hangzik. Az értelme nem sérül: az „újra be kell jelentkezni” egyértelműen ugyanarra a fiókra utal.
- **Javaslat:** „a tanulói tesztfiókból ki kell jelentkezni, majd egy új, külön munkamenetben újra be kell jelentkezni”. A mondat többi része, a sikerfeltétel („csak akkor sikeres, ha nem töltődik vissza”) is, változatlan marad.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA2-5**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md:123-125` (4.1, VO-gyártási függőség)
- **Probléma:** Elveszett minősítő (2. regressziós minta). A záró tagmondat feltétel nélkül tiltja a kurzusrepóbeli módosítást, pedig az előtte felsorolt engedélyezett út részben a kurzusrepóban fut: ide érkezik a VO fix pack, és itt történik a látható szöveg újrapinnelése. A projektgazda szövege („Do not alter audio outside its authorized pipeline”) csak az úton kívüli módosítást tiltja.
- **Bizonyíték:** „csak a hanggyártás engedélyezett útján (VO fix pack, újrarenderelés, a látható szöveg újrapinnelése) változhat; a kurzusrepóban nem módosítjuk.”
- **Hatás:** Egy későbbi `/course-fix` futás ezt úgy olvashatja, hogy az M1.1-NAR-05 `@source` szövegét VO fix packból sem szabad átvezetni.
- **Javaslat:** „…változhat; a kurzusrepóban ezen az úton kívül nem módosítjuk.” Egyéb változtatás nem kell; a 4. szakasz angol idézetblokkjai érintetlenek maradnak.
- **Típus:** objektív
- **Verdikt:** —
````

### A.8. QA2 — implementációs lencse

````text
## Célzott implementációs QA: 3 finding

A diffben az IMPL-QA-1 javítása rendben van. A :98 és az IKO-02 `review` mezője kizárja, hogy a dia Moodle-oldali mezőt vagy tartalékutat kapjon. Igaz, hogy a lecke egyetlen szabad szöveges lépése az 5. dia: az 1. dián önbevallós választás van, a 6. dián kvíz. Ez összhangban van a runtime acceptance 6. és 24. pontjával és a manifest LMS-M1-01 sorával. A 21. ponttal nincs ütközés, és a Teszt-állapot táblázat is rendben van: az RT-P0-24 `IMPLEMENTATION_TEST_REQUIRED`. Az új diaszöveg nem feltételez Moodle-mezőt, és „nem tároljuk” típusú állítást sem tesz. A :793 egyezik a completionnel és a :80 sorral. A hibák a 24. pont új mentettállapot-tesztjében és a feltételes beviteli elemes változatban vannak.

---

**ID:** IMPL-QA2-1
**Súlyosság:** P1
**Bizalom:** magas
**Lencse:** implementáció
**Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, „A mentett állapot tesztje bármely beviteli elemnél…”) és `:11` (Environment record, új sor)
**Probléma:** Az, hogy a szöveg nem töltődik vissza, egyedül nem igazolja, hogy a mentett állapotban sincs meg. Az eljárás nem ellenőrzi, hogy a kijelentkezés előtt egyáltalán lefutott-e a mentés: alapértékként 60 másodpercenként fut. Azt sem ellenőrzi, hogy a betöltés működött-e: kikapcsolt beállításnál a Moodle egy korábban tárolt állapotot sem tölt be. Így hamis „megfelelt” jöhet ki.
**Bizonyíték:** A repóból: „rögzíteni kell, hogy a beírt szöveg visszatöltődik-e; a teszt csak akkor sikeres, ha nem töltődik vissza.” Moodle `mod/h5pactivity/settings.php`: `'mod_h5pactivity/savestatefreq'`, alapérték `60`; a súgó szövege: „How often (in seconds) that the user's current state is saved.” Moodle `h5p/classes/player.php`, `get_state_data()`: „$savestate = (bool) get_config($this->component, 'enablesavestate'); if (!$savestate) { return $emptystatedata; }”
**Hatás:** Hamis „megfelelt” esetén a :792 és a 24. pont szerint az M1.1 5. diáján beviteli elem alkalmazható lesz, miközben a személyes reflexió szerveroldali xAPI-állapotban tárolódhat. Ez ellentmond az N-M1-04-nek. Ugyanez igaz a 24. pontban felsorolt összes tanuló-lokális lépésre.
**Javaslat:** Négy kiegészítés kell a 24. pont eljárásához:
1. A szöveg beírása után legalább a célkörnyezet `savestatefreq` értékét (plusz ráhagyást) ki kell várni, és át kell lépni egy másik diára, és csak ezután lehet kijelentkezni.
2. Pozitív kontroll: a teszt csak akkor sikeres, ha újranyitáskor a Course Presentation a legutóbb nézett diánál nyílik meg (a CP forrása szerint `previousState.progress`; vagyis az állapotot elmentette és betöltötte), és a beírt szöveg mégsem jelenik meg. Ha bekapcsolt `enablesavestate` mellett az 1. diánál nyílik, az eredmény nem dönthető el: a tesztet meg kell ismételni, és nem „megfelelt”.
3. Az Environment record új sorába a `savestatefreq` értéke is kerüljön.
4. A pont elején álló, képzői fiókos mentettállapot-ellenőrzés hivatkozzon erre az eljárásra.

Ezekhez nem szabad nyúlni: az RT-P0-24 állapota marad `IMPLEMENTATION_TEST_REQUIRED`; runtime-eredményt nem írunk be; a DPO-kérdés (BIZT-QA-1) nyitva marad; a beállítás értékét a dokumentum továbbra sem írja elő.
**Típus:** objektív
**Verdikt:** —

---

**ID:** IMPL-QA2-2
**Súlyosság:** P2
**Bizalom:** közepes
**Lencse:** implementáció
**Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, „A beállítás értékét a célkörnyezet adja, ez a dokumentum nem írja elő; a teszt idején érvényes értékét…”)
**Probléma:** Ha a teszt kikapcsolt mentett állapottal fut, a „nem töltődik vissza” magától teljesül. A 24. pont viszont nem mondja ki, hogy az eredmény csak ennél a beállításnál (és a rögzített verzióknál) érvényes, és hogy a beállítás későbbi bekapcsolása újranyitja az RT-P0-24-et. A Moodle alapértéke ráadásul a bekapcsolt állapot.
**Bizonyíték:** A repóból: „A beállítás értékét a célkörnyezet adja, ez a dokumentum nem írja elő; a teszt idején érvényes értékét az Environment record erre szolgáló sorában kell rögzíteni”. Moodle `settings.php`: `admin_setting_configcheckbox('mod_h5pactivity/enablesavestate', …, 1)`. Moodle `h5p/classes/helper.php`: „if ($component !== null && get_config($component, 'enablesavestate')) { $savefreq = get_config($component, 'savestatefreq'); }”
**Hatás:** Az egyszer igazolt beviteli elem (LMS-M1-01, illetve a többi tanuló-lokális lépés) a beállítás átkapcsolása után is igazoltnak számít, közben észrevétlenül tárolni kezdi a tanulói szöveget.
**Javaslat:** Egy mondattal ki kell egészíteni a 24. pontot: a sikeres eredmény a rögzített `enablesavestate`- és `savestatefreq`-értékre, valamint a rögzített Moodle-, H5P- és Course Presentation-verzióra érvényes. Ha ezek bármelyike változik, az RT-P0-24 visszaáll `IMPLEMENTATION_TEST_REQUIRED` állapotba, és addig a beviteli elem nem alkalmazható, a saját jegyzetes út érvényes. A beállítás értékét továbbra se írd elő.
**Típus:** objektív
**Verdikt:** —

---

**ID:** IMPL-QA2-3
**Súlyosság:** P2
**Bizalom:** magas
**Lencse:** implementáció
**Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:768`, illetve `:763` és `:792`
**Probléma:** A dia új, rögzített szövege csak az alapértelmezett, saját jegyzetes utat írja le. A :763 és a :792 szerinti feltételes, beviteli elemes változathoz a spec nem ad diaszöveget. Abban a változatban tehát a dia a saját jegyzetbe küldi a tanulót, a mező viszont „Ide írj” felirattal ide kéri az írást.
**Bizonyíték:** `:768`: „Válassz ki **egy** kérdést, és írj rá **2–3 mondatot** a saját jegyzetedbe (ha szeretnél). Nem kell beküldened.” `:763`: „Szövegmező („Ide írj, ha szeretnél. Elég 2–3 mondat.”) csak a H5P-beállítás szerinti, igazoltan adatmentes elemként kerülhet a diára.”
**Hatás:** A fejlesztő a beviteli elemes változatban vagy ellentmondó utasítást tesz ki, vagy a pinnelt látható szöveget írja át ad hoc, pin és indoklás nélkül.
**Javaslat:** A :763-hoz (vagy a :792-höz) kell egy build-utasítás. A beviteli elemes változatban a dia „a saját jegyzetedbe” fordulatát a mezővel összehangolt szöveg váltja, például „…a saját jegyzetedbe vagy az alábbi mezőbe…”. Ez látható szöveg változása, ezért a változtatáskészlettel együtt újra kell pinnelni. A másik lehetőség annak kimondása, hogy ez a változat csak külön rögzített diaszöveggel nyitható meg. Változatlan marad az alapértelmezett út, a „Nem kell beküldened”, az opcionalitás, a completion és a mikrocél, és „nem tároljuk” típusú mondat nem kerülhet a dia szövegébe.
**Típus:** objektív
**Verdikt:** —

---

Források:
- [Moodle `mod/h5pactivity/settings.php`](https://raw.githubusercontent.com/moodle/moodle/main/public/mod/h5pactivity/settings.php)
- [Moodle `mod/h5pactivity/lang/en/h5pactivity.php`](https://raw.githubusercontent.com/moodle/moodle/main/public/mod/h5pactivity/lang/en/h5pactivity.php)
- [Moodle `h5p/classes/player.php`](https://raw.githubusercontent.com/moodle/moodle/main/public/h5p/classes/player.php)
- [Moodle `h5p/classes/helper.php`](https://raw.githubusercontent.com/moodle/moodle/main/public/h5p/classes/helper.php)
- [H5P core `h5p.js`](https://raw.githubusercontent.com/h5p/h5p-php-library/master/js/h5p.js)
- [H5P Course Presentation `cp.js`](https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/src/scripts/cp.js)
- [h5p.org – How does saving progress work?](https://h5p.org/node/106535)

A forrásokat a `main` ágon olvastam (a célverziót nem ismerjük). A beállításnevek és az alapértékek a célverzión is visszaolvasandók; ez a 24. pont dolga, a fenti findingok nem állítanak runtime-eredményt.

Fájlok:
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
````

### A.9. QA3 — nyelvi újraellenőrzés

````text
## Célzott nyelvi újraellenőrzés (QA3): eredmény

Mind az öt korábbi finding megszűnt. A javított mondatokban négy új, bizonyítható nyelvi hibát találtam, mind P2. Hárman az RT-P0-24 új tesztlépéseiben vannak, egy a jegyzőkönyv forrásparafrázisában.

A QA2-findingok eredeti szövege nem volt elérhető. A javítás célját a scratchpad `commit1.txt` fájljából vettem.

### Tételenkénti státusz

- **NYELV-QA2-1 — MEGSZŰNT.** M1.1 :98: a mondat egyes számban áll („lépésében … ez nem kötött megoldású elem”). A „megvalósítását” a lépésre mutat, az ellipszis („nem az … általános útjai”) szabályos. Ellenőriztem: az M1.1-ben valóban ez az egyetlen szabad szöveges lépés (a manifest LMS-M1-01 sora is ezt mondja). A „szabad szöveges mezők” többes számú címke 21 leckében azonos sablon, ezért nem finding.
- **NYELV-QA2-2 — MEGSZŰNT.** M1.1 :763: az új mondat egyértelmű. A „lenti „Szöveg a dián”” a közvetlenül alatta álló blokkra mutat, az ellentmondás tényszerű, és nincs benne kitalált indoklás.
- **NYELV-QA2-3 — MEGSZŰNT.** Runtime acceptance :11: a sorcímke már a beállításról szól, nem a mentett adatról. Ugyanez a keverés viszont a 24. pont új mondatában visszatér, lásd NYELV-QA3-3.
- **NYELV-QA2-4 — MEGSZŰNT.** A „tanulói tesztfiókból ki kell jelentkezni” vonzata helyes. „A két beállítás” egyértelműen visszamutat, a két kódkulcs a pontosvessző után meg is van nevezve. Ugyanebben a mondatsorban három új hiba van: NYELV-QA3-1, -2 és -3.
- **NYELV-QA2-5 / BIZT-QA2-2 — MEGSZŰNT.** Jegyzőkönyv 4.1:
  - Visszakerült az „ahol releváns”, a kiemelt hozzáférés példálózó lett („például”), és a BIZT-2 forrása meg van nevezve. A forrást ellenőriztem: `Adatvédelem – tanulói adatok és AI.md` :109.
  - A VO-sorban az „ezen az úton kívül” egyértelműen a „hanggyártás engedélyezett útja”-ra mutat.
  - A parafrázisból viszont kimaradt egy minősítő, lásd NYELV-QA3-4.

### Új findingok

**NYELV-QA3-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, „A mentett állapot tesztje …” mondat)
- **Probléma:** A mondat időtartamot hasonlít gyakorisághoz: egy gyakoriságnál nem lehet „hosszabb ideig” várni, így a várakozás hossza csak a kódkulcsból következtethető ki.
- **Bizonyíték:** „a szöveg beírása után a célkörnyezet mentési gyakoriságánál (`mod_h5pactivity/savestatefreq`) hosszabb ideig várni kell”
- **Hatás:** A várakozás a teszt kulcslépése: ha a mentés nem fut le, az eredmény hamisan „sikeres” (IMPL-QA2-1). A tesztelőnek magának kell kitalálnia, hogy a beállítás értékét mint időközt kell kivárnia.
- **Javaslat:** „…a célkörnyezet mentési gyakoriság-beállításában (`mod_h5pactivity/savestatefreq`) megadott időköznél hosszabb ideig várni kell…”. Ez csak akkor jó, ha a fix forrása (Moodle `mod_h5pactivity` settings.php) szerint az érték időköz. Ha ez nem ellenőrizhető, legyen „…beállítás értékénél hosszabb ideig”. A lépésekhez és a sorrendjükhöz nem szabad nyúlni.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA3-2**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont)
- **Probléma:** A környező tesztlépések mind „… kell” alakúak. Köztük a „nem szerkeszthető” olvasható rendszertulajdonságnak vagy ellenőrizendő eredménynek is, pedig a tesztelőnek szóló előfeltételről (tilalomról) van szó.
- **Bizonyíték:** „A két munkamenet között az activity tartalma nem szerkeszthető.”
- **Hatás:** A tesztelő ellenőrzési lépésnek vagy tényállításnak veheti, és nem tartja be a tilalmat. A mondat célja láthatóan a hamis „sikeres” eredmény kizárása, és éppen ezt gyengíti.
- **Javaslat:** „A két munkamenet között az activity tartalmát nem szabad szerkeszteni.” Ez előfeltétel marad, a jelentés nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA3-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv (D10, terminológia)
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, „Bekapcsolt mentett állapotnál …”)
- **Probléma:** A „mentett állapot” egyetlen mondaton belül két fogalmat jelöl. Először a „Save state” beállítást (az kapcsolható be), utána a tárolt tanulói állapotot. A sorcímkében a NYELV-QA2-3 javítása éppen ezt a kettőt választotta szét.
- **Bizonyíték:** „Bekapcsolt mentett állapotnál a teszt csak akkor értékelhető, ha az újranyitott activity a mentett állapotból folytatódik”
- **Hatás:** Nem egyértelmű, hogy a feltétel a beállításra vagy egy már meglévő mentésre vonatkozik. A szöveg eltér az Environment record sorcímkéjétől („„Save state” beállítás”).
- **Javaslat:** „Bekapcsolt „Save state” beállításnál a teszt csak akkor értékelhető, ha …”, a mondat többi része változatlan. Ugyanebben a pontban a régebbi glossza is így keveri a kettőt: „mentett állapot (a célverzió „Save state” beállítása, …) sem őrzi meg a szöveget”. Erre nem javaslok szöveget, mert az átírás a feltételt értelmezné (beállítás vagy adat).
- **Típus:** objektív
- **Verdikt:** —

**NYELV-QA3-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntés – N-M1-04, M1.1 SLIDE 5 önreflexió.md:120–121`
- **Probléma:** A „vö.” kettősponttal a §3-ra hivatkozik, de a §3 mondatából kimaradt a „csoporttól független” minősítő (2. regressziós minta). Így a BIZT-2 tárgya tágabbnak olvasható: mintha minden szerkesztő tanári, menedzseri és rendszergazdai hozzáférés DPO-kérdés volna.
- **Bizonyíték:** A jegyzőkönyvben: „§3: a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés DPO-kérdése, BIZT-2”. Az `Adatvédelem – tanulói adatok és AI.md:109` szövege: „A szerkesztő tanári, a menedzseri és a rendszergazdai, csoporttól független hozzáférés elfogadhatósága DPO-kérdés (BIZT-2)”
- **Hatás:** A forrásra mutató parafrázis nem egyezik a forrással, és a pontatlan terjedelem átkerülhet a DPO-értékelésbe. Audit trail, kis kockázat. A §11 (:230) is a rövid alakot használja, ezért közepes a bizalom.
- **Javaslat:** „§3: a szerkesztő tanári, a menedzseri és a rendszergazdai, csoporttól független hozzáférés DPO-kérdése, BIZT-2”. A projektgazda szó szerinti idézetblokkjaihoz nem szabad nyúlni.
- **Típus:** objektív
- **Verdikt:** —

### Nem nyelvi megfigyelések az implementációs lencsének

Ezek nem findingok, nem javaslok rájuk szöveget, mindkettő a 24. pontban (:105) van:
1. „A mentett állapot tesztje bármely beviteli elemnél: … át kell lépni egy másik diára”. A felsorolt LMS-M6-01…04 sorok között lehet olyan activity is, amelyben nincs dia (az M6.4 Branching Scenario).
2. A teszthez a böngészőt és az eszközt is rögzíteni kell, de az érvényességet kimondó mondat („csak ezekre a rögzített értékekre és verziókra érvényes; ha bármelyik változik”) ezeket nem említi. Nyelvileg ez következetes, mert az IMPL-QA2-2 a „beállításokra és verziókra” szólt, de hogy a böngésző vagy az eszköz cseréje után kell-e újra tesztelni, azt az implementációs lencsének kell eldöntenie.
````

### A.10. QA3 — implementációs újraellenőrzés

````text
## Célzott újraellenőrzés (QA3), implementációs lencse

Ezeket néztem át: a `qa3-diff.patch` hunkjait, valamint a munkakönyvtár végállapotát a következő helyeken: `02 Tervezet/LMS – H5P runtime acceptance.md` (:11 és a 24. pont, :105), illetve `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md` (:98, :700, :763, :768, :792–794). Elsődleges forrásként a Moodle `MOODLE_405_STABLE` kódját, a H5P Course Presentation és az ExportableTextArea forrását használtam.

### A javított findingok állapota

**IMPL-QA2-1 / BIZT-QA2-1: NEM SZŰNT MEG teljesen.**
- **A mentés még nem futott le:** ez az ág megszűnt. Ha a tesztelő a beírás után a `savestatefreq`-nél tovább vár, legalább egy periodikus mentés biztosan lefut a szöveggel együtt. A Moodle-forrás szerint a `savestatefreq` alapértéke 60, típusa `PARAM_INT`. A mentés „Enable attempt tracking” nélkül nem működik (`validate_state`: `$manager->is_tracking_enabled() && $manager->can_submit($user)`), de a H5P-C profil ezt kötelezően Yes-re állítja (manifest §1, BSPEC-06), ezért itt nincs rés.
- **A szerkesztés miatti állapottörlés:** ez is megszűnt. A H5P core szerint: „When an author edits H5P content … all states that were saved … will be reset.”
- **A betöltés nem működik:** ez az ág egy, az eljárás szövege által megengedett végrehajtásnál nyitva maradt. A pozitív kontroll nem különböztet meg semmit, ha a „másik dia” az első dia (lásd IMPL-QA3-1).
- **Az Environment record :11 sora:** rendben van, mindkét beállítást kéri, és a beállításnevek valósak (`mod_h5pactivity/enablesavestate`, `mod_h5pactivity/savestatefreq`).

**IMPL-QA2-2: MEGSZŰNT** a beállításértékekre, valamint a Moodle-, H5P core- és CP-verzióra nézve. A szándékosan elhagyott státusz-visszaállítást nem kérem számon. Szűkebb maradék rés: a beviteli elem saját H5P-könyvtárának verziója nincs a rögzítendő verziók között, pedig a szöveg ennek a kódjától kerül a mentett állapotba (IMPL-QA3-2).

**IMPL-QA2-3 / NYELV-QA2-2 (M1.1:763): MEGSZŰNT.**
- A beviteli elemes változat most egy további feltételhez kötött: a mezővel összehangolt diaszöveghez. Ez nem ütközik a :792-es ponttal, sem a runtime acceptance 24. pontjával, mert azok szükséges feltételt fogalmaznak meg („csak akkor”), nem elégségeset.
- A „nyitható meg” fordulat ugyanúgy használja az igét, mint a HUM-fájl 586. sora („a saját jegyzetes úton nyílik meg”).

**NYELV-QA2-1 (M1.1:98): implementációs szempontból MEGSZŰNT.** A nyelvi minőséget a nyelvi lencse ítéli meg.
- Az „egyetlen szabad szöveges lépés” állítás egyezik a manifest LMS-M1-01 sorával: csak a SLIDE 5 szerepel benne, és más beviteli lépést a leckében nem találtam.
- A javítás kivette a mondatból a Free Text Question és az Essay megvalósíthatósági kikötését („igazolt host/befoglaló-támogatással” és társai). Ez nem lazít a korláton, mert:
  - itt ezek az utak kifejezetten ki vannak zárva;
  - a kikötések kánonilag a runtime acceptance 6. pontjában maradnak („Az Essay Course Presentationbe ágyazását továbbra sem feltételezzük”);
  - „A Course Presentation dián belüli szabad szöveges mező nem feltételezhető” mondat a blokkban maradt.
- A blokk „szabad szöveges mezők” címkéje 21 leckében azonos, ez szabványcímke, nem egyeztetési hiba.

### Új findingok

**ID:** IMPL-QA3-1
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, „A mentett állapot tesztje …” mondatsor)
- **Probléma:** Ha a tesztelő az első diára lép át, a pozitív kontroll mentett állapot nélkül is teljesül. A Course Presentation állapot nélkül az első dián nyílik, így ilyenkor egy nem működő betöltés mellett is születhet hamis „sikeres”.
- **Bizonyíték:** A fájlban: „és át kell lépni egy másik diára” és „ha az újranyitott activity a mentett állapotból folytatódik (Course Presentationnél az utoljára nézett diánál nyílik meg)”. A h5p-course-presentation forrásában (`src/scripts/cp.js`): `this.currentSlideIndex = this.previousState && this.previousState.progress ? this.previousState.progress : 0;` és `state.progress = this.getCurrentSlideIndex() || null;` A WebFetch-kivonat szó szerint így adta vissza; a teljes nyers fájlt nem ellenőriztem karakterre.
- **Hatás:** Ilyen végrehajtásnál a kontroll nem szűri ki azt az esetet, amikor a szerver elmenti az állapotot, de a betöltés nem működik. Ilyenkor a szöveg a mentett állapotban marad, a teszt mégis sikeres, és az LMS-M1-01 (illetve bármely tanuló-lokális lépés) beviteli eleme jogosulatlanul nyílhat meg.
- **Javaslat:** A mondatban az „át kell lépni egy másik diára” helyett ez álljon: „át kell lépni egy másik, nem az első diára”. Opcionálisan: a diaváltás után is a `savestatefreq`-nél tovább kell várni a kijelentkezés előtt. Indok: a diaváltás csak 3 másodperces mentést ütemez, a lapelhagyáskori mentés pedig „somewhat unreliable” (snordian.de). Ha ott is vár, a mentett pozíció determinisztikusan az utoljára nézett dia lesz. Javítási korlát: a sikerkritérium („a beírt szöveg nem töltődik vissza”), a szerkesztési tilalom, az érvényességi mondat és az LMS-M1-01 mondata változatlan. Státusz-visszaállítás nem kerül be.
- **Típus:** objektív
- **Verdikt:** (verifier)

**ID:** IMPL-QA3-2
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:105` (24. pont, a rögzítési és az érvényességi mondat); ugyanott az Environment record, :9–27
- **Probléma:** Az érvényességi mondat csak a Moodle-, H5P- és CP-verzióhoz köti a sikeres eredményt. A szöveget a mentett állapotba a beviteli elem saját könyvtára teszi (a 24. pont által megnevezett `H5P.ExportableTextArea`), ennek verziója viszont sem itt, sem az Environment recordban nincs rögzítve.
- **Bizonyíték:** A fájlban: „a tesztelt Moodle-, H5P- és Course Presentation-verzióval, valamint a böngészővel és az eszközzel együtt. A sikeres eredmény csak ezekre a rögzített értékekre és verziókra érvényes”. A h5p-exportable-text-area forrásában (`src/eta.js`): `C.prototype.getCurrentState = function () { var text = this.$input.val(); if (text.trim()) { return { answer: text }; } };`
- **Hatás:** Ha a beviteli elem könyvtára frissül, és ettől megváltozik, hogy a szöveget a mentett állapotba teszi-e, a korábbi sikeres eredmény a szöveg szerint továbbra is érvényesnek számít. Ismétlés nélkül olyan build mehet ki, amelyben a reflexió szövege a szerveren tárolódik.
- **Javaslat:** A rögzítési mondatba be kell venni „a beviteli elem H5P-könyvtárának (például `H5P.ExportableTextArea`) verzióját” is, így az érvényességi mondat „bármelyik változik” fordulata erre is kiterjed. Opcionálisan az Environment recordba is kerülhet egy sor az ExportableTextArea-nak, a többi tartalomtípus-sorhoz hasonlóan. Javítási korlát: a teszt sikerkritériuma és a beállítások „a célkörnyezet adja” elve változatlan. Státusz-visszaállítás nem kerül be, és más leckékre szóló tiltás sem.
- **Típus:** objektív
- **Verdikt:** (verifier)

### Szándékosan nyitva hagyott tételek, ezeket nem jelentem újra
- **BIZT-QA-1 (DPO):** ide tartozik az is, hogy a tanulói UI-n végzett visszatöltés-teszt elég-e a szerveroldali tárolás kizárásához.
- **RT-P0-24 runtime-bizonyíték:** `IMPLEMENTATION_TEST_REQUIRED` marad, a HUM 586. sora szerint G2/G3b.

Források:
- [Moodle `MOODLE_405_STABLE` – mod/h5pactivity/settings.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/settings.php)
- [Moodle – mod/h5pactivity/lang/en/h5pactivity.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/lang/en/h5pactivity.php): „How often (in seconds) that the user's current state is saved.”
- [Moodle – h5p/classes/helper.php (saveFreq)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/h5p/classes/helper.php)
- [Moodle – mod/h5pactivity/classes/xapi/handler.php (validate_state)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/classes/xapi/handler.php)
- [Moodle – mod/h5pactivity/mod_form.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/mod_form.php)
- [h5p-course-presentation – src/scripts/cp.js](https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/src/scripts/cp.js)
- [h5p-exportable-text-area – src/eta.js](https://raw.githubusercontent.com/h5p/h5p-exportable-text-area/master/src/eta.js)
- [snordian.de – How does resuming an exercise work in H5P?](https://snordian.de/2023/03/04/how-does-resuming-an-exercise-work-in-h5p/) (H5P core-fejlesztő blogja, nem hivatalos h5p.org-dokumentáció)
- [MDL-67789 (Moodle Tracker)](https://moodle.atlassian.net/browse/MDL-67789): a lap tartalma nem volt elérhető, nem erre építettem.
````
