#!/usr/bin/env python3
"""Montag 8 Uhr: E-Mail an Daniel über den Make-Webhook MAKE_NOTIFY_URL (Make verschickt die Mail).

  python3 tools/woche/notify.py content/KW48
"""
import html, json, os, ssl, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import CTX, ampel, ampel_html, week

w, plan, out = week(sys.argv[1])
hook = os.environ.get("MAKE_NOTIFY_URL") or sys.exit("MAKE_NOTIFY_URL fehlt.")
# Montag läuft in einer frischen Cloud-Kopie: der Link kommt aus dem Wochen-Branch (content/KWnn/freigabe-link.txt)
link_f = next((f for f in (w / "freigabe-link.txt", out / "freigabe-link.txt") if f.exists()), None)
link = link_f.read_text().strip() if link_f else ""
rows = ampel(w, plan)
rot = sum(r["ampel"] == "rot" for r in rows)
bereit = f"flowkraft: KW {plan['kw']} ist bereit zur Freigabe" + (f" ({rot} blockiert)" if rot else "")
body = {"betreff": bereit if link else f"flowkraft: Woche KW {plan['kw']} ist NICHT fertig",
        "link": link, "hooks": ampel_html(rows),
        "offene_einwaende": "Details zu jedem Punkt stehen auf der Freigabeseite." if rows else "", "kw": plan["kw"]}
req = urllib.request.Request(hook, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST")
with urllib.request.urlopen(req, timeout=60, context=CTX) as r: print("Benachrichtigung:", r.status)
