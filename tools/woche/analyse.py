#!/usr/bin/env python3
"""Holt die veröffentlichten Posts der letzten 7 Tage samt Kennzahlen aus Zernio (Rohdaten für den Analyst).

  python3 tools/woche/analyse.py [tage=7]  -> out/analyse-roh.json

Zernio holt die Kennzahlen erst beim ersten Abruf von der Plattform und antwortet so lange mit
HTTP 202 („syncStatus: pending“). Deshalb: erst alle Posts anstoßen, dann bis zu RUNDEN-mal mit
Pause nachfragen. Posts auf Kanälen, die in Zernio nicht (mehr) verbunden sind, liefern nie Zahlen
und werden als solche markiert statt als „keine Daten“.
"""
import json, sys, time
from datetime import datetime, timedelta, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import REPO, accounts, call

RUNDEN, PAUSE = 6, 60
tage = int(sys.argv[1]) if len(sys.argv) > 1 else 7
seit = datetime.now(timezone.utc) - timedelta(days=tage)
verbunden = set(accounts())
st, r = call("GET", "/posts?status=published&limit=100")
posts = [p for p in r.get("posts", []) if (p.get("publishedAt") or p.get("scheduledFor") or "") >= seit.isoformat()[:19]]

roh = {}
for p in posts:
    kan = [q.get("platform") for q in p.get("platforms", [])]
    roh[p["_id"]] = {"id": p["_id"], "text": (p.get("content") or "")[:120], "kanaele": kan,
                     "veroeffentlicht": p.get("publishedAt"), "analytics": None, "status": "offen"}
    if not any(k in verbunden for k in kan):
        roh[p["_id"]]["status"] = "Kanal in Zernio nicht verbunden, keine Zahlen möglich"


def abrufen(pid):
    a_st, a = call("GET", f"/analytics?postId={pid}")
    e = roh[pid]
    if a_st == 200:
        e["analytics"] = a.get("analytics"); e["plattformen"] = a.get("platformAnalytics"); e["status"] = "ok"
    elif a_st == 202:
        e["status"] = "wird noch synchronisiert"
    else:
        e["status"] = f"Fehler HTTP {a_st}: {a.get('error') or a.get('message') or ''}"[:160]


offen = [pid for pid, e in roh.items() if e["status"] == "offen"]
for runde in range(RUNDEN):
    for pid in offen: abrufen(pid)
    offen = [pid for pid in offen if roh[pid]["status"] == "wird noch synchronisiert"]
    print(f"Runde {runde + 1}: {len(roh) - len(offen)} fertig, {len(offen)} warten noch")
    if not offen: break
    if runde < RUNDEN - 1: time.sleep(PAUSE)
for pid in offen:
    roh[pid]["status"] = f"nach {RUNDEN} Versuchen noch nicht synchronisiert (Post zu neu oder auf der Plattform gelöscht)"

f = REPO / "out" / "analyse-roh.json"; f.parent.mkdir(exist_ok=True)
f.write_text(json.dumps(list(roh.values()), indent=1, ensure_ascii=False))
zaehl = {}
for e in roh.values(): zaehl[e["status"]] = zaehl.get(e["status"], 0) + 1
print(len(roh), "Posts ->", f); [print(" ", n, "×", s) for s, n in zaehl.items()]
