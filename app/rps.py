from random import choice


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"


def generate_computer_choice():
    """
    Generates a random choice for the computer.

    Returns:
        str: A random choice from the VALID_OPTIONS list.

    """
    return choice(VALID_OPTIONS)


def determine_outcome(u, c):
    """
    Determines the outcome of a Rock-Paper-Scissors game.

    Args:
        u (str): The user's choice.
        c (str): The computer's choice.

    Returns:
        str: The result of the game.

    Examples:
        determine_outcome(u="rock", c="scissors")
        'USER WINS'
        determine_outcome(u="paper", c="scissors")
        'COMPUTER WINS'
    """ 
    winners ={
        'rock': {
            'rock': TIE_GAME_MESSAGE,
            'paper': COMPUTER_WINS_MESSAGE,
            'scissors': USER_WINS_MESSAGE


        },
        'paper': {
            'rock': USER_WINS_MESSAGE, 
            'paper': TIE_GAME_MESSAGE,
            'scissors': COMPUTER_WINS_MESSAGE 
        },
        'scissors': {
            'rock': COMPUTER_WINS_MESSAGE,
            'paper': USER_WINS_MESSAGE,
            'scissors': TIE_GAME_MESSAGE
        }
    }
    return winners[u][c]

if __name__ == "__main__":

    u = input("Please choose one of 'rock', 'paper', or 'scissors': ").lower()
    print("USER Choice:", u)
    if u not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        exit()

    c = generate_computer_choice()
    print("COMPUTER Choice:", c)


    print(determine_outcome(u, c))


