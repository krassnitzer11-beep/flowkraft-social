# Gegenposition KW 47 (16.–21.11.2026)

Geschrieben vom Social-Media-Manager vor dem Plan, nach Teamregel 6. Fakt, Annahme und Vermutung sind gekennzeichnet.

Grundlage: das am 09.11.2026 freigegebene Material der Probewoche (`content/kw47/`), angepasst an Daniels Entscheidungen vom 12.11.2026 (18:00 Wien, Storys ohne Sticker, Reels nur als Drohnenflug, Posts als Standbild mit `clean: true`, LinkedIn nur Di Video 4:5 und Do Standbild). KW 47 ist der Trockenlauf: Es wird nichts gepostet (CLAUDE.md, 12.11.2026).

## Warum diese Woche scheitern könnte

### 1. Das Material ist eventuell schon öffentlich (größtes Risiko)
- **Fakt:** Die Analyse KW 46 meldet 13 Instagram-Posts mit Status „published“ und Instagram-URLs, inhaltlich Texte der Testwoche (Termine, Suche, Angebote, „Wann sich Automatisierung nicht lohnt“). Laut CLAUDE.md ist Instagram in Zernio nicht verbunden.
- **Folge:** Wenn diese Posts wirklich auf dem Konto stehen, plant diese Woche Inhalte, die schon draußen sind. Für eine echte Woche wäre das doppelter Inhalt. Für den Trockenlauf ist es egal, aber die Themen von KW 47 dürfen dann nicht unverändert in eine spätere echte Woche wandern.
- **Vorschlag:** Daniel prüft vor der nächsten echten Woche das Instagram-Konto. Bis das geklärt ist, gilt dieser Plan nur als Trockenlauf.

### 2. Szenen in Nachbar-Posts (Regel „keine Szene in zwei Nachbar-Posts“ verletzt)
- **Fakt (aus den Post-Dateien vom 09.11.):**
  - Mo Reel und Di Karussell teilen `flowpanel` und `hourglass`.
  - Do Reel und Fr Karussell teilen `chaos` und `dochub`.
  - Story Do (`chaos`) steht direkt vor dem Fr-Karussell mit `chaos`; Story Mo zeigt wie das Reel `calendar`.
- **Entscheidung:** Themen bleiben. Das Mo-Reel ist die freigegebene Referenz und wird nicht angefasst. Deshalb tauscht der Designer die Szenen in den Nachbarn aus:
  - Di: `flowpanel` (Slide Lösung) und `hourglass` durch andere Szenen ersetzen. Das stärkt nebenbei die dünne Lösungs-Slide 5, die der alte Prüfbericht bemängelt.
  - Fr: `chaos` und `dochub` ersetzen (Do behält beide, weil sie dort die Vorher/Nachher-Geschichte tragen).
  - Storys: keine Szene verwenden, die im Post desselben oder des Folgetags vorkommt.
- **Restrisiko:** `flowpanel` kommt dann noch Mo und Fr vor, `yeargrid` Di und Fr. Nicht benachbart, also regelkonform, aber die Handschrift wiederholt sich (alter Einwand: „nach 10 Postings wissen alle, was kommt“).

### 3. Drei Rechen-Posts in einer Woche
- **Fakt:** Mo (132 h), Di (220 h, 9.900 €) und Fr (80 h) folgen demselben Muster Aufgabe × Minuten = Stunden im Jahr. Der alte Prüfbericht hat höchstens zwei vorgeschlagen.
- **Entscheidung:** für den Trockenlauf beibehalten, weil das Material freigegeben ist und der Lauf die Technik testet, nicht die Inhalte. Für KW 48: höchstens zwei Rechen-Posts.

### 4. Storys ohne Sticker bringen bei 0 Followern vermutlich nichts
- **Fakt:** Die Storys vom 09.11. sind als Umfragen gebaut („1 · 2 · 3 oder mehr“), `storys.js` sagt im Kommentar, Daniel setze die Sticker in der App. Das gilt nicht mehr.
- **Folge:** Alle sechs Story-Texte müssen umgeschrieben werden: offene Frage als Text, klarer Hinweis „Antwort per DM“, keine Antwortoptionen, die nach Umfrage aussehen. Der Kommentar in `storys.js` muss weg.
- **Annahme:** Eine DM ist eine viel höhere Hürde als ein Umfrage-Tipp. Bei 0 Followern ist mit null Antworten zu rechnen. Das ist kein Fehler des Plans, aber die Story-Kennzahl wird in den ersten Wochen nichts aussagen.

