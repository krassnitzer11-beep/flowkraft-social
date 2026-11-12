---
name: flowkraft-motion-skill
description: 'Baut animierte flowkraft-Posts als Videos: Instagram-Karussells, Storys und Reels mit Motion Graphics, 3D-Szenen, F-Ball und Soundeffekten, in den Farbvarianten Navy, Dunkel und Mist. Immer verwenden, wenn der Nutzer einen flowkraft-Post, ein Karussell, eine Story, ein Reel, ein Social-Media-Video oder Motion Graphics für flowkraft möchte, auch wenn er nur ein Thema nennt ("mach mir ein Karussell zu Rechnungen", "Story zu Terminbuchung in Mist", "Reel zum Zeitfresser") oder bestehende Slides ändern will (Text, Icon, Farbe, Szene, Lautstärke).'
---

# flowkraft Motion

Erzeugt fertige MP4s aus einer kleinen Post-Datei. Inhalte (Texte, Icons, Szene, Variante) stehen nur in der Post-Datei, die Technik liegt in `engine/`. Dadurch ist jede Änderung auf Zuruf eine Zeile plus neu rendern.

## Ablauf

1. **Einmalig pro Rechner:** `scripts/setup.sh` ausführen (legt `~/.flowkraft-motion/venv` an). Braucht Google Chrome, ffmpeg, Python 3. Prüfe zuerst, ob `~/.flowkraft-motion/venv/bin/python` existiert.
2. **Klären, nur was fehlt:** Thema, Format (Karussell, Story, Reel), Variante. Sinnvolle Vorgabe: Problem-Thema → Dunkel, Lösung/Ablauf → Mist, Leistung/Marke → Navy. Texte selbst vorschlagen, wenn keine geliefert wurden. Keine erfundenen Kennzahlen, Kundenzitate oder Preise: fehlt eine Zahl, frag nach.
3. **Post-Datei schreiben** im aktuellen Projektordner, z. B. `posts/rechnungen.js`. Vorlagen in `posts/` des Skills. Schema unten, Szenen in `references/scenes.md` (vor der Szenenwahl lesen).
4. **Kontrollbilder rendern** und ansehen, bevor Videos laufen (`--stills`). Achte auf Text, der in Szenen läuft, und zu lange Headlines.
5. **Videos rendern**, Ergebnis prüfen, dem Nutzer die Dateien geben. Klang kannst du nicht hören, nur Pegel messen. Sag das offen.

```bash
~/.flowkraft-motion/venv/bin/python <skill>/engine/render.py posts/x.js --out videos --format carousel
```

Optionen: `--format carousel|story|reel` · `--theme navy|dark|mist` (überschreibt die Datei) · `--slides 2 5` (nur diese) · `--stills` · `--audio-only` (nur Ton neu einsetzen, Bild bleibt, etwa 1 Minute).

Ein Lauf dauert rund 40 Sekunden pro Slide. Laufzeiten über 2 Minuten im Hintergrund starten.

## Formate

| Format | Größe | Ergebnis |
|---|---|---|
| carousel | 1080 × 1350 | ein Video pro Slide |
| story | 1080 × 1920 | ein Video pro Slide |
| reel | 1080 × 1920 | ein durchgehendes Video, Übergang durch den F-Ball |

**Einzel-Post = Standbild.** Ein Post mit nur einer Slide geht als Bild raus, nicht als Video: Instagram veröffentlicht Feed-Videos als Reel, dann wäre die Wochenmischung (Reel, Karussell, Post) dahin, und das Video startet mit leerer Fläche. Mit `--stills` rendern und das letzte Kontrollbild (fertiges Bild) nehmen, 1080 × 1350 PNG. In der Post-Datei `clean: true` setzen und kein `cta`: Das Standbild hat kein Logo, kein Label oben rechts, keinen Button und kein flowkraft.at, nur Szene und Text. Reels und Karussells bleiben Videos.

**Reel-Layout:** kein Logo, kein Label, kein flowkraft.at (wie Story). Der F-Ball bleibt aus den Zonen, die Instagram verdeckt: rechts etwa 120 px Buttons, unten etwa 400 px Caption, oben etwa 200 px. Er parkt bei x 880 und endet in der letzten Szene bei (800, 1150) statt im Wasserzeichen rechts unten.

