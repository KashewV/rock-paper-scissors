import random


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"

# ASK USER FOR AN INPUT (R/P/S)

user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
print("USER:", user_choice)

# VALIDATIONS

if user_choice not in VALID_OPTIONS:
    print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
    # exit()
    quit()

# GENERATE RANDOM COMPUTER CHOICE

computer_choice = random.choice(VALID_OPTIONS)
print("COMP:", computer_choice)

# DETERMINE THE WINNER

# quick alias to facilitate some copy and pasting
# we will soon move this into a function anyway
u = user_choice
c = computer_choice


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

print(determine_outcome(u, c))


