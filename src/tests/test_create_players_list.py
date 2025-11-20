import pytest
from backend.create_players_list import create_players_list

# Hilfsfunktion für Tests
dict_2 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean',
    'pig_4': 'clean',
    'pig_5': 'clean'
}
dict_3 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean',
    'pig_4': 'clean'
}
dict_4 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean'
}
dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}

def test_create_players_list_length():
    """Test, dass die Liste die richtige Länge hat"""
    players = create_players_list(3)
    assert len(players) == 3

def test_create_players_list_content_2_players():
    """Test für 2 Spieler: Dictionary stimmt mit dict_2 überein"""
    players = create_players_list(2)
    for player_dict in players:
        assert player_dict == dict_2

def test_create_players_list_content_3_players():
    """Test für 3 Spieler: Dictionary stimmt mit dict_3 überein"""
    players = create_players_list(3)
    for player_dict in players:
        assert player_dict == dict_3

def test_create_players_list_content_4_players():
    """Test für 4 Spieler: Dictionary stimmt mit dict_4 überein"""
    players = create_players_list(4)
    for player_dict in players:
        assert player_dict == dict_4

def test_create_players_list_test_dictionary():
    """Test für den speziellen Testfall number=123"""
    players = create_players_list(123)
    for player_dict in players:
        assert player_dict == dict_test