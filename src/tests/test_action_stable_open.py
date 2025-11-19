from backend.action_stable_open import action_stable_open
from backend.action_clean import action_clean

# Test-Dictionary
dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}

def test_action_stable_open_unlocked_pig_cleaned():
    """Wenn das Schwein nicht 'locked' hat, wird es von action_clean gereinigt."""
    data = dict_test.copy()
    result = action_stable_open(data, 'pig_2')
    assert result['pig_2'] == 'clean'


def test_action_stable_open_preserves_other_pigs():
    """Andere Schweine bleiben unverändert, wenn ein Schwein gereinigt wird."""
    data = dict_test.copy()
    result = action_stable_open(data, 'pig_3')
    for key in data:
        if key != 'pig_3':
            assert result[key] == data[key]



