"""Soundeffekte, synthetisch erzeugt (lizenzfrei) und frame-genau auf die Timeline (window.TL) gelegt."""
import numpy as np, wave

SR = 48000
BALL_DB = -45.0   # Spitzenpegel der Ball-Töne (dBFS)
RNG = np.random.default_rng(7)
# Pentatonik (G4 aufwärts) – jeder Aufprall des Balls einen Ton höher
NOTES = [392.0, 440.0, 523.25, 587.33, 659.25, 783.99, 880.0, 1046.5, 1174.7, 1318.5]


def _t(d): return np.arange(int(d * SR)) / SR


def plop(f, d=.28, vol=.55):
    t = _t(d)
    fr = f * (1 + 0.9 * np.exp(-t / .018))                    # schneller Pitch-Fall = „Blob“
    ph = 2 * np.pi * np.cumsum(fr) / SR
    s = np.sin(ph) * np.exp(-t / .07) + .35 * np.sin(2 * ph) * np.exp(-t / .03)
    s[:int(.004*SR)] += RNG.normal(0, .25, int(.004*SR)) * np.linspace(1, 0, int(.004*SR))
    return vol * s * np.minimum(1, t / .002)


def _lowpass(x, fc):
    X = np.fft.rfft(x); fr = np.fft.rfftfreq(len(x), 1/SR)
    X *= 1 / (1 + (fr / fc) ** 4); return np.fft.irfft(X, len(x))


def drop(f, d=.9, vol=.032):
    """Weicher Tropfen: sanfter Einsatz, leichtes Aufwärtsgleiten, langer Ausklang – kein Klick."""
    t = _t(d)
    fr = f * (1 + .06 * (1 - np.exp(-t / .05)))
    ph = 2*np.pi*np.cumsum(fr)/SR
    env = (1 - np.exp(-t / .012)) * np.exp(-t / .28)
    s = np.sin(ph) + .18*np.sin(2*ph + .5) * np.exp(-t / .12)
    return vol * _lowpass(s * env, 2400)


def breeze(d, vol=.011):
    """Lufthauch für den Sprung: tief gefiltertes Rauschen, sehr sanfte Hüllkurve."""
    n = int(d * SR); x = np.linspace(0, 1, n)
    return vol * _bandnoise(n, 180, 1400) * np.sin(np.pi * x) ** 3


def swell(d, f0=440, f1=660, vol=.016):
    """Aufsteigender, weicher Schweller statt Pfeifton beim Hereinfallen."""
    t = _t(d); x = t / d; fr = f0 + (f1 - f0) * x
    s = np.sin(2*np.pi*np.cumsum(fr)/SR) + .5*np.sin(2*np.pi*np.cumsum(fr*1.5)/SR)
    return vol * s * np.sin(np.pi*x/2) ** 2 * (1 - x**4) + breeze(d, .01)


def bubble(f=620, d=.16, vol=.32):
    t = _t(d); fr = f * (0.7 + 0.8 * (1 - np.exp(-t / .025)))   # Ton steigt = „Pop“
    return vol * np.sin(2*np.pi*np.cumsum(fr)/SR) * np.exp(-t / .045) * np.minimum(1, t/.002)


def tick(f=3200, d=.035, vol=.18):
    t = _t(d)
    s = (np.sin(2*np.pi*f*t) * .8 + RNG.normal(0, .12, len(t))) * (1 - np.exp(-t / .0015)) * np.exp(-t / .007)
    return .55 * vol * _lowpass(s, 5000)


def _bandnoise(n, lo, hi):
    X = np.fft.rfft(RNG.normal(0, 1, n)); fr = np.fft.rfftfreq(n, 1/SR)
    X[(fr < lo) | (fr > hi)] = 0
    s = np.fft.irfft(X, n); return s / (np.abs(s).max() + 1e-9)


def whoosh(d, vol=.16, lo=400, hi=4500):
    n = int(d * SR); t = np.linspace(0, 1, n)
    env = np.sin(np.pi * t) ** 2 * (0.6 + 0.4 * t)
    return vol * _bandnoise(n, lo, hi) * env


def whistle(d, f0=1500, f1=520, vol=.09):
    t = _t(d); x = t / d; fr = f0 + (f1 - f0) * x ** 1.5
    return vol * np.sin(2*np.pi*np.cumsum(fr)/SR) * np.sin(np.pi*x) ** .6


def bell(freqs, d=1.6, vol=.22, decay=.45):
    t = _t(d); s = np.zeros_like(t)
    for i, f in enumerate(freqs):
        for k, a in ((1, 1), (2.76, .35), (5.4, .12)):
            s += a * np.sin(2*np.pi*f*k*t + i) * np.exp(-t / (decay / k ** .5))
    s *= np.minimum(1, t / .003)
    return vol * s / len(freqs)


def sparkle(d=.5, vol=.12):
    s = np.zeros(int(d*SR))
    for i, f in enumerate([2093, 2637, 3136, 3951]):
        b = bell([f], .35, 1, .09); o = int(i * .06 * SR); s[o:o+len(b)] += b[:len(s)-o]
    return vol * s


def click(vol=.4):
    vol *= .45
    t = _t(.12)
    thump = np.sin(2*np.pi*(140 + 260*np.exp(-t/.01))*t) * np.exp(-t/.03)
    return vol * (thump + .5 * np.pad(tick(2600, .03, 1), (0, len(t) - int(.03*SR))))


