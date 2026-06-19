# OPINION-AUDIT — Egy AI-szakvélemény adverzális ellenőrzése

**Tárgy:** A Hasomer Hacair madrichképzésről készült AI-szakvélemény 14 állításának (C1–C14) adverzális, bizonyíték-alapú felülvizsgálata.
**Módszer:** Állításonként belső (korpusz: `02 Tervezet/…`) és külső (szakirodalom) bizonyíték, a legjobb cáfolat, majd kalibrált újrafogalmazás.
**Dátum:** 2026-06-19

---

## 1. Vezetői összefoglaló

| Verdikt | Darab |
|---|---|
| **Alátámasztott** (substantiated) | 5 |
| **Részben alátámasztott** (partially-substantiated) | 7 |
| **Túlzó** (overstated) | 2 |
| **Megalapozatlan** (unsupported) | 0 |
| **Összesen** | 14 |

**Őszinte összértékelés.** A szakvélemény összességében megáll a lábán: a 14 állításból egy sem bizonyult teljesen megalapozatlannak, és öt minden lényeges ponton tartható. Nem "levegőbe beszélés" — a megfigyelések túlnyomó része konkrét, a korpuszban visszakereshető tényhez vagy mértékadó szakirodalomhoz horgonyzott, és a szerző gyakran épp azokat a feszültségeket nevezi meg, amelyeket a program saját belső auditja (`GATE-VALIDITY.md`, `IDEOLOGY-GATE-REVIEW.md`) is dokumentál. A gyengeség mintázatos és kétféle: (a) **komparatív túlnyúlás** — a "ritka", "a mezőny fölött áll", "tipikus fölött" típusú állítások head-to-head benchmark nélkül a szerző saját, igazolatlan értékelői hozzátoldásai (C1, C10, részben C4); (b) **részleges hiány globálissá tágítása** — a "mérőeszközei nem léteztek" (C5), "csak kvízzel mér" (C6), "rendre alulbecsült" (C7) megfogalmazások egy lokalizált, 3–4 modulra szűkíthető jelenséget egész-program-szintű ítéletté nagyítanak. A magállítások iránya szinte mindenütt helyes; a kalibráció jellemzően nem megfordít, hanem visszametsz a túlzó kvantorokról ("rendre", "egyik sem", "nem léteztek") a pontos hatókörre.

---

## 2. Állításonkénti elemzés

### C1 — Curriculáris ív · **OVERSTATED** · magabiztosság: magas

**Eredeti állítás:** A programnak valódi curriculáris íve van ("ki vagyok én (M1–M2) → kikkel dolgozom (M3–M4) → mivel (M5–M6) → hogyan áll össze egy peulává (M7) → zárás (Z)"). Ez ritka egy madrichképzésben.

**Belső bizonyíték:**
- `02 Tervezet/Program terv.md:33-40` — §0.4 explicit ív-leírás, de M3–M4 itt **"Kikkel ÉS HOGYAN dolgozom"**, nem tisztán "kikkel" (M4 = kiállás/kérdezés/kommunikáció = "hogyan").
- `02 Tervezet/MODULOK/M7/M7 – „Peula a papírtól a valóságig"…md:195-203` — capstone-átkötés-tábla: a Peula v2 a korábbi modulok kész produktumaira épít (M1 SBI / M2 érték / M3 safety+kvuca / M5 módszer / M6 játéklap). Erős bizonyíték, hogy az ív **tartalmilag is kumulatív**.
- `02 Tervezet/MODULOK/Z/Z – „Zárás & híd a terepre".md:17,25-26,40,78` — a Z modul ténylegesen visszatekint az M0–M7 ívre.
- Korpusz-szintű grep (`ritka|más képzés|hagyományos madrich|egyedülálló`) — **nulla** összehasonlító állítás más madrichképzésekről.

**Külső bizonyíték:** —

**Legjobb ellenérv:** A "ritka egy madrichképzésben" összehasonlító, empirikus állítás, amelyhez a korpusz nulla bizonyítékot ad — nincs benchmark, ez tisztán a szerző igazolatlan külső értékelése (ráadásul vitatható: a kompetenciaalapú ív sok modern nonformális képzésben bevett). Másodszor: a négyfázisú besorolás M3–M4-et illetően leegyszerűsít. Az ív LÉTE viszont nem cáfolható.

**Kalibrált újrafogalmazás:** *"A programnak valódi, jól dokumentált curriculáris íve van (én → kikkel és hogyan → mivel → peulává szintézis → zárás), amelyet a modulok közötti explicit visszakötések (M7 capstone, Z visszatekintés) is alátámasztanak; a négyfázisú leegyszerűsítés M4-et illetően kissé pontatlan, a 'ritkaság' pedig a korpusz alapján nem igazolható állítás."*

---

### C2 — Someres beágyazás · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A someres beágyazás átszövi az egészet és hiteles: dugma ishit, kvuca-központúság, a három pillér nem ráaggatott dísz, hanem szervező elv.

**Belső bizonyíték:**
- `02 Tervezet/Program terv.md:44-45` — explicit pedagógiai elv: "Dugma ishit…", "Kvuca-központúság: minden modul vissza van kötve a kvuca valóságához".
- `02 Tervezet/MODULOK/M2/M2 – KAPU – értékelő (item-bank + rubrika).md:30-37` — a mastery-kapu someres dimenziókat MÉR (someres érték, pillér-kapcsolat, dugma ishit-vállalás).
- `02 Tervezet/MODULOK/M2/M2_ONLINE_LECKE/M2.3 – Somer 3 pillére – mini-kapszula.md:37-156` — a három pillér konkrét kvuca-szituációhoz kötve.
- `02 Tervezet/MODULOK/M5/M5_ONLINE_LECKE/M5.3 … spacing.md:119-245` — még a generikus tanuláselméletet is someres helyzetekre fordítja.
- **Ellenbizonyíték:** M1 főfájl (Johari + SBI): somer=0, dugma=0, kvuca=1 — a someres réteg itt majdnem teljesen a peula/madrich-keretezésre szűkül.
- **Ellenbizonyíték:** a "pillér" érdemben csak az M2 fájljaiban fordul elő; a többi 7 modulban szervező elvként nem jelenik meg.
- `02 Tervezet/GLOSSZÁRIUM – someres és pedagógiai fogalmak.md:18-33,140` — kánoni terminológiai fegyelem.

