import pytest
from logik.check_action_locked import check_action_locked

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, current_arrester,'
}

def test_check_action_locked():
    result = check_action_locked(dict_test,"pig_3")
    assert result == 0
def test_check_action_locked_exists():
    result = check_action_locked(dict_test, "pig_4")
    assert result == 1
def test_check_action_locked_no_stable():
    result = check_action_locked(dict_test, "pig_2")
    assert result == -1