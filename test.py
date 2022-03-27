""" testing module"""
from python.board import CreateBoard
from ship_damage import ShipDamage

user_board = CreateBoard().board
user_fleet = CreateBoard().ships

def game_result(turn):
    """
    checks if any ships left
    if so ends the game
    """
    check = 0
    if check == 0:
        if turn == "computer":
            print("That was our last ship!!")
            game_over = True
            return game_over

go = game_result("computer")
print(go)