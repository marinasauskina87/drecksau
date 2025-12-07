from backend.create_dictionary import create_dictionary


def create_players_list(amount_players: int) -> list:
    players_list = []
    for player in range(amount_players):
        dict = create_dictionary(amount_players)
        players_list.append(dict)

    return players_list

