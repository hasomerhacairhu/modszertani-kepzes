# Jóváhagyási csomag – médiafelelős / VO-gazda – egyetlen VO fix pack (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: a médiafelelős / VO-gazda (HUM 14 VO-1). A hangokat a csomag csak szerepnéven említi. A kurzusoldali alkalmazást a felhasználó kéri, fix packként; a pack a privát VO QA-repóban készül, onnan szerepnéven érkezik vissza.

## Hogyan válaszolj

- Tételenként: **ELFOGADOM** / **MÓDOSÍTOM: …** / **VÉTÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- A VO-02 blokknál a fő session ajánlása a (b) változat (a validált M1:NYELV-G1-6 és QA-PED-1 együtt); az (a) a minimális alternatíva.
- A VO-10 (M6.2-NAR-05) a D-07 GYV-18 item-döntésétől független, mert a lecke mintakérdését a D-07 nem érinti; ha a jóváhagyók mégis érintik, ez az egy blokk visszatartandó.

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| A. újrarender (10 blokk) | M1.3-NAR-04/-05/-06, M1.2-NAR-04, M4.1-NAR-07, M4.3-NAR-03, M6.1-NAR-03, M6.3-NAR-05, Z.1-NAR-01, M6.2-NAR-05 | M1:BIZT-G2-7, M1:NYELV-G1-6, M1:NYELV-G2-5, M1:QA14-BIZT-1, M4:QA14-BIZT-4, M4:BIZT-G1-2, M6:NYELV-G1-7, M6:NYELV-G2-1, Z:NYELV-G1-6, M6:QA14-BIZT-3 |
| B. írásmódi (9 blokk) | M3.1-NAR-02/-03, M3.3-NAR-03, M4.1-NAR-05, M7.2-NAR-04/-05, M7.3-NAR-04, M7.3-VID-01, M6.1-VID-01 | M3:NYELV-G1-13, M3:NYELV-G2-15, M4:NYELV-G1-12, M7:NYELV-G2-9, M7:NYELV-G2-13, M6:NYELV-G1-11 |

## Részletes javaslatok

### V1: egyetlen VO fix pack tervezete a médiafelelősnek és a VO-gazdának (HUM 14 VO-1 `F`, HUM:746)


**A pack mérete:** 19 `@source`-blokk és 2 `@asset` spec.
- **Újrarender kell 10 blokknál**, mert a kimondott szöveg változik: a VO-1 6 csillagos blokkja és a KF-01 négy blokkja.
- **9 blokk írásmódi:** ezeknél igazolni kell, hogy a kiejtés változatlan.
- **Már javítva:** a 19 blokk közül egyik sem. Csak ezek a specek kész: M1.3:749, :837, :938; M6.1:407; M6.3:872; M1.2:573 („szóra” rész).

Lezárt projektgazdai döntés a pack alapja: VO-1, D-1, ERT-12, ADV-3 és GYV-18. A DPO, a Memuna és a VO-gazda aláírása bizonyíték-kapu, nem nyitott döntés.

---

### A. Újrarender kell (a kimondott szöveg változik)

### VO-01 — M1.3-NAR-04-VO: „beírni” → „leírni”
- Fájl: `02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md:810` (`@source`); a változó sor: :813.
- Alap: VO-1; D-1 (HUM:524); kulcs: `M1:BIZT-G2-7`.
- Hatáskör: SZEREP: médiafelelős / VO-gazda (X-17). A tartalom a lezárt D-1 átvezetése.
- OLD: `próbáld meg beírni,`
- NEW: `próbáld meg leírni,`
- Régi hash: `417ebdad19e0`
- `@asset` spec :749 már javítva („írja le”). A leirat az M1.3-NAR-04::TRANSCRIPT, buildből készül.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG
- Indoklás: a dián nincs beviteli elem (:798). A már legyártott régi hang a pack előtt ne kerüljön tanulói felületre (CSOMAG:1782).

