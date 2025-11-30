import check_dirty
import check_clean
import check_stable
import check_locked
import check_current_arrester
import check_open
import check_flash


def check_withdraw_cards(cards: list, pigs: dict) -> int:
    """
    Prüft, ob der Spieler mindestens eine seiner aktuell gezogenen
    Karten spielen kann.
    
    Regeln:
   - Wenn mindestens eine Karte spielbar ist -> return 0
     (Spieler darf aus seinen Karten wählen)
   - Wenn KEINE der 3 Karten spielbar ist -> return 1
     (Spieler muss Karten abwerfen)

   Die Funktion verändert nicht den Spielzustand.

    Parameters
    ----------
    cards : list
        Die 3 aktuell gezogenen Karten des Spielers
        Beispiel: ["dirty", "flash", "stable"]
    pigs : dict
        Der aktuelle Zustand aller Schweine des Spielers.
        Beispiel: {"1": "dirty,stable,", "2": "clean,", ...}

    Returns
    -------
    int
        0 : Mindestens eine Karte ist spielbar (kein Abwerfen nötig)
       1 : Keine Karte ist spielbar (Spieler muss Karten abwerfen)

    """
    
    for card in cards:
        for pig_number in pigs.keys():

            # Mapping Karte → Check-Funktion
            if card == "dirty":
                result = check_dirty(pigs, pig_number)

            elif card == "clean":
                result = check_clean(pigs, pig_number)

            elif card == "stable":
                result = check_stable(pigs, pig_number)

            elif card == "locked":
                result = check_locked(pigs, pig_number)

            elif card == "current_arrester":
                result = check_current_arrester(pigs, pig_number)

            elif card == "open":
                result = check_open(pigs, pig_number)

            elif card == "flash":
                result = check_flash(pigs, pig_number)

            else:
                # unbekannte Karte → ignorieren
                continue

            # Karte ist spielbar
            if result == 0:
                return 0

    # Wenn keine einzige Karte spielbar ist:
    return 1