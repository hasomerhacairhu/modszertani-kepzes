# Projektgazdai döntések — Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés (2026-10-10)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda 2026-10-10-i válasza, szó szerint (1. szakasz). Előzmény:
> egy külső, 2026-10-10-i véglegesítési specifikáció (helyi, nem követett referenciaanyag; privát levelezésből származó
> tényeket is tartalmaz, ezért nem kerül a repóba), és a fő munkamenet két kérdése:
>
> 1. Indulhat-e az Anna-féle szerkesztések és auditjegyzetek teljes, Git-alapú megfeleltetése a `/course-review`-n
>    kívül, mert a skill reviewerei nem látják a Git-historyt („A sáv”)?
> 2. Az M0.1 SLIDE 5 kérdésének finomítása (kíváncsiság ↔ félelem) `POST-PILOT` legyen-e, vagy freeze-kivétel?
>
> A külső specifikáció azonosítói: `CC-04` = az M0.1 SLIDE 5 kérdés-finomítása; `CC-06` = a Moodle-ben ténylegesen
> felépített tartalom és a repó-forrás összevetése. Kánoni fájl ebben a lépésben nem változott.

## 1. A projektgazda válasza, szó szerint

```text
**Döntések:**

**1. Az A sávot jóváhagyom, indíthatod.** Végezd el a teljes Anna-commit- és auditjegyzet-megfeleltetést, kizárólag olvasó Git-műveletekkel. A tananyagot ne módosítsd.

A cél nem 916 diff-hunk mechanikus felsorolása, hanem egy teljes körű, visszakövethető szakmai döntési mátrix.

Minden Anna-auditponthoz és érdemi szerkesztési egységhez rögzítsd:

- Anna eredeti módosítása vagy javaslata, pontos forrással.
- Jelenlegi állapot a main-en.
- Későbbi módosító commit, ha van.
- A módosítás dokumentált indoka, elkülönítve a saját következtetésedtől.
- Szakmai értékelés: RETAIN / VALID_IMPROVEMENT / REGRESSION / UNRESOLVED / NOT_IMPLEMENTED / NOT_APPLICABLE.
- Szükséges teendő és prioritás.
- Bizonyíték és visszakereshető hivatkozás.

A grep-alapú szövegegyezés önmagában nem elegendő. A parafrázisokat és az átnevezéseket is vizsgáld. Ahol nem található dokumentált indok, ott RATIONALE_NOT_FOUND legyen, ne találj ki utólagos magyarázatot.

Ne feltételezd, hogy egy tétel megoldatlan pusztán azért, mert a HEAD nem változott a riport óta. Minden hipotézist ellenőrizz.

A meglévő projektgazdai döntéseket tartsd tiszteletben. Az Anna-féle korábbi változatot sem szabad automatikusan jobbnak tekinteni; minden esetben szakmai indoklás szükséges.

A végleges mátrix kerüljön az auditmappába, de privát levelezési tartalom ne kerüljön a publikus repositoryba.

**2. CC-04: POST-PILOT.** Az M0+M1 freeze maradjon érvényben. Az M0.1 kérdésének finomítását a pilot visszajelzéseivel együtt kezeljük. Freeze-kivételt csak tényleges P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy a tanulói előrehaladást blokkoló hiba indokolhat.

**3. CC-06:** a Moodle összevetését most ne kezeld blokkolóként. A Moodle MCP a jóváhagyott, aktuális GitHub-forrásból fogja felépíteni a képzést. A pontos SHA, az implementált szöveg és a tényleges működés ellenőrzését külön build/runtime feladatként kezeljük. A média hiánya önmagában nem bizonyít elavult tartalmat.

**4. A B sávban** modulonként maradjon a kötelező `/course-review` folyamat. A review parancsokat külön indítom. A validált eredmények után kizárólag a ténylegesen szükséges javítások kerüljenek `/course-fix` vagy `/hungarian-edit` alá.

A külső kutatási hivatkozásokat ne kezeld automatikusan igazolt bizonyítékként. Ellenőrizd a forrás és a konkrét ajánlás kapcsolatát, különösen ott, ahol a riport pedagógiai preferenciát fogalmaz meg, nem bizonyított hibát.

**5. A végső cél:** ne egy újraírt, bonyolultabb képzés legyen, hanem a meglévő képzés legjobb, szakmailag alátámasztott változata. Kerüld a szükségtelen módosításokat, a redundanciát és az Anna-féle természetes magyar szövegezés romlását.

Indítsd most az A sávot. Az eredmény legyen teljes, auditálható, egyértelmű, és konkrét végrehajtási döntésekre alkalmas. A tananyaghoz egyelőre ne nyúlj.
```

## 2. Hatás (rögzítés, nem új döntés)

- **A sáv:** a megfeleltetési mátrix a `01 Fejlesztés/04 Audit/` alá kerül; tananyag nem változik. A mátrix
  szakmai értékelése javaslat a későbbi `/course-fix` / `/hungarian-edit` körökhöz, nem maga a javítás.
- **M0.1 SLIDE 5:** `POST-PILOT`. Az M0+M1 authoring-freeze (2026-10-05) érvényben marad; freeze-kivétel csak P0
  biztonsági, adatvédelmi, hozzáférhetőségi vagy előrehaladást blokkoló hibára.
- **Moodle-összevetés:** nem blokkoló a repó-munkában; külön build/runtime feladat (a pontos SHA, az implementált
  szöveg és a működés bizonyítéka). A média hiánya önmagában nem bizonyít elavult tartalmat (vö. PILOT-4).
- **B sáv:** modulonkénti `/course-review`, a projektgazda indítja.
- **Külső kutatási hivatkozások:** nem igazolt bizonyítékok; a forrás és a konkrét ajánlás kapcsolatát ellenőrizni
  kell, különösen pedagógiai preferenciánál.
