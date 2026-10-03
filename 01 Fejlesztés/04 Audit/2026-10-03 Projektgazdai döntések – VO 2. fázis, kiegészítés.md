# Projektgazdai döntések — VO 2. fázis, kiegészítés (2026-10-03)

> **Audit trail, nem tananyag.** A projektgazda válaszai a VO 2. fázis course fix pack (`/course-fix`) utáni
> egyeztetésen, 2026-10-03-án, a munkamenetben feltett kérdésekre (AskUserQuestion). A kérdés és a választott opció
> szó szerint áll; a hangok szerepnéven (2026-10-03-A). Ez a fájl a K1–K4 döntések bizonyítéka; a kapcsolódó
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
