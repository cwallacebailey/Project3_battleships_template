""" this is where we test """

from board import CreateBoard

GO = CreateBoard().board

SHIPS = [chr(8517), chr(8486), chr(8492), chr(8497)]

"""
TEST_ARRAY = [['.'], ['.']]
print(TEST_ARRAY)
DOT = ['.'] in TEST_ARRAY
print(DOT)
"""


def ship_check():
    """
    checks if ships present
    """
    destroyer = 0
    battleship = 0
    ship = 0
    friggot = 0
    for row in GO:
        for column in row:
            destroyer += 1 if column == chr(8517) else False
            battleship += 1 if column == chr(8486) else False
            ship += 1 if column == chr(8492) else False
            friggot += 1 if column == chr(8497) else False

    print(destroyer, battleship, ship, friggot)
    return(destroyer, battleship, ship, friggot)


ship_check()
