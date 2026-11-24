# Ny hemsida för Samfälligheten Väringen: analys och förslag

*Underlag till styrelsen, november 2026. Ansvarig för förslaget: Nicklas Karpaty (protokoll nr 3 §12)*

## 1. Bakgrund

- **Gamla sidan** (varinge.wordpress.com) uppdaterades senast 2014. Det går inte att logga in. Där fanns flikarna Bilder, Dokument, Gräsklippningsschema, Kontakt, Motioner, Om, Projekt (garagen), Protokoll och Viktiga datum. Sidan innehåller dessutom privata e-postadresser till tidigare redaktörer.
- **Protokoll nr 2 §6 och nr 3 §12:** En ny hemsida ska ersätta den gamla. Nicklas tar fram förslaget.
- **Stadgarna (1997)** säger vilket ansvar föreningen har (§2), att alla 28 fastigheter har lika andelstal (§3), att styrelsen ska ha 3–5 ledamöter (§4–5) och vilka tidsfrister som gäller inför stämman (§12–13). Det är grunden för det som står på sidan.

## 2. Vad liknande samfälligheter har på sina hemsidor

Radhussamfälligheter i Stockholmsområdet brukar ha med ungefär samma saker:

| Innehåll | Vanligt hos andra | Med i förslaget |
|---|---|---|
| Om föreningen: vad som förvaltas, antal hus | Ja | Startsidan, Mäklarinfo |
| Stadgar och ordningsregler | Ja | Stadgar & protokoll, med stadgarna i korthet |
| Stämmoprotokoll, kallelser, underhållsplan | Ja | Stadgar & protokoll |
| Styrelse och kontakt | Ja | Kontakt & styrelse |
| Sopor, parkering, städdagar | Ja | Egna färgkodade flikar |
| Information till nyinflyttade, ofta en "välkomstmapp" som följer huset | Vanligt | Ny i Väringen |
| Blankett eller rutin vid ägarbyte | Vanligt | Mäklarinfo |
| Historik om området | Ibland | Historik |
| Forum eller anslagstavla | Sällan | Forum (efterfrågat av medlemmarna) |

## 3. Sidstruktur (12 flikar och en startsida)

Varje flik har en egen färg och en knapp för PDF eller utskrift.

1. Sophantering (brun)
2. Parkering (blå)
3. Laddstolpar (svart)
4. Garage & projekt (tegelröd)
5. Städdagar & skötsel (grön)
6. TV & bredband (lila)
7. Stadgar & protokoll (sten/guld)
8. Ny i Väringen (ockra), med en grov fördelning av avgiften
9. Mäklarinfo (skiffer)
10. Historik (runstensröd)
11. Forum (blågrön)
12. Kontakt & styrelse (marinblå)

**Gamla hemsidan:** Den behöver ingen egen flik, eftersom innehållet är föråldrat. Det räcker med en länk under Dokument och i sidfoten. Det som fortfarande gäller (stadgar, parkeringsregler, fakta om området) är redan överfört. Ladda gärna ner det som finns kvar där, eftersom WordPress kan ta bort inaktiva sidor.

## 4. Fyra designförslag

| | Förslag | Känsla | Passar om… |
|---|---|---|---|
| 1 | **Runsten** | Ljus, redaktionell, serif-typsnitt, runbandsornament | ni vill ha något elegant och tidlöst |
| 2 | **Fjäll** | Modern och app-lik, stora färgkort ("bento") | färgerna ska bära navigeringen och mobilen är viktigast |
| 3 | **Nattväring** | Mörk med mässingsdetaljer och sidomeny | ni vill ha en exklusiv och tydligt vikingainspirerad profil |
| 4 | **Föreningspärmen** | En pärm med färgade registerflikar och en anslagstavla | ni vill att sidan ska kännas som föreningens pärm, praktisk och lite lekfull |

Alla fyra har samma innehåll, logga och färgkoder. Det är bara utseendet som skiljer, så det går att välja ett förslag och ta med enskilda detaljer från de andra.

**Loggan** är en *runslinga*, alltså det ormband som runorna ristades i på runstenarna. Den knyter an till gatunamnet Runslingan och till Runriket i Täby. Inuti slingan finns ett hustak och ett V.

## 5. Teknik: GitHub Pages

- Sidan består av statisk HTML utan databas. Det gör hostingen gratis och säker, och sidan blir lätt att flytta.
- Texterna redigeras direkt i GitHub i webbläsaren, eller via Claude.
- **PDF per sida:** Knappen *Skriv ut* ger en ren utskrift med "Spara som PDF". Färdiga PDF:er, till exempel stadgar och sopbladet, läggs i mappen `pdf/`.
- **Egen domän** (t.ex. varingen.se) kostar ungefär 100–200 kr/år och kan kopplas till GitHub Pages.

### Forum: styrelsen behöver välja
GitHub Pages kan inte driva ett forum på egen hand. Alternativ:

| Alternativ | För | Emot |
|---|---|---|
| **A. GitHub Discussions + Giscus** (inbäddat på sidan) | Gratis, ligger på hemsidan | Kräver GitHub-konto, vilket är en tröskel för många |
| **B. Stängd grupp** (Facebook, WhatsApp-community eller Signal) som det länkas till | Alla kan delta direkt | Ligger utanför hemsidan, och inte alla har kontot |
| **C. Hostat forum** (t.ex. Discourse eller Flarum) | Riktigt forum med inloggning | Kostar pengar och kräver drift |

**Rekommendation:** Börja med B, alltså en stängd grupp som länkas från forumsidan, eftersom det är lättast för alla medlemmar. Gå vidare till A eller C om det visar sig finnas behov.

## 6. Integritet (GDPR): GitHub Pages är publikt

- Publicera inte medlemmarnas namn, telefonnummer, kontonummer eller debiteringslängd.
- Styrelsens namn och roller går bra att visa. Grändvärdar anges med husnummer.
- Stämmoprotokoll kan publiceras, men stryk personuppgifter som inte behövs. Styrelseprotokoll lämnas förslagsvis ut på begäran.
- Kontaktformulär kräver en extern tjänst. Föreningens e-postadress räcker.

## 7. Att fylla i eller bekräfta (gult markerat på sidorna)

- [ ] Organisationsnummer (717900-0299 eller 816000-1635)
- [ ] Föreningens e-postadress (Gmail, Alexander) och postadress
- [ ] Tömningsdag för soporna
- [ ] Laddstolpar: hur man laddar, hur elen debiteras, felanmälan, om engångsavgiften gäller alla hushåll
- [ ] Telia: vilket TV-paket som ingår och vad som gäller för bredband
- [ ] Datum för städdagar och stämma 2027 enligt stämmoprotokollet
- [ ] Gräsklippningsschema och rutin för att låna redskap i kallförrådet
- [ ] Byggår och byggherre för husen (historiksidan)
- [ ] Regel för avgiften vid ägarbyte
- [ ] Foton: husen, lekparken, gårdarna (Nicklas)

## 8. Nästa steg

1. Styrelsen väljer förslag, eller en kombination av förslag.
2. Styrelsen beslutar om forumlösning och om vilka protokoll som ska publiceras.
3. Gula uppgifter fylls i och foton läggs in.
4. Sidan publiceras på GitHub Pages och länkas i nästa informationsblad.
