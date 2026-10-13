# Projektgazdai felhatalmazás – a HUM 14. szakasz átvezetése, AP-2026-10-12-01 (2026-10-12)

A projektgazda 2026-10-12-i üzenete, szó szerint:

> Indítsd a HUM 14. szakaszban rögzített mind a 125 OWNER_DECIDED döntés teljes átvezetését a `next-version/AP-2026-10-11-01` ágon.
>
> A cél a végleges, szakmailag javított M0–Z tananyag előállítása, nem újabb döntés-előkészítés.
>
> - Mind a 125 döntést dolgozd fel, az A és F döntéseket egyaránt.
> - Az F döntéseknél alkalmazd az elfogadott óvatos alapértelmezést, amíg a külső feltétel nem teljesül.
> - Hajtsd végre a szükséges tartalmi, értékelési, LMS-specifikációs és kanonikus módosításokat.
> - Használd a meglévő review → fix → célzott QA → regresszió workflow-t. Ne kezdj újabb teljes alapreview-t.
> - A 16 bizonyítékkaput tartsd nyitva, de ne állítsd le miattuk a függetlenül elvégezhető fejlesztést.
> - Minden döntéshez rögzítsd az implementációt, a tesztelést és a fennmaradó külső függőséget.
> - A végén futtasd le a teljes elérhető validációt, és adj tételes, 125/125 lefedettségi jelentést.
>
> Dolgozz autonóm módon a teljes implementációs körön. A módosításokat commitold és pushold a next-version ágra.
>
> A `main`, a futó M0/M1 pilot és a CC-04 freeze érintetlen marad. A PR #30 maradjon draft. Merge, staging deployment és learner release nem engedélyezett.
>
> A végén különítsd el az IMPLEMENTED, a QA-ra váró és a külső bizonyítéktól függő tételeket. Ne jelölj semmit teljesítettnek tényleges bizonyíték nélkül.

**A futás:**
- Run-ID: `AP-2026-10-12-01`, változat: `next-version`.
- Ág: `next-version/AP-2026-10-11-01`; bázis `beaea60`.
- A döntések: `Emberi jóváhagyás szükséges.md` 14. szakasz.
- Ledger: `AUTOPILOT-LEDGER.md`. Az előző futás (`AP-2026-10-11-01`) ledgere a git-historyban marad, utolsó állapota `beaea60`.
