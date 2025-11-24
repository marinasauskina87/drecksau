def check_current_arrester(dictionary: dict, pig_number:str) -> int:
    """
    Prüft, ob eine 'current_arrester'-Karte auf das angegebene Schwein
    gelegt werden darf.

    Bedingungen:
    - Das Schwein muss sich im Stall befinden ('stable').
    - Es darf noch kein 'current_arrester' vorhanden sein.

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String zuordnet.
        Der Status-String enthält Informationen wie Sauberkeit und
        zusätzliche Karten, z. B. 'dirty,stable'.
    pig_number : str
        Die ID des Schweins, für das geprüft werden soll, ob eine
        'current_arrester'-Karte gelegt werden kann.

    Returns
    -------
    int
        0 : Die Karte darf gelegt werden.
        1 : Die Karte soll nicht gelegt werden ( weil ein 'current_arrester' existiert).
        -1 : Die Karte darf nicht gelegt werden, da kein Stall vorhanden
    """

    status = dictionary[pig_number]

    if "stable" not in status:
        return -1
    
    if "current_arrester" in status:
        return 1
    
    return 0