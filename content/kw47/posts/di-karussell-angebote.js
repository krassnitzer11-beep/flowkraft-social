// Di 17.11. · Karussell · Säule 4 Rechnet sich das? · Navy
window.POST = {
  name: 'kw47-di-angebote', theme: 'navy', label: 'NACHGERECHNET',
  slides: [
    { hook: true, layout: 'bottom', outline: 'Angebote abtippen:', title: '220 Stunden im', script: 'Jahr.', scene: 'hourglass', props: { value: 220, unit: 'h' } },
    { layout: 'side', title: 'Kommt dir das', script: 'bekannt?', p: 'Anfrage per Mail. Daten raussuchen. Ins Programm tippen. PDF erstellen. Zurückschicken.', scene: 'mailscan', props: { tag: 'Anfrage' } },
    { layout: 'stack', num: '01', title: '5 Stunden pro', script: 'Woche.', p: '15 Angebote × 20 Minuten. Die Daten stehen schon in der Anfrage und werden trotzdem noch einmal eingetippt.', scene: 'retype', props: { left: 'Anfrage', right: 'Programm' } },
    { layout: 'bottom', num: '02', title: '220 Stunden × 45 € = 9.900 € im', script: 'Jahr.', p: 'Beispielrechnung: 5 Stunden × 44 Arbeitswochen, 45 € Stundensatz.', scene: 'yeargrid',
      props: { title: '44 Arbeitswochen', value: 220, unit: 'Stunden', note: '5 Stunden pro Woche' } },
    { layout: 'stack', num: '03', title: 'Du prüfst nur noch und klickst', script: 'Senden.', p: 'Die Anfrage wird erkannt, die Daten übernommen, das Angebot vorbereitet.', scene: 'flowpanel',
      props: { nodes: [['mail','Anfrage'], [null,'Agent'], ['file','Angebot'], ['send','Senden']], status: 'Wartet auf dich' } },
    { layout: 'center', title: 'Lohnt sich das immer?', script: 'Nein.', p: 'Bei 3 Angeboten im Monat: lass es. Ab etwa 10 pro Woche: rechne nach.', scene: 'none' },
    { layout: 'stack', title: 'Rechne selbst', script: 'nach.', p: 'Speichere dir den Post. Angebote pro Woche × Minuten × Stundensatz, mehr braucht es nicht.', cta: 'Speichern', scene: 'roiform',
      props: { title: 'Deine Rechnung', fields: ['Angebote','Minuten','Stundensatz'], result: 'Kosten pro Jahr' } },
  ],
};
