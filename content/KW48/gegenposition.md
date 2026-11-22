# Gegenposition KW 48 (23.–28.11.2026) · zweiter Testlauf

Geschrieben vom Social-Media-Manager vor dem Plan, nach Teamregel 6. **Fakt**, **Annahme** und **Vermutung** sind gekennzeichnet.

Rahmen (Fakt, CLAUDE.md 17.11.2026): KW 48 ist der zweite Testlauf. Es entstehen nur Entwürfe, nichts wird gepostet, „flowkraft Freigabe“ bleibt aus. Geprüft werden Ampel, „Was nicht passt“, Kennzahlen, langsame Reels (Faktor 1,6), Mist mit dunkler Schrift und Abwechslung. Anders als KW 47 entsteht diese Woche **neues Material**: Kein Thema aus KW 47 oder der Probewoche darf wiederkommen.

Grundlagen: `CLAUDE.md`, `WOCHE.md`, `tools/woche/PLAN.md`, `docs/flowkraft-voice.md`, `docs/flowkraft-team-regeln.md`, `docs/prompt-social-post.md`, `content/analysen/KW47.md`, Branch `origin/claude/woche-KW47` (plan, gegenposition, pruefbericht, texte), Probewoche `content/kw47/`. Ein Branch `claude/woche-KW46` existiert nicht (Fakt, `git branch -a`).

## Der Plan in einer Zeile pro Tag

| Tag | Format | Säule | Thema | Einwand | Rechen-Post |
|---|---|---|---|---|---|
| Mo 23.11. | Reel (Drohnenflug) | 1 Zeitfresser | Zahlungserinnerungen: offenen Rechnungen hinterherlaufen | – | ja (1 von 2) |
| Di 24.11. | Karussell | 3 Haltung | Automatisieren ohne IT-Abteilung | „Nur was für große Firmen“ | nein |
| Mi 25.11. | Post (Standbild) | 2 Vorher/Nachher | Stundenzettel vom Zettel abtippen | – | nein |
| Do 26.11. | Reel (Drohnenflug) | 4 Rechnet sich das? | Abendbüro: was deine eigene Stunde kostet | (berührt „zu teuer“, siehe Punkt 6) | ja (2 von 2) |
| Fr 27.11. | Post (Standbild) | 3 Haltung | Das Team entscheidet mit | „Meine Leute machen da nicht mit“ | nein |
| Sa 28.11. | Karussell | 5 Praxisbeispiel | Musterprojekt Fehlerwächter | – | nein |

LinkedIn: Di Video 4:5 aus dem **Mo-Reel** (Zahlungserinnerungen), Do Standbild 4:5 aus dem **Mi-Post** (Stundenzettel). Beide 18:00. Die LinkedIn-Texte stehen in `texte.md` in den Abschnitten „Di 24.11.“ bzw. „Do 26.11.“ (dort liest `drafts.py` sie). `build.py` liefert `linkedin_video` nur für Reels und `linkedin_bild` nur für Posts: Mo ist ein Reel, Mi ist ein Post (Fakt, `tools/woche/build.py` Zeilen 33–55).

## Warum kein Thema doppelt ist

### Gegen die letzten 4 Wochen
**Fakt:** Es gibt nur zwei Quellen: KW 47 (`origin/claude/woche-KW47`) und die Probewoche (`content/kw47/`, gleiche Themen). KW 46 hatte nur Testposts mit denselben Texten (Analyse KW 46). Belegte Themen der letzten 4 Wochen:

