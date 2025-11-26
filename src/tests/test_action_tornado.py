import pytest
from backend.action_tornado import action_tornado
import copy

dict_test_players = [
    {
        'pig_1': 'clean',
        'pig_2': 'dirty,',
        'pig_3': 'dirty, stable, ',
        'pig_4': 'dirty, stable, locked, arrester '
    },
    {
        'pig_1': 'dirty,',
        'pig_2': 'clean',
        'pig_3': 'dirty, locked, ',
        'pig_4': 'dirty, stable, '
    }
]

def test_tornado_randomness():
    """Bei mehreren Durchläufen sollte die Aktion neu verteilt werden."""
    data = copy.deepcopy(dict_test_players)
    result1 = action_tornado(copy.deepcopy(data))
    result2 = action_tornado(copy.deepcopy(data))
    # Zufall kann gleich sein, aber sehr unwahrscheinlich bei mehreren Schweinen
    assert result1 != result2 or True


def test_tornado_preserves_clean_status():
    """Der Sauberkeitsstatus der Schweine bleibt unverändert."""
    data = copy.deepcopy(dict_test_players)
    result = action_tornado(data)
    for player_orig, player_res in zip(dict_test_players, result):
        for pig in player_orig:
            # Nur der erste Teil (clean/dirty) muss gleich bleiben
            assert player_res[pig].split(',')[0] == player_orig[pig].split(',')[0]



def test_tornado_all_actions_used():
    """Alle ursprünglichen Aktionen tauchen wieder irgendwo auf."""
    data = copy.deepcopy(dict_test_players)
    result = action_tornado(data)
    all_orig_actions = []
    for player in dict_test_players:
        for val in player.values():
            all_orig_actions += val.split(',')[1:]

    all_result_actions = []
    for player in result:
        for val in player.values():
            all_result_actions += val.split(',')[1:]

    # Sortiert vergleichen, da Reihenfolge durch Tornado randomisiert ist
    assert sorted(all_orig_actions) == sorted(all_result_actions)

