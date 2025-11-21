from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support
import random
from tkinter import Frame

import config
import manage_pigs
import manage_action_cards
import manage_support_cards

def parse_widget_to_pig_location(widget):
    """
    Returns firstly 
    """
    return_values = {
        "player_number": 0,
        "pig_number": 0
    }
    for part_of_name in str(widget).split('.'):
        if "pigs_player" in part_of_name:
            return_values["player_number"] = part_of_name[-1]
        elif "ctkbutton" in part_of_name:
            if (part_of_name[-1] == 'n'):
                return_values["pig_number"] = 1
            else:
                return_values["pig_number"] = part_of_name[-1]
    return return_values

def setup_command_pigs(root_window):
    for player in range(config.amount_of_players):
        pigs = root_window.nametowidget(f".pigs_player_{player+1}")
        for pig in pigs.winfo_children():
            if (pig.__class__.__name__ == "CTkButton"):
                pig.configure(command=lambda button=pig: trigger_action(button))

def setup_command_action_card(root_window):
    action_cards = root_window.nametowidget(f".action_cards")
    for action_card in action_cards.winfo_children():
        action_card.configure(command=lambda button=action_card: deselect_action_cards(button))

def trigger_action(clicked_btn):
    # TODO: Change it as label
    global current_player

    # Get the selected action_card
    action_card_frame = root.nametowidget(f".action_cards")
    for action_card in action_card_frame.winfo_children():
        if action_card.cget("state") == "enabled":
            selected_pig = parse_widget_to_pig_location(clicked_btn)
            selected_pig_number = selected_pig["pig_number"]
            # For later implementation:
            print("SELECTED ACTION CARD:")
            print(action_card)
            print(action_card.cget("image").pil_image)
            print(action_card.cget("image").pil_image.split('.')[0])
            print("---------------------")
            print("SELECTED PIG:")
            print(selected_pig_number)
            print(clicked_btn.winfo_parent())
            print(clicked_btn)
            print("-------------------------")
            selected_action_card = action_card.cget("image").pil_image.split('.')[0]
            if (selected_action_card in config.status_cards):
                manage_pigs.change_state_pig(root, int(str(clicked_btn.winfo_parent())[-1]), selected_pig_number, "dirty")
            elif (selected_action_card in config.actional_cards):
                ## TODO: Implement logic
                print("actional")
            elif (selected_action_card in config.support_cards):
                ## TODO: Implement logic
                selected_player = selected_pig["player_number"]
                manage_support_cards.add_support_card(root, selected_player, selected_pig_number, selected_action_card)

    current_player = config.configure_current_player(current_player)
    enable_player_cards()
    manage_action_cards.show_action_cards(root, card_dict_players, current_player)
    setup_command_action_card(root)

    return None

def deselect_action_cards(button):
    enable_player_cards()

    # Remove the played card
    name_of_card = button.cget("image").pil_image.split('.')[0]
    for index, card in enumerate(card_dict_players[f"player-{current_player}"]):
        if card == name_of_card:
            card_dict_players[f"player-{current_player}"].pop(index)

    # Draw a card
    new_card = manage_action_cards.choose_random_card()
    card_dict_players[f"player-{current_player}"].append(new_card[0])

    # Disable all cards except the selected one
    frame = root.nametowidget(f".action_cards")
    for action_card in frame.winfo_children():
        if button == action_card:
            action_card.configure(state="enabled")
        else:
            action_card.configure(state="disabled")

def enable_player_cards():
    for player in range(config.amount_of_players):
        frame = root.nametowidget(f".pigs_player_{player+1}")
        children = frame.winfo_children()
        for widget in children:
            if not widget.__class__.__name__ == "Frame":
                widget.configure(state="enabled")

# -------------------------------------------------------------------------------
current_player = 1
card_dict_players = config.configure_player_card_dictionary(config.amount_of_players)

root = config.configure_board()

# TODO: Delete after final implementation
# Reason: Demonstration purposes 
btn = CTkButton(root, text="Delete", command=lambda: manage_support_cards.remove_support_card(root, 2, 2, "Stallkarte"))
btn.grid(row=0,column=0)

# GENERAL TODO: Experiment with the following:
# btn.flag = "Hallo"

# Pigs
root = manage_pigs.add_pigs(root)
setup_command_pigs(root)

# Action cards
for player in range(1,config.amount_of_players+1):
    manage_action_cards.draw_cards(player, 3, card_dict_players)

manage_action_cards.create_frame(root)
manage_action_cards.show_action_cards(root, card_dict_players, current_player)
setup_command_action_card(root)

root.mainloop()