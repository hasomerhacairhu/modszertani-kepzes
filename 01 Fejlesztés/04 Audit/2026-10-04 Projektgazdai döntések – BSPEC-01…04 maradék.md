# Projektgazdai döntések — BSPEC-01…04 maradék (2026-10-04)

> **Audit trail, nem tananyag.** A projektgazda döntései a BSPEC-01…04 `/course-fix` futás és a célzott
> újraellenőrzés után (napló: `2026-10-04 course-fix napló – BSPEC-01…04.md`). A projektgazda a válaszát a munkamenetben
> írásban adta meg (beillesztett szövegként), majd megerősítette, hogy azok az ő döntései, és rögzíteni kell őket
> (AskUserQuestion: „Igen, rögzítsd”). A döntések szó szerint állnak. A kánoni döntési helyre (`Emberi jóváhagyás
> szükséges.md` 10. szakasz) a következő `/course-fix` vezeti át őket.

**Jóváhagyta:** projektgazda · **Dátum:** 2026-10-04

## Azonosítók

| ID | Tárgy | Kapcsolódó finding |
|---|---|---|
| BS-D1 | a Group-alapú tartalékút elvetése; privacy-safe tartalékút vagy bizonyítottan „nincs tartalékút” | IMPL-3, BIZT-2 (BSPEC-01) |
| BS-D2 | a Q-REL-2 értelmezése: első tanulási lecke vs. a sikerhez kötött downstream activity | IMPL-5 (BSPEC-04) |
| BS-D3 | bukott M7-kapu: LMS-M7-08 = „Még nem teljesítve”; a program-/kurzusteljesítés blokkolva marad | IMPL-4 (BSPEC-01/04) |
| BS-D4 | „nem üres” ≠ „minimálisan értelmezhető tartalom”; ahol nem automatizálható, emberi ellenőrzés | IMPL-8 (BSPEC-02) |
| BS-D5 | az M0 belépőkvíz 4. itemének D) disztraktora javítandó; a helyes válasz és az answer key nem változik | M0 kvíz 4. item |
| BS-D6 | az LMS-Z-06 megőrzése DPO-döntés marad; nem találgatható | BIZT-7 |
| BS-D8 | Z.3 biztonsági lépés: a beküldés kötelező és nem blokkol; külön mentor által elfogadott állapot a végső modul-/kurzusteljesítés feltétele; a Memuna vétója megmarad | IMPL-8, BIZT-6 (BSPEC-02) |

Lezárt projektgazdai döntés a BS-D1…D6 és a BS-D8 (lásd lent, „Második döntési kör”). BS-D7 azonosító nincs.

## Kutatási paraméter — nem döntés

| Mező | Érték |
|---|---|
| exact target Moodle version | `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED` |
| research compatibility range | `Moodle 4.5–5.2` |
| státusz | kutatási tartomány, **nem** lezárt projektgazdai döntés; **nem** kerül át a HUM 10. szakaszába |
| a pontos verzió forrása | a tényleges staging-/célkörnyezetből, G3-bizonyítékként (`LMS – H5P runtime acceptance.md`, Environment record) |

Ezt a sort korábban tévesen BS-D7 azonosítóval, döntésként vettem fel; a projektgazda korrekciója (lent) alapján
visszavonva. BS-D7 azonosító nincs.

## A projektgazda szövege (szó szerint)

