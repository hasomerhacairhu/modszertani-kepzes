# course-fix napló — BSPEC-02 leltár (2026-10-04)

> **Audit trail, nem kánon.** A `/course-fix` lépésenkénti naplója. Bemenet: `2026-10-04 BSPEC-02 leltár – egyesített
> mezőleltár, 1–20. scope.md` (és az általa hivatkozott `… validált mezőleltár, 1–7. scope.md` F-tételei). Döntési
> forrás: D-1…D-6 és H-6 (`2026-10-04 Projektgazdai döntések – BSPEC-02 leltár D-1…D-3.md`), BS-D1…D6, BS-D8, HUM-PRIV-01.
> Bázis: `ed82dbb`, munkaág `fix/moodle-build-hardening`. A felhasználó utasítása: csak a BSPEC-02-höz tartozó validált
> findingok; a BSPEC-02-n kívüli tételek (H-1…H-5, F-M0.4-6, F-M0.4-7, F-M3.4-4 produktum-fele, F-M3.4-6, F-M5.4-2,
> F-M5.4-3) kihagyva. Rövidítések: MAN, RA, PT, HUM, RR (mint a leltárban). Köztes állapot: a pinek és a média-build a
> csomag végén frissülnek, addig a média-tesztek bukhatnak.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| C-01 | D-1…D-6 átvezetése a HUM 10. szakaszba (forráshivatkozás + 6 sor) | HUM | alkalmazva | két Edit: bevezető forrásmondat, sorok a BS-D8 után |
| C-02 | új sor: LMS-M1-07 (F-M1.3-1) | MAN | alkalmazva | a C-04-gyel egy Editben (közös horgony) |
| C-03 | LMS-M1-03 completion + megjegyzés (F-M1.3-1, D-1) | MAN | alkalmazva | |
| C-04 | LMS-M1-04 unlock → LMS-M1-07 | MAN | alkalmazva | |
| C-05 | új sor: LMS-M2-08 (F-M2.2-1) | MAN | alkalmazva | a C-06-tal egy Editben |
| C-06 | LMS-M2-02 completion | MAN | alkalmazva | |
| C-07 | új sor: LMS-M2-09 (F-M2.4-1; N-4 nyitottként jelölve) | MAN | alkalmazva | a C-08-cal egy Editben |
| C-08 | LMS-M2-03 completion + megjegyzés (F-M2.4-1, -5) | MAN | alkalmazva | |
| C-09 | LMS-M2-04 unlock → LMS-M2-09 + megjegyzés (F-M2.3-3) | MAN | alkalmazva | |
| C-10 | LMS-M2-07 megjegyzés: BIZT-R5 nyitott (F-M2.3-5) | MAN | alkalmazva | |
| C-11 | új sor: LMS-M7-10 (F-M7.1-1) | MAN | alkalmazva | a C-13-mal egy Editben |
| C-12 | LMS-M7-01 completion | MAN | alkalmazva | |
| C-13 | LMS-M7-02 unlock → LMS-M7-10 | MAN | alkalmazva | |
| C-14 | §2 bevezető TEXT-C-felsorolás + tanuló-lokális mondat | MAN | alkalmazva | két Edit |
| C-15 | LMS-M0-01 megjegyzés (D-4) | MAN | alkalmazva | |
| C-16 | LMS-M0-02 megjegyzés (D-4) | MAN | alkalmazva | |
| C-17 | LMS-M0-03 megjegyzés (D-6) | MAN | alkalmazva | |
| C-18 | LMS-M0-04 megjegyzés (F-M0.4-4) | MAN | alkalmazva | |
| C-19 | LMS-M0-05 megjegyzés BS-D4 (F-M0.4-5) | MAN | alkalmazva | |
| C-20 | LMS-M3-03 megjegyzés (F-M3.3-2/-3) | MAN | alkalmazva | |
| C-21 | LMS-M3-04 megjegyzés (F-M3.4-2) | MAN | alkalmazva | |
| C-22 | LMS-M3-05 beküldés-gomb (F-M3.4-5) | MAN | alkalmazva | |
| C-23 | LMS-M5-02 megjegyzés (D-4) | MAN | alkalmazva | |
| C-24 | LMS-M5-04 megjegyzés (D-4) | MAN | alkalmazva | |
| C-25 | LMS-M6-01 megjegyzés (D-5) | MAN | alkalmazva | a választós completion-elemek listája nem került be (a verifier szerint nem bizonyított) |
| C-26 | LMS-M6-02 megjegyzés (D-5) | MAN | alkalmazva | |
| C-27 | LMS-M6-03 megjegyzés (D-5) | MAN | alkalmazva | |
| C-28 | LMS-M6-04 megjegyzés (D-5) | MAN | alkalmazva | |
| C-29 | LMS-M7-04 megjegyzés (D-4) | MAN | alkalmazva | |
| C-30 | LMS-M7-06 kipróbálási kötelezettségvállalás (F-M7.4-4) | MAN | alkalmazva | |
| C-31 | LMS-Z-01 megjegyzés (D-2) | MAN | alkalmazva | |
| C-32 | LMS-Z-02 megjegyzés (D-3) | MAN | alkalmazva | |
| C-33 | BSPEC-02 sor: leltár, új sorok, tanuló-lokális lista; státusz OPEN a megoldó commitig | MAN | alkalmazva | |
| C-32b | LMS-M5-01 megjegyzés (H-6) | MAN | alkalmazva | |
| C-34 | RA 6. pont (a) felsorolás + 4 sor + a 24. pontra mutató mondat | RA | alkalmazva | |
| C-35 | X-2: új 24. pont (tanuló-lokális szöveges lépések) + RT-P0-24 sor | RA | alkalmazva | két Edit |
| C-36 | RA 7: példák | RA | kihagyva: a javítás után az M0.4 és az M7.4 nem ígér rendszerbeli visszakeresést (F-M0.4-3, F-M7.4-3), így nincs mit tesztelni | |
| C-37 | RA 19: LMS-M3-05 beküldés-gomb tesztje (F-M3.4-5) | RA | alkalmazva | |
| C-38 | RA: M6.1 biztonsági keret felfedése (F-M6.1-2) | RA | alkalmazva | a 24. pont mondataként |
| C-39 | RR G2: BIZT-R5 nyilvántartás (F-M2.3-5) | RR | alkalmazva | |
| C-40 | PT §4 :222 zárójel → választós itemek (D-5) | PT | alkalmazva | |
| C-41 | PT §4 :225 M0.1-tagmondat (D-4) | PT | alkalmazva | |
| C-42 | PT §4 :238 (1) M0.1-hivatkozás (D-4) | PT | alkalmazva | |
| C-43 | PT §7 :319 M7.4 SLIDE 3 példa (D-4) | PT | alkalmazva | |
| L-01 | M1.3: :80, :888–889, :926–928, :1100–1101 – a 6. dia → LMS-M1-07; az 5. dia tanuló-lokális (F-M1.3-1, D-1) | M1.3 | alkalmazva | látható szöveg (pin a végén) |
| L-02 | M2.2: :29, Completion-sor, SLIDE 5/6 mező → LMS-M2-08, tanulói mutató, záró dia (F-M2.2-1…3) | M2.2 | alkalmazva | a kérdések és a narráció változatlan |
| L-03 | M2.3: :11 @asset (3 részlet), :15, :44, :114, :116 (F-M2.3-1, -3) | M2.3 | alkalmazva | @asset → build a végén |
| L-04 | M2.3: :896, :901, :922 → „M2.3 – Záró mondat” (LMS-M2-07) (F-M2.3-2) | M2.3 | alkalmazva | a :900, a hágsámá-mondat és a narráció változatlan |
| L-05 | M2 hub: :72 (F-M2.2-1), :183 BS-D4 (F-M2.4-6), :215–216 (F-M2.3-4), :219 (F-M2.4-7) | M2 hub | alkalmazva | |
| L-06 | M2.4: :584 szűkítése + SLIDE 5/6 Moodle-jelölés (F-M2.4-2) | M2.4 | alkalmazva | a tanulói mutató a mezőt is megnevezi (az M2.2 mintája); a háromoszlopos lista privát marad |
| L-07 | M2.4: :588 és :35 szó szerint a SLIDE 5/6 mezői mellé (F-M2.4-3) | M2.4 | alkalmazva | a L-06 SLIDE 5/6-blokkjával egy Editben; új tiltás nincs, a :691 változatlan |
| L-08 | M2.4: :590, :640, :671 alapértelmezett hely + :511/:549 asset-megjegyzés (F-M2.4-4) | M2.4 | alkalmazva | @asset → build a végén; a :657–659 biztonsági blokk és a :661 változatlan |
| L-09 | M2.4: :53 mezőspecifikus runtime-mondat (X-1) | M2.4 | alkalmazva | az M2.2:29 mintája; tárolt mezők → LMS-M2-09 |
| L-10 | M3.3: :44 első mondata tanuló-lokálisra; a „ne ebbe a mezőbe” kiesik (nincs mező) (F-M3.3-1) | M3.3 | alkalmazva | a Memuna-jelzés és a „Segítség és kapcsolatok” szó szerint; Memuna-QA (G1) |
| L-11 | M3.3: :807 🔒 doboz – az olvasó továbblépésére épülő mondat és az arra mutató „Ez nem büntetés…” kiesik; :810 fejlesztői feltétel a tanuló-lokális útra (F-M3.3-1) | M3.3 | alkalmazva | 112, 116-111 és a :808 doboz (116-111/000/123) szó szerint; „nem tároljuk” nincs; Memuna-QA (G1) |
| L-12 | M3.3: :795 beviteli elem nélkül; „Beállítás:” sor; :708 „(opcionális)”; Completion-sor (F-M3.3-2, -3) | M3.3 | alkalmazva | „1–3”, „1–2” változatlan; a completion definíciója (:17, hub :254) változatlan |
| L-13 | M3.3: a :44 tiltó mondata szó szerint a SLIDE 6 promptja után (F-M3.3-4) | M3.3 | alkalmazva | a „ne ebbe a mezőbe” az L-10 szerint itt sincs |
| L-14 | M3.4: :602 🔒 doboz – az olvasóra épülő mondat és az arra mutató „Ez nem büntetés…” kiesik; :604 a tanuló-lokális útra (F-M3.4-1) | M3.4 | alkalmazva | „keresd meg személyesen a Memunát” szó szerint; a :59 (112, „Segítség és kapcsolatok”) változatlan; Memuna-QA (G1); vétólista |
| L-15 | M3.4: Completion-sor (SLIDE 4 besoroló; SLIDE 5 tanuló-lokális) (F-M3.4-2) | M3.4 | alkalmazva | „legalább 3-3 pont” marad; „opcionális” nem került be |
| L-16 | M3.4: EGY-06 cím/subtype/spec/technical/a11y/notes, IKO-02 notes, :582 (F-M3.4-3) | M3.4 | alkalmazva | az M2.3-EGY-01 (`ui-text`, beviteli elem nélkül) mintája; ETA nem került be útként; @asset → build a végén |
| L-17 | M3.4: :63 és :601 – a lista tanuló-lokális; a :30 Label-spec 🔒-összefoglalója (F-M3.4-4, lista-fele) | M3.4 | alkalmazva | a modulproduktum címzettjei (produktum-fele) változatlanok: hatókörön kívül (learner release) |
| L-18 | M5.1: :24 mezőspecifikus runtime-mondat (X-1 → M5.1, H-6) | M5.1 | alkalmazva | a :605 prompt és a „ha szeretnél” változatlan; a SLIDE 6 just-in-time doboza (:610–616) nem része a H-6 javításának (lásd a jelentést) |
| L-19 | M5.2: SLIDE 9 just-in-time doboz → „Hova írod?” + a :623 mondat szó szerint; fejlesztői feltétel a tanuló-lokális útra; :629 a mező helye (F-M5.2-1, -2) | M5.2 | alkalmazva | a :613–619 feladat változatlan; Free Text Question / Essay kizárva; site-szintű Save state nem került elő; vétólista (tájékoztató-pontok törlése) |
| L-20 | M5.2: MUNK-01 notes; Completion-sor (F-M5.2-2) | M5.2 | alkalmazva | @asset → build a végén |
| L-21 | M5 hub :185 (M5.4 completion → LMS-M5-04 profil; leadás → 2. pont); M5.4 MUNK-01 purpose „leadást” (F-M5.4-1) | M5 hub, M5.4 | alkalmazva | a 2. pont küszöbe, a :189 és a MAN §4 változatlan; @asset → build |
| L-22 | M5.4: :41 „Mit gyűjtünk”, :44 „Ki látja”, :189, :202, :230, Completion-sor (F-M5.4-5) | M5.4 | alkalmazva | „3–4 helyzet”, „legalább 3 sor”, :200 és :41 „Ne írj bele…” szó szerint; „opcionális” nem került be |
| L-23 | M6.1: :46 mezőspecifikus (SLIDE 5, 7, 8 tanuló-lokális); :924, :1228, :1455 „Írd le magadnak … nem adod be” (F-M6.1-1, F-M6-X) | M6.1 | alkalmazva | a kérdések és a számok változatlanok; „opcionális” nem került be; a VO-forrás változatlan |
| L-24 | M6.1: EGY-05, EGY-08, EGY-11 title/spec/technical/a11y/notes – „H5P natív” ki (F-M6.1-1) | M6.1 | alkalmazva | @asset → build a végén |
| L-25 | M6.1: :1230 Biztonsági keret – a tanuló saját lépésére, választól függetlenül; EGY-08 spec/notes (F-M6.1-2) | M6.1 | alkalmazva | a :1231–1235 szöveg és sorrend változatlan; RA 24. pont (C-38) |
| L-26 | M6.1: :1399 „Ha elakadsz a beadásnál” → a :40 megfogalmazása (F-M6.1-3) | M6.1 | alkalmazva | a csatorna- és kontaktutalás szó szerint |
| L-27 | M6.1: Completion-sor (F-M6.1-4, F-M6-X) | M6.1 | alkalmazva | a választós elemek ID-listája nem került be (C-25 szerint nem bizonyított); hub :224 változatlan |
| L-28 | M6.2: :46 mezőspecifikus (SLIDE 7 K1–K2, SLIDE 8 tanuló-lokális); :1002 jegyzet; Completion-sor (F-M6.2-1, F-M6-X) | M6.2 | alkalmazva | a :998–1000, :778 és a VO változatlan |
| L-29 | M6.2: :903 második mondata (hozzáférés a mezőhöz) → „magadnak írod le … nem adod be” (F-M6.2-2) | M6.2 | alkalmazva | az első mondat szó szerint; vétólista |
| L-30 | M6.3: :48 mezőspecifikus; :1048 a :48-ra mutat; :1070 „3 nyitott kérdés”, beviteli elem nélkül; Completion-sor (F-M6.3-1, -2, F-M6-X) | M6.3 | alkalmazva | „CP-n belüli mező nem feltételezhető” marad; új kötelező/opcionális címke nem került be; @asset (:1048) → build |
| L-31 | M6.3: :38 „kell” – tanuló-lokális jelölés a bevezetőben; :1191–1196 (F-M6.3-1/-2) | M6.3 | alkalmazva (a :38 után egy jelölő sor); a :1191–1196: kihagyva | a D-5 RBLL-ágán a „kell” és a lezáró szöveg helyes (kötelező tanulási lépés marad), ezért szöveges csere nem kellett; az F-M6.3-3 (tárolt ág) tárgytalan |
| L-32 | M6.4: :105 második fele mezőspecifikus (mini-reflexió rögzítés nélküli; záró vázlat tanuló-lokális) (F-M6.4-1, -2) | M6.4 | alkalmazva | Free Text Question csomópont nem került elő; az RA 2 változatlan |
| L-33 | M6.4: :997 „nyitott mező” → tanuló-lokális lépés; :1022 második mondata; Completion-sor (F-M6.4-2, F-M6-X) | M6.4 | alkalmazva | a :1017 doboz, „4–6 mondat”, a négy kérdés változatlan; DPO-QA; vétólista |
| L-34 | M7.1: :540 második tagmondata az M4.4:26/:664 mintájára (F-M7.1-1) | M7.1 | alkalmazva | „Nincs automatikus pontszám, csak completion”, a mentori „csak ha szükséges” és a :541 változatlan |
| L-35 | M7.1: :8, :45, :518, :520 eszköz- és mezőleírás → LMS-M7-10; „Írd le az „M7.1 – Saját SMART cél” szövegmezőbe:”; M7 hub :183 (F-M7.1-2) | M7.1, M7 hub | alkalmazva | a :524–537 feladatszöveg és terjedelme változatlan; pin |
| L-36 | M7.1: SLIDE 4 (:333) – a (d) Fill in the Blanks az alapút, a (b) csak igazolt működés után (F-M7.1-3) | M7.1 | alkalmazva | az elfogadási elv, a feladatszövegek, a :340/:347 megoldássorok és a visszajelzések változatlanok |
| L-37 | M7.4: Completion-sor (SLIDE 1–5 választós elemei); :536 „rögzíti” → „a 14. pontja teszteli” (F-M7.4-1) | M7.4 | alkalmazva | answer key és opciók változatlanok |
| L-38 | M7.4: :429, :431, :833 tanuló-lokális lépés; tanulói jelölés a SLIDE 3-on; „Szövegmező 1/2” → „Szöveges lépés 1/2” (F-M7.4-2) | M7.4 | alkalmazva | a :439–441 adatminimalizálás szó szerint; a kérdések és a terjedelem változatlan; a :13 és a :820 eszköz-metája nem említ szövegmezőt: nincs teendő |
| L-39 | M7.4: :682 mentési utasítás (F-M7.4-3) | M7.4 | alkalmazva | a :683–686 és a v1 minimum változatlan |
| L-40 | Z.1: :506, :523 SLIDE 6 tanuló-lokális („Írd le magadnak (jegyzet, képernyőkép). Nem adod be.”) (F-Z.1-1) | Z.1 | alkalmazva | a :519 kérdés és a VO-forrás változatlan; a :15 mikrocél és a hub :72 nem gyengült |
| L-41 | Z.1: Completion-sor (SLIDE 1 SC, SLIDE 3 MC, SLIDE 4 SCS) (F-Z.1-2) | Z.1 | alkalmazva | |
| L-42 | Z.1: :435 a két M0-mondat a saját jegyzetbe (F-Z.1-3) | Z.1 | alkalmazva | új tárolt mező nincs |
| L-43 | Z.1: :11 nem „beágyazott” szabad szöveg; :53 mezőspecifikus; IKO-01 notes (F-Z.1-4, -6) | Z.1 | alkalmazva | a :57 tájékoztató-kötelezettsége változatlan; @asset → build |
| L-44 | Z.1: :437, :447, :449, :451, :453 a D-2 szerint; Z hub :71–72 (F-Z.1-7) | Z.1, Z hub | alkalmazva | Memuna és 112 szó szerint; a :449 átfogalmazása Memuna-QA alá esik; „nem tároljuk” nincs; a :514 („kiválasztottál legalább 3 saját fénypontot”) a D-2 alatt is igaz: nincs teendő; vétólista |
| L-45 | Z.2: „minimális karakterszám (pl. 250)” és „minimális karakterszám” → nincs; a terjedelem útmutatás (F-Z.2-1) | Z.2 | alkalmazva | a „pl. 250” nem vált küszöbbé, a 6. diára nem került szám; az „Írj 5–8 mondatot” marad |
| L-46 | Z.2: „(ESSAY)” és „Beágyazott kérdés” → pedagógiai megnevezés (F-Z.2-2) | Z.2 | alkalmazva | |
| L-47 | Z.2: SLIDE 7 tanuló-lokális; Completion-sor (F-Z.2-3) | Z.2 | alkalmazva | „opcionális” nem került be |
| L-48 | Z.2: :39, :42, :44, :280, :305 a D-3 szerint (F-Z.2-4, F-Z.2-6) | Z.2 | alkalmazva | Memuna és 112 szó szerint; a passz-blokk (:307) szó szerint; Memuna-QA; vétólista |
| L-49 | Z.2: :59 mezőspecifikus; :63 hatóköre „adatot rögzítő mező” (F-Z.2-5, F-Z.2-6) | Z.2 | alkalmazva | új megőrzési szabály nincs; „nem tároljuk” tanulói állítás nem került be |
| L-50 | M0.1: :57 mezőspecifikus; SLIDE 1 tanulói mutató („Írd le magadnak (jegyzet, képernyőkép). Nem adod be.”); :406 segédszöveg → promptszöveg (F-M0.1-1) | M0.1 | alkalmazva | a :120, a :393–402 és a :410–413 változatlan; sor nem nyílt |
| L-51 | M0.1: Completion-sor (SLIDE 3–4 SC, SLIDE 5 MC; SLIDE 1, 6, 7 tanuló-lokális) (F-M0.1-2) | M0.1 | alkalmazva | a hub :168 és a MAN §4 M0-sora változatlan |
| L-52 | M0.1: :11 eszközlista; :118, :377, :404 címke (F-M0.1-3) | M0.1 | alkalmazva | H5P-típusnév nem került be |
| L-53 | M0.1: SLIDE 6 just-in-time doboz és megnyitási feltétel → „Hova írod?” + a :369 mondat szó szerint; :42; „Szövegmező, instrukció:” → „Instrukció:”; M0 hub :70 (F-M0.1-4) | M0.1, M0 hub | alkalmazva | a :369 adattakarékossági mondata, a :49 blokk, a „2–4 mondat” és a kérdés változatlan; „nem tároljuk” nincs; vétólista (tájékoztató-pontok törlése) |
| L-54 | M0.2: :60 mezőspecifikus; :11, :120, :353, :488 címke; SLIDE 1 és 4 tanulói mutató; :490 segédszöveg → promptszöveg; M0 hub :79 (F-M0.2-1) | M0.2, M0 hub | alkalmazva | a kérdésszövegek, az „1–2 mondat”, a :357, a :495–496 és a :498 változatlan; „opcionális” nem került be |
| L-55 | M0.2: Completion-sor (SLIDE 3 négy MC; SLIDE 1, 4, 6, 7 tanuló-lokális) (F-M0.2-2) | M0.2 | alkalmazva | a SLIDE 3 kulcsa, visszajelzései és a11y-specifikációja változatlan |
| L-56 | M0.2: :454 a tanuló-lokális útra; :457 – az olvasóra épülő mondat kiesik, az elv („a mentorod sem ígérheti azt neked”) és a Memuna/112-utasítás marad; :465 (F-M0.2-3) | M0.2 | alkalmazva | a :459 HUM-SAFE-03 blokk és a :461 fejlesztői feltétel szó szerint; Memuna-QA; vétólista |
| L-57 | M0.3: :11, :44, :57, :318, :342–345, :350 a D-6 (a) ága szerint; SLIDE 7 tanulói mutató; a záró szöveg az intró két irányító mondatát (:48–49) veszi át szó szerint; Completion-sor (F-M0.3-1, -2, -3) | M0.3 | alkalmazva | az opcionális státusz és a :339–340 prompt (a „parázok a kapuktól” példával) változatlan; a :356 M0.A-blokk változatlan; új eszkalációs út nincs |
| L-58 | M0.4: :59 mezőspecifikus; :11, :442, :487 címke; SLIDE 5 tanulói mutató (F-M0.4-2) | M0.4 | alkalmazva | |
| L-59 | M0.4: :495 első mondata tanuló-lokális jelölésre + mentési utasítás (F-M0.4-1, -3) | M0.4 | alkalmazva | a :496 és a :497 szó szerint; „5–10 mondat” változatlan |
| L-60 | M0.4: :509, :540 a saját jegyzetre mutat (F-M0.4-3) | M0.4 | alkalmazva | az RA 7 példalistája: lásd C-36 (kihagyva) |
| L-61 | M0.4: Completion-sor (F-M0.4-4) | M0.4 | alkalmazva | „kötelező” nem cserélődött |
| L-62 | M0.4: :561 fórumleírás terjedelme a hub :135 szerint (F-M0.4-5) | M0.4 | alkalmazva | automatikus validáció nem került be; a :561 láthatósági része (F-M0.4-6) hatókörön kívül, változatlan |

