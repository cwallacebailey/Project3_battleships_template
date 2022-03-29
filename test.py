""" testing module"""

import random
import time
import sys
from python.board import CreateBoard

go = CreateBoard().board


class PlayGame():
    """
    creates board for the user and takes
    guesses until the game ends in user
    or computer victory
    """
    def __init__(self):
        self.coordinates = []
        self.target = []  # once hit possible other hits are [[row+1, col],[row-1, col], [row, col+1], [row, col-1]]
        self.board_size = 5
        self.computer_board = go
        self.com_row = None
        self.com_col = None
        self.destroyer = 0
        self.battleship = 0
        self.ship = 0
        self.friggot = 0
        self.turns = 0
        print(go) # THIS IS FIRST STEP FOR LATER SEE IF IT IS MISSING EVEN THOUGH PICK() SELECTS COORDINATES WITH SHIPS IN
        self.take_computer_guess = self.computer_guess()

    def computer_guess(self):
        """
        Creates a random guess for the computer
        passes guess to a check that the guess -
        has not been made before
        """
        self.destroyer = 0
        self.battleship = 0
        self.ship = 0
        self.friggot = 0
        self.target = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.com_row = random.randint(0, self.board_size**2 - 1) // \
            self.board_size
        self.com_col = random.randint(0, self.board_size**2 - 1) % \
            self.board_size
        self.com_row = int(self.com_row)
        self.com_col = int(self.com_col)
        self.computer_check_guess(self.com_row, self.com_col,
                                  self.computer_board)

    def computer_check_guess(self, row, col, board):
        """
        Ensures the guess has not been made before
        if not, passes guess to check_hit_or_miss
        if it has been guessed before computer_guess is called again
        """
        if board[row][col] == chr(9410):
            self.hit_success()  # if this guess has been made before then go back to hit_success if it is active
        elif board[row][col] == chr(128369):
            self.hit_success()  # if this guess has been made before then go back to hit_success if it is active
        else:
            self.computer_check_hit(self.com_row, self.com_col,
                                    self.computer_board, self.computer_board)

    def computer_check_hit(self, row, col, board, update_board):
        """
        Checks if a ship is at the computer guess coordinates
        """
        self.turns += 1
        if board[row][col] != ".":
            update_board[row][col] = chr(128369)
            print(self.com_col, self.com_row)

            self.hit()  # update the success hit array and add in new coordinates
            self.ship_check()  # first check if the game is over
            self.hit_success()  # begin process of targetting around the coordinate in the success array
        else:
            update_board[row][col] = chr(9410)
            self.computer_guess()

    def ship_check(self):
        """
        checks board arrays to see
        if ships are still present
        """
        for row in self.computer_board:
            for column in row:
                if column == chr(8517):
                    self.destroyer += 1
                if column == chr(8486):
                    self.battleship += 1
                if column == chr(8492):
                    self.ship += 1
                if column == chr(8497):
                    self.friggot += 1
        if self.destroyer + self.battleship + self.ship + self.friggot == 0:
            self.game_end()
        else:
            self.hit_success()

    def hit_success(self):
        """
        start here
        """
        if len(self.target) > 0:
            self.pick()
            if 0 <= self.com_row < self.board_size:
                self.pick()  # this is if the column is outside the board range then try again
            elif 0 <= self.com_col < self.board_size:
                self.pick()  # this is if the column is outside the board range then try again
            else:
                self.computer_check_guess(self.com_row, self.com_col,
                                          self.computer_board)
        else:
            self.computer_guess()
    
    def pick(self):
        """
        picks and ensures that this is not outside the board range
        """
        if len(self.target) != 0:
            select_next_coordinate = random.randint(0, len(self.target)-1)  # create random number between 0 and array length
            next_coordinate = self.target[random.randint(0, len(self.target)-1)]  # retrieve array item that corresponds to selection
            del self.target[select_next_coordinate]  # remove choice from array
            self.com_col = self.coordinates[1] + next_coordinate[-1]  # update com_col with new item from array of possible next hits
            self.com_row = self.coordinates[0] + next_coordinate[0]  # update com_row with new item from array of possible next hits
            print(f"trying {self.com_col} {self.com_row}")
            self.hit_success()
        else:
            self.computer_guess()

    def hit(self):
        """
        This will activate the hit programme
        """
        self.coordinates = []  # empty the array of its contects to allow a refill:
        self.coordinates.append(self.com_row)  # new successful target hit added to coordinate array
        self.coordinates.append(self.com_col)  # new successful target hit added to coordinate array

    def game_end(self):
        """
        Semi useless to be deleted
        Just makes the simulation End
        """
        print("Game Ends")
        print(self.turns)
        time.sleep(5)
        sys.exit()


PlayGame()
