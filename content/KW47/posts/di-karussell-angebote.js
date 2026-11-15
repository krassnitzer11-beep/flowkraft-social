// Di 17.11. · Karussell · Säule 4 Rechnet sich das? · Navy
// KW 47: hourglass und flowpanel ersetzt (teilt sie sonst mit dem Mo-Reel), Schluss-Slide ohne roiform
window.POST = {
  name: 'kw47-di-angebote', theme: 'navy', label: 'NACHGERECHNET',
  slides: [
    { hook: true, layout: 'bottom', outline: 'Angebote abtippen:', title: '220 Stunden im', script: 'Jahr.', scene: 'yeargrid', dy: -130,
      props: { title: '44 Arbeitswochen', value: 220, unit: 'Stunden', note: '15 Angebote pro Woche' } },
    { layout: 'side', title: 'Kommt dir das', script: 'bekannt?', p: 'Anfrage per Mail. Daten raussuchen. Ins Programm tippen. PDF erstellen. Zurückschicken.', scene: 'mailscan', props: { tag: 'Anfrage' } },
    { layout: 'stack', num: '01', title: '5 Stunden pro', script: 'Woche.', p: '15 Angebote × 20 Minuten. Die Daten stehen schon in der Anfrage und werden trotzdem noch einmal eingetippt.', scene: 'retype', props: { left: 'Anfrage', right: 'Programm' } },
    { layout: 'bottom', num: '02', title: '220 Stunden × 45 € = 9.900 € im', script: 'Jahr.', p: 'Beispielrechnung: 5 Stunden × 44 Arbeitswochen, angenommen 45 € pro Stunde.', scene: 'roiform', dy: -410,
      props: { title: 'Beispielrechnung', fields: ['5 h / Woche','44 Wochen','45 € / h'], result: 'Kosten pro Jahr' } },
    { layout: 'stack', num: '03', title: 'Du prüfst nur noch und klickst', script: 'Senden.', p: 'Die Anfrage wird erkannt, die Daten übernommen, das Angebot vorbereitet.', scene: 'extract',
      props: { fields: ['Kunde','Leistung','Menge'], file: 'Angebot_Kunde_Datum.pdf' } },
    { layout: 'center', title: 'Lohnt sich das immer?', script: 'Nein.', p: 'Faustregel: Bei 3 Angeboten im Monat lass es. Ab etwa 10 pro Woche rechne nach.', scene: 'none' },
    { layout: 'bottom', title: 'Rechne selbst', script: 'nach.', p: 'Speichere dir den Post. Angebote pro Woche × Minuten ÷ 60 = Stunden pro Woche. Dann × Arbeitswochen × Stundensatz.', cta: 'Speichern', scene: 'calculator', dy: -40, sceneScale: 0.9,
      props: { steps: ['Stunden/Woche','× Wochen','× Stundensatz'] } },
  ],
};
