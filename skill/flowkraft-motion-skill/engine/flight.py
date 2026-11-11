#!/usr/bin/env python3
"""flowkraft Drohnenflug: ein Reel als durchgehende Kamerafahrt in echtem 3D (flight3d.html).

  flight.py POST.js --out ORDNER [--theme navy|dark|mist] [--stills 0.5 2 4.2 ...] [--keep]

Ablauf: 1) Die Engine rendert jede Szene als Bildfolge mit F-Ball, ohne Hintergrund und Headline (transparent).
        2) flight3d.html stellt die Szenen als Flächen in eine 3D-Welt, setzt die Headline als 3D-Schrift an
           dieselben Stellen und fliegt ohne Schnitt durch alle Stationen.
        3) Ton: die Szenen-Töne der Engine an ihren Zeitpunkten + Flug-Whooshes.
"""
import argparse, json, math, pathlib, shutil, subprocess, sys, tempfile, wave
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sfx
from playwright.sync_api import sync_playwright
import shutil as _sh


def launch(p, args):
    """Mac: Google Chrome. Cloud/Linux ohne Chrome: mitgeliefertes Chromium mit Software-WebGL."""
    extra = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]
    try:
        return p.chromium.launch(channel="chrome", args=args)
    except Exception:
        return p.chromium.launch(args=args + extra)

HERE = pathlib.Path(__file__).resolve().parent
ARGS = ["--force-color-profile=srgb", "--font-render-hinting=none", "--allow-file-access-from-files", "--ignore-gpu-blocklist"]


def read_wav(p):
    with wave.open(str(p)) as w:
        a = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(float) / 32767
        return a.reshape(-1, w.getnchannels())


def scene_layers(b, post, n, tmp, theme, dsf):
    """Pro Station: transparente Bildfolge der Szene + Layout + Szenen-Ton."""
    lays = []
    for sid in range(1, n + 1):
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=dsf)
        pg.on("pageerror", lambda e: print("JS-FEHLER Szene", sid, e))
        lay = None
        for part in ("h", "t"):   # zwei getrennte Ebenen: Szene und Schrift, jeweils ganz (nichts angeschnitten)
            pg.goto((HERE / "engine.html").as_uri() + f"?post={post.as_uri()}&s={sid}&f=story&layer=hero&part={part}" + (f"&v={theme}" if theme else ""))
            pg.evaluate("window.ready")
            if lay is None: lay = pg.evaluate("window.LAYOUT"); sfx.render(pg.evaluate("window.TL"), tmp / f"s{sid}.wav")
            frames = int(math.ceil((lay["H0"] + .4) * 30))
            for k in range(frames):
                pg.evaluate(f"window.seek({k / 30})")
                pg.screenshot(path=str(tmp / f"s{sid}{part}_{k:04d}.png"), omit_background=True)
        lay["frames"] = frames
        lays.append(lay); pg.close()
        print("Szene", sid, f"{frames} Bilder")
    (tmp / "layout.json").write_text(json.dumps(lays))


