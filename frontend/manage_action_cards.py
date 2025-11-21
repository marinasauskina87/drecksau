import random
import config
from tkinter import Frame
from customtkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Import PIL for PNG support

current_card_deck = config.card_deck

def create_frame(root_window):
    # Create space for Action-Cards
    action_cards = Frame(root_window, bg="#242424", name="action_cards")
    action_cards.grid(row=2, column=2)

def choose_random_card():
    all_cards_written_out = []
    for card_type in current_card_deck:
        for _ in range(card_type[1]):
            all_cards_written_out.append(card_type[0])
    
    selectedCard = random.choice(all_cards_written_out)

    for card_type in current_card_deck:
        if selectedCard == card_type[0]:
            # Lower the appearance in the deck
            card_type[1] -= 1
            # If all cards of a certain type are out of the game
            if card_type[1] == 0:
                current_card_deck.remove(selectedCard)
            if current_card_deck == []:
                current_card_deck.append(config.card_deck)
            return card_type
    return None

def draw_cards(player, amount, card_dict_players):
    for card in range(amount):
        selectedCard = choose_random_card()
        card_dict_players[f"player-{player}"].append(selectedCard[0])
    return card_dict_players

def clear_action_cards(action_card_frame):
    # Destroy previous widgets
    for widget in action_card_frame.winfo_children():
        widget.destroy()

def show_action_cards(root_window, card_dict_players, current_player):
    frame = root_window.nametowidget(f".action_cards")
    
    # Load new cards
    for index, action_card in enumerate(card_dict_players[f"player-{current_player}"]):
        img = Image.open(f"images/{action_card}.png")
        rez_img = img.resize((int(img.width*1.2), int(img.height*1.2)))
        action = ImageTk.PhotoImage(rez_img)
        action.pil_image = f"{action_card}.png"

        # Show new cards
        btn = CTkButton(frame, text="", image=action, fg_color="transparent")
        btn.grid(column=index, row=0)