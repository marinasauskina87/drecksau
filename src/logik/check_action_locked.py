def check_action_locked(dictionary: dict, pig_number: str) -> int:
    """
    Prüft ob eine Locked-Karte gelegt werden kann / darf.
    
    - Das Schwein muss sich im Stall befinden.
    - Es soll noch kein "locked" vorhanden sein.

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String
        zuordnet. Beispiel: 'dirty,stable,'.
    pig_number : str
        Die ID des Schweins, für das geprüft werden soll, ob die
        'locked'-Karte gelegt werden kann.

    Returns
    -------
    int
        -1 = Fehler
        1 = Warnung
        0 = OK

    """
    status = dictionary[pig_number]
    
    # Locked kann nur gelegt werden, wenn der Stall vorhanden ist
    if "stable" not in status:
        return -1
    
    if "locked" in status:
        return 1
    
    return 0