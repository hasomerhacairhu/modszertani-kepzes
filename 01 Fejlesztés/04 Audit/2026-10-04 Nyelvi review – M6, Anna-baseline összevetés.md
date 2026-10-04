# Nyelvi review – M6, Anna-baseline összevetés (2026-10-04)

> **Audit trail, nem kánon és nem tananyag.** A `/course-review M6 --lens language` futás validált eredménye. A
> review-orchestrator a hat nyelvi reviewer visszaérkezése előtt adta vissza a riportját, ezért a skillben előírt
> adverzális második kört (`verifier`) a fő munkamenet indította el, csoportpáronként (G1+G2, G3+G4, G5+G6). A nyers
> findingok szó szerint: `2026-10-04 Nyelvi review – M6, nyers findingok.md`. Javítás ebben a futásban nem történt.

## A kérdés és a módszer

- **A projektgazda kérdése:** történt-e nyelvi, nyelvtani, magyarsági, szó- és kifejezéshasználati romlás Anna
  szerkesztéseihez képest?
- **Összevetési pontok:** Anna nyelvi baseline-ja `adee907`; a magyar nyelvi QA lezárása `a15ee79` (2026-08-25);
  a vizsgált állapot `main` @ `ea36214` (2026-10-04). A régi fájlnevek a mai nevekre leképezve (Toolbox → Eszköztár,
  „4 kvucára” → „3 aktuális kvucára”, workshop → műhely).
- **Eredet-besorolás findingonként** (a bizonyíték kulcsszövege a két régi állapotban, `grep -F`):
  - `ÚJ` — a QA-állapotban még nem volt, azóta került be (= romlás a QA után);
  - `QA-KORI` — a `a15ee79`-ben már megvolt, Annánál még nem;
  - `ANNA-KORI` — már Anna állapotában is megvolt (régi, nem romlás).
- A régi írásmód (madrich, chanich, Leviatan, „4 kvuca”) a HUM-SOMER-02 (2026-10-02) óta nem romlás.

## Eredmény röviden

| | Tétel |
|---|---:|
| Nyers finding (6 reviewer-csoport) | 87 (+2 P2, amelyet a G6 reviewer kimeneti korlát miatt levágott; nem rekonstruálva) |
| Elvetve | 12 |
| Duplikátumként beolvasztva | 1 (NYELV-108 → NYELV-211) |
| Objektív, javítható (megerősítve vagy pontosítva) | 55 |
| Emberi döntést igényel (egészben vagy részben) | 20 |
| Bizonyíték-kapu | 0 |

**Romlás Anna óta:** igen, de nem Anna javításainak visszaesése. **12 tétel teljesen, kb. 13 részben ÚJ** (a QA után
keletkezett). Mind a QA utáni tartalmi, terminológiai és policy-átvezetések mellékterméke, amelyek után nyelvi QA nem
futott:

- **korosztály-migráció (4 → 3 kvuca):** az R2 rubrika „Oké” és „Erős” szintje ugyanarra a címkesorra került
  (NYELV-104, P1); mechanikus „(16–17)” beszúrások a mondatok közepén (NYELV-508, NYELV-608 A:399);
- **gyermekvédelmi átvezetés (HUM-SAFE-01):** a jelzési út torlódó, részfelsorolásos mondatba került (NYELV-301,
  NYELV-406); személyváltás egy védelmi betoldásban (NYELV-112, M6.F:125);
- **adatvédelmi mondat:** governance-nyelvű tanulói tájékoztató (NYELV-312 = NYELV-513);
- **SBI → Megfigyelés–Hatás csere (M6.B):** csonka mondat és alaptag nélküli cím (NYELV-611, NYELV-612);
- **Workshop → „élő műhely” csere:** időrendileg zavaros mondat (NYELV-610 e);
- **utólag betett visszajelzések és opció-átírások:** a többi elosztót nem fedik le, vagy nyelvtanilag súgnak
  (NYELV-206, NYELV-207, NYELV-314, NYELV-308 :539, NYELV-410);
- **egyéb szerkesztések, ahol jelentés vagy alany veszett el:** M6.4:809 „nincs tér” → „nem lesz hol” (NYELV-510),
  M6.A:481 „valaki rosszul lesz” → „valakit rosszul érint” (NYELV-614).

A megerősített tételek többsége `ANNA-KORI`: AFFiNE-/gépi fordítási maradvány, amelyet a restauráció sem javított —
ez nem romlás, hanem régi hiba.

