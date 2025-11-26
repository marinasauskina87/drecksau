def check_action_stable(dictionary: dict, pig_number: str) -> int:
    """
   Prüft, ob ein 'stable' (Stall) auf das angegebene Schwein gebaut
   werden darf.
   
   Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String
        zuordnet. Beispiel: 'dirty,' oder 'clean,stable,'.
    pig_number : str
        Die ID des Schweins, das überprüft werden soll.

    Returns
    -------
    int
         1 : Fehler – ein Stall ist bereits vorhanden.
         0 : OK – Stall darf gebaut werden.
    """
    status = dictionary[pig_number]
    
    if "stable" in status:
       return 1
   
    return 0