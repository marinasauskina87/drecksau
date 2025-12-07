import random
from tkinter import Frame
from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

import frontend.config as config

def create_frame(root_window):
    # Create space for Action-Cards
    frame_action_cards = Frame(root_window, bg="#242424", name="action_cards")
    frame_action_cards.grid(row=2, column=2)

def choose_random_card():
    current_card_deck = config.card_deck
    # Get every card in a list to assure probablility
    # F.e. ["Matschkarte", 2] -> ["Matschkarte", "Matschkarte"]
    all_cards_written_out = []
    for card_type in current_card_deck:
        for _ in range(card_type[1]):
            all_cards_written_out.append(card_type[0])
    
    # Select a random card
    selectedCard = random.choice(all_cards_written_out)

    # card_type[0] -> Name der Karte
    # card_type[1] -> Amount in deck
    for card_type in current_card_deck:
        if selectedCard == card_type[0]:
            # Lower the appearance in the deck
            card_type[1] -= 1
            # If all cards of a certain type are out of the game -> remove it
            if card_type[1] == 0:
                current_card_deck.remove(card_type)
            # If the card-deck is empty -> refill it
            if current_card_deck == []:
                config.card_deck = config.preset_card_deck[:]
            return card_type
    return -1

def draw_cards(player, amount, card_dict_players):
    for card in range(amount):
        selected_card = choose_random_card()
        card_dict_players[f"player-{player}"].append(selected_card[0])
    return card_dict_players

def clear_action_cards(action_card_frame):
    # Destroy previous widgets
    for widget in action_card_frame.winfo_children():
        widget.destroy()
    
def show_action_cards(root_window, card_dict_players, current_player):
    frame_action_cards = root_window.nametowidget(f"action_cards")
    frame_action_cards.configure(bg="#DDDDDD")
    
    # Label for player
    player_label_action_card = CTkLabel(frame_action_cards, text=f"It is your turn: Player {current_player}", font=("Arial", 20), text_color="black")
    player_label_action_card.grid(columnspan=3, row=0)

    # Load new cards
    for index, action_card in enumerate(card_dict_players[f"player-{current_player}"]):
        img_action_card = Image.open(f"frontend/images/{action_card}.png")
        rez_img_action_card = img_action_card.resize((int(img_action_card.width*1.2), int(img_action_card.height*1.2)))
        tk_img_action_card = ImageTk.PhotoImage(rez_img_action_card)
        tk_img_action_card.pil_image = f"{action_card}.png"

        # Show new cards
        btn_action_card = CTkButton(frame_action_cards, text="", image=tk_img_action_card, fg_color="#DDDDDD")
        btn_action_card.flag = "Inactive"
        btn_action_card.grid(column=index, row=1)
    
    # Button for withdrewing cards
    btn_withdrew_cards = CTkButton(frame_action_cards, text="Withdrew your cards")
    btn_withdrew_cards.flag = "withdraw_btn"
    btn_withdrew_cards.grid(row=2, columnspan=3, sticky="ew")
    
    # Button for wasting cards
    btn_waste_card = CTkButton(frame_action_cards, text="Waste selected action_card")
    btn_waste_card.flag = "waste_btn"
    btn_waste_card.grid(row=3, columnspan=3, sticky="ew")
    # Saves position of button
    btn_waste_card.grid_remove()

def is_waste_button_visible(frame_waste_button, is_visible):
    for widget in frame_waste_button.winfo_children():
        if widget.__class__.__name__ == "CTkButton":
            if widget.flag == "waste_btn":
                if is_visible:
                    widget.grid()
                else:
                    widget.grid_remove()
                break
    


