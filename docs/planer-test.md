# Planer-Test · Stand 09.11.2026

Recherche aus Hilfeseiten und Testberichten, noch nicht selbst ausprobiert. Preise vor dem Kauf auf der Anbieterseite prüfen.

## Was der Planer können muss

| Format | Kanal | Ergebnis Recherche |
|---|---|---|
| Reel | Instagram, Facebook | Geht automatisch |
| Karussell aus Video-Slides | Instagram | Geht automatisch, bis 10 Slides, Videos bis 60 s (unsere: 9 s) |
| Karussell aus Video-Slides | Facebook | Geht nicht (Metricool: Karussell auf Facebook nicht unterstützt) |
| Post als Standbild | alle | Geht automatisch |
| Story ohne Sticker | Instagram, Facebook | Geht automatisch |
| Story mit Umfrage oder Frage-Box | Instagram | Geht nicht über die Schnittstelle, Planer schickt eine Erinnerung, Daniel postet |
| PDF-Karussell | LinkedIn persönliches Profil | Metricool und Buffer: ja. Make-Modul: kein Dokument-Post gefunden |
| Übergabe vom Agenten | alle | Metricool ab Advanced: API, Make, MCP |

## Kandidaten

1. **Metricool Advanced** (Empfehlung): ab etwa 43 € pro Monat (jährlich, ohne MwSt.), API ab diesem Tarif. Kann alle Formate außer Facebook-Karussell und Sticker-Storys.
2. **Make und direkte Schnittstellen:** günstig, Make ist schon da. Instagram geht (Karussell, Reel), LinkedIn-PDF und Storys nur über eigene API-Aufrufe. Mehr Wartung.
3. **Buffer:** LinkedIn-PDF und gemischte Instagram-Karussells laut Hilfe ja, Schnittstelle und Storys unklar.

## Günstigere Alternativen (Recherche 09.11.2026)

| Tool | Preis für 3 Konten (IG, FB, LinkedIn) | Video-Karussell IG | Storys | LinkedIn-PDF persönlich | Schnittstelle |
|---|---|---|---|---|---|
| **Zernio** (früher Late) | 2 Konten gratis, ab dem 3. 6 $ pro Monat, also etwa 6 $ | unklar, Doku nennt 1 Video pro Post, muss getestet werden | ja (Video bis 60 s) | ja | ja, in jedem Tarif |
| Upload-Post | ab 16 $ pro Monat (jährlich) | unklar | unklar | ja | ja |
| Publer Business | etwa 10 $ plus 7 $ pro weiteres Konto | **nein**, keine Videos im Karussell | ja (Business-Konto) | ja | ja |
| Metricool Advanced | ab etwa 43 € | ja | ja (ohne Sticker) | ja | ja |

**Empfehlung:** Zuerst Zernio gratis testen (Instagram und LinkedIn als die 2 freien Konten), Prüfpunkt Nummer 1 ist das Karussell mit 7 Video-Slides. Klappt das, Facebook als 3. Konto dazu. Klappt es nicht, bleibt Metricool. Publer fällt raus.

Risiko Zernio: kleiner, junger Anbieter. Fällt er weg, müssen nur die Übergabe-Aufrufe der Agenten getauscht werden, die Inhalte bleiben gleich.

## Folgen für den Wochenplan

- **Facebook-Karussell:** Entschieden am 09.11.2026: als Bildergalerie aus den Endbildern der Slides, gleiche Caption wie Instagram. KW 47 liegt in `probewoche-kw47/facebook/`.
- **Storys:** Weil alle 6 einen Sticker haben, bleiben sie Handarbeit (etwa 2 Minuten am Tag). Alternative: Storys ohne Sticker automatisch.

## Praxistest (nächster Schritt)

Zernio testen (sonst Metricool), Konten verbinden, dann für KW 47 planen:
1. Mo-Reel auf Instagram und Facebook, LinkedIn-Text
2. Di-Karussell (7 Video-Slides) auf Instagram, Bildergalerie auf Facebook, LinkedIn-PDF
3. Mi-Standbild
4. Eine Story ohne Sticker

Prüfen: Kommt alles zur geplanten Zeit, stimmen Reihenfolge, Ton und Bildschnitt, und wird das Karussell nicht als einzelnes Video gepostet.

## Ergebnis Zernio-Test, Stufe 1 (09.11.2026)

- Konten verbunden: Instagram (flowkraft.at) und LinkedIn (persönliches Profil).
- Upload der 7 Video-Slides und des PDFs: ok.
- Dienstag als Entwurf angelegt: Instagram-Post mit 7 Videos angenommen, LinkedIn-Post mit Dokument und Titel angenommen. Beide Status „draft“, nichts veröffentlicht.
- Noch nicht bewiesen: ob Instagram beim Veröffentlichen wirklich ein Karussell daraus macht und ob LinkedIn das PDF blätterbar zeigt. Das zeigt erst der echte Post.
- Hinweis: `dryRun` gilt bei Zernio nur für TikTok, deshalb wurde direkt als Entwurf getestet.
- Technik: Homebrew-Python braucht die Zertifikate von macOS (`/etc/ssl/cert.pem`), ist im Skript gelöst.

## Ergebnis Simulation 09.11.2026 (echt gepostet, vom Nutzer danach gelöscht)

- Mo bis Do: Reels, Video-Karussell (als Feed-Post /p/, 7 Videos), Standbild, LinkedIn-Text, LinkedIn-PDF und Storys ohne Sticker gingen pünktlich raus. Ein Video-Karussell braucht bei Instagram etwa 3 bis 4 Minuten Verarbeitung.
- **Titelbild fehlte:** `thumbnail` am Medium ignoriert Instagram. Laut SDK-Doku heißt das Feld `platformSpecificData.instagramThumbnail` (Alias `reelCover`, alternativ `thumbOffset` in ms). Im Skript umgestellt, noch nicht getestet.
- Fr und Sa: Karussell (6 Videos), LinkedIn-Text, Standbild und Storys pünktlich raus.
- Titelbild-Test 14:15 mit `platformSpecificData.instagramThumbnail`: funktioniert, vom Nutzer im Raster bestätigt. Thumbnail am Medium (`thumbnail`) wirkt bei Instagram nicht.
- Facebook nicht getestet (im Gratis-Test nicht verbunden).

## Ergebnis Facebook und LinkedIn (11.11.2026, echt gepostet, Nutzer löscht von Hand)

- Facebook: Reels mit Titelbild (`thumbnail` am Medium), Galerien mit 7 und 6 Bildern, Standbilder, alle pünktlich veröffentlicht.
- LinkedIn persönliches Profil: Video (Di) und Standbild (Do) pünktlich veröffentlicht.
- Damit sind alle geplanten Formate über Zernio getestet. Offen: Storys mit Sticker bleiben Handarbeit; Instagram ist in Zernio aktuell nicht mehr verbunden.
