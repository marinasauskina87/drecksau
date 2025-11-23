from tkinter import Frame
from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

import config

def add_support_card(root_window, player, pig, action_card):
    player = int(player)
    pig = int(pig)

    frame_exist = False
    pigs_of_player = root_window.nametowidget(f"pigs_player_{player}")
    for widget in pigs_of_player.winfo_children():
        if str(widget) == f".pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}":
            frame_support_cards = widget
            frame_exist = True
    if not frame_exist:
        frame_support_cards = Frame(pigs_of_player, bg="#242424", name=f"frame_support_cards_player_{player}_pig_{pig}")
    
    img_action_card = Image.open(f"images/{action_card}.png")
    # Resize it (make it three times smaller)
    pil_img_action_card = img_action_card.resize((int(img_action_card.width / 3), int(img_action_card.height / 3)), Image.Resampling.LANCZOS)
    resized_photo_rot = pil_img_action_card.rotate(config.positions[player-1][3], expand=True)
    resized_photo = ImageTk.PhotoImage(resized_photo_rot)
    resized_photo.pil_image = action_card
    
    gustav = CTkLabel(frame_support_cards, text="", bg_color="transparent", image=resized_photo)
    if (config.positions[player-1][3] % 180 == 0):
        gustav.grid(column=len(frame_support_cards.winfo_children())-1, row=0)
    else:
        gustav.grid(row=len(frame_support_cards.winfo_children())-1, column=0)
    
    if (config.positions[player-1][3] % 180 == 0):
        frame_support_cards.grid(row=0, column=pig-1, sticky=config.positions[player-1][2]) 
    else:
        frame_support_cards.grid(row=pig-1, column=0, sticky=config.positions[player-1][2])

def remove_support_card(root_window, player, pig, action_card):
    """
    f.e. root, 2, 2, "Stallkarte"
    """
    pigs_of_player = root_window.nametowidget(f"pigs_player_{player}")
    for widget in pigs_of_player.winfo_children():
        if str(widget) == f".pigs_player_{player}.frame_support_cards_player_{player}_pig_{pig}":
            # widget ist das frame
            for subwidget in widget.winfo_children():
                print(subwidget)
                print(subwidget.cget("image").pil_image)
                if (subwidget.cget("image").pil_image.split('.')[0] == action_card):
                    subwidget.destroy()
            if len(widget.winfo_children()) == 0:
                widget.destroy()