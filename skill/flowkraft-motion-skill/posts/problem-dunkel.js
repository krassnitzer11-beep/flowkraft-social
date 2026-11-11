// Beispiel-Post: Dunkel · Problem-Karussell.
window.POST = {
  name: 'flowkraft-problem', theme: 'dark', label: 'PROBLEM',
  slides: [
    { hook: true, layout: 'bottom', title: 'Dieser Zeitfresser kostet dich 40', script: 'Stunden.', scene: 'hourglass', props: { value: 40, unit: 'h' } },
    { layout: 'bottom', title: '10 Minuten am Tag abtippen = 40 Stunden im', script: 'Jahr.', p: 'Gerechnet mit 240 Arbeitstagen. Und das ist nur eine Aufgabe von vielen.', scene: 'yeargrid',
      props: { title: '240 Arbeitstage', value: 40, unit: 'Stunden', note: '10 Minuten pro Tag' } },
    { layout: 'stack', num: '01', title: 'Angebote ins System', script: 'tippen.', p: 'Die Daten stehen schon in der Anfrage – sie werden nur noch einmal eingegeben.', scene: 'retype', props: { left: 'Anfrage', right: 'System' } },
    { layout: 'center', num: '02', title: 'Termine per Mail', script: 'bestätigen.', p: 'Jede Bestätigung, jede Erinnerung, jede Verschiebung – von Hand.', scene: 'calendar', props: { items: ['Bestätigung','Erinnerung','Verschiebung'] } },
    { layout: 'side', num: '03', title: 'Rechnungen', script: 'zuordnen.', p: 'Beleg suchen, Projekt finden, ablegen. Jeden Monat wieder.', scene: 'pile', props: { folder: 'Projekt' } },
    { layout: 'stack', title: 'Wo verlierst du die meiste', script: 'Zeit?', p: 'Kommentiere ZEIT und du bekommst den Zeitfresser-Check: deine Top-3-Automationen, gerechnet in Stunden pro Jahr.', cta: 'Kommentiere ZEIT', scene: 'ranking',
      props: { title: 'Zeitfresser-Check', right: 'Stunden pro Jahr', bars: [92, 66, 44] } },
  ],
};