## Célzott újraellenőrzés (diff-hunkok) és utójavítások

| ID | reviewer | finding | állapot | megjegyzés |
|---|---|---|---|---|
| R-01 | assessment (ERT-1, P2) | M1.3 :1100 – az 5. dia „kötelező” státusza kiesett az összefoglalóból (saját regresszió) | alkalmazva | „kötelező, de tanuló-lokális gyakorlás”; nem completion-feltétel, sor nincs, a :801 változatlan |
| R-02 | assessment (ERT-2, P2) | RA 24 – az LMS-M2-04 (M2.3 mini-reflexiói) hiányzott a listából | alkalmazva | a 10. pont változatlan |
| R-03 | safety (BIZT-1, P1) | M5.1 SLIDE 6 – a just-in-time doboz és a 90 napos fejlesztői sor tárolást sugallt egy H-6 szerint tanuló-lokális lépésnél; a :24 feltételes beviteli elemet engedett | alkalmazva | az M5.2 SLIDE 9 mintája: „Hova írod?” + a „Mit írsz le?” sor szó szerint; a :24 a többi leckéhez igazítva (beviteli elem nélkül); a :605 prompt és a „ha szeretnél” változatlan; „nem tároljuk” nincs; DPO-QA; vétólista |
| R-04 | safety (BIZT-3, P2) | M0.2 :457 – az „Egy fontos kivétel” felvezetés a „nálad marad” után olvasót sugallt | alkalmazva | „Ha veszélyről van szó:” keret (a Z.2 mintája); az elv-mondat, a Memuna- és a 112-utasítás szó szerint; a :459 HUM-SAFE-03 blokk változatlan; Memuna-QA |
| R-05 | safety (lencsén kívüli észrevétel) | M2 hub :183 – az „és javítást kérhet” tagmondat nem szerepelt az F-M2.4-6-ban, és a BS-D4 sem mondja ki (saját kitalált kiegészítés) | alkalmazva | törölve; a többi változatlan |
| R-06 | safety (BIZT-2, P1, részben) | az N-1 és az N-3 nyitott kérdés csak az audit-mappában élt | alkalmazva (csak a csomag új soraiban: LMS-M1-07 ← N-1, LMS-M2-09 ← N-3) | a kérdés nincs megválaszolva; az N-5…N-9 meglévő, a BSPEC-02-n kívüli sorokra vonatkozik → jelentés |
| R-07 | safety (BIZT-4) | RT-P0-24 visszaolvasás | bizonyíték-kapu | nem javítható; G3b |
| R-08 | implementation (IMPL-1, P1) | M1.3 5. dia: a dia törzse még 3 mezőt és üres mezőre reagáló H5P-visszajelzést írt elő (CP-ben nem építhető, D-1 szerint tanuló-lokális) | alkalmazva | :58, :799 beviteli elem nélkül + tanulói mutató; a két visszajelző mondat szó szerint, statikus szövegként („Ha megvan:” kötőszóval); :925 csak a 6. dia mezőire; a VO-forrás („próbáld meg beírni”) és a „Kötelező sablon” változatlan |
| R-09 | implementation (IMPL-2, P1) | M5.1 SLIDE 6 doboz | már alkalmazva | lásd R-03 |
| R-10 | implementation (IMPL-3, P2) | LMS-M0-05: „M0 hub §6” → §5 (a Kapuk szakasz) | alkalmazva | |
| R-11 | implementation (IMPL-4, P2) | M2.4 :676 „(vagy egy nagy közös mező…)” ellentmondott az LMS-M2-09 öt „Required” kérdésének | alkalmazva | a kérdésszám és a beállítás változatlan |
| R-12 | implementation (IMPL-5, P2) | a D-4 hivatkozás a döntés által nem fedett diákra is (M0.1 SLIDE 1/7, M0.2 SLIDE 1/4/7, M0.4 SLIDE 5/6) | alkalmazva | „BSPEC-02 leltár; a SLIDE 6-nál D-4” (M0.1, M0.2, M0 hub, LMS-M0-01/02); M0.4: „BSPEC-02 leltár”; a besorolás nem változott |
| R-13 | implementation (IMPL-6, P2) | M6.1 biztonsági keret: megvalósítási mód nem volt megadva; fejlesztői metaszöveg a tanulói címben | alkalmazva | statikus szöveg a kérdés alatt vagy a következő dián (az eredeti IMPL-2 javaslata); a meta fejlesztői megjegyzésbe került; RA 24 csak ellenőriz; a keret négy pontja szó szerint |
| R-14 | implementation (IMPL-7, P2) | M2.3 :11 és Z.1 IKO-01 „review” mezőállítás tanuló-lokális lépésre | alkalmazva | @asset → újra build |
| R-15 | hungarian (NYELV-1) | „Írd le magadnak (jegyzet, képernyőkép)” – rossz szókapcsolat | alkalmazva (M0.1 :124, M0.3 :344, Z.1 :525, M1.3 :799) | az M0.1 :410–411 (F-M0.1-1 korlátja szerint változatlan) és a Z.1 :437 (meglévő, az M0-mondatok mentésére utal) nem változott |
| R-16 | hungarian (NYELV-2) | a tanulói mutató a fejlesztői típusjelölő zárójelében állt | alkalmazva (M0.2, M6.1 ×3, M6.2, Z.1) | külön `>` sorba került; a zárójeles típusjelölő és a számok változatlanok |
| R-17 | hungarian (NYELV-3) | névmási zuhanás | alkalmazva (M0.3 M0.A-doboz „a fenti technikai segítségkérési csatornán”, Z.2 :282 „A reflexiódat”, Z.2 :337 „(3–5 szó bőven elfér)” törölve) | az M0.2 :359 („ne írj ide”) a F-M0.2-1 korlátja (:357 változatlan) miatt maradt, a :454 vele párban szintén; jelentés |
| R-18 | hungarian (NYELV-4) | M3.3 :45, :808 „amennyit szívesen megosztasz” → „amennyi jólesik” | alkalmazva | a két mondat egyezése megmaradt; a 🔒-doboz többi része változatlan; Memuna-QA; vétólista |
| R-19 | hungarian (NYELV-5) | M0.3 – az emoji a kettőspont és a lista közé került | alkalmazva | |
| R-20 | hungarian (NYELV-6, -7) | M1.3 :80 vonzat és tartalom; :886 beágyazott idézőjel | alkalmazva | a beküldési feltétel változatlan |
| R-21 | hungarian (NYELV-8) | fejlesztői azonosító a tanulói szövegben (M2.2 :705, M5.4 :42, M5.2 :624, M3.4 :64) | alkalmazva | |
| R-22 | hungarian (NYELV-9, -10) | M2.3 :896 – a „lecke ezzel teljesül” a sablon után; :11 spec mondatsorrend | alkalmazva | a szöveg nem változott, csak a sorrend; @asset → build |
| R-23 | hungarian (NYELV-11) | egyeztetés a fejlesztői sablonmondatokban (M6.1, M6.2 :47; M0.1, M0.2, Z.1 :11) | alkalmazva | |
| R-24 | hungarian (NYELV-12) | M7.4 Completion-sor: a fókuszválasztás tagmondatából hiányzott az állítmány | alkalmazva, nyitott jelöléssel | a completion-szerepet nem találtam ki: „nyitott: a megvalósítását az RA 14. pontja teszteli” → jelentés (emberi/értékelési döntés) |
| R-25 | hungarian (NYELV-13) | Z.1, Z.2 „(ugyanúgy, mint az M3.3-ban)” → „(a szabály ugyanaz, mint az M3.3-ban)” | alkalmazva | Memuna-QA |
| R-26 | hungarian (NYELV-14) | egy fogalom, egy név: „kísérő activity” → „szövegmező” (M7 hub :183, M7.1 :8, :45); tanulói mutató hellyel (M7.1 :526); „mezőbe” → „szövegmezőbe” (M2.2 :705, M2.3 :896) | alkalmazva | a manifest §2 kánoni „kísérő activity” megnevezése változatlan |

## Nyilvántartás

| ID | lépés | állapot | megjegyzés |
|---|---|---|---|
| P-01 | BSPEC-02 → `BUILD_SPEC_RESOLVED`, megoldó commit `5b61e25` (tartalom, napló, pinek), média-build `0d40424` | alkalmazva (külön, csak nyilvántartási commitban) | valós SHA, nem kitalált; a nyitott kérdések learner-release tételek és bizonyíték-kapuk |
