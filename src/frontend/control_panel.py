from customtkinter import *

import frontend.config as config
import frontend.manage_pigs as manage_pigs
import frontend.manage_action_cards as manage_action_cards
import frontend.manage_support_cards as manage_support_cards

from backend.action_clean import action_clean
from backend.function_rain import action_rain
from backend.create_dictionary import create_dictionary
from backend.action_stable_open import action_stable_open
from backend.action_flash import action_flash
from backend.function_dirty import action_dirty
from backend.function_stable import action_stable
from backend.action_stable_locked import action_stable_locked
from backend.function_current_arrester import action_current_arrester
from backend.function_rain import action_rain
from backend.action_tornado import action_tornado

def update_UI(root_window, player_number, pig_number, player_dict):
    pigs = root_window.nametowidget(f".pigs_player_{int(player_number)}")
    chosen_pig = pigs.winfo_children()[int(pig_number)-1]
    states = player_dict[f'pig_{pig_number}']
    if "dirty" in states:
        manage_pigs.change_state_pig(root_window, player_number, pig_number, "dirty")
    elif "clean" in states:
        manage_pigs.change_state_pig(root_window, player_number, pig_number, "clean")
    if "stable" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Stallkarte")
    if "arrester" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Blitzableiterkarte")
    if "locked" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Bauer-ärgere-dich-Karte")

def parse_widget_to_pig_location(widget):
    """
    Helper function to receive the player-number and the pig-number of the selected pigs
    more gently 
    """
    return_values = {
        "player_number": 0,
        "pig_number": 0
    }
    for part_of_name in str(widget).split('.'):
        if "pigs_player" in part_of_name:
            return_values["player_number"] = part_of_name[-1]
        elif "ctkbutton" in part_of_name:
            return_values["pig_number"] = widget.flag
    return return_values

def setup_command_pigs(root_window):
    # During pig-button initialisation, the command-function (executed when clicked) couldn't
    # be initialised as it is in another module. Therefore, it is done here
    for player in range(1, config.amount_of_players+1):
        pigs = root_window.nametowidget(f".pigs_player_{player}")
        for pig in pigs.winfo_children():
            # As we just want to tackle the buttons and not the label "Player X"
            if (pig.__class__.__name__ == "CTkButton"):
                pig.configure(command=lambda button=pig: trigger_action(button))

def setup_command_action_card(root_window):
    # During action-card-button initialisation, the command-function (executed when clicked) couldn't
    # be initialised as it is in another module. Therefore, it is done here
    action_cards = root_window.nametowidget(f".action_cards")
    for action_card in action_cards.winfo_children():
        # As we just want to tackle the buttons and not the label "It's your turn..."
        if action_card.__class__.__name__ == "CTkButton":
            action_card.configure(command=lambda button=action_card: handle_action_card_selection(button))

def handle_played_action_card(current_player, played_card, card_dict_players):
    # Remove the played card
    for index, card in enumerate(card_dict_players[f"player-{current_player}"]):
        if card == played_card:
            card_dict_players[f"player-{current_player}"].pop(index)
    
    # Draw a card
    new_card = manage_action_cards.choose_random_card()
    card_dict_players[f"player-{current_player}"].append(new_card[0])
    return card_dict_players