## Verdiktek tételenként

Fájl-rövidítések: HUB = `M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md`, KAPU = `M6 – Kapu – értékelő
(item-bank + rubrika).md`, M6.1–M6.4 = online leckék, M6.A, M6.B, M6.F = peulák (mind a `02 Tervezet/Modulok/M6/`
alatt).

### G1 – HUB, KAPU, M6.F

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-101 | KAPU 349–364 | PONTOSÍTVA | objektív + emberi-döntés (364) | P1 | ANNA-KORI | 349/352/359 javítható; a 364 „ha valaki erősen érintett” minősítője eszkalációs szabály — Memuna dönt |
| NYELV-102 | HUB 222, KAPU 35/409 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | completion-logika nem változik |
| NYELV-103 | KAPU 393/403 | MEGERŐSÍTVE | emberi-döntés | P2 | ANNA-KORI | R1 kvantor („pontosan 1” vs „1”) — értékelési felelős |
| NYELV-104 | KAPU 394/404, HUB 211 | MEGERŐSÍTVE | emberi-döntés | P1 | **ÚJ** | a 3-kvucás migráció óta az R2 „Oké” és „Erős” ugyanaz a címkesor |
| NYELV-105 | HUB 155 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | *dugma isit* tárgyra; az M6.B-vel együtt (lásd NYELV-603 emberi döntés) |
| NYELV-106 | HUB 218 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | a KAPU „képző/mentor” és R4+R5 átvétele |
| NYELV-107 | KAPU 128–293 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | 128 (elosztó) és 137 kimarad |
| NYELV-108 | KAPU 174/186 | duplikátum | objektív | P2 | ANNA-KORI | beolvad a NYELV-211-be |
| NYELV-109 | HUB 91/254, M6.F | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | „Történet mint tükör” — csak átnevezéssel együtt (`git mv`); viszi a NYELV-205 (1467) és -302 pontot |
| NYELV-110 | KAPU, HUB, M6.F | PONTOSÍTVA | objektív | P2 | ANNA-KORI (KAPU:147 ÚJ) | „DE”, KAPU:81, KAPU:372 kimarad |
| NYELV-111 | KAPU 103–429 | PONTOSÍTVA | objektív | P2 | ANNA-KORI (103 QA-KORI, 429 ÚJ) | 287 (elosztó) és „item-pool” kimarad; 361 új szöveggel |
| NYELV-112 | M6.F | MEGERŐSÍTVE | objektív | P2 | vegyes (125 **ÚJ**) | 420 eredete `?` |
| NYELV-113 | HUB 63, KAPU 64 | ELVETVE | — | — | ANNA-KORI | a „T-ágak” / „B-ág” létező hivatkozás |
| NYELV-114 | M6.F, HUB, KAPU | PONTOSÍTVA | objektív | P2 | ANNA-KORI (M6.F:54 ÚJ) | HUB:34 kimarad (modulokon átívelő képlet) |
| NYELV-115 | KAPU 38 | MEGERŐSÍTVE | emberi-döntés | P2 | ANNA-KORI | „kötelezően” vs „ajánlott” — értékelési felelős |

### G2 – M6.1

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-201 | 1423 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | „durva” → „erős” |
| NYELV-202 | 313 | ELVETVE | — | — | ANNA-KORI | a főnévi „kézműves” a modul bevett használata |
| NYELV-203 | több sor | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | egybeírás; a cím csak `git mv`-vel; 887 → NYELV-212 |
| NYELV-204 | 1409–1412 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | csak a ✅ opció 2. személyű; a ✅ helye nem mozdul |
| NYELV-205 | 853, 1467 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | 1467 → NYELV-109 |
| NYELV-206 | 1428–1429 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | csak a ✅ opciót írták át, a disztraktorok sutábbak — súgás |
| NYELV-207 | 673, 685, 1205, 1211 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** (685/1205/1211) | „kevésbé kínos” — az alany elcsúszik |
| NYELV-208 | 1219–1235 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | biztonsági tartalom nem változik |
| NYELV-209 | 1084–1085, kártyák | MEGERŐSÍTVE | objektív | P2 | QA-KORI / ANNA-KORI | narráció → VO-újrarenderelés |
| NYELV-210 | 327 (spec 236) | MEGERŐSÍTVE | objektív | P2 | QA-KORI | alt-szöveg „heurisztika” |
| NYELV-211 | 876–880, 1233; KAPU 174/186 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | „akadálymentes”, „vezető társ” |
| NYELV-212 | 887 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | a kilépési védelem marad |
| NYELV-213 | 1452, 1392 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | „korosztálynál”; narráció |
| NYELV-214 | 928, 1055, 1075 | MEGERŐSÍTVE | emberi-döntés | P2 | QA-KORI | a B kártya az 5. kategória példája-e |
| NYELV-215 | 320, 452 | MEGERŐSÍTVE | objektív | P2 | QA-KORI / ANNA-KORI | |

