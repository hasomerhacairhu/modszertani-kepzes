# Projektgazdai felhatalmazás – a célzott QA döntései és a részleges átvezetések, AP-2026-10-12-02 (2026-10-12)

A projektgazda 2026-10-12-i üzenete, szó szerint:

> Folytasd a PR #30 fejlesztését a `20d29c3` állapotból.
>
> Dolgozd fel a 40 új QA-döntést és a fennmaradó részleges implementációkat. Kutatással és szakmai indoklással javasolj megoldást, vond össze az átfedéseket, és implementálj mindent, ami a már elfogadott döntések alapján biztonságosan lezárható.
>
> Ne indíts új teljes auditot, és ne nyisd újra a 125 elfogadott döntést.
>
> A valódi szakértői jóváhagyásokat különítsd el. Ellenőrizd külön az M7 kapukvíz visszajelzéseinek válaszszivárgási kockázatát.
>
> Futtasd le a célzott QA-t és a regressziós teszteket, commitolj és pusholj a next-version ágra.
>
> A végén adj rövid, csoportosított listát kizárólag azokról a kérdésekről, amelyekhez tényleges emberi döntés vagy bizonyíték kell.
>
> A PR maradjon draft. Nincs merge, staging deployment vagy learner release.

**A futás:**
- Run-ID: `AP-2026-10-12-02`, változat: `next-version`.
- Ág: `next-version/AP-2026-10-11-01`; bázis `20d29c3`.
- Bemenet: az `AP-2026-10-12-01` ledgerének nyitott tételei (a célzott QA 40 `QA14`-kulcsú emberi döntés-tétele, a korábbi `BLOCKED_HUMAN` és `EVIDENCE_GATE` sorok), a `2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md` részleges átvezetései és nyitott megfigyelése (ERT-5, M7).
- Ledger: `AUTOPILOT-LEDGER.md`. Az előző futás ledgere a git-historyban marad, utolsó állapota `20d29c3`.
