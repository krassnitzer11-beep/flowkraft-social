#!/usr/bin/env python3
"""Rendert eine ganze Woche nach plan.json und schreibt out/KWnn/manifest.json.

  python3 tools/woche/build.py content/KW48 [--nur Mo Di]

Reel      -> Drohnenflug 9:16 (Instagram, Facebook) + Titelbild; für LinkedIn zusätzlich 4:5 aus den Karussell-Slides
Karussell -> Video-Slides (Instagram) + Endbilder als Galerie (Facebook)
Post      -> Standbild (Instagram, Facebook 1080) + HD-Standbild 2160 (LinkedIn)
Storys    -> je ein Video pro Slide
"""
import argparse, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import PY, SKILL, week

ap = argparse.ArgumentParser(); ap.add_argument("woche"); ap.add_argument("--nur", nargs="*")
a = ap.parse_args()
w, plan, out = week(a.woche)
man = json.loads((out / "manifest.json").read_text()) if (out / "manifest.json").exists() else {}


def run(*args):
    print("»", " ".join(map(str, args[1:3])), flush=True); subprocess.run([PY, *map(str, args)], check=True)


def last(folder, prefix):
    s = sorted(Path(folder).glob(f"{prefix}*.png")); return s[-1] if s else None


for p in plan["posts"]:
    if a.nur and p["tag"] not in a.nur: continue
    src = w / p["post"]; d = out / p["tag"]; d.mkdir(exist_ok=True); m = {"format": p["format"]}
    if p["format"] == "reel":
        run(SKILL / "flight.py", src, "--out", d, "--keep", d / "_ebenen")
        v = next(d.glob("*-flug.mp4")); cover = d / "cover.jpg"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.1", "-i", str(v), "-frames:v", "1", "-q:v", "2", str(cover)], check=True)
        # LinkedIn-Fassung 4:5: Slides als Karussell-Videos, aneinandergehängt
        li = d / "linkedin"; li.mkdir(exist_ok=True)
        run(SKILL / "render.py", src, "--out", li, "--format", "carousel")
        parts = sorted(x for x in li.glob("*.mp4") if not x.name.endswith("-4x5.mp4"))
        lst = li / "_l.txt"; lst.write_text("".join(f"file '{x}'\n" for x in parts))
        v45 = li / "reel-4x5.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(v45)], check=True)
        m.update(instagram=[str(v)], facebook=[str(v)], cover=str(cover), linkedin_video=str(v45))
    elif p["format"] == "karussell":
        run(SKILL / "render.py", src, "--out", d, "--format", "carousel")
        run(SKILL / "render.py", src, "--out", d / "stills", "--format", "carousel", "--stills", "--hd")
        vids = sorted(d.glob("*.mp4")); names = [x.stem for x in vids]
        gal = [str(last(d / "stills", n + "_")) for n in names]
        m.update(instagram=[str(x) for x in vids], facebook=gal)
    else:
        run(SKILL / "render.py", src, "--out", d / "stills", "--format", "carousel", "--stills", "--hd")
        hd = last(d / "stills", ""); sd = d / "standbild.png"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(hd), "-vf", "scale=1080:-1:flags=lanczos", str(sd)], check=True)
        m.update(instagram=[str(sd)], facebook=[str(sd)], linkedin_bild=str(hd))
    man[p["tag"]] = m
    (out / "manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False))

if plan.get("storys") and not a.nur:
    sd = out / "storys"; run(SKILL / "render.py", w / plan["storys"], "--out", sd, "--format", "story")
    man["storys"] = [str(x) for x in sorted(sd.glob("*.mp4"))]
    (out / "manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False))
print("fertig:", out / "manifest.json")