**Reel-Variante Drohnenflug (Entwurf, noch nicht freigegeben):** `flight: true` in der Post-Datei. Statt der Ball-Abdeckung fliegt die Kamera am Szenenende nach vorn durch Wolken, abwechselnd abtauchend und steigend, die nächste Szene kommt aus der Tiefe. Der Ball fliegt voraus. Code: `camera()` in `engine.html`.

**Drohnenflug-Reel (vom Nutzer am 11.11.2026 abgenommen, nach Vorbild FPV-Flug):** Stand: Modus split, Szene und Schrift als ganze Ebenen, Ringe in 3D, Tempo als Hermite-Kurve (an Stationen 330, Übergänge 1,8–2,5 s), geglättete Bahn, Blick zeitlich geglättet, Horizont halb gedämpft, Wellen-Landschaft mit Flow-Welle der Homepage, 4 % Schrifttiefe. Nicht ohne Rückfrage zurückdrehen. `engine/flight.py POST.js --out ORDNER [--stills t1 t2 …]` rendert mit `engine/flight3d.html` in echtem 3D (three.js 0.160 in `engine/lib`, Schrift als TTF in `assets`). Alle Szenen stehen hintereinander in einer Welt mit Nebel, Punktraster-Boden und Staub. Standard ist `--mode split`: jede Slide wird zu zwei Stationen (Szene eng zugeschnitten, Headline), 1,3-fach größer, abwechselnd links/rechts; Reihenfolge pro Slide mit `first: 'text'` oder `'scene'` (Hook: Schrift zuerst). Die Szenen-Zeit friert zwischen beiden Stationen ein, der F-Ball fliegt nur noch in 3D von Treffer zu Treffer. Flächen werden ausgeblendet, sobald die Kamera zu nah ist. `--mode pass`: Szenen stehen abwechselnd links und rechts schräg im Raum, die Drohne schlängelt sich vorbei, Tempo aus dem Abstand zur nächsten Szene (nah 300, dazwischen bis 2600 Einheiten/s, nie null), Motion Graphics poppen beim Anflug auf, Hook mit langsamem Anflug, Ende = bester Blick auf die letzte Szene. `--mode front`: frontal mit Lese-Halt. Frontal-Variante: Die Kamera folgt einer weichen Kurve und bleibt nie stehen: beim Lesen langsam (70 Einheiten/s), dazwischen schnell, abwechselnd unter und über der Schrift durch, mit Querlage in Kurven. Headlines haben standardmäßig **4 % Tiefe** (Anteil der Schrifthöhe, vom Nutzer nach Tests mit 30 %, 8 %, flach und 6 % festgelegt). Abweichend: `depth` auf Post- oder Slide-Ebene (0 = flach), `scriptDepth` nur fürs Script-Wort. Weiße Schrift nie mit blauen Seiten. TTFLoader rechnet in Punkt, deshalb `size * .72`. Die Szenen kommen aus der Engine: `engine.html?…&f=story&layer=hero` rendert jede Szene transparent mit F-Ball, ohne Hintergrund und Headline; der Flug zeigt diese Bildfolge als Fläche an der Station und setzt die 3D-Headline an die Engine-Positionen, getaktet auf die Ball-Treffer. Zwischen den Stationen fliegt ein 3D-Ball. Ton = Szenen-Töne der Engine + Flug-Whooshes. `--keep ORDNER` hebt die Bildfolgen für schnelle Wiederholungen auf. Ältere CSS-Variante: `--engine css` (unscharf, nicht verwenden).

**Reel-Titelbild = letztes Bild.** Reels starten leer, also braucht jedes Reel ein eigenes Titelbild, sonst zeigt das Raster ein leeres Feld: `ffmpeg -sseof -0.1 -i reel.mp4 -frames:v 1 -q:v 2 cover.jpg`. Bei Zernio geht es als `platformSpecificData.instagramThumbnail` mit (nicht `thumbnail` am Medium).

