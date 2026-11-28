# Samfälligheten Väringen: ny hemsida (förslag)

Två designförslag för styrelsen att diskutera. Alla förslag har samma innehåll.

```
site/
  index.html                 ← översikt med länkar till förslagen
  forslag-2a-fjall/          ← modern, stora färgkort
  forslag-2b-fjall-flikar/   ← grupperade flikar, sök (huvudspår)
  assets/logo-varingen.svg
  pdf/                       ← lägg färdiga PDF:er här (stadgar.pdf, sopsortering.pdf …)
src/                         ← generator: content.py (texter), themes.py + theme_fjall.py (utseende), build.py
ANALYS.md                    ← analys och beslutspunkter för styrelsen
```

## Lägga upp på GitHub Pages (cirka 10 minuter)

1. Skapa ett konto på github.com, om det inte redan finns.
2. Skapa ett nytt repository, t.ex. `varingen`. Det ska vara **Public**, eftersom det krävs för gratis Pages.
3. Välj **Add file → Upload files** och dra in *innehållet* i mappen `site/` (inte själva mappen). Klicka sedan på **Commit**.
4. Gå till **Settings → Pages → Build and deployment**. Välj *Deploy from a branch* och sedan `main` / `(root)`, och klicka **Save**.
5. Efter någon minut ligger sidan på `https://<användarnamn>.github.io/varingen/`.

Vill ni ha en egen domän, t.ex. varingen.se? Lägg in den under *Settings → Pages → Custom domain* och peka domänens DNS mot GitHub.

## Ändra texter

- **Enkelt:** Redigera direkt i `index.html` på GitHub (pennikonen).
- **Alla förslag på en gång:** Ändra i `src/content.py` och kör `python3 src/build.py`.
- Text inom `<span class="tbd">…</span>` visas gulmarkerad. Det betyder att uppgiften ska fyllas i.

## PDF per sida

- *Skriv ut*-knappen skriver bara ut den sida som visas. Välj "Spara som PDF".
- *Ladda ned*-knappen pekar på `pdf/<sidnamn>.pdf`, t.ex. `pdf/sophantering.pdf`. Lägg dit färdiga PDF:er.

## Bilder

Lägg foton i `assets/` och byt ut platshållarna (`<figure class="photo">`) mot `<img src="../assets/hus.jpg" alt="…">`.
