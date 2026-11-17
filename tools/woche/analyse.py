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

# Wochen-Kennzahlen für Daniel (Mail und Freigabeseite): content/analysen/KWnn-zahlen.json
# Der Analyst ergänzt danach nur das Feld "lernpunkt" (ein Satz, was das Team daraus ändert).
heute = datetime.now(timezone.utc)
kw = heute.astimezone().isocalendar()[1]
_, fs = call("GET", f"/accounts/follower-stats?fromDate={seit.date()}&toDate={heute.date()}")
follower = [{"kanal": a["platform"], "aktuell": a.get("currentFollowers"), "zuwachs": a.get("growth")} for a in fs.get("accounts", []) if a.get("isActive")]
zeilen = []
for e in roh.values():
    a = e.get("analytics") or {}
    if e["status"] != "ok": continue
    inter = sum(a.get(k) or 0 for k in ("likes", "comments", "shares", "saves"))
    reich = a.get("reach") or a.get("impressions") or 0
    zeilen.append({"datum": (e.get("veroeffentlicht") or "")[:10], "kanal": e["kanaele"][0] if e["kanaele"] else "",
                   "text": e["text"].split("\n")[0][:70], "impressionen": a.get("impressions") or 0, "reichweite": a.get("reach") or 0,
                   "aufrufe": a.get("views") or 0, "interaktionen": inter, "speichern_teilen": (a.get("saves") or 0) + (a.get("shares") or 0),
                   "rate": round(100 * inter / reich, 1) if reich else None})
zeilen.sort(key=lambda z: (z["datum"], z["kanal"]))
summe = {k: sum(z[k] for z in zeilen) for k in ("impressionen", "reichweite", "aufrufe", "interaktionen", "speichern_teilen")}
bewertet = [z for z in zeilen if z["reichweite"] or z["impressionen"]]
rang = sorted(bewertet, key=lambda z: (z["interaktionen"], z["reichweite"] or z["impressionen"]), reverse=True)
zahlen = {"kw": kw, "von": str(seit.date()), "bis": str(heute.date()), "follower": follower, "posts": len(zeilen), "summe": summe,
          "top": rang[0] if len(rang) >= 2 else None, "flop": rang[-1] if len(rang) >= 2 else None, "zeilen": zeilen,
          "ohne_zahlen": [{"text": e["text"].split("\n")[0][:70], "grund": e["status"]} for e in roh.values() if e["status"] != "ok"],
          "zu_wenig_daten": len(bewertet) < 3, "lernpunkt": ""}
z = REPO / "content" / "analysen" / f"KW{kw:02d}-zahlen.json"; z.parent.mkdir(parents=True, exist_ok=True)
z.write_text(json.dumps(zahlen, indent=1, ensure_ascii=False)); print("Wochen-Kennzahlen ->", z)
