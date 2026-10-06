# Projektgazdai döntések — MAN completion és mentor-láthatóság, D-e…D-j (2026-10-05)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda 2026-10-05-i válasza a `2026-10-05 Validált findingok – MAN
> completion és mentor-láthatóság.md` 4. pontjának kérdéseire, szó szerint (1. szakasz). Előzmény: `2026-10-05
> Projektgazdai döntések – build-blocker leltár D-a…D-d.md`. Kánoni fájl nem változott; az átvezetés a `/course-fix`
> (illetve az M6.4-nél a `/course-develop`) feladata. Munkaág: `fix/moodle-build-hardening` @ `9ef2b25`.

## 1. A projektgazda válasza, szó szerint

```text
Projektgazdai döntések a validált MAN completion / mentor-visibility review alapján:

## D-e — M6.4 három szcenárió

Az M6.4 marad EGY Branching Scenario activity, de a tartalmat fix sorrendű három-szcenáriós lánccá kell alakítani.

Követelmény:

- a tanuló mindhárom külön szcenárión végigmegy;
- egy szcenárión belül lehetnek eltérő választási ágak;
- minden ág visszakonvergál a következő szcenárióra;
- az 1. vagy 2. szcenárió után semmilyen út nem vezethet a lesson end/completion screenre;
- a végső completion csak a 3. szcenárió után érhető el;
- a „legalább 3 külön szcenárió” követelmény nem gyengíthető.

Ne bontsd három külön Moodle activityre és ne használj staff checkpointot erre.

## D-f — BSPEC-07

`BSPEC-07` jóváhagyva.

Scope: azok a Moodle Assignment-alapú utak, ahol a submission és a mentor/staff confirmation két külön, Moodle-ban kódolandó állapot, és a jelenlegi manifest nem specifikálja a confirmation checkpointot.

## D-g — BS-D1 alkalmazása BSPEC-05-re

A BS-D1 szerinti `no independent fallback` megoldást jóváhagyom a BSPEC-05 soraira:

- LMS-M2-04
- LMS-M3-03
- LMS-M5-02
- LMS-M6-04

de csak akkor, ha a row-specifikus scored Branching Scenario + Moodle `Receive a grade` primary route a target Moodle-on determinisztikusan teljesíti a lesson completion semanticsot és átmegy a szükséges negatív runtime teszteken.

Ha ez bármelyik sornál nem bizonyítható, az activity BUILD BLOCKER marad. Ne találj ki Group-, kézi vagy más kerülő fallbacket.

M3.3 esetén külön ellenőrizd a teljes, mind a négy szcenáriót lefedő flow-t; a korábbi reviewer csak az elsőt olvasta végig.

## D-h — Assignment two-state pattern

A BS-D8-hoz hasonló kétállapotú mintát jóváhagyom BSPEC-07-hez:

1. `SUBMITTED`
   - a Moodle Assignment submission completionje;
   - azt a downstream activityt nyithatja, amelyhez a kánon szerint pusztán a leadás szükséges.

2. `CONFIRMED`
   - külön staff checkpoint;
   - azt a downstream/high-stakes/completion állapotot vezérli, amelyhez mentor/staff confirmation szükséges.

A két állapotot ne mosd össze.

A row-specifikus unlockokat a kánonból vezesd le; ne feltételezd, hogy minden Assignment ugyanazt nyitja.

## D-i — további unscored choice completion

D-d elve kiterjed:

- M0.3 SLIDE 7 → NEM önálló completion element
- M2.2 value choice → NEM önálló completion element

Ezek pedagógiai/reflektív interakciók lehetnek, de a választásuk önmagában nem gate-elheti a Moodle lesson completiont.

## D-j — M2.3 pillar branch storage

Somer-side döntés:

A M2.3 pillar-branch választásának learner accounttal összekötött tartós tárolása NEM pedagógiai követelmény, és nem kívánt adat.

