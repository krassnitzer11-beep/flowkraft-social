// Mo 23.11. · Reel (Drohnenflug, flight.py Modus split) · Säule 1 Zeitfresser · Dunkel · vier Stationen
// Eigene Icons: Bank (Zahlungseingang), Rechnung mit Euro (Bezahlt ✓)
window.POST = {
  name: 'kw48-mo-zahlungserinnerungen', theme: 'dark', depth: .04, label: 'ZEITFRESSER',
  slides: [
    { hook: true, first: 'text', layout: 'bottom', size: 150, outline: 'Rechnung ist raus.', title: 'Das Geld', script: 'nicht.',
      scene: 'hourglass', props: { text: 'Offen' }, dy: 60 },
    { layout: 'side', title: 'Zweimal nachschauen. Pro', script: 'Rechnung.', p: 'Angenommen: 30 Rechnungen im Monat, je 3 Minuten.',
      scene: 'mailscan', props: { tag: 'Bezahlt?', scans: 2 }, sceneScale: .9, dy: -40 },
    { layout: 'bottom', title: 'Macht 51 Stunden im', script: 'Jahr.', p: 'Beispielrechnung, dazu 5 Erinnerungen à 15 Minuten im Monat.',
      scene: 'yeargrid', props: { title: '12 Monate', value: 51, unit: 'Stunden', split: 180/255, legend: ['Nachschauen', 'Erinnern'] } },
    { layout: 'stack', title: 'Die Erinnerung liegt bereit. Du gibst sie', script: 'frei.', p: 'Der Zahlungseingang wird abgeglichen.',
      scene: 'flowpanel', props: { status: 'Erinnerung wartet auf dich', nodes: [
        ['<path d="M3 10 12 4l9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8"/><path d="M3 20h18"/>', 'Zahlungseingang'],
        [null, 'flowkraft'],
        ['<path d="M6 3h9l4 4v14H6Z"/><path d="M15 3v4h4"/><path d="M15 11.6a3 3 0 1 0 0 4.3M9.5 13h4.5M9.5 14.7h4"/>', 'Bezahlt ✓'] ] } },
  ],
};