### VO-02 — M1.2-NAR-04-VO: „szóra vagy kifejezésre” → „szóra”
- Fájl: `…/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md:637`; a változó sor: :640.
- Alap: VO-1; kulcs: `M1:NYELV-G1-6`. A (b) változat alapja még a validált `QA-PED-1` (2026-10-12-i M1 QA :61, :164; a ledgerben nincs saját sora).
- OLD: `Kattints rá minden olyan szóra vagy kifejezésre, ami inkább **címke vagy minősítés**, nem konkrét tény.”`
- **NEW (b), javasolt:** `Kattints rá minden olyan szóra, ami inkább **címke vagy minősítés** – ha a címke több szóból áll, mindegyikre.”`
  - Ez a NYELV-G1-6 saját példája. Kiveszi a „nem konkrét tény” fordulatot is, amelyet a QA-PED-1 a :618/:629-cel ütközőnek talált.
- **NEW (a), minimális:** `Kattints rá minden olyan szóra, ami inkább **címke vagy minősítés**, nem konkrét tény.”`
- Spec :573 (BUILD-INPUT), csak a (b) változatnál:
  - OLD: `kattints rá minden szóra, ami inkább címke vagy minősítés, nem konkrét tény.`
  - NEW: `kattints rá minden szóra, ami inkább címke vagy minősítés; ha a címke több szóból áll, mindegyikre.`
  - Az (a) változatnál a spec már javítva.
- Régi hash: `c7b6be710572`
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG · BUILD-INPUT
- Az 5 célszó és a pontozás nem változik. Az (a) vagy (b) közti választás a fő session dolga, mielőtt a VO-gazdához megy.

### VO-03 — M1.3-NAR-06-VO: „az Assignmentben” → „a beadandóban”
- Fájl: M1.3:1052; a változó sor: :1056.
- Alap: VO-1; kulcs: `M1:NYELV-G2-5`.
- OLD: `a következő leckében és az Assignmentben erre építhetsz.`
- NEW: `a következő leckében és a beadandóban erre építhetsz.`
- Régi hash: `ad3218992935`. Spec :938 már javítva.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG

### VO-04 — M1.3-NAR-05-VO: csak kitalált helyzetre biztasson (ERT-12)
- Fájl: M1.3:898; a változó sor: :901.
- Alap: ERT-12 `A` (HUM:682); KF-01; kulcs: `M1:QA14-BIZT-1`. A szöveg a G8 kutató javaslata (nyers kimenetek :1589).
- Hatáskör: VO-gazda; vétó: DPO.
- OLD: `Gondolj egy helyzetre, ami eszedbe jut – vagy találj ki egy egyszerű, kisebb sztorit.`
- NEW: `Találj ki egy egyszerű, kisebb sztorit.`
- Régi hash: `5792a1e841d9`. Spec :837 már javítva („kitalált, életszerű helyzet”).
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG
- Csak törlés, új szöveg nincs benne. Igazodik a :885-höz („Valós helyzetet – név nélkül sem – ne írj le”).

### VO-05 — M4.1-NAR-07-VO: a „magadnak” elhagyása (ADV-3)
- Fájl: `…/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md:1186`; a változó sor: :1199.
- Alap: ADV-3 `F` (HUM:649); KF-01; kulcsok: `M4:QA14-BIZT-4` és az `M4:BIZT-G1-2` narrációs maradéka.
- Hatáskör: VO-gazda; vétó: DPO.
- OLD: `Most írd le magadnak ezt a két dolgot –`
- NEW: `Most írd le ezt a két dolgot –`
- Régi hash: `c88971559dfe`. A spec (:1126) semleges, nem változik.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG
- Indoklás: a tárolt TEXT-C ígérete (:1206) szerint a mentor és a rendszergazda is hozzáférhet a válaszhoz.

### VO-06 — M4.3-NAR-03-VO: a „magadnak” elhagyása (ADV-3)
- Fájl: `…/M4/Online leckék/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md:632`; a változó sor: :644.
- Alap és kulcsok: ugyanaz, mint a VO-05-nél.
- OLD: `Most írd le magadnak röviden:`
- NEW: `Most írd le röviden:`
- Régi hash: `a5385923c885`. A spec (:569) nem változik.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG
- Az ígéret helye: :650.

