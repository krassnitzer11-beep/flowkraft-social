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


def hook(w, day):
    """Bessere Hook-Variante aus texte.md (Zeile mit „(besser)“, sonst die erste Variante)."""
    t = (w / "texte.md").read_text(); i = t.find(f"## {day}")
    if i < 0: return ""
    sec = t[i:]; sec = sec[:sec.index("\n---")] if "\n---" in sec else sec
    m = re.search(r"\*\*(?:Hook|Text im Bild)[^\n]*\n(.*?)(?=\n\n|\n\*\*|\Z)", sec, re.S)
    if not m: return ""
    lines = [l.strip("- ").strip() for l in m.group(1).splitlines() if l.strip()]
    best = next((l for l in lines if "besser" in l), lines[0] if lines else "")
    return re.sub(r"^[A-Z]\s*(\([^)]*\))?\s*:\s*", "", best).strip()


FARBE = {"gruen": ("#2e9e6a", "bereit"), "gelb": ("#d9a21b", "Hinweis"), "rot": ("#d0453a", "blockiert")}
FORMAT = {"reel": "Reel", "karussell": "Karussell", "post": "Standbild"}


def ampel(w, plan):
    """Kurze Übersicht pro Post: Tag, Format, Hook, Ampel, Grund. Quelle: content/KWnn/ampel.json vom Prüfer.
    Fehlt die Datei, gibt es die Liste ohne Ampel."""
    f = w / "ampel.json"; a = {x["tag"]: x for x in json.loads(f.read_text())} if f.exists() else {}
    rows = []
    for p in plan["posts"]:
        x = a.get(p["tag"], {})
        rows.append({"tag": p["tag"], "format": FORMAT.get(p["format"], p["format"]), "thema": x.get("thema", ""),
                     "hook": x.get("hook") or hook(w, p["texte"]), "ampel": x.get("ampel", ""), "grund": x.get("grund", ""),
                     "linkedin": bool(p.get("linkedin"))})
    return rows


def ampel_html(rows):
    """Tabelle für Mail und Freigabeseite: eine Zeile pro Tag, farbiger Punkt, ein kurzer Grund."""
    import html as H
    n = {k: sum(r["ampel"] == k for r in rows) for k in FARBE}
    kopf = " · ".join(f'<span style="color:{FARBE[k][0]};font-weight:700">{n[k]} {FARBE[k][1]}</span>' for k in FARBE if n[k]) if any(n.values()) else ""
    tr = []
    for r in rows:
        c, lab = FARBE.get(r["ampel"], ("#9aa7b4", "–"))
        dot = f'<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:{c}"></span>'
        sub = H.escape(r["grund"]) if r["grund"] else ""
        tr.append(f'<tr><td style="padding:8px 10px;vertical-align:top">{dot}</td>'
                  f'<td style="padding:8px 10px;vertical-align:top;white-space:nowrap"><b>{r["tag"]}</b><br><span style="color:#6b7c8c">{r["format"]}{" + LinkedIn" if r["linkedin"] else ""}</span></td>'
                  f'<td style="padding:8px 10px;vertical-align:top"><b>{H.escape(r["hook"] or r["thema"])}</b>'
                  f'{"<br><span style=color:#6b7c8c>" + sub + "</span>" if sub else ""}</td></tr>')
    return (f'<p style="margin:0 0 8px">{kopf}</p>' if kopf else "") + \
        '<table style="border-collapse:collapse;font:15px/1.4 -apple-system,Segoe UI,sans-serif">' + "".join(tr) + "</table>"
