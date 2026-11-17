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


def md_html(md):
    """Prüfbericht lesbar machen: Überschriften, Listen, Tabellen, fett; ohne Code-Zeichen wie `…`."""
    import html as H
    def inline(t):
        t = H.escape(t.replace("`", ""))
        return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    out, rows, lst = [], [], False
    def flush():
        nonlocal rows
        if rows:
            body = [r for r in rows if not re.fullmatch(r"\|?\s*:?-{2,}.*", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in body]
            head, rest = cells[0], cells[1:]
            out.append('<div class="tw"><table><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>" +
                       "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest) + "</table></div>")
            rows = []
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("|"): rows.append(s); continue
        flush()
        if lst and not re.match(r"^([-*]|\d+\.)\s", s): out.append("</ul>"); lst = False
        if not s: continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m: out.append(f"<h{len(m.group(1)) + 2}>{inline(m.group(2))}</h{len(m.group(1)) + 2}>"); continue
        m = re.match(r"^([-*]|\d+\.)\s+(.*)", s)
        if m:
            if not lst: out.append("<ul>"); lst = True
            out.append(f"<li>{inline(m.group(2))}</li>"); continue
        out.append(f"<p>{inline(s)}</p>")
    flush()
    if lst: out.append("</ul>")
    return "".join(out)


def probleme_html(w, plan):
    """„Was nicht passt“: alle gelben und roten Posts mit Grund und den Punkten des Prüfers (ampel.json: punkte)."""
    import html as H
    f = w / "ampel.json"
    if not f.exists(): return ""
    a = {x["tag"]: x for x in json.loads(f.read_text())}; items = []
    for p in plan["posts"]:
        x = a.get(p["tag"])
        if not x or x.get("ampel") not in ("gelb", "rot"): continue
        c, lab = FARBE[x["ampel"]]
        pk = "".join(f"<li>{H.escape(str(q.get('was', q) if isinstance(q, dict) else q).replace('`', ''))}"
                     f"{'<br><span class=sub>Vorschlag: ' + H.escape(q['vorschlag'].replace('`', '')) + '</span>' if isinstance(q, dict) and q.get('vorschlag') else ''}</li>"
                     for q in x.get("punkte", []))
        items.append(f'<div class="prob" style="border-left:4px solid {c}"><b>{p["tag"]} · {FORMAT.get(p["format"], p["format"])}</b> '
                     f'<span style="color:{c};font-weight:700">{lab}</span><p>{H.escape(x.get("grund", ""))}</p>{"<ul>" + pk + "</ul>" if pk else ""}</div>')
    return "".join(items) or '<p>Alles grün, nichts offen.</p>'


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


KANAL = {"instagram": "Instagram", "facebook": "Facebook", "linkedin": "LinkedIn"}


def letzte_zahlen(w):
    """Neueste Wochen-Kennzahlen (content/analysen/KWnn-zahlen.json), sonst None."""
    d = REPO / "content" / "analysen"
    # nach Enddatum sortieren (Datei-Zeiten sind nach git checkout alle gleich, KW-Nummern springen zum Jahreswechsel)
    zs = [json.loads(f.read_text()) for f in d.glob("KW*-zahlen.json")] if d.exists() else []
    return max(zs, key=lambda z: z.get("bis", "")) if zs else None


def zahlen_html(z, voll=False):
    """„Letzte Woche“: Kennzahlen-Kacheln, bester/schwächster Post, Lernpunkt; voll=True zusätzlich Tabelle pro Post."""
    import html as H
    if not z: return '<p style="color:#6b7c8c">Noch keine Auswertung vorhanden.</p>'
    f = lambda n: f"{n:,}".replace(",", ".") if isinstance(n, int) else ("–" if n is None else str(n))
    kach = [("Reichweite", f(z["summe"]["reichweite"] or z["summe"]["impressionen"]), ""), ("Interaktionen", f(z["summe"]["interaktionen"]), ""),
            ("Speichern + Teilen", f(z["summe"]["speichern_teilen"]), ""), ("Posts mit Zahlen", f(z["posts"]), "")]
    for a in z.get("follower", []):
        zw = a.get("zuwachs") or 0
        kach.append((f"Follower {KANAL.get(a['kanal'], a['kanal'])}", f(a.get("aktuell")), f"{'+' if zw >= 0 else ''}{zw} diese Woche"))
    box = "".join(f'<div style="display:inline-block;vertical-align:top;min-width:110px;margin:0 14px 10px 0"><div style="font-size:22px;font-weight:700">{v}</div>'
                  f'<div style="color:#6b7c8c;font-size:13px">{k}{"<br>" + e if e else ""}</div></div>' for k, v, e in kach)
    dat = lambda d: f"{d[8:10]}.{d[5:7]}.{d[:4]}" if d and len(d) >= 10 else d
    out = [f'<p style="margin:0 0 6px;color:#6b7c8c">{dat(z["von"])} bis {dat(z["bis"])}</p><div>{box}</div>']
    if z.get("zu_wenig_daten"):
        out.append('<p style="color:#6b7c8c">Noch zu wenig Daten für einen Vergleich. Die Zahlen werden ab mehreren echten Posts aussagekräftig.</p>')
    else:
        for lab, c, p in (("Am besten", "#2e9e6a", z.get("top")), ("Am schwächsten", "#d0453a", z.get("flop"))):
            if p: out.append(f'<p style="margin:6px 0"><span style="color:{c};font-weight:700">{lab}:</span> {H.escape(p["text"])} '
                             f'<span style="color:#6b7c8c">({KANAL.get(p["kanal"], p["kanal"])}, {f(p["reichweite"] or p["impressionen"])} erreicht, {p["interaktionen"]} Interaktionen)</span></p>')
    if z.get("lernpunkt"): out.append(f'<p style="margin:8px 0"><b>Was wir ändern:</b> {H.escape(z["lernpunkt"])}</p>')
    if voll and z.get("zeilen"):
        mx = max((r["interaktionen"] for r in z["zeilen"]), default=0)
        tr = "".join(f'<tr><td>{r["datum"][8:10]}.{r["datum"][5:7]}.</td><td>{KANAL.get(r["kanal"], r["kanal"])}</td><td>{H.escape(r["text"])}</td>'
                     f'<td style="text-align:right">{f(r["reichweite"] or r["impressionen"])}</td><td style="text-align:right">{f(r["aufrufe"])}</td>'
                     f'<td style="text-align:right;{"color:#2e9e6a;font-weight:700" if mx and r["interaktionen"] == mx else ""}">{r["interaktionen"]}</td>'
                     f'<td style="text-align:right">{"–" if r["rate"] is None else str(r["rate"]).replace(".", ",") + " %"}</td></tr>' for r in z["zeilen"])
        out.append('<div class="tw"><table class="zt"><tr><th>Tag</th><th>Kanal</th><th>Post</th><th>Reichweite</th><th>Aufrufe</th><th>Interaktionen</th><th>Rate</th></tr>' + tr + '</table></div>')
    if voll and z.get("ohne_zahlen"):
        out.append(f'<p style="color:#6b7c8c;font-size:14px">{len(z["ohne_zahlen"])} Posts ohne Zahlen (z. B. Kanal nicht verbunden oder noch nicht synchronisiert).</p>')
    return "".join(out)
