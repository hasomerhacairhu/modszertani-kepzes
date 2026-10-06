# Validált findingok — MAN completion (BSPEC-05/06, C-1) és PR-01 mentor-láthatóság (2026-10-05)

> **Audit trail, nem kánon.** `/course-review "02 Tervezet/LMS – activity manifest.md"` két futása: `--lens
> implementation` és `--lens safety`, egyetlen közös verifier-körrel (SKILL §5; git-history nélkül, „baseline
> ismeretlen”). **Döntések a 4. pont kérdéseire:** D-e…D-j, `2026-10-05 Projektgazdai döntések – MAN completion és
> mentor-láthatóság D-e…D-j.md` (IMPL-1, IMPL-3 tartalékút-része, IMPL-4/5, IMPL-10, IMPL-11 projektgazdai része
> eldöntve; a BIZT-tételek nyitva). Bemenet: `2026-10-05 Build-blocker leltár – H-1…H-5, 38 checklist-tétel, 4 fotó.md` és `2026-10-05
> Projektgazdai döntések – build-blocker leltár D-a…D-d.md`. Javítás nem történt, commit nincs. Munkaág:
> `fix/moodle-build-hardening` @ `9ef2b25`.

## 1. Scope és lencsék

- Scope: `02 Tervezet/LMS – activity manifest.md`, kereszthivatkozásokkal (M2.3, M2 hub, M3.3, M5.2, M6.4, M4.3, M4.4,
  M7.4, M0.3, M2.2, RA, ADV, GK, HUM, RR).
- Implementációs lencse: a 40 lépéses korlátba futott, SendMessage-dzsel folytatva, teljes riporttal zárt. Saját
  hiánya: az M6 hub §6 és az M4 hub nem olvasva; az M3.3 négy szcenáriójából csak az 1. szerkezete (linearitás:
  közepes bizalom); a h5p.org BS-pontozási leírása szó szerint nem volt elérhető.
- Biztonság-jog lencse: a kötelező lencse (triggerek: `adatvéd`, `gyermekvédel`, `feltárás`). Saját hiánya: a
  `MOODLE_502_STABLE` ágon csak négy elem visszaolvasva, a többi a 4.5 alapján; `mod_assign`/`mod_h5pactivity`
  csoportkezelése nem kutatva; runtime nem futott.
- Verifier: 30 lépéses korlátba futott, folytatva; mind a 24 finding verdiktet kapott. 13 MEGERŐSÍTVE (ebből 2
  bizonyíték-kapu), 11 EMBERI DÖNTÉS, 0 ELVETVE. Valódi duplikátum nincs; részleges átfedés: IMPL-3/IMPL-7 (együtt
  javítandók), IMPL-12/BIZT-9 (az RT-P0-15 a BIZT-9-nél), BIZT-8/N-3.
- Cap (egy fájl: 15): 11 objektív finding — `LEVÁGVA: 0`.

## 2. Validált findingok (objektív)

