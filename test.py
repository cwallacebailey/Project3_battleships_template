""" testing module"""

from python.board import CreateBoard

fleet = CreateBoard().ships
destroyer = chr(8517)
battleship = chr(8486)
ship = chr(8492)
friggot = chr(8497)


def splice_fleet(array, key):
    """
    called to remove specific item
    from array, specifically used
    to remove ships from player/ computer fleet
    """
    array.remove(key)
    return array


def remove(array):
    """
    .
    """
    if destroyer in array:
        splice_fleet(array, destroyer)
        print(array)
    else:
        print("its gone")

fleet = CreateBoard().ships
print(fleet)