| Altes Thema | Neues Thema, das am nächsten dran ist | Warum es nicht dasselbe ist |
|---|---|---|
| Termine / Termin-Mails (Mo) | – | kein Termin, keine Kalender-Mails in KW 48. Do „Abendbüro“ darf keine Termin-Mails als Beispiel nennen. |
| Angebote abtippen (Di) | Mo Zahlungserinnerungen | anderer Schritt im Ablauf: nicht das Angebot vor dem Auftrag, sondern das Geld nach der Rechnung. Copy darf Angebote nicht erwähnen. |
| Excel / „Leute beim Kunden, nicht in Excel“, Haltung „Automatisieren ersetzt niemanden“ (Mi) | Fr Team entscheidet mit | KW 47 sagte: *Die Arbeit wird deinen Leuten abgenommen.* Fr sagt: *Deine Leute bestimmen, womit angefangen wird, und prüfen mit.* Das ist Mitsprache und Einführung, nicht Entlastung. **Annahme:** Der Unterschied ist für den Leser sichtbar, solange Fr weder „ersetzen“ noch „Excel“ noch „Arbeit, die keiner gern macht“ verwendet. Prüfer bitte genau darauf achten. |
| Anfragen abtippen, Vorher/Nachher (Do) | Mi Stundenzettel | anderer Beleg (Arbeitszeiten der eigenen Leute statt Kundenanfragen), andere Richtung (intern statt von außen). Gemeinsam ist nur das Wort „abtippen“; Copy soll im Hook ein anderes Verb nehmen. |
| Datei suchen / Ablage (Fr) | Sa Fehlerwächter | Fehlerwächter meldet, wenn ein Ablauf hängen bleibt. Es geht nicht ums Finden. Das Beispiel im Karussell darf keine Ablage oder Dateisuche sein. |
| „Drei Fragen“ / Wann lohnt es sich nicht (Sa) | Do Abendbüro, Di Grenze | Do rechnet den Wert der eigenen Stunde, keine Checkliste „oft, gleich, ungeliebt“. Die ehrliche Grenze in Di ist eine andere: „Wenn jeder es jedes Mal anders macht, erst den Ablauf einmal festlegen.“ Die Formel „oft, gleich, ungeliebt“ und die Faustregel „3 im Monat: lass es“ sind diese Woche tabu. |

Säule-5-Auswahl: Von den fünf Use Cases in voice.md Abschnitt 10 kollidieren vier mit alten Themen: Kundenservice-Agent und Sales-Agent mit **Anfragen**, Wissenssystem mit **Suchen**, Meetingvorbereitung mit **Termine** und **Suchen**. Nur der **Fehlerwächter** ist frei. **Fakt:** Er war für die Probewoche schon vorgesehen und wurde ersetzt, weil Details fehlten (`content/kw47/pruefbericht.md` Zeile 35). Er war nie in einem Plan und nie öffentlich, zählt also nicht als Thema der letzten 4 Wochen.

### Innerhalb der Woche
Die sechs Themen haben jeweils einen anderen Gegenstand (Geld eintreiben, Projektgröße, Arbeitszeit erfassen, eigener Stundenwert, Mitsprache des Teams, Überwachung von Abläufen). Drei Paare liegen nah beieinander und sind deshalb abgegrenzt:
- **Di „ohne IT-Abteilung“ und Do „Abendbüro“:** Beide sprechen den Inhaber an. Di handelt von der *Größe des Vorhabens* (ein Ablauf, vorhandene Programme bleiben, kein eigener Server, keine IT-Leute). Do handelt vom *Preis der eigenen Zeit*. Di darf nicht mit „du machst das Büro selbst am Abend“ argumentieren, Do nicht mit „auch kleine Betriebe können das“.
- **Di „ohne IT-Abteilung“ und Fr „Team entscheidet mit“:** beide Einwände. Di beantwortet „passt das zu meinem Betrieb“, Fr „ziehen meine Leute mit“. Fr darf nicht „klein anfangen“ als Kernaussage nehmen, das gehört Di.
- **Fr „Team“ und Sa „Fehlerwächter“:** Beide berühren Vertrauen. Fr: Menschen entscheiden und prüfen. Sa: ein System meldet sich, wenn etwas nicht läuft. Sa darf das Team nicht zum Thema machen, nur „die richtige Person bekommt die Meldung“.

