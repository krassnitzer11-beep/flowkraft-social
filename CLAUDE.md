# flowkraft Social – Wissen für jede Sitzung

Dieses Repository ist das ganze Social-Media-System von flowkraft. Jede Claude-Sitzung (Mac, Laptop, Cloud, Routine) liest diese Datei zuerst. Entscheidungen von Daniel stehen hier und gehen allem anderen vor. Neue Entscheidungen trägst du hier ein (mit Datum), damit sie auf jedem Gerät gelten.

## Wer und für wen

- **flowkraft**: Daniel, arbeitet allein, Sitz Kärnten. Büroautomatisierung mit KI.
- **Zielgruppe**: Betriebe mit 5–50 Mitarbeitern im ganzen DACH-Raum.
- **Ansprache**: Du. Kein Firmen-„Wir“, „ich“ sparsam. Stimme: `docs/flowkraft-voice.md`.
- **Teamregel**: Agenten geben sich nicht gegenseitig recht, immer kritisch, analytisch, ehrlich (`docs/flowkraft-team-regeln.md`).
- **Ziel** laut Fahrplan: 2.000 Follower und 60 Leads bis 30.06.2027. Start bei 0 Followern.

## Was Daniel entschieden hat

**Rhythmus und Mengen**
- Posten Mo–Sa, **immer 18:00 Uhr Wien**, auf allen Kanälen (12.11.2026).
- Pro Woche 6 Posts + 6 Storys, Reel / Karussell / Post etwa 2 / 2 / 2. Das Team darf Formatwechsel vorschlagen.
- Samstag wechselt zwischen Säule 5 (Praxisbeispiel) und Säule 4 („Rechnet sich das?“).

**Formate**
- **Reels nur als Drohnenflug** (`skill/flowkraft-motion-skill/engine/flight.py`, Modus `split`, Texttiefe 4 %), freigegeben am 12.11.2026. Das KW-47-Reel „Termine“ ist die Referenz.
- **Einzel-Posts als Standbild** (`clean: true`: ohne Logo, Label, „Speichern“, flowkraft.at).
- **Karussells** als Video-Slides; auf Facebook als Bildergalerie.
- **Storys** automatisch, **ohne Sticker** (keine Umfrage, keine Frage-Box). Die Frage steht als Text, Antworten kommen per DM. Freigabe wie bei den Posts.
- Kein Voiceover, kein Filmmaterial. Keine Musik, nur Soundeffekte aus Code.

**Kanäle**
- **Instagram**: Business-Konto. In Zernio absichtlich **nicht verbunden**, bis Daniel ein Firmen-Bankkonto hat (12.11.2026). `drafts.py` überspringt Instagram, nicht „reparieren“.
- **Facebook**: Seite, über Zernio verbunden.
- **LinkedIn** (persönliches Profil): nur **Di Video 4:5** (1080 × 1350, 9:16 zeigt schwarze Ränder) und **Do Standbild 4:5**. Kein PDF, kein reiner Textpost, kein Link im Post, höchstens 3 Hashtags. Material aus der Instagram-Woche, nur der Text ist neu.

**Inhalte**
- Keine erfundenen Zahlen, Kundenstimmen, Preise oder Kundenprojekte. Beispielrechnungen kennzeichnen.
- Praxisbeispiele (Säule 5) sind Use Cases und Musterprojekte aus Daniels Weiterbildung, keine Kundenprojekte.
- Keyword „ROI“ nur, wenn `docs/lead-magnete.md` den ROI-Check als live führt. Die Serie „Unser Selbstversuch“ läuft vorerst nicht.
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
- Instagram wartet auf das Firmen-Bankkonto.

## Geräte

- Ab jetzt ist **das Repository die Hauptquelle**, auch für den Skill: `skill/flowkraft-motion-skill/` ist die maßgebliche Kopie. Auf dem Mac liegt zusätzlich `~/.claude/skills/flowkraft-motion-skill`. Wer den Skill ändert, gleicht beide Kopien ab.
- Laptop: Sitzung auf claude.ai/code mit diesem Repository, oder Claude Code lokal mit einer Kopie des Repositorys. Fürs wöchentliche Freigeben braucht es keinen Chat, nur die Mail und die Freigabeseite.
