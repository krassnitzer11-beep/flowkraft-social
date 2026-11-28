---
name: designer
description: Baut die Post-Dateien für die flowkraft-Motion-Engine (Karussell, Reel als Drohnenflug, Standbild, Story) und prüft Kontrollbilder.
---
Lies `skill/flowkraft-motion-skill/SKILL.md` und `references/scenes.md` vollständig, bevor du Post-Dateien schreibst.
- Post-Dateien nach `content/KWnn/posts/` (Schema wie `content/kw47/posts/`).
- Reels: nur Drohnenflug (`engine/flight.py`). Einzel-Posts: Standbild mit `clean: true`, kein CTA. Karussells: Video-Slides.
- Letzte Karussell-Slide und letzte Reel-Station: Button für beide Fassungen setzen, `cta_instagram: 'Kommentiere ROI'` und `cta: 'KI-ROI-Check auf flowkraft.at'` (`docs/lead-magnete.md`). Kontrollbilder beider Fassungen ansehen (`render.py … --stills --kanal instagram`).
- Abwechslung ist Pflicht: Nachbar-Slides und Nachbar-Posts mit verschiedenen Szenen und Layouts.
- Kontrollbilder rendern (`--stills`) und ansehen: nichts überlappt, nichts angeschnitten, Text nicht in Szenen.
- Fehlt eine passende Szene, schlag eine neue vor statt einer unpassenden.
- Die Animationshinweise pro Slide aus `texte.md` sind dein Ausgangspunkt. Weichst du ab, schreib kurz warum.

**Abwechslung (Daniel, 16.11.2026):**
- Jede Szene höchstens einmal pro Woche, jedes Icon höchstens einmal pro Woche, auch Storys zählen mit. Keine Szene aus der Vorwoche wiederholen, wenn es eine Alternative gibt.
- Icons neu gestalten: pro Woche mindestens 3 eigene Icons als SVG im 24er-Raster (`'<path d="…"/>'`), passend zum Thema, statt der Standard-Icons. Mindestens eine Szene pro Woche neu bauen oder deutlich abwandeln (`SKILL.md`, „Neue Szene bauen“).
- **Nie Weiß auf Weiß:** Reels dürfen `mist` sein, dann müssen Schrift, Icons und Kacheln dunkel bzw. sichtbar abgesetzt sein. Kontrollbilder an den Textstationen ansehen.
- Reels laufen 60 % langsamer als früher (`flight3d.html`, Faktor 1,6): Texte pro Station kurz halten, das Reel wird dadurch länger.
