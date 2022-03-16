import random, time, sys

def take_guess(self):
        """
        prompts the user to make a guess
        Takes the input from the user as coordinates
        """
        self.display()
        check_list = ['1','2','3','4','5','6','7','8']
        self.row = input('\n                Enter a row between 1 and 8: \n                              ')
        while self.row not in check_list:
            print('Please enter a valid row')
            self.row = input('Enter a row between 1 and 8: \n')
        self.col = input('Enter a column between 1 and 8: \n')
        while self.col not in check_list:
            print('Please enter a valid column')
            self.col = input('Enter a Column between 1 and 8: \n')
        self.row = int(self.row) - 1
        self.col = int(self.col) - 1
        self.check_guess(self.row, self.col, self.guess_board)

def check_guess(self, row, col, board):
        """
        Checks if a ship is at the guess location
        """
        print("checking guess")
        if board[row][col] == "\U0001f30a":
            display_clear()
            print("We've shot there before, try another coordinate")
            self.take_guess()
        elif board[row][col] == "\U0001f525":
            display_clear()
            print("We've shot there before, try another coordinate")
            self.take_guess()
        else: 
            self.check_hit_or_miss(self.row, self.col, self.computer_board, self.guess_board)

def check_hit_or_miss(self, row, col, board, update_board):
        """
        Checks if a ship is at the user guess coordinates
        """
        display_clear()
        if board[row][col] == "\U0001f6a2":
            update_board[row][col] = "\U0001f525"
            print("direct hit, well done")

            self.computer_ships -= 1
            
            if self.computer_ships == 0:
                print("Its Over")
                time.sleep(5)
                self.game_end_win()

            else:
                self.computer_guess()
        else:
            update_board[row][col] = "\U0001f30a"
            print("Miss")
            self.computer_guess()