- completionhez a branch identity tartalmát nem használjuk;
- reportban/manifestben ne állítsuk, hogy a konkrét pillar choice megőrzése szükséges;
- ha a core H5P attempt tracking technikailag mégis per-user eltárolja ezt az interactiont, annak adatvédelmi elfogadhatósága DPO/legal QA marad;
- ezt ne oldd meg feltételezéssel.

## Nem projektgazdai döntések

Továbbra is NYITVA maradnak, és /course-fix nem oldhatja meg őket feltételezéssel:

- BIZT-1 — disclosure eltávolítás / Memuna access / SLA
- BIZT-2 privacy része — editing teacher / manager / admin szélesebb P2 hozzáférése
- BIZT-5
- BIZT-6
- BIZT-7
- BIZT-8
- BIZT-10
- BIZT-12
- IMPL-11 DPO/legal része
- N-1, N-3, N-4…N-9
- BIZT-R5
- RT-P0-24
- G1/G2/G3b
- LMS-Z-06 retention
- PR-04

Rögzítsd D-e…D-j-t az audit trailben.
```

(A beillesztett üzenet utolsó mondata — „Ezután STOP, ne próbáld a slash skillt magadtól meghívni. Add vissza a pontos
/course-fix parancsokat, amelyeket nekem kell elindítanom.” — munkautasítás, nem döntés.)

## 2. Hatás a validált findingokra

| Döntés | Érintett finding | Következmény |
|---|---|---|
| D-e | IMPL-1 | eldöntve: egy BS activity, fix sorrendű háromszcenáriós lánc, a végképernyő csak a 3. szcenárió után; külön activity és stáb-checkpoint kizárva. A lánc a lecke jelentős átszerkesztése (navigáció, konvergencia) → `/course-develop` |
| D-f | IMPL-4 | BSPEC-07 jóváhagyva; `BUILD_SPEC_OPEN`-ként regisztrálandó |
| D-g | IMPL-3 (+ IMPL-1 sora) | a BSPEC-05 négy sorára „nincs független tartalékút” (BS-D1), feltételesen; M3.3: a teljes, négyszcenáriós flow ellenőrzése előírt |
| D-h | IMPL-5 | BSPEC-07 két állapota (`SUBMITTED`, `CONFIRMED`); a soronkénti unlock a kánonból |
| D-i | IMPL-10 | eldöntve: az M0.3 SLIDE 7 és az M2.2 értékválasztás nem önálló completion-elem |
| D-j | IMPL-11 (projektgazdai rész) | eldöntve: a pillér-ág választásának fiókhoz kötött tárolása nem követelmény és nem kívánt; a completion nem használja; a DPO/jogi QA-rész nyitva |

Az IMPL-2, IMPL-6, IMPL-7, IMPL-8, IMPL-9, BIZT-3, BIZT-4, BIZT-11 és a BIZT-2 objektív része döntés nélkül is javítható
(validált objektív findingok). A „Nem projektgazdai döntések” listája változatlanul nyitva.

## 3. A végrehajtáshoz nyitva maradó pontok (rögzítés, nem döntés)

1. **D-e — melyik három szcenárió.** A kánon ma négy szcenáriót ír (A–D; M6 hub :119 „4 szcenárió … legalább 3
   különböző ágat kell végigjátszani, a 4. opcionális”; M6.4 :79, :104, :133, :162). A D-e háromszcenáriós láncot ír,
   de nem nevezi meg, melyik hármat, milyen sorrendben, és mi lesz a negyedikkel (elhagyás; a végképernyő utáni,
   completionön kívüli gyakorlás; vagy négytagú kötelező lánc). Kánoni háttér a választáshoz: az M6 kapu item-bankja
   a 11–12. itemet az M6.4 B-ágához köti (M6 kapu :64); a D-ág saját biztonsági blokkot tartalmaz (M6.4 :833); az M6
   biztonsági korlátja szerint kirekesztés-szimuláció nincs. **Eldöntve (4. szakasz, D-e pontosítás):** A → B → D
   kötelező, a C opcionális bónusz.
2. **D-g — a feltétel és a build-verdikt viszonya.** A feltétel része a célverzión futó negatív runtime-teszt, ami
   csak a staging build után keletkezhet; a release-modell v2 (RR :7) szerint ilyen bizonyíték a build-verdiktet nem
   blokkolja. Két következetes rögzítés lehetséges: (a) a BSPEC-05 sorai a specifikáció szintjén `RESOLVED`-ra
   kerülhetnek (rögzített determinisztikus primary route, BS-D1/D-g), kifejezett feltétellel: ha az RT-P0-02, -05,
   -09, -10, -11 vagy -18 negatív esete a célverzión elbukik, az érintett sor `BUILD_SPEC_OPEN`-re nyílik vissza;
   (b) a sorok a runtime-bizonyítékig `BUILD_SPEC_OPEN`-ek maradnak — ez a buildet a csak buildből keletkező
   bizonyítékra várakoztatja (a v2 által megszüntetett körkörösség). **Eldöntve (4. szakasz, D-g pontosítás):** (a).
3. **D-j — az M2 hub analitikai mutatója.** Az M2 hub :214 („Melyik pillérnél … állnak meg sokan M2.3-ban”) a
   pillér-választást mutatóként használja; a `/course-fix` ellenőrizze a D-j-vel való összhangot (fiókhoz kötött
   tárolást nem állíthat szükségesnek), és ha a megoldás nem objektív, álljon meg.

## 4. Projektgazdai pontosítások a D-e-hez és a D-g-hez (2026-10-05), szó szerint

```text
Két projektgazdai pontosítás:

