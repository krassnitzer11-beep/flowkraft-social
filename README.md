# flowkraft Social

Privat. Agenten-System für die flowkraft-Posts auf Instagram, Facebook und LinkedIn.

- `skill/flowkraft-motion-skill/` – Motion-Engine (Karussell, Story, Reel, Drohnenflug), Anleitung in `SKILL.md`
- `content/kw47/` – Probewoche KW 47: Post-Dateien, Texte, Prüfbericht
- `docs/` – Voice, Teamregeln, Planer-Test
- `tools/zernio/` – Einplanen über Zernio (Schlüssel nur als Umgebungsvariable `ZERNIO_API_KEY`)

## Rendern (Mac oder Cloud)

```bash
bash skill/flowkraft-motion-skill/scripts/setup.sh
~/.flowkraft-motion/venv/bin/python skill/flowkraft-motion-skill/engine/render.py content/kw47/posts/mi-post-excel.js --out out --format carousel
```
