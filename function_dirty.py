
def action_dirty(dictionary: dict, pig_number: str) -> dict:
    """
    Die Funktion trägt in einem Wörterbuch ein, dass ein bestimmtes Schwein jetzt als „dirty“ markiert ist.
    """
    dictionary[f"{pig_number}"] = "dirty"
    return dictionary

