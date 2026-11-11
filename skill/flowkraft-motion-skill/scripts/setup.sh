#!/bin/bash
# Einmalig pro Rechner: Render-Umgebung anlegen. Braucht Google Chrome, ffmpeg und Python 3.
set -e
ENV="$HOME/.flowkraft-motion/venv"
command -v ffmpeg >/dev/null || { echo "ffmpeg fehlt: brew install ffmpeg (Mac) oder apt-get install -y ffmpeg (Linux)"; exit 1; }
[ -x "$ENV/bin/python" ] || python3 -m venv "$ENV"
"$ENV/bin/pip" install -q playwright numpy fonttools brotli
# ohne Google Chrome (z. B. Linux/Cloud): mitgeliefertes Chromium laden
[ -d "/Applications/Google Chrome.app" ] || command -v google-chrome >/dev/null || "$ENV/bin/python" -m playwright install --with-deps chromium
echo "OK: $ENV/bin/python"