**Külső bizonyíték:** —

**Legjobb ellenérv:** A "három pillér mint szervező elv" tag túloz: a pillérek tényleges szervező-elv funkciója egyetlen modulra (M2) korlátozódik, és ott is slogan-szintű. A kvuca és a dugma ishit tartja ki az "átszövi az egészet" állítást, a pillér nem. Az eloszlás egyenetlen (M1-ben minimális). A "hiteles" jelző részben nem auditálható — objektíven csak a konzisztencia és a nem-felületesség igazolható.

**Kalibrált újrafogalmazás:** *A someres beágyazás következetesen átszövi a képzést és nem felületi dísz; a kvuca-központúság és a dugma ishit valódi, minden modulra kiterjedő, a kapu-rubrikákban mért szervező elv. A "három pillér" viszont az M2 lokális gerince, nem az egész képzés átfogó szervező elve, és az eloszlás egyenetlen (M1-ben a someres réteg minimális). A "hiteles" objektíven konzisztencia és nem-felületesség formájában igazolható.*

---

### C3 — Ideológiai mélység híg · **SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** Az ideológiai mélység helyenként híg: a szocializmus-pillér interperszonális csapatmunka-etikára szűkül, a cionizmus "kapcsolat Izraellel"-re, a hagshamát a programterv ígéri, de egyik modul sem operacionalizálja.

**Belső bizonyíték:**
- `MODULOK/M2/M2_ONLINE_LECKE/M2.3 … SLIDE 2 (124–140)` — Szocializmus = "kvuca, egyenlőség, közös döntés, felelősségmegosztás, szolidaritás a gyengébbekkel" — interperszonális etika, strukturális dimenzió nélkül.
- `M2.3 … SLIDE 4 (211–239)` — a szocializmus-szituáció a feladatelosztás méltányossága, nem társadalmi/gazdasági szocializmus.
- `M2.3 … SLIDE 3 (171–177)` — cionizmus szó szerint "kapcsolatunk van Izraellel".
- **Grep:** "hagshama/hagshamá" **0 előfordulás** a MODULOK alatt; kizárólag `Program terv.md` 15., 17., 78. sorában (ígéret/keret szinten).
- `MODULOK/M2/M2 – KAPU … .md:174 (R3) és :34` — elég "legalább 1 pillér" konkrét helyzethez kötése; a tanuló a másik két pillért kihagyhatja.

**Külső bizonyíték:**
- https://www.hhnabogrim.com/three-pillars-of-hashomer-hatzair.html
- https://www.hholami.com/copy-of-history
- https://en.wikipedia.org/wiki/Hashomer_Hatzair
- https://www.hashyaus.org/ideology

**Legjobb ellenérv:** A hígulás valójában egyetlen modul (M2) egyetlen 15 perces leckéjének (M2.3) sajátja — ott viszont a vékonyítás tudatos pedagógiai döntés (cél: dugma ishitté fordítás 15+ kezdőknek), és a cionizmust/szocializmust viselkedési szinten operacionalizálja is (essay + M2-kapu R3). Tehát NEM igaz, hogy "egyik modul sem operacionalizálja" — pontosabban a hagshamát nem operacionalizálja egyik sem. De mivel a hagshama-rész (0 modulbeli operacionalizálás) és a szocializmus interperszonális szűkítése kitart, a verdikt substantiated marad.

**Kalibrált újrafogalmazás:** *Az ideológiai mélység tényleg híg, és gyakorlatilag az M2.3 leckére koncentrálódik: a szocializmus interperszonális kvuca-etikára szűkül (strukturális/kollektív vízió nélkül), a cionizmus relációs "kapcsolat Izraellel"-re (bár kísérő réteggel: kritikus gondolkodás, béke, méltóság), a hagshama pedig a teljes MODULOK-korpuszban 0-szor szerepel — egyetlen modul sem operacionalizálja. A cionizmust/szocializmust az M2-kapu viselkedési szinten azért operacionalizálja, csak ideológiailag vékonyan.*

---

### C4 — Gyerekvédelmi tudatosság · **SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A gyerekvédelmi tudatosság jelen van és a youth-work mezőny fölött áll: "nem vagy terapeuta" keret, jelzési lánc/escalation, dedikált M3 modul, titoktartás-korlátok.

**Belső bizonyíték:**
- `MODULOK/M0/M0_ONLINE_LECKE/M0.2 … .md` SLIDE 4 (160-187) — négylépéses jelzési folyamatábra; "nem terapeuta vagy, hanem dugma ishit" keret (sor 22).
- `MODULOK/M3/M3_ONLINE_LECKE/M3.3 – „Gyerekvédelem 101".md` 78-100 (titoktartás-korlát), 229-235 (akut önveszély: 112 / 116-123), 287-293 (meghallgatni szabad, nyomozni nem), 323-328 (NE konfrontáld).
- `MODULOK/M3/M3 – KAPU … .md` 18-28 (ÉLES gate ≥80% + kritikus itemek), 290-301 (R2 titoktartás és R4 nem-nyomoz/nem-konfrontál BLOKKOLÓ sorok).
- `M3.3:1-10` és `M3-KAPU:5-6` — ⚠️ kötelező gyerekvédelmi felelős review, név/dátum **még nyitott placeholder** (⟬kitöltendő⟭).
- `Program terv.md:80,93,234,244` — program-szinten is rögzítve; 18 fájl érinti.

**Külső bizonyíték:**
- https://nya.org.uk/wp-content/uploads/2024/02/Safeguarding-for-youth-work-main-editable-1.pdf
- https://learning.nspcc.org.uk/child-abuse-and-neglect/recognising-and-responding-to-abuse
- https://www.childsafeguardingconsultant.co.uk/safeguarding-training-for-volunteers-overcoming-challenges-and-maximising-impact/

