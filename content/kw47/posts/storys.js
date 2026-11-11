// Storys Mo–Sa · eine Frage zum Post des Tages · Sticker (Umfrage, Regler, Frage) setzt Daniel in der App
window.POST = {
  name: 'kw47-story', theme: 'navy', label: 'FRAGE',
  slides: [
    { layout: 'center', title: 'Wie viele Mails schreibst du pro', script: 'Termin?', scene: 'calendar', props: { items: ['Bestätigung','Erinnerung','Verschiebung'] } },
    { layout: 'bottom', title: 'Wie viele Angebote schreibst du pro', script: 'Woche?', scene: 'calculator', props: { steps: ['Angebote','× Minuten','= Stunden'] } },
    { layout: 'bottom', title: 'Was würdest du mit 5 Stunden mehr', script: 'machen?', scene: 'hourglass', props: { value: 5, unit: 'h' }, dy: 110 },
    { layout: 'top', title: 'Wie kommen deine Anfragen', script: 'rein?', scene: 'chaos' },
    { layout: 'side', title: 'Wo suchst du am', script: 'längsten?', scene: 'pile', props: { folder: 'Projekt' } },
    { layout: 'center', title: 'Welche Aufgabe würdest du zuerst', script: 'abgeben?', scene: 'none' },
  ],
};
