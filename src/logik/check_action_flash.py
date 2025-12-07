def check_action_flash(dictionary: dict, pig_number: str) -> int:
    """
    Der Blitz fackelt den Stall ab. Wenn ein Blitzableiter vorhanden ist, 
    bringt es nichts. Und wenn es den Stall nicht gibt, kann nicht abge-
    fackelt werden.

    Parameters
    ----------
    dictionary : dict
       Ein Dictionary, das jedem Schwein (Key) einen Status-String
       zuordnet. Der Status enthält Informationen wie 'dirty',
       'clean', 'stable', 'locked', 'current_arrester' usw.
    pig_number : str
       Die ID des Schweins, auf das die Blitzkarte angewendet werden soll.

    Returns
    -------
    int
        -1 : Fehler – es ist kein Stall vorhanden, daher kann nichts
             abgefackelt werden.
         1 : Warning – ein 'current_arrester' ist vorhanden, der Blitz
             zeigt keine Wirkung.
         0 : OK – ein Stall ist vorhanden und kein Blitzableiter schützt;
             der Blitz kann gespielt werden.

    """
    status = dictionary[pig_number]
    
    # Mit dem Blitableiter wird es abgeleitet, macht keinen Sinn
    if "current_arrester" in status:
        return 1
    
    # Wenn Stall nicht im Status, dann kann es nicht gespielt werden
    if "stable" not in status:
        return -1
    
    return 0