| ID | Súly | Hely | Probléma | Javítási korlát |
|---|---|---|---|---|
| IMPL-2 | P1 | MAN „Nyitott build-spec tételek” | a D-b szerint jóváhagyott BSPEC-05/06 nincs a táblában; a gép nem látja | két `BUILD_SPEC_OPEN` sor; forrás D-b; precedens BSPEC-01; RR G3a |
| IMPL-3 | P1 | M2.3 :11, :114; M2 hub :81; M3.3 :17–18; M5.2 :9; MAN :58, :63, :78; RA :71, :82 | a BS-alapú LMS-M2-04, LMS-M3-03, LMS-M5-02 sorhoz nincs rögzített Moodle completion-beállítás és BS-pontozási mód; M2.3 definiálatlan „Moodle-checkpoint”; M3.3/M5.2-nél se tartalékút, se indokolt „nincs”; M5.2 körbehivatkozás | soronként: pontozott BS, „Receive a grade” passing grade nélkül, tartalékút vagy indokolt „nincs” (a BS-D1 új alkalmazása → projektgazdai megerősítés); M5.2: a feltétel a lecke forrásából, nem gyengülhet |
| IMPL-4 (C-1) | P1 | MAN :19, :161; RA :32; LMS-M2-05, -M4-05, -M7-05, -Z-04 | az ASSIGN-S mentori megerősítésének nincs Moodle-kódolása; a „checkpoint-út” tartalékútnak nincs sora | külön sor (BSPEC-07, az ID projektgazdai jóváhagyással); a „puszta leadás nem completion” nem gyengülhet |
| IMPL-5 | P1 | MAN :98, :132; RA :33 | az LMS-M7-07 „v1 leadására” nyílása core-ban nem állítható (az availability-feltételek: completion, date, grade, group, grouping, profile) | BSPEC-07-ben két állapot a BS-D8 mintájára (`completionsubmit` + külön megerősítés-objektum) — a minta átvitele új alkalmazás → projektgazdai megerősítés |
| IMPL-6 (H-4) | P1 | MAN :16; §2 „profil”; RA :70 | a H5P-C profil nem rögzít Moodle completion-beállítást | BSPEC-06 osztályonként (3. pont); LMS-M2-01: csak az köthető ki, hogy az identitás-kör kérdése ne a követett activityben fusson — a HUM-PRIV-01 két útja (MAN :52) közül egyiket sem szabad kizárni |
| IMPL-7 | P1 | M2.3 :11; M6.4 :104; RA :36, :71; MAN :16 | a források összemossák a H5P belső végét/attempts-riportját a Moodle Activity completionnel (docs.moodle.org/501 H5P activity: „…no connection with the 'Grade to pass' activity setting nor with activity completion settings.”) | a BSPEC-05/06 szövegében és a hivatkozott sorokban: unlockot csak Moodle Activity completion vagy Grade-feltétel hajt; az attempts-riport bizonyíték/analitika; „mérhető” → „Moodle Activity completionként beáll” |
| IMPL-8 | P1 | M7.4 :14; HUM 10. szakasz után | a D-d lezárt, az M7.4 completion-sora „nyitott”-at mond; a D-a…D-d nincs a HUM-ban | M7.4 :14 a D-d szerint; új datált HUM-szakasz (2026-10-05) a jegyzőkönyvre hivatkozva; a SLIDE 4 AI-biztonsági MC completion-elem marad; RA 14 torzítási tesztje marad |
| IMPL-9 | P1 | M4.3 :20; M4.4 :26; MAN :72, :74 | „végignézve” vs. „mini-kvíz” / „H5P befejezve” vs. a profil „puszta megtekintés nem elég”; mindkét lecke pontozott mini-kvízt tartalmaz | a szigorúbb, profil szerinti irányba (BSPEC-06 b osztály) |
| BIZT-3 | P1 | RA 15. pont; jegyzőkönyv | az `analysis.php` és az Excel-export Separate groups módban csoport nélküli nézőnek minden választ kiad (4.5 forráskód); grouping-ág közepes bizalom | RT 15 negatív esetei (csoport nélküli `viewreports` mentor; grouping esetén groupingon kívüli csoporttag); a build-spec rögzítse, kap-e az activity groupingot; mentor szerepkör csak a csoportba sorolás után |
| BIZT-4 | P1 | MAN :24, :159 | a kurzusszintű „Force group mode” felülírja az activity csoportmódját; a MAN nem rögzíti | TEXT-C rögzített beállításai: kurzus „Force group mode” = No, TEXT-C „Group mode” = „Separate groups”; Group/Grouping hozzáférési feltétel sehol (BS-D1, nem újranyitás); staging-visszaolvasás |
| BIZT-11 | P2 | MAN :24 | a beküldési értesítés nincs rögzítve; nem anonim módban teljes név + közvetlen link a `receivemail` jogúaknak | az „Enable notification of submissions” értéke rögzítendő; ha Yes, RT 15 teszteli a címzetteket |

A BIZT-2 objektív része (a verifier szerint): a PR-01 build-része sorolja fel a kurzusszintű szerepkiosztásokat
(non-editing teacher, editing teacher, manager, site admin) `viewreports`/`accessallgroups` állapottal, és a MAN :24
„alapból a tanári és a menedzseri szerep” mondata pontosítandó.

## 3. Javasolt hatókörök

