// Do 26.11. · Reel (Drohnenflug, flight.py Modus split) · Säule 4 Rechnet sich das? · Mist (dunkle Schrift und Icons) · vier Stationen
// Eigenes Icon: Mond (Abendfelder im Kalender). Neue Szene „feierabend“.
window.POST = {
  name: 'kw48-do-abendbuero', theme: 'mist', depth: .04, label: 'RECHNET SICH DAS?',
  slides: [
    { hook: true, first: 'text', layout: 'center', size: 150, outline: 'Deine Abendstunde', title: 'ist nicht', script: 'gratis.',
      scene: 'calendar', props: { items: ['Mo-Abend', 'Mi-Abend', 'Do-Abend'], hot: [5, 12, 18],
        itemIcon: '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/>' }, dy: -40 },
    { layout: 'top', title: '6 Stunden pro', script: 'Woche.', p: 'Angenommen: 3 Abende à 2 Stunden Büro.',
      scene: 'chaos', props: { a: '€', aLabel: 'Belege', b: 'Tel', bLabel: 'Rückrufe', count: false }, dy: 40 },
    { layout: 'bottom', title: '276 Stunden im', script: 'Jahr.', p: 'Beispielrechnung: 6 h × 46 Wochen. Angenommen 60 € pro Stunde: 16.560 €.',
      scene: 'calculator', props: { steps: ['Abendstunden', 'Wochen', 'Stundenwert'] } },
    { layout: 'side', title: 'Rechne deinen', script: 'Feierabend.', p: 'Die Euro sind gedacht. Die Stunden nicht.',
      scene: 'feierabend' },
  ],
};
