# BSPEC-02 leltár — egyesített mezőleltár, 1–20. scope (2026-10-04)

> **Audit trail, nem kánon.** A BSPEC-02 maradék szabadszöveg-leltára mind a 20 scope-ra, a projektgazda D-1…D-3
> döntésével (`2026-10-04 Projektgazdai döntések – BSPEC-02 leltár D-1…D-3.md`) alkalmazva. Az 1–7. scope részletes
> mezőtáblája, findingjai és indoklása: `2026-10-04 BSPEC-02 leltár – validált mezőleltár, 1–7. scope.md` (ez a fájl
> azt a D-1…D-3 szerint felülírja, a többit hivatkozza). Brief: `2026-10-04 BSPEC-02 leltár – projektgazdai utasítás és
> review-brief.md`. Bázis: `ed82dbb`, munkaág `fix/moodle-build-hardening`; tananyagot ez a kör nem módosított.
> Rövidítések: MAN, RA, ADV, PT, HUM, RR, A11Y (mint az 1–7. fájlban); RBLL = `REQUIRED_BUT_LEARNER_LOCAL`, OLL =
> `OPTIONAL_LEARNER_LOCAL`, ROW-MISSING = `REQUIRED_STORED_MANIFEST_ROW_MISSING`, COVERED =
> `REQUIRED_STORED_ALREADY_COVERED`, NAFT = `NOT_ACTUALLY_FREE_TEXT`, HDR = `HUMAN_DECISION_REQUIRED`.

## 0. Futás és lefedettség

- **20/20 scope**, mind a felhasználó által indított `/course-review` futás (1–7: első kör; 8–20: második kör, a
  D-1…D-3 rögzítése után, a briefbe felvett döntésekkel). Lencsék: implementáció + biztonság-jog; M2.3, M7.1, Z.1, Z.2,
  M7.4-nél értékelés is.
- **Eljárás:** az orchestrator-fork mind a 20 futásnál a lencse-reviewerek indítása után, a verifier előtt visszatért.
  A SKILL.md 5–6. lépését a fő session futtatta: scope-onként **egyetlen** verifier az összes findinggal, közös
  kontextusfájllal (a „Lezárt döntések” szabály, „git-history nincs”, D-1…D-3 kezelése). Az M0.1 orchestrátora a
  várakozást a repón kívüli, eredménytelen read-only Grep/Glob keresésekkel töltötte (saját riportja szerint); a
  további 12 futás argumentumához ezért a fő session egy mondatot fűzött („ne várakozz, semmilyen keresést ne futtass
  várakozásként”). Az M5.2 implementációs reviewere tévesen worktree-izolációval indult; a futás után a `git worktree
  list` csak a fő munkafát mutatta.
- **Részleges eredmények, folytatással teljessé téve:** M1.3 implementáció, Z.1 biztonság-jog, M3.4 implementáció,
  M5.2 implementáció (lencsék), M3.4 verifier. **Hiányos lencse nincs.**
- **Számok (findingonkénti verdiktsorokból):** 20 scope, 43 lencse-riport, 20 verifier, 236 finding. MEGERŐSÍTVE 157
  (ebből 26 bizonyíték-kapu), ELVETVE 28, EMBERI DÖNTÉS 51 (duplikátumokkal; deduplikálva lent).
- **Lefedettségi rés (nem a 20 scope része):** az M5.1:605 („Írj le 1 mondatot (ha szeretnél):”) mezőt a BSPEC-02
  nyilvántartás nem sorolta fel. A saját szövege szerint opcionális, ezért BSPEC-02-sor nem kell hozzá (MAN:35 csak a
  kötelező mezőkről szól), de az M5.1:24 runtime-sablonja („… a mező Moodle-oldalra kerül”) név szerinti tárolásba
  terelné (X-1). Lásd 5. szakasz.

## 1. A D-1…D-3 alkalmazása

- **D-1:** M1.3 5. dia (vezetett S/B/I) → RBLL; nincs külön sor, nem completion-feltétel. Az LMS-M1-07 három
  „Required” kérdése az S, a B és az I (6. dia). Javítandó: M1.3:801 („Kötelező sablon”), :1100 („1 kötelező, 1
  opcionális mondat”), a :926–928 hatóköre és az 5. dia tárolást/completiont sugalló megjegyzései.
- **D-2:** Z.1 SLIDE 5 → RBLL; nincs TEXT-C. Javítandó: Z.1:447, :449 (Memuna-QA alatt; :451 feltétele szerint),
  :451, :453 (karakterminimum), :53, :11, :514; Z hub :71–72.
- **D-3:** Z.2 SLIDE 5, 6, 7 → RBLL; nincs TEXT-C. Javítandó: Z.2:39, :42, :44, :59, :63, :248, :276, :280, :284,
  :305, :311 (a passz-blokk és a Memuna/112 szó szerint marad).
- **Tárgytalanná vált:** D-2b (Z.1 karakterminimum) és D-3b (Z.2 passz a tárolt ágon).

## 2. Egyesített mezőleltár — csak a besorolás és a teendő

