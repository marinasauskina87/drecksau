from tkinter import Frame
from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

import frontend.config as config

def add_support_card(root_window, player, pig, action_card):
    positions = config.get_positions(config.amount_of_players)
    player = int(player)
    pig = int(pig)

    # Get (if non existent: create) a frame for support_cards for the specific pig
    frame_exist = False
    pigs_of_player = root_window.nametowidget(f"pigs_player_{player}")
    for widget in pigs_of_player.winfo_children():
        if str(widget) == f".pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}":
            frame_support_cards = widget
            frame_exist = True
    if not frame_exist:
        frame_support_cards = Frame(pigs_of_player, bg="#242424", name=f"frame_support_cards_player_{player}_pig_{pig}")
    
    # If the frame already possesses this widget -> Return an error
    for widget in frame_support_cards.winfo_children():
        if widget.cget("image").pil_image.split('.')[0] == action_card:
            return -1
    
    ## Prepare image before adding it
    img_action_card = Image.open(f"frontend/images/{action_card}.png")
    # Resize it (make it three times smaller)
    pil_img_action_card = img_action_card.resize((int(img_action_card.width / 3), int(img_action_card.height / 3)), Image.Resampling.LANCZOS)
    # Rotate it
    resized_photo_rot = pil_img_action_card.rotate(positions[player-1][3], expand=True)
    resized_photo = ImageTk.PhotoImage(resized_photo_rot)
    # For later referencing
    resized_photo.pil_image = action_card
    
    lbl_support_card = CTkLabel(frame_support_cards, text="", bg_color="transparent", image=resized_photo)
    # If the player is either on top (P.2/3) or on the bottom (P.1)
    if (positions[player-1][3] % 180 == 0):
        lbl_support_card.grid(column=len(frame_support_cards.winfo_children())-1, row=0)
    else:
        lbl_support_card.grid(row=len(frame_support_cards.winfo_children())-1, column=0)
    
    if (positions[player-1][3] % 180 == 0):
        frame_support_cards.grid(row=0, column=pig-1, sticky=positions[player-1][2]) 
    else:
        frame_support_cards.grid(row=pig-1, column=0, sticky=positions[player-1][2])

def get_support_cards(root_window, player, pig):
    list_of_support_cards = []
    # Get frame which contains all the pigs of a player
    pigs_of_player = root_window.nametowidget(f"pigs_player_{player}")
    for widget in pigs_of_player.winfo_children():
        # If the selected pig already has a frame for the support cards
        if str(widget) == f".pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}":
            for support_card in widget.winfo_children():
                # Add every support card to a list
                list_of_support_cards.append(support_card.cget("image").pil_image)
    return list_of_support_cards


def remove_support_card(root_window, player, pig, action_card):
    """
    f.e. root, 2, 2, "Stallkarte"
    """
    # Get frame which contains all the pigs of a player
    pigs_of_player = root_window.nametowidget(f"pigs_player_{player}")
    for widget in pigs_of_player.winfo_children():
        if str(widget) == f".pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}":
            # Widget is the frame with the support cards of a certain pig
            for subwidget in widget.winfo_children():
                # If the action_card is in the list of support cards for this pig:
                # Remove it
                if (subwidget.cget("image").pil_image.split('.')[0] == action_card):
                    subwidget.destroy()
                # It doesn't need an else as this method only gets called in rare and controlled environments
            # Keep widget-control in removing unneccessary widgets
            if len(widget.winfo_children()) == 0:
                widget.destroy()