def render(tl, path):
    T = tl['T']; n = int(T * SR) + SR // 2
    L = np.zeros(n); R = np.zeros(n)
    BL = np.zeros(n); BR = np.zeros(n)   # eigene Spur für den Ball

    def add(sig, at, pan=0.0, ball=False):
        i = int(at * SR)
        if i >= n or i + len(sig) <= 0: return
        if i < 0: sig = sig[-i:]; i = 0
        sig = sig[:n - i]
        l, r = (BL, BR) if ball else (L, R)
        l[i:i+len(sig)] += sig * np.sqrt((1 - pan) / 2) * 1.41
        r[i:i+len(sig)] += sig * np.sqrt((1 + pan) / 2) * 1.41

    pan = lambda x: float(np.clip((x / 1080 - .5) * .7, -.7, .7))
    stops, H0, merge = tl['stops'], tl['H0'], tl['merge']

    # Ball fällt herein (Reel ab Szene 2: Ball schrumpft aus der Abdeckung)
    if tl.get('intro'): add(whoosh(.8, .06, 180, 3200) if tl.get('flight') else whoosh(.45, .06, 250, 2600), 0)
    else: add(swell(stops[0]['t'] - .25), .25, pan(stops[0]['x']), True)
    for i, st in enumerate(stops):
        t, p, key = st['t'], pan(st['x']), st['key']
        add(drop(NOTES[min(i, len(NOTES)-1)]), t - .01, p, True)                # weicher Tropfen beim Aufsetzen
        nxt = stops[i+1]['t'] if i + 1 < len(stops) else merge['t1']
        add(breeze(max(.25, nxt - t + .05)), t, p, True)                         # Lufthauch beim Sprung
        if key == 'num':                                                   # Zählwerk-Ticks
            for c in range(tl['digits']):
                k = 5 + 2*c + 1; s0 = t + .03 + c*.12; dur = .9 + c*.15
                xs = np.linspace(0, 1, 400); u = 1 + 1.9*(xs-1)**3 + .9*(xs-1)**2
                for j in range(1, k + 1):
                    hit = np.argmax(u >= j / (k + 1)); add(tick(2400 + 200*c, .03, .07), s0 + xs[hit]*dur, p)
            add(whoosh(.7, .025, 1200, 5000), t + 1.3, p)                   # Füllung läuft ab
        elif key.startswith('g'):                                          # Wörter steigen auf
            gi = int(key[1:])
            for w in range(tl['groups'][gi]): add(tick(1800 + 220*w, .03, .1), t + .1 + w*.08, p)
            if tl['sid'] == 1 and gi == 0: add(whoosh(.9, .06, 3000, 9000), t + .7, p)
        elif key == 'script': add(_lowpass(sparkle(.6, .04), 6000), t + .05, p)
        elif key == 'p': add(whoosh(.5, .06, 1500, 7000), t + .02, p)
        elif key == 'cta': add(click(.45), t, p)
        elif key == 'arrow': add(tick(2400, .04, .2), t + .12, .5)
    # Eintauchen ins Wasserzeichen
    # Lesezeit-Akzente
    if tl.get('outro'): add(whoosh(.85, .09, 180, 3200) if tl.get('flight') else whoosh(.4, .07, 250, 2600), merge['t0'])   # Ball wächst übers Bild
    else: add(whoosh(1.5, .045, 250, 2200), H0 + .1)
    # Szenen-Effekte (kommen aus der Animation)
    for e in tl.get('events', []):
        t, p, k = e['t'], pan(e.get('x', 540)), e['k']
        if k == 'pop': add(_lowpass(bubble(e.get('f', 560), .18, .07), 3000), t + .02, p)
        elif k == 'tick': add(tick(e.get('f', 2000), .03, e.get('v', .08)), t, p)
        elif k == 'click': add(click(.3), t, p)
        elif k == 'thud': add(_lowpass(bubble(170, .26, .2), 900), t, p)
        elif k == 'coin': add(_lowpass(bell([2349.3], .5, .05, .1), 5000), t + .02, p)
        elif k == 'whoosh': add(whoosh(e.get('d', .7), .05, 300, 3000), t, p)
        elif k == 'ding': add(_lowpass(bell([1567.98, 2093.0], 1.6, .06, .45), 4000), t, p)
    if tl['cta']:
        add(click(.35), H0 + .55); add(click(.35), H0 + 1.35)
    add(tick(2000, .035, .12), H0 + 1.2, .5); add(tick(2300, .035, .09), H0 + 1.6, .5)

    # dezenter Raum (kurzer Hall)
    ir = RNG.normal(0, 1, int(.45*SR)) * np.exp(-np.arange(int(.45*SR)) / SR / .12) * .02
    for ch in (L, R):
        wet = np.fft.irfft(np.fft.rfft(ch, 2*n) * np.fft.rfft(ir, 2*n), 2*n)[:n]
        ch += wet
    bpk = max(np.abs(BL).max(), np.abs(BR).max()) + 1e-12
    g = 10 ** (BALL_DB / 20) / bpk                                         # Ball-Spur: Spitze exakt BALL_DB
    st = np.stack([L, R], 1)[:int(T * SR)]
    st = np.tanh(st * 1.2) / np.tanh(1.2)                                  # weich begrenzen (wie vorher)
    st += (np.stack([BL, BR], 1) * g)[:len(st)]                          # Ball erst danach: Spitze bleibt BALL_DB
    pk = np.abs(st).max()
    if pk > .89: st *= .89 / pk                                            # nur schützen, nicht hochziehen
    if not tl.get('outro'): st[-int(.3*SR):] *= np.linspace(1, 0, int(.3*SR))[:, None]   # sanftes Ende (nicht mitten im Reel)
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype('<i2').tobytes())