Az 1–7. scope mezőinek részletei (köt./opc., tárolt, completion, privacy, bizonyíték) az 1–7. fájl 1. szakaszában; itt
a D-1…D-3 utáni végső besorolás áll. A 8–20. scope sorai a verifierek végső besorolásai.

| Scope | Mező (fájl:sor) | Végső besorolás | Teendő |
|---|---|---|---|
| M1.3 | 5. dia S/B/I (:797–805, :1100) | RBLL (D-1) | F-M1.3-2 |
| M1.3 | 6. dia saját mini-SBI (:887–895) | ROW-MISSING | új sor LMS-M1-07 (F-M1.3-1) |
| M1.3 | :888, :1030–1037, :1061 | NAFT | — |
| M2.2 | SLIDE 5 (:468–495), SLIDE 6 (:499–525) | ROW-MISSING | új sor LMS-M2-08 (F-M2.2-1…3) |
| M2.2 | kapu-utalás (:16, :699) | COVERED (LMS-M2-05) | — |
| M2.2 | választós elemek, :706 | NAFT | — |
| M2.3 | záró mondat (:896–901) | COVERED (LMS-M2-07) | F-M2.3-1, -2, -5; N-2 |
| M2.3 | MR1–MR9 mini-reflexiók | OLL | F-M2.3-3, -4 |
| M2.3 | hook, CHECK | NAFT | — |
| M2.4 | háromoszlopos lista (:574–582) | RBLL | — |
| M2.4 | szabálymondat, esetválasz, 3 határszabály (:584–691) | ROW-MISSING | új sor LMS-M2-09 (F-M2.4-1…7) |
| M2.4 | önjelző pollok, keretszövegek | NAFT | F-M2.4-5 |
| M7.1 | SLIDE 7 peula + SMART cél (:511–541) | ROW-MISSING | új sor LMS-M7-10 (F-M7.1-1…3) |
| M7.1 | AI-prompt (:412–428) | HDR, nem BSPEC-02-blokkoló | N-5 |
| M7.1 | :422 saját jegyzet / v2 AI-sor | OLL / COVERED (LMS-M7-06) | — |
| Z.1 | SLIDE 5 fénypont-esszé (:437–453) | RBLL (D-2) | F-Z.1-7 |
| Z.1 | SLIDE 6 záró mondat (:517–523) | RBLL | F-Z.1-1, -2 |
| Z.1 | :435 M0-mondatok | OLL | F-Z.1-3 |
| Z.2 | SLIDE 5, 6 (:274–311) | RBLL (D-3) | F-Z.2-6 |
| Z.2 | SLIDE 7 három szó (:333–335) | RBLL | F-Z.2-3 |
| M0.1 | SLIDE 1 egy szó (:118–122) | RBLL | F-M0.1-1 |
| M0.1 | SLIDE 6 „Írj le 2–4 mondatot” (:351–381) | RBLL (D-4) | F-M0.1-4 |
| M0.1 | SLIDE 7 „1 mondat magadnak” (:385–411) | RBLL | F-M0.1-1 |
| M0.1 | meta, doboz, választós elemek | NAFT | F-M0.1-2, -3 |
| M0.2 | SLIDE 1, 4, 7 (:120–125, :353–357, :469–496) | RBLL | F-M0.2-1 |
| M0.2 | SLIDE 6 határ-reflexió (:435–465) | RBLL (D-4) | F-M0.2-3 |
| M0.2 | meta, SLIDE 2–3 választós elemek | NAFT | F-M0.2-2 |
| M0.3 | SLIDE 7 segítségkérés (:337–345) | OLL (D-6) | F-M0.3-1, -3 |
| M0.3 | utalások, választós elemek | NAFT | F-M0.3-1, -2 |
| M0.4 | SLIDE 5 saját online szabály (:440, :454–460) | RBLL | F-M0.4-1…4 |
| M0.4 | SLIDE 6 fórumvázlat (:466–497) | RBLL | F-M0.4-1…3 |
| M0.4 | bemutatkozó poszt + válasz (:518–566) | COVERED (LMS-M0-05) | F-M0.4-5…7; N-6…8 |
| M0.4 | választós elemek, pipák, meta | NAFT | — |
| M3.3 | SLIDE 6 reflexió (:795–805) | OLL | F-M3.3-1…4 |
| M3.3 | keretszövegek, választós elemek, Branching | NAFT | — |
| M3.4 | SLIDE 5 DO/DON'T lista (:584–604) | RBLL | F-M3.4-1…3 |
| M3.4 | korai vázlat (:785) | `OPTIONAL_STORED` (az LMS-M3-05 piszkozata) | F-M3.4-5 |
| M3.4 | modulproduktum (:789–803) | COVERED (LMS-M3-05) | F-M3.4-4…6; N-9 |
| M3.4 | választós elemek, keretszövegek | NAFT | — |
| M5.2 | SLIDE 9 mondatbefejezés (:609–629) | RBLL (D-4) | F-M5.2-1, -2 |
| M5.2 | M5.2-MUNK-01 munkalap; :638 tipp | OLL | — |
| M5.2 | választós elemek, SLIDE 1, intro | NAFT | F-M5.2-1 |
| M5.4 | SLIDE 4 és SLIDE 5 vázlatmező (:189–232) | RBLL (D-4) | F-M5.4-5 |
| M5.4 | táblázat Assignment + M5.4-MUNK-01 fájlút | COVERED (LMS-M5-05) | F-M5.4-1…4 |
| M5.4 | hub :185, választós elemek, keretszövegek | NAFT | — |
| M6.1 | SLIDE 5 Interakció 2, SLIDE 7 Szitu 2 (:916–924, :1222–1228) | RBLL (D-5) | F-M6.1-1, -4; F-M6-X |
| M6.1 | SLIDE 8 mini-reflexió (:1447–1455) | RBLL | F-M6.1-1 |
| M6.1 | választós elemek, keretszövegek | NAFT | F-M6.1-2…4 |
| M6.2 | SLIDE 7 K1–K2 (:905–913) | RBLL (D-5) | F-M6.2-2; F-M6-X |
| M6.2 | SLIDE 8 mini-reflexió (:998–1002) | RBLL | F-M6.2-1 |
| M6.2 | választós elemek, keretszövegek | NAFT | F-M6.2-2 |
| M6.3 | SLIDE 3–5 „Kérdés 2” (3 mező), SLIDE 6 K1–K3 | RBLL (D-5) | F-M6.3-1, -2; F-M6-X |
| M6.3 | SLIDE 7 mini-reflexió (:1179–1185) | OLL | F-M6.3-1 |
| M6.3 | keretszövegek, választós elemek | NAFT | F-M6.3-2, -3 |
| M6.4 | 12 ág-specifikus mini-reflexió | OLL | F-M6.4-1 |
| M6.4 | záró saját kvuca-vázlat (:992–1030) | RBLL (D-5) | F-M6.4-2; F-M6-X |
| M6.4 | Check, választógombok, keretszövegek | NAFT | — |
| M7.4 | SLIDE 3 kvuca-meta + SMART cél (:456–481) | RBLL (D-4) | F-M7.4-2, -3 |
| M7.4 | :80 saját jegyzet / v2 AI-sor | OLL / COVERED (LMS-M7-06) | — |
| M7.4 | AI-prompt (:547–555) | HDR, nem BSPEC-02-blokkoló | N-5 (kiterjesztve az LMS-M7-04-re) |
| M7.4 | v1 1–4. pont (:754–764) | COVERED (LMS-M7-05) | — |
| M7.4 | kipróbálás a v1-ben / a v2 mellett (:777–785) | `OPTIONAL_STORED` (LMS-M7-05) / COVERED (LMS-M7-06) | F-M7.4-4 |
| M7.4 | választós elemek, SLIDE 2/6 utalások | NAFT | F-M7.4-1…3 |

