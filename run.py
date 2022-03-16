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
