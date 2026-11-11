# Cloud-Render-Test (Schritt 4)

Getestet am 11.11.2026 in einer Claude-Code-Cloud-Umgebung (Linux, 4 CPU-Kerne, 15 GB RAM, **keine GPU**).
Frage: Kann die Motion-Engine ohne den Mac rendern?

**Kurz: Ja.** Alle drei Render-Arten laufen in der Cloud, inklusive 3D-Drohnenflug mit Software-WebGL.
Es ist langsamer als auf dem Mac, aber für einen Wochen-Batch völlig ausreichend.

## Umgebung

- ffmpeg 7 (apt), Python 3.13, `scripts/setup.sh` lief ohne Änderung durch (51 s).
- Browser: In der Umgebung ist bereits „Chrome for Testing“ (Chromium 153) vorinstalliert, daher nimmt
  `channel="chrome"` diesen Browser und `setup.sh` lädt kein eigenes Chromium. Auf einem Linux-Server
  ohne Chrome lädt `setup.sh` Playwright-Chromium samt Systempaketen (`--with-deps`), das ist unverändert.
- WebGL: `ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero)), SwiftShader driver)`, also reines
  Software-WebGL auf der CPU. three.js lief ohne JS-Fehler.

## Ergebnisse

| Job | Befehl | Dauer | Ergebnis |
|---|---|---|---|
| Kontrollbilder Karussell | `render.py sa-post-drei-fragen.js --format carousel --stills` | **5 s** | 4 PNG, 1080 breit |
| Karussell-Video (1 Slide, 9 s) | `render.py sa-post-drei-fragen.js --format carousel` | **3:21 min** | 1080×1350, 30 fps, 9,0 s, Ton ✔ |
| Reel (4 Szenen, 21 s) | `render.py mo-reel-termine.js --format reel` | **8:27 min** | 1080×1920, 30 fps, 21,1 s, Ton ✔ |
| 3D-Drohnenflug (20 s) | `flight.py mo-reel-termine.js --keep …` | **18:40 min** | 1080×1920, 30 fps, 20,1 s, Ton ✔ |

Sichtprüfung (je 3–5 Einzelbilder pro Video): Schriften korrekt (Outline, Bold, Script „baust.“/„Stunden.“),
Szenen-Animationen, F-Ball, Hintergrund und Partikelband da. Keine schwarzen Bilder, kein kaputtes 3D.
Ton: Pegel bei ca. −31 dB Mittel / −7 bis −9 dB Spitze, also hörbar und nicht übersteuert.
Die Ebenen des Flugs (`--keep`) belegen ca. 300 MB.

Faustregel: ca. **20–25 s Renderzeit pro Sekunde Video** (2D) und ca. **55 s pro Sekunde** (3D-Flug).
Die Supersampling-Screenshots (2160 px breit) und x264 `-preset slow`/CRF 12 kosten die meiste Zeit.

## Probleme und Korrekturen (committet)

1. **Sporadischer Abbruch „Unable to capture screenshot“**: Headless-Chromium ohne GPU kann bei 2x-Supersampling
   gelegentlich keinen Screenshot liefern, meist beim ersten Bild einer neuen Szene. Der erste Reel-Lauf brach
   in Szene 2 bzw. 3 ab. Lösung: `shot()` in `render.py` wiederholt den Screenshot bis zu 5-mal mit kurzer
   Pause und meldet `Screenshot-Retry` auf stderr. Im erfolgreichen Lauf griff das einmal. `flight.py` nutzt
   jetzt dieselbe Funktion (und `launch()`) aus `render.py`, statt eine Kopie zu haben.
2. **Software-WebGL nur, wo nötig**: Auf Linux bekommt der Browser die SwiftShader-Flags jetzt nur für
   `flight.py` (`launch(..., webgl=True)`). Für `render.py` sind sie nicht nötig und machten das Reel
   deutlich langsamer (13:41 statt 8:27 min).
3. Testausgabe `out/` steht jetzt in `.gitignore`.

Auf dem Mac ändert sich nichts: Dort startet weiter Google Chrome ohne zusätzliche Flags. Der Retry greift
nur, wenn ein Screenshot tatsächlich fehlschlägt.

## Hochrechnung für eine Woche (wie KW 47)

Bei 2 Reels + 2 Drohnenflügen + 2 Karussells + 1 Post + Storys sind auf 4 Kernen ungefähr
**1,5–2 Stunden** Rechenzeit pro Woche zu erwarten. Das läuft unbeaufsichtigt in einem Batch.
Mehr Kerne verkürzen das, wenn man Posts parallel rendert (jeder Job nutzt etwa 1–2 Kerne).

## Empfehlung

**Cloud-Rendering ist machbar, ja.** Die Ergebnisse sehen gleich aus wie auf dem Mac (1080 breit,
Supersampling, CRF 12, Ton). Der Mac muss dafür nicht laufen.

- Für den Wochenbetrieb: Cloud-Umgebung mit `setup.sh` (ein Setup-Skript der Umgebung kann das bei jedem
  Start erledigen), dann die Render-Befehle der Woche nacheinander oder parallel.
- Die fertigen Videos müssen danach irgendwohin (z. B. Upload zu Zernio oder in einen Speicher), weil der
  Cloud-Container nach der Sitzung gelöscht wird. Das ist der nächste Schritt und hier nicht getestet.
- Fallback Mac bleibt sinnvoll für schnelle Einzel-Korrekturen (dort mit GPU deutlich schneller), ist aber
  nicht mehr Voraussetzung.
