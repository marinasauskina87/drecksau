import pytest
from logik.check_action_clean import check_clean

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'clean, stable,',
    'pig_4': 'dirty, stable, locked, arrester,'
}

def test_check_clean_can_be_cleaned():
    result = check_clean(dict_test, "pig_2")
    assert result == 0


def test_check_clean_is_clean():
    result = check_clean(dict_test, "pig_1")
    assert result == 1
def test_check_clean_is_in_stable():
    result = check_clean(dict_test, "pig_4")
    assert result == -1

