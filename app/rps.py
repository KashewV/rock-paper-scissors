from random import choice


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"


def generate_computer_choice():
    return choice(VALID_OPTIONS)


def determine_outcome(u, c):
# Using a dictionary 
    winners ={
        'rock': {
            'rock': TIE_GAME_MESSAGE,
            'paper': COMPUTER_WINS_MESSAGE,
            'scissors': USER_WINS_MESSAGE


        },
        'paper': {
            'rock': COMPUTER_WINS_MESSAGE, # Intentional Mistake
            'paper': TIE_GAME_MESSAGE,
            'scissors': USER_WINS_MESSAGE # Intentional Mistake
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


