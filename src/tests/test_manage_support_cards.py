import pytest
from unittest.mock import patch, MagicMock

# Module importieren
from frontend.manage_support_cards import add_support_card, get_support_cards, remove_support_card


# --------------------------
# Globale Mocks für GUI + Bilder
# --------------------------
@pytest.fixture(autouse=True)
def mock_gui_elements():
    with patch("frontend.manage_support_cards.CTk", MagicMock()), \
            patch("frontend.manage_support_cards.Frame", MagicMock()), \
            patch("frontend.manage_support_cards.CTkLabel", MagicMock()), \
            patch("frontend.manage_support_cards.Image.open", MagicMock(return_value=MagicMock(width=300, height=300))), \
            patch("frontend.manage_support_cards.ImageTk.PhotoImage",
                  MagicMock(return_value=MagicMock(pil_image="mock_card"))):
        yield


# --------------------------
# Fixture: virtuelles Root-Fenster (Mock)
# --------------------------
@pytest.fixture
def root_window():
    root = MagicMock()
    # Jeder Spieler hat ein "Frame" für die Schweine
    root.nametowidget.side_effect = lambda name: MagicMock(winfo_children=lambda: [], name=name)
    return root


# --------------------------
# TEST 1: add_support_card fügt Karte korrekt hinzu (gibt nicht -1 zurück)
# --------------------------
def test_add_support_card_creates_card(root_window):
    result = add_support_card(root_window, player=1, pig=1, action_card="Stallkarte")
    assert result != -1



# --------------------------
# TEST 2: remove_support_card ruft destroy auf
# --------------------------
def test_remove_support_card_mocked():
    player = 1
    pig = 1
    action_card = "Stallkarte"

    # Mock root_window
    root_window = MagicMock()

    # Mock Frame des Schweins
    subwidget_1 = MagicMock()
    subwidget_1.cget.return_value.pil_image = "Stallkarte.png"
    subwidget_1.destroy = MagicMock()

    subwidget_2 = MagicMock()
    subwidget_2.cget.return_value.pil_image = "Matschkarte.png"
    subwidget_2.destroy = MagicMock()

    support_frame = MagicMock()
    support_frame.winfo_children.return_value = [subwidget_1, subwidget_2]
    support_frame.__str__.return_value = f".!ctktoplevel.pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}"
    support_frame.destroy = MagicMock()

    # Mock Frame des Spielers
    pigs_frame = MagicMock()
    pigs_frame.winfo_children.return_value = [support_frame]

    # nametowidget auf root_window mocken
    root_window.nametowidget.return_value = pigs_frame

    # Aufruf der Funktion
    remove_support_card(root_window, player, pig, action_card)

    # Assertions
    # Das richtige Support-Card-Widget wurde zerstört
    subwidget_1.destroy.assert_called_once()
    # Das andere Widget bleibt unberührt
    subwidget_2.destroy.assert_not_called()
    # Da noch ein Subwidget übrig ist, wird das Frame NICHT zerstört
    support_frame.destroy.assert_not_called()
    # Prüfen, dass nametowidget korrekt aufgerufen wurde
    root_window.nametowidget.assert_called_once_with(f"pigs_player_{player}")





# --------------------------
# TEST 3: get_support_cards liefert Liste mit Karten
# --------------------------
def test_get_support_cards_mocked():
    player = 1
    pig = 1

    # Mock root_window
    root_window = MagicMock()
    root_window.update = MagicMock()

    # Mock Frame für die Support Cards eines Schweins
    support_card_1 = MagicMock()
    support_card_1.cget.return_value.pil_image = "image1"
    support_card_2 = MagicMock()
    support_card_2.cget.return_value.pil_image = "image2"

    support_frame = MagicMock()
    support_frame.winfo_children.return_value = [support_card_1, support_card_2]
    # __str__ so setzen, dass der Vergleich in der Funktion passt
    support_frame.__str__.return_value = f".!ctktoplevel.pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}"

    # Mock Frame des Spielers
    pigs_frame = MagicMock()
    pigs_frame.winfo_children.return_value = [support_frame]

    # Mock nametowidget auf root_window
    root_window.nametowidget.return_value = pigs_frame

    # Aufruf der Funktion
    result = get_support_cards(root_window, player, pig)

    # Assertions
    assert len(result) == 2
    assert result[0] == "image1"
    assert result[1] == "image2"

    # Prüfen, dass update und nametowidget aufgerufen wurden
    root_window.update.assert_called_once()
    root_window.nametowidget.assert_called_once_with(f"pigs_player_{player}")
