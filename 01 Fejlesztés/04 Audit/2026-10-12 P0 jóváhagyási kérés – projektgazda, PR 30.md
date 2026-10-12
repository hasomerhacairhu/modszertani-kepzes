# Jóváhagyási kérés — Projektgazda (P0, futó M0+M1 pilot)

**Állapot:** DÖNTÉSRE VÁR. Ebben a dokumentumban semmi nincs jóváhagyottként rögzítve.

**Források:**
- A pilot forrása `main@213a4c5`. A sorszámok erre vonatkoznak, ha nincs más jelölve.
- A next-version jelölt (draft PR #30) `e67cce5`.
- A teljes döntési csomag: `01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`. Ez a kérés csak a futó pilotot érintő tételeket emeli ki; a többi döntés ott marad.

## P-1 — ERT-12: valós vagy csak kitalált helyzet az M1.3 saját mini-SBI-ben (LMS-M1-07)

- **Kérdés:** kerülhet-e a tárolt, névhez kötött LMS-M1-07 mezőbe (TEXT-C, három „Required” kérdés, MAN:48) valós, névtelenített helyzet, vagy csak kitalált?
- **Finding:** `M1:BIZT-G2-1` (P0; az M1 B-sávos riport szerint PILOT-BLOCKER). Ráépül: `M1:BIZT-G2-3`, `M1:BIZT-G2-10` (a Memuna, GYV-12).
- **Mai tanulói szöveg (main):**
  - M1.3:886: „Lehet valós, hétköznapi helyzet (pl. múlt heti peula, de név és felismerhető részlet nélkül), vagy teljesen kitalált sztori.”
  - A NAR-05 hangszövege (M1.3:900–903) és specje (:838) ugyanígy szól: „valós vagy kitalált”.
  - Az M1 HUB:117: „(valós vagy fiktív)”.
  - MAN:48: „nyitott”.
- **Opciók:**
  - **(a)** Valós, névtelenített helyzet. Ehhez DPO által jóváhagyott adatkör, megőrzés és hozzáférés kell.
  - **(b)** Csak kitalált helyzet. Ez szövegigazítás az M1.3:886-on, a NAR-05/-06-on, a HUB:117-en és a MAN:48-on.
- **Ajánlott alapértelmezés: (b)**, a DPO vétójának fenntartásával. Indokok:
  1. Ugyanez a tanuló az M1.4 kapujában már csak kitalált helyzetet írhat (M1.3:886 vége: „oda már csak kitalált, életszerű helyzet kerülhet”).
  2. A lezárt HUM:462 a kapuproduktumra kimondja: „csak kitalált, életszerű eset; valós eset névtelenítve sem”.
  3. A tárolt mező névhez kötött, és egy „múlt heti peula” leírása kiskorú hanihokat érinthet. Kis közösségben ez névtelenítve is visszaazonosítható (GK §2, ugyanaz az indok).
  4. Az ADV §2 alapértelmezése a kevesebb személyes adat.

  A (b) a lezárt elv új alkalmazása, ezért kell hozzá a döntésed.
- **A döntés után:** külön engedélyezett `/course-fix`-kör. A Memuna GYV-12 M1-döntésével egy lépésben megy. A hang a VO-gyártási úton jön; a PILOT-4 szerint az M0/M1 pilot nem függ a narrációtól.

## P-2 — Freeze-kivétel a futó pilotra (külön döntés a P-1-től)

- **Kérdés:** a futó M0+M1 pilot forrásában (`main`) is átvezetődjenek-e P0 adatvédelmi freeze-kivételként ezek?
  - az ERT-12 választott szövege;
  - az ADV-6 tájékoztatója vagy completion-változása, ha a DPO döntése szövegváltozást kér.
- **Szabály:** CC-04, `2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md` :41: „Freeze-kivételt csak tényleges P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy a tanulói előrehaladást blokkoló hiba indokolhat.” Precedens: az N-M1-04 kánoni átvezetése P0 adatvédelmi freeze-kivételként (HUM §12, main :576–580).
- **Opciók:**
  - **(i)** Freeze-kivétel: szövegjavítás a `main`-en, a merge előtt, külön kis PR-ben.
  - **(ii)** Nincs freeze-kivétel: az LMS-M1-07 zárva marad a pilotban. Ennek ára, hogy az LMS-M1-04 az LMS-M1-07-hez kötött (MAN:49), így az M1.4 és az M1 kapu (LMS-M1-05/-06) sem nyílik.
  - **(iii)** Átmeneti operatív utasítás a cohortnak (a (b) tartalma, repóváltozás nélkül), amíg az (i) elkészül. Ez is a te döntésed; nem új szabály, hanem a P-1 választásának ideiglenes alkalmazása.
- **Ajánlás:**
  - Ha a P-1 = (b) és az LMS-M1-07 már elérhető valódi tanulónak (ez nem tudható, lásd lent), akkor (i) és addig (iii).
  - Ha még nem elérhető, akkor (i), mielőtt megnyílik.

## P-3 — PILOT-1: van-e rögzített M0+M1 GO-döntés és evidence list?

- **Tény:** a repóban nincs PILOT-1 szerinti M0+M1 evidence list, és nincs rögzített go/no-go döntés.
  - A HUM §11, main :548 szerint a GO „külön, explicit M0+M1 evidence list alapján kerül rögzítésre”.
  - Az RR:35 és :113 szerint ez dátummal, jóváhagyókkal és a runtime-bizonyítékokra hivatkozva kerül a release-jegyzőkönyvbe (PT §9.3).
  - Az M1 B-sávos riport (:674) sem látott ilyet.
- **Kérés:**
  - Ha a GO a repón kívül megvan, add meg a helyét: dátum, jóváhagyók, a felhasznált bizonyítékok.
  - Ha nincs meg, akkor a pilot élő tanulói hozzáférése a kánon szerinti GO nélkül fut. A döntés a tiéd (release owner).

## Csak tudomásul (nem kér most döntést)

- **RT-1 — „Segítség és kapcsolatok”** (`M0:IMPL-9` = `M0:BIZT-2`, P0):
  - A PILOT-3 (HUM §11, main :550) szerint kitöltetlen csatornával learner-facing pilot nem indul.
  - A valódi technikai és programkontaktot a programvezető adja; a megjelenést az LMS-gazda olvassa vissza (RT-P0-17).
  - A csomagban P1-ként szerepel, mert a P0-s `M0:BIZT-2` duplikátumként az `M0:IMPL-9`-be olvadt. **Futó pilot-blokkolóként kezelendő.**
- **PR #30 draft marad.** Merge csak a pilot után, vagy tételes freeze-kivétellel (CC-04). A merge módját te választod.
