#!/usr/bin/env python3
"""Baut die Freigabeseite der Woche und lädt sie hoch. Link landet in out/KWnn/freigabe-link.txt.

  python3 tools/woche/freigabe.py content/KW48 [--lokal]

Jeder Post hat „Freigeben“ / „Nicht posten“. Ein Klick ruft den Make-Webhook MAKE_APPROVE_URL auf:
  ?id=<Zernio-ID>&zeit=<YYYY-MM-DDTHH:MM:SS>&aktion=ok|stop
Make setzt bei ok den Zernio-Entwurf auf eingeplant (PUT /v1/posts/{id} mit isDraft=false, scheduledFor, timezone).
"""
import html, json, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import CTX, week
import io, secrets, urllib.request, zipfile

w, plan, out = week(sys.argv[1]); lokal = "--lokal" in sys.argv
drafts = json.loads((out / "drafts.json").read_text())
hook = os.environ.get("MAKE_APPROVE_URL", "")
if not hook and not lokal: sys.exit("MAKE_APPROVE_URL fehlt.")
bericht = (w / "pruefbericht.md").read_text() if (w / "pruefbericht.md").exists() else ""
def netlify_deploy(f, kw):
    """Lädt die Seite zu Netlify (NETLIFY_TOKEN, NETLIFY_SITE_ID). Pfad mit Zufallsteil: nicht erratbar, nicht in Suchmaschinen."""
    tok, site = os.environ.get("NETLIFY_TOKEN"), os.environ.get("NETLIFY_SITE_ID")
    if not (tok and site): sys.exit("NETLIFY_TOKEN oder NETLIFY_SITE_ID fehlt.")
    slug = f"kw{kw}-{secrets.token_urlsafe(9)}"; buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{slug}/index.html", f.read_text()); z.writestr("robots.txt", "User-agent: *\nDisallow: /\n")
        z.writestr("index.html", "<!doctype html><meta name=robots content=noindex><title>flowkraft</title>")
        z.writestr("_headers", "/*\n  X-Robots-Tag: noindex\n  Referrer-Policy: no-referrer\n")
    req = urllib.request.Request(f"https://api.netlify.com/api/v1/sites/{site}/deploys", data=buf.getvalue(), method="POST",
                                 headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/zip"})
    with urllib.request.urlopen(req, timeout=120, context=CTX) as r: d = json.loads(r.read())
    base = d.get("ssl_url") or d.get("url"); return f"{base.rstrip('/')}/{slug}/"


KAN = {"instagram": "Instagram", "facebook": "Facebook", "linkedin": "LinkedIn"}


def media(urls):
    h = []
    for u in urls[:8]:
        h.append(f'<video src="{u}" controls muted playsinline preload="metadata"></video>' if u.endswith(".mp4") else f'<img src="{u}" alt="" loading="lazy">')
    return "".join(h)


cards = []
for d in drafts:
    z = d["zeit"].replace("T", " ")[:16]
    cards.append(f'''<article class="card" data-id="{d['id']}" data-zeit="{d['zeit']}">
<header><b>{d['tag']} · {KAN.get(d['kanal'], d['kanal'])}</b><span>{z}</span></header>
<p class="typ">{html.escape(d.get('typ', ''))}</p>
<div class="media">{media(d['medien'])}</div>
<details><summary>Text</summary><pre>{html.escape(d['text'])}</pre></details>
{'<p class="st">Kein Knopf: Story mit Sticker postest du selbst in der App.</p>' if d.get('manuell') else '<div class="btns"><button class="ok">Freigeben</button><button class="stop">Nicht posten</button><span class="st"></span></div>'}</article>''')

page = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Freigabe KW {plan['kw']}</title><style>
:root{{--bg:#f4f7fa;--card:#fff;--ink:#14324f;--sub:#4f6478;--acc:#2878b5;--line:#dce4ec}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0b1622;--card:#122334;--ink:#e7eef5;--sub:#9db0c2;--acc:#4a9bd8;--line:#21374c}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,system-ui,sans-serif}}
.wrap{{max-width:1100px;margin:0 auto;padding:24px 16px 80px}} h1{{margin:0 0 6px}} .lead{{color:var(--sub);margin:0 0 18px}}
.all{{position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:2;display:flex;gap:10px;align-items:center}}
.grid{{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px}}
.card header{{display:flex;justify-content:space-between;margin-bottom:10px}} .card header span{{color:var(--sub)}} .typ{{display:inline-block;margin:0 0 10px;padding:3px 10px;border-radius:999px;background:var(--acc);color:#fff;font-size:13px;font-weight:600}}
.media{{display:flex;gap:6px;overflow-x:auto}} .media video,.media img{{height:260px;border-radius:8px;background:#000}}
pre{{white-space:pre-wrap;font:14px/1.4 inherit;color:var(--sub)}}
button{{font:inherit;padding:9px 14px;border-radius:9px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}}
button.ok{{background:var(--acc);color:#fff;border-color:var(--acc)}} .btns{{display:flex;gap:8px;align-items:center;margin-top:10px}}
.card.done-ok{{outline:3px solid #2e9e6a}} .card.done-stop{{opacity:.5}} .st{{color:var(--sub);font-size:14px}}
details.rep{{margin:24px 0}} details.rep pre{{color:var(--ink)}}
</style></head><body><div class="wrap">
<h1>Freigabe KW {plan['kw']}</h1>
<p class="lead">Nur was du freigibst, wird eingeplant. Ohne Klick geht nichts raus. Storys mit Sticker postest du selbst in der App.</p>
<div class="all"><button class="ok" id="allok">Alle freigeben</button><span class="st" id="allst"></span></div>
<div class="grid">{"".join(cards)}</div>
<details class="rep"><summary>Prüfbericht</summary><pre>{html.escape(bericht)}</pre></details>
</div><script>
const HOOK = {json.dumps(hook)};
function send(card, aktion) {{
  const st = card.querySelector('.st'); st.textContent = 'sendet …';
  const u = HOOK + (HOOK.includes('?') ? '&' : '?') + new URLSearchParams({{id: card.dataset.id, zeit: card.dataset.zeit, aktion}});
  return fetch(u, {{mode: 'no-cors'}}).then(() => {{ card.classList.add('done-' + aktion); st.textContent = aktion === 'ok' ? 'freigegeben ✓' : 'wird nicht gepostet';
    try {{ localStorage.setItem('fk-' + card.dataset.id, aktion); }} catch (e) {{}} }}).catch(() => st.textContent = 'Fehler, bitte nochmal');
}}
document.querySelectorAll('.card').forEach(c => {{ if (!c.querySelector('.ok')) return;
  c.querySelector('.ok').onclick = () => send(c, 'ok'); c.querySelector('.stop').onclick = () => send(c, 'stop');
  try {{ const v = localStorage.getItem('fk-' + c.dataset.id); if (v) {{ c.classList.add('done-' + v); c.querySelector('.st').textContent = v === 'ok' ? 'freigegeben ✓' : 'wird nicht gepostet'; }} }} catch (e) {{}}
}});
document.getElementById('allok').onclick = async () => {{ for (const c of [...document.querySelectorAll('.card:not(.done-ok):not(.done-stop)')].filter(c => c.querySelector('.ok'))) await send(c, 'ok'); document.getElementById('allst').textContent = 'alles freigegeben ✓'; }};
</script></body></html>'''

f = out / "freigabe.html"; f.write_text(page)
if lokal: print("lokal:", f); sys.exit()
link = netlify_deploy(f, plan["kw"]); (out / "freigabe-link.txt").write_text(link + "\n"); (w / "freigabe-link.txt").write_text(link + "\n"); print("Freigabeseite:", link)
