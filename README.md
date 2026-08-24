# Módszertani Képzés (Madrichképzés)

## A projektről

Ez a repository a Hasomer Hacair ifjúsági mozgalom megújult, **blended learning** alapú madrichképzésének (ifjúsági vezetőképzés) teljes módszertani és tartalmi **fejlesztési és implementációs specifikációja**.

A program célja egy adaptív, 21. századi igényekre szabott, adatvezérelt oktatási rendszer, amely ötvözi az online mikroleckék rugalmasságát a személyes tréningek (peulák) közösségi élményével. A képzés moduláris felépítésű (M0–M7 + Zárás), és a **mastery learning** elvére épül.

A rendszer **Open Educational Resource (OER)**, azaz nyílt oktatási segédanyag, így szabadon adaptálható más (ifjúsági) szervezetek számára is.

> **Release-státusz:** a repository tartalma jelenleg **nem tekinthető éles, jóváhagyott Moodle-kurzusnak**. A tananyag pedagógiai váza fejlett, de a [`RELEASE-READINESS.md`](./02%20Tervezet/RELEASE-READINESS.md) dokumentumban felsorolt gyermekvédelmi, adatvédelmi, szervezeti és LMS/H5P kapuk lezárása szükséges az élesítéshez.

## Kezdő lépések (linkek)

* 📖 **[Program terv](./02%20Tervezet/Program%20terv.md)** – a képzés részletes pedagógiai és strukturális leírása.
* 📂 **[Modulok](./02%20Tervezet/Modulok)** – a tananyagok bontása modulonként (M0–M7 + Z).
* 📚 **[Források](./01%20Fejlesztés/00%20Források)** – a kidolgozáshoz felhasznált szakirodalom.
* 📖 **[Glosszárium](./02%20Tervezet/Glosszárium%20–%20someres%20és%20pedagógiai%20fogalmak.md)** – someres és pedagógiai fogalmak kánoni szótára.
* ♿ **[LMS hozzáférhetőségi sztenderd](./02%20Tervezet/LMS%20–%20hozzáférhetőségi%20sztenderd.md)** – WCAG 2.2 AA követelmények a Moodle/H5P megvalósításhoz.
* 🎬 **[Média-asset regiszter](./02%20Tervezet/Média-assetek)** – a legyártandó médiaelemek auditált leltára.
* 🚦 **[Release readiness](./02%20Tervezet/RELEASE-READINESS.md)** – a kötelező Go / No-Go kapuk.

## Repository-térkép

```text
.
├── 01 Fejlesztés/
│   ├── 00 Források/          # kutatási és háttéranyagok
│   ├── 01 Promptok/          # fejlesztési promptok
│   ├── 02 Interjúk/          # intake / szükségletfelmérés
│   ├── 03 Beszámolók/        # összefoglalók
│   └── 04 Audit/             # auditnaplók, release-audit, deep-audit rubrika
├── 02 Tervezet/              # MAGA A TANANYAG
│   ├── Modulok/
│   │   ├── M0/ … M7/ és Z/
│   │   │   ├── Mx – ….md              # modul-hub (áttekintő)
│   │   │   ├── Mx – Kapu – ….md       # mastery-kapu (item-bank + rubrika; ahol van)
│   │   │   ├── Online leckék/         # Moodle/H5P mikroleckék
│   │   │   └── Peulák/                # élő tréningek (A, B és F = Study Lab)
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
- helyi link, duplikált kánoni fájl, tiltott release-állítás és ismert veszélyes regresszió ellen CI fut (`tools/content_integrity.py`).

## Release-folyamat

A merge önmagában nem jelent élesíthetőséget. A kötelező kapuk és bizonyítékok a [RELEASE-READINESS](./02%20Tervezet/RELEASE-READINESS.md) dokumentumban vannak. A Moodle-implementáció után külön mobil, billentyűzetes, képernyőolvasós és H5P runtime teszt szükséges.

## Közreműködők (Contributors)

A projekt a Hasomer Hacair önkénteseinek és szakmai stábjának munkájával jött létre.

* **Projektvezetés:** Bedő Marci
* **Módszertani fejlesztés:** Bedő Laura, Marton Marcell, Rácz Eszter, Weinberger Anna
* **Technikai megvalósítás:** Bedő Marci

*Ha szeretnél hozzájárulni a fejlesztéshez, nyiss egy Issue-t, küldj egy Pull Requestet, vagy keress meg minket a [somer.hu/kapcsolat](https://somer.hu/kapcsolat) oldalon található elérhetőségek egyikén!*

## Licenc

Ez a képzés a **Creative Commons Nevezd meg! 4.0 Nemzetközi Licenc (CC BY 4.0)** feltételei szerint használható fel.

Ez azt jelenti, hogy szabadon:

* ✅ **Megoszthatod** — másolhatod és terjesztheted a képzést bármely módon vagy formátumban.
* ✅ **Átdolgozhatod** — származékos műveket hozhatsz létre, átalakíthatod és építhetsz rá bármilyen célból (akár üzleti célra is).

Cserébe csak annyit kérünk, hogy tüntesd fel az eredeti szerzőt (Hasomer Hacair).

Harmadik féltől származó idézetekre, képekre, videókra és egyéb assetekre a saját forrás/licenc feltételei vonatkoznak. A licenc teljes szövege: [`LICENSE`](./LICENSE) és [creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0/).

## Támogatás

Ha tetszik a munkánk, és egyetértesz a céljainkkal, kérjük, támogasd a Hasomer Hacair működését!

Minden adomány segít abban, hogy folytathassuk a progresszív, humanista nevelőmunkát és innovatív oktatási programok fejlesztését.

👉 **[Támogatom a Hasomer Hacairt](https://somer.hu/tamogatom)**

Köszönjük! Házák VeÁmác!
