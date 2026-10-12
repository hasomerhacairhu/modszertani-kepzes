# Jóváhagyási kérés — DPO / jogi felelős (adatvédelem, G2)

**Állapot:** DÖNTÉSRE ÉS BIZONYÍTÉKRA VÁR. Ebben a dokumentumban semmi nincs jóváhagyottként rögzítve.

- A pilot forrása `main@213a4c5`. Az `Adatvédelem – tanulói adatok és AI.md` (ADV) a `main`-en és a next-version jelöltben azonos.
- Automatikus review, AI-összefoglaló vagy generált nyugtázás nem helyettesíti a saját írásos jóváhagyásodat.

## D-0 — Van-e DPO-jóváhagyás a futó pilot-kurzusra?

- **Szabály:**
  - ADV §1:5: „A learner-facing Moodle-kurzust a tényleges adatkezelő szervezet privacy/DPO/jogi felelőse hagyja jóvá.”
  - ADV:230: a kurzus adatvédelmi tájékoztatója „a DPO jóváhagyása előtt nem élesíthető”.
- **Tény:** a repóban ilyen jóváhagyás nincs rögzítve. A tájékoztató `PRIVACY_CONTACT_TO_CONFIGURE` mezője is nyitott (ADV §11, belső mezők).
- **Kérés:** ha a jóváhagyás a repón kívül megvan, add meg a helyét, a dátumát és a hatókörét. Ha nincs meg, a pilot a kánon szerinti DPO-jóváhagyás nélkül fut.

## D-1 — ADV-6: a „Bemutatkozó fal” fórum (LMS-M0-05, FORUM-C) megőrzése és a pilot (`M0:BIZT-7`, P0, PILOT-BLOCKER)

- **Tények (main):**
  - Az ADV §3 jogalap- és megőrzési mátrixában (:60–75) nincs fórumposzt-sor.
  - Az ADV :79 kifejezetten külön review-t ír elő az M0 „Bemutatkozó fal”-ra; ennek eredménye nincs rögzítve.
  - A tanulói tájékoztató (ADV §11) közli, hogy a fórumhozzászólást a résztvevők látják, de a „Meddig őrizzük meg?” listában nincs fórumsor.
  - PT:228: „Ha egy adatot gyűjtő aktivitásra ez nincs rögzítve, az nem nyitható meg valódi madrihnak.”
- **Pilot-következmény:** a fórum az „M0 complete” része (MAN:155: „Bemutatkozó fal 1 új téma/1 válasz”), és az M1.1 erre nyílik (MAN:45).
  - Ha a fórum nyitva van, a PT:228 sérül.
  - Ha zárva van, az M0 nem teljesíthető, és az M1 nem nyílik, hacsak a completiont nem módosítják. A módosítás projektgazdai freeze-kivétel.
  - Hogy a fórum ténylegesen elérhető-e valódi tanulóknak: **ISMERETLEN**; a repó nem tartalmaz élő Moodle-állapotot.
- **Döntés, kérdésenként:**
  1. Melyik megőrzési sor vonatkozik a fórumposztra és a válaszra?
     - (a) egy meglévő sor, pl. „Szabad szöveges reflexió”: a képzés vége + 90 nap;
     - (b) új, fórumra szabott sor;
     - (c) a pilotban a fórum nem nyílik meg, vagy rögzítés nélküli, szóbeli bemutatkozás váltja az M0.A-n.
  2. Mi az ADV :79 szerinti külön review eredménye?
  3. Ha a fórum már nyitva van és van benne valódi poszt: mi a teendő a meglévő posztokkal?
- **Ajánlás:** nincs. A megőrzési időt a repó nem választja meg (ADV §1:7); ez a te ítéleted. A tájékoztató szövegének és a completionnek a változásához projektgazdai freeze-kivétel kell.

## D-2 — ADV-E1 (pilot-rész): írásos release-jóváhagyás activitynként

- **Szabály:**
  - ADV §9 utolsó sora: „privacy/DPO/jogi signoff bizonyítéka rögzítve”.
  - RR G2 (:25): a DPO release-ellenőrzése FINAL_RELEASE_QA.
  - RR:83: az M1 Assignment valódi madrihnak csak jóváhagyott adatkezeléssel nyitható meg.
- **Hatókör (a futó M1):**
  - **LMS-M1-05** (M1.4 SBI-beadandó, ASSIGN-M) — `M1:BIZT-G2-2`, P0;
  - **LMS-M1-07** (M1.3 saját mini-SBI, TEXT-C, névhez kötött) — `M1:BIZT-G2-2`, az ERT-12 döntése után;
  - **LMS-M1-01** (M1.1 SLIDE 5, N-M1-04, BIZT-QA-1): a QA a HUM §12 (main :576–586) szerint nyitott; `M1:BIZT-G1-3`, P0.
- **Bemenet, amire a jóváhagyás épül** (az LMS-gazda adja, a runtime acceptance szerint; lásd az RT-2 ellenőrzőlistát):
  - RT-P0-15: két mentor és két csoport, közvetlen URL sem visz át;
  - RT-P0-24: az N-M1-04 adatmentessége, vagy annak rögzítése, hogy nincs beviteli elem;
  - RT-P0-06: a TEXT-C beállításai;
  - a szerepkör-kiosztás (ki szerkesztő tanár, menedzser, rendszergazda).
- **A jóváhagyás kötelező elemei:**
  - dátum és a jóváhagyó szerepe;
  - activitynként a build-ID és a Moodle `cmid`;
  - a Moodle-kurzus verziója;
  - a felhasznált runtime-bizonyítékok hivatkozása;
  - vétó esetén az érintett lezárt döntés megnevezése (az a tétel REOPENED lesz).

  Helye: a release-jegyzőkönyv (PT §9.3) és a tracker #2 (RR:61, :69).
- **Nem fogadható el:** az LMS-gazda tesztje önmagában, vagy generált szöveg.

## D-3 — ADV-1: szerkesztő tanári, menedzseri és rendszergazdai hozzáférés; csoportszűkítés (BIZT-2, BIZT-5; `M1:BIZT-G2-4`)

- **Miért most:** a D-2 M1-jóváhagyásához kell. Az M1.4:502 azt ígéri, hogy „a kijelölt mentorod/értékelőd látja”. Moodle-alapértelmezés mellett ez az ASSIGN-M-nél nem igaz (ADV §3:104–117).
- **Opciók (ADV-1):**
  - **(a)** szűkítés;
  - **(b)** a hozzáférés marad, a tájékoztató megnevezi az adminisztratív szerepeket;
  - **(c)** vegyes megoldás.
- **Ajánlás:** nincs; ez a te ítéleted.

## D-4 — ERT-12: vétójog

- A projektgazda ajánlott alapértelmezése a (b): az LMS-M1-07-be csak kitalált helyzet kerülhet.
- Ha a projektgazda mégis az (a)-t (valós, névtelenített helyzet) választaná, ahhoz a te adatkör-, megőrzési és hozzáférési jóváhagyásod kell. A projektgazda (b) döntését vétóval újranyithatod.

## Nem most

ADV-2…ADV-15, ADV-E2, ADV-E3: next-version tételek (a döntési csomag 4. szakasza). A futó M0+M1 pilotot nem érintik, kivéve a fenti D-0…D-4-et.
