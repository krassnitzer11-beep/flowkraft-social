#!/usr/bin/env python3
"""Montag 8 Uhr: E-Mail an Daniel über den Make-Webhook MAKE_NOTIFY_URL (Make verschickt die Mail).

  python3 tools/woche/notify.py content/KW48
"""
import html, json, os, ssl, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import CTX, text, week

w, plan, out = week(sys.argv[1])
hook = os.environ.get("MAKE_NOTIFY_URL") or sys.exit("MAKE_NOTIFY_URL fehlt.")
link_f = out / "freigabe-link.txt"
link = link_f.read_text().strip() if link_f.exists() else ""
hooks = [f"{p['tag']} · {p['format']} · {text(w, p['texte'], 'Hook') or text(w, p['texte'], 'Text im Bild')}" for p in plan["posts"]]
offen = ""
if (w / "pruefbericht.md").exists():
    t = (w / "pruefbericht.md").read_text(); i = t.find("## Offene Einwände")
    offen = t[i:i + 1500] if i >= 0 else ""
body = {"betreff": f"flowkraft: Woche KW {plan['kw']} ist bereit zur Freigabe" if link else f"flowkraft: Woche KW {plan['kw']} ist NICHT fertig",
        "link": link, "hooks": "<br>".join(html.escape(h) for h in hooks),
        "offene_einwaende": html.escape(offen).replace("\n", "<br>"), "kw": plan["kw"]}
req = urllib.request.Request(hook, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST")
with urllib.request.urlopen(req, timeout=60, context=CTX) as r: print("Benachrichtigung:", r.status)
