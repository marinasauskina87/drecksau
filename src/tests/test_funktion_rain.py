from backend.funktion_rain import action_rain

dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}

# Test: Schwein wird gereinigt, wenn es nicht im Stall ist
def test_action_rain_cleans_non_stable_pig():
    """Wenn das Schwein nicht 'stable' enthält, wird es von action_rain gereinigt."""
    data = [dict_test.copy()]
    result = action_rain(data)
    assert result[0]['pig_2'] == 'clean,'

# Test: Schweine im Stall bleiben unverändert
def test_action_rain_preserves_stable_pigs():
    """Schweine mit 'stable' im Status bleiben unverändert."""
    data = [dict_test.copy()]
    result = action_rain(data)
    assert result[0]['pig_3'] == dict_test['pig_3']
    assert result[0]['pig_4'] == dict_test['pig_4']

# Test: Andere Schweine unverändert, wenn ein Schwein gereinigt wird
def test_action_rain_preserves_other_pigs_when_cleaning_one():
    """Andere Schweine bleiben unverändert, wenn ein Schwein gereinigt wird."""
    data = [dict_test.copy()]
    result = action_rain(data)
    # pig_1 war schon clean
    assert result[0]['pig_1'] == dict_test['pig_1']