""" This module houses code to create and format the board """

import random


class CreateBoard():
    """
    creates a board and places
    ships randomly ensuring
    they do not go over the edge
    and do not cross over each other
    """
    # pylint: disable=too-many-instance-attributes
    # Twelve is reasonable in this case.
    
    def __init__(self):
        self.ships = [4, chr(8517), 3, chr(8486), 3, chr(8492), 2, chr(8497)]
        self.number_of_ships = int(len(self.ships)/2)
        self.board_size = 8
        self.length = 0
        self.ship_length_array_item = 0
        self.ship_display_array_item = 1
        self.array = []
        self.build = self.build_board()
        self.start = self.run()

    def build_board(self):
        """
        creates a board structure inside an array.
        To board ships will be added and visible
        hidden_board is created for the user to guess
        """
        bs = self.board_size
        self.hidden_board = [["." for _ in range(bs)] for _ in range(bs)]
        self.board = [["." for _ in range(bs)] for _ in range(bs)]
        return self.board, self.hidden_board

    def ship_direction(self):
        """
        randomly selects if a ship
        will be placed horizontal
        or vertical
        """
        if random.randint(0, 1) == 0:
            direction = True  # vertical
        else:
            direction = False  # horizontal
        return direction

    def coordinate(self):
        """
        creates a starting coordinate
        for the ship to be placed
        """
        row = random.randint(0, self.board_size**2 - 1) // self.board_size
        col = random.randint(0, self.board_size**2 - 1) % self.board_size
        direction = self.ship_direction()
        self.direction_check(row, col, direction)

    def direction_check(self, row, col, direction):
        """
        checks if the ships direction and total length
        will lead to the ship coming off the board
        if so coordinate is called to start again
        """
        if direction:
            if (row + self.length) > (self.board_size - 1):
                self.coordinate()
            else:
                self.coordinate_check(row, col, direction)
        else:
            if (col + self.length) > (self.board_size - 1):
                self.coordinate()
            else:
                self.coordinate_check(row, col, direction)

    def coordinate_check(self, row, col, direction):
        """
        checks if coordinates that the ship would require
        to be placed based on direction and length
        are already in use
        """
        temp_coordinates = []
        i = 1
        if direction:
            for _ in range(self.length):
                temp_coordinates.append(str(row + i) + str(col))
                i += 1
        else:
            for _ in range(self.length):
                temp_coordinates.append(str(row) + str(col + i))
                i += 1
        self.array_check(temp_coordinates)

    def array_check(self, temp_coordinates):
        """
        Checks if proposed coordinates of ship
        already contain a ship
        """
        # https://stackoverflow.com/questions/36190533/python-check-if-an-numpy-array-contains-any-element-of-another-array
        if any(i in temp_coordinates for i in self.array):
            self.coordinate()
        else:
            for i in temp_coordinates:
                self.array.append(i)
            for i in temp_coordinates:
                row = int(i[:1])
                col = int(i[1:])
                self.board[row][col] = self.symbol

    def run(self):
        """
        calls methods with each ship type and length
        placing them on the board one after another
        """
        for _ in range(self.number_of_ships):
            self.length = self.ships[self.ship_length_array_item]
            self.symbol = self.ships[self.ship_display_array_item]
            self.ship_length_array_item += 2
            self.ship_display_array_item += 2
            self.coordinate()
        return(self.board)


class BoardFormat():
    """
    formats board into a usable form
    and displays it for the user to see
    the computer or 'hidden' board alongside
    their own board
    """
    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.board_format = self.board_formatting(board1, board2)

    def board_formatting(self, board1, board2):
        """
        Converts the board given into a usable appearance
        """
        print("      1 2 3 4 5 6 7 8   "*2)
        print(" "*6 + "— "*8 + " "*4 + "— "*8)
        for i, (col, row) in enumerate(zip(board1, board2)):
            print(
                (i + 1),
                " | ",
                ''.join(x for x in row[0]),
                " "
                ''.join(x for x in row[1]),
                " "
                ''.join(x for x in row[2]),
                " "
                ''.join(x for x in row[3]),
                " "
                ''.join(x for x in row[4]),
                " "
                ''.join(x for x in row[5]),
                " "
                ''.join(x for x in row[6]),
                " "
                ''.join(x for x in row[7]),
                " | ",
                ''.join(x for x in col[0]),
                " "
                ''.join(x for x in col[1]),
                " "
                ''.join(x for x in col[2]),
                " "
                ''.join(x for x in col[3]),
                " "
                ''.join(x for x in col[4]),
                " "
                ''.join(x for x in col[5]),
                " "
                ''.join(x for x in col[6]),
                " "
                ''.join(x for x in col[7]),
                " | ",
                (i + 1)
            )
        print("\n", " "*3, "   Enemy Ships     ", " "*1, "   Our Ships     ")
        return board1, board2
