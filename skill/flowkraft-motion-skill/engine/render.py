#!/usr/bin/env python3
"""flowkraft Motion: rendert eine Post-Datei zu Videos.

  render.py POST.js --out ORDNER [--format carousel|story|reel] [--theme navy|dark|mist]
                    [--slides 1 3] [--stills] [--audio-only]

  carousel = 1080x1350, ein Video pro Slide
  story    = 1080x1920, ein Video pro Slide
  reel     = 1080x1920, ein Video; der F-Ball deckt am Szenenende das Bild ab und bringt die nächste Szene
"""
import argparse, pathlib, shutil, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sfx
from playwright.sync_api import sync_playwright
import shutil as _sh


def launch(p, args):
    """Mac: Google Chrome. Linux/Cloud: Chrome oder mitgeliefertes Chromium, immer mit Software-WebGL (keine GPU)."""
    extra = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]
    if sys.platform != "darwin":
        args = args + extra
    try:
        return p.chromium.launch(channel="chrome", args=args)
    except Exception:
        return p.chromium.launch(args=args + extra)


def shot(page, tries=5, **kw):
    """Screenshot mit Wiederholung: Headless-Chromium ohne GPU meldet bei 2x-Supersampling
    gelegentlich 'Unable to capture screenshot'; ein zweiter Versuch klappt."""
    for k in range(tries):
        try:
            return page.screenshot(**kw)
        except Exception as e:
            if k == tries - 1 or "capture screenshot" not in str(e):
                raise
            print("  Screenshot-Retry", k + 1, file=sys.stderr); page.wait_for_timeout(250 * (k + 1))

ENGINE = pathlib.Path(__file__).resolve().parent / "engine.html"
SS = 2   # Render-Faktor; Ausgabe bleibt 1080 breit
ENC = ["-c:v", "libx264", "-preset", "slow", "-crf", "12", "-tune", "film", "-maxrate", "25M", "-bufsize", "50M", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.2"]


def shrink(src, dst, w):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", f"scale={w}:-1:flags=lanczos", str(dst)], check=True)


def open_page(browser, post, sid, theme, fmt):
    size = {"width": 1080, "height": 1350 if fmt == "carousel" else 1920}
    page = browser.new_page(viewport=size, device_scale_factor=SS)   # Supersampling: doppelt rendern, scharf verkleinern
    page.on("pageerror", lambda e: print("JS-FEHLER", sid, e))
    q = f"?post={post.as_uri()}&s={sid}&f={fmt}" + (f"&v={theme}" if theme else "")
    page.goto(ENGINE.as_uri() + q)
    page.evaluate("window.ready")
    return page


def mux(video, tl, dst):
    tmp = pathlib.Path(tempfile.mkdtemp()); wav = tmp / "a.wav"; out = tmp / "o.mp4"
    sfx.render(tl, wav)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    shutil.move(str(out), dst)


def video(page, dst):
    T, fps, tl = page.evaluate("[window.T, window.FPS, window.TL]")
    silent = pathlib.Path(tempfile.mkdtemp()) / "v.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-i", "-", "-vf", "scale=1080:-2:flags=lanczos", *ENC,
                           "-r", str(fps), str(silent)], stdin=subprocess.PIPE)
    for i in range(int(round(T * fps))):
        page.evaluate(f"window.seek({i / fps})")
        ff.stdin.write(shot(page, type="png"))
    ff.stdin.close(); ff.wait()
    mux(silent, tl, dst)
    print("ok", dst.name, f"{T}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post"); ap.add_argument("--out", default="videos")
    ap.add_argument("--format", default="carousel", choices=["carousel", "story", "reel"])
    ap.add_argument("--theme", choices=["navy", "dark", "mist"])
    ap.add_argument("--slides", nargs="*", type=int)
    ap.add_argument("--stills", action="store_true", help="nur Kontrollbilder")
    ap.add_argument("--hd", action="store_true", help="Standbilder in doppelter Auflösung (2160 breit) für LinkedIn und Facebook")
    ap.add_argument("--audio-only", action="store_true", help="Ton in fertige Videos neu einsetzen")
    a = ap.parse_args()
    post = pathlib.Path(a.post).resolve(); out = pathlib.Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = launch(p, ["--force-color-profile=srgb", "--font-render-hinting=none"])
        pg = open_page(b, post, 1, a.theme, a.format); info = pg.evaluate("({n: POST.slides.length, name: POST.name, scenes: POST.slides.map(s => s.scene || 'text')})"); pg.close()
        ids = a.slides or list(range(1, info["n"] + 1)); done = []
        for sid in ids:
            pg = open_page(b, post, sid, a.theme, a.format)
            name = f"{info['name']}-{sid}-{info['scenes'][sid-1]}" + ("" if a.format == "carousel" else "-9x16")
            if a.stills:
                T = pg.evaluate("window.T")
                for t in (1.2, 2.4, 3.6, T - .4):
                    pg.evaluate(f"window.seek({t})"); big = out / f"_{name}.png"; shot(pg, path=str(big)); shrink(big, out / f"{name}_{t:04.1f}.png", 2160 if a.hd else 1080); big.unlink()
                print("stills", name)
            elif a.audio_only:
                dst = out / f"{name}.mp4"; mux(dst, pg.evaluate("window.TL"), dst); print("audio ok", dst.name)
            else:
                dst = out / f"{name}.mp4"; video(pg, dst); done.append(dst)
            pg.close()
        b.close()
    if a.format == "reel" and done:
        lst = out / "_list.txt"; lst.write_text("".join(f"file '{d}'\n" for d in done))
        reel = out / f"{info['name']}-reel.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(reel)], check=True)
        lst.unlink(); [d.unlink() for d in done]; print("ok", reel.name)


if __name__ == "__main__":
    main()