## Warum diese Woche scheitern könnte

### 1. Säule 5 hat keine freigegebene Grundlage (größtes inhaltliches Risiko)
- **Fakt:** `docs/praxisbeispiele.md` existiert nicht. Der Agent `recherche` darf laut `.claude/agents/recherche.md` Praxisbeispiele nur aus dieser Datei nehmen, „sonst keins“. Voice.md Abschnitt 10 und CLAUDE.md erlauben dagegen die fünf Use Cases aus Daniels Weiterbildung ausdrücklich.
- **Entscheidung:** CLAUDE.md und Voice gehen der Agentendatei vor. Der Fehlerwächter läuft als **neutraler Beispielablauf**: Was beobachtet er, wann meldet er sich, wer bekommt die Meldung, was entscheidet ein Mensch. Keine Zahlen, keine Testwerte, kein „im Einsatz bei“, keine Technik-Namen ohne Erklärung.
- **Vermutung:** Ohne Details aus der Weiterbildung bleibt das Karussell allgemein. Genau daran ist der Fehlerwächter schon einmal gescheitert.
- **Rückfall, falls Recherche oder Prüfer blockieren:** Sa wird ein Karussell Säule 2 Vorher/Nachher zum Thema „Urlaubsvertretung: wer weiß, wie das geht?“ (kein altes Thema). Dann hat Säule 5 zwei Wochen null Posts. Das schreibe ich offen in den Prüfbericht.
- **Für Daniel:** `docs/praxisbeispiele.md` mit ein bis zwei freigegebenen Musterprojekten anlegen. Ohne diese Datei wird Säule 5 jede zweite Woche wackeln.

### 2. Szenen reichen nicht für „jede Szene höchstens einmal pro Woche“
- **Fakt:** Die Engine hat 18 Szenen plus `none` (`references/scenes.md`). `roiform` (sieht nach ROI-Rechner aus, der nicht live ist) und `comment` (Kommentar-Keyword, keines ist live) fallen aus. Bleiben 16.
- **Fakt:** Die Feed-Posts brauchen rund 20 Szenen (Reels je 4, Karussells je 6, Posts je 1, abzüglich je einer `none`-Slide in den Karussells). Dazu 6 Storys.
- **Entscheidung:** Der Designer baut mindestens **drei neue Szenen** (Vorschläge: `feierabend` für Do, `team` für Fr, `waechter` für Sa). Damit kommt im Feed jede Szene genau einmal vor. Für die **Storys** gilt: keine Szene, die im Post desselben Tags, des Vortags oder des Folgetags steht. Eine Story darf also eine Szene wiederholen, die mindestens zwei Tage entfernt im Feed steht. Das ist eine Lockerung der CLAUDE.md-Regel für Storys; ich nehme sie bewusst in Kauf, statt sechs weitere Szenen in einem Testlauf zu bauen, und lege sie im Prüfbericht als offenen Punkt für Daniel vor.
- **Szenen-Vorschlag (der Designer darf tauschen, solange die Regeln halten):**

| Tag | Szenen im Feed |
|---|---|
| Mo Reel | `hourglass`, `mailscan` (Tag „Bezahlt ✓“), `yeargrid`, `flowpanel` |
| Di Karussell | `pin` (Tag z. B. „1–50 Leute“), `clock`, `beforeafter`, `dochub`, `ranking`, `none` |
| Mi Post | `retype` (links „Zettel“, rechts „Stunden“) |
| Do Reel | `calendar` (Abend/Wochenende, ohne Termin-Mails), `chaos`, `calculator`, **neu** `feierabend` |
| Fr Post | **neu** `team` |
| Sa Karussell | **neu** `waechter`, `pile`, `extract`, `folders`, `none`; eine sechste Slide entweder zweite `none` oder eine vierte neue Szene (alle 16 alten Szenen sind dann vergeben) |

