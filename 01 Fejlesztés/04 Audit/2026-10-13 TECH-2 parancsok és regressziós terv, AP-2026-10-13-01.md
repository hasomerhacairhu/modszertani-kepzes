# TECH-2 – az M6.1 és az M6.2 átnevezése: ellenőrzött parancsok és regressziós terv (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Végrehajtási útmutató a HUM 14. szakasz TECH-2 döntéséhez (`F`): „Az M6.1/M6.2 két
> címbeli/fájlnévi javítását elvégezném külön, review-olható change setként, az összes hivatkozás, két gépi útvonalkulcs,
> baseline-rename mapping, pin és generált média együttmozgásával. A git mv-t a tulajdonos futtassa a saját termináljában,
> a hookot nem kerülve meg; utána célzott selftest, invariáns és külön media commit.” Vétó/QA: a felhasználó (az
> átnevezési commit futtatása) + projektgazda (a `tools/` két sora és a baseline-sor). A sorszámok a `61cc98a` állapoton
> ellenőrizve (2026-10-13).

## Miért nem futtatja a session

A `git mv` nincs a sandboxon kívül engedélyezett git-alparancsok között (`.claude/hooks/guard-repo-safety.sh`), és a
sandbox a repóba írást OS-szinten tiltja. A végrehajtási korlátot nem kerüljük meg: az átnevezési commitot a felhasználó
futtatja **normál terminálban** (nem a Claude-sessionből), a repó gyökeréből.

## Érintett findingok

`M6:NYELV-G1-11`, `M6:IMPL-G2-5`, `M6:NYELV-G3-3` (b), `M6:QA-IMPL-5` (ledger: X-7). A `M0:NYELV-G2-11` és a
`M3:IMPL-G2-15` szintén a TECH-2-re vár, de más fájlt nem nevez át; a TERM-1/TERM-4 szövegrészük külön tétel.

## 1. lépés – a felhasználó, normál terminálban (csak az átnevezés)

Előtte (olvasó parancsok):

```bash
cd "<a repó gyökere>"
git status --short            # üres legyen
git branch --show-current     # next-version/AP-2026-10-11-01
git log --oneline -1
```

Az átnevezés és a commit:

```bash
git mv "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md" "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játékkategóriák 3 aktuális kvucára.md"
git mv "02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md" "02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet mint tükör.md"
git commit -m "rename(M6): M6.1 and M6.2 file names (TECH-2, M6:NYELV-G1-11, M6:IMPL-G2-5)"
```

Ellenőrzés:

```bash
git show --stat --summary HEAD    # két „rename … (100%)” sor, más változás nincs
```

Fontos: az 1. lépés után **ne pusholj**, amíg a 2–4. lépés el nem készül. Az átnevezés után a
`tools/content_integrity.py` M6.1-es fájlszintű őre a régi útvonalat keresi, és hiányzó fájlnál csendben kihagyja —
ezért a 2. lépésnek ugyanabban a change setben kell következnie.

## 2. lépés – a session (`tools`, projektgazdai felhatalmazással)

- `tools/content_integrity.py:152` — a `FILE_FORBIDDEN_PHRASES` kulcs az új M6.1 útvonalra
  (`…/M6.1 – Játékkategóriák 3 aktuális kvucára.md`); a tiltott kifejezés és az indoklás változatlan.
- `tools/test_media_manifest.py:62` — a kulcs az új M6.1 útvonalra; a `:63` baseline-érték (`…/M6.1 – Játék-kategóriák 4 kvucára.md`) marad.
- `tools/test_media_manifest.py:80` után (`DECISIONS_2026_10_02_RENAMES` mintájára) új szótár, például
  `TECH2_2026_RENAMES = {"…/M6.2 – Történet mint tükör.md": "…/M6.2 – Történet, mint tükör.md"}`, és felvétele a
  `:102` `BASELINE_RENAMES` összefésülésébe (a baseline-commitban az M6.2 a régi néven létezik).
- Nem kötelező: a két régi útvonal a `tools/content_integrity.py:46` `LEGACY_PATHS`-ba (precedens: 2026-10-02).
- Az őr nem gyengülhet: a tiltott kifejezések, a baseline és a pin-logika változatlan.

