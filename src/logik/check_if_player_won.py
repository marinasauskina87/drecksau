def has_player_won(dictionary):
    
    all_status = dictionary.values()
    
    for status in all_status:
        if "clean" in status:
            return False
    return True
