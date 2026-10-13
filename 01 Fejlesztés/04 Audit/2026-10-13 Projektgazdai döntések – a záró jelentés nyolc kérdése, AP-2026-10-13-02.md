# Projektgazdai döntések – a záró jelentés nyolc kérdése, AP-2026-10-13-02

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i válasza az `AP-2026-10-13-01` záró jelentésének nyolc
> projektgazdai kérdésére, és a felhatalmazás a következő célzott körre. Szó szerint, változtatás nélkül. A kánoni
> átvezetés: `02 Tervezet/Emberi jóváhagyás szükséges.md` 16. szakasz.

---

Folytasd az AP-2026-10-13-01 záró jelentése alapján a PR #30 next-version ágán.

A nyolc projektgazdai kérdésben az alábbi irányokat fogadom el:

1. D-21: a /course-develop terv elfogadva, E7 igen, az M2.F és M4.F csak opcionális hivatkozást kap. Az E1–E6 szerepköri döntések maradnak nyitva. Az új tananyag kidolgozását külön /course-develop futásként kezeld.
2. D-20: a B-változatok belső blokkhatár-eltolása engedélyezett, amennyiben a teljes időkeret és a védett lépések változatlanok. A modulgazdai és programvezetői jóváhagyás továbbra is szükséges.
3. ERT-43: az új R1-horgony elve elfogadva, de csak az értékelési felelős és a lektor QA-ja, valamint előzetes tanulói tájékoztatás után léphet hatályba. Nincs visszamenőleges hatás.
4. M6-NY-D27: feloldva a Memuna szakmai review-ja céljára; a küszöb módosítása nincs előre jóváhagyva.
5. D-08 (b): a meglévő szituációcím külön, semleges előnézeti csomóponton jelenjen meg a passz-választás előtt, a történet feltárása nélkül. Az eredeti kérdés és két opció marad. Memuna-QA és runtime-teszt szükséges.
6. LMS-M4-05: egyetlen holisztikus rubrikakritérium, 0/1/2 szintpont, Grade type Point, Maximum grade 2, Grade to pass üres. A numerikus érték rejtve, a szöveges értékelés látható. Az eredeti három szint tartalmát ne változtasd. Értékelési QA és Moodle-visszaolvasás szükséges.
7. D-16: a végleges lezárt státusz helyett szakmai jóváhagyásra váró besorolás; a meglévő implementációt ne vond vissza automatikusan.
8. JOG-1: tedd közzé a záró jelentésben előkészített kommentet a GitHub #1 issue-ban, személyes adatok nélkül.

Rögzítsd a projektgazdai döntéseket a kánoni HUM-helyen. A szakértői hatáskörű döntéseket és bizonyítékkapukat ne zárd le helyettük.

Végezd el az engedélyezett célzott módosításokat és teszteket, frissítsd a ledgert, majd commitolj és pusholj a next-version ágra.

Ezután ne indíts újabb általános auditot. Készíts rövid státuszjelentést arról, hogy pontosan milyen Memuna-, DPO-, értékelési és LMS-bizonyíték szükséges még a staginghez és a release-hez.

A main, a pilot és a CC-04 freeze érintetlen. A PR draft marad. Nincs merge, staging deployment vagy learner release.
