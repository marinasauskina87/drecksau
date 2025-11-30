from customtkinter import *
from tkinter import Frame
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

import frontend.config as config


def prepare_pig_image(player, pig_state):
    positions = config.get_positions(config.amount_of_players)

    # Image-Path can be accessed by "img_pig.filename"
    img_pig = Image.open(f"frontend/images/{pig_state}.png")
    rez_img_pig = img_pig.resize((int(img_pig.width*0.8), int(img_pig.height*0.8)))
    rez_img_pig_rot = rez_img_pig.rotate(positions[player][3], expand=True)
    widget_img_pig = ImageTk.PhotoImage(rez_img_pig_rot)

    return widget_img_pig

def add_pigs(root_window):
    amount_of_pigs = config.pigs_per_player[config.amount_of_players]
    positions = config.get_positions(config.amount_of_players)
    background_color_pigs = "violet"

    for player in range(config.amount_of_players):
        group_of_pigs = Frame(root_window, bg=background_color_pigs, name=f"pigs_player_{player+1}")
        group_of_pigs.grid(row=positions[player][0], column=positions[player][1], sticky=positions[player][2])

        for pig in range(amount_of_pigs):
            btn_pig = CTkButton(group_of_pigs, text="", image=prepare_pig_image(player, "Sauberschwein"), fg_color="transparent", width=0, state="disabled")
            # Needed for an faster recognition of the selected pig
            btn_pig.flag = pig+1
            if (positions[player][3] % 180 == 0):
                btn_pig.grid(column=pig, row=0)
            else:
                btn_pig.grid(row=pig, column=0)
        
        # Needed to get the correct and updated widths of the widgets
        root_window.update()

        font_lbl_player = ImageFont.truetype("arial.ttf", 40)
        ## Horizontal image
        img_lbl_player_hor = Image.new("RGBA", (group_of_pigs.winfo_width(), 50), background_color_pigs)
        draw_lbl_player_hor = ImageDraw.Draw(img_lbl_player_hor)
        # Calculation from ChatGPT (based on pixel-width, amount of characters in string and scaling due to fontsize)
        draw_lbl_player_hor.text(((img_lbl_player_hor.width-(0.4 * 40 * len("Player X")))/2, 0), f"Player {player+1}", fill="white", font=font_lbl_player)
        
        ## Vertical image
        img_lbl_player_ver = Image.new("RGBA", (group_of_pigs.winfo_height(), 50), background_color_pigs)
        draw_lbl_player_ver = ImageDraw.Draw(img_lbl_player_ver)
        # Calculation from ChatGPT (based on pixel-width, amount of characters in string and scaling due to fontsize)
        draw_lbl_player_ver.text(((img_lbl_player_ver.width-(0.4 * 40 * len("Player X")))/2, 0), f"Player {player+1}", fill="white", font=font_lbl_player)

        # Due to the differentiation of vertical and horizontal and the different sticky-attributes than the
        # config-file, we can't simplify the code below
        if positions[player][2] == "s":
            tk_img_lbl_player = ImageTk.PhotoImage(img_lbl_player_hor)
            lbl_player = CTkLabel(root_window, image=tk_img_lbl_player, text="", fg_color=background_color_pigs)
            lbl_player.grid(row=4, column=2, sticky="n")
        elif positions[player][2] == "n":
            tk_img_lbl_player = ImageTk.PhotoImage(img_lbl_player_hor)
            lbl_player = CTkLabel(root_window, image=tk_img_lbl_player, text="", fg_color=background_color_pigs)
            lbl_player.grid(row=0, column=2, sticky="s")
        elif positions[player][2] == "w":
            # Rotate it due to verticality
            img_lbl_player_ver = img_lbl_player_ver.rotate(270, expand=True)
            tk_img_lbl_player = ImageTk.PhotoImage(img_lbl_player_ver)
            lbl_player = CTkLabel(root_window, image=tk_img_lbl_player, text="")
            lbl_player.grid(row=2, column=0, sticky="e")
        else:
            # Rotate it due to verticality
            img_lbl_player_ver = img_lbl_player_ver.rotate(90, expand=True)
            tk_img_lbl_player = ImageTk.PhotoImage(img_lbl_player_ver)
            lbl_player = CTkLabel(root_window, image=tk_img_lbl_player, text="", anchor="center")
            lbl_player.grid(row=2, column=4, sticky="w")
        
    return root_window

def change_state_pig(root_window, player, pig, new_state):
    player = int(player)
    if new_state == "dirty":
        new_img_widget = prepare_pig_image(player-1, "Dreckssau")
    elif new_state == "clean":
        new_img_widget = prepare_pig_image(player-1, "Sauberschwein")
    else:
        return f"Wrong state: {new_state}"
    
    frame = root_window.nametowidget(f"pigs_player_{player}")

    # Change image of selected file (-1 due to zero-indexing)
    widget = frame.winfo_children()[int(pig)-1]
    widget.configure(image = new_img_widget)

