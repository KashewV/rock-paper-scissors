import pytest

from web_app import create_app

from time import sleep
# Troubleshooted with Claude Was hitting the alphavantage rate limit of 5 requests per minute. Added a sleep to avoid hitting the limit.


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()


# Home routes

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Welcome Home</h1>" in response.data


def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About Me</h1>" in response.data


def test_hello(test_client):
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data

#url params
    response = test_client.get("/hello?name=Kash")
    assert response.status_code == 200
    assert b"<h1>Hello, Kash!</h1>" in response.data



# RPS routes

def test_rps_form(test_client):
    response = test_client.get("/rps/form")
    assert response.status_code == 200
    assert b"<h1>Rock, Paper, Scissors</h1>" in response.data
    assert b'<option value="rock">' in response.data


def test_rps_results(test_client):
    response = test_client.post("/rps/results", data={"user_choice": "rock"})
    assert response.status_code == 200
    assert b"<h1>Game Results</h1>" in response.data
    assert b"ROCK" in response.data
    assert (b"USER WINS" in response.data
            or b"COMPUTER WINS" in response.data
            or b"TIE GAME" in response.data)



# Stocks Routes


def test_stocks_form(test_client):
    response = test_client.get("/stocks/form")
    assert response.status_code == 200
    assert b"<h1>Stocks Dashboard</h1>" in response.data


def test_stocks_dashboard(test_client):
    sleep(2)
    response = test_client.post("/stocks/dashboard", data={"symbol": "NVDA"})
    assert response.status_code == 200
    assert b"<h1>Stocks Dashboard (NVDA)</h1>" in response.data
    assert b"Latest Close:" in response.data
# table has 1 header row + 10 data rows
    assert response.data.count(b"<tr>") == 11


def test_stocks_invalid_symbol(test_client):
    sleep(2)
    response = test_client.post("/stocks/dashboard", data={"symbol": "OOPS123"})
    assert response.status_code == 302  
# redirects back to the form
    assert response.headers["Location"].endswith("/stocks/form")

# following the redirect shows the flash message
    response = test_client.post("/stocks/dashboard", data={"symbol": "OOPS123"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Market data error" in response.data