## D-e — M6.4 kötelező szcenáriók

A fix sorrendű három kötelező szcenárió:

**A → B → D**

Indok:
- A: alap módszerválasztási eset, fiatalabb kvuca;
- B: a kirekesztés/befogadás eset, és a M6 gate item bank 11–12 ehhez kapcsolódik;
- D: magasabb komplexitású idősebb kvuca + safety/safeguarding tartalom, ezért nem lehet opcionális.

**C nem törlődik.** Opcionális negyedik/bónuszgyakorlás marad.

Flow:

START
→ A
→ B
→ D
→ választás:
   - `Lezárom a leckét` → FINAL
   - `Megnézek még egy plusz helyzetet` → C → FINAL

Követelmények:
- A, B és D kihagyhatatlan;
- A vagy B után nincs út FINAL-ra;
- D után választható a lezárás vagy az opcionális C;
- C nem completion-követelmény;
- a lecke completion-feltétele a három kötelező szcenárió A+B+D érdemi végigvitele;
- a C teljesítése nem ad külön completion state-et és hiánya nem blokkol;
- minden szcenárión belüli módszerválasztási ág visszakonvergál a következő kötelező szcenárióra / D után a választópontra;
- a jelenlegi „legalább 3, a negyedik opcionális” learner-facing szöveget igazítsd a determinisztikus flow-hoz anélkül, hogy pedagógiailag úgy kommunikálnánk, mintha csak egyetlen helyes módszerválasztás lenne.

## D-g — build-spec vs runtime proof

Választás: **(a)**.

BSPEC-05 sorai spec-szinten lezárhatók `BUILD_SPEC_RESOLVED` státuszra, ha a determinisztikus build-konfiguráció teljesen rögzítve van.

A target-Moodle runtime proof külön staging/release evidence gate.

Tehát:

- a runtime teszt hiánya önmagában nem tartja `BUILD_SPEC_OPEN` állapotban a sort;
- ha az előírt negatív runtime teszt a target Moodle-on megbukik, az érintett mechanizmus ismét build blocker;
- ilyen esetben BSPEC-05-öt újra kell nyitni vagy explicit regression/build defectet kell regisztrálni a repo szabályai szerint;
- a pedagógiai/completion követelményt nem szabad azért gyengíteni, hogy a core Moodle mechanizmus átmenjen.

A release-model v2 build-spec/runtime-evidence szétválasztását őrizzük meg.