### G3 – M6.2

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-301 | 778 | EMBERI DÖNTÉS | emberi-döntés | P1 | **ÚJ** (a „többek között” keret) | a §4.1 mellett megengedett-e a részfelsorolás — Memuna; az M6.3:743 és az M6.4:1014 azonos dobozával együtt |
| NYELV-302 | cím, fájlnév | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | = NYELV-109; az `asset-migration-map.csv` történeti útvonalai nem változnak |
| NYELV-303 | 50, 133 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | VID-01 narráció |
| NYELV-304 | 154 | ELVETVE | — | — | ANNA-KORI | a kétértelműség elméleti |
| NYELV-305 | 262, 269, 177 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | lista + alt + spec együtt |
| NYELV-306 | 288 | ELVETVE | — | — | ANNA-KORI | a „bevonódás” itt helyes |
| NYELV-307 | 502–506 | ELVETVE | — | — | ANNA-KORI | elfogadható; a P2 pilotszkriptet érvénytelenítené |
| NYELV-308 | 521, 539 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI (539 ÚJ) | a ✅ nem mozdul |
| NYELV-309 | 607–608 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | |
| NYELV-310 | 645 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | |
| NYELV-311 | 667, 775 (+36, 676, 712) | MEGERŐSÍTVE (szűkítve) | objektív | P2 | ANNA-KORI | csak a 667 perjel és a 775 vonzat; a 769/773 és a „nyelvezet” kimarad |
| NYELV-312 | 903 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | a lezárt HUM-PRIV-01 szó szerinti átvezetése; = NYELV-513 |
| NYELV-313 | 926 | ELVETVE | — | — | ANNA-KORI | |
| NYELV-314 | 965–972 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | a közös visszajelzés nem fedi le a 2. elosztót |

### G4 – M6.3

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-401 | 727 | EMBERI DÖNTÉS | emberi-döntés | P1 | ANNA-KORI (a glossza ÚJ) | *dugma isit* — someres terminológia; = NYELV-105/-603 |
| NYELV-402 | 734 | EMBERI DÖNTÉS | emberi-döntés | P2 | ANNA-KORI | „csak a viselő nevét” — tartalomgazda |
| NYELV-403 | 193… (6 sor) | EMBERI DÖNTÉS | emberi-döntés | P2 | **ÚJ** | „mellől elérhető” — a nyitott UE-IMPL-4-re vár; az M6.1/M6.2 azonos sorai is |
| NYELV-404 | 934, 938 | EMBERI DÖNTÉS | emberi-döntés | P2 | ANNA-KORI (meta-mondat ÚJ) | Somer zászló- és színhagyomány — helyi someres kérdés |
| NYELV-405 | 529 | EMBERI DÖNTÉS | emberi-döntés | P2 | ANNA-KORI | „mi van rajtunk” |
| NYELV-406 | 743 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | a bontás csak a NYELV-301 döntése után; minden védelmi elem marad |
| NYELV-407 | 1092–1094 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI (zárójel ÚJ) | az „1” számjegy marad |
| NYELV-408 | 1106–1107 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | NAR-06 újrarenderelés |
| NYELV-409 | 940 | ELVETVE | — | — | ANNA-KORI | |
| NYELV-410 | 1149–1175 | EMBERI DÖNTÉS | emberi-döntés | P2 | ANNA-KORI (1. kérdés visszajelzése ÚJ) | opciók személye — értékelési felelős |
| NYELV-411 | 1185 | EMBERI DÖNTÉS | emberi-döntés | P2 | ANNA-KORI | „kérdések” — tartalomgazda |
| NYELV-412 | 1200, 595, 998 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | a ✅ és az elosztó csak tipográfiailag |
| NYELV-413 | 37, 1193 | ELVETVE | — | — | ANNA-KORI | a „2–3” magában foglalja a hármat |

