from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support
import random
from tkinter import Frame

import frontend.config as config
import frontend.manage_pigs as manage_pigs
import frontend.manage_action_cards as manage_action_cards
import frontend.manage_support_cards as manage_support_cards

from backend.action_clean import action_clean
from backend.funktion_rain import action_rain
from backend.create_dictionary import create_dictionary
from backend.action_stable_open import action_stable_open
from backend.action_flash import action_flash
from backend.function_dirty import action_dirty
from backend.function_stable import action_stable
from backend.action_stable_locked import action_stable_locked
from backend.function_current_arrester import action_current_arrester
from backend.action_tornado import action_tornado

from logik.check_action_current_arrester import check_current_arrester
from logik.check_action_flash import check_action_flash
from logik.check_action_locked import check_action_locked
from logik.check_action_open import check_action_open
from logik.check_action_stable import check_action_stable
from logik.check_function_dirty import check_action_dirty
from logik.check_if_player_won import has_player_won
from logik.check_action_withdraw_cards import check_withdraw_cards

def standard_config_after_move(root, card_dict_players):
    global current_player

    # Standard configuration after move
    current_player = config.configure_current_player(current_player)
    change_state_player_pigs(root, "disabled")
    manage_action_cards.show_action_cards(root, card_dict_players, current_player)
    setup_command_action_card(root, card_dict_players)


def update_UI(root_window, player_number, pig_number, player_dict):
    pigs = root_window.nametowidget(f"pigs_player_{int(player_number)}")
    chosen_pig = pigs.winfo_children()[int(pig_number)-1]
    states = player_dict[f'pig_{pig_number}']
    support_cards_of_pig = manage_support_cards.get_support_cards(root_window, player_number, pig_number)
    to_be_removed_support_cards = []

    if "dirty" in states:
        manage_pigs.change_state_pig(root_window, player_number, pig_number, "dirty")
    elif "clean" in states:
        manage_pigs.change_state_pig(root_window, player_number, pig_number, "clean")
    
    if "stable" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Stallkarte")
    elif ("stable" not in states) and (config.state_to_card["stable"] in support_cards_of_pig):
        to_be_removed_support_cards.append(config.state_to_card["stable"])
    
    if "current_arrester" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Blitzableiterkarte")
    elif ("current_arrester" not in states) and (config.state_to_card["current_arrester"] in support_cards_of_pig):
        to_be_removed_support_cards.append(config.state_to_card["current_arrester"])
    
    if "locked" in states:
        manage_support_cards.add_support_card(root_window, player_number, pig_number, "Bauer-ärgere-dich-Karte")
    elif ("locked" not in states) and (config.state_to_card["locked"] in support_cards_of_pig):
        to_be_removed_support_cards.append(config.state_to_card["locked"])
    
    for to_be_removed_card in to_be_removed_support_cards:
        manage_support_cards.remove_support_card(root_window, player_number, pig_number, to_be_removed_card)
    
    config.update_frame_statistics(root)

def withdrew_cards(root, card_dict_players):
    list_of_all_pigs = []
    for player_num in range(1, config.amount_of_players+1):
        list_of_all_pigs.append(globals()[f"dict_player_pigs_{player_num}"])
    if not (check_withdraw_cards(card_dict_players[f"player-{current_player}"], list_of_all_pigs, current_player) == 0):
        for action_card in card_dict_players[f"player-{current_player}"]:
            config.played_cards.append(action_card)

        card_dict_players[f"player-{current_player}"].clear()
        manage_action_cards.draw_cards(current_player, 3, card_dict_players)

        standard_config_after_move(root, card_dict_players)
        # As Update-UI would be a waste, we still have to update the statistics
        config.update_frame_statistics(root)
    else:
        msg_withdraw_failed = CTkMessagebox(title="Withdraw Cards", message="You cannot withdraw cards at this time.", icon="warning")
        msg_withdraw_failed.after(1500, msg_withdraw_failed.destroy)

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
        pigs = root_window.nametowidget(f"pigs_player_{player}")
        for pig in pigs.winfo_children():
            # As we just want to tackle the buttons and not the label "Player X"
            # Second test is for the button "Waste card"
            if (pig.__class__.__name__ == "CTkButton"):
                pig.configure(command=lambda button=pig: trigger_action(button))

def setup_command_action_card(root_window, card_dict_players):
    # During action-card-button initialisation, the command-function (executed when clicked) couldn't
    # be initialised as it is in another module. Therefore, it is done here
    action_cards = root_window.nametowidget(f"action_cards")
    for action_card in action_cards.winfo_children():
        # As we just want to tackle the buttons and not the label "It's your turn..."
        if (action_card.__class__.__name__ == "CTkButton"):
            if (hasattr(action_card.cget("image"), "pil_image")):
                action_card.configure(command=lambda button=action_card: handle_action_card_selection(button))
            if action_card.flag == "waste_btn":
                action_card.configure(command=lambda: waste_action_card(root_window))
            if action_card.flag == "withdraw_btn":
                action_card.configure(command=lambda: withdrew_cards(root_window, card_dict_players))


