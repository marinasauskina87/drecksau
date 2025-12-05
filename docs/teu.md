##Kontext
PM1 mit Python, 3. Projekt - Kartenspiel-Dreckssau

##Ziel
- Das Spiel "Dreckssau" mit den geforderten Funktionalitäten entwickeln
- Zusätzlich ein passendes GUI zum Spiel entwickeln
- Eine sinnvolle Aufteilung der Funktionalitäten finden
- Code hinreichend und nachvollziehbar dokumentieren
- Nur die Programmierkonstrukte von PROG1 benutzen
- Effizient GitHub, Jira und SCRUM nutzen

##Projektorganisation
- Produkt-Owner: Amer P.
- Scrum-Master: Lucien L.
- Entwickler-Team: Marina S., Laura M., Lucien L., Amer P.

##Aufbau vom Programm
Der Code ist in Backend, Frontend, Logik und Tests klar voneinander getrennt.
Das Frontend steuert über ein Control-Panel die Spielaktionen, greift auf die Backend-Funktionen zu und nutzt die Logik-Checks, um Spielregeln zu prüfen.
Alle Funktionen sind systematisch durch automatisierte Tests abgesichert.
![Aufbau_Code](assets/Aufbau_Code.png){ width="550" }


##Design vom Spielbrett
So sieht unser Spielbrett aus, welches wir mit einem GUI in Python erstellt haben.
Da CustomTkinter nicht beim Start sofort erkennt, wie gross der Fullscreen ist und dann sofort die Grösse 200x200 wählt, ist das Hintergrundbild teilweise nicht ersichtlich. Bitte in diesem Fall das Programm neustarten.

![Kartenspiel Drecksau](assets/Bild_Projekt3.png){ width="550" }
