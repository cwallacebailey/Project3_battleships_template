""" module to see update ship damage """

from general_functions import splice_fleet


class ShipDamage():
    """
    checks ship damage based
    on the board passed to it
    """

    def __init__(self, board, fleet):
        self.board = board
        self.fleet = fleet
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
        if self.destroyer == 0 and self.destroyer in self.fleet:
            print("The destroyer's been destroyed")
            splice_fleet(self.fleet, "destroyer")
        if self.battleship == 0 and self.battleship in self.fleet:
            print("That's the battleship gone")
            splice_fleet(self.fleet, "battleship")
        if self.ship == 0 and self.ship in self.fleet:
            print("That's the battleship gone")
            splice_fleet(self.ship, "ship")
        if self.friggot == 0 and self.friggot in self.fleet:
            print("That's the friggot down")
            splice_fleet(self.ship, "ship")
        return self.fleet
