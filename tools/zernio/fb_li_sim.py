#!/usr/bin/env python3
"""Simulation KW 47 auf Facebook (alle 6 Tage) und LinkedIn (Di Video, Do Standbild), 2 Minuten Abstand pro Tag.

  python3 fb_li_sim.py plan                       zeigt, was wann rausgeht (schickt nichts)
  python3 fb_li_sim.py planen 2026-11-11T14:10:00 plant alles echt ein, IDs in fbli-ids.json
  python3 fb_li_sim.py status                     Status aller Posts
"""
import json, os, sys
from datetime import datetime, timedelta
from pathlib import Path

ns = {"__file__": os.path.abspath(Path(__file__).parent / "zernio_test.py")}
exec((Path(__file__).parent / "zernio_test.py").read_text().split("ap = argparse")[0], ns)
call, upload, caption, account, ROOT = ns["call"], ns["upload"], ns["caption"], ns["account"], ns["ROOT"]
IDS = Path(__file__).parent / "fbli-ids.json"
V, FB = ROOT / "videos", ROOT / "facebook"
COVER = {"kw47-mo-termine-reel.mp4": ROOT / "cover/kw47-mo-termine-cover.jpg", "kw47-do-anfragen-reel.mp4": ROOT / "cover/kw47-do-anfragen-cover.jpg"}

# Tag, Facebook-Medien, LinkedIn (Medien, Text-Block aus Tag)
DAYS = [
    ("Mo 16.11.", [V / "1-mo/kw47-mo-termine-reel.mp4"], None),
    ("Di 17.11.", sorted((FB / "kw47-di-angebote").glob("*.png")), ([V / "1-mo/kw47-mo-termine-reel.mp4"], "Mo 16.11.")),
    ("Mi 18.11.", [ROOT / "posts-statisch/kw47-mi-excel.png"], None),
    ("Do 19.11.", [V / "4-do/kw47-do-anfragen-reel.mp4"], ([ROOT / "posts-statisch/kw47-sa-drei-fragen.png"], "Fr 20.11.")),
    ("Fr 20.11.", sorted((FB / "kw47-fr-suchen").glob("*.png")), None),
    ("Sa 21.11.", [ROOT / "posts-statisch/kw47-sa-drei-fragen.png"], None),
]
TYPE = lambda p: "video" if p.suffix == ".mp4" else "image"


def item(p):
    m = {"type": TYPE(p), "url": upload(p)}
    if p.name in COVER: m["thumbnail"] = upload(COVER[p.name])   # bei Facebook und LinkedIn wirkt das Feld am Medium
    return m


def show(start):
    t0 = datetime.fromisoformat(start)
    for i, (day, fb, li) in enumerate(DAYS):
        when = (t0 + timedelta(minutes=2 * i)).strftime("%H:%M")
        print(f"{when}  {day}  Facebook: {len(fb)} x {TYPE(fb[0])}" + (f"  |  LinkedIn: {TYPE(li[0][0])} mit Text von {li[1]}" if li else ""))


def planen(start):
    accs = call("GET", "/accounts")[1].get("accounts", [])
    fb_id, li_id = account(accs, "facebook"), account(accs, "linkedin")
    t0, ids = datetime.fromisoformat(start), []
    for i, (day, fb, li) in enumerate(DAYS):
        when = (t0 + timedelta(minutes=2 * i)).isoformat(timespec="seconds")
        base = {"scheduledFor": when, "timezone": "Europe/Vienna"}
        jobs = [("facebook", {**base, "content": caption(day, "Caption Instagram und Facebook"), "mediaItems": [item(p) for p in fb],
                 "platforms": [{"platform": "facebook", "accountId": fb_id}]})]
        if li:
            jobs.append(("linkedin", {**base, "content": caption(li[1], "LinkedIn"), "mediaItems": [item(p) for p in li[0]],
                         "platforms": [{"platform": "linkedin", "accountId": li_id}]}))
        for name, body in jobs:
            st, r = call("POST", "/posts", body); pid = r.get("post", {}).get("_id")
            print(f"{day} {name} {when[11:16]}: HTTP {st} {r.get('post', {}).get('status', r)}")
            if pid: ids.append({"day": day, "what": name, "id": pid, "when": when})
            IDS.write_text(json.dumps(ids, indent=1, ensure_ascii=False))


def status():
    for x in json.loads(IDS.read_text()):
        p = call("GET", f"/posts/{x['id']}")[1].get("post", {})
        pl = [(q.get("status"), q.get("errorMessage") or q.get("error"), q.get("platformPostUrl")) for q in p.get("platforms", [])]
        print(x["day"], x["what"], x["when"][11:16], p.get("status"), pl)


cmd = sys.argv[1]
if cmd == "plan": show(sys.argv[2] if len(sys.argv) > 2 else datetime.now().replace(second=0).isoformat())
elif cmd == "planen": planen(sys.argv[2])
else: status()
