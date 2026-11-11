#!/usr/bin/env python3
"""Zernio-Test für flowkraft KW 47.

Schlüssel: ~/.flowkraft-motion/zernio.env mit einer Zeile ZERNIO_API_KEY=sk_...
(der Schlüssel steht nie im Projektordner).

  python3 zernio_test.py konten                      verbundene Konten zeigen
  python3 zernio_test.py di --modus entwurf          als Entwurf in Zernio ablegen (geht nicht raus)
  python3 zernio_test.py di --modus planen --zeit 2026-11-17T18:00:00   wirklich einplanen
  python3 zernio_test.py status POST_ID              Status eines Posts

Dienstag = Instagram-Karussell aus 7 Video-Slides + LinkedIn-PDF, Caption aus texte.md.
"""
import argparse, json, mimetypes, os, re, ssl, sys, urllib.request, urllib.error
from pathlib import Path

API = "https://zernio.com/api/v1"
ROOT = Path(os.environ.get("FK_WEEK") or Path(__file__).resolve().parent.parent / "probewoche-kw47")   # Wochenordner; im Repo per FK_WEEK setzen
ENV = Path.home() / ".flowkraft-motion" / "zernio.env"   # Schlüssel nie im Repository; in der Cloud als Umgebungsvariable ZERNIO_API_KEY
# Homebrew-Python findet die Zertifikate von macOS nicht von selbst
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if Path("/etc/ssl/cert.pem").exists() else None)


def key():
    k = os.environ.get("ZERNIO_API_KEY")
    if not k and ENV.exists():
        for line in ENV.read_text().splitlines():
            if line.startswith("ZERNIO_API_KEY="):
                k = line.split("=", 1)[1].strip().strip('"')
    if not k:
        sys.exit(f"Kein Schlüssel. Lege {ENV} an (siehe Anleitung).")
    return k


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def upload(path):
    ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    st, pre = call("POST", "/media/presign", {"filename": path.name, "contentType": ctype, "size": path.stat().st_size})
    if st != 200:
        sys.exit(f"Upload-Anfrage fehlgeschlagen ({st}): {pre}")
    put = urllib.request.Request(pre["uploadUrl"], method="PUT", data=path.read_bytes(), headers={"Content-Type": ctype})
    with urllib.request.urlopen(put, timeout=600, context=CTX) as r:
        if r.status != 200:
            sys.exit(f"Upload fehlgeschlagen: {path.name} ({r.status})")
    print("  hochgeladen", path.name)
    return pre["publicUrl"]


def caption(day, block):
    t = (ROOT / "texte.md").read_text()
    sec = t[t.index(f"## {day}"):]
    sec = sec[:sec.index("\n---")] if "\n---" in sec else sec
    m = re.search(rf"\*\*{re.escape(block)}[^\n]*\n\n(.*?)(?=\n\*\*|\Z)", sec, re.S)
    return m.group(1).strip()


def account(accounts, platform):
    for a in accounts:
        if a.get("platform") == platform:
            return a["_id"]
    sys.exit(f"Kein {platform}-Konto verbunden.")


def post_di(modus, zeit):
    st, acc = call("GET", "/accounts")
    accs = acc.get("accounts", [])
    ig, li = account(accs, "instagram"), account(accs, "linkedin")
    vids = sorted((ROOT / "videos/2-di").glob("kw47-di-angebote-*.mp4"))
    assert len(vids) == 7, vids
    print("Lade 7 Video-Slides und das PDF hoch ...")
    media = [{"type": "video", "url": upload(v)} for v in vids]
    pdf = {"type": "document", "url": upload(ROOT / "linkedin/kw47-di-angebote-linkedin.pdf")}
    base = {"timezone": "Europe/Vienna"}
    if modus == "entwurf": base["isDraft"] = True   # isDraft gewinnt immer: wird gespeichert, nie veröffentlicht
    else: base["scheduledFor"] = zeit
    posts = [
        {**base, "content": caption("Di 17.11.", "Caption Instagram und Facebook"), "mediaItems": media,
         "platforms": [{"platform": "instagram", "accountId": ig}]},
        {**base, "title": "Angebote abtippen: 220 Stunden im Jahr", "content": caption("Di 17.11.", "LinkedIn"),
         "mediaItems": [pdf], "platforms": [{"platform": "linkedin", "accountId": li}]},
    ]
    for p in posts:
        st, r = call("POST", "/posts", p)
        name = p["platforms"][0]["platform"]
        print(f"{name}: HTTP {st}", json.dumps(r, ensure_ascii=False)[:600])


ap = argparse.ArgumentParser()
ap.add_argument("was", choices=["konten", "di", "status"])
ap.add_argument("id", nargs="?")
ap.add_argument("--modus", choices=["entwurf", "planen"], default="entwurf")
ap.add_argument("--zeit", help="Ortszeit Wien, z. B. 2026-11-17T18:00:00")
a = ap.parse_args()
if a.was == "konten":
    st, r = call("GET", "/accounts")
    for x in r.get("accounts", []):
        print(x.get("platform"), x.get("username") or x.get("name"), x.get("_id"))
    if st != 200: print(st, r)
elif a.was == "status":
    print(json.dumps(call("GET", f"/posts/{a.id}")[1], ensure_ascii=False, indent=1)[:3000])
else:
    if a.modus == "planen" and not a.zeit:
        sys.exit("--zeit fehlt")
    post_di(a.modus, a.zeit)
