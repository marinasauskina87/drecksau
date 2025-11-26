# -*- coding: utf-8 -*-
import random

def action_tornado(dict_all_players):
    """
    Führt die Aktion Tornado aus, welche die Aktionskarten der jeweiligen
    Schweine durchmischt. Der Sauberkeitsgrad der Schweine bleibt jedoch
    bestehen. Es ist durchaus möglich, dass der Tornado die Aktionskarten
    eines Schweins zufälligerweise dem gleichen Schwein zuordnet.

    Parameters
    ----------
    dict_all_players : lists of dictionaries
        Liste mit den Dictionaries aller Spieler.

    Returns
    -------
    dict_all_players : lists of dictionaries
        Liste mit den Dictionaries aller Spieler.

    """
    # Zwischenspeicher für alle Aktionen im Spiel
    all_action_items = []
    
    # Alle momentanen Aktionen der Schweine erhalten:
    for player_dict in dict_all_players:
        # Wir möchten nur die Aktionen eines Schweins ändern und nicht sein
        # Sauberkeitszustand
        all_action_items += [action.split(',')[1:] for action in list(player_dict.values())]
    
    # Aktionen der Schweine neu zuordnen:
    for player_dict in dict_all_players:
        for pig in player_dict:
            # Löscht die momentanen Aktionen des jeweiligen Schweins
            player_dict[pig] = player_dict[pig].split(',')[0]
            # Wählt die zufälligen (neuen) Aktion(en) des Schweins
            new_action = random.choice(all_action_items)
            all_action_items.remove(new_action)
            # Da alle Werte als Listen abgespeichert sind
            for action in new_action:
                player_dict[pig] += "," + action
    
    return dict_all_players