### 5. Säulen über zwei Wochen schief
- **Fakt:** KW 47 hat Säule 1 zweimal (Mo, Fr), Säule 4 zweimal (Di, Sa), Säule 2 und 3 je einmal, Säule 5 gar nicht. Sa ersetzt das Praxisbeispiel Fehlerwächter (Details fehlten).
- **Folge:** Samstag wechselt laut CLAUDE.md zwischen 5 und 4. Damit muss KW 48 am Samstag Säule 5 bringen. `docs/praxisbeispiele.md` existiert nicht, die Details zum Fehlerwächter fehlten schon am 09.11. Ohne Material droht nächste Woche wieder ein Ersatz-Post.
- **Annahme:** Der Fahrplan liegt nicht im Repository; die Verteilung ist an CLAUDE.md und voice.md gemessen, nicht am Fahrplan selbst.
- **Vorschlag:** Daniel legt bis Mitte der Woche ein Musterprojekt für Säule 5 fest (z. B. Fehlerwächter oder Meetingvorbereitung) mit den nötigen Details. KW 48 mit Säule 2, 3 und 5 stärker, Säule 1 höchstens einmal.

### 6. Kein Lead möglich
- **Fakt:** `docs/lead-magnete.md` existiert nicht, voice.md führt den ROI-Check als „nicht live“. Also kein Keyword, jeder Post endet mit folgen, speichern oder teilen.
- **Folge:** Diese Woche kann (wenn sie echt liefe) höchstens Follower bringen, keinen der 60 Leads. Bewusst so entschieden.
- **Prüfpunkt:** Die Di-Schluss-Slide nutzt die Szene `roiform`. Der Prüfer soll kontrollieren, dass dort nichts wie ein ROI-Check oder ein Tool zum Ausfüllen aussieht, das es noch nicht gibt.

### 7. LinkedIn-Texte stehen am falschen Ort und mit falscher Uhrzeit
- **Fakt:** In `content/kw47/texte.md` steht der Di-LinkedIn-Text unter Mo, der Do-LinkedIn-Text unter Fr, beide mit „8 Uhr“. Der Plan verweist jetzt auf die Abschnitte „Di 17.11.“ und „Do 19.11.“.
- **Folge:** Der Copywriter muss die Texte in die Abschnitte Di und Do verschieben und „18:00“ eintragen, sonst findet `drafts.py` den falschen oder keinen Text. Der Reserve-Text unter Di (9.900 €) muss aus dem Di-Abschnitt raus oder klar als nicht verwendet markiert werden, damit er nicht als LinkedIn-Text gelesen wird.
- **Restrisiko:** Das LinkedIn-Video kommt aus dem Drohnenflug-Reel. Ob der Flug als 4:5 (1080 × 1350) sauber aussieht, ist **ungetestet** (Vermutung: Schrift am Rand kann angeschnitten sein). Der Designer prüft das Kontrollbild.
- **Do-Standbild:** stammt aus dem Sa-Post und erscheint auf LinkedIn zwei Tage vor Instagram. Vertretbar, da andere Leserschaft.

### 8. Technik: erster Lauf am Stück
- **Fakt:** Die Kette ist noch nie am Stück gelaufen. Rendern dauert in der Cloud 1,5–2 h, zwei Drohnenflug-Reels sind der teuerste Teil.
- **Folge:** Fällt ein Schritt aus, gibt es Montag 08:00 die Mail „Woche ist NICHT fertig“. Für den Trockenlauf ist genau das der Zweck.
- **Wichtig:** Das Make-Szenario „flowkraft Freigabe“ ist aus. Klicks auf der Freigabeseite sammeln sich in der Webhook-Warteschlange. Vor dem Einschalten leeren, sonst gehen KW-47-Entwürfe nachträglich raus.

### 9. Offene Punkte aus dem Prüfbericht vom 09.11.
- Mo: „mehr als drei volle Arbeitswochen“ hängt an 40 h/Woche, steht nicht im Bild. Im Reel steht der Satz nicht, nur „132 Stunden“; erledigt, solange die Caption ihn nicht aufnimmt.
- Do: Hook „Vorher: Chaos. Nachher: Ruhe.“ zeigt keine Branche oder Rolle (Prüfliste Punkt 3). Bleibt für den Trockenlauf; für eine echte Woche schärfen.
- Fr: 20 Minuten Suchzeit pro Tag ist ein Beispielwert ohne Quelle, muss als Beispielrechnung gekennzeichnet bleiben.
- Mi und Sa haben keinen Nutzen in Stunden oder Euro (Prüfliste Punkt 4). Bei Haltungs- und Fragen-Post vertretbar.

## Was ich trotzdem so plane und warum
Der Trockenlauf soll die Kette testen, nicht neue Inhalte. Das Material ist von Daniel freigegeben, also ändere ich keine Themen. Ich ändere nur, was seit dem 09.11. entschieden wurde (Uhrzeit, Storys, Formate, LinkedIn) und die Szenen, die gegen die Nachbar-Regel verstoßen.