**Új TEXT-C sorok (döntéstől függetlenül):** LMS-M1-07 (M1.3, 3 kérdés), LMS-M2-08 (M2.2, 2), LMS-M2-09 (M2.4, 5),
LMS-M7-10 (M7.1, 2) — részletek az 1–7. fájl 2.1 szakaszában. A D-4…D-6 „tárolt” ágai további sorokat hoznának.

## 3. A leltár utolsó BSPEC-02 emberi döntései — LEZÁRVA (D-4…D-6, 2026-10-04)

> **Lezárva.** A projektgazda mindhárom kérdésben a tanuló-lokális ágat választotta, és a H-6-ot az X-1 kiterjesztésével
> rendezte (szó szerint: `2026-10-04 Projektgazdai döntések – BSPEC-02 leltár D-1…D-3.md`, „D-4…D-6 és a H-6
> kezelése”). Az alábbi szöveg a döntés előtti kérdésfelvetés, nyilvántartásként.

Mind ugyanabba az osztályba esik: kötelező tanulási lépés egy H5P-leckében, a lecke szövege részben tárolást
feltételez (just-in-time doboz, „Moodle-oldalra kerül” sablon, „ki fér hozzá”), a kánon a tárolást feltételezi, de nem
dönti el, és az adatvédelmi alapértelmezés (ADV:29, :112) a tanuló-lokális út felé mutat. A D-1…D-3 indoklása a
verifierek szerint csak mérlegelési szempont, mert új alkalmazási esetek. Gazda mindháromnál: projektgazda; vétó/QA:
DPO/jogi felelős (HUM-PRIV-01).

- **D-4 — vázlat- és önreflexiós mezők, amelyeknek a beadandó változatát egy későbbi tárolt produktum gyűjti, vagy
  amelyekhez tárolási cél nincs:** M0.1 SLIDE 6; M0.2 SLIDE 6; M5.2 SLIDE 9 (tárolt változat: LMS-M5-05 R1–R3);
  M5.4 SLIDE 4–5 (LMS-M5-05); M7.4 SLIDE 3 két mezője (LMS-M7-05; a SMART célt az LMS-M7-10 is tárolja). Kérdés:
  RBLL (kötelező tanulási lépés, nem tárolt, nem completion-feltétel, nincs TEXT-C sor), vagy tárolt TEXT-C új sorral?
  Kánoni háttér a tárolás felé: PT:225/:238 („az M0.1 nem érzékeny reflexiós mezői”), PT:319 („pl. … M7.4 SLIDE 3”),
  MAN:35, a leckék just-in-time dobozai (M0.1:367–375, M5.2:621–627, M7.4:431) és láthatósági ígéretei (M0.2:454,
  :457; M5.4:41–44). Az RBLL-ág következménye: a PT:225/:238 M0.1-tagmondata és a PT:319 M7.4-példája igazítandó (a
  projektgazdai döntés az 1–3. forrás fölött áll). A tárolt ágon nyílnak: M0.1 tartalmi korlát (BIZT-6), M0.2 passz és
  átnézés (A1–A3), M7.4 megőrzési sor (DPO, BS-D6 mintájára).