Rögzítsd ezt a D-e és D-g döntésekhez az audit trailben.
```

> **Felülírva a topológiában (5. szakasz):** a fenti „A → B → D → választás → (C →) FINAL” flow helyére az 5.
> szakasz flow-ja lép; a D-e pontosítás többi része változatlan. Az alábbi végrehajtási megjegyzés kockázatát az 5.
> szakasz feloldja (a C a D előtt áll, így a félbehagyott C-nél a D sincs teljesítve).

**Végrehajtási megjegyzés (nem döntés; az 5. szakasz feloldja):** a C a D utáni választóponton érhető el, és a FINAL-ra vezet; mindkét út
csak az A+B+D után éri el a FINAL-t. Nyitott megvalósítási kockázat a `/course-develop`-nak: a pontozott BS a grade-et
a végképernyőn adja át, így aki a C-t elkezdi, de nem fejezi be, annak a completionje nem áll be, pedig a pontosítás
szerint a C hiánya nem blokkolhat. A megoldás nem gyengítheti az A+B+D feltételt, és nem vezethet be kerülő
tartalékutat (D-g); ha a projektgazdai korlátokon belül nincs determinisztikus megoldás, a `/course-develop` álljon
meg. A pontosítás az M6 hub :119 és :224, valamint az M6.4 :47, :79, :104, :133, :162 „legalább 3 / a 4.
opcionális” megfogalmazását érinti (a `/course-develop` hatóköre); az M6 kapu item-bankjának B-ághoz kötött 11–12.
iteme változatlan. A D-g (a) szerinti visszanyitási feltétel a BSPEC-05 sorának szövegébe kerül (`/course-fix`).

## 5. D-e végrehajtási pontosítás (2026-10-05), szó szerint — a 4. szakasz topológiáját felülírja

```text
D-e végrehajtási pontosítás — a korábbi §4 topológiát ebben az egy pontban felülírja.

A D utáni opcionális C nem elfogadható, mert ha a learner A+B+D után belép C-be, majd félbehagyja, nem jut el H5P endinghez / FINAL-hoz, így a már teljesített kötelező A+B+D ellenére elmaradhat a Moodle felé küldött eredmény.

A végleges determinisztikus flow ezért:

START
→ A
→ B
→ OPTIONAL-C CHOICE

innen két út:

1. `Kihagyom a plusz helyzetet`
   → D
   → FINAL

2. `Megnézek még egy plusz helyzetet`
   → C
   → D
   → FINAL

Értelmezés:

- a három kötelező szcenárió továbbra is sorrendben A → B → D;
- C opcionális bonus practice, amely B és D közé illeszthető;
- C nem completion-követelmény;
- C kihagyása nem blokkolhat;
- A, B vagy D nem hagyható ki;
- minden completion-path végigmegy A-n, B-n és D-n;
- FINAL csak D után érhető el;
- ha valaki az opcionális C közben hagyja félbe a leckét, még nem teljesítette D-t, tehát nincs ellentmondás a completion szemantikával;
- B gate-item kapcsolat és D safety tartalma minden learner számára kötelezően megmarad;
- külön Moodle activity, staff checkpoint vagy kerülő fallback továbbra is kizárt.

Ezt a pontosítást rögzítsd a D-e döntés mellett. Ez felülírja kizárólag a korábbi:
A → B → D → optional C → FINAL
topológiát; D-e többi része változatlan.

A módosított /course-develop parancs:

