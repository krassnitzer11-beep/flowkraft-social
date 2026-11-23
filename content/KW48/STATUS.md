# Status KW 48 (zweiter Testlauf, Produktion fertig Mo 23.11.2026)

## Verspätet
- Der Sonntags-Lauf vom 22.11. ist nach Plan und Recherche abgebrochen (Branch endete bei „KW 48: Recherche“). Dieser Lauf hat am **Mo 23.11. ab ca. 08:35 Wien** fortgesetzt und war gegen 10:45 fertig.
- Die Montags-Mail (08:00) lief deshalb vor Fertigstellung, vermutlich mit „Woche ist NICHT fertig“. Die Freigabeseite ist jetzt trotzdem da (Link in freigabe-link.txt).
- Der Mo-Post ist für heute 18:00 angelegt. Testlauf: nichts posten, „flowkraft Freigabe“ bleibt aus.

## Fertig
- Plan, Gegenposition, Recherche (vom 22.11.), Texte, Post-Dateien, Prüfbericht und Ampel (2 Runden + Entscheidung Manager).
- Ampel: Mo, Di, Mi, Do, Fr grün; Sa gelb (Beispiel „Bestellung beim Lieferanten“ ist frei gewählt, nicht aus Daniels Musterprojekt, braucht seine Bestätigung).
- Gerendert in der Cloud (ca. 1 h): Mo-Reel Drohnenflug 31,8 s (dark), Do-Reel Drohnenflug 26,5 s (mist, dunkle Schrift, neue Kontrast-Option), LinkedIn-Video 4:5 aus dem Mo-Reel (34 s, 1080×1350), Di Karussell 7 Slides, Sa Karussell 8 Slides (+ Facebook-Galerien), Mi/Fr Standbilder (clean), 6 Storys als reine Textstorys.
- Zernio: 14 Entwürfe (isDraft: true, nichts eingeplant): Facebook 6 Posts + 6 Storys, LinkedIn 2 (Di Video, Do Standbild). Instagram: 12 Vorschauen (6 Posts + 6 Storys), nur hochgeladen, absichtlich nicht verbunden.
- Freigabeseite auf Netlify (Deploy „ready“), Link in freigabe-link.txt.

## Hinweise für Daniel
- Freigabeseite liefert ohne Netlify-Anmeldung HTTP 401 (Visitor access, wie in KW 47). Im Browser bei Netlify angemeldet sein.
- Testlauf: Knöpfe nicht klicken bzw. vor dem Einschalten von „flowkraft Freigabe“ die Make-Warteschlange leeren. Entwürfe nach der Durchsicht in Zernio löschen.
- Engine geändert (skill/flowkraft-motion-skill/engine/engine.html): neue Szenen feierabend, team, waechter, zuerst; neue optionale Props; neue Optionen `middle` (Slide) und `contrast` (Mist-Post). Mac-Kopie des Skills abgleichen. `middle` und `contrast` stehen noch nicht in references/scenes.md.
- Zur Entscheidung: Storys sind diese Woche reine Textstorys, weil 22 Szenen nicht für Posts und Storys reichen (Regel „jede Szene einmal pro Woche, auch Storys“). Als festes Format bestätigen oder neue Szenen bauen lassen.
- Szenen `comment` (Di Slide 7, „Weiterleiten“) und `roiform` (Sa Slide 5, „Meldung“) wurden umgedeutet, ohne Keyword und ohne Euro. Prüfer: sieht nicht nach Lead-Keyword oder ROI-Rechner aus.
- `docs/praxisbeispiele.md` und `docs/lead-magnete.md` fehlen weiterhin (Säule 5 wackelt, kein Lead-Weg).