## 3. lépés – a session (`fix(M6)`, `/course-fix`-szel)

A hivatkozások és a címek a végállapotra (a `61cc98a` sorszámai):

| Hely | Most | Változás |
|---|---|---|
| M6 hub :252 | címke: `M6.1 – „Játék-kategóriák 3 aktuális kvucára”`; cél: `./Online%20leckék/M6.1%20–%20Játék-kategóriák%203%20aktuális%20kvucára.md` | címke és link-cél: „Játékkategóriák” |
| M6 hub :254 | címke: `M6.2 – „Történet, mint tükör”`; cél: `./Online%20leckék/M6.2%20–%20Történet,%20mint%20tükör.md` | címke és link-cél: „Történet mint tükör” |
| M6 hub :79, :91 | szakaszcímek | ugyanígy |
| M6.1 :25, :1483; M6.2 :23 | a lecke saját címe, illetve a következő lecke címe | ugyanígy |
| M6.A :40, :59; M6.B :8, :9; M6.F :11, :12 (és a G3-helyek: `M6:NYELV-G3-3` (b)) | kódként idézett leckecímek | ugyanígy |
| `LMS – activity manifest.md` :87 (LMS-M6-01 „Név”) | `M6.1 – Játék-kategóriák 3 aktuális kvucára` | „Játékkategóriák” (az LMS-M6-02 „Név”-je már egyezik) |
| `Média-assetek/VOICE-PILOT-SCRIPTS.md` :135 (kánoni bemenet, nem generált) | út: `…/M6.2 – Történet, mint tükör.md`; „deklaráció: 492. sor, törzs: 493–512. sor” | új út; a sorszám a végállapotra (ma a deklaráció a 497. sor) |
| az M6.1 `@asset` specjei | „Játék-kategóriák” | build úton |

Nem nyúl: M6.1 :202 (`@source`, VO-1 — a VO fix pack hozza), `asset-migration-map.csv`, `_legacy/`, a korábbi
audit-fájlok (történeti útvonalak).

Utána, önálló hívásként:

```bash
python3 tools/test_media_manifest.py --pin-visible "M6:NYELV-G1-11, M6:IMPL-G2-5, M6:NYELV-G3-3, M6:QA-IMPL-5: az M6.1/M6.2 átnevezése, TECH-2"
```

## 4. lépés – a session (`chore(media)`)

`python3 tools/media_manifest.py build` kétszer (stabil-e), majd `check` és `reconcile`; külön commit.

## Regressziós terv (a 4. lépés után, push előtt)

1. `python3 -X pycache_prefix="${TMPDIR:-/tmp}/pyc" -m py_compile tools/*.py`
2. `python3 tools/content_integrity.py --selftest` és `python3 tools/content_integrity.py` — 0 ERROR; a kimenetben az
   M6.1 fájlszintű őre az új útvonalon fut (nem „hiányzó fájl” miatt kihagyva).
3. `python3 tools/media_manifest.py check`, `reconcile` (0 nem egyeztetett), `lint --high-only`.
4. `python3 -m unittest tools.test_media_manifest` — a pin-teszt és a baseline-teszt az új M6.2 útvonalon is zöld.
5. `git log --follow --oneline -- "02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet mint tükör.md"` — a history
   átível az átnevezésen (hasonlóság ≥ 50%).
6. Régi név nem maradhat élő hivatkozásban:
   `grep -rn -e "Játék-kategóriák 3" -e "Történet, mint tükör" "02 Tervezet" | grep -v -e _legacy -e asset-migration-map -e "@source"`
   — üres (a VO-forrás kivételével).
7. `git diff --check origin/main...HEAD` és a `/release-check` ellenőrzőlistája.
8. A PR merge módjánál a merge commit őrizze meg az átnevezés-commitot (PR #12 precedens); a merge módját a felhasználó
   választja.

## Visszalépés

Ha a 2–4. lépés előtt kiderül, hogy az átnevezés hibás, ne használj `reset`-et: `git revert <az átnevezés SHA-ja>` új
commitot hoz létre, a history nem íródik át.
