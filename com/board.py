import random

class CreateBoard:

    def __init__(self):
        self.ships_to_place = 6
        self.board_size = 8
        self.build_board = self.build_board()
        self.place_ships = self.place_ships()

    def build_board(self):
        """
        creates a board structure inside an array.
        To board ships will be added and visible
        hidden_board is created for the user to guess
        """
        self.hidden_board = [["\U0001f532" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board = [["\U0001f532" for _ in range(self.board_size)] for _ in range(self.board_size)]
        return self.board, self.hidden_board

    def place_ships(self):
        """
        Places ships randomly into board array
        """
        ships_placed = 0
        while ships_placed < self.ships_to_place:
            row, col = random.randint(0, self.board_size**2 - 1) // self.board_size, random.randint(0, self.board_size**2 - 1) % self.board_size
            
            if self.board[row][col] == "\U0001f6a2":
                    continue
        
            self.board[row][col] = "\U0001f6a2"
            ships_placed +=1
        return self.board

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

