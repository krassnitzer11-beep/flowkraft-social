#!/usr/bin/env python3
"""Holt die veröffentlichten Posts der letzten 7 Tage samt Kennzahlen aus Zernio (Rohdaten für den Analyst).

  python3 tools/woche/analyse.py [tage=7]  -> out/analyse-roh.json
Welche Kennzahlen Zernio liefert, hängt vom Kanal ab; fehlende Felder bleiben leer.
"""
import json, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import REPO, call

tage = int(sys.argv[1]) if len(sys.argv) > 1 else 7
seit = datetime.now(timezone.utc) - timedelta(days=tage)
st, r = call("GET", "/posts?status=published&limit=100")
posts = [p for p in r.get("posts", []) if (p.get("publishedAt") or p.get("scheduledFor") or "") >= seit.isoformat()[:19]]
roh = []
for p in posts:
    a_st, a = call("GET", f"/analytics?postId={p['_id']}")
    roh.append({"id": p["_id"], "text": (p.get("content") or "")[:120], "kanaele": [q.get("platform") for q in p.get("platforms", [])],
                "url": [q.get("platformPostUrl") for q in p.get("platforms", [])], "analytics": a if a_st == 200 else None})
f = REPO / "out" / "analyse-roh.json"; f.parent.mkdir(exist_ok=True); f.write_text(json.dumps(roh, indent=1, ensure_ascii=False))
print(len(roh), "Posts ->", f)
