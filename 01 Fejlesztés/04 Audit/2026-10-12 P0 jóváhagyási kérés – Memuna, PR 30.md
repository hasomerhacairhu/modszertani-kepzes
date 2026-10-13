# Jóváhagyási kérés — Memuna (gyermekvédelem, G1)

**Állapot:** BIZONYÍTÉKRA ÉS DÖNTÉSRE VÁR. Ebben a dokumentumban semmi nincs jóváhagyottként rögzítve.

- A pilot forrása `main@213a4c5`, a sorszámok erre vonatkoznak.
- A gyermekvédelmi jóváhagyás egyetlen felelőse a Memuna (RR:39; GK §5).
- Automatikus review, AI-összefoglaló vagy generált nyugtázás nem helyettesíti a saját írásos bejegyzésedet.

## M-1 — GYV-24 (pilot-rész): írásos „átnéztem” az M0 gyermekvédelmi elemeire (`M0:BIZT-1`, P0)

- **Szabály:**
  - GK §2:17: „…nem nyitható meg valódi madrihoknak a Memuna írásos átnézése nélkül”.
  - GK §2:19 és RR:40: egyszeri, írásos „átnéztem” a release-jegyzőkönyvben (PT §9.3), a kész anyagra.
  - Az M0 riport §6 szerint az M0-rész a futó pilothoz most kell.
- **Hatókör (a futó M0, `main@213a4c5`):**
  - M0.2 SLIDE 3–4;
  - M0.4 SLIDE 2–4;
  - az M0 belépőkvíz 1–2. iteme (kulcs és visszajelzés; LMS-M0-06);
  - az M0.A mini-protokoll.
- **A bejegyzés kötelező elemei:**
  1. „átnéztem” nyilatkozat dátummal;
  2. az átnézett verzió: a repó-commit (`213a4c5`) **és** a Moodle-kurzus verziója vagy dátuma, ahogy a pilotban fut;
  3. a fenti hatókör felsorolása;
  4. a GK §6 ide tartozó sorai, soronként igen/nem:
     - nincs 100%-os titoktartási ígéret;
     - nincs nyomozásra vagy konfrontációra utasítás;
     - az 1:1 helyzetek és a kvízkulcsok megfelelnek a HUM-SAFE-02-nek;
  5. az akut út és a segélyvonalak ellenőrzése az átnézés napján, dátummal és forrással (GK §6; a forrás a GK §4.1 kontaktsora és a §7 listája);
  6. a tracker #1 frissítése a bejegyzés linkjével (RR:60, :69).

  Ha a bejegyzés a repón kívül már megvan, elég megadni a helyét.
- **Nem fogadható el:**
  - más által beírt vagy generált „átnéztem”;
  - hatókör vagy verzió nélküli szóbeli vagy chatbeli „ok”;
  - egy ledger- vagy tracker-állapot átírása a bejegyzés nélkül.

## M-2 — GYV-3 (M0-rész): kiterjed-e a SAFE-7 az M0.4 SLIDE 3 2. helyzetére? (`M0:BIZT-3`, feltételes pilot-blokkoló)

- **Kérdés:** a késő esti 1:1 üzenetes helyzet szövege és kulcsa megfelel-e a HUM-SAFE-02-nek és a kivételeinek (GK §4.2), és a kiskorú madrih szerephatárának?
- **Opciók (GYV-3):**
  - **(a)** a QA mind a hét 1:1 helyre kiterjed;
  - **(b)** csak az M3.3 S1;
  - **(c)** kiterjesztés, és a nem megfelelő helyek javítása a te szövegeddel.
- **Ajánlás a hatókörre: (a).** Indok: a GK §6 1:1 sora „a négyszemközti (1:1) helyzetek tananyagát és kvízkulcsait” kéri egyeztetni, nem csak az M3.3-at. A megfelelésről a te ítéleted dönt; addig a ✅ és a kulcs nem változik.
- **A pilothoz:** ha az M0.4 SLIDE 3 nem felel meg, a szövegváltozáshoz projektgazdai freeze-kivétel kell (CC-04).

## M-3 — GYV-12 (M1-rész): támogató szöveg a tárolt M1 mezőknél (`M1:BIZT-G2-10`, `M1:BIZT-G2-3`)

- **Kérdés:** az M1.3:914–916 és az M1.4:506–507 egyedi „ha nagyon nehéz helyzet” szövege helyére mi kerüljön?
  - **(a)** az ADV §11:241 feladatszintű adattakarékossági mondata;
  - **(b)** csak a már ott álló GK §4.3 blokk;
  - **(c)** marad.

  Az M1.4 Memuna-mondata (:508) egyik opcióban sem törölhető.
- **Ajánlás: (a)**, egy szerkesztésben a projektgazda ERT-12 döntésével. Indok: a GK §4.3:102 nem hagy ad hoc támogató szöveget a §4.3 blokk mellett, és a mostani „finomíthatsz” forma a nehéz helyzet beírására biztat.
- **Ki dönt:** a Memuna (a HUM-SAFE-03 szerint a programvezetővel).

## Csak tudomásul — M0-hoz kötődik, de az M0 riport szerint nem pilot-blokkoló

- **GYV-5 / `M0:BIZT-9`** (a programvezetővel): kell-e második felnőtt az M0.A-n. Operatív döntés, az M0.A dátuma a repóból nem ismert.
- **GYV-7 / `M0:BIZT-5`:** a csoportchat-szívatás jelzési küszöbe. Ajánlás nincs; ez a te ítéleted.
- **GYV-23 / `M0:PED-8`** (programvezető + Memuna; adatkör: DPO): egyéni utánkövetés a belépőkvíz 1–2. itemén.

## Nem most

- **GYV-1** (M2, N-3) és **GYV-2** (M2/M3 passz-út): jövőbeli modulok. A pilot hatóköre M0+M1 (HUM §11, PILOT-1), és a dátumfüggő M2-activity nem nyitható meg valódi tanulónak, amíg a dátuma nincs beállítva (PILOT-2). Élő bizonyíték arról, hogy M2 nyitva van, nincs. Ha az LMS-gazda visszaolvasása mást mutat, ezek azonnal pilot-tétellé válnak.
- **A GYV-24 teljes next-version hatóköre** a GYV-1…23 átvezetése után, a végleges verzióra.
