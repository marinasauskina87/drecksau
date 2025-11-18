def action_current_arrester(dictionary: dict, pig_number: str) -> dict:
    """
    Fügt einem Schwein einen 'lightningrod' hinzu, wenn es sich in einem Stall befindet.
    Der Blitzableiter schützt das Schwein vor zukünftigen Blitz-Aktionen.

    Parameters
    ----------
    dictionary : dict
        Wörterbuch mit den Status-Strings der Schweine eines Spielers.
        Beispielstatus: 'dirty,stable,locked,' oder 'clean,stable,'.
    pig_number : str
        Die ID des Schweins, das den Blitzableiter erhalten soll.

    Returns
    -------
    dict
        Das aktualisierte Wörterbuch.
    """

    status = dictionary[pig_number]

    # current_arrester kann NUR gebaut werden, wenn das Schwein im Stall ist
    if "stable" not in status:
        return dictionary

    # Wenn schon ein current_arrester vorhanden ist ->  nicht doppelt hinzufügen
    if "current_arrester" in status:
        return dictionary

    # current_arrester hinzufügen
    dictionary[pig_number] = status + "current_arrester,"

    return dictionary
