##Kontext
PM1 mit Python, 3. Projekt - Kartenspiel-Dreckssau

##Ziel
- Das Spiel "Dreckssau" mit den geforderten Funktionalitäten entwickeln
- Eine sinnvolle Aufteilung der Funktionalitäten finden
- Code hinreichend und nachvollziehbar dokumentieren
- Nur die Programmierkonstrukte von PROG1 benutzen
- Effizient GitHub, Jira und SCRUM nutzen

##Spezialitäten
- passendes GUI zum Spiel entwickeln

##Projektorganisation
- Produkt-Owner: Amer P.
- Scrum-Master: Lucien L.
- Entwickler-Team: Marina S., Laura M., Lucien L., Amer P.

##Aufbau vom Programm
Der Code ist in Backend, Frontend, Logik und Tests klar voneinander getrennt.
Das Frontend steuert über ein Control-Panel die Spielaktionen, greift auf die Backend-Funktionen zu und nutzt die Logik-Checks, um Spielaktionen zu prüfen.
Alle Funktionen sind systematisch durch automatisierte Tests abgesichert.
![Aufbau_Code](assets/Aufbau_Code.png){ width="550" }

##Verwendete Module im Projekt
**Tkinter:**
Tkinter ist die Standard-GUI-Bibliothek für Python. Damit erstellt man Fenster, Buttons, Eingabefelder und einfache Benutzeroberflächen. Es ist bereits in Python enthalten.


**customtkinter:**
customtkinter ist eine modernere Erweiterung von Tkinter. Es bietet ein schickeres Design mit Dark-Mode und modernen Widgets. Die Bedienung ist sehr ähnlich zu Tkinter.


**ctkmessagebox:**
ctkmessagebox ist eine moderne MessageBox für customtkinter. Damit zeigt man Dialogfenster wie Warnungen, Fehler oder Bestätigungen an. Optisch passt sie perfekt zu customtkinter.


**pytest:**
pytest ist ein Framework zum automatischen Testen von Python-Code. Es hilft, Funktionen zuverlässig zu prüfen. Tests lassen sich einfach schreiben und automatisch ausführen.



##Design vom Spielbrett
So sieht unser Spielbrett aus, welches wir mit einem GUI in Python erstellt haben.
Wenn man die Supportkarten ergänzen möchte erfolgt dies, wenn man auf das Schwein klickt und nicht auf die bevorstehenden Supportkarten.
Da CustomTkinter nicht beim Start sofort erkennt, wie gross der Fullscreen ist und dann sofort die Grösse 200x200 wählt, ist das Hintergrundbild teilweise nicht ersichtlich. Bitte in diesem Fall das Programm neustarten.

![Kartenspiel Drecksau](assets/Bild_Projekt3.png){ width="550" }

##Ausblick
Als Ausblick bleibt festzuhalten, dass wir als Gruppe die Blitz-Variante von Drecksau gerne noch implementiert und weiterentwickelt hätten, wenn uns mehr Zeit zur Verfügung gestanden wäre.


##Quellen

[Tkinter](https://docs.python.org/3/library/tkinter.html)

[CustomTkinter](https://customtkinter.tomschimansky.com/)

[ctkmessagebox](https://coderslegacy.com/python/customtkinter-messagebox-using-ctkmessagebox/)

[pytest](https://docs.pytest.org/en/stable/)