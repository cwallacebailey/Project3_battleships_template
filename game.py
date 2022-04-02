"""
Main game file
"""

import random
import time
from python.general_functions import display_clear
from python.board import CreateBoard, BoardFormat
from ship_damage import ShipDamage

user_board = CreateBoard().board
user_fleet = CreateBoard().ships
computer_board = CreateBoard().board
computer_fleet = CreateBoard().ships
guess_board = CreateBoard().hidden_board


class PlayGame():
    """
    creates board for the user and takes
    guesses until the game ends in user
    or computer victory
    """
    def __init__(self):
        self.board_size = 8
        self.user_board = user_board
        self.computer_board = computer_board
        self.guess_board = guess_board
        self.user_fleet = user_fleet
        self.computer_fleet = computer_fleet
        self.com_row = None
        self.com_col = None
        self.take_user_guess = self.take_guess()

    def display(self):
        """
        prints the board for the user to see
        """
        BoardFormat(self.user_board, self.guess_board)

    def take_guess(self):
        """
        prompts the user to make a guess
        Takes the input from the user as coordinates
        """
        self.display()
        check_list = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.row = input('\n                  Enter a row between 1 and 8: ')
        while self.row not in check_list:
            display_clear()
            self.display()
            print(" "*17, 'Please enter a valid row \n')
            self.row = input('                  Enter a row between 1 and 8: ')
        self.col = input('                  Enter a Column between 1 and 8: ')
        while self.col not in check_list:
            display_clear()
            self.display()
            print(" "*17, 'Please enter a valid column\n')
            self.col = input('               Enter a Column between 1 and 8: ')
        self.row = int(self.row) - 1
        self.col = int(self.col) - 1
        self.check_guess(self.row, self.col, self.guess_board)
        return(self.row, self.col)

    def computer_guess(self):
        """
        Creates a random guess for the computer
        passes guess to a check that the guess -
        has not been made before
        """
        self.com_row = random.randint(0, self.board_size**2 - 1) // \
            self.board_size
        self.com_col = random.randint(0, self.board_size**2 - 1) % \
            self.board_size
        self.com_row = int(self.com_row)
        self.com_col = int(self.com_col)
        self.computer_check_guess(self.com_row, self.com_col, self.user_board)

    def computer_check_guess(self, row, col, board):
        """
        Ensures the guess has not been made before
        if not, passes guess to check_hit_or_miss
        if it has been guessed before computer_guess is called again
        """
        if board[row][col] == chr(9410):
            self.computer_guess()
        elif board[row][col] == chr(128369):
            self.computer_guess()
        else:
            self.computer_check_hit(self.com_row, self.com_col,
                                    self.user_board, self.user_board)

    def check_guess(self, row, col, board):
        """
        Checks if a ship is at the guess location
        """
        if board[row][col] == chr(9410):
            display_clear()
            print(" "*12, "We shot there before, try another coordinate")
            self.take_guess()
        elif board[row][col] == chr(128369):
            display_clear()
            print(" "*12, "We shot there before, try another coordinate")
            self.take_guess()
        else:
            self.check_hit(self.row, self.col, self.computer_board,
                           self.guess_board)

    def check_hit(self, row, col, board, update_board):
        """
        Checks if a ship is at the user guess coordinates
        """
        display_clear()
        if board[row][col] != ".":
            update_board[row][col] = chr(128369)
            board[row][col] = "."
            print(" "*18, "direct hit, well done")
            ShipDamage(self.computer_board, self.computer_fleet, "user")
            time.sleep(0.5)
            self.computer_guess()
        else:
            update_board[row][col] = chr(9410)
            print(" "*17, "Miss")
            time.sleep(0.5)
            self.computer_guess()

    def computer_check_hit(self, row, col, board, update_board):
        """
        Checks if a ship is at the computer guess coordinates
        """
        time.sleep(0.5)
        print(" "*18, "They're getting ready to shoot!!")
        time.sleep(0.5)
        display_clear()
        if board[row][col] != ".":
            update_board[row][col] = chr(128369)
            print(" "*18, "One of our ships has been hit!")
            time.sleep(0.5)
            ShipDamage(board, self.user_fleet, "computer")
            self.take_guess()
        else:
            update_board[row][col] = chr(9410)
            print(" "*18, "They missed us!! Carry on lads!")
            time.sleep(0.5)
            self.take_guess()