/course-develop "M6.4 átszerkesztése a D-e és végrehajtási pontosításai szerint (2026-10-05; döntések: 01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – MAN completion és mentor-láthatóság D-e…D-j.md): egyetlen Branching Scenario activity; START → A → B → opcionális C választópont. A választópontból: „Kihagyom a plusz helyzetet” → D → FINAL; vagy „Megnézek még egy plusz helyzetet” → C → D → FINAL. A, B és D kihagyhatatlan és ebben a kötelező sorrendben követik egymást; C opcionális bonus practice, nem completion-követelmény és hiánya nem blokkolhat. FINAL kizárólag D után érhető el. Minden szcenárión belüli módszerválasztási ág a következő determinisztikus pontra konvergál. A „legalább 3, a negyedik opcionális” learner-facing szöveget a flow-hoz igazítsd, de ne sugallja, hogy a módszerválasztásban egyetlen helyes válasz van. Az M6 kapu B-ághoz kötött 11–12. iteme változatlan. D safety blokkja minden learner számára kötelezően elérendő. Külön activity, staff-checkpoint és bármilyen kerülő tartalékút kizárva. Ha ez a target Branching Scenario struktúrában determinisztikusan nem implementálható, állj meg és ne gyengítsd a követelményt."
```

## 6. Projektgazdai döntés az M33-IMPL-6-ra (2026-10-05), szó szerint

Forrás: a projektgazda `/course-review M3.3 --lens safety` hívásának fókusz-szövege (`2026-10-05 Validált findingok –
M3.3 Branching Scenario-flow.md`, 4. pont):

```text
Projektgazdai döntés M33-IMPL-6-ra: ne kerüljön új learner-facing bridging mondat a C ág után; a meglévő safeguarding szöveg maradjon változatlan, csak a flow-node kapcsolat változhat.
```

Hatás: az M33-IMPL-6 eldöntve; a `/course-fix` az S1-K1 C) ágát új tanulói mondat nélkül köti a következő csomópontra
(M33-IMPL-1), a gyermekvédelmi szöveg változatlan. A biztonság-jog lencse ezt a döntést figyelembe véve vizsgálja a
flow-t.

## 7. Projektgazdai döntések az M3.3 safety review után (SAFE-1, SAFE-4, SAFE-7; 2026-10-05), szó szerint

Előzmény: `2026-10-05 Validált findingok – M3.3 Branching Scenario-flow.md`, 8. pont.

```text
Projektgazdai döntések az M3.3 safety review után:

## SAFE-1 — passz / szünet / completion

A HUM-SAFE-03 passzolási joga kötelező és elsőbbséget élvez az M3.3 korábbi „mind a négy szcenáriót végigviszi” megfogalmazásával szemben.

A `passz` NEM a D-g által tiltott technikai/workaround fallback. Ugyanazon elsődleges Branching Scenario learner-safety útvonala.

Implementáció:

- minden érzékeny scenario előtt legyen elérhető `Passzolom ezt a helyzetet` út;
- indoklást nem kérünk;
- passz esetén az adott scenario tartalma kihagyható és a flow a következő scenario/checkpointra megy;
- minden scenario-checkpoint két módon teljesíthető:
  1. a learner végigviszi a scenariót, vagy
  2. a HUM-SAFE-03 alapján passzolja;
- FINAL csak a négy scenario-checkpoint után érhető el;
- Moodle completion továbbra is csak az egyetlen FINAL/grade-emission után történik;
- nincs külön Moodle activity, staff checkpoint, Group fallback vagy kézi completion-kerülőút.

A completion szemantika ezért:

`S1 (completed OR passed) AND S2 (completed OR passed) AND S3 (completed OR passed) AND S4 (completed OR passed) → post-scenario content → FINAL`.

### Szünet / félbehagyás

- a learner bármikor szünetet tarthat / kiléphet;
- félbehagyott M3.3 nem complete;
- nincs büntetés;
- visszatérésnél a target H5P által ténylegesen támogatott resume viselkedést használjuk;
- ha a target környezet nem tud megbízható resume-ot, ez nem jogosít completion-gyengítésre vagy külön fallbackre: a learner újraindíthatja az activityt és használhatja a passz-útvonalakat;
- ezt stagingben tesztelni kell.

### Egyenértékű alternatíva

HUM-SAFE-03 szerint továbbra is kérhető egyenértékű alternatíva.

Ez nem technikai completion fallback, és nem kell külön Moodle gate-et létrehozni hozzá: a passz önmagában nem zárja ki a course completiont.

Ne találj ki most új érzékeny alternatív learner-contentet. Ha a program/Memuna külön pedagógiai alternatívát kér, az külön tartalmi QA-t kap.

### Third-person default

