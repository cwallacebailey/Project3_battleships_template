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

def computer_guess(self):
        """
        Creates a random guess for the computer
        passes guess to a check that the guess -
        has not been made before
        """
        self.com_row, self.com_col = random.randint(0, self.board_size**2 - 1) // self.board_size, random.randint(0, self.board_size**2 - 1) % self.board_size
        self.com_row = int(self.com_row)
        self.com_col = int(self.com_col)
        self.computer_check_guess(self.com_row, self.com_col, self.user_board)


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

def computer_check_guess(self, row, col, board):
        """
        Ensures the guess has not been made before
        if not, passes guess to check_hit_or_miss
        if it has been guessed before computer_guess is called again
        """
        if board[row][col] == "\U0001f30a":
            self.computer_guess()
        elif board[row][col] == "\U0001f525":
            self.computer_guess()
        else: 
            self.computer_check_hit_or_miss(self.com_row, self.com_col, self.user_board, self.user_board)

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

    def computer_check_hit_or_miss(self, row, col, board, update_board):
        """
        Checks if a ship is at the computer guess coordinates
        """
        time.sleep(0.5)
        print("They're getting ready to shoot!!")
        time.sleep(0.5)
        display_clear()
        if board[row][col] == "\U0001f6a2":
            update_board[row][col] = '\U0001f525'
            print("                    One of our ships has been destroyed!")

            self.user_ships -= 1
            
            if self.user_ships == 0:
                ("                     That was their last ship!!")
                time.sleep(5)
                self.end_game_lose()

            else:
                self.take_guess()
        else:
            update_board[row][col] = "\U0001f30a"
            print("                    They missed us!! Carry on lads!")
            self.take_guess()

   def end_game_lose():
        """
        plays losing sequence
        """
        print(ascii_game)
        time.sleep(0.5)
        print(ascii_over)
        time.sleep(0.5)
        display_clear()
        print(ascii_you)
        time.sleep(0.5)
        print(ascii_lose)
        time.sleep(3)
        Intro()

    def end_game_win():
        """
        plays losing sequence
        """
        print(ascii_game)
        time.sleep(0.5)
        print(ascii_over)
        time.sleep(0.5)
        display_clear()
        print(ascii_you)
        time.sleep(0.5)
        print(ascii_win)
        time.sleep(3)
        Intro()