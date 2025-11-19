from backend.action_stable_locked import action_stable_locked

dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}

def test_action_stable_locked_appends_locked():
    """Das Wort 'locked,' wird korrekt an den Status angehängt."""
    data = dict_test.copy()
    result = action_stable_locked(data, 'pig_1')
    assert result['pig_1'].endswith('locked,')


def test_action_stable_locked_preserves_existing_status():
    """Der bestehende Status bleibt erhalten und 'locked,' wird angehängt."""
    data = dict_test.copy()
    result = action_stable_locked(data, 'pig_3')
    # Vorher war 'dirty, stable, ' → nachher sollte 'dirty, stable, locked,'
    assert result['pig_3'] == 'dirty, stable, locked,'

def test_action_stable_locked_preserves_other_pigs():
    """Andere Schweine im Dictionary bleiben unverändert."""
    data = dict_test.copy()
    result = action_stable_locked(data, 'pig_2')
    for key in data:
        if key != 'pig_2':
            assert result[key] == data[key]

