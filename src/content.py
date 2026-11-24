# -*- coding: utf-8 -*-
"""Gemensamt innehåll för alla fyra designförslagen.
Allt som står inom <span class="tbd">…</span> är uppgifter som styrelsen behöver fylla i eller bekräfta."""

def tbd(t):
    return f'<span class="tbd">{t}</span>'

ICONS = {
 "hem": '<path d="M3 11l9-8 9 8"/><path d="M5 9v12h14V9"/>',
 "sophantering": '<path d="M4 7h16"/><path d="M9 7V4h6v3"/><path d="M6 7l1 13h10l1-13"/><path d="M10 11v6M14 11v6"/>',
 "parkering": '<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M10 17V8h3a2.5 2.5 0 0 1 0 5h-3"/>',
 "laddstolpar": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "projekt": '<path d="M3 10l9-6 9 6v10H3z"/><path d="M7 20v-6h10v6M7 17h10"/>',
 "stadning": '<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19l7-7"/>',
 "grasklippning": '<path d="M3 20h18"/><path d="M6 20c0-5-1-8-3-10M10 20c0-6 0-10-2-14M14 20c0-6 1-9 3-12M18 20c0-4 1-6 3-8"/>',
 "tv-bredband": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M8 21h8M8 2l4 4 4-4"/>',
 "dokument": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
 "ny-har": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
 "maklare": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V4h8v3M3 13h18"/>',
 "historik": '<path d="M7 21V9c0-4 2.5-6 5-6s5 2 5 6v12z"/><path d="M10 9l2 3 2-3M12 12v6M4 21h16"/>',
 "forum": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 "kontakt": '<circle cx="9" cy="7.5" r="3.5"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6"/><path d="M16 4.5a3 3 0 0 1 0 6M22 20c0-3-2-5-5-5.5"/>',
}

def icon(key, size=24, sw=1.7):
    return (f'<svg class="ico" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>')

# id, namn, kort namn, färg, kort beskrivning
TOPICS = [
 ("sophantering","Sophantering","Sopor","#7b4a2b","Sortering och tömning"),
 ("parkering","Parkering","Parkering","#1f5fa8","Regler och snöröjning"),
 ("laddstolpar","Laddstolpar","Laddning","#16181b","Laddning av elbil"),
 ("projekt","Projekt","Projekt","#b4472c","Garage och pågående projekt"),
 ("stadning","Städdagar & skötsel","Städdagar","#3f7a3c","Vi ses på gården vår och höst"),
 ("grasklippning","Gräsklippning","Gräsklippning","#6f9a1f","Schema och brandgator"),
 ("tv-bredband","TV & bredband","TV & nät","#5b4a9b","Telia-TV och bredband"),
 ("dokument","Stadgar & protokoll","Dokument","#7a6a48","Stadgar och protokoll"),
 ("ny-har","Ny i Väringen","Ny här","#b7801a","Välkommen hit!"),
 ("maklare","Mäklarinfo","Mäklare","#4b5866","Faktablad vid försäljning"),
 ("historik","Historik","Historik","#8e3b2e","Runriket och väringarna"),
 ("forum","Forum","Forum","#1d7a78","Prata med grannarna"),
 ("kontakt","Kontakt & styrelse","Kontakt","#22344d","Styrelsen och grändvärdar"),
]
TOPIC = {t[0]: t for t in TOPICS}

def pdf_bar(pid, label=None):
    label = label or "Ladda ned sidan som PDF"
    return (f'<div class="pdfbar"><a class="btn btn-pdf" href="../pdf/{pid}.pdf">{icon("dokument",18)}<span>{label}</span></a>'
            f'<button class="btn btn-ghost" type="button" data-print>Skriv ut</button></div>')

