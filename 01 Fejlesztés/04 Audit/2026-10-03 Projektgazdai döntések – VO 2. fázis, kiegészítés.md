# Projektgazdai döntések — VO 2. fázis, kiegészítés (2026-10-03)

> **Audit trail, nem tananyag.** A projektgazda válaszai a VO 2. fázis course fix pack (`/course-fix`) utáni
> egyeztetésen, 2026-10-03-án, a munkamenetben feltett kérdésekre (AskUserQuestion). A kérdés és a választott opció
> szó szerint áll; a hangok szerepnéven (2026-10-03-A). Ez a fájl a K1–K4, K6, K7 döntések és a K5 tényközlés bizonyítéka; a kapcsolódó
> nyitott findingok: `2026-10-03 course-fix napló – VO 2. fázis.md`, „Célzott utóellenőrzés”.

**Jóváhagyta:** projektgazda · **Dátum:** 2026-10-03

## K1 — Hangnév-utalás a nyilvános döntésmásolatban (UE-BIZT-7)

- **Kérdés:** „A nyilvános döntésmásolatban (CF-01, 857–859. sor) ez áll: az egyik hangnév egy forrás-beszélő
  keresztneve, a másik becenévszerű. Nevet nem tartalmaz, de részben visszafejthetővé teszi, melyik hang melyik
  forrás-beszélőé. Mi legyen vele, mielőtt commitolok?”
- **Válasz:** „Semlegesítsd (Ajánlott)” — a félmondatot a nyilvános másolatból kihagyom, és a fájl elején jelzem a
  kihagyást. A teljes, szó szerinti szöveg a privát VO QA-repóban marad.
- **Végrehajtva:** a `2026-10-03 Projektgazdai döntések – VO 2. fázis.md` ADDENDUM 1. kérdésében a félmondat helyén
  szögletes zárójeles jelzés áll, a fájl fejléce kimondja a kihagyást (commit előtt; a félmondat a git-historyba
  nem került).

## K2 — A csak hangot tartalmazó narrációk a11y-jegyzete (UE-IMPL-1, VO D-19)

- **Kérdés:** „A csak hangot tartalmazó narrációk a11y-jegyzete (kb. 80+ asset, köztük a P-NAR, M4.2-NAR-03) még
  kötelező feliratot ír elő. A VO D-19 szerint a látható leirat a szöveges ekvivalens. Átvezessem mindre a következő
  fix packban?”
- **Válasz:** „Mindre, egységesen (Ajánlott)” — csak az a11y-jegyzet szövege változik, az M3.3 mintájára. A
  `captions` derivatíva archivált .vtt-ként marad, a deliverable-ek száma nem változik.
- **Hatókör-korlát:** a videó hangsávjaként szóló narrációkra (szinkronizált média) a felirat-követelmény
  (WCAG 2.2 SC 1.2.2) változatlan.

## K3 — A voice-ID helye (UE-IMPL-5)

- **Kérdés:** „Hol legyen a két hang voice-ID-ja? A döntéscsomag csak annyit mond: nem nyilvános, bizonyíték
  szempontjából biztonságos helyen. A dokumentumok most egymásnak ellentmondóan írják.”
- **Válasz:** „VO QA-repó gyártási konfig (Ajánlott)” — csak a privát VO QA-repó gyártási konfigurációjában lesz. A
  nyilvános kurzusrepó csak annyit rögzít, hogy nem nyilvános helyen van, ID nélkül. Az R3 a P-NAR fülre
  jóváhagyásáig nyitott marad.

## K4 — A második hang az első gyártási körben (a VO D-14 módosítása)

- **Kérdés:** „Használjuk-e a második hangot már az első gyártási körben? (Jelenleg a VO D-14 szerint az első körben
  mindent a kanonikus narrátorhang mond, az M1.3 két szerepét is, külön szegmensben.)”
- **Válasz:** „M1.3 Madrih B már most” — az első körben is a második hang mondja Madrih B-t. Előbb kalibrálni kell
  (ez QA-repó oldali munka), és a kurzusdokumentumokban a D-14 módosul.
- **Következmény (a döntésből levezetve, nem új döntés):**
  - Az `M1.3-VID-01` párbeszédében Madrih A a kanonikus narrátorhang, Madrih B a második hang; a
    beszélőnkénti szegmentálás és a feliratbeli beszélőjelölés marad. Minden más narráció, köztük az `M1.3-NAR-08`
    képleírás és az M4.1-jelenetek (VO D-15), a kanonikus narrátorhanggal szól.
  - Az `M1.3-VID-01` hanganyaga ezért a második hang kalibrálásától függ: a VO D-14 „do not block the first-pass VO
    production on the calibration of the second voice” kitétele erre az egy tételre nem érvényes; a többi tételt ez
    nem blokkolja.
  - A második hang kalibrálása és a gyártási konfigurációja a VO QA-repó feladata; a hangjog formális bizonyítéka
    (R2-5) változatlanul függő.
  - A kurzusoldali dokumentumok (VOICE-BIBLE 8., 9., 11.; PRODUCTION-DECISIONS D11; az M1.3 `decision` mezője;
    PRODUCTION-STACK 5., 11.; PILOT-PRODUCTION-PACK P-KAR; ELEVENLABS-VOICE-TEST 7.) átvezetése `/course-fix`-szel.