- **D-5 — az M6 gyakorló szöveges válaszai:** M6.1 SLIDE 5 Interakció 2 és SLIDE 7 Szitu 2 (kockázat-válaszok);
  M6.2 SLIDE 7 K1–K2 (nyitott és kerülendő kérdések); M6.3 SLIDE 3–5 „Kérdés 2” és SLIDE 6 K1–K3 (mit tanít,
  variáció); M6.4 záró saját kvuca-vázlat. A tárolt, mentor által értékelt produktum mindegyiknél a játéklap
  (LMS-M6-05; R1, R4, R5). Kérdés: RBLL, vagy tárolt TEXT-C (leckénként új sor)? Kánoni háttér a tárolás felé: PT:222
  („M6.1–M6.4 Single Choice / rövid szöveges válasz kvíz-itemek … teljesítési feltételt mérnek” — a verifierek szerint
  akadálymentesítési checklist-indoklás, nem tárolási döntés), hub :224 („érdemi kitöltéssel”), MAN:35. Az RBLL-ág
  következménye: a PT:222 zárójeles felsorolása a választós itemekre szűkül, az akadálymentesítési minimum változatlan.
  A tárolt ágon nyílik: M6.3 SLIDE 6 mező melletti korlát (harmadik fél különleges adata).
- **D-6 — M0.3 SLIDE 7 segítségkérés:** (a) opcionális, tanuló-lokális lépés; a stábjelzés a tanuló saját üzenete a
  HUM-OPS-02 szerinti „Segítség és kapcsolatok” csatornán; vagy (b) tárolt, a stábnak szóló jelzés, kijelölt olvasóval
  (a programvezető jelöli ki, HUM-OPS-02)? Kánoni háttér: M0.3:318 („jelzés a stábnak”) ↔ :44 („megoszthatsz”), :350
  („oda viheted”); a hub :88 nem ismeri a mezőt; a (b) ághoz a manifestben nincs profil opcionális tárolt szövegre.

## 4. Validált objektív findingok a `/course-fix`-hez — 8–20. scope

Az 1–7. scope findingjai (F-M1.3-1 … F-Z.2-5) az 1–7. fájl 2. szakaszában; a D-1…D-3 miatt kiegészülnek: **F-M1.3-2**
(D-1: az 5. dia tárolást/completiont sugalló állításai, :801, :1100, :926–928 hatóköre), **F-Z.1-7** (D-2: Z.1:447,
:449 [Memuna-QA], :451, :453, :53, :11, :514; Z hub :71–72), **F-Z.2-6** (D-3: Z.2:39, :42, :44, :59, :63, :280, :305,
:311; a passz-blokk szó szerint marad). „Nem tároljuk” típusú tanulói állítás mindenhol csak az X-2 runtime-igazolása
után.

**Keresztmetszeti (a leckénkénti findingok közös mintája):**
- **X-1** — a „Runtime-követelmény – szabad szöveges mező(k)” sablon („ha a teszt nem igazolja, a mező Moodle-oldalra
  kerül”) leckénként mezőspecifikus legyen (F-Z.1-6 minta): tanuló-lokális mezőhöz nincs Moodle-oldali tartalékút és
  CP-be ágyazott, rögzítő beviteli elem; tárolt mezőnél a saját sorra mutat. Érintett: M0.1, M0.2, M0.3, M0.4, M2.2,
  M2.4, M6.1, M6.2, M6.3, M6.4, Z.1, Z.2 (és M5.1, lásd 5. szakasz). Globális csere nincs; tárolt mezőnél a
  tájékoztatási kötelezettség nem gyengül.
- **X-2** — RA-visszaolvasási lépés minden tanuló-lokális H5P-szövegre (F-Z.1-5 kiterjesztése): célverzión aktív-e a
  „Save state” (`enablesavestate`), keletkezik-e mentett állapot vagy próbálkozás-válasz (CP-be ágyazott
  `H5P.ExportableTextArea` mint konkrét teszteset), és a completion nem függ tőle. Érintett activityk: LMS-M0-01…04,
  LMS-M2-03, LMS-M3-03, LMS-M3-04, LMS-M5-02, LMS-M5-04, LMS-M6-01…04, LMS-M7-04, LMS-Z-01, LMS-Z-02. A beállítás
  értékét kitalálni tilos.
- **X-3** — beágyazott-kérdés címkék („Beágyazott kérdés – szabad szöveges válasz”, „(ESSAY)”) pedagógiai
  megnevezésre (A11Y §6:62–63): M0.1, M0.2, M0.3, M0.4, M3.4 (EGY-06, media build), M7.1, M7.4, Z.1, Z.2.

