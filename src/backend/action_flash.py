from backend.create_dictionary import create_dictionary


def action_flash(dictionary: dict, pig_number:str) -> dict:
    """
    Die Funktion entfernt das Wort "stable" aus dem Status eines Schweins und simuliert damit einen Blitz,
    der den Stall zerstört.
    """
    status = dictionary[pig_number]
    if status.startswith("clean"):
        status = "clean,"
    else:
        status = "dirty,"
    dictionary[pig_number] = status
    return dictionary



