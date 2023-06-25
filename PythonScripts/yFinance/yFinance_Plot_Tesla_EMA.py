import yfinance
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

period = '5y'
ticker = 'INTC'
stock = yfinance.Ticker(ticker) # OK
hist = stock.history(period=period) # OK

filename = "INTC_1_Years.csv"
print('Read from file...')
#hist = pd.read_csv(filename)

#hist.to_csv(filename) #OK
#print('File Saved') #OK

hist['diff'] = hist['Close'] - hist['Open']
hist.loc[hist['diff']>=0, 'color'] = 'green'
hist.loc[hist['diff']<0, 'color'] = 'red'

fig3 = make_subplots(rows=2, cols=1, 
               vertical_spacing=0.03, subplot_titles=(ticker, 'Volume'), 
               row_width=[0.2, 0.7], shared_xaxes=True)
fig3.add_trace(go.Candlestick(x=hist.index,
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                              name='OHLC'),row=1,col=1)
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].rolling(window=20).mean(),marker_color='blue',name='20 Day MA'),row=1, col=1)
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].rolling(window=50).mean(),marker_color='Green',name='50 Day MA'),row=1, col=1)
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].ewm(span=100, adjust=False).mean(),marker_color='Pink',name='100 Day EMA'),row=1, col=1)
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].rolling(window=180).mean(),marker_color='Red',name='180 Day MA'),row=1, col=1)
fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], showlegend=False), row=2, col=1)

# Add range slider
fig3.update_layout(title_text = 'Date',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1M",
                     step="month",
                     stepmode="backward"),
                dict(count=3,
                     label="3M",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6M",
                     step="month",
                     stepmode="backward"),
                dict(count=9,
                     label="9M",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=10,
                     label="10 days",
                     step="day",
                     stepmode="backward"),
                dict(count=20,
                     label="20 days",
                     step="day",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)


fig3.update_xaxes(rangebreaks = [
                       dict(bounds=['sat','mon']), # hide weekends
                       #dict(bounds=[16, 9.5], pattern='hour'), # for hourly chart, hide non-trading hours (24hr format)
                       dict(values=["2021-12-25","2022-01-01","2023-05-29","2023-06-19","2023-04-07"]) #hide Xmas and New Year
                                ]) #June 19 is - Juneteenth, an annual commemoration of the end of slavery in the United States after the Civil War
#May 29 - Memorial Day'''
#https://www.bankrate.com/investing/stock-market-holidays/

'''fig3.update_layout(
    #title_text = 'Date',
    #rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))'''

'''fig3.update_layout(
    title = {
        'text': ticker +' SHARE PRICE LAST '+period,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})'''

fig3.show()

fig3.write_html(r'/home/pi/StockCharts/TSLA/20230624.html')





