import pytest
from logik.check_function_dirty import check_action_dirty

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, current_arrester,'
}

def test_check_action_dirty_for_clean():
    result = check_action_dirty(dict_test,"pig_1")
    assert result == 0

def test_check_action_dirty_for_dirty():
    result = check_action_dirty(dict_test,"pig_2")
    assert result == 1
def test_check_action_dirty_if_stable_exists():
    result = check_action_dirty(dict_test, "pig_3")
    assert result == 0