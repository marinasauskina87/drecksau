def check_current_arrester(dictionary: dict, pig_number:str) -> bool:
    """
    Prüft, ob eine 'current_arrester'-Karte auf das angegebene Schwein
    gelegt werden darf.

    Bedingungen:
    - Das Schwein muss sich im Stall befinden ('stable').
    - Es darf noch kein 'current_arrester' vorhanden sein.
    """

    status = dictionary[pig_number]

    if "stable" not in status:
        return -1
    
    if "current_arrester" in status:
        return 1
    
    return 0