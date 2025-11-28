import pytest
from logik.check_action_current_arrester import check_current_arrester

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, current_arrester,'
}

def test_check_action_current_arrester():
    result = check_current_arrester(dict_test,"pig_3")
    assert result == 0
def test_check_action_current_arrester_exists():
    result = check_current_arrester(dict_test, "pig_4")
    assert result == 1
def test_check_action_current_arrester_no_stable():
    result = check_current_arrester(dict_test, "pig_2")
    assert result == -1