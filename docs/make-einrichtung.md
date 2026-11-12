# Make einrichten: Freigabe und Montags-Mail

Zwei Szenarien. Dauer zusammen etwa 15 Minuten. Die Webhook-Adressen sind wie Schlüssel: nicht weitergeben, nicht in Screenshots.

---

## Szenario 1: „flowkraft Freigabe“

Wird von den Knöpfen der Freigabeseite aufgerufen und plant den Post in Zernio ein.

1. In Make: **Create a new scenario**.
2. Erstes Modul: **Webhooks → Custom webhook**. **Add**, Name `flowkraft-freigabe`, **Save**. Die angezeigte Adresse kopieren und in `~/.flowkraft-motion/make.env` als Zeile eintragen:
   `MAKE_APPROVE_URL=` direkt gefolgt von der Adresse.
   Das Modul wartet jetzt auf einen Test-Aufruf („Determine data structure“). Sag mir Bescheid, ich schicke ihn; danach kennt Make die Felder `id`, `zeit`, `aktion`.
3. Zweites Modul: **Router**.
4. **Weg 1 „Freigeben“**: Filter (Schraubenschlüssel auf der Linie): Bedingung `aktion` *Equal to* `ok`, zweite Bedingung `id` *Matches pattern* `^[0-9a-f]{24}$`.
   Modul **HTTP → Make a request**:
   - URL: `https://zernio.com/api/v1/posts/{{1.id}}`
   - Method: `PUT`
   - Headers: `Authorization` = `Bearer ` + dein Zernio-Schlüssel (aus `~/.flowkraft-motion/zernio.env`), `Content-Type` = `application/json`
   - Body type: `Raw`, Content type `JSON (application/json)`
   - Request content:
     ```
     {"isDraft": false, "scheduledFor": "{{1.zeit}}", "timezone": "Europe/Vienna"}
     ```
5. **Weg 2 „Nicht posten“**: Filter `aktion` *Equal to* `stop` und dieselbe `id`-Bedingung.
   Modul **HTTP → Make a request**: URL wie oben, Method `DELETE`, nur der Header `Authorization`. (Löscht nur den Entwurf in Zernio, veröffentlicht ist er ja nicht.)
6. Unten links **Scheduling** auf **Immediately as data arrives**, Szenario **ON**, **Save**.

---

## Szenario 2: „flowkraft Woche bereit“

Wird Montag um 8 Uhr von der Cloud aufgerufen und schickt dir die Mail.

1. **Create a new scenario** → **Webhooks → Custom webhook**, **Add**, Name `flowkraft-woche-bereit`, **Save**. Adresse in `~/.flowkraft-motion/make.env` eintragen:
   `MAKE_NOTIFY_URL=` direkt gefolgt von der Adresse.
   Auch hier schicke ich den Test-Aufruf; danach kennt Make `betreff`, `link`, `hooks`, `offene_einwaende`, `kw`.
2. Zweites Modul: **Gmail → Send an email** (Gmail-Konto verbinden) oder **Email → Send an email**.
   - To: deine Adresse
   - Subject: `{{1.betreff}}`
   - Content (Text):
     ```
     Die Woche ist bereit:
     {{1.link}}

     Die Posts:
     {{1.hooks}}

     {{1.offene_einwaende}}

     Ohne Freigabe geht nichts raus.
     ```
3. Scheduling **Immediately**, Szenario **ON**, **Save**.

---

## Danach

Wenn beide Adressen in `make.env` stehen, schicke ich die Test-Aufrufe und prüfe, ob alles ankommt. Für die Cloud trägst du später dieselben Werte als geschützte Variablen in der Cloud-Umgebung ein.
