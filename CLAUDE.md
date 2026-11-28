# flowkraft Social – Wissen für jede Sitzung

Dieses Repository ist das ganze Social-Media-System von flowkraft. Jede Claude-Sitzung (Mac, Laptop, Cloud, Routine) liest diese Datei zuerst. Entscheidungen von Daniel stehen hier und gehen allem anderen vor. Neue Entscheidungen trägst du hier ein (mit Datum), damit sie auf jedem Gerät gelten.

## Wer und für wen

- **flowkraft**: Daniel, arbeitet allein, Sitz Kärnten. Büroautomatisierung mit KI.
- **Zielgruppe** (19.11.2026): Klein- und Mittelbetriebe mit **1–50 Mitarbeitern** im ganzen DACH-Raum. Typische Einwände, die Posts aufgreifen: „Das ist nur was für große Firmen“, „Zu teuer“, „Meine Leute machen da nicht mit“.
- **Ansprache**: Du. Kein Firmen-„Wir“, „ich“ sparsam. Stimme: `docs/flowkraft-voice.md`.
- **Teamregel**: Agenten geben sich nicht gegenseitig recht, immer kritisch, analytisch, ehrlich (`docs/flowkraft-team-regeln.md`).
- **Ziel** laut Fahrplan: 2.000 Follower und 60 Leads bis 30.06.2027. Start bei 0 Followern.

## Was Daniel entschieden hat

**Rhythmus und Mengen**
- Posten Mo–Sa, **immer 18:00 Uhr Wien**, auf allen Kanälen (12.11.2026).
- Pro Woche 6 Posts + 6 Storys, Reel / Karussell / Post etwa 2 / 2 / 2. Das Team darf Formatwechsel vorschlagen.
- Samstag wechselt zwischen Säule 5 (Praxisbeispiel) und Säule 4 („Rechnet sich das?“).

**Formate**
- **Reels in jeder Variante, aber nie Weiß auf Weiß:** In `mist` sind Schrift, Outline, Schmuckwort und Icons dunkel (Engine angepasst 16.11.2026). Reels laufen **60 % langsamer** als die erste Fassung (Faktor 1,6), damit man die Texte lesen kann (16.11.2026).
- **Abwechslung** (16.11.2026): kein Thema zweimal in der Woche und keines aus den letzten 4 Wochen. Jede Szene und jedes Icon höchstens einmal pro Woche, Icons immer wieder neu gestalten.
- **Kennzahlen für Daniel** (17.11.2026): Montags-Mail mit Block „Letzte Woche“ (Reichweite, Interaktionen, Speichern + Teilen, Follower je Kanal mit Zuwachs, bester und schwächster Post, ein Lernpunkt), Freigabeseite zusätzlich mit Tabelle pro Post. Quelle: `content/analysen/KWnn-zahlen.json`. Bei wenig Daten steht das offen da, nichts wird schöngerechnet.
- **Übersicht für Daniel** (16.11.2026): Mail und Freigabeseite zeigen pro Post eine Ampel (grün, gelb, rot) mit einem kurzen Grund, keinen Prüfbericht als Text. Der Prüfer schreibt dafür `content/KWnn/ampel.json`.
- **Reels nur als Drohnenflug** (`skill/flowkraft-motion-skill/engine/flight.py`, Modus `split`, Texttiefe 4 %), freigegeben am 12.11.2026. Das KW-47-Reel „Termine“ ist die Referenz.
- **Einzel-Posts als Standbild** (`clean: true`: ohne Logo, Label, „Speichern“, flowkraft.at).
- **Karussells** als Video-Slides; auf Facebook als Bildergalerie.
- **Storys** automatisch, **ohne Sticker** (keine Umfrage, keine Frage-Box). Die Frage steht als Text, Antworten kommen per DM. Freigabe wie bei den Posts.
- Kein Voiceover, kein Filmmaterial. Keine Musik, nur Soundeffekte aus Code.