## K5 — A forrás-beszélők nagykorúsága (UE-BIZT-3) — projektgazdai tényközlés

- **Forrás:** a projektgazda szabad szöveges üzenete a munkamenetben, 2026-10-03 (nem AskUserQuestion-válasz), szó
  szerint: „forrásbeszélők nagykorúak”.
- **Osztály:** projektgazdai tényközlés (a VO D-01 hanghasználati közlésének mintájára). Tartalmilag lezárja, hogy a
  két forrás-beszélő (`VOICE-SRC-01`, `VOICE-SRC-02`) nagykorú.
- **Nem állítja:** hogy a nagykorúság formális igazolását a DPO vagy a jogi felelős ellenőrizte. Az igazolás
  (a `VOICE-RIGHTS-REGISTER` nem személyes hivatkozása, jóváhagyói minősítés) a VO D-08 szerint bizonyíték-kapu marad;
  személyes adat (életkor, születési dátum) a repóba nem kerül.
- **Átvezetés:** a kurzusoldali hivatkozó helyek (RIGHTS-EVIDENCE R2-5, ELEVENLABS-VOICE-TEST 1.0., a HUM-MEDIA-02
  2026-10-03-i bekezdése) a következő fix packban, `/course-fix`-szel.

## K6 — A nagykorúság igazolása a hangjogosultsági nyilvántartásban (UE3-BIZT-3)

- **Kérdés (a munkamenetben, szabad szöveggel):** „Nagykorúság igazolása: kerüljön-e a hangjogosultsági
  nyilvántartásba (pl. „ellenőrizve: igen”, életkor nélkül)?”
- **Válasz, szó szerint:** „persze kerüljön ellenőrizve vanna knagykorúak, pont.”
- **Döntés:** a `VOICE-RIGHTS-REGISTER` a forrás-beszélőkhöz rögzíti, hogy a nagykorúság ellenőrizve (igen/nem), az
  ellenőrzés dátumával és az ellenőrző szerepével; életkor, születési dátum vagy igazolvány-adat nem kerül bele. A
  projektgazda közlése szerint mindkét forrás-beszélő nagykorúsága ellenőrizve van.
- **Nem állítja:** DPO- vagy jogi jóváhagyást. A nyilvántartás bejegyzése és a jóváhagyói minősítés a VO D-08 szerint
  bizonyíték-kapu marad (a nyilvántartás a repón kívül, korlátozott hozzáférésű helyen él; a repóba csak a nem
  személyes hivatkozás kerülhet). Utólagos ellenőrzés (vétó/QA): DPO.
- **Átvezetés:** ELEVENLABS-VOICE-TEST 1.0. („nyitott” mondat), RIGHTS-EVIDENCE (a nyilvántartás kötelező mezői, R2-5),
  HUM-MEDIA-02 2026-10-03-i bekezdése — a következő fix packban, `/course-fix`-szel.

## K7 — Az `M1.3-NAR-08` képleírás ikon-hozzárendelésének helye (UE3-PED-2)

- **Kérdés:** „M1.3 képleírás: a kb. 19 mp-es ikon-magyarázat maradjon Madrih A és B mondata között, vagy kerüljön B
  válasza után? mit ajánlasz erre?” Az ajánlás: kerüljön B válasza után, mert a lecke célja („a tanuló *érezze* a
  különbséget”) és a videó utáni kérdés („amire ezért nehezebb védekezve reagálni”) az SBI-mondat és B azonnali
  reakciója közti kapcsolatra épül; így a 2. verzió üteme az 1.-ével azonos; ára a hozzárendelés kb. 3 mp-es késése.
- **Válasz, szó szerint:** „csináljuk az ajánlásod szerint ha magabiztos vagy benne és megalapozottan jobb a hatása”.
- **Döntés:** a 2. verzió két replikája között csak az ikonok felvillanása és B reakciója hangzik el; a három ikon
  szövegrész-hozzárendelése egy új, ötödik részben, Madrih B válasza után, a videó megállása (a kérdés) előtt szól. A
  VO D-18 („place it in available dialogue gaps”) erre is kiterjed; a négyrészes felosztás nem a döntés része volt.
- **Ellenőrzés:** a legyártott videón hallgatási próba (a képleírás hallásra elkülönül Madrih A replikájától — azonos
  hang, K4) és hossz-újramérés a VO QA-repóban.
- **Átvezetés:** az M1.3 lecke `M1.3-NAR-08-VO` forrásblokkja, a gyártási jegyzet és az `M1.3-NAR-08` asset `spec`
  mezője — a következő fix packban, `/course-fix`-szel.
