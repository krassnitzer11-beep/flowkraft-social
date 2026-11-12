# Wochenplan `content/KWnn/plan.json`

```json
{
  "kw": 48,
  "jahr": 2026,
  "theme_default": "dark",
  "posts": [
    {"tag": "Mo", "datum": "2026-11-23", "zeit": "18:00", "format": "reel",      "saeule": "1 Zeitfresser",
     "post": "posts/mo-reel-termine.js", "texte": "Mo 23.11.", "story": 1,
     "linkedin": null},
    {"tag": "Di", "datum": "2026-11-24", "zeit": "18:00", "format": "karussell", "saeule": "4 Rechnet sich das?",
     "post": "posts/di-karussell-angebote.js", "texte": "Di 24.11.", "story": 2,
     "linkedin": {"datum": "2026-11-24", "zeit": "18:00", "typ": "video", "quelle": "Mo", "texte": "Mo 23.11."}},
    {"tag": "Mi", "format": "post", "...": "..."}
  ],
  "storys": "posts/storys.js"
}
```

- `format`: `reel` (Drohnenflug), `karussell` (Video-Slides; Facebook bekommt die Bildergalerie), `post` (Standbild, `clean: true`).
- `texte`: Überschrift des Tages in `texte.md` (`## Mo 23.11. · …`), daraus kommen Caption und LinkedIn-Text.
- `story`: Nummer der Slide in `storys.js`. Storys werden **automatisch und ohne Sticker** gepostet (Instagram und Facebook), zur selben Zeit wie der Post. Die Frage steht als Text in der Story.
- `linkedin`: nur Di (`typ: video`, 4:5 aus dem genannten Reel) und Do (`typ: bild`, Standbild); `quelle` = Tag, dessen Post die Medien liefert; `texte` = Abschnitt mit dem LinkedIn-Text.
- **Alle Posts um 18:00** Ortszeit Wien, auch LinkedIn (Entscheidung von Daniel, 12.11.2026).
