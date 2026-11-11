// Fr 20.11. · Karussell · Säule 1 Zeitfresser · Dunkel
window.POST = {
  name: 'kw47-fr-suchen', theme: 'dark', label: 'ZEITFRESSER',
  slides: [
    { hook: true, layout: 'side', title: 'Wo war nochmal die', script: 'Datei?', scene: 'pile', props: { folder: 'Projekt' }, dy: -150, sceneScale: 0.8 },
    { layout: 'top', title: 'Mail, Ordner, WhatsApp,', script: 'Zettel.', p: 'Die Info gibt es. Nur nicht dort, wo du gerade suchst.', scene: 'chaos' },
    { layout: 'bottom', num: '80', title: 'Stunden im Jahr nur fürs', script: 'Suchen.', p: 'Beispielrechnung: 20 Minuten pro Tag × 240 Arbeitstage. Pro Person.', scene: 'yeargrid',
      props: { title: '240 Arbeitstage', value: 80, unit: 'Stunden', note: '20 Minuten pro Tag' } },
    { layout: 'stack', num: '01', title: 'Alles landet an einem', script: 'Ort.', p: 'Anhänge und Nachrichten werden automatisch dem richtigen Projekt zugeordnet.', scene: 'flowpanel',
      props: { nodes: [['mail','Mail und WA'], [null,'Ablage'], ['folder','Projekt']], status: 'Ordnet automatisch' } },
    { layout: 'bottom', num: '02', title: 'Und du findest es mit einer', script: 'Frage.', p: 'Statt Ordner durchzuklicken: „Was hat der Kunde zum Termin geschrieben?“', chips: ['Frage','Agent','Antwort'], scene: 'dochub', dy: 90 },
    { layout: 'center', title: 'Wie viele Minuten sind es bei', script: 'dir?', p: 'Speichere die Rechnung und setz deine Zahl ein: Minuten pro Tag × 240 Arbeitstage.', cta: 'Speichern', scene: 'none' },
  ],
};