- **Nachbar-Check:** Keine Szene steht in zwei benachbarten Posts. Mi `retype` und Do bleiben getrennt, Mo und Di teilen nichts. Achtung: `yeargrid` zeigt fest 240 Kästchen (Prüfbericht KW 47); wenn Mo mit 44 Wochen oder 220 Tagen rechnet, Bild und Zahl nicht vermischen oder Szene tauschen.
- **Icons:** jedes Icon höchstens einmal pro Woche und neu gestaltet (CLAUDE.md 16.11.2026). Das betrifft vor allem `flowpanel`-Knoten und die Chips.

### 3. Zwei Rechen-Reels und beide als Drohnenflug
- **Fakt:** Mo und Do sind die zwei erlaubten Rechen-Posts. Beide sind Reels. Die übrigen vier Posts rechnen nicht nach dem Muster Aufgabe × Minuten × Jahr.
- **Risiko:** Zwei Reels mit Rechnung in einer Woche wirken wie ein Baukasten (Einwand 2 aus dem KW-47-Prüfbericht). **Gegenmaßnahme:** Mo rechnet in Stunden (Zeit für Erinnerungen), Do rechnet in Euro (Wert der eigenen Stunde) und endet auf „Feierabend“. Zahlen dürfen sich nicht mit KW 47 decken (keine 132 h, 220 h, 73 h, 9.900 €, kein Stundensatz 45 €), sonst sieht es nach Vorlage aus.
- **Annahme:** Ein Stundensatz für die eigene Stunde des Inhabers ist eine Annahme, keine Quelle. Er steht sichtbar als „angenommen“ im Reel, nicht nur in der Caption, weil die LinkedIn-Fassung keine Caption zeigt. Kein Preis für flowkraft, kein „Automatisierung kostet X“.
- **Technik (Fakt):** Zwei Drohnenflüge sind der teuerste Teil beim Rendern (1,5–2 h in der Cloud). Mit Faktor 1,6 werden die Reels länger. Bei 4 Szenen bleiben sie kurz genug; mehr als 5 Szenen pro Reel nicht.

### 4. Zahlungserinnerungen sind heikel im Ton
- **Annahme:** Inhaber erinnern ungern an offene Rechnungen, weil sie Kunden nicht verärgern wollen. Eine automatische Erinnerung kann als unpersönlich gelten.
- **Folge:** Das Reel darf nicht „Mahnungen laufen von selbst raus“ versprechen. Die ehrliche Grenze: Die Erinnerung ist vorbereitet, raus geht sie, wenn du oder jemand aus dem Team sie bestätigt. Rechtliches (Mahngebühren, Verzugszinsen, Fristen in AT/DE/CH) gar nicht ansprechen, das ist nicht belegt und je Land anders.

### 5. Drei Posts für Betriebe mit Team, aber die Zielgruppe beginnt bei 1 Person
- **Fakt:** Voice.md 2: „deine Leute“ passt nicht für Ein-Personen-Betriebe.
- **Risiko:** Mi (Stundenzettel) und Fr (Team) setzen Mitarbeiter voraus. Das ist bei diesen Themen nicht zu vermeiden. Dafür müssen Mo, Di, Do und Sa ohne Team funktionieren. Di sagt ausdrücklich „auch wenn du allein bist“. Mi braucht im Text einen Satz, der auch den Einzelnen meint (eigene Stunden für die Abrechnung beim Kunden), sonst lieber so lassen und hinnehmen.

### 6. „Zu teuer“ fehlt als ausdrücklicher Einwand
- **Entscheidung:** Diese Woche greifen zwei Posts einen Einwand ausdrücklich auf (Di, Fr). „Zu teuer“ hebe ich für KW 49 auf. Grund: Bei der Regel „kein Thema aus den letzten 4 Wochen“ sind drei Einwände schnell verbraucht, wenn jede Woche alle drei kommen. Do berührt „zu teuer“ von der anderen Seite (was kostet es, nichts zu ändern), nennt den Einwand aber nicht.
- **Risiko:** Ohne flowkraft-Preise (die es nicht geben darf, solange keine freigegeben sind) bleibt jede Antwort auf „zu teuer“ halb. Das gilt auch für KW 49. Daniel sollte entscheiden, ob er eine Preisspanne oder ein Förderprogramm (KMU.DIGITAL, nur Österreich, nur aus offizieller Quelle) freigibt.

