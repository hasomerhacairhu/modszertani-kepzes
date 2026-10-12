# Projektgazdai döntés – a next-version 125 döntési javaslatának elfogadása (2026-10-12)

- **Futás és ág:** AP-2026-10-11-01 (`next-version`), `next-version/AP-2026-10-11-01`, draft PR #30. A pilot forrása (`main@213a4c5`) nem változik.
- **A kérdések:** `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`. 141 bejegyzés: 125 döntés és 16 bizonyíték- vagy aláírás-bejegyzés.
- **Az elfogadott dokumentum:** `2026-10-12 Döntési javaslat – M0–Z 125 döntés, kutatással megalapozva.md`. Az eredeti fájl `M0-Z_125_kutatassal_megalapozott_dontesi_javaslat_2026-10-12.md`, sha256 `7c1179d65bf65d0c687abec986840b37065a42daecbaa5198b7a7b0c325c9758`.
  - A repóbeli példányban csak a 13 sorvégi, két szóközös kemény sortörés lett `\` (CI-szabály: `.claude/rules/course-content.md`). Más eltérés nincs.
  - A dokumentum mind a 125 döntés-azonosítót pontosan egyszer tartalmazza (53 `A`, 72 `F`), és felsorolja a 16 bizonyíték-bejegyzést. Ezt a fő session szkripttel ellenőrizte a döntési csomaggal szemben.

## A projektgazda szó szerinti döntése (2026-10-12)

> „minden feltételes é konkrét javaslatot elfogadok egy az egybe, minde ajánlat és válasz a nyitott kérdésekre iott találod a választ! Mindenre, szóval minde nlezárható, nincs több nyitott kérdés”

(A csatolt fájl: `/…/Downloads/M0-Z_125_kutatassal_megalapozott_dontesi_javaslat_2026-10-12.md`; a repóbeli példány fent.)

A dokumentum saját fejléce szerint önmagában „nem a 125 döntés formális meghozatala”. A formális döntés ez a projektgazdai elfogadás.

## Mit jelent a döntés a kánon szerint

Alap: `.claude/rules/safety-and-human-gates.md`, „Lezárt döntések”; `Emberi jóváhagyás szükséges.md` 11. szakasz, státusz-szemantika.

1. **A 125 döntés lezárt projektgazdai döntés (`OWNER_DECIDED`).** Minden döntés tartalma a dokumentum azonos azonosítójú sora, szó szerint. A kánoni átvezetés helye az `Emberi jóváhagyás szükséges.md` 14. szakasza. A HUM-táblában az átvezetés két ponton tér el a betűtől, jelentésváltozás nélkül; mindkettőt a gépi ellenőrzés tette szükségessé:
   - a modulazonosító előtti névelő „az” (ERT-7, ERT-20, ERT-23, ERT-35, LMS-6);
   - a TECH-1 sorában körülírás áll a gyermekvédelmi őr által tiltott egybeírt alak helyett.

   A szó szerinti eredeti a dokumentumban áll.
2. **Az `F` döntések feltétele a döntés része.** Amíg a sorban megnevezett feltétel nem teljesül, a sorban megnevezett óvatos alapértelmezés érvényes. Ilyen feltétel: szerepköri QA, DPO által rögzítendő érték, runtime-teszt, szerzői megerősítés.
3. **A szerepek ellenőrzése vétó/QA.** A döntési csomagban bejegyzésenként megnevezett jóváhagyók utólag ellenőriznek (vétó/QA): Memuna, DPO/jogi felelős, értékelési felelős, programvezető, modulgazda, LMS-gazda, hozzáférhetőségi gazda, szakmai lektor, VO-gazda. Vétónál az érintett döntés `REOPENED`.
4. **Ahol a dokumentum eltér a döntési csomag ajánlásától, a dokumentum érvényes.** Az eltéréseket a dokumentum „Lényeges eltérések” szakasza sorolja fel: TECH-1, LMS-6, GYV-4/GYV-14, ERT-40, ADV-11.
5. **PRG-17:** a döntés a CC-04 szerinti halasztás; az M0.1 SLIDE 5 kérdését a pilot-visszajelzéssel együtt kell eldönteni.

## Amit ez a döntés nem zár le

- **A 16 bizonyíték- és aláírás-bejegyzés nem zárul:** GYV-24, ADV-E1, ADV-E2, ADV-E3, SIG-1…SIG-6, RT-1…RT-6.
  - Ezek a `RELEASE-READINESS.md` G1–G8 kapuinak bizonyíték-kapui. A megnevezett szerep írásos bizonyítékával vagy célkörnyezeti runtime-eredménnyel zárulnak, projektgazdai döntéssel nem.
  - A dokumentum maga is kimondja: „kutatással sem jelölhető DONE-nak”.
- **Szerepkörhöz kötött bemenetek az `F` döntéseken belül.** Ezek nem nyitott projektgazdai kérdések, hanem vétó/QA vagy bizonyíték. Példák:
  - a DPO által rögzítendő megőrzési értékek (pl. ADV-6, ADV-14);
  - a GDPR 9. cikk szerinti minősítés (ADV-5);
  - a jogi szakértő értelmezése a Gyvt. 17. § címzettjeiről és határidőiről (JOG-1, GYV-15);
  - a Memuna helyenkénti verdiktje (GYV-3);
  - a segélyvonal-leírás pontosítása (GYV-4, GYV-14). A lezárt HUM-SAFE-01 kontaktsorát a dokumentum szerint a Memuna nyitja újra formálisan; addig a szöveg nem változik.
- **Végrehajtás.** A döntések átvezetése a tananyagba külön, engedélyezett javítási kör a next-version ágon. A dokumentum végrehajtási sorrendjének 4. pontja szerint ez a projektgazda erre adott felhatalmazásával indul.
- **Futó pilot.** A `main@213a4c5` és az M0+M1 freeze (CC-04) változatlan. A dokumentum szerint az ADV-6 bemutatkozó fóruma valódi tanulóknak zárva marad a DPO megőrzési döntéséig; ez üzemeltetési lépés, nem repóváltozás. A PR #30 draft marad.
- **Release.** `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO` — változatlan, és egyik sem release-jóváhagyás.
- **Ledger.** Az AP-2026-10-11-01 ledger (FINISHED) tételállapotai nem változnak. A végrehajtási kör saját futást és ledgert kap, ennek a döntésnek az azonosítóival.
