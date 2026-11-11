// Beispiel-Post: Navy · Leistungs-Karussell. Kopieren, Texte/Szenen ändern, rendern.
window.POST = {
  name: 'flowkraft-leistung', theme: 'navy', label: 'LEISTUNG',
  slides: [
    { hook: true, layout: 'top', outline: 'Weniger Routine.', title: 'Mehr Zeit fürs', script: 'Geschäft.', scene: 'chaos' },
    { layout: 'bottom', title: 'Erst rechnen, dann', script: 'bauen.', p: 'So arbeitet flowkraft – in drei Schritten. Und manchmal raten wir auch ab.', scene: 'calculator' },
    { layout: 'side', num: '01', title: 'Zeitfresser', script: 'finden.', p: 'Wir schauen uns deine Abläufe an und rechnen in Stunden und Euro, was sie kosten.', scene: 'clock' },
    { layout: 'stack', num: '02', title: 'Automatisierung', script: 'umsetzen.', p: 'Workflows und KI-Agenten, die zu deinen Tools passen. Deine Leute bleiben vorne.', scene: 'flowpanel',
      props: { nodes: [['crm','CRM'],[null,'KI-Agent'],['calc','Buchhaltung'],['invoice','Rechnung']], status: 'Läuft automatisch' } },
    { layout: 'center', num: '03', title: 'Persönlich', script: 'betreut.', p: 'Ein fixer Ansprechpartner aus Kärnten – auch nach dem Start.', scene: 'pin', props: { tag: 'Kärnten', icon: 'user' } },
    { layout: 'stack', title: 'Lohnt sich das für deinen', script: 'Betrieb?', p: 'Kommentiere FÖRDERUNG und du bekommst per DM den Kurzguide zu KMU.DIGITAL: was gefördert wird und wie viel.', cta: 'Kommentiere FÖRDERUNG', scene: 'comment',
      props: { word: 'FÖRDERUNG', title: 'Kurzguide', sub: 'KMU.DIGITAL' } },
  ],
};
