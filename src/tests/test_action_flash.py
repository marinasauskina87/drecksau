from backend.action_flash import action_flash

# Test-Dictionary
dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}



def test_action_flash_overwrites_existing_state():
    """Auch wenn ein Schwein schon einen anderen Zustand hat, wird er überschrieben."""
    data = dict_test.copy()
    result = action_flash(data, 'pig_3')
    assert result['pig_3'] == 'dirty,'


def test_action_flash_preserves_other_pigs():
    """Andere Schweine im Dictionary bleiben unverändert."""
    data = dict_test.copy()
    result = action_flash(data, 'pig_2')
    # Alle anderen Keys ausser pig_2 sollten unverändert bleiben
    for key in data:
        if key != 'pig_2':
            assert result[key] == data[key]