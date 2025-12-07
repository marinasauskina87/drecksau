import pytest
from backend.function_dirty import action_dirty

# Test-Dictionary
dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, arrester,'
}

def test_action_dirty_marks_clean_pig_as_dirty():
    """Ein sauberes Schwein wird korrekt als 'dirty' markiert."""
    data = dict_test.copy()
    result = action_dirty(data, 'pig_1')
    assert result['pig_1'].startswith('dirty,')


def test_action_dirty_preserves_other_status_parts():
    """Andere Statusinformationen (z.B. 'stable') bleiben erhalten."""
    data = dict_test.copy()
    result = action_dirty(data, 'pig_3')
    assert result['pig_3'].startswith('dirty,')
    assert 'stable' in result['pig_3']

def test_action_dirty_multiple_pigs():
    """Mehrere Schweine werden nacheinander korrekt auf 'dirty' gesetzt."""
    data = dict_test.copy()
    for pig in ['pig_1', 'pig_3']:
        data = action_dirty(data, pig)
    assert data['pig_1'].startswith('dirty,')
    assert data['pig_3'].startswith('dirty,')

