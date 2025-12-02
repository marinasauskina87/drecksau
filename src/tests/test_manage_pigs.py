import pytest
from unittest.mock import MagicMock, patch
from frontend.manage_pigs import prepare_pig_image, add_pigs, change_state_pig


# -------------------------------------------------------------------
# Test prepare_pig_image
# -------------------------------------------------------------------
@patch("frontend.manage_pigs.ImageTk.PhotoImage")
@patch("frontend.manage_pigs.Image.open")
@patch("frontend.manage_pigs.config")
def test_prepare_pig_image(mock_config, mock_image_open, mock_photoimage):
    # Mock config
    mock_config.amount_of_players = 2
    mock_config.get_positions.return_value = [(0, 0, "s", 0), (0, 1, "n", 90)]

    # Mock Image object
    mock_img = MagicMock()
    mock_img.width = 100
    mock_img.height = 100
    mock_img.resize.return_value = mock_img
    mock_img.rotate.return_value = mock_img
    mock_image_open.return_value = mock_img

    result = prepare_pig_image(0, "Sauberschwein", 1440, 900)

    mock_image_open.assert_called_once_with("frontend/images/Sauberschwein.png")
    mock_img.resize.assert_called()
    mock_img.rotate.assert_called()
    mock_photoimage.assert_called_once_with(mock_img)
    assert result == mock_photoimage.return_value


# -------------------------------------------------------------------
# Test add_pigs
# -------------------------------------------------------------------
@patch("frontend.manage_pigs.ImageTk.PhotoImage", return_value="mock_photo")
@patch("frontend.manage_pigs.prepare_pig_image", return_value="mock_img")
@patch("frontend.manage_pigs.CTkButton")
@patch("frontend.manage_pigs.CTkLabel")
@patch("frontend.manage_pigs.Frame")
@patch("frontend.manage_pigs.config")
def test_add_pigs(mock_config, mock_frame, mock_label, mock_button, mock_prepare_img, mock_photo):
    # Setup config
    mock_config.amount_of_players = 2
    mock_config.pigs_per_player = {2: 2}
    mock_config.get_positions.return_value = [(0, 0, "s", 0), (0, 1, "n", 90)]

    root_window = MagicMock()
    root_window.update = MagicMock()

    # >>>>>>>>>>>>>> IMPORTANT FIX <<<<<<<<<<<<<<
    # Ensure Frame().winfo_width() and winfo_height() return real ints
    frame_instance = MagicMock()
    frame_instance.winfo_width.return_value = 200
    frame_instance.winfo_height.return_value = 100
    mock_frame.return_value = frame_instance
    # >>>>>>>>>>>>>> END FIX <<<<<<<<<<<<<<

    result = add_pigs(root_window)

    assert mock_frame.call_count == 2
    assert mock_button.call_count == 4
    assert mock_label.call_count == 2
    root_window.update.assert_called()
    assert result == root_window


# -------------------------------------------------------------------
# Test change_state_pig
# -------------------------------------------------------------------
@patch("frontend.manage_pigs.prepare_pig_image", return_value="new_img")
def test_change_state_pig(mock_prepare_img):
    root_window = MagicMock()

    # Mock Frame und Button
    frame_mock = MagicMock()
    button_mock = MagicMock()
    frame_mock.winfo_children.return_value = [button_mock]

    root_window.nametowidget.return_value = frame_mock

    change_state_pig(root_window, player=1, pig=1, new_state="clean")

    mock_prepare_img.assert_called_once_with(0, "Sauberschwein", root_window.winfo_screenwidth(),
                                             root_window.winfo_screenheight())
    button_mock.configure.assert_called_once_with(image="new_img")


# Optional: Test falscher Zustand
def test_change_state_pig_wrong_state():
    root_window = MagicMock()
    result = change_state_pig(root_window, player=1, pig=1, new_state="invalid")
    assert result == "Wrong state: invalid"