**Legjobb ellenérv:** A komparatív "youth-work mezőny fölött áll" megfogalmazásnak nincs head-to-head benchmarkja — design-szintű, papíron-mért becslés. Másodszor: a biztonsági réteg élesedése feltételhez kötött és jelenleg befejezetlen (felelős neve, dátum, helyi protokoll-illesztés még placeholder). Harmadszor: a tartalom formatív-önreflexiós ("csak a mentor látja"), nem terepi kompetenciamérés.

**Kalibrált újrafogalmazás:** *A megírt tananyagban a gyerekvédelmi keret a recognized youth-work standard fölött részletezett és kemény, blokkoló-soros mastery-kapuval védett — feltéve, hogy az élesítés előtti gyerekvédelmi felelős-review és a helyi protokoll-illesztés ténylegesen megtörténik. Mind a négy elem (nem-terapeuta keret, eszkalációs lánc, dedikált M3, titoktartás-korlát) dokumentáltan jelen van.*

---

### C5 — Mastery-kapuk leírva, de nem megépítve · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A mastery-kapuk eredetileg le voltak ÍRVA, de nem voltak megépítve (item-bankok és rubrikák hiányoztak) — egy "mastery" program, aminek a mérőeszközei nem léteztek.

**Belső bizonyíték:**
- `_AUDIT/GATE-VALIDITY.md:60` — M3 🔴: "A kapu-kvízhez NINCS megírva tényleges item-bank".
- `:62` — M3 🔴: "Az Assignment modulproduktumhoz NINCS értékelő rubrika".
- `:120` — M7 🔴: "A Moodle Quiz item-bankja nem létezik".
- `:124` — M7 🟡: a rubrika "példa" szintű, szintleírások nélkül.
- `:49` — M2 🔴: kapstone "NINCS hozzá rubrika".
- `:92` — M5 🟡: M5.4-hez nincs rubrika.
- **Ellenbizonyíték — `:36-38`** — M1 🟢: működő, performansz-alapú SBI-rubrika + H5P item-bank már az audit előtt.
- `Program terv.md:231-247` — a kapuk + küszöb-tábla deklarálva (LE VOLTAK ÍRVA).
- git `8b5c2f2` — a mérőeszközök a read-only audit (`e61cee4`) UTÁN, válaszként készültek el.

**Külső bizonyíték:** —

**Legjobb ellenérv:** Az "aminek a mérőeszközei nem léteztek" túl abszolút: az M1 éles kapunak már az audit előtt is volt működő SBI-rubrikája és H5P item-bankja. Az audit összesítése 🔴 10 · 🟡 23 · 🟢 11 — a hiány több helyen küszöb-/validitás-probléma, nem teljes hiány. A teljes hiány bizonyíthatóan M3, M7, M2-kapstone és M5.4 esetén áll fenn — 4 pont, nem az egész program.

**Kalibrált újrafogalmazás:** *A mastery-kapuk programszinten le voltak írva, és az éles kapuk EGY RÉSZÉNÉL (kiemelten M3, M7, részben M2, M5) a konkrét item-bank és/vagy rubrika tényleg hiányzott a kidolgozott anyagból — nem az egész program maradt mérőeszköz nélkül (az M1-kapunak volt működő rubrikája és item-bankja). A tényleges mérőeszközök az audit válaszaként készültek el.*

---

### C6 — Mérés-mód vs. tanítás-filozófia ellentmondás · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A program központi ellentmondása: nonformális nevelést hirdet ("a Somer nem suli"), de több éles kaput konvergens, egy-helyes-válaszos kvízzel mér (M3, M5) — a mérés módja ellentmond a tanítás filozófiájának.

**Belső bizonyíték:**
- `Program terv.md:77` — filozófia: "közösségi élményen, részvételen … nem frontális oktatással" (mellette).
- `MODULOK/M5/M5_ONLINE_LECKE/M5.1 … .md:328` — "a Somer nem suli, de nem is csak random lógás" (a kulcsmondat megvan).
- `_AUDIT/IDEOLOGY-GATE-REVIEW.md:58-63 §B` — a program SAJÁT auditja kimondja a feszültséget (erősen mellette).
- `MODULOK/M5/M5 – KAPU … .md:15-16` — kvíz ≥80% (10/12), egyetlen ✅ helyes válasz.
- **Ellene a "csak kvíz" framingnek:** `MODULOK/M3/M3 – KAPU … .md:16-25` — KÉTKOMPONENSŰ kapu (kvíz ÉS nyílt Assignment + rubrika); `M5 – KAPU:17-18` — kompozit (kvíz ÉS M5.4 produktum-rubrika).
- `IDEOLOGY-GATE-REVIEW.md:84-89 §B3` — az M3-kvíz konvergenciája gyerekvédelmi okból INDOKOLT.

**Külső bizonyíték:**
- https://pjp-eu.coe.int/en/web/youth-partnership/non-formal-learning
- https://www.coe.int/en/web/youth-portfolio/key-questions-about-the-portfolio
- https://www.intechopen.com/online-first/1241626 (Biggs constructive alignment)
- https://www.researchgate.net/publication/393946096 ("assessment drives learning")
- https://www.youthandpolicy.org/wp-content/uploads/2017/06/ord-yandp108.pdf

**Legjobb ellenérv:** A claim azt sugallja, hogy az M3/M5 kapuk "egy-helyes-válaszos kvízzel mérnek", miközben mindkét kapu dokumentáltan kétkomponensű — a blokkoló, valódi transzfer-bizonyítékot adó komponens egy NYÍLT, rubrikával értékelt produktum. Az M3 konvergenciája nem filozófiai hiba, hanem safeguarding-minimum (van helyes válasz). A kvízitemek szcenárió-alapúak. A "központi ellentmondás" túl erős.

**Kalibrált újrafogalmazás:** *Valós, a program saját auditja által is dokumentált feszültség, hogy a nonformális filozófia mellett az M3/M5 éles kapuk konvergens kvíz-komponenst is tartalmaznak — ez a "sulis" mérési logikát reprodukálja. De a kapuk KÉTKOMPONENSŰ kompozitok (kvíz + nyílt, rubrikával értékelt, someres-kompatibilis produktum), az M3-kvíz konvergenciája gyerekvédelmi okból részben legitim, a feszültség pedig leginkább az M5/M6 fogalom-kvíznél éles. Tehát részleges, lokalizálható feszültség, nem feloldhatatlan inkoherencia.*

