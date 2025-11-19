def action_rain(list_of_dictionaries):
    """
    Setzt alle Schweine auf „clean“, ausser die, die sich im Stall befinden.
    Schweine im Stall ('stall,') bleiben in ihrem aktuellen Zustand.

    Parameters
    ----------
    dictionary : dict
        Ein Wörterbuch, das den Status jedes Schweins enthält.
        Der Status ist z.B. 'dirty,' oder 'dirty,stable,' etc.

    Returns
    -------
    dict
        Das aktualisierte Wörterbuch, in dem alle nicht-geschützten Schweine
        als 'clean,' markiert sind.
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
