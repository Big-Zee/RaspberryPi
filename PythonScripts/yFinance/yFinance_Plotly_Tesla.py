import yfinance
#import plotly.graph_objects as go
import csv

header = ['Date', '5-day EMA']

tsla = yfinance.Ticker('TSLA')
hist = tsla.history(period='1d')

hist.to_csv('/home/pi/test_df.csv', encoding='utf-8')
#f = open('/home/pi/test.csv', 'w')

#Using with - we don not need to call close file
#with open('/home/pi/test.txt', 'w', encoding='UTF8') as f:
#    f.write(hist)
#print(hist)
#fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines+markers'))
#fig.show()

# Import the plotting library
import matplotlib.pyplot as plt
%matplotlib inline

# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()