**Kanäle**
- **Instagram**: Business-Konto. In Zernio absichtlich **nicht verbunden**, bis Daniel ein Firmen-Bankkonto hat (12.11.2026). Die Instagram-Posts werden trotzdem jede Woche komplett gebaut: `drafts.py` lädt die Medien hoch und zeigt sie als **Instagram-Vorschau** (ohne Knöpfe) auf der Freigabeseite (Wunsch von Daniel, 12.11.2026). Nicht „reparieren“, Instagram nicht selbst verbinden.
- **Facebook**: Seite, über Zernio verbunden.
- **LinkedIn** (persönliches Profil): nur **Di Video 4:5** (1080 × 1350, 9:16 zeigt schwarze Ränder) und **Do Standbild 4:5**. Kein PDF, kein reiner Textpost, kein Link im Post, höchstens 3 Hashtags. Material aus der Instagram-Woche, nur der Text ist neu. Das Di-Video bleibt die Reel-Slides als 4:5-Videos hintereinander, kein Drohnenflug (Entscheidung 17.11.2026).

**Inhalte**
- Keine erfundenen Zahlen, Kundenstimmen, Preise oder Kundenprojekte. Beispielrechnungen kennzeichnen.
- Praxisbeispiele (Säule 5) sind Use Cases und Musterprojekte aus Daniels Weiterbildung, keine Kundenprojekte.
- **Nächster Schritt = KI-ROI-Check** (28.11.2026): Homepage ist online, das Formular https://www.flowkraft.at/ki-check/ funktioniert. **Jeder Post** endet damit: Instagram „Kommentiere ROI und du bekommst den Link zum kostenlosen KI-ROI-Check.“ (Link per DM), Facebook Link direkt, LinkedIn „Link in meinem Profil“ (kein Link im Post), Story „Schreib mir ROI“. Letzte Slide/Station: Instagram-Fassung zeigt „Kommentiere ROI“ (`cta_instagram`, `--kanal instagram`), Facebook-Galerie und LinkedIn „KI-ROI-Check auf flowkraft.at“ (`cta`); das Reel ist die Instagram-Fassung und läuft auch auf Facebook. Details: `docs/lead-magnete.md`. Die Serie „Unser Selbstversuch“ läuft vorerst nicht.
- **Social-Post-Prompt** (19.11.2026): `docs/prompt-social-post.md` gilt zusätzlich für alle Agenten, übernommen in `docs/flowkraft-voice.md` (Abschnitt 13). Bei Widerspruch bleibt: überall Du (auch LinkedIn), Karussell 6–8 Slides, DACH-Raum, kein Voiceover/Musik/Textpost. Der KI-Check aus dem Prompt ist der KI-ROI-Check, seit 28.11.2026 in jedem Post.
- Stil der Motion-Posts: `skill/flowkraft-motion-skill/SKILL.md` (kein Loop, F-Ball, Abwechslung pro Slide, Homepage-Look).

## Nie ohne klares Ja

- **Nichts geht live ohne Daniels Freigabe.** Agenten und Routinen legen nur Entwürfe an (`isDraft: true`).
- Vor jedem echten Einplanen oder Veröffentlichen außerhalb der Freigabeseite eine eigene Ja/Nein-Frage stellen („Das geht öffentlich raus, wirklich posten?“). „Testen“ oder „simulieren“ heißt nicht posten.
- Schlüssel nie in den Chat, nie ins Repository, nie in Web-Formulare tippen. Daniel trägt sie selbst ein.
- Pushen nach GitHub macht Daniel selbst im Terminal.

## Wie das System läuft

Ablauf im Detail: `WOCHE.md`. Kurz:

| Wann (Wien) | Cloud-Routine | Ergebnis |
|---|---|---|
| Sa 06:00 | flowkraft Analyse | `content/analysen/KWnn.md` auf Branch `claude/analyse-KWnn` |
| So 05:00 | flowkraft Produktion | Woche rendern, Zernio-Entwürfe, Freigabeseite; Branch `claude/woche-KWnn` |
| Mo 08:00 | flowkraft Benachrichtigung | Mail an Daniel mit Link zur Freigabeseite |

