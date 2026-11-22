# Recherchen beitragen

1. Eine klare Fragestellung, einen Raum und eine Zeitspanne abgrenzen. Heutige Länder sind mögliche Suchhilfen, keine verbindlichen Inhaltscontainer.
2. Vor einer neuen Datei bestehende IDs und Quellen durchsuchen. Geteilte Personen, Orte und Quellen nicht pro Kapitel kopieren.
3. Quellen lesen und genaue Fundstellen erfassen. Ein Verweis auf eine allgemeine Übersichtsseite ist kein automatischer Beleg für jedes Detail.
4. Identität als Entität, datierte Beziehung als Aussage und mehrseitigen Vorgang als Ereignis erfassen. Die Form einer Fläche ist ein gesonderter Geometriedatensatz.
5. Unsicherheit konkret beschreiben. „Unbekannt“ bleibt unbekannt; ein Jahr ohne Tagesdatum wird nicht zu einem exakten 1. Januar.
6. Geometrie und Medien mit Herkunft, Bearbeitung, Lizenz und Attribution versehen. Verlinken einer Quelle und lokales Ausliefern ihres Inhalts sind unterschiedliche Handlungen.
7. DE-/EN-Texte getrennt pflegen, Originalnamen und Transliteration erhalten. Ein Kapitel muss ohne Kenntnis früherer Unterhaltungen verständlich sein.
8. Das Eigentümerpaket und erforderliche Paketabhängigkeiten vollständig aktualisieren. Eingehende Aussagen nicht vergessen.
9. Mit dem fixierten lokalen Autorenwerkzeug prüfen und die Vorschau in beiden Sprachen sichten. Noch nicht implementierte Werkzeuge nicht als ausgeführte Prüfung darstellen.
10. Im Beitrag geprüfte Quellen, geänderte IDs, bekannte Lücken und tatsächlichen Reviewstatus nennen.

Im Entwurf ist `editorial.status: draft` richtig. `reviewed` setzt einen tatsächlich erfolgten, nachvollziehbar bezeichneten Prüfprozess voraus. Eine unsichere historische Aussage kann redaktionell sorgfältig geprüft sein; deshalb sind Review und historische Gewissheit getrennte Angaben.

Neue Beziehungstypen oder Änderungen an Schemas werden im Engine-Repo abgestimmt und versioniert. Das lokale Autorenwerkzeug wird nicht verändert, um fehlerhafte Daten durch die Prüfung zu bringen. Eine neue Entität eines vorhandenen Typs braucht dagegen keine Programmänderung.

Für eine Veröffentlichung wird das Content-Artefakt separat erzeugt. `published/` ist ein Buildprodukt; dort nicht recherchieren oder Dateien von Hand korrigieren. Korrekturen erfolgen im kanonischen Bestand und erzeugen einen neuen, vollständig konsistenten Release.
