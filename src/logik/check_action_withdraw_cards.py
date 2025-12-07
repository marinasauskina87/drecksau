from logik.check_function_dirty import check_action_dirty
from logik.check_action_clean import check_clean
from logik.check_action_stable import check_action_stable
from logik.check_action_locked import check_action_locked
from logik.check_action_current_arrester import check_current_arrester
from logik.check_action_open import check_action_open
from logik.check_action_flash import check_action_flash
 
import frontend.config as config
 
 
def check_withdraw_cards(cards: list, pigs_all_players: dict, current_player: int) -> int:
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
        if (card in config.status_cards) or (card in config.support_cards):
            for pig_of_current_player in pigs_all_players[current_player-1]:
                if card == "Matschkarte":
                    result = check_action_dirty(pigs_all_players[current_player-1], pig_of_current_player)
                elif card == "Stallkarte":
                    result = check_action_stable(pigs_all_players[current_player-1], pig_of_current_player)
                elif card == "Blitzableiterkarte":
                    result = check_current_arrester(pigs_all_players[current_player-1], pig_of_current_player)
                elif card == "Bauer-ärgere-dich-Karte":
                    result = check_action_locked(pigs_all_players[current_player-1], pig_of_current_player)
                if result == 0:
                    return 0
        else:
            for index, pigs in enumerate(pigs_all_players):
                if (index == current_player-1):
                    continue     
                for pig_number in pigs.keys():
                    # Mapping Karte: Check-Funktion
                    if card == "Bauer-schrubbt-die-Sau-Karte":
                        result = check_action_open(pigs, pig_number)
                    elif card == "Blitzkarte":
                        result = check_action_flash(pigs, pig_number)
                    elif card == "Tornadokarte" or card == "Regenkarte":
                        result = 0
                    else:
                        # unbekannte Karte: ignorieren
                        continue
                    if result == 0:
                        return 0
 
    # Wenn keine einzige Karte spielbar ist:
    return 1