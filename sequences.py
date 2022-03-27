""" Module houses visual sequences such as intro """

import time
from python.general_functions import type_slowly, display_clear
import python.ascii as art


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
        print(art.ASCII_OPENING_PAGE)
        type_slowly(
            """
                Ready to play? Type 'P' then return
                To see the rules type 'R' then return
                To skip the intro type 'S' then the return key
            """
        )
        answer = input("\n                                       ").upper()
        while answer not in answers:
            display_clear()
            print(art.ASCII_OPENING_PAGE)
            type_slowly(
                """
                \n
                    Lets try that again
                    Ready to play? Type 'P' then return
                    To see the rules type 'R' then return
                    To skip the intro type 'S' then the return key
                """
            )
            answer = input("\n                                       ").upper()
        if answer == 'P':
            display_clear()
            print("\n")
            type_slowly(".........................Somewhere on the seven seas")
            time.sleep(0.5)
            for _ in range(3):
                self.ship_animation()
            self.door_animation()
        elif answer == 'S':
            display_clear()
            self.collect_username()
        else:
            self.rules()
        return "complete"  # added to remove error "assigning result of a
        # function call where the function has no return value"

    def ship_animation(self):
        """
        plays an animation of a ship travelling on the sea
        then calls the door animation
        """
        display_clear()
        print(art.ASCII_SHIP_1)
        time.sleep(0.3)
        display_clear()
        print(art.ASCII_SHIP_2)
        time.sleep(0.3)
        display_clear()
        print(art.ASCII_SHIP_3)
        time.sleep(0.3)
        display_clear()
        print(art.ASCII_SHIP_2)
        time.sleep(0.3)
        display_clear()
        print(art.ASCII_SHIP_1)
        time.sleep(0.3)

    def door_animation(self):
        """
        plays an animation of a door and the openening text
        then calls the play_screen function
        """
        display_clear()
        time.sleep(1)
        print(art.ASCII_DOOR_1)
        time.sleep(1)
        display_clear()
        print(art.ASCII_DOOR_2)
        time.sleep(1)
        type_slowly(".......................hello?.....................\n")
        time.sleep(1)
        type_slowly("...............is...is anybody there?.............\n")
        time.sleep(0.5)
        type_slowly(".............I'm locked aboard this ship..........\n")
        type_slowly("...............In the captains quarters...........\n")
        time.sleep(0.5)
        type_slowly(".......................I think....................\n")
        time.sleep(0.5)
        type_slowly("...........I'm in desperate need of rescue........\n")
        time.sleep(1)
        self.play_screen()

    def play_screen(self):
        """
        Welcomes the user and gets a username
        """
        answers = ['Y', 'N']
        display_clear()
        time.sleep(1)
        type_slowly(
            """
            \n
            Hello there.
            Welcome aboard, our first mate has been kidnapped.
            To make things worse between us and them is a fleet of pirate ships
            We could use every available able hand in the coming battle.
            Will you help us rescue them?
            Type 'Y' to help or 'N' to return to the safety of the main menu.
            \n
            """
            )
        self.answer = input("            ").upper()
        while self.answer not in answers:
            display_clear()
            type_slowly(
                """
                \n
                        I'm sorry, I can't make sense of what you said....
                        Could you try again?
                        Type 'Y' to join us, 'N' to return to the main menu
                \n
                """
            )
            self.answer = input("            ").upper()
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
        print(art.ASCII_BATTLE)
        time.sleep(0.8)
        print(art.ASCII_SHIPS)
        input("            Hit any key to continue \n")
        display_clear()

    def rules(self):
        """
        displays the rules to the user
        """
        display_clear()
        print(art.ASCII_RULES)
        print("rules to go here")
        cont = input("            Type 'Y' to continue\n").upper()
        while cont != 'Y':
            display_clear()
            print(art.ASCII_RULES)
            print("rules to go here")
            print("            You didn't type 'Y'\n")
            cont = input("            Type 'Y' to continue \n").upper()
        display_clear()
        print("rules to go here 2")
        input("            Hit enter to return to the main menu \n")
        self.opening_menu()

    def collect_username(self):
        """
        takes the username from the user and
        stores it in the username variable
        if spaces are given the user is asked again
        """
        display_clear()
        type_slowly(
            """
            Thanks for joining the hunt, before we commence,
            what's your name stranger?
            """
        )
        username = input("            ")
        while len(username.strip(" ")) == 0:
            display_clear()
            type_slowly(
                """
                ...The silent type are we? I'm going to need to know what to
                call you so what's your name?
                """
                )
            username = input("            ")
        display_clear()
        type_slowly(f"            Welcome aboard {username}")
        time.sleep(1)
        display_clear()
        print(art.ASCII_LETS)
        time.sleep(0.8)
        print(art.ASCII_HUNT)
        time.sleep(0.8)
        display_clear()
        print(art.ASCII_PIRATES)
        time.sleep(0.8)
        self.battle_ship_animation()