**Leckénként (megtartott reviewer-ID; korlát a 3. oszlopban):**

| ID | Lényeg | Javítási korlát |
|---|---|---|
| F-M0.1-1 (IMPL-2, P1) | :57 mezőspecifikus; SLIDE 1 és 7 beviteli elem nélküli, tanuló-lokális lépés („Írd le magadnak … Nem adod be.”); :406 segédszöveg promptszöveggé | :120, :393–402, :410–413 és a Z-oldali felidézések változatlanok; sor nem nyílik; pin |
| F-M0.1-2 (IMPL-3, P1) | „Completion (lecke):” sor (SLIDE 3–4 SC, SLIDE 5 MC); SLIDE 1/7 nem completion-feltétel; SLIDE 6 a D-4 után; LMS-M0-01 megjegyzése (LMS-M1-01 minta) | hub :168, MAN §4 M0-sora és a választós itemek változatlanok |
| F-M0.1-3 (IMPL-4, P2) | :11 eszközlista; :118, :404 címke; :377 és hub :70 a D-4 után | H5P-típusnév nem kitalálható |
| F-M0.2-1 (IMPL-03, P1) | :60 mezőspecifikus; SLIDE 1, 4, 7 tanuló-lokális, beviteli elem nélkül; :11, :120, :353, :488, hub :79 címkéi | kérdésszövegek, „1–2 mondat”, :357, :495–496, :498 változatlanok; „opcionális” szó nem kerül be |
| F-M0.2-2 (IMPL-04, P1) | „Completion (lecke):” sor (SLIDE 3 négy MC); LMS-M0-02 megjegyzése; BSPEC-02 sor | a SLIDE 3 kulcsa, visszajelzései, a11y-specifikációja változatlan |
| F-M0.2-3 (IMPL-02, P1) | a :454/:457 a D-4 ága szerint | Memuna- és 112-utasítás, :459 HUM-SAFE-03 blokk szó szerint; Memuna-QA |
| F-M0.3-1 (IMPL-2, P1) | :342 beágyazott címke és :57 tartalékút a D-6 ága szerint; :350 „beírtál” → RA 7 | opcionális státusz, :339–340 prompt, :352 változatlan |
| F-M0.3-2 (IMPL-3, P1) | „Completion (lecke):” sor (SLIDE 1, 3, 4, 6, 7 választós elemei); SLIDE 7 szöveg a D-6 után | interakció kötelező/opcionális státusza nem cserélhető |
| F-M0.3-3 (BIZT-2, P1) | :44, :318, :350 a D-6 ága szerint; a „parázok a kapuktól” példa tartalmi útja (PT:242, :48–:49) | új eszkalációs út nem írható |
| F-M0.4-1 (IMPL-1, P1) | :495 első mondata tanuló-lokális jelölésre | :496, :497 szó szerint; „5–10 mondat” változatlan |
| F-M0.4-2 (IMPL-2, P1) | :59 mezőspecifikus; :11, :442, :487 címkéi | tárolt mezőnél a tájékoztatás nem gyengül |
| F-M0.4-3 (IMPL-3, P1) | 6. dia mentési utasítás; :509, :540 a saját jegyzetre mutat; RA 7 példalista | Save state értéke nem kitalálható |
| F-M0.4-4 (IMPL-4, P2) | LMS-M0-04 megjegyzése és „Completion (lecke):” sor; BSPEC-02 sor | „kötelező” nem cserélhető „opcionálisra” |
| F-M0.4-5 (IMPL-5, P2) | :561 terjedelem a hub :135 szerint; LMS-M0-05 megjegyzése BS-D4 | automatikus validáció nem kerül be |
| F-M0.4-6 (BIZT-3, P1) | :497, :561 láthatóság a MAN:21/PT:230 szerint; :550 ne kvucát nevezzen közönségnek | „nem privát”, „annyit ossz meg” szó szerint; learner-release tétel |
| F-M0.4-7 (BIZT-4, P1) | §4 fórum-specifikáció és LMS-M0-05 megjegyzése hivatkozzon a just-in-time dobozra | a „meddig” az N-6-ig üres; learner-release tétel |
| F-M3.3-1 (BIZT-1, P0) | :44 első mondata, :807 olvasót feltételező tagmondata, :810 a tanuló-lokális útra | Memuna, 112, 116-111/000/123, :808 szó szerint; Memuna-QA (G1) |
| F-M3.3-2 (IMPL-2, P1) | :795: a követett LMS-M3-03-ban nincs beviteli elem; LMS-M3-03 megjegyzése; X-2 negatív eset | TEXT-C nem nyílik; a két kérdés szövege változatlan |
| F-M3.3-3 (IMPL-3, P2) | „Beállítás: opcionális szöveges válasz: nem completion-feltétel” (M3.1:686 minta); :708 „(opcionális)”; Completion-sor; BSPEC-02 | „1–3”/„1–2” változatlan; pin |
| F-M3.3-4 (BIZT-3, P2) | a :44 tiltó mondata szó szerint a SLIDE 6 elé | az F-M3.3-2-vel egyeztetve; új szabály nincs |
| F-M3.4-1 (BIZT-1, P0) | :602 olvasóra épülő tagmondata a :604 szerint; :604 a választott útra | Memuna, „Segítség és kapcsolatok”, 112 szó szerint; Memuna-QA (G1) |
| F-M3.4-2 (BIZT-3, P1) | „Completion (lecke):” sor (SLIDE 4 besoroló); SLIDE 5 RBLL; LMS-M3-04 megjegyzése; BSPEC-02 | „legalább 3-3 pont” marad; „opcionális” nem kerül be |
| F-M3.4-3 (IMPL-3, P1) | EGY-06: nincs CP-n belüli szövegmező; :582, IKO-02 :569; media build | ETA nem vehető fel útként |
| F-M3.4-4 (BIZT-2, P1) | :63/:601 szétválasztása: a lista tanuló-lokális; a modulproduktum címzettjei a MAN:62/:807 szerint | új címzett nem írható; learner-release rész |
| F-M3.4-5 (BIZT-4, P1) | LMS-M3-05: „Require students to click the submit button” = Yes + RA-teszt (Z.4:337 minta) | határidők, próbálkozásszám, rubrika változatlan |
| F-M3.4-6 (BIZT-6, P2) | RA-teszt a „kikerül a Moodle-ből” eltávolításra | szabály nem írható; BSPEC-02-n kívül |
| F-M5.2-1 (BIZT-2, P1) | SLIDE 9 mező helye; Free Text Question kizárva; X-2 az LMS-M5-02-re | TEXT-C nem nyílik; site-szintű Save state kikapcsolása nem írható elő |
| F-M5.4-1 (IMPL-3, P1) | hub :185: az M5.4 completionje az LMS-M5-04 profilja, a táblázat leadása (online szöveg vagy fájl) a 2. pont; L:273 purpose; media build | 2. pont küszöbe, hub :189, MAN §4 változatlan |
| F-M5.4-2 (IMPL-4, P1) | az Assignment „M5.B után + M3 complete” nyílik: L:31, SLIDE 7, :314, :326 | unlock és a két leadási út változatlan |
| F-M5.4-3 (IMPL-5, P2) | egy név: a MAN:78 „Név” oszlopa a lecke tanulói nevét veszi át | `build_id`, profil, completion változatlan |
| F-M5.4-4 (IMPL-1 része, P1) | a just-in-time tájékoztató az LMS-M5-05 indítópontján (PT:225) | a :41–:44 többi része a D-4 után |
| F-M6.1-1 (BIZT-2, P1) | :46 mezőspecifikus; SLIDE 8 tanuló-lokális; EGY-11 technical; :734, :1165, :1308 „H5P natív” állítás; media build; LMS-M6-01 megjegyzése | :1449–1455 és VO :1390–1393 változatlan |
| F-M6.1-2 (BIZT-3, P1) | :1230 biztonsági keret a tanuló próbálkozása után, tárolt választól függetlenül; RA-tétel | :1231–1235 szöveg és sorrend változatlan |
| F-M6.1-3 (BIZT-4, P2) | :1399 „beadás” a :40 szerint | kontaktutalások szó szerint; pin |
| F-M6.1-4 (IMPL-3, P1) | „Completion (lecke):” sor; SLIDE 5/7 a D-5 után | hub :224 nem változik |
| F-M6.2-1 (BIZT-3, P1) | :46 mezőspecifikus; SLIDE 8 tanuló-lokális; :1002 jegyzet; LMS-M6-02 megjegyzése; BSPEC-02 | :998–1000, :778, VO :921–937 változatlan |
| F-M6.2-2 (BIZT-2, P1) | :903 második mondata a D-5 ága szerint (azonos az M6.4:1022-vel; eltérő ágnál leckénként válik el) | első mondat szó szerint |
| F-M6.3-1 (BIZT-2, P1) | :48 mezőspecifikus; SLIDE 7 rögzítés nélküli; SLIDE 3–6 a D-5 után; :1048 a :48-ra mutat | „CP-n belüli mező nem feltételezhető” marad; nem kerül új kötelező/opcionális címke |
| F-M6.3-2 (IMPL-3, P1) | LMS-M6-03 megjegyzése és Completion-sor a D-5 után; PT:222 közösen, a D-5 szerint | akadálymentesítési minimum nem gyengül |
| F-M6.3-3 (IMPL-4, P2) | csak tárolt ágon: mező melletti korlát a meglévő kánonból (ADV:75, :29; MAN:52 minta) | új policy nem írható |
| F-M6.4-1 (BIZT-3, P1) | :105: a mini-reflexiók rögzítés nélküli gondolkodtató kérdések; LMS-M6-04 megjegyzése; BSPEC-02 | promptok változatlanok; Free Text Question csomópont nem írható elő; RA 2 nem gyengül |
| F-M7.4-1 (IMPL-3, P1) | „Completion (lecke):” sor (SLIDE 1–5 választós elemei); SLIDE 3 a D-4 után; :536 „rögzíti” → „az RA 14. pontja teszteli”; LMS-M7-04 megjegyzése | answer key, opciók változatlanok |
| F-M7.4-2 (IMPL-2, P1) | :429, :431, :833, :13, :820 a D-4 ága szerint | :439–441 adatminimalizálás szó szerint |
| F-M7.4-3 (IMPL-4, P2) | :682 „Használd fel, amit itt leírtál” → mentési utasítás vagy TEXT-C saját válasz (ágfüggő); RA 7 | :683–686 és v1 minimum változatlan |
| F-M7.4-4 (ERT-2, P2) | LMS-M7-06 megjegyzése: a kipróbálási kötelezettségvállalás a KAPU:259/:422 szerint (completion-szinten elvárt, nem pontozott, nem blokkol); az AI-sornál a KAPU:423 | nem lesz Moodle completion-feltétel; külön sor nem kell |

