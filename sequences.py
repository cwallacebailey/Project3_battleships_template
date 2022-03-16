""" Module houses visual sequences such as intro """

import time
from tool_functions import type_slowly, display_clear
from ascii import ASCII_OPENING_PAGE, ASCII_BATTLE, ASCII_SHIPS, ASCII_RULES
from ascii import ASCII_LETS, ASCII_HUNT, ASCII_PIRATES
from ascii import ASCII_SHIP_1, ASCII_SHIP_2, ASCII_SHIP_3
from ascii import ASCII_DOOR_1, ASCII_DOOR_2
# from run import PlayGame

Username = []


class Intro():
    """
    plays opening sequence
    starting with the opening_menu
    """

    def __init__(self):
        """
        begins opening sequence of the game
        starting with the opening menu
        """
        self.answer = None
        self.opening = self.opening_menu()

    def opening_menu(self):  # https://fsymbols.com/generators/carty/
        """
        opening menu displayed with
        ship and game title. User
        can select to play or see rules
        """
        display_clear()
        answers = ['R', 'P', 'S']
        print(ASCII_OPENING_PAGE)
        type_slowly("Ready to play? Type 'P' then return")
        type_slowly("To see the rules type 'R' then return\n")
        type_slowly("To skip the intro type 'S' then the return key")
        answer = input("\n").upper()
        while answer not in answers:
            display_clear()
            print(ASCII_OPENING_PAGE)
            type_slowly("lets try that again\n")
            type_slowly("Ready to play? Type 'P' then return\n")
            type_slowly("To see the rules type 'R' then return\n")
            type_slowly("To skip the intro type 'S' then the return key")
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
        print(ASCII_SHIP_1)
        time.sleep(0.3)
        display_clear()
        print(ASCII_SHIP_2)
        time.sleep(0.3)
        display_clear()
        print(ASCII_SHIP_3)
        time.sleep(0.3)
        display_clear()
        print(ASCII_SHIP_2)
        time.sleep(0.3)
        display_clear()
        print(ASCII_SHIP_1)
        time.sleep(0.3)

    def door_animation(self):
        """
        plays an animation of a door and the openening text
        then calls the play_screen function
        """
        display_clear()
        time.sleep(1)
        print(ASCII_DOOR_1)
        time.sleep(1)
        display_clear()
        print(ASCII_DOOR_2)
        time.sleep(1)
        type_slowly(".......................hello?.....................\n")
        time.sleep(1)
        type_slowly("..............is...is anybody there?.................\n")
        time.sleep(0.5)
        type_slowly(".............I'm locked aboard this ship............\n")
        type_slowly("................In the captains quarters..............\n")
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
        type_slowly("Hello there.\n")
        type_slowly("Welcome aboard, our first mate has been kidnapped. \n")
        type_slowly("To make things worse between us and them is a fleet of")
        type_slowly("pirate vessels.\nWe could use every able hand.")
        type_slowly(" Will you help us rescue them? \n")
        type_slowly("Type 'Y' to help or 'N' to return to the main menu")
        self.answer = input("\n").upper()
        while self.answer not in answers:
            display_clear()
            type_slowly("I'm sorry, I can't make sense of what you said, ")
            type_slowly("could you try again?\n")
            type_slowly("Type 'Y' to continue or 'N' to return to the ")
            type_slowly("main menu")
            self.answer = input("\n").upper()
        if self.answer == "Y":
            display_clear()
            self.collect_username()
        else:
            self.opening_menu()

    def battle_ship_animation(self):
        """
        clears the screen and
        types battle ships
        """
        display_clear()
        print(ASCII_BATTLE)
        time.sleep(0.8)
        print(ASCII_SHIPS)
        input("Hit any key to continue \n")
        display_clear()
        #  PlayGame()

    def rules(self):
        """
        displays the rules to the user
        """
        display_clear()
        print(ASCII_RULES)
        print("rules to go here")
        cont = input("Type 'Y' to continue\n").upper()
        while cont != 'Y':
            display_clear()
            print(ASCII_RULES)
            print("rules to go here")
            print("You didn't type 'Y'\n")
            cont = input("Type 'Y' to continue \n").upper()
        display_clear()
        print("rules to go here 2")
        input("Type any key and hit enter to return to the main menu \n")
        self.opening_menu()

    def collect_username(self):
        """
        takes the username from the user and
        stores it in the username variable
        if spaces are given the user is asked again
        """
        display_clear()
        type_slowly("Thanks for joining the hunt, before we commence, ")
        type_slowly("what's your name stranger")
        username = input("? \n")
        while len(username.strip(" ")) == 0:
            display_clear()
            type_slowly(".......the silent type are we? I'm going to")
            type_slowly(" need a name to start. Now what is it?")
            username = input("\n")
        display_clear()
        type_slowly(f"Welcome aboard {username}")
        time.sleep(1)
        display_clear()
        print(ASCII_LETS)
        time.sleep(0.8)
        print(ASCII_HUNT)
        time.sleep(0.8)
        print(ASCII_PIRATES)
        time.sleep(0.8)
        self.battle_ship_animation()