def ul(items, cls="list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def facts(rows):
    return '<dl class="facts">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"

def card(title, body, extra=""):
    return f'<div class="card {extra}"><h3>{title}</h3>{body}</div>'

def callout(title, body, kind=""):
    return f'<aside class="callout {kind}"><strong>{title}</strong>{body}</aside>'

def photo(label, ratio="16/9"):
    return f'<figure class="photo" style="aspect-ratio:{ratio}"><span>{icon("hem",20)} {label}</span></figure>'

# ---------- Sidinnehåll ----------
PAGES = {}

PAGES["sophantering"] = dict(
 lead="Vi delar på kärlen, och med lite omtanke från alla blir gården ren och trevlig. Här ser du vad som ska i vilket kärl.",
 body=f"""
<div class="grid g2">
 {card('<i class="dot" style="background:#3a3a3a"></i>Restavfall – svart/grått kärl', '<p class="muted">Lägg i väl knuten påse.</p>' + ul(["Dammsugarpåsar","Blöjor och bindor","Kuvert och klisterlappar","Plåster, tops och tandborstar","Tuggummi, fimpar och snus","Annat som inte går att återvinna"]))}
 {card('<i class="dot" style="background:#7b4a2b"></i>Matavfall – brunt kärl', '<p class="muted">Lägg i papperspåsen – aldrig plastpåse.</p>' + ul(["Matrester, kött och fisk","Skal från frukt och grönt","Äggskal","Bröd, ris och pasta","Kaffesump, filter och tepåsar","Mejeriprodukter som blivit för gamla"]))}
</div>
<h2>Ska <em>inte</em> i kärlen – lämnas separat</h2>
<div class="table">
 <div><b>Förpackningar <small style="font-weight:400;color:var(--muted)">kartong, plast, glas, metall</small></b><span>Återvinningsstationen</span></div>
 <div><b>Tidningar och returpapper</b><span>Återvinningsstationen</span></div>
 <div><b>Kläder, skor och textil</b><span>Klädinsamling / återvinningscentral</span></div>
 <div><b>Farligt avfall, batterier, lampor, el</b><span>Miljöstation / återvinningscentral</span></div>
 <div><b>Grovavfall, möbler, mycket kartong</b><span>Återvinningscentral / städdagens container</span></div>
</div>
{callout('Tänk på det här', ul(["Släng aldrig om kärlet är fullt – vänta till efter tömning eller använd ett annat kärl.","Ställ inget bredvid eller ovanpå kärlet. Det lockar fåglar och råttor.","Använd väl knutna påsar, inte stora sopsäckar. Stäng locket.","Osäker? Kolla Täbys sorteringsguide. Styrelsen är ingen skräppolis – vi hjälps åt."]), "warn")}
{facts([("Hämtas av","Verdis (rullkärl)"),("Tömningsdag", tbd("Fastställs – fylls i")),("Sorteringsguide",'<a href="https://www.taby.se" rel="noopener">taby.se</a> → Avfall och återvinning'),("Frågor","Din grändvärd eller styrelsen")])}
""")

PAGES["parkering"] = dict(
 lead="Med lite hänsyn kommer alla fram, både grannar, sopbilen och räddningstjänsten. Här är reglerna i korthet.",
 body=f"""
<div class="grid g3">
 {card("Här får du parkera", "<p>Endast på <b>markerade parkeringsrutor</b> eller i garage.</p>", "ok")}
 {card("Här får du inte parkera", "<p>I gränderna (bara i- och urlastning), längs grönområden och framför garagen.</p><p><b>Gästparkeringarna</b> är till för våra gäster. Parkera din egen bil på din plats eller i garaget.</p>", "no")}
 {card("Om allt är fullt", "<p>Parkera uppe på vägen enligt Täby kommuns regler (datumparkering).</p>")}
</div>
<h2>Snöröjning av din plats</h2>
<p>Föreningens entreprenör sköter den generella snöröjningen i området. Utöver det <b>ansvarar varje hushåll för att skotta sin egen märkta plats</b>. För omärkta platser fördelar grändvärdarna uppgiften.</p>
{callout("Brandrisk i garagen", "<p>Förvara inte brandfarliga ämnen eller stora mängder saker i garagen.</p>", "warn")}
{callout("På gång", "<p>Styrelsen undersöker alternativ och kostnader för tydligare parkeringsskyltning.</p>")}
""")

PAGES["laddstolpar"] = dict(
 lead="Laddstolparna är nu i drift, och alla hushåll kan ladda elbilen hemma på gården. Information om hur det fungerar har skickats till alla medlemmar och läggs snart in här.",
 body=f"""
{facts([("Engångsavgift","12 000 kr per hushåll (enligt budget 2026/27)"),("Status","I drift sedan november 2026"),("Så laddar du", tbd("Instruktion: app/tagg, hur man startar – fylls i")),("Elkostnad", tbd("Hur elen debiteras – fylls i")),("Felanmälan", tbd("Kontakt vid fel – fylls i"))])}
<h2>Regler för laddning</h2>
{ul(["Ladda bara vid föreningens laddpunkter.","Dra aldrig sladd från huset över gångvägar eller gemensamma ytor.", "Flytta bilen när den är färdigladdad om laddpunkten delas. " + tbd("bekräfta"), "Egen laddbox? Prata med styrelsen innan du gör något."], "list check")}
<h2>Vanliga frågor</h2>
<details><summary>Vad kostar det att ladda?</summary><p>{tbd("Fylls i när avtalet för debitering är klart.")}</p></details>
<details><summary>Måste jag betala engångsavgiften om jag inte har elbil?</summary><p>Avgiften gäller varje hushåll enligt det förslag som lades fram till årsstämman 2026. {tbd("Bekräfta mot stämmoprotokollet.")}</p></details>
<details><summary>Vem kontaktar jag om laddaren inte fungerar?</summary><p>{tbd("Leverantör/serviceavtal – fylls i.")} Under tiden: hör av dig till styrelsen.</p></details>
""")

PAGES["projekt"] = dict(
 lead="Här samlar vi det som är på gång i föreningen. Störst just nu är garageprojektet, och fler idéer är alltid välkomna.",
 body=f"""
<h2>Garageprojektet</h2>
<p>Garagen projekterades under verksamhetsåret 2025/26 och informerades om på årsstämman i september 2026. En arbetsgrupp tar nu arbetet vidare.</p>
<ol class="steps">
 <li class="done"><b>2025/26</b><span>Projektering</span></li>
 <li class="now"><b>2026/27</b><span>Arbetsgrupp tar fram förslag</span></li>
 <li><b>{tbd("Datum")}</b><span>Förslag till beslut på stämma</span></li>
 <li><b>{tbd("Datum")}</b><span>Genomförande</span></li>
</ol>
<h2>Aktuella projekt</h2>
<div class="projects">
 <div><span class="chip soft">Klart</span><b>Laddstolpar</b><p>I drift. Information har skickats till alla medlemmar.</p></div>
 <div><span class="chip">Pågår</span><b>Träd och häckar</b><p>Dialog med arborist om skadade träd.</p></div>
 <div><span class="chip soft">Utreds</span><b>Vattenmätarbyte</b><p>Styrelsen undersöker upphandling.</p></div>
 <div><span class="chip soft">Utreds</span><b>Parkeringsskyltning</b><p>Alternativ och kostnader tas fram.</p></div>
</div>
<h2>Kallförrådet</h2>
<p>I förrådet finns föreningens gemensamma redskap: motorgräsklippare, kompostkvarn, stegar, snöslädar, skottkärra, röjsåg med skyddsutrustning, krattor och mer. {tbd("Hur man lånar / var nyckeln finns")}</p>
""")

PAGES["stadning"] = dict(
 lead="Två gånger om året ses vi på gården för att umgås, lära känna nya grannar och ha trevligt tillsammans. Att det samtidigt blir fint omkring oss, och att vi håller nere kostnaderna, är en bonus.",
 body=f"""
<div class="grid g2">
 <div class="date-card"><span>Vårstäddag</span><b>17 april 2027</b><small>Preliminärt</small></div>
 <div class="date-card"><span>Höststäddag</span><b>16 oktober 2027</b><small>Preliminärt</small></div>
</div>
<p class="note">Datumen är styrelsens förslag till årsstämman 2026 och bekräftas när stämmoprotokollet finns. Ett informationsblad delas ut i brevlådan senast en vecka före.</p>
<h2>Så brukar dagen se ut</h2>
{ul(["Vi samlas på gården, säger hej och delar upp uppgifterna","Vi krattar, rensar rabatter och klipper buskar, och alla hjälper till efter förmåga","Barnen är välkomna, det finns något att göra för alla åldrar","En container för grovavfall står på plats under dagen","Vi avslutar med grillning och fika tillsammans, och det är dagens höjdpunkt"], "list check")}
<p>Har du inte varit med förut? Kom ändå, det är det bästa sättet att lära känna grannarna. Kan du inte komma den dagen går det bra att säga till din grändvärd.</p>
<h2>Grändvärdar 2026/27</h2>
<div class="grid g3 small">
 {card("Runslingan 1 och 3","<p>Familjerna i 1D och 3B</p>")}
 {card("Runslingan 5 och 7","<p>Familjerna i 5C och 7D</p>")}
 {card("Runslingan 9 och 11","<p>Familjerna i 9D och 11B</p>")}
</div>
<p>Grändvärdarna håller koll på gränden och kärlen och fördelar snöskottning av omärkta platser. På vintern ser de också till att det är skottat runt soptunnorna när det behövs, så att alla kommer fram och sopbilen kan tömma. Uppdraget roterar och fastställs på årsstämman.</p>
<h2>Gräsklippning och snöröjning</h2>
<p>Gräsytorna klipper vi själva enligt ett rullande schema – se <a href="#grasklippning">Gräsklippning</a>. Snöröjningen görs av entreprenör; du skottar din egen märkta plats.</p>
""")

PAGES["grasklippning"] = dict(
 lead="De gemensamma gräsytorna klipper vi själva, i ett rullande schema. Varje hushåll har en vecka och ett område.",
 body=f"""
<div class="grid g2">
 {card("Framsidan", "<p>Gräsytan ovanför parkeringen och den större ytan ovanför hus 11.</p><p><b>Klipp även gränderna på baksidan, alltså brandgatorna mellan huslängorna.</b> Se också till att inget står eller ligger i vägen där.</p>")}
 {card("Baksidan", "<p>Från gångbron fram till stigen vid Runslingan.</p>")}
</div>
{callout("Brandgatorna ska alltid vara framkomliga", "<p>Gränderna mellan huslängorna är brandgator. Räddningstjänsten måste kunna ta sig fram där om det börjar brinna. Därför får inget från hushållen stå där, till exempel cyklar, möbler, sopsäckar, ris eller annat skräp.</p><p>Står något i vägen, eller har det vuxit igen? <b>Säg till husägaren direkt eller meddela styrelsen</b> på varingen@proton.me.</p>", "warn")}
<h2>Så fungerar schemat</h2>
{ul(["Varje hushåll får en vecka och ett område, framsidan eller baksidan.","Du ansvarar för att klippningen blir gjord under din vecka.","Är du bortrest eller kan inte klippa? Byt vecka med ett annat hushåll.","Ett hushåll vilar varje år. " + tbd("bekräfta"),"Gräsklipparen står i kallförrådet. " + tbd("Var bensinen finns och hur utlägg ersätts")], "list check")}
<h2>Schema 2027</h2>
<div class="table sched"><div class="sh"><b>Vecka</b><span>Framsidan + brandgator</span><span>Baksidan</span></div><div><b>v. 18</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 20</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 22</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 24</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 26</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 28</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 30</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 32</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 34</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 36</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 38</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 40</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div><div><b>v. 42</b><span>{tbd("hus")}</span><span>{tbd("hus")}</span></div></div>
<p class="note">Styrelsen fastställer schemat inför säsongen, på samma sätt som grändvärdarna roterar. Klippningen infördes genom beslut på årsstämman 2010. Den gamla sidan hade klippning varannan vecka, vecka 18–42.</p>
""")

PAGES["tv-bredband"] = dict(
 lead="Kabel-TV från Telia ingår i årsavgiften och levereras via områdets centralantennanläggning.",
 body=f"""
<div class="grid g3">
 {card("TV-utbud", f"<p>{tbd('Vilket paket/vilka kanaler som ingår – fylls i')}</p><p><a href='https://www.telia.se' rel='noopener'>Telias kanallista →</a></p>")}
 {card("Bredband", f"<p>{tbd('Leverantör, hastigheter och hur man beställer – fylls i')}</p>")}
 {card("Felanmälan", "<p>Fel i din egen utrustning: kontakta Telias kundservice.</p><p>Fel som gäller hela området: kontakta styrelsen.</p>")}
</div>
{callout("Bra att veta", f"<p>Kostnaden för TV ingår i avgiften – du behöver inte teckna eget abonnemang för grundutbudet. {tbd('Bekräfta')}</p>")}
""")

PAGES["dokument"] = dict(
 lead="Alla föreningens viktiga dokument samlade på ett ställe.",
 body=f"""
<div class="docs">
 <h3>Föreningen</h3>
 <a href="../pdf/stadgar.pdf"><b>Stadgar</b><span>Läsversion, ordagrant avskriven. Antagna vid årsstämman 1997-09-22</span><em>PDF</em></a>
 <a href="../pdf/stadgar-original.pdf"><b>Stadgar, original</b><span>Skannat original med underskrifter</span><em>PDF</em></a>
 <a href="../pdf/parkeringsregler.pdf"><b>Ordningsregler för parkering</b><span>Styrelsen</span><em>PDF</em></a>
 <a href="../pdf/sopsortering.pdf"><b>Sopsortering vid kärlen</b><span>Informationsblad, A4</span><em>PDF</em></a>
 <h3>Årsstämma 2026</h3>
 <a href="../pdf/kallelse-arsstamma-2026.pdf"><b>Kallelse med bilagor</b><span>Stämma 28 september 2026, Täby gård</span><em>PDF</em></a>
 <a href="../pdf/protokoll-arsstamma-2026.pdf"><b>Protokoll årsstämma 2026</b><span>{tbd("Publiceras när det är justerat")}</span><em>PDF</em></a>
 <a href="../pdf/underhallsplan-2026.pdf"><b>Underhålls- och förnyelseplan</b><span>2026/27</span><em>PDF</em></a>
 <h3>Arkiv</h3>
 <a href="https://varinge.wordpress.com/" rel="noopener"><b>Gamla hemsidan</b><span>varinge.wordpress.com – protokoll och inlägg 2011–2014</span><em>Länk</em></a>
</div>
<h2>Stadgarna i korthet</h2>
<div class="grid g2 small">
 {card("Vad vi förvaltar (§2)","<p>Lekplatser, gångvägar, parkering, garage, kallförråd, serviceledningar, centralantenn, garagebelysning och entrévägar. Styrelsen får även debitera gemensam sophämtning.</p>")}
 {card("Medlemmar (§3)","<p>Ägarna till de 28 fastigheterna Väringen 1–28. Alla har lika andelstal.</p>")}
 {card("Styrelsen (§4–7)","<p>3–5 ledamöter som väljs på årsstämman för ett år. Möte minst en gång per kvartal.</p>")}
 {card("Inför stämman (§12–13)","<p>Motioner senast 4 veckor före stämman. Kallelse skickas senast 2 veckor före.</p>")}
</div>
""")

FEE_ROWS = [("Snöröjning",1800),("Sophämtning",1400),("Renhållning & städdagar",1100),("Kabel-TV",1050),
            ("Underhållsfond",700),("El & vatten (gemensamt)",450),("Försäkring, bank, bokföring m.m.",750),("Överskott till buffert",700)]

def fee_chart():
    mx = max(v for _, v in FEE_ROWS)
    rows = "".join(f'<div class="bar"><span>{k}</span><i style="--w:{v/mx*100:.0f}%"></i><b>≈ {v:,} kr</b></div>'.replace(",", " ") for k, v in FEE_ROWS)
    return f'<div class="bars">{rows}</div><p class="note">Ungefärlig fördelning per hus av avgiften exklusive moms (8 000 kr), baserad på utfallet 2025/26. Avrundade belopp.</p>'

PAGES["ny-har"] = dict(
 lead="Varmt välkommen till Väringen! Vi är 28 hushåll som delar gård, lekpark och vardag. Här är det viktigaste att veta när du har flyttat in.",
 body=f"""
<ol class="welcome">
 <li><b>Du är automatiskt medlem.</b> Alla som äger ett av de 28 husen ingår i samfälligheten, med lika andel.</li>
 <li><b>Hör av dig till styrelsen</b> på varingen@proton.me. Lämna namn, husnummer och e-post så att fakturor och information hamnar rätt.</li>
 <li><b>Avgiften betalas kvartalsvis.</b> 10 000 kr per år inklusive moms (2026/27) – alltså 2 500 kr per kvartal.</li>
 <li><b>Läs om sopor och parkering.</b> Två saker som påverkar alla grannar varje dag.</li>
 <li><b>Kom på städdagarna.</b> Vår och höst ses vi på gården, hjälps åt en stund och grillar tillsammans. Det är det bästa sättet att lära känna grannarna.</li>
 <li><b>Grändvärd i tur och ordning.</b> Uppdraget roterar mellan hushållen.</li>
</ol>
<h2>Vad avgiften går till – i grova drag</h2>
{fee_chart()}
<h2>Vad vi förväntar oss av varandra</h2>
<div class="grid g2 small">
 {card("Du sköter", ul(["Sortering av ditt avfall","Snöskottning av din märkta plats","Att parkera på rätt ställe","Ditt eget hus och din tomt"]))}
 {card("Föreningen sköter", ul(["Lekplats, gångvägar och belysning","Snöröjning och sophämtning","Garage, kallförråd och gemensam el","Kabel-TV och underhållsplan"]))}
</div>
""")

PAGES["maklare"] = dict(
 lead="Faktablad för mäklare och köpare. Kontakta styrelsen för frågor som inte besvaras här.",
 body=f"""
{facts([
 ("Förening","Anläggningssamfälligheten Väringen"),
 ("Gemensamhetsanläggning","Täby Väringen ga:1"),
 ("Organisationsnummer", tbd("Bekräftas av styrelsen")),
 ("Fastigheter","28 radhus (Väringen 1–28), lika andelstal"),
 ("Adresser","Runslingan 1–11, Täby kyrkby"),
 ("Årsavgift 2026/27","10 000 kr per fastighet inkl. moms, faktureras kvartalsvis. Kabel-TV och sophämtning ingår."),
 ("Engångsavgift","12 000 kr per hushåll för laddstolpar (installerade hösten 2026)"),
 ("Underhållsfond","617 740 kr (bokslut 2026-06-30)"),
 ("Föreningen förvaltar","Lekplatser, gångvägar, parkering, garage, kallförråd, serviceledningar, centralantenn, belysning och entrévägar"),
 ("Pågående projekt","Garageprojektet"),
 ("Laddstolpar","I drift sedan november 2026"),
 ("Kontakt","Styrelsen: varingen@proton.me"),
])}
<h2>Vid ägarbyte</h2>
{ul(["Säljaren meddelar styrelsen tillträdesdag och köparens kontaktuppgifter.", "Avgiften faktureras den som äger fastigheten. " + tbd("Regel för fördelning vid tillträde – bekräfta"), "Köparen får gärna läsa sidan <a href='#ny-har'>Ny i Väringen</a>."], "list check")}
""")

PAGES["historik"] = dict(
 lead="Väringen ligger vid Runslingan i Täby kyrkby – mitt i ett av Sveriges mest runstensrika landskap.",
 body=f"""
<div class="prose">
<p><b>Runriket.</b> Trakten runt Vallentunasjön kallas Runriket. Här står ovanligt många runstenar kvar ute i landskapet, och Jarlabankes bro i Täby är porten in till området. Gatunamnet <i>Runslingan</i> anspelar på runslingan – det ormformade band som runorna ristades i.</p>
<p><b>Väringarna.</b> Väringar kallades de nordbor som tog tjänst hos den bysantinske kejsaren i Konstantinopel. På Täby kyrkas vapenhus finns två inmurade runstensdelar som berättar om Holme, som dog i Langbardaland – Syditalien, som då låg under kejsaren. Han var troligen en av dem.</p>
</div>
<h2>Tidslinje</h2>
<ol class="timeline">
 <li><b>1000-talet</b><span>Jarlabanke reser runstenar och bygger bro i Täby.</span></li>
 <li><b>{tbd("Årtal")}</b><span>Radhusen på Runslingan 1–11 byggs. {tbd("Byggherre/arkitekt")}</span></li>
 <li><b>1997</b><span>Nuvarande stadgar antas den 22 september.</span></li>
 <li><b>2011–2014</b><span>Föreningens första hemsida, varinge.wordpress.com.</span></li>
 <li><b>2026</b><span>Ny styrelse, laddstolpar och ny hemsida.</span></li>
</ol>
{callout("Har du gamla bilder eller berättelser?", "<p>Vi samlar gärna på historik om området. Hör av dig till styrelsen.</p>")}
""")

PAGES["forum"] = dict(
 lead="En plats där vi grannar kan diskutera, ställa frågor och tycka till – utanför årsstämman.",
 body=f"""
<div class="threads">
 <a><span class="chip" style="--c:#b4472c">Garage</span><b>Garageprojektet – tankar om utformning</b><small>Exempeltråd</small></a>
 <a><span class="chip" style="--c:#16181b">Laddning</span><b>Laddstolpar – hur ska debiteringen fungera?</b><small>Exempeltråd</small></a>
 <a><span class="chip" style="--c:#3f7a3c">Utemiljö</span><b>Lekparken – önskemål om ny utrustning</b><small>Exempeltråd</small></a>
 <a><span class="chip" style="--c:#1d7a78">Allmänt</span><b>Lånelådan – vem har en stege eller släpkärra?</b><small>Exempeltråd</small></a>
</div>
{callout("Förslag på teknisk lösning", "<p>Trådarna ovan är exempel. Ett forum kräver en tjänst bakom hemsidan. Styrelsen väljer lösning – se analysen.</p>")}
<p class="note">Forumet är till för medlemmarna. Beslut fattas fortfarande av styrelsen och på årsstämman.</p>
""")

PAGES["kontakt"] = dict(
 lead="Frågor, synpunkter eller felanmälan? Hör av dig – vi svarar så snart vi kan.",
 body=f"""
{facts([("E-post till styrelsen", '<a href="mailto:varingen@proton.me">varingen@proton.me</a>'),("Post", tbd("Postadress – bekräftas"))])}
<h2>Styrelsen 2026/27</h2>
<div class="grid g3 people">
 {card("Emelie Singman, 1C","<p>Ordförande · garage</p>")}
 {card("Nicklas Karpaty, 7A","<p>Sekreterare · hemsida</p>")}
 {card("Alexander Yngve, 9A","<p>Kassör · städdagar</p>")}
</div>
<h2>Vem kontaktar jag?</h2>
<div class="table">
 <div><b>Trasig belysning, lekplats, gångväg</b><span>Styrelsen</span></div>
 <div><b>Soporna har inte tömts</b><span>Styrelsen</span></div>
 <div><b>Fel på TV i ditt hus</b><span>Telias kundservice</span></div>
 <div><b>Skräpigt vid kärlen, snöskottning</b><span>Din grändvärd</span></div>
 <div><b>Förslag till årsstämman</b><span>Motion till styrelsen senast 4 veckor före</span></div>
</div>
""")

NEWS = [
 ("November 2026","Laddstolparna är i drift","Nu kan du ladda elbilen hemma på gården. Information har skickats till alla medlemmar och kommer snart även här.","laddstolpar"),
 ("December 2026","Kvartalsfakturan skickas","Fakturan för nästa kvartal skickas ut i början av december.","ny-har"),
 ("Vinter","Skotta din egen plats","Entreprenören röjer området – din märkta plats skottar du själv.","parkering"),
 ]
DATES = [("Dec","2026","Kvartalsfaktura skickas",""),("17","apr","Vårstäddag 2027","prel."),("27","sep","Årsstämma 2027","prel."),("16","okt","Höststäddag 2027","prel.")]
