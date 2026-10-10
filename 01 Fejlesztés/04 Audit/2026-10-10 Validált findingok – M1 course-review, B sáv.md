# 2026-10-10 Validált findingok – M1 `/course-review`, B sáv

> **Mentés:** 2026-10-10, a projektgazda jóváhagyásával: „Írd be a teljes M0 és M1 riportot az `01 Fejlesztés/04 Audit/`
> mappába, változtatás nélkül”. A riport és a mellékletek a munkamenet ideiglenes munkaterületéről, tartalmi változtatás
> nélkül kerültek át.
>
> **Státusz:** audit trail — nem kánon, nem tanulói tartalom. Read-only review; a tananyag nem változott.
>
> **Szerkezet:** I. a validált riport (szó szerint); A. melléklet: a verifier-kontextus (szabályok, klaszter-térkép) —
> a riportban `VERIFY-CONTEXT.md`; B. melléklet: a hat verifier verdiktjei (116/116) — a riportban `VER-V1a.md` … `VER-V4.md`; C. melléklet: a 12 lencse-csoport nyers findingjai (116), elvetett hipotézisei és levágott tételei — a riportban `ALL.md`.
>
> **Gépi normalizálás (tartalmi változás nélkül):** a helyi abszolút útvonal-előtag repó-relatívra rövidítve; a C. melléklet egyetlen relatív Markdown-linkje szóközzel megtörve (`] (`), hogy a link-ellenőrző ne élő linkként kezelje.
>
> **A mentés után, 2026-10-10:** a projektgazda jóváhagyta az N-M1-04 P0 adatvédelmi freeze-kivételét (az ERT-G1-1 (b) és az IMPL-G1-2 átvezetése), külön `/course-fix` futásban; a DPO QA és a runtime-bizonyíték addig nyitott. A projektgazda jelezte továbbá: a PED-G1-4 (M1.2 Mark the Words) és a BIZT-G3-1 (M1.F valós helyzetre utaló instrukció) pilot-besorolását a résztvevők tényleges hozzáférése előtt prioritás szerint meg kell vizsgálni — a lenti riport POST-PILOT besorolása ezeknél nem végleges. A döntés szó szerinti szövege a `/course-fix` döntési jegyzőkönyvébe kerül.

---

# M1 – `/course-review` validált riport (2026-10-10)

> Read-only review. Tananyag nem változott. Nyers findingok: `ALL.md` (116, 12 lencse-csoport), verdiktek:
> `VER-V1a.md`, `VER-V1b.md`, `VER-V2a.md`, `VER-V2b.md`, `VER-V3.md`, `VER-V4.md` (116/116, egyik sem RÉSZLEGES).
> Git-history nem állt rendelkezésre (baseline ismeretlen). A hipotézisek forrása az Anna-mátrix (audit trail, nem kánon).

## 1. Scope és futtatott lencsék

- **Scope:** a teljes M1 — hub, KAPU, M1.1–M1.4, M1.A, M1.B, M1.F — és a rájuk vonatkozó manifest-, runtime acceptance-,
  adatvédelmi és HUM-sorok. Három fájlcsoport: (1) hub, M1.1, M1.2; (2) KAPU, M1.3, M1.4; (3) M1.A, M1.B, M1.F.
- **Lencsék:** pedagógia, értékelés, implementáció, biztonság-jog, fájlcsoportonként (4 × 3 = 12 reviewer). Nyelvi
  lencse nem futott (nem kérték). Hat verifier, témánként.
- **Mérce:** a pilot minőségi küszöbe (2026-10-05, :55–77) és a freeze-kivétel (2026-10-10, :41). A pilot 2026-10-10-én
  elindult, októberben a cohort az M0-val és az M1-gyel foglalkozik: egy M1-es PILOT-BLOCKER azt jelenti, hogy az érintett
  activity nem nyitható meg valódi tanulónak, amíg nincs rendezve. **(a)** = runtime/üzemeltetési/szerepköri lépés,
  freeze-kivétel nem kell; **(b)** = tananyag- vagy build-spec-szöveg módosítása, freeze-kivétel (projektgazdai engedély).
- **N-M1-04:** a projektgazda 2026-10-10-i, szó szerinti döntése (M1.1 SLIDE 5: opcionális, tanuló-lokális, nem tárolódik
  Moodle/H5P oldalon, nem completion-feltétel; ha a H5P ezt nem garantálja, saját jegyzetes, adatmentes út; a runtime-teszt
  és a DPO QA nyitva) lezárt döntésként szolgált mércéül. A repóban még nincs rögzítve.
- **Számok:** 56 megerősítve (ebből 8 bizonyíték-kapu), 36 emberi döntés, 24 elvetve; a lencsék további 13 P2 tételt
  vágtak le. Összevonás után: 25 + 2 objektív sor, 21 emberi döntés, 4 bizonyíték-kapu.

## 2. Validált objektív findingok (25 + 2 P3, duplikátumok összevonva)

| ID (összevont) | Prio | Hely | Probléma | Javítás és korlát | Pilot |
|---|---|---|---|---|---|
| **ERT-G1-1** (=BIZT-G1-2, IMPL-G1-1, IMPL-G1-3, PED-G1-1) | P0 | M1.1:98, :792, :794, :699 (@asset notes); MAN:45, :308; RA:104 | A kánon a N-M1-04-nél gyengébb: „lehetőleg” tanuló-lokális (M1.1:794, MAN:45), a mentor „láthatja” (:794), és ha a teszt nem igazol, a mező Moodle-oldalra, név szerint tárolva kerül (:98, TEXT-C, MAN:24). Az RT-P0-24 listájából (RA:104) és a BSPEC-02 opcionális leltárából (MAN:308) hiányzik az LMS-M1-01. | A döntés **szó szerinti** szövege a :794-be és a MAN:45-be (nem a lencsék „kizárólag…” parafrázisa); a :98 tároló tartaléka helyére a döntés tartalékútja (saját jegyzetes, adatmentes út); a mentor-mellékmondat törlése; RA:104 lista + LMS-M1-01; MAN:308 csak datált kiegészítés (a `BUILD_SPEC_RESOLVED` rekordot nem írjuk át); az @asset notes média-folyamaton át. **Nem használható:** „ide beviteli elem nem épül” — a döntés az igazoltan nem tároló elemet megengedi. Opcionalitás, a három kérdés, a completion változatlan. | **PILOT-BLOCKER (a)+(b)**: (a) az M1.1 SLIDE 5 a pilotban tároló mező nélkül, saját jegyzetes úton nyíljon, amíg az RT-P0-24 nem igazol nem tároló elemet — ehhez szöveg nem kell, a lezárt döntés a forrás fölött áll; (b) a kánoni átvezetés freeze-kivétel |
| **IMPL-G1-2** (=BIZT-G1-1) | P1 | HUM 10–11. szakasz (:494–575); `01 Fejlesztés/04 Audit/` | Az N-M1-04 sem a HUM-fájlban, sem döntési jegyzőkönyvben nincs rögzítve; a mátrix még `UNRESOLVED` P0-ként tartja (MTX:1030). | Új, datált HUM-szakasz + `04 Audit` jegyzőkönyv a szó szerinti szöveggel (a DPO szerepét maga a döntés nevezi meg); a mátrixot nem írjuk át (audit trail). Ugyanebben a lépésben a CC-04 és a CC-06 döntés átvezetése (M0 ERT-8). | PILOT-BLOCKER (b): repó-commit, projektgazdai engedéllyel |
| **PED-G1-4** (=ERT-G1-5) | P1 | M1.2:618, :629, :651 | A Mark the Words utasítása és visszajelzése a jelöletlen részt megfigyelésnek/ténynek nevezi, holott benne általánosítás („Megint”, „végig”, „5 percig sem”) és következtetés („nem készültél”) van — ellentmond a lecke saját definíciójának (:203, :362, :384–392). | Csak az utasítás (:618), a magyarázat (:629) és a visszajelzés (:651) szövege; az 5 célszó, a pontozás és a mondatok változatlanok (mondatcsere = emberi döntés). Pin. | POST-PILOT |
| **BIZT-G3-1** (=PED-G3-1) | P1 | M1.F:270, :276; M1.B:476, :507 | Az M1.F a „terepen tényleg használt” SBI beadását ajánlja az M1.4 kapu-Assignmentbe; ez ütközik a lezárt HUM 8. szakasz :462 sorával („csak kitalált, életszerű eset; valós eset névtelenítve sem”) és az M1.4:457-tel. Az M1.B hurokzárása nem jelzi a korlátot. | Az M1.F:270 és az M1.B:476 mondatába szó szerint az M1.4:457 / M1.3:886 korlátja. A próbálkozás-logika érintetlen. | POST-PILOT (a beadás helyén az M1.4:457 látható tiltást ad) |
| **BIZT-G2-5** | P1 | M1.4:440–510; PT:225; MAN:20 | A Program terv a tényleges Assignment-beadás elé just-in-time adatkezelési dobozt ír elő (mit, mire, meddig, ki látja, kihez fordulhatsz); az M1.4 kapu-Assignment csak a „ki látja” sort tartalmazza (az M3 és az M5 KAPU-ban megvan). | A doboz a §11 szó szerinti soraiból (:243, :250, :252); kontaktot nem találunk ki. | POST-PILOT (a kurzusszintű §11-es tájékoztató lefedi a célt és a megőrzést) |
| **BIZT-G2-3** | P1 | M1.3:914–916 | A tárolt mini-SBI mező melletti megjegyzésből hiányzik a kánoni mondat (Gyermekvédelem §4.1:84; Adatvédelem §11:241: valós gyermekvédelmi helyzetet ne tanulási feladatban jelezz); az M1.4:508-ban megvan. | Szó szerinti átvétel; a BIZT-G2-1 (N-1) és a BIZT-G2-10 döntésével egy lépésben, hogy a blokkot ne kelljen kétszer szerkeszteni. | POST-PILOT |
| PED-G1-3 (=ERT-G3-5) | P2 | M1.1:61, :930 ↔ M1.A:273–274, :299–301 | Az M1.1 kétszer ígéri, hogy a saját vakfolt-reflexiót az M1.A-n a kvucával közösen dolgozzák fel; az M1.A a vakfoltot kifejezetten nem nyitja meg. | Csak a :61 és a :930 hídmondata igazodik az M1.A-hoz. A további javaslatok (új keretező mondat, „Nem esszét” csere) elvetve. Pin; a NAR-06 nem érintett. | POST-PILOT |
| IMPL-G1-6 (=ERT-G1-10, PED-G1-10 obj. rész) | P2 | M1.1:344 ↔ MAN:16 | A SLIDE 2 pontozatlan emoji-skáláját a forrás „Completion”-nek jelöli; a H5P-C profil szerint pontozatlan választó nem completion-elem (a D-d/D-i lezárt elv). | Csak a „(Completion, …)” jelölés cseréje; a mondat többi része változatlan. | POST-PILOT |
| ERT-G1-3 obj. rész (=BIZT-G1-5, IMPL-G1-7) | P2 | HUB:86 ↔ M1.1:857–912 | A hub az M1.1 Check-jét „1 nyitott kérdésnek” írja; a lecke Check-je 3 zárt kvízkérdés. | A HUB:86 a tényleges Check-et írja le. A „6–8 slide” (HUB:81) nem hiba. A 4. kompetencia kérdése: 3. szakasz. | POST-PILOT |
| ERT-G1-7 (csak az M1.2-rész) | P2 | M1.2:775–784 | A D&D „minden kártyához 1 mondatos magyarázatot” ígér; 6 kártyából 3-hoz van megírva. | A hiányzó három magyarázat a lecke meglévő definícióiból; a kártyák és a kulcs változatlanok. Az M1.1 Q2-rész elvetve. | POST-PILOT |
| IMPL-G1-8 | P2 | M1.2:797, :741–791; A11Y:33 | A hozzáférhetőségi sztenderd a Drag & Drop-hoz indoklást kér a fejlesztői megjegyzésben; az M1.2-ben nincs. A felsorolt „legördülő” változat a CP-ben nem beágyazható (semantics.json igazolva). | Indoklás + a megvalósítható húzásmentes út (rádiógombos) megnevezése; a követelmény nem gyengül. | POST-PILOT |
| ERT-G2-6 (=PED-G2-4, IMPL-G2-5 megjelenítési rész) | P2 | KAPU:298 (§5), :255; MAN:50; M1.4:499 | Sem a KAPU §5, sem a manifest nem rögzíti a Moodle-rubrika tanulói megjelenítését (előnézet beadás előtt; soronkénti szint és megjegyzés utána); az M2 KAPU:176 rögzíti, az F-peula erre épít. | A KAPU §5-be és az LMS-M1-05 megjegyzésébe; elsődleges forrásból igazolt beállítás: „Allow users to preview rubric” (alapértéke MOODLE_405_STABLE-ben 1). Tanulói fiókos visszaolvasás: G3b. Rubrika, pontok, küszöb változatlan. | POST-PILOT (a mérce a beadás előtt az Assignment-leírásban látható) |
| ERT-G2-5 (=IMPL-G2-5 szövegrész) | P2 | M1.4:482, :484, :586, :611 ↔ KAPU:55, :67, :75 | A beadás előtt látható tanulói rubrika-összefoglaló két horgonyban eltér a hivatalostól: az S „Erős” szigorúbb, az I „Erős”-ből kimarad a „logikusan következik a B-ből”, a sornév eltér. Az M1.4 maga a KAPU-t nevezi forrásnak (:635). | A cellák a KAPU:55/:67/:75 szövegéhez igazodnak; szintnevek, pontok, küszöb változatlan. Pin. | POST-PILOT |
| ERT-G2-7 (=PED-G2-8) | P2 | M1.4:321–324, :328 ↔ KAPU:134 | A SLIDE 3-on a helyes S-opció az egyetlen időjelölt válasz — pontosan a KAPU által megnevezett hibatípus (a SLIDE 4 és a KAPU Item 1 már javítva). | A disztraktorok időjelölést kapnak, hibatípusuk marad; **a kérdés szövege is a KAPU Item 1 mintáját követi** („csak a helyzetet”), különben a disztraktor tartalmazza a helyes választ. ✅ változatlan; pin. | POST-PILOT |
| ERT-G2-8 | P2 | M1.3:724–736 | „Ebben a mondatban melyik rész…” — a D opció nincs benne a mondatban, felületi alapon kizárható (KAPU:132 elv). | A D törlése (csere csak óvatosan, kétértelmű I-részt hozhat); ✅ és A–C változatlan. Pin. | POST-PILOT |
| BIZT-G2-7 | P2 | M1.3:814 (NAR-04), :750 (spec) | Az 5. dia narrációja és specje „beírást” kér, holott a dián nincs beviteli elem (:799) — ellentmond a lezárt D-1-nek (HUM:522). | A D-1 átvezetése a NAR-04-be. VO-forrás: a VO QA-repó fix packján keresztül. | POST-PILOT (PILOT-4: narráció opcionális) |
| PED-G2-6 (=IMPL-G2-9) | P2 | M1.3:886–887, :1022–1033; MAN:48 | A 6. dia „Másold ki… ezt a mondatot”-ot kér, de nincs előzménye és nincs hová írni; a mező (LMS-M1-07) csak a lecke után nyílik, közben a 7. dia „a saját mondatod” ellenőrzését kéri. | A 6. dia instrukciója helymegjelöléssel (jegyzet/papír most, a mező a lecke után). A „név és felismerhető részlet nélkül” és az „oda már csak kitalált” kitétel szó szerint marad; az N-1-et nem érinti. | POST-PILOT |
| IMPL-G2-1 | P2 | KAPU:303–305 ↔ MAN:51, :167–171; KAPU:5 | A KAPU §5 a kapueredmény rögzítését nyitott, acceptance-teszten eldöntendő kérdésként kezeli, és nem nevezi meg a már rögzített `GATE_CONFIRMED_M1`-et (LMS-M1-06, GATE-CP; BS-D1 lezárt, tartalékút nincs). (Az F-peula-út nem ellentmondás: a MAN:20 és az RA:90 szerinti.) | A :304 a manifest szerint; a további próbálkozás „Manually” módja a 2026-10-02-i döntésből levezethető. Küszöb, F-peula-kötelezettség változatlan. | POST-PILOT |
| IMPL-G2-6 (+ levágott PED-G2-11) | P2 | M1.4:18, :153, :309, :655 | A mini-kvíz típusa „Course Presentation vagy Question Set” — a Question Set nem hordoz hangot és nem kérdés jellegű diát (semantics.json igazolva); a :153 a típust a runtime acceptance-re bízza, ott nincs M1.4-tétel. | Csak „Course Presentation”; az RA-ba M1.4-tétel vagy a D-d/D-i elv átvezetése. A javasolt „Specific slide number” megvalósítás kitalált, nem használható. Kérdések, opciók, ✅ változatlanok. | POST-PILOT |
| IMPL-G2-7 | P2 | M1.4:446 ↔ MAN:49–50 | A kapu-Assignment címe a lecke címe, majdnem azonos a H5P-activity nevével; a manifest neve „M1.4 – SBI-beadandó” (a tanulói szöveg :27 már ezt használja). | A §3.1 „Cím” sora a manifest-név. Pin. | POST-PILOT |
| ERT-G3-1 (=PED-G3-2 (a)) | P2 | M1.F:277; :349–365 ↔ KAPU:24, hub:258, :223 | A kötelező F-peula „facilitált, strukturált javítási alkalom” (KAPU:24, hub:258), de a csendes blokkban a képző csak technikai segítséget ad; a javított vázlatot senki nem nézi át a rubrika szerint, a hub:223 lépése hiányzik. | Az M1.F:277 körbejárása a bukott tanulók vázlatára rövid M→H→K visszajelzést ad (hub:257). Az M1.F:54 cél önálló átírása és a 4.4-be emelés K21-terület; a hangnem-kulcspont (PED-G3-2 (b)) elvetve. 45’ és safer-working (M1.F:95) változatlan. | POST-PILOT |
| IMPL-G3-3 (=ERT-G3-4, PED-G3-3) | P2 | M1.B:148, :214, :218, :241, :495; :69, :86 (@asset KART-02) | E-M1-069 maradvány: a kvíz négysarkos, de a tér-előkészítés és a checklist „A/B sarkot” ír, a KART-02 a 3 smiley-t ajánlja sarokjelölőnek, a MAG-címke (:218) a régi 4. kérdést nevezi meg. | A látható sorok pinnel, az @asset-metaadat build-del; ✅, kérdések, opciók változatlanok. Új „→” visszajelzés és eszközlista-bővítés nem kell. | POST-PILOT |
| BIZT-G3-7 | P2 | M1.F:36 ↔ :313 | Fájlon belüli ellentmondás: „Nem tesszük ki névvel, hogy ki hol tart” ↔ Opció 2 nyilvános jelentkezése („Ki az, aki inkább a Joharinál akadt el?”). | Csak az Opció 2 igazodik a :36-hoz; a képző privát követése (:36) marad. | POST-PILOT |
| PED-G3-8 | P2 | M1.F:47 ↔ KAPU:24, hub:258 | „Létszám: 6–20 fő” ↔ „egyéni vagy kiscsoportos támogatás”; 1–3 résztvevőnél a név nélküli gyűjtés gyakorlatilag azonosít. | Az eltérés valós, de a javaslat nem használható: a kánon nem ad létszámot, a kis létszámú változat új tartalom — a modulgazda írja meg. A safer-working mondat a :95-ben megvan. | POST-PILOT |
| BIZT-G3-4 | P2 | M1.A:477, :484–486 | A „személyesebb” kiscsoportos reflexió (saját sértő visszajelzések) passzt nem kínál, csak könnyebb sztorit; a §4:61 szerint indoklás nélküli passz jár. | A §4.3 „Mondhatsz passzt” fordulatának szó szerinti átvétele. | POST-PILOT |

**P3 (a következő érintő szerkesztésbe csomagolva):** IMPL-G3-4 (=ERT-G3-9, PED-G3-4) — az M1.B 4.1.1 fejenkénti
smiley-felmutatást kér, az eszközlista és a KART-02 3 képzői kártyát ír (M1.B:192, :203 ↔ :70, :74, :140–143, :186, :491;
az eszköz igazodik az élő instrukcióhoz). IMPL-G3-9 — M1.F:171–172 kemény sortörés két sorvégi szóközzel (`course-content.md`:60);
a megjelenítést nem rontja.

## 3. Emberi döntést igénylő tételek (21) — javasolt szöveg nélkül

| ID | Kérdés | Ki dönt | Pilot |
|---|---|---|---|
| **BIZT-G2-1** (+ levágott PED-G2-12) | N-1: kerülhet-e az LMS-M1-07 (M1.3 saját mini-SBI, tárolt, névhez kötött TEXT-C) mezőbe valós, névtelenített helyzet, vagy – mint az M1.4-ben – csak kitalált? (MAN:48: nyitott; BSPEC-02 leltár :244/:278: learner-release emberi döntés.) | projektgazda; vétó: DPO | **PILOT-BLOCKER** az LMS-M1-07 megnyitására; a döntéshez szöveg nem kell, „csak kitalált” esetén a szöveg igazítása freeze-kivétel |
| PED-G2-1 (=ERT-G1-4, ERT-G2-3, ERT-G3-7) | Az SBI kánoni hossza: 2–3 mondat (PT:106/:138/:142, hub:33/:39/:125, KAPU:21/:197) vagy 1–2 (M1.3:45/:801, M1.4:10/:450, M1.B:359, KAPU 4.1 minta)? A rubrika a hosszt nem pontozza. Lezárt döntés nincs. | projektgazda / modulgazda + értékelési felelős | POST-PILOT |
| ERT-G2-1 (=PED-G2-2) | A M1.4:475–476 kész SBI a B kapuhelyzetre: kapjon-e a KAPU §5 értékelői szabályt a minta (közel) szó szerinti visszaadására, és cserélődjön-e a példa? A példacsere önmagában nem elég (a saját helyzetes út, M1.4:457). | értékelési felelős; QA: módszertani lektor | POST-PILOT; **a pilot alatt repón kívüli értékelői utasítással kezelhető** |
| ERT-G2-2 (=PED-G2-7) | A B-sor („becsúszik egy ítélkező szó”) és a hangnem-sor („enyhe minősítés”) ugyanazt vonja-e le (KAPU:126 „nincs kettős súlyozás”), és a 4.1 határeset-minta „kissé minősítő” B ↔ „nincs címke” hangnem indoklása melyik? A HUM 8. szakasz csak a szintneveket zárja le. | értékelési felelős + módszertani lektor | POST-PILOT; **a pilot alatt értékelői kalibrációs egyeztetés kell** (téves bukásnál a második értékelő, KAPU:25) |
| ERT-G1-3 (=PED-G1-5) | A hub 4. kompetenciájának „záróreflexiós” produktuma sehol nincs: képeződjön le meglévő elemekre (és kerüljön ki a „reflexiós produktum” kitétel), vagy legyen új lépés? Tárolt produktumként új adatkör (HUM-PRIV-01/DPO), freeze alatt nem. | programvezető; DPO, ha tárolt | POST-PILOT |
| IMPL-G2-2 | Az LMS-M1-05 (ASSIGN-M) saját completion-beállítása nincs rögzítve; kiterjeszthető-e a D-h kétállapotú mintája (SUBMITTED / CONFIRMED) az ASSIGN-M sorokra? A D-f szó szerint nem fedi. | projektgazda / build-spec gazda | POST-PILOT (az M2-nyitás az LMS-M1-06-hoz kötött) |
| BIZT-G2-4 (=IMPL-G2-3 döntési rész) | Az M1.4:502 „a kijelölt mentorod/értékelőd látja”; az ASSIGN-M csoport szerinti szűkítése (BIZT-5) és a szerkesztő tanári/menedzseri hozzáférés (BIZT-2) nyitott (ADV:104, :117). A mondatot a döntés előtt nem írjuk át. | DPO | POST-PILOT döntésként; a láthatóság visszaolvasása a BIZT-G2-2 kapuban PILOT-BLOCKER |
| ERT-G2-4 (=PED-G2-3, IMPL-G2-8) | A KAPU §3 item-bankja tanulói activity (manifest-sor: profil, completion, privacy a szabad szöveges Item 5–6-ra) vagy szerzői itempool (a KAPU:11/:28/:200/:308 igazodik)? | projektgazda + értékelési felelős; DPO, ha activity | POST-PILOT |
| PED-G1-8 (=ERT-G1-8) | A hub M1.1→M1.2 visszacsatolást és Johari-felidézést ígér (HUB:97/:99), és „4/5”-öt mér (HUB:93); a leckében egyik sincs. Bekerüljön (Moodle-intróba), vagy a hub igazodjon? Objektív rész: a HUB:102 „besorolás” csak a Q1-re igaz. | programvezető | POST-PILOT |
| PED-G3-9 (=ERT-G3-8, ERT-G3-10, IMPL-G3-5, IMPL-G3-6, IMPL-G3-7) | Modulon belül a hub vagy a részletes peulafájl az irányadó? Három eltérés: M1.A percbontás (hub:147–151), M1.F fogalomtérkép-poszter és „cél 4” (hub:172–203, :221–222; asset forrás nélkül), M1.B-végi analitikai kérdés (hub:275–278). Szabály/lezárt döntés nincs; a „Rövid percbontás-vázlat” címke és a hub:196 a peulafájl felé mutat, de nem kodifikál. | modulgazda / programvezető (a poszterről médiafelelős) | POST-PILOT |
| IMPL-G3-8 | A PT:219 minden modulban „Peulák” és „Extra / F-peula” Moodle-blokkot ír, a manifest egyiket sem (MAN:114, :248). Programszintű 1↔2. forrás ütközés, az N-M4-07-hez kötött (vö. M0 IMPL-2). | programvezető + build-felelős | POST-PILOT |
| IMPL-G2-10 | Az M1.4 kapu fájlos útjához nincs „Accepted file types” / fájlszám (üres mező = minden típus, docs.moodle.org/405). Mi legyen, figyelve a „két egyenértékű út” akadálymentességére? Korpusz-szintű hiány. | LMS-gazda + DPO + hozzáférhetőségi gazda | POST-PILOT |
| IMPL-G1-5 (=BIZT-G1-6, PED-G1-10 tárolási rész) | Az M1.1 SLIDE 1–2 érzelmi önbevallásának választós tartalékútja követett H5P-C-ben tanulónként rögzítene, a próbálkozás-riportot a nem szerkesztő tanár is látja (ADV:115). Megengedett-e? (A D-d/D-i csak a completiont rendezi, a D-j és az N-M1-04 más elemre szól.) | DPO | POST-PILOT; a build a forrás elsődleges, nem rögzítő útját (szöveg + Tovább) követheti, szöveg nélkül |
| BIZT-G1-4 | Kapjon-e az M1.1 SLIDE 5 a mező előtt feltárást a Memunához irányító mondatot (a Z.2:307 mintájára)? A „csak nálad marad” mondat az RA:104 szerint a visszaolvasásig tilos. | Memuna | POST-PILOT (az M1.1:90 segítő blokk megadja a passzt és a gyermekvédelmi utat) |
| BIZT-G1-7 (=PED-G1-9) | Az M1.1:926 a (kiskorú) madrih önfeltárását a kvucához való közelség eszközeként keretezi, határ-mondat nélkül; kell-e határ az M1.A:282 mintájára? Az M1 nincs a Memuna G1-hatókörében (GK:17). | Memuna + szakmai lektor | POST-PILOT |
| BIZT-G2-10 | Az M1.3:914–916 és az M1.4:506–507 egyedi „ha nagyon nehéz helyzet” szövege kiváltandó támogató blokk (§4.3:102), vagy feladatszintű adattakarékossági utasítás? Az M1.4:508 Memuna-mondata semmiképp nem törölhető. | Memuna | POST-PILOT |
| BIZT-G2-6 | A KAPU:27 előírja az eszkalációt, de nem mondja meg, ki és hogyan veszi ki a feltárást tartalmazó beadványt (ADV:75), mi lesz a kapueredménnyel, és mi az alternatív beadási út (az M3-ra N-9-ként nyitott). | Memuna + DPO; értékelési felelős | POST-PILOT (az azonnali út helyes) |
| BIZT-G3-8 | Mi lesz az M1.A önfeltáró Johari-cetlijeivel a peula után, és fotózható-e a tábla? A HUM:149 (HUM-PRIV-02) az M1.A-t felsorolja, a peulában nincs hivatkozás (ennek átvezetése objektív). | DPO | POST-PILOT |
| BIZT-G3-2 | A peulák képzői in-the-moment utasításának (M1.A:503–505, M1.B:389–391, M1.F:107) szó szerint át kell-e vennie a HUM-SAFE-03 facilitátori minimumát (felkavart kiskorút nem küldünk ki egyedül; felnőtt marad vele), vagy elég a képzőképzés (HUM-SAFE-05)? Ellentmondás nincs. | Memuna | POST-PILOT |
| BIZT-G3-5 | A „név és felismerhető részlet nélkül” korlát kiterjedjen-e a szóbeli peula-példákra (M1.A:372 „a saját kvucádra szabva”, M1.B:157)? | Memuna + DPO | POST-PILOT |
| BIZT-G3-9 | Kell-e az M1.B 4.4.2 terepi SBI-vállalásához „valódi gyermekvédelmi aggálynál vond be a Memunát” utalás? Az M1.4:508 ugyanennek a tanulónak kimondja. | Memuna | POST-PILOT |

## 4. Bizonyíték-kapuk (4) — nem mennek `/course-fix`-be

| ID | Mi hiányzik | Szerep / kapu | Pilot |
|---|---|---|---|
| **BIZT-G1-3** (=IMPL-G1-4, PED-G1-2, ERT-G1-2 SLIDE 5-része) | N-M1-04: az M1.1 H5P-C activity a SLIDE 5 szövegét nem tárolja-e — próbálkozás-riport, mentett állapot (`enablesavestate`), mentori hozzáférés, completion-függetlenség. A H5P-C-ben az attempt tracking be van kapcsolva (MAN:16), a Moodle a választ adatbázisba menti (`save_statement()`, MOODLE_405_STABLE igazolva). RT-P0-24 `IMPLEMENTATION_TEST_REQUIRED`; DPO QA nyitva. | LMS-gazda (RT-P0-24, G3b); DPO (G2) | **PILOT-BLOCKER (a)** a SLIDE 5 beviteli elemére: addig saját jegyzetes, adatmentes út; beviteli elem nélkül a hiányát kell rögzíteni (RA:104) |
| **ERT-G1-2** (többletrész) | Az M1.1–M1.2 completion/unlock runtime-ja: a SLIDE 1–2 pontozatlan választói, a CP-completion, az M1.2 húzásmentes útja (RT-P0-09, -13, -14). | LMS-gazda · G3b | **PILOT-BLOCKER (a)** (pilot-küszöb: „törött prerequisite/completion/unlock”) |
| **BIZT-G2-2** (+ IMPL-G2-3 visszaolvasása) | Az LMS-M1-05 (kapu-Assignment) és az LMS-M1-07 (mini-SBI) adatkezelési bizonyítéka: DPO-jóváhagyás (ADV:230 — előtte nem élesíthető; §9 :207/:209), RT-P0-15 láthatósági visszaolvasás két mentorral, két csoporttal, tesztfiókkal (kit lát a nem szerkesztő tanár). Ha a teszt szerint más mentor is látja a beadást: P0. | DPO (G2); LMS-gazda (RT-P0-15, G3b) | **PILOT-BLOCKER (a)**; tananyag-módosítás nem kell. Ha a repón kívül megvan, elég rá hivatkozni |
| **IMPL-G2-4** (+ IMPL-G3-2) | A kapumechanika runtime-ja: RT-P0-08 (a 0/1/2/2 = 5 negatív eset, GATE-CP állapotmátrix), RT-P0-19 (javító próbálkozás nem indul az F-peula előtt, kézi nyitás, a legjobb megerősített eredmény számít; az „Allowed attempts” értéke — a repóban sehol nincs, 2 esetén az M1.B önkéntes újrabeadása beragad), RT-P0-01 (Max grade 8, Grade to pass 5), RT-P0-09 (LMS-M1-03 → -07 → -04 → -05 lánc). | LMS-gazda · G3b | **PILOT-BLOCKER (a)** az M1-kapu és az M2-nyitás előtt; freeze-kivétel nem kell |

## 5. Elvetve (24)

- **P1 (5):** ERT-G1-6 (a „háromszor”-jel és az abszolút disztraktorok a tanított szabályt alkalmazzák); ERT-G3-3 (az
  M1.B trió-checklist a saját deklarált célját követi, a háromfokú átalakítás preferencia; társa a P2 PED-G2-5);
  BIZT-G3-3 (a cetliket a teljes csoportnak tették láthatóvá, név nélküli felolvasás, szabálysértés nem igazolható; társa a
  P2 PED-G3-10); ERT-G3-2 (a Blokk 3 a kapus hiányokra fókuszál, a hangnem lényegét a „címke = ítélet” fedi); IMPL-G3-1
  (az F-peula „jelenléti completion” útja szó szerint a lezárt 2026-10-02-i döntés — MAN:20, :149, RT:90 —, a MAN:248
  kezeli).
- **P2 (19):** ERT-G1-9, IMPL-G1-9, IMPL-G1-10, PED-G1-6, PED-G1-7, PED-G2-5, ERT-G2-9, ERT-G2-10, PED-G2-9, BIZT-G2-8,
  BIZT-G2-9, PED-G3-10, BIZT-G3-6, ERT-G3-6, PED-G2-10, IMPL-G3-10, PED-G3-5, PED-G3-6, PED-G3-7 — preferencia, a
  forrásban már kezelt kérdés vagy nem bizonyított kár (indoklás a `VER-*.md` fájlokban).
- **A lencsék levágtak 13 P2-t** (ERT-G1-11, ERT-G2-11, ERT-G2-12, ERT-G3-11…13, IMPL-G3-11…13, PED-G2-11, PED-G2-12,
  PED-G3-11, PED-G3-12); közülük öt beolvadt egy megtartott tételbe (ERT-G2-11 → BIZT-G2-7, PED-G2-11 → IMPL-G2-6,
  IMPL-G3-11 → PED-G3-8, ERT-G3-13 → IMPL-G3-9, PED-G2-12 → BIZT-G2-1).

## 6. Következő lépés

**A futó pilothoz, az érintett activity megnyitása előtt (repóváltozás nélkül):**
1. LMS-gazda, pilot-Moodle: az M1.1 SLIDE 5 tároló mező nélkül, saját jegyzetes úton (ERT-G1-1 (a)); RT-P0-24 (BIZT-G1-3);
   az M1.1–M1.2 completion/unlock (ERT-G1-2); RT-P0-15 láthatóság az LMS-M1-05/-07-re (BIZT-G2-2); RT-P0-01/-08/-09/-19 és az
   „Allowed attempts” értéke (IMPL-G2-4) — az M1-kapu és az M2-nyitás előtt.
2. DPO: az LMS-M1-05/-07 jóváhagyása (BIZT-G2-2); a N-M1-04 DPO QA-ja (nyitva marad a bizonyítékig).
3. Projektgazda (DPO-vétóval): N-1 (BIZT-G2-1) — addig az LMS-M1-07 nem nyitható meg valódi tanulónak.
4. Értékelési felelős: kalibrációs egyeztetés a pilot-értékelőkkel (ERT-G2-2) és értékelői utasítás a mintamásolásra (ERT-G2-1).

**Freeze-kivételhez kötött tananyag- és spec-módosítás** (projektgazdai engedély): az N-M1-04 kánoni átvezetése
(ERT-G1-1 (b), IMPL-G1-2) — P0 adatvédelmi, a freeze-kivétel feltételét teljesíti; a BIZT-G2-1 szövege, ha a döntés
„csak kitalált”; a BIZT-G2-2 nyomán, ha a visszaolvasás szerint más mentor is látja a beadást.

**POST-PILOT `/course-fix`** (a pilot-visszajelzéssel együtt): PED-G1-4, BIZT-G3-1, BIZT-G2-5, BIZT-G2-3, PED-G1-3,
IMPL-G1-6, ERT-G1-3 (obj.), ERT-G1-7, IMPL-G1-8, ERT-G2-6, ERT-G2-5, ERT-G2-7, ERT-G2-8, PED-G2-6, IMPL-G2-1, IMPL-G2-6,
IMPL-G2-7, ERT-G3-1, IMPL-G3-3, BIZT-G3-7, PED-G3-8 (szöveg: modulgazda), BIZT-G3-4; P3: IMPL-G3-4, IMPL-G3-9.
**VO-fix pack** (a VO QA-repón át): BIZT-G2-7. **Átvezetés** (objektív): N-M1-04, CC-04, CC-06 a HUM-fájlba és döntési
jegyzőkönyvbe.

---

# A. melléklet – verifier-kontextus

# M1 verifier — kontextus és klaszter-térkép (fő munkamenet, 2026-10-10)

A findingok hat verifier-bemenetben vannak ugyanebben a mappában: `V-V1a.md` (21), `V-V1b.md` (16), `V-V2a.md`
(23), `V-V2b.md` (10), `V-V3.md` (21), `V-V4.md` (25); összesen 116 finding a 12 lencse-csoportból (4 lencse × 3
fájlcsoport). A teljes, csoportonkénti nyers anyag (a lencsék „Elvetett hipotézisek” és „LEVÁGVA” részeivel):
`ALL.md`. Egy klaszter tagjai néha másik verifier-bemenetben vannak: ilyenkor a társ-ID-ket az `ALL.md`-ben olvasd
el, de verdiktet csak a saját bemeneted ID-ira adj.

## Szabályok, amelyekhez mérni kell

- Lezárt döntés és bizonyíték-kapu: `.claude/rules/safety-and-human-gates.md` „Lezárt döntések”; az M1-re ható
  lezárt döntések többek között a HUM 8. szakasz („Az M1 rubrikahorgonyai”), a HUM 10. szakasz D-1…D-6
  (tanuló-lokális lépések) és a PILOT-1…PILOT-4 (`02 Tervezet/Emberi jóváhagyás szükséges.md` :545–551). A
  manifest :48 szerinti N-1 kérdés NYITOTT döntés, nem lezárt.
- **N-M1-04 — lezárt projektgazdai döntés, 2026-10-10, a repóban még NINCS rögzítve.** A projektgazda ebben a
  munkamenetben szó szerint ezt írta:

  > Az M1.1 SLIDE 5 önreflexiója maradjon opcionális, tanuló-lokális, és ne tárolódjon Moodle/H5P oldalon. Nem
  > completion-feltétel. Ha a H5P szövegmezője vagy mentett állapota ezt nem tudja garantálni, legyen helyette saját
  > jegyzetes, adatmentes út.
  >
  > A tényleges LMS-implementáción külön ellenőrizni kell a próbálkozás-riportot, mentett állapotot és a mentori
  > hozzáférést. A megfelelő runtime-tesztet és DPO QA-t tartsuk nyitva a bizonyíték megszületéséig.

  Ugyanebben az üzenetben megtiltotta a tananyag-módosítást, a commitot és a pusht külön engedély nélkül — ezért
  nincs még átvezetve. Az átvezetés tartozás (a döntés tartalma nem nyitott kérdés); hogy a kánoni szöveg (M1.1,
  manifest, runtime acceptance) javítása a futó pilot alatt freeze-kivétellel menjen-e, az a projektgazda
  engedélye. A lencsék egy része a döntést átfogalmazva idézi („kizárólag tanuló-lokális, központi tárolás
  nélkül”): a javasolt javításokat a fenti szó szerinti szöveghez mérd, ne a parafrázishoz.
- **Git-history nem áll rendelkezésre.** A „restauráció vagy baseline” kérdésre a válasz „baseline ismeretlen”; a
  súlyosság emiatt nem emelkedik.
- **Pilot minőségi küszöb** (2026-10-05): `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – pilot-ütemezés
  és M0+M1 freeze.md` :55–77 — „Pilot előtt nem halasztható” és „Pilot utánra halasztható” lista.
- **Freeze-kivétel** (2026-10-10): `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés
  indítása, M0.1 POST-PILOT, Moodle-összevetés.md` :41 — „Freeze-kivételt csak tényleges P0 biztonsági,
  adatvédelmi, hozzáférhetőségi vagy a tanulói előrehaladást blokkoló hiba indokolhat.” A Moodle-összevetés
  (CC-06) külön build/runtime feladat, nem blokkoló.
- A pilot 2026-10-10-én elindult; 2026 októberében a cohort az M0-val és az M1-gyel foglalkozik (HUM :547). Egy
  M1-es PILOT-BLOCKER tehát azt jelenti: az érintett activity nem nyitható meg valódi pilot-tanulónak, amíg nincs
  rendezve. Különítsd el: (a) runtime/üzemeltetési lépés vagy bizonyíték (freeze-kivétel nem kell); (b)
  tananyag- vagy build-spec-szöveg módosítása (freeze-kivétel → projektgazdai engedély).
- Repón kívüli állapotot (Moodle-konfiguráció, szerepköri bejegyzés a repón kívül) a reviewerek nem láthattak: ahol
  a finding a repón kívüli bizonyíték hiányára épül, a helyes típus `bizonyíték-kapu`, nem objektív tananyaghiba.
- Az `01 Fejlesztés/04 Audit/` mátrixa (Anna-megfeleltetés, 2026-10-10) audit trail, nem kánon: egy ottani sor csak
  hipotézis, a kánoni forrásban kell igazolni.
- A projektgazda célja: „a lehető legkevesebb, de szakmailag szükséges és bizonyított javítás”. Ízlésbeli vagy
  preferencia-alapú finding → ELVETVE.

## Klaszterek (egy tényállás, több lencse) — egyszer ellenőrizd, de minden ID kapjon verdiktet; jelöld a megtartandót

| Klaszter | Verifier | Findingok | Tárgy |
|---|---|---|---|
| K1 | V1a | BIZT-G1-1, BIZT-G1-2, ERT-G1-1, IMPL-G1-1, IMPL-G1-2, IMPL-G1-3, PED-G1-1 | N-M1-04 át nem vezetése; M1.1:98 / :763 / :792 / :794, MAN:45, MAN:308 (BSPEC-02), RA:41 / :104 (RT-P0-24 lista) a döntésnél gyengébb |
| K2 | V1a | BIZT-G1-3, ERT-G1-2, IMPL-G1-4, PED-G1-2 | N-M1-04 runtime-bizonyítéka (próbálkozás-riport, mentett állapot, mentori hozzáférés) és DPO QA hiánya |
| K3 | V1a | BIZT-G1-4, PED-G1-3, ERT-G3-5 | M1.1 SLIDE 5 / :930 / :61 tanulói keretezése; az M1.A-ra tett ígéret |
| K4 | V1a | BIZT-G1-6, ERT-G1-10, IMPL-G1-5, IMPL-G1-6, PED-G1-10 | M1.1 SLIDE 1–2 önbevallás: „Completion” jelölés és a rögzítő választós tartalékút |
| K6 | V1a | BIZT-G1-7, PED-G1-9 | M1.1:926 önfeltárás-keretezés |
| K5 | V1b | BIZT-G1-5, ERT-G1-3, PED-G1-5, IMPL-G1-7 | Hub: 4. kompetencia „záróreflexió”, M1.1 Check mint nyitott kérdés, dia-szám |
| K7 | V1b | ERT-G1-5, PED-G1-4 | M1.2 Mark the Words: a jelöletlen rész nem mind megfigyelés |
| K8 | V1b | ERT-G1-8, PED-G1-8 | Hub M1.2-leírása ↔ lecke |
| K9 | V2a | ERT-G1-4, ERT-G2-3, PED-G2-1, ERT-G3-7 | SBI hossza 1–2 ↔ 2–3 mondat (mátrix 12. szakasz M1a) |
| K10 | V2a | ERT-G2-1, PED-G2-2 | M1.4:475–476 példamondat a B kapuhelyzetre |
| K11 | V2a | ERT-G2-2, PED-G2-7 | KAPU B-sor ↔ hangnem-sor kettős levonás; a 4.1 kalibrációs minta |
| K12 | V2a | ERT-G2-4, PED-G2-3 | KAPU §3 item-bank ↔ manifest-sor hiánya |
| K13 | V2a | ERT-G2-6, PED-G2-4 | Moodle-rubrika tanulói megjelenítése; MUNK-01 fájlút |
| K14 | V2a | ERT-G2-7, PED-G2-8 | M1.4 SLIDE 3 időjelölés csak a helyes opcióban |
| K15 | V2a | BIZT-G2-7, PED-G2-6 | M1.3 NAR-04 „beírni” (D-1) és az írási lépések sorrendje (levágott rokon: ERT-G2-11) |
| K17 | V2a | ERT-G3-3, PED-G2-5 | M1.B trió-checklist ↔ kapurubrika |
| K16 | V3 | BIZT-G2-1, BIZT-G3-1, PED-G3-1, BIZT-G3-5, BIZT-G3-9 | Valós helyzet / valós személy a beadásokban és a peulákon (M1.F:270, M1.B:476, M1.3:886 ↔ M1.4:457; nyitott N-1; levágott rokon: PED-G2-12) |
| K25 | V3 | BIZT-G2-2, BIZT-G2-4, BIZT-G2-5 | LMS-M1-05 / -07 adatkezelési bizonyíték, mentori láthatóság, beadás előtti tájékoztató |
| K26 | V3 | BIZT-G2-3, BIZT-G2-10 | M1.3 / M1.4 egyedi támogató szöveg a HUM-SAFE-03 blokk mellett |
| K22 | V3 | BIZT-G3-3, PED-G3-10 | M1.A cetlik felolvasása |
| K23 | V3 | BIZT-G3-7, PED-G3-8 | M1.F kis létszám, nyilvános jelentkezés (levágott rokon: IMPL-G3-11) |
| K27 | V3 | BIZT-G3-6 | M1.B:385 valós kör ↔ M1.A vakfolt-ígéret (levágott rokon: PED-G3-12) |
| K18 | V4 | ERT-G3-1, ERT-G3-2, PED-G3-2 | M1.F remediáció: vázlat-visszajelzés, hangnem-sor |
| K19 | V4 | ERT-G3-4, IMPL-G3-3, PED-G3-3, ERT-G3-6 | M1.B A/B/C/D sarkok, MAG 4. kérdés (E-M1-069) |
| K20 | V4 | ERT-G3-9, IMPL-G3-4, PED-G3-4 | M1.B fejenkénti smiley-kártya |
| K21 | V4 | ERT-G3-8, ERT-G3-10, IMPL-G3-5, IMPL-G3-6, IMPL-G3-7, PED-G3-9 | Hub ↔ M1.A / M1.B / M1.F (poszter, percbontás, M1.B-végi kérdés) |
| K24 | V4 | IMPL-G3-1, IMPL-G3-2, PED-G2-10 | Javító próbálkozás nyitása: F-peula „jelenléti completion”, Allowed attempts, M1.4 ↔ M1.B |

**V2b (IMPL-G2-1…10) kapcsolódásai más bemenetekhez:**

| V2b-ID | Társ-ID-k (másik bemenetben) | Tárgy |
|---|---|---|
| IMPL-G2-1 | IMPL-G3-1, IMPL-G3-2 (V4, K24) | KAPU §5 ↔ manifest: GATE_CONFIRMED_M1, F-peula-út, „additional attempts” módja |
| IMPL-G2-2 | — | LMS-M1-05 saját completionje (ASSIGN-M) ↔ D-f / D-h |
| IMPL-G2-3 | BIZT-G2-4 (V3, K25) | M1.4:502 „a kijelölt mentorod/értékelőd látja” ↔ ADV:117 |
| IMPL-G2-4 | BIZT-G2-2 (V3, K25) | RT-P0-01/-08/-09/-19 a GATE-CP-re és a próbálkozás-kezelésre |
| IMPL-G2-5 | ERT-G2-5, ERT-G2-6, PED-G2-4 (V2a, K13) | rubrika tanulói megjelenítése; M1.4:482 ↔ KAPU:55 |
| IMPL-G2-6 | levágott PED-G2-11 | M1.4 H5P-típus (CP vagy Question Set), 1. dia kártyaválasztás |
| IMPL-G2-7 | — | M1.4 Assignment-cím ↔ manifest-név |
| IMPL-G2-8 | ERT-G2-4, PED-G2-3 (V2a, K12) | KAPU item-bank ↔ manifest |
| IMPL-G2-9 | PED-G2-6, BIZT-G2-7 (V2a, K15) | M1.3 6. dia „Másold ki” ↔ LMS-M1-07 nyitása |
| IMPL-G2-10 | — | Assignment fájltípus / fájlszám a build-specben |

A klaszteren kívüli ID-k egyedi findingok.

## Mit kérünk minden findingnál (a verifier saját utasításain felül)

- verdikt (MEGERŐSÍTVE / ELVETVE / EMBERI DÖNTÉS) és típus (objektív / emberi-döntés / bizonyíték-kapu);
- súlyosság-korrekció, ha a lencse túl- vagy alulbecsült;
- a **Pilot-besorolás** helyes-e (PILOT-BLOCKER / POST-PILOT) a fenti szabályok szerint; PILOT-BLOCKER-nél: (a)
  runtime/üzemeltetési lépés, vagy (b) tananyag-/spec-módosítás (freeze-kivétel, projektgazdai engedély);
- a javasolt javítás nem ront-e: nem nyit-e újra lezárt döntést, nem talál-e ki policy-t, kulcsot, küszöböt;
- duplikátumnál: melyik a megtartandó ID.

Kimenet: egy rövid bevezető (mit olvastál vissza, mit nem tudtál ellenőrizni), majd findingonként egy sor:
`ID · verdikt · típus · súlyosság · Pilot-besorolás · indok (file:line) · duplikátum/megtartandó`.

---

# B. melléklet – verifier-verdiktek (116/116)

## B.V1a – N-M1-04 és az M1.1 adatkezelése (21)

**V1a verifier: 21 finding (K1, K2, K3, K4, K6 és a hozzájuk tartozó egyedi ID-k), nem részleges**

Mind a 21 finding hivatkozott helyét a forrásban olvastam vissza.
- **M1.1:** :55–100, :198–207, :330–347, :692–703, :755–799, :915–942.
- **Manifest (MAN):** :14–47 (köztük :16, :24, :35, :39, :45, :79) és :300–311.
- **Runtime acceptance (RA):** :41, :101, :104, :137–152.
- **HUM:** a szakaszfejlécek, :136, :276–278, :505–574.
- **Adatvédelem (ADV):** :115 és :150. **RELEASE-READINESS:** :25–27. **Gyermekvédelem:** :15–21.
- **Peulák és más leckék:** M1.A :262–303, Z.2:307.
- **Auditfájlok:** a pilot-freeze döntés :55–77 (pilot minőségi küszöb), a 2026-10-10-i döntési jegyzőkönyv (PD1010) :14–61, a mátrix N-M1-04 sorai.
- **Webforrás:** a Moodle `MOODLE_405_STABLE` `attempt.php` `save_statement()` része (`$record->response = $result->response ?? '';`) és az `enablesavestate_help` szövege. Mindkettő szó szerint egyezik.
- **Nem ellenőriztem:** a MoodleDocs „Teachers can see all attempts” mondatát és a h5p-course-presentation `semantics.json`-t. Ezek helyett a repó ADV:115 és RA:104 sora az alátámasztás.

Minden findingban az idézet egyezik a fájllal. Git-history nem állt rendelkezésre, ezért a „restauráció vagy baseline” kérdésre mindenhol „baseline ismeretlen” a válasz.

**Két általános megjegyzés a K1-hez és a K2-höz**

1. **A lencsék parafrázisa nem azonos a döntéssel.** Több lencse a döntést így idézi: „kizárólag tanuló-lokális, központi tárolás nélkül”. A szó szerinti szöveg ennél többet mond, három részből áll:
   - opcionális, tanuló-lokális, nem tárolódik Moodle/H5P oldalon, nem completion-feltétel;
   - ha a H5P szövegmezője vagy mentett állapota ezt nem garantálja, saját jegyzetes, adatmentes út kell helyette;
   - a runtime-teszt és a DPO QA nyitva marad, amíg a bizonyíték meg nem születik.

   A HUM-sorba és a kánoni helyekre ez a szó szerinti szöveg kerüljön, mindhárom résszel. A DPO szerepét maga a döntés nevezi meg, tehát nem kitalált szerep.

   A döntés **nem tiltja a beviteli elemet**. Ha az igazoltan nem tárol, megengedett, a saját jegyzet csak tartalékút. Ezért az a javaslat, hogy „beviteli elem nem épül”, túlmegy a döntésen.
2. **A K1 pilot-besorolásának két része:**
   - **(a) Üzemeltetés, freeze-kivétel nélkül.** A lezárt döntés a forrás fölött áll, ezért a build már most a döntés szerint építhet. Az M1.1 SLIDE 5-öt valódi pilot-tanulóknak csak tároló mező nélkül szabad megnyitni (saját jegyzetes, adatmentes út), amíg az RT-P0-24 egy nem tároló elemet nem igazol. Emiatt a teljes M1.1-et nem kell zárva tartani.
   - **(b) Kánoni átvezetés.** Az M1.1:98/:792/:794, a MAN:45/:308, az RA:104 és a HUM-sor javítása. Freeze-kivételre esélyes, mert P0 adatvédelmi hiba (PD1010:41), de csak projektgazdai engedéllyel mehet. A HUM nem lecke, a commitot viszont a projektgazda engedélyhez kötötte.

**Findingok**

BIZT-G1-1 · MEGERŐSÍTVE · objektív · P0→P1 (a nyilvántartási hiány önmagában P1; a P0 a K1 tartalmi ütközése) · PILOT-BLOCKER, csak (b): commit projektgazdai engedéllyel; a lencse „nem tananyag-módosítás” állítása igaz, de az engedélyt nem váltja ki · A HUM utolsó datált szakasza a 11. (:529); `N-M1-04` csak a mátrixban szerepel (:24, :48, :1030, :1130). A javaslat a parafrázist írná be „szó szerinti szöveg” címen, és a mátrix sorát frissítené; ez nem használható · duplikátum → IMPL-G1-2

BIZT-G1-2 · MEGERŐSÍTVE · objektív · P0 · PILOT-BLOCKER (a)+(b) · M1.1:98 („ha a teszt nem igazolja, a mező Moodle-oldalra kerül”), :794 („lehetőleg … a kijelölt mentor … láthatja”), MAN:45 („lehetőleg learner-local”), RA:104 (az LMS-M1-01 hiányzik a listából) – mind egyezik. Pontatlan a MAN:35-re hivatkozás: az a kötelező (`REQUIRED_BUT_LEARNER_LOCAL`) lépésekről szól, a SLIDE 5 opcionális. Az ütközés az N-M1-04-ből fakad. A javaslat használható (a build választ, az RT-P0-24 igazol) · duplikátum → ERT-G1-1

ERT-G1-1 · MEGERŐSÍTVE · objektív · P0 · PILOT-BLOCKER (a)+(b) · Ez a legteljesebb K1-lefedés: M1.1:98, :792, :794, :699; MAN:45, MAN:308 (a BSPEC-02 opcionális listájából hiányzik az M1.1 SLIDE 5); RA:104. A „csak saját jegyzet vagy igazoltan rögzítésmentes elem” ága megfelel a szó szerinti döntésnek. Két korrekció kell. A „kizárólag” helyére a döntés szó szerinti szövege kerüljön. A MAN:308 egy datált `BUILD_SPEC_RESOLVED` rekord, ezért nem átírandó, csak datált kiegészítést kaphat (az IMPL-G1-3 módszere). Az RA:41 önmagában nem hibás, a leltáron keresztül fedi a lépéseket · **megtartandó (K1, tartalmi oldal)**

IMPL-G1-1 · MEGERŐSÍTVE · objektív · P0 · PILOT-BLOCKER (a)+(b) · M1.1:98, :763, :792, :794, :699 és MAN:45 egyezik. A MAN:24 TEXT-C „User's name will be logged” és az RA:41 „Essay CP-be ágyazását nem feltételezzük” megállapítás igazolt. A javaslat (a), (b) és (f) pontja nem használható: a :763 törlése és az „ide beviteli elem nem épül” kizárná az igazoltan nem tároló elemet, amit a döntés megenged. A (c)–(e) pont a szó szerinti szöveggel használható · duplikátum → ERT-G1-1

IMPL-G1-2 · MEGERŐSÍTVE · objektív · P1 · PILOT-BLOCKER, csak (b): HUM-szakasz és `04 Audit`-jegyzőkönyv, commit projektgazdai engedéllyel · HUM :494/:529, nincs 12. szakasz; MTX:1030 „`UNRESOLVED` P0”. A javaslat helyes: szó szerinti szöveg, a mátrixot nem írja át, a szerepet a csomagból veszi. A DPO a döntés szövegében név szerint szerepel. A PD1010 2. pontjának (freeze-szabály) HUM-be vétele nem kötelező része · **megtartandó (K1, nyilvántartás)**

IMPL-G1-3 · MEGERŐSÍTVE · objektív · P1 · PILOT-BLOCKER (b); az RT-P0-24 a döntés alapján (a)-ként az LMS-M1-01-en a lista bővítése nélkül is lefuttatható · RA:104 lista és MAN:308 egyezik; az ADV:115 a manifest §2-re hivatkozik · duplikátum → ERT-G1-1 (részhalmaza), de a MAN:308 datált kiegészítésének módszere ebből a findingból veendő

PED-G1-1 · MEGERŐSÍTVE · objektív · P0 · PILOT-BLOCKER (a)+(b) · Ugyanazok a helyek, mint ERT-G1-1-nél; az idézetek egyeznek. A javaslat (3) pontja („ha nem igazolható nem tároló elem, beviteli mező nélkül”) megfelel a döntésnek. A „döntés” idézete parafrázis, ezt szó szerintire kell cserélni · duplikátum → ERT-G1-1

BIZT-G1-3 · MEGERŐSÍTVE · bizonyíték-kapu · P0 · PILOT-BLOCKER (a): a SLIDE 5 beviteli eleme csak sikeres RT-P0-24 visszaolvasás után nyílhat, addig saját jegyzetes út; az RA:104 szerint beviteli elem nélkül a hiányát kell rögzíteni; a DPO QA a döntés szerint nyitva marad. Nem tartalmi módosítás · MAN:16 („Enable attempt tracking” = Yes), RA:152 (`IMPLEMENTATION_TEST_REQUIRED`), HUM:136 („éles learner release minden személyes adatot tároló activitynél”), a Moodle `save_statement()` WebFetch-csel igazolva · **megtartandó (K2)**

ERT-G1-2 · MEGERŐSÍTVE · bizonyíték-kapu · P0 a SLIDE 5 részre; az RT-P0-09/13/14 rész P1 · PILOT-BLOCKER (a): a PILOT-1 szerinti M0+M1 bizonyítéklista része; a completion/unlock a pilot minőségi küszöb :63 sora alá tartozik · RA:137/141/142/152 és RR:25 egyezik · részduplikátum → a SLIDE 5 része BIZT-G1-3-ra; a többletrész (SLIDE 1–2 választói, CP-completion, M1.2 húzásmentes út) **megtartandó**

IMPL-G1-4 · MEGERŐSÍTVE · bizonyíték-kapu · P1→P0 (egységesen a K2-vel) · PILOT-BLOCKER (a) · RA:152 és az `enablesavestate_help` (WebFetch) szó szerint egyezik · duplikátum → BIZT-G1-3

PED-G1-2 · MEGERŐSÍTVE · bizonyíték-kapu · P0 · PILOT-BLOCKER (a) · MAN:16 és RA:152 egyezik · duplikátum → BIZT-G1-3

BIZT-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P1→P2 · POST-PILOT (helyes) · M1.1:763 és :771 egyezik. A mező előtti, feltárást a Memunához irányító mondat új alkalmazás lenne (a Z.2:307 mintája); az a gyermekvédelmi kapuhoz tartozik. A „csak nálad marad” mondatot az RA:104 utolsó mondata tiltja, amíg a visszaolvasás sikeres nem lesz. Az M1.1:90 segítő blokk már megadja a passzt és a gyermekvédelmi utat · nem duplikátum (a PED-G1-3 (2) pontjával átfed)

PED-G1-3 · MEGERŐSÍTVE · objektív · P1→P2 · POST-PILOT (helyes; az M1.A:282 a peulán kizárja a kényszerű feltárást) · M1.1:61 („amit itt a vakfoltodról végiggondolsz, azt a peulán a kvucával együtt dolgozzátok fel”) és :930 ellentmond az M1.A:273–274 és :299–301 sorainak (a vakfoltot nem nyitják meg). Csak az (1) pont (:61 és :930 hídmondata) bizonyított. A (2) új keretező mondat és a (3) „Nem esszét” → „Nem kell esszé” csere ízlés, az a rész ELVETENDŐ · **megtartandó (K3)**

ERT-G3-5 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · M1.1:930 ↔ M1.A:273–274 egyezik; az M1.1-NAR-06 (:936–938) valóban nem tartalmazza a mondatot · duplikátum → PED-G1-3 (az a :61-et is lefedi)

BIZT-G1-6 · EMBERI DÖNTÉS · emberi-döntés · P1→P2 · POST-PILOT (helyes) · M1.1:204 és :335–344 egyezik. A D-d/D-i (HUM:556, :561) csak a completiont rendezi, a D-j csak az M2.3 tárolását, az N-M1-04 csak a SLIDE 5-öt. A SLIDE 1–2 választós tartalékútjának tárolása tehát új alkalmazás, adatvédelmi kérdés (DPO) · duplikátum → IMPL-G1-5

ERT-G1-10 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · M1.1:344 „(Completion, …)” ütközik a MAN:16 H5P-C szabályával („A pontozatlan választók nem önálló completion-elemek”). A :204-gyel nem közvetlen az ellentmondás: az csak a megvalósításról szól · duplikátum → IMPL-G1-6

IMPL-G1-5 · EMBERI DÖNTÉS · emberi-döntés · P1→P2 · POST-PILOT; a build a forrás elsődleges, nem rögzítő szöveg + Tovább útját követheti, ehhez kánoni módosítás nem kell · ADV:115 (a próbálkozás-riportot a nem szerkesztő tanár is látja) és ADV:150 egyezik; az RA:101 M2.1-mintája létezik, de a projektgazda azt egy másik elemre hozta. A döntésig a szöveg nem változik, ez helyes · **megtartandó (K4, tárolás)**

IMPL-G1-6 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · M1.1:344 ↔ MAN:16. A K4-kérdésre a válasz: a lezárt elv alkalmazása, nem új döntés. A MAN:16 a H5P-C profilban általános szabályként rögzíti a D-d/D-i elvét. A javasolt csere minimális, a mondat többi része nem változik · **megtartandó (K4, „Completion”)**

PED-G1-10 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A :344-es objektív része IMPL-G1-6-tal azonos. A :80 („válaszoltál a kérdésekre”) módosítása nem bizonyított hiba, mert a SLIDE 6 kvízére is vonatkozhat; ez a rész nem használható. A tárolási része IMPL-G1-5-tel azonos · duplikátum → IMPL-G1-5 (a tárolási rész) és IMPL-G1-6 (az objektív rész)

BIZT-G1-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT (helyes) · M1.1:926 egyezik. A Gyermekvédelem :17 hatókörébe az M1 nem tartozik, a HUM:278 az M4 önfeltárását a Memunához köti. Kánoni szabálysértés nincs. A kiskorú madrih és a hanihok közötti határ kérdése a gyermekvédelmi kivétel miatt bizonytalanság esetén is emberi döntés, nem elvetés · **megtartandó (K6)**

PED-G1-9 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · M1.1:926 egyezik. A gyermekvédelmi része BIZT-G1-7-tel azonos. A pedagógiai része (a fogalom „kvíz utáni új fogalom”, az áthelyezés SLIDE 3/4-re) preferencia, ELVETENDŐ: a rejtett mező a Johari-inputban már szerepel · duplikátum → BIZT-G1-7

**Összesítés**

- **Verdiktek:** MEGERŐSÍTVE 15, ELVETVE 0, EMBERI DÖNTÉS 6. A 15 megerősítettből 4 bizonyíték-kapu: BIZT-G1-3, ERT-G1-2, IMPL-G1-4, PED-G1-2.
- **Megtartandók:** ERT-G1-1 és IMPL-G1-2 (K1), BIZT-G1-3 és ERT-G1-2 többletrésze (K2), PED-G1-3 (K3), IMPL-G1-6 és IMPL-G1-5 (K4), BIZT-G1-7 (K6), BIZT-G1-4 (önálló).
- **Duplikátumok:**
  - BIZT-G1-1 → IMPL-G1-2
  - BIZT-G1-2, IMPL-G1-1, IMPL-G1-3, PED-G1-1 → ERT-G1-1 (a MAN:308 módszere az IMPL-G1-3-ból)
  - IMPL-G1-4, PED-G1-2, valamint ERT-G1-2 SLIDE 5 része → BIZT-G1-3
  - ERT-G3-5 → PED-G1-3
  - ERT-G1-10 → IMPL-G1-6
  - BIZT-G1-6 → IMPL-G1-5
  - PED-G1-10 → IMPL-G1-5 és IMPL-G1-6
  - PED-G1-9 → BIZT-G1-7

**Ezek a javaslatok nem használhatók**
- IMPL-G1-1 (a), (b), (f): a „beviteli elem nem épül” túlmegy a döntésen.
- A K1 „kizárólag …” parafrázisa: helyette a szó szerinti szöveg kell, a tartalékúttal és a nyitva tartott runtime-/DPO QA-résszel.
- PED-G1-3 (2) és (3).
- PED-G1-10 :80-as része.
- BIZT-G1-1 mátrix-frissítése.

## B.V1b – M1.1, M1.2 és a hub (16)

**M1 V1b verifier — 16 finding, mind kapott verdiktet (nem RÉSZLEGES)**

**Mit olvastam vissza a forrásban:**
- HUB (`02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md`): :24–105.
- M1.1: :48–102, :456–695, :855–954.
- M1.2: :1–60, :150–209, :350–394, :600–799, :860–919, :966–970.
- A11Y: :26–39.
- RA: RT-P0-13/14 (:141–142).
- MAN:46.
- Pilot quality bar: :55–77.
- Webes forrás: a h5p-course-presentation `semantics.json` (master).

**Grep-ellenőrzések:**
- A „segített már” és a „záróreflex” csak a HUB:36-ban és a :86-ban fordul elő.
- Az M1.2-ben nincs se „M1.1”, se Johari-/vakfolt-utalás; az egyetlen találat az M1.A címe a :936-ban.
- Az M1.2-ben nincs Drag & Drop-indoklás.

**Amit nem tudtam ellenőrizni:**
- Elsődleges forrásból nem néztem meg, hogy a H5P DragQuestion ad-e húzható elemenkénti visszajelzést, és milyen a Mark the Words billentyűzetmodellje.
- A PED-G1-5 M1.A:217 / M1.B:367 mellékállítását nem olvastam vissza.
- Git-history nincs, ezért minden tételnél „baseline ismeretlen”, és a súlyosság emiatt nem emelkedik.

**K5 lényege:** a HUB:86 szerint az M1.1 Check-je „1 nyitott kérdés”. A leckében ez 3 zárt kérdés (M1.1:857–912). A HUB:36 4. kompetenciájának („záróreflexió”) sehol nincs tevékenysége.

**K7 lényege:** igen, a tanulói szöveg állítja, hogy a jelöletlen rész megfigyelés/tény:
- M1.2:618: „(A többi rész legyen megfigyelés / tény.)”
- M1.2:629: „A „nem készültél”, „végig a többiek szavába vágtál” inkább megfigyelés” — a :648 szerint ez szövegként megjelenik.
- M1.2:651: „tényt is megjelöltél”

Ez ellentmond a lecke saját definíciójának:
- M1.2:203: „a ‘mindig’ … általánosít”
- M1.2:384–386, :392: az „egész végig” címke, a „soha” általánosítás
- M1.2:362: „Megfigyelés az, amit egy kamera is felvenne”

Ráadásul a „nem készültél” következtetés, nem megfigyelés.

---

**Findingonként:**

BIZT-G1-5 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT (helyes) · A HUB:85–86 nyitott Check-et ír, a lecke Check-je 3 zárt kvízkérdés (M1.1:857–912); az M1.1 egyetlen szabad szöveges lépése a SLIDE 5. A 4. kompetenciánál a finding helyesen hagyja nyitva a döntést. · duplikátum (K5) → megtartandó: ERT-G1-3

ERT-G1-3 · EMBERI DÖNTÉS · emberi-döntés (benne egy objektív lépés: a HUB:86 igazítása az M1.1 SLIDE 6-hoz) · P1 · POST-PILOT (helyes) · A HUB:36 „reflexiós produktumként jelenik meg”, de a Grep szerint semmilyen M1-fájlban nincs ilyen lépés.
- Hogy hol valósuljon meg, az pedagógiai döntés, és ha tárolt szöveg lesz, új adatkör (HUM-PRIV-01/DPO). A finding helyesen jelzi, hogy ez az N-M1-04 új alkalmazási esete, nem átvezetése.
- Nem talál ki policyt.
· K5 megtartandó (BIZT-G1-5 adatvédelmi korlátjával együtt)

PED-G1-5 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes) · Ugyanaz a tényállás (HUB:36, :86 ↔ M1.1:857–912). Az 1. kompetenciáról szóló mellékállítás (M1.A:217) nincs visszaolvasva. · duplikátum → megtartandó: ERT-G1-3

IMPL-G1-7 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · A HUB:86 ↔ M1.1:857–912 eltérés valós. A HUB:81 „6–8 slide” → „6 slide” javaslat viszont nem szükséges: a 6 benne van a tartományban, nincs ellentmondás az M1.1:51/:100-zal. Ezt a részt a minimális javítás elve szerint el kell hagyni. · duplikátum → megtartandó: ERT-G1-3

ERT-G1-5 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT (helyes; formatív, nem blokkol, nem freeze-kivétel) · A 4. mondat „nem bírsz nyugton maradni 5 percig sem” része (M1.2:626) általánosítás, mégis a „tény” oldalra kerül (:618, :651). A javaslat (a mondat szövegének cseréje) viszont túlmegy a minimálison: itemszöveg-csere, és a PED-G1-4 kulcs- és mondatváltozás nélkül megoldja. · duplikátum (K7) → megtartandó: PED-G1-4

PED-G1-4 · MEGERŐSÍTVE · objektív · P1 (félrevezető szakmai állítás tanulói szövegben) · POST-PILOT (helyes) · A jelöletlen részt megfigyelésnek/ténynek nevezi a :618, :629 és :651, ami ellentmond a SLIDE 1–2 definíciójának (:203, :362, :384–392); a „nem készültél” következtetés.
- A javaslat a legkisebb beavatkozás: utasítás, magyarázat és visszajelzés; az 5 célszó, a pontozás és a mondatok változatlanok.
- A mondatcserét helyesen emberi döntésnek jelöli.
- A javítás látható szöveg, ezért pin kell hozzá. A VO-narrációt (:640) nem érinti.
· K7 megtartandó

ERT-G1-8 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · A HUB:102 „besorolás” megnevezése csak a Q1-re illik (M1.2:866); a Q2 (:885) és a Q3 (:906) fogalmi kérdés. A „4/5” (HUB:93) nem képezhető le egy 5 tételes feladatra (D&D: 6 kártya, :750); a HUB:30 arányként is olvasható, ezért ez a rész gyengébb. · duplikátum (K8) → megtartandó: PED-G1-8

PED-G1-8 · MEGERŐSÍTVE · emberi-döntés (a :97/:99 iránya és a „4/5” megfeleltetése pedagógiai döntés, a programvezetőé; nem policy) + objektív (c) rész (HUB:102) · P2 · POST-PILOT (helyes) · Az M1.2-ben nincs M1.1-visszacsatolás és Johari-felidézés (Grep: 0 találat az „M1.1”-re, a „Johari” csak a :936 M1.A-címben). Ez ellentmond a HUB:97/:99-nek; azonos rangú kánoni források ütköznek, irányt nem választok. · K8 megtartandó (a teljesebb finding)

ERT-G1-6 · ELVETVE · — · — · — · A „háromszor”-jel a lecke tanított szabályának alkalmazása (HUB:101 „konkrét idő/hely/viselkedés = megfigyelés”; M1.2:362–364). Az „abszolút” disztraktorok éppen a tanított általánosítást célozzák (M1.2:203, :392). Az M1.1 Q2 disztraktorait (M1.1:885–887) az ERT-G1-7 maga nevezi „célzott tévképzetnek”. Bizonyított hiba nélküli disztraktorcsere (course-content invariáns) → preferencia.

ERT-G1-7 · MEGERŐSÍTVE (csak az M1.2-rész) · objektív · P1→P2 · POST-PILOT (helyes) · Az M1.2:775 „minden kártyához 1 mondatos magyarázat”-ot ígér, de 6 kártyából csak 3 magyarázat van megírva (:779–784, a 2., 5. és 6. kártyához nincs). A hiányzó tanulói szöveget az építőnek kellene kitalálnia.
- Az M1.1 Q2-rész elvetendő: ott semmilyen forrás nem ígér opciónkénti visszajelzést, ez preferencia.
- Hibás állítás, hogy a megvalósíthatóságot az RT-P0-13/14 „igazolja”: mindkettő `IMPLEMENTATION_TEST_REQUIRED` (RA:141–142).
- Nem ellenőriztem, hogy a DragQuestion ad-e húzható elemenkénti visszajelzést.

ERT-G1-9 · ELVETVE · — · — · — · Formatív, nem kapuzott mikrocél (HUB:26). A Q1 opciói mind a 4 mezőt megnevezik (M1.1:863–866), a lecke a 4 mezőt tanítja (:459–472, :920–924). A mikrocél (:55) átírása tanulói célszöveg-preferencia, és átfed a K3-mal (ERT-G3-5); az N-M1-04 nem tiltja, hogy a cél az opcionális lépést megnevezze.

IMPL-G1-8 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes; a rádiógombos húzásmentes út már előírt, :797, MAN:46) · Az A11Y:33 a lecke fejlesztői megjegyzésében indoklást kér a Drag & Drop-hoz, de az M1.2-ben nincs ilyen (Grep: :21, :661, :958, :968, :970 — egyik sem indoklás).
- Elsődleges forrással igazolva: a h5p-course-presentation `semantics.json` (master) beágyazható típusai között nincs legördülő választós típus (H5P.Blanks 1.14 igen, Advanced Blanks nem).
- A javaslat nem gyengít követelményt, és az indoklást helyesen nem a /course-fix-re bízza.

IMPL-G1-9 · ELVETVE · — · — · — · Az M1.1-ILL-02 a11y-jegyzete (:549–551: „Szövegrétegek valódi szövegként; a pici ikonok dekoratívak”) egyezik a dia kötelező szabályával (:621). A :952 összefoglaló „(alt-szöveget)” zárójele laza fogalmazás, nem ellentmondás. Az IKO-02 (:687–689) és az M1.2-IKO-01 (:270–272) `informative` besorolású, alt-text derivatívával; a jegyzetük feltételes („ha tartalmi jelzésnek szánják”), nem önellentmondó.

IMPL-G1-10 · ELVETVE · — · — · — · A kódkerítés (M1.2:30, :44) és a link nélküli Glosszárium (:39) valós. A „###/** jelenik meg a Label-ben” hatás azonban feltételezés. Az M1.1:85 linkje repó-relatív út, Moodle-ban így sem működik, és nincs kánoni szabály, amely ezt a formát előírná → formázási preferencia.

PED-G1-6 · ELVETVE · — · — · — · A rács és a narráció példái a nyitott mező kivételével ugyanannak a gondolatnak a parafrázisai (:626↔:640, :627↔:642, :628↔:644), tehát a „8 példa 4 fogalomra” túlzás. A rácsot az asset-spec szándékosan így rögzíti (:542, :575), a narráció VO-gyártott → multimédia-preferencia, nem bizonyított hiba.

PED-G1-7 · ELVETVE · — · — · — · A két T/F (:485 hamis, :655 igaz) ugyanazt a tévképzetet ellentétes polaritással kérdezi, a dia címe szerint szándékosan (:501 „+ „vakfolt = baj?””). Itemcserét javasol bizonyított hiba nélkül; az N-M1-03 csak mátrix-hipotézis → preferencia.

---

**Összesítés:**
- MEGERŐSÍTVE: 8 (BIZT-G1-5, IMPL-G1-7, ERT-G1-5, PED-G1-4, ERT-G1-8, PED-G1-8, ERT-G1-7, IMPL-G1-8)
- ELVETVE: 6 (ERT-G1-6, ERT-G1-9, IMPL-G1-8 nem; IMPL-G1-9, IMPL-G1-10, PED-G1-6, PED-G1-7)
- EMBERI DÖNTÉS: 2 (ERT-G1-3, PED-G1-5)
- Ebből `bizonyíték-kapu`: 0
- PILOT-BLOCKER: nincs; mind a 16 helyesen POST-PILOT.

Az ELVETVE-lista helyesen: ERT-G1-6, ERT-G1-9, IMPL-G1-9, IMPL-G1-10, PED-G1-6, PED-G1-7.

**Duplikátumok:**
- K5: BIZT-G1-5, PED-G1-5, IMPL-G1-7 → megtartandó: **ERT-G1-3**
- K7: ERT-G1-5 → megtartandó: **PED-G1-4**
- K8: ERT-G1-8 → megtartandó: **PED-G1-8**

## B.V2a – KAPU, M1.3, M1.4 – pedagógia és értékelés (23)

## V2a verifier: M1, KAPU / M1.3 / M1.4 pedagógiai és értékelési tételek (23 finding, teljes)

**Mit olvastam vissza:**
- KAPU :1–309, teljes.
- M1.4 :130–160 és :286–525.
- M1.3 :718–819, :866–895 és :1018–1035.
- M1.B :96–141 és :345–374.
- MAN :30–51.
- PT :106, :138, :140–142, :271.
- HUM 8–11. szakasz (:449–554), és a safety-szabály „Lezárt döntések” szakasza.
- Az SBI-hosszra Grep a teljes M1-mappán, a PT-n, a HUM-on és a `04 Audit/` döntési jegyzőkönyvein.
- Hub: csak Greppel (:33, :39, :125, :132, :213, :239, :249).
- M2KAPU: csak Greppel (:176).

**Mit nem tudtam ellenőrizni:**
- Git-history nincs, ezért mindenhol „baseline ismeretlen”. A mátrix :1070 „2a7cbc5 óta” sora csak hipotézis.
- A Moodle rubrika-megjelenítési beállításait elsődleges forrásból csak részben igazoltam. A docs.moodle.org/405 „Rubrics” oldala az „Allow users to preview rubric” opciót megnevezi. A többi beállításnevet és az alapértékeket nem közli.
- Runtime-állapotot nem láttam.

**K9 kánoni háttere:** A PT (1. forrás) :106/:142 szerint „1–2 db 2–3 mondatos SBI-váz”, :138 szerint „2–3 mondatos”. A hub :33/:39/:125 és a KAPU :21/:197 szintén 2–3 mondatot ír. Az 1–2 mondatot ezek valósítják meg: M1.4 :10/:380/:426/:434(VO)/:450, M1.3 :45/:801 („1 mondat”), M1.B :359, és a KAPU 4.1-es, egymondatos „épp átmegy” mintája. Lezárt döntés erről sincs: sem a HUM-ban (8–11. szakasz), sem a `04 Audit/` döntési jegyzőkönyveiben. A CLAUDE.md szerint ha az 1–4. források ellentmondanak egymásnak, nem választunk közülük magunktól. A rubrika a hosszt nem pontozza, és a küszöb (≥1 soronként ÉS ≥5/8) minden forrásban azonos, ezért egyik K9-tétel sem PILOT-BLOCKER.

**Rubrika, küszöb, szintnevek:** A HUM 8. szakasz csak a szintneveket zárja le (0 = Még nem / 1 = Rendben / 2 = Erős). A sorleírások tartalmát, a kalibrációs minták verdiktjét és a beadás-másolás kezelését nem. Ezek tehát nyitott értékelési kérdések: K10, K11.

## Findingonként

- ERT-G1-4 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes) · Az ellentmondás valós (KAPU:21 ↔ M1.4:10/:450). A javaslat önhatalmúlag a 2–3 mondatot választja, holott a PT/hub/KAPU ↔ M1.3/M1.4/M1.B/KAPU 4.1 ütközést lezárt döntés nem rendezi; a javaslat így nem használható · duplikátum → **PED-G2-1**
- ERT-G2-3 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes) · A PT:106/:142 ↔ M1.4:450/:434(VO) ütközés szó szerint igazolt, lezárt döntés nincs · duplikátum → **PED-G2-1**
- PED-G2-1 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes) · Ez a legteljesebb tétel: benne van az M1.3:801 („1 mondat”), a darabszám–hossz keveredés (M1.4:461/:491 ↔ hub:132) és a KAPU 4.1 egymondatos mintája (KAPU:260). A rubrikához és a küszöbhöz nem nyúl · **megtartandó (K9)**
- ERT-G3-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT (helyes) · Az M1.B:359 „1–2 mondatban” és a :476 hurokzárás valós. A javasolt „2–3 mondatos” félmondat a nyitott K9-választ előlegezné · duplikátum → **PED-G2-1**
- ERT-G2-1 · EMBERI DÖNTÉS · emberi-döntés · P0→**P1** (cél ↔ értékelés széttartás; nem hamis completion, mert a beadást ember értékeli) · POST-PILOT (helyes; a hamis átengedés nem blokkolja az előrehaladást, nem freeze-kivétel) · Az M1.4:475–476 kész SBI a B kapuhelyzetre (M1.4:138). Rubrika szerint kb. 7/8, mert a „ma a körben” S-je legfeljebb Rendben. A „saját, kitalált helyzet” út (M1.4:457) miatt a példacsere önmagában nem elég, értékelői szabály kell, és az az értékelési felelős döntése. A pilot alatt repón kívüli értékelői utasítással kezelhető · **megtartandó (K10)**
- PED-G2-2 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes) · Ugyanaz a tényállás. Az „objektív” példacsere a saját helyzetes úton nem zárja a rést (az M1.4:290–292 példa ott is másolható), ezért objektív javításként nem használható. A C-kártyás „összerakás” rész gyenge: a részek összerakása már alkotás · duplikátum → **ERT-G2-1**
- ERT-G2-2 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (helyes; a pilotban értékelői kalibrációval kezelhető repóváltozás nélkül, (a) típusú lépés; téves bukás esetén ott a második értékelő, KAPU:25) · Valós és szövegből igazolt:
  - A B-sor és a hangnem-sor „Rendben” szintje szinte azonos tartalmat von le: KAPU:64 „becsúszik egy ítélkező szó” ↔ KAPU:86 „enyhe minősítés”, a példák is majdnem egyformák.
  - A 4.1-es minta ugyanarra a szövegre „kissé minősítő-általános”-t (:265) és „nincs címke”-t (:267) mond, épp a küszöbön.
  - Ez feszül a KAPU:126 „nincs kettős súlyozás” állításával.
  - A HUM 8. szakasz csak a szintneveket zárja le, ezt nem rendezi.
  - **megtartandó (K11)**
- PED-G2-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT (helyes) · Ugyanaz a 4.1-es ellentmondás (KAPU:265 ↔ :267 ↔ :86), szűkebb hatókörrel · duplikátum → **ERT-G2-2**
- ERT-G2-4 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT (helyes) · Valós:
  - A KAPU:28/:308 külön, completion-only tanulói Quiz/H5P Question Setet ír elő, szabad szöveges Item 5–6-tal (KAPU:186–200).
  - A MAN §2-ben (:45–51) nincs sora, holott a MAN:35 szerint minden Moodle-oldali szabadszöveg-mező saját sort kap.
  - Hogy tanulói activity-e, és a szabad szöveg milyen tárolási besorolást kap, az LMS- és DPO-döntés.
  - **megtartandó (K12)**
- PED-G2-3 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT (helyes) · Ugyanaz a KAPU:308 ↔ MAN:49–50 hiány · duplikátum → **ERT-G2-4**
- ERT-G2-6 · MEGERŐSÍTVE · objektív (a runtime-igazolás bizonyíték-kapu, G3b) · P2 · POST-PILOT (helyes; stagingben (a) típusú runtime-ellenőrzés) · Valós:
  - Sem a KAPU §5 (:297–308), sem a MAN:50 nem rögzíti a rubrika tanulói megjelenítését.
  - Az M2KAPU:176 rögzíti.
  - A hub:213 F-peulája és az M1.4:499 („visszajelzést kapsz a rubrika alapján”) erre épít.
  - A pontos beállításneveket a célverzión kell igazolni, a rubrika tartalma, a pontok és a küszöb nem változik.
  - Rokon V2b-tétel: IMPL-G2-5.
  - **megtartandó (K13)**
- PED-G2-4 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · A rubrika-megjelenítés része ugyanaz, mint az ERT-G2-6-é. Az M1.4-MUNK-01 része nem bizonyított hiba. A sablont az Assignment-oldalról töltik le, ahol a 3. lépés táblázata (M1.4:478–487) látható, és a spec (:523) zárt felsorolása nem állítja, hogy teljes. Ez a részjavaslat nem szükséges. A javaslatban szereplő beállításnevek közül csak az „Allow users to preview rubric” igazolt elsődleges forrásból · duplikátum → **ERT-G2-6**
- ERT-G2-7 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · Valós. Az M1.4:321 helyes opciója az egyetlen időjelölt válasz (:322–324 nem az), pontosan a KAPU:134 által megnevezett hiba. A Slide 4 (:347) és a KAPU Item 1 (:136–145) már javítva van. A javaslatra figyelni kell: időjelölt disztraktorral (pl. „Ma a peula közepén nagyon tiszteletlen voltál.”) a mostani kérdés („Mit mondanál el S-ként”) kétértelművé válik, mert a disztraktor tartalmazza a helyes választ. Ezért a kérdésnek is a KAPU Item 1 mintáját kell követnie („csak a helyzetet”). A ✅ változatlan, --pin-visible kell · **megtartandó (K14)**
- PED-G2-8 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · Ugyanaz (M1.4:321–324 ↔ KAPU:134), ugyanazzal a javaslat-figyelmeztetéssel · duplikátum → **ERT-G2-7**
- BIZT-G2-7 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes; PILOT-4: a narráció opcionális) · Valós. Az M1.3:814 („próbáld meg beírni”) és a :750 spec („írja be”) ellentmond a :799-nek („a dián nincs beviteli elem… nem adod be”) és a lezárt D-1-nek (HUM:522). A javítás a lezárt döntés átvezetése. VO-forrás, ezért a VO QA-repó fix packján keresztül megy · **megtartandó (K15, NAR-04 rész)**
- PED-G2-6 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · A NAR-04 rész a BIZT-G2-7 duplikátuma. Az önálló rész valós:
  - Az M1.3:886 „Másold ki… ezt a mondatot”-nak nincs előzménye, mert a dián nincs beviteli elem (:887), és az írás a lecke utáni LMS-M1-07-be kerül.
  - Így a 7. dia „Ellenőrizd a saját mondatod!” (:1022–1033) még megírt mondat nélkül fut.
  - A javasolt 6. dia-szöveg és a tájékoztató bővítése csak javaslat. A tájékoztató a LMS-M1-07 privacy-kikötésével közös sor, változtatásnál a „név és felismerhető részlet nélkül” kikötés szó szerint marad.
  - Rokon V2b-tétel: IMPL-G2-9.
  - részben duplikátum → BIZT-G2-7 (NAR-04); a 6–7. dia sorrendje miatt **megtartandó**
- ERT-G3-3 · ELVETVE · — · — · — · A trió-checklist (M1.B:134–139) a saját deklarált célját követi: az S/B/I meglétét és a becsúszó címkét (:101). Egy 4 perces szóbeli peer-kör formatív eszköze, amelyet egyetlen kánoni forrás sem köt a kapurubrika szintjeihez. A háromfokú átalakítás tervezési preferencia, és a szigorúan 1 perces mini-reflexió időkeretét is érintené (:350, :366) · K17
- PED-G2-5 · ELVETVE · — · — · — · Ugyanaz a tényállás (M1.B:134–139). Az M1.3 önellenőrzés átvétele preferencia, nincs bizonyított hiba · K17 (a két tétel együtt elvetve)
- ERT-G2-5 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · Valós. Az M1.4:482 S-„Erős” szintje szigorúbb a KAPU:55-nél (mikor ÉS hol ÉS helyzet ↔ idő ÉS/VAGY hely ÉS szakasz). Az M1.4:484-ből kimarad a KAPU:75 „hiteles / logikusan következik a B-ből” feltétele, és a sornév is eltér (:484 ↔ KAPU:67). Az M1.4 maga mondja, hogy a KAPU a forrás (:635). A szintnevek, a pontok és a küszöb változatlanok, --pin-visible kell · —
- ERT-G2-8 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT (helyes) · Valós. A kérdés („Ebben a mondatban melyik rész…”, M1.3:724–725) D opciója (:732) nincs benne a mondatban, így felületi alapon kizárható. Ez sérti a KAPU:132 plauzibilis-disztraktor elvét. A D törlése tiszta javítás. A „mondatból vett” csereopció kétértelmű I-részt hozhat létre, ezért az óvatosan kezelendő. A ✅ változatlan · —
- ERT-G2-9 · ELVETVE · — · — · — · Repón belül nincs ellentmondás. A KAPU:157 „szándékot tulajdonít” a B-re (megfigyelés) vonatkozik, a KAPU:87 viszont kifejezetten megengedi az én-perspektívás I-t („úgy éreztem…”). Tárgyi hibát a finding maga sem igazolt elsődleges forrással. Az answer keyhez bizonyíték nélkül nem nyúlunk · —
- ERT-G2-10 · ELVETVE · — · — · — · A KAPU:43 maga „régi szóhasználatnak” jelöli a fordulatot. A :97 múlt időben vezeti be a két régi leírást („élt”), a :100 pedig „korábbi, mostanra érvénytelen”-nek nevezi az M1.4-es küszöböt. A történeti jelleg tehát jelölve van, a döntési szabály (:104–109) egyértelmű, és a hubban már nincs „alapszint” vagy „fejlődő”. Kalibrációs zaj nem bizonyított · —
- PED-G2-9 · ELVETVE · — · — · — · A tanulói narráció (M1.4:146–147) már őszintén keretez: „amelyikről leginkább el tudnál képzelni egy beszélgetést”. A „mélyebben belemenni” csak a builder-spec (:153), a :154 pedig kimondja, hogy a választás nem kerül át az Assignmentbe. Élményminőségi preferencia · —

## Összesítés

- **MEGERŐSÍTVE:** 8 (ERT-G2-6, PED-G2-4, ERT-G2-7, PED-G2-8, BIZT-G2-7, PED-G2-6, ERT-G2-5, ERT-G2-8)
- **ELVETVE:** 5 (ERT-G3-3, PED-G2-5, ERT-G2-9, ERT-G2-10, PED-G2-9)
- **EMBERI DÖNTÉS:** 10 (ERT-G1-4, ERT-G2-3, PED-G2-1, ERT-G3-7, ERT-G2-1, PED-G2-2, ERT-G2-2, PED-G2-7, ERT-G2-4, PED-G2-3)
- **ebből bizonyíték-kapu:** 0 önálló tétel. Az ERT-G2-6 runtime-részigazolása G3b bizonyíték-kapu.
- **PILOT-BLOCKER:** egy sincs. Egyik tétel sem P0 biztonsági, adatvédelmi vagy akadálymentességi hiba, és egyik sem blokkolja a tanulói előrehaladást.
- **Pilot alatti teendő (repón kívüli értékelői utasítás, nem freeze-kivétel):**
  - K10: a minta szó szerinti átvételének kezelése;
  - K11: kalibrációs egyeztetés a 4.1-es határesetről.

**Duplikátumok:**

| Klaszter | Megtartandó | Duplikátumok |
|---|---|---|
| K9 | PED-G2-1 | ERT-G1-4, ERT-G2-3, ERT-G3-7 |
| K10 | ERT-G2-1 | PED-G2-2 |
| K11 | ERT-G2-2 | PED-G2-7 |
| K12 | ERT-G2-4 | PED-G2-3 |
| K13 | ERT-G2-6 | PED-G2-4 (V2b-rokon: IMPL-G2-5) |
| K14 | ERT-G2-7 | PED-G2-8 |
| K15 | BIZT-G2-7 (NAR-04) | PED-G2-6 NAR-04 része; a PED-G2-6 a 6–7. dia sorrendje miatt külön megtartandó (V2b-rokon: IMPL-G2-9) |
| K17 | — | ERT-G3-3, PED-G2-5: mindkettő elvetve |

Hivatkozott fájlok:
- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/Program terv.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md

## B.V2b – KAPU, M1.3, M1.4 – implementáció (10)

**V2b verifier-eredmény (IMPL-G2-1…10), M1. Mind a 10 ID kapott verdiktet, a jelentés teljes.**

**Mit olvastam vissza.**
- KAPU: :5, :28, :55, :132, :297–308.
- M1.4: :18, :27, :69, :153, :309, :440–553, :655.
- M1.3: :799, :886–887, :1022–1031.
- MAN: :8, :16–25, :35–60, :165–173, :245–254, továbbá a BSPEC- és ASSIGN-M-találatok.
- RA: :88–92, valamint az RT-P0-01/08/09/15/19 sor (:129, :136, :137, :143, :147).
- ADV: :104, :113–119, :230.
- HUM: :494–563 (10–11. szakasz; BS-D1, D-1, D-f, D-h, PILOT-1…4).
- A freeze-jegyzőkönyv: :55–77.
- Az ALL.md társ-ID-i: IMPL-G3-1/2, BIZT-G2-2/4/7, ERT-G2-4/5/6, PED-G2-3/4/6.

**Webes állítások, elsődleges forrásból ellenőrizve:**
- docs.moodle.org/405 Assignment settings: „Manually (via the Submissions page or Grader page), Automatically (after grading), or Automatically until pass”. Ugyanitt: „Leaving the field blank will allow all file types.”
- MOODLE_405_STABLE `gradingform_rubric.php`: „Allow users to preview rubric (otherwise it will only be displayed after grading)”.
- MOODLE_405_STABLE `lib.php` `get_default_options()`: `'alwaysshowdefinition' => 1`, `'showdescriptionstudent' => 1`.
- h5p-question-set `semantics.json`: a „questions” mező könyvtárlistája szó szerint egyezik a findinggal. Az introPage-ben nincs hangmező.

**Nem tudtam ellenőrizni:**
- a Moodle „Maximum number of uploaded files” alapértékét;
- hogy a Single Choice Setben nincs kérdésenkénti visszajelzés;
- hogy egy újranyitott, gyengébb próbálkozás a gradebookban lerontja-e az Assignment completionjét (IMPL-G2-2, Hatás mező);
- a repón kívüli staging-bizonyítékot;
- a PILOT-1 explicit M0+M1 evidence listájának repóbeli példányát (nem kerestem tovább).

Ezekre súlyosságot nem emeltem. Git-history nincs, ezért mindenhol „baseline ismeretlen”.

**A kiemelt kérdésekre:**
- **IMPL-G2-1 – ellentmond-e a KAPU §5 a manifestnek?** Részben.
  - A KAPU:304 elavult. A mechanizmust a manifest már rögzítette: GATE-CP és Grade-feltétel, tartalékút nincs (MAN:167–171; a lezárt BS-D1, HUM:515). A KAPU:304 opciói között olyan is van, amelyet a manifest kizár („külön completion-feltétel” ↔ MAN:169; a kézi completion ↔ MAN:25).
  - A KAPU saját magának is ellentmond: a KAPU:5 szerint a Moodle-beállítás a manifestben van, az M1.4:547 viszont a KAPU §5-re mutat.
  - Az F-peula-opció a KAPU:305-ben **nem** ellentmondás. Szó szerint a MAN:20 (ASSIGN-M) és az RA:90 szövegét követi, a MAN:248 pedig csak feltételesen zárja ki.
- **IMPL-G2-2 – megválaszolja-e lezárt döntés?** Szó szerint nem. A D-f a BSPEC-07 hatókörét azokra az utakra szűkíti, ahol „a manifest nem specifikálja a megerősítő checkpointot”, az M1-ben viszont van checkpoint (LMS-M1-06). Ezért a D-h kiterjesztése az ASSIGN-M sorokra új alkalmazási eset, és a safety-szabály szerint emberi jóváhagyás kell hozzá.
- **IMPL-G2-3 és -4 – bizonyíték-kapu-e, és mikor kell?** Mindkettő bizonyíték-kapu. A lencse POST-PILOT besorolása viszont önellentmondó („a PILOT-1 GO-evidence lista része”). A freeze-jegyzőkönyv :59–66 szerint pilot előtt nem halasztható a „hibás hozzáférés vagy érzékeny adat láthatósága” és a „törött prerequisite/completion/unlock”; a :74 csak a „későbbi modulok runtime proofját” engedi halasztani. Ezért mindkettő PILOT-BLOCKER (a): runtime/üzemeltetési lépés, freeze-kivétel nélkül. Az érintett activityk addig nem nyithatók valódi pilot-tanulónak, amíg a bizonyíték meg nincs, vagy a repón kívül meglévő bizonyíték nincs rögzítve.

**Findingonként:**

IMPL-G2-1 · MEGERŐSÍTVE · objektív · P1→P2 · POST-PILOT (szövegjavítás; a próbálkozás-mód runtime-ellenőrzése az IMPL-G2-4 / RT-P0-19 alá tartozik) · A KAPU:304 nyitottként kezeli a már rögzített GATE-CP utat, és nem nevezi meg a `GATE_CONFIRMED_M1`-et. Ezt az M3 KAPU:333 megteszi, a MAN:51 és a MAN:167–171 pedig rögzíti. A KAPU:5 maga a manifestre mutat, ezért P2. A „kizárt F-peula-út” állítás túlzó: a KAPU:305 a MAN:20 és az RA:90 szövegét követi. A „Manually” mód levezethető a 2026-10-02-i döntésből („nem automatikus… a képző nyitja meg”), a Moodle-idézet egyezik a forrással. A javítás a küszöbhöz és az F-peula-kötelezettséghez nem nyúl, rendben. · Részduplikátum: az F-peula-út és az Allowed attempts kérdésében az IMPL-G3-1 és az IMPL-G3-2 (K24) a megtartandó; a GATE_CONFIRMED-rész csak itt szerepel, ez marad.

IMPL-G2-2 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT (a MAN §4 szerint az M2 nyitása az LMS-M1-06-hoz kötődik, nem az LMS-M1-05 completionjéhez) · Az ASSIGN-M Moodle-szintű completion-beállítása sehol nincs rögzítve. A MAN:20 és a MAN:50 egy cellába vonja össze a leadást és a megerősítést, az LMS-M1-05 viszont kurzusteljesítési kritérium (MAN:165). A lezárt döntések nem válaszolnak (D-f, HUM:558; D-h, HUM:560). Ez új alkalmazási eset; a kérdés a projektgazdáé, illetve a build-spec gazdáé. A „Hatás” mező gradebook-viselkedését elsődleges forrásból nem igazoltam. A „MOODLE-BUILD-VERDICT-et is érinti” állítás nem igazolt, nem átveendő. · —

IMPL-G2-3 · MEGERŐSÍTVE · bizonyíték-kapu (RT-P0-15, G3b; DPO-jóváhagyás az ADV:230 szerint, G2) · P1 · PILOT-BLOCKER (a): a pilot-kurzusban tesztfiókkal vissza kell olvasni az LMS-M1-05 és az LMS-M1-07 láthatóságát, mielőtt az LMS-M1-05 valódi tanulónak megnyílik. Szövegmódosítás nem kell. · Az M1.4:502 azt ígéri, hogy csak a kijelölt mentor látja a beadást. Az ADV:104 és :117 szerint az ASSIGN-M adatait a Moodle-alapértelmezésben csoporttól függetlenül minden nem szerkesztő tanár látja, a szűkítés pedig „nincs rögzítve (BIZT-5)”. Az ADV:230 szerint a tájékoztató DPO-jóváhagyás előtt nem élesíthető. A „teszt előtt ne írd át” korlát helyes. · Duplikátum: a BIZT-G2-4 (K25) a megtartandó, mert tágabb (M1.3:926, BIZT-2); a RT-P0-15-bizonyíték a BIZT-G2-2-vel is átfed.

IMPL-G2-4 · MEGERŐSÍTVE · bizonyíték-kapu (G3b) · P1 · PILOT-BLOCKER (a): az RT-P0-08 és az RT-P0-19 kell az LMS-M1-05/-06 és az M2-nyitás előtt, az RT-P0-09 és az RT-P0-01 az M1-lánchoz. Runtime-lépés, freeze-kivétel nem kell. · Az M1.4:496–500 tanulói ígéretei az RA:129, :136, :137 és :147 sorainak `IMPLEMENTATION_TEST_REQUIRED` állapotú tételein múlnak. A javasolt tesztesetek a MAN:20, a MAN:51 és az RA:88–92 szövegét követik, küszöböt nem találnak ki. · Nem duplikátum: a BIZT-G2-2 az RT-P0-15-öt fedi, nem a kapumechanikát.

IMPL-G2-5 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · A széttartás valós: az M1.4:482 szerint „mikor, hol és melyik helyzetben”, a KAPU:55 szerint „idő ÉS/VAGY hely ÉS a helyzet szakasza”. A beállításnevek és az alapértékek (előnézet = 1, leírás = 1) a MOODLE_405_STABLE-ből igazolva. A javaslat 1. pontja így csak az alapértéket rögzíti: ártalmatlan, de csekély értékű. · Duplikátum: a szövegrészben az ERT-G2-5 a megtartandó (tágabb: az S- és az I-sor, valamint a sornév); a megjelenítés és az RT-tétel kérdésében az ERT-G2-6 a megtartandó (K13), az IMPL-G2-5 igazolt beállításneveivel kiegészítve.

IMPL-G2-6 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Az M1.4:18 és :655 szerint „Course Presentation vagy Question Set”. Az M1.4:153 a típust a runtime acceptance-re bízza, de az RA-ban nincs M1.4-tétel (Grep: 0 találat), vagyis a hivatkozás árva. A Question Set nem hordoz hangot és nem kérdés jellegű diát (semantics.json igazolva). A javaslat :153-ra adott konkrét megvalósítása („Specific slide number” ugrás) kitalált: így nem használható. A helyes irány az RA-tétel pótlása vagy a D-d / D-i elv átvezetése. A „nincs kérdésenkénti visszajelzés” állítás nem igazolt. · A levágott PED-G2-11 duplikátum; az IMPL-G2-6 a megtartandó.

IMPL-G2-7 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Az M1.4:446 címe („M1.4 – Miniszituációk: „Mondd el SBI-ben””) eltér a MAN:50 „Név” oszlopától („M1.4 – SBI-beadandó”), és majdnem azonos a MAN:49-es H5P-névvel. A tanulói szöveg (M1.4:27) már az „SBI-beadandó” nevet használja. Látható szöveg, ezért pin kell. · —

IMPL-G2-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A KAPU:28, :132 és :308 külön Quiz / Question Set activityt ír elő, a MAN:45–51-ben nincs ilyen sor (a MAN:8 csak tényleges activityket sorol). Hogy tanulói activity-e, az a projektgazda és az értékelési felelős döntése. · Duplikátum: K12; az ERT-G2-4 a megtartandó (a MAN:35-szabállyal és a két úttal teljesebb), a PED-G2-3 és az IMPL-G2-8 beolvad.

IMPL-G2-9 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Az M1.3:886 most írást és „ezt a mondatot” kimásolást kér, de a dián nincs hová írni: a :887 szerint a mezők helye az LMS-M1-07, amely a MAN:48 szerint csak az LMS-M1-03 után nyílik. A :1029 már „a saját mondatodra” néz. A javításnak érintetlenül kell hagynia a „név és felismerhető részlet nélkül” és az „oda már csak kitalált” kitételt, és a nyitott N-1 kérdést sem érintheti. · Duplikátum: a PED-G2-6 (K15) a megtartandó, mert az 5–7. diát együtt fedi.

IMPL-G2-10 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A hiány valós: a `02 Tervezet/` alatt sehol nincs „Accepted file types” vagy fájlszám-beállítás, és a Moodle üres mezőnél minden fájltípust enged (docs.moodle.org/405). A KAPU:297 és a MAN:24 alapján a fájlos út nyitott. A javasolt értékek viszont nem kánoni eredetűek (az .odt sehol nem szerepel, a max. 1 fájl önkényes), és a fájltípus szűkítése a „két egyenértékű út” akadálymentességét is érintheti. Adattakarékossági és akadálymentességi kétség, ezért döntés kell: LMS-gazda + DPO + hozzáférhetőségi gazda. A hiány korpusz-szintű, nem M1-specifikus. · —

**Összesítés:**
- MEGERŐSÍTVE 7: IMPL-G2-1, -3, -4, -5, -6, -7, -9. Ebből 2 bizonyíték-kapu: IMPL-G2-3, -4.
- ELVETVE: 0.
- EMBERI DÖNTÉS 3: IMPL-G2-2, -8, -10.
- Pilot-besorolás korrekciója: IMPL-G2-3 és -4 POST-PILOT → PILOT-BLOCKER (a).
- Súlyosság-korrekció: IMPL-G2-1 P1 → P2.

**Duplikátumok:**
- IMPL-G2-1 F-peula/attempts-része → IMPL-G3-1 és IMPL-G3-2 a megtartandó; a GATE_CONFIRMED-rész az IMPL-G2-1-ben marad.
- IMPL-G2-3 → BIZT-G2-4 a megtartandó.
- IMPL-G2-5 → ERT-G2-5 (szöveg) és ERT-G2-6 (megjelenítés) a megtartandó.
- IMPL-G2-6 ← a levágott PED-G2-11 beolvad; az IMPL-G2-6 a megtartandó.
- IMPL-G2-8 → ERT-G2-4 a megtartandó.
- IMPL-G2-9 → PED-G2-6 a megtartandó.

Fájlok:
- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – pilot-ütemezés és M0+M1 freeze.md

## B.V3 – biztonság és adatvédelem (21)

## M1 verifier, V3: 21 finding, mind a 21 kapott verdiktet

**Visszaolvasott források:**
- M1.3: :880–929
- M1.4: :440–529
- M1 KAPU: :20–29 és :200–227
- M1.A: :156–305, :364–509
- M1.B: :150–158, :376–507
- M1.F: :30–109, :262–317
- Manifest: :18–25, :47–50 (az :48-as N-1-szöveg szó szerint)
- Adatvédelem: :70–119, :196–257
- Program terv: :225–230
- Gyermekvédelem: :23, :52–107
- HUM: :140–151, :450–575
- A BSPEC-02 leltár két auditfájlja (az N-1 besorolása) és a D-a…D-d jegyzőkönyv :85

**Amit nem olvastam vissza:**
- a hub :39, :117, :216 és :258 sorát;
- az M1.B :345–346 sorát;
- az M1.3 :1059 sorát;
- a runtime acceptance :143-as sorának szövegét (csak azt láttam, hogy az RT-P0-15 létezik);
- az M1.A 4.3.1 blokkjának keretét (a :372-es sort igen).

Repón kívüli állapotot nem láttam: a PILOT-1 szerinti M0+M1 GO-evidence listát, a DPO-bejegyzéseket és a Moodle-konfigurációt. Git-history nincs, ezért mindenhol „baseline ismeretlen”.

**Findingok:**

BIZT-G2-1 · EMBERI DÖNTÉS · emberi-döntés · P0 marad · PILOT-BLOCKER (a): a döntés maga nem igényel szerkesztést; ha a döntés „csak kitalált”, a szövegjavítás (b), azaz freeze-kivétel kell hozzá · Az N-1 valóban nyitott: a manifest :48 szó szerint „nyitott: kerülhet-e ide valós, névtelenített helyzet…”, a D-a…D-d jegyzőkönyv :85 „Változatlanul nyitva … N-1”. A BSPEC-02 leltár :244/:278 „learner-release emberi döntésnek” sorolja be, így az LMS-M1-07 valódi pilot-tanulónak való megnyitása előtt el kell dönteni. Az „ellentmondás TÉNY” állítás túlzó: az M1.3:886 maga mondja ki, hogy az M1.4-be „oda már csak kitalált… helyzet kerülhet”. Két külön activityről van szó, nem két egymásnak ellentmondó szabályról · önálló (a K16 része, de más activity: LMS-M1-07)

BIZT-G3-1 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT; a szöveg módosítása (b) lenne, a P0-s freeze-kivétel nem teljesül, mert a beadás helyén az M1.4:457 tiltja · A ütközés valós, és az M1.F:270-nél direkt: „amit majd a peulán / terepen tényleg használni fog” (valós helyzetre és személyre szóló mondat) ↔ M1.4:457 „Valós helyzetet – név nélkül sem – ne írj le”. Mögötte a HUM 8. szakaszának :462-es lezárt sora áll („Esetalapú kapuproduktum | csak kitalált… valós eset névtelenítve sem”). Az M1.B:476/:507 gyengébb: mulasztás, nem ellentmondás, mert a peula fő SBI-jei fiktív kártyákból születnek, csak a :382-es valós kör ad valós társról szóló mondatot. A javaslat használható, ha szó szerint az M1.4:457 / M1.3:886 korlátját veszi át; a próbálkozás-logika érintetlen marad · **megtartandó** (a PED-G3-1 duplikátuma)

PED-G3-1 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT · Ugyanaz a tényállás (M1.F:270/:276 ↔ M1.4:457), ugyanazzal a javítási iránnyal · duplikátum → a BIZT-G3-1 a megtartandó

BIZT-G3-5 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · Az M1.A:372 („lehetőleg a saját kvucádra szabva”) és az M1.B:157 nem korlátozza a valós szereplők azonosíthatóságát szóbeli peulán. A „név és felismerhető részlet nélkül” korlát kiterjesztése szóbeli peula-tartalomra a lezárt szabály új alkalmazási esete, és kiskorúak azonosíthatóságát érinti. A kockázat spekulatív, de a safety-kivétel miatt emberi döntés, nem elvetés · önálló

BIZT-G3-9 · EMBERI DÖNTÉS · emberi-döntés · P2, alacsony bizalommal · POST-PILOT · Az M1.B:472 vállalás-példája („Ha valami zavar… S–B–I szerint”) a hétköznapi bosszúságra szól, és nem mond ellent szó szerint a §4:58-nak („nem konfrontál feltételezett elkövetőt”). Hogy a terepi hídba kell-e a „vond be a Memunát” utalás (§4.1:82 engedi), az a Memuna kérdése. Az M1.4:508 ugyanennek a tanulónak kimondja a határt · önálló

BIZT-G2-2 · MEGERŐSÍTVE · bizonyíték-kapu (G2 DPO FINAL_RELEASE_QA; az Adatvédelem §9 :207/:209 RELEASE-EVIDENCE; az RT-P0-15 post-build; G4b/G8 a kontaktra) · súlyosság kapu-szinten, nem tartalmi hiba · PILOT-BLOCKER (a): csak runtime- és szerepköri bizonyíték kell, tananyag-módosítás nem, freeze-kivétel nem kell · Kánon: az Adatvédelem :230 szerint „a DPO jóváhagyása előtt nem élesíthető”; a §9 :207, :209 és :216 nyitott kapu; az :80 kötelező „külön review”-t ír elő az M1 SBI-beadandóra; a HUM :574 az RT-P0-15-öt post-build G2-nek jelöli. A repóban a bizonyíték nincs meg, de lehet, hogy a repón kívüli PILOT-1 GO-evidence listán szerepel; ezt nem láthattam. Nem M1-specifikus: a kurzusszintű tájékoztató DPO-jóváhagyása az M0-t is érinti. A javasolt megfogalmazás a szabályfájl mintája szerinti · részleges átfedés az IMPL-G2-4-gyel (V2b)

BIZT-G2-4 · EMBERI DÖNTÉS · emberi-döntés · P1 · POST-PILOT önállóan, a pilotra gyakorolt hatását a BIZT-G2-2 fedi · Az M1.4:502 „a kijelölt mentorod/értékelőd látja” megfelel a §5 / §11:245 lezárt szabályának. Az Adatvédelem :104 és :117 szerint viszont az ASSIGN-M csoport szerinti szűkítése (BIZT-5) és a szerkesztő tanári, menedzseri és rendszergazdai hozzáférés (BIZT-2) nyitott DPO-kérdés. A javaslat helyes: a döntés előtt a tanulói mondatot nem kell átírni · cross-duplikátum: az IMPL-G2-3 (V2b) ugyanezt mondja; a pilot-összesítőben egyet tartsatok meg, javaslom ezt, a DPO-döntési keretezés miatt

BIZT-G2-5 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT; a szöveg módosítása (b) lenne, nem P0, mert a kurzusszintű §11-es tájékoztató tartalmazza a célt és a megőrzést · A Program terv :225 kifejezetten előírja a „tényleges Assignment-beadások” előtti just-in-time dobozt. Az M1.4 3.1 (:440–510) csak a „ki látja” sort tartalmazza (:502), a manifest ASSIGN-M profilja (:20) nem specifikál ilyen dobozt, az M1 KAPU-ban sincs (az M3 KAPU:82-ben és az M5 KAPU:28-ban van). A javaslat használható, mert csak szó szerinti §11-sorokat vesz át (:243, :250, :252) és kontaktot nem talál ki · önálló

BIZT-G2-3 · MEGERŐSÍTVE · objektív · P1 · POST-PILOT · Az M1.3:914–916 tárolt mező melletti megjegyzéséből hiányzik a kánoni mondat: Gyermekvédelem §4.1:84 (azonosítható esetrészlet nem kerül Moodle-be vagy beadandóba), illetve Adatvédelem §11:241 („Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd…”). Az M1.4:508-ban a mondat megvan. Szó szerinti átvétel, ezért objektív. A javítás az N-1 (BIZT-G2-1) és a BIZT-G2-10 döntésével együtt menjen, hogy ugyanazt a blokkot ne kelljen kétszer szerkeszteni · részleges átfedés a BIZT-G2-10-zel, ugyanazon a szövegen

BIZT-G2-10 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A Gyermekvédelem §4.3:102 („Minden meglévő, ad hoc ‘ha nehéz…’ típusú támogató blokk helyére ez kerül”) és az M1.3:914–916 / M1.4:506–507 szövege valóban egymás mellett áll a kánoni blokkal. Hogy ezek kiváltandó támogató blokkok vagy feladatszintű adattakarékossági utasítások, az a HUM-SAFE-03 alkalmazási kérdése, és a Memunára tartozik. Az M1.4:508 Memuna-mondata semmiképp nem törölhető · önálló

BIZT-G2-6 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A KAPU:27 előírja az eszkalációt, de nem mondja meg, ki és hogyan veszi ki a feltárást tartalmazó beadványt (Adatvédelem :75 „kikerül a Moodle-ből”), mi lesz ilyenkor a kapueredménnyel és milyen alternatív beadási út van. Ugyanez a kérdés az M3-ra nyitott N-9-ként él (leltár :252). Az azonnali út helyes · önálló

BIZT-G2-8 · ELVETVE · — · — · — · Az M1.4:526 már a lezárt HUM-PRIV-01 szövegét alkalmazza („csak szervezeti fiókban, korlátozott megosztással”). Ha nincs szervezeti fiók, a feltétel maga zárja ki a Google-változatot, és a .docx-út egyenértékű. Az M1 SBI-beadandó a „Külön review” listán már szerepel (Adatvédelem :80). Nincs bizonyított hiba · —

BIZT-G2-9 · ELVETVE · — · — · — · A KAPU:212/:224 „a hely külön kérdés” mondata tényszerű tévesztő-magyarázat, és nem ad négyszemközti utasítást, így nem ütközik a HUM-SAFE-02-vel. Hogy kell-e mellé utalás, az ízlés kérdése · —

BIZT-G3-3 · ELVETVE · — · — · — · A cetliket a résztvevők a „teljes csoportnak láthatóvá” tételre tették ki (M1.A:282); a 4.3.2-es felolvasás (:440) ugyanennek a közönségnek szól, név nélkül, és a képző a könnyed, nem azonosítható cetliket választja. Kánoni szabálysértés (§4:61 passz) nem igazolható: a kitétel önkéntes. A súlyosító körülmény (kézírásból felismerhető szerző) spekuláció · a PED-G3-10-zel azonos tényállás

PED-G3-10 · ELVETVE · — · — · — · Ugyanaz a tényállás, mint a BIZT-G3-3-nál. Az „előre jelezd” javaslat preferencia; a 4.2.4 (:290) a rátekintésnél kifejezetten nem elemez cetliket · a BIZT-G3-3 duplikátuma

BIZT-G3-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A HUM :149 (HUM-PRIV-02 implementáció) az M1.A-t is felsorolja a központi felvételi szabályra hivatkozó activityk között; az M1.A-ban nincs ilyen hivatkozás (Grep „HUM-PRIV-02|fotó|felvétel|megsemmis”: 0 találat). A hiány TÉNY. Hogy az önfeltáró cetlikre a „kézírásos plakát”, a „név nélküli munkalap” vagy a visszaadás vonatkozik-e, az a DPO döntése. A puszta hivatkozás átvezetése a HUM :149 alapján a döntés nélkül is objektív lehet · önálló

BIZT-G3-7 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Fájlon belüli ellentmondás: M1.F:36 („Nem tesszük ki névvel, hogy ki hol tart, mit kell még pótolnia”) ↔ :313 Opció 2 („Ki az, aki inkább a Joharinál akadt el?”). A javaslat :57 / hub:216 része nem használható: a képző privát tudását a :36 kifejezetten megengedi („nem nyilvános mentorjegyzetében követheti”), csak az Opció 2 igazítandó · megtartandó az Opció 2 tényállására (részleges átfedés a PED-G3-8-cal)

PED-G3-8 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Valós eltérés: M1.F:47 „Létszám: 6–20 fő” ↔ KAPU:24 (és a hub) „egyéni vagy kiscsoportos támogatás”. A javaslat nem használható objektív javításként: a kánon nem ad létszámértéket, a létszám számszerű invariáns, és az „1–5 főnél Blokk 3 = beszélgetés” változat új tartalom, amelyet a modulgazdának kell megírnia. A safer-working mondat a :95-ben már megvan · részleges átfedés a BIZT-G3-7-tel; a létszámra ez a megtartandó

BIZT-G3-2 · EMBERI DÖNTÉS · emberi-döntés · P2-re csökkentve (P1-ről) · POST-PILOT · Az M1.A:503–505, az M1.B:389–391 és az M1.F:107 egyike sem sérti a §4:63–64-et: az M1.A:504 a nyilvános feldolgozás helyett külön beszélgetésre terel, kiküldésről pedig sehol nincs szó. A két mondat hiányzik, de ellentmondás nincs. Hogy a peulák képzői in-the-moment utasításának szó szerint át kell-e vennie a HUM-SAFE-03 facilitátori minimumát, vagy elég a képzőképzés (HUM-SAFE-05), az a Memuna alkalmazási kérdése. Ha jóváhagyják, a javítás szó szerinti átvétel · önálló

BIZT-G3-4 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Az M1.A 4.4.1 a saját célja szerint „személyesebb” gyakorlat (:477), így a §4:61 hatálya alá esik („indoklás nélkül passzolhat”). A :484–486 csak könnyebb sztorit kínál, passzt nem; a passz csak a ráhangolónál hangzik el (:185, :199). A §4.3 „Mondhatsz passzt” fordulatának szó szerinti átvétele objektív · önálló

BIZT-G3-6 · ELVETVE · — · — · — · Ellentmondás nem bizonyítható: az M1.A:273–274 a vakfolt „valódi feltárását” halasztja későbbre, az M1.B:382–385 pedig opcionális, csak pozitív, passzolható „apró visszajelzést” köt a Vakfolt-mezőhöz. Ez fokozatos nyitás, nem megszegett ígéret, és pedagógiai keretezés, nem biztonsági kérdés · —

**Összesítés**

| Verdikt | Darab | ID-k |
|---|---|---|
| MEGERŐSÍTVE | 8 | BIZT-G3-1, PED-G3-1, BIZT-G2-2, BIZT-G2-5, BIZT-G2-3, BIZT-G3-7, PED-G3-8, BIZT-G3-4 |
| ELVETVE | 5 | BIZT-G2-8, BIZT-G2-9, BIZT-G3-3, PED-G3-10, BIZT-G3-6 |
| EMBERI DÖNTÉS | 8 | BIZT-G2-1, BIZT-G3-5, BIZT-G3-9, BIZT-G2-4, BIZT-G2-10, BIZT-G2-6, BIZT-G3-8, BIZT-G3-2 |

A MEGERŐSÍTVE tételek közül 1 bizonyíték-kapu: a BIZT-G2-2.

**PILOT-BLOCKER:**
- **BIZT-G2-2:** (a) típus; csak szerepköri és runtime-bizonyíték kell, tananyag-módosítás nem.
- **BIZT-G2-1:** emberi döntés. A döntéshez szerkesztés nem kell; ha a döntés „csak kitalált”, a szöveg igazítása (b), azaz freeze-kivétel kell hozzá.

A K16 két tétele (BIZT-G3-1, PED-G3-1) P1 és POST-PILOT, mert a beadás helyén az M1.4:457 látható tiltást ad.

**Duplikátumok:**
- PED-G3-1 → a BIZT-G3-1 a megtartandó.
- PED-G3-10 ↔ BIZT-G3-3: mindkettő ELVETVE.
- BIZT-G3-7 ↔ PED-G3-8: részleges átfedés; a BIZT-G3-7 az Opció 2-re, a PED-G3-8 a létszámra megtartandó.
- BIZT-G2-3 ↔ BIZT-G2-10: részleges átfedés ugyanazon a szövegen (M1.3:914–916); együtt ütemezendő.
- Bemeneten átnyúló: BIZT-G2-4 ↔ IMPL-G2-3 (V2b) duplikátum, a BIZT-G2-4 a megtartandó; BIZT-G2-2 ↔ IMPL-G2-4 (V2b) részleges átfedés.

## B.V4 – peulák (25)

## M1 verifier V4: adverzális második kör (25 finding, nem RÉSZLEGES)

**Mit olvastam vissza a forrásban:**
- M1.F: teljes.
- M1.B: :55–:507.
- M1.A: :160–:280 és :350–:374.
- Hub: :1–:30 és :140–:284.
- KAPU: grep a :24, :85–86 és :306 sorra.
- M1.4: :466–:505.
- MAN: :20, :149 és :248; grep a „Peulák” / „Allowed attempts” szóra.
- RT: :88–:94 (19. pont).
- PT: :219.
- `course-content.md`: :60.
- Hozzáférhetőségi sztenderd: grep.
- Pilot quality bar: :55–:77.
- Anna-mátrix: :554 (E-M1-069) és :1069–:1075 (M1a/M1b).
- Elsődleges forrás: Moodle Docs 4.5, Assignment settings („Allowed attempts” idézet, szó szerint egyezik).

**Nem ellenőriztem:**
- a Moodle Docs „Restrict access” idézetét (a verdikt nem rajta múlik);
- az M1.3:805 sort;
- a MAN :114–129 teljes szövegét (csak azt, hogy „Peulák” vagy „Extra / F-peula” elem nincs benne);
- az M0 „a peulát a Moodle-ben találod” ígéretét.

Git-history nincs: a baseline ismeretlen, kivéve, ahol az Anna-mátrix szerkesztési maradványt rögzít (E-M1-069, M1a).

**Kánoni elsőbbség (K21):** sem szabály, sem lezárt döntés nem mondja meg, hogy modulon belül a hub vagy a részletes peulafájl az irányadó.
- Ezt a HUM-fájlban és repószinten is greppel kerestem.
- Mindkét fájl a 2. kánoni szint (`Modulok/`). A CLAUDE.md szerint ezek ellentmondása finding, és nem én választok közülük, ezért a típus emberi döntés.
- A döntéshez két szöveges támpont van: a hub „Rövid percbontás-vázlat” címkéje és a hub:196 „Részletek az M1.F peula-fájlban.” Ezek a peulafájl elsőbbségét valószínűsítik, de nem kodifikálják.

---

ERT-G3-1 · MEGERŐSÍTVE · objektív · P1→P2 · POST-PILOT · Az M1.F:277 („csak röviden segít (technika, „hol találom ezt?”)”) ellentmond a KAPU:24-nek és a hub:258-nak („facilitált, strukturált javítási alkalom (egyéni vagy kiscsoportos támogatás)”), valamint a hozzáférhetőségi sztenderd:116-nak („egyéni/kiscsoportos támogató tér”); a 4.4-ből hiányzik a hub:223 „mire figyel a javított SBI-ben” lépése. A javaslat csak részben használható: az M1.F:54 célját önmagában átírni új eltérést nyitna a hub:214-gyel (ugyanaz a „vagy” szöveg), a 4.4-be emelés pedig K21-terület; a 45’ és a safer-working (M1.F:95) marad · **K18 megtartandó**

ERT-G3-2 · ELVETVE · objektív · — · — · A Blokk 3 kifejezetten a kapus visszajelzésben jelzett hiányokra fókuszál (M1.F:293, :299), és a hangnem-sor lényegét (a személy minősítése) a „címke = ítélet a másikról” magyarázat fedi (M1.F:325, :361). Csak a „mindig/soha” nincs kimondva; ez képzői Q&A-ban áthidalható, kára nem bizonyított. Negyedik kulcspont felvétele a fix 10’-be preferencia · K18

PED-G3-2 · MEGERŐSÍTVE · objektív · P1→P2 · POST-PILOT · Az (a) rész (a javított vázlatot senki nem nézi át, M1.F:277) ugyanaz a tényállás, mint az ERT-G3-1-é. A (b) rész (hangnem kulcspontként) az ERT-G3-2 indokával nem bizonyított · duplikátum → **ERT-G3-1**

ERT-G3-4 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Az M1.B:148 és :495 „A/B sarok”, az M1.B:69 és :86 smiley-k mint sarokjelölők, a :218 régi MAG-címke ↔ a :214 és :241 négyopciós kvíz. Az Anna-mátrix :554 (E-M1-069) szerkesztési maradványként rögzíti · duplikátum → IMPL-G3-3

IMPL-G3-3 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · Ugyanazok a helyek (M1.B:148, :214, :218, :241, :495, :69, :86), szó szerint egyeznek. A javaslat a legpontosabb és a legszűkebb: a látható sorokhoz pin kell, az @asset-metaadathoz Edit, majd build, és a ✅-ok, a kérdések és az opciók változatlanok. Az a negyedik „mozgásos” fogalom (igaz/hamis oldal), amit a PED-G3-3 felvet, a :214-ben már szerepel · **K19 megtartandó**

PED-G3-3 · MEGERŐSÍTVE · objektív · P2 · POST-PILOT · A tényállás azonos az IMPL-G3-3-éval. A többletjavaslatai nem kellenek: az eszközlistába kért A–D sarokjelölő lap, a :214 kérdésenkénti átírása és a 4. kérdéshez új „→” visszajelzés túlmegy a minimális javításon, illetve új tartalom · duplikátum → IMPL-G3-3

ERT-G3-6 · ELVETVE · objektív · — · — · A 4. kérdés opciói mellett dőlt típusjegyzet áll (M1.B:242–245), ebből a képző kimondja a visszajelzést. A „címke a helyzetre” és az M1.F:325 között nincs érdemi ellentmondás: mindkettő címkének sorolja a mondatot. Kára nem bizonyított, képzői szinten áthidalható · K19 (nem duplikátum)

ERT-G3-9 · MEGERŐSÍTVE · objektív · P2→P3 · POST-PILOT · Az M1.B:192 és :203 fejenkénti kártyafelmutatást kér, a :70, :74, :140–143 és :186 viszont 3 képzői kártyát ír. Az Anna-mátrix :1071 (M1a) szerint az Anna-féle 4.1.1-átírás maradványa · duplikátum → IMPL-G3-4

IMPL-G3-4 · MEGERŐSÍTVE · objektív · P2→P3 · POST-PILOT · Ez a legteljesebb hely-lista (a :491 checklisttel együtt), és helyesen választja szét a látható sort (pin) és a metaadatot (build). Helyesen az eszközt igazítja a megtartott instrukcióhoz, mert a mátrix :554 szerint az M1.B:192–203 élő döntés. A fejenkénti készlet darabszáma gyártási kérdés, nem policy · **K20 megtartandó**

PED-G3-4 · MEGERŐSÍTVE · objektív · P2→P3 · POST-PILOT · Azonos tényállás. A „kézjel” alternatíva instrukció-módosítás lenne, ami szerzői választás; ezért az IMPL-G3-4 iránya a jobb · duplikátum → IMPL-G3-4

ERT-G3-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A hub:275–278 M1.B-végi név nélküli kérdése nincs az M1.B 4.4-ben (:431–478). Hogy a kérdés bekerüljön vagy a hub-sor törlődjön, az a hub ↔ peula elsőbbségi kérdés, és erre nincs szabály · duplikátum → PED-G3-9

ERT-G3-10 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A hub:221–222 („leckénként 1 gondolat”, „Közös fogalom-térkép”) eltér az M1.F:84–86 és :115 szövegétől. Az M1-HUB-POSZ-02 a „M1.F cél 4”-re hivatkozik (hub:178), de az M1.F-ben nincs 4. számozott cél. Az irányt ember dönti el (K21) · duplikátum → PED-G3-9

IMPL-G3-5 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · Ugyanez a tényállás, és igaz, hogy forrás nélküli gyártandó poszter (hub:172–203) áll szemben az M1.F-MUNK-01 notes (:209) mondatával, amely szerint a táblaábrák nem külön assetek. Hogy az asset törlődik vagy reuse lesz, az szerzői vagy médiafelelősi döntés · duplikátum → PED-G3-9

IMPL-G3-6 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A hub:147–151 percbontása eltér az M1.A:168–173-tól, igaz. A „példák a 4 mezőre” (hub:148) viszont képzői magyarázatként is olvasható, mert az M1.A:267–272 mind a 4 mezőt elmagyarázza. A hatás („élesben vakfoltot gyűjt”) feltételezés. Irány: K21 · duplikátum → PED-G3-9

IMPL-G3-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · Ugyanaz, mint az ERT-G3-8 (hub:276 ↔ M1.B:167). A lencse típusbesorolása helyes · duplikátum → PED-G3-9

PED-G3-9 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · Mindhárom hub ↔ peula eltérést lefedi (hub:148 ↔ M1.A:270; hub:178, :196, :221–222 ↔ M1.F:84–86, :115; hub:276–278 ↔ M1.B 4.4). Jól teszi fel a kérdést: a részletes peulafájl-e az irányadó. Döntéshozó: modulgazda vagy programvezető; a 45’ nem változik · **K21 megtartandó**

IMPL-G3-1 · ELVETVE · objektív · — · — · Az M1.F:68, :397 és az M1.B:478 „a képző nyitja meg, vagy … F-peula jelenléti completionje” mondata szó szerint a lezárt 2026-10-02-i projektgazdai döntés (MAN:20 ASSIGN-M, MAN:149, RT:90). A MAN:248 kezeli, hogy activity nincs. A peula ellenőrzőlistájának alapértelmezése a ma működő út: „megnyitom … ha nem az F-peula … nyitja meg”. Ellentmondás nincs. A restrict-access kötése már a runtime acceptance 19. pontjának nyitott tesztje (RT:94). (V2b-társ: IMPL-G2-1) · K24

IMPL-G3-2 · MEGERŐSÍTVE · bizonyíték-kapu (G3b, RT-P0-19) · P1→P2 · runtime-ellenőrzés (a), freeze-kivétel nem kell · A repóban sehol nincs „Allowed attempts” érték (grep a `02 Tervezet` alatt), pedig az RT:92 („további próbálkozás … csak a képző kézi nyitásával”) és az M1.B:476/:478 (az önkéntes új próbálkozás) 2-nél nagyobb vagy korlátlan értéket feltételez. A Moodle Docs 4.5 idézete szó szerint egyezik. Ha a staging értéke 2, az a pilot quality bar „törött completion/unlock” tétele lenne; ezt az M1.B előtt a stagingben kell visszaolvasni, és csak negatív eredménynél PILOT-BLOCKER (a). A peula-szöveg szűkítését („csak megerősített Teljesítve után”) nem javaslom: szűkítené a hub:8 és a KAPU:306 kánoni önkéntes finomítását, és döntést igényelne. A hub:8 csak „érdemes leadni”, nem „esedékes” · K24

PED-G2-10 · ELVETVE · objektív · — · — · Az M1.4:500 már kimondja, hogy az elfogadott beadás utáni önkéntes, csiszoltabb újrabeadás nem veszélyezteti a teljesítést. Az M1.B:476 és :507 szerint a képző a peulán szóban közli az új próbálkozást. Tájékoztatási finomítás, kára nem bizonyított · K24

IMPL-G3-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · POST-PILOT · A PT:219 (minden modulban „Peulák” és „Extra / F-peula” blokk) valóban eltér a MAN-tól (a :114 „Kurzusszintű elemek” alatt nincs ilyen elem; :248). Ez az 1. és a 2. kánoni forrás programszintű ellentmondása, nem csak M1-es. Az irány (MAN-bővítés vagy PT-pontosítás) és a leíró tartalom a nyitott N-M4-07-hez kötött, ezért ember dönti el (programvezető, build-felelős)

IMPL-G3-9 · MEGERŐSÍTVE · objektív · P2→P3 · POST-PILOT · A sorvégi két szóköz grep-pel igazolva az M1.F:171–172-n, és ez sérti a `course-content.md`:60 szabályát. A megjelenítést ma nem rontja: az idézetblokkon belül működő kemény sortörés. Kockázatot csak a sor következő szerkesztésekor jelent (`git diff --check`). Ugyanannak a fájlnak egy későbbi szerkesztésébe érdemes becsomagolni, külön szerkesztést nem indokol. A mátrix :1074 is P3-nak sorolja

IMPL-G3-10 · ELVETVE · objektív · — · — · A hozzáférhetőségi sztenderdben (:3 hatókör) nincs mozgásra vonatkozó követelmény, ezt a finding maga is elismeri. Nem pontozott bemelegítő játékokról van szó (M1.A:365, M1.B:214), ahol a képző helyben alkalmazkodik. Előírt követelmény sérülése nem bizonyított; ha kell, a hozzáférhetőségi gazda sztenderd-kérdése, nem tananyaghiba

PED-G3-5 · ELVETVE · objektív · — · — · Az M1.B:321 és :334 a 4 fős csoport forgását csak alulspecifikálja, nem teszi végrehajthatatlanná. Az M1.B:350 kifejezetten „3 vagy 4 kör”-t enged, a 26–30’ puffer (:393–395) elnyeli a 4. kört, a 10–30’ blokkhatár nem sérül. Képzői szinten áthidalható; a javasolt forgásszabály új tervezés

PED-G3-6 · ELVETVE · objektív · — · — · Az M1.F:101–104 előzetes képzői átgondolást kér, és a képző a 2.3 szerint (:99) átnézte az M1.1–M1.4-et. Az „érzés az I-ben” válasza ugyanebben a fájlban ott áll (M1.F:331 „mit okozott bennem”), és a mintakvízben is (M1.B:237). Kára nem bizonyított

PED-G3-7 · ELVETVE · objektív · — · — · Az M1.F:163–165 „nézd meg a Moodle-ben” utasítása természetes módon magában foglalja a belépést. Az :269 „kezdőpont” a kiválasztott lecke megnyitása. Wifi-leállásnál az A–D önbecslés fejből is elvégezhető. Sorrendi finomítás, kára nem bizonyított

---

**Összesítés**
- 10 MEGERŐSÍTVE: ERT-G3-1, PED-G3-2, ERT-G3-4, IMPL-G3-3, PED-G3-3, ERT-G3-9, IMPL-G3-4, PED-G3-4, IMPL-G3-2, IMPL-G3-9. Ebből 1 bizonyíték-kapu: IMPL-G3-2 (G3b, RT-P0-19).
- 8 ELVETVE: ERT-G3-2, ERT-G3-6, IMPL-G3-1, PED-G2-10, IMPL-G3-10, PED-G3-5, PED-G3-6, PED-G3-7.
- 7 EMBERI DÖNTÉS: ERT-G3-8, ERT-G3-10, IMPL-G3-5, IMPL-G3-6, IMPL-G3-7, PED-G3-9, IMPL-G3-8.
- PILOT-BLOCKER egy sincs. Az IMPL-G3-2 csak akkor lesz (a) típusú blokkoló, ha a staging „Allowed attempts” értéke 2-nek bizonyul; tananyag- vagy freeze-kivétel ehhez nem kell.

**Duplikátumok (a megtartandó vastagon)**
- K18: **ERT-G3-1** ← PED-G3-2. Az ERT-G3-2 nem duplikátum, hanem elvetve.
- K19: **IMPL-G3-3** ← ERT-G3-4, PED-G3-3. Az ERT-G3-6 külön tétel, elvetve.
- K20: **IMPL-G3-4** ← ERT-G3-9, PED-G3-4.
- K21: **PED-G3-9** ← ERT-G3-8, ERT-G3-10, IMPL-G3-5, IMPL-G3-6, IMPL-G3-7.
- K24: nincs megtartandó duplikátum. Az IMPL-G3-1 és a PED-G2-10 elvetve, az IMPL-G3-2 bizonyíték-kapu. Az IMPL-G3-1-nek a V2b-ben IMPL-G2-1 a társa.

---

# C. melléklet – nyers lencse-findingok (12 csoport)


# BIZT-G1

BIZTONSÁG-JOG lencse, M1, 1. fájlcsoport (hub + M1.1 + M1.2). Read-only review, egyik fájlt sem szerkesztettem. 7 finding: 3 P0, 3 P1, 1 P2.

Mindhárom fájlt teljes terjedelmében elolvastam. Kánoni kontextusként célzottan néztem: Adatvédelem §2–§5, HUM-PRIV-01, a HUM-fájl 10–11. szakasza, manifest §1–§2, runtime acceptance 6./15./24. pont, RELEASE-READINESS G2 és a Gyermekvédelem §2. Elsődleges webforrás: Moodle forráskód és MoodleDocs.

---

**BIZT-G1-1**
- **Súlyosság:** P0 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md` 10–11. szakasz (:494–575; nincs N-M1-04 sor) · `01 Fejlesztés/04 Audit/` (nincs hozzá döntési jegyzőkönyv)
- **Probléma:** A 2026-10-10-i N-M1-04 projektgazdai döntést egyik kánoni döntési nyilvántartásba sem vezették át. A döntés szerint az M1.1 SLIDE 5 önreflexiója kizárólag tanuló-lokális, központi tárolás nélkül, és nem completion-feltétel. Egyedül az audit-mátrix említi, ott is nyitott P0 döntésként.
- **Bizonyíték:** mátrix:243 „döntés — projektgazda (DPO utólagos QA): tárolja-e a pilot-build az M1.1 SLIDE 5 reflexióját”. Grep `N-M1-04` a teljes repóban: egyetlen találat, a mátrix-fájl. A HUM-fájl utolsó datált szakasza a 11. (:529, 2026-10-05).
- **Hatás:** Az LMS-gazda és a DPO kánoni forrásból nem látja, hogy a tárolás kizárt. A build a gyengébb „lehetőleg learner-local” szabályt követi (BIZT-G1-2), és kiskorú résztvevők személyes önreflexiója központilag tárolódhat.
- **Javaslat:** Objektív átvezetés. Új datált projektgazdai döntés-szakasz vagy -sor az `Emberi jóváhagyás szükséges.md`-be, a D-6 mintájára (HUM:527 „Az M5.1 opcionális mezője ugyanígy tanuló-lokális, sor nélkül.”). Tartalma a döntés szó szerinti szövege: „az opcionális személyes önreflexió (M1.1 SLIDE 5) kizárólag tanuló-lokális, központi tárolás nélkül; nem completion-feltétel”. Forrás a projektgazda 2026-10-10-i döntési csomagja, amelyet szó szerint rögzíteni kell a `01 Fejlesztés/04 Audit/` alatt. A mátrix N-M1-04 sorát a döntésre hivatkozva kell frissíteni. Az utólagos ellenőrző szerepet (a mátrix szerint DPO) csak a döntési csomagból szabad beírni, találgatni nem. Tilos a döntés tartalmát bővíteni (megosztás-kapcsoló, mentor-hozzáférés).
- **Típus:** objektív · **Állítás-osztály:** a döntés PROJEKT-DÖNTÉS; az átvezetés hiánya TÉNY
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. Tényleges P0 adatvédelmi hiba: a 2026-10-10-án indult M0+M1 pilot M1.1-es buildjének nincs kánoni forrása a tárolási tilalomról. Az átvezetés nem tananyag-módosítás.
- **Hipotézis:** N-M1-04 (0. szakasz :48–50; 11. szakasz M1-02 :1030; X-06 :1059; 13. szakasz :1130)

---

**BIZT-G1-2**
- **Súlyosság:** P0 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md:98`, `:794` · `02 Tervezet/LMS – activity manifest.md:45` (LMS-M1-01) · `02 Tervezet/LMS – H5P runtime acceptance.md:104` (24. pont)
- **Probléma:** Négy kánoni hely gyengébb az N-M1-04 döntésnél, vagy eltér tőle:
  - M1.1:98: ha a runtime-teszt bukik, a lecke a szabad szöveges mezőt Moodle-oldalra teszi. Ez TEXT-C-szerű, név szerinti, mentor által látható tárolás. Az M1.1-ben egyetlen szabad szöveges mező van, a SLIDE 5-é.
  - M1.1:794: a SLIDE 5 csak „lehetőleg” learner-local, a mentor láthatja, és jogalapot/megőrzést rendel hozzá.
  - MAN:45: csak „lehetőleg learner-local”.
  - RA:104: a tanuló-lokális lépések listája („LMS-M0-01…04, LMS-M1-03, LMS-M2-03, …”) nem tartalmazza az LMS-M1-01-et.
  - Mindez ellentmond a MAN:35 szabályának is: a tanuló-lokális lépésnek „Moodle-oldali tartalékútja sincs”.
- **Bizonyíték:**
  M1.1:98 „**A Course Presentation dián belüli szabad szöveges mező nem feltételezhető** – ha a teszt nem igazolja, a mező Moodle-oldalra kerül.”
  MAN:45 „a SLIDE 5 személyes reflexiója opcionális, nem completion-feltétel; lehetőleg learner-local”
- **Hatás:** A build-szerződés megengedi, a lecke tartalékútja pedig elő is írja kiskorú résztvevők opcionális, személyes, akár rejtett-mezős önfeltárásának név szerinti központi tárolását. A runtime-teszt ezt nem is ellenőrizné.
- **Javaslat:**
  - M1.1:98: ki kell mondani, hogy a Moodle-oldali tartalékút nem vonatkozik a SLIDE 5-re. Ez tanuló-lokális lépés, Moodle-oldali mezője és tartalékútja nincs (MAN:35; RA:41).
  - M1.1:794: a „lehetőleg … mentor … láthatja” mondat helyére a döntés szó szerinti szövege kerüljön N-M1-04 hivatkozással. A jogalap- és megőrzési hivatkozást a nem tárolt mezőnél el kell hagyni.
  - MAN:45: az LMS-M0-01 mintájára „tanuló-lokális: nem tárolt, nem completion-feltétel, beviteli mező nem rögzíti (N-M1-04; runtime acceptance 24. pont)”.
  - RA:104: a listába fel kell venni az LMS-M1-01-et.
  - Javítási korlát: nem változhat a completion-logika és az opcionális besorolás. A megvalósítás módját (beviteli elem nélkül vagy nem perzisztáló elemmel) a build választja, és az RT-P0-24 igazolja. Tanulói „nem tároljuk” mondat nem kerülhet be (RA:104 utolsó mondata).
- **Típus:** objektív · **Állítás-osztály:** PROJEKT-DÖNTÉS (N-M1-04, MAN:35 szabálya); TÉNY (az eltérés)
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. Freeze-kivételi P0 adatvédelmi hiba: a jelenlegi tartalékút a pilot M1 tanulóinál a döntéssel ellentétes központi tárolást írna elő.
- **Hipotézis:** N-M1-04; 12. szakasz „M1a” 3. pont (:1072): megerősítve

---

**BIZT-G1-3**
- **Súlyosság:** P0 · **Bizalom:** magas (a Moodle-tárolás forráskódból igazolt; az elemtípusonkénti xAPI-válasz közepes)
- **Lencse:** biztonság-jog
- **Hely:** M1.1:790–794 (SLIDE 5 H5P-beállítás) · RA:152 (RT-P0-24) · RA:143 (RT-P0-15) · `02 Tervezet/RELEASE-READINESS.md:25` (G2)
- **Probléma:** Nincs runtime-bizonyíték arra, hogy az M1.1 H5P-C activity a SLIDE 5 szövegét nem tárolja. A H5P-C profilban be van kapcsolva a próbálkozás-követés. Követett H5P activityben a Moodle az xAPI-eredmény válaszát adatbázisba menti, és a tanári szerep minden próbálkozást lát. Ha a SLIDE 5 xAPI-választ küldő elemmel (Free Text Question/Essay, RA:41) vagy mentett állapotú szövegelemmel (`H5P.ExportableTextArea`, RA:104) épül, a szöveg központilag tárolódik.
- **Bizonyíték:**
  MAN:16 „Moodle-beállítás (BSPEC-06): „Enable attempt tracking” = Yes”
  Moodle forráskód (`MOODLE_405_STABLE`, `mod/h5pactivity/classes/local/attempt.php`, `save_statement()`): `$record->response = $result->response ?? '';`. MoodleDocs „H5P activity”: „Teachers can see all attempts by all users from the Attempts report link.”
- **Hatás:** Amíg nincs readback, nem tudható, hogy a pilot buildje kiskorúak személyes szövegét tárolja-e, és látja-e a nem szerkesztő tanár (ADV:115).
- **Javaslat:** Nem javítható. Megvalósítási döntés: a projektgazda jóváhagyta (N-M1-04); a formális szerepköri bizonyíték függő. Kell:
  - RT-P0-24 readback az LMS-M1-01-re, BIZT-G1-2 után: tanulói fiókkal szöveget beírni, képzői fiókkal ellenőrizni, hogy a próbálkozás-riportban és a mentett állapotban nincs szöveg, és a completion nem függ tőle;
  - RT-P0-15 / 15. pont: a riport tényleges tartalmának visszaolvasása;
  - a G2 kapu (tracker #2);
  - a DPO release-ellenőrzése (FINAL_RELEASE_QA).
  Nem írjuk be és nem feltételezzük.
- **Típus:** bizonyíték-kapu · **Állítás-osztály:** TÉNY (Moodle-viselkedés, hiányzó bizonyíték); PROJEKT-DÖNTÉS (N-M1-04)
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER az M1.1 valódi pilot-tanulóknak történő megnyitására. A HUM-PRIV-01 a „Blokkol: éles learner release minden személyes adatot tároló activitynél” szabállyal köti (HUM:136); a PILOT-1 M0+M1 bizonyítéklistájába tartozik. Ez nem tartalmi módosítás.
- **Hipotézis:** N-M1-04 (mátrix:243, „a próbálkozás-riportot az ADV:115 szerint a nem szerkesztő tanár is látja”): megerősítve

---

**BIZT-G1-4**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M1.1:763–774 (SLIDE 5, „Szöveg a dián”)
- **Probléma:** A dia közli, hogy az írás opcionális. Azt viszont nem mondja meg a mező előtt, hogy a válasz csak a tanulónál marad, és senki nem olvassa. Azt sem, hogy veszélyhelyzetet vagy feltárást ne ide írjon, hanem a segítségkérő útra vigye. Közben a 2. kérdés rejtett mezős önfeltárásra hív, az 1. kérdés más személyekre utal.
- **Bizonyíték:**
  M1.1:763 „1 szövegmező („Ide írj, ha szeretnél. Elég 2–3 mondat.”)”
  M1.1:771 „Van-e olyan dolog magadban, amit szívesen megmutatnál a többieknek, de még nem tetted?”
- **Hatás:** Egy kiskorú tanuló azt hiheti, hogy a mentora olvassa, amit beír. Ha ide ír le egy feltárást, az senkihez nem jut el. A Z.2:307 ugyanerre a helyzetre mező melletti mondatot tartalmaz („ha veszélyről van szó, azt ne a reflexióba írd, hanem azonnal vond be a Memunát”).
- **Javaslat:** EMBERI DÖNTÉS: kapjon-e a SLIDE 5 mező előtti megjegyzést.
  - (a) „csak nálad marad, senki nem olvassa” típusú mondat: kizárólag a sikeres RT-P0-24 readback után (RA:104 utolsó mondata). Döntő: projektgazda; utólagos QA: DPO.
  - (b) A Z.2:307 mintájú feltárás-irányító mondat új alkalmazási esete. Szövegezését a Memuna hagyja jóvá.
  Új szakpolitikai szöveget nem írunk; a meglévő M1.1:90 segítő blokk tartalma nem változik.
- **Típus:** emberi-döntés · **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A Moodle-intro (M1.1:90) a lecke előtt megadja a passz- és a gyermekvédelmi utat, a „nem tároljuk” állítás pedig readback előtt amúgy sem kerülhet be. Nem freeze-kivételi P0.
- **Hipotézis:** N-M1-04 (mátrix:243 „vagy a mező előtt tájékoztatni” ág): részben; a tárolással kombinált tájékoztatás ága elvetve

---

**BIZT-G1-5**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md:85–86` (és :36)
- **Probléma:** A hub az M1.1 Check-részébe egy személyes, nyitott kérdést ír. A leckében ilyen nincs: a Check három zárt kvízkérdés (M1.1:857–912), az egyetlen nyitott személyes szöveg pedig a SLIDE 5 opcionális, tanuló-lokális önreflexiója. A hub ezzel completion-részként kezelt személyes szabad szöveget sugall, ami ellentmond az N-M1-04-nek és az Adatvédelem §2 alapértelmezésének (ADV:29).
- **Bizonyíték:**
  hub:85 „Activity: 1–2 egyszerű kvíz / önreflexiós kérdés a diák között;”
  hub:86 „Check: 1 nyitott kérdés arról, milyen visszajelzés segített már neki.”
- **Hatás:** Ha a hubból építik vagy pótolják a leckét, tárolt, személyes nyitott válasz kerülhet a completion-útvonalba.
- **Javaslat:** A hub M1.1 „Tartalom röviden” részét a leckéhez kell igazítani: a Check három zárt kvízkérdés; az Activity opcionális, tanuló-lokális önreflexió (N-M1-04). Javítási korlát: a 4. kompetencia (hub:36) „reflexiós produktum” helyét ez a finding nem dönti el. Ha ott tárolt produktum a szándék, az EMBERI DÖNTÉS: projektgazda, DPO utólagos QA-val.
- **Típus:** objektív · **Állítás-osztály:** TÉNY (a hub és a lecke eltérése); PROJEKT-DÖNTÉS (N-M1-04)
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A build-szerződés (MAN:45) és a lecke nem tartalmaz ilyen Check-et; ez hubszöveg, nem freeze-kivételi P0.
- **Hipotézis:** új

---

**BIZT-G1-6**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M1.1:204 (SLIDE 1 „Megvalósítás”) · M1.1:335–344 (SLIDE 2 emoji-skála)
- **Probléma:** A lecke a helyes válasz nélküli önbevallós kérdésekre két utat enged. Az elsődleges út szöveg + Tovább gomb, ez nem rögzít. A tartalékút választós H5P-elem, ez követett H5P-C activityben tanulónként rögzíti a pillanatnyi érzelmi állapotot („Kicsit feszült vagyok tőle”), és a tanári szerep látja (BIZT-G1-3 bizonyítéka). Erről a tárolásról nincs döntés: a D-i (HUM:561) csak a completiont rendezi, a D-j csak az M2.3 tárolását.
- **Bizonyíték:**
  M1.1:204 „ha mégis választós H5P-elem kell, minden opciót helyesnek kell jelölni, és ezt a runtime acceptance igazolja.”
  M1.1:335 „*Hogy érzed magad most ettől a témától?*”
- **Hatás:** Pedagógiailag nem szükséges, név szerinti érzelmiállapot-adat keletkezhet kiskorúakról. Ez ütközik az ADV:22 „szükséges-e egyáltalán begyűjteni” elvével.
- **Javaslat:** EMBERI DÖNTÉS. Döntő: projektgazda, utólagos QA: DPO. A kérdés: csak a nem rögzítő szöveges út megengedett-e, vagy a választós út tárolása elfogadható. Bizonyíték mindkét esetben: staging-readback a próbálkozás-riportról (runtime acceptance 15. pont). A completion-logika nem változhat (D-i).
- **Típus:** emberi-döntés · **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. Az elsődleges út nem rögzít, és az adat nem különleges kategóriájú. Hogy ténylegesen melyik út épült, azt a pilot staging-readbackje mutatja meg.
- **Hipotézis:** új

---

**BIZT-G1-7**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** biztonság-jog
- **Hely:** M1.1:926 (SLIDE 6 zárószöveg)
- **Probléma:** A szöveg a madrih (aki maga is lehet kiskorú) önfeltárását a kvucához (kiskorú hanihokhoz) való közelség eszközeként keretezi, a szakmai határra hivatkozás nélkül. Az M1 nincs benne a Memuna G1-átnézésének hatókörében (Gyermekvédelem :17). Ezzel szemben az M4 önfeltáró elemeit a Memuna átnézi (HUM:278).
- **Bizonyíték:** M1.1:926 „Madrihként ez a **hitelesség** egyik eszköze: nem kell mindent kitenned, de amit megmutatsz magadból, azzal közelebb engeded a kvucát.”
- **Hatás:** Határkeret nélkül a „közelebb engedés” a madrih–hanih viszonyban félreérthető lehet.
- **Javaslat:** EMBERI DÖNTÉS: a Memuna döntse el, kell-e határkeret ehhez a mondathoz, és ha igen, milyen meglévő kánoni szöveggel. Új szabály nem írható.
- **Típus:** emberi-döntés · **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A mondat már tartalmaz korlátot („nem kell mindent kitenned”); nem P0.
- **Hipotézis:** új

---

**Elvetett hipotézisek**
- **N-M1-04 mint nyitott döntés** („UNRESOLVED … tárolja-e a pilot-build”; mátrix :48–50, :243, M1-02 :1030, X-06 :1059, 13. szakasz :1130): a 2026-10-10-i projektgazdai döntés lezárta. Ami nyitva marad: átvezetés (G1-1), a források igazítása (G1-2), runtime-bizonyíték (G1-3). A mátrix „vagy a mező előtt tájékoztatni” alternatíváját (tárolás tájékoztatással) a „kizárólag tanuló-lokális” döntés kizárja.
- **N-M1-04, „tanulói megosztás-kapcsoló”** (mátrix:243): nem a mai fájlok hibája, a döntés központi tárolás nélküli. Ha új igényként felmerül, emberi döntés.
- **M1.2 önfeltárás vagy valós személyekről szóló megfigyelés:** nem igazolódott. Az M1.2-ben nincs szabad szöveges bevitel; minden példa kitalált, kötött item. A segítő blokk (M1.2:42) azonos az M1.1:90-nel.

**Források (elsődleges)**
- [Moodle forráskód, `MOODLE_405_STABLE`, `mod/h5pactivity/classes/local/attempt.php`](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/classes/local/attempt.php) – a kódsort egy összefoglaló fetch-eszköz adta vissza, a fájlt magam nem olvastam. Megerősítésre szorul.
- [MoodleDocs – H5P activity (5.2)](https://docs.moodle.org/502/en/H5P_activity) – a 4.5-ös dokumentációs oldal 404-et adott, ezért az 5.2-es oldalt használtam.

**Érintett fájlok**
- 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- 02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/RELEASE-READINESS.md
- 01 Fejlesztés/04 Audit/2026-10-10 Anna-kommitok és szakmai javaslatok – teljes megfeleltetési mátrix.md


# BIZT-G2

## M1, 2. fájlcsoport: biztonság-jog lencse (KAPU, M1.3, M1.4)

Mind a három fájlt végigolvastam, a kanonikus szakaszokat célzottan. Tíz findingot találtam: kettő P0, három P1, öt P2. Kettő pilot-blokkoló: a BIZT-G2-1 (nyitott emberi döntés) és a BIZT-G2-2 (hiányzó bizonyíték). Fájlt nem szerkesztettem. A runtime-működést nem tekintettem ellenőrzöttnek.

---

**BIZT-G2-1**
- **Súlyosság:** P0 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1.3 – SBI-modell….md:886`. Ugyanez a nyitott kérdés érinti még: M1.3:902 (NAR-05), M1.3:1059 (NAR-06), hub:117, `LMS – activity manifest.md:48`.
- **Probléma:** Az M1.3 6. diája engedi, hogy a tanuló valós, névtelenített helyzetet írjon a tárolt, névhez kötött mezőbe (LMS-M1-07, TEXT-C). Hogy ez megengedett-e, az a nyitott N-1 döntés. Közben az M1.4 ugyanerre a helyzettípusra azt mondja, hogy név nélkül is visszaazonosítható.
- **Bizonyíték:**
  - M1.3:886: „Lehet valós, hétköznapi helyzet (pl. múlt heti peula, de név és felismerhető részlet nélkül)”
  - M1.4:457: „Valós helyzetet – név nélkül sem – ne írj le: egy kis közösségben könnyen kiderül, kiről van szó.”
  - manifest:48: „nyitott: kerülhet-e ide valós, névtelenített helyzet … (gazda: projektgazda; vétó: DPO; BSPEC-02 leltár N-1)”
  - `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md:85`: „Változatlanul nyitva … N-1”
- **Hatás:**
  - Más madrihokról vagy kiskorú hanihokról szóló, visszaazonosítható viselkedésleírás kerülhet a Moodle-be, a szerző nevével.
  - Ezt a mentor, a szerkesztő tanár, a menedzser és a rendszergazda is látja (BIZT-2), és a képzés vége után 90 napig megmarad.
  - Az érintett harmadik fél erről nem tud.
  - A NAR-06 („az Assignmentben erre építhetsz”) a valós mini-SBI továbbvitelét sugallja olyan beadandóba, ahol valós helyzet tilos.
- **Javaslat:** EMBERI DÖNTÉS (N-1): a projektgazda dönt, a DPO-nak vétójoga van. A kérdés: kerülhet-e valós, névtelenített helyzet az LMS-M1-07-be, vagy – ahogy az M1.4 és az Adatvédelem §3:82 M3-as sora indokolja – csak kitalált. A döntés alapja: Adatvédelem §2:29 („Mindig elfogadható legyen fiktív…”) és M1.4:457. Döntés után a döntést szó szerint át kell vezetni ide: M1.3:886, NAR-05/NAR-06, hub:117, és a manifest:48 szerinti TEXT-C-tájékoztatóba. A döntés előtt tilos a tanulói szabályt átírni.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. Az ellentmondás TÉNY.
- **Pilot-besorolás:** PILOT-BLOCKER. Nyitott adatvédelmi döntés egy pilot-activityn (LMS-M1-07), amely kiskorúakra vonatkozó adatot érint. A döntéshez nem kell szerkesztés; ha a döntés „csak kitalált”, a szövegjavítás az adatvédelmi freeze-kivétel alá esik.
- **Hipotézis:** új (BSPEC-02 leltár N-1, nem mátrix-tétel)
- **Verdikt:** —

---

**BIZT-G2-2**
- **Súlyosság:** P0 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** két adatgyűjtő pont: LMS-M1-05 (M1.4 Assignment, kapu) és LMS-M1-07 (M1.3 TEXT-C). Hivatkozott helyek:
  - `Adatvédelem – tanulói adatok és AI.md:207`, `:209`, `:230`
  - `LMS – H5P runtime acceptance.md:143`
  - `Emberi jóváhagyás szükséges.md:574`
- **Probléma:** A pilot 2026-10-10-én elindult (HUM:547–548, M0+M1). Az M1 két névhez kötött adatgyűjtő pontjához a repóban nincs meg a szükséges szerepköri és runtime-bizonyíték:
  - a DPO jóváhagyása a tájékoztatóra;
  - az activity-szintű adatleltár kitöltése, beleértve a megőrzési sor hozzárendelését;
  - az adatvédelmi kontakt;
  - az Adatvédelem §3:80 szerint kötelező külön review az „M1 SBI-beadandóra”;
  - az RT-P0-15 láthatósági teszt.
- **Bizonyíték:**
  - Adatvédelem:230: „A tájékoztató a §1 release-szabálya szerint a DPO jóváhagyása előtt nem élesíthető.”
  - runtime acceptance:143: „| RT-P0-15 | `IMPLEMENTATION_TEST_REQUIRED` | 15. Szabad szöveg láthatósága |”
- **Hatás:** Pilot-tanulók, köztük kiskorúak, névhez kötött szövege kerülhet olyan rendszerbe, ahol a láthatóság igazolatlan, a tájékoztatót senki nem hagyta jóvá, és nincs adatvédelmi kontakt.
- **Javaslat:** A kapuk és szerepek:
  - **G2** – DPO release-ellenőrzés (FINAL_RELEASE_QA), és az activity-leltár §9:207 sora (RELEASE-EVIDENCE): ezt a privacy felelős és az LMS-gazda tölti ki, a DPO-nak vétójoga van;
  - **G2 + G3b** – az RT-P0-15 lefuttatása (POST-BUILD), két mentorral és két csoporttal, a HUM:574 feltételei szerint;
  - **G4b/G8** – a `PRIVACY_CONTACT_TO_CONFIGURE` kitöltése;
  - a hiányt a programvezető M0+M1 GO/NO-GO evidence listájának rögzítenie kell (PILOT-1).

  Megfogalmazás: „megvalósítási döntés: projektgazda jóváhagyta (HUM-PRIV-01, D-1, RT-P0-15 feltételek); a formális szerepköri bizonyíték függő”. Bizonyítékot nem írunk be és nem feltételezünk.
- **Típus:** bizonyíték-kapu
- **Állítás-osztály:** PROJEKT-DÖNTÉS (HUM-PRIV-01, D-1, HUM:574). A bizonyíték hiánya a repóban TÉNY.
- **Pilot-besorolás:** PILOT-BLOCKER. Nem kell hozzá tartalmi szerkesztés, ezért a freeze nem érinti. A kánon szerint ezek nélkül az activity nem nyitható meg valódi madrihnak (Adatvédelem:230; Program terv:228).
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-3**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1.3….md:914–915` (SLIDE 6, „Biztonsági megjegyzés”)
- **Probléma:** A tárolt mini-SBI mező melletti megjegyzés egy „nagyon nehéz helyzet” átírását („finomíthatsz rajta”) ajánlja, és nem mondja ki a kanonikus utasítást: valós gyermekvédelmi helyzetet ne tanulási feladatba írj, hanem azonnal vond be a Memunát. Ez az utasítás az M1.4:508-ban és az Adatvédelem §11:241-ben megvan.
- **Bizonyíték:**
  - M1.3:914–915: „Ha egy nagyon nehéz helyzet jut eszedbe, nyugodtan finomíthatsz rajta, / vagy választhatsz enyhébb, fiktív verziót is.”
  - Adatvédelem:241: „Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd: azonnal vond be a kijelölt Memunát”
- **Hatás:**
  - Valós, akár bántalmazásra utaló helyzet kerülhet „finomítva” a névhez kötött Moodle-mezőbe, ellentétben a HUM-SAFE-01-gyel (Gyermekvédelem:84).
  - A manifest:24 szerint a TEXT-C-tájékoztató szó szerint átveszi a lecke megjegyzését, így a hiány a mező elé is átkerül.
- **Javaslat:** Az M1.3 6. dia biztonsági megjegyzése után szó szerint át kell vezetni az M1.4:508 mondatát (vagy az Adatvédelem §11:241 mondatát), a HUM-SAFE-01 azonosítóval.

  Tilos hozzányúlni: a „Ha ez a téma téged is érint” blokkhoz (HUM-SAFE-03, szó szerinti kánon); a passz- és szünet-joghoz; a Memuna-útvonal tartalmához. A „finomíthatsz rajta” mondat sorsa a BIZT-G2-10 kérdése; új szakpolitikai mondat nem kerülhet be.
- **Típus:** objektív
- **Állítás-osztály:** PROJEKT-DÖNTÉS (HUM-SAFE-01, HUM-PRIV-01). A hiány TÉNY.
- **Pilot-besorolás:** POST-PILOT. Ugyanazon a dián a HUM-SAFE-03 blokk már a gyermekvédelmi útra terel (M1.3:918), és a spontán feltárásra a manifest §1 eljárása vonatkozik, ezért a P0-s freeze-kivétel nem teljesül.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-4**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** `M1.4….md:502`. Ugyanez a kérdés: `M1.3….md:926`, `Adatvédelem….md:109`, `:117`.
- **Probléma:** A tanulói szöveg azt ígéri, hogy a kapu-beadást „a kijelölt mentorod/értékelőd látja”. A build-spec szerint viszont:
  - az ASSIGN-M beadásokat a csoporttól függetlenül minden nem szerkesztő tanár látja, és a szűkítés nincs rögzítve (BIZT-5);
  - a TEXT-C és az ASSIGN-M esetén a szerkesztő tanári, menedzseri és rendszergazdai hozzáférés nyitott DPO-kérdés (BIZT-2).
- **Bizonyíték:**
  - M1.4:502: „A beadásodat a kijelölt mentorod/értékelőd látja (és ha újraértékelést kérsz, a második képző is).”
  - Adatvédelem:117: „| ASSIGN-S, ASSIGN-M, GATE-CP | … nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) |”
- **Hatás:** A címzettekről adott tájékoztatás pontatlan lehet. A kapu-beadást kiskorú tanuló is adja, és többen láthatják, mint amennyit a szöveg ígér.
- **Javaslat:** EMBERI DÖNTÉS (DPO): a BIZT-5 (az ASSIGN-M csoport szerinti szűkítése) és a BIZT-2 (szerkesztő tanári, menedzseri, rendszergazdai hozzáférés) eldöntése. Döntés után a beállítást az RT-P0-15 olvassa vissza, és a tanulói mondatot a döntéshez kell igazítani (M1.4:502 és a §11 „Ki látja?” szakasza). A döntés előtt a tanulói mondat nem írandó át.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL (BIZT-2, BIZT-5). A szabály maga (HUM-PRIV-01) PROJEKT-DÖNTÉS.
- **Pilot-besorolás:** POST-PILOT önállóan. A pilotra gyakorolt hatását a BIZT-G2-2 fedi, mert a DPO tájékoztató-jóváhagyása az Adatvédelem:230 szerint épp ezeken a kérdéseken múlik.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-5**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1.4….md > 3.1. Assignment leírás` (:442–510); `LMS – activity manifest.md:20` (az ASSIGN-M profil)
- **Probléma:** A Program terv §4 szerint a tényleges Assignment-beadás előtt egy rövid adatkezelési tájékoztatónak kell állnia, amely öt kérdésre felel: mit rögzítünk, mire használjuk, meddig őrizzük, ki látja, kihez fordulhatsz. Az M1.4 kapu-Assignmentje ezt nem tartalmazza:
  - csak a „ki látja” szerepel (:502), a beadási lépések után;
  - a cél és a megőrzés nincs benne (Assignment: a képzés vége + 12 hónap; kapueredmény: 24 hónap);
  - az ASSIGN-M profil a TEXT-C-vel ellentétben nem specifikál ilyen tájékoztatót.
- **Bizonyíték:** Program terv:225: „…a tényleges Assignment-beadások… a feladat ELŐTT ott áll egy rövid, életkorhoz illő, célonként tagolt „just-in-time” tájékoztató doboz.”
- **Hatás:** A tanuló, aki gyakran kiskorú, a kapu-beadás előtt nem tudja meg, mire és meddig őrizzük a szövegét.
- **Javaslat:** Az M1.4 3.1 elejére, az 1. lépés elé tájékoztató doboz kerüljön, kizárólag lezárt szöveg szó szerinti átvezetésével:
  - a cél: Adatvédelem §11:243 első mondata;
  - a megőrzés: §11:250 és §11:252 („a végső pontszámodat és a kapueredményedet: 24 hónapig”; „a beadandóidat és a peulaterveidet: a képzés vége után 12 hónapig”);
  - a kontakt: utalás a kurzus adatvédelmi tájékoztatójára (Program terv:229).

  A „ki látja” sor a BIZT-G2-4 döntéséig marad. Megőrzési időt és kontaktot kitalálni tilos.
- **Típus:** objektív
- **Állítás-osztály:** PROJEKT-DÖNTÉS (Program terv §4, HUM-PRIV-01). A hiány TÉNY.
- **Pilot-besorolás:** POST-PILOT. A kurzusszintű §11-es tájékoztató tartalmazza a megőrzést és a címzetteket, így ez nem P0-s freeze-kivétel; az élesíthetőséget a BIZT-G2-2 kezeli.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1 – Kapu – értékelő….md:27` (0. fejléc, „Gyermekvédelmi feltárás a beadványban”)
- **Probléma:** A kapu előírja a Memuna bevonását és az incidensnyilvántartást, de nyitva hagy három dolgot:
  - ki és hogyan veszi ki a feltárást tartalmazó beadványt a Moodle Assignmentből (az Adatvédelem:75 szerint az ilyen adat kikerül a Moodle-ből);
  - mi lesz ilyenkor a kapu értékelésével és a 24 órás megerősítési határidővel (:26);
  - milyen alternatív beadási utat kap a tanuló.
- **Bizonyíték:**
  - KAPU:27: „Az ügy dokumentációja nem Moodle-ben, hanem külön, hozzáférés-korlátozott incidensnyilvántartásban készül; a rubrikába és a Moodle-visszajelzésbe nem írsz róla azonosítható részletet.”
  - Adatvédelem:75: „Ha feltáráskor mégis megjelenik, kikerül a Moodle-ből”
- **Hatás:** A feltárást tartalmazó beadvány a 12 hónapos Assignment-megőrzésben maradhat, minden tanárszerep számára láthatóan. Az értékelő sem tudja, értékelje-e a beadványt.
- **Javaslat:** EMBERI DÖNTÉS. A Memuna (HUM-SAFE-01), az értékelési felelős és a DPO dönt: ki és milyen Moodle-mechanizmussal (runtime-teszttel igazolva) távolítja el a beadványt, mi a kapueredmény ilyenkor, és milyen alternatív beadási út van. A jelzési úthoz és a Memuna szerepéhez tilos hozzányúlni.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. A hivatkozott szabályok PROJEKT-DÖNTÉS (HUM-SAFE-01, HUM-PRIV-01).
- **Pilot-besorolás:** POST-PILOT. Az azonnali eszkalációs út megvan és helyes; a nyitott rész eljárási és megőrzési kérdés.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1.3….md:814` (M1.3-NAR-04-VO); `:750` (a NAR-04 spec)
- **Probléma:** Az 5. dia narrációja és spec-je „beírásra” kéri a tanulót. A D-1 szerint ez a dia tanuló-lokális, beviteli elem nélkül, a dián pedig ez áll: „Írd le magadnak… nem adod be”. A narráció így beviteli mezőt és tárolást sugall.
- **Bizonyíték:**
  - M1.3:814: „Képzelj el egy egyszerű helyzetet, és próbáld meg beírni,”
  - M1.3:799: „a dián nincs beviteli elem, a tanulói mutató: „Írd le magadnak, jegyzetbe vagy papírra; nem adod be.””
- **Hatás:** A tanuló mezőt keres, vagy azt hiszi, hogy a gyakorlását tároljuk. A D-1 tanuló-lokális jellege a hangban elmosódik.
- **Javaslat:** A NAR-04-VO szövegében és a spec-ben a „beírni” / „írja be” helyére „leírni” / „írja le” kerüljön. Ez VO-változás: a VO QA-repó fix packján, újrarenderelésen és látható szöveg pinelésén megy át. A D-1 tartalmához és a completion-logikához tilos hozzányúlni.
- **Típus:** objektív
- **Állítás-osztály:** PROJEKT-DÖNTÉS (D-1, HUM:522). Az eltérés TÉNY.
- **Pilot-besorolás:** POST-PILOT. A PILOT-4 szerint az M0/M1 narráció opcionális, és adat nem tárolódik.
- **Hipotézis:** új (a 3. lencse-fókusz)
- **Verdikt:** —

---

**BIZT-G2-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** `M1.4….md:526` (@asset M1.4-MUNK-01, technical.note)
- **Probléma:** A kapu fájlalapú beadási sablonja „Google Doc (csak szervezeti fiókban…) és/vagy .docx” formában készül. A HUM-PRIV-01 szerint Google-sablon csak szervezeti fiókban használható, nem tudni viszont, van-e a 15–17 éves tanulóknak szervezeti fiókjuk. A sablon a Google-sablonok adatvédelmi review-listájában sem szerepel (Adatvédelem:87: csak az M5.4 és az M6).
- **Bizonyíték:**
  - M1.4:526: „Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx”
  - Adatvédelem:53: „Google-sablon csak **szervezeti fiókban**, korlátozott megosztással használható”
- **Hatás:** A kiskorú tanuló a sablont a saját, személyes Google-fiókjába másolhatja, és ott tölti ki. Így a kapuprodukt egy harmadik fél személyes fiókjába kerül.
- **Javaslat:** EMBERI DÖNTÉS: a DPO és az LMS-gazda dönt arról, hogy a tanulók kapnak-e Google Doc-változatot (vagyis van-e szervezeti fiókjuk), vagy csak .docx/PDF jár. Az eredményt fel kell venni az Adatvédelem §3/§9 Google-sablon leltárába.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. Ez a lezárt HUM-PRIV-01 új alkalmazási esete.
- **Pilot-besorolás:** POST-PILOT. A .docx és az online szöveges út egyenértékű (M1.4:544), így a kockázat a Google-változat kiadása nélkül nem áll fenn.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-9**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** biztonság-jog
- **Hely:** `M1 – Kapu – értékelő….md:212` (Item 7), `:224` (Item 8)
- **Probléma:** Az item-bank „csak négyszemközt” / „csak 1:1-ben” tévesztőinek visszajelzése szerint „a hely külön kérdés”. A gyakorlatban az SBI címzettje gyakran hanih (KAPU:138; M1.4:138), a kettesben zajló helyzetre pedig a HUM-SAFE-02 vonatkozik. A visszajelzés erre nem utal.
- **Bizonyíték:** KAPU:224: „Az sem a különbség, hol mondod el (a „csak 1:1-ben” válasz): a hely külön kérdés.”
- **Hatás:** A tanuló nyitott kérdésként kezelheti, hogy hanihnak négyszemközt adjon-e visszajelzést. Ugyanez a fájl a saját kettesben folyó helyzeteire kifejezetten utal a HUM-SAFE-02-re (:24).
- **Javaslat:** EMBERI DÖNTÉS: a Memuna (a HUM-SAFE-02 utólagos ellenőrzője) dönt arról, kell-e az item-visszajelzésbe utalás. Ha igen, csak a meglévő kánoni mondat kerülhet át (KAPU:24: „Kettesben folyó helyzetben a … §4.2 safer-working szabálya érvényes… (HUM-SAFE-02)”). A helyes választ jelölő ✅ és a tévesztők érintetlenek maradnak.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Pilot-besorolás:** POST-PILOT. Az item-bank formatív, a szöveg nem ad 1:1-utasítást, így nem P0-s hiba.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G2-10**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** biztonság-jog
- **Hely:** `M1.3….md:914–916`; `M1.4….md:506–507`
- **Probléma:** Mindkét leckében egy egyedi, „ha nagyon nehéz helyzet jut eszedbe” típusú támogató szöveg áll a kanonikus HUM-SAFE-03 blokk mellett. A HUM-SAFE-03 §4.3 szerint minden ilyen egyedi blokk helyére a kanonikus blokknak kell kerülnie. Ugyanakkor ezek a szövegek adattakarékossági tanácsot is adnak (enyhébb, fiktív helyzet választása), amelyet a `course-content.md` szerint nem szabad törölni.
- **Bizonyíték:**
  - Gyermekvédelem:102: „Minden meglévő, ad hoc „ha nehéz / ha téged is érint / ha felkavar” típusú támogató blokk helyére ez kerül”
  - M1.4:506: „Ha nagyon nehéz vagy személyes helyzet jut eszedbe, nyugodtan válassz”
- **Hatás:** Párhuzamos, eltérő hangú támogató szövegek állnak egymás mellett, és az M1.3-ban ezek egyike a nehéz helyzet „finomítására” biztat (lásd BIZT-G2-3).
- **Javaslat:** EMBERI DÖNTÉS: a Memuna (a HUM-SAFE-03 utólagos ellenőrzője) dönt arról, hogy ezek kiváltandó támogató blokkok vagy megtartandó, feladatszintű adattakarékossági utasítások. Döntés előtt egyiket sem szabad törölni vagy átírni.
- **Típus:** emberi-döntés
- **Állítás-osztály:** EMBERI JÓVÁHAGYÁS KELL. Ez a lezárt HUM-SAFE-03 alkalmazási kérdése.
- **Pilot-besorolás:** POST-PILOT. Mindkét dián megvan a kanonikus blokk, és nincs veszélyes utasítás.
- **Hipotézis:** új
- **Verdikt:** —

---

### Elvetett hipotézisek

- **M1-03 (N-M1-06, -07, -09, -11), a rubrika láthatósága:** Nem biztonsági-jogi kérdés. A szempontok a forrásban a beadás előtt láthatók (M1.4:478–487); hogy a Moodle-ben ténylegesen megjelennek-e, az az implementációs lencsére tartozik.
- **X-06 / M1-02 (N-M1-04), az M1.1 SLIDE 5 reflexiója:** A KAPU, az M1.3 és az M1.4 sehol nem hivatkozik az M1.1 reflexiójára (Grep: 0 találat), és nem mond ellent a 2026-10-10-i döntésnek. Az M1.3 5. diája a D-1 hatálya alá tartozik, ez külön tétel; a narrációs eltérése a BIZT-G2-7.
- **12. szakasz, M1a, „1–2 vs. 2–3 mondatos SBI”:** A széttartás ma is fennáll (M1.4:450 „1–2 mondatos”, KAPU:21 és :197 „2–3 mondatos”), de ez értékelési lencse, nem biztonság-jog. Az értékelési reviewernek kell továbbadni, nem eldobni.
- **12. szakasz, M1a, RT-P0-24 / LMS-M1-01:** Az M1.1-et érinti, az 1. csoport hatóköre.
- **12. szakasz, M1a, smiley-kártyák az M1.B-ben:** A 3. csoport hatóköre.

### Érintett fájlok

- `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`
- `02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md`
- `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`
- `02 Tervezet/LMS – activity manifest.md`
- `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`
- `02 Tervezet/Gyermekvédelem – release gate.md`
- `02 Tervezet/Emberi jóváhagyás szükséges.md`
- `02 Tervezet/Program terv.md`
- `02 Tervezet/LMS – H5P runtime acceptance.md`



# BIZT-G3

BIZTONSÁG-JOG lencse, M1 3. fájlcsoport (M1.A, M1.B, M1.F; a hub csak kontextusként). Read-only review: semmit nem szerkesztettem. 9 findingot találtam (3×P1, 6×P2), mindegyik POST-PILOT. Mindegyiket a mai fájlállapot és a kánoni forrás adott szakasza alapján ellenőriztem. Runtime-bizonyítékot nem vizsgáltam.

Fájlok:
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- Kánon: 02 Tervezet/Gyermekvédelem – release gate.md (§2, §4, §4.1, §4.3), 02 Tervezet/Adatvédelem – tanulói adatok és AI.md (§2, §3, §6), 02 Tervezet/Emberi jóváhagyás szükséges.md (HUM-SAFE-01–03, HUM-PRIV-01/02, 11. szakasz)

---

**BIZT-G3-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:**
  - M1.B:476 és M1.B:507 (hurokzárás és checklist)
  - M1.F:270 és M1.F:276
  - kapcsolódik: M1.B:157, M1.B:382 („valós kör”)
- **Probléma:** Az M1.B és az M1.F arra biztat, hogy a peulán született SBI-mondatot, illetve egy „terepen tényleg használt” mondatot a tanuló adja be az M1.4 kapu-Assignmentbe. Ez ütközik egy lezárt projektgazdai döntéssel: az esetalapú kapuproduktumba csak kitalált, életszerű eset kerülhet, valós eset névtelenítve sem. Ugyanez a szabály áll az M1.4:457-ben és az M1.3:886-ban.
- **Bizonyíték:**
  - M1.B:476: „Ha most a peula alatt olyan SBI-mondatod született, ami **jobb a beadottnál**, kérd meg a képződet, hogy nyisson neked **új próbálkozást** az `M1.4` Assignmentben”
  - M1.F:270: „az M1.4 Assignmentben megír még **egy extra SBI-mondatot**, amit majd a peulán / terepen tényleg használni fog”
  - Kánon, Gyermekvédelem – release gate.md:23: „Esetalapú kapuproduktumba (elsősorban az M3 helyzetleírásába) **csak kitalált, életszerű eset** kerülhet; valós eset névtelenítve sem”
  - M1.4:457: „Valós helyzetet – név nélkül sem – ne írj le”
- **Hatás:**
  - Az M1.B szerint valós helyzet is hozható (:157), a „valós kör” pedig (:382) eleve egy jelen lévő, akár kiskorú társ valódi viselkedéséről szól.
  - Az ilyen mondat azonosítható harmadik személyről (társról vagy hanihról) szóló adatként kerülhet a Moodle-be. Ott az Assignment megőrzési ideje a képzés vége + 12 hónap, és a mentor/értékelő is látja.
  - Enyhítő körülmény: a beadás helyén, az Assignment leírásában a tiltás látható (M1.4:457).
- **Javaslat:**
  - Az M1.B:476, :507 és az M1.F:270 mondatához vezesd át szó szerint a kánoni korlátot (Gyermekvédelem §2, PROJEKT-DÖNTÉS 2026-10-02). Minta: M1.3:886 „(oda már csak kitalált, életszerű helyzet kerülhet)”.
  - Tilos hozzányúlni: a próbálkozás-logikához, a „legjobb megerősített eredmény” szabályhoz és a valós kör passz-lehetőségéhez.
- **Típus:** objektív
- **Osztály:** a lezárt szabály PROJEKT-DÖNTÉS; az ütközés TÉNY.
- **Pilot-besorolás:** POST-PILOT. P1, nem P0, mert a beadás helyén (M1.4:457) a tanuló látja a tiltást. Ha a döntéshozó P0-nak minősíti, freeze-kivétel lehet.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:**
  - M1.A:162, M1.A:503–505
  - M1.B:158, M1.B:389–391
  - M1.F:107
- **Probléma:** A képzői in-the-moment utasítások számolnak azzal, hogy valakit „erősen megérint a téma”, illetve „nagyon nehéz sztori jön fel”. Mégis hiányzik belőlük a kánoni safeguarding-minimum két eleme: felkavart kiskorút nem küldünk ki egyedül, és saját érintettségnél nincs nyilvános feldolgozás, hanem biztonságos támogatási útra terelés.
- **Bizonyíték:**
  - M1.A:503–504: „Ha nagyon nehéz sztori jön fel: „Köszi, hogy ezt behoztad. Ha szeretnéd, erről a peula után szívesen beszélgetek veled külön is.””
  - Kánon, Gyermekvédelem §4:63–64: „a facilitátor nem folytat nyilvános feldolgozást, hanem biztonságos támogatási útra terel” és „felkavart kiskorút **nem küldünk ki egyedül**”
- **Hatás:**
  - A kiscsoportos részben a képző csak körbejár (M1.A:502). Kiskorú résztvevőnél előfordulhat, hogy a felkavart tanulót „menj, szedd össze magad” alapon egyedül küldik ki.
  - Az is előfordulhat, hogy a kiscsoport tovább beszéli a hallott történetet.
  - A Memuna-út megvan (M1.A:505, a prep-sorok), a fenti két elem viszont hiányzik.
- **Javaslat:**
  - Vezesd át szó szerint a Gyermekvédelem §4 két mondatát (HUM-SAFE-03, PROJEKT-DÖNTÉS 2026-10-02) az M1.A 2.3/4.4.1, az M1.B 2.3/„Biztonsági tipp” és az M1.F 2.3 képzői utasításához.
  - Új szabályt ne fogalmazz. A meglévő Memuna- és safer-working mondatokhoz ne nyúlj.
- **Típus:** objektív
- **Osztály:** a §4 szövege PROJEKT-DÖNTÉS; a hiány TÉNY.
- **Pilot-besorolás:** POST-PILOT. Nem P0: az eszkaláció (Memuna) megvan, és a HUM-SAFE-05 szerint a képzőt a standard v1.0 köti és képzi. A freeze-kivétel feltétele nem teljesül.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-3**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** M1.A:440–442 (4.3.2); vö. M1.A:276–282 (4.2.3)
- **Probléma:** A résztvevők önkéntesen, „láthatóvá tételre” teszik fel az önfeltáró cetliket („szeretem magamban”, „nehéz nekem magamban”). A 4.3.2-ben a képző ezek közül felolvas néhányat, a csoport pedig értékeli, hogy címke-e. Erről a másodlagos felhasználásról a kiragasztáskor nincs előzetes tájékoztatás, és kimaradási lehetőség sincs.
- **Bizonyíték:**
  - M1.A:440: „A képző **leemel néhány cetlit** (olyanokat, amik elég könnyedek, nem túl azonosíthatóak). Nevet **nem olvas fel**.”
  - M1.A:282: „csak olyan tartalom kerüljön, amit szívesen teszel láthatóvá a teljes csoportnak”
- **Hatás:**
  - 8–20 fős kvucában a kézírásból és abból, hogy ki hova ragasztott, a szerző felismerhető.
  - A saját nehézségről szóló mondat csoportos „címkézés-elemzése” megszégyenítő lehet.
  - A kánoni passzjog (Gyermekvédelem §4:61) itt nem érvényesíthető, mert a résztvevő nem tudja előre, mi lesz a cetlijével.
- **Javaslat:** EMBERI DÖNTÉS (pedagógiai felelős + a Memuna mint HUM-SAFE-03 vétó/QA): a 4.3.2 valódi cetlik helyett a képzői segédlet kész példa-cetlijeivel dolgozzon (M1.A-MUNK-02 spec), vagy a 4.2.3-ban előre jelezze a felolvasást, és adjon kimaradási lehetőséget. A 4.2.3 önkéntességi mondatai nem gyengíthetők.
- **Típus:** emberi-döntés
- **Osztály:** a másodlagos felhasználás TÉNY; a megoldás választása EMBERI JÓVÁHAGYÁS KELL.
- **Pilot-besorolás:** POST-PILOT. Nem P0: a kiragasztás önkéntes, és a képző a „könnyed, nem azonosítható” cetliket választja.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-4**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** M1.A:484–498 (4.4.1); vö. M1.A:199
- **Probléma:** A kiscsoportos reflexió saját, korábban kapott sértő visszajelzésekről kérdez („Hogyan hatott rád?”). Indoklás nélküli passzt nem ajánl fel, csak azt, hogy a résztvevő könnyebb sztorit választhat. A passz egyedül a ráhangolónál hangzik el, ott is csak a „most” idejére.
- **Bizonyíték:**
  - M1.A:485–486: „Nem kötelező nagyon nehéz vagy személyes sztorit hozni – beszélj olyanról, ami komfortos számodra.”
  - Kánon, Gyermekvédelem §4:61: „bárki **indoklás nélkül passzolhat**, szünetet vagy egyenértékű alternatívát kérhet”
- **Hatás:** Akinek csak fájdalmas élménye van a témáról, annak beszélnie vagy kitalálnia kell valamit. Ez személyesen érintő gyakorlat, kiskorú résztvevőkkel.
- **Javaslat:** A 4.4.1 instrukciójába vezesd át a kánoni passzjogot (HUM-SAFE-03; §4:61 szó szerint vagy a §4.3 „Mondhatsz passzt” fordulatával). Az instrukció többi részéhez és a 9 perces kerethez ne nyúlj.
- **Típus:** objektív
- **Osztály:** a passzjog PROJEKT-DÖNTÉS; a hiány TÉNY.
- **Pilot-besorolás:** POST-PILOT. Van könnyített alternatíva, a biztonsági mondat a peulán többször elhangzik (M1.A:161, :227), ezért nem P0.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:**
  - M1.A:372
  - M1.B:157, M1.B:345–346
  - vö. M1.3:886, M1.4:457
- **Probléma:** A peulák valós helyzetekre és a saját kvucára szabott példákra hívnak, de a valós szereplők (társak, hanihok) azonosíthatóságára nem adnak korlátot. Az online lánc ugyanerre a „név és felismerhető részlet nélkül” korlátot adja.
- **Bizonyíték:**
  - M1.A:372: „Írj mellé 1–2 újat is, lehetőleg a saját kvucádra szabva, és azokat is olvasd fel.”
  - M1.B:157: „elég, ha egy tipikus, kisebb helyzetet választotok, vagy egy fiktív példát”
  - M1.3:886 (online): „Lehet valós, hétköznapi helyzet (pl. múlt heti peula, de név és felismerhető részlet nélkül)”
- **Hatás:**
  - A mozgásos játékban egy felismerhető valós esetre épülő címke-mondat („Nem tiszteled a kvucát”) egy jelen lévő résztvevő nyilvános megbélyegzésévé válhat.
  - A triókban hanihokról szóló valós, felismerhető részletek hangozhatnak el.
- **Javaslat:** EMBERI DÖNTÉS (programvezető, adatvédelmi kérdésben a DPO): kiterjeszthető-e az M1.3:886 „név és felismerhető részlet nélkül” korlátja az M1.A 4.3.1 kvucára szabott példamondataira és az M1.B valós helyzeteire. Ez új alkalmazási eset, ezért nem objektív. A passz- és cserelehetőségekhez (M1.B:346) ne nyúlj.
- **Típus:** emberi-döntés
- **Osztály:** a hiány TÉNY; a kiterjesztés EMBERI JÓVÁHAGYÁS KELL.
- **Pilot-besorolás:** POST-PILOT. Szóbeli, nem rögzített tartalomról van szó, nem P0.
- **Hipotézis:** M1-04 / N-M1-05 (részben: a P3 pedagógiai részét ez a lencse nem értékeli)
- **Verdikt:** —

---

**BIZT-G3-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** M1.B:385; vö. M1.A:273–274, M1.A:301
- **Probléma:**
  - Az M1.A tanulói szövegben megígéri, hogy a vakfolt valódi feltárása egy „későbbi, bizalmibb fázisban” jön.
  - Az M1.B a következő peulán már erre köti vissza a valós kört.
  - A két peula biztonsági keretezése ellentmond egymásnak.
- **Bizonyíték:**
  - M1.A:273–274: „Ezt a részt most nem nyitjuk meg élesben … a vakfolt valódi feltárása egy későbbi, bizalmibb fázis lesz a kvuca életében.”
  - M1.B:385: „Ez az a mozzanat, ahol a résztvevők a saját **vakfoltjukról** is kaphatnak egy apró visszajelzést – ide kötheted vissza az M1.A-ban üresen hagyott **Vakfolt-mezőt**.”
- **Hatás:** A résztvevőnek tett ígéret hamar sérül, ami a biztonságos térbe vetett bizalmat gyengíti. Enyhítő körülmény: a valós kör csak pozitív visszajelzést enged, passzal (M1.B:382).
- **Javaslat:** EMBERI DÖNTÉS (pedagógiai felelős): melyik keretezés érvényes, vagyis mikor nyílik meg a vakfolt. A javítás csak a két mondatot igazíthatja össze. A valós kör passz- és „csak pozitív” korlátja nem gyengíthető.
- **Típus:** emberi-döntés
- **Osztály:** az ellentmondás TÉNY; a választás EMBERI JÓVÁHAGYÁS KELL.
- **Pilot-besorolás:** POST-PILOT. Opcionális, csak pozitív, passzolható kör, nem P0.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:**
  - M1.F:310–313 (4.3, Opció 2)
  - vö. M1.F:36, M1.F:282
  - hub:216 és M1.F:57
- **Probléma:** Az F-peula saját adatvédelmi elve szerint senkit nem teszünk ki névvel. A 4.3 Opció 2 mégis nyilvános jelentkezéssel kéri, hogy a résztvevők megmutassák, kinek mi nem állt össze. A cél-mondat (M1.F:57, hub:216: „A képző lássa, kinek mi homályos”) szintén személyre szóló azonosítást feltételez, miközben a tanulónak az hangzik el, hogy „Nem azt fogom nézni, ki mit írt” (:282).
- **Bizonyíték:**
  - M1.F:313: „Ki az, aki inkább a Joharinál akadt el? Kinek a ‘megfigyelés vs. címke’ nem állt teljesen össze?”
  - M1.F:36: „Nem tesszük ki névvel, hogy ki hol tart, mit kell még pótolnia vagy javítania.”
- **Hatás:** A kötelező, bukott kapu utáni F-peulán a nyilvános jelentkezés megmutatja, kinek mit kell pótolnia. Ez ellentmond a fájl saját privát-állapotfelmérés elvének (vö. E-M1-071).
- **Javaslat:** Az Opció 2 kérdését és az M1.F:57 / hub:216 „kinek” fordulatát igazítsd az M1.F:36 elvéhez. Hogy az Opció 2 törlődik vagy tematikus, személyhez nem kötött kérdéssé válik, szerkesztői döntés. Az M1.F:36 elvéhez és az Opció 1 név nélküliségéhez nem lehet nyúlni.
- **Típus:** objektív
- **Osztály:** a belső ellentmondás TÉNY.
- **Pilot-besorolás:** POST-PILOT. Enyhe, nem rögzített adat, nem P0.
- **Hipotézis:** E-M1-071 (megerősítve, hogy a nyilvános „hőmérő” megszűnt, de az Opció 2 maradék-ellentmondás)
- **Verdikt:** —

---

**BIZT-G3-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** M1.A:259–305 (4.2.3–4.2.4), M1.A:436–440; vö. HUM-fájl:149
- **Probléma:** A közös Johari-táblára kézírásos, önfeltáró cetlik kerülnek („nehéz nekem magamban”). A fájl nem mondja meg, mi lesz velük a peula után (visszakapja-e a szerző, megsemmisül, megőrzik-e), és a tábla fotózásáról sem szól. A HUM-PRIV-02 implementációs sora az M1.A-t a központi felvételi/kézírás-szabályra hivatkozó activityk között sorolja fel, a fájlban azonban nincs ilyen hivatkozás.
- **Bizonyíték:**
  - HUM:149: „**Implementáció:** központi média-/felvételi szabály, amelyre minden médiaaktivitás hivatkozik (pl. M0.A, M1.A, …)”
  - Adatvédelem §6:163 (HUM-PRIV-02): „A kézírásos plakátot lehetőleg **fizikailag** őrizzük meg. Ha fotó kell: előbb a nevek és azonosítók eltávolítása”
- **Hatás:**
  - A kézírással azonosítható önfeltárás ellenőrizetlenül a teremben maradhat, vagy egy résztvevő telefonján végezheti.
  - A „fizikai megőrzés” alapszabály önfeltáró cetlire alkalmazva nem egyértelmű.
- **Javaslat:** EMBERI DÖNTÉS (DPO/jogi felelős, HUM-PRIV-02 vétó/QA): az M1.A Johari-cetlijeire a „kézírásos plakát” sor, a „név nélküli papír munkalap” sor (30 napon belüli megsemmisítés) vagy a szerzőnek való visszaadás vonatkozik-e. A döntés után a hivatkozás átvezetése objektív. A cetli-önkéntesség mondataihoz ne nyúlj.
- **Típus:** emberi-döntés
- **Osztály:** a hiányzó hivatkozás TÉNY; a HUM-PRIV-02 PROJEKT-DÖNTÉS; az önfeltáró cetlire való alkalmazása EMBERI JÓVÁHAGYÁS KELL.
- **Pilot-besorolás:** POST-PILOT. Nem rögzített, név nélküli papír, nem P0.
- **Hipotézis:** új
- **Verdikt:** —

---

**BIZT-G3-9**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** biztonság-jog
- **Hely:** M1.B:463–472 (4.4.2 vállalás); M1.F:270 („terepen tényleg használni fog”); vö. M1.4:508
- **Probléma:** A terepre vitt SBI-vállalás bármilyen zavaró helyzetre szól. Egy 15–17 éves madrihnak semmi nem jelzi, hogy valódi gyermekvédelmi aggálynál nem SBI-visszajelzés vagy szembesítés a teendő, hanem a Memuna bevonása. Az online leckében (M1.4:508) ez a határ megvan, a peulák terepi hídjában nincs.
- **Bizonyíték:**
  - M1.B:472: „‘Ha valami zavar, nemcsak magamban puffogok, hanem megpróbálom elmondani S–B–I szerint.’”
  - Kánon, Gyermekvédelem §4:58: „a madrih nem konfrontál feltételezett elkövetőt”
- **Hatás:** A kiskorú madrih egy határátlépést vagy bántást SBI-ben „megbeszélhet” a feltételezett elkövetővel. Ez ellentmond a jelzési út 3. lépésének (§4.1).
- **Javaslat:** EMBERI DÖNTÉS (a Memuna, HUM-SAFE-01/03 vétó/QA): kell-e az M1.B 4.4.2-be és az M1.F 4.2-be a §4.1 által megengedett utalás („azonnal vond be a Memunát”), illetve az M1.4:508 határmondatának átvétele. Új szabály nem írható. A vállalás-példák önkéntességéhez ne nyúlj.
- **Típus:** emberi-döntés
- **Osztály:** a kánoni tilalom PROJEKT-DÖNTÉS; a peulába való átvétel szükségessége EMBERI JÓVÁHAGYÁS KELL.
- **Pilot-besorolás:** POST-PILOT. Az online M1.4:508 ugyanennek a tanulónak kimondja a határt, nem P0.
- **Hipotézis:** új
- **Verdikt:** —

---

**Elvetett hipotézisek**

- **N-M1-04 / X-06 / M1-02:** A 3. csoport egyik peulája sem kéri, hogy a tanuló elhozza, megossza vagy megmutassa az M1.1 SLIDE 5 online reflexióját. Az M1.A 4.2.1 rokon kérdései papíron és a tanulónál maradnak. Az M1.F:270 („ha a korábbi munkája nem jelenik meg”) nem kér tartalmat, és központi tárolást sem feltételez. Ebben a csoportban nincs ütközés a 2026-10-10-i döntéssel; az átvezetés hiánya az 1. csoport scope-ja.
- **E-M1-069 (biztonsági szempontból):** A sarok- és mozgásos gyakorlatok (M1.A 4.3.1, M1.B 4.1.2) tudásalapú besorolást kérnek, nem érzékeny önpozicionálást. Az M1.B 4.1.1 hangulatjelzésében van semleges opció (😐 „oké / semleges”, M1.B:142). A „MAG”- és az „A/B sarok”-széttartás implementációs lencse.
- **M1a:** A fejenkénti smiley-kártya hiánya (M1.B:192/:203 ↔ :140) logisztikai/implementációs kérdés, biztonsági-jogi kockázatot nem hordoz.
- **M1b:** Médiametaadat-széttartás (M1.B:86), nem biztonsági-jogi kérdés.
- **E-M1-063 / E-M1-064 / E-M1-067:** Az M1.A 4.2.2 titoktartás-határ és Memuna-mondata összhangban van a §4.1 megengedett utalásával. A 4.2.3 önkéntessége megvan, a 4.4.1 átcsoportosítása pedig védő hatású. Új hiba nincs bennük, az önálló problémákat a BIZT-G3-3 és a BIZT-G3-4 rögzíti.


# ERT-G1

**Fájlrövidítések:**
- HUB = `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md`
- M1.1 = `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md`
- M1.2 = `02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md`
- M1.3 / M1.4: ugyanebben az `Online leckék/` mappában (csak célzott Greppel néztem bele)
- KAPU = `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`
- MAN = `02 Tervezet/LMS – activity manifest.md`
- RA = `02 Tervezet/LMS – H5P runtime acceptance.md`
- HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`
- RR = `02 Tervezet/RELEASE-READINESS.md`

---

**ERT-G1-1**
- **Súlyosság:** P0
- **Bizalom:** magas
- **Lencse:** értékelés (érinti a biztonság-jog lencsét is)
- **Hely:** M1.1:794, M1.1:98, M1.1:792, M1.1:699 (@asset M1.1-IKO-02 notes); MAN:45 (LMS-M1-01); MAN:308 (BSPEC-02 leltár); RA:41 (6. pont) és RA:104 (24. pont felsorolása); HUM 10. szakasz :522–527
- **Probléma:** Az N-M1-04 projektgazdai döntés (2026-10-10, a fő munkamenet közvetítésével) nincs átvezetve. A kánon tárolási oldala ellentmond neki: a forrás „lehetőleg” tanuló-lokális tárolást ír, mentori láthatóságot enged, és tartalékútként Moodle-oldali (központi) mezőt ír elő. A completion-oldal rendben van: M1.1:80 és :793, valamint MAN:45 egybehangzóan „nem feltétel”.
- **Bizonyíték:** M1.1:794: „ez saját önreflexió, ezért lehetőleg csak a tanuló látja (learner-local); a kijelölt mentor csak akkor láthatja, ha erre ténylegesen szükség van” · M1.1:98: „ha a teszt nem igazolja, a mező Moodle-oldalra kerül.”
  - MAN:308 opcionális tanuló-lokális listája („M0.3 SLIDE 7, M2.3 mini-reflexiók, M3.3 SLIDE 6, M5.1 SLIDE 6, M6.3 SLIDE 7, M6.4 mini-reflexiók”) nem tartalmazza az M1.1 SLIDE 5-öt.
  - Az RA:104 listájából hiányzik az LMS-M1-01.
- **Hatás:**
  - Aki az M1.1:98 tartalékútját követi, Moodle-oldali mezőt épít, manifest-sor nélkül (ezt a MAN:35 is tiltja).
  - Aki a :792 Essay/Free Text útját követi, H5P-próbálkozásban tárolja a szöveget.
  - Mindkét esetben a pilot (részben kiskorú) tanulóinak személyes önreflexiója központilag tárolódik, és a mentor láthatja, ellentétben a lezárt döntéssel.
- **Javaslat:**
  - (1) A döntést szó szerint („kizárólag tanuló-lokális, központi tárolás nélkül; nem completion-feltétel”) rögzítsd a HUM új datált döntés-szakaszában, a bizonyítékot pedig a `04 Audit` döntési jegyzőkönyvében. Forrás: projektgazda, 2026-10-10. Utólagos ellenőrzőt nem feltételezünk: a mátrix DPO-QA-t említ, de ezt a döntési csomagból kell venni.
  - (2) Vezesd át a döntést:
    - M1.1:794: a „lehetőleg” helyett „kizárólag”, a mentori láthatósági mellékmondat kikerül (a HUM-PRIV-01-hivatkozás maradhat, a döntés szigorúbb).
    - M1.1:98 és :792: a SLIDE 5-re nem vonatkozhat Moodle-oldali mező vagy tárolt H5P-elem; csak saját jegyzet, vagy az RA 24. pont szerint igazoltan rögzítésmentes elem.
    - M1.1:699: csak a media-manifest folyamatán át.
    - MAN:45: „lehetőleg” → „kizárólag”.
    - MAN:308: kerüljön az „opcionális, tanuló-lokális” listába.
    - RA:104: az LMS-M1-01 kerüljön a listába.
  - Ne nyúlj hozzá: az opcionalitás és a „nem completion-feltétel” marad. „Nem tároljuk” típusú tanulói mondat csak a sikeres RT-P0-24 után kerülhet be (RA:104 utolsó mondata).
- **Típus:** objektív
- **Pilot-besorolás:** PILOT-BLOCKER – tényleges adatvédelmi P0, mert a kánon központi tárolásra utasítja a pilot-hatókörbe tartozó M1.1 buildjét; teljesíti a freeze-kivételt.
- **Hipotézis:** N-M1-04; M1-02; X-06; M1a (3. pont)
- **Verdikt:** —

**ERT-G1-2**
- **Súlyosság:** P0
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** RA:152 (RT-P0-24), RA:143 (RT-P0-15), RA:142 (RT-P0-14), RA:141 (RT-P0-13), RA:137 (RT-P0-09); RR:25 (G2), RR:27 (G3b); érintett sorok: MAN:45–46
- **Probléma:** Az M1.1–M1.2 completion- és tárolási viselkedésére nincs runtime-bizonyíték:
  - SLIDE 5: nem tárolt, és a completion nem függ tőle;
  - a SLIDE 1–2 pontozatlan önbevallós választói nem jelölnek hibásnak őszinte választ (M1.1:204);
  - a CP-összefoglalóval beáll a completion;
  - az M1.2 húzásmentes útja azonos visszajelzést és completiont ad.
- **Bizonyíték:** RA:152: „| RT-P0-24 | `IMPLEMENTATION_TEST_REQUIRED` | 24. Tanuló-lokális szöveges lépések |” · RR:25: „láthatósági és szerepkör-tesztek: POST-BUILD; a DPO release-ellenőrzése: FINAL_RELEASE_QA”
- **Hatás:** Az M0+M1 pilot GO/NO-GO döntése (HUM:548, PILOT-1) nem támaszkodhat arra, hogy az M1.1 SLIDE 5-be írt szöveg nem kerül a próbálkozás-riportba vagy a mentett állapotba (`enablesavestate`).
- **Javaslat:** Megvalósítási döntés: a projektgazda jóváhagyta; a formális szerepköri és runtime-bizonyíték függő. A teendők:
  - RT-P0-24 az LMS-M1-01-re: tanulói fiókkal beírt szöveg után képzői fiókkal visszaolvasni, hogy nincs tárolt szöveg és mentett állapot sem;
  - RT-P0-09: üres SLIDE 5 mellett is beáll a completion;
  - RT-P0-14, 3. alpont: SLIDE 1–2;
  - RT-P0-13: M1.2;
  - mindez a G2/G3b bizonyítékként, az M0+M1 evidence listán. Nem írod be és nem feltételezed.
- **Típus:** bizonyíték-kapu
- **Pilot-besorolás:** PILOT-BLOCKER – a PILOT-1 szerinti M0+M1 evidence list része, az ERT-G1-1 adatvédelmi P0-jához tartozik; tartalmi szerkesztést nem igényel, ezért a freeze-t nem sérti.
- **Hipotézis:** N-M1-04; M1a (3. pont)
- **Verdikt:** —

**ERT-G1-3**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** HUB:36, HUB:86; M1.1 SLIDE 6 (M1.1:798–913)
- **Probléma:** A 4. kimeneti kompetencia ígért „záróreflexiós” produktumának egyik M1-fájlban sincs megfelelője: a „segített már” kifejezés csak a hubban fordul elő. A hub az M1.1 Check-jét ennek a nyitott kérdésnek írja le, a lecke Check-je viszont 3 zárt kvízkérdés.
- **Bizonyíték:** HUB:36: „Megfogalmaz a záróreflexióban 1 mondatot arról, milyen visszajelzés segített már neki” · HUB:86: „Check: 1 nyitott kérdés arról, milyen visszajelzés segített már neki.”
- **Hatás:**
  - A kimondott cél tanulási tevékenység nélkül marad.
  - Aki a hub alapján épít, új szabad szöveges mezőt tehet az M1.1-be, az N-M1-04 és a HUM-PRIV-01 keretén kívül.
- **Javaslat:**
  - Objektív lépés: a HUB:86-ot igazítsd az M1.1 SLIDE 6 tényleges 3 kérdéses kvízéhez.
  - EMBERI DÖNTÉS (projektgazda + értékelési felelős): hol valósuljon meg a 4. kompetencia reflexiója. Ha online szabad szöveg lesz, az az N-M1-04 mintájára tanuló-lokális és nem completion-feltétel; ez a döntés új alkalmazási esete, tehát jóváhagyás kell.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT – nem P0, a freeze-kivétel nem áll fenn.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-4**
- **Súlyosság:** P1
- **Bizalom:** magas (az ellentmondásban), közepes (a javítás irányában)
- **Lencse:** értékelés
- **Hely:** HUB:33, :39, :125; KAPU:21, :197 ↔ M1.4:10, :380, :426, :434, :450; M1.3:45
- **Probléma:** A kapuprodukátum hosszelőírása ellentmondásos. A hub és a hivatalos kapudefiníció 2–3 mondatos SBI-t ír elő, a tanulói feladatleírás (M1.4) 1–2 mondatosat.
- **Bizonyíték:** KAPU:21: „…címkézésmentes, tisztelettudó, 2–3 mondatos SBI-visszajelzést írni.” · M1.4:10: „A lecke végére tudsz 1–2 mondatos, konkrét SBI-visszajelzést írni”
- **Hatás:** A rubrika nem pontoz hosszt, de a kapu „Mit mér” sora igen. Két értékelő eltérően kezelheti az 1 mondatos beadványt, és a tanuló mást olvas, mint amit a kapu állít.
- **Javaslat:**
  - A hub (HUB:239, :299) a KAPU-fájlt jelöli hivatalos kapudefiníciónak, ezért az M1.4 tanulói szövegét kell a KAPU:21 „2–3 mondatos” előírásához igazítani. Rubrika, küszöb és answer key változatlan.
  - Ha a projektgazda az 1–2 mondatot akarja, az a KAPU és a hub módosítása lenne (nem e finding hatóköre).
  - Javítási hely: M1.4 (2. csoport) – a 2. csoport findingjával deduplikálandó.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – nem blokkol, a rubrika szerinti értékelés ettől működik.
- **Hipotézis:** M1a (1. pont)
- **Verdikt:** —

**ERT-G1-5**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.2:626, M1.2:629, M1.2:651
- **Probléma:** A Mark the Words 4. mondatában a nem jelölendő rész („nem bírsz nyugton maradni 5 percig sem”) képességre vonatkozó általánosítás, nem kamerával rögzíthető esemény. Aki a lecke saját kameratesztje szerint megjelöli, azt a visszajelzés „tény megjelölésének” minősíti.
- **Bizonyíték:** M1.2:626: „4. „**Éretlen** vagy, nem bírsz nyugton maradni 5 percig sem.”” · M1.2:651: „Maradt jelöletlen címke, vagy tényt is megjelöltél.”
  - Ellentétben a lecke saját szabályával, M1.2:362: „Megfigyelés az, amit egy kamera is felvenne.”
- **Hatás:** Az item pont azt bünteti, amit a modul tanít (általánosítás ≠ megfigyelés; vö. M1.2:203, KAPU B-sor „Erős”), és torzítja a hub §7 H5P-statisztikáját.
- **Javaslat:**
  - A célszó („Éretlen”) és a kulcs változatlan. Csak a második tagmondatot írd át kamerával rögzíthető cselekvésre (pl. „…a beszélgetőkör alatt háromszor felálltál”).
  - A :629 magyarázatát igazítsd hozzá.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – formatív, küszöb nélküli item, nem freeze-kivétel.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-6**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.2:192 (≙ :158), :385, :871; M1.1:885–887; M1.2:885; M1.2:911–913
- **Probléma:** A disztraktorok felszíni vagy nyelvi kulccsal elárulják a választ.
  - Az M1.2 mindhárom Single Choice itemjében a ✅ az egyetlen opció, amelyben szám („háromszor”) áll. A SLIDE 1-es ✅ szó szerint a hook buborékja.
  - Az M1.1 Q2 és az M1.2 Q3 téves opciói, valamint az M1.2 Q2 igaz/hamis állítása abszolút vagy extrém szavakkal kitöltő zajjá válnak („pontosan ugyanúgy”, „mindig”, „biztosan… rögtön”, „sokkal… sokkal”, „Semmi gond”, „mindig… tilos”).
- **Bizonyíték:** M1.2:911–912: „A másik biztosan egyetért veled, így rögtön meg is változik majd / Egy rövid címkével sokkal objektívebb és sokkal hitelesebb leszel a többiek előtt”
- **Hatás:** Az itemek a „szám = megfigyelés” és az „abszolút = hamis” heurisztikát jutalmazzák, nem a megfigyelés–címke megkülönböztetést. A hub 2. kompetenciájának formatív mérése így nem informatív.
- **Javaslat:**
  - Csak a disztraktorok szövege változik; a ✅ és helye marad.
  - Az M1.2 SC-itemekben legalább egy disztraktor tartalmazzon számot, de maradjon címke (pl. „Háromszor is tiszteletlen voltál”).
  - Az M1.1 Q2 és az M1.2 Q3 extrém kitöltői helyett valós madrih-tévképzetek kellenek (a KAPU:132 elve szerint).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – formatív item, nem freeze-kivétel.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-7**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.1:893–895 (Q2 helytelen-visszajelzés); M1.2:775–784 a :754–759 kártyákhoz
- **Probléma:** Ahol a spec tanító visszajelzést ígér vagy a tévképzet a modul célja, ott a visszajelzés hiányzik vagy általános.
  - Az M1.1 Q2 egyetlen helytelen-visszajelzése nem kezeli a két célzott tévképzetet: „a visszajelzés objektív igazság”, illetve „visszajelzés = rosszul csináltam”.
  - Az M1.2 D&D „minden kártyához” ígért magyarázatából 6-ból csak 3 van megírva (az 1., 3. és 4. kártyához).
- **Bizonyíték:** M1.1:895: „Nem egészen. A visszajelzés abban segíthet, hogy olyan dolgokat is észrevegyél magadon, amiket eddig nem láttál – vagyis jobban lásd a vakfoltjaidat.” · M1.2:775: „H5P-visszajelzés – minden kártyához 1 mondatos magyarázat”
- **Hatás:**
  - Pont a 4. kompetencia tévképzetét választó tanuló nem kap magyarázatot.
  - A D&D-nél az építő három visszajelzést maga találna ki, és a húzásmentes út „azonos visszajelzése” (M1.2:797) definiálatlan.
- **Javaslat:**
  - M1.1 Q2: opciónkénti visszajelzés (Multiple Choice „Single Choice” mód, mint M1.2:183) a lecke meglévő tartalmából (HUB:36, M1.1:911–912).
  - M1.2: a 2., 5. és 6. kártya magyarázata a :780–784 mintájára.
  - A típusbeli megvalósíthatóságot az RT-P0-13 és RT-P0-14 igazolja.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – nem P0.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-8**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** HUB:30, HUB:93, HUB:102; M1.2:619–627, :750, :864–913
- **Probléma:** A hub mást ír az M1.2 méréséről, mint ami a leckében van:
  - a „4/5 mondat helyes besorolása” célértékhez nincs 5 tételes besoroló feladat (a D&D 6 kártyás, a Mark the Words szószintű);
  - a hub szerint a 3 záró kérdés „besorolás”, de csak a Q1 az; a Q2 és a Q3 fogalmi kérdés.
- **Bizonyíték:** HUB:93: „Besorolni 4/5 mondatot helyesen” · HUB:102: „Check: 3 rövid záró kérdés a megfigyelés–címke különbségre (besorolás, nem átírás).”
- **Hatás:** A formatív célérték nem olvasható le egyetlen H5P-eredményből sem, a stáb nem tudja értelmezni.
- **Javaslat:**
  - HUB:102: igazítsd az M1.2 SLIDE 6-hoz (1 besorolás + 2 fogalmi kérdés).
  - A 4/5 számot ne írd át. Hogy melyik M1.2-feladat méri: EMBERI DÖNTÉS (értékelési felelős).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – csak hub-leírás, nem blokkol.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.1:55; HUB:77; M1.1:859; M1.1:768
- **Probléma:** Az M1.1 mikrocélja két dolgot ígér, de egyikhez sincs kötelező online lépés:
  - a 4 mező megnevezése: az egyetlen ellenőrző item csak a vakfoltot kérdezi;
  - a vakfolt saját példával való illusztrálása: ez csak az opcionális SLIDE 5-ben van, amely az N-M1-04 szerint nem lehet kötelező.
- **Bizonyíték:** M1.1:55: „meg tudod nevezni a Johari-ablak 4 mezőjét … és saját példával illusztrálni a vakfoltot” · M1.1:859: „Mi a „vakfolt” a Johari-ablakban?”
- **Hatás:** A tanuló és a stáb olyan online eredményt vár, amelyet a lecke nem mér. A hub 1. kompetenciája formatív, és az M1.A részben fedi.
- **Javaslat:** A mikrocél és a HUB:77 jelölje, hogy online a mezők felismerése történik, a saját példa pedig opcionális vagy az M1.A-n zajlik. A SLIDE 5 nem válhat kötelezővé (N-M1-04).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – formatív cél, nem freeze-kivétel.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G1-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.1:344; M1.1:204; MAN:16
- **Probléma:** A SLIDE 2 pontozatlan emoji-skáláját a forrás „Completion”-elemnek nevezi. Ez ellentmond a dia saját elsődleges megvalósításának (szöveg + Tovább) és a H5P-C profil szabályának.
- **Bizonyíték:** M1.1:344: „(Completion, nincs jó/rossz. Megvalósítás: mint az 1. dia önbevallós kérdésénél – pontozott választós típusba nem kerülhet.)” · MAN:16: „A pontozatlan választók nem önálló completion-elemek”
- **Hatás:** Az építő a választást completion-feltételként kezelheti.
- **Javaslat:** A „Completion” jelzőt cseréld erre: „nem pontozott, nem completion-elem”. A megvalósítás az M1.1:204 szerint.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT – a CP completionje („Receive a grade”) technikailag nem kapuzza.
- **Hipotézis:** új
- **Verdikt:** —

LEVÁGVA: 1 további finding, súlyosságuk: 1×P2
- ERT-G1-11 · P2 · M1.1:655–667 · Az igaz/hamis állítás a vakfoltot „hasznos információnak” nevezi, de definíció szerint a visszajelzés az információ, a vakfolt az, amit nem látok. Fogalmilag pontos tanuló „Hamis”-t is válaszolhat.

---

**Elvetett hipotézisek**
- **N-M1-03 / M1-01:** a SLIDE 3–4 átfedése pedagógiai és terhelési kérdés (D2), nem értékelési hiba. Az ismétlődő igaz/hamis üzenetek (:485, :655, :902) visszakérdezésként értelmezhetők.
- **M1-03 (N-M1-06/-07/-09/-11):** a hub §6 négy rubrikasora és küszöbe (HUB:239–249) egyezik a KAPU:23-mal és a MAN:50-nel, hubszintű eltérés nincs. A Moodle-beállítás runtime-feladat (CC-06), és a 2. csoport hatóköre.
- **N-M1-01:** a HUB:249 ma „hivatalos küszöböt” ír, a „kanonikus” szó nem tanulói szövegben áll.
- **N-M1-02:** a HUB:253 „javítási útvonal” fordulata érthető, „bukás-útvonal” nincs.
- **N-M1-08:** a hub szintnevei („Még nem / Rendben / Erős”, HUB:249) egyeznek a KAPU:40–41-gyel.
- **M1a, 2. pont (M1.B smiley-kártyák):** a 3. csoport hatóköre, nem vizsgáltam.
- **N-M1-04 mint nyitott emberi döntés:** nem az. A közvetített projektgazdai döntés lezárta; a fennmaradó rész átvezetés (ERT-G1-1) és bizonyíték-kapu (ERT-G1-2).


# ERT-G2

Fájlrövidítések (abszolút utak):
- KAPU = 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- M1.3 = 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- M1.4 = 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- HUB = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- PT = 02 Tervezet/Program terv.md
- RA = 02 Tervezet/LMS – H5P runtime acceptance.md
- M2KAPU = 02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md

---

**ERT-G2-1**
- Súlyosság: P0 · Bizalom: közepes · Lencse: értékelés
- Hely: M1.4:473–476 (vö. M1.4:138, :456; KAPU §1 és §5)
- Probléma: A kapu-Assignment tanulói leírása kész, teljes SBI-mintát ad a három választható kapuszituáció egyikére (B – kinevetés). A rubrikában nincs olyan szempont, amely a minta szó szerinti visszaadását kiszűrné, így a kapu saját megfogalmazás nélkül is teljesíthető.
- Bizonyíték: M1.4:475–476 „Amikor ma a körben háromszor kinevetted a többieket, / a kicsik utána már nem szólaltak meg.” — M1.4:138 „A beszélgetőkörben az egyik hanih mindenkit kinevet, aki megszólal.”
- Hatás: Ha a tanuló a B helyzetet választja és bemásolja a mintát, a KAPU §1 szerint ez kb. 7–8/8 („Teljesítve”). A kapu a KAPU:21 szerint az SBI *írását* méri, ezt így nem igazolja. Az értékelőnek nincs szabálya az elutasításra.
- Javaslat: EMBERI DÖNTÉS (értékelési felelős; QA: modulgazda/módszertani lektor, HUM 8. szakasz „Az M1 rubrikahorgonyai”). Két kérdés: (a) a KAPU §5 kapjon-e értékelői szabályt arra az esetre, ha a beadás a lecke vagy a kvíz mintamondatát szó szerint vagy közel szó szerint adja vissza; (b) a M1.4:475–476 példa helyére a három kapuszituáción kívüli, már meglévő kánoni példa kerüljön-e (M1.4:290–292). A (b) önmagában nem elég, mert a „saját, kitalált helyzet” út (M1.4:457) bármely mintát átengedi. Javítási korlát: a küszöb (≥1 soronként ÉS ≥5/8), a rubrikaszintek, a próbálkozásszám és minden ✅ változatlan.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT. A hamis átengedés nem biztonsági, nem adatvédelmi, nem akadálymentességi és nem előrehaladást blokkoló hiba, ezért nem teljesíti a 2026-10-10-i freeze-kivételt. A pilot alatt repón kívüli értékelői utasítással mérsékelhető, de ezt az értékelési felelős dönti el.
- Hipotézis: új

**ERT-G2-2**
- Súlyosság: P1 · Bizalom: magas · Lencse: értékelés
- Hely: KAPU:64 és :86; KAPU:126; KAPU 4.1, :265–269
- Probléma: Ugyanazt az enyhe minősítő szót két sor is pontozza: a B-sor („becsúszik egy ítélkező szó”) és a hangnem-sor („enyhe minősítés”), majdnem azonos példával. Ez ellentmond a KAPU:126 „nincs kettős súlyozás” állításának. A ponthatáron álló kalibrációs minta ráadásul következetlenül alkalmazza a két sort.
- Bizonyíték: KAPU:265 „„sokat beszéltél bele” – … nincs szám/idő és kissé minősítő-általános.” (B = 1) — KAPU:267 „Hangnem | Erős | 2 | … nincs címke” (a 4. sor „Rendben” szintje: „enyhe minősítés”, :86)
- Hatás: Ha a 4.1 mintán a „kissé minősítő” tartalmat a 4. sorban is levonják, az eredmény 1/1/1/1 = 4, nincs „Erős” sor, tehát „Még nem teljesítve”. A mostani minta szerint viszont épp átmegy. Pont a vágási határon dönthet két értékelő eltérően (KAPU:36 kalibrációs célja sérül). A 2. sor szintjei ráadásul nem sorolják be az ítélkező szó nélküli, de számszerűsítetlen cselekvést.
- Javaslat: EMBERI DÖNTÉS (értékelési felelős + modulgazda/módszertani lektor). Eldöntendő: (1) melyik sor vonja le az enyhe minősítő szót, vagy szándékos-e a kettős levonás (ez esetben a KAPU:81 és :126 állítását kell javítani); (2) a 2. sor hová sorolja a „sokat beszéltél bele” típust; (3) ennek megfelelően a 4.1 indoklása és verdiktje. Korlát: a 0/1/2 szintnevek, a 4 sor és a küszöb változatlan.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT. A rubrika lezárt, bukásnál ott az F-peula és a javító próbálkozás, az M2 tanulási része pedig a Q-REL-2 szerint nyílik. A pilotban értékelői kalibrációval kezelhető, repóváltozás nélkül.
- Hipotézis: új

**ERT-G2-3**
- Súlyosság: P1 · Bizalom: magas · Lencse: értékelés
- Hely: M1.4:10, :380 (@asset), :426, :434 (@source VO), :450; M1.3:45 ↔ PT:106, :138, :142; HUB:33, :39, :125; KAPU:21, :197
- Probléma: A kapuprodukum hossza ellentmondásos. A tanulói leckeszöveg 1–2 mondatos SBI-t kér, a PT, a HUB és a KAPU 2–3 mondatost. A rubrika hosszt egyáltalán nem mér: a KAPU egymondatos 4.1-es mintája „Teljesítve”.
- Bizonyíték: M1.4:450 „Ebben a feladatban **1–2 mondatos SBI-visszajelzést** fogalmazol meg” — PT:142 „1–2 db 2–3 mondatos SBI-váz Moodle Assignmentben”
- Hatás: A kimondott cél (HUB:33) és a kapu „Mit mér” sora (KAPU:21) olyan hosszt ígér, amelyet sem a rubrika, sem a tanulói instrukció nem követ. Az M1.4 „1–2”-je feltehetően az SBI-k *számával* keveredett (HUB:132 „írjon 1 (max. 2) SBI-t”; M1.4:461, :491–492).
- Javaslat: EMBERI DÖNTÉS (modulgazda + értékelési felelős). Kérdés: melyik a kánoni hosszelőírás, és legyen-e rubrikaszempont. Lezárt projektgazdai döntés nem rendezi; a kánoni sorrend szerint a PT (1.) és a modulfájlok (2.) ütköznek. Átvezetésnél: az M1.4:434 VO-forrás, változása VO-újragyártást von maga után; az M1.4:380 @asset-metaadat.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT. A hossz nem pontozott, az M1.4-et követő tanuló nem bukik miatta.
- Hipotézis: mátrix 12. szakasz „M1a” (≈1070) — megerősítve, kiegészítve az M1.3:45, M1.4:380 és PT:106/:138/:142 helyekkel

**ERT-G2-4**
- Súlyosság: P2 · Bizalom: magas · Lencse: értékelés
- Hely: KAPU:11, :28, :308, :200 ↔ MAN §2 (:45–51), MAN:35
- Probléma: A KAPU §3 item-bankját a forrás külön, completion-only tanulói activitynek írja le, szabad szöveges 5–6. itemmel. A manifest §2-ben viszont nincs neki sora, így sem completion-, sem privacy-specifikációja nincs.
- Bizonyíték: KAPU:308 „**A 3. szakasz item-bankja** külön Quiz/H5P Question Set, **completion-only**” — MAN:35 „Ha más leckében is Moodle-oldali szabadszöveg-mező készül, az a build előtt ugyanígy saját sort kap (build_id, profil, completion, privacy).”
- Hatás: Ha a build a manifestet követi, a tanuló sosem látja a tíz javított itemet (köztük az egyetlen „alkalmazó” itemeket). Ekkor a KAPU:200 tanulói utasítása („ezt add be az M1.4 Assignmentbe”) és a PT:271 kvíz-utalása árva marad. Ha ad hoc épül, a szabad szöveg P2-adatként specifikáció nélkül tárolódik.
- Javaslat: EMBERI DÖNTÉS (LMS-gazda/programvezető + értékelési felelős). Két út: (a) az item-bank csak szerzői itempool, és ehhez igazodik a KAPU:11/:28/:308/:200; vagy (b) új §2-sor (profil, completion, P2 privacy az 5–6. itemre), és döntés arról, beszámít-e az „M1 complete”-be (HUB:248). Korlát: az LMS-M1-05/-06 és a küszöb nem érintett.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT. Sor nélkül a pilot-build nem hozza létre, a tanulói előrehaladást nem érinti.
- Hipotézis: új

**ERT-G2-5**
- Súlyosság: P2 · Bizalom: magas · Lencse: értékelés
- Hely: M1.4:482, :484 (és a §4.2 másolat: :586, :611) ↔ KAPU:55, :75; önellenőrzés: KAPU:199, M1.3:1030
- Probléma: A beadás előtt látható tanulói rubrika-összefoglaló két horgonyban eltér a hivatalos rubrikától. Az S „Erős” szintje szigorúbb (mikor, hol *és* melyik helyzet), az I „Erős” szintjéből pedig kimarad a „hiteles / logikusan következik a B-ből” feltétel. A sornév is eltér: „érthetősége” a „hitelessége / érthetősége” helyett.
- Bizonyíték: M1.4:482 „Kiderül, mikor, hol és melyik helyzetben történt.” — KAPU:55 „idő ÉS/VAGY hely ÉS a helyzet szakasza azonosítható.”
- Hatás: A tanuló nem tudja, hogy az I-sorban a B-hez képesti hihetőséget is pontozzák, ezért váratlanul veszíthet pontot. Az S-nél a szükségesnél többet céloz meg; a „konkrét hely és idő” önellenőrzés ugyanígy szigorúbb. Az M1.4 maga mondja, hogy a KAPU a forrás (M1.4:553, :635).
- Javaslat: Objektív. Az M1.4:482/:484 (és a :586/:611) szövegét igazítsd a KAPU:55/:75 horgonyaihoz és sornevéhez; az önellenőrzés igazítása másodlagos. Korlát: a szintnevek, a pontok, a sorok száma és a küszöb nem változik; látható szöveg, ezért --pin-visible kell.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT. A szempontok láthatók, az eltérés nem blokkol, a freeze alatt látható szöveg ezért nem módosul.
- Hipotézis: N-M1-07, N-M1-09 (az „egyezik / horgonyok egyeznek” megállapítás részben cáfolva)

**ERT-G2-6**
- Súlyosság: P2 · Bizalom: közepes · Lencse: értékelés
- Hely: KAPU:298 (§5), KAPU:255; MAN:50 (LMS-M1-05); RA:36
- Probléma: Sem a KAPU §5, sem az M1.4 §3.2, sem a manifest nem rögzíti a Moodle-rubrika tanulói megjelenítését. Nincs előírva, hogy a tanuló a beadás előtt előnézetben lássa a rubrikát, sem az, hogy értékelés után lássa a soronkénti szintet és az értékelői megjegyzést. Runtime-teszt sincs rá. Az M2 KAPU ezzel szemben rögzíti a tanulói megjelenítést (M2KAPU:176).
- Bizonyíték: KAPU:298 „**Grading method:** Rubric → vidd be a fenti 4 sort, soronként 0/1/2 ponttal és a szintleírásokkal.” — KAPU:255 „Így a tanuló látja, miből jött a pont.”
- Hatás: A kézi rubrika-létrehozás (MAN:190, MANUAL FALLBACK) a beállításokat az építőre bízza. A KAPU:255 ígérete és a HUB:213-ban leírt F-peula-ráhangolódás („melyik rubrikasor nem teljesült”) a futásidejű beállítástól függ.
- Javaslat: Objektív. A KAPU §5-be és az LMS-M1-05 megjegyzésébe kerüljön a forrás szándékából (KAPU:255, M1.4:478) következő megjelenítés: rubrika-előnézet a beadás előtt, utána soronkénti szint és megjegyzés. A pontos beállításneveket a célverzión kell rögzíteni; ezeket elsődleges forrásból itt nem ellenőriztem. Futásidőben tanulói tesztfiókkal kell igazolni: RT-tétel, G3b bizonyíték-kapu. Korlát: a rubrika tartalma, a pontok és a küszöb változatlan.
- Típus: objektív (a runtime-igazolás bizonyíték-kapu, G3b) · Verdikt: —
- Pilot-besorolás: POST-PILOT. A szempontok a beadás előtt az Assignment-leírásban láthatók (M1.4:478–487), a pontozás után a M→H→K komment magyaráz.
- Hipotézis: N-M1-06, N-M1-11, mátrix M1-03 (≈1031; CC-06)

**ERT-G2-7**
- Súlyosság: P2 · Bizalom: magas · Lencse: értékelés
- Hely: M1.4:321–324 (Slide 3) ↔ KAPU:134
- Probléma: Az M1.4 3. diáján a helyes S-opció az egyetlen időhatározós válasz. Ez pontosan az a felületi jel, amelyet a KAPU maga nevez meg hibaként, és a saját itemjeiben már kijavított (KAPU Item 1–2).
- Bizonyíték: M1.4:321 „„Ma a peula közepén…” ✅” (a három elosztó: „Nagyon tiszteletlen voltál.” / „Elegem van ebből.” / „Felforgattad az egész kört.”) — KAPU:134 „(pl. az egyetlen időhatározós opció felületi mintázatból megfejthető)”
- Hatás: Az item nem az S fogalmát méri, csak a „van-e időhatározó” jelet. A formatív visszajelzés így hamis biztonságot ad.
- Javaslat: Objektív. Az M1.4:322–324 elosztóiba kerüljön időjelölés a KAPU Item 1 mintájára, a hibatípus (címke / érzés / minősítés) maradjon; a :328 visszajelzés ehhez igazodjon. A ✅ nem változik; --pin-visible kell.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT. Formatív, nem kapuzó item.
- Hipotézis: új

**ERT-G2-8**
- Súlyosság: P2 · Bizalom: magas · Lencse: értékelés
- Hely: M1.3:724–736 (Slide 4, „melyik az I?”)
- Probléma: A kérdés azt kéri, hogy a megadott mondat melyik *része* az I. A D elosztó viszont nem szerepel a mondatban, így olvasás nélkül kizárható.
- Bizonyíték: M1.3:725 „…félbeszakítottad a többieket, miközben éppen ők beszéltek, én emiatt elvesztettem a fonalat, és a kicsik elcsendesedtek.” — M1.3:732 „„elég kaotikusan, kapkodva és összevissza vezetted az egész kört” *(ez címke, nem hatás)*”
- Hatás: Valójában háromopciós item, kitöltő elosztóval; a :736 visszajelzés nem mondja meg, hogy a D nem a mondat része.
- Javaslat: Objektív. A D-t töröld, vagy cseréld a mondatból vett opcióra; a :736 visszajelzés ehhez igazodjon. A ✅ és az A–C nem változik; --pin-visible kell.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT. Formatív item.
- Hipotézis: új

**ERT-G2-9**
- Súlyosság: P2 · Bizalom: közepes · Lencse: értékelés
- Hely: KAPU:165 (Item 3 ✅), KAPU:75 (I „Erős” horgony), M1.4:359 (Slide 5 ✅) ↔ KAPU:157
- Probléma: A modul a szándék tulajdonítását hibának tanítja. Ugyanakkor a „leghitelesebb I” kulcsa és az „Erős” horgony a másik belső állapotát tulajdonítja („nem fontos neked”), és a visszajelzés nem magyarázza a különbséget.
- Bizonyíték: KAPU:165 „A) „Úgy éreztem, nem fontos neked, amit megbeszélünk.” ✅” — KAPU:157 „a „látszott, hogy szét akarod verni” pedig **szándékot tulajdonít**”
- Hatás: A tanuló épp a modul magját (megfigyelés ≠ értelmezés) tanulhatja ellentmondásosan, és a kapuban a mintát követő I-t „Erős”-nek kapja.
- Javaslat: EMBERI DÖNTÉS (modulgazda/módszertani lektor + értékelési felelős). Két út: (a) a kulcs és a horgony marad, és a visszajelzés (KAPU:170, M1.4:366) kap megkülönböztető magyarázatot (saját észlelés én-alakban vs. tényként állított szándék); vagy (b) a horgony helyére olyan I kerül, amely nem tulajdonít belső állapotot. Az answer key döntés nélkül nem változik; tárgyi hibát elsődleges forrással nem igazoltam.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT. Senkit nem buktat, tisztázást igényel.
- Hipotézis: új

**ERT-G2-10**
- Súlyosság: P2 · Bizalom: magas · Lencse: értékelés
- Hely: KAPU:43, :97–100 ↔ HUB:239, :249
- Probléma: Az értékelőknek szóló KAPU olyan hub- és M1.4-állapotra hivatkozik, amely már nem létezik: 3 soros rubrika, „alapszint” és „fejlődő” szint, „SBI struktúra összhatása” sor. A :43 megjegyzés jelen időben állítja, hogy a hub a régi szóhasználatot használja.
- Bizonyíték: KAPU:43 „a „minden sorban legalább alapszint” fordulat a modul-áttekintő régi szóhasználata” — HUB:239 „A kapu **hivatalos, 4 soros rubrikáját**…” (HUB:249 „Rendben” / „Erős”)
- Hatás: Az értékelő nem létező szintneveket („fejlődő”) és régi küszöböt (6/8) olvas a hivatalos forrásban, ami kalibrációs zaj.
- Javaslat: Objektív. A :43 megjegyzést és a :97–100 bekezdést jelöld egyértelműen történetinek, vagy igazítsd a hub mai állapotához. A küszöb és a szintek nem változnak.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT. Értékelői dokumentum, a döntési szabályt (:104–109) nem érinti.
- Hipotézis: új

LEVÁGVA: 2 további finding, súlyosságuk: 2×P2
- ERT-G2-11 · P2 · M1.3:813–815 (+ @asset NAR-04 spec :750) · Az 5. dia narrációja („próbáld meg beírni”) beviteli mezőt sugall, holott a dia (:799) és a D-1 szerint nincs beviteli elem; a szöveg @source VO, a javítása VO-újragyártással jár.
- ERT-G2-12 · P2 · M1.4:491–492 ↔ KAPU:300 · Két beadott SBI esetén a jobbik számít, ezt a tanulói leírás nem mondja; a Moodle-rubrikában csak egy SBI pontjai rögzülnek, a másikra adott soronkénti visszajelzés elvész.

Elvetett hipotézisek
- N-M1-04: a 2. csoport fájljai (KAPU, M1.3, M1.4) nem építenek az M1.1 SLIDE 5 reflexióra (az „M1.1” és „reflexió” keresés a KAPU-ban 0 találat, az M1.3/M1.4-ben csak az M1.3 saját SLIDE 5 címe), így ebben a csoportban nincs ütközés a projektgazdai döntéssel.
- Fókusz 3, D-1 (nem mátrix-ID): elvetve. Az 5. dia tanuló-lokális, nem tárolt és nem completion-feltétel, a 6. dia tárolt LMS-M1-07; ez egyezik az M1.3:58, :80, :799, :924–926, :1098–1099, a MAN:47–49 és a HUM 10. szakasz :522 szövegével. Az egyetlen árnyalat az ERT-G2-11.


# ERT-G3

**Fájlrövidítések (abszolút utak)**
- M1.A = 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- M1.B = 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- M1.F = 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- HUB = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- KAPU = 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- M1.1 = 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- PT = 02 Tervezet/Program terv.md

Runtime-bizonyíték nincs; a Moodle-beállításra vonatkozó megállapítás egyike sem ellenőrzött.

---

**ERT-G3-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.F:277 (4.2 Lépések, 2. pont), M1.F:54 (2. cél), M1.F:349–365 (4.4); HUB:223
- **Probléma:** Az F-peula a kapu szerint „facilitált, strukturált javítási alkalom”, a bukott tanuló javított SBI-vázlatára mégsem ad formatív visszajelzést. A csendes blokkban a képző csak technikai segítséget ad. A 2. cél vázlat nélkül, egy leckerész újranézésével is teljesül. A zárásból hiányzik a hub szerinti tanulói lépés: „mire figyel a javított SBI-ben”.
- **Bizonyíték:** M1.F:277 „A képző **körbejár**, de csak röviden segít (technika, „hol találom ezt?”).” ↔ KAPU:24 „facilitált, strukturált javítási alkalom (egyéni vagy kiscsoportos támogatás)”
- **Hatás:** A mastery-hurok így „bukás → újranézés → újrabeadás” marad, ellenőrzés nélkül. A tanuló ugyanazzal a rubrikasor-hibával mehet a javító próbálkozásba, és az újabb bukás az M3-kapu felé blokkol.
- **Javaslat:**
  - A 4.2 2. lépésébe: a nem teljesült kapujú tanulóhoz a képző diszkréten odaül, és a vázlatra a KAPU 1. szakaszának szintleírásaival rövid, Megfigyelés → Hatás → Következő lépés szerkezetű visszajelzést ad, csak a nem teljesült sorra. A szöveget nem írja át helyette.
  - Az M1.F:54 2. célja bukott tanulónál a vázlat megírását kérje.
  - A 4.4-be bekerül a HUB:223 tanulói lépése, privát jegyzetlapra: „mire figyelek a javított SBI-ben”.
  - Nem nyúlhat hozzá: a 45’ és a blokkhatárok, a kapu, a küszöb, a completion, az M1.F:36 adatvédelmi kerete és a safer-working szabály (M1.F:95).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A javító út létezik és megnyílik, a hiány csak a minőségét gyengíti; nem P0, és nem blokkolja az előrehaladást.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G3-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.F:293–299 (4.3 Cél és időbeosztás), M1.F:340–343, M1.F:263 és az M1.F-MUNK-01 spec (M1.F:192)
- **Probléma:** A Blokk 3 a kapus visszajelzés négy lehetséges hiányából (S, B, I, hangnem) csak hármat fed le. A 4. rubrikasor (általánosítás „mindig/soha/megint”, gúny, a személy minősítése) nem kap magyarázatot. Közben a kapu által nem mért Vakfolt kötelező („40’-re mind a 3 kulcsfogalom”), és az időbeosztási szabály is csak a 3 fogalomhoz igazodik.
- **Bizonyíték:** M1.F:293 „…amelyeket a kapun kapott visszajelzések jeleztek (S, B, I vagy hangnem).” ↔ KAPU:85 „általánosító „mindig/soha”, jellem-címke, gúny, leszólás.”
- **Hatás:** Akinél a hangnem-sor lett 0 (pl. KAPU:86 „Megint elkéstél, ami azért elég gáz tőled.”), az célzott magyarázat nélkül megy a javító próbálkozásba.
- **Javaslat:**
  - Az M1.F:322–325 „Megfigyelés ≠ címke” mini-magyarázatát egészítsd ki a KAPU 4. sorának (KAPU:81–87) szintleírásával, vagy vedd fel a hangnemet a mini-összegzésbe (:340–343) és az időbeosztási szabályba (:299).
  - A B-terv összefoglalójába (M1.F:263, M1.F-MUNK-01) kerüljön egy hangnem-sor. Az @asset-blokk szerkesztése után media build.
  - A Vakfolt-rész maradhat (HUB:28).
  - Nem nyúlhat hozzá: a 45’, a 25–40’ sáv és a rubrika.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Minőségi illeszkedési hiány, nem blokkoló hiba.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G3-3**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.B:134–139 (2.1 trió-checklist), M1.B:362–369 (4.2.3, 3–4. lépés), @asset M1.B-MUNK-01 spec (M1.B:102)
- **Probléma:** A megfigyelő (C) checklistje csak az S/B/I és a címke meglétét kérdezi (igen/nem), és a „mindig/soha/megint” általánosítást nem kérdezi. A kapu viszont minőségi szinteket mér: a tág S csak „Rendben”, és legalább egy „Erős” sor kell. Így egy kapu alatti SBI is „minden igen” jelölést kap.
- **Bizonyíték:** M1.B:135 „Volt **S**? (igen / nem)” ↔ KAPU:54 „**Rendben (1)** | Van valamilyen helyzet-megjelölés, de **tág / általános**”
- **Hatás:** A trió azt tanítja, hogy az elemek megléte elég. Egy csupa „Rendben” (4/8) SBI-t a megfigyelő sikeresnek jelez, pedig a kapun megbukna. Ez félrevezet az M1.B:476 szerinti újrabeadásnál és az F-peula előtti javításnál is.
- **Javaslat:**
  - A checklist sorai az igen/nem helyett háromfokúak legyenek: „nincs / van, de általános / konkrét”, a KAPU 1–3. sorának tanulói nyelvű kivonatával.
  - Új sor: „Volt „mindig/soha/megint” vagy minősítő szó?”
  - Ehhez igazodjon a C mini-reflexiós kérdése (:369) és az @asset (media build).
  - Nem nyúlhat hozzá: a kapu-rubrika, a küszöb és az időkeret.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Formatív peer-eszköz, nem kapu és nem completion-feltétel.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G3-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.B:148, :214, :218, :241, :495; M1.B:69 és :86 (@asset M1.B-KART-02 purpose/notes); M1.B 2.1 Eszközök (:127–143)
- **Probléma:** A mini-kvíz A/B/C/D sarokkal fut (:214; az 1., 2. és 4. kérdés négyopciós, ✅-kulccsal), több hely azonban még a régi elrendezést írja:
  - a tér (:148) és az ellenőrző lista (:495) „A/B sarkot” ír;
  - az @asset a 3 smiley-kártyát nevezi meg „A/B/igaz-hamis” sarokjelölőnek (:86, :69): 3 kártya jut 4 sarokra, és a 2.1-ben nincs sarokjelölő eszköz;
  - a MAG-lista a 4. kérdést egy már nem létező tartalommal nevezi meg (:218).
- **Bizonyíték:** M1.B:495 „Van hely mozogni A/B sarkok között.”; M1.B:218 „**4. kérdés** (melyikből tudsz javítani?)” ↔ :241 „Melyik mondat nevez meg konkrét viselkedést és hatást?”
- **Hatás:** Ha a képző két sarkot rendez be, vagy a 3 smiley-t teszi ki, a négyopciós kérdések egyik válasza nem választható. Időcsúszásnál a MAG-címke alapján rossz kérdést tarthat meg. Maga az answer key konzisztens.
- **Javaslat:**
  - :148 és :495 → „A/B/C/D sarok”.
  - :218 → „4. kérdés (melyik mondat nevez meg konkrét viselkedést és hatást?)”.
  - A KART-02 :69 purpose és :86 notes mezőjéből töröld a sarokjelölő szerepet; ha jelölőlap kell, a 2.1-be egy sor „A–D sarokjelölő” kerüljön.
  - Az @asset-blokk forrásszerkesztése után `python3 tools/media_manifest.py build`, külön chore(media) commitban; generált kimenetet kézzel ne szerkessz.
  - Nem nyúlhat hozzá: a ✅-jelölések, a kérdések és az opciók szövege.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A :214 utasítás önmagában végrehajtható; ez képzői dokumentációs széttartás (a mátrix is POST-PILOT-nak sorolta).
- **Hipotézis:** E-M1-069; a 12. szakasz M1b 2. pontja (M1.B:86) is igazolva.
- **Verdikt:** —

**ERT-G3-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés (routing: pedagógia/biztonság-jog)
- **Hely:** M1.1:930 (SLIDE 6 zárómondat, dia-szöveg) ↔ M1.A:270–274, :299–301
- **Probléma:** Az online lecke azt ígéri, hogy az M1.A-n a kvucával közösen dolgozzák fel a tanuló saját vakfolt-reflexióját. Az M1.A ezzel szemben kifejezetten nem nyitja meg a Vakfolt-mezőt, és nem épít az online, opcionális reflexióra (N-M1-04 szerint ez tanuló-lokális).
- **Bizonyíték:** M1.1:930 „ott a kvucával együtt dolgozzátok ki, amit itt a saját vakfoltjaidról végiggondoltál.” ↔ M1.A:273–274 „Ezt a részt most nem nyitjuk meg élesben … a vakfolt valódi feltárása egy későbbi, bizalmibb fázis lesz”
- **Hatás:** A tanuló úgy készül, hogy a privát önreflexióját a csoport előtt kell feldolgoznia, és ezt elvárásként éli meg. Ez feszül az N-M1-04 tanuló-lokális keretével.
- **Javaslat:**
  - Az M1.1:930 dia-szövegét igazítsd az M1.A tényleges tartalmához: közösen a Johari-logika, a Nyitott/Rejtett cetlik és a megfigyelés vs. címke; a saját önreflexiót nem kell megosztani.
  - A narráció (M1.1-NAR-06-VO, :936–938) nem tartalmazza ezt a mondatot, VO-érintettség nincs.
  - Nem nyúlhat hozzá: M1.A.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Az M1.A-n nincs kötelező önfeltárás (M1.A:282), így nem P0. Ha a biztonság-jog lencse önfeltárási nyomásnak minősíti, újrasorolható.
- **Hipotézis:** új (N-M1-04-ellenőrzés mellékterméke)
- **Verdikt:** —

**ERT-G3-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** M1.B:241–245 (4.1.2, 4. kérdés)
- **Probléma:** A MAG-ként „mindig menjen” 4. kérdésnek nincs kimondandó visszajelzése, pedig az 1., 2., 3. és 5. kérdésnek van (:228–229, :235–236, :239–240, :248–249). Az A opció jegyzete („címke a helyzetre”) ráadásul eltér a modul saját besorolásától.
- **Bizonyíték:** M1.B:242 „A: „Szétverted a peulát.” *(címke a helyzetre)*” ↔ M1.F:325 „Címke az, amit **te gondolsz / ítélsz a másikról**: – ‘tiszteletlen voltál’, ‘szétverted a peulát’.”
- **Hatás:** A rossz sarokba állók nem kapnak tanító magyarázatot a B+I együttes felismeréséről. A képző a jegyzetből téves indoklást mondhat: helyzet, holott ez nem S.
- **Javaslat:**
  - A 2. kérdés mintájára egy „→” visszajelzés kerüljön a meglévő opció-jegyzetekből: B konkrét viselkedés + hatás; A és C címke a másikról (C: „megint” általánosít); D érzés konkrétum nélkül.
  - Az A jegyzete: „címke a másikról”.
  - Nem nyúlhat hozzá: a ✅ (B) és az opciók szövege.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Nem pontozott szóbeli bemelegítés.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G3-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** M1.B:359 (4.2.3, 2. lépés), M1.B:476 (hurokzárás); vö. KAPU:21, KAPU:197, PT:106, HUB:33
- **Probléma:** Az M1.B 1–2 mondatos SBI-t gyakoroltat, és a peulán született „SBI-mondat” beadását ajánlja az M1.4 Assignmentbe. A kapu és a Program terv viszont 2–3 mondatos SBI-t ír elő, a hurokzárás pedig nem jelzi a beadási formát.
- **Bizonyíték:** M1.B:359 „Megpróbál **1–2 mondatban** S–B–I szerint fogalmazni.” ↔ KAPU:21 „…tisztelettudó**, 2–3 mondatos SBI-visszajelzést **írni**.”
- **Hatás:** A tanuló ugyanarra a produktumra két eltérő formai elvárást kap. A rubrika hosszat nem pontoz, így a kapudöntést ez nem rontja.
- **Javaslat:**
  - Az M1.B:476-ba egy félmondat: beadásnál a kapufeladat formája érvényes (2–3 mondatos SBI, S+B+I; KAPU:21, PT:106).
  - A szóbeli gyakorlás 1–2 mondata (:359) maradhat.
  - Az M1.3 és az M1.4 „1–2 mondatos” megfogalmazása a 2. csoport hatóköre.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A kapueredményre nincs hatása.
- **Hipotézis:** 12. szakasz M1a, 1. pont (az M1.B-re kiterjesztve igazolva)
- **Verdikt:** —

**ERT-G3-8**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** HUB:275–278 (§7/4 „Offline visszajelzés”) ↔ M1.B 4.4 (:431–478) és 5. képzői lista (:482–507)
- **Probléma:** A hub az M1.B végére 1 perces, név nélküli önbecslő kérdést ír elő analitikai adatforrásként, az M1.B forgatókönyvében viszont ilyen lépés nincs (Grep: a kérdés csak a hubban szerepel).
- **Bizonyíték:** HUB:276–277 „M1.B végén 1 perces, név nélküli kérdés: … „Mennyire érzed, hogy tudnál SBI-t használni a való életben? (1–5)””; M1.B 4.4.2 csak vállalást kér (M1.B:463).
- **Hatás:** A hub §7 egyik mérése adatforrás nélkül marad, így a stáb nem kap transzfer-önbecslést.
- **Javaslat:**
  - A hub két kérdését szó szerint, név nélküli kilépőkártyaként (az M1.A 4.4.2 mintájára) vezesd át az M1.B 4.4.2 végére és az 5. lista 6. pontjába.
  - Ha ez a 40–45’ sávba nem fér bele: EMBERI DÖNTÉS (programvezető), hogy a hub §7/4 maradjon-e.
  - Nem nyúlhat hozzá: a 45’.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Analitikai hiány, nem tanulói blokk.
- **Hipotézis:** új
- **Verdikt:** —

**ERT-G3-9**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés (routing: implementáció/D12)
- **Hely:** M1.B:192, :203 (4.1.1) ↔ M1.B:70, :74 (@asset KART-02), M1.B:140–143 (2.1), M1.B:186
- **Probléma:** A 4.1.1 minden résztvevőtől kétszer kér kártyafelmutatást (hangulat, majd elégedettség). Az eszközlista és az asset viszont csak 3 db, a képző által felmutatott kártyát ír elő.
- **Bizonyíték:** M1.B:192 „háromra emeljétek fel azt a kártyát, ami leginkább tükrözi, hogyan érkeztetek meg” ↔ M1.B:70 „Három nagyméretű, felmutatható kártya … A képző a ráhangoló blokkban (4.1.1.) felmutatja”
- **Hatás:** A gyors hangulat- és elégedettségi felmérés írott formában végrehajthatatlan; a képző improvizál.
- **Javaslat:**
  - A 2.1-be és a KART-02 specbe: fejenként egy kis 3-as szett (😃/😐/😬), a 3 nagy képzői kártya marad. Utána media build.
  - Könnyebb alternatíva: az instrukcióban kézjel (1–3 ujj) szerepeljen.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Kézjellel helyben pótolható, nem P0.
- **Hipotézis:** 12. szakasz M1a, 2. pont (igazolva)
- **Verdikt:** —

**ERT-G3-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** HUB:221–222 és HUB:178 (@asset M1-HUB-POSZ-02) ↔ M1.F:84–86, :115, :303–315
- **Probléma:** A hub és az M1.F három ponton eltér:
  - a jegyzetlap: a hubban „leckénként 1 gondolat, 1 kérdés”, az M1.F-ben 1 mondat + 1 kérdés;
  - a 25–40’ sáv: a hubban „Közös fogalom-térkép”, az M1.F-ben kérdés–válasz és 3 mini-magyarázat, fogalomtérkép-építő lépés nélkül;
  - a hub erre külön posztert gyárt („M1.F cél 4”), de az M1.F-ben nincs 4. számozott cél.
- **Bizonyíték:** HUB:221 „jegyzetlap: „leckénként 1 gondolat, 1 kérdés”.” / HUB:222 „25–40’ – Közös fogalom-térkép” ↔ M1.F:85 „„**1 mondat** arról, mi volt a legfontosabb…””
- **Hatás:** A képző a hubból más formatív eszközt és más blokkot készít elő, mint amit a peula vezet. A poszter-asset olyan lépéshez kötődik, amelyet a forgatókönyv nem ír le.
- **Javaslat:**
  - A HUB §5 percbontását (221–222) és a M1-HUB-POSZ-02 purpose mezőjét igazítsd az M1.F tényleges blokkjaihoz (M1.F:303–308). Utána media build.
  - Hogy az asset megmarad-e, az a médiafelelős döntése.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Előkészítési széttartás, nem tanulói blokk.
- **Hipotézis:** új
- **Verdikt:** —

LEVÁGVA: 3 további finding, súlyosságuk: 3×P2
- ERT-G3-11 · P2 · KAPU:253–291 ↔ M1.F:163: Az M1.F arra épít, hogy a bukott tanuló a kapus visszajelzésből kiolvassa a nem teljesült sort, a KAPU 4. szakasza viszont csak átment beadványra ad mintavisszajelzést; nem teljesítettre (a 0-s sor megnevezése és a következő lépés) nincs sablon. A javítás helye a kapufájl, a 2. csoport hatóköre.
- ERT-G3-12 · P2 · M1.B:223–227, :246: Az 1. kérdés D) „Sound – hangerő” elosztója kitöltő zaj, nem valós tévedés; az 5. kérdés abszolút „tilos” szava előre jelzi a „hamis” választ. A ✅ helyes.
- ERT-G3-13 · P2 · M1.F:171–172: A kemény sortörés két sorvégi szóköz, nem `\` (course-content.md). Lencsén kívüli; a 12. szakasz M1b 1. pontja ezzel igazolva.

**Elvetett hipotézisek**
- N-M1-05 / 11. szakasz M1-04: értékelési lencsén nem finding. Az M1.A mozgásos játéka kifejezetten nem pontozott (M1.A:368), új mondatok írására az M1.A:372 már utasít, az M1.B kártyái pedig szándékosan az M1.4-ből jönnek (M1.B:128). Pedagógiai finomításként POST-PILOT marad.
- Q-REL-2 (3. fókuszpont): az M1.F-ben nincs a Q-REL-2-nek ellentmondó mastery- vagy unlock-állítás; M2-re vagy downstream zárásra sem utal. Az időzítés („megerősítés után, javító előtt, hétfő 18:00-tól”, M1.F:65) egyezik a HUM:510-zel és a manifest:245-tel.
- N-M1-04 (a peulák oldala): egyik peula sem épít az M1.1 SLIDE 5 reflexiójára beadott vagy hozott produktumként. Az M1.A új cetliket írat (M1.A:230–235), az M1.B:385 az M1.A Vakfolt-mezőjére utal, az M1.F privát (M1.F:36). Ellentétes jelzés csak az online M1.1:930 áthidaló mondatában van, ez az ERT-G3-5.
- E-M1-070, E-M1-071, E-M1-073: a megőrzött szövegekben nincs értékelési hiba.
- E-M1-072: az M1.F:316, :326, :339 csak szóközös sor, formázás, értékelési hatás nélkül.
- 12. szakasz M1a, 3. pont (RA:104 / RT-P0-24): nem a 3. csoport hatóköre, nem vizsgáltam.


# IMPL-G1

RÉSZLEGES: az N-M1-04 lánc (a)–(e) pontját végignéztem: M1.1 SLIDE 5, LMS-M1-01, RT-P0-24/RT-P0-15, az Adatvédelem-leltár és a HUM-fájl. Négy dolog maradt ki: (1) a H5P.ExportableTextArea xAPI- és állapotmentési viselkedése, mert a forrásfájl URL-je 404-et adott; (2) a H5P Drag and Drop (DragQuestion) egypontos, illetve billentyűzetes kezelése és a Mark the Words billentyűzetmodellje elsődleges forrásból; (3) a KAPU-fájl H1-címének és a hub link-címkéjének egyezése; (4) a WCAG sikerkritériumok szövegét nem kértem le a w3.org-ról. A hivatkozott 2.5.7, 2.5.8, 1.2.1 és 1.1.1 sikerkritérium tartalmát nem vitatom.

Rövidítések (abszolút utak):
- HUB = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- M1.1 = 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- M1.2 = 02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- RA = 02 Tervezet/LMS – H5P runtime acceptance.md
- ADV = 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- HUM = 02 Tervezet/Emberi jóváhagyás szükséges.md
- RR = 02 Tervezet/RELEASE-READINESS.md
- A11Y = 02 Tervezet/LMS – hozzáférhetőségi sztenderd.md
- PD1010 = 01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md
- MTX = 01 Fejlesztés/04 Audit/2026-10-10 Anna-kommitok és szakmai javaslatok – teljes megfeleltetési mátrix.md

---

**IMPL-G1-1**
- **Súlyosság:** P0
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** M1.1:98; M1.1:699 (@asset M1.1-IKO-02 `notes`); M1.1:763; M1.1:792; M1.1:794; MAN:45
- **Probléma:** Az M1.1 SLIDE 5 opcionális önreflexiójához a forrás beviteli mezőt ír elő. Ha a teszt nem igazolja a mezőt, Moodle-oldali, név szerint tárolt tartalékmezőt rendel hozzá. A tanuló-lokalitás csak „lehetőleg” érvényes, és van mentor-láthatósági út. Ez ellentmond az N-M1-04 döntésnek („kizárólag tanuló-lokális, központi tárolás nélkül”). Ellentmond a manifest tanuló-lokális mintájának is (LMS-M0-01, LMS-M5-01).
- **Bizonyíték:**
  - M1.1:98: „ha a teszt nem igazolja, a mező Moodle-oldalra kerül.”
  - M1.1:794: „lehetőleg csak a tanuló látja (learner-local); a kijelölt mentor csak akkor láthatja”
  - MAN:45: „opcionális, nem completion-feltétel; lehetőleg learner-local”, szemben a MAN:79 mintával: „opcionális és tanuló-lokális: nem tárolt, nem completion-feltétel”
- **Hatás:** A build a GitHub-forrásból készül (PD1010:43). Két úton jöhet létre központi tárolás:
  - A :98 tartalékútja TEXT-C. Ez nem anonim Feedback: „User's name will be logged and shown with answers” (MAN:24).
  - A :763 „1 szövegmező” megépíthető CP-n belül is. A h5p-course-presentation semantics.json beágyazható típusai között szerepel a „H5P.ExportableTextArea 1.3”. Az RA:104 szerint ez „a szöveget a tartalom állapotában tartja”, a Moodle „Save state” beállítása pedig felhasználónként menti az állapotot (lásd IMPL-G1-4).

  Így a pilot (részben kiskorú) tanulóinak személyes önreflexiója központilag tárolódhat. Az ADV:115 szerint a nem szerkesztő tanár is láthatja, ami ütközik az N-M1-04-gyel és az ADV:150-nel. A :792 Essay-útja CP-ben nem is létezik: A11Y:63, és a semantics.json opciói között nincs H5P.Essay.
- **Javaslat:**
  - (a) M1.1:98: a SLIDE 5-re a M5.1:24 / M0.1:59 minta: „A SLIDE 5 mezője opcionális és tanuló-lokális (N-M1-04): a tanuló magának írja le, CP-be ágyazott beviteli elem és Moodle-oldali mező nem épül hozzá, és nem completion-feltétel (LMS-M1-01; runtime acceptance 24. pont).”
  - (b) M1.1:763: a „1 szövegmező (…)” sor kikerül, beviteli elem nincs.
  - (c) M1.1:792: a mezőről és az Essay-ről szóló sor helyére a tanuló-lokális besorolás kerül.
  - (d) M1.1:794: a „lehetőleg… mentor… láthatja” mondat helyére a döntés szövege kerül: kizárólag tanuló-lokális, központi tárolás nélkül, nem completion-feltétel.
  - (e) M1.1:699: az @asset `notes` „szövegmező (Moodle-oldali vagy H5P…)” része helyett: beviteli elem nélkül. Utána `python3 tools/media_manifest.py build`.
  - (f) MAN:45 új szövege: „a SLIDE 5 személyes önreflexiója opcionális és tanuló-lokális: nem tárolt, nem completion-feltétel, beviteli elem nem épül hozzá (N-M1-04; runtime acceptance 24. pont)”.

  Javítási korlát:
  - Nem változik: a három kérdés, a :767–774 tanulói szöveg, az M1.1-NAR-05 `@source`, a completion-logika, a SLIDE 1–4 és a SLIDE 6.
  - „Nem tároljuk” típusú tanulói mondat nem kerülhet be, amíg az RT-P0-24 visszaolvasása nem sikeres (RA:104, utolsó mondat).
  - A :763 címke kiesése látható szöveget érint, ezért `--pin-visible` kell.
  - Előfeltétel: IMPL-G1-2.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. Tényleges P0 adatvédelmi hiba a pilot M1-ének első leckéjében. A javítás a fejlesztői specben és a manifestben történik, a tanulói kérdésszöveg nem változik. A felépített kurzus állapotáról nem állítok semmit (CC-06).
- **Hipotézis:** N-M1-04 / M1-02 / X-06 (MTX:356, :1030, :1059)

**IMPL-G1-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:**
  - HUM: az utolsó datált szakasz a :529-es „## 11. … (2026-10-05)”; az `N-M1-04` azonosítóra nincs találat.
  - PD1010:16–52: a szó szerinti válasz csak az 1–5. pontot tartalmazza.
  - MTX:24, :356, :1030, :1130: a tétel még `UNRESOLVED` / `EMBERI DÖNTÉS` állapotú.
- **Probléma:** A projektgazda 2026-10-10-i N-M1-04 döntése nincs átvezetve sem a HUM-fájlba, sem a `04 Audit` döntési jegyzőkönyvébe. A mátrix még nyitott P0 emberi döntésként tartja nyilván.
- **Bizonyíték:**
  - MTX:1030: „| M1-02 | M1.1 SLIDE 5 reflexió láthatósága | N-M1-04 | `UNRESOLVED` **P0**: tárolja-e a pilot-build (projektgazda, DPO-QA). |”
  - HUM:529: „## 11. Projektgazdai döntések – pilot-ütemezés, build-blocker leltár, completion és M3.3 (2026-10-05)”; ezután nincs újabb datált szakasz.
- **Hatás:** Az IMPL-G1-1 javítása nem tud kánoni helyen rögzített döntésre hivatkozni. Egy későbbi reviewer vagy fixer nyitott kérdésnek veheti, vagy a mátrix „a mező előtt tájékoztatni” alternatíváját valósíthatja meg (MTX:50). A 2026-10-10-i freeze-kivételi szabály (PD1010:41, :58–59) sincs a HUM-fájlban.
- **Javaslat:**
  - A döntési csomagból (szerepnév: projektgazda) a N-M1-04 szó szerinti szövegét egy `04 Audit` döntési jegyzőkönyvben kell rögzíteni.
  - Új datált szakaszban (12., 2026-10-10) át kell vezetni a HUM-fájlba, a Forrás oszlopban a jegyzőkönyvre hivatkozva.
  - Utólagos ellenőrző szerepet csak akkor írj be, ha a csomag megnevezi; ne találd ki.
  - A PD1010 2. pontja (freeze-kivételi szabály) ugyanebbe a szakaszba vehető.
  - Az MTX audit trail: a sorait nem írjuk át, legfeljebb datált kiegészítést kapnak.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. Ez az IMPL-G1-1 P0 adatvédelmi freeze-kivételének kánoni alapja; tananyagot nem érint.
- **Hipotézis:** N-M1-04 (MTX:1130), M1-02

**IMPL-G1-3**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** RA:104 (a 24. pont felsorolása); RA:41 (6. pont: „BSPEC-02 leltár, D-1…D-6”); MAN:308 (a BSPEC-02 „opcionális, tanuló-lokális” listája); ADV:115 (a H5P-C sor, amely a manifest §2-re hivatkozik)
- **Probléma:** Az LMS-M1-01, illetve az M1.1 SLIDE 5 két helyről hiányzik:
  - az RT-P0-24 felsorolásából, amely a tanuló-lokális szöveges lépések rögzítésmentességét igazolja;
  - a BSPEC-02 leltár „opcionális, tanuló-lokális” listájából.

  Ezért az ADV:115 garanciája („a tanuló-lokális lépések nem tárolódnak (manifest §2)”) sem terjed ki rá. Az Adatvédelem-dokumentumban nincs M1.1-sor, és a „Külön review” listán (ADV:80) csak az „M1 SBI-beadandó” szerepel.
- **Bizonyíték:**
  - RA:104: „(a manifest §2 LMS-M0-01…04, LMS-M1-03, LMS-M2-03, LMS-M2-04, …” (az LMS-M1-01 nincs benne)
  - MAN:308: „opcionális, tanuló-lokális: M0.3 SLIDE 7, M2.3 mini-reflexiók, M3.3 SLIDE 6, M5.1 SLIDE 6, M6.3 SLIDE 7, M6.4 mini-reflexiók”
- **Hatás:** A staging-tesztterv nem ellenőrzi, hogy az M1.1 SLIDE 5 szövege nem tárolódik. Az RT-P0-15 (RA:84) csak a láthatóságot nézi, a tárolt szöveget vagy mentett állapotot nem. Ez az IMPL-G1-1 javítása után is lefedetlen maradna.
- **Javaslat:**
  - RA:104: az „LMS-M1-01” beszúrása a felsorolásba, az LMS-M1-03 elé.
  - MAN:308: ez datált, `BUILD_SPEC_RESOLVED` sor, ezért legfeljebb datált kiegészítést kap („2026-10-10: M1.1 SLIDE 5 opcionális, tanuló-lokális, N-M1-04”). Elég lehet a MAN:45 javított megjegyzése is (IMPL-G1-1 f).
  - ADV:115: a MAN:45 javításával lefedetté válik, külön szerkesztés nem kell.

  Javítási korlát: az RT-P0-24 állapota `IMPLEMENTATION_TEST_REQUIRED` marad; más sor nem változik.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. A P0 adatvédelmi javítás tesztfedezete az M0+M1 pilot evidence listájához (PILOT-1, HUM:548). M1-tananyagot nem érint.
- **Hipotézis:** MTX:1072 (12. szakasz, „M1a” 3. pont); az N-M1-04 „Kapcsolódó hiány” része (MTX:356)

**IMPL-G1-4**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** RA:152 (RT-P0-24); RA:143 (RT-P0-15); RA:137 (RT-P0-09); RR:25 (G2); RR:27 (G3b)
- **Probléma:** Nincs runtime-bizonyíték arra, hogy az M1.1 SLIDE 5 szövege nem tárolódik (sem a próbálkozás-riportban, sem mentett állapotban), és hogy a completion nem függ tőle.
- **Bizonyíték:**
  - RA:152: „| RT-P0-24 | `IMPLEMENTATION_TEST_REQUIRED` | 24. Tanuló-lokális szöveges lépések | | | |”
  - Moodle `MOODLE_405_STABLE`, mod/h5pactivity/lang/en/h5pactivity.php, `enablesavestate_help`: „Automatically save the user's current state. The user can return later and resume where they left off.”
- **Hatás:** A pilot előtt nincs igazolva, hogy a „központi tárolás nélkül” döntés megvalósult. A „Save state” felhasználónként menti a H5P-állapotot, így egy CP-be ágyazott szövegbevitel a döntés ellenére megmaradhat.
- **Javaslat:** A repóban nem javítható. Megvalósítási döntés: a projektgazda jóváhagyta (N-M1-04); a formális szerepköri bizonyíték függő.
  - G2: a láthatósági tesztek POST-BUILD tételek, a DPO release-ellenőrzése FINAL_RELEASE_QA.
  - G3b: runtime-tesztek.
  - Tracker: #2 és #3.

  A teszt az RA 24. pont szerint fut az LMS-M1-01-re is (az IMPL-G1-3 után). Ha nincs beviteli elem, ezt rögzíteni kell. Képzői fiókkal vissza kell olvasni a próbálkozás-riportot és a mentett állapotot, és ellenőrizni, hogy a completion független a szövegtől.
- **Típus:** bizonyíték-kapu
- **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER. Az M0+M1 GO/NO-GO evidence listájának (PILOT-1) adatvédelmi tétele; nem tartalmi változtatás.
- **Hipotézis:** MTX:1072 („csak az RT-P0-15 általános teszt fedi”)

**IMPL-G1-5**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** M1.1:204 (SLIDE 1, „Megvalósítás”); M1.1:344 (SLIDE 2); MAN:16 (H5P-C: „Enable attempt tracking” = Yes); ADV:115; ADV:150
- **Probléma:** A SLIDE 1–2 önbevallós kérdései érzelmi önjellemzést kérnek (pl. „Kicsit feszült vagyok tőle”, „Eléggé összezavar”). A tartalék megvalósítás választós H5P-elem, minden opciót helyesnek jelölve. A H5P-C profil bekapcsolt próbálkozás-rögzítése mellett ez a választ fiókhoz kötve rögzíti. A forrás ezt nem zárja ki, és tárolási szabályt sem rendel hozzá.
- **Bizonyíték:**
  - M1.1:204: „ha mégis választós H5P-elem kell, minden opciót helyesnek kell jelölni, és ezt a runtime acceptance igazolja.”
  - ADV:150: „**saját önreflexió:** ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség.”
- **Hatás:** Ha a build ezt az utat választja, a tanulók érzelmi önjellemzése a próbálkozás-riportban a nem szerkesztő tanárnak is látszik (ADV:115). Az M2.1 hasonló kérdésénél a kánon ezt kifejezetten kezeli (RA:101); itt nincs ilyen szabály.
- **Javaslat:** EMBERI DÖNTÉS. Gazda: projektgazda; utólagos ellenőrzés: DPO/jogi felelős, a HUM-PRIV-01 szerint. Kérdés: tárolható-e fiókhoz kötve az M1.1 SLIDE 1–2 önbevallós válasza? Ha nem, a választós tartalékút csak kikapcsolt próbálkozás-rögzítéssel, vagy csak az elsődleges, szöveges úton (M1.1:204 első mondata) valósulhat meg. A döntésig a szöveg nem változik.
- **Típus:** emberi-döntés
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A forrás elsődleges útja (szöveg és Tovább gomb) nem rögzít választ. Hogy a build ténylegesen melyik utat használja, azt a CC-06 ellenőrzi.
- **Hipotézis:** új

**IMPL-G1-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** M1.1:344
- **Probléma:** A SLIDE 2 pontozatlan emoji-skálájánál a „(Completion, …)” jelölés completion-elemnek nevezi a választót. Ez ellentmond a D-d/D-i elvnek és a H5P-C profilnak.
- **Bizonyíték:**
  - M1.1:344: „(Completion, nincs jó/rossz. Megvalósítás: mint az 1. dia önbevallós kérdésénél – pontozott választós típusba nem kerülhet.)”
  - MAN:16: „A pontozatlan választók nem önálló completion-elemek”
- **Hatás:** A fejlesztő a hangulatskálát completion-feltételként vagy rögzített elemként építheti be.
- **Javaslat:** „(Completion, nincs jó/rossz.” helyett „(Nem completion-elem, nincs jó/rossz.” (D-i, HUM:561). A mondat többi része változatlan. Ha a zárójel szerepel a látható-szöveg pinekben, `--pin-visible` kell.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. Fejlesztői megjegyzés; a pontozatlan elem nem gate-eli a lecke completionjét (MAN:16).
- **Hipotézis:** új

**IMPL-G1-7**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** HUB:81 és HUB:86, összevetve: M1.1:51, M1.1:100, M1.1:857–912
- **Probléma:** A modulhub szerint az M1.1 „6–8 slide” hosszú, és a Check „1 nyitott kérdés”. A lecke 6 diás, a Check pedig 3 zárt kvízkérdés (2 Single Choice és 1 igaz/hamis), nyitott kérdés nélkül.
- **Bizonyíték:**
  - HUB:81: „H5P Course Presentation (6–8 slide, beépített kérdések)”
  - HUB:86: „Check: 1 nyitott kérdés arról, milyen visszajelzés segített már neki.”
  - M1.1:100: „Összesen **6 slide**.”
- **Hatás:** A hubból dolgozó fejlesztő vagy képző egy második szabad szöveges mezőt várhat vagy építhet az M1.1-be, tárolási szabály nélkül. Pont abba a leckébe, amelynek egyetlen szöveges lépése az N-M1-04 szerint tanuló-lokális.
- **Javaslat:**
  - HUB:81: „(6–8 slide, …)” helyett „(6 slide, …)”.
  - HUB:86: „Check: 3 rövid kvízkérdés (2 Single Choice + 1 igaz/hamis)”.

  Javítási korlát: a 4. kimeneti kompetencia (HUB:36) és a támogató tartalmak listája nem változik.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A build forrása a lecke (MAN:45, „Forrás” oszlop); a hub leírása sem completion-, sem adatkezelési szabályt nem ad.
- **Hipotézis:** új

**IMPL-G1-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** M1.2:797; M1.2:741–791; M1.2:970; A11Y:33
- **Probléma:** A SLIDE 5 Drag & Drop-ot használ, a hozzáférhetőségi sztenderd által előírt indoklás nélkül. A kötelező húzásmentes utat nem köti konkrét típushoz. A felsorolt „legördülő” változatot a h5p-course-presentation semantics.json beágyazható típusai között egyik sem adja.
- **Bizonyíték:**
  - A11Y:33: „Ha valahol mégis Drag & Drop kell, azt a lecke fejlesztői megjegyzésében indokolni kell”
  - M1.2:797: „kattintásos/kijelölős párosítás, kártyánként egy **legördülő** / rádiógombos kategória-választás”
  - h5p-course-presentation semantics.json (master): a beágyazható típusok között ott van a „H5P.MultiChoice 1.16”, a „H5P.DragQuestion 1.15” és a „H5P.Blanks 1.14”, de legördülő választós típus nincs.
- **Hatás:** A fejlesztő CP-n belül nem megvalósítható vagy nem igazolt típust választhat. Az LMS-M1-02 „drag-free egyenértékű út kötelező” követelménye így csak a buildnél dől el.
- **Javaslat:**
  - M1.2:797-ben az alapértelmezett húzásmentes típus: kártyánként H5P Multiple Choice „Single Choice (Radio Buttons)” módban, mint az M1.2:183-ban (az A11Y:31 szerint ez tipikusan húzásmentes). Az opciónkénti visszajelzés az M1.2:775–784 mondataiból jön.
  - A „legördülő” változat csak ezzel a feltétellel maradjon: „ha a célverzió CP-be ágyazható típusa igazoltan adja”.
  - A Drag & Drop megtartásának indokát ne a `/course-fix` fogalmazza meg. Ha a szerző nem ad indokot, a hozzáférhetőségi gazda dönt.

  Javítási korlát: a kártyák, a kategóriák és a besorolási kulcs (M1.2:754–759) változatlanok; a „mindig, nem feltételesen” követelmény nem gyengül.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A húzásmentes út már kötelező, és egy megvalósítható változata (a rádiógombos) fel van sorolva.
- **Hipotézis:** új

**IMPL-G1-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** M1.1:549–551 (@asset M1.1-ILL-02), összevetve: M1.1:621 és :952; M1.1:687–689 (@asset M1.1-IKO-02); M1.2:270–272 (@asset M1.2-IKO-01)
- **Probléma:** Több elem akadálymentesítési besorolása önellentmondó:
  - A példa-grid (M1.1-ILL-02) „decorative”, alt-derivatíva nélkül, pedig a lecke checklistje szerint a példa-grid alt-szöveget kap.
  - Az M1.1-IKO-02 és az M1.2-IKO-01 „informative”, a saját megjegyzésük szerint viszont dekoratív, és üres alt is elég.
- **Bizonyíték:**
  - M1.1:549: `"visual": "decorative",`, összevetve az M1.1:952-vel: „Minden tartalmat hordozó ábra/animáció (Johari-grafika, példa-grid) kap szöveges ekvivalenst (alt-szöveget)”
  - M1.1:689: „Dekoratív → üres alt elegendő; ha tartalmi jelzésnek szánják, rövid alt”
- **Hatás:** A média-manifestből dolgozó gyártó nem tudja eldönteni, kell-e alt-szöveg. A képernyőolvasós tanuló vagy felesleges ikonleírást hall, vagy hiányzik az ekvivalens.
- **Javaslat:**
  - M1.1:952 pontosítása az M1.1:621-hez: „a példa-grid mezőcímkéi és példamondatai valódi szövegként (SLIDE 4), a díszítő ikonok üres alttal”. A szöveges ekvivalens követelménye nem gyengül.
  - Az M1.1-IKO-02 és az M1.2-IKO-01 `note`-ja igazodjon az `informative` besoroláshoz (rövid alt kötelező); a derivatívát ne töröld.
  - Utána `python3 tools/media_manifest.py build`; a generált kimenetet kézzel ne szerkeszd.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A díszítő illusztráció a pilotban opcionális (PILOT-4), a grid szövege valódi szöveg (M1.1:621).
- **Hipotézis:** új

**IMPL-G1-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** M1.2:30–44 (Moodle intro); M1.2:39; összevetve: M1.1:76–90 és M1.1:85
- **Probléma:** Az M1.2 Moodle-intrója kódblokkban áll, ezért a címsor, a félkövér és a lista jelölése szó szerint kerülhet a Label-be. A Glosszárium-hivatkozás link nélküli, míg az M1.1 ugyanezt idézetblokkban, linkkel adja.
- **Bizonyíték:**
  - M1.2:30–31: a „```” kerítés után a „### M1.2 – Megfigyelés ≠ értelmezés” sor következik.
  - M1.2:39: „nézd meg a **Glosszáriumot**”, szemben az M1.1:85-tel: „nézd meg a [Glosszáriumot] (../../../Glosszárium%20–%20someres%20és%20pedagógiai%20fogalmak.md)”
- **Hatás:** A Label-ben „###” vagy „**” jel jelenhet meg, vagy hiányozhat a címsor (A11Y:37: minden H5P elé címsor kell az aktivitás nevével). A tanuló nem éri el egy kattintással a Glosszáriumot.
- **Javaslat:**
  - A :30 és a :44 kódkerítés megszüntetése; a blokk az M1.1:76–90 formáját kapja (címsor és idézetblokk).
  - M1.2:39: a „**Glosszáriumot**” helyére az M1.1:85 relatív linkje kerül.

  Javítási korlát: az intro szövege és a „Ha ez a téma téged is érint” blokk szó szerint változatlan.
- **Típus:** objektív
- **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. Formázási és navigációs eltérés, nem blokkolja az előrehaladást.
- **Hipotézis:** új

---

**Elvetett hipotézisek**
- **N-M1-04 (MTX:48–50, :243, :356, :1130), M1-02 (:1030), X-06 (:1059):** elvetve a „nyitott emberi döntés: tárolja-e a pilot-build” keret, mert a projektgazda 2026-10-10-én döntött (a fő session közvetítésével). A „vagy a mező előtt tájékoztatni” alternatíva (MTX:50) nem fér össze a „központi tárolás nélkül” döntéssel. A tartalmi hiányt viszont megerősítettem: IMPL-G1-1…4.
- **N-M1-04, tanulói megosztás-kapcsoló (MTX:243):** tárgytalan, mert központi tárolás nélkül nincs mit megosztani.
- **N-M1-03 / M1-01 (MTX:220, :300, :1029):** az implementációs lencsén elvetve. A SLIDE 3–4 átfedése pedagógiai finomítás; a „6 slide” szám, az asset-azonosítók és a narrációs hivatkozások a leckén belül konzisztensek.
- **CC-06 (MTX:1024):** nem finding. A 2026-10-10-i döntés 3. pontja szerint külön build/runtime feladat; a felépített kurzusról nem állítok semmit.
- **E-M1-002…E-M1-040 (a hubot, az M1.1-et és az M1.2-t érintő sorok):** nyelvi tételek, implementációs eltérést nem hordoznak.
- **M1-03, M1-04, N-M1-05…N-M1-11:** a 2. és 3. fájlcsoport hatóköre, itt nem vizsgáltam.

Források:
- [h5p/h5p-course-presentation semantics.json](https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/semantics.json)
- [Moodle MOODLE_405_STABLE mod/h5pactivity/lang/en/h5pactivity.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/lang/en/h5pactivity.php)


# IMPL-G2

## IMPL – M1, 2. fájlcsoport (KAPU, M1.3, M1.4) – implementációs lencse

A bizonyítékokban használt rövidítések (abszolút utak):
- KAPU = 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- M1.3 = 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- M1.4 = 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- RA = 02 Tervezet/LMS – H5P runtime acceptance.md
- ADV = 02 Tervezet/Adatvédelem – tanulói adatok és AI.md

Runtime-bizonyíték nincs. A felépített Moodle-kurzusról semmit nem állítok.

---

**IMPL-G2-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:303–305. Ellentmond neki: MAN:171 és MAN:248.
- **Probléma:** Az M1.4 (:547, :553) a KAPU §5-öt jelöli ki a Moodle-beállítás forrásaként. A KAPU §5 viszont nyitott, acceptance-teszten eldöntendő kérdésként kezeli a kapueredmény rögzítését. Sehol nem nevezi meg a már rögzített `GATE_CONFIRMED_M1`-et (LMS-M1-06, GATE-CP; BSPEC-01 RESOLVED, BS-D1), pedig az M3 KAPU:333 már erre köt. Az F-peula jelenléti útját egyenrangú opcióként adja, holott a MAN:248 szerint nincs F-peula-activity. A Moodle „további próbálkozás” módját sem rögzíti.
- **Bizonyíték:** KAPU:304 „(kézi „Teljesítve” jelölés, külön completion-feltétel, restrict access, vagy sor-szintű feltétel), a build **acceptance-tesztjén** dől el”. Ezzel szemben MAN:171: „**Tartalékút nincs** (BS-D1). … a két kézi completionös activity és az egyedi profilmező nem determinisztikus”.
- **Hatás:** Aki a KAPU alapján épít, kizárt utat választhat. A MAN:25 szerint egy kézzel „complete”-re állított bukó érték a kurzusteljesítésben teljesítettnek számít. A „további próbálkozás” módja nincs rögzítve. Ha valaki az „Automatically until pass”-t választja, a javító próbálkozás az F-peula előtt nyílik, és a nyers ponthoz kötődik. Ez sérti a KAPU:305 saját kikötését („akkor is meg kell nyitni, ha a nyers pontszám eléri az 5-öt, de valamelyik sor 0”).
- **Javaslat:** A KAPU §5 :303–305-öt a manifest szerint kell átvezetni:
  - a továbblépés a `GATE_CONFIRMED_M1` (LMS-M1-06, GATE-CP) Grade-feltételeihez kötődik („M1 megerősítve” / „M1 complete”, MAN §4), tartalékút nincs (BS-D1);
  - a célverziós bizonyíték az RT-P0-08;
  - a javító próbálkozáshoz kerüljön oda a MAN:248 mondata, ugyanígy a KAPU:24-ben és az M1.4 :21, :546, :647-ben;
  - rögzíteni kell, hogy a további próbálkozást kézzel kell megadni („Manually”). A docs.moodle.org/405 Assignment settings szerint: „Manually (via the Submissions page or Grader page), Automatically (after grading), or Automatically until pass”.
  - Tilos módosítani: küszöb, rubrika, próbálkozásszám, F-peula-kötelezettség.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Forrásszintű inkonzisztencia; a build-szerződés a manifest, ezért nem freeze-kivételes tanulói hiba.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/LMS – activity manifest.md:50 (LMS-M1-05) és :20 (ASSIGN-M); érinti még: KAPU:297–301 és M1.4:542–553.
- **Probléma:** Az LMS-M1-05 saját Moodle activity-completion beállítása sehol nincs rögzítve:
  - az ASSIGN-M profil egyetlen cellába vonja össze a leadást és a megerősített kapueredményt;
  - a BSPEC-07 kétállapotú mintája a D-f szerint csak azokra az utakra szól, ahol a manifest nem ad megerősítő checkpointot (gyakorlatilag az ASSIGN-S sorokra);
  - a KAPU §5 és az M1.4 §3.2 csak a Grade to pass = 5-öt írja elő.
- **Bizonyíték:** MAN:50 „| ASSIGN-M | igen | M1.4 + M1 KAPU | LMS-M1-04 | leadva + megerősített kapueredmény |”. MAN:25: „a beállított Grade to pass … miatt a „Még nem teljesítve” „complete, fail” … a kurzusteljesítés activity-kritériumát csak a „complete, pass” teljesíti”.
- **Hatás:** Az LMS-M1-05 kurzusteljesítési kritérium (MAN:165). Ha a completionje jegyalapú, a Grade to pass = 5 visszahozza a nyers pontot:
  - 2/2/1/0 = 5-nél az Assignment állapota „complete, pass”, miközben a kapu „Még nem teljesítve”;
  - egy későbbi, önkéntes, gyengébben pontozott újrabeadás „complete, fail”-re ronthatja. A gradebook viselkedését az RT-P0-19 vizsgálja.
  - Ez ütközik a „legjobb megerősített eredmény” szabályával (KAPU:306), és a D-h szerint a két állapot nem mosható össze.
- **Javaslat:** EMBERI DÖNTÉS (projektgazda / build-spec gazda). Kérdés: kiterjeszthető-e a D-h kétállapotú mintája az ASSIGN-M sorokra (LMS-M1-05, ugyanígy M3/M5/M6/M7)? Javasolt minta:
  - SUBMITTED: „Make a submission” (`completionsubmit`), a jegyalapú completion kikapcsolva;
  - CONFIRMED: LMS-M1-06;
  - rögzítés a MAN LMS-M1-05 sorában és a KAPU §5-ben.
  - Ez a D-f hatókörén túli új alkalmazási eset. Amíg nincs döntés, BSPEC-sorként kell nyilvántartani; ez a `MOODLE-BUILD-VERDICT`-et is érinti.
  - Tilos módosítani: Grade to pass = 5, Maximum grade = 8, a konjunkciós küszöb.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT. A pilot M1-előrehaladását a GATE-CP (LMS-M1-06) vezérli; az LMS-M1-05 completionje a kurzusteljesítést érinti.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-3**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:502; mellette M1.3:926 (LMS-M1-07); ADV:117 és :230.
- **Probléma:** Az M1.4 tanulói mondata szerint a kapubeadást csak a kijelölt mentor/értékelő látja. Az ASSIGN-M profilhoz azonban nincs rögzített szűkítő mechanizmus: a Moodle-alapértelmezés szerint minden nem szerkesztő tanár csoporttól függetlenül látja, a szűkítés pedig nyitott DPO-kérdés (BIZT-5). Az RT-P0-15 visszaolvasása sem az LMS-M1-05-re, sem a TEXT-C-s LMS-M1-07-re nem futott.
- **Bizonyíték:** M1.4:502 „A beadásodat a kijelölt mentorod/értékelőd látja (és ha újraértékelést kérsz, a második képző is).” ADV:117: „| ASSIGN-S, ASSIGN-M, GATE-CP | … nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) |”.
- **Hatás:** Ha a pilot-kurzusban több nem szerkesztő tanár van, a P2 kapubeadványról szóló tájékoztatás valótlan (HUM-PRIV-01: legszűkebb hozzáférés).
- **Javaslat:** Tartalmi szerkesztés nem kell. Kell:
  - a G2 / RT-P0-15 bizonyítéka az LMS-M1-05-re, az LMS-M1-06-ra és az LMS-M1-07-re (két mentor, két csoport, tesztfiókkal);
  - a BIZT-5 DPO-döntése (ADV:230: a tájékoztató DPO-jóváhagyás előtt nem élesíthető).
  - Teszt előtt a mondatot ne írd át és ne töröld.
- **Típus:** bizonyíték-kapu (RT-P0-15; G2, G3b)
- **Pilot-besorolás:** POST-PILOT. Nem freeze-kivételes tartalmi hiba, de a bizonyíték a PILOT-1 szerinti M0+M1 GO-evidence lista része. Ha a stagingteszt szerint más mentor is látja a beadást, az már P0 adatvédelmi freeze-kivétel.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-4**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:496–500; KAPU:303–306; RA:129, :136, :137, :147.
- **Probléma:** Az M1.4 tanulói ígéretei a GATE-CP és a próbálkozás-kezelés célverziós működésén múlnak:
  - az M2 a megerősítéssel nyílik, „Még nem teljesítve” esetén is;
  - az M3-kapu csak sikeres eredménnyel nyílik;
  - a javító próbálkozás csak az F-peula után nyílik;
  - a megerősített teljesítés önkéntes újrabeadástól nem vész el.
  Az RT-P0-01, -08, -09 és -19 állapota mégis `IMPLEMENTATION_TEST_REQUIRED`.
- **Bizonyíték:** M1.4:496 „Az M2 leckéi akkor nyílnak meg, amikor a képződ a rubrika alapján megerősítette az eredményedet – akkor is, ha az eredményed „Még nem teljesítve”.” RA:136: „| RT-P0-08 | `IMPLEMENTATION_TEST_REQUIRED` | 8. Összetett (konjunkciós) kapuk kikényszerítése |”.
- **Hatás:** Igazolás nélkül a pilot M1-kapujánál rossz nyitás vagy beragadt előrehaladás jöhet elő. Ilyen eset például a 0/1/2/2 = 5, vagy egy F-peula előtt induló javító próbálkozás.
- **Javaslat:** Tartalmi szerkesztés nem kell. A célverzión, dátummal és verzióval kell futtatni:
  - RT-P0-08: az M1 0/1/2/2 negatív esete és a GATE-CP állapotmátrix;
  - RT-P0-19: ASSIGN-M javító beadás nem indítható az F-peula előtt; kézi nyitás; a legjobb megerősített eredmény számít;
  - RT-P0-01: visszaolvasás, Maximum grade = 8, Grade to pass = 5;
  - RT-P0-09: a LMS-M1-03 → -07 → -04 → -05 nyitási lánc.
- **Típus:** bizonyíték-kapu (G3b)
- **Pilot-besorolás:** POST-PILOT. Nem freeze-kivételes tartalmi hiba; a bizonyíték a PILOT-1 szerinti M0+M1 GO-evidence lista része.
- **Hipotézis:** új (a CC-06 csak a felépített kurzus összevetését fedi, nem ezt)
- **Verdikt:** —

**IMPL-G2-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:298; M1.4:478–487 (főleg :482) és :585 a KAPU:55-tel szemben; MAN:50.
- **Probléma:** A beadás előtt két forrásból látszhat rubrika: az M1.4 3.1 Assignment-leírásának táblázatából és a KAPU §5 szerint bevitt Moodle-rubrikából. A build-spec nem rögzíti a rubrika tanulói megjelenítési opcióit, a két szöveg nem azonos, és a tanulói láthatóságra nincs RT-tétel. Az RT-P0-01 csak a Max grade és a Grade to pass értékét olvassa vissza.
- **Bizonyíték:** M1.4:482 „Kiderül, mikor, hol és melyik helyzetben történt.” KAPU:55: „Érthető a **konkrét alkalom**: idő ÉS/VAGY hely ÉS a helyzet szakasza azonosítható.” Webforrás: Moodle `gradingform_rubric.php` (MOODLE_405_STABLE): „Allow users to preview rubric (otherwise it will only be displayed after grading)”; `lib.php` `get_default_options()`: „'alwaysshowdefinition' => 1,”.
- **Hatás:** A Moodle-alapértelmezés bekapcsolt előnézet. Ilyenkor a tanuló a beadás előtt két eltérő S-„Erős” horgonyt lát. Ha az építő kikapcsolja az előnézetet, a tanuló értékelés után más szöveget kap vissza, mint amit a beadás előtt látott. A hivatalos szöveg a KAPU-é (M1.4:553).
- **Javaslat:**
  1. A KAPU §5 :298-ban és az LMS-M1-05 megjegyzésében rögzíteni: „Allow users to preview rubric” = Yes és „Display rubric description to those being graded” = Yes.
  2. Az M1.4 :482-es (és :585-ös) S-sor „Erős” celláját a KAPU:55 horgonyához kell igazítani; a hivatalos szint nem változik.
  3. Az RT-P0-01 kapjon egy sort: tanulói fiókkal a rubrika a beadás előtt látható (G3b).
  - Tilos módosítani: szintek, pontok, küszöb, sorszám, KAPU-szöveg.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Megfogalmazásbeli széttartás, nem blokkoló; a Moodle-alapértelmezés a rubrikát a beadás előtt amúgy is mutatja.
- **Hipotézis:** M1-03 (N-M1-06, -07, -09, -11). Részben megerősítve: a leírás-táblázat a beadás előtt látható. Részben elvetve: a horgonyok nem azonosak, és a rubrika-opció már a forrásban sincs rögzítve, tehát nem csak runtime-kérdés.
- **Verdikt:** —

**IMPL-G2-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:18, :153, :309, :655
- **Probléma:**
  - A mini-kvíz H5P-típusa nincs eldöntve („Course Presentation vagy Question Set”), pedig a Question Set nem tudja hordozni a nem kérdés jellegű diákat: a kártyákat a NAR-01-gyel, a diagramot a NAR-02-vel és az átvezetést a NAR-03-mal.
  - Az 1. dia pontozatlan kártyaválasztásának típusát a lecke a runtime acceptance-re bízza, de abban nincs M1.4-tétel.
  - A 3–5. dia „Single Choice” típusa sincs megadva.
- **Bizonyíték:** M1.4:18 „* **H5P mini-kvíz** (Course Presentation vagy Question Set) – 3 szituáció bemutatása + 3 kérdés”. M1.4:153 „…a megvalósítási típust a runtime acceptance rögzíti.” Webforrás: h5p/h5p-question-set `semantics.json`, a „questions” mező engedett könyvtárai: „H5P.MultiChoice 1.16, H5P.DragQuestion 1.15, H5P.Blanks 1.14, H5P.MarkTheWords 1.11, H5P.DragText 1.10, H5P.TrueFalse 1.8, H5P.Essay 1.5, H5P.MultiMediaChoice 0.3”. Az introPage csak címet, szöveget és háttérképet ad, hangot nem.
- **Hatás:** Question Set esetén elvész a narráció és a leirat (RA:102: „H5P Audio a Course Presentation dián”), és a MAN H5P-C szabálya („Hide summary slide” = No) nem alkalmazható. A kártyaválasztás két rossz irányba mehet:
  - pontozott elemként torzít (a Single Choice Setben az első opció mindig helyes, RA:80);
  - specifikáció nélkül épül, a kötelező billentyűzet-, fókusz- és 24×24 px-es követelmény ellenőrzése nélkül.
  A Single Choice Setben nincs kérdésenkénti visszajelzés.
- **Javaslat:**
  - :18 és :655: csak „Course Presentation”.
  - :153: konkrét megvalósítás. Például nem pontozott kártyák képként vagy szövegként, opcionálisan elemszintű „Specific slide number” ugrással a 3–5. diára (a CP semantics ezt a mezőt adja). Ki kell mondani, hogy nem completion-elem.
  - :309: „H5P Multiple Choice, Single Choice (Radio Buttons) mód”, ahogy az M1.3-ban.
  - Az RT-14 és az RT-A11Y-01 kapjon tesztsort az M1.4 1. diájára.
  - Tilos módosítani: kérdések, opciók, ✅, visszajelzések.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A PILOT-4 szerint a narráció a pilotban opcionális; a hiba építési kétértelműség, nem tanulói blokkolás.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-7**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md:444–446; MAN:49–50.
- **Probléma:** Az M1.4 a kapu-Assignment címeként a lecke címét adja meg. Ez majdnem azonos az LMS-M1-04 H5P-activity nevével, és eltér az Assignment manifest szerinti nevétől („M1.4 – SBI-beadandó”).
- **Bizonyíték:** M1.4:446 „> M1.4 – Miniszituációk: „Mondd el SBI-ben””. MAN:49–50: „| M1.4 – Mondd el SBI-ben | H5P-C |” / „| M1.4 – SBI-beadandó | ASSIGN-M |”.
- **Hatás:** A copy-paste leírásból két majdnem azonos nevű activity (kvíz és kapu) kerülhet egymás alá. A tanulói szöveg („beadtad az SBI-beadandót”, :27) nem a látható címre mutat, és képernyőolvasóval a kettő nehezen különíthető el.
- **Javaslat:** Az M1.4 §3.1 „Cím” sora legyen „M1.4 – SBI-beadandó” (MAN LMS-M1-05 „Név”); más szöveg nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Tanulói szöveg, nem blokkoló.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:28, :132, :308; MAN:8 és :45–51.
- **Probléma:** A KAPU a 10 itemes kísérő item-bankot külön Moodle Quiz vagy H5P Question Set activityként, completion-alapon építteti (két szabad szöveges itemmel). A manifest, amely csak tényleges activityket sorol, M1-ben ilyen sort nem tartalmaz: nincs build_id, profil, privacy-osztály és unlock.
- **Bizonyíték:** KAPU:308 „**A 3. szakasz item-bankja** külön Quiz/H5P Question Set, **completion-only**, NEM kötve a kapuhoz.” MAN:8: „A táblázat csak **tényleges Moodle-activityket** sorol.”
- **Hatás:** Ha az építő kihagyja, a KAPU Item 6 útja („ezt add be az M1.4 Assignmentbe”) üres marad. Ha manifest-sor nélkül építi meg, az Item 5–6 P2 szabad szövege adatleltár nélkül tárolódik, a completion-szerepe pedig tisztázatlan.
- **Javaslat:** EMBERI DÖNTÉS (projektgazda / LMS-gazda): Moodle-activity-e az item-bank, vagy képzői/önellenőrző forrás?
  - Ha activity: kapjon manifest-sort (build_id, nem kapuzó profil, privacy, unlock).
  - Ha forrás: a KAPU :28, :132, :308 ennek megfelelően módosul.
  - Tilos módosítani: itemek, kulcs, „NEM kapu” státusz.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT. A kapudöntést nem érinti.
- **Hipotézis:** új
- **Verdikt:** —

**IMPL-G2-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md:886; :1028–1029; MAN:48 (LMS-M1-07 unlock: LMS-M1-03).
- **Probléma:** A 6. dia most kér saját mini-SBI-t, és azt mondja, hogy a tanuló „másolja ki és mentse el”. A dián azonban nincs beviteli elem, és nincs megadva, hová írjon a tanuló most. Az LMS-M1-07 mező csak a lecke teljesítése után nyílik, a 7. dia önellenőrzése viszont már egy „saját mondatra” hivatkozik.
- **Bizonyíték:** M1.3:886 „💡 **Másold ki és mentsd el magadnak** ezt a mondatot – … A három részt a lecke után következő ‘M1.3 – Saját mini-SBI’ szövegmezőbe írd be.” Ezzel szemben az 5. dia, M1.3:799: „Írd le magadnak, jegyzetbe vagy papírra; nem adod be.”
- **Hatás:** A tanuló beviteli mezőt keres a dián. A 7. dia önellenőrzése és a lecke utáni beírás így nincs mire épüljön. A mező TEXT-C-be költöztetését (BSPEC-02, D-1) nem vezették át a tanulói útba.
- **Javaslat:** A 6. dia instrukciójában a „Másold ki” helyére kerüljön az 5. dia mintájára egy helymegjelölés, például: „Most írd le jegyzetbe vagy papírra; a lecke után a ‘M1.3 – Saját mini-SBI’ mezőbe írd be.” A NAR-05 narráció és a mezők változatlanok.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A beküldés a lecke utáni mezőben így is lehetséges; ez pontosítás, nem blokkoló hiba.
- **Hipotézis:** új (az E-M1-045 ugyanezt a mondatot csak nyelvileg érintette)
- **Verdikt:** —

**IMPL-G2-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:297; M1.4:542–544; MAN:24 (BIZT-1).
- **Probléma:** A kapubeadás online szöveges és fájlos útjához a build-spec nem rögzít „Accepted file types” értéket, feltölthető fájlszámot és szószám-határt. Közben a manifest maga rögzíti, hogy az Assignment online szövegszerkesztője fájlt is fogad.
- **Bizonyíték:** KAPU:297 „**Activity:** Assignment (M1.4) – Online text submission ✅ + File submission ✅”. MAN:24: „az Assignment online szövege erre nem alkalmas, mert a szerkesztője fájlt fogad (BIZT-1 …)”.
- **Hatás:** A kapuba csak kitalált SBI kerülhet (M1.4:457), mégis bármilyen kép vagy fájl feltölthető. Ez P2 adat, és sérti az adattakarékosságot. A fájlos út akadálymentessége (M1.4-MUNK-01) a formátumtól függ.
- **Javaslat:** A KAPU §5-ben az M1.4-MUNK-01-hez igazítva rögzíteni kell a „File submissions” mezőket, például „Accepted file types”: .docx, .odt, .pdf; „Maximum number of uploaded files”: 1. Az online szövegszerkesztő képfeltöltésének kezelése az LMS-gazda és a DPO kérdése (a BIZT-5 mellett). Tilos módosítani: a két út egyenértékűsége és a beadás tartalmi szabályai.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Adattakarékossági finomítás; a tanuló a kitalált helyzetet előíró instrukciót kapja.
- **Hipotézis:** új
- **Verdikt:** —

---

### Elvetett vagy módosított hipotézisek
- **M1-03 / N-M1-11:** Részben elvetve. A „csak runtime-kérdés” nem áll, mert a rubrika tanulói megjelenítési opciója már a forrásban sincs rögzítve (IMPL-G2-5).
- **N-M1-06:** Megerősítve. A leírás-táblázat (M1.4:478–487) a beadás előtt látható; a szövegeltérést lásd az IMPL-G2-5-ben.
- **N-M1-07:** Részben elvetve. A sornevek nem teljesen azonosak (M1.4:484 „Hatás (I) érthetősége” ↔ KAPU:67 „hitelessége / érthetősége”; KAPU:57 „(nincs címke)”). Ez kozmetikai eltérés, külön findingot nem ér.
- **N-M1-09:** Részben elvetve. Az S-sor „Erős” szintjén a horgonyok nem egyeznek a KAPU-val (IMPL-G2-5).
- **CC-06:** Nem vizsgáltam. A felépített kurzus összevetése a 2026-10-10-i döntés 3. pontja szerint külön build/runtime feladat.
- **M1a (12. szakasz):** Nem a 2. csoport hatóköre (M1.B, 3. csoport).
- **N-M1-04:** A KAPU, az M1.3 és az M1.4 nem hivatkozik az M1.1 SLIDE 5-re, és nem mond ellent a projektgazdai döntésnek. Az át nem vezetett döntés a MAN:45 és az RA:104 helyén az 1. csoport hatóköre.
- **„1–2 vs 2–3 mondatos” (a fő session hipotézise, nem mátrixtétel):** Mezőhosszt és validációt nem érint. Sem a KAPU §5, sem az M1.4 §3.2 nem ír elő szószám-határt, és a rubrika nem pontozza a hosszt. A tartalmi széttartás (M1.4:10, :426, :450 ↔ KAPU:21, :197; hub:33, :125) a pedagógia/értékelés lencse feladata.



# IMPL-G3

RÉSZLEGES: nem olvastam szó szerint az M0-belépőkvíz 7. tételét (Emberi jóváhagyás szükséges.md ≈469–473) az IMPL-G3-8-hoz. Elsődleges forrásból azt sem igazoltam, hogy új próbálkozás nyitása után a Moodle-ben értékelhető-e még a korábbi próbálkozás; ezért közepes az IMPL-G3-2 bizalma. A M1-HUB-POSZ-02 generált regiszterbeli státuszát sem néztem meg. Az E-M1-069 négysarkos A/B-maradványait és az online ↔ peula összhangot végignéztem.

Útvonalak:
- M1.A = 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- M1.B = 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- M1.F = 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- hub = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- MAN = 02 Tervezet/LMS – activity manifest.md
- PT = 02 Tervezet/Program terv.md

---

**IMPL-G3-1**
- Súlyosság: P1
- Bizalom: magas
- Lencse: implementáció
- Hely: M1.F:68, M1.F:397, M1.B:478
- Probléma: A peulák a javító próbálkozás második nyitási útjaként az „F-peula jelenléti completionjét” adják meg. A build-szerződés szerint ilyen activity nincs. A Moodle hozzáférési korlátozása ráadásul activity-szintű, egyetlen próbálkozást nem tud kapuzni.
- Bizonyíték: M1.F:68 „a hozzáférési feltétele az F-peula jelenléti completionje”; MAN:248 „a manifestben nincs külön F-peula-activity. Amíg a build nem hoz létre egyet (kézi completionnel jelölt jelenlét), a javító próbálkozást a képző nyitja meg felhasználói felülbírálással.” Moodle Docs 4.5, Restrict access: „The restrict access feature enables teachers to restrict the availability of any activity or even a course section according to certain conditions…”
- Hatás: A képző automatikus nyitásra várhat, és a hétfői F-peula meg a szerdai javító határidő között nem nyitja meg a próbálkozást. Ha valaki a teljes LMS-M1-05-re tenne korlátozást, az első beadás is elzáródna.
- Javaslat: Az M1.F:68, :397 és az M1.B:478 igazodjon a MAN §7:248-hoz. A pilot-buildben a javító próbálkozást a képző nyitja meg a peula után (Assignmentnél „Allow another attempt”). A „jelenléti completion” út csak külön F-peula-activity és igazolt runtime acceptance 19. pont mellett maradhat. Tilos: az „1 normál + 1 javító” és az „F-peula után nyílik” szabály módosítása. Ugyanez a próbálkozás-szintű megfogalmazás a kánonban is áll (MAN §1/§3, RT 19, hub:257, KAPU §5:305); az a 2. csoport és a manifest scope-ja.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. A képzői ellenőrzőlista (:397 „megnyitom”) alapértelmezésként a ma működő utat írja elő, ezért tényleges blokkolás nem bizonyított.
- Hipotézis: új (rokon a mátrix GEN-mellékmegfigyelésével, PT:219 ↔ MAN:248)
- Verdikt:

**IMPL-G3-2**
- Súlyosság: P1
- Bizalom: közepes
- Lencse: implementáció
- Hely: M1.B:476, M1.B:478, M1.F:270, M1.F:276
- Probléma: A peulák finomításhoz „új próbálkozást” kérnek az M1.4 Assignmentben. Az M1.B-n ezt olyan tanuló is kérheti, akinek a kapueredménye még függőben van (a beadás az M1.B előtt esedékes, hub:8). A „1 normál + 1 javító + további kézzel” csak akkor építhető meg, ha az „Allowed attempts” értéke 2-nél nagyobb vagy korlátlan, ezt viszont sem a MAN ASSIGN-M profilja, sem az M1.4 3.2 nem rögzíti.
- Bizonyíték: M1.B:476 „kérd meg a képződet, hogy nyisson neked **új próbálkozást** az `M1.4` Assignmentben”; Moodle Docs 4.5, Assignment settings: „Allowed attempts: The maximum number of attempts that can be made. Once this number is reached, the submission can no longer be reopened.”
- Hatás: Ha a build szó szerint 2 próbálkozást állít be, az M1.B utáni finomítás elhasználja a javító helyet. Bukás esetén az F-peula utáni javító próbálkozás nem nyitható, és elakad az M1 completion. Függő eredménynél a finomítás megkerüli a lezárt szabályt is: éles kapunál a javító próbálkozás az F-peula után nyílik (MAN:149, projektgazdai döntés, 2026-10-02).
- Javaslat: Az M1.B:476 hurokzárása és a :478 jegyzet szűküljön a már megerősített „Teljesítve” eredményre (KAPU §5:306 „pl. az M1.B után”). Mondja ki, hogy függő eredménynél a képző nem nyit új próbálkozást. A próbálkozásszám (Allowed attempts korlátlan vagy legalább 3, Grant attempts = Manually) a MAN ASSIGN-M profiljában és az M1.4 3.2-ben pótolandó; ez a 2. csoport és a manifest scope-ja, a runtime acceptance 19. pontjával igazolandó. Tilos: a küszöb, a próbálkozás-logika és a „legjobb megerősített eredmény” módosítása.
- Típus: objektív (a peula-oldal). A runtime-igazolás bizonyíték-kapu: G3b.
- Pilot-besorolás: POST-PILOT a peula-szövegre. A blokkolás a build-beállításon múlik: ha a staging LMS-M1-05 „Allowed attempts” értéke 2, az a tanulói előrehaladást blokkolja. Ezt a manifest scope-jában PILOT-BLOCKER-jelöltként kell vizsgálni.
- Hipotézis: új
- Verdikt:

**IMPL-G3-3**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: M1.B:148, :214, :218, :241, :495; @asset M1.B-KART-02 :69 (purpose) és :86 (notes)
- Probléma: A mini-kvíz négysarkos (A/B/C/D). A tér-előkészítés, az ellenőrzőlista és az asset-metaadat viszont A/B, illetve igaz/hamis sarkot ír. A MAG-lista 4. kérdés-címkéje nem a mai 4. kérdést írja le. A KART-02 a 3 smiley-t ajánlja sarokjelölésre, pedig 4 sarok van, és sarokjelölő az eszközlistában sincs.
- Bizonyíték: M1.B:214 „Használj **A/B/C/D sarkot** vagy „igaz/hamis” mozgást.” ↔ M1.B:495 „Van hely mozogni A/B sarkok között.” (ugyanígy :86 „…mini-kvíz A/B/igaz-hamis sarkainál is.”; :218 „4. kérdés (melyikből tudsz javítani?)” ↔ :241)
- Hatás: A képző két sarkot készít elő. Így a négyválaszos 1., 2. és 4. kérdés nem játszható le, a 3 smiley pedig nem jelöl 4 sarkot.
- Javaslat: Látható szöveg, Edit-tel, utána egyszer `--pin-visible "E-M1-069: …"`: a :148 legyen „A/B/C/D sarok, igaz/hamis”, a :495 „A/B/C/D sarkok”, a :218 címkéje igazodjon a :241 kérdéséhez. Metaadat: a leckefájlbeli @asset-blokk a kánoni forrás, Edit-tel kézzel szerkeszthető, és a látható ujjlenyomatot nem érinti, ezért ehhez pin nem kell. A :69 és a :86 ne rendelje a smiley-kat A/B/C/D sarokjelöléshez. Ezután `python3 tools/media_manifest.py build`, a generált assetek.csv és _build JSON külön chore(media) commitban. A ✅-ok, a kérdések és az opciók változatlanok.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. Nem biztonsági és nem blokkoló hiba; a képző helyben alkalmazkodhat.
- Hipotézis: E-M1-069; M1b (M1.B:86)
- Verdikt:

**IMPL-G3-4**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: M1.B:192, :203 ↔ M1.B:70, :74 (@asset KART-02), :140–143, :186, :491
- Probléma: A ráhangolóban minden résztvevő kétszer felmutat egy smiley-kártyát. Az eszközlista és az asset-spec viszont csak 3 db nagy, képzői kártyát ír elő; fejenkénti készlet nincs.
- Bizonyíték: M1.B:192 „háromra emeljétek fel azt a kártyát, ami leginkább tükrözi, hogyan érkeztetek meg”; M1.B:74 „Nagy formátum (A4/karton), 3 db”
- Hatás: Az előkészítés 3 kártyát gyárt, a két fejenkénti felmutatás eszköz nélkül marad.
- Javaslat: Az eszközspec igazodjon a megtartott (E-M1-069 VALID_IMPROVEMENT) instrukcióhoz: fejenként egy kis 3 smiley-s szett 8–20 főre, plusz a 3 nagy képzői kártya. Látható sorok: :140–143 és :491 (pin kell). Metaadat: :70 spec és :74 technical (Edit, majd build). Ha inkább az instrukció változna (pl. kézjelre), az szerzői döntés, nem e javítás része.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. Háromperces ráhangoló, nem blokkol.
- Hipotézis: M1a (M1.B:192/:203 ↔ :70/:140), igazolva
- Verdikt:

**IMPL-G3-5**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: hub:172–203 (@asset M1-HUB-POSZ-02), hub:221–222 ↔ M1.F:82, :84–86, :115, :209, :379
- Probléma: A hub generate módú „Közös fogalom-térkép” posztert ír elő (R1, R5, print-pdf), és a részleteket az M1.F-be utalja. Az M1.F egyik blokkja sem épít fogalom-térképet: a 25–40’ Q&A és rövid magyarázat. Az M1.F-MUNK-01 notes (:209) szerint a Blokk 3 táblaábrái nem külön gyártandó assetek. Az M1.F:82 és :379 mégis említi a fogalom-térképet. A hub:221 jegyzetlapja „leckénként 1 gondolat, 1 kérdés”, az M1.F:84–86 szerint egy mondat és egy kérdés összesen.
- Bizonyíték: hub:196 „"notes": "Részletek az M1.F peula-fájlban."”, hub:222 „25–40’ – Közös fogalom-térkép” ↔ M1.F:115 „**25–40’** – Kérdések–válaszok + rövid magyarázat”
- Hatás: Forrás nélküli nyomtatvány kerül a gyártási tervbe. A hubból készülő képző mást vezet, mint amit a peula leír.
- Javaslat: A hub igazodjon az M1.F-hez: a hub:222 kövesse az M1.F:115-öt, a hub:221 legyen „1 mondat + 1 kérdés”. A M1-HUB-POSZ-02 kapjon `reuse` módot az M1.F-MUNK-01-re, vagy kerüljön törlésre (metaadat: Edit, majd build). Az M1.F:82 és :379 „fogalom-térkép” helyett a Blokk 3 mini-összegzésére (:340–343) utaljon (látható, pin kell). Ha a fogalom-térkép tevékenységet meg akarják tartani, az szerzői döntés.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. Az M1.F csak kapusikertelenség után fut, és nem blokkol.
- Hipotézis: új
- Verdikt:

**IMPL-G3-6**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: hub:146–151 ↔ M1.A:168–173, :217, :270–274
- Probléma: A hub M1.A-percbontása eltér a peulától: más a ráhangoló témája, mások az idősávok (játék 15–30’ ↔ 20–32’), és „példák a 4 mezőre”. A peula szándékosan csak a Nyitott és a Rejtett mezőt nyitja meg.
- Bizonyíték: hub:148 „5–15’ – Nagy Johari-ablak megrajzolása, példák a 4 mezőre.” ↔ M1.A:270 „A ‘Vakfolt’ és az ‘Ismeretlen’ mezőt most békén hagyjuk.”
- Hatás: A hubból készülő képző élesben gyűjthet vakfolt-példát, holott a peula ezt egy későbbi, bizalmibb fázisra hagyja (M1.A:273–274).
- Javaslat: A hub §4 „Peula A” percbontása az M1.A 3. szakasza szerint frissüljön, 6 sávval; a 2. pont legyen: „példák a Nyitott/Rejtett mezőre; a Vakfolt és az Ismeretlen ma üres marad”. Látható hubszöveg, ezért pin kell. A peula változatlan.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. A képző a részletes peulából dolgozik; nem P0.
- Hipotézis: új
- Verdikt:

**IMPL-G3-7**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: hub:275–278 ↔ M1.B:167, M1.B 4.4 (:431–472)
- Probléma: A hub analitikája az M1.B végére egyperces, név nélküli kérdést ír elő (1–5-ös skála és „Mi az, ami még zavaros?”). Az M1.B zárása ezt nem tartalmazza, és gyűjtési csatorna sincs (papír vagy Moodle-elem; Moodle-elemhez manifest-sor sincs).
- Bizonyíték: hub:276 „M1.B végén 1 perces, név nélküli kérdés:” ↔ M1.B:167 „**40–45’** – Zárás & terepre kapcsolás: 1 mondatos madrih-vállalás”
- Hatás: A hub által várt offline visszajelzési adat nem keletkezik.
- Javaslat: EMBERI DÖNTÉS (szerző, programvezető): megmarad-e a kérdés. Ha igen, a meglévő 40–45’ sávon belül, papíron és név nélkül kerüljön az M1.B 4.4-be (a 45’ keret nem változik). Ha nem, a hub:275–278 törlendő.
- Típus: emberi-döntés
- Pilot-besorolás: POST-PILOT. Analitikai hiány, a tanulót nem érinti.
- Hipotézis: új
- Verdikt:

**IMPL-G3-8**
- Súlyosság: P2
- Bizalom: közepes
- Lencse: implementáció
- Hely: PT:219; MAN:114–129, :133, :248; M1.F:65
- Probléma: A PT minden modulban „Peulák” és „Extra / F-peula” Moodle-blokkot ír elő. A build-szerződés M1-re egyiket sem rendeli el (a peula nem activity, F-peula-activity nincs). A kötelező M1.F helye és időpontja (M1.F:65 „a képző jelöli ki”) így a Moodle-ben nem jelenik meg.
- Bizonyíték: PT:219 „minden modulon belül: „Online mikroleckék”, „Peulák”, „Modul-kapu”, „Extra / F-peula”.”; MAN:248 „a manifestben nincs külön F-peula-activity.”
- Hatás: A PT és az M0 ígérete (a peulát a Moodle-ben találod) az M1-ben nem teljesül. A kötelező F-peula közlése teljesen a képzőn múlik.
- Javaslat: A MAN „Kurzusszintű elemek” (:114–129) szakasza M1-re kapjon „Peulák” (M1.A, M1.B) és „Extra / F-peula” (M1.F) leíróelemet: nem activity, cmid és completion nélkül (a mátrix N-GEN-09 teendője). A leírás tartalmát („mire készülj”) az N-M4-07 döntéséig nem szabad kitalálni. Az M1 tanulói szövege nem változik.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. Nem blokkol: az F-peula időpontját a képző közli, a kvíz diagnosztikus.
- Hipotézis: N-GEN-09 (X-01)
- Verdikt:

**IMPL-G3-9**
- Súlyosság: P2
- Bizalom: magas
- Lencse: implementáció
- Hely: M1.F:171–172
- Probléma: A kemény sortörés két sorvégi szóköz, nem `\`, ellentétben a `.claude/rules/course-content.md` „Kemény sortörés” szabályával.
- Bizonyíték: M1.F:171 „> Mindegyikhez válassz egy betűt – **csak magadnak**:␣␣”; M1.F:172 „…**D)** elakadtam, segítség kell.␣␣” (␣ = szóköz)
- Hatás: A sort szerkesztő következő PR-ban a CI `git diff --check` bukik; ha a szóközt valaki eltávolítja, a felsorolás egy sorba olvad.
- Javaslat: A két sorvégi szóköz helyére `\` kerüljön (a :173 ugyanabban az idézetbekezdésben folytatódik, ezért a `\` sortörésként működik). A fájl szövege változik, ezért egyszer `--pin-visible` kell.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. A megjelenítés ma helyes.
- Hipotézis: M1b (M1.F:171–172), igazolva
- Verdikt:

**IMPL-G3-10**
- Súlyosság: P2
- Bizalom: közepes
- Lencse: implementáció
- Hely: M1.A:365–366 (4.3.1), M1.B:148, :214 (4.1.2)
- Probléma: A két mozgásos játék helyváltoztatással kér választ, és nincs helyből adható egyenértékű jelzés annak, aki nem tud vagy nem akar mozogni. A hozzáférhetőségi sztenderd a peulákra is vonatkozik (sztenderd:3), de mozgásra vonatkozó szabálya nincs.
- Bizonyíték: M1.A:365 „Ha megfigyelésnek érzed, menj a MEGFIGYELÉS-oldalra,”; M1.B:214 „Használj **A/B/C/D sarkot** vagy „igaz/hamis” mozgást.”
- Hatás: Mozgásában korlátozott résztvevő kimarad, vagy feltűnővé válik a játékban.
- Javaslat: Mindkét blokkba egy facilitációs mondat: aki nem tud vagy nem akar helyet változtatni, a helyéről jelez (betűs vagy ikonos lappal, illetve kézjellel), és ez egyenértékű. Új policy nem kerül be. Látható szöveg, ezért pin kell.
- Típus: objektív
- Pilot-besorolás: POST-PILOT. Nem P0 hozzáférhetőségi hiba; a képző helyben alkalmazkodhat.
- Hipotézis: új
- Verdikt:

LEVÁGVA: 3 további finding, súlyosságuk: 3×P2
- IMPL-G3-11 · P2 · M1.F:47 ↔ hub:258: „Létszám: 6–20 fő”, holott az F-peula kötelezően csak a kaput nem teljesítőknek szól („egyéni vagy kiscsoportos támogatás”). 1–3 fős alkalomra nincs instrukció: a név nélküli lapgyűjtés (:305–308) ott nem anonim, és a teljes alkalom 1:1 lehet (safer-working; a mondat :95-ben megvan).
- IMPL-G3-12 · P2 · M1.F:210, :243: az @asset `review` és `notes` mezője elavult v1-mezőkre hivatkozik („lineRef”, „Location”, „v1 dedup-tag”), amelyek a v2-blokkban nem léteznek.
- IMPL-G3-13 · P2 · M1.B:39–40, :71–72, :103–104: a nyomtatható sablonok provenance-a „human / emberi-felvétel”, szemben az M1.F-MUNK-01/-02 „gyártandó sablon, nem felvétel” javításával.

**Elvetett hipotézisek**
- M1b (M1.B:86 „kézzel nem szerkeszthető, csak build és pin javíthatja”): elvetve. A leckefájlbeli @asset-blokk a kánoni forrás: Média-assetek/README.md:9 „A jelenlegi leckefájlok.”, :97 „beírsz egy `@asset` blokkot abba a leckefájlba … majd `build`”. Edit-tel kézzel szerkesztendő; generált csak a `build` kimenete (README:42–55). A metaadat-szerkesztés nem kér pint (tools/test_media_manifest.py:1220 „Metadata-only edits keep the fingerprint.”); pin csak a látható M1.B:148/:218/:495 sorokhoz kell.
- N-M1-04 (döntés: az M1.1 SLIDE 5 tanuló-lokális): a 3. csoport egyik peulája sem épít az M1.1 SLIDE 5 reflexiójára (SLIDE-hivatkozás nincs; az M1.F:159 csak a haladást és a kapu-visszajelzést nézi), így ellentmondás nincs.
- M1-04 / N-M1-05 (új helyzetkártyák): nem implementációs hiba. Az M1.A:372 képzői utasítás él; a mátrix POST-PILOT pedagógiai hipotézise változatlan.
- E-M1-072 (M1.F:316, :321, :326, :339 sorvégi szóköz): üres vagy folytatósorok, megjelenítést nem rontanak. A mátrix RETAIN-je helytálló, külön nem jelentem.
- Elavult számszerű sorhivatkozás az @asset-blokkokban (M5-minta): a 3. csoportban nincs ilyen. Minden szakaszhivatkozás létező szakaszra mutat (2.1, 2.3, 4.1.1, 4.1.2, 4.2.1–4.2.3, 4.3, 5.).
- Online ↔ peula eltérés: nem találtam. Az M1.B 1–3. helyzetkártyája egyezik az M1.4 Slide 1 A–C szituációival (M1.4:136–140), a 4–5. kártya „extra”. Az M1.F-POSZ-01 leckenevei egyeznek a MAN LMS-M1-01…04 „Név” értékeivel. Az M1.A online hídja (M1.3–M1.4) egyezik az LMS-M1-03 „M1.A után nyílik” feltételével. Az M1.B:478 KAPU §0, §4.1 és §5 hivatkozásai létező szakaszra mutatnak.


# PED-G1

Rövidítések (abszolút utak):
- HUB = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- M1.1 = 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md
- M1.2 = 02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md
- M1.A = 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- M1.B = 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- KAPU = 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- MAN = 02 Tervezet/LMS – activity manifest.md
- RT = 02 Tervezet/LMS – H5P runtime acceptance.md
- ADV = 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- HUM = 02 Tervezet/Emberi jóváhagyás szükséges.md
- MTX = 01 Fejlesztés/04 Audit/2026-10-10 Anna-kommitok és szakmai javaslatok – teljes megfeleltetési mátrix.md

---

**PED-G1-1**
- **Súlyosság:** P0 · **Bizalom:** magas · **Lencse:** pedagógia (D12, D13; D8-érintettség)
- **Hely:** M1.1:794, M1.1:98; MAN:45; RT:104 (a 24. pont listája); HUM 10. szakasz (:522–527); M1.1:699 (@asset M1.1-IKO-02 notes)
- **Probléma:** Az N-M1-04 döntés („az opcionális személyes önreflexió (M1.1 SLIDE 5) kizárólag tanuló-lokális, központi tárolás nélkül; nem completion-feltétel”) sehol nincs átvezetve. A kánon még a régi, megengedőbb állapotot írja: „lehetőleg” tanuló-lokális, a mentor láthatja, a tartalékút pedig tároló Moodle-oldali mező (RT:41: a Moodle-oldali mező a nem anonim Moodle Feedback TEXT-C profilja).
- **Bizonyíték:** M1.1:794 „ez saját önreflexió, ezért lehetőleg csak a tanuló látja (learner-local); a kijelölt mentor csak akkor láthatja, ha erre ténylegesen szükség van” · MAN:45 „a SLIDE 5 személyes reflexiója opcionális, nem completion-feltétel; lehetőleg learner-local”
- **Hatás:** A build-spec ma megengedi, hogy a kiskorú pilot-tanulók személyes reflexiója központilag tárolódjon és a mentor lássa, ami ellentmond a lezárt döntésnek. Az RT 24. pontja (:104) nem sorolja fel az LMS-M1-01-et, ezért a runtime-teszt sem fedi le.
- **Javaslat:** (1) A döntést szó szerint vezesd át a HUM-ba új, datált (2026-10-10) projektgazdai döntés-sorként, a 10. szakasz D-6 mintájára (HUM:527: „opcionális mezője ugyanígy tanuló-lokális, sor nélkül”). Forrás: a projektgazda 2026-10-10-i döntési csomagja. A vétó/QA-szerepet csak a csomagból vedd át (a mátrix a DPO-t nevezi), ne találd ki. A jegyzőkönyv a `04 Audit` alá kerüljön. (2) M1.1:794: a döntés szövege kerüljön a helyére; a mentor-láthatósági mellékmondat törlendő. (3) M1.1:98: a SLIDE 5 mezőjének ne legyen tároló Moodle-oldali tartalékútja. Ha nem igazolható nem tároló beviteli elem, a lépés beviteli mező nélkül fut (a dia már felkínálja: :774 „fejben is végiggondolhatod”), az RT:41 és az RT:104 „saját jegyzet” ága szerint. (4) MAN:45: az M0.1-sor (MAN:39) mintája szerint („tanuló-lokális: nem tárolt, nem completion-feltétel, beviteli mező nem rögzíti”), hivatkozással az N-M1-04-re és a runtime acceptance 24. pontjára. (5) RT:104: az LMS-M1-01 kerüljön fel a listára. (6) Az M1.1-IKO-02 asset notes-ja (:699) csak a media-manifest folyamaton át módosítható. Tilos hozzányúlni: az opcionális jelleghez, a három kérdéshez, a completion-logikához, a „Ha ez a téma téged is érint” blokkhoz.
- **Típus:** objektív
- **Pilot-besorolás:** PILOT-BLOCKER: az M1.1 a 2026-10-10-án indult M0+M1 pilot része, kiskorú tanulók személyes adatát érinti, és a forrás a döntéssel ellentétes tárolást enged. Ez adatvédelmi P0, freeze-kivétel; a javítás pedagógiai tartalmat nem változtat.
- **Hipotézis:** N-M1-04 (M1-02, X-06)
- **Verdikt:** —

**PED-G1-2**
- **Súlyosság:** P0 · **Bizalom:** magas · **Lencse:** pedagógia (D12; D8-érintettség)
- **Hely:** RT:104 és RT:152 (RT-P0-24); MAN:16 (H5P-C profil); ADV:115
- **Probléma:** Nincs runtime-bizonyíték arra, hogy az M1.1 SLIDE 5 mezője nem tárol szöveget. A H5P-C profil a próbálkozás-rögzítést bekapcsolja, a próbálkozás-riportot a nem szerkesztő tanár is látja, az RT-P0-24 pedig nem futott (és az LMS-M1-01 jelenleg a hatókörén kívül esik).
- **Bizonyíték:** MAN:16 „„Enable attempt tracking” = Yes” · RT:152 „| RT-P0-24 | `IMPLEMENTATION_TEST_REQUIRED` | 24. Tanuló-lokális szöveges lépések |”
- **Hatás:** A döntés megvalósulása a pilotban nem igazolt. Az RT:104 utolsó mondata szerint a tanulónak szóló „nem tároljuk” típusú mondat sem kerülhet a leckébe, amíg az ellenőrzés le nem fut, így a PED-G1-3 keretező mondatának egy része is erre vár.
- **Javaslat:** Nem javítható; G3b (RT-P0-24, az LMS-M1-01-gyel kiegészítve, lásd PED-G1-1) és G2 (HUM-PRIV-01, DPO-QA a döntési csomag szerinti szereppel), tracker #3 és #2. Az ellenőrzés menete: tanulói tesztfiókkal szöveget kell írni a SLIDE 5 mezőbe, majd nem szerkesztő tanári fiókkal vissza kell olvasni, hogy a próbálkozás-riportban és a mentett állapotban (`mod_h5pactivity/enablesavestate`) nincs szöveg, és a completion nem függ tőle. Megfogalmazás: „megvalósítási döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő”.
- **Típus:** bizonyíték-kapu
- **Pilot-besorolás:** PILOT-BLOCKER: kiskorú pilot-tanulók adatát érintő P0 adatvédelmi tétel, az M0+M1 GO/NO-GO evidence listának tartalmaznia kell.
- **Hipotézis:** N-M1-04 (a mátrix „Kapcsolódó hiány: az RA:104 (RT-P0-24) listájából kimaradt az LMS-M1-01” megállapítása igazolva)
- **Verdikt:** —

**PED-G1-3**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** pedagógia (D12, D13)
- **Hely:** M1.1:930 (diaszöveg), M1.1:61, M1.1:767; vö. M1.A:217, M1.A:270–274, M1.A:282
- **Probléma:** A SLIDE 5 a tanulónak nem mondja ki, hogy a reflexió csak neki szól; a „Nem esszét várunk” ráadásul címzettet sugall. A lecke két helyen azt is ígéri, hogy amit a saját vakfoltjáról végiggondolt, azt az M1.A-n a kvucával közösen dolgozzák fel. Az M1.A ezzel szemben kifejezetten nem nyitja meg a vakfoltot.
- **Bizonyíték:** M1.1:930 „ott a kvucával együtt dolgozzátok ki, amit itt a saját vakfoltjaidról végiggondoltál.” · M1.A:274 „a vakfolt valódi feltárása egy későbbi, bizalmibb fázis lesz a kvuca életében.”
- **Hatás:** A kiskorú tanuló joggal hiheti, hogy a privát vakfolt-reflexiója a csoport elé kerül. Ez önkorlátozást vagy nyomást szül, aláássa az N-M1-04 tanuló-lokális keretét, és a peulán meg nem történő dolgot ígér (rossz online ↔ peula átkötés).
- **Javaslat:** (1) Az M1.1:930 és :61 hídmondata igazodjon az M1.A tényleges tartalmához: a peulán a Johari-ablakkal, a nyitott és a rejtett mezővel dolgoztok közösen, a vakfoltot csak megértitek, és amit az 5. dián magadnak végiggondoltál, azt nem kell megosztanod. (2) A SLIDE 5 diaszövegébe kerüljön egy kötelezettségre vonatkozó (nem tárolási) keretező mondat, pl. „Ezt magadnak írod: nem kell megmutatnod senkinek, és a teljesítéshez sem kell.” (3) A „Nem esszét várunk” helyett címzett nélküli alak álljon („Nem kell esszé”). „Nem kerül sehova / nem tároljuk” típusú mondat csak a PED-G1-2 sikeres visszaolvasása után kerülhet be (RT:104). Tilos hozzányúlni: az M1.A biztonsági keretezéséhez (:274, :282), a három kérdéshez, az opcionális jelleghez, és a NAR-05 narrációhoz (VO-gyártott). Látható szöveg, ezért `--pin-visible` kell.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT: az írás opcionális, és az M1.A saját keretezése (passz, „nem kötelező”, a vakfolt nem nyílik meg) a peulán kizárja a kényszerű feltárást, így nem tényleges P0.
- **Hipotézis:** N-M1-04 (pedagógiai keretezés), egyébként új
- **Verdikt:** —

**PED-G1-4**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** pedagógia (D1, D9)
- **Hely:** M1.2:618, M1.2:629, M1.2:651 (SLIDE 4, Mark the Words); vö. M1.2:203, M1.2:392, KAPU:85
- **Probléma:** A Mark the Words utasítása és a tanulónak megjelenő magyarázat megfigyelésnek vagy ténynek nevezi a jelöletlen részeket. Ezek között általánosítás („Megint”, „végig”, „egész idő alatt”, „nem bírsz nyugton maradni 5 percig sem”) és következtetés („nem készültél”) is van, holott a lecke az SLIDE 1–2-ben éppen az általánosítást minősíti nem-megfigyelésnek.
- **Bizonyíték:** M1.2:618 „(A többi rész legyen megfigyelés / tény.)” · M1.2:629 „A „nem készültél”, „végig a többiek szavába vágtál” inkább megfigyelés”
- **Hatás:** Aki a tanult kamera-tesztet alkalmazza és a „Megint”-et jelöli, „tényt is megjelöltél” visszajelzést kap. A tanuló így rossz határt tanul meg, ami az M1 kapu 2. és 4. rubrikasorában (megfigyelhető B, „mindig/soha” nélkül) visszaüthet.
- **Javaslat:** A kulcs (az 5 célszó, a pontozás és a mondatok) változatlan marad. (1) A :618 zárójeles része ne állítsa, hogy a többi rész megfigyelés, pl. „(A többi rész nem címke – de nem mind tiszta megfigyelés.)”. (2) A :629 magyarázata mondja ki, hogy a „megint”, a „végig”, az „egész idő alatt” és az „5 percig sem” általánosít, a „nem készültél” pedig következtetés; adjon kamera-változatot is (pl. „háromszor közbevágtál”). (3) A :651-ben a „tényt is megjelöltél” helyett „címkén kívüli szót is megjelöltél” álljon. Ha a mondatokat kellene cserélni: EMBERI DÖNTÉS (értékelési felelős), mert az kulcsváltozás.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT: formatív, nem kapuzott elem; a kapun emberi értékelő ad visszajelzést, így nem P0.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G1-5**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** pedagógia (D1, D13)
- **Hely:** HUB:36, HUB:86, HUB:27–28; vö. M1.1:857–912, M1.1:768, M1.A:217, M1.B:367
- **Probléma:** A 4. kimeneti kompetencia záróreflexiós mondata („milyen visszajelzés segített már neki”, „mit tesz legközelebb, amikor visszajelzést kap”) az M1 egyetlen fájljában sem jelenik meg tevékenységként; Grep szerint csak a HUB:36 és a HUB:86 tartalmazza. A hub az M1.1 Checkjét nyitott kérdésnek írja le, a lecke Checkje viszont 3 zárt kérdés. Az 1. kompetencia saját vakfolt-példájára pedig csak az opcionális SLIDE 5 ad helyet, mert az M1.A a vakfoltot üresen hagyja.
- **Bizonyíték:** HUB:86 „Check: 1 nyitott kérdés arról, milyen visszajelzés segített már neki.” · HUB:36 „Megfogalmaz a záróreflexióban 1 mondatot arról, milyen visszajelzés segített már neki”
- **Hatás:** A képző olyan reflexiós produktumot keres, ami nem létezik. A modul kimeneti célja és a tevékenységek széttartanak, a hub pedig félrevezető tervezési alapot ad.
- **Javaslat:** Objektív rész: a HUB:86 a tényleges M1.1 Checket írja le (3 zárt kérdés a vakfoltról és a visszajelzés hasznáról). EMBERI DÖNTÉS (programvezető) a 4. kompetenciáról: (a) a meglévő elemekre képeződjön le (M1.B:367 „B: „Hogy esett így hallani?””, M1.B 4.4.2 vállalás), és kerüljön ki a „reflexiós produktumként jelenik meg” kitétel; vagy (b) új lépés kerüljön be. Tárolt produktumként ez új adatkör lenne (HUM-PRIV-01/DPO), és freeze alatt nem lehet. Az 1. kompetencia „saját példájáról” ugyanígy döntés kell (opcionális vagy fiktív példa). Kapuhoz, rubrikához, küszöbhöz nem nyúl.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT: a hub leírását érinti, a pilot-tanuló útját nem blokkolja.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G1-6**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia (D2)
- **Hely:** M1.1:625–628 (SLIDE 4 rács) ↔ M1.1:638–644 (SLIDE 4 narráció); M1.1:463, :466 (SLIDE 3)
- **Probléma:** A SLIDE 4 diaszövege és egyidejű narrációja két különböző példasort ad mind a négy mezőre. A rács nyitott és rejtett példája ráadásul a SLIDE 3 példáit ismétli, új funkció nélkül, miközben a narráció új, madrih-kontextusú példákat hoz.
- **Bizonyíték:** M1.1:625 „Nyitott: „Mindenki tudja rólad, hogy hangosan nevetsz, és te is.”” · M1.1:638 „Ha mindenki tudja rólad, hogy imádod a tábortüzes éneklést, és te is, akkor ez a **nyitott terület**.”
- **Hatás:** Megosztott figyelem: egy dián 8 példa szól 4 fogalomra. A feliratot olvasó tanuló két eltérő szöveget lát egyszerre, a dia pedig a SLIDE 3-at ismétli.
- **Javaslat:** A rács (:625–628) vegye át a narráció példáit (:638–644). Így a dia azt mutatja, ami elhangzik, és nem a SLIDE 3-at ismétli. Az M1.1-ILL-02 specje (:542) csak a media-manifest folyamaton át módosul. Tilos hozzányúlni: a dia-számhoz, a T/F-hez és a narrációhoz (VO-gyártott).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT: pedagógiai minőségjavítás, nem P0.
- **Hipotézis:** N-M1-03, csak a rács-részére igazolva (a „felesleges dia” változatot lásd az elvetettek között)
- **Verdikt:** —

**PED-G1-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** pedagógia (D1, D2)
- **Hely:** M1.1:485 (SLIDE 3 T/F), M1.1:655 (SLIDE 4 T/F), M1.1:902 (SLIDE 6 K3); mikrocél: M1.1:55
- **Probléma:** A SLIDE 3 és a SLIDE 4 T/F-je egymás után ugyanazt az állítást kérdezi (vakfolt → „baj van velem”), új funkció nélkül. Közben egyetlen item sem kéri, hogy a tanuló egy új példát a négy mező egyikébe soroljon, pedig a mikrocél a négy mező megnevezése.
- **Bizonyíték:** M1.1:485 „„Az a cél, hogy a Johari-ablakban **ne legyen vakfoltom**, különben baj van velem.”” · M1.1:655 „„A vakfolt egy hasznos információ arról, hogy mások hogyan látnak engem – nem azt jelenti, hogy baj van velem.””
- **Hatás:** A mikrocél első felét (4 mező) csak a SLIDE 6 K1 disztraktorai érintik közvetve, alkalmazó gyakorlás nincs. Az interakciós helyek egy üzenetre mennek el.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős + programvezető, a pilot adataival): a SLIDE 4 T/F helyére kerüljön-e egy „Melyik mezőbe tartozik?” alkalmazó item a SLIDE 4 példáiból. Ez item- és kulcsváltozás, ezért nem objektív. A SLIDE 6 K3 (térközös felidézés) és a SLIDE 3 T/F marad.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT: formatív lecke, nem P0.
- **Hipotézis:** N-M1-03 (a T/F-ismétlés része igazolva)
- **Verdikt:** —

**PED-G1-8**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia (D1, D2, D13)
- **Hely:** HUB:93, HUB:97, HUB:99, HUB:102 ↔ M1.2 (teljes; :750, :885, :906)
- **Probléma:** A hub szerint az M1.2-ben van M1.1-visszacsatolás és Johari-vakfolt felidézés, és a lecke „4/5 mondatos” besorolást mér. A leckében viszont nincs Johari- vagy vakfolt-utalás (Grep: egyetlen találat, az M1.A címe a :936-ban), nincs 5 tételes besorolás (a D&D 6 kártyás), és a 3 záró kérdésből csak egy besorolás.
- **Bizonyíték:** HUB:97 „rövid felidézés a Johari-vakfoltról.” · M1.2:750 „Alul 6 „kártya” mondatokkal (húzható elemek).”
- **Hatás:** Az M1.1 → M1.2 ívből kimarad a beígért felidézés, a „4/5” formatív célérték pedig a lecke adataiból nem olvasható le (a hub §7 analitikája erre építene).
- **Javaslat:** EMBERI DÖNTÉS (programvezető): (a) bekerüljön-e az M1.2 Moodle-introjába (nem a VO-narrációba) egy mondatos vakfolt-felidézés, vagy törlődjön a HUB:97/:99 ígérete; (b) melyik tételekre vonatkozik a „4/5”. A szám nem változik, csak a megfeleltetés; (c) a HUB:102 „besorolás” megjelölése igazodjon a három záró kérdéshez. Kulcshoz és kártyaszámhoz nem nyúl.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT: ív- és leírásbeli eltérés, a tanulói előrehaladást nem blokkolja.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G1-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** pedagógia (D2, D12; D7-kétség)
- **Hely:** M1.1:926 (SLIDE 6 zárószöveg); vö. M1.1:936–938 (NAR-06), M1.A:282
- **Probléma:** A záró dia a kvíz után új fogalmat (önfeltárás → rejtett mező), új mechanizmust és egy madrih-normát vezet be. Ezt sem a narráció nem mondja, sem item nem dolgozza fel. A kvuca felé irányuló önfeltárásra pedig nem ad határt, amit az M1.A ugyanerre a korosztályra megad.
- **Bizonyíték:** M1.1:926 „Madrihként ez a **hitelesség** egyik eszköze: nem kell mindent kitenned, de amit megmutatsz magadból, azzal közelebb engeded a kvucát.”
- **Hatás:** A feldolgozatlan új fogalom elsikkad. A (gyakran maga is kiskorú) madrih a hanihjai felé irányuló önfeltárást hitelességi eszközként kapja meg, határkritérium nélkül.
- **Javaslat:** EMBERI DÖNTÉS. Pedagógiai rész (programvezető): az önfeltárás → rejtett mező mechanizmusa a SLIDE 3/4 inputba kerüljön-e, vagy maradjon a zárásban. Gyermekvédelmi rész (Memuna + szakmai lektor): kell-e határ-mondat az M1.A:282 („érzékeny magáninformáció megosztása nem feladat”) mintájára. Új szakpolitikai szöveget nem javaslok.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT: nem tényleges P0, a mondat már tartalmaz korlátot („nem kell mindent kitenned”).
- **Hipotézis:** új
- **Verdikt:** —

**PED-G1-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** pedagógia (D12)
- **Hely:** M1.1:344, M1.1:204, M1.1:80; vö. MAN:16, ADV:115
- **Probléma:** A SLIDE 2 érzelmi önbevallását („Hogy érzed magad most ettől a témától?”) a forrás „Completion”-nek jelöli, az intro pedig „válaszoltál a kérdésekre” feltételt ír. A tartalékút (választós H5P-elem, minden opció helyes) bekapcsolt próbálkozás-rögzítés mellett a kiskorú tanuló érzelmi állapotát rögzítené, és ezt a nem szerkesztő tanár is látná.
- **Bizonyíték:** M1.1:344 „(Completion, nincs jó/rossz. Megvalósítás: mint az 1. dia önbevallós kérdésénél – pontozott választós típusba nem kerülhet.)” · M1.1:204 „ha mégis választós H5P-elem kell, minden opciót helyesnek kell jelölni, és ezt a runtime acceptance igazolja.”
- **Hatás:** Egy ráhangoló, privátnak szánt check-in kötelezőnek és megfigyeltnek tűnhet. Ez torzítja a választ („Oké, kíváncsi vagyok”), és szükségtelen adatot képezhet.
- **Javaslat:** Objektív rész: a :344 és a :80 mondja ki, hogy az 1–2. dia önbevallása nem completion-elem (összhangban a :204 szöveges alapértelmezésével). EMBERI DÖNTÉS (DPO/projektgazda): megengedett-e a választós tartalékút rögzítéssel. Ez a D-d/D-i elv (HUM:556, :561) új alkalmazása lenne; az M2.1-nél a rögzítés kikapcsolása a minta (RT:101). Completion-logikához nem nyúl.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT: a forrás alapértelmezése (:204) szöveges, nem rögzít. Hogy a pilot-build a tartalékutat használja-e, azt runtime nem igazolta.
- **Hipotézis:** új
- **Verdikt:** —

---

**Elvetett hipotézisek**
- **N-M1-03 / M1-01 („a SLIDE 4 felesleges, a SLIDE 3–4 összevonandó”):** dia-szinten elvetve. A SLIDE 3 a definíciót adja a két tengellyel és szinkron-animációval; a SLIDE 4 madrih-kontextusú példákat hoz (peula, „madrihként”) és a „hasznos információ” átkeretezést, vagyis más a funkciója. Csak az elem-szintű ismétlés igazolt: PED-G1-6 (rács) és PED-G1-7 (T/F).
- **N-M1-04 / M1-02 / X-06 („UNRESOLVED P0, emberi döntés: tárolja-e a pilot-build”):** nyitott döntésként elvetve, mert a projektgazda 2026-10-10-én döntött. A mátrix „vagy a mező előtt tájékoztatni” alternatívája (mentor-láthatóság jelzéssel) és a tanulói megosztás-kapcsoló a „kizárólag tanuló-lokális, központi tárolás nélkül” szöveggel nem fér össze. A maradék teendő a PED-G1-1 (átvezetés) és a PED-G1-2 (bizonyíték).
- **M1a, M1b (M1.B smiley-kártyák, M1.B-KART-02 notes):** nem vizsgáltam, a 3. csoport hatóköre; az 1. csoport fájljaiban nincs rájuk utaló elem.
- **M1-03 (N-M1-06/-07/-09/-11, az M1.4 rubrika láthatósága):** nem vizsgáltam, a 2. csoport hatóköre.
- **M1-04 / N-M1-05 (az M1.A példamondatai azonosak az M1.2-éivel):** a forrásoldali átfedés megvan (M1.2:536–537, :754–757), de az értékelés a 3. csoporté; az 1. csoportban nincs belőle önálló finding.
- **E-M1-* sorok (M1 hub, M1.1, M1.2):** a mai fájlokban minden ellenőrzött sor a mátrix szerinti állapotban van, ellentmondást nem találtam.


# PED-G2

PED-G2 – M1, 2. fájlcsoport, pedagógia lencse (D1, D2, D9, D12, D13). Csak olvastam, nem szerkesztettem semmit.

Rövidítések (abszolút utak):
- KAPU = 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- M1.3 = 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md
- M1.4 = 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- hub = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- M1.B = 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- MAN = 02 Tervezet/LMS – activity manifest.md
- PT = 02 Tervezet/Program terv.md

Mind a 10 finding POST-PILOT. Egyik sem felel meg a freeze-kivétel feltételének: nem P0 biztonsági, adatvédelmi vagy hozzáférhetőségi hiba, és a tanulói előrehaladást sem blokkolja.

---

**PED-G2-1**
- Súlyosság: P1 · Bizalom: magas · Lencse: pedagógia (D1, D13)
- Hely: M1.3:45, :801 · M1.4:10, :426, :434, :450, :461, :491 ↔ KAPU:21, :197 · hub:33, :39, :125 · PT:106, :138, :142
- Probléma: A tanulói leckék 1–2 mondatos SBI-t kérnek. A kapu „Mit mér” sora, a KAPU 6. iteme, a hub és a Program terv viszont 2–3 mondatost. Az M1.4 ráadásul a „mondat” szót darabszámként is használja („legalább 1, de maximum 2 különböző SBI-mondatot”, „Minimum: 1 teljes SBI-mondat”).
- Bizonyíték: M1.4:450 „Ebben a feladatban **1–2 mondatos SBI-visszajelzést** fogalmazol meg egy konkrét helyzetre.” · KAPU:21 „…**címkézésmentes, tisztelettudó**, 2–3 mondatos SBI-visszajelzést **írni**.”
- Hatás: A tanuló és a képző két különböző hosszmércét kap. A KAPU 6. iteme (KAPU:197, :200) „2–3 mondatos SBI”-t kér, és azt mondja: „ezt add be az M1.4 Assignmentbe”. Közben a hivatalos rubrika a hosszt nem pontozza, és a KAPU saját „épp átmegy” mintája (KAPU:260) egyetlen mondat. Azért nem P0, mert az operatív küszöb (minden sor ≥1 ÉS ≥5/8) minden forrásban azonos.
- Javaslat: EMBERI DÖNTÉS (értékelési felelős + projektgazda): melyik hossz a kánoni. A Program terv a forrás-sorrendben elöl áll, de a leckék, az M1.B:359 („1–2 mondatban”) és a KAPU 4.1-es mintája az 1–2 mondatot valósítja meg. A döntés után minden felsorolt helyre egyetlen megfogalmazás kerüljön, az M1.4-ben pedig az „SBI-mondat” darabszám helyett „SBI” álljon. A rubrikához, a küszöbhöz és a próbálkozásszámhoz nem nyúl.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT – a hosszt egyik forrás sem pontozza, ezért a pilot-tanuló előrehaladását nem blokkolja.
- Hipotézis: mátrix 12. szakasz „M1a” 1. pont. Megerősítve, és kiegészítve a darabszám–hossz keveredéssel, valamint az M1.3:801 „Kötelező sablon (1 mondat)” sorral.

**PED-G2-2**
- Súlyosság: P1 · Bizalom: közepes · Lencse: pedagógia (D1)
- Hely: M1.4:475–476 ↔ M1.4:138 (B-kártya) · M1.4:359, :366 ↔ M1.4:140 (C-kártya)
- Probléma: A kapufeladat leírásában álló példamondat kész, maximális szintű SBI az egyik választható kapuhelyzetre (B – kinevetés). A C-helyzethez a mini-kvíz helyes I-válasza és S-ként magyarázott disztraktora adja meg a részeket. A kapu így két helyzetnél összerakást vagy átmásolást mér, nem önálló megfogalmazást.
- Bizonyíték: M1.4:138 „A beszélgetőkörben az egyik hanih mindenkit kinevet, aki megszólal.” · M1.4:475–476 „Amikor ma a körben háromszor kinevetted a többieket, / a kicsik utána már nem szólaltak meg.”
- Hatás: A KAPU:21 szerint a kapu azt méri, hogy a tanuló „tud-e … SBI-visszajelzést írni”. A példát átvevő beadvány viszont legalább 7/8-cal átmegy (B, I és hangnem „Erős”). Így a megerősített „Teljesítve” nem bizonyítja az M7-be továbbvitt készséget (hub:251).
- Javaslat: Két lehetőség:
  - Az Assignment-leírás példája olyan helyzetre szóljon, amely nem választható kapuhelyzet, például az M1.3 HOOK már ismert „játék közben félbeszakítottad” helyzetére.
  - Vagy a példa alá kerüljön egy mondat: „A példát ne vedd át: a választott helyzetre a saját szavaiddal írj.”
  A rubrika, a küszöb, a helyzetkártyák és a kvízek answer key-e változatlan marad.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – validitási gyengeség, nem freeze-kivételi hiba, és nem blokkol.
- Hipotézis: új

**PED-G2-3**
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia (D2, D13)
- Hely: KAPU:11, :28, :200, :308 ↔ MAN:45–51 (LMS-M1-01…07) · PT:142, :225 · M1.4:309
- Probléma: A KAPU §3 item-bankja külön tanulói Quiz vagy H5P Question Set activityként van előírva. Benne van a kapu előtti egyetlen olyan írásgyakorlat, amely a rubrika négy sorára épül (Item 5–6). Az activity manifestben viszont nincs sora, és egyik lecke sem helyezi el a tanulói útban. A kapu előtt így az M1.4 csak egyes S/B/I-elemek felismerését gyakoroltatja.
- Bizonyíték: KAPU:308 „**A 3. szakasz item-bankja** külön Quiz/H5P Question Set, **completion-only**, NEM kötve a kapuhoz.” · MAN:49–50: az LMS-M1-04 után közvetlenül az LMS-M1-05 (Assignment) jön, kvíz-sor nincs.
- Hatás: A builder két kánoni forrásból mást olvas: a KAPU és a PT szerint van M1-kvíz (PT:142, :225), a manifest szerint nincs. Ha a kvíz kimarad, a tanuló a kapu előtt nem kap rubrika-szintű gyakorló írást. Ha a KAPU alapján mégis megépül, az Item 5–6 szabad szöveges válaszai tárolási besorolás és a PT:225 szerinti tájékoztató nélkül maradnak. (A tárolás kérdése a safety-lencséé.)
- Javaslat: EMBERI DÖNTÉS (projektgazda + értékelési felelős): tanulói activity-e az item-bank vagy képzői tartalék.
  - Ha tanulói activity: kapjon manifest-sort az LMS-M1-04 és az LMS-M1-05 közé, completion-feltétel nélkül, tárolási besorolással.
  - Ha képzői tartalék: a KAPU:11, :28, :200, :308 és a PT:142 „kvíz”-szövegét kell hozzá igazítani.
  Az itemek, a ✅ jelölések és a küszöb változatlanok.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT – nem completion-feltétel, nem blokkol, a pilot-build a manifestet követi.
- Hipotézis: új

**PED-G2-4**
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia (D1, D12)
- Hely: M1.4:523 (M1.4-MUNK-01 spec) ↔ M1.4:478–487 · KAPU:298 · hub:213, :220
- Probléma: A tanuló a kapu mércéjét csak az Assignment online leírásának 3. lépésében látja. Az „egyenértékű” fájlalapú út sablonjának specifikációja a 3. lépés táblázatát nem sorolja fel. A KAPU §5 nem írja elő, hogy a Moodle-rubrika a tanulónak megjelenjen: sem előnézetként, sem értékelés után soronként. Pedig erre épül az M1.F első lépése („melyik rubrikasor nem teljesült”).
- Bizonyíték: M1.4:523 „…kizárólag a lecke 2–4. lépésének meglévő elemeivel, szó szerint: a három mező (…); a „Formátum – javaslat” mondatváza (…); két SBI-blokk a 4. lépés szerint…” · KAPU:298 „**Grading method:** Rubric → vidd be a fenti 4 sort, soronként 0/1/2 ponttal és a szintleírásokkal.”
- Hatás: Aki letöltött vagy nyomtatott sablonnal ír, írás közben nem látja a négy szempontot és az átmenő szabályt. Ha a build nem jeleníti meg a rubrikát a tanulónak, a bukott tanuló nem látja, melyik sor maradt 0-n. Ekkor az M1.F privát önellenőrzése (hub:220) csak a szöveges visszajelzésre támaszkodhat.
- Javaslat:
  - Az M1.4-MUNK-01 spec felsorolásába kerüljön be szó szerint a 3. lépés táblázata és az átmenő mondat (M1.4:478–487). Ez a „2–4. lépés” keretén belül marad; média-manifest build + pin kell hozzá.
  - A KAPU §5-be és az M1.4 §3.2-be kerüljön be a rubrika tanulói megjelenítése. Ezek a Moodle-rubrika ide tartozó beállításai: „Allow users to preview rubric”, „Display rubric description to those being graded”, „Display points for each level to those being graded”, „Show remarks to those being graded”.
  - A célverzió alapértelmezését nem ismerjük; a tanulói tesztfiókos visszaolvasás RT-tétel (G3a spec / G3b runtime).
  A küszöb és a szintek változatlanok.
- Típus: objektív. A futásidejű megjelenés igazolása külön bizonyíték-kapu (G3b). · Verdikt: —
- Pilot-besorolás: POST-PILOT – a mérce az online leírásban elérhető, nem blokkol.
- Hipotézis: N-M1-06, N-M1-11 (mátrix 11. szakasz M1-03). A mérce beadás előtti láthatósága a forrásban megerősítve; a fájlút és a rubrika-megjelenítés hiánya új.

**PED-G2-5**
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia (D13)
- Hely: M1.B:134–139 és az M1.B-MUNK-01 spec (M1.B:102) ↔ KAPU:53–55, :79–87 · M1.3:1030–1033
- Probléma: Az M1.B megfigyelői trió-checklistje csak azt kérdezi igen/nem alapon, volt-e S, B, I, illetve címke. Hiányzik belőle a kapu 4. sora (hangnem, „mindig/soha”). Hiányzik a „Rendben” és az „Erős” közti különbség is (tág vagy konkrét S és I). Közben az M1.B kifejezetten a kapuprodukum csiszolására és újrabeadására biztat.
- Bizonyíték: M1.B:135–138 „Volt **S**? (igen / nem) … Volt **címke**? (igen / nem + példa)” · M1.B:476 „…ami **jobb a beadottnál**, kérd meg a képződet, hogy nyisson neked **új próbálkozást**”
- Hatás: Egy tág „a peulán…” S vagy egy „mindig”-es fordulat is „volt S / nincs címke” pipát kap. A tanuló így nem tudja meg, hogy épp ezeken a sorokon lesz „Rendben” vagy „Még nem”. Az online M1.3 négypontos önellenőrzése és a peula megfigyelői listája nem ugyanazt a mércét használja.
- Javaslat: A trió-checklist vegye át szó szerint az M1.3 SLIDE 7 négy önellenőrző kérdését (M1.3:1030–1033), új kritérium nélkül. Az M1.B-fájl és a MUNK-01 metaadat változik (média-manifest build + pin); a rubrika és a küszöb nem.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – formatív peulaeszköz, nem blokkol.
- Hipotézis: új (a 3. csoporttal átfedhet)

**PED-G2-6**
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia (D2, D12)
- Hely: M1.3:799 ↔ :814–815 (NAR-04) · M1.3:886 ↔ :1022–1033 · MAN:48 (az LMS-M1-07 az LMS-M1-03 után nyílik)
- Probléma: Az M1.3 írási lépéseinek sorrendje nem követhető:
  - az 5. dia narrációja „beírást” kér, pedig a dián a D-1 szerint nincs beviteli elem;
  - a 6. dia „ezt a mondatot” másoltatja ki, holott előtte nincs mondat, a mezőbe írást pedig a lecke utánra teszi;
  - a 7. dia közben már „a saját mondatod” ellenőrzését kéri;
  - a mező (LMS-M1-07) csak a H5P completionje után nyílik meg, és ott nincs önellenőrzés.
- Bizonyíték: M1.3:814 „Képzelj el egy egyszerű helyzetet, és próbáld meg beírni,” · M1.3:886 „💡 **Másold ki és mentsd el magadnak** ezt a mondatot – … A három részt a lecke után következő ‘M1.3 – Saját mini-SBI’ szövegmezőbe írd be.”
- Hatás: A tanuló mezőt keres az 5. dián. A 7. diánál még nincs leírt saját mondata, így az önellenőrzés üres. A ténylegesen beadott mini-SBI-t, amelyre az M1.4 épít, már semmi nem ellenőrizteti.
- Javaslat:
  - NAR-04: „beírni” helyett „leírni magadnak” – ez a lezárt D-1 átvezetése; VO-forrásblokk, ezért média-manifest build + pin.
  - 6. dia: „Írd le most vázlatként (jegyzetbe vagy papírra), a következő dián ellenőrizd, a lecke után másold be a mezőbe.”
  - Az LMS-M1-07 mező előtti tájékoztatóba szó szerint kerüljön be az M1.3:1030–1033 négy kérdése.
  A completion, a tárolás és a D-1 változatlan.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – zavaró, de nem blokkol, a mező a lecke után megtalálható.
- Hipotézis: új

**PED-G2-7**
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia (D12; értékelési átfedés: D3)
- Hely: KAPU:260–269 (4.1-es minta) ↔ KAPU:86 (a 4. sor „Rendben” szintje)
- Probléma: Az „épp átmegy” kalibrációs mintában egyetlen sor „Erős”: a hangnem, „nincs címke” indoklással. Ugyanennek a beadványnak a B-sorát viszont „kissé minősítő-általános”-nak nevezi. A 4. sor „Rendben” szintje pedig épp az „enyhe minősítés”. A küszöböt eldöntő minta így önmagának ellentmond.
- Bizonyíték: KAPU:265 „…de **nincs szám/idő** és kissé minősítő-általános.” · KAPU:267 „| Hangnem | Erős | **2** | Végig a **viselkedésről** szól, nincs címke, nincs „mindig/soha”…”
- Hatás: Ha a képző a 4. sor szövegét követi, a hangnem „Rendben”, az összpont 4/8, és a minta „Még nem teljesítve”. A pilotban két értékelő ugyanazt a határesetet ellentétesen döntheti el. Ez az F-peula kötelezettségét és az M3-kapu nyílását is érinti.
- Javaslat: EMBERI DÖNTÉS (értékelési felelős): a „sokat beszéltél bele” / „ilyen voltál” fordulat a 4. sor szerint enyhe minősítés-e. Utána a B- és a hangnem-indoklást össze kell hangolni. A küszöb, a szintek és a minta pontszámai addig nem változnak. A pilot-értékelők kalibrációs egyeztetése ettől függetlenül ajánlott; ez nem tartalmi javítás.
- Típus: emberi-döntés · Verdikt: —
- Pilot-besorolás: POST-PILOT – tartalmi módosításként nem freeze-kivétel; a pilot-kockázat kalibrációs egyeztetéssel kezelhető.
- Hipotézis: új

**PED-G2-8**
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia (D1)
- Hely: M1.4:321–324, :328 ↔ KAPU:134 · M1.4:347
- Probléma: Az M1.4 3. diáján egyedül a helyes S-opcióban van időjelölés, így a kérdés felszíni mintázatból megfejthető. A KAPU maga írja le ezt a hibatípust, és az M1.4 4. diáján már javították.
- Bizonyíték: M1.4:321–322 „„Ma a peula közepén…” ✅ / „Nagyon tiszteletlen voltál.” *(címke a személyről)*” · KAPU:134 „…az egyetlen időhatározós opció felületi mintázatból megfejthető”
- Hatás: A gyakorlás nem kényszeríti ki, hogy a tanuló elválassza az S-t a B-től és az I-től. Az S felismerése így hamis biztonságérzetet ad.
- Javaslat: A három disztraktor kapjon időjelölést úgy, hogy megmarad a hibatípusuk (a KAPU Item 1 mintájára, pl. „Ma a peula közepén nagyon tiszteletlen voltál.”). A ✅ és a típusmegjegyzések változatlanok. A visszajelzés az M1.4:347 mintájára egy félmondattal bővül. A csere oka objektív validitási hiba, nem stílus.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – formatív item, nem blokkol.
- Hipotézis: új

**PED-G2-9**
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia (D12)
- Hely: M1.4:147, :153–154 ↔ M1.4:309–366
- Probléma: Az 1. dia azt ígéri, hogy a tanuló kiválasztja, „melyik helyzetbe akar mélyebben belemenni”. A választásnak nincs következménye: a 3–5. dia mindhárom helyzeten ugyanúgy végigvisz, és a választás az Assignmentbe sem kerül át.
- Bizonyíték: M1.4:153 „a tanuló kiválasztja, melyik helyzetbe akar mélyebben belemenni.” · M1.4:309 „Minden szitunál 1 **Single Choice** kérdés”
- Hatás: Ez látszat-autonómia: a tanuló választ, a lecke nem reagál rá. Ez gyengíti a következő, valódi választás (az Assignment 1. lépése) súlyát.
- Javaslat: A kártyaválasztás instrukciója őszintén gondolkodási előkészítésként fogalmazzon, például: „Válaszd ki, melyikről tudnál leginkább beszélgetni – a következő diákon mindhármat megnézzük, és ezt viheted tovább a beadandóba.” Az M1.4-NAR-01-VO ehhez igazítandó (média-manifest build + pin). A diák és az itemek változatlanok.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – élményminőség, nem blokkol.
- Hipotézis: új

**PED-G2-10**
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia (D13)
- Hely: M1.4:494–502 ↔ hub:8 · M1.B:476
- Probléma: Az M1.4 tanulói szövege egyszer sem említi az M1.B-t. A hub szerint a beadás M1.B előtt ajánlott, és az M1.B hurokzárása erre épít. Az M1.4 határideje (az M2.A előtti szerda) viszont az M1.B utánra esik, és a lecke nem mondja el, hogy a peulán csiszolt SBI új próbálkozásként beadható.
- Bizonyíték: hub:8 „Az M1.4 SBI-beadandót (kapu) a 2. héten, M1.B előtt érdemes leadni.” · M1.4:497 „**Határidő:** legkésőbb az M2.A peula előtti szerdán 18:00-ig add be”
- Hatás: A tanuló nem tudja, mikor érdemes beadnia. Aki M1.B után ad be, annál az M1.B „jobb a beadottnál” hurokzárása nem értelmezhető. Aki előtte ad be, nem tudja, hogy utána finomíthat. Az online és a peula közti transzfer így csak a képző szóbeli közlésén múlik.
- Javaslat: Az M1.4 „Fontos” listája kapjon egy mondatot a hub:8 és az M1.B:476 tartalmának szó szerinti átvételével: ajánlott beadás M1.B előtt; a peulán csiszolt SBI a képző által nyitott új próbálkozásban beadható; a legjobb megerősített eredmény számít. A határidő és a próbálkozásszám nem változik.
- Típus: objektív · Verdikt: —
- Pilot-besorolás: POST-PILOT – tájékoztatási hiány, nem blokkol.
- Hipotézis: új

LEVÁGVA: 2 további finding, súlyosságuk: 2×P2
- PED-G2-11 · P2 · hub:129 ↔ M1.4:18, MAN:49 · A hub az M1.4 H5P-részét „H5P Column felidéző”-nek írja, a lecke „Course Presentation vagy Question Set”-nek, a manifest H5P-C-nek (az implementációs lencsével átfed). Pilot: POST-PILOT. Hipotézis: új.
- PED-G2-12 · P2 · M1.3:886 ↔ :1059 (NAR-06) ↔ M1.4:457 · A 6. dia valós, névtelenített helyzetet is megenged. A NAR-06 megkötés nélkül mondja, hogy „az Assignmentben erre építhetsz”, az M1.4 viszont tiltja a valós helyzetet. A tartalmi kérdés a MAN:48 szerinti nyitott N-1 döntéstől függ (gazdája a projektgazda, DPO-vétóval); a narráció ehhez igazítandó. Pilot: POST-PILOT. Hipotézis: új.

**Elvetett hipotézisek**
- N-M1-06: hibaként elvetve. Az M1.4:478–487 a beadás előtt, a tanulói leírásban mutatja a 4×3-as táblázatot és az átmenő szabályt. A fájlút hiánya új, külön finding (PED-G2-4).
- N-M1-07: elvetve. Az M1.4:482–485 sornevei egyeznek a KAPU 1–4. sorával; a 3. sor rövidebb neve („érthetősége”) a jelentést nem változtatja.
- N-M1-09: elvetve. A cellák a KAPU §1 hű kivonatai. Az S „Erős” cellája („mikor, hol és melyik helyzetben”) kicsit szigorúbb a KAPU „idő ÉS/VAGY hely” megfogalmazásánál, de felfelé tol, a kapudöntést nem érinti.
- N-M1-11: forrásszinten elvetve. A Rubric, a Maximum grade = 8, a Grade to pass = 5 és az összetett feltétel benne van (KAPU:22, :298–303; M1.4:548–553). A tanulói megjelenítés előírásának hiánya a PED-G2-4-be került; a tényleges Moodle-beállítás runtime-kérdés (CC-06, G3b).
- Mátrix 11. szakasz M1-03: a fenti N-M1-06/-11 ítélet szerint; az M1.4 rubrikájának láthatósága a forrásban teljesül.
- N-M1-04 (a fő session közvetítése): a 2. csoport fájljai nem hivatkoznak az M1.1 SLIDE 5-re. A KAPU-ban és az M1.3-ban 0 Grep-találat, az M1.4-ben nincs M1.1-hivatkozás, ezért ebből a csoportból nincs ide tartozó finding.
- M1a 2–3. pont (M1.B smiley-készlet, RA:104): az 1. és a 3. csoport hatóköre, itt nem vizsgáltam.


# PED-G3

M1 pedagógiai review, 3. fájlcsoport (M1.A, M1.B, M1.F): 10 finding (2×P1, 8×P2), 2 levágott finding (P2), 4 elvetett vagy nem értékelt hipotézis. PILOT-BLOCKER nincs. A legfontosabb: az M1.F valós helyzetről írt SBI beadását kéri, amit az M1.4 beadási leírása tilt.

**Rövidítések (abszolút utak)**
- M1.A = 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- M1.B = 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- M1.F = 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md
- HUB = 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md
- M1.2 / M1.3 / M1.4 = 02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md, …/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md, …/M1.4 – Miniszituációk – Mondd el SBI-ben.md
- ADATV = 02 Tervezet/Adatvédelem – tanulói adatok és AI.md

Runtime-bizonyíték nincs; Moodle-beállításra egyik finding sem tesz állítást.

---

**PED-G3-1**
- **Súlyosság:** P1
- **Bizalom:** magas az ellentmondásra; közepes a súlyosságra
- **Lencse:** pedagógia (D13, D8 határán)
- **Hely:** M1.F:270, valamint :276; másodlagosan M1.B:476. A :476 a :382-es valós kör és a :425-ös „terepen is használnád” kérdés után áll.
- **Probléma:** Az M1.F azoknak, akik a kaput már teljesítették, extra SBI beadását ajánlja az M1.4 Assignmentbe, „amit majd a peulán / terepen tényleg használni fog”. Ez valós helyzetet és valós személyt feltételez. Az M1.4 beadási leírása és a HUB:39 viszont kitalált, életszerű helyzetet ír elő.
- **Bizonyíték:** M1.F:270 „az M1.4 Assignmentben megír még **egy extra SBI-mondatot**, amit majd a peulán / terepen tényleg használni fog” ↔ M1.4:457 „Valós helyzetet – név nélkül sem – ne írj le: egy kis közösségben könnyen kiderül, kiről van szó.”
- **Hatás:**
  - A képző szóbeli instrukciója ellentmond a beadási felület szabályának.
  - A tanuló, aki maga is lehet kiskorú, visszaazonosítható szöveget tölthet fel egy valós hanihról vagy társáról.
  - Az M1.B hurokzárása (:476) sem figyelmeztet arra, hogy a valós körben (:382) született mondat nem adható be.
- **Javaslat:**
  - Az M1.F:270 mondatrészét igazítsd az M1.4:457-hez és a HUB:39-hez („egy kitalált, de életszerű helyzetre; valós helyzetet név nélkül sem”).
  - Az M1.B:476 kapjon egy tagmondatot ugyanezzel a korláttal.
  - Ne nyúlj hozzá: próbálkozás-logika, „a legjobb megerősített eredmény számít”, a javító próbálkozás nyitása.
  - Ha valós helyzetet engedni kellene az M1 SBI-beadandóban (ADATV:80 „Külön review” tétel), az EMBERI DÖNTÉS (DPO), nem /course-fix.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. P1, mert a beadás helyén az Assignment leírása (M1.4:457) tiltja a valós helyzetet, tehát van kontroll. Ha a biztonság-jog lencse P0 adatvédelmi hibának minősíti, PILOT-BLOCKER.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-2**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** pedagógia (D1, remediáció)
- **Hely:** M1.F > 4.2 Blokk 2 (:277) és 4.3 Blokk 3 (:293–297)
- **Probléma:** A kötelező F-peula célja a nem teljesült rubrikasorok javítása (M1.F:53: „S, B, I vagy hangnem”), de a terv hiányos:
  - a 4. rubrikasorhoz (hangnem, HUB:244) nem ad magyarázatot;
  - a javított vázlatot a javító próbálkozás előtt senki nem nézi át a rubrika szerint, sem a tanuló, sem a képző;
  - közben a nem kapuzott Vakfolt (HUB:26) fix sávot kap.
- **Bizonyíték:** M1.F:277 „A képző **körbejár**, de csak röviden segít (technika, „hol találom ezt?”).”; M1.F:294–297 „**3 kulcspontot röviden helyrerakni**: – Vakfolt (Johari), – megfigyelés ≠ címke, – S–B–I.”
- **Hatás:**
  - Aki a hangnem soron bukott („mindig/soha”, a személy minősítése), az nem kap célzott segítséget.
  - A javított vázlat ugyanazzal a hibával mehet a javító próbálkozásba.
  - A remediáció így csendes munka és általános magyarázat marad, nem „facilitált, strukturált javítás” (HUB:258).
- **Javaslat:** A 45’ és a blokkidők változatlanok.
  - (a) Blokk 2, 1–2. lépés: aki a kapun bukott, a vázlatát soronként vesse össze az M1.4 tanulói rubrikatáblájával (M1.4:480–487). A képző körbejárás közben ezekre a vázlatokra adjon rövid visszajelzést „Megfigyelés → Hatás → Következő lépés” formában (HUB:257).
  - (b) Blokk 3: a hangnem kerüljön a kulcspontok közé, a HUB:244 / M1.4:485 szövegével. A Vakfolt lehet az „1 mondatban elintézhető” pont, ha a kapus visszajelzések nem jelzik.
  - Ne nyúlj hozzá: küszöb, próbálkozásszám, az F-peula kötelező jellege, completion.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Az M1.F a megerősítés után fut, a javító próbálkozás a mai szöveggel is megnyílik, tehát nem blokkol.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D12)
- **Hely:** M1.B:69 és :86 (@asset M1.B-KART-02), :148, :214, :218, :495; az Eszközök (:127–143) és a checklist (:488–492) A–D sarokjelölő nélkül; a 4. kérdés (:241–245) „→” visszajelzés nélkül.
- **Probléma:** A 4.1.2 mozgásos kvíz sarok-hivatkozásai széttartanak:
  - Az 1., 2. és 4. kérdés A–D választós, a 3. és az 5. igaz/hamis. Mégis :214 „vagy”-gyal választhatónak írja a két módot, :148 és :495 csak „A/B sarkot” említ.
  - Az @asset (:69, :86) a 3 smiley-t ajánlja sarokjelölőnek, de 3 kártya nem jelölhet 4 sarkot.
  - A MAG-címke (:218) a 4. kérdést a régi tartalmával nevezi meg.
- **Bizonyíték:** M1.B:214 „Használj **A/B/C/D sarkot** vagy „igaz/hamis” mozgást.” ↔ M1.B:495 „Van hely mozogni A/B sarkok között.”; M1.B:218 „**4. kérdés** (melyikből tudsz javítani?)” ↔ M1.B:241 „Melyik mondat nevez meg konkrét viselkedést és hatást?”
- **Hatás:**
  - A tér- és az eszközlista alapján a képző 2 sarokra készül, a kvízhez viszont 4 sarok és egy igaz/hamis oldal kell.
  - Csúszáskor a MAG-címke alapján rossz kérdést tarthat meg.
  - A 4. (MAG) kérdéshez nincs kimondható visszajelzés, az 1–3. és az 5. kérdéshez van.
  - Improvizálással végrehajtható, de felkészülés nélkül nem egyértelmű.
- **Javaslat:**
  - :148 és :495: „A/B/C/D sarok (+ igaz/hamis oldal)”.
  - :214: a „vagy” helyett 1., 2., 4. kérdés A–D sarok, 3. és 5. kérdés igaz/hamis oldal.
  - :218: a MAG-leírás kövesse a 4. kérdés mai szövegét.
  - Az Eszközökbe és a checklistbe 4 sarokjelölő lap (A–D).
  - A KART-02 :69 és :86 szövegéből töröld vagy pontosítsd a sarokjelölő szerepet. Az @asset-módosítás után `media_manifest.py build` és pin kell.
  - Opcionális: a 4. kérdés „→” visszajelzése a meglévő dőlt típusjelölésekből (:242–245), új tartalom kitalálása nélkül.
  - A ✅ jelölések nem változnak.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Képzői pontatlanság, improvizálással áthidalható.
- **Hipotézis:** E-M1-069 és a mátrix 12. szakasz M1b (M1.B:86). Megerősítve, kibővítve a :69, a :214 „vagy”, az eszközlista és a 4. kérdés visszajelzése tételekkel.
- **Verdikt:** —

**PED-G3-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D12)
- **Hely:** M1.B:192 és :203 ↔ :70, :74, :140–143, :186, :491
- **Probléma:** A 4.1.1 kétszer kéri, hogy minden résztvevő felmutasson egy smiley-kártyát. Az @asset, az eszközlista és a checklist viszont csak 3 nagy, képzői kártyát ír elő; fejenkénti készlet nincs.
- **Bizonyíték:** M1.B:192 „háromra emeljétek fel azt a kártyát, ami leginkább tükrözi, hogyan érkeztetek meg” ↔ M1.B:70 „Három nagyméretű, felmutatható kártya kartonon … A képző a ráhangoló blokkban (4.1.1.) felmutatja”
- **Hatás:** A peula első 3 percének instrukciója a beszerzett eszközökkel szó szerint nem hajtható végre; a képző a helyszínen improvizál.
- **Javaslat:** Két lehetőség:
  - Eszközt nem bővítő javítás: :192 és :203-ban kártya helyett más jelzés (pl. ujjal 1/2/3 a három smiley-ra), a képzői kártyák referenciaként maradnak.
  - Fejenkénti készlet az Eszközökben és a KART-02 `technical` mezőjében (létszám × 3 db); ez @asset-módosítás, build és pin kell hozzá.
  - A kettő közti választás szerkesztési döntés; a reflexiós kérdések tartalma nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. 3 perces ráhangoló, áthidalható.
- **Hipotézis:** mátrix 12. szakasz „M1a”, 2. pont (mátrix-ID nélkül). Megerősítve.
- **Verdikt:** —

**PED-G3-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D2, D12)
- **Hely:** M1.B:321, :323, :334, :350, :395
- **Probléma:** A 4 fős csoport forgása ellentmond az A→C, C→B, B→A szabálynak, és a 4. kör ideje nincs betervezve. 8 főnél minden csoport 4 fős (:323); a legtöbb létszámnál legalább egy ilyen csoport van.
- **Bizonyíték:** M1.B:321 „A 4. személy a **2. körtől lép be A-ként**, addig ő is megfigyel.” ↔ M1.B:334 „**A → C, C → B, B → A.**” A szabály szerint a 2. körben az 1. kör B-je lenne az A.
- **Hatás:**
  - A forgást a helyszínen kell kitalálni; ha rosszul sikerül, valaki nem lesz A vagy B, így sérül a :260-as cél.
  - 4 kör × 4’ = 16’, ez a 14–30’ sávot teljesen kitölti.
  - A puffer-szöveg (:395) csak 3 körrel számol; a puffer és az opcionális valós kör elfogy, a nagykör késve indul.
- **Javaslat:**
  - Rögzíts egy egymondatos 4 fős forgásrendet, amelyben mindenki egyszer A és egyszer B (pl. „minden körben a következő ember lesz A, az előző kör A-ja lesz B”).
  - A :395-ben jelezd, hogy a 4. kör a puffer terhére megy.
  - A 10–30’ blokkhatár és a 45’ változatlan.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Improvizálással végrehajtható.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-6**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D13, D12)
- **Hely:** M1.F:101–104 (2.3) ↔ M1.F 4.3 (:317–343)
- **Probléma:** A képző három „tipikus félreértés-kérdést” gondol át előre, de az M1.F csak a „Vakfolt = baj?” kérdésre ad kimondható választ (:320). A „Nem túl száraz így?” és a „Belefér-e érzés az I-be?” válasz nélkül marad, pedig a válasz a kánonban megvan.
- **Bizonyíték:** M1.F:103–104 „Megfigyelés vs. címke: „Nem túl száraz így?” / SBI: „Belefér-e érzés az I-be?”” ↔ M1.3:805 „(I – mit éreztem / mi lett a hatás)”; M1.B:422 „az SBI elsőre szokatlan … Ez gyakorlással válik természetesebbé.”
- **Hatás:** Épp azon a peulán, ahol a pontos fogalom a cél, a képző rögtönözve válaszol. Ha az érzésre nemet mond, ellentmond az M1.3-nak és az M1.4 beadási sablonjának (M1.4:471), és ez rontja az I-sor javítását. Kapcsolódó: az M1.A:447 „érzés/címke” jelölése ugyanezt a bizonytalanságot erősítheti (alacsony bizalom).
- **Javaslat:** Az M1.F 2.3 két kérdése mellé egy-egy válaszmondat a meglévő kánonból: az érzéshez M1.3:805 / M1.4:471, a „száraz” kérdéshez M1.B:422. Új állítást ne írj.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Nem blokkol.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-7**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D2, D12)
- **Hely:** M1.F:163–173 (Blokk 1, 0–5’) ↔ :269–270 (Blokk 2, 5–7’); :261
- **Probléma:** A Blokk 1-ben a tanuló a Moodle-ben nézi meg a kapus visszajelzést és a leckék állását, a belépést viszont csak a Blokk 2 első lépése kéri. Az offline B-terv is csak a Blokk 2-re szól.
- **Bizonyíték:** M1.F:165 „Utána nézd meg **magadnak** a Moodle-ben az M1 négy leckéjét” ↔ M1.F:269–270 „**Technikai belépés, kezdőpont (5–7’)** … Mindenki lépjen be a Moodle-be”
- **Hatás:** A 0–5’ sáv belépési gondokkal telik, vagy a tanuló visszajelzés nélkül választ feladatot. Wifi-leállásnál a Blokk 1-re nincs terv.
- **Javaslat:** A belépés kerüljön a Blokk 1 instrukciójának elejére; a 0–5’ sáv és a privát jelleg nem változik. A Blokk 2 1. lépése maradjon „kezdőpont”. A B-terv mondja ki, hogy a Blokk 1 betűs önbecslése (A–D) Moodle nélkül, fejből is elvégezhető.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-8**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia (D12, D13)
- **Hely:** M1.F:47; :175; :303–315 ↔ HUB:258; M1.F:36, :95
- **Probléma:** Az M1.F 6–20 fős plenáris peulaként van megírva (név nélküli cetlik, nagyköri kérdés–válasz). A hub szerint viszont egyéni vagy kiscsoportos támogatás, és a kötelező résztvevők (csak a kapun bukottak) a pilotban várhatóan kevesen lesznek.
- **Bizonyíték:** M1.F:47 „**Létszám:** 6–20 fő” ↔ HUB:258 „facilitált, strukturált javítási alkalom (egyéni vagy kiscsoportos támogatás)”
- **Hatás:**
  - 1–3 résztvevőnél a név nélküli gyűjtés (:305) és a „Ki az, aki inkább a Joharinál akadt el?” (:313) gyakorlatilag azonosít. Ez ütközik a :36 elvével („Nem tesszük ki névvel…”).
  - Egyéni alkalomra a peulafájl nem veszi át a HUB:258 safer-working mondatát; csak a mellékes 1:1 pontnál szerepel (:95).
- **Javaslat:**
  - A létszámsort igazítsd a hubhoz.
  - Egy rövid jegyzet a kis létszámú változatra: 1–5 főnél a Blokk 3 a tanuló saját kapus visszajelzéséről szóló rövid beszélgetés, név nélküli gyűjtés nélkül.
  - Egyéni alkalomnál a HUB:258 safer-working mondata szó szerint kerüljön át (HUM-SAFE-02).
  - A blokkidők és a 45’ változatlanok.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A megerősítés után fut; a safer-working szabály a hubban és a kánoni gate-dokumentumban él.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-9**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** pedagógia (D13)
- **Hely:**
  - HUB:147–148 ↔ M1.A:168–169, :270
  - HUB:178, :196, :216, :221–222 ↔ M1.F:53–57, :84–86, :115
  - HUB:276–278 ↔ M1.B:164–167 és a 4.4 szakasz (:431–478)
- **Probléma:** A hub peula-összefoglalói három ponton mást írnak elő, mint a részletes peulafájlok. Ez a 3. csoport fájljait érinti.
- **Bizonyíték:** HUB:148 „5–15’ – Nagy Johari-ablak megrajzolása, példák a 4 mezőre.” ↔ M1.A:270 „A ‘Vakfolt’ és az ‘Ismeretlen’ mezőt most békén hagyjuk.”
- **Hatás:**
  1. A hubból készülő képző a Vakfolt-mezőre is példát kérhet, amit az M1.A szándékosan nem nyit meg (:273–274).
  2. Az M1-HUB-POSZ-02 fogalomtérkép-asset „M1.F cél 4”-re és az „M1.F peula-fájl részleteire” hivatkozik, de az M1.F-ben nincs 4. cél és nincs fogalomtérkép-lépés (csak :82 és :379 említi). Legyártott eszköz marad használati utasítás nélkül. A jegyzetlap is eltér: „leckénként 1 gondolat, 1 kérdés” ↔ „1 mondat + 1 kérdés”.
  3. A hub analitikája egy M1.B végi, 1 perces, név nélküli, 1–5 skálás kérdésre épít, ami az M1.B percbontásában nincs, így az adat nem keletkezik.
- **Javaslat:** EMBERI DÖNTÉS (modulgazda): a részletes peulafájl-e az irányadó. Ha igen:
  - a HUB:147–148 és :221–222 igazodjon az M1.A/M1.F percbontásához;
  - a fogalomtérkép vagy bekerül az M1.F 4.3 mini-összegzésébe (:340–343, időbővítés nélkül), vagy az asset és a „cél 4” hivatkozás kikerül;
  - az M1.B-végi kérdés vagy bekerül a 4.4.2-be a 40–45’ keretben, vagy kikerül a hub analitikájából.
  - A 45’ keret nem változik.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT. Dokumentum-konzisztencia; a képző a peulafájlból dolgozik.
- **Hipotézis:** új
- **Verdikt:** —

**PED-G3-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** pedagógia (D12, részvételi biztonság)
- **Hely:** M1.A:276–282 ↔ :440–447
- **Probléma:** A résztvevők úgy ragasztják ki a cetlijüket, hogy az a csoport számára „látható” lesz. Nem tudják, hogy a képző később felolvassa, és a csoport megítéli, címke-e. A példák között a „nehéz nekem magamban” típusú cetlik is szerepelnek (:445–447).
- **Bizonyíték:** M1.A:282 „A közös táblára **csak olyan tartalom kerüljön, amit szívesen teszel láthatóvá a teljes csoportnak**.” ↔ M1.A:440–442 „A képző **leemel néhány cetlit** … Egyesével felolvassa a tartalmat, és megkérdezi: „Szerintetek ez inkább **megfigyelés** vagy **címke** magunkról?””
- **Hatás:** A hozzájárulás a láthatóságra szólt, nem a nyilvános elemzésre. A páros megosztás (:242–255) után a szerző könnyen azonosítható, és a saját nehézségét „címkeként” hallja minősíteni. Ez gyengíti a peula saját biztonsági keretét (:160–161).
- **Javaslat:** Két lehetőség, a blokkidők nem változnak:
  - a 4.2.3-ban egy mondattal jelezd előre, hogy néhány cetlit név nélkül felolvashatsz példaként;
  - vagy a 4.3.2 alapból az M1.A-MUNK-02 segédlet kész példacetlijeivel dolgozzon (:410).
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A cetlik önkéntesek, és a képző a „könnyedeket” választja; nem P0.
- **Hipotézis:** új
- **Verdikt:** —

---

LEVÁGVA: 2 további finding, súlyosságuk: 2×P2
- **PED-G3-11** · P2 · M1.A:372–381 és M1.B:128–133 · Az N-M1-05 és a mátrix 11. szakasz M1-04 sora megerősítve. Az M1.A 8 példamondatából 5 az M1.2 tétele (M1.2:536–537, :754–757); az M1.B 5 helyzetkártyájából 3 az M1.4 kapu-szituációja, mintamegoldással (M1.4:136–140, :475). Az „Írj mellé 1–2 újat” utasításhoz nincs kész új tétel, így a peula főleg felidéztet, új helyzetre kevéssé visz át. POST-PILOT.
- **PED-G3-12** · P2 (alacsony bizalom) · M1.B:385 ↔ M1.A:273–274, :301 · Az M1.B a valós kört egy héttel később az „M1.A-ban üresen hagyott Vakfolt-mező” visszakötéseként ajánlja. Az M1.A viszont azt ígérte, hogy a vakfolt feltárása „egy későbbi, bizalmibb fázis lesz a kvuca életében”. Az elem pozitív, passzolható és opcionális, ezért a kockázat alacsony. POST-PILOT.

**Elvetett hipotézisek**
- **N-M1-04:** az M1.A, M1.B és M1.F nem épít az M1.1 SLIDE 5 önreflexiójára (Greppel nincs „hozd el / mutasd meg” vagy SLIDE-hivatkozás). Ebben a csoportban így nincs ellentmondás a 2026-10-10-i döntéssel; az át nem vezetett döntés az M1.1 és a manifest scope-ja.
- **Mátrix 12. szakasz M1a, 1. pont (1–2 vs. 2–3 mondatos SBI):** a 3. csoport fájljai az M1.4-gyel egyezően 1–2 mondatot írnak (M1.B:22, :359). Az eltérés a hub és a KAPU oldalán van (1–2. csoport).
- **E-M1-069, „kiesett a ‘Mennyire segíti a fejlődésedet?’ kérdés”:** az M1.B:202 („min változtass, és mit tarts meg?”) lefedi, nem finding.
- **Mátrix 12. szakasz M1b, M1.F:171–172 (sorvégi két szóköz):** a pedagógia lencsén kívül esik, nem értékeltem.