### VO-07 — M6.1-NAR-03-VO: „vagy” → „és”
- Fájl: `…/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:472`; a változó sor: :485. Ha a TECH-2 előbb fut, az útvonal az új fájlnév.
- Alap: VO-1; kulcs: `M6:NYELV-G1-7` (a).
- OLD: `A **bizalom- vagy kontaktjátékok** már több kockázatot hoznak.`
- NEW: `A **bizalom- és kontaktjátékok** már több kockázatot hoznak.`
- Régi hash: `6a51801924a6`. Spec :407 már javítva. Ugyanez az alak áll a :463-on és a :857-en.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG

### VO-08 — M6.3-NAR-05-VO: a vonzat javítása
- Fájl: `…/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:965`; a változó sorok: :974 és :976.
- Alap: VO-1; kulcs: `M6:NYELV-G2-1`. Minta: M6.4:490/:492.
- OLD 1: `> Tanít közös döntést:` → NEW 1: `> Közös döntésre tanít:`
- OLD 2: `> Tanít felelősséget:` → NEW 2: `> Felelősségre tanít:`
- Régi hash: `2db3e67b6430`. Spec :872 már javítva.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG

### VO-09 — Z.1-NAR-01-VO: névelő az azonosító előtt
- Fájl: `…/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md:268`; a változó sor: :271.
- Alap: VO-1; kulcs: `Z:NYELV-G1-6`. Korlát (IMPL-G1-6): csak újrarenderrel együtt kerülhet be.
- OLD: `Látod, honnan indultunk M0-ban, és hova jutottunk el M7-re.`
- NEW: `Látod, honnan indultunk az M0-ban, és hova jutottunk el az M7-re.`
- Spec :195 (BUILD-INPUT; a spec szerint „szó szerint” a forrást követi):
  - OLD: `honnan indultunk M0-ban, hova jutottunk M7-re;`
  - NEW: `honnan indultunk az M0-ban, hova jutottunk az M7-re;`
- Régi hash: `9bcc9f6d7b62`. A hangbemenet „az em nullában … az em hétre” lesz (VOICE-BIBLE :162).
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG · BUILD-INPUT

### VO-10 — M6.2-NAR-05-VO: a „nálatok” kérdés opcionális és passzolható (GYV-18)
- Fájl: `…/M6/Online leckék/M6.2 – Történet, mint tükör.md:619`; a változó sorok: :631–632.
- Alap: GYV-18 `F` (HUM:641); KF-01 (kapcsolódó tétel); kulcs: az `M6:QA14-BIZT-3` narrációs része.
- Hatáskör: VO-gazda; vétó/QA: Memuna és értékelési felelős (GYV-18).
- OLD (két sor): `> – ‘Milyen hasonló helyzet volt már nálatok?` / `> Nem kell nevet mondani.’`
- NEW: `> – opcionálisan: ‘Milyen hasonló helyzet volt már nálatok?` / `> Nem kell nevet mondani, és bárki indoklás nélkül passzolhat.’`
- Régi hash: `f219beea277d`. A spec (:559) nem változik.
- Címkék: VO-PACK · LÁTHATÓ SZÖVEG
- Ez a már átvezetett diaszöveg (M6.2:606) és a hub (M6:98) szó szerinti átvétele.
- **D-07-függés:** a D-07 (b) a KAPU 12. itemjéről szól, a lecke mintakérdését nem érinti. Ha a jóváhagyók a leckemintát is módosítják, ez az egy blokk visszatartandó, és velük együtt mozog.

---

### B. Írásmódi blokkok: igazolni kell, hogy a kiejtés változatlan, kétség esetén újrarender

### VO-11 — M3.1-NAR-02-VO
- Fájl: `…/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md:260`; a változó sor: :279.
- Kulcs: `M3:NYELV-G1-13`.
- OLD: `az **adjourning**-ot,` → NEW: `az **adjourningot**,`
- Régi hash: `92d86f7be3c4`
- Kiejtési kockázat: a szakasznevek kiejtését a szótár aliasa adja (VO D-04; VOICE-BIBLE :156–158). A Leviatán-precedens (VOICE-BIBLE :140) szerint a toldalékos alakhoz külön alias kellett. Ha az alias nem illeszkedik a kötőjel nélküli alakra, a kiejtés megváltozik, és újrarender kell.

