# rock-paper-scissors
Repo for Qual Control Project & Stock Dashboard

![CI](https://github.com/Kashewv/rock-paper-scissors/actions/workflows/python-app.yml/badge.svg)


## Project Structure

```
app/
  __init__.py
  rps.py          # Game logic and CL game
  stocks.py       # stocks dashboard
  
test/
  rps_test.py     # Automated tests for rps
  stocks_test.py  # stocks test
conftest.py
requirements.txt
.github/workflows/python-app.yml   # CI workflow
```

## Configuration

The stocks dashboard requires an AlphaVantage API key.
Create a file called `.env` in the root of the repo and add your key:

```sh
ALPHAVANTAGE_API_KEY="your-key-here"
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

Run the stock dashboard:
```sh
python -m app.stocks
```
When prompted type a stock ticker symbol or press enter to use the default (NVDA)


## Testing

Run the automated tests

```sh
pytest
```

## Continuous Integration

Tests run automatically through Github Actions on every push and pull request to 'main'. See `.github/workflows/python-app.yml`