**Exportqualität (Wunsch des Nutzers, Bilder wirkten unscharf):** Alles wird doppelt gerendert (Supersampling) und mit Lanczos auf 1080 verkleinert, Videos mit CRF 12, `-tune film`, bis 25 Mbit/s. Standbilder für LinkedIn und Facebook mit `--hd` in 2160 Breite ausgeben (Instagram nimmt 1080).

**LinkedIn-Formate:** Video im Feed in **4:5 (1080 × 1350)**, nicht 9:16, sonst zeigt LinkedIn schwarze Ränder (getestet 11.11.2026). Standbild 4:5 passt in der großen Ansicht.

**Karussell auf Facebook = Bildergalerie.** Der Planer kann auf Facebook keine Video-Karussells. Dafür das letzte Kontrollbild jeder Slide nehmen, in Slide-Reihenfolge nummeriert (`name-1.png` …). Instagram bekommt die Videos. LinkedIn bekommt nur Video-Uploads oder Standbilder, kein PDF (Entscheidung des Nutzers).

Bei 9:16 sitzt die Komposition mittig, oben und unten bleiben 285 px frei: das sind die Instagram-Sicherheitszonen, dort liegt die App-Oberfläche.

Story und Reel sind keine Slides: Die Engine lässt dort Seitenzahl („2 / 6“) und Wisch-Pfeil automatisch weg. Für Reels und Storys ergibt ein Wisch-Hinweis keinen Sinn, also auch im Text keinen einbauen.

**Story:** ohne Logo, ohne Label oben rechts und ohne `flowkraft.at`. Das Wasserzeichen sitzt tiefer und ist unten angeschnitten. Eine Story ist eine Frage oder ein Gedanke zum Post des Tages, meist eine Slide. Sticker setzt der Nutzer in der App, also im Bild Platz dafür lassen.

**Reels nur als Drohnenflug (Entscheidung des Nutzers, 12.11.2026):** Jedes Reel wird mit `engine/flight.py POST.js --out ORDNER` gerendert (Modus split, siehe unten), nicht mehr mit `render.py --format reel`. Die Ball-Übergänge unten gelten nur noch als Altbestand.

**Reel:** Ein Reel ist eine durchgehende Geschichte, kein Karussell am Stück. Am Ende jeder Szene parkt der F-Ball klein am Rand, wächst dann über das ganze Bild und bringt beim Schrumpfen die nächste Szene mit. Der Wechsel dauert rund eine halbe Sekunde: Der Ball beschleunigt beim Wachsen bis zum Schnitt und schrumpft danach schnell, damit das Tempo über den Schnitt weiterläuft und keine Pause entsteht, die nach Ende aussieht. Die Lesezeit richtet sich nach der Wortzahl (1 bis 2,2 s). Nur die letzte Szene endet im Wasserzeichen. Im Reel kein CTA-Button, der nächste Schritt steht in der Caption. Für den Text gilt:
- Ein Satz pro Szene, jeder Satz führt den vorigen weiter („Ein Termin. Drei Mails.“ → „Bei 30 Terminen sind das 3 Stunden.“ → „Aufs Jahr: 132 Stunden.“ → „Oder es läuft von selbst.“).
- Keine Nummern (`num`) und fast kein Fließtext (`p`), höchstens ein kurzer Hinweis wie „Beispielrechnung“.
- 4 bis 6 Szenen, ein nächster Schritt in der letzten.

## Post-Datei

```js
window.POST = {
  name: 'flowkraft-rechnungen',   // Dateiname der Videos
  theme: 'mist',                  // navy | dark | mist
  label: 'LÖSUNG',                // oben rechts
  // script: '#9CCBF0',           // optional: Farbe der Script-Wörter überschreiben
  slides: [
    { hook: true, layout: 'top', outline: 'Weniger Routine.', title: 'Mehr Zeit fürs', script: 'Geschäft.', scene: 'chaos' },
    { layout: 'side', num: '01', title: 'Zeitfresser', script: 'finden.', p: 'Fließtext.', scene: 'clock', props: { coin: '€' } },
    { layout: 'stack', title: 'Lohnt sich das für deinen', script: 'Betrieb?', p: '…', cta: 'Kommentiere WORT', scene: 'comment', props: { word: 'WORT' } },
  ],
};
```

