# course-fix napló — FREEZE-A (2026-10-05)

> **Audit trail, nem kánon.** A `/course-fix` lépésenkénti naplója. Bemenet: `2026-10-05 Projektgazdai döntés –
> pilot-ütemezés és M0+M1 freeze.md` (1., 3., 4. szakasz: pilot-ütemezés, PILOT-1…4, scope-korrekció); `2026-10-05
> Build-blocker leltár – H-1…H-5, 38 checklist-tétel, 4 fotó.md` R-1, R-2, R-11; `2026-10-05 Validált findingok – MAN
> completion és mentor-láthatóság.md` IMPL-2; `2026-10-05 Validált findingok – M3.3 Branching Scenario-flow.md` SAFE-6;
> döntések: D-a…D-d, D-e…D-j (1., 4., 5., 6., 7., 7.1., 7.2. szakasz). Bázis: `9ef2b25`, munkaág
> `fix/moodle-build-hardening`. Completion-beállítás nem rögzül; M2–Z tartalmi javítás nincs; a „Segítség és
> kapcsolatok” blokk (PILOT-3) és a média (PILOT-4) a következő kör. Rövidítések: HUM, RR, PT, MAN, GK, ADV, STD.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| H-01 | új datált HUM-szakasz (11.) — a 2026-10-05-i döntések regisztrálása, a HUM-OPS-01 naptári értékeinek felülírása | HUM | alkalmazva | 21 sor; szó szerinti átvezetés a három jegyzőkönyvből; utólagos ellenőrző csak ott, ahol a jegyzőkönyv megnevez |
| H-02 | HUM :226 naptár superseded-jelölés | HUM | alkalmazva | a történeti szöveg marad |
| H-03 | HUM :483 „Hiányzó naptári pontok” superseded-jelölés | HUM | alkalmazva | a történeti szöveg marad |
| S-01 | RR :42 G8 naptár | RR | alkalmazva | a „2027-03-11 18:00” teljesítés-megerősítési dátum kiesett, a „bevárja” szabály marad |
| S-02 | PT :60 V1 naptár | PT | alkalmazva | |
| S-03 | MAN §7 cím és bevezető | MAN | alkalmazva | a két ismert dátum + a PILOT-2 szabálya; a szabályok változatlanok |
| S-04 | MAN §7 modultábla | MAN | alkalmazva | minden dátum `SCHEDULE_TO_RESYNC`, az időpontok (18:00) maradnak |
| S-05 | MAN §7 levezetett M7-pontok | MAN | alkalmazva | a mentori visszajelzésnél „(a v1 beadása utáni csütörtök)” — a levezetési viszony megőrzése |
| S-06 | MAN §7 M4-értesítő | MAN | alkalmazva | |
| S-07 | MAN §7 kurzus-hozzáférés | MAN | alkalmazva | a hozzáférés napja nem következtethető a cohort-indulásból |
| S-08 | MAN §7 javítási úton lévő madrih | MAN | alkalmazva | |
| S-09 | MAN §7 M3 kapuablak | MAN | alkalmazva | hétköznapok megtartva |
| S-10 | MAN §7 éles kapuk javítási útja tábla | MAN | alkalmazva | hétköznapok megtartva |
| S-11 | MAN §7 `schedule_key` tábla | MAN | alkalmazva | |
| S-12 | MAN :99 LMS-M7-09 | MAN | alkalmazva | |
| S-13 | Terepgyakorlat :66 | Terepgyakorlat | alkalmazva | |
| S-14 | RIGHTS-EVIDENCE :335 (R8-4) | Média-assetek | alkalmazva | a 119 napos számítás a régi naptárhoz kötve; a 90 napos szabály (HUM-PRIV-02) változatlanul kimondva; vétólista |
| M-01…M-33 | modulfájlok régi dátumai → „a központi naptár szerint” | Modulok | alkalmazva | lásd lent; a hétköznap és az időpont marad; tanulói szövegben jelölő nincs |
| R1-01 | BSPEC-05, -06, -07 `BUILD_SPEC_OPEN` (R-1, IMPL-2; D-b, D-f) | MAN | alkalmazva | a riport: `MANIFEST-OPEN 3` |
| R2-SG | GK §6 11 tétel jelölése | GK | alkalmazva | human-qa 5, post-build 1, release-evidence 2, signoff 3 |
| R2-PR | ADV §9 7 tétel jelölése | ADV | alkalmazva | build 2, post-build 2, release-evidence 2, human-qa 1 |
| R2-A1 | STD :80–89 8 tétel jelölése | STD | alkalmazva | human-qa 7, build 1 (A11Y-07) |
| R2-A2 | STD :105–116 12 tétel jelölése | STD | megállva: emberi döntés (2 tétel) | 10 tétel jelölve (post-build 8, build 1: A11Y-17, human-qa 1); az A11Y-15 (:111) és az A11Y-18 (:114) jelöletlen: a leltár `release-evidence, repo-fixable`-t írt, a scope-korrekció szerint viszont repo-fixable tétel nem maradhat release-evidence állapotban — a két projektgazdai döntés ütközik; jelöletlenül hibabiztosan build-blokk |
| R11-01 | GK §6 145. tétel hatóköre a GK §2 szerint | GK | alkalmazva | a GK §2 (:17) szó szerint; vétólista |
| R11-02 | RR :40 hatóköre a GK §2 szerint | RR | alkalmazva | a leltár R-11 sora szerint (GK §2 szó szerint); vétólista |
| DI-01 | M0.3 :14 completion-sor a D-i szerint | M0.3 | alkalmazva | a SLIDE 7 skála kikerült a completion-elemek közül; az M2.2 és a MAN :54 nem ebben a körben |