### 7. Kein Weg zum Lead, wieder
- **Fakt:** `docs/lead-magnete.md` existiert nicht, voice.md 9 führt ROI-Check und KI-Check als „nicht live“. Also kein Keyword, kein „Link in Bio“, kein flowkraft.at-Link. Jeder Post endet mit genau einem Schritt: folgen, speichern oder teilen.
- **Folge:** Selbst als echte Woche brächte KW 48 höchstens Follower, keinen Lead. Für den Testlauf egal, für das Ziel 60 Leads bis 30.06.2027 nicht.

### 8. Messen geht diese Woche nicht
- **Fakt:** Analyse KW 47: keine veröffentlichten Posts, keine Kennzahlen, LinkedIn 2 Follower, Facebook 0, Instagram nicht verbunden.
- **Folge:** Der Plan stützt sich auf keine einzige Zahl aus echten Posts. Formatwahl, Säulen und Uhrzeit sind Daniels Vorgaben, nicht Ergebnisse. Der Kennzahlen-Block in Mail und Freigabeseite muss „keine Daten“ ehrlich zeigen, nicht leere Tabellen mit Nullen, die nach Ergebnis aussehen.

### 9. Säulen über zwei Wochen
- **Fakt:** KW 47: Säule 1 ×2, 2 ×1, 3 ×1, 4 ×2, 5 ×0. KW 48: 1 ×1, 2 ×1, 3 ×2, 4 ×1, 5 ×1. Zusammen: 1 ×3, 2 ×2, 3 ×3, 4 ×3, 5 ×1.
- **Annahme:** Der Fahrplan liegt nicht im Repository; „nah am Fahrplan“ ist an gleichmäßiger Verteilung und an der Samstagsregel gemessen. Säule 5 bleibt dünn, weil sie laut Daniel nur jeden zweiten Samstag kommt. Säule 3 hat diese Woche zwei Posts, weil beide Einwand-Posts dort am besten passen. Säule 2 ist mit Mi nur als Standbild vertreten; ein Vorher/Nachher im Standbild ist schwerer als im Reel.

### 10. Einwand-Posts können belehrend wirken
- **Vermutung:** Bei 0 Followern liest niemand „Du denkst, das ist nur für Große?“ als Gespräch, sondern als Werbung, die Einwände wegredet.
- **Gegenmaßnahme:** Der Einwand wird nicht zitiert und widerlegt, sondern ernst genommen und mit einer echten Grenze beantwortet. Di nennt, wann es auch im kleinen Betrieb nicht passt. Fr gibt dem Leser recht: Wenn die Leute nicht gefragt werden, machen sie zu Recht nicht mit.

### 11. Technik und Testziele
- **Fakt:** Testziele laut CLAUDE.md: Ampel, „Was nicht passt“, Kennzahlen, langsame Reels, Mist mit dunkler Schrift, Abwechslung. Damit Mist getestet wird, braucht mindestens ein Reel die Variante `mist` (Vorschlag: Do). Mo bleibt `dark`, Karussells `navy` bzw. `dark`, Standbilder abwechselnd. Der Designer setzt die Variante pro Post.
- **Ungetestet (Vermutung):** Das LinkedIn-Di-Video sind die Reel-Slides als 4:5-Videos hintereinander, kein Drohnenflug (Entscheidung 17.11.2026). Für die 4:5-Fassung gab es in KW 47 kein Kontrollbild. Designer prüft diesmal ein Kontrollbild der 4:5-Fassung.
- **Wichtig:** „flowkraft Freigabe“ bleibt aus. Klicks auf der Freigabeseite sammeln sich in der Make-Warteschlange und müssen vor dem Einschalten gelöscht werden.

