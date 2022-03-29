""" this module is also for testing """

import random

board = [['.', '.', '.', 'A', '.'], ['.', '.', '.', '.', 'A'], ['.', '.', 'A', 'A', 'A'], ['.', '.', 'A', 'A', 'A'], ['.', 'A', 'A', 'A', 'A']]
board_size = 5


com_row = random.randint(0, board_size**2 - 1) // board_size
com_col = random.randint(0, board_size**2 - 1) % board_size

coordinates = []
coordinates.append(com_col)
coordinates.append(com_row)

go = random.randint(0, 3)
possible_locations = [[0, 1], [0, -1], [1, 0], [-1, 0]]

x = random.randint(0, 10)
print(x)
go = 0 < x < board_size
print(go)