### 4.1 A D-4…D-6 szerinti döntésfüggő javítások (a döntés után objektívek)

| ID | Lényeg | Javítási korlát |
|---|---|---|
| F-M0.1-4 (D-4) | SLIDE 6 tanuló-lokális: a :367–375 just-in-time doboz és a :375 megnyitási feltétel helyére „nem adod be” jellegű jelölés; :377 címke, :42, hub :70 igazítva; a PT:225 és :238 M0.1-tagmondata szűkül (a projektgazdai döntés az 1. rangú forrás fölött áll); SLIDE 6 nem completion-feltétel (F-M0.1-2) | a :369 adattakarékossági mondata, a :49 blokk, a „2–4 mondat”, a :379–381 kérdés változatlan; „nem tároljuk” csak az X-2 után; pin |
| F-M0.2-3 (D-4) | :454 és :457 a tanuló-lokális úthoz (az F-Z.2-4 mintája); SLIDE 6 a Completion-sorban nem feltétel (F-M0.2-2) | Memuna- és 112-utasítás, :459 HUM-SAFE-03 blokk szó szerint; Memuna-QA |
| F-M0.3-1/-3 (D-6) | (a) ág: :342 beviteli elem nélküli, opcionális lépés; :57 mezőspecifikus; :318 a mikrocél szerint (:42); :44 nem ígér címzettet; :350 „amit itt megfogalmaztál”; LMS-M0-03 megjegyzése | opcionális státusz és :339–340 prompt változatlan |
| F-M5.2-2 (D-4) | SLIDE 9 tanuló-lokális: a :621–627 doboz és a :627 fejlesztői feltétel a tényleges kezeléshez; „a mondat nálad marad (munkalap M5.2-MUNK-01 vagy saját jegyzet)”; LMS-M5-02 megjegyzése; Completion-sor | :613–619 feladat, :623 adattakarékossági mondat változatlan; pin |
| F-M5.4-5 (D-4) | SLIDE 4–5 tanuló-lokális vázlat: :41 „Mit gyűjtünk” az Assignmentre és a teljesítésre szűkül, :44 a leadott táblázatra; :230 „Essay / szövegmező” → beviteli elem nélküli lépés vagy igazoltan nem rögzítő elem (X-2); :202 „min. 3 sor” útmutatás (BS-D4); LMS-M5-04 megjegyzése; Completion-sor | „3–4 helyzet”, „legalább 3 sor”, :200 és :322 korlát szó szerint; „opcionális” nem kerül be |
| F-M6-X (D-5) | a PT:222 zárójeles felsorolása a választós itemekre szűkül; az M6.1–M6.4 szöveges gyakorló válaszai tanuló-lokálisak: LMS-M6-01…04 megjegyzése (LMS-M1-01 minta), Completion-sorok, a :46/:48/:105 mezőspecifikus sablon | az akadálymentesítési minimum (célméret, billentyűzet, fókusz) és a hub :224 változatlan |
| F-M6.2-2 (D-5) | :903 második mondata törlendő (tárolást sugall); az első mondat szó szerint | ugyanez az M6.4:1022-ben (F-M6.4-2) |
| F-M6.4-2 (D-5) | a záró vázlat :997 („nyitott mező” → tanuló-lokális lépés), :1022 második mondata, :105 második fele | :1017 doboz, „4–6 mondat”, négy kérdés változatlan; DPO-QA |
| F-M6.3-1/-2 (D-5) | SLIDE 3–6 mezői tanuló-lokálisak; :48 ennek megfelelően; :38 „kell” és :1191–1196 igazítása; LMS-M6-03 megjegyzése | az F-M6.3-3 (tárolt ági korlát) tárgytalan |
| F-M7.4-2/-3 (D-4) | SLIDE 3 tanuló-lokális: :429, :833 beviteli elem nélküli lépés; :431 nem nevezi adatgyűjtőnek; a PT:319 „M7.4 SLIDE 3” példája kikerül; :682 mentési utasítás („írd le magadnak / vidd át a v1-be”) | :439–441 adatminimalizálás szó szerint; a mezők szövege és terjedelme változatlan |
| X-1 → M5.1 (H-6) | az M5.1:24 runtime-sablon mezőspecifikus; a :605 opcionális, tanuló-lokális | a :605 prompt és „ha szeretnél” változatlan |