## Was ich trotzdem so plane und warum
Die Woche testet die Abwechslung mit echtem neuem Material. Sechs Themen, die sich gegen KW 47 und gegeneinander abgrenzen lassen, zwei Einwände, zwei Rechnungen, ein Praxisbeispiel am Samstag. Die größten Lücken (Säule-5-Material, fehlende Szenen, kein Lead) liegen nicht am Plan, sondern an fehlenden Freigaben. Sie stehen hier, damit sie im Prüfbericht nicht verschwinden.

---

## Aufträge pro Post (für recherche, copywriter, designer)

Für alle: Du-Ansprache (auch LinkedIn), DACH-Raum, keine erfundenen Zahlen/Preise/Kunden, Beispielrechnungen kennzeichnen, Annahmen sichtbar, Hook höchstens 7 Wörter mit starkem Schlusswort, genau ein nächster Schritt (folgen, speichern oder teilen), kein ROI, kein KI-Check, kein Link. Storys: Frage als Text, Antwort per DM, keine Sticker, keine Antwortoptionen. Die tabu-Formulierungen aus „Warum kein Thema doppelt ist“ beachten.

### Mo 23.11. · Reel · Säule 1 · Zahlungserinnerungen
- **Schmerzpunkt:** Rechnung ist raus, Geld nicht da. Wer schaut nach, wer erinnert, wann? Meist der Inhaber, nebenbei, mit schlechtem Gefühl.
- **Winkel:** Nicht das Erinnern kostet Zeit, sondern das Nachschauen, ob bezahlt ist. Beispielrechnung in Stunden pro Jahr (Annahmen: Zahl offener Rechnungen pro Monat, Minuten pro Prüfung und Erinnerung). Lösung: Zahlungseingang wird abgeglichen, die Erinnerung liegt vorbereitet bereit, du bestätigst.
- **Einwand:** keiner. **Grenze:** Ton beim Kunden bleibt Sache des Menschen; nichts zu Mahngebühren oder Recht.
- **Recherche:** wenn möglich eine belegte Zahl zu Zahlungsverzug bei KMU im DACH-Raum (mit Link). Sonst nur Beispielrechnung.
- **Schritt:** speichern. **LinkedIn Di:** eigener, sachlicherer Text über dieses Reel, im Abschnitt „Di 24.11.“, Du, höchstens 3 Hashtags, kein Link.

### Di 24.11. · Karussell (6–8 Slides) · Säule 3 · Ohne IT-Abteilung
- **Schmerzpunkt:** „Automatisierung ist was für Konzerne mit IT-Abteilung.“
- **Winkel:** Ein Ablauf, nicht das ganze Büro. Die Programme, die du schon hast (Mail, Kalender, Tabelle, Buchhaltungsprogramm), bleiben. Kein eigener Server, keine IT-Leute. Gilt ab 1 Person.
- **Einwand:** „Das ist nur was für große Firmen.“ Ernst nehmen, nicht wegreden.
- **Ehrliche Grenze:** Wenn jeder den Ablauf jedes Mal anders macht, zuerst einmal festlegen, wie es laufen soll. (Nicht die alte Formel „oft, gleich, ungeliebt“.)
- **Keine Rechnung** auf diesem Post. **Schritt:** teilen (mit jemandem, der das auch glaubt) oder folgen; genau einer.

