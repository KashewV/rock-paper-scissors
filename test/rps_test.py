from app.rps import determine_outcome, generate_computer_choice, VALID_OPTIONS


def test_winners():
    assert determine_outcome(u="rock", c="rock") == "TIE GAME"
    assert determine_outcome(u="rock", c="paper") == "COMPUTER WINS"
    assert determine_outcome(u="rock", c="scissors") == "USER WINS"

    assert determine_outcome(u="paper", c="rock") == "USER WINS"
    assert determine_outcome(u="paper", c="paper") == "TIE GAME"
    assert determine_outcome(u="paper", c="scissors") == "COMPUTER WINS"

    assert determine_outcome(u="scissors", c="rock") == "COMPUTER WINS"
    assert determine_outcome(u="scissors", c="paper") == "USER WINS"
    assert determine_outcome(u="scissors", c="scissors") == "TIE GAME"


def test_computer_choice():
    for i in range(6):
        assert generate_computer_choice() in VALID_OPTIONS