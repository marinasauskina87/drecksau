def action_rain(list_of_dictionaries):
    """
    Mit der Regenkarte werden alle Schweine wieder sauber, ausser diese sind in einem Stall.

    Parameters
    ----------
    list_of_dictionaries : Liste
        Eine Liste von Dictionaries, jedes Dictionary enthält die "pigs"

    Returns
    -------
    list_of_dictionaries : Liste
        Die aktualisierte Liste mit Dictionaires nach der Anwendung der Regenkarte.

    """
    for dictionary in list_of_dictionaries:
        for pig_number, status in dictionary.items():
            # Schwein bleibt unverändert, wenn es im Stall ist
            if 'stable' in status:
                continue
            
            # Ansonsten: 'dirty' -> 'clean'
            status = status.replace('dirty', 'clean')
            dictionary[pig_number] = status


    return list_of_dictionaries
