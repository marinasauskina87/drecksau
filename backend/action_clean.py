from create_dictionary import create_dictionary


def action_clean(dictionary: dict, pig_number: str) -> dict:
    """
    Die Funktion trägt in einem Wörterbuch ein, dass ein bestimmtes Schwein jetzt als „clean“ markiert ist.
    """
    dictionary[f"{pig_number}"] = "clean"
    return dictionary


