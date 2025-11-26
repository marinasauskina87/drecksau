def action_stable(dictionary: dict, pig_number:str) -> dict:
    """
    Im Spiel Drecksau bedeutet das Anhängen von "stable", dass ein offener Stall für das Schwei geabut wurde.
    Das Schwein kann dadurch nicht mehr vom Regen beeinflusst werden (z.B. nicht sauber gemacht werden)
    
    Parameters
    ----------
    dictionary : dict
        Das Wörterbuch, das die Statuswerte aller Schweine enthält.
    pig_number : str
        Die ID bzw. Nummer des Schweins, dessen Status aktualisiert werden soll.

    Returns
    -------
    dict
        Das aktualisierte Wörterbuch mit neuem Status für das angegebene Schwein.

    """
    status = dictionary[pig_number]
    status = status + "stable"
    dictionary[pig_number] = status
    return dictionary



