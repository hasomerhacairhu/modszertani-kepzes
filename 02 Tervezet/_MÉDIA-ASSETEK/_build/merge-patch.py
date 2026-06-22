#!/usr/bin/env python3
# Patch-réteg: workflow JSON(ok) + javítások → merged.json (workflow-result alak).
# Hozzáad 13 szöveges-ekvivalens sort (audit-blokkolók pótlása) + diszpozíciókat ír az audit-findingokba.
import json, sys, re

MAIN="/private/tmp/claude-501/-Users-heymarcell-DEV-modszertani-kepzes/beb636e4-af7c-47e2-be5f-706dab45bcec/tasks/wcc9r3yg2.output"
SUPP="/private/tmp/claude-501/-Users-heymarcell-DEV-modszertani-kepzes/beb636e4-af7c-47e2-be5f-706dab45bcec/tasks/w92vr1f21.output"
OUT="/tmp/media-merged.json"

def load(p):
    d=json.load(open(p,encoding="utf-8"))
    if isinstance(d.get("result"),str):
        try:d=json.loads(d["result"])
        except:pass
    if isinstance(d.get("result"),dict):d=d["result"]
    return d

main=load(MAIN); supp=load(SUPP)
assets={}
for src in (main,supp):
    for a in src.get("assets",[]):
        if a.get("assetId") and a["assetId"] not in assets:
            assets[a["assetId"]]=a
dedup=[g for src in (main,supp) for g in src.get("dedup",[])]
# audit: dimenziónként összevonva
audit_by={}
for src in (main,supp):
    for a in src.get("audit",[]):
        dim=a["dimension"]
        audit_by.setdefault(dim,{"dimension":dim,"summary":a.get("summary",""),"findings":[]})
        audit_by[dim]["findings"].extend(a.get("findings",[]))
missing=sorted({mf for src in (main,supp) for mf in src.get("missingFiles",[])})

# ---------- ÚJ SOROK (13) ----------
M61_FILE="MODULOK/M6/M6_ONLINE_LECKE/M6.1 – „Játék-kategóriák 4 kvucára”.md"
M61_SHORT="M6.1 – „Játék-kategóriák 4 kvucára”.md"
M72_FILE="MODULOK/M7/M7_ONLINE_LECKE/M7.2 – „Nem csak játék, hanem peula” – 11 tervezési pont & AI-támogatás.md"
M72_SHORT="M7.2 – „Nem csak játék, hanem peula” – 11 tervezési pont & AI-támogatás.md"

def lei(aid,file,short,mod,slide,parent,sec,note):
    return {"assetId":aid,"assetType":"leirat-transzkript","category":"szöveges-ekvivalens","mod":mod,
        "file":file,"fileShort":short,"kind":"online-lecke","location":f"SLIDE {slide} – „Mit hallunk?” blokk",
        "lineRef":f"{parent} narrációhoz","title":f"Leirat – SLIDE {slide} narráció ({parent})",
        "contentSpec":f"A SLIDE {slide} narráció ({parent}) szó szerinti szöveges átirata (leirat/transzkript) a slide-notesban. WCAG 2.2 (1.2.1) — KÖTELEZŐ, nem opcionális.",
        "purpose":"Hangos narráció kötelező szöveges ekvivalense képernyőolvasóhoz/siket-nagyothalló felhasználóhoz (WCAG 2.2 A, 1.2.1).",
        "techSpec":"sima szöveg a slide-notesban / letölthető .txt, magyar","a11y":"—",
        "provenance":f"szöveges-ekvivalens (a {parent} narrációból származtatva)","notes":note,
        "dedup":"","audit":f"✅ pótolva — audit-blokkoló ({sec}); WCAG kötelező leirat"}

def fel(aid,file,short,mod,slide,parent,sec):
    return {"assetId":aid,"assetType":"felirat","category":"szöveges-ekvivalens","mod":mod,
        "file":file,"fileShort":short,"kind":"online-lecke","location":f"SLIDE {slide} – narráció/videó",
        "lineRef":f"{parent} narrációhoz","title":f"Felirat – SLIDE {slide} ({parent})",
        "contentSpec":f"A SLIDE {slide} narráció/videó ({parent}) szinkron felirata (zárt felirat, .vtt/.srt). A forrás a11y-jegyzete kötelező feliratot ír elő.",
        "purpose":"Szinkron felirat a hangos/videós tartalomhoz (WCAG 2.2 A, 1.2.2).",
        "techSpec":"WebVTT vagy SRT, szinkronizált időbélyegekkel, magyar","a11y":"—",
        "provenance":f"szöveges-ekvivalens (a {parent} narrációból származtatva)","notes":f"Audit-blokkoló ({sec}) pótlása.",
        "dedup":"","audit":f"✅ pótolva — audit-blokkoló ({sec}); WCAG kötelező felirat"}

