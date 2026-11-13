from random import choice


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"


def generate_computer_choice():
    return choice(VALID_OPTIONS)


def determine_outcome(u, c):
    if u == "rock" and c == "rock":
        return TIE_GAME_MESSAGE
    elif u == "rock" and c == "paper":
        return COMPUTER_WINS_MESSAGE
    elif u == "rock" and c == "scissors":
        return USER_WINS_MESSAGE

    elif u == "paper" and c == "rock":
        return COMPUTER_WINS_MESSAGE  # OOPS
    elif u == "paper" and c == "paper":
        return TIE_GAME_MESSAGE
    elif u == "paper" and c == "scissors":
        return USER_WINS_MESSAGE  # OOPS

    elif u == "scissors" and c == "rock":
        return COMPUTER_WINS_MESSAGE
    elif u == "scissors" and c == "paper":
        return USER_WINS_MESSAGE
    elif u == "scissors" and c == "scissors":
        return TIE_GAME_MESSAGE

if __name__ == "__main__":

    u = input("Please choose one of 'rock', 'paper', or 'scissors': ").lower()
    print("USER Choice:", u)
    if u not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        exit()

    c = generate_computer_choice()
    print("COMPUTER Choice:", c)


    print(determine_outcome(u, c))


