dict_2 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean',
    'pig_4': 'clean',
    'pig_5': 'clean',
    'pig_6': 'clean'
}
dict_3 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean',
    'pig_4': 'clean'
}
dict_4 = {
    'pig_1': 'clean',
    'pig_2': 'clean',
    'pig_3': 'clean'
}
dict_test = {
    'pig_1': 'clean',
    'pig_2': 'dirty,',
    'pig_3': 'dirty, stable, ',
    'pig_4': 'dirty, stable, locked, arrester '
}

def create_dictionary(number):
    """
    Die Funktion gibt je nach Spieler Anzahl ein passendes Dictionary zurück.
    """

    if number == 2:
        return dict_2
    elif number == 3:
        return dict_3
    elif number == 4:
        return dict_4
    elif number == 123:     # Test-dictionary wird abgerufen.
        return dict_test
    return None

