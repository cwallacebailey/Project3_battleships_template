import time
from com.tool_functions import *
from com.ascii import *
from run import *

Username = []

class Intro:
    def __init__(self):
        self.opening_menu = self.opening_menu()

    def opening_menu(self): #https://fsymbols.com/generators/carty/
        display_clear()
        answers = ['R', 'P', 'S']
        print(ascii_opening_page)
        type_slowly("Ready to play, type 'P', to see the rules type 'R' followed by return")
        type_slowly("\nYou can skip the intro sequence by typing 'S' followed by the return key") 
        answer = input("\n").upper()
        while answer not in answers:
            display_clear()
            print(ascii_opening_page)
            type_slowly("Let's try that again. Ready to play? Type 'P' or to see the rules type 'R' followed by return")
            answer = input("\n").upper()
        if answer == 'P':
            display_clear()
            type_slowly("......................Somewhere on the seven seas")
            time.sleep(0.5)
            for _ in range(3):
                self.ship_animation()
            self.door_animation()
        elif answer == 'S':
            display_clear()
            self.collect_username()
        else:
            self.rules()

    def ship_animation(self):
        """
        plays an animation of a ship travelling on the sea
        then calls the door animation
        """
        display_clear()
        print(ascii_ship_1)
        time.sleep(0.3)
        display_clear()
        print(ascii_ship_2)
        time.sleep(0.3)
        display_clear()
        print(ascii_ship_3)
        time.sleep(0.3)
        display_clear()
        print(ascii_ship_2)
        time.sleep(0.3)
        display_clear()
        print(ascii_ship_1)
        time.sleep(0.3)    
    
    def door_animation(self): 
        """
        plays an animation of a door and the openening text
        then calls the play_screen function
        """
        display_clear()
        time.sleep(1)
        print(ascii_door_1)
        time.sleep(1)
        display_clear()
        print(ascii_door_2)
        time.sleep(1)
        type_slowly("..........................hello?.....................\n")
        time.sleep(1)
        type_slowly("................is...is anybody there?.................\n")
        time.sleep(0.5)
        type_slowly("...............I'm locked aboard this ship..............\n................In the captains quarters..............\n")
        time.sleep(0.5)
        type_slowly("........................I think.....................\n")
        time.sleep(0.5)
        type_slowly(".............I'm in desperate need of rescue.........\n")
        time.sleep(1)
        self.play_screen()

    def play_screen(self):
        """
        Welcomes the user and gets a username
        
        """
        answers = ['Y', 'N']
        display_clear()
        time.sleep(1)
        type_slowly("Hello there.\nWelcome aboard, our first mate has been kidnapped. \nTo make things worse between us and them is a fleet of pirate vessels.\nWe could use every able hand. Will you help us rescue them? \n\n")
        self.answer = input("Type 'Y' to help the rescue or 'N' to return to the main menu \n").upper()
        while self.answer not in answers:
            display_clear()
            type_slowly("I'm sorry, I can't make sense of what you said, could you try again?\n")
            self.answer = input("Type 'Y' to continue or 'N' to return to the main menu \n").upper()
        if self.answer == "Y":
            display_clear()
            self.collect_username()
        else:
            self.opening_menu()

    def battle_ship_animation(self):
        display_clear()
        print(ascii_battle)
        time.sleep(0.8)
        print(ascii_ships)
        input("Hit any key to continue \n")
        display_clear()
        Play_Game()

    def rules(self):
            display_clear()
            print(ascii_rules)
            print("Battleship is a war-themed board game for two players in which the opponents try to guess the location of their opponent's warships and sink them. Before the game starts, each opponent secretly places their own five ships on the ocean grid (lower part of the board) by laying out their ships and anchoring them into the holes on the grid. \n")
            cont = input("Type 'Y' to continue\n").upper()
            while cont != 'Y':
                    display_clear()
                    print(ascii_rules)
                    print("Battleship is a war-themed board game for two players in which the opponents try to guess the location of their opponent's warships and sink them. Before the game starts, each opponent secretly places their own five ships on the ocean grid (lower part of the board) by laying out their ships and anchoring them into the holes on the grid. \n")
                    print("You didn't type 'Y'\n")
                    cont = input("Type 'Y' to continue \n").upper()
            display_clear()
            print("Each ship must be placed horizontally or vertically across grid spaces—not diagonally—and the ships can't hang off the grid. Ships can touch each other, but they can't occupy the same grid space. You cannot change the position of the ships after the game begins. Players take turns firing shots (by calling out a grid coordinate) to attempt to hit the opponent's enemy ships. On your turn, call out a letter and a number that identifies a row and column on your target grid. Your opponent checks that coordinate on their ocean grid and verbally responds 'miss' if there is no ship there, or 'hit' if you have correctly guessed a space that is occupied by a ship.\n")
            rules_finished = input("Happy with the rules and ready to play? Type any key and hit return to continue \n")
            self.menu()

    def collect_username(self):
        """
        takes the username from the user and
        stores it in the username variable
        if spaces are given the user is asked again
        """
        display_clear()
        type_slowly("Thanks for joining the hunt, before we commence, what's your name stranger")
        username = input("? \n")
        while len(username.strip(" ")) == 0:
            display_clear()
            username = input(".......the silent type are we? I'm going to need a name to start. Now what is it? \n")
        else:
            display_clear()
            type_slowly(f"Welcome aboard {username}")
            time.sleep(1)
            display_clear()
            print(ascii_lets)
            time.sleep(0.8)
            print(ascii_hunt)
            time.sleep(0.8)
            print(ascii_pirate)
            time.sleep(0.8)
            self.battle_ship_animation()

Intro()