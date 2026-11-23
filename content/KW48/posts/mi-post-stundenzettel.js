// Mi 25.11. · Post (Standbild, clean) · Säule 2 Vorher/Nachher · Dunkel
// retype abgewandelt: links schiefe, verwischte Zettel-Zeilen (messy), rechts saubere Liste mit Haken (checks)
window.POST = {
  name: 'kw48-mi-stundenzettel', theme: 'dark', label: 'VORHER / NACHHER', clean: true,
  slides: [
    { layout: 'stack', title: 'Monatsende ohne Stapel', script: 'Stundenzettel.',
      scene: 'retype', props: { left: 'Zettel', right: 'Stunden', messy: true, checks: true }, dy: 60 },
  ],
};