NEW=[
    lei("M6.1-LEI-03",M61_FILE,M61_SHORT,"M6",2,"M6.1-NAR-02","[05]","Audit-blokkoló [05] pótlása."),
    lei("M6.1-LEI-04",M61_FILE,M61_SHORT,"M6",3,"M6.1-NAR-03","[06]","Audit-blokkoló [06] pótlása."),
    lei("M6.1-LEI-05",M61_FILE,M61_SHORT,"M6",4,"M6.1-NAR-04","[07]","Audit-blokkoló [07] pótlása."),
    lei("M6.1-LEI-06",M61_FILE,M61_SHORT,"M6",5,"M6.1-NAR-05","[08]","Audit-blokkoló [08] pótlása."),
    lei("M6.1-LEI-07",M61_FILE,M61_SHORT,"M6",6,"M6.1-NAR-06","[09]","Audit-blokkoló [09] pótlása."),
    fel("M7.2-FEL-03",M72_FILE,M72_SHORT,"M7",2,"M7.2-NAR-02","[11]"),
    lei("M7.2-LEI-03",M72_FILE,M72_SHORT,"M7",2,"M7.2-NAR-02","[11]","Audit-blokkoló [11] pótlása (leirat)."),
    fel("M7.2-FEL-04",M72_FILE,M72_SHORT,"M7",3,"M7.2-NAR-03","[12]"),
    lei("M7.2-LEI-04",M72_FILE,M72_SHORT,"M7",3,"M7.2-NAR-03","[12]","Audit-blokkoló [12] pótlása (leirat)."),
    fel("M7.2-FEL-05",M72_FILE,M72_SHORT,"M7",4,"M7.2-NAR-04","[13]"),
    lei("M7.2-LEI-05",M72_FILE,M72_SHORT,"M7",4,"M7.2-NAR-04","[13]","Audit-blokkoló [13] pótlása (leirat)."),
    fel("M7.2-FEL-06",M72_FILE,M72_SHORT,"M7",5,"M7.2-NAR-05","[14]"),
    lei("M7.2-LEI-06",M72_FILE,M72_SHORT,"M7",5,"M7.2-NAR-05","[14]","Audit-blokkoló [14] pótlása (leirat)."),
]
added=0
for a in NEW:
    if a["assetId"] not in assets:
        assets[a["assetId"]]=a; added+=1

# ---------- DISZPOZÍCIÓK az audit-findingokba (fix-prefix) ----------
AI_TAG=("[A) OSZTÁLY-SZABÁLY ✅ — lefedve: Program terv §9 / 7. blokkoló sor + EU AI Act 50. cikk. "
        "Minden provenance=AI asseten KÖTELEZŐ: C2PA Content Credentials beágyazás + látható vízjel + ember-olvasható AI-címke. Külön sor-szintű javítás nem szükséges.] ")
RESOLVED={
 "M6.1-NAR-02":"[✅ PÓTOLVA: M6.1-LEI-03 (kötelező leirat) hozzáadva a regiszterhez.] ",
 "M6.1-NAR-03":"[✅ PÓTOLVA: M6.1-LEI-04 hozzáadva.] ",
 "M6.1-NAR-04":"[✅ PÓTOLVA: M6.1-LEI-05 hozzáadva.] ",
 "M6.1-NAR-05":"[✅ PÓTOLVA: M6.1-LEI-06 hozzáadva.] ",
 "M6.1-NAR-06":"[✅ PÓTOLVA: M6.1-LEI-07 hozzáadva.] ",
 "M6.1-NAR-07":"[✅ TISZTÁZVA: hang-only esetén a meglévő M6.1-LEI-02 elegendő; videó esetén M6.1-FEL-02 válik kötelezővé.] ",
 "M7.2-NAR-02":"[✅ PÓTOLVA: M7.2-FEL-03 + M7.2-LEI-03 hozzáadva.] ",
 "M7.2-NAR-03":"[✅ PÓTOLVA: M7.2-FEL-04 + M7.2-LEI-04 hozzáadva.] ",
 "M7.2-NAR-04":"[✅ PÓTOLVA: M7.2-FEL-05 + M7.2-LEI-05 hozzáadva.] ",
 "M7.2-NAR-05":"[✅ PÓTOLVA: M7.2-FEL-06 + M7.2-LEI-06 hozzáadva.] ",
}
FOTO_RESOLVED=("[✅ DÖNTVE (emberi): illusztráció — az egész M6.3-FOTO szériát (FOTO-01..05) illusztrációként gyártjuk; "
          "GDPR/kiskorú-kockázat megszűnt. A regiszterben FOTO→illusztráció típusra váltva, provenance=AI-generált.] ")