### G5 – M6.4

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-501 | 826–828 ↔ 1014 | MEGERŐSÍTVE | emberi-döntés | P1 | ANNA-KORI | két ellentétes kiváltó feltétel a jelzési útra — projektgazda + Memuna |
| NYELV-502 | 259–262 | ELVETVE | — | — | ANNA-KORI | |
| NYELV-503 | 660–664 | MEGERŐSÍTVE | emberi-döntés | P2 | ANNA-KORI | előzmény nélküli utalás — szerzői tartalom |
| NYELV-504 | 348–924 | PONTOSÍTVA | objektív | P2 | ANNA-KORI (445 QA-KORI) | a 444–445 tiltás nem változik |
| NYELV-505 | 949–972 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | az „eszközön” marad |
| NYELV-506 | 978, 983 | ELVETVE | — | — | ANNA-KORI | |
| NYELV-507 | több sor | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | 175/753/1011 kötőszava szerzői döntés |
| NYELV-508 | 777, 800, 884, 930 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | mechanikus „(16–17)” beszúrás |
| NYELV-509 | 175, 753, 437, 864 | PONTOSÍTVA | objektív | P2 | ANNA-KORI (437 QA-KORI) | főnévi címkeforma marad |
| NYELV-510 | több sor | PONTOSÍTVA | objektív | P2 | vegyes (809, 878 **ÚJ**) | 435 új szöveggel |
| NYELV-511 | 679–800 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | 874 kimarad |
| NYELV-512 | 847, 430, 478 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI (430 QA-KORI) | |
| NYELV-513 | 1019 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | = NYELV-312, egy közös javítás; ki láthatja a mezőt: DPO-kérdés marad |
| NYELV-514 | 306–876 | ELVETVE | — | — | ANNA-KORI | |
| NYELV-515 | 89 | ELVETVE | — | — | ÚJ | helyes, 32 fájlban és a `Program terv.md`-ben is így áll |

### G6 – M6.A, M6.B

| ID | Hely | Verdikt | Típus | Súly | Eredet | Megjegyzés |
|---|---|---|---|---|---|---|
| NYELV-601 | A:176 | MEGERŐSÍTVE | emberi-döntés | P1 | ANNA-KORI | „tét nélkül” — biztonsági szűrő kétféle olvasata |
| NYELV-602 | B:565 | MEGERŐSÍTVE | emberi-döntés | P1 | ANNA-KORI | „kinek jelzel” — gyermekvédelmi ügy-e a helyzet |
| NYELV-603 | B:87, 473, 491 | MEGERŐSÍTVE | emberi-döntés | P1 | ANNA-KORI | *dugma isit* tárgyra; a 87 kérdőjele objektív |
| NYELV-604 | A:475, 559 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | 475 új szöveggel |
| NYELV-605 | A, B | PONTOSÍTVA | objektív | P2 | ANNA-KORI | csak A:708, A:62–63, B:356, B:567 |
| NYELV-606 | B:215–216 | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI | a 49–50 szó szerint |
| NYELV-607 | A, B | PONTOSÍTVA | objektív | P2 | ANNA-KORI | B:76 kimarad |
| NYELV-608 | A, B | PONTOSÍTVA | objektív | P2 | ANNA-KORI (A:399 ÚJ) | A:447 kimarad |
| NYELV-609 | B:21–359 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | 21/71 kimarad (modulszintű) |
| NYELV-610 | A:451, A:569, B | PONTOSÍTVA | emberi-döntés | P2 | ANNA-KORI ((e) **ÚJ**) | (a) kimarad; (b)–(e) tartalomgazda |
| NYELV-611 | B:418 | PONTOSÍTVA | objektív | P2 | **ÚJ** | a `a15ee79` M6.B:220 szövegéből |
| NYELV-612 | B:420, 422 | MEGERŐSÍTVE | objektív | P2 | **ÚJ** | az „SBI-” törlésével kiesett az alaptag |
| NYELV-613 | A:239, 498 | PONTOSÍTVA | objektív (498) / emberi-döntés (239) | P2 | ANNA-KORI | |
| NYELV-614 | A, B | MEGERŐSÍTVE | objektív | P2 | ANNA-KORI (A:481 ÚJ) | |
| NYELV-615 | B:107–113, A:171, 488 | PONTOSÍTVA | objektív | P2 | ANNA-KORI | A:488-ba nem kerül új utasítás |

## A pontosított javaslatok (a nyers javaslat helyett ezek érvényesek)

