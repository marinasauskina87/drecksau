

def action_clean(dictionary: dict, pig_number: str) -> dict:
    """
    Die Funktion trägt in einem Wörterbuch ein, dass ein bestimmtes Schwein jetzt als „clean“ markiert ist.
    """
    status = dictionary[f"{pig_number}"]
    status = status.replace("dirty", "clean")
    dictionary[f"{pig_number}"] = status
    return dictionary


