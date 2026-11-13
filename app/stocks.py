import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# Fetch data

symbol = "NFLX"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

stocks_df = read_csv(request_url)
print(stocks_df.head())

fig = px.line(stocks_df, x="timestamp", y="adjusted_close",
              title=f"Stock Prices ({symbol})",
              height=450)
fig.show()
