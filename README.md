# PandaLoveTest

Der PandaLoveTest soll ein Klon eines typischen LoveTests sein.

D.h. es gibt die Möglichkeit zwei Namen einzutragen. Diese Namen werden an die Webseite gesendet und eine "Love-Prozentzahl" wird zurückgeliefert.

In einem späteren Schritt werden die Namenskombinationen in einer Datenbank gespeichert.

D.h. wenn die gleichen Namen übertragen werden, dann soll das gleiche Ergebnis kommen.

Das kann man vielleicht mit einem Timeout versehen. D.h. es kommt nur das gleiche Ergebnis, wenn maximal 5 Minuten vergangen sind. Wird der Test zu einem späteren Zeitpunkt ausgeführt, dann soll ein neues Ergebnis kommen. D.h. es gibt die Möglichkeit ein neues Ergebnis für eine Namenskombination zu erhalten.

Es wäre theoretisch auch möglich, die Datenbank alle xxx Minuten zu löschen, ist aber keine sinnvolle Lösung.

Wichtige Bibliotheken:

* random || Zufallszahl
* fastapi[standard] || Python-Web-Framework
* jinja2 || Template Engine
* sqlmodel || Datenbankstuff

## Routen

* / || GET: Home
* / || POST: Ergebnis

## Architekturfragen

* Soll es zu einem Page-Refresh kommen, d.h. ganze Seite neu geladen, oder reicht es das Ergebnis darzustellen?
  * Falls nur das Ergebnis -> **Bibliothek HTMX JA, wollen wir**
  * https://htmx.org/
* Wie lange es dauern bis das Ergebnis dargestellt wird?

## Grafiken

Wir brauchen noch Grafiken für unser Projekt.

Da die Grafiken skalierbar sein sollen, würde sich das Format SVG anbieten. | z.B. Inkscape

Erstelle folgende Grafiken als SVG:

* zwei unterschiedliche Pandas. Diese sollten zumindest in die andere Richtung sehen. 
* Ein Herz
* Blumen (rote), Art egal

## Animationen

Soll es auf der Webseite Animationen geben? Wenn ja, welche?

Größe ändern? ;)
