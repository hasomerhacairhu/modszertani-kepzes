# Módszertani Képzés (Madrih Képzés)

## A Projektről

Ez a repository a Hasomer Hacair ifjúsági mozgalom megújult, **blended learning** alapú madrichképzésének (ifjúsági vezetőképzés) teljes módszertani és tartalmi anyagát tartalmazza.

A program célja egy adaptív, 21. századi igényekre szabott, adatvezérelt oktatási rendszer létrehozása, amely ötvözi az online mikroleckék rugalmasságát a személyes tréningek közösségi élményével. A képzés moduláris felépítésű (M0-M7 + Zárás), és a "mastery learning" (mesterfokú tanulás) elvére épül, biztosítva, hogy minden végzett vezető magas szintű pedagógiai és vezetői kompetenciákkal rendelkezzen.

A rendszer **Open Educational Resource (OER)**, azaz nyílt oktatási segédanyag, így szabadon adaptálható más (ifjúsági) szervezetek számára is.

## Kezdő lépések (Linkek)

Ismerkedj meg a projekt alapjaival:

*   📖 **[Program Terv](./02%20Tervezet/Program%20terv.md)** – A képzés részletes pedagógiai és strukturális leírása.
*   📂 **[Modulok](./02%20Tervezet/Modulok)** – A tananyagok bontása modulonként (M0-M7).
*   📚 **[Források](./01%20Fejlesztés/00%20Források)** – A képzés kidolgozásához felhasznált szakirodalom és források.
*   📖 **[Glosszárium](./02%20Tervezet/Glosszárium%20–%20someres%20és%20pedagógiai%20fogalmak.md)** – Someres és pedagógiai fogalmak kánoni szótára.
*   ♿ **[LMS hozzáférhetőségi sztenderd](./02%20Tervezet/LMS%20–%20hozzáférhetőségi%20sztenderd.md)** – WCAG 2.2 AA követelmények a Moodle/H5P megvalósításhoz.
*   🎬 **[Média-asset regiszter](./02%20Tervezet/Média-assetek)** – A legyártandó médiaelemek (narráció, videó, illusztráció…) teljes, auditált leltára.

## Repó-struktúra

```
modszertani-kepzes/
├── README.md
├── 01 Fejlesztés/                    # A képzés kidolgozásának nyersanyagai
│   ├── 00 Források/                  #   felhasznált szakirodalom
│   ├── 01 Promptok/                  #   AI-promptok
│   ├── 02 Interjúk/                  #   felvételi interjú-jelentések
│   └── 03 Beszámolók/                #   összefoglalók
└── 02 Tervezet/                      # MAGA A TANANYAG
    ├── Program terv.md               #   a képzés pedagógiai + strukturális gerince
    ├── GLOSSZÁRIUM – ….md            #   fogalmi kánon
    ├── LMS – hozzáférhetőségi ….md   #   akadálymentességi sztenderd
    ├── _EMBERI-JÓVÁHAGYÁS-….md       #   handoff: amit embernek kell kitöltenie/jóváhagynia
    ├── _MÉDIA-ASSETEK/               #   legyártandó médiaelemek auditált regisztere (xlsx/csv/md) + build-pipeline
    └── MODULOK/                      #   M0–M7 + Z, modulonként:
        └── Mx/
            ├── Mx – ….md             #     modul-hub (áttekintő)
            ├── Mx – KAPU – ….md      #     mastery-kapu (item-bank + rubrika; ahol van)
            ├── Mx_ONLINE_LECKE/      #     online mikroleckék (Moodle/H5P)
            └── Mx_PEULA/             #     élő tréningek (peulák)
```

## Közreműködők (Contributors)

A projekt a Hasomer Hacair önkénteseinek és szakmai stábjának munkájával jött létre.

*   **Projekt Vezetés:** [Név/Szervezet]
Bedő Marci
*   **Módszertani Fejlesztés:** [Név/Csapat]
Bedő Laura
Marton Marcell
*   **Technikai Megvalósítás:** [Név/Csapat]
Bedő Marci

*Ha szeretnél hozzájárulni a fejlesztéshez, nyiss egy Issue-t, küldj egy Pull Requestet, vagy keress meg minket a [somer.hu/kapcsolat](https://somer.hu/kapcsolat) oldalon található elérhetőségek egyikén!*

## Licensz (License)

Ez a képzés a **Creative Commons Nevezd meg! 4.0 Nemzetközi Licenc (CC BY 4.0)** feltételei szerint használható fel.

Ez azt jelenti, hogy szabadon:
*   ✅ **Megoszthatod** — másolhatod és terjesztheted a képzést bármely módon vagy formátumban.
*   ✅ **Átdolgozhatod** — származékos műveket hozhatsz létre, átalakíthatod és építhetsz rá bármilyen célból (akár üzleti célra is).

Cserébe csak annyit kérünk, hogy tüntesd fel az eredeti szerzőt (Hasomer Hacair).

> **A licensz hivatalos szövege:**
> [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)

## Támogatás

Ha tetszik a munkánk, és egyetértesz a céljainkkal, kérjük, támogasd a Hasomer Hacair működését!

Minden adomány segít abban, hogy folytathassuk a progresszív, humanista nevelőmunkát és innovatív oktatási programok fejlesztését.

👉 **[Támogatom a Hasomer Hacairt](https://somer.hu/tamogatom)** (vagy hivatalos weboldal linkje)

Köszönjük! Házák VeÁmác!