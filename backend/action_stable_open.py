from action_clean import action_clean


def action_stable_open(dictionary: dict, pig_number: str):
    """
    Die Funktion action_stable_open(dictionary, pig_number) prüft,
    ob ein bestimmtes Schwein im übergebenen Dictionary den Status "locked" hat.
    Falls der Stall abgeschlossen ist, wird keine Aktion ausgeführt.
    Falls der Stall nicht abgeschlossen ist, wird das Dictionary über action_clean() weiterverarbeitet
    (das Schwein wird gereinigt) und anschließend zurückgegeben."""

    status = dictionary[pig_number]
    if 'locked' in status:
        return None
    else:
        dictionary = action_clean(dictionary, pig_number)
        return dictionary






