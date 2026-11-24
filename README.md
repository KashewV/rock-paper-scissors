# rock-paper-scissors
A Python app with a Rock, Paper, Scissors game and a stocks dashboard, available both from the command line and as a Flask web application.

![CI](https://github.com/Kashewv/rock-paper-scissors/actions/workflows/python-app.yml/badge.svg)

**Live APP:** https://kash-rps-stocks.onrender.com/ 

## Project Structure

```
app/
  __init__.py
  rps.py          # Game logic and CL game
  stocks.py       # stocks dashboard
  
test/
  rps_test.py     # Automated tests for rps
  stocks_test.py  # stocks test
  web_app_test.py # web app tests

web_app/
  __init__.py     # creates the Flask app
  routes/         # home, RPS, and stocks routes
  templates/      # HTML pages and shared Bootstrap layout
  

conftest.py
requirements.txt
.github/workflows/python-app.yml   # CI workflow
```

## Configuration

Create a file called `.env` in the root of the repo with the following contents:

```sh
ALPHAVANTAGE_API_KEY="your-key-here"
SECRET_KEY="any-long-random-string"
FLASK_APP="web_app"
```

- `ALPHAVANTAGE_API_KEY` is needed for the stocks dashboard.
- `SECRET_KEY` is needed for flash messages in the web app.
- `FLASK_APP` tells Flask where the web app lives.

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

### Web App

Run the web app locally:

```sh
python -m flask run --debug
```

Then visit http://localhost:5000 in a browser.

Pages:
- `/` - Home
- `/about` - About
- `/hello?name=YourName` - Hello
- `/rps/form` - Play Rock, Paper, Scissors
- `/stocks/form` - Stocks dashboard (enter a ticker symbol)

To stop the server, press `ctrl+C`.


## Testing

Run the automated tests

```sh
pytest
```

## Continuous Integration

Tests run automatically through Github Actions on every push and pull request to 'main'. See `.github/workflows/python-app.yml`

## Deployment

See [DEPLOYING.md](DEPLOYING.md) for instructions on deploying to Render.
