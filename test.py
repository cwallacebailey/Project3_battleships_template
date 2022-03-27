""" testing module"""

from board import CreateBoard   
import random

board_size = CreateBoard.board_size
go = CreateBoard.board

def computer_guess(self, go):
    """
    Creates a random guess for the computer
    passes guess to a check that the guess -
    has not been made before
    """
    com_row = random.randint(0, self.board_size**2 - 1) // \
        board_size
    com_col = random.randint(0, self.board_size**2 - 1) % \
        board_size
    com_row = int(com_row)
    com_col = int(com_col)
    computer_check_guess(com_row, com_col, go)