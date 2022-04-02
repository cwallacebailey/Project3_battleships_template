""" this module is also for testing """
import random
import sys
import time

board1 = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', 'Ω', 'Ω', 'Ω'], ['.', '.', '.', 'ℱ', 'ℱ', '.', '.', '.'], ['.', '.', '.', 'ⅅ', '.', '.', '.', '.'], ['.', '.', '.', 'ⅅ', '.', '.', '.', '.'], ['.', '.', '.', 'ⅅ', '.', '.', '.', '.'], ['.', '.', '.', 'ⅅ', '.', '.', '.', '.'], ['.', '.', '.', '.', 'ℬ', 'ℬ', 'ℬ', '.']]
board_size = 8
array = []


def guess(board):
    """
    Initial Guess
    """
    if len(array) > 0:
        new_target = array[0]
        row = int(new_target[0])
        col = int(new_target[-1])
        del(array[0])
    else:
        row = random.randint(0, board_size**2 - 1) // board_size
        col = random.randint(0, board_size**2 - 1) % board_size
    computer_check_guess(row, col, board)


def computer_check_guess(row, col, board):
    """
    Ensures the guess has not been made before
    if not, passes guess to check_hit_or_miss
    if it has been guessed before computer_guess is called again
    """
    if board[row][col] == 'M':
        guess(board)
    elif board[row][col] == 'A':
        guess(board)
    else:
        computer_check_hit(row, col, board)


def computer_check_hit(row, col, board):
    """
    Checks if a ship is at the computer guess coordinates
    """
    if board[row][col] != ".":
        board[row][col] = "A"
        shoot(row, col, board)
        guess(board)
    else:
        board[row][col] = 'M'
        guess(board)


def shoot(row, col, board):
    """
    picks and iterates around a successful hit
    """
    for r in range(max(0, row-1), min(board_size, row+2)):
        for c in range(max(0, col-1), min(board_size, col+2)):
            if board[r][c] != '.' and board[r][c] != 'A' and board[r][c] != 'M':
                coordinate = str(r) + str(c)
                array.append(coordinate)
    guesser(board)


def guesser(board):
    """
    gh
    """
    destroyer = 0
    for row in board:
        for column in row:
            if column == chr(8517):
                destroyer += 1
            if column == chr(8486):
                destroyer += 1
            if column == chr(8492):
                destroyer += 1
            if column == chr(8497):
                destroyer += 1
    if destroyer == 0:
        print(board)
        sys.exit()
    else:
        guess(board)


guess(board1)