FOTO_IDS={"M6.3-FOTO-01","M6.3-FOTO-02","M6.3-FOTO-03","M6.3-FOTO-04","M6.3-FOTO-05"}

# --- M6.3 FOTO → illusztráció típusváltás (emberi döntés alapján) ---
foto_conv=0
for fid in FOTO_IDS:
    if fid in assets:
        a=assets[fid]
        a["assetType"]="illusztráció"
        a["provenance"]="AI-generált (illusztráció)"
        a["notes"]=((a.get("notes","") or "")+" | DÖNTÉS: illusztráció (GDPR-kockázat elkerülése), FOTO→ILL.").strip(" |")
        a["audit"]="✅ döntés: illusztráció — GDPR/kiskorú-kockázat megszűnt"
        foto_conv+=1

print(f"M6.3 FOTO→illusztráció konvertálva: {foto_conv} asset")

# ---------- PRODUKCIÓS KONVENCIÓK (osztály-szabályok a 'fontos' tételekhez) ----------
PRODUCTION_RULES=[
 ("R1","Egységes AI-jelölés","Minden provenance=AI asseten EGYETLEN kanonikus, ember-olvasható AI-címke (egységes szöveg + megjelenés) + gépi-olvasható C2PA/vízjel. Kiterjed az M0–M3 beszélőfej-videókra is, ahol eddig hiányzott. (Program terv §9 / 7. blokkoló sor + EU AI Act 50. cikk.)"),
 ("R2","AI-avatar / AI-hang IP-megfelelőség","Minden AI-avatar és AI-hang assethez dokumentálandó: a használt generátor neve, a kereskedelmi/oktatási felhasználást engedő licenc, és a voice-talent release. A konkrét licenc-igazolás ⟬KITÖLTENDŐ⟭ (szervezeti/jogi)."),
 ("R3","Narrátor hang-bible","EGYETLEN konzisztens narrátor-hang az egész tananyagban, tegező + barátságos regiszterben — a Z-záró és az M4 modulokat is beleértve. Modulonként a TTS vs. emberi felmondó döntés dokumentálandó; a konkrét TTS-motor / voice-ID ⟬KITÖLTENDŐ⟭."),
 ("R4","Védjegy-semlegesség","Tilos a védjegyzett platformok (Messenger / WhatsApp / Discord / Insta / Moodle) vizuális nyelvének másolása; semleges, nem-védjegyzett stílus kötelező (semleges chat-buborék, sztori-kör, LMS-felület)."),
 ("R5","Ikon- és karakter-batch + lock","A visszatérő ikon-készletek (SBI 3-szín; 4-kvuca piktogramok; M6.4 9 szekció-ikon) EGYSZER gyártandók közös stílus-tokennel és rögzített palettával, több helyen újrahasznosítva. Az AI karakter-jelenetek (M1.3-VID-01; M4.1-VID-03/04/05) rögzített referencia-karakterrel/seeddel készülnek, a freeze-frame-ek a videó-gyártás részeként. A konkrét someres hex-paletta ⟬KITÖLTENDŐ⟭."),
 ("R6","Szín-szótár","Tananyag-szintű szín-szótár: ugyanazon alapszín eltérő szemantikai újrahasznosítását (pl. kék = SBI-S vs. kék = Cionizmus) kerülni vagy explicit jelölni kell."),
 ("R7","Produkciós függőségek","A véglegesített Moodle-felülettől függő assetek (pl. M0.3-FOTO-01 screenshot) csak a kurzus-véglegesítés UTÁN gyárthatók — gate-elt függőség, célzott felbontás/arány előre rögzítve."),
 ("R8","GDPR / képmás-védelem","Valós fotó/screenshot esetén minden azonosítható személyt/kézírást anonimizálni vagy kikeretezni kell; felismerhető kiskorúnál dokumentált szülői hozzájárulás ELŐRE kötelező. Screenshotnál nincs valós felhasználónév/arc és nincs licenc-korlátos 3rd-party elem. (Megerősíti az M6.3 illusztráció-döntést.)"),
]
RULE_TITLE={r[0]:r[1] for r in PRODUCTION_RULES}

