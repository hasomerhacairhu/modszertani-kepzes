# Módszertani madrichképzés

A Hasomer Hacair magyarországi módszertani madrichképzésének **fejlesztési és implementációs specifikációja**.

> **Release-státusz:** a repository tartalma jelenleg **nem tekinthető éles, jóváhagyott Moodle-kurzusnak**. A tananyag pedagógiai váza fejlett, de a `02 Tervezet/RELEASE-READINESS.md` dokumentumban felsorolt gyermekvédelmi, adatvédelmi, szervezeti és LMS/H5P kapuk lezárása szükséges az élesítéshez.

## Repository-térkép

```text
.
├── 01 Fejlesztés/
│   ├── 00 Források/          # kutatási és háttéranyagok
│   ├── 01 Promptok/          # fejlesztési promptok
│   ├── 02 Interjúk/          # intake / szükségletfelmérés
│   ├── 03 Beszámolók/        # összefoglalók
│   └── 04 Audit/             # auditnaplók, release-audit, rubrika
├── 02 Tervezet/
│   ├── Modulok/
│   │   ├── M0/ … M7/
│   │   │   ├── Online leckék/
│   │   │   └── Peulák/
│   │   └── Z/
│   ├── Média-assetek/        # média-regiszter és build-eszközök
│   ├── Program terv.md
│   ├── Glosszárium – someres és pedagógiai fogalmak.md
│   ├── Emberi jóváhagyás szükséges.md
│   ├── LMS – hozzáférhetőségi sztenderd.md
│   ├── LMS – activity manifest.md
│   ├── LMS – H5P runtime acceptance.md
│   ├── Adatvédelem – tanulói adatok és AI.md
│   ├── Gyermekvédelem – release gate.md
│   ├── Terepgyakorlat – 2. félév.md
│   └── RELEASE-READINESS.md
├── tools/
│   └── content_integrity.py  # statikus tartalmi integritás-ellenőrzés
└── .github/workflows/
    └── content-integrity.yml # CI
```

## Kánoni források és sorrend

1. `02 Tervezet/Program terv.md` – program-architektúra.
2. `02 Tervezet/Modulok/` – modul-, lecke-, peula- és kapuspecifikációk.
3. `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md` – terminológiai referencia **a nyitott helyi terminológiai döntés figyelembevételével**.
4. `02 Tervezet/Emberi jóváhagyás szükséges.md` és a release-gate dokumentumok – olyan pontok, amelyeknél emberi/szakértői döntést tilos automatizálással helyettesíteni.
5. `01 Fejlesztés/04 Audit/` – audit trail, nem tanulói tartalom.

## Fejlesztési szabály

A tananyagon végzett módosításnál:

- a pedagógiai célt, értékelést és kapulogikát együtt kell ellenőrizni;
- gyermekvédelmi, jogi, adatvédelmi vagy helyi mozgalmi döntést nem szabad feltételezni;
- új vagy módosított H5P-funkció csak a cél Moodle/H5P verzión lefuttatott acceptance test után tekinthető támogatottnak;
- a tanulói felületen nem maradhat megoldatlan `KITÖLTENDŐ` mező;
- helyi link, duplikált kánoni fájl, tiltott release-állítás és ismert veszélyes regresszió ellen CI fut.

## Release-folyamat

A merge önmagában nem jelent élesíthetőséget. A kötelező kapuk és bizonyítékok a [RELEASE-READINESS](./02%20Tervezet/RELEASE-READINESS.md) dokumentumban vannak. A Moodle-implementáció után külön mobil, billentyűzetes, képernyőolvasós és H5P runtime teszt szükséges.

## Licenc

Eltérő jelzés hiányában a repository saját szöveges tananyaga **Creative Commons Attribution 4.0 International (CC BY 4.0)** alatt használható. Harmadik féltől származó idézetekre, képekre, videókra és egyéb assetekre a saját forrás/licenc feltételei vonatkoznak. Lásd: `LICENSE`.