def handle_played_action_card(current_player, played_card, card_dict_players):
    # Remove the played card
    for index, card in enumerate(card_dict_players[f"player-{current_player}"]):
        if card == played_card:
            card_dict_players[f"player-{current_player}"].pop(index)
            break
    
    # Add the removed card to the history of played cards:
    config.played_cards.append(played_card)

    # Draw a card
    new_card = manage_action_cards.choose_random_card()
    card_dict_players[f"player-{current_player}"].append(new_card[0])

    return card_dict_players

def trigger_action(clicked_btn):
    # Get the selected action_card
    action_card_frame = root.nametowidget(f"action_cards")
    correct_move = True

    # For showing waste-card-button
    manage_action_cards.is_waste_button_visible(action_card_frame, False)

    for action_card in action_card_frame.winfo_children():
        # Just select the selected action_card
        if action_card.__class__.__name__ == "CTkButton" and action_card.flag == "Selected":
            # Define entities
            selected_entity = parse_widget_to_pig_location(clicked_btn)
            selected_pig = selected_entity["pig_number"]
            selected_pig_str = f"pig_{selected_pig}"
            selected_player = selected_entity["player_number"]
            selected_action_card = action_card.cget("image").pil_image.split('.')[0]
            selected_player_dict = globals()[f"dict_player_pigs_{selected_player}"]

            # If a status card has been played:
            if (selected_action_card in config.status_cards):
                if (str(current_player) == selected_player):
                    if check_action_dirty(selected_player_dict, selected_pig_str) == 0:
                        selected_player_dict = action_dirty(selected_player_dict, selected_pig_str)
                        msg_dreckssau = CTkMessagebox(title="DRECKSSAU! :D", message="DRECKSSAU! :D", icon="warning")
                        msg_dreckssau.after(1000, msg_dreckssau.destroy)
                    else:
                        correct_move=False
                        msg_dirty_failed = CTkMessagebox(title="Action dirty failed", message="You cannot dirty this pig.", icon="warning")
                        msg_dirty_failed.after(1500, msg_dirty_failed.destroy)
                else:
                    correct_move=False
                    msg_dirty_someone = CTkMessagebox(title="Action dirty failed", message="You cannot dirty someone else's pig.", icon="warning")
                    msg_dirty_someone.after(1500, msg_dirty_someone.destroy)

            # If an action card has been played:
            elif (selected_action_card in config.actional_cards):
                if not (str(current_player) == selected_player):
                    if (selected_action_card == "Blitzkarte"):
                        if check_action_flash(selected_player_dict, selected_pig_str) == 0:
                            selected_player_dict = action_flash(selected_player_dict, selected_pig_str)
                        else:
                            correct_move=False
                            msg_flash_failed = CTkMessagebox(title="Action flash failed", message="Action flash failed.", icon="warning")
                            msg_flash_failed.after(1500, msg_flash_failed.destroy)
                    elif (selected_action_card == "Bauer-schrubbt-die-Sau-Karte"):
                        if check_action_open(selected_player_dict, selected_pig_str) == 0:
                            selected_player_dict = action_stable_open(selected_player_dict, selected_pig_str)
                            msg_dreckssau = CTkMessagebox(title="ICH PUTZ DICH! :D", message="ICH PUTZ DICH! :D", icon="warning")
                            msg_dreckssau.after(1000, msg_dreckssau.destroy)
                        else:
                            correct_move=False
                            msg_open_failed = CTkMessagebox(title="Action open failed", message="Action open failed.", icon="warning")
                            msg_open_failed.after(1500, msg_open_failed.destroy)
                    else:
                        msg_general_error = CTkMessagebox(title="Error", message="General error occurred. Please contact support.", icon="warning")
                        msg_general_error.after(2000, msg_general_error.destroy)
                        correct_move=False
                else:
                    correct_move=False
                    msg_donot_attack = CTkMessagebox(title="Don't attack yourself", message="Don't attack yourself.", icon="warning")
                    msg_donot_attack.after(1500, msg_donot_attack.destroy)
            # If a support card has been played:
            elif (selected_action_card in config.support_cards):
                if (str(current_player) == selected_player):
                    if (selected_action_card == "Stallkarte"):
                        if check_action_stable(selected_player_dict, selected_pig_str) == 0:
                            selected_player_dict = action_stable(selected_player_dict, selected_pig_str)
                        else:
                            correct_move=False
                            msg_stable_failed = CTkMessagebox(title="Action stable failed", message="Action stable failed.", icon="warning")
                            msg_stable_failed.after(1500, msg_stable_failed.destroy)
                    elif selected_action_card == "Blitzableiterkarte":
                        if check_current_arrester(selected_player_dict, selected_pig_str) == 0:
                            selected_player_dict = action_current_arrester(selected_player_dict, selected_pig_str)
                        else:
                            correct_move=False
                            msg_arrester_failed = CTkMessagebox(title="Action arrester failed", message="Action arrester failed.", icon="warning")
                            msg_arrester_failed.after(1500, msg_arrester_failed.destroy)
                    elif selected_action_card == "Bauer-ärgere-dich-Karte":
                        if check_action_locked(selected_player_dict, selected_pig_str) == 0:
                            selected_player_dict = action_stable_locked(selected_player_dict, selected_pig_str)
                        else:
                            correct_move=False
                            msg_locked_failed = CTkMessagebox(title="Action locked failed", message="Action locked failed.", icon="warning")
                            msg_locked_failed.after(1500, msg_locked_failed.destroy)
                    else:
                        msg_general_error2 = CTkMessagebox(title="General error", message="An error has occurred. Please contact support.", icon="question")
                        msg_general_error2.after(2000, msg_general_error2.destroy)
                        correct_move=False
                else:
                    correct_move=False
                    msg_help_others = CTkMessagebox(title="Don't help others", message="Don't help the others.", icon="warning")
                    msg_help_others.after(1500, msg_help_others.destroy)

    if correct_move:
        handle_played_action_card(current_player, selected_action_card, card_dict_players)
        # Update the GUI after changes
        update_UI(root, selected_player, selected_pig, selected_player_dict)
        if not has_player_won(selected_player_dict):
            standard_config_after_move(root, card_dict_players)
        else:
            CTkMessagebox(title="GAME OVER!", message=f"PLAYER {current_player} HAS WON!", icon="check", option_1="Close game")
            root.destroy()