**BSPEC-05 — Branching Scenario completion és tartalékút:** LMS-M2-04 (M2.3), LMS-M3-03 (M3.3), LMS-M5-02 (M5.2),
LMS-M6-04 (M6.4); downstream: LMS-M2-07, LMS-M3-04, LMS-M6-06, a §4 M2/M3/M5/M6 „H5P-k”. Soronként: pontozott BS
(hogy grade jusson a Moodle-be), „Receive a grade” passing grade nélkül, a végképernyő egybeesik-e a feltétellel (igen:
M2.3, M5.2, M3.3 — utóbbi linearitása nem ellenőrzött; nem: M6.4), tartalékút vagy indokolt „nincs”. M6.4: IMPL-1
döntés. RA 2, 5, 9, 10, 11, 18. IMPL-7 nyelvi szabálya.

**BSPEC-06 — a standard H5P activity completion-profilja:** (a) Course Presentation-alapú H5P-C pontozott
interakciókkal: LMS-M0-01…04, M1-01…04, M2-01…03, M3-01/02/04, M4-01/02, M5-01/03/04, M6-01…03, M7-01…04, Z-01…03 →
„Receive a grade”, passing grade nélkül, attempt tracking be, View nem completion-feltétel ott, ahol a lecke választ
kér; LMS-M2-01: IMPL-6 korlátja. (b) mini-kvízes: LMS-M4-03/-04 (IMPL-9). (c) pontozatlan választók: M7.4 SLIDE 4 a
D-d szerint nem completion-elem (IMPL-8); M0.3 SLIDE 7 és M2.2 értékválasztás: IMPL-10 döntés (az M4.4 poll kiesett:
nem completion-elem, M4.4 :26). (d) LMS-M5-07. A BS-sorok a BSPEC-05-ben, az Assignment a BSPEC-07-ben. RA 9, 14,
21, 24. IMPL-7 nyelvi szabálya.

**BSPEC-07 (javasolt, az ID projektgazdai jóváhagyásra vár) — ASSIGN-S megerősítés:** LMS-M2-05, LMS-M4-05,
LMS-M7-05, LMS-Z-04, az LMS-M7-07 és az LMS-M7-06 unlock-cellája; §1 ASSIGN-S, §4 :145, :147, :150, :151, :153, :161;
RA 1, 3, 19 (IMPL-4, IMPL-5).

## 4. Emberi döntést igénylő tételek (javasolt szöveg nélkül)

| ID | Súly | Kérdés | Gazda |
|---|---|---|---|
| IMPL-1 | P0 | M6.4: melyik út valósítja meg a „legalább 3 külön eset” feltételt (külön activityk / stáb-checkpoint / kötött sorrendű BS); a feltétel nem gyengülhet | projektgazda |
| IMPL-10 | P2 | kiterjed-e a D-d az M0.3 SLIDE 7 skálájára és az M2.2 értékválasztására (új alkalmazási eset) | projektgazda |
| IMPL-11 | P2 | rögzíthető-e fiókhoz kötve az M2.3 BS pillérválasztója (Branching Question); ha nem, RA 10 kiterjesztése | DPO/jogi; someres vonatkozásban projektgazda |
| BIZT-1 | P0 | ki emeli ki a feltárást tartalmazó Feedback-választ a Moodle-ből, milyen szerepkörrel és határidővel; naplók, mentések; a Memuna hozzáférése | Memuna, DPO, LMS-gazda |
| BIZT-2 | P1 | elfogadható-e az editing teacher, a manager és a site admin csoportfüggetlen hozzáférése a P2 szövegekhez | DPO/jogi |
| BIZT-5 | P1 | kiterjed-e a csoport-alapú hozzáférés a H5P-C, ASSIGN-S/M, GATE-CP profilokra; a második képző és a Memuna hozzáférése (kétszemes döntés, újraértékelés) | DPO/jogi, programvezető, értékelési felelős |
| BIZT-6 | P1 | hozzáférhet-e a mentor szerepkör a Z.4 FEEDBACK-N válaszaihoz (csoportonként 2 válasznál elemzés) | DPO, programvezető |
| BIZT-7 | P1 | hogyan fér hozzá a Memuna a BS-D8 vétójához szükséges LMS-Z-06 válaszhoz; ki látja a csoportot mentor-helyettesítéskor | Memuna, DPO, programvezető |
| BIZT-8 | P1 | kell-e a TEXT-C tájékoztatóba, hogy a mezőt nem figyelik folyamatosan, és hova forduljon, akinek segítség kell (átfed: N-3) | Memuna, DPO |
| BIZT-10 | P2 | láthatja-e az új/helyettes mentor a korábbi válaszokat; a mentor-csoport nyilvántartásának hiteles forrása | DPO |
| BIZT-12 | P2 | a mentor-csoport tagságának tanulói láthatósága a BS-D1 hatókörébe esik-e (értelmezés, nem újranyitás) | DPO/jogi |