M3.3 jelenlegi második személyű döntési framingjét projektgazdai szinten fikciós `helper-role case analysis` formának tekintjük, nem szerepjátéknak:

- a learner nem játszik sértettet vagy elkövetőt;
- nem kell saját történetet felidéznie vagy megosztania;
- a szituáció fikciós;
- a feladat a madrih következő lépésének elemzése.

Memuna/DPO release-QA/vétó változatlanul megmarad.

## SAFE-4 — S1-K1 C ág

Választás: Option 1.

Az S1-K1 C válasz a meglévő feedback után közvetlenül S1-K2-re megy.

- ne írj új bridging mondatot;
- ne küldd vissza S1-K1-re;
- a learnernek nem kell addig újraválasztania, amíg „helyes” választ nem ad;
- az all-wrong path továbbra is elérheti a FINAL-t és nem üres grade-et;
- a narratív átmenet fennmaradó QA-kockázata a Memuna review része.

## SAFE-7

Nem projektgazdai döntéssel zárjuk.

A jelenlegi answer key marad változatlan a staging buildben.

A Memuna release előtt explicit QA-zza, hogy a `23:15` bejövő privát üzenet és a ✅ első válasz megfelel-e HUM-SAFE-02-nek. Addig:
- a ✅-hoz ne nyúlj;
- ne állítsd, hogy SAFE-7 resolved;
- learner-release előtt kötelező lezárni;
- Moodle staging buildet önmagában nem blokkolja.

Rögzítsd ezeket a D-e…D-j / M3.3 döntési audit trailben.

A SAFE-1 strukturális változása miatt az LMS-M3-03 BSPEC-05 részét tekintsd újranyitottnak addig, amíg a fenti passz-node map és completion semantics nincs determinisztikusan rögzítve; ugyanabban a BSPEC-05 fixkörben visszazárható.

Ezután ne indíts új review-t. Add vissza a frissített command 5-öt úgy, hogy SAFE-1 és SAFE-4 implementációja is benne legyen.
```

**Hatás:** SAFE-1 és SAFE-4 eldöntve; SAFE-7 nyitva (Memuna-QA, learner-release előtt kötelező; a staging buildet nem
blokkolja; a ✅ változatlan). Az LMS-M3-03 BSPEC-05-része újranyitottnak tekintendő a passz-csomóponttérkép és a fenti
completion-szemantika determinisztikus rögzítéséig (ugyanabban a fixkörben visszazárható). A GK §2 „harmadik személyű
esetelemzés” alapértelmezéséhez: az M3.3 második személyű framingje projektgazdai szinten fikciós „helper-role case
analysis”; a Memuna/DPO release-QA és vétó marad.

**Végrehajtási megjegyzés (nem döntés) — mindkét pontot a 7.1. szakasz eldönti:**
1. a passz-választó csomópont tanulói szövegéből csak a passz-opció címkéje adott („Passzolom ezt a helyzetet”); a
   csomópont kérdés-szövege és a folytatás-opció címkéje nincs megadva;
2. passz esetén a passzolt scenario utáni biztonsági csomópont (M33-IMPL-3; pl. az S1 utáni 112-es akut doboz) az
   útvonalon marad-e, vagy a „scenario tartalmával” együtt kimarad.

### 7.1. A SAFE-1 két nyitott végrehajtási pontjának projektgazdai döntése (2026-10-05), szó szerint

```text
SAFE-1 két nyitott végrehajtási pontjának projektgazdai döntése:

## 1. Pass-choice node szövege

Minden S1–S4 scenario előtt ugyanaz a pass-choice node áll.

Kérdés, szó szerint:

**„Mit szeretnél tenni ezzel a helyzettel?”**

Opciók, szó szerint:

- **„Végigmegyek ezen a helyzeten”**
- **„Passzolom ezt a helyzetet”**

A passzhoz:
- nem kérünk indoklást;
- nincs külön megerősítő kérdés;
- nincs „biztos vagy benne?” modal;
- egyik opció sincs vizuálisan vagy nyelvileg preferáltként kezelve.

