from customtkinter import *
from CTkMessagebox import CTkMessagebox
import tkinter
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

# Hard-Coded config variables
card_deck = [["Matschkarte", 21], #21
             ["Regenkarte", 4], #4
             ["Stallkarte", 9], #9
             ["Blitzkarte", 4], #4
             ["Blitzableiterkarte", 4], #4
             ["Bauer-schrubbt-die-Sau-Karte", 8], #8
             ["Bauer-ärgere-dich-Karte", 4], #4
             ["Tornadokarte", 2]] #2

played_cards = []

amount_of_players = 4

pigs_per_player = {
    2: 5,
    3: 4,
    4: 3
}

state_to_card = {
    "dirty": "Matschkarte",
    "clean": "Bauer-schrubbt-die-Sau-Karte",
    "stable": "Stallkarte",
    "locked": "Bauer-ärgere-dich-Karte",
    "current_arrester": "Blitzableiterkarte",
    "flash": "Blitzkarte"
}

status_cards = ["Matschkarte"]
actional_cards = ["Blitzkarte", "Bauer-schrubbt-die-Sau-Karte"]
support_cards = ["Stallkarte", "Blitzableiterkarte", "Bauer-ärgere-dich-Karte"]

def pop_up_amount_of_player():
    global amount_of_players
    msg_amount_players = CTkMessagebox(title="Welcome! :D", message="With how many players do you want to play?", icon="question", option_1="2", option_2="3", option_3="4")
    amount_of_players = int(msg_amount_players.get())

def create_frame_statistics(root_window):
    frame_stats = tkinter.Frame(root_window, name="statistics", bg="grey")
    lbl_title_stats = CTkLabel(frame_stats, text="STATISTICS:")
    lbl_title_stats.grid(row=0)
    for index, card in enumerate(card_deck):
        lbl_stat = CTkLabel(frame_stats, text=f"{card[0]}: {played_cards.count(card[0])}")
        lbl_stat.grid(row=index+1, padx=5)
    frame_stats.grid(column=4, row=1, rowspan=5, sticky="e")

def update_frame_statistics(root_window):
    frame = root_window.nametowidget("statistics")
    for lbl in frame.winfo_children():
        if not (lbl.cget("text") == "STATISTICS:"):
            played_card = lbl.cget("text").split(":")[0]
            lbl.configure(text=f"{played_card}: {played_cards.count(played_card)}")

def close_application():
    tkinter._default_root.destroy()

def configure_board():
    # Will represent the main window
    root = CTkToplevel()
    root.protocol("WM_DELETE_WINDOW", close_application)

    # Fullscreen
    width = root.winfo_screenwidth()    
    height = root.winfo_screenheight()            
    root.geometry(f"{width}x{height}")
    print("Your window will be scaled on the computer size:", width, "-", height)
    root.update()
    
    # Part the grid in 5 rows and 5 columns (equally thick)
    for index in range(5):
        root.grid_columnconfigure(index, weight=1)
        root.grid_rowconfigure(index, weight=1)

    # Background picture:
    background_img = Image.open("frontend/images/Hintergrund.jpg")
    background_img = background_img.resize((root.winfo_width(), root.winfo_height()))
    photo_background_img = ImageTk.PhotoImage(background_img)
    
    lbl_background_img = CTkLabel(root, image=photo_background_img, text="")
    lbl_background_img.image=photo_background_img
    lbl_background_img.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="nsew")

    root.update()

    return root

def configure_player_card_dictionary(amount_of_players):
    # Create one dictionary which has the player-name as key and player-cards as value (in list)
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

def get_positions(amount_of_players):
    positions = {}
    if amount_of_players == 2:
        # positions = [row, column, sticky, rotation]
        positions = {
            0: [3, 2, "s", 0], # down (player 1)
            1: [1, 2, "n", 180], # top (player 2/3)
        }
    else:
        # positions = [row, column, sticky, rotation]
        positions = {
            0: [3, 2, "s", 0], # down (player 1)
            1: [2, 1, "w", -90], # left (player 2/3)
            2: [1, 2, "n", 180], # top (player 2/3)
            3: [2, 3, "e", 90]  # right (player 4)
        }
    return positions