- Die Routinen laufen in der Cloud-Umgebung „Default“, verwaltet auf claude.ai/code/routines. Die Cron-Zeiten stehen in UTC, deshalb ab Ende März um eine Stunde anpassen.
- **Zernio** plant und postet. **Netlify** hostet die Freigabeseite (`tools/woche/freigabe.py`). **Make** hat zwei Szenarien: „flowkraft Freigabe“ setzt Entwürfe auf eingeplant oder löscht sie, „flowkraft Woche bereit“ schickt die Mail per Gmail. Einrichtung: `docs/make-einrichtung.md`, Vorlagen in `docs/make/`.
- Umgebungsvariablen (Cloud-Umgebung, lokal in `~/.flowkraft-motion/*.env`): `ZERNIO_API_KEY`, `MAKE_NOTIFY_URL`, `MAKE_APPROVE_URL`, `NETLIFY_TOKEN`, `NETLIFY_SITE_ID`.
- Agenten: `.claude/agents/` (social-media-manager, recherche, copywriter, designer, pruefer, analyst, community).
- Rendern geht auf dem Mac und in der Cloud (`docs/cloud-render-test.md`). Einrichten mit `bash skill/flowkraft-motion-skill/scripts/setup.sh`.

## Stand (bei Änderungen hier nachtragen)

- 12.11.2026: Alle Teile einzeln getestet: Zernio-Entwürfe, Netlify, Make-Mail, „Nicht posten“, Cloud-Rendern, Cloud-Variablen.
- Noch nie am Stück gelaufen: der erste Durchlauf ist So 15.11.2026 (KW 47) als Trockenlauf. „Freigeben“ wird mit der ersten echten Freigabe zum ersten Mal getestet.
- **Trockenlauf KW 47: Daniel will danach NICHTS posten** (12.11.2026). Das Make-Szenario „flowkraft Freigabe“ ist dafür **ausgeschaltet**. Die KW-47-Entwürfe bleiben in Zernio liegen und werden nach der Durchsicht gelöscht, nicht eingeplant.
- **KW 48 (23.–28.11.2026) ist der zweite Testlauf** (Entscheidung 17.11.2026): wie KW 47 nur Entwürfe, nichts posten, „flowkraft Freigabe“ bleibt aus. Ziel: die Änderungen vom 16./17.11. prüfen (Ampel, „Was nicht passt“, Kennzahlen, langsame Reels, Mist mit dunkler Schrift, Abwechslung: kein Thema aus KW 47). Danach Entwürfe löschen.
- 17.11.2026: Alle 14 KW-47-Entwürfe in Zernio gelöscht. Die 16 Testposts vom 09.11. bleiben im Zernio-Verlauf als „veröffentlicht“ stehen: Zernio löscht veröffentlichte Posts nicht, auf den Plattformen sind sie weg. Die Analyse ignoriert sie (älter als 7 Tage).
- 17.11.2026: Warteschlange geleert (14 KW-47-Klicks gelöscht). „Freigeben“ getestet: Make setzt den Zernio-Entwurf auf eingeplant, 18:00 Wien korrekt; Testpost gelöscht. Szenario danach wieder aus. Vor KW 48 (Mo 23.11.2026) einschalten, nur auf Daniels Ja.
- Samstags-Analyse fragt Zernio-Kennzahlen jetzt nach (HTTP 202 = wird synchronisiert).
- Vor dem Wiedereinschalten von „flowkraft Freigabe“: in Make die Webhook-Warteschlange von `flowkraft-freigabe` leeren. Ein ausgeschalteter Webhook sammelt Klicks und würde sie beim Einschalten ausführen. Einschalten nur auf Daniels ausdrückliches Ja.
- Instagram wartet auf das Firmen-Bankkonto.
- 28.11.2026: Homepage online, KI-ROI-Check live. Für „ROI“-Kommentare und -DMs gibt es noch keine Automatik: der Community-Agent entwirft die Antwort mit Link, Daniel schickt sie ab. Daniel trägt den Link noch im LinkedIn-Profil und in der Instagram-Bio ein.

## Geräte

- Ab jetzt ist **das Repository die Hauptquelle**, auch für den Skill: `skill/flowkraft-motion-skill/` ist die maßgebliche Kopie. Auf dem Mac liegt zusätzlich `~/.claude/skills/flowkraft-motion-skill`. Wer den Skill ändert, gleicht beide Kopien ab.
- Laptop: Sitzung auf claude.ai/code mit diesem Repository, oder Claude Code lokal mit einer Kopie des Repositorys. Fürs wöchentliche Freigeben braucht es keinen Chat, nur die Mail und die Freigabeseite.
