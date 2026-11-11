# Zernio-Test · Anleitung

## Was du machst (etwa 10 Minuten)

1. **Konto anlegen** auf zernio.com, gratis und ohne Kreditkarte.
2. **Instagram verbinden:** das Business-Konto von flowkraft, Anmeldung läuft über Facebook.
3. **LinkedIn verbinden:** Nach der Anmeldung **dein persönliches Profil** wählen, nicht eine Seite.
   Facebook noch nicht verbinden, damit der Test bei den 2 Gratis-Konten bleibt.
4. **API-Schlüssel erstellen** in den Einstellungen von Zernio (API Keys).
5. **Schlüssel ablegen:** Diesen Befehl im Terminal ausführen. Er öffnet eine leere Datei in TextEdit:

   ```bash
   mkdir -p ~/.flowkraft-motion && touch ~/.flowkraft-motion/zernio.env && chmod 600 ~/.flowkraft-motion/zernio.env && open -e ~/.flowkraft-motion/zernio.env
   ```

   Dort eine Zeile eintragen und speichern: `ZERNIO_API_KEY=` und direkt dahinter deinen Schlüssel.
   Den Schlüssel bitte nicht in den Chat schreiben. Er liegt so nur auf deinem Mac und nicht im Projektordner.

## Was danach passiert

| Schritt | Befehl | Geht etwas raus? |
|---|---|---|
| Konten prüfen | `zernio_test.py konten` | nein |
| Als Entwurf ablegen | `zernio_test.py di --modus entwurf` | nein, du siehst ihn im Kalender von Zernio |
| Wirklich einplanen | `zernio_test.py di --modus planen --zeit 2026-11-17T18:00:00` | **ja**, nur nach deinem Okay |

Getestet wird der Dienstag: Instagram-Karussell aus 7 Video-Slides und LinkedIn-PDF, Texte aus `probewoche-kw47/texte.md`.

## Prüfpunkte

1. Nimmt Zernio das Karussell mit 7 Videos an, oder nur 1 Video?
2. Erscheint auf Instagram ein Karussell und kein einzelnes Video?
3. Kommt das LinkedIn-PDF als Dokument mit Titel und blätterbaren Seiten an?
4. Offen: Wie setzt man bei Reels ein Titelbild? Steht nicht in der Doku, wird beim Montag-Reel getestet.
