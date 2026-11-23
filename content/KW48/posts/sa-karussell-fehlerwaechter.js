// Sa 28.11. · Karussell · Säule 5 Praxisbeispiel (Musterprojekt) · Dunkel · 8 Slides
// Neue Szenen „waechter“ (Slide 1) und „zuerst“ (Slide 7); roiform als Meldungs-Formular abgewandelt (Slide 5, ohne Euro/Zahlen)
// Eigenes Icon: Glocke (Slide 7)
window.POST = {
  name: 'kw48-sa-fehlerwaechter', theme: 'dark', label: 'PRAXISBEISPIEL',
  slides: [
    { hook: true, layout: 'top', title: 'Wer merkt, wenn nichts', script: 'passiert?', scene: 'waechter' },
    { layout: 'side', title: 'Stillstand sieht harmlos', script: 'aus.', p: 'Die Lieferantenbestellung soll automatisch raus. Sie bleibt hängen. Du merkst es, wenn Material fehlt.',
      scene: 'pile', props: { folder: 'Bestellung' }, sceneScale: .85, dy: -60 },
    { layout: 'stack', num: '01', title: 'Jeder Schritt hat ein', script: 'Ziel.', p: 'Bestellung erzeugt, verschickt, vom Lieferanten bestätigt. Bis wann, steht vorher fest.',
      scene: 'extract', props: { fields: ['Erzeugt', 'Verschickt', 'Bestätigt'], file: 'Frist je Schritt festgelegt' }, sceneScale: .9, dy: -40 },
    { layout: 'center', num: '02', title: 'Der Wächter schaut nur', script: 'nach.', p: 'In festen Abständen prüft er, ob jeder Schritt angekommen ist. Selbst eingreifen kann er nicht.',
      scene: 'folders', props: { out: 'Angekommen?' }, sceneScale: .85, dy: 40 },
    { layout: 'stack', num: '03', title: 'Er meldet sich bei einer', script: 'Person.', p: 'Welcher Schritt, seit wann, was fehlt. Nur an die Person, die zuständig ist.',
      scene: 'roiform', props: { title: 'Meldung', fields: ['Schritt', 'Seit wann', 'Was fehlt'], result: 'An die zuständige Person', value: '✓' }, sceneScale: .9, dy: 100 },
    { layout: 'bottom', num: '04', title: 'Die Entscheidung trifft ein', script: 'Mensch.', p: 'Neu starten, von Hand erledigen oder bewusst liegen lassen. Der Wächter repariert nichts selbst.', scene: 'none' },
    { layout: 'stack', title: 'Du erfährst es zuerst. Nicht dein', script: 'Kunde.', p: 'Ehrliche Grenze: Ein Wächter meldet Fehler. Verhindern kann er sie nicht.',
      scene: 'zuerst', props: { a: 'Meldung an dich', b: 'Kunde', icon: '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2.5h-15Z"/><path d="M10 21h4"/><path d="M12 3v2"/>' } },
    { layout: 'center', title: 'Für das nächste Praxisbeispiel:', script: 'folgen.', p: 'Musterprojekt, kein Kundenprojekt.', cta: 'Folgen', scene: 'none' },
  ],
};
