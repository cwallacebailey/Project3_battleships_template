""" run program from here """

from sequences import Intro
from game import PlayGame


def run_game():
    """
    calls the key classes
    to play the game
    """
    Intro()
    PlayGame()

run_game()