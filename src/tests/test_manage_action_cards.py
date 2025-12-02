import pytest
from unittest.mock import MagicMock, patch
from frontend.manage_action_cards import (
    create_frame,
    choose_random_card,
    draw_cards,
    clear_action_cards,
    show_action_cards,
    is_waste_button_visible
)


# --------------------------
# TEST: create_frame
# --------------------------
@patch("frontend.manage_action_cards.Frame")
def test_create_frame(mock_frame):
    root = MagicMock()
    frame_instance = MagicMock()
    mock_frame.return_value = frame_instance

    create_frame(root)

    mock_frame.assert_called_once_with(root, bg="#242424", name="action_cards")
    frame_instance.grid.assert_called_once_with(row=2, column=2)


# --------------------------
# TEST: choose_random_card
# --------------------------
@patch("frontend.manage_action_cards.random.choice", return_value="Blitzkarte")
@patch("frontend.manage_action_cards.config")
def test_choose_random_card(mock_config, mock_choice):
    # Setup card deck
    mock_config.card_deck = [
        ["Blitzkarte", 2],
        ["Matschkarte", 1],
    ]

    result = choose_random_card()

    assert result[0] == "Blitzkarte"
    assert result[1] == 1  # count gets reduced by one


# --------------------------
# TEST: draw_cards
# --------------------------
@patch("frontend.manage_action_cards.choose_random_card")
def test_draw_cards(mock_choose):
    mock_choose.side_effect = [
        ["Blitzkarte", 1],
        ["Matschkarte", 1],
    ]

    cards = {"player-1": []}

    result = draw_cards(1, 2, cards)

    assert result["player-1"] == ["Blitzkarte", "Matschkarte"]


# --------------------------
# TEST: clear_action_cards
# --------------------------
def test_clear_action_cards():
    frame = MagicMock()
    w1 = MagicMock()
    w2 = MagicMock()
    frame.winfo_children.return_value = [w1, w2]

    clear_action_cards(frame)

    w1.destroy.assert_called_once()
    w2.destroy.assert_called_once()


# --------------------------
# TEST: show_action_cards
# --------------------------
@patch("frontend.manage_action_cards.CTkButton")
@patch("frontend.manage_action_cards.CTkLabel")
@patch("frontend.manage_action_cards.ImageTk.PhotoImage")
@patch("frontend.manage_action_cards.Image.open")
def test_show_action_cards(mock_open, mock_photo, mock_label, mock_button):
    root = MagicMock()
    frame = MagicMock()
    root.nametowidget.return_value = frame

    # Mock image + resize
    mock_img = MagicMock()
    resized = MagicMock()
    mock_img.resize.return_value = resized
    mock_open.return_value = mock_img

    # PhotoImage mock
    mock_photo.return_value = MagicMock()   # <-- WICHTIG!

    player_cards = {"player-1": ["Blitzkarte", "Matschkarte"]}

    show_action_cards(root, player_cards, 1)

    # Assertions
    root.nametowidget.assert_called_with("action_cards")
    frame.configure.assert_called_with(bg="#DDDDDD")

    # Label erzeugt?
    assert mock_label.call_count == 1

    # Buttons erzeugt?
    assert mock_button.call_count == 4  # 2 Karten + Withdraw + Waste Buttons

    # Images geladen?
    assert mock_open.call_count == 2
    mock_photo.assert_called()


# --------------------------
# TEST: is_waste_button_visible
# --------------------------
def test_is_waste_button_visible():
    btn1 = MagicMock()
    btn1.__class__.__name__ = "CTkButton"
    btn1.flag = "waste_btn"

    btn2 = MagicMock()
    btn2.__class__.__name__ = "CTkButton"
    btn2.flag = "other"

    frame = MagicMock()
    frame.winfo_children.return_value = [btn1, btn2]

    # make visible
    is_waste_button_visible(frame, True)
    btn1.grid.assert_called_once()

    # hide again
    btn1.grid.reset_mock()
    btn1.grid_remove.reset_mock()

    is_waste_button_visible(frame, False)
    btn1.grid_remove.assert_called_once()
