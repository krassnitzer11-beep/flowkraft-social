#!/usr/bin/env python3
"""Simulation KW 47 im 15-Minuten-Takt (Instagram + LinkedIn, Storys ohne Sticker).

  python3 woche_sim.py planen 2026-11-09T12:40:00   plant alles ein, IDs in sim-ids.json
  python3 woche_sim.py status                       Status aller Posts
  python3 woche_sim.py loeschen                     alle Posts der Simulation löschen
"""
import json, os, sys
from datetime import datetime, timedelta
from pathlib import Path

ns = {"__file__": os.path.abspath(Path(__file__).parent / "zernio_test.py")}
exec((Path(__file__).parent / "zernio_test.py").read_text().split("ap = argparse")[0], ns)
call, upload, caption, account, ROOT = ns["call"], ns["upload"], ns["caption"], ns["account"], ns["ROOT"]
IDS = Path(__file__).parent / "sim-ids.json"

V = ROOT / "videos"
DAYS = [  # Tag, Feed-Medien, LinkedIn-Medien (None = Text, [] = kein LinkedIn), Story
    ("Mo 16.11.", [V / "1-mo/kw47-mo-termine-reel.mp4"], None, V / "storys/kw47-story-1-calendar-9x16.mp4"),
    ("Di 17.11.", sorted((V / "2-di").glob("*.mp4")), [ROOT / "linkedin/kw47-di-angebote-linkedin.pdf"], V / "storys/kw47-story-2-calculator-9x16.mp4"),
    ("Mi 18.11.", [ROOT / "posts-statisch/kw47-mi-excel.png"], [], V / "storys/kw47-story-3-hourglass-9x16.mp4"),
    ("Do 19.11.", [V / "4-do/kw47-do-anfragen-reel.mp4"], [], V / "storys/kw47-story-4-chaos-9x16.mp4"),
    ("Fr 20.11.", sorted((V / "5-fr").glob("*.mp4")), None, V / "storys/kw47-story-5-pile-9x16.mp4"),
    ("Sa 21.11.", [ROOT / "posts-statisch/kw47-sa-drei-fragen.png"], [], V / "storys/kw47-story-6-none-9x16.mp4"),
]
COVER = {"kw47-do-anfragen-reel.mp4": ROOT / "cover/kw47-do-anfragen-cover.jpg", "kw47-mo-termine-reel.mp4": ROOT / "cover/kw47-mo-termine-cover.jpg"}
TYPE = lambda p: "video" if p.suffix == ".mp4" else "document" if p.suffix == ".pdf" else "image"


def planen(start, nur=None):
    accs = call("GET", "/accounts")[1].get("accounts", [])
    ig, li = account(accs, "instagram"), account(accs, "linkedin")
    t0, ids = datetime.fromisoformat(start), []
    days = [d for d in DAYS if not nur or d[0][:2] in nur]
    for i, (day, feed, lin, story) in enumerate(days):
        when = (t0 + timedelta(minutes=15 * i)).isoformat(timespec="seconds")
        print(f"\n{day} -> {when}")
        base = {"scheduledFor": when, "timezone": "Europe/Vienna"}
        jobs = [("instagram", {**base, "content": caption(day, "Caption Instagram und Facebook"),
                 "mediaItems": [{"type": TYPE(p), "url": upload(p)} for p in feed],
                 "platforms": [{"platform": "instagram", "accountId": ig,   # Titelbild: "thumbnail" am Medium ignoriert Instagram, das Feld heißt instagramThumbnail
                                **({"platformSpecificData": {"instagramThumbnail": upload(COVER[feed[0].name])}} if feed[0].name in COVER else {})}]})]
        if lin is None:
            jobs.append(("linkedin", {**base, "content": caption(day, "LinkedIn"), "platforms": [{"platform": "linkedin", "accountId": li}]}))
        elif lin:
            jobs.append(("linkedin", {**base, "title": caption(day, "Hook").split("\n")[0] if False else "Angebote abtippen: 220 Stunden im Jahr",
                 "content": caption(day, "LinkedIn"), "mediaItems": [{"type": "document", "url": upload(p)} for p in lin],
                 "platforms": [{"platform": "linkedin", "accountId": li}]}))
        jobs.append(("story", {**base, "content": "", "mediaItems": [{"type": "video", "url": upload(story)}],
                 "platforms": [{"platform": "instagram", "accountId": ig, "platformSpecificData": {"contentType": "story"}}]}))
        for name, body in jobs:
            st, r = call("POST", "/posts", body)
            pid = r.get("post", {}).get("_id")
            print(f"  {name}: HTTP {st} {r.get('post', {}).get('status', r)}")
            if pid: ids.append({"day": day, "what": name, "id": pid, "when": when})
            old = json.loads(IDS.read_text()) if IDS.exists() and nur else []
            IDS.write_text(json.dumps([o for o in old if o["id"] not in {i["id"] for i in ids}] + ids if nur else ids, indent=1, ensure_ascii=False))


def status():
    for x in json.loads(IDS.read_text()):
        p = call("GET", f"/posts/{x['id']}")[1].get("post", {})
        pl = [(q.get("status"), q.get("errorMessage") or q.get("error"), q.get("platformPostUrl") or q.get("url")) for q in p.get("platforms", [])]
        print(x["day"], x["what"], x["when"][11:16], p.get("status"), pl)


def loeschen():
    for x in json.loads(IDS.read_text()):
        st, r = call("DELETE", f"/posts/{x['id']}")
        print(x["day"], x["what"], "HTTP", st, str(r)[:200])


cmd = sys.argv[1]
planen(sys.argv[2], sys.argv[3].split(",") if len(sys.argv) > 3 else None) if cmd == "planen" else status() if cmd == "status" else loeschen()
