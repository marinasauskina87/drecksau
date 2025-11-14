

def action_flash(dictionary: dict, pig_number:str) -> dict:
    """
    Die Funktion entfernt das Wort "stable" aus dem Status eines Schweins und simuliert damit einen Blitz,
    der den Stall zerstört.
    """
    dictionary[f"{pig_number}"] = 'dirty,'
    return dictionary

