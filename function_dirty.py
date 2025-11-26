
def action_dirty(dictionary: dict, pig_number: str) -> dict:
    """
    Die Funktion trägt in einem Wörterbuch ein, dass ein bestimmtes Schwein jetzt als „dirty“ markiert ist.
    """
    status = dictionary[pig_number]
    status = status.replace('clean', 'dirty')
    dictionary[pig_number] = status
    return dictionary

