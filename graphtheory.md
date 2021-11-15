# Graphentheorie

- [Algorithmus von Prim](#algorithmus-von-prim)

## Algorithmus von Prim

1930 vom tschechischen Mathematiker Vojtěch Jarník entwickelt.
1957 von Robert C. Prim wiederentdeckt
1959 von Edsger W. Dijkstra wiederentdeckt

- [Welches Problem löst dieser Algorithmus?](#welches-problem-löst-der-algorithmus-von-prim)
- [Wie läuft er ab?](#wie-läuft-der-algorithmus-von-prim-ab)
- [Warum liefert wer immer das korrekte Ergebnis?](#warum-liefert-der-algorithmus-von-prim-immer-das-korrekte-ergebnis)
- [Gibt es Einschränkungen hinsichtlich der Gültigkeit?](#gibt-es-einschränkungen-hinsichtlich-der-gültigkeit-des-algorithmus-von-prim)

### Welches Problem löst der Algorithmus von Prim?

Er findet den minimalen Spannbaum eines zusammenhängenden, kantengewichteten Graphen.

### Wie läuft der Algorithmus von Prim ab?

1. Es wird ein zufälliger Knoten auf dem Graph ausgewählt.
2. Von diesem Knoten wird eine anliegende Kante mit minimalem Gewicht und der dazugehörige Knoten zum Graph hinzugefügt.
3. Anschliessend wird ein noch nicht erschlossener Knoten mit einer Verbindungskante mit minimalem Gewicht zum Graph hinzugefügt.
4. Schritt 3 wird wiederholt, bis alle Punkte erschlossen sind.

[![Beispielgraph](./img/graphtheory/prim-example.jpg)](./img/graphtheory/prim-example.jpg)

### Warum liefert der Algorithmus von Prim immer das korrekte Ergebnis?

Weil alle Knoten verbunden werden müssen und dazu immer der kürzeste Weg verwendet wird.

### Gibt es Einschränkungen hinsichtlich der Gültigkeit des Algorithmus von Prim?

Nein, es gibt keine Einschränkungen.
