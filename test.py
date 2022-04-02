from python.general_functions import type_slowly, display_clear


def hard_mode():
    """
    Lets the user choose hard or easy mode
    """
    speech = """
    We have two choices here. We can go west towards
    a young fleet with a young, inexperienced commander. The battle
    will be EASY but there will be no honour in it. Or we can face
    a significantly more experienced fighting commander. The battle
    will be tough but your name will be known across the seven seas
    What will it be?
    Should we face off against the greater of the two opponents?
    Type 'Y' if so or 'N to take the easy route
    """
    choices = ['Y', 'N']
    type_slowly(
        speech
        )
    answer = input("")
    while answer not in choices:
        display_clear()
        print("""
    didn't understand that, I'll say it again""", speech)
        answer = input("    ").upper()

hard_mode()