A D-4…D-6 tárolt ágához kötött alkérdések (M0.1 BIZT-6, M0.2 A1–A3, M6.3 IMPL-4, M7.4 megőrzési sor) tárgytalanok.

## 5. Nem blokkoló emberi döntések, bizonyíték-kapuk, hatókörön kívüli tételek

**Learner-release emberi döntések (a BSPEC-02-t nem blokkolják):** N-1…N-5 (1–7. fájl 3.2); N-5 hatóköre kiterjed az
LMS-M7-04-re. Újak:
- **N-6** (M0.4 BIZT-5): az LMS-M0-05 posztjaira melyik ADV §3 sor vonatkozik, vagy saját sor kell? Gazda: projektgazda
  (HUM-PRIV-01), a BS-D6 mintájára a DPO-ra bízható.
- **N-7** (M0.4 BIZT-6): a FORUM-C „személyes/érzékeny adatot ne kérjen” szabálya alá esik-e a „Ki vagy és honnan
  jöttél?” segítő kérdés? Gazda: projektgazda; vétó: DPO.
- **N-8** (M0.4 BIZT-7): ki figyeli a Bemutatkozó falat, és ki, milyen határidővel veszi ki a feltárást tartalmazó
  posztot? Gazda: HUM-SAFE-01 döntéshozó (programvezető a Memunával — nem ellenőrzött).
