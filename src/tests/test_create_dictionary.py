import pytest
from backend.create_dictionary import create_dictionary

def test_create_dictionary_2_players():
    result = create_dictionary(2)
    expected = {
        'pig_1': 'clean',
        'pig_2': 'clean',
        'pig_3': 'clean',
        'pig_4': 'clean',
        'pig_5': 'clean'
    }
    assert result == expected

def test_create_dictionary_3_players():
    result = create_dictionary(3)
    expected = {
        'pig_1': 'clean',
        'pig_2': 'clean',
        'pig_3': 'clean',
        'pig_4': 'clean'
    }
    assert result == expected

def test_create_dictionary_4_players():
    result = create_dictionary(4)
    expected = {
        'pig_1': 'clean',
        'pig_2': 'clean',
        'pig_3': 'clean'
    }
    assert result == expected

def test_create_dictionary_test_dictionary():
    result = create_dictionary(123)
    expected = {
        'pig_1': 'clean',
        'pig_2': 'dirty,',
        'pig_3': 'dirty, stable, ',
        'pig_4': 'dirty, stable, locked, arrester '
    }
    assert result == expected