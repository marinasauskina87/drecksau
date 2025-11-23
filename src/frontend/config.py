from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

card_deck = [["Matschkarte", 21], #21
             ["Regenkarte", 4], #4
             ["Stallkarte", 9], #9
             ["Blitzkarte", 4], #4
             ["Blitzableiterkarte", 4], #4
             ["Bauer-schrubbt-die-Sau-Karte", 8], #8
             ["Bauer-ärgere-dich-Karte", 4]] #4

amount_of_players = 4

positions = {
    0: [3, 2, "s", 0], # down (player 1)
    1: [1, 2, "n", 180], # top (player 2/3)
    2: [2, 1, "w", -90], # left (player 2/3)
    3: [2, 3, "e", 90]  # right (player 4)
}

status_cards = ["Matschkarte"]
actional_cards = ["Regenkarte", "Blitzkarte", "Bauer-schrubbt-die-Sau-Karte"]
support_cards = ["Stallkarte", "Blitzableiterkarte", "Bauer-ärgere-dich-Karte"]

def configure_board():
    # Will represent the main window
    root = CTk()

    # TODO: Background
    # image = Image.open("images/Hintergrund.jpg")
    # photo = ImageTk.PhotoImage(image)
    # label = CTkLabel(root, image=photo)
    # label.grid(row=0, column=0, rowspan=4, columnspan=4)

    # Fullscreen
    width = root.winfo_screenwidth()               
    height = root.winfo_screenheight()               
    root.geometry(f"{width}x{height}")
    
    # Part the grid in 5 rows and 5 columns (equally thick)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_columnconfigure(4, weight=1)
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    return root

def configure_player_card_dictionary(amount_of_players):
    player_card_dict = {}
    for player in range(amount_of_players):
        player_card_dict[f"player-{player+1}"] = []
    return player_card_dict

def configure_current_player(current_player):
    current_player += 1
    if current_player != amount_of_players:
        return (current_player % amount_of_players)
    else:
        return current_player