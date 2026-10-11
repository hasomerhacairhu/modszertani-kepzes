# 2026-10-11 Validált findingok – M1, nyelvi lencse, AP-2026-10-11-01

> **Audit trail — nem kánon, nem tanulói tartalom.** Read-only `/course-review M1 --lens language --run AP-2026-10-11-01`
> (`next-version` autopilot-futás). A tananyag a review alatt nem változott.
>
> - **Scope:** a teljes M1 modul, csak a hiányzó `language` lencse. A másik négy lencse (pedagógia, értékelés,
>   implementáció, biztonság-jog) a `2026-10-10 Validált findingok – M1 course-review, B sáv.md` riportban lefutott,
>   és a M1 a review-bázisa (82d0c7c) óta csak az M1.1-ben változott (N-M1-04, PR #29) — ezek újrahasznosítva (REUSED).
> - **Lencsék ebben a riportban:** language. **Run-ID:** AP-2026-10-11-01.
> - **Review-bázis:** `886165b` (a `02 Tervezet/` tartalma azonos a `main@213a4c5`-tel); nem commitolt változás a scope-ban: nincs.
> - **Read-only bizonyíték (kezdet):** `git diff HEAD -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`;
>   `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`.
> - **Read-only bizonyíték (mentés előtt):** `da39a3ee5e6b4b0d3255bfef95601890afd80709` / `da39a3ee5e6b4b0d3255bfef95601890afd80709` — egyezik a kezdő értékkel.
> - **Állapot:** VALIDÁLT (57/57 verdikt).
> - **Szerkezet:** I. riport · A. verifier-kontextus · B. verdiktek · C. nyers lencse-kimenetek (szó szerint; a helyi
>   abszolút útvonal-előtag repó-relatívra rövidítve, sorvégi szóközök törölve).

---

# I. M1 nyelvi lencse — validált riport (2026-10-11)

> Read-only review. Tananyag nem változott. Nyers findingok: C. melléklet (57: NYELV-G1-1…16, NYELV-G2-1…14,
> NYELV-G3-1…27); verdiktek: B. melléklet (három verifier, 57/57). Git-history a reviewereknél és a verifiereknél nem
> állt rendelkezésre: a restauráció/baseline kérdésre „baseline ismeretlen”, a súlyosság emiatt nem emelkedett.

## 1. Scope és futtatott lencsék

- **Scope:** a teljes M1 (9 fájl), három fájlcsoportban: G1 = hub, M1.1, M1.2 · G2 = KAPU, M1.3, M1.4 · G3 = M1.A, M1.B, M1.F.
- **Ténylegesen lefutott lencse ebben a riportban:** `language` (hungarian-editorial-reviewer, csoportonként egy ügynök;
  a levágott tételeket folytatással mind leadták: G1 16, G2 14, G3 27 — hiányos lencse nincs).
- **Újrahasznosítva (REUSED):** pedagógia, értékelés, implementáció, biztonság-jog — a `2026-10-10 Validált findingok – M1
  course-review, B sáv.md` riportból (review-bázis `82d0c7c`). A modul azóta csak az M1.1-ben változott (N-M1-04, PR #29);
  az ott érintett B sávos findingok a ledgerben `NEEDS_RECHECK`. Így az M1-re mind az öt lencse lefutott.
- **Kötelező biztonság-jog lencse:** a B sávban lefutott; ebben a riportban nem ismételtük (csak a hiányzó lencse futott).
- **Read-only bizonyíték:** a kezdő és a mentés előtti `git diff HEAD -- "02 Tervezet" | shasum` és
  `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` egyaránt `da39a3ee5e6b4b0d3255bfef95601890afd80709`.

**Számok (a verdiktsorokból):** MEGERŐSÍTVE + objektív 28 · EMBERI DÖNTÉS 7 (ebből 2 duplikátum) · ELVETVE 22 · bizonyíték-kapu 0.

## 2. Validált objektív findingok (28, mind P2)

Javítási út: `/hungarian-edit` fájlonként; ahol a hely `@source` (VO-szöveg), ott a javítás útja a hanggyártás fix packja
(a kurzusrepóban csak a nem-VO rész javítható). Minden látható szövegváltozás után `--pin-visible`; `@asset`-spec után
`media_manifest.py build`.

| ID | Hely | Probléma | Javítás és korlát (verifier) |
|---|---|---|---|
| NYELV-G1-2 | M1.2:906 | felső szintű ‘…’ idézőjel | „lusta vagy” „…” idézőjelben; opciók, ✅ marad |
| NYELV-G1-3 | M1.2:885, :934 | perjel kötőszó helyett tanulói mondatban | „értelmezés vagy címke”; a kulcs (Hamis ✅), a drop-zóna címke (:749) és a grafika marad |
| NYELV-G1-6 | M1.2:640 (`@source` M1.2-NAR-04-VO), :573 (spec) | a narráció „szóra vagy kifejezésre” kattintást kér, a Mark the Words csak szót jelöl (:631) | minimális: „vagy kifejezésre” törlése, a PED-G1-4 javításával összehangolva; VO-fix pack, utána spec + build; célszó, pontozás marad |
| NYELV-G1-8 | HUB:253 | kb. 60 szavas tanulói mondat, homályos „így” | bontás három mondatra; semmi nem eshet ki („Jó, ha tudod”, a három elem, M1.B-hivatkozás, „fogódzóként”) |
| NYELV-G1-9 | HUB:77 | „hogyan nem látunk” tükörfordítás; „saját szóval” | „hogy nem látunk…”, „a saját szavaival” (M1.1:55 szerint) |
| NYELV-G1-10 | HUB:132 | az I „rá” előzménye „a másik” | az előzmény megnevezése az M1.3:50 / M1.4:466 / KAPU:199 szerint; S, B marad |
| NYELV-G1-11 | HUB:220, M1.F:36 | „Megőrzésére” előzménye nem egyértelmű | „A mentorjegyzet megőrzésére” (Adatvédelem §3:69 és §5:151 szerint kánonból bizonyított); a szabály, a §3-hivatkozás, a „minimális adat” korlát marad |
| NYELV-G1-12 | HUB:249, KAPU:23 | „átmenet” = teljesítés helyett | „teljesítés(hez)”; küszöb, szintnevek, pontok érintetlenek; a „Vigyázz:” nem kötelező tétel |
| NYELV-G1-13 | HUB:266 | „modulonként” leckék helyett | „leckénként” |
| NYELV-G1-15 (részben) | HUB:177, :179, :183, :222; M1.1:66, :74, :15; M1.2:28, :741, :958 (+ M1.F:82, :379) | egybe-/különírás: fogalomtérkép, Moodle-oldal, mondatszinten, diagram-animáció, mondatok kategorizálása, klipek | csak ezek; a „bulletpontokkal” és a „személyes kapcsolás” kimarad; @asset sorok után build |
| NYELV-G2-1 | KAPU:87, M1.4:629 | „ők” előzmény nélkül az „Erős” mintamondatban | „ők” → „a többiek”, két helyen azonosan; szintnév, pont, sorkritérium marad |
| NYELV-G2-2 | M1.3:1029, :1032 | „Nézd rá” (tárgyas ragozás); én/te vált | „Nézz rá”, „rám” → „rád”; a „csoportra” marad |
| NYELV-G2-3 | M1.3:310 | „mindhármat” rossz előzménye | „mindhármat (S, B és I)”; opció, ✅ marad |
| NYELV-G2-5 | M1.3:1059 (`@source` NAR-06), :941 (spec); KAPU:200 | „Assignment” ↔ „SBI-beadandó” a tanulói szövegben | KAPU:200 „az M1.4 SBI-beadandóba”; a :1059 VO-fix packon át, a :941 build-del; a fejlesztői „Moodle Assignment” marad (L2: a NYELV-G3-12-vel egy lépésben) |
| NYELV-G2-6 | KAPU:109 | „A két feltétel … adnak” — számegyeztetés | „ad”; a Szabály B tartalma, a küszöb és a „Grade to pass” mondat szó szerint marad |
| NYELV-G2-7 | KAPU:132 | „érzés-helyett-hatás” tükörszerkezet (fordított jelentés) | „hatás helyett érzés”; item, opció, ✅ marad |
| NYELV-G2-11 | M1.4:611 | „vele” előzmény nélkül a rubrikacellában | „a beadvány írójával” (KAPU:75 szó szerint), az ERT-G2-5-tel egy lépésben |
| NYELV-G2-13 | KAPU:23, :30, :43, :97, :111, :113, :200, :271; M1.4:14, :448, :574, :633, :640; M1.3:984 | kéttagú összetételek kötőjellel; idegen előtagúak kötőjel nélkül | egybeírás (kapueredmény, kapuküszöb …), „copy-paste-barát”, „Assignment-kitöltés”; „KAPU-fájl” marad; rubrikaszöveg, küszöb nem változik |
| NYELV-G2-14 | M1.4:136 | „és közben … érkezik meg” időlogika | a „közben” törlése, a KAPU:196 alakjára |
| NYELV-G3-3 | M1.F:55 | „Le tud írni / mondani” → „le tud mondani” is | „Le tud írni vagy el tud mondani” |
| NYELV-G3-4 | M1.A:315, M1.F:330 | „kamera-lát” nem magyar szó | a modul meglévő alakja („amit egy kamera is felvenne” / „amit a kamera is lát”) |
| NYELV-G3-8 | M1.B:227, :229 | „Sound – hangerő” fordítási hiba | „hang”; ✅, sorrend, angol szó marad |
| NYELV-G3-10 | M1.B:476 | „ettől nem veszíted el” tárgy nélkül; „nem javítás” ↔ „javító próbálkozás” | „nem veszíted el a teljesítést”, „nem javító próbálkozás”; a validált BIZT-G3-1-gyel egy lépésben (L7) |
| NYELV-G3-11 | M1.F:270 | a képző magáról 3. személyben a felolvasott szövegben | „szóljon nekem, és nyitok neki új próbálkozást”; a bontás opcionális; BIZT-G3-1-gyel egy lépésben |
| NYELV-G3-12 | M1.F:270, :361; M1.B:476 | „M1.4 Assignment” a tanulói idézetekben | „az M1.4 SBI-beadandóban”; a képzői jegyzetekben az „Assignment” maradhat (L2, L7) |
| NYELV-G3-13 | M1.B:139, :365 (+ spec :102, notes :118) | a „B” két jelentésben ugyanazon a lapon | „a visszajelzést kapó (B)”; szerepnevek, DIA-01, forgás marad; spec build-del |
| NYELV-G3-15 | M1.A:517–518 | a vakfolt-meghatározásból kiesett „de mi nem” | „…mások látnak rajtunk, de mi nem.” (Glosszárium :135, M1.F:320) |
| NYELV-G3-24 | M1.F:81, :263 | „1 db” összefoglaló, de párban osztják ki | az „1 db” törlése; példányszámot nem találunk ki; a MUNK-01 formátummező marad |

## 3. Emberi döntést igénylő tételek — javasolt szöveg nélkül

| ID | Kérdés | Ki dönt |
|---|---|---|
| NYELV-G1-14 (= NYELV-G3-19) | Az SBI „S” elemének kánoni magyar neve: „helyzet” (Glosszárium:138, HUB:33, :231) vagy „szituáció” (HUB:241, KAPU:47 rubrikasor-név, M1.2:936, M1.4:482, M1.A:534, M1.B:181) — a 2. és a 3. kánoni forrás ütközik; a rubrikasor neve is érintett | modulgazda + értékelési felelős, a Glosszárium gazdájával |
| NYELV-G2-4 | A KAPU:55 S-„Erős” horgonya („idő ÉS/VAGY hely ÉS a helyzet szakasza”) melyik olvasata érvényes; a 4.1–4.2 nem dönti el. Az ERT-G2-5 S-horgony-átvezetése ettől függ | értékelési felelős |
| NYELV-G2-8 | A KAPU:79 4. rubrikasor vezérkérdésének „(megtartható kapcsolatban)” zárójele külön szempont vagy magyarázat | értékelési felelős / modulgazda |
| NYELV-G2-9 | Az SBI-sablon S-rése határozói („Amikor ma a játék közben…”) vagy tagmondatos („…voltunk”) — a sablon négy helyen (M1.3:803–805, :889–893; M1.4:470–471; MUNK-01 spec) ellentmond a saját példáinak | modulgazda; QA: értékelési felelős |
| NYELV-G3-16 (c) | Az M1.A:277 „tedd meg nyugodtan” gyakorlati vonzata (új cetlire írás, ha a 3 elfogyott) | modulgazda |
| NYELV-G1-7 | Az M1.1:926 „ez” kétértelműsége — a validált BIZT-G1-7 (kiskorú madrih önfeltárásának határa) nyelvi többlete; azzal egy döntésben | Memuna + szakmai lektor (BIZT-G1-7) |

## 4. Bizonyíték-kapuk

Nincs. (A NYELV-G1-2/G1-3 stb. nem gyermekvédelmi helyek; a M1-et érintő bizonyíték-kapuk a B sávos riportban.)

## 5. Elvetve (22)

NYELV-G1-1 (bevett fordulat, answer-key opció átírása szükségtelen) · G1-4 (természetes, VO-újragyártást nem indokol) ·
G1-5 (hallgathatósági preferencia) · G1-16 (stílus) · G2-10 (a konjunktív szabály kétszer kimondva előtte; félreolvasás
nem bizonyított) · G2-12 (stílus, Anna-szövegezés) · G3-1 (vonatkozás nem bizonyított) · G3-2 („mondotok” szabályos) ·
G3-5 (távirati képzői stílus) · G3-6 („kapus” bevett melléknév) · G3-7 (produktív szóalkotás) · G3-9 (érthető
helyreigazítás) · G3-14 (szabályos normamondat, kánoni keret) · G3-17 (a „4 fős trió” a modul következetes egysége) ·
G3-18 (érthető, regressziós kockázat) · G3-20 (stílusegységesítés, tömeges átírás) · G3-21 (regiszter-preferencia) ·
G3-22 (kánoni határ-mondat, nem változtatható) · G3-23 (távirati stílus) · G3-25 (a csere rontana) · G3-26 (levezethető) ·
G3-27 (az idősávok azonosítják a blokkot).

## 6. Következő lépés

- `/hungarian-edit` fájlonként a 28 objektív tételre (a VO-forrású részek kivételével): HUB (G1-8, G1-9, G1-10, G1-11, G1-12,
  G1-13, G1-15), M1.1 (G1-15), M1.2 (G1-2, G1-3, G1-15; a G1-6 `@source`-része VO), KAPU (G1-12, G2-1, G2-5, G2-6, G2-7,
  G2-13), M1.3 (G2-2, G2-3, G2-13; a G2-5 `@source`-része VO), M1.4 (G2-1, G2-11 az ERT-G2-5-tel, G2-13, G2-14),
  M1.A (G3-4, G3-15), M1.B (G3-8, G3-10, G3-12, G3-13), M1.F (G1-11, G1-15, G3-3, G3-4, G3-11, G3-12, G3-24).
- Sorrendi függés: NYELV-G3-10, -11, -12 a validált BIZT-G3-1 javításával egy lépésben; NYELV-G2-11 az ERT-G2-5-tel; az
  ERT-G2-5 S-horgonya a NYELV-G2-4 döntése előtt nem implementálható.
- Az emberi döntések a ledger Külső kapuinál.

---

# A. melléklet – verifier-kontextus

## M1 nyelvi lencse — verifier-kontextus és klaszter-térkép (fő munkamenet, 2026-10-11)

Findinglista: a riport C. melléklete — 57 nyers finding: NYELV-G1-1…16 (hub, M1.1, M1.2), NYELV-G2-1…14 (KAPU, M1.3, M1.4), NYELV-G3-1…27 (M1.A, M1.B, M1.F).

**Szabályok:** `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” (szó szerint a promptban); `.claude/rules/hungarian-editorial.md` (norma, 10 regressziós minta); a `next-version` felhatalmazás (2026-10-11): a pilot-freeze és a POST-PILOT nem halasztási ok; a 2026-10-10-i projektgazdai döntés 5. pontja (szükségtelen módosítás és Anna természetes szövegezésének romlása kerülendő) → „lehetne szebb” = ELVETVE; értékelési invariáns: answer key, küszöb, rubrikaszint jelentése nyelvi javítással nem változhat; N-M1-04 (HUM 12. szakasz) az M1.1 SLIDE 5-re; `@source` (VO) szöveg csak a hanggyártás útján változik (a finding attól még valós lehet, a javítás útja VO-fix pack). Git-history nincs a verifiernél: a restauráció/baseline kérdésre „baseline ismeretlen”. A B sávos validált M1-findingok (2026-10-10-i riport) nem ismételhetők; átfedésnél a nyelvi többlet számít.

**Klaszterek (egy tényállás, több finding — ugyanabba a hívásba):**

| Klaszter | Findingok | Tárgy |
|---|---|---|
| L1 | NYELV-G1-14, NYELV-G3-19 | az SBI „S” elemének két neve (helyzet ↔ szituáció); Glosszárium ↔ modul |
| L2 | NYELV-G2-5, NYELV-G3-12 | „Assignment” ↔ „SBI-beadandó” a tanulói szövegben (vö. validált IMPL-G2-7) |
| L3 | NYELV-G1-15, NYELV-G3-* (M1.F „fogalom-térkép”) | egybeírás; a G1-15 az M1.F:82, :379-et is említi |
| L4 | NYELV-G1-11 (HUB:220 ↔ M1.F:36) | „Megőrzésére” előzménye, mindkét fájlban |
| L5 | NYELV-G1-12 (HUB:249 ↔ KAPU:23) | „átmenet” = teljesítés |
| L6 | NYELV-G2-13 (KAPU, M1.4, M1.3) | kapu-/rubrika- összetételek egybeírása |
| L7 | NYELV-G3-10, NYELV-G3-11 | ugyanaz a hurokzárás-mondat (M1.B:476, M1.F:270), validált BIZT-G3-1 helye |

**Mit kérünk minden findingnál:** verdikt (MEGERŐSÍTVE / ELVETVE / EMBERI DÖNTÉS) és típus; ha a lencse objektívnak jelölte, de a javítás jelentést változtatna vagy a szándék nem dönthető el → EMBERI DÖNTÉS; ha a finding preferencia → ELVETVE; duplikátumnál a megtartandó ID; a javasolt szöveg nem ront-e (regressziós minták, kánoni mondat, answer key).

---

# B. melléklet – verifier-verdiktek

## VERIFIER V2 — NYELV-G2-1…14, NYELV-G3-12 (15 ID)

Adverzális verifikáció: AP-2026-10-11-01, M1 nyelvi lencse, G2-klaszter és NYELV-G3-12 (15 ID). Minden hivatkozott helyet visszaolvastam a jelenlegi fájlokban:
- `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`
- `…/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md`
- `…/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`
- `…/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md`
- `…/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md`

Minden idézet egyezik a fájllal. Git-history nem volt, ezért a restauráció/baseline kérdésre mindenhol: baseline ismeretlen, a súlyosság nem emelkedett.

- NYELV-G2-1 · MEGERŐSÍTVE · objektív · P2 · A KAPU:87 és az M1.4:629 „Erős” mintamondatában („…háromszor közbevágtál, … – jó lenne, ha ők is több teret kapnának.”) az „ők”-nek nincs előzménye. A forrás, az M1.3:259 még tartalmazza („félbeszakítottad a többieket”). · duplikátum: nincs (az ERT-G2-5 a :629-et nem érinti) · javítási korlát: csak „ők” → „a többiek”, a két helyen szó szerint azonosan. A szintnév, a pont és a sorkritérium nem változik. Pin kell.
- NYELV-G2-2 · MEGERŐSÍTVE · objektív · P2 · Az M1.3:1029 „Nézd rá a saját mondatodra” hibás tárgyas ragozás: a „ránéz valamire” tárgyatlan, a KAPU:198 helyesen „Nézz rá”-t ír. Ugyanebben a listában a :1032 első személyű („rám / a csoportra”), a :1033 viszont tegező („beszélsz-e”, „minősíted”). · duplikátum: nincs (a PED-G2-6 ugyanitt a sorrendről szól, nem a nyelvről) · javítási korlát: csak „Nézd” → „Nézz” és „rám” → „rád”. A „csoportra” marad, a pontok tartalma és sorrendje, valamint a „nem pontozott” besorolás nem változik. Pin kell.
- NYELV-G2-3 · MEGERŐSÍTVE · objektív · P2 · Az M1.3:310-ben a „mindhármat” előtt pontosan három elem áll („az érzés”, „viselkedés (B)”, „mit okozott (I)”), az S nincs köztük. Így a névmás az érzés–B–I hármasra is érthető, ami az érzést külön SBI-elemnek mutatja. · duplikátum: nincs · javítási korlát: csak a „(S, B és I)” beillesztése. Az opció, a ✅ és a visszajelzés többi része nem változik. Pin kell.
- NYELV-G2-4 · EMBERI DÖNTÉS · emberi-döntés · P2 · A KAPU:55 „idő ÉS/VAGY hely ÉS a helyzet szakasza” valóban kétféleképpen olvasható, és a 4.1–4.2 nem dönti el. A 4.2 (idő + szakasz → Erős) mindkét olvasattal összefér, a 4.1-ben egyik elem sincs meg. A „Rendben” sor kritériuma („nem köthető konkrét alkalomhoz”) pedig azt sugallja, hogy egy konkrét időpont önmagában is kiemelhet a „Rendben”-ből. A javasolt folyó szöveg így rögzítené a rubrikaszint jelentését: az értékelési felelős dönt. · duplikátum: nincs · javítási korlát: a kétértelmű szöveg az ERT-G2-5-tel kerülne át az M1.4:482/:586-ba, ezért az ERT-G2-5 S-horgonya ennek a döntésnek a függvénye, előtte nem implementálható.
- NYELV-G2-5 · MEGERŐSÍTVE · objektív · P2 · Egy fogalomra két név áll a tanulói szövegben: M1.3:886 „az M1.4 beadandóban”, M1.3:1059 (VO) „az Assignmentben”, KAPU:200 (tanulói visszajelzés) „add be az M1.4 Assignmentbe”. A manifest neve „M1.4 – SBI-beadandó” (vö. IMPL-G2-7). · duplikátum: nincs. Az L2 klaszterben a NYELV-G3-12-vel egy lépésben javítandó, más helyekről szól. Az IMPL-G2-7 csak a §3.1 címsort érinti. · javítási korlát: az M1.3:1059 `@source` VO-szöveg csak a hanggyártás fix packján át változik; a :941 asset-spec a `media_manifest build` útján. A fejlesztői „Moodle Assignment” megnevezés marad. Pin kell.
- NYELV-G2-6 · MEGERŐSÍTVE · objektív · P2 · KAPU:109: „A két feltétel konjunkció – csak együtt adnak átmenőt.” Az elhagyott alany a számnévi jelzős, egyes számú „a két feltétel”, mellette többes számú állítmány áll. Ez a 6. regressziós minta (szám/személy elcsúszás). · duplikátum: nincs · javítási korlát: kizárólag „adnak” → „ad”. A Szabály B tartalma, a küszöb (≥1 ÉS ≥5/8) és a „Grade to pass” mondat szó szerint marad.
- NYELV-G2-7 · MEGERŐSÍTVE · objektív · P2 · A KAPU:132 „érzés-helyett-hatás” angol szórendű tükörszerkezet. Magyarul azt jelenti, hogy a hatás áll az érzés helyén, ami nem hibatípus. A szándékot az M1.3:299 típusjelölése („érzés a viselkedés/hatás megnevezése nélkül”) és a KAPU „Rendben” I-szintje („Rossz érzés volt.”) egyértelműen „hatás helyett érzés”-nek mutatja. Szerzői, nem tanulói megjegyzés. · duplikátum: nincs · javítási korlát: csak a zárójeles lista harmadik tagja fordul meg. Item, opció és ✅ nem változik.
- NYELV-G2-8 · EMBERI DÖNTÉS · emberi-döntés · P2 · A 4. rubrikasor vezérkérdésében (KAPU:79) a „(megtartható kapcsolatban)” nem magyaros, és a korpuszban máshol nem fordul elő ebben az értelemben. Nem dönthető el, hogy külön szempont-e (a kapcsolat megőrzése) vagy csak magyarázat. Rubrikakérdés, ezért a szándékot az értékelési felelős vagy a modulgazda erősíti meg. · duplikátum: nincs · javítási korlát: addig nincs csereszöveg. A viselkedés ↔ személy logika semmiképp nem változhat.
- NYELV-G2-9 · EMBERI DÖNTÉS · emberi-döntés · P2 · Igazolt: a sablon (M1.3:803–805, :889–893; M1.4:470–471; MUNK-01 spec :523) S-súgója tagmondatot vár („voltunk”). A leckék S-példái viszont határozói szerkezetek (M1.3:428 „Amikor ma a játék közben…”), és a kánoni példák egyike sem követi az „…, és te …” vázat (M1.4:475, KAPU:87). Hogy a kötőszó vagy a súgó változzon, az tanítási sablon-döntés: a modulgazda dönt, az értékelési felelős QA-t ad, mert a KAPU:87 Erős-leírása a sablonra hivatkozik. · duplikátum: nincs (a PED-G2-1 a hosszról, az ERT-G2-1 a példamásolásról szól) · javítási korlát: mind a négy helyen egyszerre, a spec után `media_manifest build`. A KAPU:87 zárójeles mondata és a rések tartalma nem változik.
- NYELV-G2-10 · ELVETVE · — · P2 · Az M1.4:642 „Ha ennél kevesebb:” közvetlenül a konjunktív szabály kétszeri kimondása után áll (:637–638 felsorolás, :640 „minden sor ≥1 ÉS összpont ≥5/8”). Egy 0 pontos sor szó szerint is „kevesebb” a „legalább 1 pont”-nál, így a feltételezett félreolvasás nincs bizonyítva. A projektgazdai döntés 5. pontja szerint szükségtelen módosítás. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-11 · MEGERŐSÍTVE · objektív · P2 · Az M1.4:611 „Érthető, mi történt vele / a kvucával.” névmásának nincs előzménye. A rubrikában a visszajelzés címzettjére is érthető, ami megfordítja a hatás alanyát. A szándék levezethető: KAPU:75 „a beadvány írójával”, M1.4:484 „benned vagy a kvucában”. · duplikátum: részleges átfedés az ERT-G2-5-tel (annak Hely mezőjében benne van a :611). Nyelvi többlet a névmás megnevezése, amelyet egy szűk ERT-G2-5-javítás érintetlenül hagyhatna. · javítási korlát: az ERT-G2-5-tel egy lépésben, „vele” → „a beadvány írójával” (a KAPU:75 szó szerint). Ha az ERT-G2-5 a cellát szó szerint a KAPU:75-höz igazítja, ez a tétel abban teljesül. Szintnév és pont nem változik. Pin kell.
- NYELV-G2-12 · ELVETVE · — · P2 · Az M1.4:454–457 „Választhatsz: … vagy egy saját … helyzetet is hozhatsz” enyhe anakoluthon, de a jelentése teljesen egyértelmű. A javasolt csere („választhatsz egy saját, kitalált helyzetet”) a természetesebb „hozhatsz” igét gyengébbre cserélné. Ez stíluskérdés, amelyet a projektgazdai döntés 5. pontja (Anna-féle szövegezés megőrzése) kizár. · duplikátum: nincs · javítási korlát: — (a sor „Valós helyzetet – név nélkül sem – ne írj le” kitétele amúgy sem érinthető)
- NYELV-G2-13 · MEGERŐSÍTVE · objektív · P2 · A felsorolt helyeken a kéttagú összetételek kötőjellel állnak (pl. KAPU:111 „kapu-eredmény” ↔ KAPU:24/:26/:306 „kapueredmény”; M1.3:984 „kapu-feladatot” ↔ M1.3:1075 „kapufeladatba”). Ez AkH-hiba és fájlon belüli következetlenség, a KAPU:200-ban tanulói szövegben is. A „copy-paste barát” és az „Assignment kitöltés” helyesen kötőjeles. Az M1.4:574 és :633 címsorra nincs horgony-link a repóban. · duplikátum: nincs · javítási korlát: csak helyesírás. A „KAPU-fájl”/„Kapu-fájl” azonosító marad, rubrikaszöveg, küszöb és táblázati érték nem változik. Az M1.3:984 asset-spec a `media_manifest build` útján változik. Pin kell.
- NYELV-G2-14 · MEGERŐSÍTVE · objektív · P2 · Az M1.4:136 „…fél órát késik valaki, és közben hangosan röhögve érkezik meg” az egyetlen „közben”-es változat. Ugyanez a helyzet a KAPU:196-ban, az M1.B:129-ben és az M1.4-ILL-01 specben (:50) „közben” nélkül áll, és az érkezés időben nem a késés „közben” történik. · duplikátum: nincs · javítási korlát: csak a „közben” törlése, a KAPU:196 alakjára. A kártyacím, a helyzet tartalma és az ILL-01 spec nem változik. Pin kell.
- NYELV-G3-12 · MEGERŐSÍTVE · objektív · P2 · Az M1.F-en belül ugyanaz az activity hol „M1.4 SBI-beadandó” (:62, :64), hol „M1.4 Assignment” (:68, :270, :276, :355, :361, :395). A tanulóknak felolvasott idézetekben is az angol név áll (M1.F:270, :361; M1.B:476), holott a manifest neve „M1.4 – SBI-beadandó”. · duplikátum: nincs. Az L2 klaszterben a NYELV-G2-5-tel egy lépésben javítandó, más fájlokról szól. · javítási korlát: csak a tanulónak szóló idézetekben (M1.F:270, :361; M1.B:476). A felolvasott mondatban a nagykötőjeles „az M1.4 – SBI-beadandóban” helyett az M1.F:62-ben már használt „az M1.4 SBI-beadandóban” alak ajánlott. Az M1.B:476 és az M1.F:270 a validált BIZT-G3-1 helye (L7 klaszter), ezért azzal egy lépésben javítandó, és annak tartalmát nem írhatja felül. A képzői jegyzetekben az „Assignment” maradhat. A „(Moodle Assignment)” kiegészítés nem kötelező.

Összesítés:
- **MEGERŐSÍTVE: 10** (NYELV-G2-1, -2, -3, -5, -6, -7, -11, -13, -14, NYELV-G3-12)
- **ELVETVE: 2** (NYELV-G2-10, -12)
- **EMBERI DÖNTÉS: 3** (NYELV-G2-4 és -8: értékelési felelős; NYELV-G2-9: modulgazda, az értékelési felelős QA-jával)
- **bizonyíték-kapu: 0**

Duplikátumok:
- Teljes duplikátum nincs.
- Részleges átfedés: NYELV-G2-11 ↔ ERT-G2-5. Megtartandó a NYELV-G2-11 is, de csak az ERT-G2-5-tel egy lépésben.
- Egy lépésben javítandó: a NYELV-G2-5 és a NYELV-G3-12 (L2 klaszter), valamint a NYELV-G3-12 M1.B:476-os és M1.F:270-es része a BIZT-G3-1-gyel (L7 klaszter).
- Sorrendi függés: az ERT-G2-5 S-horgonya (M1.4:482/:586) a NYELV-G2-4 döntése előtt nem implementálható.

## VERIFIER V1 — NYELV-G1-1…16, NYELV-G3-19 (17 ID)

AP-2026-10-11-01 · M1 nyelvi lencse · V1 verifikáció (NYELV-G1-1…16 és NYELV-G3-19). Mind a 17 hivatkozott helyet a jelenlegi fájlban olvastam vissza. Git-history nem állt rendelkezésre, ezért minden tételnél: baseline ismeretlen. Fájlt nem szerkesztettem.

NYELV-G1-1 · ELVETVE · objektív · P2 · Az M1.1:864 egyezik („Amit mások látnak rólad, de te nem ✅”). Az „amit mások látnak rólad” a Johari-leírásokban bevett magyar fordulat, a jelentése egyértelmű; a vonzathiba nem bizonyítható. A finding egy answer-key opció szövegét írná át pusztán a :870-nel való egyezés kedvéért, ezt a 2026-10-10-i döntés 5. pontja kerülendőnek mondja · – · –

NYELV-G1-2 · MEGERŐSÍTVE · objektív · P2 · Az M1.2:906 egyezik: „(‘lusta vagy’)” felső szinten áll. A lecke többi ‘…’ alakja mind „…” idézeten belül van: :168, :171, :364, :367, :550–554 narrációban, :199, :392, :877, :917, :923 visszajelzésben. A hungarian-editorial tipográfiai szabálya („…”, beágyazva ‘…’) ezt kifejezetten előírja · – · Csak az idézőjel cserélődik. Az opciók és a ✅ maradnak, pin kell.

NYELV-G1-3 · MEGERŐSÍTVE · objektív · P2 · A :885 („Az értelmezés / címke mindig rossz…”) és a :934 egyezik. A szabály szerint a „/” helyett rendes mondat kell, és a „vagy” alakot a lecke maga is használja (:366 „Értelmezés vagy címke”) · – · A kulcs (Hamis ✅) és a visszajelzések maradnak. A drop-zóna címkéje (:749) és a grafika (:225, :344) nem változik.

NYELV-G1-4 · ELVETVE · objektív · P2 · Az M1.1:644 egyezik („amiket még te sem próbáltál ki”). A mondat természetes magyar, és következetes a :471 „senki nem tud rólad – még te sem” definícióval. Az a hatás, hogy „mintha mások már kipróbálták volna”, a szövegből nem következik. Egy `@source` VO újragyártását nem indokolja · – · –

NYELV-G1-5 · ELVETVE · objektív · P2 · Az M1.2:548 és :553–554 egyezik. Felolvasva a „megfigyelés–értelmezés különbsége” és az idézett tagmondat alanyként érthető, a hangsúly elválasztja. Ez hallgathatósági preferencia, nem bizonyított hiba, és VO-újragyártással járna; a döntés 5. pontja szerint ELVETVE · – · –

NYELV-G1-6 · MEGERŐSÍTVE · objektív · P2 · Valós ellentmondás. A :640 narráció „minden olyan szóra vagy kifejezésre” kattintást kér, a :631 szerint viszont „csak egyes szavak jelölhetők, kifejezés nem”; a :573 spec ugyanígy „szóra/kifejezésre”. A PED-G1-4 (:618, :629, :651) a megfigyelés/tény állításról szól, nem erről, ezért nem duplikátum · – · A javítás útja a VO-fix pack, utána a :573 spec és build. A javasolt betét („ha a címke több szóból áll, mindegyikre”) új tippet ad a feladathoz. A minimális javítás a „vagy kifejezésre” törlése, a dián látható utasítással és a PED-G1-4 javításával összehangolva. Célszó és pontozás nem változik.

NYELV-G1-7 · EMBERI DÖNTÉS · emberi-döntés · P2 · Az M1.1:926 egyezik. Az „ez” mutathat a nyitott terület tágítására és az önfeltárásra is. A mondat a kiskorú madrih önfeltárásáról szól, ez gyermekvédelmi határeset, ezért kétség esetén emberi döntés · Duplikátum: a validált BIZT-G1-7 (K6, Memuna + szakmai lektor) a megtartandó, ez a finding csak nyelvi többletként csatolandó hozzá · A döntésig nincs szövegváltozás, a „nem kell mindent kitenned” korlát nem törölhető.

NYELV-G1-8 · MEGERŐSÍTVE · objektív · P2 · A HUB:253 egyezik. Egyetlen, kb. 60 szavas tanulói mondat. A zárójeles betét a felsorolás és az „így” közé ékelődik, ezért nem egyértelmű, mire utal az „így”. A hungarian-editorial két normát is sért: hosszú beágyazott mondat, névmási referencia · – · Minimális bontás. Nem eshet ki semmi: „Jó, ha tudod”, a három elem, az M1.B-hivatkozás és a „fogódzóként” (9. regressziós minta). Új állítás nem kerülhet be.

NYELV-G1-9 · MEGERŐSÍTVE · objektív · P2 · A HUB:77 egyezik („saját szóval elmagyarázni, hogyan nem látunk mindent magunkból”). A „hogyan nem látunk” tükörfordítás, és módhatározói olvasatot ad. A lecke saját mikrocélja (M1.1:55) „vagyis azt, hogy nem látunk mindent magunkból” · – · Csak a „hogyan” → „hogy” csere és a „saját szóval” → „a saját szavaival”. A kompetencia és az „ezért…” rész marad.

NYELV-G1-10 · MEGERŐSÍTVE · objektív · P2 · A HUB:132 egyezik („B – mit csinált a másik; I – hogyan hatott rá / a csoportra”). A „rá” legközelebbi előzménye „a másik”, a kánon szerint viszont az I az íróra vagy a csoportra gyakorolt hatás: M1.3:50 „hogyan hatott rád / a kvucára”, M1.4:466, KAPU:199 · – · Csak az előzmény megnevezése. Az S, a B és a „/ a csoportra” marad.

NYELV-G1-11 · MEGERŐSÍTVE · objektív · P2 · A HUB:220 és az M1.F:36 egyezik; a „Megőrzésére” előzménye nem egyértelmű. A finding előfeltételére van válasz: az Adatvédelem §3:69 „Mentori fejlesztési jegyzet” sora a nem Moodle-ben vezetett mentori jegyzetet a meta-napló sora szerinti jogalappal és azonos megőrzéssel kezeli, a §5:151 pedig kimondja, hogy a megőrzés a mentori jegyzetre vonatkozik. Így a „A mentorjegyzet megőrzésére” kánonból bizonyított, DPO-döntés nem kell · L4-klaszter: az M1.F:36 ugyanez a tényállás. Ha a G3-ban van rá külön finding, ez a megtartandó · Csak az előzmény nevesítése. A szabály, a §3-hivatkozás és a „minimális adat” korlát marad. A sor-hivatkozás átírása (meta-napló → „Mentori fejlesztési jegyzet” sor, §5:151) nem része ennek a findingnak, ilyen szerkesztés nem kerülhet be.

NYELV-G1-12 · MEGERŐSÍTVE · objektív · P2 · A HUB:249 („az átmenethez nem elég”) és a KAPU:23 („az átmenethez kevés”) egyezik. Az „átmenet” jelentése ‘transition’, nem a kapu teljesítése; ez jelentést torzító szóválasztás egy küszöbmagyarázatban · L5: a KAPU:23 a G2 hatóköre, ha ott külön finding van, egy lépésben kell javítani · Csak az „átmenet” → „teljesítés”. A küszöb (≥5/8, ≥1 pont soronként), a szintnevek és a pontok érintetlenek. A „Vigyázz:” → „Figyelem:” rész preferencia, nem kötelező.

NYELV-G1-13 · MEGERŐSÍTVE · objektív · P2 · A HUB:266 egyezik („M1.1–M1.4 activity completion modulonként”). A korpuszban a „modul” az M0–M7 + Z egység, az M1.1–M1.4 egy modul leckéi, így a szó két fogalmat jelöl. Grep szerint ez a fordulat csak itt fordul elő · – · Csak „leckénként”, más nem változik.

NYELV-G1-14 · EMBERI DÖNTÉS · emberi-döntés · P2 · Valós kánoni eltérés. A Glosszárium:138 és a HUB:33, :231 „Helyzet”-et ír. A HUB:241, a KAPU:47 (rubrikasor neve), az M1.2:936, az M1.4:482 és az M1.B:181 „Szituáció”-t. Az M1.B:229 a kettőt rokon értelműként kezeli („szituáció / helyzet”). A HUM-fájlban nincs erről lezárt döntés. A 2. és a 3. kánoni forrás ütközik, és a rubrikasor neve is érintett, ezért magunktól nem választhatunk · Megtartandó, a G3-19 ennek a duplikátuma · A döntésig nincs csere, a rubrikasor nevét döntés nélkül tilos átírni. A döntés lehet az is, hogy a Glosszárium rögzíti a szinonimát.

NYELV-G1-15 · MEGERŐSÍTVE (részben) · objektív · P2 · Az idézett helyek egyeznek. Helyesírási hiba és ezért javítandó: „fogalom-térkép” (HUB:177, :183, :222; kimaradt a HUB:179 nagybetűs „Fogalom-térkép”), „Moodle oldal” (M1.1:74, M1.2:28), „mondat-szinten” (M1.2:741), „diagram animáció” (M1.1:66), „mondat kategorizálás” (M1.2:958), „klippek” (M1.1:15; a :11 „klipek”) · L3: az M1.F:82, :379 a G3 fogalomtérkép-findingjával közös. Ott elég egy javítás, ez a finding a megtartandó a G1 helyekre · Kimarad a „bulletpontokkal” (M1.1:762): fejlesztői sorban az angol szakszó a szabály szerint maradhat, ez preferencia. Kimarad a „személyes kapcsolás” is: nem bizonyított hiba. A „diagram animáció” AkH szerinti alakja „diagramanimáció”. A „diagram-animáció” csak a HUB:81-gyel való egyezés miatt fogadható el, normaként nem szerepeltethető. Az @asset sorok (HUB:177, :179, :183, M1.1:15) után build kell.

NYELV-G1-16 · ELVETVE · objektív · P2 · A HUB:8 egyezik, de a kifogások stílusbeliek. „A mikroleckék … haladnak” és „M1.A-t … végezze”: érthető, a kontextus (online → peula) egyértelmű. A névelőt ugyanez a sor máshol is elhagyja („M1.B előtt érdemes leadni”), és a csupa nagybetűs ELŐTT is kiemelés-ízlés. A javasolt teljes mondatcsere a döntés 5. pontja szerint szükségtelen módosítás · – · –

NYELV-G3-19 · EMBERI DÖNTÉS · emberi-döntés · P2 · Az M1.A:534 („Szituáció – Viselkedés – Hatás.”) és az M1.F:343 („helyzet – viselkedés – hatás”) egyezik. Ugyanaz az L1 tényállás, mint a G1-14 · Duplikátum → a NYELV-G1-14 a megtartandó. A G3-19 helyei (M1.A:534, M1.B:181, M1.F:338, :343) beolvasztandók · Mint a G1-14-nél.

NYELV-G3-12: verdikt nem kértek, a G1-ben nincs vele átfedés. A V3 hívás adja.

Összesítés: 10 MEGERŐSÍTVE (G1-2, G1-3, G1-6, G1-8, G1-9, G1-10, G1-11, G1-12, G1-13, G1-15 részben), 4 ELVETVE (G1-1, G1-4, G1-5, G1-16), 3 EMBERI DÖNTÉS (G1-7, G1-14, G3-19). Bizonyíték-kapu: 0. Duplikátumok:
- A G3-19 a G1-14 duplikátuma; a G1-14 a megtartandó.
- A G1-7 a B sávos BIZT-G1-7 (K6) nyelvi többlete; a BIZT-G1-7 a megtartandó.
- Klaszterátfedések, amelyeket a V3 hívás egyeztet: L3 – a G1-15 és a G3 M1.F fogalomtérkép-findingja; L4 – a G1-11 és az esetleges G3-finding az M1.F:36-ról; L5 – a G1-12 és az esetleges G2-finding a KAPU:23-ról.

## VERIFIER V3 — NYELV-G3-1…27, a G3-12 és a G3-19 nélkül (25 ID)

Adverzális verifikáció, M1 nyelvi lencse, G3 (25 ID). Minden idézett helyet visszaolvastam a jelenlegi fájlokban:
- 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md
- 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md

Restauráció vagy baseline: mind a 25 ID-nél „baseline ismeretlen”, ezért egyik súlyosság sem emelkedik. Bizonyíték-kapu nincs.

NYELV-G3-1 · ELVETVE · objektív · P2 · Az idézet egyezik (:302, :304), de nem bizonyítható, hogy az „ilyen lapjai” csak a cetlikre mutathat. A záró üzenet (:516–519) ugyanezt a fordulatot („Ez normális, nem azt jelenti, hogy ‘rossz madrih vagyok’”) éppen a vakfoltokhoz köti. A betoldás-hipotézis csak feltételezés, és a „lényeg” ismétlése ízlés kérdése · — · A bekezdések átrendezése megváltoztathatná a vonatkozást.

NYELV-G3-2 · ELVETVE · objektív · P2 · A „mondotok” (:314) a kötőhangzós, kettős mássalhangzóra végződő tövű igék szabályos többes szám 2. személyű alakja (vö. tartotok, küldötök), nem hiba. A „mondtok” csak gyakoribb változat, a csere ízlés kérdése · — · —

NYELV-G3-3 · MEGERŐSÍTVE · objektív · P2 · Az M1.F:55 „Le tud írni / mondani **1 mondatot**” alakban az igekötő mindkét igére vonatkozik, így „le tud mondani” (lemond) is kiolvasható. A tanulói nyelvű célmondat valóban félreérthető, és a szabályzat szerint a perjel helyére rendes mondat kell · — · Csak az „írni vagy el tud mondani” szerkezet változhat; az „1 mondatot” és az „1 kérdést” marad.

NYELV-G3-4 · MEGERŐSÍTVE · objektív · P2 · A „(kamera-lát)” az M1.A:315-ben és az M1.F:330-ban szerepel. Ez nem szabályos szóalkotás (főnév + puszta igető), és a fogalomnak a modulban van bevett alakja: M1.A:362, M1.B:236, M1.F:325 „amit egy kamera is felvenne”; M1.A:398 „amit a kamera is lát” · — · Csak a modulban már meglévő két alak egyike használható. Az M1.F-MUNK-01 spec „kamera-mondat” szavához nem kell nyúlni.

NYELV-G3-5 · ELVETVE · objektív · P2 · A „minden csoportnál meghallgat 1–2 percet” (:502) a képzői forgatókönyv bevett távirati stílusa, és egyértelmű. A tárgyesetű időtartam köznyelvben elfogadott; a „vonzathiba” nem bizonyított · — · —

NYELV-G3-6 · ELVETVE · objektív · P2 · A „kapus” a korpusz bevett melléknévi alakja: „kapus elem”, „kapus beadandó”, „kapus completion” (LMS-hozzáférhetőségi sztenderd :76/:78, M4.1, M4.2, H5P runtime acceptance :92, Program terv :232). A futballkapus-félreértés nem bizonyított, és a „kapun kapott visszajelzés” változattal nem két külön fogalomról van szó · — · —

NYELV-G3-7 · ELVETVE · objektív · P2 · Az „újraértettem” (M1.F:85, :226 spec) szokatlan, de az „újra-” előtagú szóalkotás produktív (újranéz, újragondol). Nem bizonyított nyelvi hiba, a csere ízlés kérdése. Ráadásul build-utat igényelne (M1.F-MUNK-02) · — · —

NYELV-G3-8 · MEGERŐSÍTVE · objektív · P2 · Az M1.B:227 „D: Sound – hangerő” és a :229 „nem hangerő” tényleges fordítási hiba: a „sound” jelentése hang, a „hangerő” angolul volume. Ez a nyelvi többlet; a levágott, nem validált ERT-G3-12 az elosztó funkciójáról szól (kitöltő zaj), nem a fordításról · Átfedés: ERT-G3-12 (levágott, nem validált); a fordítási tényállásra ez a megtartandó · A ✅, az opciók sorrendje és az angol szó marad. Ha egy későbbi értékelési javítás az elosztót cseréli, a kettőt egy lépésben kell kezelni.

NYELV-G3-9 · ELVETVE · emberi-döntés · P2 · A „Nem az a cél, hogy mindent ‘becukrozzunk’, hanem hogy beszéljünk – címkézés helyett.” (:249) a kérdés kontextusában érthetően helyreigazít: nehéz dolgot ki lehet mondani, csak címke nélkül. Nem biztonsági vagy jogi tétel, és az, hogy az M1.F:338 másként fogalmaz, nem hiba · — · —

NYELV-G3-10 · MEGERŐSÍTVE · objektív · P2 · Az M1.B:476 „ettől nem veszíted el” után a határozott ragozás tárgya csak a „kaput” lehetne, ami értelmetlen; az M1.F:270 kiírja: „A teljesítését ettől nem veszíti el”. A „nem javítás” a tanulói szövegben összemosható a „javító próbálkozás” szakszóval, amelytől a :478 képzői jegyzet kifejezetten elválasztja · L7-ben nem duplikátum: más mondat és más hiba, mint a G3-11; mindkettő megtartandó · Egy lépésben a validált BIZT-G3-1 átvezetésével (ugyanez a mondat). A próbálkozás-logika és a „legjobb megerősített eredmény” szabály nem változik; tárgyként a „teljesítést” kell kiírni.

NYELV-G3-11 · MEGERŐSÍTVE · objektív · P2 · Az M1.F:270 felolvasandó szövegében a képző előbb első személyben beszél („szólj, segítek”), majd önmagáról harmadik személyben: „ehhez kérje meg a képzőt, hogy nyisson neki új próbálkozást”. A képző szájából ez önellentmondás · L7: nem duplikátum, megtartandó · A kötelező javítás az önhivatkozás; a három bekezdésre bontás opcionális, és csak tartalmi változtatás nélkül megengedett. A BIZT-G3-1 ugyanerre az idézetre vezet át kánoni korlátot, ezért egy lépésben kell elvégezni; a „legjobb megerősített eredmény” mondat marad.

NYELV-G3-13 · MEGERŐSÍTVE · objektív · P2 · Ugyanazon a lapon a „B” két jelentésben áll: M1.B:136 „Volt **B**?” (viselkedés), majd :139 „B hogyan érezte magát?” és :365 „a B-érzést” (szerep). Ugyanez áll az M1.B-MUNK-01 specben (:102) és a notes-ban (:118) · — · Csak a minimális egyértelműsítés jöhet szóba („a visszajelzést kapó (B)”). Az A/B/C szerepnevekhez, a DIA-01-hez és a forgáshoz nem szabad nyúlni; az @asset spec csak a build-úton változhat.

NYELV-G3-14 · ELVETVE · objektív · P2 · A „Figyeljetek arra, hogy amit a másik mond, azt nem visszük tovább…” (:255) kijelentő módú normamondatként szabályos és természetes (vö. M3.B:346, :503 „nem visszük tovább pletykaként”). Nyelvtani hiba nem bizonyított, és a gyermekvédelmi titoktartási keretben a szükségtelen átírás kockázat. A második, HUM-SAFE-01-es kánoni mondatot a finding sem érinti · — · —

NYELV-G3-15 · MEGERŐSÍTVE · objektív · P2 · Az M1.A:517–518 „vannak, amiket mások látnak rajtunk” minősítő nélkül a Nyitott mezőt is lefedi. Ez ellentmond a Glosszárium :135 meghatározásának („amit mások látnak, én nem”) és az M1.F:320-nak („mások látnak rajtad, de te nem”). A kötelező záró üzenetről van szó · — · Csak a „, de mi nem” minősítő kerül be, más nem változik.

NYELV-G3-16 · EMBERI DÖNTÉS (bontva) · emberi-döntés · P2 · Az idézet egyezik (:276–277). (c) A „tedd meg nyugodtan” gyakorlati vonzata nem dönthető el: új cetlire kell-e írni, ha a 3 cetli (:230) elfogyott? Ez a modulgazdára tartozik, és a 4.2.3 önkéntességi mondatai (:282) nem gyengülhetnek. (a) A személyváltás („aki szeretné” → „a cetlidet”) a szóbeli instrukcióban bevett, és (b) a „felhelyeznél” szabályos szó: mindkettő ELVETVE (ízlés) · — · Az (a) és (b) részhez nem kell nyúlni; a (c) részhez a döntésig ne nyúlj.

NYELV-G3-17 · ELVETVE · objektív · P2 · A „2 maradékfős eset” (:323) tömör képzői jegyzet, a :322 alapján egyértelműen visszafejthető. A „4 fős trió” a modul következetes csoportegység-neve (:302, :321, :322, :334, az M1.B-MUNK-01 technikai mezője :106, a DIA-01 spec :274). A csere szükségtelen, és asset-specet is érintene · — · —

NYELV-G3-18 · ELVETVE · objektív · P2 · A :478 zárójeles képzői jegyzet nehézkes, de érthető. A „tehát” az első mondatból következik (a KAPU megengedi az önkéntes újrapróbálást), így a finding logikai állítása nem áll. A próbálkozás-logika átfogalmazása regressziós kockázat, kimutatható haszon nélkül · — · —

NYELV-G3-20 · ELVETVE · objektív · P2 · A Cél-listák szerkezeti egyenetlensége (pl. M1.A:183–185) alacsony bizalmú, több fájlra kiterjedő stílusegységesítés lenne. Ezt a 2026-10-10-i projektgazdai döntés 5. pontja (a szükségtelen módosítás kerülendő) és a tömeges átírás tilalma kizárja; a finding maga is jelentésváltozás-kockázatot jelez · — · —

NYELV-G3-21 · ELVETVE · objektív · P2 · Alacsony bizalmú regiszter-preferenciák képzői szövegben: „FAQ”, „a tech”, „tanuló-lab”, „Normalizálni”. A „kapuproduktum” kánoni szó (Gyermekvédelem release gate). A javasolt „Kapcsolás az M1.4 – SBI-beadandóhoz” ráadásul a G3-12 és a BIZT-G3-1 tárgyába nyúlna. A „tanuló-lab” helyére a finding maga sem tud biztos szót · — · —

NYELV-G3-22 · ELVETVE · objektív · P2 · Az M1.A:282 határ-mondata („érzékeny magáninformáció megosztása nem feladat”) szabályos: a „magán-” előtag produktív. A hivatali hangnem ízlés kérdése. A mondatot a B sáv riportja (:2782) szó szerint mintaként idézi egy nyitott gyermekvédelmi döntéshez, és a javasolt „magánügyeket” szó jelentésben eltér az „információ”-tól. Ezt a kánoni határ-mondatot nem szabad változtatni · — · —

NYELV-G3-23 · ELVETVE · objektív · P2 · Az M1.A:286, :447, az M1.B:413 és az M1.F:265 a képzői forgatókönyv bevett távirati stílusa; a megbízás szerint ez nem hiba. A töredékek a kontextusból érthetők · — · —

NYELV-G3-24 · MEGERŐSÍTVE · objektív · P2 · Fájlon belüli működési ellentmondás. Az M1.F:81 eszközlistájában és a :263-ban „1 db kinyomtatott, 1 oldalas összefoglaló” áll, a :263 viszont „ezt osztod ki, és **párban átbeszélik**”, a MUNK-01 purpose mezője (:191) pedig „a csoport párban dolgozik vele”. Egy példánnyal a B-terv nem működik · — · Csak az „1 db” törölhető; az „1 oldalas” marad. Példányszámot nem szabad kitalálni, és az M1.F-MUNK-01 „1 db A4, 1 oldal” formátum-mezőjéhez nem kell nyúlni.

NYELV-G3-25 · ELVETVE · objektív · P2 · A „milyen szavakat adunk a másiknak magáról” (:527) érthető, szándékos kulcsüzenet: a madrih szókincset ad a másik önképéhez. A javasolt „milyen szavakkal beszélünk a másiknak saját magáról” ezt a jelentést elveszítené · — · A javasolt szöveg rontana.

NYELV-G3-26 · ELVETVE · objektív · P2 · (1) Az M1.F:264 „A nyert időt visszaadhatod” a szerkezetből levezethető: ha a Blokk 3 előrekerül, a 25–40’ sáv felszabadul, és visszamehet a csendes pótlásra. Nem kell hozzá emberi döntés. (2) Az M1.B:395 „ezt a 2 percet” előzménye ugyanebben a mondatban áll („hagyj rá 1–2 percet”). (3) Az M1.B:350 „figyeli a checklistet” távirati összefoglaló; a lépéseket a :362–365 részletezi · — · —

NYELV-G3-27 · ELVETVE · objektív · P2 · A percbontás és a blokkfejlécek mind a négy blokknál eltérő címkét használnak (:164–167 ↔ :173, :253, :401, :431), az idősávok viszont azonosak, így a blokk egyértelműen azonosítható. Egyetlen fejléc átnevezése stílusegységesítés lenne · — · —

Összesítés:
- MEGERŐSÍTVE: 8 (NYELV-G3-3, -4, -8, -10, -11, -13, -15, -24), mind objektív P2
- ELVETVE: 16 (NYELV-G3-1, -2, -5, -6, -7, -9, -14, -17, -18, -20, -21, -22, -23, -25, -26, -27)
- EMBERI DÖNTÉS: 1 (NYELV-G3-16, csak a (c) rész; az (a) és (b) rész elvetve)
- Bizonyíték-kapu: 0

Duplikátumok és átfedések:
- L7: a NYELV-G3-10 és a -11 nem duplikátum (más mondat, más hiba), mindkettő megtartandó; mindkettőt a BIZT-G3-1-gyel egy lépésben kell javítani.
- A NYELV-G3-8 csak részben fedi a levágott, nem validált ERT-G3-12-t; a fordítási tényállásra a G3-8 a megtartandó.
- A NYELV-G3-21 utolsó tétele átfedne a G3-12-vel, de a G3-21 elvetve.

Hiányzó ID nincs.

---

# C. melléklet – nyers lencse-kimenetek (szó szerint)

## LENCSE: NYELV — G3 (M1.A, M1.B, M1.F)

## NYELV lencse, G3: M1.A, M1.B, M1.F (AP-2026-10-11-01, next-version)

**Rövidítések a Hely mezőben (abszolút útvonalak):**
- **M1.A** = `02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md`
- **M1.B** = `02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md`
- **M1.F** = `02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md`

**Mit hagytam ki szándékosan:**
- A már validált tételeket nem jelentem újra: IMPL-G3-3, IMPL-G3-4, IMPL-G3-9, BIZT-G3-1, BIZT-G3-4, BIZT-G3-7, ERT-G3-1.
- Régi írásmód (madrich, chanich, hagshama, dugma ishit, Leviatan) nincs a három fájlban.
- `@source` / VO-szöveg nincs a scope-ban.
- Git-előzményt nem tudtam nézni (nincs Bash-eszközöm). Ahol egy korábbi szerkesztés nyomát gyanítom, azt csak a szöveg alapján mondom.

---

**NYELV-G3-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.A:294–305 (4.2.4, képzői szöveg, tanulóknak felolvasva)
- **Probléma:** Két egymás utáni mondat kezdődik úgy, hogy „a lényeg”. A közéjük beékelt Vakfolt-bekezdés miatt az „ilyen lapjai” már a Vakfolt-mezőre mutat, nem a ‘szeretem’ és ‘nehéz’ cetlikre. Ez a 3. regressziós minta (névmási zuhanás) gyanúja: a Vakfolt-bekezdés valószínűleg későbbi betoldás.
- **Bizonyíték:** „> Ma a lényeg, hogy **megértsük: létezik ilyen mezőnk**.” / „> A lényeg: mindannyiunknak vannak ilyen lapjai –”
- **Hatás:** A felolvasott zárás ismétlődik. A „mindannyiunknak vannak ilyen lapjai – ez normális” mondat elszakad attól, amire vonatkozik (a saját erősségek és nehézségek).
- **Javaslat:** A 299–302. sori Vakfolt-bekezdést tedd a 304–305. sor után. Így az „ilyen lapjai” újra közvetlenül a 296–297. sor után áll. A szó szerinti ismétlés elkerülésére a „Ma a lényeg, hogy megértsük:” helyett lehet „Ma elég annyit megérteni:”. Tartalmat ne told be és ne törölj.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M1.B:314 (4.2.1, szó szerinti instrukció)
- **Probléma:** A „mondotok” régies, a mai köznyelvben szokatlan igealak. A mai alak: „mondtok”.
- **Bizonyíték:** „ahol egymás *tényleges* peula közbeni viselkedéséről mondotok egy apró, **csak pozitív**, megfigyelésalapú visszajelzést.”
- **Hatás:** A felolvasott instrukcióban furcsán, régiesen hangzik.
- **Javaslat:** „mondotok” → „mondtok”. A mondat többi része, így a „csak pozitív” is, változatlan marad.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-3**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M1.F:55 (Fő célok, 3. pont)
- **Probléma:** A perjeles rövidítés miatt a szöveg „le tud mondani 1 mondatot”-ként olvasható, vagyis lemondásként, nem elmondásként.
- **Bizonyíték:** „3. Le tud írni / mondani **1 mondatot arról, mi volt most neki a legfontosabb**”
- **Hatás:** A célmondat félreolvasható, a hiba nevetséges hatású.
- **Javaslat:** „Le tud írni vagy el tud mondani **1 mondatot** arról…”. Minden más változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv (D10 terminológia)
- **Hely:** M1.A:315; M1.F:330 (táblára írandó szöveg)
- **Probléma:** A „kamera-lát” nem magyar szó. A modul a fogalmat máshol így nevezi: „amit egy kamera is felvenne” (M1.2:362, M1.A:362) vagy „amit a kamera is lát” (M1.A:398).
- **Bizonyíték:** „Ráérezni a **megfigyelés** (kamera-lát) és a **címke/értelmezés** (amit gondolok)” / „**B** – Behavior: mit csinált a másik? (kamera-lát)”
- **Hatás:** A táblán és a képzői célban értelmetlen szóösszetétel áll egy olyan fogalom helyén, amelynek a modulban már van bevett alakja.
- **Javaslat:** Mindkét helyen „(amit egy kamera is felvenne)”. Az M1.F táblaszövegébe rövidebben is mehet: „(amit a kamera is lát)”, az M1.A:398 szerint.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-5**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M1.A:502 (4.4.1, Képző szerepe)
- **Probléma:** Vonzathiba: a „meghallgat” igének egy időtartam („1–2 percet”) lett a tárgya.
- **Bizonyíték:** „* Körbejár, minden csoportnál meghallgat 1–2 percet.”
- **Hatás:** Nyelvtanilag hibás képzői utasítás.
- **Javaslat:** „Körbejár, és minden csoportba 1–2 percre belehallgat.” (Vö. M1.B:376: „belehallgat 1-1 trióba”.) Az időtartam változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (D10 terminológia)
- **Hely:** M1.F:173 (tanulói instrukció); M1.F:299
- **Probléma:** A „kapus visszajelzés” két helyen áll. A fájl máshol mindenhol „a kapun kapott visszajelzés”-t ír (pl. :53, :62, :68, :157). A „kapus” elsődleges jelentése a köznyelvben „kapus” mint személy (pl. a futballkapus), ezért komikusan félreérthető.
- **Bizonyíték:** „– ha kaptál kapus visszajelzést, az abban jelzett hiánnyal kezdd.” / „vagy a kapus visszajelzésekben leggyakrabban jelzett”
- **Hatás:** Egy fogalomra két alak van, és az egyik félreérthető a tanulónak.
- **Javaslat:**
  - :173 → „ha kaptál visszajelzést a kapun, az abban jelzett hiánnyal kezdd”
  - :299 → „vagy a kapun kapott visszajelzésekben leggyakrabban jelzett”
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.F:85 (jegyzetlap, nyomtatva a tanulóhoz kerül); ugyanez a szöveg az M1.F:226 `@asset` M1.F-MUNK-02 spec mezőjében is
- **Probléma:** Az „újraértettem” nem bevett magyar ige.
- **Bizonyíték:** „„**1 mondat** arról, mi volt a legfontosabb, amit most tanultam / újraértettem:””
- **Hatás:** A tanulónak kiosztott lapon nem létező szóalak áll.
- **Javaslat:** „újraértettem” → „újra megértettem”. A látható sornál pin kell. Az @asset spec a média-buildes úton változzon, külön.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-8**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** M1.B:227 és :229 (mini SBI-kvíz, 1. kérdés)
- **Probléma:** Fordítási hiba a disztraktor magyarázatában: a „Sound” jelentése hang, nem hangerő (az angolul „volume”).
- **Bizonyíték:** „* D: Sound – hangerő” / „Nem megoldás (Solution), nem kijelentés és nem hangerő”
- **Hatás:** A kvíz a fogalmi pontosságot tanítja, miközben maga hibás fordítást mutat. Egy figyelmes tanuló észreveszi.
- **Javaslat:** :227 → „D: Sound – hang”; :229 → „nem hang”. A ✅, az opciók sorrendje és az angol szó változatlan marad. Ez objektív fordítási javítás, nem stílusból cserélt disztraktor.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-9**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.B:249 (az 5. kvízkérdés visszajelzése; MAG-kérdés, „ezt ne hagyd ki”)
- **Probléma:** A visszajelzés csonka, és két módon olvasható. (a) A becukrozás ellentéte a nyílt beszéd. (b) A lényeg az, hogyan mondjuk, címkézés helyett. Önmagában a „beszéljünk – címkézés helyett” értelmetlen ellentét, hiszen a címkézés is beszéd. Az 1. vagy 2. regressziós minta gyanúja (hiányzó alaptag vagy elveszett minősítő).
- **Bizonyíték:** „> „Nem az a cél, hogy mindent ‘becukrozzunk’, hanem hogy beszéljünk – címkézés helyett.””
- **Hatás:** Éppen azt a félreértést nem igazítja helyre egyértelműen, amelyet a kérdés a saját állítása szerint helyre igazít.
- **Javaslat:** EMBERI DÖNTÉS: a modulgazda mondja meg, melyik a szándékolt olvasat. Ha a (b), akkor az M1.F:338 modulon belüli mondata („nem arról szól, hogy ‘ne mondjunk nehéz dolgokat’, hanem arról, hogy **hogyan** mondjuk – címkézés helyett helyzet, viselkedés és hatás”) szó szerint átvehető. Új szöveget ne írj rá. A ✅ (Hamis) változatlan.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-G3-10**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.B:476 (hurokzárás, tanulónak szóló mondat)
- **Probléma:** Két gond van egy mondatban:
  - A „nem veszíted el” igének nincs tárgya. Az M1.F:270 kiírja: „A teljesítését ettől nem veszíti el”.
  - A „nem javítás” összemosható a „javító próbálkozás” szakszóval, pedig épp attól akarja megkülönböztetni.
- **Bizonyíték:** „– ez fejlesztő finomítás, nem javítás. Ha a beadásod már teljesítette a kaput, ettől nem veszíted el: a legjobb megerősített eredményed számít.”
- **Hatás:** A tanuló nem tudja biztosan, mit nem veszít el, és hogy ez a próbálkozás azonos-e a javító próbálkozással.
- **Javaslat:** „ettől nem veszíted el a teljesítést”; „nem javítás” → „nem javító próbálkozás”. Egy lépésben a BIZT-G3-1 átvezetésével (ugyanez a mondat), annak tartalmához nem nyúlva. A próbálkozás-logika változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-11**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (képzői végrehajthatóság)
- **Hely:** M1.F:270 (Blokk 2, 1. lépés, felolvasandó szöveg)
- **Probléma:** Egyetlen, kb. 110 szavas felolvasandó idézetben három feltételes ág áll a három tanulócsoportnak. A beszédhelyzetben a személy is vált (3. személy → „szólj, segítek” → 3. személy). A képző ráadásul önmagáról harmadik személyben beszél.
- **Bizonyíték:** „Ha elakadsz technikailag, szólj, segítek.” … „ehhez kérje meg a képzőt, hogy nyisson neki új próbálkozást.”
- **Hatás:** Élőben nehezen felolvasható és követhető. A „kérje meg a képzőt” a képző szájából értelmetlen.
- **Javaslat:**
  - Az idézetet három rövid, külön felolvasható bekezdésre kell bontani csoportonként, tartalmi változtatás nélkül.
  - „kérje meg a képzőt, hogy nyisson neki új próbálkozást” → „szóljon nekem, és nyitok neki új próbálkozást” (vö. M1.B:478: „Ha valaki kéri, nyisd meg neki kézzel”).
  - Egy lépésben a BIZT-G3-1-gyel, mert ugyanerről az idézetről van szó.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-12**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (D10 terminológia)
- **Hely:**
  - „Assignment” alak: M1.F:68, :270, :276, :355, :361, :395; M1.B:476, :507
  - „SBI-beadandó” alak: M1.F:62, :64
- **Probléma:** Ugyanazt az activityt ugyanabban a fájlban hol „M1.4 SBI-beadandó”-nak, hol „M1.4 Assignment”-nek hívja. A tanulóknak szóló, felolvasott mondatokban is az angol típusnév áll. A manifest szerinti activity-név „M1.4 – SBI-beadandó” (a validált IMPL-G2-7 szerint).
- **Bizonyíték:** „– az M1.4 SBI-beadandó beadva” / „írd meg a javított SBI-t, és add be az M1.4 Assignmentben.”
- **Hatás:** A tanuló a záró üzenetben más nevet hall, mint amit a kurzusban lát. Egy dologra két név van.
- **Javaslat:**
  - A tanulónak szóló idézetekben (M1.F:270, :361; M1.B:476) „az M1.4 – SBI-beadandóban”.
  - A képzői technikai jegyzetekben az „Assignment” maradhat, de az első előfordulásnál a manifest-névvel együtt: „M1.4 – SBI-beadandó (Moodle Assignment)”.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-13**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (D10 terminológia)
- **Hely:** M1.B:136 és :139 (trió-checklist); M1.B:365; az @asset M1.B-MUNK-01 spec mezőjében ugyanez
- **Probléma:** A „B” betű két fogalmat jelöl ugyanazon a megfigyelőlapon: az SBI viselkedés-elemét és a visszajelzést kapó szerepét. A „B-érzés” szóösszetétel így kétértelmű.
- **Bizonyíték:** „* Volt **B**? (igen / nem)” … „* B hogyan érezte magát?” / „* bekarikázza a B-érzést (😃 / 🙂 / 😐 / 😬 / 😡).”
- **Hatás:** A megfigyelő (C) két egymás alatti sorban ugyanazt a betűt két jelentésben olvassa.
- **Javaslat:**
  - Minimális javítás: :139 → „A visszajelzést kapó (B) hogyan érezte magát?”; :365 → „bekarikázza, hogyan érezte magát a visszajelzést kapó (B)”. Az @asset spec a buildes úton változzon.
  - A szerepek átnevezése (A/B/C) érintené az M1.B-DIA-01 ábrát és a forgásleírást. Ez nem szükséges ehhez a javításhoz. Ha mégis kell: EMBERI DÖNTÉS, a modulgazda dönt.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-14**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.A:255 (4.2.2, felolvasandó szöveg; az idézet második mondata gyermekvédelmi, HUM-SAFE-01-es szöveg)
- **Probléma:** Módhiba: a „Figyeljetek arra, hogy…” szerkezet után kijelentő mód („nem visszük tovább”) áll felszólító helyett. Így a szöveg tényt közöl ahelyett, hogy szabályt kérne.
- **Bizonyíték:** „> Figyeljetek arra, hogy amit a másik mond, azt **nem visszük tovább pletykaként vagy engedély nélkül**.”
- **Hatás:** Nyelvtanilag hibás szabálymondat egy biztonsági keretben.
- **Javaslat:** Elsőként: „Figyeljetek: amit a másik mond, azt **nem visszük tovább** pletykaként vagy engedély nélkül.” Ez megőrzi az M3.B:346-ban is használt fordulatot. A második mondat („Egy fontos kivétel van: … nem ígérünk teljes titoktartást … bevonjuk a kijelölt Memunát …”) kánoni gyermekvédelmi szöveg, nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-15**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.A:516–518 (4.4.2, záró üzenet, „ezt soha ne hagyd el”)
- **Probléma:** A vakfolt magyarázatából hiányzik a minősítő „de mi nem”. Így a „vannak, amiket mások látnak rajtunk” a Nyitott mezőt is lefedi. Ez a 2. regressziós minta (elveszett minősítő) gyanúja. A Glosszárium szerint vakfolt az, „amit mások látnak, én nem”, és az M1.F:320 is így írja: „mások látnak rajtad, de te nem”.
- **Bizonyíték:** „> vannak dolgok, amiket mi látunk magunkról, > és vannak, amiket mások látnak rajtunk.”
- **Hatás:** A peula kulcsfogalma a kötelező zárásban pontatlanul hangzik el.
- **Javaslat:** „és vannak, amiket mások látnak rajtunk, de mi nem.” Ez a Glosszárium és az M1.F:320 minősítője, nem új tartalom.
- **Típus:** objektív
- **Verdikt:** —

LEVÁGVA: 12 további finding, súlyosságuk: 12×P2

## LENCSE: NYELV — G2 (KAPU, M1.3, M1.4)

## Nyelvi review: M1, 2. fájlcsoport (G2), autopilot AP-2026-10-11-01

**Lencse:** nyelv (D11, D10 terminológiai része). **Csak olvastam, fájlt nem módosítottam.**

Rövidítések a Hely mezőben:
- KAPU = `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`
- M1.3 = `02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md`
- M1.4 = `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`

**Előzetes ellenőrzések:**
- **Régi írásmód:** a teljes M1 mappában nincs találat a `madrich|chanich|hagshama|dugma ishit|Leviatan` mintára.
- **Kihagyott, már validált tételek:** nem jelentem újra a B sáv validált tételeit (ERT-G2-5/-7/-8, PED-G2-1/-6, BIZT-G2-1/-3/-7/-10, IMPL-G2-6/-7, ERT-G2-1). Ahol egy finding ugyanazt a cellát érinti, ezt jelzem.
- **Összesen 14 finding, mind P2.** A sapkát (15) nem értem el, nincs levágás.

---

**NYELV-G2-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** KAPU:87 (1. szakasz, 4. sor, „Erős” idézhető példa) és M1.4:629 (4.2, 4. sor, „2 – Erős” példa)
- **Probléma:** A hangnem-sor „Erős” mintamondatában az „ők” névmásnak nincs előzménye. A B-rész („közbevágtál”) tárgy nélküli, így nem derül ki, kik kapjanak több teret. Ez névmási zuhanás (3. regressziós minta): a HOOK-mondatból maradt, ahol az előzmény még megvolt („a többieket”).
- **Bizonyíték:**
  - KAPU:87: „„Amikor ma a körben háromszor közbevágtál, nehéz volt megtartani a figyelmet – jó lenne, ha ők is több teret kapnának.””
  - Forrásminta, M1.3:259: „…háromszor félbeszakítottad a többieket, … Jó lenne, ha ők is több teret kapnának.”
- **Hatás:** A kalibrációs „Erős” példa éppen azt a pontosságot sérti, amelyet a rubrika mér. A képző (és az M1.4 4.2-t olvasó) találgatja, kire vonatkozik a mondat.
- **Javaslat:** Az előzményt a mondaton belül kell visszaadni: „ők” → „a többiek” (a HOOK-forrás szava), a KAPU:87-ben és az M1.4:629-ben szó szerint azonosan. Nem változhat: a szintnév, a pont és a sor kritériuma. Látható szöveg, ezért `--pin-visible` kell. Az ERT-G2-5 ezt a sort nem érinti.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M1.3:1029 és :1032 (SLIDE 7, „Mit látunk?”, önellenőrző pontok)
- **Probléma:** Két hiba ugyanabban a listában:
  - A „Nézd rá” hibás tárgyas ragozás. A „ránéz valamire” tárgyatlan, a helyes alak „Nézz rá”, ahogy a KAPU és a korpusz többi része írja.
  - A 3. pont első személyű („rám”), a 4. pont viszont tegező („beszélsz-e”, „minősíted”). A KAPU azonos önellenőrzése következetesen második személyű.
- **Bizonyíték:**
  - M1.3:1029: „„Nézd rá a saját mondatodra, és pipáld ki, amire igaz.””
  - M1.3:1032: „„Van benne, hogy ez **rám / a csoportra hogyan hatott** (I)?”” — vö. KAPU:198–199: „Nézz rá a saját mondatodra: … hogyan hatott rád / a kvucára (I)?”
- **Hatás:** Nyelvtani hiba van egy tanulói dián, és a négypontos lista perspektívája pontonként vált (én ↔ te).
- **Javaslat:** „Nézd rá” → „Nézz rá”; a 3. pontban „rám” → „rád” (a KAPU:199 és a 4. pont szerint). Nem változik a pontok tartalma, sorrendje és a „helyes válasz nélkül, nem pontozott” besorolás. A „csoportra” ↔ „kvucára” eltérés külön megnevezési kérdés, ebben a lépésben ne nyúlj hozzá. Pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.3:310 (SLIDE 1, a „Tényleg nagyon rossz érzés volt…” opció visszajelzése)
- **Probléma:** A „mindhármat” előzménye kétértelmű. A mondat három dolgot nevez meg: az érzést, a viselkedést (B) és azt, hogy mit okozott (I). Az S nem szerepel benne. Így a „mindhármat” az {érzés, B, I} hármasra is érthető, ami félretanítja a modellt, mintha az érzés külön harmadik elem volna.
- **Bizonyíték:** M1.3:310: „„Itt csak az érzés szerepel, de nem derül ki a konkrét viselkedés (B) és hogy pontosan mit okozott (I). Az SBI mindhármat megnevezi.””
- **Hatás:** Tanulói visszajelzés, amely rosszul olvasva az S–B–I helyett érzés–B–I felépítést sugall.
- **Javaslat:** Az elemek kiírása: „Az SBI mindhármat (S, B és I) megnevezi.” Nem változik az opció, a ✅ és a visszajelzés többi része. Pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** KAPU:55 (1. sor, „Erős (2)” szövegjegy). Az ERT-G2-5 ezt a horgonyt viszi át az M1.4:482/:586-ba.
- **Probléma:** A zárójelezés nélküli logikai operátorok („idő ÉS/VAGY hely ÉS a helyzet szakasza”) kétféleképpen olvashatók:
  - (idő és/vagy hely) és szakasz;
  - idő, vagy (hely és szakasz) — ebben az olvasatban egy puszta időpont is „Erős”.
- **Bizonyíték:**
  - KAPU:55: „Érthető a **konkrét alkalom**: idő ÉS/VAGY hely ÉS a helyzet szakasza azonosítható.”
  - KAPU:264: „van helyzet, de **tág**: nem derül ki, melyik peula, a peula melyik szakasza. Ezért nem „Erős”.”
- **Hatás:** Ez kalibrációs horgony („hogy két képző ugyanazt a beadványt ugyanoda sorolja”, KAPU:36). A két olvasat eltérő S-pontot ad, és az ERT-G2-5 a kétértelmű szöveget másolná tovább.
- **Javaslat:** Folyó szövegben, a 4.1–4.2 mintaértékelés szerinti olvasattal, például: „az idő vagy a hely (vagy mindkettő), és a helyzet szakasza is azonosítható”. A rubrikaszint jelentése nem változhat. Ha a verifier ezt az olvasatot a 4.1–4.2-ből nem tudja egyértelműen levezetni: EMBERI DÖNTÉS (értékelési felelős). Az ERT-G2-5-tel egy lépésben kell elvégezni.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-5**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M1.3:1059 (`@source` M1.3-NAR-06-VO, VO-szöveg; a NAR-06 spec :941 is) és KAPU:200 (Item 6, tanulói önellenőrző visszajelzés)
- **Probléma:** Egy fogalomra két név áll a tanulói szövegben:
  - az M1.3-on belül a 6. dia „beadandó”, a 7. dia narrációja angol „Assignment”;
  - a KAPU tanulói visszajelzése „Assignment”;
  - az M1.4 tanulói szövege és a manifest neve viszont „SBI-beadandó”.
- **Bizonyíték:**
  - M1.3:1059: „Mentsd el magadnak: a következő leckében és az Assignmentben erre építhetsz.”
  - M1.3:886: „az M1.4 beadandóban erre építhetsz”
- **Hatás:** A tanuló a Moodle-ben „SBI-beadandó” nevű tevékenységet lát, a narráció és a kvíz-visszajelzés viszont angol szót használ rá.
- **Javaslat:**
  - M1.3:1059: „az Assignmentben” → „a beadandóban”. VO-szöveg, ezért a hanggyártás fix packján keresztül megy, a spec :941-gyel együtt.
  - KAPU:200: „az M1.4 Assignmentbe” → „az M1.4 SBI-beadandóba”.
  - A fejlesztői szakaszok „Moodle Assignment” megnevezése marad. Pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** KAPU:109 (2. szakasz, „Szabály B (numerikus)”)
- **Probléma:** Számegyeztetési hiba: a számnév utáni egyes számú alanyhoz („A két feltétel”) többes számú állítmány tartozik („adnak”).
- **Bizonyíték:** KAPU:109: „A két feltétel **konjunkció** – csak együtt adnak átmenőt.”
- **Hatás:** Nyelvtani hiba a hivatalos küszöbszabály mondatában.
- **Javaslat:** „adnak” → „ad”. Más nem változik: a Szabály B tartalma (minden sorban ≥1 ÉS összpont ≥5/8, konjunkció), a küszöb és a „Grade to pass” mondat szó szerint marad.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** KAPU:132 (3. szakasz bevezetője, szerzői megjegyzés)
- **Probléma:** Angol szórendű tükörszerkezet. Magyarul „X helyett Y” azt jelenti, hogy Y kerül X helyére, így az „érzés-helyett-hatás” szó szerint „hatás az érzés helyett”, ami nem hibatípus. A valószínű szándék: „hatás helyett érzés” (vö. az M1.3:299 típusjelölésével).
- **Bizonyíték:**
  - KAPU:132: „mindegyik egy valós madrih-tévedést testesít meg (címke, általánosítás, érzés-helyett-hatás)”
  - M1.3:299: „*(érzés a viselkedés/hatás megnevezése nélkül)*”
- **Hatás:** A képző a hibatípus-listában fordított, értelmetlen kategóriát olvas.
- **Javaslat:** „érzés-helyett-hatás” → „hatás helyett érzés”. Nem változik egyetlen item, opció vagy ✅ sem. Ha a verifier a szándékot nem tartja egyértelműnek: EMBERI DÖNTÉS (értékelési felelős), szöveg kitalálása nélkül.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** KAPU:79 (1. szakasz, 4. sor, „Kérdés a szöveghez”)
- **Probléma:** A „(megtartható kapcsolatban)” zárójeles minősítés nem magyar szerkezet, és nem dönthető el, mit akar mondani a „viselkedésről beszél-e” kérdéshez képest. A korpuszban sehol máshol nem fordul elő.
- **Bizonyíték:** KAPU:79: „„A szöveg a **viselkedésről** beszél-e (megtartható kapcsolatban), vagy a **személyt támadja / minősíti**?””
- **Hatás:** Ez a 4. rubrikasor vezérkérdése. A képző nem tudja, a zárójel külön szempont-e (pl. a kapcsolat megőrzése), vagy csak magyarázat.
- **Javaslat:** EMBERI DÖNTÉS: az értékelési felelős vagy a modulgazda erősítse meg a zárójel szándékolt jelentését. Addig a szöveg nem írható át, csere sem javasolható. A kérdés logikája (viselkedés ↔ személy) semmiképp nem változhat.
- **Típus:** emberi-döntés · **Verdikt:** —

**NYELV-G2-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:**
  - M1.3:803–805 (SLIDE 5 „Kötelező sablon”);
  - M1.3:889–893 (SLIDE 6 mezősablon);
  - M1.4:470–471 („Formátum – javaslat”);
  - M1.4:523 (az @asset M1.4-MUNK-01 spec szó szerint idézi).
- **Probléma:** Az „Amikor ___ (S), és te ___ (B), …” sablon csak akkor ad magyar mondatot, ha az S-rés tagmondat (erre utal a „voltunk” súgó). A leckék saját S-példái viszont határozói szerkezetek („Amikor ma a játék közben…”), és ezekkel a sablon töredékmondatot ad („Amikor ma a játék közben, és te háromszor…”). Egyik teljes kánoni példa sem követi a sablont: sem a HOOK, sem az M1.4:290–292, :475, sem a KAPU:87.
- **Bizonyíték:**
  - M1.4:470: „„Amikor \[S – mikor, hol, milyen helyzetben voltunk], és te \[B – mit csináltál konkrétan],”
  - M1.3:428: „Például: *‘Amikor ma a játék közben…’*,”
- **Hatás:** A példákat beillesztő tanuló nyelvtanilag hibás kapubeadást ír, és a sablon közvetlenül ellentmond az alatta álló példának (M1.4:475).
- **Javaslat:** EMBERI DÖNTÉS (modulgazda): határozói S-rés kell (a példák szerint), vagy tagmondatos (a súgó szerint)? Ennek megfelelően vagy a sablon „, és te” kötőszava, vagy az S-súgó igazítandó, mind a négy helyen egyszerre (7. regressziós minta; az M1.4-MUNK-01 spec után `media_manifest build`). A KAPU:87 leírása („a B „te”-, az I „én / a kvuca” alakú”) egyik úton sem sérül. Az S/B/I rések és a súgók tartalma nem változik.
- **Típus:** emberi-döntés · **Verdikt:** —

**NYELV-G2-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.4:642 (4.3 „Kapu-szint”)
- **Probléma:** A „Ha ennél kevesebb:” mennyiségi összevetést sugall, holott a kapuszint két feltétel konjunkciója. Egy 2/2/2/0 = 6 pontos beadás nem „kevesebb”, mégsem teljesít; a KAPU éppen ezt az esetet hangsúlyozza.
- **Bizonyíték:**
  - M1.4:642: „Ha ennél kevesebb:”
  - KAPU:120: „ha bármelyik rubrikasor 0 maradt, a beadvány akkor sem megy át, ha a pontösszeg elérné vagy meghaladná az 5-öt”
- **Hatás:** A képzői összefoglaló félreolvasható úgy, mintha a pontösszeg döntene.
- **Javaslat:** „Ha a beadás nem éri el ezt a szintet (bármelyik feltétel nem teljesül):”. A zárójel a KAPU:302 szabályát mondja vissza, újat nem állít. Nem változik a küszöb és a felsorolás négy pontja.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-11**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.4:611 (4.2, 3. sor, „2 – Erős”)
- **Probléma:** A „vele” előzmény nélkül áll. A rubrika kontextusában a visszajelzés címzettjére is érthető, ami megfordítja a hatás alanyát. A KAPU-horgony kiírja, kiről van szó.
- **Bizonyíték:**
  - M1.4:611: „* Érthető, mi történt vele / a kvucával.”
  - KAPU:75: „érthető, mi történt a beadvány írójával / a kvucával”
- **Hatás:** Egy rubrikaszint-leírás kétértelmű.
- **Javaslat:** „vele” → „a beadvány írójával” (a KAPU:75 szó szerint). Az ERT-G2-5-tel egy lépésben, mert ugyanazt a cellát igazítja. Ez nem ismétlés: az ERT-G2-5 a „logikusan következik a B-ből” hiányát és a sornevet rögzíti, a névmást nem. Szintnév és pont nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-12**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.4:454–457 (3.1, „1. lépés – Válassz szituációt!”)
- **Probléma:** A „Választhatsz:” bevezetésű felsorolás 2. pontja saját állítmányt kap („hozhatsz”). Az eredmény kettős állítmány („Választhatsz … egy saját … helyzetet is hozhatsz”), a pontok nem párhuzamosak.
- **Bizonyíték:**
  - M1.4:454: „> Választhatsz:”
  - M1.4:457: „* egy **saját, kitalált, de életszerű** helyzetet is hozhatsz (most inkább legyen egy hétköznapibb helyzet …”
- **Hatás:** A kapubeadás tanulói leírásában döccen az instrukció.
- **Javaslat:** A 2. pontból elhagyandó az „is hozhatsz”: „egy **saját, kitalált, de életszerű** helyzetet (most inkább …)”. Szó szerint marad a zárójel és a „Valós helyzetet – név nélkül sem – ne írj le: …” mondat (lezárt kitétel, a K16/BIZT-G2-1 nem érinti). Pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-13**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:**
  - KAPU:23 („Kapu-küszöb”), :30 („rubrika-küszöböt”), :43 („kapu-küszöbnél”), :97 („kapu-leírás”, „kapu-validitási”), :111 és :303 („kapu-eredmény”), :113 („Rubrika-pontok”, „Kapu-eredmény”), :200 („kapu-érett”, tanulói), :271 („copy-paste barát”);
  - M1.4:14 („Assignment kitöltés”), :448 („copy-paste barát”), :574 („rubrika-szintek”), :633 („Kapu-szint”), :640 („kapu-küszöböt”);
  - M1.3:984 („kapu-feladatot”, @asset spec).
- **Probléma:** Kéttagú összetételek állnak kötőjellel (AkH 12: a kéttagú összetételt egybeírjuk), egy fájlon belül következetlenül is: „kapu-eredmény” ↔ „kapueredmény” (KAPU:24–26, :306), „kapu-feladat” ↔ „kapufeladat” (M1.3:1075). Az idegen előtagú összetételekből viszont hiányzik a kötőjel („copy-paste barát”, „Assignment kitöltés”).
- **Bizonyíték:**
  - KAPU:111: „**A kapu-eredmény négy tipikus esetben:**” vs KAPU:26: „A kapueredményt legkésőbb …”
  - KAPU:200: „akkor kapu-érett az SBI-vázad”
- **Hatás:** Tipográfiai következetlenség, a KAPU:200-ban a tanuló is látja.
- **Javaslat:**
  - Egybeírandó: kapueredmény, kapuküszöb, rubrikaküszöb, kapuleírás, kapuvaliditási, rubrikapontok, kapuérett, rubrikaszintek, kapuszint, kapufeladat.
  - Kötőjellel: „copy-paste-barát”, „Assignment-kitöltés”.
  - A nagybetűs, azonosító jellegű „KAPU-fájl” marad. Rubrikaszöveg, küszöb és táblázati érték nem változik. Ahol látható szöveg változik, pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-14**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.4:136 (2.1, „Szituáció A” kártyaszöveg)
- **Probléma:** A „közben” időbeli logikája hibás: az érkezés a késés végén történik, nem „közben”. Ugyanez a helyzet a KAPU Item 6-ban és az M1.4-ILL-01 specben „közben” nélkül áll.
- **Bizonyíték:**
  - M1.4:136: „„A peuláról fél órát késik valaki, és közben hangosan röhögve érkezik meg a körbe.””
  - KAPU:196: „„A peuláról fél órát késik valaki, és hangosan röhögve érkezik meg a körbe.””
- **Hatás:** A tanulói kártyán döccenő mondat áll, és ugyanaz a helyzet két szövegváltozatban él.
- **Javaslat:** A „közben” törlése, a KAPU:196 alakjára. Más nem változik: a kártya címe, a helyzet tartalma és az ILL-01 spec. Pin kell.
- **Típus:** objektív · **Verdikt:** —

## LENCSE: NYELV — G3 (M1.A, M1.B, M1.F) (folytatás 2)

## NYELV lencse, G3, 2. (utolsó) adag: M1.A, M1.B, M1.F (AP-2026-10-11-01, next-version)

**Rövidítések a Hely mezőben (abszolút útvonalak):**
- **M1.A** = `02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md`
- **M1.B** = `02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md`
- **M1.F** = `02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md`

Ez a 12 finding a korábban levágottak teljes listája. Az 1–15. findingot nem ismétlem.

Két jelöltet nem tartottam findingnak, ezek nem kerültek be:
- **Névelő nélküli színpadi utasítások** („Képző körbejár”, „Időnként képző:”, „Képző felmutat”). Ez a forgatókönyv-műfaj bevett távirati stílusa, nem nyelvi hiba.
- **Személyváltás a safer-working mondatban** (M1.A:152, M1.B:150, M1.F:95). Gyakorlatilag kánoni szöveg, és a „beszélj vele” egyértelműen olvasható.

---

**NYELV-G3-16**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (képzői végrehajthatóság)
- **Hely:** M1.A:276–277 (4.2.3, felolvasandó szöveg)
- **Probléma:** Egy bekezdésen belül három gond van:
  - A személy vált: „aki szeretné” (3. személy) → „a cetlidet” (2. személy).
  - A „felhelyeznél” természetellenes.
  - A „tedd meg nyugodtan” vonatkozása homályos. Nem derül ki, hogy új, üres cetlire kell-e írni, pedig a 3 kiosztott cetli már elfogyott (:230).
- **Bizonyíték:** „> Most az jön, hogy **aki szeretné**, felragaszthat a táblára 1–3 cetlit,” / „Ha a cetlidet nem ragasztanád fel, de eszedbe jutott valami, amit szívesen felhelyeznél, tedd meg nyugodtan!”
- **Hatás:** A felolvasott instrukcióból a résztvevő nem tudja, mit tegyen, ha a saját cetlijét nem akarja kitenni.
- **Javaslat:**
  - A személy legyen egységes, 2. személy: „ha szeretnéd, felragaszthatsz… oda, ahová szerinted illik”.
  - „felhelyeznél” → „feltennél”.
  - A „tedd meg nyugodtan” vonatkozását, vagyis hogy új cetlire írást jelent-e, a modulgazda erősítse meg. Addig ehhez a félmondathoz ne nyúlj. Tartalmat ne told be.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-17**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.B:323; mellékesen M1.B:321, :322, :334
- **Probléma:** Két gond:
  - A „2 maradékfős eset” nem létező, zavaros szóösszetétel.
  - A „4 fős trió” önellentmondó, hiszen a trió háromfős. A fájl maga is így ír: „Háromfős csoport esetén…” (:262).
- **Bizonyíték:** „* Alsó határon (8 fő) ez 2 négyes (a 2 maradékfős esetből, lásd fent);” / „csinálj **egy 4 fős triót**”
- **Hatás:** A csoportbontási szabály nehezen olvasható a képzőnek.
- **Javaslat:**
  - :323 → „(ez a „2 fő marad” eset, lásd fent)”.
  - A „4 fős trió” helyett „4 fős csoport” (:321, :322, :334). Ez utóbbi alacsony bizalmú, maradhat is.
  - A létszámok és a forgási szabály változatlanok.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-18**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** M1.B:478 (képzői megjegyzés a hurokzárás után)
- **Probléma:** Két gond:
  - Főnévtorlódás: „A nem teljesített eredmény utáni javító próbálkozás mellett … az átment beadvány önkéntes finomítása”.
  - A „tehát” nem következik az előző mondatból, amely arról szól, hogy a javító próbálkozás nem automatikus.
- **Bizonyíték:** „A nem teljesített eredmény utáni javító próbálkozás mellett tehát az átment beadvány önkéntes finomítása is rendben van:”
- **Hatás:** A próbálkozás-logika magyarázata, amely a képzőnek szól, nehezen követhető.
- **Javaslat:**
  - Bontsd két mondatra: „A javító próbálkozás a nem teljesített eredményhez tartozik. Ettől függetlenül a már teljesített beadványt is lehet önként finomítani:”, majd a mondat változatlan folytatása.
  - Az „átment” helyett lehet „teljesített”, a Glosszárium kapueredmény-címkéje szerint.
  - A próbálkozás-szabály, a KAPU-hivatkozások és az „5/8” változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-19**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (D10 terminológia)
- **Hely:**
  - „Szituáció”: M1.A:534, M1.B:181
  - „helyzet”: M1.F:338, M1.F:343
  - A kánon forrásai: Glosszárium (`02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md`):138 „Helyzet”, illetve M1-hub:241 és M1.3:48 „Szituáció”
- **Probléma:** Az SBI „S” elemének két magyar neve van („szituáció” és „helyzet”). A kánoni források is eltérnek: a Glosszárium „Helyzet → Viselkedés → Hatás”-t ír, az M1-hub és az M1.3 „Szituáció”-t. Lezárt döntés erről nincs (a HUM-fájlban nincs találat; a HUM-SOMER-02 csak a héber írásmódokról szól).
- **Bizonyíték:** „> Szituáció – Viselkedés – Hatás.” (M1.A:534) / „* „SBI: **helyzet – viselkedés – hatás**.”” (M1.F:343)
- **Hatás:** Az SBI mozaikszó feloldása peulánként más. Ez sérti az egy fogalom, egy név szabályt.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda vagy a modulgazda döntse el, melyik a hivatalos magyar feloldás (a Glosszárium „Helyzet”-e vagy a modul „Szituáció”-ja). Utána a vesztes forrást kell igazítani. Magamtól nem választok, mert a 2. és a 3. kánoni forrás ütközik.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-G3-20**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** Cél-listák: M1.A:183–185; M1.B:180–182, :260–263, :438–439; M1.F:293–294
- **Probléma:** A Cél-felsorolások pontjai más-más szerkezetűek: főnévi igenév, kötőmódú mellékmondat és főnévi szerkezet keveredik. A párhuzamosság szabálya ezt tiltja.
- **Bizonyíték:** „* Mindenki megszólaljon 1 szó/1 mondat erejéig.” / „* A biztonságos tér jelzése: **lehet passzolni**.” (M1.A:184–185)
- **Hatás:** Kisebb olvashatósági egyenetlenség a képzői célokban.
- **Javaslat:**
  - Listánként egy szerkezet legyen. A fájlok Cél-listáinak többsége főnévi igeneves (pl. M1.A:215–217, M1.F:257–259, :354–356).
  - Ahol az átalakítás jelentést változtatna, a pont maradjon. Például az M1.A:184 nem lehet „mindenkit megszólaltatni”, mert az a passzolási jogot gyengítené.
  - A minősítők („legalább egyszer”, „lehet passzolni”) maradnak.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-21**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M1.F:70, :263, :264, :278; M1.B:408, :474
- **Probléma:** Angol szavak és szleng a képzői szövegben, ahol van bevett magyar megfelelő. Egyik sem terméknév vagy UI-elem.
- **Bizonyíték:** „Ha a tech megáll, ezt osztod ki” (M1.F:263) / „**Hurokzárás a kapu-produktum felé (opcionális):**” (M1.B:474)
- **Hatás:** Fejlesztői metanyelv és angolos regiszter kerül a képzői anyagba.
- **Javaslat:** Egyesével, kontextusban:
  - „FAQ” → „gyakori kérdések” (M1.F:70)
  - „a tech” → „a technika” (M1.F:263, :264)
  - „tanuló-lab” → „csendes, közös tanulás” jellegű körülírás (M1.F:278). Lehet, hogy a „Study Lab” név visszhangja; a „műhely” szót ne használd, mert a Glosszárium szerint az nem az F-peula neve.
  - „Normalizálni, hogy” → „Kimondani, hogy természetes:” (M1.B:408)
  - „Hurokzárás a kapu-produktum felé” → „Kapcsolás az M1.4 – SBI-beadandóhoz” (M1.B:474)
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-22**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M1.A:282 (felolvasandó határ-mondat; a BIZT-G1-7 mintának hivatkozza)
- **Probléma:** Hivatali, főneves szerkezet áll a tanulóknak felolvasott mondatban, és a „magáninformáció” nem bevett szó.
- **Bizonyíték:** „A Rejtett mező megértéséhez használhatsz fiktív vagy általános példát is; érzékeny magáninformáció megosztása nem feladat.”
- **Hatás:** A biztonsági határ hivatali hangon hangzik el egy 15–17 éves közönségnek.
- **Javaslat:** Csak a megfogalmazás változzon, a jelentés („nem része a feladatnak”) nem: „érzékeny magánügyeket megosztani nem része a feladatnak”. Két irányt kerülj: a „nem kell” megengedőbb, a „ne ossz meg” szigorúbb az eredetinél. A mondat első fele változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-23**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M1.A:286, :447; M1.B:413; M1.F:265
- **Probléma:** Töredékes, távirati mondatok a képzői szövegben: hiányzik az alany vagy az ige, illetve számjegy áll szöveg helyett.
- **Bizonyíték:** „* Lehet egyszerre kimenni, vagy sorban, ahogy komfortos.” / „→ érzés/címke, lehet mögé szitu”
- **Hatás:** A képzőnek ki kell találnia, mit jelent a töredék.
- **Javaslat:**
  - :286 → „ahogy a csoportnak kényelmesebb”
  - :447 → „érzés/címke, mögötte lehet egy konkrét helyzet” (a :446 „milyen helyzetben?” párja)
  - M1.B:413 → „(nem kell mindet feltenni; ez a javasolt sorrend)”
  - M1.F:265 → „ha egyetlen eszköz sem működik”
  - Új tartalmat ne told be.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-24**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv (képzői végrehajthatóság)
- **Hely:** M1.F:81, :263
- **Probléma:** Az „1 db kinyomtatott, 1 oldalas összefoglaló” szó szerint egy példányt jelent. A szöveg viszont azt írja, hogy „ezt osztod ki”, és a csoport „párban átbeszéli”. Egy példányt nem lehet párokra kiosztani.
- **Bizonyíték:** „– **Hozz be előre 1 db kinyomtatott, 1 oldalas összefoglalót** … Ha a tech megáll, ezt osztod ki, és **párban átbeszélik**”
- **Hatás:** A képző szó szerint olvasva egyetlen példánnyal érkezik, és így a B-terv nem működik.
- **Javaslat:**
  - Az „1 db” törlése mindkét helyen; az „1 oldalas” marad.
  - Példányszámot ne találj ki. Ha kell, a modulgazda adja meg.
  - Az @asset M1.F-MUNK-01 „1 db A4, 1 oldal” formátumleírás, nem példányszám, ahhoz ne nyúlj.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-25**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M1.A:526–527 (záró üzenet)
- **Probléma:** Tükörfordítás-gyanú: a „szavakat adunk a másiknak magáról” nem magyaros szerkezet.
- **Bizonyíték:** „> Madrihként hatalmas erőnk van abban, > hogy **milyen szavakat adunk a másiknak magáról**.”
- **Hatás:** A peula kulcsüzenete természetellenesen hangzik el.
- **Javaslat:** Minimális csere: „hogy **milyen szavakkal beszélünk a másiknak saját magáról**”. Az „erőnk” maradjon, ne legyen belőle „felelősség”, mert az jelentésváltozás. Ha a verifier ezt elfogadható köznyelvinek ítéli, maradhat.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-26**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** M1.F:264; M1.B:395; M1.B:350
- **Probléma:** Három pontatlan vonatkozás:
  - A „nyert idő” és a „visszaadhatod” vonatkozása homályos (a Blokk 3 előrehozásával nem nyer időt a képző).
  - A „ezt a 2 percet” mögött nincs előzmény: a sáv 4 perces, a szöveg előtte „1–2 percet” ír.
  - A „figyeli a checklistet” rossz ige-tárgy pár: a 3. lépés szerint C kitölti a lapot.
- **Bizonyíték:** „A nyert időt visszaadhatod, ha a tech közben helyreáll.” (M1.F:264) / „C párhuzamosan figyeli a checklistet” (M1.B:350)
- **Hatás:** A képzői időbeosztás és a szerepleírás félreérthető.
- **Javaslat:**
  - M1.B:395: „ezt a 2 percet” → „ezt az időt”.
  - M1.B:350 → „C közben kitölti a checklistet”, a :362–365 szerint.
  - M1.F:264: a mondat szándékolt jelentését a modulgazda erősítse meg (valószínűleg: ha a technika helyreáll, a maradék idő visszamegy a csendes pótlásra). Addig ne írd át.
  - Az időtartamok változatlanok.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-G3-27**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv (D10 terminológia)
- **Hely:** M1.B:166 ↔ M1.B:401
- **Probléma:** Ugyanannak a blokknak a percbontásban és a fejlécben más a neve.
- **Bizonyíték:** „**30–40’** – Nagyköri megosztás: élmények, nehézségek, felismerések” / „### 4.3. Blokk 3 – Kvuca-megosztás (30–40’)”
- **Hatás:** A képző a percbontásból és a blokkleírásból nem azonosítja egyből ugyanazt a blokkot.
- **Javaslat:** Egy név legyen. A blokkszöveg „nagykörbe” ültet (:411), ezért a fejléc legyen „Nagyköri megosztás”. Az idősáv változatlan.
- **Típus:** objektív
- **Verdikt:** —

NINCS TÖBB

## LENCSE: NYELV — G1 (hub, M1.1, M1.2)

## NYELV-G1 – M1 nyelvi lencse, 1. fájlcsoport (hub, M1.1, M1.2) – AP-2026-10-11-01

**Rövidítések a Hely mezőben** (abszolút utak):
- HUB = `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md`
- M1.1 = `02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md`
- M1.2 = `02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md`
- Csak hivatkozásként, nem a scope része: KAPU = `…/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`, M1.4, M1.B, M1.F (`…/M1/Peulák/`), Glosszárium = `…/02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md`

**Szándékosan nem jelentem újra, mert már validált:** PED-G1-4 (M1.2:618, :629, :651), PED-G1-3 (M1.1:61, :930), ERT-G1-3 (HUB:86), PED-G1-8 (HUB:93, :97, :99, :102), IMPL-G1-6 (M1.1:344), ERT-G1-7 (M1.2:775–784), és a BIZT-G1-7 tartalmi része (M1.1:926). Az M1.1-NAR-05 „gépelni” fordulata már rögzített VO-függőség (N-M1-04 jegyzőkönyv :124; course-fix napló :28).

**Korábbi írásmód:** a scope-ban nincs régi alak (madrich, chanich, hagshama, dugma ishit, Leviatan). **Regressziós minta** a 10-es listából: nem találtam.

---

### NYELV-G1-1
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M1.1:864 (SLIDE 6, 1. kérdés, a ✅ opció)
- **Probléma:** A helyes válaszban a „lát” ige rossz vonzattal áll: „rólad” szerepel, a „tud rólad” opciók mintájára. A lecke máshol ugyanerre a mondatra „rajtad”-ot ír.
- **Bizonyíték:** :864 `* Amit mások látnak rólad, de te nem ✅` ↔ :870 `A vakfolt az, amit a többiek látnak rajtad, de te nem igazán.`
- **Hatás:** A kvíz helyes opciója nem magyaros, és eltér a közvetlenül utána következő visszajelzéstől. A „lát rólad” a „képet lát rólad” jelentést is felkínálja.
- **Javaslat:** „Amit mások látnak rajtad, de te nem ✅”. Csak a vonzat cserélődik. A ✅ helye, a másik három opció és a visszajelzések változatlanok. Látható szöveg, ezért pin kell.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-2
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M1.2:906 (SLIDE 6, 3. kérdés szövege)
- **Probléma:** Az idézett címke legfelső szinten áll, ‘…’ jelben. Nincs körülötte „…” idézet, ezért „…” kellene.
- **Bizonyíték:** `> *Mi lehet a gond azzal, ha csak címkét mondasz (‘lusta vagy’), és nem konkrét megfigyelést?*`
- **Hatás:** Tipográfiai hiba egy tanulói kérdésben. A lecke többi helyén a ‘…’ csak „…” idézeten belül áll (:199, :392, :917).
- **Javaslat:** `(„lusta vagy”)`. A kérdés többi része, az opciók és a ✅ változatlanok. Pin kell.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-3
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.2:885 (SLIDE 6, 2. kérdés, igaz/hamis állítás); M1.2:934 (záró diaszöveg)
- **Probléma:** A tanulói mondatokban perjel köti össze a kategória két nevét. A szabály szerint `/` helyett rendes mondat kell. A grafika és a drop-zóna címkéje (:345, :749) maradhat.
- **Bizonyíték:** :885 `„Az értelmezés / címke mindig rossz, és tilos ilyet gondolni.”`; :934 `– **értelmezés / címke** = amit ez alapján gondolsz a másikról.`
- **Hatás:** A képernyőolvasó „per”-ként vagy „perjel”-ként olvassa fel. Az igaz/hamis állítás nehezen olvasható, és két külön dolognak is érthető.
- **Javaslat:** :885 „Az értelmezés vagy a címke mindig rossz, és tilos ilyet gondolni.”; :934 „**értelmezés** vagy **címke** = …”. A „vagy” megtartja, hogy egy kategória két nevéről van szó (az „és” két dolgot csinálna belőle). A kulcs (Hamis ✅) és a visszajelzések változatlanok. A :618 a PED-G1-4-é, ide nem tartozik. Pin kell.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-4
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.1:644 – `@source` M1.1-NAR-04-VO (VO-szöveg, a hanggyártás útján változik)
- **Probléma:** Az ismeretlen terület példájában két szerkezet csúszott össze: a „még te sem [tudod]” (:471) és a „még nem próbáltál ki” (:472). Az eredmény logikátlan: mintha mások már kipróbálták volna.
- **Bizonyíték:** :644 `És vannak olyan dolgok, amiket még te sem próbáltál ki – például, hogy milyen lennél egy nagy csoport előtt madrihként.` ↔ :472 `Olyan dolgok, amiket még nem próbáltál ki, vagy helyzetek, amikben még nem voltál.`
- **Hatás:** A narráció, és vele a szó szerinti felirat és leirat, épp a fogalmat bemutató példánál közöl hibás mondatot.
- **Javaslat:** „amiket még nem próbáltál ki” (a NAR-03 :472 szóhasználata). A példa szövege változatlan. VO-fix packként a VO QA-repón át; a felirat és a leirat a forrással együtt változik.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-5
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.2:548, :553–554 – `@source` M1.2-NAR-03-VO (VO-szöveg)
- **Probléma:** Két írott szerkezet nem olvasható fel jól. (a) A nagykötőjeles főnévi összetételben a jel kimondva elvész. (b) A puszta idézett mondatot alanyként vagy állítmányként használja, a :550–551 „Ha azt mondod: …” kerete nélkül.
- **Bizonyíték:** :548 `„A megfigyelés–értelmezés különbsége **mindenhol ott van**: suliban, kenben, otthon.`; :553–554 `Ugyanígy a kenben: *‘kétszer kivonultál a teremből’* megfigyelés.` / `A *‘szétverted a peulát’* már címke.`
- **Hatás:** A narrátorhangban „a megfigyelés értelmezés különbsége” hallatszik, és az idézetek határa eltűnik („A szétverted a peulát már címke”). A hallgató nehezen követi éppen a kulcspéldáknál.
- **Javaslat:** (a) „A megfigyelés és az értelmezés közti különbség mindenhol ott van…”. (b) A narráció saját kerete a :550–551-ből: „Ugyanígy a kenben: ha azt mondod, ‘kétszer kivonultál a teremből’, az megfigyelés. Ha azt mondod, ‘szétverted a peulát’, az már címke.” Tartalom és példák változatlanok. VO-fix packként.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-6
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.2:640 – `@source` M1.2-NAR-04-VO (VO-szöveg); ugyanez az @asset spec-ben: M1.2:573
- **Probléma:** A narrált utasítás „szóra vagy kifejezésre” kattintást kér. A Mark the Words viszont csak egyes szavakat jelöl, a többszavas címke minden szavát külön kell megjelölni.
- **Bizonyíték:** :640 `Kattints rá minden olyan szóra vagy kifejezésre, ami inkább **címke vagy minősítés**, nem konkrét tény.”`; :631 `a Mark the Wordsben csak egyes szavak jelölhetők, kifejezés nem.`
- **Hatás:** Az 5. mondatnál („Egyáltalán nem érdekel”) a tanuló egyetlen kattintással jelölné „a kifejezést”, két célszó jelöletlen marad, és a visszajelzés olyan hibát jelez, amelyet maga az utasítás okozott.
- **Javaslat:** A narráció igazodjon a dián látható, PED-G1-4 szerint javított utasításhoz (:618) és a :631 szabályához. Például: „Kattints rá minden olyan szóra, amely inkább címke vagy minősítés – ha a címke több szóból áll, mindegyikre.” A célszavak és a pontozás változatlanok. VO-fix packként; a :573 spec-sor ugyanígy, utána build.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-7
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M1.1:926 (SLIDE 6, záró diaszöveg). Ez a BIZT-G1-7 mondata; ez a finding csak a nyelvi rész, nem duplikátum.
- **Probléma:** A mondat homályos képpel indul („az ablak nem áll meg”), és kétértelmű névmás áll benne. Az „ez” mutathat a nyitott terület tágítására (közvetlen előzménye a „mindkettő …”), vagy csak az önfeltárásra (a kettőspont utáni rész).
- **Bizonyíték:** `> És az ablak nem áll meg: **a másoktól kapott visszajelzés a vakfoltodat csökkenti, …` / `… mindkettő a nyitott területet tágítja. Madrihként ez a **hitelesség** egyik eszköze: nem kell mindent kitenned,`
- **Hatás:** A tanuló nem tudja eldönteni, hogy a visszajelzés kérése is a hitelesség eszköze, vagy csak az, amit magáról megmutat. Ez éppen a kiskorú madrih önfeltárásáról szóló nyitott kérdés.
- **Javaslat:** EMBERI DÖNTÉS: melyik olvasat a szándékolt. Döntenek a BIZT-G1-7 döntéshozói (Memuna + szakmai lektor), azzal egy lépésben. A kép és az „ez” javítása csak a döntés után jöhet; a „magadtól” minősítő nem törölhető. Most nem javaslok szöveget.
- **Típus:** emberi-döntés · **Verdikt:** —

### NYELV-G1-8
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:253 (6. Kapuk, „És nem csak adni: kapni is.” tanulói doboz)
- **Probléma:** A doboz utolsó mondata kb. 60 szavas: zárójeles betéttel és gondolatjeles folytatással három gondolatot fűz össze. A következtető „így” után álló tiltó felszólítás („ne … éld meg”) kapcsolata sem világos.
- **Bizonyíték:** `**mit látott az értékelő a munkádban, mi lett ennek a hatása, és mi a következő lépés** (a konkrét visszajelzést az M1.B-ben adni *és* kapni is gyakoroltad) – így a javító visszajelzést ne támadásként éld meg,`
- **Hatás:** Felolvasva és képernyőolvasóval nehezen követhető, a lényeg (a javító visszajelzés fogódzó, nem támadás) a mondat végére szorul.
- **Javaslat:** Három mondatra bontás, tartalomvesztés nélkül: (1) „Jó, ha tudod: … és mi a következő lépés.” (2) „A konkrét visszajelzést az M1.B-ben adni és kapni is gyakoroltad.” (3) „Ezért a javító visszajelzést ne támadásként éld meg, hanem fogódzóként, amiből látod, mit csinálj máshogy legközelebb.” Feltétel és hivatkozás nem eshet ki (9. regressziós minta).
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-9
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** HUB:77 (M1.1 „Cél”)
- **Probléma:** Tükörfordítás: a „hogyan nem látunk mindent magunkból” angol mintájú („explain how we don't see …”), magyarul nem így mondjuk. A „saját szóval” helyesen „a saját szavaival”.
- **Bizonyíték:** `**Megnevezni** a Johari-ablak 4 mezőjét, és **saját szóval elmagyarázni**, hogyan **nem látunk mindent magunkból**, ezért a többiektől kapott visszajelzés segíthet feltárni a vakfoltjainkat.`
- **Hatás:** A lecke képzői célmondata nem magyar mondat. A „hogyan” módhatározói olvasatot ad, mintha a „nem látás” módját kellene elmagyarázni.
- **Javaslat:** „…és **a saját szavaival elmagyarázni**, hogy **nem látunk mindent magunkból**, ezért …”. A „hogyan” helyett „hogy”, a lecke mikrocélja szerint (M1.1:55: „vagyis azt, hogy nem látunk mindent magunkból”). Más nem változik.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-10
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:132 (M1.4 „Tartalom röviden”)
- **Probléma:** A hatás leírásában a „rá” legközelebbi előzménye „a másik” (a B-elemből). Így úgy olvasható, hogy az I a visszajelzést kapóra gyakorolt hatás. A lecke szerint viszont a visszajelzést adóra vagy a csoportra gyakorolt hatás.
- **Bizonyíték:** HUB:132 `(S – mikor/hol; B – mit csinált a másik; I – hogyan hatott rá / a csoportra);` ↔ M1.4:466 `* **I – Hatás:** ez hogyan hatott rád vagy a csapatra?`
- **Hatás:** A képzői összefoglaló félreérthetően írja le az SBI hatás-elemét. Aki a hubból dolgozik, az I-t a másik emberre gyakorolt hatásként magyarázhatja.
- **Javaslat:** „I – hogyan hatott az SBI írójára / a csoportra”. Csak az előzményt nevezi meg, az M1.4:466 jelentése szerint; az S és a B változatlan.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-11
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:220 (M1.F percbontás, 1. pont); ugyanez a mondat: M1.F:36 (G3)
- **Probléma:** A „Megőrzésére” birtokos személyjelének nincs egyértelmű előzménye. A legutóbbi főnév az „árnyékdosszié” (amely éppen nem készül), előtte az „adat”, a „mentorjegyzet” és „a kép” is szóba jöhet.
- **Bizonyíték:** `ebbe csak a fejlődéstámogatáshoz szükséges minimális adat kerül, „árnyékdosszié” nem készül. Megőrzésére az `Adatvédelem – tanulói adatok és AI.md` §3 mátrixának …`
- **Hatás:** Egy adatkezelési szabálynál nem egyértelmű, minek a megőrzését köti a mondat a §3 mátrix sorához.
- **Javaslat:** Csak az előzményt kell megnevezni: „**A mentorjegyzet** megőrzésére …”. Előtte ellenőrizni kell, hogy a §3 mentori 1:1 meta-napló sora a mentorjegyzetet fedi-e; ha nem, EMBERI DÖNTÉS (DPO). A szabály, a hivatkozás és a „minimális adat” korlát változatlan. Az M1.F:36 ugyanígy (G3).
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-12
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:249 (Minimális teljesítés); ugyanez a szó: KAPU:23 (G2)
- **Probléma:** A kapu teljesítése helyett az „átmenet” szó áll, ami magyarul ‘transition’, nem sikeres teljesítés. Ugyanitt a 3. személyű specifikációban váratlanul tegező felszólítás áll („Vigyázz:”).
- **Bizonyíték:** `(Vigyázz: a rubrikában a „Még nem” a **legalsó, 0 pontos** szint, ezért az átmenethez nem elég – minden sornak legalább „Rendben” szintűnek kell lennie.)`
- **Hatás:** A küszöbmagyarázat kulcsszava félreérthető (átmenet a következő modulba? szintek között?), éppen abban a mondatban, amelynek a félreolvasást kellene megelőznie.
- **Javaslat:** „ezért a teljesítéshez nem elég”. A „Vigyázz:” helyett a KAPU:23 „Figyelem:” fordulata. A küszöb, a pontok és a szintnevek változatlanok. A KAPU:23 „az átmenethez kevés” ugyanígy (G2).
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-13
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:266 (7. Tanulási analitika, 1. pont)
- **Probléma:** A „modulonként” rossz egységet nevez meg: az M1.1–M1.4 egyetlen modul leckéi, a korpuszban a „modul” az M0–M7 + Z egység.
- **Bizonyíték:** `– M1.1–M1.4 activity completion modulonként és csoportszinten.`
- **Hatás:** A stáb nem tudja, leckénként vagy (értelmetlenül) modulonként bontsa-e az adatot, és ugyanaz a szó két fogalmat jelöl.
- **Javaslat:** „leckénként és csoportszinten”. Más nem változik.
- **Típus:** objektív · **Verdikt:** —

### NYELV-G1-14
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv (D10, terminológia)
- **Hely:** HUB:33 ↔ HUB:241; M1.2:936 (kontextus: Glosszárium:138; KAPU:47; M1.4:464; M1.B:181)
- **Probléma:** Az SBI „S” elemének két magyar neve van. A Glosszárium és a hub kompetenciasora „helyzet”-et ír; a hub rubrikasora, az M1.2 hídmondata, a KAPU 1. sorának neve, az M1.4 és az M1.B „szituáció”-t.
- **Bizonyíték:** HUB:33 `amely tartalmaz S-t (helyzet), B-t (viselkedés) és I-t (hatás)`; M1.2:936 `ez lesz az SBI-modell: S (szituáció) – B (viselkedés) – I (hatás).`
- **Hatás:** Sérül az „egy fogalomra egy megnevezés” szabály, és két kánoni forrás eltér egymástól: a Glosszárium (Helyzet → Viselkedés → Hatás) és a KAPU rubrikasorának neve.
- **Javaslat:** EMBERI DÖNTÉS: „helyzet” vagy „szituáció” legyen-e az S kánoni neve. Dönt a modulgazda és az értékelési felelős (a rubrikasor neve miatt), a Glosszárium gazdájával. A döntésig sehol nem cseréljük; a rubrikasor nevét döntés nélkül nem írjuk át.
- **Típus:** emberi-döntés · **Verdikt:** —

### NYELV-G1-15
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** HUB:222, :177 és :183 (@asset); M1.1:74; M1.2:28; M1.2:741; M1.1:66; M1.2:958; M1.1:15 (@asset); M1.1:755; M1.1:762
- **Probléma:** Egybe- és különírási, illetve szóhasználati hibák a fejlesztői és képzői sorokban:
  - „fogalom-térkép” → fogalomtérkép
  - „Moodle oldal” → Moodle-oldal (ugyanezek a fájlok máshol „Moodle-oldali”-t írnak)
  - „mondat-szinten” → mondatszinten
  - „diagram animáció” → diagram-animáció (így szerepel a HUB:81-ben is)
  - „mondat kategorizálás” → mondatok kategorizálása
  - „klippek” → klipek (vö. M1.1:11)
  - „személyes kapcsolás” → személyes kapcsolódás
  - „bulletpontokkal” → felsorolásjelekkel
- **Bizonyíték:** HUB:222 `3. 25–40’ – Közös fogalom-térkép: Johari – megfigyelés vs. címke – SBI;`; M1.1:755 `**Cél:** személyes kapcsolás, de nem terápiás mélységben.`
- **Hatás:** Nem tanulói szöveg, de a képzői percbontás (HUB:222) és az asset-cím (:177) a nyomtatott sablonra és a generált médiakimenetekbe is átkerül.
- **Javaslat:** A felsorolt alakok cseréje egyenként. Az @asset sorok (HUB:177, :183, M1.1:15) után `media_manifest.py build`. Az M1.F:82 és :379 „fogalom-térkép” alakja ugyanígy javítandó (G3). A korpuszszintű „AI beszélő fej videó” alakot szándékosan kihagytam (tömeges csere lenne).
- **Típus:** objektív · **Verdikt:** —

LEVÁGVA: 1 további finding, súlyosságuk: 1×P2

## LENCSE: NYELV — G1 (hub, M1.1, M1.2) (folytatás 2)

## NYELV-G1 – folytatás (M1, 1. fájlcsoport)

Rövidítés, mint az előző adagban: HUB = `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md`

### NYELV-G1-16
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:8 (1. Modul meta, „Javasolt sorrend” sor)
- **Probléma:** A sorrend-mondatban két kapcsolódási hiba van. (a) Az alany és az ige nem illik össze: a mikroleckék „haladnak”, holott a tanuló halad. (b) A peulát a tanuló „végezze”, holott peulán részt vesz valaki. Emellett hiányzik a névelő („M1.A-t”, „M1.B-t” az „az M1.A-t” helyett; ugyanez a fájl másutt „az M1.A peulán” alakot ír), és a csupa nagybetűs „ELŐTT” eltér a fájl félkövér kiemeléseitől.
- **Bizonyíték:** `A mikroleckék tehát **nem egy ülésben**, hanem a két peula köré csoportosítva haladnak: M1.A-t a tanuló **az M1.3–M1.4 ELŐTT** végezze (M1.A előremutató SBI-hídja erre épül), M1.B-t pedig **utánuk**.`
- **Hatás:** A képzői sor nem magyaros. A „végezze” önálló, online elvégzendő feladatnak mutatja a peulát, holott jelenléti alkalom.
- **Javaslat:** A sorrend és a feltételek változatlanok, csak a kapcsolódások javulnak, a HUB:72 igéjével („a tanuló … dolgozza fel őket”): „A mikroleckéket tehát **nem egy ülésben**, hanem a két peula köré csoportosítva dolgozza fel a tanuló: az M1.A-n **az M1.3–M1.4 előtt** vegyen részt (az M1.A előremutató SBI-hídja erre épül), az M1.B-n pedig **utánuk**.” A mondat többi része (a kapu leadása, az új próbálkozás, a legjobb megerősített eredmény) érintetlen marad.
- **Típus:** objektív · **Verdikt:** —

NINCS TÖBB
