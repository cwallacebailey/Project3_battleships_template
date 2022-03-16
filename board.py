import random

class CreateBoard:

    def __init__(self):
        self.ships = [4, chr(8517), 3, chr(8486), 3, chr(8492), 2, chr(8497)]
        self.number_of_ships = int(len(self.ships)/2)
        self.board_size = 8
        self.x = 0
        self.y = 1
        self.array = []
        self.build_board = self.build_board()
        self.run = self.run()

    def build_board(self):
        """
        creates a board structure inside an array.
        To board ships will be added and visible
        hidden_board is created for the user to guess
        """
        self.hidden_board = [[chr(128911) for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board = [[chr(128911) for _ in range(self.board_size)] for _ in range(self.board_size)]
        return self.board, self.hidden_board

    def ship_direction(self):
        if random.randint(0, 1) == 0:
            direction = True #vertical row + 1
        else:
            direction = False #horizontal col + 1
        return direction

    def coordinate(self, length):
        row, col = random.randint(0, self.board_size**2 - 1) // self.board_size, random.randint(0, self.board_size**2 - 1) % self.board_size 
        direction = self.ship_direction()
        self.direction_check(row, col, direction)

    def direction_check(self, row, col, direction):
        if direction:
            if (row + self.length) > (self.board_size - 1):
                self.coordinate(self.length)
            else:
                self.coordinate_check(row, col, direction)
        else: 
            if (col + self.length) > (self.board_size - 1):
                self.coordinate(self.length)
            else: 
                self.coordinate_check(row, col, direction)

    def coordinate_check(self, row, col, direction):
        temp_coordinates = []
        x = 1
        if direction:
            for i in range(self.length):
                temp_coordinates.append(str(row + x) + str(col))
                x += 1
        else: 
            for i in range(self.length):
                temp_coordinates.append(str(row) + str(col + x))
                x += 1
        self.array_check(temp_coordinates, self.symbol)

    def array_check(self, temp_coordinates, symbol):
        if any(i in temp_coordinates for i in self.array): #https://stackoverflow.com/questions/36190533/python-check-if-an-numpy-array-contains-any-element-of-another-array
            self.coordinate(self.length)
        else:
            for i in temp_coordinates:
                self.array.append(i)
            for i in temp_coordinates:
                row = int(i[:1])
                col = int(i[1:])
                self.board[row][col] = self.symbol

    def run(self):
        for i in range(self.number_of_ships):
            self.length = self.ships[self.x]
            self.symbol = self.ships[self.y]
            self.x += 2
            self.y += 2
            self.coordinate(self.length)

class board_format():
    
    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.board_formatting = self.board_formatting(board1, board2)

    def board_formatting(self, board1, board2):
        """
        Converts the board given into an appropriate appearance
        """
        print("      1","2","3","4","5","6","7","8","    1","2","3","4","5","6","7","8")
        print(" "*6 + "— "*8 + " "*4 + "— "*8 )
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
        print("\n"," "*3, "   Enemy Ships     "," "*1, "   Our Ships     ")

go = CreateBoard().board
go2 = CreateBoard().hidden_board

board_format(go, go2)