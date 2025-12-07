import pytest
from unittest.mock import MagicMock, patch
import frontend.config as config

# -------------------------------
# Test pop_up_amount_of_player
# -------------------------------
@patch("frontend.config.CTkMessagebox")
def test_pop_up_amount_of_player(mock_msgbox):
    mock_instance = MagicMock()
    mock_instance.get.return_value = "3"
    mock_msgbox.return_value = mock_instance

    config.pop_up_amount_of_player()
    assert config.amount_of_players == 3
    mock_msgbox.assert_called_once()


# -------------------------------
# Test create_frame_statistics
# -------------------------------
@patch("frontend.config.CTkLabel")
@patch("frontend.config.tkinter.Frame")
def test_create_frame_statistics(mock_frame, mock_label):
    root = MagicMock()
    config.played_cards.clear()
    frame_instance = MagicMock()
    mock_frame.return_value = frame_instance

    config.create_frame_statistics(root)

    mock_frame.assert_called_once_with(root, name="statistics", bg="grey")
    assert mock_label.call_count == len(config.card_deck) + 1  # Title + cards
    frame_instance.grid.assert_called_once()


# -------------------------------
# Test update_frame_statistics
# -------------------------------
@patch("frontend.config.CTkLabel")
def test_update_frame_statistics(mock_label):
    root = MagicMock()
    label_title = MagicMock()
    label_card = MagicMock()
    label_card.cget.return_value = "Matschkarte: 0"
    frame = MagicMock()
    frame.winfo_children.return_value = [label_title, label_card]
    root.nametowidget.return_value = frame

    config.played_cards.append("Matschkarte")
    config.update_frame_statistics(root)

    label_card.configure.assert_called_with(text="Matschkarte: 1")


# -------------------------------
# Test close_application
# -------------------------------
@patch("frontend.config.tkinter._default_root")
def test_close_application(mock_root):
    config.close_application()
    mock_root.destroy.assert_called_once()



# -------------------------------
# Test configure_player_card_dictionary
# -------------------------------
def test_configure_player_card_dictionary():
    d = config.configure_player_card_dictionary(3)
    assert d == {"player-1": [], "player-2": [], "player-3": []}


# -------------------------------
# Test configure_current_player
# -------------------------------
def test_configure_current_player():
    config.amount_of_players = 4
    assert config.configure_current_player(0) == 1
    assert config.configure_current_player(2) == 3  # edge case


# -------------------------------
# Test get_positions
# -------------------------------
def test_get_positions_2_players():
    pos = config.get_positions(2)
    assert len(pos) == 2
    assert pos[0] == [3, 2, "s", 0]

def test_get_positions_4_players():
    pos = config.get_positions(4)
    assert len(pos) == 4
    assert pos[3] == [2, 3, "e", 90]
