// Beispiel-Post: Mist · Lösungs-Karussell.
window.POST = {
  name: 'flowkraft-loesung', theme: 'mist', label: 'LÖSUNG',
  slides: [
    { hook: true, layout: 'bottom', title: 'Rechnungen ablegen? Macht jetzt ein', script: 'Agent.', chips: ['E-Mail','Agent','Buchhaltung'], scene: 'dochub' },
    { layout: 'stack', title: 'Vorher: suchen, umbenennen, ablegen. Nachher:', script: 'nichts.', p: 'So läuft der Ablauf in drei Schritten – ohne dass jemand eine Datei anfasst.', scene: 'beforeafter',
      props: { before: ['suchen','umbenennen','ablegen'], leftTitle: 'Vorher', rightTitle: 'Nachher' } },
    { layout: 'side', num: '01', title: 'Die Rechnung kommt per', script: 'E-Mail.', p: 'Der Agent erkennt den Anhang automatisch als Rechnung.', scene: 'mailscan', props: { tag: 'Rechnung ✓' } },
    { layout: 'stack', num: '02', title: 'Der Agent liest sie', script: 'aus.', p: 'Lieferant, Datum, Betrag – und benennt die Datei nach einem festen Schema.', scene: 'extract',
      props: { fields: ['Lieferant','Datum','Betrag'], file: 'Lieferant_Datum_Betrag.pdf' } },
    { layout: 'center', num: '03', title: 'Ablage im richtigen', script: 'Ordner.', p: 'Auf Wunsch geht sie gleich weiter an die Buchhaltung.', scene: 'folders', props: { out: 'Buchhaltung' } },
    { layout: 'stack', title: 'Was würde dir das', script: 'sparen?', p: 'Kommentiere ROI und du bekommst den ROI-Rechner: Aufgabe, Minuten, Stundensatz – deine Kosten pro Jahr auf einen Blick.', cta: 'Kommentiere ROI', scene: 'roiform',
      props: { title: 'ROI-Rechner', fields: ['Aufgabe','Minuten','Stundensatz'], result: 'Kosten pro Jahr' } },
  ],
};
