def check_action_open(dictionary: dict, pig_number: str) -> int:
    """
    Die Karte kann nur gespielt werden, wenn das Schwein dreckig ist.
    Zu dem kann es aber nicht gewaschen werden, wenn der Stall abgesperrt ist.

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String
        zuordnet. Dieser enthält Informationen wie 'clean', 'dirty',
        'stable', 'locked' usw.
    pig_number : str
        Die ID des Schweins, für das geprüft werden soll, ob die
        Reinigungsaktion ausgeführt werden darf.

    Returns
    -------
    int
        -1 : Fehler – das Schwein befindet sich in einem 'locked'-Stall
           und kann daher nicht gewaschen werden.
        1 : Warning – das Schwein ist bereits 'clean' und muss nicht
           gewaschen werden.
        0 : OK – das Schwein ist 'dirty' und darf gewaschen werden.

    """
    status = dictionary[pig_number]
    
    if "locked" in status:
        return -1
    
    if "clean" in status:
        return 1
    
    return 0