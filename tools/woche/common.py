"""Gemeinsame Helfer für den Wochenablauf: Pfade, Zernio-API, Texte aus texte.md."""
import json, mimetypes, os, re, ssl, sys, urllib.error, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skill" / "flowkraft-motion-skill" / "engine"
PY = os.environ.get("FK_PY") or str(Path.home() / ".flowkraft-motion" / "venv" / "bin" / "python")
API = "https://zernio.com/api/v1"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if Path("/etc/ssl/cert.pem").exists() else None)


def week(path):
    w = Path(path).resolve(); plan = json.loads((w / "plan.json").read_text())
    out = REPO / "out" / w.name; out.mkdir(parents=True, exist_ok=True)
    return w, plan, out


def key():
    k = os.environ.get("ZERNIO_API_KEY")
    if not k:
        env = Path.home() / ".flowkraft-motion" / "zernio.env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("ZERNIO_API_KEY="): k = line.split("=", 1)[1].strip().strip('"')
    if not k: sys.exit("ZERNIO_API_KEY fehlt (Umgebungsvariable).")
    return k


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r: return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read() or b"{}")


def upload(path, ctype=None):
    path = Path(path); ctype = ctype or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    st, pre = call("POST", "/media/presign", {"filename": path.name, "contentType": ctype, "size": path.stat().st_size})
    if st != 200: sys.exit(f"Upload-Anfrage fehlgeschlagen ({st}): {pre}")
    put = urllib.request.Request(pre["uploadUrl"], method="PUT", data=path.read_bytes(), headers={"Content-Type": ctype})
    with urllib.request.urlopen(put, timeout=600, context=CTX) as r:
        if r.status != 200: sys.exit(f"Upload fehlgeschlagen: {path.name}")
    return pre["publicUrl"]


def text(w, day, block):
    t = (w / "texte.md").read_text(); i = t.find(f"## {day}")
    if i < 0: sys.exit(f"Abschnitt '## {day}' fehlt in texte.md")
    sec = t[i:]; sec = sec[:sec.index("\n---")] if "\n---" in sec else sec
    m = re.search(rf"\*\*{re.escape(block)}[^\n]*\n\n(.*?)(?=\n\*\*|\Z)", sec, re.S)
    return m.group(1).strip() if m else ""


def accounts():
    accs = call("GET", "/accounts")[1].get("accounts", [])
    return {a.get("platform"): a["_id"] for a in accs}
