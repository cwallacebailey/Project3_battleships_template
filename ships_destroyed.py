from sequences import end_game_lose

destroyer_destroyed = False
battleship_destroyed = False
ship_destroyed = False
friggot_destroyed = False
destroyer = 0
battleship = 0
ship = 0
friggot = 0


def ship_check(board):
    """
    checks board arrays to see
    if ships are still present
    """

    for row in board:
        for column in row:
            if column == chr(8517):
                destroyer += 1
            if column == chr(8486):
                battleship += 1
            if column == chr(8492):
                ship += 1
            if column == chr(8497):
                friggot += 1
    ships_destroyed(destroyer, battleship, ship, friggot)


def ships_destroyed(destroyer, battleship, ship, friggot):
    """
    ensures that each ship
    can only be destroyed once
    """
    if destroyer == 0 and destroyer_destroyed is False:
        print("The destroyer's been destroyed")
        destroyer_destroyed = True
    if battleship == 0 and battleship_destroyed is False:
        print("That's the battleship gone")
        battleship_destroyed = True
    if ship == 0 and ship_destroyed is False:
        print("That's the battleship gone")
        ship_destroyed = True
    if friggot == 0 and friggot_destroyed is False:
        print("That's the friggot down")
        friggot_destroyed = True
    return(destroyer_destroyed, battleship_destroyed,
            ship_destroyed, friggot_destroyed)


def game_end():
    """
    checks if all ships are gone
    """
    if destroyer + battleship + ship + friggot == 0:
        end_game_lose()