Felder pro Slide: `layout`, `title` (Bold), `script` (letztes Wort in Aesthetic Romance), `outline` (eigene Zeile, startet gefüllt und wird zur Outline), `num` ('01', rollt wie ein Zählwerk), `p` (Fließtext), `cta` (Button statt Seitenzahl), `hook` (erste Slide: ohne Logo, Pfeil statt Seitenzahl), `chips` (Chip-Reihe unter der Headline), `size` (Headline-Größe), `scene`, `props`, `dy` (Szene in px verschieben), `sceneScale`.

Layouts: `top` Text oben · `bottom` Text unten · `side` Zahl oben links, Headline unten, Platz rechts · `stack` Text oben, Fließtext unten, Platz dazwischen · `center` zentriert unten, Platz oben.

Icons: Namen in `references/scenes.md`, oder eigener SVG-Inhalt im 24er-Raster als String (`'<path d="…"/>'`). Neue Namen kommen in das Objekt `I` in `engine/engine.html`.

## Was den Stil ausmacht

Diese Punkte hat der Nutzer im Lauf der Arbeit entschieden. Sie sind der Grund, warum die Videos so aussehen, also ohne Rückfrage nicht zurückdrehen.

- **Abwechslung ist Pflicht.** Nachbar-Slides bekommen verschiedene Layouts und verschiedene Szenen, auch über Posts hinweg. „Nach 10 Karussell-Postings wissen alle, was als Nächstes kommt.“ Nie auf jeder Slide denselben Bauplan, keine Icon-Dreierketten als Standard. Die Szene zeigt den Inhalt: Zeitfresser → Uhr, Chaos → schießende Nachrichten.
- **Kein Loop.** Jedes Video startet mit der leeren Slide und endet im fertigen Bild.
- **Der F-Ball löst aus.** Weiße Bildmarke im Navy-Kreis hüpft zu den Elementen, jeder Aufprall startet eine Enthüllung. Am Ende taucht er ins Wasserzeichen (Mist: ins Logo, denn Mist hat kein Wasserzeichen).
- **Enthüllung statt Einblenden.** Outline-Text startet gefüllt, Zahlen rollen, Wörter steigen aus einer Maske.
- **Homepage-Look.** Neigung `rotateX(4°) rotateY(-9°)`, Perspektive 1800, dunkles Glas, F-Hub, blauer Verlauf `#2878B5 → #3F8FCD`, Kürzel-Chips wie „WA“ und „@“ statt fremder Logos.
- **Keine Flow-Welle** als Zusatz-Element in den flachen Slides. Ausnahme auf Wunsch des Nutzers: im Drohnenflug-Reel fließt die Flow-Welle der Homepage (Lichtsträhnen mit Teilchen) als Fluss durch eine Wellen-Landschaft aus Punktraster und Hügelkämmen.
- **Ton:** nur Soundeffekte, keine Musik, alle per Code erzeugt und damit lizenzfrei. Die Ball-Töne sind weich und fließend und liegen bei −45 dB (`BALL_DB` in `engine/sfx.py`), übrige Effekte normal. Keine Glocke beim Eintauchen ins Wasserzeichen; das Ding beim Häkchen bleibt.
- **Marke:** Open Sans Condensed + Aesthetic Romance, Vorlagentexte wörtlich übernehmen. Grundlage sind die Vorlagen im Artifact „flowkraft Instagram Textposts“, die Homepage liegt im Artifact „Büroarbeit automatisieren mit KI | flowkraft“.

## Neue Szene bauen

Passt keine Szene zum Inhalt, bau eine neue, statt eine unpassende zu nehmen. In `engine/engine.html` im Objekt `HEROES` eine Funktion ergänzen (Muster: `hourglass`, `ranking`) und in `ORDERS` die Reihenfolge der Ball-Stopps eintragen. Eine Szene liefert `anchors` (Ball-Ziele), `seek(t, TM, H0, L)` (Bild ist reine Funktion der Zeit, keine Timer) und `events(TM)` (Sound). Für Farben `FACE`, `SIDE`, `var(--hink)`, `var(--hsub)` nutzen, dann läuft sie in allen drei Varianten. Danach in `references/scenes.md` eintragen.