### Mi 25.11. · Post (Standbild) · Säule 2 · Stundenzettel
- **Schmerzpunkt:** Am Monatsende liegen Zettel mit Arbeitszeiten am Schreibtisch, unleserlich, unvollständig, und jemand tippt sie für Lohn oder Abrechnung ab.
- **Winkel:** Vorher/Nachher in einem Satz, ohne Erklärung verständlich, teilbar. Im Hook nicht „abtippen“ verwenden (das war KW 47 Anfragen).
- **Einwand:** keiner. Keine Rechnung. Ein Satz in der Caption auch für Einzelunternehmer (eigene Stunden für die Kundenabrechnung).
- **Hinweis Recht:** Arbeitszeitaufzeichnung ist in AT/DE/CH gesetzlich unterschiedlich geregelt. Nichts dazu behaupten, außer die Recherche liefert eine offizielle Quelle; im Zweifel weglassen.
- **Schritt:** teilen. **Bild:** `clean: true`. Dieses Bild ist auch das **LinkedIn-Standbild am Do**: Text im Abschnitt „Do 26.11.“.

### Do 26.11. · Reel · Säule 4 · Abendbüro
- **Schmerzpunkt:** Der Tag gehört den Kunden, das Büro dem Abend. Die Stunde am Schreibtisch nach 19 Uhr wird nicht als Kosten gesehen.
- **Winkel:** Rechne deine eigene Stunde wie eine Kundenstunde. Beispielrechnung mit sichtbaren Annahmen (Stunden pro Woche am Abend, angenommener Wert der eigenen Stunde, Arbeitswochen). Ergebnis in Euro **und** Feierabend. Keine flowkraft-Preise, kein „lohnt sich in X Wochen“.
- **Einwand:** nicht ausdrücklich; berührt „zu teuer“ von der Gegenseite. Nicht mit „auch für Kleine“ argumentieren (gehört Di). Keine Termin-Mails, keine Angebote als Beispiel.
- **Design:** Variante `mist` (Testziel dunkle Schrift). Annahmen im Bild, nicht nur in der Caption.
- **Schritt:** speichern.

### Fr 27.11. · Post (Standbild) · Säule 3 · Team entscheidet mit
- **Schmerzpunkt:** „Meine Leute machen da nicht mit.“ Oft stimmt das, wenn die Einführung über ihre Köpfe hinweg passiert.
- **Winkel:** Deine Leute sagen, was zuerst entlastet wird, und prüfen, bevor etwas rausgeht. Ein Satz, der hängen bleibt. Nicht: „ersetzt niemanden“, „Excel“, „Arbeit, die keiner gern macht“, „klein anfangen“.
- **Einwand:** „Meine Leute machen da nicht mit.“ Recht geben, dann Weg zeigen.
- **Keine Rechnung.** **Schritt:** teilen. **Bild:** `clean: true`, neue Szene `team`.

### Sa 28.11. · Karussell (6–8 Slides) · Säule 5 · Fehlerwächter
- **Schmerzpunkt:** Läuft etwas automatisch, merkt niemand, wenn es stehen bleibt. Das ist die Sorge hinter „Was, wenn's schiefgeht?“
- **Winkel:** Musterprojekt aus der Weiterbildung, als Beispielablauf: Ein Wächter schaut, ob jeder Schritt angekommen ist, meldet sich bei der zuständigen Person mit dem, was fehlt, und ein Mensch entscheidet. Beispiel neutral wählen: keine Rechnungen/Zahlungen (Mo), keine Anfragen, keine Ablage/Suche, keine Termine.
- **Belegpflicht:** keine Zahlen, keine Testwerte, keine Kunden, kein „im Einsatz bei“. Satz in Caption oder Slide: „Musterprojekt, kein Kundenprojekt.“
- **Ehrliche Grenze:** Ein Wächter meldet Fehler, er verhindert sie nicht.
- **Rückfall:** siehe Punkt 1 (Vorher/Nachher „Urlaubsvertretung“).
- **Schritt:** folgen (für das nächste Praxisbeispiel).

### Storys 1–6 (`posts/storys.js`)
Je eine offene Frage zum Post des Tages als Text, Antwort per DM. Keine Szene aus dem Post desselben Tags, des Vortags oder Folgetags. Story 6 nicht leer (KW-47-Einwand: obere Hälfte leer).