### VO-12 — M3.1-NAR-03-VO
- Fájl: M3.1:519; a változó sorok: :523, :526, :533.
- Kulcs: `M3:NYELV-G1-13`.
- `A **forming**-ban` → `A **formingban**`
- `A **storming**-nál` → `A **stormingnál**`
- `A **performing**-ban` → `A **performingban**`
- Régi hash: `8af73718262c`. A kiejtési kockázat ugyanaz, mint a VO-11-nél.

### VO-13 — M3.3-NAR-03-VO
- Fájl: `…/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md:841`; a változó sor: :844. A CSOMAG régi „:996”-os sorszáma elavult.
- Kulcs: `M3:NYELV-G2-15`.
- OLD: `egy alap térképed` → NEW: `egy alaptérképed`
- Régi hash: `d8fa9e5a8099`
- Prozódiai eltérés lehetséges: az összetételnek egy főhangsúlya van.

### VO-14 — M4.1-NAR-05-VO (erre hivatkozik az M4.1-VID-05 is)
- Fájl: M4.1:818; a változó sor: :826.
- Kulcs: `M4:NYELV-G1-12`.
- OLD: `‘Sziasztok, ma arról fogunk beszélni, hogy…’.”` → NEW: `‘Sziasztok, ma arról fogunk beszélni, hogy…’”`
- Régi hash: `b7472130c708`
- A spec (:509) és a VID-05 spec (:693) rendben van.
- A felirat és a leirat a konténeré: M4.1-VID-02::CAPTIONS / ::TRANSCRIPT (VOICE-BIBLE :227–229).

### VO-15 — M7.2-NAR-04-VO
- Fájl: `…/M7/Online leckék/M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md:728`; a változó sor: :736.
- Kulcs: `M7:NYELV-G2-11` c).
- OLD: `a játék az élmény-fázis,` → NEW: `a játék az élményfázis,`
- Régi hash: `935abce0a9d5`
- A :732 „élmény-blokk” marad: az f) pont szerint nem javítandó.

### VO-16 — M7.2-NAR-05-VO
- Fájl: M7.2:842; a változó sor: :847.
- Kulcs: `M7:NYELV-G2-9`.
- OLD: `red flag-ek jöhetnek elő,` → NEW: `red flagek jöhetnek elő,`
- Régi hash: `85e1c4d1cf75`
- Alias-kockázat: a „red flag” kiejtése „rett fleg” (VOICE-BIBLE :160). Ellenőrizni kell, hogy az alias a toldalékos alakra is illeszkedik-e.

### VO-17 — M7.3-NAR-04-VO
- Fájl: `…/M7/Online leckék/M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md:632`; a változó sor: :649.
- Kulcs: `M7:NYELV-G2-9`.
- OLD: `ha red flag-et látsz.` → NEW: `ha red flaget látsz.`
- Régi hash: `b730866347ee`. Az alias-kockázat ugyanaz, mint a VO-16-nál.

### VO-18 — M7.3-VID-01-VO (videó)
- Fájl: M7.3:147; a változó sor: :153.
- Kulcs: `M7:NYELV-G2-13` a). Minta: M4:NYELV-G2-11.
- OLD: `*„amikor program van a kvucával”*` → NEW: `*‘amikor program van a kvucával’*`
- Régi hash: `47a74316715f`
- A felirat és a leirat (M7.3-VID-01::CAPTIONS / ::TRANSCRIPT) külön hang–szöveg egyezési ellenőrzést kap (VO-1 `F`).

### VO-19 — M6.1-VID-01-VO (videó)
- Fájl: M6.1:186; a változó sor: :202.
- Kulcs: `M6:NYELV-G1-11` (rész; a kulcs gazdája a TECH-2).
- OLD: `hogyan gondolkodhatsz **játék-kategóriákban**` → NEW: `hogyan gondolkodhatsz **játékkategóriákban**`
- Régi hash: `b750e8d30708`
- A VID-01 spec (:115) és az M6.1 többi „játék-kategória” helye a TECH-2 change setjébe tartozik, nem ebbe a packbe.
- A felirat és a leirat (M6.1-VID-01::CAPTIONS / ::TRANSCRIPT) külön egyezési ellenőrzést kap.