def handle_action_card_selection(clicked_action_card):
    # For showing waste-card-button
    manage_action_cards.is_waste_button_visible(clicked_action_card.master, True)

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
        
        if (selected_action_card == "Regenkarte"):
            handle_played_action_card(current_player, "Regenkarte", card_dict_players)
        else:
            handle_played_action_card(current_player, "Tornadokarte", card_dict_players)

        # Update the GUI for every pig
        for player in range(1, config.amount_of_players+1):
            for pig in range(1, config.pigs_per_player[config.amount_of_players]+1):
                update_UI(root, player, pig, globals()[f"dict_player_pigs_{player}"])
        
        # Standard configuration after move
        standard_config_after_move(root, card_dict_players)

    # If no spread-move has been played
    else:
        # The player should only select pigs if he has selected an action-card
        change_state_player_pigs(root, "enabled")
        for action_card in clicked_action_card.master.winfo_children():
            # Clear the selected-flags of previously (potentially) selected action-cards
            if hasattr(action_card, "flag"):
                if action_card.flag != "waste_btn":
                    action_card.flag = "Inactive"
        # Change the new action-card to "selected"
        clicked_action_card.flag = "Selected"

def waste_action_card(root_window):
    frame_action_cards = root_window.nametowidget(f"action_cards")
    for widget in frame_action_cards.winfo_children():
        if widget.__class__.__name__ == "CTkButton":
            if widget.flag == "Selected":
                handle_played_action_card(current_player, widget.cget("image").pil_image.split('.')[0], card_dict_players)
    
    # Standard configuration after move
    standard_config_after_move(root, card_dict_players)

    # For showing waste-card-button
    manage_action_cards.is_waste_button_visible(frame_action_cards, False)

    # As Update-UI would be a waste, we still have to update the statistics
    config.update_frame_statistics(root)


def change_state_player_pigs(root_window, new_state):
    # Make the pigs of all players clickable (only available after an action card has been chosen)
    for player in range(config.amount_of_players):
        frame_player_pigs = root_window.nametowidget(f"pigs_player_{player+1}")
        for widget in frame_player_pigs.winfo_children():
            # Don't select the potential support-cards of the pig
            if not widget.__class__.__name__ == "Frame":
                widget.configure(state=new_state)

# -------------------------------------------------------------------------------

## Basic configuration
current_player = 1

config.pop_up_amount_of_player()

card_dict_players = config.configure_player_card_dictionary(config.amount_of_players)

root = config.configure_board()

config.create_frame_statistics(root)

# Pigs preparation
root = manage_pigs.add_pigs(root)
setup_command_pigs(root)

# Action cards preparation
for player in range(1,config.amount_of_players+1):
    globals()[f"dict_player_pigs_{player}"] = create_dictionary(config.amount_of_players).copy()
    manage_action_cards.draw_cards(player, 3, card_dict_players)
manage_action_cards.create_frame(root)
manage_action_cards.show_action_cards(root, card_dict_players, current_player)

setup_command_action_card(root, card_dict_players)

root.mainloop()