- **NYELV-101 (KAPU):** 349 `láthatóan rosszul érinti`; 352 `„Álljunk meg egy pillanatra, legyen egy kis levegő.”`;
  359 `pont ezt kerüli az M6.A-ban tanult 4 lépés`; 364 `nem halasztod a peula utánra`. A 364 „ha valaki erősen
  érintett” minősítője: emberi döntés (Memuna); addig a (4) pont szabálytartalma nem változik.
- **NYELV-107 (KAPU):** 227, 271, 293, 208, 291 a nyers javaslat szerint; a 128 (elosztó) és a 137 kimarad.
- **NYELV-110:** HUB:66 `…érzékenységek), és tud`; M6.F:331 `Az utolsó 5 percben, kérlek, nézz rá`; KAPU:306 `Téves:
  a túl erős`; HUB:175, 179 `fogalomtérkép` (az asset-JSON címek nem); KAPU:147 `Leviatán-kvuca`; HUB:225 a nyers
  javaslat mondatával. A „DE” → „de”, a KAPU:81 és a KAPU:372 kimarad.
- **NYELV-111 (KAPU):** 103 `szeretnéd felvetni a kirekesztés témáját` és `csoportfolyamatok`; 182 `a kockázat
  szempontjából lényegtelen`; 429 a nyers javaslat szerint (az M6.B:403 asset-jegyzettel együtt); 387 `Stábdöntés a
  blokkoló sorokon`; 361 `…a „nem szólok senkinek” pedig épp a gyermekvédelmi felelős, a Memuna bevonását mulasztja
  el.` (a „gyermekvédelmi jelzés” terminus nem kerül be). A 287 (elosztó) és az „item-pool” csere kimarad.
- **NYELV-114:** M6.F:460, HUB:235, KAPU:368, KAPU:437, M6.F:54, HUB:61 a nyers javaslat szerint; a HUB:34 kimarad.
- **NYELV-311 (M6.2):** csak a :667 (és vele a :36, :676, :712) perjele és a :775 vonzata; a :769/:773 perjel-csere és
  a „nyelvezet” csere kimarad.
- **NYELV-302 / NYELV-109:** az átnevezés az `asset-migration-map.csv` és a `_legacy/` történeti útvonalait nem írja át.
- **NYELV-504 (M6.4):** a :444–445 „ne hagyjatok ki senkit demonstrációként” nem változik; :348 „csinálhatják
  **állva**, … így mozoghatnak is”; :539–541 „dolgozzanak először kis csoportokban, … utána rakják össze a végleges
  zászlót”; :920–921 „oszd a plakátot több részre, és dolgozhatnak kis csoportokban is”; a :535 és a :922 közös
  cselekvésként marad.
- **NYELV-505 (M6.4):** az „egy saját eszközön” → „eszközzel” csere kimarad; a többi a nyers javaslat szerint.
- **NYELV-509 (M6.4):** :175, :753, :736 „Cél: a felelősségről [kötőszó a NYELV-507 szerint, szerzői döntés] a
  társadalmi kérdésekről való gondolkodás elindítása”; a :437 és a :864 a nyers javaslat szerint.
- **NYELV-510 (M6.4):** :435 „ha az eset túlságosan hasonlít a kvuca egy valódi tagjának helyzetére vagy a kvuca friss
  konfliktusára”; :519 „közös döntésre tanít:”; :521 „felelősségre tanít:”; a többi a nyers javaslat szerint.
- **NYELV-511 (M6.4):** a :874 kimarad; :679 „Melyik kis pillanatot volt ma jó átélni?”; a :680, :185, :790, :800 a
  nyers javaslat szerint.
- **NYELV-604 (M6.A):** :475 „De ha a játék menet közben láthatóan rosszul érint valakit (visszahúzódik, sírva fakad,
  kilép a körből, lefagy) – ne várj …”; :559 „kirekesztést már átélt gyerek”.
- **NYELV-605:** csak A:708 „amit a résztvevők az M6.B műhelyen kezdenek el, és a Moodle-ben adnak le”; A:62–63
  harmadik személy; B:356 „játszottak”; B:567 „ha csúszol”. A 2.3 tegezésre váltása és a „ti/te” egységesítése kimarad.
- **NYELV-607:** a B:76 „biztonsági mondatot” → „bátorító mondatot” csere kimarad; a többi a nyers javaslat szerint.
- **NYELV-608:** az A:447 kimarad; A:611 „amikor játékot választasz egy valós kvucának?”; a többi a nyers javaslat
  szerint.