> Ne commitolj még.
>
> Jó volt megállni. A jelenlegi munkapéldány addig nem merge-elhető, amíg a BIZT-1 P1 és a BSPEC-01/02 hiányai nincsenek lezárva.
>
> Néhány döntést most lezárok:
>
> 1. **IMPL-3 / BIZT-2: a Group fallback ELVETVE.**
>    Ne kezeld tovább nyitott implementációs opciónak. A HUM-PRIV-01-et nem változtatjuk meg azért, hogy a fallback működjön. Olyan megoldás kell, amelynél a tanulók nem láthatják egymás kapuállapotát vagy csoporttagságát.
>
>    Kutass privacy-safe fallbacket kizárólag a cél Moodle-verzió tényleges, dokumentált képességeiből. Ha nincs biztonságos fallback és a primary út determinisztikus + támogatott, akkor az is elfogadható eredmény, hogy **nincs fallback**, de ezt bizonyítani és dokumentálni kell.
>
> 2. **IMPL-5: nem új döntés.**
>    A Q-REL-2 értelmezése:
>    - bukott kapu után a következő modul első tanulási leckéje megnyílhat;
>    - a sikeres kapueredményhez kötött downstream activity nem nyílhat meg a siker előtt.
>
>    A „downstream feloldás előtt” szövegezést ennek megfelelően tedd egyértelművé minden érintett helyen.
>
> 3. **IMPL-4:**
>    Bukott M7-kapu esetén az `LMS-M7-08` állapota legyen **„Még nem teljesítve”**.
>
>    Ez NEM pass és NEM M7-completion. A Q-REL-2 szerinti következő tanulási rész megnyílhat, de a végleges program-/kurzusteljesítés maradjon blokkolva addig, amíg az M7 korrekció sikeresen le nem zárul.
>
> 4. **IMPL-8:**
>    A pusztán „nem üres” válasz nem bizonyítja a Program terv szerinti „minimálisan értelmezhető tartalmat”.
>
>    Minden érintett mezőnél vizsgáld meg, mi kényszeríthető ki strukturálisan Moodle-ban. Ahol ez nem automatizálható megbízhatóan, ott ne állíts automatikus szemantikai validációt: jelöld a szükséges emberi ellenőrzést. Ez különösen fontos a Z.3 safety lépésnél.
>
> 5. **M0 kvíz 4. item:**
>    A D) disztraktort javítani kell, mert Q-REL-2 után részben igaz.
>
>    A HELYES VÁLASZ és az answer key nem változhat. Csak a hibás disztraktor szövegét módosítsd olyanra, amely Q-REL-2 mellett is egyértelműen téves.
>
>    Ezt projektgazdaként engedélyezem.
>
> 6. **BIZT-7:**
>    Maradjon DPO-döntés. Ne találgasd, hogy az LMS-Z-06 retentionje 90 nap vagy 12 hónap.
>
> Most először fuss egy SZŰK, READ-ONLY `/course-review` kört a BSPEC-01/02 által érintett felületekre és a reviewer által talált tanulói ellentmondásokra.
>
> Minimum scope:
> - M2.1
> - M2.3
> - M3.1
> - M3.2
> - M4.3
> - M4.4
> - Z.3 / LMS-Z-06
> - M1.4 :496
> - M5.3 §3.6
> - M7 KAPU :27/:416
> - M0 kvíz 4. item
> - `LMS – activity manifest.md`
> - `LMS – H5P runtime acceptance.md`
> - az érintett privacy/adatleltár szabályok
>
> A review célja NEM egy új általános course audit. Csak:
> - IMPL-1/2/6/7/9/10/11
> - BIZT-1/3/4/5/6
> - a fenti négy tanulói ellentmondás
> - BSPEC-01 és BSPEC-02 maradék hatóköre.
>
> **BIZT-1-nél külön kutasd ki a cél Moodle-verzióból, hogyan lehet olyan privát szöveges választ megvalósítani, ahol ténylegesen nincs fájl-/kép-/médiafeltöltési vagy embed út.**
> Ne elégedj meg azzal, hogy `File submissions = No`, ha a rich text editorból továbbra is fel lehet tölteni vagy csatolni fájlt.
>
> Vizsgáld meg többek között:
> - van-e core Moodle response/activity konfiguráció valóban file-picker nélküli plain-text vagy korlátozott text inputtal;
> - megoldható-e capability-/editor-konfigurációval activity-szinten, nem veszélyes site-wide hackkel;
> - van-e jobb core activity-típus a jelenlegi TEXT-C helyett;
> - hogyan őrizhető meg a private-by-default és az adatmegőrzési követelmény.
>
> Csak elsődleges Moodle dokumentációval vagy forráskóddal igazolt megoldást fogadj el.
>
> A review után:
> 1. add vissza a teljes finding-listát severityvel;
> 2. külön jelöld, mi objektíven javítható;
> 3. külön jelöld, mihez maradt valódi human/DPO döntés;
> 4. javasolj konkrét megoldást BSPEC-01-re és BSPEC-02-re;
> 5. csak utána fusson új `/course-fix`.
>
> BSPEC-03 és BSPEC-04 jelenlegi megoldását őrizd meg, de most még semmit ne commitolj.
>
> A cél továbbra is:
> `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`
>
> Nem az a cél, hogy a checker zöld legyen bármi áron, hanem hogy ténylegesen buildelhető, privacy-safe és determinisztikus Moodle-spec legyen.

## Megerősítés (AskUserQuestion, 2026-10-04)

- „A beillesztett 1–6. pontot … a te projektgazdai döntéseidként rögzítsem szó szerint a `01 Fejlesztés/04 Audit/` alá a
  review előtt?” → **„Igen, rögzítsd (Recommended)”**
- „Mi a cél Moodle-verzió, amelyre a BIZT-1 … és a privacy-safe tartalékút kutatása szóljon?” → **„Nem ismert: 4.5–5.2
  (Recommended)”** — ez kutatási tartomány, nem döntés (lásd a korrekciót).

## Governance-korrekció (2026-10-04, a projektgazda szövege, szó szerint)

> **BS-D1…D6 marad projektgazdai döntés. BS-D7 viszont ne legyen lezárt projektgazdai döntés.**
>
> A válaszom az volt, hogy a cél Moodle-verzió **nem ismert**, és a kutatást 4.5–5.2 tartományban kell elvégezni. Ez nem azt jelenti, hogy a célverziót 4.5–5.2-re eldöntöttük.
>
> Javítsd az audit trailben úgy, hogy:
>
> - exact target Moodle version: `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED`
> - research compatibility range: `Moodle 4.5–5.2`
> - ez NEM kerül később a HUM 10-be lezárt döntésként
> - az exact verzió majd a tényleges staging/target environmentből lesz G3 evidence.
>
> Commit továbbra se legyen.

