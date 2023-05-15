import yfinance as yf
import pandas as pd

# Define the ticker for the stock you want to get data for
#ticker = "NVDA"
msft = yf.Ticker("MSFT")
div = msft.dividends

# Download 3 months of historical data using the daily time frame
data = yf.download(msft.ticker, period="1mo", interval="1d")

# Calculate the 100-day EMA for the stock using pandas
ema = data["Close"].ewm(span=5, adjust=False).mean()

# Print the 100-day EMA values to the console
print("5-day EMA: ", ema)
print("Dividents: ", div)
#print("MSFT Info: ",msft.info)