- **NYELV-609 (M6.B):** :67 „drótvázát” → „áttekintő leírását”; a :21 és :71 „kézműves” csere kimarad (modulszintű);
  a :359 a nyers javaslat szerint.
- **NYELV-610:** az (a) A:451 kimarad; a (b)–(e) emberi döntés; az (e) baseline-ja ismert (QA M6.B:352 „Workshopban
  pedig egymásnak is tudnak majd visszajelzést adni”).
- **NYELV-611 (M6.B):** :418 „…amikor ember viselkedésére adsz SBI-t, a **B mindig megfigyelhető viselkedés**.” (a
  `a15ee79` M6.B:220 szövegéből).
- **NYELV-613 (M6.A):** :239 emberi döntés (a „Biztonsági keret +” címrész törlése vagy a keret pótlása); :498 utaló
  sor a 4.3.1 végére a nyers javaslat szerint.
- **NYELV-615:** A:488 „Itt a csendes sarok, bármikor visszajöhetsz, amikor jó.” (új „(mutass rá)” utasítás nem kerül
  be); a B:109–111 és az A:171 a nyers javaslat szerint.

## Duplikátumok és összekapcsolt tételek

- *dugma isit*: NYELV-105 (HUB:155) ↔ NYELV-401 (M6.3:727) ↔ NYELV-603 (M6.B) — egy emberi döntés.
- „Történet mint tükör”: NYELV-109 viszi (NYELV-205 :1467, NYELV-302) — csak átnevezéssel együtt.
- „akadálymentes”: NYELV-211 viszi (NYELV-108 beolvadt).
- adatvédelmi mondat: NYELV-513 viszi (M6.4:1019 és M6.2:903, NYELV-312).
- jelzési út dobozai: NYELV-301 ↔ NYELV-406 ↔ M6.4:1014 (NYELV-501).
- csoporton belül: NYELV-203 :887 → NYELV-212; NYELV-507 ↔ NYELV-509; NYELV-508 ↔ NYELV-608 (A:399);
  NYELV-604 ↔ NYELV-614 (A:475/481).

## Emberi döntést igénylő tételek

> **2026-10-04: mind eldöntve.** A projektgazda 23 kérdésre válaszolt: `2026-10-04 Projektgazdai döntések – M6 nyelvi
> review.md` (M6-NY-D1…D23; az UE-IMPL-4 is lezárult). Az alábbi táblázat a döntés előtti állapotot rögzíti.

| Terület | Tételek | Ki dönt |
|---|---|---|
| Gyermekvédelmi eszkaláció | NYELV-501 (kibillenés mint kiváltó feltétel), NYELV-301/-406 (részfelsorolás a §4.1 mellett), NYELV-101 364 (feltételes Memuna-bevonás), NYELV-602 (gyermekvédelmi helyzet-e) | projektgazda + Memuna |
| Értékelés | NYELV-103 (R1 kvantor), NYELV-104 (R2 szintek a migráció után), NYELV-115 (kötelező vs ajánlott), NYELV-410 (opciók személye) | értékelési felelős |
| Someres terminológia | NYELV-105/-401/-603 (*dugma isit*), NYELV-404 (zászló- és színhagyomány) | projektgazda / someres tartalomgazda |
| Tartalom, szerzői szándék | NYELV-214, NYELV-402, NYELV-405, NYELV-411, NYELV-503, NYELV-601, NYELV-610 (b–e), NYELV-613 (:239) | tartalomfelelős |
| Akadálymentesség | NYELV-403 („mellől elérhető” — a nyitott UE-IMPL-4) | projektgazda / hozzáférhetőségi felelős |

## Javítási következmények (a javítás előtt tudni kell)

- **Átnevezés:** NYELV-109 (M6.2 címe és fájlneve) és NYELV-203 (M6.1 címe) csak külön `git mv` commitban, minden
  hivatkozó hellyel és build-del.
- **Narráció (VO-újrarenderelés a VO QA-repóban):** NYELV-203 (480, 851, 488, 1077), NYELV-205 (853), NYELV-209,
  NYELV-213, NYELV-303, NYELV-408.
- **Látható szöveg:** minden tanulói szövegváltozás után pin (`--pin-visible`).
- **Answer key:** a ✅ helye egyik javaslatban sem mozdul; elosztó tartalma nem változik (a stílusból javasolt
  elosztó-cseréket a verifier kivette).
