import pytest
from logik.check_action_open import check_action_open

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable,',
    'pig_4': 'dirty, stable, locked, current_arrester,'
}

def test_check_action_open():
    result = check_action_open(dict_test,"pig_3")
    assert result == 0
def test_check_action_open_pig_is_clean():
    result = check_action_open(dict_test, "pig_1")
    assert result == 1
def test_check_action_open_stable_is_locked():
    result = check_action_open(dict_test, "pig_4")
    assert result == -1