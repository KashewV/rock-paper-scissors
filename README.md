# rock-paper-scissors
Repo for Qual Control Project

![CI](https://github.com/Kashewv/rock-paper-scissors/actions/workflows/python-app.yml/badge.svg)


## Project Structure

```
app/
  __init__.py
  rps.py          # Game logic and CL game
test/
  rps_test.py     # Automated tests
conftest.py
requirements.txt
.github/workflows/python-app.yml   # CI workflow
```

## Setup

Clone the repo and navigate to it from the command line:

```sh
git clone https://github.com/KashewV/rock-paper-scissors.git
cd rock-paper-scissors
```


Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the game:

```sh
python -m app.rps
```
When prompted type one of 'rock' 'paper' or 'scissors'. The Computer picks randomly and the program prints the winner


## Testing

Run the automated tests

```sh
pytest
```

## Continuous Integration

Tests run automatically through Github Actions on every push and pull request to 'main'. See `.github/workflows/python-app.yml`
