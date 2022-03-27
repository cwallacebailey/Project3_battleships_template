""" testing module"""

import random
from python.board import CreateBoard

go = CreateBoard().board


class PlayGame():
    """
    creates board for the user and takes
    guesses until the game ends in user
    or computer victory
    """
    def __init__(self):
        self.guesses = 0
        self.success_array = []
        self.ships = 0
        self.board_size = 5
        self.computer_board = go
        self.com_row = None
        self.com_col = None
        self.destroyer = 0
        self.battleship = 0
        self.ship = 0
        self.friggot = 0
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
            if self.guesses != 0:
                self.hit_success()  # if this guess has been made before then go back to hit_success if it is active
            else:
                self.computer_guess()
        elif board[row][col] == chr(128369):
            self.computer_guess()
        else:
            self.computer_check_hit(self.com_row, self.com_col,
                                    self.computer_board, self.computer_board)

    def computer_check_hit(self, row, col, board, update_board):
        """
        Checks if a ship is at the computer guess coordinates
        """
        if board[row][col] != ".":
            update_board[row][col] = chr(128369)
            self.ship_check()  # first check if the game is over
            self.hit()  # update the success hit array and add in new coordinates
            self.hit_success()  # begin process of taretting around the coordinate in the success array
        else:
            update_board[row][col] = chr(9410)
            self.ship_check()

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
        if self.destroyer + self.battleship + self.ship + self.friggot > 0:
            print(self.ships)
        else:
            self.hit_success()

    def hit_success(self):
        """
        start here
        """
        # once hit possible other hits are [[row+1, col],[row-1, col], [row, col+1], [row, col-1]]
        # pick one, try it if failed splice array and then try again on the next turn
        if self.guesses > 0:
            self.com_row = self.com_row + 1
            self.guesses -= 1
            computer_check_guess(self.com_row, self.com_col,
                                 self.computer_board)

    def hit(self):
        """
        This will activate the hit programme
        """
        self.guesses = 4  # four potential guesses to keep hitting the position
        self.success_array = []  # empty the array of tis contects to allow:
        self.success_array.append(self.com_row)  # new successful targets to be added
        self.success_array.append(self.com_col)  # new successful targets to be added


PlayGame()
