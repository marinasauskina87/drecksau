
def action_stable_locked(dictionary: dict, pig_number:str) -> dict:
    """
    Im Spiel Drecksau bedeutet das Anhängen von "locked,", dass der Stall für den Bauer geschlossen bzw. blockiert wird.
    Das Schwein kann dadurch nicht mehr vom Bauern direkt beeinflusst werden (z.B. nicht sauber gemacht)
    """
    status = dictionary[pig_number]
    status = status + "locked"
    dictionary[pig_number] = status
    return dictionary


