// Do 19.11. · Reel · Säule 2 Vorher/Nachher · Mist · eine Geschichte in sechs Sätzen
window.POST = {
  name: 'kw47-do-anfragen', theme: 'mist', label: 'VORHER / NACHHER',
  slides: [
    { hook: true, layout: 'top', outline: 'Vorher: Chaos.', title: 'Nachher:', script: 'Ruhe.', scene: 'chaos' },
    { layout: 'stack', title: 'Heute wird jede Anfrage dreimal', script: 'angefasst.', scene: 'beforeafter',
      props: { before: ['abtippen','weiterleiten','nachfragen'], leftTitle: 'Vorher', rightTitle: 'Nachher' } },
    { layout: 'side', title: 'Ab jetzt wird sie sofort', script: 'erkannt.', scene: 'mailscan', props: { tag: 'Anfrage ✓' } },
    { layout: 'stack', title: 'Die Daten landen von selbst im', script: 'System.', scene: 'extract',
      props: { fields: ['Name','Anliegen','Dringlichkeit'], file: 'Anfrage_Name_Datum' } },
    { layout: 'center', title: 'Und sie liegt gleich bei der richtigen', script: 'Person.', p: 'Raus geht die Antwort erst, wenn jemand sie prüft.', scene: 'folders', props: { out: 'Zuständig' } },
    { layout: 'bottom', title: 'Wer tippt bei dir noch', script: 'ab?', chips: ['Anfrage','Agent','Team'], scene: 'dochub', dy: 110 },
  ],
};
