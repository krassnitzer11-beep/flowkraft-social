# Wochenablauf flowkraft Social

Läuft automatisch in der Cloud. Daniel gibt nur frei. **Nichts geht live ohne seine Freigabe auf der Freigabeseite.**

| Wann | Routine | Was passiert |
|---|---|---|
| Sa 06:00 | Analyse | `analyst` wertet die Vorwoche aus → `content/analysen/KWnn.md` |
| So 05:00 | Produktion | Plan, Texte, Post-Dateien, Prüfung, Rendern, Zernio-Entwürfe, Freigabeseite |
| Mo 08:00 | Benachrichtigung | E-Mail an Daniel mit Link zur Freigabeseite |
| Mo–Sa | Posten | Zernio postet nur, was freigegeben ist |

## Produktion (Sonntag), Schritt für Schritt

Arbeite im Repository-Wurzelordner. KW = die kommende Woche (Mo–Sa).

1. **Plan:** `social-media-manager` schreibt `content/KWnn/gegenposition.md` und `content/KWnn/plan.json` (Schema: `tools/woche/PLAN.md`). Grundlage: Analyse, Vorwoche, `docs/`.
2. **Recherche:** `recherche` → `content/KWnn/recherche.md`.
3. **Texte:** `copywriter` → `content/KWnn/texte.md`.
4. **Design:** `designer` → `content/KWnn/posts/*.js`, Kontrollbilder prüfen.
5. **Prüfung:** `pruefer` → `content/KWnn/pruefbericht.md`. Höchstens zwei Korrekturrunden, dann entscheidet der Manager.
6. **Rendern:** `python3 tools/woche/build.py content/KWnn` (dauert in der Cloud 1,5–2 h). Ergebnis in `out/KWnn/` plus `out/KWnn/manifest.json`.
7. **Entwürfe:** `python3 tools/woche/drafts.py content/KWnn` lädt alles zu Zernio hoch und legt jeden Post als **Entwurf** an (nicht eingeplant).
8. **Freigabeseite:** `python3 tools/woche/freigabe.py content/KWnn` baut die Seite und lädt sie hoch, Link in `out/KWnn/freigabe-link.txt`.
9. **Sichern:** Texte, Plan, Post-Dateien und Berichte committen (keine Videos), Branch `woche/KWnn`, kurz zusammenfassen.

## Benachrichtigung (Montag 08:00)

`python3 tools/woche/notify.py content/KWnn` schickt die E-Mail über Make (Webhook `MAKE_NOTIFY_URL`).

## Umgebungsvariablen (in der Cloud-Umgebung hinterlegt, nie im Repository)

- `ZERNIO_API_KEY`
- `MAKE_NOTIFY_URL` – Make-Webhook „Woche bereit“ → E-Mail an Daniel
- `MAKE_APPROVE_URL` – Make-Webhook „Freigabe“ → setzt den Zernio-Entwurf auf eingeplant
- `NETLIFY_TOKEN`, `NETLIFY_SITE_ID` – Netlify hostet die Freigabeseite (Pfad mit Zufallsteil, noindex)

## Regeln, die nie verletzt werden

- Keine erfundenen Zahlen, Kundenstimmen, Preise. Beispielrechnungen kennzeichnen.
- Keyword ROI nur, wenn `docs/lead-magnete.md` es als live führt.
- Alle Posts um 18:00 Uhr (Wien), Mo–Sa, auf allen Kanälen.
- Storys automatisch, ohne Sticker (keine Umfrage, keine Frage-Box): die Frage steht als Text in der Story.
- Reels nur als Drohnenflug. Einzel-Posts als Standbild. LinkedIn: Di Video 4:5, Do Standbild, kein PDF.
- Nie selbst veröffentlichen: nur Entwürfe (`isDraft: true`).
