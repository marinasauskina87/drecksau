import pytest
from backend.function_current_arrester import action_current_arrester

# Test-Dictionary
dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty, stable,',
    'pig_3': 'dirty, stable, locked,',
    'pig_4': 'clean, stable,'
}

def test_current_arrester_appends_status():
    """Die Funktion hängt 'current_arrester,' korrekt an den Status an."""
    data = dict_test.copy()
    result = action_current_arrester(data, 'pig_1')
    assert result['pig_1'].endswith('arrester,')

def test_current_arrester_preserves_existing_status():
    """Vorhandene Statusinformationen bleiben erhalten."""
    data = dict_test.copy()
    result = action_current_arrester(data, 'pig_3')
    assert 'locked' in result['pig_3']
    assert result['pig_3'].endswith('arrester,')

