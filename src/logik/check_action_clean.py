def check_clean(dictionary: dict, pig_number: str) -> int:
    """
    Die Check clean Funktion überprüft, ob ein Schwein sauber 
    werden kann oder nicht. z.B. bei Regen oder im Stall...

    Parameters
    ----------
    dictionary : dict
        Ein Dictionary, das jedem Schwein (Key) einen Status-String
        zuordnet. Der Status enthält Informationen wie 'dirty',
        'clean', 'stable', 'locked' usw.
    pig_number : str
        Die ID des Schweins, für das überprüft werden soll, ob die
        Reinigung durchgeführt werden darf.

    Returns
    -------
    int
        -1 : Fehler – das Schwein befindet sich im Stall ('stable') und
             kann nicht sauber gemacht werden.
        1 : Warning – das Schwein ist bereits sauber ('clean').
        0 : OK – das Schwein ist dreckig ('dirty') und nicht im Stall,
             daher darf die Reinigung durchgeführt werden.

    """
    
    status = dictionary[pig_number]
    
    # wenn im Stall, dann nicht möglich
    if "stable" in status:
        return -1
    # wenn bereits sauber, macht es keinen Sinn
    if "clean" in status:
        return 1
    
    # wenn dirty + nicht im Stall = clean i.O.
    return 0