A korrekció további utasításai (folyamat): a Moodle-kutatás normál sessionben, read-only, kizárólag elsődleges
forrásból (`docs.moodle.org`, `moodle/moodle` forráskód, hivatalos plugin-metaadat), eredménye dátumozott audit note a
`01 Fejlesztés/04 Audit/` alatt; utána a `/course-review` futások scope-onként külön, a projektgazda által megadott
14 invocationnel; utána egyetlen deduplikált összesítés; csak ezután új `/course-fix`.

## Második döntési kör (2026-10-04, a projektgazda szövege, szó szerint)

A kutatási jegyzet (`2026-10-04 Moodle-kutatás – BIZT-1, GATE_CONFIRMED tartalékút, IMPL-8.md`) után, a 14
`/course-review` futás előtt. A projektgazda a válaszát a munkamenetben írásban adta meg (beillesztett szövegként), az
első kör megerősített gyakorlatával egyezően.

> A kutatási eredmény rendben van. Mielőtt elindítjuk a 14 `/course-review` futást, egy új projektgazdai döntést lezárok.
>
> **BS-D8 — Z.3 safety step completion**
>
> A Z.3-nál külön kell választani a beküldést és a tartalmi elfogadást.
>
> Döntés:
>
> - a tanuló számára a válasz beküldése legyen kötelező;
> - a technikai input legyen privacy-safe és fájlmentes;
> - pusztán a nem üres válasz NEM jelenti azt, hogy a „minimálisan értelmezhető tartalom” teljesült;
> - a beküldés után a tanuló továbbhaladhat, tehát a mentor review nem blokkolja az azonnali downstream learning contentet;
> - legyen külön mentor-reviewed / accepted állapot;
> - ez az elfogadott állapot a végső modul-/kurzusteljesítés feltétele;
> - ha a mentor nem fogadja el, korrekció és újraellenőrzés szükséges;
> - automatikus szemantikai validációt ne találjunk ki;
> - Memuna gyermekvédelmi vétójoga megmarad.
>
> Ezt rögzítsd projektgazdai döntésként a meglévő BS-D1…D6 mellé. A BS-D7 továbbra is csak research constraint, nem döntés.
>
> A Moodle-kutatás következtetéseit egyelőre evidence-ként kezeld, ne automatikusan kánoni implementációként:
>
> 1. **BSPEC-01**
>    Elfogadható végállapot az is, hogy nincs független fallback, ha a primary `GATE_CONFIRMED` implementáció:
>    - core Moodle;
>    - determinisztikus;
>    - 4.5–5.2 kutatási tartományban támogatott;
>    - pontosan specifikált;
>    - runtime-teszttel igazolható.
>
>    Ne gyárts alternatív fallbacket csak azért, hogy legyen.
>
> 2. **BSPEC-02**
>    A Feedback `Longer text answer` jelenleg erős jelölt a fájlmentes core szöveges inputra, de NE cseréld automatikusan minden TEXT-C mezőt Feedbackre.
>
>    A review külön ellenőrizze mezőnként:
>    - learner privacy;
>    - egyéni teacher/mentor review;
>    - szerkeszthetőség / resubmission;
>    - completion semantics;
>    - retention/deletion;
>    - export/hozzáférés;
>    - szükséges visszajelzési workflow;
>    - megfelel-e pedagógiailag az adott activity céljának.
>
>    A Quiz Essay plain csak akkor maradjon jelölt, ha az adott activity assessment-semanticsot igényel. Ne használjuk pusztán technikai workaroundként.
>
> Most indítsd el a scope-onkénti `/course-review` futásokat a korábban felsorolt 14 invocationnel.
>
> Fontos:
> - egy invocation = egy scope;
> - csak a megadott lencsék;
> - ne induljon általános course audit;
> - BS-D1…D6 és BS-D8 lezárt döntés;
> - BS-D7 research constraint;
> - BIZT-7 továbbra is DPO-döntés;
> - a Moodle primary-source research audit note legyen releváns evidence a reviewer számára, ahol a scope indokolja.
>
> A futások végén ne kezdj rögtön javítani.
>
> Előbb készíts egyetlen deduplikált master finding-listát:
> - ID;
> - severity;
> - scope;
> - validált/elvetett;
> - objektív vs human decision vs evidence gate;
> - repo-fixable;
> - melyik BSPEC-et érinti;
> - javasolt implementáció;
> - érinti-e a Moodle-build readiness-t.
>
> Külön adj:
> - végleges BSPEC-01 megoldási javaslatot;
> - végleges BSPEC-02 megoldási javaslatot;
> - minden megmaradó valódi human/DPO/Memuna döntést;
> - minden runtime-only bizonyítékot.
>
> Csak ezt követően induljon az új `/course-fix`.
>
> Továbbra se commitolj.

**Státusz:** a kutatási jegyzet következtetései evidence, nem kánoni implementáció; a BSPEC-01 „nincs független
tartalékút” végállapota a fenti öt feltétellel elfogadható; a BSPEC-02 útját mezőnként, a nyolc szempont szerint kell
eldönteni.
