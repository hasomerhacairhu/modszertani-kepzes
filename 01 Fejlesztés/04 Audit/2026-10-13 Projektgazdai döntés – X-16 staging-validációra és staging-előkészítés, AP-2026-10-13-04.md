# Projektgazdai döntés – X-16 staging-validációra és a staging-előkészítés, AP-2026-10-13-04

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i válasza az `AP-2026-10-13-03` jelentésére. Szó szerint,
> változtatás nélkül. A kánoni átvezetés: `02 Tervezet/Emberi jóváhagyás szükséges.md` 17. szakasz.

---

Folytasd a `hasomerhacairhu/modszertani-kepzes` projektet a PR #30 aktuális HEAD-jéről (ellenőrzési alap: `86b78ab`).

**X-16 projektgazdai döntés**

A javasolt Moodle Grade Letter megoldást elfogadom staging-validációra, a következő feltételekkel:

- Egységes címke: „Szöveges értékelés”, 0%-os alsó határral.
- LMS-M2-05, LMS-M4-05, LMS-M6-05: `showscorestudent = No`, `Grade display type = Letter`; a grade item látható.
- A javasolt tanulói pontkönyv-beállítások érvényesek; `Show average = No`, `Show grades = Yes`, `Show feedback = Yes`.
- Course total rejtett.
- Rubrikaszintek, pontértékek, küszöbök, completion és GATE-CP változatlanok.
- A kurzusszintű mellékhatásokat külön regressziós teszttel ellenőrizd.

Ez staging-tesztelési jóváhagyás, nem végleges X-16 release-elfogadás.

Az RT-P0-28 igazolja az Assignment, Grades, Quiz, mobil- és API-megjelenítést. Ha a tanuló a `graderaw` vagy más út révén mégis hozzáfér a numerikus pontszámhoz, ezt ne minősítsd teljesített rejtésnek. Vizsgáld meg a jogosultságkorlátozás lehetőségét, és hagyd nyitva a release-kaput, amíg a kérdés nincs rendezve.

**Staging előkészítés**

A legkisebb értelmes M0+M1 szintetikus staging-szeletet készítsd elő a már jóváhagyott manifest és a staging-leltár alapján.

Ne kérj valódi dátumot vagy személyes kontaktot a staging build előfeltételeként. A hiányzó célkörnyezetet, Moodle/H5P-verziókat és hozzáféréseket tételesen jelezd. Hitelesítő adatot ne tárolj a repóban.

A tényleges deploymentre még nem adok engedélyt. A runtime-teszteket ne jelöld sikeresnek, ha nem futottak le a célkörnyezetben.

Ne indíts új teljes auditot. Az engedélyezett dokumentációs és build-spec javításokat teszteld, commitold és pushold a next-version ágra.

A main, pilot és CC-04 freeze változatlan, PR #30 draft, merge és learner release nincs.

A végén röviden jelentsd: X-16 konfigurációs státusz, staginghez hiányzó konkrét hozzáférések, következő végrehajtható művelet és nyitott runtime-kapuk.
