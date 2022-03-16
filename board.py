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