## 2. Safety node passz után

A passzolt scenario UTÁNI safety node az útvonalon MARAD.

Flow példa:

`S1 PASS → S1 SAFETY NODE → S2 PASS-CHOICE`

A szabály S1–S4-re egységes.

Értelmezés:
- a HUM-SAFE-03 passzjoga a szenzitív esetelemzésből való kilépésre vonatkozik;
- nem hagyja ki a képzés kötelező safeguarding minimum-információját;
- a safety node ezért completion-path része akkor is, ha maga a scenario passzolt.

A safety node:
- nem kér választ;
- nem pontozott;
- nem kér személyes reflexiót;
- nem ismétli meg a passzolt scenario narratíváját;
- kizárólag a már létező safety-box tartalmat használja;
- új érzékeny learner-facing szöveget ne írj hozzá.

Memuna QA/vétó továbbra is megmarad a kész staging activityre.

Ezzel a SAFE-1 végrehajtási specifikáció projektgazdai oldalon teljes. SAFE-7 továbbra is nyitott Memuna QA, és learner release előtt zárandó, de a staging buildet nem blokkolja.

Rögzítsd ezt a D-e…D-j döntési jegyzőkönyv §7 kiegészítéseként, majd a korábban megadott frissített command 5 futtatható.
```

**Hatás:** a SAFE-1 végrehajtási specifikációja projektgazdai oldalon teljes. Az M3.3 útvonala scenariónként:
pass-choice („Mit szeretnél tenni ezzel a helyzettel?” — „Végigmegyek ezen a helyzeten” / „Passzolom ezt a
helyzetet”) → (scenario | passz) → a scenario saját biztonsági csomópontja → a következő pass-choice; S4 után
post-scenario tartalom → FINAL. A SAFE-7 nyitva (Memuna-QA; learner-release előtt; a staging buildet nem blokkolja).

### 7.2. A pass-choice pontozásának pontosítása (2026-10-05), szó szerint

```text
A §7.1 pass-choice scoring pontosítása:

A bracketelt scoring-korlát maradjon, de így:

**„a két pass-choice opciónak azonos a scoring-hatása; egyik választása sem növelheti vagy csökkentheti a learner grade-jét a másikhoz képest.”**

Ez azt jelenti:

- `Végigmegyek ezen a helyzeten` és `Passzolom ezt a helyzetet` scoring szempontból egyenértékű;
- a passzolás nem járhat pontlevonással vagy alacsonyabb completion-grade-del;
- a folytatás nem járhat bonuszponttal;
- a scenario válaszainak helyessége továbbra sem mastery-gate;
- a csupa ❌ és a csupa passzolt út egyaránt eléri a FINAL-t és ott nem üres Moodle-grade-et eredményez;
- a nem üres grade létrehozásának technikai módja lehet scoringOption-függő, de nem teheti learner-visible teljesítménypontszámmá ezt a leckét.

Ha ezek együtt a target H5P/Moodle implementációban nem teljesíthetők, állj meg.
```

**Végrehajtási megjegyzés (levezetés, nem döntés):** ha a „Végigmegyek” ágon a scenario-válaszok pontot adnának, a
végigvitt út többet érne a passzolt útnál; a 7.2 feltételei ezért együtt úton-független Moodle-grade-et kívánnak
(a FINAL-on minden úton ugyanaz a grade). Hogy ezt a BS melyik `scoringOption`-je és az `includeInteractionsScores`
melyik értéke adja meg, és hogy a végképernyő mutat-e tanulónak pontszámot, a `/course-fix`-nek a `semantics.json`
alapján kell igazolnia; ha nem teljesíthető, álljon meg (7.2 utolsó mondata).

**Érvényes D-e (összevonva):** egyetlen BS activity; START → A → B → választópont → (C →) D → FINAL; A, B, D
kötelező és ebben a sorrendben; C opcionális, B és D között; FINAL csak D után; a D-e 1. szakasz és a 4. szakasz
követelményei a topológián kívül változatlanok.