def classify(issue,fix):
    t=((issue or "")+" "+(fix or "")).lower()
    if any(k in t for k in ["gdpr","kiskorú","képmás","anonimiz","szülői","azonosítható személy","azonosítható adat"]): return "R8"
    if any(k in t for k in ["védjegy","márkanev","messenger","whatsapp","discord","insta-"]): return "R4"
    if any(k in t for k in ["moodle-felület","moodle-screenshot","screenshot","véglegesít","függőség","még nem létez","nem véglegesít"]): return "R7"
    if any(k in t for k in ["likeness","voice-talent","voice release","voice-release","avatar-licenc","ip-megfelel","release-t"]): return "R2"
    if any(k in t for k in ["narrátor","hang-bible","hangkarakter","tts","voice-id","felmondó","hangnem","tegező","hangszín","felolvasó"]): return "R3"
    if any(k in t for k in ["szín-szótár","szemantik","ütközés","eltérő szemantik"]): return "R6"
    if any(k in t for k in ["provenance","ai-jelölés","ai-provenance","badge","robot","watermark","c2pa"]): return "R1"
    if any(k in t for k in ["batch","karakter","freeze-frame","rotálható","ikon","shot-list","b-roll","seed","stílus-token","piktogram","jelenetlista","avatar","paletta","someres szín","hex","derivált"]): return "R5"
    return None

JAVASOLT_OVERRIDE={
 ("M2.3-VID-02","Akadálymentesség"):"[✅ TISZTÁZVA: a meglévő M2.3-FEL-03 + M2.3-LEI-03 lefedi a feliratot+leiratot; nincs hiányzó asset.] ",
 ("M2.3-VID-02","Produkciós"):"[✅ DÖNTÉS: az M2.3 OUTRO alapból narráció-only (M2.3-NAR-03); a VID-02 opcionális — terhelés-csökkentés. Ha mégis videó, R5 (karakter-lock) érvényes.] ",
 ("M4.2-ILL-01","Stílus"):"[⟬SZERZŐI DÖNTÉS⟭ M4 HOOK-formátum: javaslat — M4.1 marad videó-HOOK (indokolt), M4.2–4.4 egységes statikus illusztráció + narráció. Megerősítendő.] ",
 ("M1.1-NAR-04","Tartalmi"):"[ℹ️ TARTALMI ELLENŐRZÉS: a SLIDE 4 négy példája illeszkedjen a kánoni Johari-mezőkhöz (vakfolt = MÁSOK látják, ÉN nem). A korábbi auditok a Johari-koncepciót kánonira hozták.] ",
 ("M3.1-NAR-02","Tartalmi"):"[✅ ELLENŐRIZVE: a forrás (M3.1, 124. sor) helyes — Tuckman 1977, Mary Ann Jensen, adjourning. Kánoni, nincs javítandó.] ",
 ("M3.2-DIA-04","Tartalmi"):"[✅ ELLENŐRIZVE: a korosztály-sávok (Parparim 6–10, Kivsza 11–13, Leviatan 14–16, Zorea 16+) kánoniak és modulok között konzisztensek.] ",
}

patched=0
for dim,blk in audit_by.items():
    for f in blk["findings"]:
        if (f.get("fix","") or "").startswith("["): continue
        sev=f.get("severity"); aid=f.get("assetId",""); base=re.sub(r"\s*\(.*?\)\s*$","",aid).strip()
        pre=""
        if base in FOTO_IDS: pre=FOTO_RESOLVED                       # bármely súlyosság
        elif sev=="blokkoló":
            if "AI-jelölés" in dim: pre=AI_TAG
            elif base in RESOLVED: pre=RESOLVED[base]
        elif sev=="fontos":
            rid=classify(f.get("issue",""),f.get("fix",""))
            if rid: pre="[%s ✅ — Produkciós konvenció: %s.] " % (rid, RULE_TITLE[rid])
        elif sev=="javasolt":
            ov=None
            for (b,dimkw),tag in JAVASOLT_OVERRIDE.items():
                if base==b and dimkw in dim: ov=tag; break
            if ov: pre=ov
            else:
                rid=classify(f.get("issue",""),f.get("fix",""))
                if rid: pre="[%s ✅ — Produkciós konvenció: %s.] " % (rid, RULE_TITLE[rid])
        if pre:
            f["fix"]=pre+(f.get("fix","") or ""); patched+=1

merged={"assets":list(assets.values()),
        "dedup":dedup,
        "audit":list(audit_by.values()),
        "missingFiles":missing,
        "productionRules":[{"id":r[0],"title":r[1],"text":r[2]} for r in PRODUCTION_RULES]}
json.dump(merged,open(OUT,"w",encoding="utf-8"),ensure_ascii=False)
print(f"merged.json kész: {len(merged['assets'])} asset (+{added} új), {patched} audit-diszpozíció beírva → {OUT}")
