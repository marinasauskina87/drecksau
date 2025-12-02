import pytest
from unittest.mock import patch

from logik.check_action_withdraw_cards import check_withdraw_cards


# ------------------------------------------------------------------------
# Testdaten (für alle Tests gleich)
# ------------------------------------------------------------------------

dict_test = {
    'pig_1': 'clean,',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, current_arrester',
    'pig_4': 'dirty, stable, locked, current_arrester '
}


@pytest.fixture
def pigs_all_players():
    """
    Zwei Spieler, beide mit identischem Schweine-Dictionary.
    """
    return [
        dict_test.copy(),  # Spieler 1
        dict_test.copy(),  # Spieler 2
    ]


# ------------------------------------------------------------------------
# TEST 1: Mindestens EINE Statuskarte ist spielbar  return 0
# Beispiel: "Matschkarte"
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.check_action_dirty", return_value=0)
@patch("logik.check_action_withdraw_cards.config")
def test_playable_status_card(mock_config, mock_dirty, pigs_all_players):
    mock_config.status_cards = ["Matschkarte"]
    mock_config.support_cards = []

    cards = ["Matschkarte", "irgendeine", "karte"]

    result = check_withdraw_cards(cards, pigs_all_players, current_player=1)

    assert result == 0
    mock_dirty.assert_called()


# ------------------------------------------------------------------------
# TEST 2: Statuskarte NICHT spielbar  return 1
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.check_action_dirty", return_value=1)
@patch("logik.check_action_withdraw_cards.config")
def test_status_card_not_playable(mock_config, mock_dirty, pigs_all_players):
    mock_config.status_cards = ["Matschkarte"]
    mock_config.support_cards = []

    cards = ["Matschkarte"]

    result = check_withdraw_cards(cards, pigs_all_players, current_player=1)

    assert result == 1
    mock_dirty.assert_called()


# ------------------------------------------------------------------------
# TEST 3: Offensivkarte "Blitzkarte" spielbar  return 0
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.check_action_flash", return_value=0)
@patch("logik.check_action_withdraw_cards.config")
def test_flash_card_playable(mock_config, mock_flash, pigs_all_players):
    mock_config.status_cards = []
    mock_config.support_cards = []

    cards = ["Blitzkarte"]

    result = check_withdraw_cards(cards, pigs_all_players, current_player=1)

    assert result == 0
    mock_flash.assert_called()


# ------------------------------------------------------------------------
# TEST 4: Offensivkarte NICHT spielbar  return 1
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.check_action_flash", return_value=1)
@patch("logik.check_action_withdraw_cards.config")
def test_flash_card_not_playable(mock_config, mock_flash, pigs_all_players):
    mock_config.status_cards = []
    mock_config.support_cards = []

    cards = ["Blitzkarte"]

    result = check_withdraw_cards(cards, pigs_all_players, current_player=1)

    assert result == 1
    mock_flash.assert_called()


# ------------------------------------------------------------------------
# TEST 5: "Tornadokarte" und "Regenkarte" sind immer spielbar  return 0
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.config")
def test_tornado_and_rain_always_work(mock_config, pigs_all_players):
    mock_config.status_cards = []
    mock_config.support_cards = []

    assert check_withdraw_cards(["Tornadokarte"], pigs_all_players, 1) == 0
    assert check_withdraw_cards(["Regenkarte"], pigs_all_players, 1) == 0


# ------------------------------------------------------------------------
# TEST 6: Keine der 3 Karten ist spielbar  return 1
# ------------------------------------------------------------------------

@patch("logik.check_action_withdraw_cards.config")
def test_no_card_playable(mock_config, pigs_all_players):
    mock_config.status_cards = []
    mock_config.support_cards = []

    # Keine Checkfunktion wird gemockt alle liefern implizit NICHT 0
    cards = ["Blitzkarte", "Blitzkarte", "Blitzkarte"]

    result = check_withdraw_cards(cards, pigs_all_players, current_player=1)

    assert result == 1