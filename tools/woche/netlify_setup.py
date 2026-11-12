#!/usr/bin/env python3
"""Einmalig: legt die Netlify-Seite für die Freigabe an und gibt NETLIFY_SITE_ID aus.

  NETLIFY_TOKEN=... python3 tools/woche/netlify_setup.py   (oder Token in ~/.flowkraft-motion/netlify.env)
"""
import json, os, secrets, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import CTX

tok = os.environ.get("NETLIFY_TOKEN")
env = Path.home() / ".flowkraft-motion" / "netlify.env"
if not tok and env.exists():
    for l in env.read_text().splitlines():
        if l.startswith("NETLIFY_TOKEN="): tok = l.split("=", 1)[1].strip().strip('"')
if not tok: sys.exit("NETLIFY_TOKEN fehlt.")
name = f"flowkraft-freigabe-{secrets.token_hex(3)}"
req = urllib.request.Request("https://api.netlify.com/api/v1/sites", data=json.dumps({"name": name}).encode(), method="POST",
                             headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=60, context=CTX) as r: d = json.loads(r.read())
print("Seite:", d.get("ssl_url") or d.get("url"))
print("NETLIFY_SITE_ID=" + d["id"])
if env.exists():
    t = env.read_text()
    if "NETLIFY_SITE_ID=" not in t: env.write_text(t.rstrip("\n") + f"\nNETLIFY_SITE_ID={d['id']}\n")
