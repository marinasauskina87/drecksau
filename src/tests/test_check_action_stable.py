import pytest
from logik.check_action_stable import check_action_stable

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, current_arrester,'
}

def test_check_action_stable_for_clean():
    result = check_action_stable(dict_test,"pig_1")
    assert result == 0

def test_check_action_stable_for_dirty():
    result = check_action_stable(dict_test,"pig_2")
    assert result == 0
def test_check_action_stable_exists():
    result = check_action_stable(dict_test, "pig_3")
    assert result == 1
