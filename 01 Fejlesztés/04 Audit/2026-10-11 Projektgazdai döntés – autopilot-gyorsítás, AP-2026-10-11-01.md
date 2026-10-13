# 2026-10-11 Projektgazdai döntés – autopilot-gyorsítás (AP-2026-10-11-01)

> **Audit trail — a projektgazda szó szerinti válasza.** A döntés a futás munkarendjét érinti, a tananyag tartalmát nem;
> governance-fájl nem változott. Kérdező: a Claude Code-session (autopilot), 2026-10-11 este; a válasz a session
> kérdőívén érkezett.

## Kérdések és válaszok (szó szerint)

1. **Kérdés:** „Javíthatok már most a lezárt review-jú modulokban (M0–M3, majd M4), amíg az M5–Z review fut? A CLAUDE.md
   szerint review közben nem szerkesztek tananyagot.”
   - A választott opció: **„Igen, átfedéssel (Recommended)”** — leírása: „Javítás csak lezárt review-jú modul fájljain,
     minden javítás azonnal commitolva. A futó review-k fejlécében rögzítem, hogy a saját scope-juk fájljai nem változtak.
     Kánoni közös fájlt (manifest, HUM, Glosszárium, Program terv) csak az összes review lezárása után javítok.
     Kb. 4–8 óra megtakarítás.”

2. **Kérdés:** „Mehet egyszerre 8-nál több read-only ügynök? A CLAUDE.md legfeljebb 8-at enged, és este már egyszer
   elfogyott a heti limit.”
   - A választott opció: **„Legfeljebb 12”** — leírása: „A review-fázis kb. 1–2 órával rövidebb lehet, de gyorsabban fogy
     a kvóta.”

## Alkalmazás ebben a futásban

- A CLAUDE.md „review közben nem szerkesztesz tananyagot” és „egyszerre legfeljebb 8” szabálya ennek a futásnak a
  hátralévő részére a fenti feltételekkel módosul; a CLAUDE.md maga nem változik (governance-módosítás nincs).
- Átfedéses javítás csak `VERIFIED` modul saját fájljain (`02 Tervezet/Modulok/<modul>/`), minden javítás azonnal
  commitolva, hogy a futó review-k read-only bizonyítéka (`git diff HEAD -- "02 Tervezet"`) a mentéskor is üres legyen.
  A futó review-k riportfejléce rögzíti a köztes javításcommitokat és azt, hogy a saját scope-juk fájljai nem változtak.
- A közös kánoni fájlok (`LMS – activity manifest.md`, `Emberi jóváhagyás szükséges.md`, a Glosszárium, a `Program terv.md`,
  az `Adatvédelem – tanulói adatok és AI.md`, a `Gyermekvédelem – release gate.md`, a `RELEASE-READINESS.md` és a
  `Média-assetek/` kánonja) javítása az összes modul review-jának lezárása után kezdődik.
- Párhuzamosan legfeljebb 12 read-only ügynök fut; tananyagot továbbra is csak a fő session ír, sorban.
