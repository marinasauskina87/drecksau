def check_action_dirty(dictionary: dict, pig_number: str) -> int:
    """
    Die Karte dirty kann nur auf ein sauberes Schwein gesetzt werden.

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String zuordnet.
        Beispiel: 'clean,stable,' oder 'dirty,'.
    pig_number : str
        Die ID des Schweins, das überprüft werden soll.

    Returns
    -------
    int
        1 : Karte darf nicht gelegt werden (Schwein ist bereits 'dirty')
        0 : Karte darf gelegt werden (Schwein ist 'clean')

    """
    
    status = dictionary[pig_number]
    
    # Prpfen, ob das Schwein bereits dreckig ist, wenn ja, kann es nicht dreckig werden
    if "dirty" in status:
        return 1
    
    return 0