A 9 írásmódi blokk (VO-11 … VO-19) mindegyike VO-PACK · LÁTHATÓ SZÖVEG, a hatáskör a médiafelelős / VO-gazda.

---

### C. A kurzusoldali alkalmazás sorrendje (egy change set)

0. **Előfeltételek:**
   - a VO-gazda írásban elfogadja ezt a szövegcsomagot;
   - a felhasználó a saját üzenetében kéri az alkalmazást (`/course-fix`, külső findinglista);
   - a fő session dönt a VO-02 (a)/(b) változatáról;
   - a VO-10-nél megnézi a D-07 állását.
1. **TECH-2:** nincs kötött sorrend (CSOMAG:1802). Ha a TECH-2 fut előbb, a VO-07 és a VO-19 az új M6.1-útvonalra mutat. A kettő ne kerüljön egy commitba.
2. **Commit `fix(M1,M3,M4,M6,M7,Z)`:**
   - a 19 `@source` törzs, plus a Z.1:195 spec, és a (b) változatnál az M1.2:573 spec, `Edit`-tel;
   - `python3 tools/content_integrity.py` → 0 ERROR;
   - `git diff` visszaolvasása;
   - egyetlen pin: `python3 tools/test_media_manifest.py --pin-visible "M1:BIZT-G2-7, M1:NYELV-G1-6, M1:NYELV-G2-5, M1:QA14-BIZT-1, M3:NYELV-G1-13, M3:NYELV-G2-15, M4:NYELV-G1-12, M4:QA14-BIZT-4, M4:BIZT-G1-2, M6:NYELV-G1-7, M6:NYELV-G2-1, M6:NYELV-G1-11, M6:QA14-BIZT-3, M7:NYELV-G2-9, M7:NYELV-G2-11, M7:NYELV-G2-13, Z:NYELV-G1-6: VO-1 fix pack (@source)"`.
   - A spec-mezők metaadatként kimaradnak a pin-ujjlenyomatból (`strip_metadata`), a `@source` törzse viszont látható szöveg.
3. **Commit `chore(media)`:** `python3 tools/media_manifest.py build`, `check`, `reconcile`, `python3 -m unittest tools.test_media_manifest`. A build újraírja az `assetek.csv`, a `deliverable-ek.csv` és a `_build/media-manifest.v2.json` fájlt, benne az új source hasht, a felirat- és a leiratszöveget.
4. **Átadás:** az új hashek a VO-gazdához mennek. A VO QA-repóban a 10 blokk újrarenderelése és meghallgatása következik, a 9 írásmódi blokknál az igazolás.
5. **Átmeneti tilalom:** amíg nincs új hang, a 10 újrarenderes blokk régi hangja nem mehet tanulói felületre, mert a leirat már az új szöveg (VOICE-BIBLE :212–214, :232–233). Nem blokkol: a narráció B fázis, és a pilotban opcionális (HUM:553).

### D. Összefoglaló tábla

| Blokk | Újrarender? | Finding-kulcsok |
|---|---|---|
| M1.3-NAR-04-VO | igen | M1:BIZT-G2-7 (D-1) |
| M1.2-NAR-04-VO | igen | M1:NYELV-G1-6 (+QA-PED-1 a (b)-nél) |
| M1.3-NAR-06-VO | igen | M1:NYELV-G2-5 |
| M1.3-NAR-05-VO | igen | M1:QA14-BIZT-1 (ERT-12) |
| M4.1-NAR-07-VO | igen | M4:QA14-BIZT-4, M4:BIZT-G1-2 narr. (ADV-3) |
| M4.3-NAR-03-VO | igen | M4:QA14-BIZT-4, M4:BIZT-G1-2 narr. (ADV-3) |
| M6.1-NAR-03-VO | igen | M6:NYELV-G1-7 (a) |
| M6.3-NAR-05-VO | igen | M6:NYELV-G2-1 |
| Z.1-NAR-01-VO | igen | Z:NYELV-G1-6 |
| M6.2-NAR-05-VO | igen (D-07-feltétellel) | M6:QA14-BIZT-3 narr. (GYV-18) |
| M3.1-NAR-02-VO | igazolás, alias-kockázat | M3:NYELV-G1-13 |
| M3.1-NAR-03-VO | igazolás, alias-kockázat | M3:NYELV-G1-13 |
| M3.3-NAR-03-VO | igazolás | M3:NYELV-G2-15 |
| M4.1-NAR-05-VO (+VID-05) | igazolás | M4:NYELV-G1-12 |
| M7.2-NAR-04-VO | igazolás | M7:NYELV-G2-11 c) |
| M7.2-NAR-05-VO | igazolás, alias-kockázat | M7:NYELV-G2-9 |
| M7.3-NAR-04-VO | igazolás, alias-kockázat | M7:NYELV-G2-9 |
| M7.3-VID-01-VO | igazolás + felirat/leirat | M7:NYELV-G2-13 a) |
| M6.1-VID-01-VO | igazolás + felirat/leirat | M6:NYELV-G1-11 (TECH-2 rész) |

