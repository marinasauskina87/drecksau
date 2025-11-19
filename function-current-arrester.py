def action_current_arrester(dictionary: dict, pig_number: str) -> dict:
    """
    Fügt einem Schwein einen Blitzableiter hinzu, wenn es sich in einem Stall befindet.
    Der Blitzableiter schützt das Schwein vor zukünftigen Blitz-Aktionen.

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das Schweine ihren Status-Strings (Values) zuordnet.
    pig_number : str
        Die ID des Schweins, dem ein Blitzableiter hinzugefügt werden soll.

    Returns
    -------
    dict
        Das aktualisierte Dictionary mit erweitertem Status für das angegebene Schwein.

    """

    status = dictionary[pig_number]

    # current_arrester hinzufügen
    dictionary[pig_number] = status + "current_arrester,"

    return dictionary