def trigger_action(clicked_btn):
    # TODO: Change it as label
    global current_player

    # Get the selected action_card
    action_card_frame = root.nametowidget(f".action_cards")
    for action_card in action_card_frame.winfo_children():
        # Just select the selected action_card
        if action_card.__class__.__name__ == "CTkButton" and action_card.flag == "Selected":
            # Define entities
            selected_entity = parse_widget_to_pig_location(clicked_btn)
            selected_pig = selected_entity["pig_number"]
            selected_player = selected_entity["player_number"]
            selected_action_card = action_card.cget("image").pil_image.split('.')[0]
            selected_player_dict = globals()[f"dict_player_pigs_{selected_player}"]

            handle_played_action_card(current_player, selected_action_card, card_dict_players)

            # If a status card has been played:
            if (selected_action_card in config.status_cards):
                selected_player_dict = action_dirty(selected_player_dict, f"pig_{selected_pig}")
            # If an action card has been played:
            elif (selected_action_card in config.actional_cards):
                if (selected_action_card == "Blitzkarte"):
                    selected_player_dict = action_flash(selected_player_dict, f"pig_{selected_pig}")
                elif (selected_action_card == "Bauer-schrubbt-die-Sau-Karte"):
                    selected_player_dict = action_stable_open(selected_player_dict, selected_pig)
                else:
                    print(f"Card not found {selected_action_card}")
            # If a support card has been played:
            elif (selected_action_card in config.support_cards):
                if (selected_action_card == "Stallkarte"):
                    selected_player_dict = action_stable(selected_player_dict, f"pig_{selected_pig}")
                elif selected_action_card == "Blitzableiterkarte":
                    selected_player_dict = action_current_arrester(selected_player_dict, f"pig_{selected_pig}")
                elif selected_action_card == "Bauer-ärgere-dich-Karte":
                    selected_player_dict = action_stable_locked(selected_player_dict, f"pig_{selected_pig}")
            
            # Update the GUI after changes
            update_UI(root, selected_player, selected_pig, selected_player_dict)

    # Standard configuration after move
    current_player = config.configure_current_player(current_player)
    change_state_player_pigs(root, "disabled")
    manage_action_cards.show_action_cards(root, card_dict_players, current_player)
    setup_command_action_card(root)

def handle_action_card_selection(clicked_action_card):
    selected_action_card = clicked_action_card.cget("image").pil_image.split('.')[0]
    # Spread moves don't need a specific pig selection
    if (selected_action_card == "Regenkarte") or (selected_action_card == "Tornadokarte"):
        # Get a list of all pig-dictionaries
        list_of_all_pigs = []
        for player_dict in range(config.amount_of_players):
            list_of_all_pigs.append(globals()[f"dict_player_pigs_{player_dict+1}"])
        
        if (selected_action_card == "Regenkarte"):
            list_of_all_pigs = action_rain(list_of_all_pigs)
        else:
            list_of_all_pigs = action_tornado(list_of_all_pigs)
        
        # Update the GUI for every pig
        for player in range(1, config.amount_of_players+1):
            for pig in range(1, config.pigs_per_player[config.amount_of_players]+1):
                update_UI(root, player, pig, globals()[f"dict_player_pigs_{player}"])

        # Standard configuration after move
        change_state_player_pigs(root, "disabled")
        manage_action_cards.show_action_cards(root, card_dict_players, config.configure_current_player(current_player))
        setup_command_action_card(root)
        if (selected_action_card == "Regenkarte"):
            handle_played_action_card(current_player, "Regenkarte", card_dict_players)
        else:
            handle_played_action_card(current_player, "Tornadokarte", card_dict_players)
    # If no spread-move has been played
    else:
        # The player should only select pigs if he has selected an action-card
        change_state_player_pigs(root, "enabled")
        for action_card in clicked_action_card.master.winfo_children():
            # Clear the selected-flags of previously (potentially) selected action-cards
            if hasattr(action_card, "flag"):
                action_card.flag = "Inactive"
        # Change the new action-card to "selected"
        clicked_action_card.flag = "Selected"

def change_state_player_pigs(root_window, new_state):
    # Make the pigs of all players clickable (only available after an action card has been chosen)
    for player in range(config.amount_of_players):
        frame_player_pigs = root_window.nametowidget(f".pigs_player_{player+1}")
        for widget in frame_player_pigs.winfo_children():
            # Don't select the potential support-cards of the pig
            if not widget.__class__.__name__ == "Frame":
                widget.configure(state=new_state)

# -------------------------------------------------------------------------------

## Basic configuration
current_player = 1
card_dict_players = config.configure_player_card_dictionary(config.amount_of_players)

root = config.configure_board()

# Pigs preparation
root = manage_pigs.add_pigs(root)
setup_command_pigs(root)

<<<<<<< Updated upstream:src/frontend/control_panel.py
# Action cards
for player in range(1, config.amount_of_players + 1):
=======
# Action cards preparation
for player in range(1,config.amount_of_players+1):
    globals()[f"dict_player_pigs_{player}"] = create_dictionary(config.amount_of_players).copy()
>>>>>>> Stashed changes:frontend/control_panel.py
    manage_action_cards.draw_cards(player, 3, card_dict_players)
manage_action_cards.create_frame(root)
manage_action_cards.show_action_cards(root, card_dict_players, current_player)
setup_command_action_card(root)

root.mainloop()