### E. A pack elfogadási feltételei (bizonyíték-kapuk, nem írom be és nem feltételezem)

1. **VO-gazda, újrarenderes blokkok:** mind a 10 blokk újrarenderelve, teljes tételként újravéve (VOICE-BIBLE 13.6), és meghallgatva.
2. **VO-gazda, írásmódi blokkok:** a 9 blokk mindegyikéről dokumentálni kell:
   - a régi és az új source hasht;
   - a `tts_text` eltérését (nulla, vagy alias-ekvivalens);
   - a szótárverziót.

   Az M3.1-nél és a két „red flag” blokknál kifejezetten igazolni kell az alias-lefedést. Kétség esetén újrarender.
3. **A két videó** (M6.1-VID-01, M7.3-VID-01): a WebVTT-felirat és a leirat szóról szóra egyezzen a hanggal (VOICE-BIBLE §9). Az M4.1-VID-02 konténerfeliratát is érdemes ugyanígy ellenőrizni, mert a NAR-05 szövegét hordozza.
4. **DPO-vétó:** VO-04 (ERT-12), VO-05 és VO-06 (ADV-3). Az írásos bizonyíték a G2-höz tartozik.
5. **Memuna és értékelési felelős QA:** VO-10 (GYV-18).
6. **A renderelt felület:** a felirat és a leirat ellenőrzése a G5b (RUNTIME_VERIFIED) kapuhoz, a regressziós zöld állapot a G7-hez tartozik.
7. **Ledger:** a kulcsok a hang elfogadásáig nyitottak. A kurzusoldali rész legfeljebb IMPLEMENTED állapotba kerülhet.

### F. Amit nem tudtam ellenőrizni

- Nem futtattam a `media_manifest.py check`-et, ezért nem igazolt, hogy a régi hashek frissek.
- A privát VO QA-repó szótár-aliasait nem látom, és azt sem, mely blokkokhoz készült már hang. Csak az M1.3-NAR-04-ről mondja ki forrás, hogy legyártották.
- Az `M7:NYELV-G2-11` és a `QA-PED-1` kulcsnak nem találtam nyitott sort a ledgerben.
- Nem tudom, hogy a D-07 kimenete érinti-e a lecke mintakérdését.
- Nem néztem meg az M2.4:770 („válaszolj magadnak”) és az M4.B:332 helyet. Ezek az ADV-3 itt vizsgált körén kívül esnek.

### G. Ellentmondás a kánonban, és megfigyelés

- **Újrarenderes blokkok száma:** a VO-1 `F` „6 + 9” blokkot nevez meg. A KF-01 négy blokkja a döntés saját szabálya szerint újrarenderes, így az összesen 10 + 9. Ez a döntés alkalmazása, nem új döntés.
- **Elavult sorszámok a CSOMAG-ban:** például M3.3 „:996” helyett :844, M6.3 „:974/976” stimmel. A fenti sorszámok a mostaniak.
- **„A két videó”:** a VO-1 `F` csak két videót nevez meg, pedig az M4.1-VID-02 felirata is `@source`-ból épül (NAR-05).
- **Nem validált megfigyelés (nem része a packnek):** az „adjourning-ot” toldaléka a jóváhagyott „edzsörning” kiejtéssel magánhangzó-illeszkedési kérdést vet fel. Ezt nyelvi döntés zárhatja le, a pack nem nyúl hozzá.