- **N-9** (M3.4 BIZT-5): valós eset miatt eltávolított M3 modulproduktumnál az eredeti beadás számít-e próbálkozásnak,
  ki nyit új beadást, milyen határidővel? Gazda: értékelési felelős + programvezető; vétó: Memuna.

**Bizonyíték-kapuk (nem javíthatók; G1/G2/G3b):** az 1–7. fájl 4. szakasza, továbbá: M0.1 (BIZT-5), M0.2 (IMPL-05),
M3.3 (IMPL-4), M3.4 (IMPL-6, BIZT-9 Memuna G1, BIZT-10), M5.2 (IMPL-6), M5.4 (IMPL-6, BIZT-3 Google-sablon), M6.1
(BIZT-5), M6.2 (IMPL-5), M6.3 (IMPL-6), M6.4 (IMPL-3, RT-P0-02), M7.4 (IMPL-6, BIZT-6). Megvalósítási döntés:
projektgazda jóváhagyta (HUM-PRIV-01); a formális szerepköri bizonyíték függő.

**Hatókörön kívül (nem BSPEC-02):** H-1…H-4 (1–7. fájl 6. szakasz), továbbá:
- **H-1 párja (M6.4 O-1):** az M6.4:103 tartalékútjának („Moodle-checkpoint”) nincs profilja és sora, a „Tovább a
  lezáráshoz” gomb egy ág után is elérhető — a H-1-gyel együtt külön BSPEC-sor tárgya.
- **H-5 (M7.4 ERT-3):** a hub :243 v1-minimumlistájából hiányzik a SMART cél (pin kell).
- **H-6 (lefedettség) — rendezve:** M5.1:605 opcionális mező, a BSPEC-02 listáján nem szerepelt; a projektgazda döntése
  szerint `OPTIONAL_LEARNER_LOCAL`, sor nélkül, az X-1 kiterjesztésével (4.1).
- **Elvetve a 8–20. körben — P1:** M0.3 BIZT-3 (az xAPI-válaszrögzítés a CP-be ágyazható egyetlen szövegtípusra nem
  áll; a mentett állapotot az X-2 fedi); M6.2 IMPL-3 (a Completion-sor hiánya nem korpusz-konvenció-sértés). **P2:** 8
  (M0.2 BIZT-05, M0.4 BIZT-8, M3.4 BIZT-7, BIZT-8, IMPL-5, M5.2 IMPL-5, M6.3 IMPL-5, M7.4 ERT-4).

## 6. Állapot

- **A leltár teljes, BSPEC-02-blokkoló emberi döntés nem maradt** (D-1…D-6 és H-6 lezárva). Minden mezőnek pontosan
  egy besorolása van (2. szakasz, a D-4…D-6 szerint frissítve).
- **BSPEC-02: `BUILD_SPEC_OPEN`, amíg a `/course-fix` nem viszi be:** a négy új TEXT-C sort (LMS-M1-07, LMS-M2-08,
  LMS-M2-09, LMS-M7-10), az 1–7. fájl 2. szakaszának és e fájl 4. és 4.1 szakaszának F- és X-tételeit, a D-1…D-6
  átvezetését a HUM 10. szakaszba, a runtime acceptance új tételeit (X-2, F-M3.4-5, F-M6.1-2 stb.), és a BSPEC-02 sor
  frissítését. Lezárás `BUILD_SPEC_RESOLVED`-ra csak a valós megoldó commit után, a meglévő nyilvántartási minta szerint.
- **Nem blokkoló, nyitva maradó tételek:** N-1…N-9 (learner release), a bizonyíték-kapuk (G1/G2/G3b), H-1…H-5.
- `MOODLE-BUILD-VERDICT: NOT_READY` (`--release-report`: BSPEC-02, 38 besorolatlan checklist-tétel, 4 fallback nélküli
  kötelező média).
