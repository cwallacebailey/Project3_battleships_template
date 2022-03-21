""" module to see update ship damage """


class ShipDamage():
    """
    checks ship damage based
    on the board passed to it
    """

    def __init__(self, board):
        self.board = board
        self.destroyer_destroyed = False
        self.battleship_destroyed = self.battleship_destroyed
        self.ship_destroyed = self.ship_destroyed
        self.friggot_destroyed = self.friggot_destroyed
        self.destroyer = 0
        self.battleship = 0
        self.ship = 0
        self.friggot = 0
        self.check = self.ship_check()
        self.ship_destroyed = self.ships_destroyed()

    def ship_check(self):
        """
        checks board arrays to see
        if ships are still present
        """
        for row in self.board:
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

    def ships_destroyed(self):
        """
        ensures that each ship
        can only be destroyed once
        """
        if self.destroyer == 0 and self.destroyer_destroyed is False:
            print("The destroyer's been destroyed")
            destroyer_destroyed = True
        if self.battleship == 0 and self.battleship_destroyed is False:
            print("That's the battleship gone")
            battleship_destroyed = True
        if self.ship == 0 and self.ship_destroyed is False:
            print("That's the battleship gone")
            ship_destroyed = True
        if self.friggot == 0 and self.friggot_destroyed is False:
            print("That's the friggot down")
            friggot_destroyed = True
        return(self.destroyer_destroyed, self.battleship_destroyed,
               self.ship_destroyed, self.friggot_destroyed)
