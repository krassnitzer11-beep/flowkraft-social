# Status KW 47 (Trockenlauf, Produktion So 15.11.2026)

## Fertig
- Plan, Gegenposition, Recherche, Texte, Post-Dateien, Prüfbericht (1 Korrekturrunde) in `content/KW47/`.
- Grundlage: das am 09.11.2026 freigegebene Probewochen-Material (`content/kw47/`), angepasst an 18:00, Storys ohne Sticker, Reels als Drohnenflug, LinkedIn Di Video 4:5 / Do Standbild.
- Gerendert (Cloud): Mo- und Do-Reel als Drohnenflug (20,1 s / 23,6 s, 1080×1920, Titelbild), Di/Fr Karussell-Videos (7 + 6 Slides) plus Facebook-Galerie, Mi/Sa Standbilder, 6 Storys, LinkedIn-Video 4:5 (1080×1350, 34 s).
- Zernio: 14 Entwürfe (`isDraft: true`, nichts eingeplant): Facebook 6 Posts + 6 Storys, LinkedIn 2 (Di Video, Do Standbild). Instagram: 12 Vorschauen (6 Posts + 6 Storys), nur hochgeladen, nicht angelegt, da absichtlich nicht verbunden.
- Freigabeseite auf Netlify hochgeladen (Deploy „ready“), Link in `freigabe-link.txt`. Seite enthält 14 Karten mit Knöpfen und 12 Instagram-Vorschauen.

## Hinweise / Probleme
- **Freigabeseite liefert ohne Netlify-Anmeldung HTTP 401.** Auf der Netlify-Seite ist „Visitor access“ per Netlify-Team-Login (SSO, alle Deploys) aktiv. Daniel muss im Browser bei Netlify angemeldet sein, um die Seite zu sehen. Nicht verändert. Falls die Seite öffentlich (nur über den Zufallspfad) erreichbar sein soll: in Netlify unter Site configuration → Access & security → Visitor access den Schutz abschalten (Entscheidung Daniel).
- **Trockenlauf:** Make-Szenario „flowkraft Freigabe“ ist laut CLAUDE.md aus. Knöpfe auf der Seite also nicht klicken; Klicks würden sich in der Webhook-Warteschlange sammeln und beim Einschalten ausgeführt. Die KW-47-Entwürfe nach der Durchsicht in Zernio löschen.
- LinkedIn-Video 4:5 ist kein Drohnenflug, sondern die Reel-Slides als 4:5-Karussell-Videos aneinandergehängt (so baut es `build.py`).
- Analyse KW 46 ohne Kennzahlen (alle HTTP 202), Vorwochen-Branch `claude/woche-KW46` gab es nicht.
- Offene Prüfer-Einwände: siehe `pruefbericht.md` (Sa-Hook 8 Wörter, Do-Reel 5/8, Szenen-Wiederholungen, `yeargrid` zeigt fest 240 Kästchen).
