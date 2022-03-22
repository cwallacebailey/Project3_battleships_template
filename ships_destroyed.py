""" module to see update ship damage """

import time
import python.ascii as art
from python.general_functions import splice_fleet, display_clear


class ShipDamage():
    """
    checks ship damage based
    on the board passed to it
    """

    def __init__(self, board, fleet, turn):
        self.turn = turn
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
        print(self.destroyer, self.battleship, self.ship, self.friggot)
        return(self.destroyer, self.battleship, self.ship, self.friggot)

    def ships_destroyed(self):
        """
        ensures that each ship
        can only be destroyed once
        """
        if self.destroyer == 0 and chr(8517) in self.fleet:
            print("The destroyer's been destroyed")
            splice_fleet(self.fleet, chr(8517))
            print(self.fleet)
        if self.battleship == 0 and chr(8486) in self.fleet:
            print("That's the battleship gone")
            splice_fleet(self.fleet, chr(8486))
            print(self.fleet)
        if self.ship == 0 and chr(8492) in self.fleet:
            print("That's the battleship gone")
            splice_fleet(self.fleet, chr(8492))
            print(self.fleet)
        if self.friggot == 0 and chr(8497) in self.fleet:
            print("That's the friggot down")
            splice_fleet(self.fleet, chr(8497))
            print(self.fleet)
        self.game_end()
        return self.fleet

    def game_end(self):
        """
        checks if any ships left
        if so ends the game
        """
        check = self.destroyer + self.battleship + self.ship + self.friggot
        if check == 0:
            if  == "computer":
                print("That was our last ship!!")
                time.sleep(0.5)
                display_clear()
                print(art.ASCII_GAME)
                time.sleep(0.5)
                print(art.ASCII_OVER)
                time.sleep(0.5)
                display_clear()
                print(art.ASCII_YOU)
                time.sleep(0.5)
                print(art.ASCII_LOSE)
                time.sleep(3)
                Intro()
            else:
                print("That was their last ship!!!")
                time.sleep(0.5)
                display_clear()
                print(art.ASCII_GAME)
                time.sleep(0.5)
                print(art.ASCII_OVER)
                time.sleep(0.5)
                display_clear()
                print(art.ASCII_YOU)
                time.sleep(0.5)
                print(art.ASCII_WIN)
                time.sleep(3)
                Intro()
        else:
            return self.fleet
