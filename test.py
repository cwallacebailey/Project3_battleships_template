""" this is where we test """

from board import CreateBoard

GO = CreateBoard().board

destroyer_destroyed = False
battleship_destroyed = False
ship_destroyed = False
friggot_destroyed = False


class ShipDamage():
    """
    checks ships damage and reacts if 
    one of them is destroyed
    """

    def __init__(self):
        self.destroyer = 0
        self.battleship = 0
        self.ship = 0
        self.friggot = 0
        self.ship_checks = self.ship_check()

    def ship_check(self):
        """
        checks if ships present
        """
        for row in GO:
            for column in row:
                if column == chr(8517):
                    self.destroyer += 1
                if column == chr(8486):
                    self.battleship += 1
                if column == chr(8492):
                    self.ship += 1
                if column == chr(8497):
                    self.friggot += 1
        return(self.destroyer, self.battleship, self.ship, self.friggot)

    def once(self, destroyer, battleship, ship, friggot):
        """
        ensures that each ship
        can only be destroyed
        once
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


ShipDamage()
