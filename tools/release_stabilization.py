#!/usr/bin/env python3
"""One-time, deterministic release-stabilization pass.

This script intentionally fixes only findings that are objectively verifiable from
repository state or authoritative external sources. Organisation-specific policy,
child-protection approval, privacy/legal sign-off, current local terminology and
LMS runtime facts remain explicit release gates instead of being invented here.

Run from repository root. It is idempotent where practical and fails loudly when
an expected high-risk source pattern has unexpectedly changed.
"""
from __future__ import annotations

from pathlib import Path
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]


def p(rel: str) -> Path:
    return ROOT / rel


def read(rel: str) -> str:
    return p(rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    path = p(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace(rel: str, old: str, new: str, *, required: bool = False) -> None:
    text = read(rel)
    if old not in text:
        if required:
            raise RuntimeError(f"Expected pattern not found in {rel}: {old[:120]!r}")
        return
    write(rel, text.replace(old, new))


def replace_re(rel: str, pattern: str, repl: str, *, count: int = 0, required: bool = False, flags: int = 0) -> None:
    text = read(rel)
    new, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n == 0 and required:
        raise RuntimeError(f"Expected regex not found in {rel}: {pattern!r}")
    if n:
        write(rel, new)


def append_once(rel: str, marker: str, addition: str) -> None:
    text = read(rel)
    if marker in text:
        return
    write(rel, text + "\n\n" + addition.strip() + "\n")


# ---------------------------------------------------------------------------
# README + licensing: make repository topology and release state truthful.
# ---------------------------------------------------------------------------
write("README.md", r'''# Módszertani madrichképzés

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
''')

write("LICENSE", r'''Creative Commons Attribution 4.0 International (CC BY 4.0)

Except where otherwise noted, the original textual training materials in this
repository are licensed under the Creative Commons Attribution 4.0 International
License.

You are free to share and adapt the material for any purpose, including
commercially, provided that appropriate credit is given, a link to the license is
provided, and changes are indicated. You may not apply legal terms or technological
measures that legally restrict others from doing anything the license permits.

Full legal code:
https://creativecommons.org/licenses/by/4.0/legalcode

Third-party quotations, images, video, audio, fonts, trademarks and other assets
are not relicensed by this notice unless explicitly stated.
''')


# ---------------------------------------------------------------------------
# M1: objective text, link integrity, grammar and confidentiality boundary.
# ---------------------------------------------------------------------------
M1 = "02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, feedback – Önismeret & visszajelzés – Johari + SBI.md"
replace(M1,
        "– **Megkülönbözteti** a **konkrét megfigyelést** („háromszor közbevágott”) a **címkézéstől / értelmezéstől** („tiszteletlen voltál”) – **legalább 4/5 tételben helyesen besorolja, és **címkéből megfigyelést ír át**.",
        "– **Megkülönbözteti** a **konkrét megfigyelést** („háromszor közbevágott”) a **címkézéstől / értelmezéstől** („tiszteletlen voltál”) – **legalább 4/5 tételben helyesen besorolja**, és **címkéből megfigyelést ír át**.")
replace(M1, "amikor visszajelzést kapsz", "amikor visszajelzést kap")
replace(M1, "SBI-vázatot", "SBI-vázlatot")
replace(M1,
        "[M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’)](M1.B%20–%20SBI-lab%20–%20Smiley-tól%20a%20használható%20visszajelzésig%20(45’).md)",
        "[M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’)](./Peulák/M1.B%20–%20SBI-lab%20–%20Smiley-tól%20a%20használható%20visszajelzésig%20%2845’%29.md)")
replace(M1, "Amennyiben eléri a minimumot, ezesetben is kap feedbacket, érdemes hangúlyozni", "Amennyiben eléri a minimumot, ebben az esetben is kap feedbacket; érdemes hangsúlyozni")
replace(M1, "Rubrika-szintek eloszlása a három fő sorban (S, B, I);", "Rubrika-szintek eloszlása mind a négy sorban (S, B, I, hangnem);")

M1A = "02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md"
replace(M1A,
        "> Figyeljetek arra, hogy amit a másik mond,\n> azt **nem adjátok tovább** a csoporton kívül,\n> csak ha ő maga akarja.”",
        "> Figyeljetek arra, hogy amit a másik mond, azt **nem visszük tovább pletykaként vagy engedély nélkül**. Egy fontos kivétel van: ha valaki veszélyben lehet, vagy gyermekvédelmi aggály merül fel, **nem ígérünk teljes titoktartást**, hanem a lehető legszűkebb körben bevonjuk a kijelölt felelős felnőttet / gyermekvédelmi felelőst.”")
replace(M1A,
        "> „Nem kötelező cetlit kitenni. Ha valaki úgy érzi, hogy ez most túl sok, nyugodtan megtarthatja magának.”",
        "> „Nem kötelező cetlit kitenni. A közös táblára **csak olyan tartalom kerüljön, amit szívesen teszel láthatóvá a teljes csoportnak**. A Rejtett mező megértéséhez használhatsz fiktív vagy általános példát is; érzékeny magáninformáció megosztása nem feladat.”")


# ---------------------------------------------------------------------------
# M3 hub: numbering, links and legally cautious safeguarding wording.
# ---------------------------------------------------------------------------
M3 = "02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md"
replace(M3, "\n1. **Gyermekvédelem & red flag-ek**", "\n3. **Gyermekvédelem & red flag-ek**")
replace(M3,
        "[M3.3 – „Gyermekvédelem 101” – red flag felismerése & első lépések](M3.3%20–%20Gyermekvédelem%20101%20–%20red%20flag%20felismerése%20&%20első%20lépések.md)",
        "[M3.3 – „Gyermekvédelem 101” – red flag felismerése & első lépések](./Online%20leckék/M3.3%20–%20Gyermekvédelem%20101%20–%20red%20flag%20felismerése%20&%20első%20lépések.md)")
replace(M3,
        "[M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab)](M3.F%20–%20Felzárkóztató%20peula%20–%20Kvucadinamika%20&%20gyermekvédelem%20(Study%20Lab).md)",
        "[M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab)](./Peulák/M3.F%20–%20Felzárkóztató%20peula%20–%20Kvucadinamika%20&%20gyermekvédelem%20%28Study%20Lab%29.md)")

legal_pattern = re.compile(r"> ⚖️ \*\*Jó tudni – a jelzés Magyarországon törvényi kötelezettség\.\*\*.*?\n> \*\(Forrás:.*?\)\*", re.S)
legal_repl = r'''> ⚖️ **Jó tudni – a jelzés Magyarországon szabályozott, de a szerepeket pontosan kell szétválasztani.**
> A Gyvt. 17. § a gyermekvédelmi jelzőrendszer résztvevői között szervezeteket és személyeket is nevesít, és veszélyeztetettség esetén jelzési / kezdeményezési kötelezettséget ír elő. A kiemelt veszélyeztető okokra vonatkozó hatályos szabályoknál a haladéktalan, legkésőbb három munkanapon belüli továbblépésnek büntetőjogi relevanciája is lehet. **Ebből azonban nem következik, hogy egy 15–17 éves önkéntes madrichnak önálló jogi minősítést vagy hatósági eljárást kellene végeznie.**
> A képzésben alkalmazandó operatív szabály ezért: **észlelj → ne nyomozz → ne ígérj teljes titoktartást → azonnal vond be a kijelölt felelős felnőttet / gyermekvédelmi felelőst → akut veszélynél a szervezeti protokoll szerint sürgősségi segítség.** A pontos helyi láncot, a felelős nevét és azt, hogy az adott szervezeti jogállás mellett ki tesz külső jelzést, a gyermekvédelmi felelősnek és szükség esetén jogi szakértőnek kell jóváhagynia az élesítés előtt.
> *(Elsődleges jogforrás: 1997. évi XXXI. törvény 17. §, Nemzeti Jogszabálytár; kapcsolódó hatályos büntetőjogi szabály: Btk. 209/A. §. A tananyag nem helyettesíti a szervezet aktuális gyermekvédelmi protokollját.)*'''
text = read(M3)
new, n = legal_pattern.subn(legal_repl, text, count=1)
if n != 1:
    raise RuntimeError("M3 legal block could not be replaced exactly once")
write(M3, new)


# ---------------------------------------------------------------------------
# M3.2 developmental science: remove deterministic age/brain claims.
# ---------------------------------------------------------------------------
M32 = "02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md"
anchor = "**Flow:** Hook → Input 1 (miért nem egyforma kvucák) → Input 2 (4 profil) → Activity (Matching) → Reflexió → Check + Outro"
replace(M32, anchor, anchor + r'''

> 🧠 **Fejlődéslélektani keret:** az alábbi korosztály-profilok **tervezési heurisztikák, nem diagnózisok**. Az életkor önmagában nem mondja meg egy gyerek figyelmét, absztrakciós képességét, érzelmi szabályozását vagy társas viselkedését. Egyéni fejlődés, neurodiverzitás, aktuális állapot, kultúra, csoporthelyzet és a feladat relevanciája erősen módosítja, mi működik. Madrichként **megfigyeled a konkrét kvucát, és ahhoz igazítasz**, nem életkor alapján címkézel.''')
replace(M32, "**Figyelem/koncentráció:** rövid, kb. pár perces fókusz – sűrűn váltogasd a tempót és a formát.", "**Figyelem/koncentráció:** gyakran segít a rövid, világos instrukció, a mozgás és a tempóváltás; a tényleges fókusz hossza gyerekenként, témánként és helyzetenként nagyon eltér.")
replace(M32, "**Gondolkodás:** konkrét, „itt és most” – kézzelfogható, látható dolgokon keresztül ért, az absztrakt „mi lenne, ha…” még nehéz neki.", "**Gondolkodás:** a kézzelfogható példa, történet és cselekvés általában jó kapaszkodó; az elvont kérdéseket is lehet használni, ha érthető kontextust és támogatást kapnak.")
replace(M32, "**Mozgásigény:** nagyon magas – ülni nehéz neki, a mozgás nem rosszaság, hanem szükséglet.", "**Mozgás:** sok gyereknek segít, ha nem kizárólag hosszan ülő formát kap; a mozgást kezelheted tanulási erőforrásként, de ne feltételezd, hogy mindenkinél ugyanaz az igény.")
replace(M32, "**Kortárs-orientáció:** itt kezd a csoport fontosabb lenni a felnőttnél – a „mit szólnak a többiek” sokszor erősebb, mint a te instrukciód.", "**Kortárs-orientáció:** a kortársak véleménye sokaknál egyre fontosabbá válik; ez nem mindenkinél azonos erősségű, ezért figyeld a tényleges csoportdinamikát.")
replace(M32, "**Gondolkodás:** elkezd nyílni az absztrakció (bír már egy-egy „mi lenne ha?” típusú kérdést), de még ingadozó – konkrét példa nélkül könnyen elveszik.", "**Gondolkodás:** egyre több elvont és hipotetikus kérdés működhet, de konkrét példák továbbra is jó támaszt adnak, különösen új vagy összetett témánál.")
replace(M32, "**Érzelmi szabályozás:** hullámzó – gyorsan lelkesedik és gyorsan megsértődik; a beégés/szégyen érzése nagyon éles.", "**Érzelmi és társas érzékenység:** a státusz, beégés és elfogadás sok résztvevőnél erős szempont lehet; kerüld a nyilvános megszégyenítést, és figyeld az egyéni reakciókat.")
replace(M32, "**Absztrakció:** már jól bírja az elvont témákat (igazság, hűség, „milyen ember akarok lenni”) – ezekkel meg lehet fogni.", "**Absztrakció:** sok résztvevővel már jól lehet elvont témákról, identitásról és értékekről dolgozni, de a bevonódás és a készség egyénileg változik.")
replace(M32, "**Érzelmi szabályozás:** intenzív és hullámzó – az érzelmi „gáz” (amygdala) hamar beindul, a „fék” (érlelődő prefrontális kéreg) még lassan kapcsol, ezért a kis dolgokból is nagy dráma lehet.", "**Érzelmi szabályozás:** serdülőkorban az érzelmi, társas és végrehajtó rendszerek tovább fejlődnek, nagy egyéni és helyzeti változatossággal. Ne használd az „érzelmi agy vs. éretlen fék” leegyszerűsítést magyarázatként; inkább adj időt a megnyugvásra, perspektívaváltásra és közös reflektálásra.")
replace(M32, "**Kortárs-orientáció:** csúcson – a kortársak véleménye és a „hova tartozom” érzése sokszor erősebb, mint bármilyen felnőtt szempont.", "**Kortárs-orientáció:** a kortárs kapcsolatok és a valahová tartozás sokaknál különösen fontossá válhat; ezt használd csoportépítésre, de ne kezeld univerzális szabályként.")
replace(M32, "**Absztrakció & reflexió:** kiforrott elvont gondolkodás – nemcsak témákról vitatkozik, hanem a saját gondolkodására is rá tud nézni („miért gondolom ezt?”).", "**Absztrakció & reflexió:** sok idősebb résztvevő hosszabb vitát és metareflexiót is jól bír; a képesség, motiváció és tapasztalat azonban itt is egyénileg eltér.")
replace(M32, "**Érzelmi szabályozás:** érettebb, stabilabb a fiatalabbaknál – jobban bírja a nézetkülönbséget anélkül, hogy szétesne (de a teljes érés még a 20-as évek közepéig tart).", "**Érzelmi szabályozás:** gyakran több tapasztalatuk van a nézetkülönbség és önálló döntések kezelésében, de ebből nem következik automatikus „érettség”; helyzet, személy és csoportkultúra továbbra is számít.")


# ---------------------------------------------------------------------------
# M3.B: remove learner enactment of high-risk safeguarding scenarios.
# ---------------------------------------------------------------------------
M3B = "02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md"
replace(M3B, "# M3.B – Red flag vagy nem? – Miniszínház & lépés-térkép", "# M3.B – Red flag vagy nem? – Esetelemzés & lépés-térkép")
replace(M3B, "**Cím (kvucának):** Red flag vagy nem? – Miniszínház & lépés-térkép", "**Cím (kvucának):** Red flag vagy nem? – Esetelemzés & lépés-térkép")
replace(M3B, "Felismers **red flag helyzeteket** élő, eljátszott szituációkban (online/offline).", "Felismers **red flag helyzeteket** fiktív, harmadik személyű esetleírásokban (online/offline).", required=False)
replace(M3B, "Felismer **red flag helyzeteket** élő, eljátszott szituációkban (online/offline).", "Felismer **red flag helyzeteket** fiktív, harmadik személyű esetleírásokban (online/offline).")
replace(M3B, "ahol a kiscsoportok **el tudják játszani** a miniszínház-jeleneteket.", "ahol a kiscsoportok **nyugodtan tudják elemezni** az esetkártyákat.")
replace(M3B, "**5–25’** – Mini-színház red flag helyzetekkel (3–4 kiscsoport × szituációkártyák)", "**5–25’** – Esetelemzés red flag helyzetekkel (3–4 kiscsoport × szituációkártyák)")
replace(M3B, "## 4.2. Blokk 2 – Mini-színház red flag helyzetekkel (5–25’)", "## 4.2. Blokk 2 – Esetelemzés red flag helyzetekkel (5–25’)")
replace(M3B,
        "> „Most olyan helyzeteket fogunk eljátszani,\n> amik sajnos **valóban előfordulhatnak** kvucában, táborban, online.\n\n> Nem azért csináljuk, hogy bárkit ijesztgessünk,",
        "> „Most olyan **fiktív esetleírásokkal** fogunk dolgozni, amelyek sajnos valóban előfordulhatnak kvucában, táborban vagy online. **Nem játsszuk el a bántalmazást, önsértést, krízist, groomingot vagy intim határátlépést**, és senkinek nem kell érintett gyerek vagy elkövető szerepébe állnia. Kívülről elemezzük: mi a red flag, mi legyen az első mondat és kit kell bevonni.\n\n> Nem azért csináljuk, hogy bárkit ijesztgessünk,")
# Replace the mixed roleplay decision/instruction block with one clear default.
replace_re(M3B,
    r"> \*\*Melyik szituációt játsszátok el, és melyiket csak ELEMEZZÉTEK\?.*?\n\nInstrukció:\n\n> „A feladatotok, hogy \*\*2–3 perces minijelenetet\*\* rakjatok össze a helyzetből\..*?\n> hogy ezek \*\*valódi, súlyos helyzetek\*\* is lehetnek.”",
    r'''> **Kötelező feldolgozási mód a jelen release-ben: harmadik személyű esetanalízis.**
> Mind a négy kártyát kívülről dolgozzátok fel. Nincs szereposztás, nincs „érintett gyerek”, „elkövető” vagy krízis eljátszása. A gyermekvédelmi felelős később engedélyezhet külön, alacsony kockázatú kommunikációs szerepgyakorlatot, de ez **nem előfeltétele** a kompetencia mérésének és nem írhatja felül a traumaérzékeny keretet.
>
> **Kiscsoportos feladat:** készítsetek 2–3 perces eset-összefoglalót négy ponttal:
> 1. Mi a megfigyelhető red flag / aggály?
> 2. Mi az az **első mondat**, amit a madrich biztonságosan mondhat?
> 3. Mit **nem** ígér / nem tesz (pl. teljes titoktartás, nyomozás, konfrontáció)?
> 4. Kit és milyen sürgősséggel von be a helyi protokoll szerint?
>
> Saját történetet nem kell megosztani. Ha valakinek a téma személyesen közel van, passzolhat vagy másik esetet választhat.''',
    count=1, flags=re.S)
replace(M3B, "### 4.2.3. Kiscsoportos készülés (kb. 5–7’)", "### 4.2.3. Kiscsoportos esetfeldolgozás (kb. 5–7’)")
replace_re(M3B,
    r"### 4\.2\.4\. Jelenetek bemutatása \+ megbeszélés \(kb\. 3–4 perc / csoport\).*?\n\n\*\*Képző kérdései a nagykörnek:\*\*",
    r'''### 4.2.4. Esetek visszahozása + megbeszélés (kb. 3–4 perc / csoport)

Alapértelmezés: 3 csoport → kb. 12 perc. Minden csoport röviden bemutatja a saját négy pontját. **Nem jelenetet mutat be**, hanem az elemzését: red flag → első mondat → tiltott reakció → bevonandó felelős.

Ha a megbeszélés közben valaki személyes érintettséget tár fel, állítsd meg a szakmai elemzést, ne kérdezd ki, és kövesd a fenti triage- és jelzési keretet.

**Képző kérdései a nagykörnek:**''',
    count=1, flags=re.S, required=False)
replace(M3B, "minijelenet", "esetfeldolgozás", required=False)
replace(M3B, "miniszínház", "esetelemzés", required=False)


# ---------------------------------------------------------------------------
# M6.A: make the actual game match the inclusive no-elimination rule.
# ---------------------------------------------------------------------------
M6A = "02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md"
replace_re(M6A,
    r"> „Most egy klasszikus játékot játszunk:\n> \*\*‘Szél fújja azt, aki…’\*\*.*?\n> Most először pár könnyedebb állítással játszunk.”",
    r'''> „Most a **‘Szél fújja azt, aki…’ inkluzív, nem versengő változatát** játsszuk.
>
> Mindenkinek van saját helye/széke. Egy önkéntes vagy a képző mondja: *‘Szél fújja azt, aki…’* és egy könnyű, nem érzékeny állítást.
>
> Akire igaz, **feláll, tesz egy nyugodt lépést a kör közepe felé vagy helyet cserél valakivel előre megbeszélt, nem versengő módon**, majd mindenki visszaül / megáll. **Nincs eggyel kevesebb szék, nincs székszerző verseny, nincs kieső, és senki nem kerül kötelezően középre.**
>
> A következő mondatot új önkéntes mondhatja; ha nincs jelentkező, a képző folytatja. A felállás bármikor passzolható. Most először pár könnyedebb állítással játszunk.”''',
    count=1, flags=re.S)
replace(M6A,
        "> **Fizikai safety-mondat (a helycseréhez – mondd ki ELŐRE):**\n\n> „Amikor helyet cseréltek, **lassan, nem teljes erőből** indulunk, **nézünk magunk elé**, és **kerüljük az ütközést** – nem lökünk, nem rángatunk széket.”\n\n> ⚠️ **10–12 éveseknél kiemelten:** ennél a korosztálynál a helycsere gyorsan vad lesz (lökés, ráülés, felboruló szék). Ha velük játszanád: **tágítsd a kört**, vegyél ki minden útban lévő bútort/kábelt.",
        "> **Fizikai safety-mondat (mondd ki ELŐRE):**\n\n> „Nem versenyzünk a helyekért. Nyugodt tempóban mozgunk, nézünk magunk elé, nem lökünk és nem húzunk ki széket más alól. Ha a tér szűk vagy valaki nem szeretne helyet változtatni, elég egy kézjel / felállás is.”")
replace(M6A, "Lejátszotok 8–10 kört, **szándékosan vegyes állításokkal**", "Lejátszotok 8–10 kört **könnyű, előre biztonságosnak szűrt állításokkal**")
replace(M6A, "* „…akinek volt már olyan, hogy kicsit kívülről nézte a kvucát.”\n", "", required=False)
replace(M6A, "* „**Nincs eggyel kevesebb szék, nincs székért-rohanás** → senki nem esik ki, középre önként állunk.”", "* „**Nincs eggyel kevesebb szék, nincs székért-rohanás** → senki nem esik ki; a mondatot önkéntes vagy a képző mondja.”")


# ---------------------------------------------------------------------------
# M6.4 constructive alignment: require practice matching the stated objective.
# ---------------------------------------------------------------------------
M64 = "02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md"
replace(M64,
        "A tanuló bármennyi ágon végigmehet, de **1 teljes ág végigjátszása** kell és elég a completionhöz.",
        "A tanuló **legalább 3 különböző teljes ágon** végigmegy; a 4. ág opcionális gyakorlás. A completion csak akkor tekinthető teljesítettnek, ha a cél Moodle/H5P környezetben **bizonyítottan mérhető a három külön ág**. Ha a telepített Branching Scenario ezt nem tudja megbízhatóan kikényszeríteni, a három esetet külön H5P-aktivitásként vagy Moodle-checkpointtal kell implementálni. **Attempt / megnyitás önmagában nem teljesítés.**")


# ---------------------------------------------------------------------------
# M6.1 AI Act: distinguish provider machine marking from deployer disclosure.
# ---------------------------------------------------------------------------
M61 = "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md"
replace_re(M61,
    r"> 🤖 \*\*AI-provenance \(buildhez, kötelező – ezen a dián és minden további AI-generált médiánál/narrációnál/kvíz-itemnél\):\*\*.*?\n> \* \*\*Human-in-the-loop:\*\* a narráció és a kvíz-kulcsok emberi szakmai lektoráláson mennek át, mielőtt élesednek\.",
    r'''> 🤖 **AI-provenance és átláthatóság (buildhez):**
> * **Ember-olvasható jelzés:** ha a tanuló AI-generált vagy lényegileg AI-manipulált kép-, hang- vagy videotartalmat lát, legyen világos, rövid közlés, pl. **„A videó AI-eszközzel készült, emberi lektorálással.”**
> * **AI Act szerepek pontosan:** az EU AI Act 50. cikk (2) szerinti gépi olvasható megjelölési kötelezettség a szintetikus tartalmat generáló **AI-rendszer szolgáltatóját (provider)** terheli. A **deployer/alkalmazó** számára külön közzétételi kötelezettség vonatkozhat többek között deepfake kép/hang/videó használatára, illetve bizonyos közérdekű AI-szövegre. **C2PA / Content Credentials ezért hasznos provenance-best-practice, de nem állítható általánosan úgy, hogy minden saját oktatási exportnál ez önmagában a deployer törvényi kötelezettsége.**
> * **Build-szabály:** ahol a használt generáló eszköz gépi jelölést/provenance-metaadatot ad, azt az export ne távolítsa el indokolatlanul; a végső médián az ember-olvasható disclosure-t külön is ellenőrizni kell.
> * **Human-in-the-loop:** a narráció és a kvíz-kulcsok emberi szakmai lektoráláson mennek át, mielőtt élesednek.''',
    count=1, flags=re.S)
anchor61 = "**Mikrocél (tanulói nyelven):**"
replace(M61, anchor61, "> **Korosztályi megjegyzés:** a 6–10 / 11–13 / 14–16 / 16+ bontás **tervezési heurisztika**. Nem diagnózis és nem írja felül a konkrét kvuca megfigyelését, az egyéni különbségeket vagy a hozzáférési szükségleteket.\n\n" + anchor61)


# ---------------------------------------------------------------------------
# M7 AI use: approved environment + minor access + no-sensitive-data fallback.
# ---------------------------------------------------------------------------
M72 = "02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nem csak játék, hanem peula – 11 tervezési pont & AI-támogatás.md"
anchor72 = "**Flow:**"
# Insert before the first Flow only.
replace_re(M72, r"\*\*Flow:\*\*", r'''### Kötelező AI-hozzáférési és adatvédelmi keret

> Az AI **opcionális segédeszköz**, nem a feladat teljesítésének feltétele. A képző csak **szervezetileg jóváhagyott** szolgáltatást adhat meg. 18 év alatti résztvevőnél a választott szolgáltatás aktuális korhatár- és szülői/gondviselői hozzájárulási feltételeinek teljesülniük kell. Ha ez nem biztosított, legyen **egyenértékű AI-fiók nélküli út**: saját ötletelés, mentor, nyomtatott promptkártya vagy képző által közvetített, anonimizált példa.
>
> AI-szolgáltatásba **nem kerülhet chanich neve, elérhetősége, fotója, egészségügyi/mentális állapota, családi háttere, zsidó/egyéb identitása, pontos helyszíne vagy más beazonosítható/szenzitív története**. Gyermekvédelmi döntést, red flag minősítést vagy kríziskezelést **nem delegálunk AI-nak**; ilyen ügyben a kijelölt felelős embert kell bevonni.

**Flow:**''', count=1)

# ---------------------------------------------------------------------------
# M7.4 naming: this is v1 draft; v2 is created after review in M7.B.
# ---------------------------------------------------------------------------
M74 = "02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md"
text = read(M74)
text = text.replace("# M7.4 – „Peula v2 + AI” – modulproduktum váz", "# M7.4 – „Peula v1 + AI” – első modulproduktum-vázlat")
text = text.replace("**Cím (tanulónak):** Peula v2 + AI – modulproduktum váz", "**Cím (tanulónak):** Peula v1 + AI – első modulproduktum-vázlat")
# Scope v2->v1 replacements to phrases describing the assignment/draft, not historical v2 references.
text = text.replace("**„Peula v2 – első vázlat”**", "**„Peula v1 – első vázlat”**")
text = text.replace("Peula v2 – első vázlat", "Peula v1 – első vázlat")
text = text.replace("első Peula v2", "első Peula v1")
# Add canonical version rule near top.
if "**Verziószabály (kánoni):**" not in text:
    marker = "**Kód:** M7.4"
    text = text.replace(marker, marker + "\n\n> **Verziószabály (kánoni):** az M7.4-ben készül a **Peula v1, vagyis az első teljes vázlat**. Az M7.B workshop és feedback után ebből lesz a **Peula v2**, amely a végső kapu produktuma. A `v2` nem jelenthet „első vázlatot”.")
write(M74, text)

M7HUB = "02 Tervezet/Modulok/M7/M7 – Peula a papírtól a valóságig – Programírás, Zmán Kvucá & AI-támogatott tervezés.md"
text = read(M7HUB)
text = text.replace("M7.4 – Peula v2 + AI", "M7.4 – Peula v1 + AI")
text = text.replace("Peula v2 + AI – modulproduktum váz", "Peula v1 + AI – első modulproduktum-vázlat")
write(M7HUB, text)


# ---------------------------------------------------------------------------
# Z.3: a 15+ participant can be a minor; do not position them as "the adult".
# ---------------------------------------------------------------------------
Z3 = "02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md"
replace_re(Z3,
    r"> A terepen nem csak madrich-módszertanilag lépsz élesbe: \*\*te leszel az a felnőtt\*\*.*?(?=\n\n|\n\*\*|\Z)",
    r'''> A terepen nem csak módszertanilag lépsz élesbe: **madrichként felelős szereped lesz**, miközben a képzés 15+ célcsoportjában te magad is lehetsz kiskorú. Gyermekvédelmi vagy más biztonsági helyzetben **nem neked kell egyedül „a felnőttnek” lenned**: tudd előre, melyik kijelölt felelős felnőttet / gyermekvédelmi felelőst vonod be, és a helyi protokoll szerint jelezz.''',
    count=1, flags=re.S)


# ---------------------------------------------------------------------------
# Z.4: remove unsupported Documentation Tool resume claim and fix sequence.
# ---------------------------------------------------------------------------
Z4 = "02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md"
text = read(Z4)
text = text.replace("H5P **Documentation Tool** – záró reflexiós ív kitöltése (a 3 kérdéshez): **~20–30’**", "**Moodle Assignment (online text, draft mentéssel)** – záró reflexiós ív kitöltése (a 3 kérdéshez): **~20–30’**")
text = text.replace("**Az ív letöltése + Moodle Assignment leadás** (a kész ívet adod be, vagy egy 2–3 perces videót veszel fel belőle): **~15–25’**", "**Véglegesítés + Moodle Assignment leadás** (a mentett szöveget adod be, vagy abból egy 2–3 perces videót készítesz): **~15–25’**")
text = text.replace("egy kész, **letölthető záró-ívet**", "egy kész, **menthető záró reflexiót**")
text = text.replace("egy összefüggő reflexiós ívbe", "egy összefüggő, Moodle-ben piszkozatként menthető reflexiós ívbe")
text = text.replace("a végén **egy darabban letöltöd**", "a végén **véglegesíted és beadod**")
text = text.replace("az ív **menet közben menthető**, így **nyugodtan tarthatsz szünetet**, és külön ülésben fejezheted be / veheted fel a végleges reflexiót.", "a Moodle Assignment **draft/piszkozat mentését a célrendszeren acceptance teszttel igazolni kell**; csak igazolt mentés mellett kommunikálható, hogy külön ülésben biztonságosan folytatható.")
text = text.replace("ez a digitális ív **nem helyettesíti**, hanem előkészíti a **Z.A élő záró-peulát**", "ez a digitális ív **nem helyettesíti** a **Z.A élő záró-peulát**. A kánoni sorrend: **Z.A élő lezárás → Z.4 egyéni záró reflexió és képzés-feedback**")
text = text.replace("H5P **Documentation Tool** – „Záró reflexiós ív” (strukturált, lépésenként kitölthető, a végén **letölthető** záró-dokumentum)", "**Moodle Assignment – Online text** – „Záró reflexiós ív” (strukturált sablonnal, piszkozatmentéssel; a tényleges draft/resume működést acceptance teszt igazolja)")
text = text.replace("A lecke végére lesz egy **letölthető, összefüggő záró-íved**", "A lecke végére lesz egy **mentett és beadott, összefüggő záró reflexiód**")
text = text.replace("→ H5P Documentation Tool (Z.4 – „Záró reflexiós ív”)", "→ Moodle Assignment (Z.4 – „Záró reflexiós ív”, Online text)")
text = text.replace("## 3. H5P Documentation Tool – „Záró reflexiós ív” (lépésről lépésre)", "## 3. Moodle Assignment – „Záró reflexiós ív” (lépésről lépésre)")
text = text.replace("**Miért Documentation Tool?**", "**Miért Moodle Assignment?**")
text = text.replace("A Documentation Tool ezeket **egy összefüggő, lépésenként kitölthető ívbe** fűzi, amit a tanuló a végén **egyben letölt** – ez a letölthető záró-dokumentum.", "A Moodle Assignment online szöveges sablonja ezeket **egy összefüggő ívbe** fűzi. Így nem támaszkodunk az H5P Documentation Tool nem igazolt session-resume képességére, és a hosszabb szöveg a Moodle saját draft/leadási folyamatában kezelhető.")
text = text.replace("**Megvalósítás (fejlesztői jegyzet):** H5P **Documentation Tool**, az alábbi lépésekkel (Steps). A „Text input” lépések a korábbi külön szövegmezőket váltják ki, a záró „Document export” lépés állítja össze a **letölthető** ívet.", "**Megvalósítás (fejlesztői jegyzet):** Moodle **Assignment / Online text** egy előre kitöltött, háromrészes sablonnal. A szakaszcímek az alábbi lépéseket követik; a végén nincs H5P-export, a tanuló a Moodle-ben véglegesíti a beadást.")
text = text.replace("Bármikor megállhatsz – az ív **mentve marad**, később folytathatod.", "Megállhatsz közben, **ha a cél Moodle-környezetben a draftmentést előzetesen leteszteltük**; enélkül a tanulónak ezt nem ígérjük.")
text = text.replace("Ez a szöveg **bekerül a letölthető ívbe**.", "Ez a szöveg **a Moodle-beadás része lesz**.")
text = text.replace("mielőtt letöltöd", "mielőtt véglegesíted")
text = text.replace("letöltött dokumentumban", "végleges beadásban")
# Remove common remaining unsupported export/download language without changing historical source notes.
text = text.replace("letölthető záró-dokumentum", "végleges záró reflexió")
text = text.replace("letölthető záró-dokumentumod", "végleges záró reflexiód")
text = text.replace("Document export", "Assignment véglegesítés")
write(Z4, text)

Z_HUB = "02 Tervezet/Modulok/Z/Z – Záró modul – reflexió, integráció & híd a terepre.md"
if p(Z_HUB).exists():
    append_once(Z_HUB, "## Kánoni zárási sorrend (release-audit 2026-08-25)", r'''## Kánoni zárási sorrend (release-audit 2026-08-25)

A zárás kánoni sorrendje: **Z.1 → Z.2 → Z.3 → Z.A élő záró-peula → Z.4 egyéni záró reflexió + anonim képzés-feedback**. A Z.4 nem „előkészíti” a Z.A-t, hanem az élő lezárást követő egyéni integráció. A Moodle határidőknek ezt kell leképezniük.''')


# ---------------------------------------------------------------------------
# Accessibility: captions are required for prerecorded synchronized video.
# ---------------------------------------------------------------------------
A11Y = "02 Tervezet/LMS – hozzáférhetőségi sztenderd.md"
text = read(A11Y)
text = re.sub(r"felirat\s*(?:vagy|/)\s*(?:teljes\s*)?leirat", "felirat **és** hozzáférhető szöveges leirat / alternatíva", text, flags=re.I)
# Add authoritative clarification if absent.
if "WCAG 2.2 SC 1.2.2" not in text:
    text += r'''

## Pontosítás: előre rögzített videó és hang

- **WCAG 2.2 SC 1.2.2:** előre rögzített, szinkronizált médiában a hangzó tartalomhoz **felirat szükséges** (a WCAG kivételétől eltekintve, amikor maga a média egy már meglévő szöveg alternatívája és így is van jelölve).
- A teljes szöveges leirat hasznos és erősen ajánlott kiegészítő, de **nem helyettesíti automatikusan a feliratot** szinkronizált videónál.
- Interaktív tartalomnál a billentyűzet, fókuszsorrend, név/szerep/érték, kontraszt és célméret a tényleges Moodle/H5P renderen tesztelendő, nem csak a Markdown-specifikációban.
'''
write(A11Y, text)


# ---------------------------------------------------------------------------
# Deep-audit workflow: remove obsolete local path names and add real rubric.
# ---------------------------------------------------------------------------
DA = ".claude/workflows/deep-audit.js"
text = read(DA)
text = text.replace("const ABS = '/Users/heymarcell/DEV/modszertani-kepzes/02 Tervezet'\nconst REPO = '/Users/heymarcell/DEV/modszertani-kepzes'\nconst MOD = ABS + '/MODULOK'\nconst RUBRIC = ABS + '/_AUDIT/DEEP-AUDIT-RUBRIC.md'",
                    "const REPO = process.cwd()\nconst ABS = REPO + '/02 Tervezet'\nconst MOD = ABS + '/Modulok'\nconst RUBRIC = REPO + '/01 Fejlesztés/04 Audit/DEEP-AUDIT-RUBRIC.md'")
write(DA, text)

write("01 Fejlesztés/04 Audit/DEEP-AUDIT-RUBRIC.md", r'''# Deep Audit Rubric

Ez a rubrika a `.claude/workflows/deep-audit.js` gépi auditjának kánoni dimenziólistája. A gépi audit **nem helyettesíti** a szakértői jóváhagyást.

| ID | Dimenzió | Piros finding | Sárga finding |
|---|---|---|---|
| D1 | Constructive alignment | cél nincs mérve / kapu mást mér | részleges vagy homályos illeszkedés |
| D2 | Tanulási ív és terhelés | blokkoló sorrendi/prerekvizit hiba | túlterhelés, gyenge ritmus |
| D3 | Értékelés / mastery | hamis completion, kritikus safety tudás nem kapuzott | rubrika/feedback finomítandó |
| D4 | LMS/H5P implementálhatóság | dokumentált funkció nincs vagy nem bizonyított | verzió-/runtime-kockázat |
| D5 | Accessibility | kulcstartalom nem hozzáférhető | javítandó UX/a11y részlet |
| D6 | Someres tartalmi/ideológiai pontosság | helyi döntést AI találna ki | helyi megerősítés kell |
| D7 | Safeguarding | veszélyes instrukció, hiányzó eszkaláció, szakértői gate megkerülése | óvatosság / keretezés javítandó |
| D8 | Adatvédelem / AI | kiskorú vagy érzékeny adat kontroll nélkül | retention/access/alternatíva tisztázandó |
| D9 | Tudományos megalapozottság | bizonyítottan félrevezető / neuromítosz | túláltalánosított állítás |
| D10 | Repo-integritás | törött link, kánoni duplikátum, release-blokkoló placeholder | terminológiai/stílus inkonzisztencia |

## Routing

- **D7** → `safeguarding-review`, biztonságkritikus tartalmat ne auto-javítson éles szakpolitikai állítássá.
- **D6** → `ideology-gate-review`, helyi Somer-konvenciót ne találjon ki.
- **D8** jogalap/retention/hozzáférés → emberi privacy/DPO review.
- Architekturális programváltozás → `architecture-review`.
- Auto-fix csak akkor, ha a helyes állapot objektíven bizonyítható (pl. link, elírás, duplikátum, egyértelmű belső ellentmondás).
''')


# ---------------------------------------------------------------------------
# Governance / release documents.
# ---------------------------------------------------------------------------
write("02 Tervezet/RELEASE-READINESS.md", r'''# Release Readiness – kötelező Go / No-Go kapuk

**Állapot:** NO-GO, amíg az alábbi P0 kapuk nincsenek bizonyítékkal lezárva.

A tananyag minősége és a release-érettség két külön kérdés. A repository erős pedagógiai specifikáció, de éles kurzusnak csak a tényleges szervezeti, adatvédelmi és LMS-implementációval együtt minősíthető.

## Globális kapuk – minden modul élesítését blokkolják

- [ ] **G1 Gyermekvédelem:** kijelölt felelős, helyi jelzési/escalation protokoll, alternatív út összeférhetetlenség esetére, M3 és kapcsolódó safety tartalmak szakértői aláírása. Lásd `Gyermekvédelem – release gate.md`.
- [ ] **G2 Adatvédelem és kiskorúak:** adatleltár, jogalapok, szerepkörök/hozzáférés, megőrzés/törlés, fotó/videó, érzékeny reflexiók, AI-szolgáltatások és kiskorú hozzáférés jóváhagyva. Lásd `Adatvédelem – tanulói adatok és AI.md`.
- [ ] **G3 LMS/H5P célkörnyezet:** Moodle-verzió és minden H5P content type verziója rögzítve; a kritikus completion, branching, draft/resume és accessibility tesztek átmentek. Lásd `LMS – H5P runtime acceptance.md`.
- [ ] **G4 Learner-facing placeholder = 0:** tanulói útvonalon nincs `KITÖLTENDŐ`, névtelen kontakt, bizonytalan határidő vagy nem létező link.
- [ ] **G5 Accessibility:** mobil + billentyűzet + screen reader + zoom/reflow + captions teszt a tényleges Moodle-renderen.
- [ ] **G6 Terminológia és korosztály:** a helyi Somer megerősítette a 2026-os kánoni alakokat és a 3/4 kvuca-architektúrát; a glosszárium és tananyag ennek megfelelő.
- [ ] **G7 Release regression:** `tools/content_integrity.py` 0 ERROR; link-check 0 broken local link; nincs kánoni duplikátum.

## Modul-specifikus kapuk

Egy modul tartalmi jóváhagyása lehet moduláris **csak akkor**, ha G1–G7 globális kapuk már zártak. Egy modul saját szakmai/ideológiai lektorálása blokkolhatja csak azt a modult, de globális safety/privacy/infrastruktúra hiányában **semmilyen modul nem élesíthető tanulóknak**.

## Program-transzfer

- [ ] A félév végi `Peula v2` nem a program végső teljesítménymutatója: működik a `Terepgyakorlat – 2. félév.md` szerinti hat valós, 60–90 perces peula + mentorfeedback ciklus.
- [ ] Pilot megtörtént kis csoporttal, findingek javítva és újratesztelve.
- [ ] Média-regiszter a tartalmi freeze **után** újragenerálva és auditálva.

## Merge ≠ release

A GitHub merge technikai esemény. Élesítéshez külön, dátummal és felelősökkel rögzített Go/No-Go review kell. A release bizonyítékai linkelhetők ebbe a dokumentumba vagy a kapcsolódó issue-kba.
''')

write("02 Tervezet/Gyermekvédelem – release gate.md", r'''# Gyermekvédelem – release gate

## Release-szabály

M3.3, M3.B, az M3 kapu, valamint minden olyan tananyagelem, amely bántalmazásra, önsértésre, groomingra, szexuális/romantikus határátlépésre, súlyos veszélyeztetettségre vagy külső jelzésre tanít, **nem élesíthető gyermekvédelmi felelős írásos jóváhagyása nélkül**.

A jelen repo biztonságos alapértelmezése: súlyos helyzeteket **harmadik személyű esetanalízissel**, nem traumatikus szerepjátékkal dolgozunk fel.

## Jóváhagyás előtt kitöltendő

| Mező | Érték |
|---|---|
| Helyi gyermekvédelmi felelős / Memuna vagy az aktuális kánoni szerep | KITÖLTENDŐ |
| Elérhetőség | KITÖLTENDŐ |
| Helyettes / alternatív eszkaláció összeférhetetlenség esetére | KITÖLTENDŐ |
| Országos/mozgalmi escalation | KITÖLTENDŐ |
| Akut veszély protokoll | KITÖLTENDŐ |
| Dokumentáció helye és hozzáférése | KITÖLTENDŐ |
| Jóváhagyó neve | KITÖLTENDŐ |
| Jóváhagyás dátuma | KITÖLTENDŐ |
| Következő review | KITÖLTENDŐ |

## Tartalmi acceptance

- nincs 100% titoktartás-ígéret;
- madrich nem nyomoz és nem konfrontál feltételezett elkövetőt;
- világos „észlel → jelzi → felelős felnőttet bevon” szerep;
- 15–17 éves madrichot nem pozicionáljuk egyedüli „felnőttként”;
- súlyos esetnél nincs kötelező személyes disclosure;
- telefonszám, hatósági út és jogszabály a review napján frissen ellenőrzött;
- facilitátor tudja, mit tesz, ha a képzés közben résztvevő saját érintettséget tár fel.

## Elsődleges magyar források a szakértői review-hoz

- 1997. évi XXXI. törvény, különösen 17. §, Nemzeti Jogszabálytár.
- Btk. 209/A. § hatályos szövege.
- Belügyminisztérium / kormányzati gyermekjóléti jelzőrendszeri protokoll és 2026-os módszertani útmutató.

A repository nem dönthet a szervezet konkrét jogállásáról vagy jelzési láncáról szakértő helyett.
''')

write("02 Tervezet/Adatvédelem – tanulói adatok és AI.md", r'''# Adatvédelem – tanulói adatok és AI

**Release gate:** a dokumentumot a tényleges adatkezelő szervezet privacy/DPO/jogi felelőse hagyja jóvá az éles Moodle előtt.

## Adatminimalizálási alapelv

A képzés csak azt az adatot kérje, amely egy konkrét pedagógiai vagy biztonsági célhoz szükséges. Érzékeny identitás-, családi-, mentális/egészségügyi vagy gyermekvédelmi történet **nem lehet kötelező tanulási artefaktum**. Ahol személyes reflexió segít, legyen fiktív/általánosított vagy csak a tanulónál maradó alternatíva.

## Kötelező adatleltár

Az LMS-owner + privacy felelős minden activitynél rögzíti: adatmező, cél, jogalap, kötelező/opcionális, címzettek, hozzáférési szerepkör, megőrzés, törlés, export, harmadik fél, ország/adattovábbítás, kiskorúakra vonatkozó szabály.

Külön review szükséges legalább:

- M1 önreflexiók és mentor-láthatóság;
- M2 identitáskörök, zsidó/egyéb identitás, család, értékek, határnapló;
- M4 kamera-, hang- vagy videófelvétel;
- M6 fotó / kézműves dokumentáció;
- M7 AI-promptok és peulatervek;
- Z.2/Z.4 személyes reflexiók és mentor-hozzáférés.

## Kiskorúak és hozzájárulás

A GDPR 8. cikkének korhatárszabálya **nem általános „minden adatkezeléshez szülői beleegyezés” szabály**: az információs társadalommal összefüggő, közvetlenül gyermeknek kínált szolgáltatásnál és hozzájárulás-alapú adatkezelésnél releváns. A képzés minden adatkezelésének jogalapját külön kell meghatározni.

## Külső generatív AI

- AI használata tanulónak opcionális; legyen teljes értékű no-AI út.
- Csak szervezetileg jóváhagyott szolgáltatás nevezhető meg.
- 18 év alatti tanuló csak akkor használhat külső szolgáltatást, ha annak aktuális minimum-age / parental-consent feltétele teljesül.
- Nem kerülhet promptba chanich neve, elérhetősége, képe, pontos helye, egészségügyi/mentális állapota, családi háttere, vallási/etnikai/egyéb érzékeny identitása vagy beazonosítható eseménye.
- Gyermekvédelmi döntést és kríziskezelést nem delegálunk AI-nak.
- A szolgáltató retention/training/admin controls beállítását a szervezetnek dokumentálnia kell.

## Fotó / videó

Felvétel csak előre rögzített cél, jogalap, hozzáférés, megőrzés és törlés mellett. A pedagógiai feladatnak legyen felvétel nélküli alternatívája, ha a felvétel nem nélkülözhetetlen. Személyes eszközre/felhőbe történő kontrollálatlan másolás nem elfogadható alapfolyamat.
''')

write("02 Tervezet/LMS – H5P runtime acceptance.md", r'''# LMS – H5P runtime acceptance

A Markdown specifikációból **nem bizonyítható**, hogy egy H5P/Moodle interakció a tényleges telepítésen működik. Release előtt a célkörnyezetet verzióval rögzíteni és tesztelni kell.

## Environment record

| Komponens | Verzió / build | Dátum | Felelős |
|---|---|---|---|
| Moodle | KITÖLTENDŐ | KITÖLTENDŐ | KITÖLTENDŐ |
| H5P core / plugin | KITÖLTENDŐ | KITÖLTENDŐ | KITÖLTENDŐ |
| Course Presentation | KITÖLTENDŐ | | |
| Branching Scenario | KITÖLTENDŐ | | |
| Dialog Cards | KITÖLTENDŐ | | |
| Column | KITÖLTENDŐ | | |
| Question Set | KITÖLTENDŐ | | |
| Interactive Video | KITÖLTENDŐ | | |
| Browser/device matrix | KITÖLTENDŐ | | |

## P0 runtime tesztek

1. **Completion semantikája:** megnyitás/attempt nem számíthat mastery teljesítésnek; grade/pass feltétel ténylegesen blokkol.
2. **M6.4 Branching Scenario:** legalább három külön ág teljesítése ténylegesen mérhető vagy Moodle-checkpointtal helyettesített.
3. **Z.4 hosszú reflexió:** Moodle Assignment draft mentés, újranyitás, visszatérés és véglegesítés ténylegesen működik. Nem támaszkodunk H5P Documentation Tool session-resume állításra.
4. **M5 Dialog Cards:** a cél verzión a kártyák mobilon, billentyűzettel és nagyított nézetben használhatók; esetleges „repetition” funkciót nem kommunikálunk bizonyított, többnapos spaced-repetition rendszerként külön teszt nélkül.
5. **Moodle 5.x / Branching Scenario:** külön regressziós teszt, mert 2026-ban Moodle 5.1.1 környezetben dokumentált Branching Scenario megjelenítési hiba jelent meg a H5P communityben.
6. **Resume / state:** minden olyan learner-facing mondat, hogy „később folytathatod”, csak igazolt state persistence után maradhat.

## Accessibility acceptance

Minden kritikus content type legalább:

- teljes billentyűzetes út;
- látható fókusz és logikus fókuszsorrend;
- screen-reader ellenőrzés;
- 200–400% zoom/reflow;
- mobil portrait;
- feliratos prerecorded videó;
- nem csak színre támaszkodó feedback;
- megfelelő kontraszt és célméret;
- hibás válasz után értelmes, nem csak „rossz” feedback.

## Release evidence

A teszt eredménye legyen issue, táblázat vagy screenshot/log, dátummal és pontos verzióval. „A H5P tudja” nem acceptance evidence.
''')

write("02 Tervezet/LMS – activity manifest.md", r'''# LMS – activity manifest

Ez a Moodle-build kánoni kontrolltáblája. A modulok Markdown-specifikációja adja a tartalmat; az éles course build során **minden tényleges Moodle activity** kapjon egy sort és konkrét ID/linket.

| Modul | Activity-csoport | Required? | Előfeltétel | Completion / pass | Mit nyit | Deadline | Megjegyzés |
|---|---|---:|---|---|---|---|---|
| M0 | M0.1–M0.4 online | igen | kurzushozzáférés | activity completion, a konkrét interakció szerint | M0.A / M1 | KITÖLTENDŐ | sorrendet a modulhub szerint |
| M0 | M0.A kickoff | igen | kijelölt online előkészítés | jelenlét / facilitator record | M1 | KITÖLTENDŐ | technikai/help keret |
| M1 | M1.1–M1.2 | igen | M0 complete | activity completion | M1.A | KITÖLTENDŐ | |
| M1 | M1.A | igen | M1.1–M1.2 | jelenlét | M1.3–M1.4 | KITÖLTENDŐ | |
| M1 | M1.3–M1.4 + Assignment gate | igen | M1.A | rubrika, minden sor ≥1 és össz. ≥5/8 | M1.B / M2 | KITÖLTENDŐ | retry mastery |
| M1 | M1.B | igen | M1.3–M1.4 | jelenlét | M2 | KITÖLTENDŐ | |
| M2 | online + peulák + napló/kapu | igen, a hub szerint | M1 complete | a modulhub/kapu szerint | M3 | KITÖLTENDŐ | identity/privacy review required |
| M3 | M3.1–M3.4 | igen | M2 complete | activity completion | M3 produktum/kapu | KITÖLTENDŐ | safeguarding gate |
| M3 | M3.A/M3.B | igen / protokoll szerint | kijelölt online előtanulás | jelenlét + biztonságos esetanalízis | M3 gate | KITÖLTENDŐ | M3.B specialist signoff |
| M3 | M3 kapu | igen | online + produktum | ≥80% + kritikus itemek + rubrika | M4 | KITÖLTENDŐ | safety critical |
| M4 | online + peulák + pitch/kapu | igen | M3 complete | hub/rubrika szerint | M5 | KITÖLTENDŐ | recording/privacy review |
| M5 | online + peulák + kapu | igen | M4 complete | hub/rubrika szerint | M6 | KITÖLTENDŐ | Dialog Cards runtime test |
| M6 | M6.1–M6.4 | igen | M5 complete | M6.4 legalább 3 eset + activity rules | M6 peulák/gate | KITÖLTENDŐ | H5P branch enforcement test |
| M6 | M6.A/M6.B + játéklap gate | igen | kijelölt online előtanulás | rubrika / mastery | M7 | KITÖLTENDŐ | photo/privacy if used |
| M7 | M7.1–M7.4 | igen | M6 complete | activity completion + **Peula v1** | M7.B | KITÖLTENDŐ | AI optional, approved tool only |
| M7 | M7.B | igen | Peula v1 | workshop/review → **Peula v2** | M7 gate | KITÖLTENDŐ | |
| M7 | final gate | igen | Peula v2 + Zmán Kvucá | kapurubrika | Z | KITÖLTENDŐ | safeguarding contact filled |
| Z | Z.1–Z.3 | igen | M7 complete | activity completion | Z.A | KITÖLTENDŐ | |
| Z | Z.A live close | igen | Z.1–Z.3 | jelenlét / facilitator record | Z.4 | KITÖLTENDŐ | kánoni sorrendben Z.4 előtt |
| Z | Z.4 Assignment + Feedback | igen | Z.A | Assignment submitted + anonymous feedback policy | online félév complete | KITÖLTENDŐ | Moodle draft/resume tested |
| Terep | 6 valódi peula | igen a teljes programkompetenciához | online félév complete | megfigyelés + feedback + revision ciklus | program field-complete | 2. félév | lásd Terepgyakorlat |

## Build acceptance

- A `KITÖLTENDŐ` deadline-okat **a tanulói hozzáférés megnyitása előtt** konkrét dátum/idő váltja fel.
- Minden `Required` activitynél Moodle-ben ellenőrizni kell, hogy a completion valóban azt méri-e, amit a sor állít.
- A megvalósított course exportból ezt a táblát vissza kell auditálni: spec ↔ activity ID ↔ prerequisite ↔ grade/pass ↔ unlock.
''')

write("02 Tervezet/Terepgyakorlat – 2. félév.md", r'''# Terepgyakorlat – 2. félév

## Miért része a programnak?

Az intake eredeti teljesítménycélja nem pusztán egy jó peulaterv elkészítése, hanem az, hogy a madrich **valós kvucában képes legyen tervezni, levezetni, reflektálni és javítani**. Az online félév Peula v2-je ezért átadási pont, nem végállomás.

## Minimum field-performance ciklus

A második félévben minden résztvevő **6 valódi, 60–90 perces peulát** tervez és vezet a saját szerepéhez igazodva.

Minden peulánál ugyanaz a ciklus:

1. **Plan:** cél, kvuca, módszer, safety, kellék, realitás-check.
2. **Run:** valódi levezetés, a helyi safeguarding szabályokkal.
3. **Evidence:** rövid, adatminimalizált megfigyelési jegyzet; chanich érzékeny adata nélkül.
4. **Feedback:** mentor / kijelölt tapasztalt vezető konkrét visszajelzése.
5. **Reflect:** mi működött, mi nem, mi lepett meg.
6. **Revise:** 1–3 konkrét változtatás a következő peulára.

## Mintavétel

A hat alkalomból legalább:

- **2** alkalmat mentor vagy kijelölt tapasztalt madrich **élőben megfigyel**;
- **2** alkalomnál a résztvevő explicit módon visszahoz egy korábbi feedback-pontot és megmutatja, mi változott;
- **1** alkalom tartalmaz tudatos inkluzivitási adaptációt;
- **1** alkalom után dokumentált safety/határ-reflexió készül akkor is, ha nem történt incidens.

## Field-rubrika

0–2 skálán: cél és alignment; instrukció/keretezés; kvuca-reakciók megfigyelése; facilitálás és kérdezés; idő/tér adaptáció; inkluzivitás; safety/határtartás; feedback felhasználása; reflektív javítás.

**Nem pontozzuk** a chanichok „engedelmességét”, a hangulatot önmagában vagy azt, hogy minden terv szerint történt-e. A kompetencia része az adaptáció.

## Programeredmény

- **Online-complete:** M0–M7 + Z és a kapuk teljesültek.
- **Field-complete:** 6 peula + kötelező megfigyelések + feedback/revision bizonyíték.
- **Program-complete:** csak a kettő együtt.

A pontos naptár, mentor-hozzárendelés és adatmegőrzési forma szervezeti döntés, és az LMS manifestben / privacy policyban élesítés előtt rögzítendő.
''')

append_once("02 Tervezet/Program terv.md", "## Release- és terepgyakorlati kiegészítés (2026-08-25)", r'''## Release- és terepgyakorlati kiegészítés (2026-08-25)

A program release-governance kánoni pontosítása:

1. **Globális safety/privacy/infrastruktúra kapuk** minden modul learner-facing élesítését blokkolják. Ezeket nem lehet moduláris MVP-re hivatkozva megkerülni.
2. **Modul-specifikus tartalmi/ideológiai signoff** lezárható modulonként, miután a globális kapuk zártak.
3. A GitHub `main` állapota nem azonos a Moodle release-státusszal. A go/no-go igazolása a `RELEASE-READINESS.md` szerint történik.
4. Az online félév után kötelező transzfer-szakasz következik: `Terepgyakorlat – 2. félév.md`, **6 valódi 60–90 perces peulával**, megfigyelés → feedback → reflektálás → javítás ciklusban.

Kánoni operációs dokumentumok: `RELEASE-READINESS.md`, `LMS – activity manifest.md`, `LMS – H5P runtime acceptance.md`, `Gyermekvédelem – release gate.md`, `Adatvédelem – tanulói adatok és AI.md`, `Terepgyakorlat – 2. félév.md`.
''')


# ---------------------------------------------------------------------------
# Terminology: do not silently overwrite an internal convention; surface conflict.
# ---------------------------------------------------------------------------
GLOSS = "02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md"
text = read(GLOSS)
notice = r'''> ⚠️ **Nyitott helyi terminológiai gate (2026-08-25):** a jelen glosszárium több helyen `madrich` / `chanich` alakot nevez kánoninak, miközben a Hasomer Hacair Hungary aktuális nyilvános felületei és a Somer–Magyar szótár jellemzően `madrih` és `hánih` / `hanih` alakot használnak. A nyilvános oldalak korosztályi terminológiája sem teljesen egyezik a repo 4-kvucás történeti modelljével. **Ezt nem automatizáljuk tömeges átírással.** A helyi ken/országos mozgalmi felelősnek egyetlen house style-t és a 2026-os korosztály-architektúrát írásban jóvá kell hagynia; utána lintelt, atomi terminológiai migráció szükséges.'''
if "Nyitott helyi terminológiai gate (2026-08-25)" not in text:
    # Insert after first introductory quote block.
    idx = text.find("\n---")
    if idx == -1:
        raise RuntimeError("Glossary intro separator not found")
    text = text[:idx] + "\n\n" + notice + "\n" + text[idx:]
write(GLOSS, text)


# ---------------------------------------------------------------------------
# Study Labs: public completion/status boards -> private check + anonymous topic need.
# ---------------------------------------------------------------------------
for path in (ROOT / "02 Tervezet/Modulok").glob("M*/Peulák/*F*.md"):
    text = path.read_text(encoding="utf-8")
    changed = False
    # Add a universal privacy rule where a Study Lab is present.
    if "Study Lab" in text and "**Study Lab progress-privacy szabály:**" not in text:
        marker = "## 1."
        pos = text.find(marker)
        rule = "\n> **Study Lab progress-privacy szabály:** azt, hogy ki melyik leckével maradt el vagy mit teljesített, **nem tesszük ki névvel nyilvános sticker/post-it/progress boardra**. A státuszt a tanuló privát self-checkben és a képző a Moodle/privát mentorlistán látja. A közös falra legfeljebb anonim témakérés kerülhet: *„Miben kérsz ma segítséget?”*\n\n"
        if pos >= 0:
            text = text[:pos] + rule + text[pos:]
        else:
            text = rule + text
        changed = True
    # Neutralize obvious public progress board phrases without trying to infer hidden LMS state.
    replacements = {
        "vizuális „progress bar”": "privát önellenőrző lista",
        "vizuális progress bar": "privát önellenőrző lista",
        "sticker": "anonim témakérő cetli",
    }
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            changed = True
    if changed:
        path.write_text(text.rstrip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Audit report and evidence map.
# ---------------------------------------------------------------------------
write("01 Fejlesztés/04 Audit/2026-08-25 Release audit.md", r'''# Release audit – 2026-08-25

## Scope

Teljes repository- és commit-history alapú stabilizáció Anna 2026.07.20–08.12 közötti kézi auditja után. A vizsgálat kiterjed: konstruktív alignment, modulok/kapuk, safeguarding, kiskorúak/adatvédelem, AI, fejlődéslélektan, Moodle/H5P implementálhatóság, accessibility, repo-integritás, terminológia, program-transzfer és release-governance.

## Eredmény

**Pedagógiai architektúra: erős. Release: NO-GO a globális kapuk lezárásáig.**

A stabilizáció objektíven javítható regressziókat javít (duplikátumok, törött útvonalak, belső ellentmondások, félrevezető runtime/jogi állítások), de nem hamisít szakértői aláírást.

### Kritikus, végrehajtott változások

- M1/M3 duplikált kánoni fájlok eltávolítása és linkkorrekció.
- M1 feedback/alignment és titoktartási keret korrekció.
- M3 jogi szerepleírás pontosítása; kiskorú madrich nem kap önálló hatósági/jogi döntéshozó szerepet.
- M3.2 determinisztikus életkori/„amygdala gáz – PFC fék” állítások helyett fejlődési heurisztika + egyéni/context variability.
- M3.B súlyos safeguarding-helyzeteknél harmadik személyű esetanalízis az alapértelmezés, nem traumatizáló szerepjáték.
- M6.A kiesés/székszerző ellentmondás megszüntetése.
- M6.4 cél ↔ completion alignment: legalább 3 eset.
- AI Act provider/deployer kötelezettségek szétválasztása; C2PA best practice, nem univerzális deployer-kötelezettség.
- M7 külső AI: szervezetileg jóváhagyott eszköz, kiskorú terms/permission, no-AI alternatíva, sensitive-data tiltás.
- M7.4 v1/v2 fogalmi rend: M7.4 = v1, M7.B után = v2.
- Z.3 minor-role korrekció; Z.4 unsupported H5P Documentation Tool resume helyett Moodle Assignment draft.
- Accessibility: prerecorded synchronized videónál captions-követelmény egyértelmű.
- Release governance, LMS manifest, runtime acceptance, privacy, safeguarding és terepgyakorlati kontrollréteg hozzáadva.

## Külső validáció – elsődleges / magas minőségű források

- Gyvt. 17. §, Nemzeti Jogszabálytár: https://njt.hu/
- 2026 gyermekjóléti módszertani útmutató és jelzőrendszeri protokoll, kormányzati források.
- GDPR, különösen Article 8: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EU AI Act, konszolidált Article 50: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- WCAG 2.2, SC 1.2.2: https://www.w3.org/TR/WCAG22/
- H5P Documentation Tool / Branching Scenario community + official docs: https://h5p.org/
- OpenAI aktuális Terms/age requirements: https://openai.com/policies/terms-of-use/ és https://help.openai.com/
- Kirschner & De Bruyckere (2017), digital native/multitasker myth.
- Frontiers in Psychology (2024), learning-styles matching meta-analysis, DOI 10.3389/fpsyg.2024.1428732.
- Kortárs adolescent-development áttekintések és nagy mintás executive-function kutatások: Nature Reviews Neuroscience / Nature Communications.
- Hasomer Hacair Hungary aktuális nyilvános Somer–Magyar szótár és programoldalak: https://somer.hu/

## Nem automatizálható P0

A `RELEASE-READINESS.md` globális kapui. Ezeket issue-ként is nyitni kell, felelőssel és bizonyítékkal kell lezárni.
''')

print("release stabilization applied")
