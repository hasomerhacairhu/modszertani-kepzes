# Projektgazdai döntés — N-M1-04, az M1.1 SLIDE 5 önreflexiója (2026-10-10)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda két 2026-10-10-i üzenetének az N-M1-04-re vonatkozó része
> szó szerint (1. szakasz), és a 2026-10-11-i `/course-fix` megbízás döntésszövege szó szerint (2. szakasz).
> Előzmény: a validált M1 `/course-review` riport (`2026-10-10 Validált findingok – M1 course-review, B sáv.md`,
> ERT-G1-1, IMPL-G1-2, BIZT-G1-3; az `audit/b-track-m0-m1-20261011` ágon, `58669c6`). A döntés 2026-10-10-én nem
> került a repóba, mert ugyanabban az üzenetben a projektgazda a tananyag-módosítást és a commitot külön engedélyhez
> kötötte (1.1); a rögzítés 2026-10-11-én, a kánoni átvezetéssel egy lépésben készült.

## 1. A projektgazda 2026-10-10-i döntése, szó szerint

### 1.1. Első üzenet (az A sáv elfogadásakor), az N-M1-04-re vonatkozó rész

```text
**N-M1-04 – projektgazdai irány:**

Az M1.1 SLIDE 5 önreflexiója maradjon opcionális, tanuló-lokális, és ne tárolódjon Moodle/H5P oldalon. Nem completion-feltétel. Ha a H5P szövegmezője vagy mentett állapota ezt nem tudja garantálni, legyen helyette saját jegyzetes, adatmentes út.

A tényleges LMS-implementáción külön ellenőrizni kell a próbálkozás-riportot, mentett állapotot és a mentori hozzáférést. A megfelelő runtime-tesztet és DPO QA-t tartsuk nyitva a bizonyíték megszületéséig.
```

Az üzenet többi pontja más tárgyú (az A sáv végrehajtási összesítője, a B sáv indítása). Az 5. pontja: „Ne módosíts
még tananyagot, és ne indíts új commitot, pusht vagy PR-t külön engedély nélkül.”

### 1.2. Második üzenet (a B sáv riportjai után), 2. pont

```text
**2. Jóváhagyom az N-M1-04 P0 adatvédelmi freeze-kivételét.**

A lezárt projektgazdai döntésem: az M1.1 SLIDE 5 személyes önreflexiója opcionális, tanuló-lokális, nem tárolódhat Moodle/H5P oldalon, és nem completion-feltétel.

Alapértelmezésben saját jegyzetes, adatmentes úton valósuljon meg. Nem tároló beviteli elem kizárólag akkor alkalmazható, ha a célkörnyezet runtime-tesztje bizonyítja az adatmentességet, beleértve a próbálkozás-riportot, a mentett állapotot és a tanári hozzáférést.

A kánoni döntést, a kapcsolódó specifikációkat és a runtime-tesztet külön `/course-fix` futásban kell javítani. A DPO QA és a tényleges runtime-bizonyíték addig nyitott marad.
```

Az üzenet 1. pontja a két riport mentéséről szól; a záró bekezdése a PED-G1-4 és a BIZT-G3-1 pilot-besorolásáról
(rögzítve a validált M1 riport fejlécében).

## 2. A `/course-fix` megbízás döntésszövege (2026-10-11), szó szerint

```text
**Lezárt döntés:**

Az M1.1 SLIDE 5 személyes önreflexiója opcionális, kizárólag tanuló-lokális, nem tárolódhat Moodle/H5P oldalon, és nem lehet completion-feltétel.

- Alapértelmezés: saját jegyzetben vagy fejben végiggondolt reflexió.
- Nem szükséges szöveget beküldeni vagy megosztani.
- Interaktív beviteli elem kizárólag igazoltan adatmentes runtime-működéssel engedélyezett.
- A próbálkozás-riport, mentett állapot és tanári/mentori hozzáférés vizsgálata kötelező.
- A DPO jóváhagyása és a Moodle runtime-ellenőrzése nyitott bizonyítékkapu marad.
```

A megbízás hatókör-pontjai közül, szó szerint:

```text
5. Őrizd meg a tanulási célt, az opcionális reflexiót, a lecke teljesítési logikáját és minden egyéb M0/M1 freeze-tartalmat.
6. A CC-04 továbbra is POST-PILOT; a CC-06 külön Moodle build/runtime feladat.
```

## 3. Hatás (rögzítés, nem új döntés)

- **Státusz:** lezárt projektgazdai döntés. A runtime-bizonyíték (RT-P0-24 az LMS-M1-01-re: próbálkozás-riport,
  mentett állapot, tanári és mentori hozzáférés) és a DPO QA nyitott bizonyíték-kapu (`RELEASE-READINESS.md` G2,
  G3b); ez a jegyzőkönyv egyiket sem állítja teljesültnek.
- **Freeze-kivétel:** P0 adatvédelmi; az M0+M1 authoring-freeze alatt csak az N-M1-04 kánoni átvezetése engedélyezett
  (1.2), más M0/M1 tartalom nem változik.
- **Átvezetés:** `Emberi jóváhagyás szükséges.md` 12. szakasz; az M1.1 3. szakaszának runtime-követelménye és a
  SLIDE 5 („Mit látunk?”, „H5P-beállítás”, az M1.1-IKO-02 `notes` mezője); az `LMS – activity manifest.md` LMS-M1-01
  sora és a BSPEC-02 datált kiegészítése (az állapot `BUILD_SPEC_RESOLVED` marad); az `LMS – H5P runtime acceptance.md`
  24. pontja (az RT-P0-24 állapota `IMPLEMENTATION_TEST_REQUIRED` marad).
- **Változatlan:** a mikrocél, a három kérdés és a dia tanulói szövege, az M1.1-NAR-05 narráció, a lecke completionje
  (az 5. dia írása nem feltétel), a kvízkérdések és kulcsaik.
- **Pilot-üzemeltetés:** amíg az RT-P0-24 nem igazol adatmentes beviteli elemet, az M1.1 SLIDE 5 beviteli elem
  nélkül, a saját jegyzetes úton nyílik meg (ERT-G1-1 (a)).
- **Tanulói mondat:** „nem tároljuk” típusú mondat csak az RT-P0-24 sikeres visszaolvasása után kerülhet a leckébe
  (runtime acceptance 24. pont, utolsó mondat); a mező előtti tájékoztató kérdése nyitott emberi döntés (BIZT-G1-4).
- **Nem e döntés tárgya:** a CC-04 (POST-PILOT) és a CC-06 (külön Moodle build/runtime feladat) változatlan; HUM-fájlba
  való átvezetésük külön tétel (M0 ERT-8). Az Anna-megfeleltetési mátrix N-M1-04 sorai audit trail: nem írjuk át.
