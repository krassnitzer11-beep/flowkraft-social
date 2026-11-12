#!/usr/bin/env python3
"""Lädt die gerenderte Woche zu Zernio hoch und legt jeden Post als ENTWURF an (nichts wird eingeplant).

  python3 tools/woche/drafts.py content/KW48

Schreibt out/KWnn/drafts.json: pro Eintrag Tag, Kanal, geplante Zeit, Zernio-ID, Medien-URLs, Text.
Eingeplant wird erst über die Freigabeseite (Make-Webhook setzt isDraft=false + scheduledFor).
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import accounts, call, text, upload, week

w, plan, out = week(sys.argv[1])
man = json.loads((out / "manifest.json").read_text()); acc = accounts(); res = []
URL = {}
def up(p):
    if p not in URL: URL[p] = upload(p); print("  hochgeladen", Path(p).name)
    return URL[p]
TYPE = lambda p: "video" if p.endswith(".mp4") else "image"


def draft(tag, kanal, when, content, media, extra=None, typ=''):
    if kanal not in acc: print(f"  {kanal} nicht verbunden, übersprungen"); return
    plat = {"platform": kanal, "accountId": acc[kanal], **(extra or {})}
    body = {"isDraft": True, "content": content, "mediaItems": media, "platforms": [plat]}
    st, r = call("POST", "/posts", body); pid = r.get("post", {}).get("_id")
    print(f"{tag} {kanal}: HTTP {st} {'Entwurf' if pid else r}")
    if pid: res.append({"tag": tag, "kanal": kanal, "typ": typ, "zeit": when, "id": pid, "text": content, "medien": [x["url"] for x in media]})


for p in plan["posts"]:
    m = man[p["tag"]]; when = f"{p['datum']}T{p['zeit']}:00"; cap = text(w, p["texte"], "Caption Instagram und Facebook")
    ig = [{"type": TYPE(x), "url": up(x)} for x in m["instagram"]]
    fb = [{"type": TYPE(x), "url": up(x)} for x in m["facebook"]]
    ig_extra = {}
    if m.get("cover"):
        cu = up(m["cover"]); ig_extra = {"platformSpecificData": {"instagramThumbnail": cu}}; fb[0]["thumbnail"] = cu
    T_IG = {"reel": "Reel", "karussell": "Karussell", "post": "Standbild-Post"}[p["format"]]
    T_FB = {"reel": "Reel", "karussell": "Bildergalerie", "post": "Standbild-Post"}[p["format"]]
    draft(p["tag"], "instagram", when, cap, ig, ig_extra, T_IG)
    draft(p["tag"], "facebook", when, cap, fb, None, T_FB)
    li = p.get("linkedin")
    if li:
        q = man[li["quelle"]]; src = q["linkedin_video"] if li["typ"] == "video" else q["linkedin_bild"]
        item = {"type": TYPE(src), "url": up(src)}
        if li["typ"] == "video" and q.get("cover"): item["thumbnail"] = up(q["cover"])
        draft(p["tag"], "linkedin", f"{li['datum']}T{li['zeit']}:00", text(w, li["texte"], "LinkedIn"), [item], None, "Video" if li["typ"] == "video" else "Standbild")

# Storys: werden automatisch gepostet, ohne Sticker (Instagram und Facebook), gleiche Freigabe wie die Posts
for p in plan["posts"]:
    k = p.get("story")
    if k and man.get("storys") and k <= len(man["storys"]):
        sv = {"type": "video", "url": up(man["storys"][k - 1])}; when = f"{p['datum']}T{p['zeit']}:00"
        draft(p["tag"], "instagram", when, "", [sv], {"platformSpecificData": {"contentType": "story"}}, "Story")
        draft(p["tag"], "facebook", when, "", [sv], {"platformSpecificData": {"contentType": "story"}}, "Story")
(out / "drafts.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))
(w / "drafts.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))
print(len(res), "Entwürfe angelegt ->", out / "drafts.json")
