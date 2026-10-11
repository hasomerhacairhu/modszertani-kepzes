# AUTOPILOT-LEDGER — formátum és állapotgép

A ledger (`01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md`) egy autopilot-futás **egyetlen** tartós
állapota. Egyetlen író van: a fő session, `Edit` eszközzel (a Bash a repóba nem ír). A subagentek
nem írják. A szerkezetet és a végállapotot a `python3 tools/autopilot_ledger.py` ellenőrzi
(`validate` · `check` · `next`); a ledger nem bizonyíték, csak sorrend és hivatkozás: minden
állapotot a fájlban vagy parancskimenetben bizonyítasz, mielőtt beírod.

Cellában `|` csak `\|` alakban állhat. Üres érték: `—`.

## Futás — `| Kulcs | Érték |`

Kötelező kulcsok: `Run-ID` (`AP-<ÉÉÉÉ-HH-NN>-<nn>`), `Állapot` (`NONE` · `ACTIVE` · `FINISHED`),
`Scope`, `Lencsék`, `Felhatalmazás` (pl. `fix: igen; commit: helyi munkaágon; push/PR: nem`),
`Munkaág`, `Bázis-commit`, `Indítva`, `Záró QA`. További kulcs megengedett (pl. `Korlátok`).

`Záró QA` = a záró `/release-check` alatti commit és a két verdikt-sor szó szerint:
`` `<sha>` · content_integrity: 0 ERROR · MOODLE-BUILD-VERDICT: … · LEARNER-RELEASE-VERDICT: … ``.

## Modulok — `| Modul | Review | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |`

| Mező | Nyitott | Lezárt |
|---|---|---|
| Review | `PENDING` · `REVIEWING` · `RAW_SAVED` | `VERIFIED` · `REUSED` · `SKIPPED` |
| Javítás | `PENDING` · `FIXING` | `DONE` · `NONE_NEEDED` · `NOT_AUTHORIZED` |

- `VERIFIED` / `REUSED`: a `Riport` egy létező `04 Audit` fájlnév backtickben, a `Review-bázis` a
  review alatti commit. `SKIPPED`: indoklás a `Következő lépés`-ben.
- `DONE`: a `Bizonyíték` megnevezi a javító commitot és a célzott ellenőrzés eredményét.
  `NONE_NEEDED` / `NOT_AUTHORIZED`: a `Bizonyíték` az indoklás.
- `Következő lépés`: a pontos folytatás (pl. `verifier 2/3: M3:IMPL-4…M3:IMPL-9`), lezárt modulnál `—`.

## Külső kapuk — `| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |`

Típus: `PRECONDITION` (a futást blokkolja) · `HUMAN_DECISION` · `EVIDENCE_GATE` · `RUNTIME` ·
`SIGNOFF`; állapot: `OPEN` · `RESOLVED`. Kulcs: `X-<n>`. Nyitott `PRECONDITION` mellett a futás nem
`ACTIVE`; a többi típus nyitva maradhat — ez a futás emberi kimenete, nem hiba.

## Findingok — `| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |`

Kulcs: `<Modul>:<riport-ID>` (pl. `M1:ERT-G1-1`), a modul szerepel a Modulok táblában. Súly `P0`–`P2`
(`P3` csak egy régebbi riportból átvett tételnél);
Típus `objektív` · `emberi-döntés` · `bizonyíték-kapu`; Verdikt `MEGERŐSÍTVE` · `ELVETVE` ·
`EMBERI DÖNTÉS` · `—` (még nincs).

| Állapot | Mikor | A bizonyíték-mező |
|---|---|---|
| `OPEN` · `IN_PROGRESS` | javításra vár / folyamatban | — |
| `NEEDS_RECHECK` | a fájl a review óta változott, vagy a javítás előtti bizonyítás nem egyezett | mi tért el |
| `FIXED` | csak `MEGERŐSÍTVE` + `objektív`; a javítás a fájlban bizonyítva | commit + `fájl:sor` |
| `ALREADY_FIXED` | a hiba már nincs meg, a javított állapot igen | commit, ahol így áll |
| `REJECTED` | `ELVETVE` (a verifier vagy egy recheck) | az elvetés oka |
| `DUPLICATE` | a verifier összevonta | `= <megtartott kulcs>` |
| `BLOCKED_HUMAN` | új emberi döntés kell; nem implementálod | `EMBERI DÖNTÉS: <mit, kitől, milyen bizonyítékkal>` |
| `EVIDENCE_GATE` | `bizonyíték-kapu`: szerepköri vagy runtime-bizonyíték hiányzik | szerep, G-kapu |
| `OWNER_DEFERRED` | lezárt projektgazdai döntés halasztja (pl. freeze → POST-PILOT) | a döntés helye |
| `NOT_AUTHORIZED` | a futás nem kapott javítási felhatalmazást | a Felhatalmazás sor |

Egy `NEEDS_RECHECK` egyszer kap célzott újraellenőrzést (a lencse-reviewer a jelenlegi szövegre);
utána `OPEN` (új bizonyítékkal) vagy `REJECTED` — nem kering.

## Végállapot (`check` → `AUTOPILOT-LEDGER: TERMINAL`, kilépési kód 0)

`Állapot: FINISHED`; minden modul Review- és Javítás-állapota lezárt, a szükséges riporttal és
commit-tal; nincs nyitott `PRECONDITION`; minden finding lezárt, a fenti bizonyíték-szabállyal; a
`Záró QA` commitja létezik, azóta a `02 Tervezet/` és a `tools/` nem változott, nincs alatta nem
követett fájl, és a `content_integrity.py` 0-val lép ki. A `next` a következő folytatható lépést
írja ki (`AUTOPILOT-NEXT: …`).

## Napló — szabad formájú, nem ellenőrzött

`| Idő | Fázis | Esemény |` — checkpointok (commitok, riportok, QA-futások), egy sor eseményenként.
