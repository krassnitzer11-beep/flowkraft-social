// Storys Mo–Sa · eine Frage zum Post des Tages, Antwort per DM
window.POST = {
  name: 'kw47-story', theme: 'navy', label: 'FRAGE',
  slides: [
    { layout: 'top', title: 'Wie viele Mails schreibst du pro', script: 'Termin?', p: 'Schreib mir deine Zahl per DM.', scene: 'chaos',
      props: { a: '@', aLabel: 'Bestätigung', b: '@', bLabel: 'Erinnerung' } },
    { layout: 'center', title: 'Wie viele Angebote schreibst du pro', script: 'Woche?', p: 'Schreib mir deine Zahl per DM.', scene: 'calendar', props: { items: ['1. Angebot','2. Angebot','3. Angebot'] } },
    { layout: 'bottom', title: 'Was würdest du mit 5 Stunden mehr', script: 'machen?', p: 'Schreib mir per DM.', scene: 'hourglass', props: { value: 5, unit: 'h' }, dy: 110 },
    { layout: 'center', title: 'Wie kommen deine Anfragen', script: 'rein?', p: 'Schreib mir per DM, wo sie bei dir landen.', scene: 'pin', props: { tag: 'Bei dir?', icon: 'mail' } },
    { layout: 'bottom', title: 'Wo suchst du am', script: 'längsten?', p: 'Schreib mir deine Antwort per DM.', scene: 'folders', props: { out: 'Gefunden?' } },
    { layout: 'center', title: 'Welche Aufgabe würdest du zuerst', script: 'abgeben?', p: 'Schreib mir per DM.', scene: 'none' },
  ],
};
