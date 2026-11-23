# Szenen

Alle Szenen laufen in Navy, Dunkel und Mist. `Layout` ist das Layout, für das die Szene positioniert ist; mit `dy` und `sceneScale` lässt sie sich anpassen. Alle `props` sind optional.

| Szene | Passt zu | Layout | props (Standard) |
|---|---|---|---|
| `chaos` | Überlastung, viele Anfragen: Nachrichten schießen hoch, Zähler bis 99+, dann Ruhe | top | `a` '@', `aLabel` 'E-Mail', `b` 'WA', `bLabel` 'WhatsApp', `count` (false = ohne Zähler, nur Haken) |
| `calculator` | Rechnen, ROI, Schritte: Tasten, dann drei Bausteine | bottom | `steps` ['Finden','Umsetzen','Betreuen'] |
| `clock` | Zeit, Zeitfresser: Zeiger rasen, Stück wird gefressen, Münzen | side | `coin` '€' |
| `flowpanel` | Prozess, Workflow: Homepage-Panel mit Kacheln und Linien (2 bis 5 Knoten) | stack | `nodes` [[icon, label], …]; der F-Hub ist immer der zweite Knoten, dort `null` als Icon (an anderer Stelle bricht das Rendern ab); `status` 'Läuft automatisch' |
| `pin` | Regional, persönlich: Pin mit F auf Punktraster | center | `tag` 'Kärnten', `icon` 'user' |
| `comment` | CTA mit Kommentar-Wort: wird getippt, DM kommt zurück (auch: Weiterleiten) | stack | `word`, `title` 'Kurzguide', `sub` 'KMU.DIGITAL', `icon` 'invoice' |
| `hourglass` | Zeitverlust als Hook: Sanduhr und Zähler | bottom | `value` 40, `unit` 'h', `text` (statt Zähler, z. B. 'Offen') |
| `yeargrid` | Hochrechnung: 240 Kästchen füllen sich | bottom | `title`, `value`, `unit`, `note`; `split` (Anteil Farbe 1, Rest Farbe 2) + `legend` [2 Texte] |
| `retype` | Doppelte Arbeit: links steht es, rechts wird es getippt | stack | `left` 'Anfrage', `right` 'System', `messy` (links schief/verwischt), `checks` (rechts Haken) |
| `calendar` | Termine, Handarbeit: Kalender und drei Mails | center | `items` (3 Texte), `itemIcon` 'mail', `hot` [6,12,17] (Felder 0–19) |
| `pile` | Unordnung, Suche: Papierstapel, Lupe, Ordner | side | `folder` 'Projekt' |
| `ranking` | Top 3, Vergleich: drei Balken wachsen | stack | `title`, `right`, `bars` [92, 66, 44] |
| `dochub` | Dokument geht an den Agenten; Slide-Feld `chips` nutzen (bis 4) | bottom | keine |
| `beforeafter` | Vorher/Nachher: Aufgaben werden gestrichen | stack | `before` (3), `leftTitle`, `rightTitle` |
| `mailscan` | Eingang erkannt: Umschlag, Scan, Schild | side | `tag` 'Rechnung ✓', `scans` 1 |
| `extract` | Daten auslesen: Scan, Felder, Dateiname tippt sich | stack | `fields` (3), `file` |
| `folders` | Ablage, Weitergabe: Dokument fällt in den Ordner | center | `out` 'Buchhaltung' |
| `roiform` | Rechner als CTA: drei Felder, Ergebnis; mit `value` auch als Formular ohne Euro (z. B. Meldung) | stack | `title`, `fields` (3), `result`, `value` |
| `feierabend` (KW 48) | Abendbüro, Feierabend: Schreibtischlampe brennt, Uhr läuft; Ball hält die Uhr an, Schalter macht das Licht aus | side | keine |
| `team` (KW 48) | Mitsprache, Team: sechs Figuren am Tisch, Zettel kommt in die Mitte, Linien zu allen, Haken | bottom | `icon` (Figur), `seats` [[x,y], …] |
| `waechter` (KW 48) | Überwachung, Stillstand: Ablauf-Linie, ein Punkt bleibt grau, Auge öffnet sich und schaut hin | top | `steps` 5, `gap` 3 (Index des grauen Punkts) |
| `zuerst` (KW 48) | Wer erfährt es zuerst: Zeitachse, Meldung mit Glocke kommt bei dir an, zweite Station bleibt leer/gestrichen | stack | `a` 'Du', `b` 'Kunde', `icon` (Glocke) |
| `none` | Reine Textslide | beliebig | keine |

Ist die Headline lang (3 Zeilen und mehr), bei `stack` Szenen mit `dy` nach unten schieben oder `size` senken, und im Kontrollbild prüfen.

## Icons (Namen für `nodes` und `icon`)

mail, chat, crm, bot, calc, invoice, user, send, check, clock, calendar, phone, search, file, folder, zap, database, chart, euro, globe, shield, wrench, home.

Eigenes Icon: SVG-Inhalt im 24er-Raster als String. Fremde Marken nicht als Logo nachzeichnen, sondern Kürzel-Chips wie „WA“ verwenden.