def sound(tl, tmp, path):
    SR = sfx.SR; T = tl["T"]; n = int(T * SR)
    M = np.zeros((n + SR, 2))
    def place(a, k):
        if k < 0: a = a[-k:]; k = 0
        a = a[:len(M) - k]; M[k:k + len(a)] += a
    for i, runs in enumerate(tl.get("split", [])):              # Modus split: Szenen-Ton passend zur angehaltenen Szenen-Zeit
        w = read_wav(tmp / f"s{i + 1}.wav")
        for k, r in enumerate(runs):
            t0 = 0 if k == 0 else r["a"]; t1 = runs[k + 1]["a"] if k + 1 < len(runs) else r["b"] + 1.2
            seg = w[int(t0 * SR):int(t1 * SR)].copy(); f = min(len(seg), int(.08 * SR))
            if f: seg[-f:] *= np.linspace(1, 0, f)[:, None]
            place(seg, int((r["rs"] - (r["a"] - t0)) * SR))
    for i, st in enumerate(tl.get("stations", [])):              # Szenen-Töne der Engine
        a = read_wav(tmp / f"s{i + 1}.wav")[:int(st["dur"] * SR)].copy()
        f = min(len(a), int(.3 * SR)); a[-f:] *= np.linspace(1, 0, f)[:, None]
        k = int(st["t0"] * SR)
        if k < 0: a = a[-k:]; k = 0
        a = a[:len(M) - k]; M[k:k + len(a)] += a
    for e in tl["events"]:                                        # Flug
        if e["k"] == "whoosh":
            sig = sfx.whoosh(e["d"], .08, 160, 3400); k = int(e["t"] * SR); sig = sig[:len(M) - k]
            M[k:k + len(sig)] += sig[:, None] * .9
    st = M[:n]; pk = np.abs(st).max()
    if pk > .89: st *= .89 / pk
    st[-int(.4 * SR):] *= np.linspace(1, 0, int(.4 * SR))[:, None]
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post"); ap.add_argument("--out", default="videos"); ap.add_argument("--theme", choices=["navy", "dark", "mist"])
    ap.add_argument("--stills", nargs="*", type=float); ap.add_argument("--pr", type=float, default=2)
    ap.add_argument("--mode", choices=["split", "pass", "front"], default="split", help="pass: Szenen seitlich, Vorbeiflug; front: frontal mit Halten")
    ap.add_argument("--keep", help="Szenen-Bildfolgen aus diesem Ordner wiederverwenden bzw. dort ablegen")
    a = ap.parse_args()
    post = pathlib.Path(a.post).resolve(); out = pathlib.Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(a.keep).resolve() if a.keep else pathlib.Path(tempfile.mkdtemp())
    tmp.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = launch(p, ARGS)
        if not (tmp / "layout.json").exists():
            pg = b.new_page(); pg.goto((HERE / "engine.html").as_uri() + f"?post={post.as_uri()}&s=1&f=story"); pg.evaluate("window.ready")
            n = pg.evaluate("POST.slides.length"); pg.close()
            scene_layers(b, post, n, tmp, a.theme, a.pr)
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)   # Supersampling, danach scharf auf 1080 verkleinern
        pg.on("pageerror", lambda e: print("JS-FEHLER", e)); pg.on("console", lambda m: m.type == "error" and print("KONSOLE", m.text))
        pg.goto((HERE / "flight3d.html").as_uri() + f"?post={post.as_uri()}&pr={a.pr}&mode={a.mode}&frames={tmp.as_uri()}" + (f"&v={a.theme}" if a.theme else ""))
        pg.wait_for_function("window.ready !== undefined", timeout=60000); pg.evaluate("window.ready")
        T, fps, tl, name = pg.evaluate("[window.T, window.FPS, window.TL, POST.name]")
        if a.stills is not None:
            for t in (a.stills or [T * k / 8 for k in range(9)]):
                pg.evaluate(f"window.seek({t})"); pg.screenshot(path=str(out / f"{name}-flug_{t:05.2f}.png"))
            print("stills", name, f"T={T}", json.dumps(pg.evaluate("window._dbg")))
        else:
            silent = tmp / "v.mp4"; wav = tmp / "a.wav"; mux = tmp / "o.mp4"; dst = out / f"{name}-flug.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-i", "-", "-vf", "scale=1080:-2:flags=lanczos", "-c:v", "libx264", "-preset", "slow",
                                   "-crf", "12", "-tune", "film", "-maxrate", "25M", "-bufsize", "50M", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.2", "-r", str(fps), str(silent)], stdin=subprocess.PIPE)
            for i in range(int(round(T * fps))):
                pg.evaluate(f"window.seek({i / fps})"); ff.stdin.write(pg.screenshot(type="png"))
            ff.stdin.close(); ff.wait()
            sound(tl, tmp, wav)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent), "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac",
                            "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(mux)], check=True)
            shutil.move(str(mux), dst); print("ok", dst.name, f"{T}s")
        b.close()
    if not a.keep: shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
