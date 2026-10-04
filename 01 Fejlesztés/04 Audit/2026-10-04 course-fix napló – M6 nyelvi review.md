# course-fix napló – M6 nyelvi review (2026-10-04)

> **Audit trail, nem kánon.** A `/course-fix` futás állapota (nagy csomagos eljárás) és a célzott újraellenőrzés
> nyitott findingjai. Bizonyíték a fájlok végállapota, nem ez a napló.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-04 Nyelvi review – M6, Anna-baseline összevetés.md` (55 objektív finding,
  a „pontosított javaslatok” szakasz szerint) és `2026-10-04 Projektgazdai döntések – M6 nyelvi review.md`
  (M6-NY-D1…D23).
- **Bázis:** `main` @ `2a9060d`.
- **Terjedelem:** 223 lépés, 9 fájl (`02 Tervezet/Modulok/M6/`: hub, kapu, M6.1–M6.4, M6.A, M6.B, M6.F).
- **Módszer:** minden lépés bizonyíték → javítás párként rögzítve. A lépéseket először egy repón kívüli másolaton
  futtattam végig (0 eltérés: minden bizonyíték pontosan a várt számban állt). Utána `Edit`-tel vittem be őket a
  repóba. A kilenc fájl végállapota bájtra azonos a szimulált végállapottal. A lépésenkénti visszaellenőrzés szerint
  minden bizonyíték 0×, minden javítás legalább a várt számban szerepel.

## Összesítés

| Állapot | Lépés |
|---|---:|
| alkalmazva | 223 |
| már alkalmazva | 0 |
| kihagyva | 0 |
| megállva | 0 |

Két megszorítás az 1. kör végén, a táblázat soraiban is jelölve. Mindkettőt a 2. kör zárta le (lásd lent):

- **G26 (D20):** alkalmazva, de ütközött a kánonnal: a `Program terv.md:193, :248` és az `LMS – activity manifest.md:75,
  :160` szerint az M6 első kiadása nem függ a Moodle Workshoptól. Lásd UE7-BIZT-1. **2. kör: M6-NY-D24, R01.**
- **E07 (D12):** a D12 első fele (a 176. sori szűrő) alkalmazva. A második fele, a ma 574. sor („A kieséses /
  felállásra kényszerítő verzió a rossz minta.”) pontosítása az 1. körben **nem volt átvezetve**. A pontos
  megfogalmazás nem volt egyértelműen levezethető a döntésből, ezért a javítás nem talált ki szöveget. Lásd UE7-PED-3.
  **2. kör: M6-NY-D25, R02.**

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| K01 | NYELV-102 | kapu | alkalmazva |  |
| K02 | NYELV-102 | kapu | alkalmazva | Completion-logika és küszöb nem változik. |
| K03 | NYELV-103; M6-NY-D5 | kapu | alkalmazva | Rubrika-kvantor (vétólista). |
| K04 | NYELV-103; M6-NY-D5 | kapu | alkalmazva | Rubrika-kvantor (vétólista). |
| K05 | NYELV-104; M6-NY-D6 | kapu | alkalmazva | Az „Erős” szint feltétele (korosztály-jellemzővel indokol) változatlan; a típusnév-bónusz kikerül (vétólista). |
| K06 | NYELV-107 | kapu | alkalmazva |  |
| K07 | NYELV-107 | kapu | alkalmazva |  |
| K08 | NYELV-107 | kapu | alkalmazva |  |
| K09 | NYELV-107 | kapu | alkalmazva |  |
| K10 | NYELV-107 | kapu | alkalmazva |  |
| K11 | NYELV-211 (NYELV-108) | kapu | alkalmazva | A ✅ helye nem változik (vétólista). |
| K12 | NYELV-211 (NYELV-108) | kapu | alkalmazva |  |
| K13 | NYELV-110 | kapu | alkalmazva | Csak írásjel; a ✅ helye nem változik. |
| K14 | NYELV-110 | kapu | alkalmazva |  |
| K15 | NYELV-111 | kapu | alkalmazva |  |
| K16 | NYELV-111 | kapu | alkalmazva |  |
| K17 | NYELV-111 | kapu | alkalmazva |  |
| K18 | NYELV-111 | kapu | alkalmazva |  |
| K19 | NYELV-111 | kapu | alkalmazva | Gyermekvédelmi megfogalmazás (vétólista); a szabály nem változik. |
| K20 | NYELV-114 | kapu | alkalmazva |  |
| K21 | NYELV-114 | kapu | alkalmazva |  |
| K22 | NYELV-101 | kapu | alkalmazva | Az M6.A 4.3.2/B szóhasználata. |
| K23 | NYELV-101 | kapu | alkalmazva | Az M6.A:484 mintamondata szó szerint. |
| K24 | NYELV-608 következménye (M6.A:492) | kapu | alkalmazva | A KAPU az M6.A négy lépését idézi; a ✅ helye nem változik. |
| K25 | NYELV-101 | kapu | alkalmazva |  |
| K26 | NYELV-101; M6-NY-D3; NYELV-608 következménye | kapu | alkalmazva | Gyermekvédelmi eszkaláció (vétólista): az M6.A:496 feltételes alakja szó szerint (D3). |
| K27 | NYELV-115; M6-NY-D7 | kapu | alkalmazva | Kötelező ↔ ajánlott a D7 szerint (vétólista). |
| H01 | NYELV-114 | hub | alkalmazva |  |
| H02 | NYELV-110 | hub | alkalmazva |  |
| H03 | NYELV-105; M6-NY-D9 | hub | alkalmazva |  |
| H04 | NYELV-110 | hub | alkalmazva |  |
| H05 | NYELV-110 | hub | alkalmazva |  |
| H06 | NYELV-104; M6-NY-D6 | hub | alkalmazva | Rubrikaszint (vétólista): a hub a KAPU „Erős” szintjét követi. |
| H07 | NYELV-106 | hub | alkalmazva |  |
| H08 | NYELV-106 | hub | alkalmazva |  |
| H09 | NYELV-102 | hub | alkalmazva | Completion-logika nem változik (a 3. pont eddig is „nem feltétel”). |
| H10 | NYELV-110 | hub | alkalmazva |  |
| H11 | NYELV-114 | hub | alkalmazva |  |
| F01 | NYELV-112 | M6.F | alkalmazva | Gyermekvédelmi szerephatár (vétólista): csak a személyrag; a feltétel szó szerint marad. |
| F02 | NYELV-112 | M6.F | alkalmazva |  |
| F03 | NYELV-112 | M6.F | alkalmazva |  |
| F04 | NYELV-112 | M6.F | alkalmazva |  |
| F05 | NYELV-112 | M6.F | alkalmazva |  |
| F06 | NYELV-112 | M6.F | alkalmazva |  |
| F07 | NYELV-112 | M6.F | alkalmazva |  |
| F08 | NYELV-112 | M6.F | alkalmazva |  |
| F09 | NYELV-112 | M6.F | alkalmazva | Ugyanez a sablon az M5.F-ben és az M7.F-ben: külön modul-review. |
| F10 | NYELV-112 | M6.F | alkalmazva |  |
| F11 | NYELV-112 | M6.F | alkalmazva |  |
| F12 | NYELV-110 | M6.F | alkalmazva |  |
| F13 | NYELV-114 | M6.F | alkalmazva |  |
| F14 | NYELV-114 | M6.F | alkalmazva |  |
| F15 | NYELV-114 | M6.F | alkalmazva |  |
| A01 | NYELV-201 | M6.1 | alkalmazva | A ✅, az opciók és a visszajelzések nem változnak. |
| A02 | NYELV-203 | M6.1 | alkalmazva |  |
| A03 | NYELV-203 | M6.1 | alkalmazva |  |
| A04 | NYELV-203 | M6.1 | alkalmazva | A modulhub 84. sorának kategórianeve. |
| A05 | NYELV-203 | M6.1 | alkalmazva |  |
| A06 | NYELV-203 | M6.1 | alkalmazva |  |
| A07 | NYELV-203 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A08 | NYELV-203 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A09 | NYELV-203 (a fájl többi előfordulása) (`replace_all`, 4×) | M6.1 | alkalmazva | Asset-mezők és a dia célsora (751, 752, 787, 826). |
| A10 | NYELV-203 | M6.1 | alkalmazva |  |
| A11 | NYELV-203 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A12 | NYELV-203 | M6.1 | alkalmazva | Csak helyesírás; a ✅ helye nem változik. |
| A13 | NYELV-203 | M6.1 | alkalmazva |  |
| A14 | NYELV-214; M6-NY-D11 | M6.1 | alkalmazva |  |
| A15 | NYELV-214; M6-NY-D11 | M6.1 | alkalmazva | A fiktív eset és a biztonsági minimum (1061–1064) nem változik. |
| A16 | NYELV-214; M6-NY-D11 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A17 | NYELV-204 | M6.1 | alkalmazva | Answer key szövege (vétólista): csak a személyrag; a ✅ helye nem változik. |
| A18 | NYELV-204 | M6.1 | alkalmazva | A spec idézete a lecke szövegét követi. |
| A19 | NYELV-205 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A20 | NYELV-206 | M6.1 | alkalmazva | Elosztó: tartalom nem változik, csak a szerkezet (a ✅-opcióval párhuzamos). |
| A21 | NYELV-206 | M6.1 | alkalmazva | Elosztó: tartalom nem változik. |
| A22 | NYELV-207 | M6.1 | alkalmazva | A ✅ nem változik. |
| A23 | NYELV-207 | M6.1 | alkalmazva |  |
| A24 | NYELV-207 | M6.1 | alkalmazva |  |
| A25 | NYELV-207 | M6.1 | alkalmazva |  |
| A26 | NYELV-208 | M6.1 | alkalmazva |  |
| A27 | NYELV-208 | M6.1 | alkalmazva |  |
| A28 | NYELV-208 | M6.1 | alkalmazva | Biztonsági tartalom nem változik. |
| A29 | NYELV-211 | M6.1 | alkalmazva |  |
| A30 | NYELV-208 | M6.1 | alkalmazva |  |
| A31 | NYELV-208 | M6.1 | alkalmazva | Biztonsági tartalom nem változik. |
| A32 | NYELV-208, NYELV-211 | M6.1 | alkalmazva | A spec a lecke szövegét követi. A specben az „ütközés-kerülés” „ütközés” lett: elveszett minősítő, lásd UE7-NYELV-2. |
| A33 | NYELV-209 | M6.1 | alkalmazva | A „fiktív eset, kívülről” védelem marad. Narráció (VO-újrarenderelés). |
| A34 | NYELV-209 | M6.1 | alkalmazva |  |
| A35 | NYELV-209 | M6.1 | alkalmazva |  |
| A36 | NYELV-210 (`replace_all`, 2×) | M6.1 | alkalmazva | Az alt-szöveg és a spec egyezően. |
| A37 | NYELV-211 | M6.1 | alkalmazva |  |
| A38 | NYELV-211 | M6.1 | alkalmazva | A négy elem tartalma és sorrendje nem változik. |
| A39 | NYELV-211 | M6.1 | alkalmazva |  |
| A40 | NYELV-212 (NYELV-203) | M6.1 | alkalmazva | A kilépési védelem nem változik. |
| A41 | NYELV-213 | M6.1 | alkalmazva |  |
| A42 | NYELV-213 | M6.1 | alkalmazva | Narráció (VO-újrarenderelés). |
| A43 | NYELV-213 | M6.1 | alkalmazva | A spec a lecke szövegét követi. |
| A44 | NYELV-215 | M6.1 | alkalmazva |  |
| A45 | NYELV-215 | M6.1 | alkalmazva |  |
| A46 | M6-NY-D22 (NYELV-403; UE-IMPL-4) (`replace_all`, 8×) | M6.1 | alkalmazva | VO D-19 szó szerint; minden ilyen sor. |
| B01 | NYELV-301; M6-NY-D2 | M6.2 | alkalmazva | Gyermekvédelmi doboz (vétólista): csak a „nyugodtan” törlése; minden védelmi elem marad. |
| B02 | NYELV-303 | M6.2 | alkalmazva |  |
| B03 | NYELV-303 | M6.2 | alkalmazva | Az asset-cím a dia címét követi. |
| B04 | NYELV-303 | M6.2 | alkalmazva | Az M6.2-VID-01 narrációja (VO, videó, felirat, leirat). |
| B05 | NYELV-305 | M6.2 | alkalmazva |  |
| B06 | NYELV-305 | M6.2 | alkalmazva |  |
| B07 | NYELV-305 | M6.2 | alkalmazva | Az IKO-01 spec a lecke szövegét követi. |
| B08 | NYELV-308 | M6.2 | alkalmazva | Az opciók és a ✅ helye nem változik. |
| B09 | NYELV-308 | M6.2 | alkalmazva |  |
| B10 | NYELV-309 | M6.2 | alkalmazva |  |
| B11 | NYELV-310 | M6.2 | alkalmazva | A ✅ és a visszajelzések nem változnak. |
| B12 | NYELV-311 | M6.2 | alkalmazva |  |
| B13 | NYELV-311 | M6.2 | alkalmazva | Az asset-cím a dia címét követi. |
| B14 | NYELV-311 | M6.2 | alkalmazva |  |
| B15 | NYELV-513 (NYELV-312) | M6.2 | alkalmazva | Adatvédelmi megfogalmazás (vétólista): szerepkör vagy megőrzés nem kerül be; a védőmondat marad. |
| B16 | NYELV-314 | M6.2 | alkalmazva | Az opciók és a ✅ helye nem változik. |
| B17 | M6-NY-D22 (NYELV-403; UE-IMPL-4) (`replace_all`, 8×) | M6.2 | alkalmazva | VO D-19 szó szerint; minden ilyen sor. |
| C01 | NYELV-405; M6-NY-D14 | M6.3 | alkalmazva |  |
| C02 | NYELV-412 | M6.3 | alkalmazva | Elosztó: csak tipográfia. |
| C03 | NYELV-412 | M6.3 | alkalmazva | Answer key szövege: csak tipográfia; a ✅ helye nem változik. |
| C04 | NYELV-412 | M6.3 | alkalmazva |  |
| C05 | NYELV-401; M6-NY-D9 | M6.3 | alkalmazva | Someres terminológia (D9): a *dugma isit* csak a madrihra; az egalitás-rész marad. |
| C06 | NYELV-402; M6-NY-D13 | M6.3 | alkalmazva | A „ne legyen kötelező” és a két másik lehetőség szó szerint marad (vétólista: kiskorú önfeltárási kilépés). |
| C07 | NYELV-406; M6-NY-D2 | M6.3 | alkalmazva | Gyermekvédelmi doboz (vétólista): mondatokra bontva, a „nyugodtan” nélkül; minden elem szó szerint marad. |
| C08 | NYELV-404; M6-NY-D10, M6-NY-D23 | M6.3 | alkalmazva | Someres keret: a hivatkozás marad (D10); a szabály hatóköre a D23 szerint. |
| C09 | NYELV-407 | M6.3 | alkalmazva | Továbbra is egy variációt kér; az R5-fordulat szó szerint marad. |
| C10 | NYELV-408 | M6.3 | alkalmazva | Narráció (VO-újrarenderelés). |
| C11 | NYELV-410; M6-NY-D8 | M6.3 | alkalmazva | A visszajelzés a ✅-opció személyét követi. |
| C12 | NYELV-410; M6-NY-D8 | M6.3 | alkalmazva | Answer key szövege (vétólista): csak a személy; tartalom és ✅ helye változatlan. |
| C13 | NYELV-411; M6-NY-D15 | M6.3 | alkalmazva |  |
| C14 | M6-NY-D22 (NYELV-403; UE-IMPL-4) (`replace_all`, 6×) | M6.3 | alkalmazva | VO D-19 szó szerint; minden ilyen sor. |
| D01 | NYELV-507 | M6.4 | alkalmazva |  |
| D02 | NYELV-511 | M6.4 | alkalmazva |  |
| D03 | NYELV-507 | M6.4 | alkalmazva |  |
| D04 | NYELV-504 | M6.4 | alkalmazva |  |
| D05 | NYELV-512 | M6.4 | alkalmazva |  |
| D06 | NYELV-510 | M6.4 | alkalmazva |  |
| D07 | NYELV-509 | M6.4 | alkalmazva |  |
| D08 | NYELV-507 | M6.4 | alkalmazva |  |
| D09 | NYELV-512 | M6.4 | alkalmazva |  |
| D10 | NYELV-510 | M6.4 | alkalmazva |  |
| D11 | NYELV-510 | M6.4 | alkalmazva |  |
| D12 | NYELV-504 | M6.4 | alkalmazva |  |
| D13 | NYELV-507 | M6.4 | alkalmazva |  |
| D14 | NYELV-510 | M6.4 | alkalmazva |  |
| D15 | NYELV-503; M6-NY-D16 | M6.4 | alkalmazva |  |
| D16 | NYELV-503; M6-NY-D16 | M6.4 | alkalmazva |  |
| D17 | NYELV-510 | M6.4 | alkalmazva |  |
| D18 | NYELV-511 | M6.4 | alkalmazva |  |
| D19 | NYELV-508 | M6.4 | alkalmazva |  |
| D20 | NYELV-511 | M6.4 | alkalmazva |  |
| D21 | NYELV-508, NYELV-511 | M6.4 | alkalmazva |  |
| D22 | NYELV-510 | M6.4 | alkalmazva |  |
| D23 | NYELV-512 | M6.4 | alkalmazva | Gombfelirat: a „/” marad (NYELV-507). |
| D24 | NYELV-509 | M6.4 | alkalmazva |  |
| D25 | NYELV-510 | M6.4 | alkalmazva |  |
| D26 | NYELV-510 | M6.4 | alkalmazva | A páros megbeszélés és az önkéntesség marad. |
| D27 | NYELV-508 | M6.4 | alkalmazva |  |
| D28 | NYELV-507 | M6.4 | alkalmazva |  |
| D29 | NYELV-504 | M6.4 | alkalmazva |  |
| D30 | NYELV-508 | M6.4 | alkalmazva |  |
| D31 | NYELV-507, NYELV-505 | M6.4 | alkalmazva |  |
| D32 | NYELV-505 | M6.4 | alkalmazva |  |
| D33 | NYELV-505 | M6.4 | alkalmazva |  |
| D34 | NYELV-505 | M6.4 | alkalmazva | Az opciók, a ✅ és a visszajelzés nem változik. |
| D35 | NYELV-507 | M6.4 | alkalmazva |  |
| D36 | M6-NY-D2 (NYELV-501 mellékpont) | M6.4 | alkalmazva | Gyermekvédelmi doboz (vétólista): csak a „nyugodtan” törlése. |
| D37 | NYELV-501; M6-NY-D1 | M6.4 | alkalmazva | Gyermekvédelmi kiváltó feltétel (vétólista): a 826–828. sori változathoz igazítva (D1). A „nemcsak „kibillen”, hanem …” résztől a mondat végéig betűre azonos; a bevezető („egy erős élményjáték közben”) a helyi előzmény miatt eltér (UE7-BIZT-2). A védelmi elemek változatlanok. |
| D38 | NYELV-507, NYELV-510 | M6.4 | alkalmazva |  |
| D39 | NYELV-513 | M6.4 | alkalmazva | Adatvédelmi megfogalmazás (vétólista): szerepkör vagy megőrzés nem kerül be. |
| E01 | NYELV-607 | M6.A | alkalmazva |  |
| E02 | NYELV-608 | M6.A | alkalmazva |  |
| E03 | NYELV-605 | M6.A | alkalmazva |  |
| E04 | NYELV-605 | M6.A | alkalmazva |  |
| E05 | NYELV-607 | M6.A | alkalmazva | A „felkavart kiskorút nem küldünk ki egyedül” védelem marad. |
| E06 | NYELV-615 | M6.A | alkalmazva | A lassú tempó, a „nincs kiesés”, a „nincs gyorsítás” és a passz lehetősége szó szerint marad. |
| E07 | NYELV-601; M6-NY-D12 | M6.A | alkalmazva (a D12 első fele) | Biztonsági szűrő (vétólista): a feltételes olvasat a kánon (D12). A D12 második fele (a ma 574. sor pontosítása) **nincs átvezetve, jelezve**: lásd UE7-PED-3. |
| E08 | NYELV-613; M6-NY-D21 | M6.A | alkalmazva | Az időtartam nem változik; a biztonsági keret a 4.3.1-ben marad. |
| E09 | NYELV-607 | M6.A | alkalmazva |  |
| E10 | NYELV-608 | M6.A | alkalmazva |  |
| E11 | NYELV-608 | M6.A | alkalmazva |  |
| E12 | NYELV-614 | M6.A | alkalmazva |  |
| E13 | NYELV-608 | M6.A | alkalmazva |  |
| E14 | NYELV-608 | M6.A | alkalmazva |  |
| E15 | NYELV-604 | M6.A | alkalmazva | Gyermekvédelmi beavatkozás (vétólista): a jelek és az „azonnal lépj” változatlanok; a kiváltó kör nem szűkül. |
| E16 | NYELV-614 | M6.A | alkalmazva |  |
| E17 | NYELV-608 | M6.A | alkalmazva |  |
| E18 | NYELV-615 | M6.A | alkalmazva |  |
| E19 | NYELV-608 | M6.A | alkalmazva |  |
| E20 | NYELV-613 | M6.A | alkalmazva | Csak utaló sor; a 4.3.2/B szövege nem változik. |
| E21 | NYELV-608 | M6.A | alkalmazva |  |
| E22 | NYELV-608 | M6.A | alkalmazva |  |
| E23 | NYELV-604 | M6.A | alkalmazva |  |
| E24 | NYELV-610 (b); M6-NY-D17 | M6.A | alkalmazva |  |
| E25 | NYELV-608 | M6.A | alkalmazva |  |
| E26 | NYELV-608 | M6.A | alkalmazva |  |
| E27 | NYELV-614 | M6.A | alkalmazva |  |
| E28 | NYELV-605 | M6.A | alkalmazva |  |
| G01 | NYELV-607 | M6.B | alkalmazva |  |
| G02 | NYELV-610 (c); M6-NY-D18 | M6.B | alkalmazva |  |
| G03 | NYELV-609 | M6.B | alkalmazva |  |
| G04 | NYELV-607 | M6.B | alkalmazva |  |
| G05 | NYELV-610 (c); M6-NY-D18 | M6.B | alkalmazva | Az időtartam nem változik. |
| G06 | NYELV-603; M6-NY-D9 | M6.B | alkalmazva |  |
| G07 | NYELV-615 | M6.B | alkalmazva | A felolvasandó lista szövege nem változik. |
| G08 | NYELV-607, NYELV-614 | M6.B | alkalmazva | A sorvégi fölösleges szóköz is kikerül. |
| G09 | NYELV-606 | M6.B | alkalmazva | A 49–50. sor és a legyártott sablon szövege. |
| G10 | NYELV-610 (d); M6-NY-D19 | M6.B | alkalmazva |  |
| G11 | NYELV-614 | M6.B | alkalmazva |  |
| G12 | NYELV-614 | M6.B | alkalmazva |  |
| G13 | NYELV-605 | M6.B | alkalmazva |  |
| G14 | NYELV-609 | M6.B | alkalmazva |  |
| G15 | NYELV-610 (c); M6-NY-D18 | M6.B | alkalmazva |  |
| G16 | NYELV-612 | M6.B | alkalmazva | A POSZ-01 spec mintamondata a 422. sort követi. |
| G17 | NYELV-111 (az M6.B asset-jegyzete) | M6.B | alkalmazva |  |
| G18 | NYELV-611 | M6.B | alkalmazva | A `a15ee79` M6.B:220 szövege. |
| G19 | NYELV-612 | M6.B | alkalmazva |  |
| G20 | NYELV-603; M6-NY-D9 | M6.B | alkalmazva |  |
| G21 | NYELV-603; M6-NY-D9 | M6.B | alkalmazva |  |
| G22 | NYELV-602; M6-NY-D4 | M6.B | alkalmazva | Gyermekvédelmi címzett (vétólista): az M6.A:180 mondata, csak a személyrag igazítva (HUM-SAFE-01). |
| G23 | NYELV-607 | M6.B | alkalmazva |  |
| G24 | NYELV-602; M6-NY-D4 | M6.B | alkalmazva | Gyermekvédelmi címzett (vétólista): az M6.A:180 mondata, csak a személyrag igazítva (HUM-SAFE-01). |
| G25 | NYELV-605 | M6.B | alkalmazva |  |
| G26 | NYELV-610 (e); M6-NY-D20 | M6.B | alkalmazva — kánon-ütközés, lásd UE7-BIZT-1 | A Moodle-tevékenység neve (UI-elem) visszakerül; ütközik a `Program terv.md:248` és az `LMS – activity manifest.md:160` szövegével. |

## Szándékosan nem ebben a futásban

| Tétel | Ok |
|---|---|
| NYELV-109, NYELV-302 (az M6.2 címe és fájlneve: „Történet mint tükör”) | átnevezés: külön `git mv` commit, minden hivatkozó hellyel és builddel |
| NYELV-203 — az M6.1 címe („játék-kategória”) | átnevezés: ugyanígy külön commit |
| NYELV-112 — M6.F:95 (többes szám 2. személy) | a nyers finding nem ad pontos javaslatot; nem rekonstruálva |
| NYELV-509 — M6.4:175, :753, :736 (kötőszó a „Cél:” sorokban) | a review szerint szerzői döntés, és nem került a 2026-10-04-i kérdések közé: nyitott a lecke tartalomfelelősénél |

## Ellenőrzések

A végállapot lépésenként visszaolvasva (223/223), a teljes M6-diff visszaolvasva. `py_compile` OK ·
`content_integrity.py` 0 ERROR · `--pin-visible` egyszer, 9 fájl (ok: „M6 nyelvi review (NYELV-101…615, 2026-10-04) és
M6-NY-D1…D23: 223 lépés a validált findingok és a projektgazdai döntések szerint”) · `build` ×2 stabil · `check` OK ·
`reconcile` 747/747 · `validate` OK · `lint --high-only` 0 · `unittest tools.test_media_manifest` OK ·
`git diff --check` és a PR-tartományé tiszta · hangnév-ellenőrzés a diffen 0 találat · `RELEASE-VERDICT: NO-GO`
(változatlan, 6 blocker). A záró `/release-check` eredménye a futás jelentésében.

## VO-újrarenderelés (a VO QA-repóban)

Forrásszövege (`Forrás-hash`) változott, újra kell renderelni: **M6.1-NAR-03, M6.1-NAR-05, M6.1-NAR-06, M6.1-NAR-07,
M6.2-VID-01** (narráció, felirat, leirat), **M6.3-NAR-06**.

Csak a gyártási spec (`Spec-hash`), a cím vagy az a11y-mező változott, hangfelvétel nem kell: M6.1-DIA-01, M6.1-EGY-08,
M6.1-EGY-09, M6.1-EGY-11, M6.1-IKO-01, M6.1-ILL-02, M6.1-VID-01, M6.2-IKO-01, M6.2-NAR-06, M6.B-MUNK-02 (2. kör),
M6.B-MUNK-06, M6.B-POSZ-01. Az M6.B-MUNK-01, -03, -04 és -05 sorában csak a forrás sorszáma tolódott el.

A lista a 2. kör után a `HEAD`-hez mért `assetek.csv` hash-összevetésből készült: a `Forrás-hash` pontosan a fenti hat
elemnél változott, a 2. kör narrációt nem érintett.

## Célzott újraellenőrzés az 1. kör után (UE7)

Négy lencse-reviewer (nyelv, biztonság, értékelés, pedagógia) a diff-hunkokon. 13 finding, összevonva 12 tétel. Az
állításokat a fájlokban visszaellenőriztem. **Állapot a 2. kör után:** a projektgazda a négy döntési tételt eldöntötte
(M6-NY-D24…D27), a hat objektív tételt a 2. kör javította. Az UE7-BIZT-2 rögzítve, teendő nincs.

| ID | Hely | Probléma (röviden) | Javaslat | Típus |
|---|---|---|---|---|
| UE7-BIZT-1 = UE7-PED-1 | M6.B:576 ↔ `Program terv.md:193, :248`, `LMS – activity manifest.md:75, :160` | A D20 visszahozta a Moodle Workshopot, a kánon (93b2fa3, 2026-09-29) viszont az M6 első kiadásából kizárja. Ráadásul új tanulói adatfolyam: a társak látják egymás játéklapját. A D20 kérdése ezt a kánoni hátteret nem mutatta meg. | A projektgazda dönt (a társértékelés adatköre miatt a DPO-val): (a) a Workshop bekerül az első kiadásba → Program terv, LMS-manifest, `Adatvédelem` §5, completion, R4/R5 végső pont; vagy (b) az M6.B:576 a kánonhoz igazodik, a „Workshop” nélkül. Addig a 576. sorhoz tartalmilag nem nyúlunk. | emberi-döntés |
| UE7-PED-2 | M6.B:86, :373 ↔ 4.4.1–4.4.2 (:426, :446–467), :569 | A D18 után a percbontás két párhuzamos félcsoportot ír, a lépésleírás viszont egyetlen, képző által moderált plénumot. Nem derül ki, ki vezeti a második félcsoportot, és hogy a 2–3 bemutató félcsoportonként értendő-e. | Objektív rész: a 4.4.1–4.4.2 mondja ki, hogy mindkét félcsoportban fut, és a szám félcsoportonként értendő. Emberi döntés (a peula tartalomfelelőse): ki vezeti a második félcsoportot. | emberi-döntés (részben objektív) |
| UE7-PED-3 | M6.A:574 ↔ :176 | A D12 második fele nincs átvezetve. A 176. sor csak a tét nélküli kiesős játékot zárja ki, az 574. sor viszont feltétel nélkül nevezi rossz mintának a kieséses verziót. | A döntés szerint pontosítandó, új szabály nélkül. Jelölt: „Ennél a játéknál a kieséses / felállásra kényszerítő verzió a rossz minta.” Hogy a „Szél fújja” kiesése „tét nélküli”-e, azt a peula tartalomfelelőse hagyja jóvá. | objektív (a megfogalmazás jóváhagyásra vár) |
| UE7-PED-4 | M6.4:1014 és :826 ↔ KAPU:364 | Az új blokk szembeállítja a „kibillenést” a feltárással, de a kibillenésre nem ad teendőt. A kapu (D3) és az M6.A 4. lépése szerint erős érintettségnél ilyenkor is be kell vonni a Memunát. | Emberi döntés (projektgazda, Memuna-QA): kerüljön-e mindkét blokkba azonos, rövid utalás az M6.A 4.3.2/B négy lépésére. A D1 kiváltó feltétele nem változik. | emberi-döntés |
| UE7-ERT-1 | hub:211 ↔ KAPU:394 | A hub R2 „Erős” összefoglalójából hiányzik a kapucella két eleme: a hangulat/állapot, illetve hogy melyik korosztálynak nem való. Részben régi eltérés. | A kapucella két meglévő eleme szó szerint kerüljön a hubba (D6). A kapucellához és a küszöbhöz nem nyúlunk. | objektív |
| UE7-ERT-2 | KAPU:394, :404; M6.B:221 | A D6 válasza szerint az „Oké” szinten elég a korosztály neve vagy évszáma. Ez nincs átvezetve, a törölt bónuszmondattal pedig az egyetlen utalás is kikerült. | Az „Oké” cellába, a 404. sori listába és az M6.B:221-be: „(név vagy évszám)”. | objektív |
| UE7-ERT-3 | M6.B:220 ↔ KAPU:403 | Az M6.B rubrika-felütésében maradt az „1 konkrét” cél. | „legalább 1 konkrét” (D5). | objektív |
| UE7-NYELV-1 | KAPU:352 | Mondatba ágyazott, zárójeles idézet végén pont. | „(„Álljunk meg egy pillanatra, legyen egy kis levegő”),”; a ✅ helye nem változik. | objektív |
| UE7-NYELV-2 | M6.1:1158 (spec) | Elveszett minősítő (A32): a felsorolásban „ütközés” áll a teendő („ütközés-kerülés”) helyett. | „; ütközés elkerülése;”. A dia „**ütközés:**” címkéje marad. | objektív |
| UE7-NYELV-3 | M6.2:177 (spec) | Az új „érezni, nem csak gondolkodni” vessző miatt a megfeleltetések határa nem látszik. | Idézőjelben, mint az alt-szövegben (269). | objektív |
| UE7-BIZT-2 | M6.4:1014 ↔ :826 | A két blokk bevezetője eltér; a kiváltó feltételtől a végéig betűre azonos. Védelmi hatása nincs. | Nincs teendő; a napló ezt rögzíti. Az egységesítés legfeljebb nyelvi kérdés. | objektív (rögzítve) |

Egy nem jelentett megfigyelés (UE7-NYELV): az M6.B:523/:565 mondatában („kinek jelzel / kihez fordulsz …: a kijelölt
Memunának”) a válasz csak a „kinek” kérdéshez illik. Ez az M6.A:180 kánoni mondatából jön, csak mindhárom helyen
együtt javítható.

## 2. kör — M6-NY-D24…D27 és a UE7 objektív tételek (2026-10-04)

- **Forrás:** a projektgazda 7. körös döntései (`2026-10-04 Projektgazdai döntések – M6 nyelvi review.md`, M6-NY-D24…D27;
  a D24 a D20 Workshopra vonatkozó részét felülírja) és a fenti UE7 objektív tételek (ERT-1, ERT-2, ERT-3, NYELV-1,
  NYELV-2, NYELV-3). Utána két rövid lencse-kör (UE8, UE9) a 2. kör saját sorain; ezek objektív findingjai ugyanebben
  a körben javítva.
- **Bázis:** az 1. kör végállapota (ugyanaz a munkafa, commit nélkül).
- **D6 átvezetése:** a projektgazda válasza „név vagy évszám”. A szövegbe „elég a név vagy az életkor” került, mert az
  „évszám” magyarul naptári évet jelent, a válasz pedig a 6–9 típusú életkorsávra vonatkozik. A nyelvi lencse ezt
  helyesnek ítélte (UE8).

| ID | alap | hely (a 2. kör végén) | állapot | megjegyzés |
|---|---|---|---|---|
| R01 | M6-NY-D24 (UE7-BIZT-1 = UE7-PED-1) | M6.B:581–583 (5. lista, 6. pont) | alkalmazva | A Workshop-tagmondat helyett a projektgazda mintamondata. Program terv, LMS-manifest, `Adatvédelem` §5 változatlan (vétólista). |
| R02 | M6-NY-D25 (UE7-PED-3; a D12 második fele) | M6.A:574 | alkalmazva | Szó szerint a projektgazda mondata (vétólista: biztonsági szűrő). |
| R03 | M6-NY-D26 (UE7-PED-2) | M6.B:88 (percbontás) | alkalmazva | Félcsoportonként 2–3 bemutató; a második félcsoportot előre kijelölt felnőtt stábtag vezeti. Időtartam változatlan. |
| R04 | M6-NY-D26 | M6.B:375 (blokkcél) | alkalmazva |  |
| R05 | M6-NY-D26; UE8-PED-2; UE9-PED-3; UE9-NYELV-2 | M6.B:378 (4.4 „Szervezés”) | alkalmazva | A 4.4.1 nagycsoportban, utána szétválás; résztvevő nem vezet félcsoportot (vétólista: szerephatár); közös időszelep; a 40. perc a határ. |
| R06 | M6-NY-D26; UE8-NYELV-1 | M6.B:416 | alkalmazva | A három kérdés a második félcsoportnak is (második flipchart vagy nyomtatva). |
| R07 | M6-NY-D26 | M6.B:430 (4.4.1 instrukció) | alkalmazva |  |
| R08 | M6-NY-D26 | M6.B:454 (4.4.2, 1. lépés) | alkalmazva |  |
| R09 | M6-NY-D26 | M6.B:575 (időszelep) | alkalmazva | „félcsoportonként 2 helyett 1”. |
| R10 | UE8-PED-2 (a D26 előkészítése) | M6.B:57 (2.1) | alkalmazva |  |
| R11 | UE8-PED-2; UE9-PED-2; UE9-PED-3; UE9-NYELV-1 | M6.B:79 (2.3) | alkalmazva | A második vezető kijelölése és eligazítása, benne a biztonsági keret (5. lista, 4. pont). |
| R12 | UE8-PED-2 | M6.B:564 (5. lista, 2. pont) | alkalmazva |  |
| R13 | UE8-PED-2 | M6.B:528 (M6.B-MUNK-06 spec, 2. blokk) | alkalmazva | A lista tükre a specben. |
| R14 | UE8-PED-4 (D24) | M6.B:515 (4.5 záró mondatok) | alkalmazva | A D24 mintamondata tegező alakban. |
| R15 | UE7-ERT-3 (D5) | M6.B:222 | alkalmazva | „legalább 1” (vétólista: rubrika). |
| R16 | UE7-ERT-2 (D6) | M6.B:223 | alkalmazva | Vétólista: rubrika. |
| R17 | UE7-ERT-2, UE7-ERT-3 (D5, D6) | M6.B:139 (M6.B-MUNK-02 spec) | alkalmazva | A kapu „Oké”-listájának tükörhelye. |
| R18 | UE7-ERT-2 (D6) | KAPU:394 („Oké” cella) | alkalmazva | Vétólista: rubrika; küszöb és blokkoló logika változatlan. |
| R19 | UE7-ERT-2 (D6) | KAPU:404 | alkalmazva | Vétólista: rubrika. |
| R20 | UE7-NYELV-1 | KAPU:352 | alkalmazva | Írásjel egy ✅-opcióban; a ✅ helye nem változik. |
| R21 | UE7-ERT-1, UE7-ERT-2 (D6) | hub:211 | alkalmazva | A kapucella hangulat/állapot és „melyiknek nem” eleme (vétólista: rubrikaszint). |
| R22 | UE7-NYELV-2 | M6.1:1158 (spec) | alkalmazva | „ütközés elkerülése”. |
| R23 | UE7-NYELV-3; UE8-NYELV-2 | M6.2:177 (spec) | alkalmazva | A szív és a tükör idézőjelben (mint a 269. sori alt-útmutatóban); a kérdőjel fogalomleírás marad. |
| R24 | M6-NY-D27 (UE7-PED-4); UE8-PED-1; UE9-BIZT-1 = UE9-PED-1 | M6.4:832–834 | alkalmazva | Vétólista (gyermekvédelem): a négy lépés a KAPU:364 megfogalmazásával; a 2. lépésnél az M6.A:492 („felkavart kiskorút nem küldünk ki egyedül, legyen vele egy felnőtt”); a Memuna-küszöb szó szerint az M6.A:498 („ha valaki erősen érintett”); a D1 kiváltó feltétele változatlan. |
| R25 | ugyanaz | M6.4:1017 | alkalmazva | Tördelés nélkül betűre azonos az R24-gyel (ellenőrizve). |

**Lencse-körök a 2. kör sorain:**

- **UE8** (az első javítások után; nyelv, biztonság, értékelés, pedagógia): BIZT 0 és ERT 0 finding. PED 4: a PED-1,
  -2 és -4 javítva (R24/R25, R05/R10–R13, R14); a PED-3 emberi döntés, lásd lent. NYELV 2, mindkettő javítva (R06,
  R23).
- **UE9** (az UE8-javítások után; nyelv, biztonság, pedagógia): BIZT 1 = PED-1 (a 2. lépés védelmi eleme) javítva
  (R24/R25). PED-2 és PED-3 javítva (R11, R05). NYELV-1 és NYELV-2 javítva (R11, R05) a lencse pontos javaslata
  szerint.
- Az UE9-javítások után újabb lencse-kör nem futott. A végállapotot visszaolvastam, a két M6.4-blokk azonosságát
  géppel ellenőriztem.

**Nyitva maradt:**

| ID | Hely | Probléma | Típus |
|---|---|---|---|
| UE8-PED-3 | M6.B:88, :378 | Nincs utasítás arra az esetre, ha a peulán nincs második felnőtt. Vagy nagycsoportos tartalékváltozat fut, vagy a peula csak második felnőttel tartható. A D26 szabályát (résztvevő nem vezet félcsoportot) nem érinti. | emberi-döntés (a peula tartalomfelelőse / projektgazda) |
| (régi, UE8-ERT megfigyelés) | KAPU P1-es pool-item | Az A (✅) opció jóval hosszabb a többinél, súghat. Nem a javítás hozta be. | objektív, külön kör |
| (régi, UE8-ERT megfigyelés) | hub:211 | A korosztály-jellemzők listája előtt nincs „pl.”, a kapucellában van. Nem a javítás hozta be. | objektív, külön kör |
| (régi, UE7-NYELV megfigyelés) | M6.A:180, M6.B:523, :565 | „kinek jelzel / kihez fordulsz …: a kijelölt Memunának”: a válasz csak a „kinek”-hez illik. A kánoni (HUM-SAFE-01) mondat, csak mindhárom helyen együtt javítható. | objektív, külön kör |

**Ellenőrzések a 2. kör végén:** a 2. kör teljes diffje visszaolvasva (az 1. kör végállapotához mérve) ·
`py_compile` OK · `content_integrity.py` 0 ERROR · `--pin-visible` egyszer, 5 fájl (hub, kapu, M6.4, M6.A, M6.B) ·
`build` ×2 bájtra azonos (415 asset, 903 deliverable, 123 forrásblokk) · `check` OK · `validate` OK · `reconcile`
747/747, 0 nem egyeztetett · `lint --high-only` 0 · `unittest tools.test_media_manifest` 150 OK · `git diff --check`
és a PR-tartományé tiszta · VO/hash: lásd fent.

## Vétólista

Minden answer key-, rubrika-, completion-, gyermekvédelmi és adatvédelmi megfogalmazás-változás a fenti táblázat
„vétólista” jelölésű sora: K03, K04, K05, K11, K19, K26, K27, H06, F01, A17, B01, B15, C06, C07, C12, D36, D37, D39,
E07, E15, G22, G24. Csak írásjel vagy helyesírás egy ✅-opcióban: K13, A12, C03. Completion-megfogalmazás: K01, K02,
H09. A ✅ helye egyik lépésben sem mozdult; küszöb, időtartam és kapu-logika nem változott.

2. kör: adatkör R01 (nincs Workshop, nincs új adatfolyam); biztonsági szűrő R02; kiskorú szerephatár R05, R11 (a
második félcsoportot felnőtt vezeti, résztvevő nem); rubrika R15–R19, R21; írásjel egy ✅-opcióban R20; gyermekvédelem
R24, R25. A ✅ helye, a küszöbök, az időtartamok és a kapu-logika a 2. körben sem változtak.
