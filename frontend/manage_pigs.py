import config
from customtkinter import *
from tkinter import Frame
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

def prepare_pig_image(player, pig_state):
    # Image-Path can be accessed by "img_pig.filename"
    img_pig = Image.open(f"images/{pig_state}.png")
    rez_img_pig = img_pig.resize((int(img_pig.width*0.8), int(img_pig.height*0.8)))

    rez_img_pig_rot = rez_img_pig.rotate(config.positions[player][3], expand=True)

    widget_img_pig = ImageTk.PhotoImage(rez_img_pig_rot)

    return widget_img_pig

def add_pigs(root_window):
    pigs_per_player = {
        2: 5,
        3: 4,
        4: 3
    }
    amount_of_pigs = pigs_per_player[config.amount_of_players]

    for player in range(config.amount_of_players):
        group_of_pigs = Frame(root_window, bg="#242424", name=f"pigs_player_{player+1}")
        group_of_pigs.grid(row=config.positions[player][0], column=config.positions[player][1], sticky=config.positions[player][2])
        
        font = ImageFont.truetype("arial.ttf", 40)
        width, height = 150, 50

        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), f"Player {player+1}", fill="white", font=font)
        if config.positions[player][2] == "s":
            tk_img = ImageTk.PhotoImage(img)
            lbl = CTkLabel(root_window, image=tk_img, text="")
            lbl.grid(row=4, column=2, sticky="new")
        elif config.positions[player][2] == "n":
            tk_img = ImageTk.PhotoImage(img)
            lbl = CTkLabel(root_window, image=tk_img, text="")
            lbl.grid(row=0, column=2, sticky="s")
        elif config.positions[player][2] == "w":
            print("hi")
            img = img.rotate(270, expand=True)
            tk_img = ImageTk.PhotoImage(img)
            lbl = CTkLabel(root_window, image=tk_img, text="")
            lbl.grid(row=2, column=0, sticky="nse")
        else:
            img = img.rotate(90, expand=True)
            tk_img = ImageTk.PhotoImage(img)
            lbl = CTkLabel(root_window, image=tk_img, text="")
            lbl.grid(row=2, column=4, sticky="nsw")

        for pig in range(amount_of_pigs):
            btn = CTkButton(group_of_pigs, text="", image=prepare_pig_image(player, "Sauberschwein"), fg_color="transparent", width=0, state="disabled")
            if (config.positions[player][3] % 180 == 0):
                btn.grid(column=pig, row=0)
            else:
                btn.grid(row=pig, column=0)
        
    return root_window

def change_state_pig(root_window, player, pig, new_state):
    if new_state == "dirty":
        new_img_widget = prepare_pig_image(player-1, "Dreckssau")
    else:
        new_img_widget = prepare_pig_image(player-1, "Sauberschwein")
    
    frame = root_window.nametowidget(f"pigs_player_{player}")

    widget = frame.winfo_children()[int(pig)-1]
    widget.configure(image = new_img_widget)

