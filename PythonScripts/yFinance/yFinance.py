import yfinance as yf

# Define the ticker for the stock you want to get data for
#TESLA = TSLA
#EPAM = EPAM

ticker = "EPAM"

# Download 6 months of historical data using the weekly time frame
data = yf.download(ticker, period="2mo", interval="1wk")

# Print the DataFrame to see the data
print(data)