**Projektgazdai megerősítést kérő, a validált findingokból következő tételek:** a BSPEC-07 azonosító (IMPL-4, IMPL-5);
a BS-D1 „tartalékút nincs” mintájának alkalmazása az M2.3/M3.3/M5.2-re, ha a kutatás ezt adja (IMPL-3); a BS-D8 két
állapotú mintájának átvitele az ASSIGN-S-re (IMPL-5).

## 5. Bizonyíték-kapuk (nem mennek `/course-fix`-be)

- **IMPL-12** (G3b, #3): az RT-P0-01…24 és RT-A11Y-01…12 `IMPLEMENTATION_TEST_REQUIRED`; célverzió ismeretlen
  (environment record).
- **BIZT-9** (G2, #2): a mentor-láthatósági jelölt projektgazdai feltételes elfogadás; bizonyíték: az RT-P0-15
  kiterjesztett stagingtesztje (LMS-gazda, POST-BUILD) és a DPO/jogi release-ellenőrzés (`FINAL_RELEASE_QA`). A
  kiterjesztett RT-P0-15 negatív esetei: csoport nélküli `viewreports` mentor (analysis, Excel-export, válaszlista);
  groupingon kívüli csoporttag; URL-manipuláció (`showcompleted`, `userid`, `group`, `analysis.php?group`, letöltés);
  editing teacher / manager / admin hozzáférés és a tényleges szerepkiosztás visszaolvasása, `accessallgroups` sehol a
  mentornak; „Force group mode” és activity csoportmód, Group/Grouping hozzáférési feltétel sehol; több csoportos és
  csoport nélküli tanuló, csoportváltás, második stábtag; az értesítés címzettjei; tanulói fiókkal más válasza, az
  elemzőoldal és a csoporttagság nem látszik; LMS-Z-05 a BIZT-6 döntése szerint.

## 6. A projektgazdai kutatás ellenőrzése

1. Core `mod_h5pactivity` completion csak View/grade — **igazolva** (`public/mod/h5pactivity/lib.php`, MOODLE_501_STABLE:
   nincs `FEATURE_COMPLETION_HAS_RULES`; a verifier WebFetch-csel ellenőrizte).
2. Az attempts-riport completionje ≠ Moodle Activity completion — **igazolva** (docs.moodle.org/501/en/H5P_activity).
3. Nincs interakció-specifikus core szabály — **core-ra igazolva**; a BS „No scoring” mód Moodle-viselkedése nem
   igazolt (RT-P0-10).
4. Feedback mentor-láthatóság Separate groups-szal — **kódszinten igazolva a mentor szerepkörre** (egyedi válasz
   közvetlen URL-lel tiltott; a válasz-táblázat letöltése szűrt); **nem teljes**: az elemzőoldal és az Excel-export
   csoport nélküli nézőnél szivárog (BIZT-3); az editing teacher, a manager és a site admin csoportfüggetlenül lát
   (BIZT-2); csak a TEXT-C-re szól (BIZT-5, BIZT-6).

## 7. Következő lépés

A validált objektív findingok (2. pont) `/course-fix`-be mehetnek; az IMPL-3 „nincs tartalékút” része, az IMPL-4/5
(BSPEC-07) és az IMPL-1 a projektgazdai döntés/megerősítés után. A 4. pont kérdéseire nincs javasolt szöveg.
