# Projektgazdai felhatalmazás — next-version M0–Z autopilot (2026-10-11)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda 2026-10-11-i indító üzenete, szó szerint (1. szakasz). Ez az
> `AP-2026-10-11-01` autopilot-futás felhatalmazása (`next-version` változat); a futás állapota az
> `AUTOPILOT-LEDGER.md`. Kánoni fájl ebben a lépésben nem változott.

## 1. A projektgazda üzenete, szó szerint

```text
**PROJEKTGAZDAI FELHATALMAZÁS — TELJES M0–Z KÉPZÉSVÉGLEGESÍTÉS**

„Projektgazdaként kifejezetten engedélyezem a módszertani képzés következő verziójának teljes M0–M7 + Z felülvizsgálatát, valamennyi validált objektív hiba javítását, beleértve a korábban POST-PILOT besorolású M0/M1 javításokat is, külön next-version munkaágon, a jelenlegi pilot változatának módosítása nélkül. Engedélyezem a szükséges rutinmódosításokat, ellenőrzéseket, generált médiakimenetek frissítését és helyi checkpoint-commitokat. Új szakpolitikai, gyermekvédelmi, adatvédelmi vagy értékelési döntést nem hozhatsz helyettem.”

**Futtasd a `/course-autopilot M0-Z --next-version` teljes munkafolyamatot mind az öt szakmai lencsével.**

A cél nem egy újabb auditriport, hanem a teljes, javított és ellenőrzött képzési anyag.

A PREFLIGHT során ellenőrizd, hogy a #26, #27, #28 és #29 PR-ek már a mainbe kerültek. A ledger X-1, X-2 és X-3 előfeltételeit a tényleges Git history és fájlok alapján vizsgáld felül; az igazoltan teljesült előfeltételeket jelöld RESOLVED-nak. Ne kérj új jóváhagyást már teljesült feltételhez.

Használd fel Anna teljes auditját, az M0/M1 validált Track B riportokat, az N-M1-04 lezárt javítását, valamennyi korábbi projektgazdai döntést és az aktuális tananyag-kánont. A már ellenőrzött, változatlan tartalmat ne auditáld újra. Az M0/M1 hiányzó nyelvi lencséjét pótold, majd végezd el a fennmaradó M2–Z felülvizsgálatokat az öt lencsével.

Minden validált objektív hibát ténylegesen javíts ki. A javítás után végezz célzott QA-t, a bizonyított regressziókat javítsd, majd folytasd a következő tétellel. Ne indíts újabb teljes auditot minden módosítás után.

A `--next-version` módot valóban alkalmazd: a POST-PILOT címke és a jelenlegi pilot-freeze önmagában nem lehet oka egy validált objektív javítás elhalasztásának ezen a külön munkaágon.

Tartsd meg a gyermekvédelmi, adatvédelmi, pedagógiai és assessment-invariánsokat. A valódi DPO-, szakértői és Moodle-runtime bizonyítékokat ne találd ki. Az ilyen tételeket dokumentáld, de folytasd a független javításokat.

Minden modul után rögzítsd a findingok állapotát a tartós AUTOPILOT-LEDGER-ben, ellenőrizd a módosított fájlokat, és készíts szükség szerint helyi checkpoint-commitot. A generált médiát csak a jóváhagyott build-folyamat módosíthatja.

A végén legyen teljes keresztmodulos konzisztenciaellenőrzés, független `/release-check`, content-integrity, média-regresszió, diff-visszaolvasás és pontos összesítés.

**Folyamatos végrehajtás:** ne állj meg egy modul, egy review vagy egy fix pack után. Ha egy finding külső döntést igényel, rögzítsd és dolgozz tovább. Megszakítás vagy context-compaction után a ledger `next` művelete alapján folytasd, az elkészült munkát ne ismételd.

**Befejezési feltétel:** a `python3 tools/autopilot_ledger.py check` adjon `AUTOPILOT-LEDGER: TERMINAL` eredményt 0-s kilépési kóddal; a jelentés külön idézze az `AUTOPILOT-RESULT` értékét, valamennyi nyitott vagy halasztott tételt, a release-check két verdiktjét és a teszteredményeket. A munkafa legyen tiszta. A TERMINAL önmagában nem jelentheti azt, hogy minden hiba ki lett javítva.

Ha az adott művelet háromszor egymás után ugyanazzal a tényleges technikai hibával elbukik, dokumentáld a hibát és az elvégzett munkát; ne próbálj jogosultsági korlátot megkerülni. Legfeljebb 200 végrehajtási kör.

Nincs push, PR, merge, governance-módosítás, éles Moodle-telepítés vagy tanulói release ebben a futásban.

**A feladatot hajtsd végre autonóm módon. Ne kérj rutinjóváhagyásokat, és ne állj meg egy újabb terv elkészítésénél.**
```

## 2. Hatás (rögzítés, nem új döntés)

- **Változat:** `next-version`, munkaág `next-version/AP-2026-10-11-01` a `main@213a4c5`-ről. A futó M0+M1 pilot
  forrása (a `main`) nem változik; az ág a pilot-vonalba csak a projektgazda külön döntésével kerülhet (VÉDETT).
- **A pilot-freeze (2026-10-05) és a `POST-PILOT` címke** ezen az ágon nem halasztási ok: a validált objektív
  M0/M1-findingok javíthatók. Más lezárt projektgazdai döntés (pl. N-M1-04, HUM-szakaszok, D-a…D-j) érvényes, nem
  nyílik újra.
- **Nem engedélyezett:** új szakpolitikai, gyermekvédelmi, adatvédelmi vagy értékelési döntés (ezek `BLOCKED_HUMAN`);
  DPO-, szakértői és Moodle-runtime bizonyíték kitalálása (`EVIDENCE_GATE`); push, PR, merge, governance-módosítás,
  éles Moodle-telepítés, tanulói release.
- **PREFLIGHT-ellenőrzés (git):** a #26 (`d48bc2a`), #27 (`49ff184`), #28 (`0c7e299`) és #29 (`213a4c5`) merge-commit a
  `main` történetében van; az `origin/fix/m1-privacy-learner-local` (`6dde193`), az `origin/gov/claude-harness-v2`
  (`ffee45e`) és az `origin/audit/anna-traceability-20261010` (`695e5e4`) a `main` őse.