## Modulfájlok (M-lépések)

| ID | fájl:sor | állapot |
|---|---|---|
| M-01 | M1 kapu :24 | alkalmazva |
| M-02 | M1 hub :209, :258 (`replace_all`, azonos token) | alkalmazva |
| M-03 | M1.4 :620 | alkalmazva |
| M-04 | M1.F :65 | alkalmazva |
| M-05 | M3 kapu :35 | alkalmazva |
| M-06 | M3 kapu :37 | alkalmazva |
| M-07 | M3 kapu :334 | alkalmazva |
| M-08 | M3 hub :230, :259 (`replace_all`, azonos token) | alkalmazva |
| M-09 | M3 hub :255 | alkalmazva |
| M-10 | M3 hub :256 | alkalmazva |
| M-11 | M3.F :44 | alkalmazva |
| M-12 | M3.4 :808 (tanulói szöveg, írott dátumformátum) | alkalmazva |
| M-13 | M5 hub :154 | alkalmazva |
| M-14 | M5 kapu :303 | alkalmazva |
| M-15 | M5.F :19 | alkalmazva |
| M-16 | M6 hub :170 | alkalmazva |
| M-17 | M6 kapu :415 (két hely) | alkalmazva |
| M-18 | M6.F :41 | alkalmazva |
| M-19 | M7 kapu :25 | alkalmazva |
| M-20 | M7 kapu :27 | alkalmazva |
| M-21 | M7 kapu :34 | alkalmazva |
| M-22 | M7 kapu :38 | alkalmazva |
| M-23 | M7 kapu :416 | alkalmazva |
| M-24 | M7 kapu :421 | alkalmazva |
| M-25 | M7 hub :115 | alkalmazva |
| M-26 | M7 hub :326, :387 (`replace_all`, azonos token) | alkalmazva |
| M-27 | M7 hub :347 | alkalmazva |
| M-28 | M7 hub :350 | alkalmazva |
| M-29 | M7.4 :86, :88 (tanulói szöveg, írott dátumformátum) | alkalmazva |
| M-30 | M7.4 :102 (fejlesztői megjegyzés) | alkalmazva |
| M-31 | M7.B :14 | alkalmazva |
| M-32 | M7.F :35 | alkalmazva |
| M-33 | Z.4 :339, Z hub :33 | alkalmazva |

## Célzott újraellenőrzés (diff-hunkok) és utójavítások

