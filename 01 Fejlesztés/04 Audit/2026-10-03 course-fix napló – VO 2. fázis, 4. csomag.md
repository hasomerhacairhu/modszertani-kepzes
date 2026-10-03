# course-fix napló – VO 2. fázis, 4. csomag (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` futás állapota és a célzott újraellenőrzés nyitott findingjai. A 13
> lépéses csomag a nagy csomagos eljárás küszöbe alatt van; bizonyíték a fájlok végállapota.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-03 Fix pack – VO 2. fázis, 4. csomag.md`, P4-01…P4-11, 13 lépés, 7 fájl.
- **Bázis:** `vo/phase2-fix-pack-4` @ `83ea27b`.

| ID | lépés | fájl | állapot |
|---|---|---|---|
| P4-01 | a, b, c | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P4-02 | — | VOICE-BIBLE.md | alkalmazva |
| P4-03 | — | Emberi jóváhagyás szükséges.md | alkalmazva |
| P4-04 | — | PRODUCTION-DECISIONS.md | alkalmazva |
| P4-05, P4-06 | — | RIGHTS-EVIDENCE.md | alkalmazva |
| P4-07 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva |
| P4-08 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P4-09 | — | RIGHTS-EVIDENCE.md | alkalmazva |
| P4-10 | — | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva |
| P4-11 | — | PRODUCTION-DECISIONS.md | alkalmazva |

**Ellenőrzések:** a végállapot lépésenként visszaolvasva (13/13: a bizonyíték-blokk 0×, a javítás-blokk 1×) · a teljes
diff visszaolvasva, csomagon kívüli változás nincs · `content_integrity.py` 0 ERROR · `--pin-visible` 2 fájl (M1.3,
`Emberi jóváhagyás szükséges.md`) · `build` ×2 bájtra azonos · `check` OK · `reconcile` 747/747 · `validate` OK ·
`lint --high-only` 0 · `unittest` 150 OK · `git diff --check` tiszta · hangnév-ellenőrzés 0 találat ·
`RELEASE-VERDICT: NO-GO` (változatlan).

## Célzott újraellenőrzés — nyitott findingok (nem verifikáltak, ebben a futásban nem javítva)

| ID | Hely | Probléma (röviden) | Javaslat |
|---|---|---|---|
| UE4-IMPL-1 | M1.3 interakció-leírás („A második verzió után a videó megáll”), 264. sor | a kérdés megállása az 5. rész előtt is lehet; akkor a K7 szerinti ikon-hozzárendelés elmarad | „A második verzió és a képleírás 5. része után a videó megáll…”; megvalósítási megjegyzés: a Single Choice kezdőideje az 5. rész vége, Pause bekapcsolva; a 264. sor: „a párbeszéd szüneteiben és a 2. verzió után”. Kérdés, opciók, ✅, visszajelzés változatlan |
| UE4-PED-1 | `M1.3-NAR-08-VO` 4. rész | a 4. rész ~7–8 mp (16 szó), az 1. verzió ~2 mp — a K7 célja (azonos ütem) csak részben teljesül; a betűk kétszer hangzanak el | 4. rész: „A mondata közben három ikon villant fel. A társa elgondolkodik.” (~4 mp) |
| UE4-PED-2 | 5. rész első mondata | „a nyugodtabban elmondott mondat” — B válasza után egy pillanatra kétértelmű | „Az ikonok a madrih nyugodtabb mondatának három részénél villantak fel.” |
| UE4-NYELV-5 | 5. rész idézett töredékei | a `‘…’` nem hallatszik, a narrátor hangja azonos Madrih A-éval | hallható idézetkeret (pl. „Az S ikon akkor villant fel, amikor ezt mondta: …”) vagy a hallgatási próba kifejezetten erre a helyre is |
| UE4-NYELV-1 | `M1.3-NAR-08` `spec` | „Hallgatási próba: a képleírás … elkülönül” kész eredménynek olvasható | „ellenőrizni kell, hogy … elkülönül-e” |
| UE4-IMPL-2 | M1.3 266., 189., 246. sor | a „kb. 25–35 mp” a K7 előtti becslés; az öt rész ~40–45 mp | jelölni, hogy a becslés a VO QA-újramérés szerint frissül (VO D-17); a mért szám külön |
| UE4-IMPL-3 = UE4-NYELV-3 | `RIGHTS-EVIDENCE.md` 102. sor | a „voice-ID” a nyitott tételek között, holott a helye eldőlt (K3); „a hiányzó rész … mind” egyeztetés | a „voice-ID” helyett az R2-4 jóváhagyói minősítése; „a hiányzó részek … mind nyitottak még” |
| UE4-IMPL-4 | HUM-MEDIA-02 (408. sor) és `VOICE-BIBLE.md` (29–31.) kötelező mezők | a K6 mező csak a RIGHTS-EVIDENCE listájában szerepel | datált toldás mindkét helyen („2026-10-03, K6: valamint a nagykorúság ellenőrzése …”); a K6 sor 3. oszlopa kapja meg a VOICE-BIBLE-t |
| UE4-BIZT-1 | `RIGHTS-EVIDENCE.md` R2-5 | a „rögzíti, K6” jelen idejű állapotállításnak olvasható | „; a bejegyzés és a jóváhagyói minősítés bizonyíték-kapu, VO D-08” |
| UE4-NYELV-2 | `PRODUCTION-DECISIONS.md` K6 sor | „rögzíti, hogy a nagykorúság ellenőrizve (igen/nem)” — hiányzó állítmány (a jegyzőkönyv szövege) | „rögzíti a „nagykorúság ellenőrizve” bejegyzést (igen/nem), …” |
| UE4-NYELV-4 | `ELEVENLABS-VOICE-TEST.md` 1.0. | „A bejegyzés” előzmény nélkül | „A nyilvántartási bejegyzés” |

**Rendben talált pontok:** a 112-es alapszabály, a 116-os szabály, a Memuna vétó/QA, a megnevezett kivétel és a feltétel
nélküli kiejtés; a K5/K6 nem állít jóváhagyást, és nincs benne személyes adat; a HUM-MEDIA-02 dátuma, jóváhagyója és
bizonyítéka változatlan; a `::CAPTIONS` hivatkozások létező derivatívákra mutatnak; a K5–K7 táblasorok formailag
rendben vannak; az öt rész a forrásblokkban, a gyártási jegyzetben és a `spec`-ben egymással és a K7-tel összhangban van;
az 5. rész csak a „Mit látunk?” tényeit mondja.

**Továbbvezetés (2026-10-03, a PR #15 merge-e után):** mind a 12 finding (a duplikátummal 11 tétel) a
`2026-10-03 Fix pack – VO 2. fázis, 5. csomag.md`-be került (P5-01…P5-11; két független `verifier` ellenőrizte, 6 lépést
az ő szövegükkel pontosítva). A mért hossz beírása a VO QA-repó újramérésére vár.

## Vétólista

- **Answer key, küszöb, rubrika, kapu-típus, completion, időtartam:** nincs változás.
- **Gyermekvédelmi megfogalmazás:** `VOICE-BIBLE.md` 7. (P4-02) — előtte: „elhangzik, mindig „száztizenkettő” alakban,
  soha nem „egy-egy-kettő”-ként”; utána: „elhangzik. A 112 kiejtése — a fenti számjegyenkénti szabálytól eltérően —
  mindig „száztizenkettő”, soha nem „egy-egy-kettő””. Az alapszabály, a 116, a Memuna-hivatkozás és a megnevezett
  kivétel változatlan.
- **Adatvédelem / jog / HUM:** P4-03…P4-07 — K5 tényközlés, K6 döntés; életkor, születési dátum, igazolvány-adat
  kizárva; jóváhagyás-állítás nincs.
- **Akadálymentesség:** P4-01 (képleírás tartalma változatlan, elhelyezése a K7 szerint), P4-08 (a videóág felirata
  kötelező, a derivatívához kötve).