---

### C7 — Terhelés alulbecsült · **OVERSTATED** · magabiztosság: magas

**Eredeti állítás:** A megadott terhelés (kb. 2–3 óra/modul) rendre alulbecsült: a peulák percbontásai feszítettek, a produktum- és kvíz-készítés ideje nincs beárazva.

**Belső bizonyíték:**
- `Program terv.md:13,60` — itt a kifogásolt "kb. 2–3 óra" összefoglaló becslés.
- **Cáfolat:** `MODULOK/M5 … .md:7-8` — "M5.4 produktum-készítés … akár 20–30 perc"; teljes terhelés 2,5–3,5 óra.
- **Cáfolat:** `MODULOK/M3 … .md:8` — 2,5–3,5 óra, "modulproduktum & kapu-kvíz ~30–45'" explicit beárazva.
- **Cáfolat:** `MODULOK/M1/M1_ONLINE_LECKE/M1.4 … .md:13-14` — "5–7 perc H5P + 10–15 perc Assignment".
- **Cáfolat:** `MODULOK/Z/Z … .md:8` — bontott produktum-idő (H5P ~15-20' + Assignment ~20-30' + feedback ~5-10').
- **Alátámasztás (peula-feszesség):** `MODULOK/M3/M3_PEULA/M3.B…md:74` — "reális, ha … feszesen tartod"; `M6.A:412-415`, `M7.B:218`, `M7.A:205` — "ha csúszik, rövidíts".
- **Részleges alátámasztás:** `M7.4:7` + `M7:8` — a Peula v2 csak "első vázlat" árazva 5-10 percre; a VÉGLEGES szintézis-produktum nincs külön órabecsléssel. M2/M4 nem bontja külön a produktum-időt.

**Külső bizonyíték:** —

**Legjobb ellenérv:** A M7 félévzáró Peula v2 a teljes félév szintézis-produktuma, amelynek végleges megírása plauzibilisen jóval több, mint az árazott 5-10 perc vázlat — erre tényleg nincs külön becslés. A puhább M0/M2/M4-nél a produktum-idő szintén nincs bontva. De a "rendre" (=mindenütt, szisztematikusan) nem áll: a frissebb modulfájlok felfelé korrigálták a sávot (3 óra fölé), és több helyen explicit beárazzák a produktum- és kvízidőt.

**Kalibrált újrafogalmazás:** *A peulák 45 perces percbontásai valóban feszesek (ezt a tervezet maga is jelzi és vágási pontokkal kezeli), és lokálisan akad alulbecslés (kiemelten az M7 végleges szintézis-produktum és a puhább M0/M2/M4 produktum-ideje). De a "rendre 2–3 óra" csak a programterv összefoglalója — a modulfájlok differenciált, gyakran 3 óra feletti sávot adnak, és a produktum-/kvízidő több modulban EXPLICIT be van árazva. A "rendre alulbecsült" és "nincs beárazva" általánosítás túlzó.*

---

### C8 — AI-generált, lyukas tartalom (307 hézag) · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A tartalom AI-generált volt és lyukas: kb. 307 helyen szavak/instrukció-stem-ek hiányoztak a tananyagból.

**Belső bizonyíték:**
- `_AUDIT/GAP-MAP.md:5` — "38 tananyag-doksi, 307 hiányjel. (+ 7 sablon-doksi, 44 jel.)".
- `_AUDIT/gap-map.json` — a 38 fájl `total` mezői összege pontosan 307 (script-tel reprodukálva).
- git `2a2c3bf` diff — nyers üres helyek írásjel előtt, pl. M1.1: "…hogy **tökéletes** legyél, hanem hogy **elfogadd**"; M0.A peulában 19 hézag.
- `_AUDIT/AUDIT.md:114` — független keresztmegerősítés a csonkaságról (M3.B 2.3-as safety-mondat).
- `GAP-MAP.md:412-416` — az "AI/ChatGPT" találatok a tananyag TÉMÁJÁRA vonatkoznak ("MINI AI-BLOKK"), NEM az eredetre; egyetlen audit-doksi sem bizonyítja az AI-eredetet.
- Auto-memória `content-gaps-must-be-rewritten.md` — maga is feltételként kezeli: "valószínűleg AI-generálás hagyott üres helyeket".

**Külső bizonyíték:** —

**Legjobb ellenérv:** (1) Az "AI-generált volt" ok-megjelölés bizonyítatlan: nincs prompt-nyom, modell-metaadat vagy generálási log; a hézagok fakadhatnak emberi szerkesztésből vagy a Yjs CRDT-konverzió/GC során elvesztett formázott placeholder-szavakból is. (2) A "307" számolás egy konkrét gap-detektálási heurisztikán nyugszik (innen a helyes "kb."); a 44 sablon-jel nem számít bele. A hézagok java kiemelendő tartalmi szó, nem "hiányzó instrukció".

**Kalibrált újrafogalmazás:** *A forrásban (AFFiNE/Yjs) determinisztikusan kimutatható, hogy kb. 307 helyen, 38 doksiban szavak/instrukció-stem-ek hiányoztak — ez mérhető és reprodukálható tény. Az "AI-generált volt" eredet-attribúció viszont közvetlen bizonyítékkal nem alátámasztott: valószínűsíthető hipotézis, de a hézagok éppúgy fakadhatnak emberi munkamenetből vagy a Yjs-konverzióból. A "307 hézag" tehát tény; az "AI-generált" hipotézis.*

---

### C9 — Gen Z / 15+ hangolás · **SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A Gen Z / 15+ célcsoportra hangolás jól eltalált: tegező hangnem, emoji self-report, "passz"-opció, érzelmi biztonsági üzenetek, rövid mikroleckék.

**Belső bizonyíték:**
- `Program terv.md:53-54` — célcsoport explicit: "15+ éves képzős madrichok".
- `MODULOK/M1/M1_ONLINE_LECKE/M1.1 … .md:101` — "Cél: érzelmi biztonság, Gen Z/Alpha »emoji self-report«".
- `M1.1:126-139` — emoji-skála (😊/😬/😴/😵‍💫) + "nincs jó/rossz".
- `M1.1:61` (és M2.1:63, M3.1:57, M6.1:60, M7.2:124) — "Tegező, barátságos hang, max. 10–12 szavas mondatok".
- `Program terv.md:221 §6` — "a hangnem tegező és bátorító".
- "passz"-opció szó szerint legalább 10 peulában (M0.A, M1.A, M3.B, M7.B …).
- `M1.A:84` — "Safe-space jelzése: lehet passzolni"; `M1.1:288, M3.1:240, M3.3:353` — "nincs jó vagy rossz válasz".
- `Program terv.md:59,203` — "4×10–20 perc mikrolecke", Hook–Input–Activity–Check.

**Külső bizonyíték:**
- https://www.commlabindia.com/blog/microlearning-genz-corporate-learners
- https://www.engageemployee.com/blog/gen-zs-workplace-imperative-psychological-safety-in-the-workplace
- https://www.solidaritynow.org/wp-content/uploads/2025/02/Manual-Trauma-Informed-Youth-Work_ENGLISH_compressed.pdf

**Legjobb ellenérv:** A "jól eltalált / jól sikerült" minőségi minősítés: a korpusz az eszközök szándékolt, következetes JELENLÉTÉT bizonyítja, de nincs pilotteszt, A/B-mérés vagy célcsoport-visszajelzés, ami a hatékonyságot igazolná. Másodlagos: a célcsoport valójában 15+ felnőtt-közeli madrichképzők, nem klasszikus 12–14 éves tinik. Harmadik: a "rövid mikrolecke" relatív (10–20 perc tagoltabb, de hosszabb a microlearning 3–5 perces ideáljánál).

**Kalibrált újrafogalmazás:** *A program tervezési szinten következetesen és evidenciaalapúan Gen Z / 15+-re van hangolva (tegező hangnem, emoji self-report, passz-opció, érzelmi biztonsági üzenetek, rövid mikroleckék) — mind a hat eszköz rendszerszinten, dokumentáltan jelen van. A tényleges célcsoport-hatékonyság empirikus visszamérése (pilot, visszajelzés) viszont még előttünk áll; a "jól eltalált" jelenleg megalapozott tervezési ígéret, nem mért eredmény.*

---

### C10 — A tipikus mozgalmi képzés fölött áll · **PARTIALLY-SUBSTANTIATED** · magabiztosság: közepes

**Eredeti állítás:** Ez a strukturáltsági/tudatossági szint a TIPIKUS ifjúsági-mozgalmi vezetőképzés (hétvégi szeminárium + árnyékolás) fölött áll.

**Belső bizonyíték:**
- `Program terv.md §3.1 (88-99)` — 9 modulblokkos blended ív, modulonkénti kompetenciafókusz, mátrix.
- `Program terv.md §5 (231-247)` — explicit puha vs. éles kapuk, kanonikus küszöb-tábla (M1 ≥5/8; M3 ≥10/12 + R2/R4 blokkoló; M7 ≥17/24).
- `Program terv.md §4, §7 (200-278)` — WCAG/GDPR-szintű akadálymentesítés + learning-analytics.
- A C10 állítás szó szerint NEM szerepel a `_AUDIT` korpuszban — ez külső értékelői normatív állítás.

**Külső bizonyíték:**
- https://www.youthandpolicy.org/articles/becoming-a-youth-worker/
- https://campshomria.com/pages/counselors-hadracha
- https://www.salto-youth.net/youthworkers-competence-model/ (ETS — ELLENBIZONYÍTÉK a túlzásra: a kompetenciaalapú képzés nem újszerű; "guidance, nem gatekeeping")
- https://scoutship.scout.org/handbook/competency-based-approach-in-training/

**Legjobb ellenérv:** A "TIPIKUS" baseline karikírozott: a "hétvégi szeminárium + árnyékolás" a szektor gyengébb/informális végét írja le, és figyelmen kívül hagyja a kompetenciaalapú, curriculum-vezérelt, demonstrációval értékelt képzést (SALTO ETS, cserkész competency-based). Az állítás emellett normatív és mérhetetlen (nincs definiált populáció, sem "strukturáltság" metrika).

**Kalibrált újrafogalmazás:** *A program strukturáltsága és értékelési-tudatossága a mozgalmi madrichképzés JELLEMZŐ alapszintje (hadracha-szeminárium + árnyékolás, mastery-küszöb nélkül) fölött van — a kemény, blokkoló mastery-kapuk ráadásul ritkábbak még a strukturált EU/cserkész kereteknél is (azok inkább "guidance"). De a "mezőny fölött / újszerű" olvasat nem tartható: a kompetenciaalapú, curriculum-vezérelt ifjúsági vezetőképzés már létező, elismert gyakorlat. Az állítás iránya védhető, de nem kvantifikálható.*

---

### C11 — Konvergens kvíz vs. nonformális feszültség (szakirodalom) · **SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A konvergens mastery-kvízek pedagógiailag feszültségben állnak a nonformális/experiential neveléssel; a szakirodalom (Council of Europe, authentic assessment) ezt alátámasztja.

**Belső bizonyíték:**
- `MODULOK/M5/M5 – KAPU … .md` (Kapu-meta) — konvergens, egy-helyes-válaszos kvíz (12 item, ✅), ≥80%, 2-3 próbálkozás.
- `M5 – KAPU` ("Modul-szintű pass-szabály") — a tervezet maga kezeli a feszültséget: kompozit kapu (kvíz ≥80% ÉS rubrika), hivatkozva a `GATE-VALIDITY.md` "construct-rés" findingra.
- `GLOSSZÁRIUM … .md:124-128` — "a Somer NEM suli" szembeállítva a mastery-kapu definíciójával.
- `M5 – KAPU` (Distraktor-elv) — magyarázó/visszairányító feedback = feszültséget enyhítő formatív elem.

**Külső bizonyíték:**
- https://pjp-eu.coe.int/en/web/youth-partnership/non-formal-learning
- https://www.coe.int/en/web/youth/trayce
- https://files.ascd.org/staticfiles/ascd/pdf/journals/ed_lead/el_198904_wiggins.pdf (Wiggins, "Teaching to the (Authentic) Test")
- https://journals.sagepub.com/doi/abs/10.1177/003172171109200721 (Wiggins, "A True Test")
- https://kognity.com/resources/retrieval-practice/ + https://files.eric.ed.gov/fulltext/EJ1303358.pdf (ELLENPÓNT: low-stakes retrieval-practice mint legitim formatív eszköz)

**Legjobb ellenérv:** A "feszültség" szó túlfeszítése. (1) A feszültség létezik, de NEM jelent összeférhetetlenséget: a low-stakes, többpróbálkozós, magyarázó-feedbackes mastery-kvíz formatívan megfér az experiential pedagógiával. (2) A CoE/Wiggins-források elsősorban a SUMMATÍV, magas tétű, rangsoroló tesztet bírálják; egy nem-rangsoroló mastery-küszöbkvíz részben kívül esik a célponton. (3) A korpusz construct-illesztése (kvíz a deklaratív tudásra, rubrika+produktum az alkalmazói kompetenciára) jelentősen csökkenti a feszültséget. De a "feszültségben állnak" megfogalmazás óvatos, ezért substantiated.

**Kalibrált újrafogalmazás:** *A konvergens, küszöbös kvízek valós pedagógiai feszültségben állnak a nonformális/experiential nevelés alapelveivel — ezt mértékadó források (CoE nonformális nevelés; Wiggins authentic assessment) alátámasztják. FONTOS: ez feszültség, nem összeférhetetlenség — a low-stakes, többpróbálkozós, magyarázó-feedbackes mastery-kvíz formatív eszközként kiegészítheti az experiential megközelítést. A feszültség akkor válik valódi problémává, ha a kvíz az EGYETLEN/DOMINÁNS éles mód; a korpusz ezt kompozit kapuval tudatosan kezeli.*

---

### C12 — Túl-építés / fenntarthatósági kockázat · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** Túl-építés kockázata: egy ilyen LMS + H5P branching + learning analytics + AI rendszer NEHÉZ egy önkéntes-vezetésű mozgalomnak; a rendszer és az önkéntes kapacitás közti szakadék valós, dokumentált kockázat.

**Belső bizonyíték:**
- `01 Fejlesztés/02 Interjúk/02 Adaptív L&D felvételi interjú - jelentés - angol.md:116` — kapacitás: 2 képző (4-5 h/hét) + 1 admin; a #1 nevesített kockázat.
- `:106-112` — üzemeltetési owner-mátrix (Moodle Trainer-1, Discord Trainer-2, Admin), fallback-láncok.
- `Program terv.md:200-207 §4` — érdemi build (Moodle + H5P Course Presentation/Interactive Video/Branching/Question Set, AI-média human-in-the-loop).
- `Program terv.md:282-291 §7` — a "learning analytics" valójában KÖNNYŰ és MANUÁLIS (LMS-export + évi egyszeri kézi elemzés), NEM automatizált motor — ez gyengíti a claim technikai-súly állítását.
- `_AUDIT/ARCHITECTURE-REVIEW.md` — a deep-audit maga dokumentálja a karbantartási terhet (M0 belépő-kvíz nincs megírva, M3 item-logika nincs implementálva, elavult riportok).
- `:117,35` — beépített enyhítés: "−30% Moodle load vizsgaidőszakban", "minimal admin, nudges".

**Külső bizonyíték:**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6329426/ ("Pilotitis")
- https://onlinelibrary.wiley.com/doi/full/10.1002/nml.21609 (Godefroid 2024, nonprofit tech-adopció)
- https://www.tandfonline.com/doi/full/10.1080/2331186X.2024.2400415
- https://www.researchgate.net/publication/345693588
- https://www.zehntech.com/learning-management-system-implementation-fails-what-not-to-do/ + https://www.d2l.com/blog/nonprofit-lms/

**Legjobb ellenérv:** (1) A technikai súly túlbecslése: a §7 analytics manuális, az AI csak tartalom-generálásra szolgál (nem adaptív tutor) — a "LMS + H5P branching + learning analytics + AI rendszer" megfogalmazás súlyosabbnak fest egy sztenderd Moodle+H5P kurzust. (2) A stack érett, ingyenes/nyílt, kisszervezeteknél bevett — a valódi kockázat a tartalom-/kapu-karbantartás emberi munkaigénye, nem a rendszer. (3) A terv MÁR tartalmaz enyhítéseket. (4) Normatív/előretekintő állítás — a szakirodalom a kockázat LÉTÉT igazolja, a bekövetkezését nem.

**Kalibrált újrafogalmazás:** *A fenntarthatósági kockázat valós és dokumentált (2-képzős önkéntes stáb, a terv maga jelöli #1 kockázatnak), de a fő szűk keresztmetszet NEM a rendszer technikai komplexitása, hanem a folyamatos TARTALOM- és KAPU-karbantartás emberi munkaigénye. A §7 analytics manuális, az AI csak generálásra szolgál, a stack érett és nyílt, a terv pedig már tartalmaz enyhítéseket. Ezt explicit karbantartási tervvel (felelős, kadencia, item-bank gondozás, AI-lektorálás) érdemes lefedni — nem a rendszer leépítésével.*

---

### C13 — AI-tartalom emberi lektorálást igényel · **SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** Az AI-generált oktatási — különösen gyerekvédelmi/biztonsági — tartalom emberi szakértői lektorálást igényel; a mértékadó útmutatás (pl. UNESCO) ezt megköveteli.

**Belső bizonyíték:** —

**Külső bizonyíték:**
- https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
- https://discovery.ucl.ac.uk/id/eprint/10176438/1/Miao%20and%20Holmes%20-%202023%20-%20Guidance%20for%20Generative%20AI%20in%20Education%20and%20Resear.pdf ("must be critically evaluated before they are used", "safeguarded by human supervision")
- https://accme.org/resource/guidance-on-ai/ ("named, qualified individuals" — explicit must/required)
- https://www.schools.nyc.gov/about-us/vision-and-mission/artificial-intelligence/guidance-on-artificial-intelligence
- https://fas.org/publication/ensuring-child-safety-ai-era/

**Legjobb ellenérv:** A "megköveteli" (requires/mandates) szó precíz súlya: (1) a UNESCO-útmutatás nem jogilag kötelező, hanem ajánlás; a "mandating" szót maga a dokumentum kizárólag az adatvédelem és korhatár kapcsán használja, a tartalom-lektorálást "need/should/must be critically evaluated" fordulattal írja le. (2) A UNESCO hangsúlya a rendszerek intézményi validálásán van, nem minden generált elem darabonkénti szakértői lektorálásán. (3) A "gyerekvédelmi" kitétel a UNESCO-nál inkább a korhatár-ajánlásokban ölt testet. De a magállítás (emberi felülvizsgálat szükséges) több forrásban explicit "must/required" formában is megjelenik.

**Kalibrált újrafogalmazás:** *A mértékadó nemzetközi/ágazati útmutatás egyöntetűen elvárja, hogy az AI-generált oktatási tartalmat ember (lehetőleg szakértő) ellenőrizze felhasználás előtt, fokozott elővigyázatossággal a gyermekeknek szóló, biztonsági/gyermekvédelmi tartalomnál. A UNESCO esetében a "megköveteli" pontosabban "nyomatékosan elvárja/ajánlja" (need/should/must be critically evaluated; safeguarded by human supervision) — maga az útmutatás nem kötelező erejű; az explicit "named, qualified individuals" jóváhagyási kötelem más forrásoknál (ACCME, NYC Schools) jelenik meg.*

---

### C14 — Produktum-/peer-/reflektív értékelés mint alternatíva · **PARTIALLY-SUBSTANTIATED** · magabiztosság: magas

**Eredeti állítás:** A produktum-/peer-/reflektív értékelés elismert, nonformális-kompatibilis alternatíva a kvíz-kapukkal szemben, amely megőrzi a minőségbiztosítást.

**Belső bizonyíték:** —

**Külső bizonyíték:**
- https://www.tandfonline.com/doi/abs/10.1080/02602938.2020.1724260 (peer assessment validitása feltételhez kötött)
- https://www.sciencedirect.com/science/article/abs/pii/S0191491X22001109 (feladat-komplexitás csökkenti a validitást)
- https://www.lrdc.pitt.edu/schunn/papers/zhangetal-reliabilityvaliditychange.pdf (peer-tanár korreláció átlag r≈0,69)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11515314/ (Dunning-Kruger: 35,5% felülbecslés, ρ=-0,59)
- https://www.journals.ac.za/sajhe/article/view/6740 (a reliabilitás-félelem indokolatlan — FELTÉVE jó rubrika + felkészítés)
- https://wmich.edu/x/teaching-learning/teaching-resources/authentic-assessment (Wiggins; egyoldalú bemutatás)
- https://pjp-eu.coe.int/en/web/youth-partnership/youthpass
- https://erasmus-plus.ec.europa.eu/resources-and-tools/quality-standards-key-action-1

**Legjobb ellenérv:** A feltétel nélküli "megőrzi a minőségbiztosítást" túloz. (1) A self/reflektív értékelés validitása rendszeresen gyenge — épp a gyengébbek (akiket a kapu kiszűrne) becsülik túl magukat (Dunning-Kruger). (2) A peer-tanár korreláció csak mérsékelt (r≈0,69), komplex feladatnál csökken. (3) Az authentic assessment fő gyengesége a rater-szubjektivitás (hawk-dove). A rubrika javít, de nem szünteti meg. (Ellen-ellenérv: a kvíz-kapu sem ad ingyen minőségbiztosítást — magas reliabilitás mellett alacsony konstruktum-validitás.)

**Kalibrált újrafogalmazás:** *A produktum-, peer- és reflektív értékelés a szakirodalomban (Wiggins) és a nonformális keretrendszerekben (Youthpass, CoE Youth Portfolio, Erasmus+/EQAVET) elismert, a nonformális tanulással kompatibilis — sőt ajánlott — alternatíva, magasabb konstruktum-validitással, mint a felidézést mérő kvíz. A minőségbiztosítás azonban NEM automatikusan őrződik meg: csak akkor közelíti a kvíz-kapuk standardizált objektivitását, ha explicit rubrikák, értékelői kalibráció/moderáció és (peer/self esetén) tanulói felkészítés társul hozzá. Ezek a kísérő feltételek nélkül a self/peer-értékelés ismert torzításoknak van kitéve.*

---

## 3. Mit kell árnyalni (a túlzó / részben-állítások korrekciói)

1. **C1 (túlzó) — "ritka egy madrichképzésben":** törlendő vagy "a korpusz alapján nem igazolható" kitétellel; a négyfázis M3–M4-et "kikkel ÉS hogyan"-ként kell jelölnie.
2. **C2 (részben) — "a három pillér szervező elv":** a pillér az M2 lokális gerince, nem az egész képzésé; a kvuca és a dugma ishit tartja az "átszövi az egészet" állítást.
3. **C5 (részben) — "a mérőeszközei nem léteztek":** a hiány M3, M7, M2-kapstone és M5.4 esetén áll fenn (4 pont); az M1-kapunak volt működő rubrikája és item-bankja.
4. **C6 (részben) — "csak egy-helyes-válaszos kvízzel mér":** az M3/M5 kapuk kétkomponensű kompozitok (kvíz + nyílt produktum-rubrika); az M3 konvergencia gyerekvédelmi okból részben legitim; a feszültség leginkább M5/M6 fogalom-kvíznél éles.
5. **C7 (túlzó) — "rendre 2–3 óra, alulbecsült, nincs beárazva":** a "rendre" nem áll; a modulfájlok differenciált, gyakran 3 óra fölötti sávot adnak, és a produktum-/kvízidő több modulban beárazott. A valós mag: az M7 végleges szintézis-produktum + M0/M2/M4 produktum-idő.
6. **C8 (részben) — "AI-generált volt":** a 307 hézag tény; az AI-eredet bizonyítatlan hipotézis (lehet emberi vagy Yjs-konverziós ok is).
7. **C9 (alátámasztott, de árnyalandó) — "jól eltalált":** a jelenlét bizonyított, a hatékonyság empirikus visszamérése (pilot) még hiányzik; a célcsoport 15+ madrichképző, nem 12–14 éves tini.
8. **C10 (részben) — "a tipikus fölött":** irányban igaz, de a baseline karikírozott; a kompetenciaalapú képzés (SALTO ETS, cserkész) létező gyakorlat — "mezőny fölött / újszerű" nem tartható.
9. **C12 (részben) — "túl-építés, a rendszer nehéz":** a kockázat valós, de a szűk keresztmetszet a tartalom-/kapu-karbantartás emberi munkaigénye, nem a (manuális analytics + nyílt stack) technikai komplexitás; a terv már tartalmaz enyhítéseket.
10. **C13 (alátámasztott, de árnyalandó) — "UNESCO megköveteli":** a UNESCO nyomatékosan elvárja/ajánlja (nem jogi kötelem); a "named, qualified" jóváhagyási kötelem más forrásokból (ACCME, NYC) jön.
11. **C14 (részben) — "megőrzi a minőségbiztosítást":** csak feltételesen — explicit rubrika, értékelői kalibráció/moderáció és tanulói felkészítés mellett.
12. **C4 (alátámasztott, de árnyalandó) — "a mezőny fölött áll":** komparatív, benchmark nélküli rész; a biztonsági réteg élesedése feltételes (gyerekvédelmi felelős-review + helyi protokoll-illesztés még placeholder).

---

## 4. Forrásjegyzék (összes hivatkozott URL)

**Hasomer Hacair / ideológia (C3):**
- https://www.hhnabogrim.com/three-pillars-of-hashomer-hatzair.html
- https://www.hholami.com/copy-of-history
- https://en.wikipedia.org/wiki/Hashomer_Hatzair
- https://www.hashyaus.org/ideology

**Safeguarding / gyerekvédelem (C4):**
- https://nya.org.uk/wp-content/uploads/2024/02/Safeguarding-for-youth-work-main-editable-1.pdf
- https://learning.nspcc.org.uk/child-abuse-and-neglect/recognising-and-responding-to-abuse
- https://www.childsafeguardingconsultant.co.uk/safeguarding-training-for-volunteers-overcoming-challenges-and-maximising-impact/

**Nonformális nevelés / értékelés (C6, C11, C14):**
- https://pjp-eu.coe.int/en/web/youth-partnership/non-formal-learning
- https://www.coe.int/en/web/youth-portfolio/key-questions-about-the-portfolio
- https://www.coe.int/en/web/youth/trayce
- https://pjp-eu.coe.int/en/web/youth-partnership/youthpass
- https://erasmus-plus.ec.europa.eu/resources-and-tools/quality-standards-key-action-1
- https://www.intechopen.com/online-first/1241626
- https://www.researchgate.net/publication/393946096
- https://www.youthandpolicy.org/wp-content/uploads/2017/06/ord-yandp108.pdf
- https://files.ascd.org/staticfiles/ascd/pdf/journals/ed_lead/el_198904_wiggins.pdf
- https://journals.sagepub.com/doi/abs/10.1177/003172171109200721
- https://kognity.com/resources/retrieval-practice/
- https://files.eric.ed.gov/fulltext/EJ1303358.pdf
- https://www.tandfonline.com/doi/abs/10.1080/02602938.2020.1724260
- https://www.sciencedirect.com/science/article/abs/pii/S0191491X22001109
- https://www.lrdc.pitt.edu/schunn/papers/zhangetal-reliabilityvaliditychange.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11515314/
- https://www.journals.ac.za/sajhe/article/view/6740
- https://wmich.edu/x/teaching-learning/teaching-resources/authentic-assessment

**Gen Z / microlearning / trauma-informed (C9):**
- https://www.commlabindia.com/blog/microlearning-genz-corporate-learners
- https://www.engageemployee.com/blog/gen-zs-workplace-imperative-psychological-safety-in-the-workplace
- https://www.solidaritynow.org/wp-content/uploads/2025/02/Manual-Trauma-Informed-Youth-Work_ENGLISH_compressed.pdf

**Ifjúsági vezetőképzés / kompetenciamodellek (C10):**
- https://www.youthandpolicy.org/articles/becoming-a-youth-worker/
- https://campshomria.com/pages/counselors-hadracha
- https://www.salto-youth.net/youthworkers-competence-model/
- https://scoutship.scout.org/handbook/competency-based-approach-in-training/

**E-learning fenntarthatóság / nonprofit tech-adopció (C12):**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6329426/
- https://onlinelibrary.wiley.com/doi/full/10.1002/nml.21609
- https://www.tandfonline.com/doi/full/10.1080/2331186X.2024.2400415
- https://www.researchgate.net/publication/345693588
- https://www.zehntech.com/learning-management-system-implementation-fails-what-not-to-do/
- https://www.d2l.com/blog/nonprofit-lms/

**AI-tartalom emberi lektorálás (C13):**
- https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
- https://discovery.ucl.ac.uk/id/eprint/10176438/1/Miao%20and%20Holmes%20-%202023%20-%20Guidance%20for%20Generative%20AI%20in%20Education%20and%20Resear.pdf
- https://accme.org/resource/guidance-on-ai/
- https://www.schools.nyc.gov/about-us/vision-and-mission/artificial-intelligence/guidance-on-artificial-intelligence
- https://fas.org/publication/ensuring-child-safety-ai-era/

---

*Megjegyzés a hatókörről: ez a dokumentum a megadott 14 állítást és a hozzájuk csatolt verdikteket strukturálja és kalibrálja; a belső bizonyítékok a `02 Tervezet/` korpusz hivatkozott fájljaira és sorszámaira, a külső bizonyítékok a fenti forrásjegyzékre épülnek.*
