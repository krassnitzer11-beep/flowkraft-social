# Szenen

Alle Szenen laufen in Navy, Dunkel und Mist. `Layout` ist das Layout, für das die Szene positioniert ist; mit `dy` und `sceneScale` lässt sie sich anpassen. Alle `props` sind optional.

| Szene | Passt zu | Layout | props (Standard) |
|---|---|---|---|
| `chaos` | Überlastung, viele Anfragen: Nachrichten schießen hoch, Zähler bis 99+, dann Ruhe | top | `a` '@', `aLabel` 'E-Mail', `b` 'WA', `bLabel` 'WhatsApp' |
| `calculator` | Rechnen, ROI, Schritte: Tasten, dann drei Bausteine | bottom | `steps` ['Finden','Umsetzen','Betreuen'] |
| `clock` | Zeit, Zeitfresser: Zeiger rasen, Stück wird gefressen, Münzen | side | `coin` '€' |
| `flowpanel` | Prozess, Workflow: Homepage-Panel mit Kacheln und Linien (2 bis 5 Knoten) | stack | `nodes` [[icon, label], …]; der F-Hub ist immer der zweite Knoten, dort `null` als Icon (an anderer Stelle bricht das Rendern ab); `status` 'Läuft automatisch' |
| `pin` | Regional, persönlich: Pin mit F auf Punktraster | center | `tag` 'Kärnten', `icon` 'user' |
| `comment` | CTA mit Kommentar-Wort: wird getippt, DM kommt zurück | stack | `word`, `title` 'Kurzguide', `sub` 'KMU.DIGITAL' |
| `hourglass` | Zeitverlust als Hook: Sanduhr und Zähler | bottom | `value` 40, `unit` 'h' |
| `yeargrid` | Hochrechnung: 240 Kästchen füllen sich | bottom | `title`, `value`, `unit`, `note` |
| `retype` | Doppelte Arbeit: links steht es, rechts wird es getippt | stack | `left` 'Anfrage', `right` 'System' |
| `calendar` | Termine, Handarbeit: Kalender und drei Mails | center | `items` (3 Texte) |
| `pile` | Unordnung, Suche: Papierstapel, Lupe, Ordner | side | `folder` 'Projekt' |
| `ranking` | Top 3, Vergleich: drei Balken wachsen | stack | `title`, `right`, `bars` [92, 66, 44] |
| `dochub` | Dokument geht an den Agenten; Slide-Feld `chips` nutzen | bottom | keine |
| `beforeafter` | Vorher/Nachher: Aufgaben werden gestrichen | stack | `before` (3), `leftTitle`, `rightTitle` |
| `mailscan` | Eingang erkannt: Umschlag, Scan, Schild | side | `tag` 'Rechnung ✓' |
| `extract` | Daten auslesen: Scan, Felder, Dateiname tippt sich | stack | `fields` (3), `file` |
| `folders` | Ablage, Weitergabe: Dokument fällt in den Ordner | center | `out` 'Buchhaltung' |
| `roiform` | Rechner als CTA: drei Felder, Ergebnis | stack | `title`, `fields` (3), `result` |
| `none` | Reine Textslide | beliebig | keine |

Ist die Headline lang (3 Zeilen und mehr), bei `stack` Szenen mit `dy` nach unten schieben oder `size` senken, und im Kontrollbild prüfen.

## Icons (Namen für `nodes` und `icon`)

mail, chat, crm, bot, calc, invoice, user, send, check, clock, calendar, phone, search, file, folder, zap, database, chart, euro, globe, shield, wrench, home.

Eigenes Icon: SVG-Inhalt im 24er-Raster als String. Fremde Marken nicht als Logo nachzeichnen, sondern Kürzel-Chips wie „WA“ verwenden.
