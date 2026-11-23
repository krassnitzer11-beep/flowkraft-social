// Di 24.11. · Karussell · Säule 3 Haltung · Navy · 7 Slides
// Eigene Icons: Werkstatt (Pin), Weiterleiten (Antwortkarte)
window.POST = {
  name: 'kw48-di-ohne-it', theme: 'navy', label: 'HALTUNG',
  slides: [
    { hook: true, layout: 'center', size: 118, outline: 'Keine IT-Abteilung?', title: 'Brauchst du', script: 'nicht.',
      scene: 'pin', dy: -10, props: { tag: '1 bis 50 Leute', icon: '<path d="M4 10v10h16V10"/><path d="M3 10l2-6h14l2 6Z"/><path d="M10 20v-5h4v5"/>' } },
    { layout: 'side', title: 'Klingt nach', script: 'Konzern.', p: 'Eigener Server, IT-Leute, ein Projekt über Monate. So stellen sich das viele vor.',
      scene: 'clock', props: { coin: 'IT' }, sceneScale: .85, dy: -40 },
    { layout: 'stack', num: '01', title: 'Ein Ablauf, nicht das ganze', script: 'Büro.', p: 'Du startest mit einer Aufgabe, die jede Woche gleich läuft.',
      scene: 'beforeafter', props: { before: ['Alles neu', 'Alle Programme', 'Alle auf einmal'], leftTitle: 'Nicht nötig', rightTitle: 'Ein Ablauf' }, dy: -20 },
    { layout: 'bottom', num: '02', title: 'Deine Programme', script: 'bleiben.', p: 'Mail, Kalender, Tabelle, Buchhaltung. Verbunden wird, was schon da ist.',
      chips: ['@', 'Kal', 'Tab', 'Buch'], scene: 'dochub', sceneScale: .8, dy: 20 },
    { layout: 'stack', num: '03', size: 104, title: 'Ehrliche Grenze: erst einmal', script: 'festlegen.', p: 'Macht jeder den Ablauf jedes Mal anders, schreibst du zuerst auf, wie er laufen soll.',
      scene: 'ranking', props: { title: 'Ablauf', right: 'In fester Reihenfolge', bars: [34, 58, 82] }, sceneScale: .8, dy: 140 },
    { layout: 'center', title: 'Kein Server, kein IT-Mensch. Auch wenn du allein', script: 'bist.', p: 'Die Größe deines Betriebs entscheidet nicht. Ein klarer Ablauf schon.', scene: 'none' },
    { layout: 'stack', title: 'Kennst du jemanden, der das', script: 'glaubt?', p: 'Schick ihm den Post weiter.', cta: 'Teilen',
      scene: 'comment', props: { word: 'Schau dir das an', title: 'Weitergeleitet', sub: 'an eine Person',
        icon: '<path d="M14 4l6 6-6 6"/><path d="M20 10h-9a6 6 0 0 0-6 6v4"/>' } },
  ],
};
