""" module to see update ship damage """

import time
import sys
import python.ascii as art
from python.general_functions import display_clear


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
        return(self.destroyer, self.battleship, self.ship, self.friggot)

    def ships_destroyed(self):
        """
        ensures that each ship
        can only be destroyed once
        and announces if a ship has been
        destroyed
        """
        if self.destroyer == 0 and chr(8517) in self.fleet:
            print("\n                   That's taken out the destroyer")
            self.splice_fleet(self.fleet, chr(8517))
            time.sleep(1.5)
            display_clear()
        if self.battleship == 0 and chr(8486) in self.fleet:
            print("\n                   That's the Omega ship gone")
            self.splice_fleet(self.fleet, chr(8486))
            time.sleep(1.5)
            display_clear()
        if self.ship == 0 and chr(8492) in self.fleet:
            print("\n                   That's the battleship gone")
            self.splice_fleet(self.fleet, chr(8492))
            time.sleep(1.5)
            display_clear()
        if self.friggot == 0 and chr(8497) in self.fleet:
            print("\n                   That's the friggot down")
            self.splice_fleet(self.fleet, chr(8497))
            time.sleep(1.5)
            display_clear()
        self.game_result()
        return self.fleet

    def splice_fleet(self, array, key):
        """
        called to remove specific item
        from array, specifically used
        to remove ships from player/ computer fleet
        """
        array.remove(key)
        return array

    def game_result(self):
        """
        checks if any ships left
        if so ends the game
        """
        check = self.destroyer + self.battleship + self.ship + self.friggot
        if check == 0:
            if self.turn == "computer":
                print(" "*20, "That was our last ship!!")
                time.sleep(1.5)
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
                display_clear()
                print(art.ASCII_SHIP_1)
                print("""


                To try and rescue the first mate again
                hit "run program" below
                """)
                time.sleep(10)
                sys.exit()

            else:
                print(" "*20, "That was their last ship!!!")
                time.sleep(1.5)
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
                display_clear()
                print(art.ASCII_SHIP_1)
                print("""


                Well done, you're a hero.
                To play again hit "run program" below
                """)
                time.sleep(10)
                sys.exit()

        else:
            return self.fleet
