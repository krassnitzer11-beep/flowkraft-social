// Mo 16.11. · Reel · Säule 1 Zeitfresser · Dunkel · eine Geschichte in vier Sätzen
window.POST = {
  name: 'kw47-mo-termine-flug', theme: 'dark', label: 'ZEITFRESSER', flight: true,
  slides: [
    { hook: true, layout: 'center', outline: 'Ein Termin.', title: 'Drei Mails. Jedes', script: 'Mal.', scene: 'calendar', props: { items: ['Bestätigung','Erinnerung','Verschiebung'] } },
    { layout: 'bottom', title: 'Bei 30 Terminen die Woche sind das 3', script: 'Stunden.', p: 'Beispielrechnung: 2 Minuten pro Mail.', scene: 'hourglass', props: { value: 3, unit: 'h' }, dy: 110 },
    { layout: 'side', title: 'Aufs Jahr gerechnet: 132', script: 'Stunden.', scene: 'clock', props: { coin: '€' }, sceneScale: 0.82 },
    { layout: 'stack', title: 'Oder es läuft ab jetzt von', script: 'selbst.', scene: 'flowpanel',
      props: { nodes: [['calendar','Buchung'], [null,'flowkraft'], ['mail','Bestätigung'], ['clock','Erinnerung']], status: 'Läuft automatisch' } },
  ],
};