Három szűk reviewer a diff-hunkokon (implementáció, biztonság-jog, nyelv). A saját lépéseink hibáit (átvezetési hűség,
elveszett megkülönböztető minősítő, nyelvtan) utójavításként alkalmaztuk; a többi a riportba került.

| ID | reviewer | finding | állapot | megjegyzés |
|---|---|---|---|---|
| U-01 | biztonság-jog (FA-BIZT-2) | HUM 11. szakasz D-g és SAFE-1 sora: kimaradt az LMS-M3-03 újranyitása és a „külön tartalmi QA” mondat; „újraindítja” ↔ „újraindíthatja” | alkalmazva | a forrás 7. szakaszából szó szerint (H-01 hűsége) |
| U-02 | biztonság-jog (FA-BIZT-3) | RR :42 — a programvezető vétója az új naptárhoz kötődött | alkalmazva | a szerep a HUM-OPS-01–02-höz kötve; új szerep nem került be |
| U-03 | implementáció (FA-IMPL-2) | RR G8 „a naptár: BUILD” ↔ PILOT-2 | alkalmazva | a PILOT-2 szó szerinti átvezetése a „Besorolás” cellába; eszközkód nem változott |
| U-04 | implementáció (FA-IMPL-3) | BSPEC-05 tárgya nyitott tartalékutat sugallt | alkalmazva | „független tartalékút nincs (BS-D1, D-g; Group-, kézi vagy más kerülő út kizárva)”; a hatókör nem változott |
| U-05 | implementáció (FA-IMPL-4) | MAN :290–291 a BSPEC-05…07 forrását is a 2026-10-04-i 11. pontra vezette | alkalmazva | |
| U-06 | implementáció (FA-IMPL-5) | „a `M7_V2_DUE`” névelő | alkalmazva | |
| U-07 | nyelv (FA-NYELV-1) | relatív időhatározó horgonya (M3.4 :808, M7.4 :88, M7.B :14) | alkalmazva | „ugyanazon a héten, szerdán”; „a v1-határidő után egy héttel” |
| U-08 | nyelv (FA-NYELV-2) | elveszett megkülönböztető minősítő (M3 kapu/hub, M5, M6, M7) | alkalmazva | csak a régi dátumokból levezethető horgony: „a kapu megerősítését követő hétfőn”, „a Z utáni hét hétfőjén / szerdája”, „a v2-határidő utáni csütörtök”, „az M7.B előtti szerda/csütörtök” |
| U-09 | nyelv (FA-NYELV-3) | „a Z.A záró peula péntek”, vessző-maradvány, Z.4 sorrend | alkalmazva | |
| U-10 | nyelv (FA-NYELV-4) | megkettőződött keret (M7 kapu :34, hub :347), M7 kapu :27, M7.B „Dátumok” | alkalmazva | |
| U-11 | nyelv (FA-NYELV-5) | egy fogalom egy név a tanulói szövegben | alkalmazva | M7.B: „Határidők a kurzus naptára szerint” (az M3.4 és az M7.4 tanulói megnevezésével egyezően) |
| — | implementáció (FA-IMPL-1) | a cohort-indulás (2026-10-10) szombat; a pénteki rend változatlannak van írva | riportban: emberi döntés | programvezető |
| — | biztonság-jog (FA-BIZT-1) | a SAFE-7 egy datált döntés-szakaszban áll; a „Lezárt döntések” definíciója szerint lezártnak olvasható; kapu-checklistben nincs | riportban | GK §6 :152 kiegészítése és a governance-definíció kérdése: projektgazda |
| — | biztonság-jog (FA-BIZT-4) | a HUM :481 (2026-10-02) Memuna-átnézési listája szűkebb a GK §2-nél | riportban: emberi döntés | a lista kimerítő vagy példálózó: projektgazda |

A második pin ugyanennek a változtatáskészletnek a része (19 fájl).

Maradék dátum-találat (szándékos): HUM :226, :483 (superseded-jelöléssel, történeti), HUM 11. szakasz (a döntés idézi a
régi indulást); `Média-assetek/PRODUCTION-STACK.md` :500 (az AI Act 2026. decemberi határideje, nem ütemezés).
