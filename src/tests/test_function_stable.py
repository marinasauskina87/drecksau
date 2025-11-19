import pytest
from backend.function_stable import action_stable

# Test-Dictionary
dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, locked,',
    'pig_4': 'clean, locked,'
}

def test_action_stable_appends_stable():
    """Die Funktion hängt 'stable,' korrekt an den Status an."""
    data = dict_test.copy()
    result = action_stable(data, 'pig_1')
    assert result['pig_1'].endswith('stable,')

def test_action_stable_preserves_existing_status():
    """Vorhandene Statusinformationen bleiben erhalten."""
    data = dict_test.copy()
    result = action_stable(data, 'pig_3')
    assert 'locked' in result['pig_3']
    assert result['pig_3'].endswith('stable,')

