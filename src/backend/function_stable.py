def action_stable(dictionary: dict, pig_number:str) -> dict:
    """
    Im Spiel Drecksau bedeutet das Anhängen von "stable,", dass ein offener Stall für das Schwei geabut wurde.
    Das Schwein kann dadurch nicht mehr vom Regen beeinflusst werden (z.B. nicht sauber gemacht werden)
    """
    status = dictionary[pig_number]
    status = status + "stable,"
    dictionary[pig_number] = status
    return dictionary



