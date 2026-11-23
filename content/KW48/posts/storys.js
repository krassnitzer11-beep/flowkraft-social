// Storys Mo–Sa · eine offene Frage zum Post des Tages als Text, Antwort per DM · keine Sticker
// Szenen nie aus dem Post desselben Tags, des Vortags oder des Folgetags. Eigenes Icon: Gruppe (Story 5)
window.POST = {
  name: 'kw48-story', theme: 'navy', label: 'FRAGE',
  slides: [
    { layout: 'stack', title: 'Was ist dir an Zahlungserinnerungen', script: 'unangenehm?', p: 'Schick mir deine ehrliche Antwort als DM.',
      scene: 'extract', props: { fields: ['Rechnung', 'Fällig', 'Offen'], file: 'Erinnern?' }, size: 108 },
    { layout: 'center', title: 'Welches Programm im Büro würdest du nie', script: 'hergeben?', p: 'Verrat es mir per DM.',
      scene: 'folders', props: { out: 'Bleibt' }, size: 108 },
    { layout: 'bottom', title: 'Wer sammelt bei dir am Monatsende die Stunden', script: 'ein?', p: 'Antworte mir per DM.',
      scene: 'pile', props: { folder: 'Stunden' }, sceneScale: .85, dy: -40, size: 108 },
    { layout: 'side', title: 'Was erledigst du am Abend, wofür tagsüber kein Platz', script: 'ist?', p: 'Schreib es mir als Nachricht.',
      scene: 'clock', props: { coin: '?' }, sceneScale: .8, dy: -60, size: 104 },
    { layout: 'center', title: 'Was sagt dein Team, wenn du „neues Programm“', script: 'sagst?', p: 'Erzähl es mir per DM.',
      scene: 'pin', props: { tag: 'Dein Team', icon: '<circle cx="12" cy="7" r="3"/><circle cx="5" cy="10" r="2.3"/><circle cx="19" cy="10" r="2.3"/><path d="M7 20c.5-3.5 2.4-5.5 5-5.5s4.5 2 5 5.5"/><path d="M1.5 19c.3-2.4 1.6-3.8 3.5-3.8M22.5 19c-.3-2.4-1.6-3.8-3.5-3.8"/>' }, dy: -40, size: 104 },
    { layout: 'stack', title: 'Welcher Fehler fällt bei dir meistens zu spät', script: 'auf?', p: 'Schick mir dein Beispiel per DM.',
      scene: 'ranking', props: { title: 'Fällt zu spät auf', right: 'Dein Beispiel?', bars: [88, 62, 36] }, size: 108 },
  ],
};
