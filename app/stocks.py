import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# Fetch data

def fetch_stock_data(symbol = "NVDA"):
    """
    Fetches daily stock price

    Params:
        Symbol (str): Stock symbol to fetch data for. Default is "NVDA".

    Returns:
        pandas.DataFrame: DataFrame containing daily stock price data with columns
    """


    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    stocks_df = read_csv(request_url)
    return stocks_df

if __name__ == "__main__":
    symbol = input("Enter stock symbol (default: NVDA): ") or "NVDA"
    stocks_df = fetch_stock_data(symbol)
    print(stocks_df.head())


    fig = px.line(stocks_df, x="timestamp", y="adjusted_close",
                  title=f"Stock Prices ({symbol})",
                  height=450)
    fig.show()
