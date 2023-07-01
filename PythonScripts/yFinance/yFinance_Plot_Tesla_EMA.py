import yfinance
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
#import plotly.express as px
from ta.trend import MACD
from ta.momentum import StochasticOscillator
from ta.volume import ForceIndexIndicator

'''period : str
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            Either Use period parameter or use start and end
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days'''
            
period = '5y'
interval = '1d'
ticker = 'INTC'
stock = yfinance.Ticker(ticker) # OK
hist = stock.history(period=period,interval=interval) # OK

#filename = "INTC_1_Years.csv"
#print('Read from file...')
#hist = pd.read_csv(filename)

#hist.to_csv(filename) #OK
#print('File Saved') #OK

# removing all empty dates
# build complete timeline from start date to end date
#dt_all = pd.date_range(start=hist.index[0],end=hist.index[-1])
# retrieve the dates that ARE in the original datset
#dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(hist.index)]
# define dates with missing values
#dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]


# MACD 
macd = MACD(close=hist['Close'], 
            window_slow=26,
            window_fast=12, 
            window_sign=9)
# Stochastic
stoch = StochasticOscillator(high=hist['High'],
                             close=hist['Close'],
                             low=hist['Low'],
                             window=14, 
                             smooth_window=3)

forceIndexIndicator = ForceIndexIndicator(close=hist['Close'],
                                          volume=hist['Volume'],
                                          window=13)
                                          

hist['diff'] = hist['Close'] - hist['Open']
hist.loc[hist['diff']>=0, 'color'] = 'green'
hist.loc[hist['diff']<0, 'color'] = 'red'

fig3 = make_subplots(rows=5, cols=1, 
               vertical_spacing=0.03, subplot_titles=(ticker, 'Volume'), 
               row_heights=[0.5,0.1,0.2,0.2,0.2], shared_xaxes=True)
#'''row_width=[0.2,0.7,0.7,0.7,0.7],'''

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

# Plot MACD trace on 3rd row
fig3.add_trace(go.Bar(x=hist.index, 
                     y=macd.macd_diff()
                    ), row=3, col=1)
fig3.add_trace(go.Scatter(x=hist.index,
                         y=macd.macd(),
                         line=dict(color='black', width=2)
                        ), row=3, col=1)
fig3.add_trace(go.Scatter(x=hist.index,
                         y=macd.macd_signal(),
                         line=dict(color='blue', width=1)
                        ), row=3, col=1)
# Plot stochastics trace on 4th row
fig3.add_trace(go.Scatter(x=hist.index,
                         y=stoch.stoch(),
                         line=dict(color='black', width=1)
                        ), row=4, col=1)
fig3.add_trace(go.Scatter(x=hist.index,
                         y=stoch.stoch_signal(),
                         line=dict(color='blue', width=1)
                        ), row=4, col=1)
fig3.add_trace(go.Bar(x=hist.index,
                          y=forceIndexIndicator.force_index(),
                          #line=dict(color='Red', width=1)
                        ), row=5, col=1)
fig3.update_yaxes(title_text="Price of "+ticker, row=1, col=1)
fig3.update_yaxes(title_text="Volume", row=2, col=1)
fig3.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)
fig3.update_yaxes(title_text="Stoch", row=4, col=1)
fig3.update_yaxes(title_text="Force Index", row=5, col=1)
fig3.update_yaxes(fixedrange=False,row =1, col=1)
# Add range slider
fig3.update_layout(height=900, width=1200,title_text = 'Date',
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
#fig3.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

fig3.update_xaxes(rangebreaks = [
                       dict(bounds=['sat','mon']), # hide weekends
                       #dict(values=dt_breaks)
                       #dict(bounds=[16, 9.5], pattern='hour'), # for hourly chart, hide non-trading hours (24hr format)
                       dict(values=["2021-12-25","2022-01-01","2023-05-29","2023-06-19","2023-04-07"]) #hide Xmas and New Year
                                ]) #June 19 is - Juneteenth, an annual commemoration of the end of slavery in the United States after the Civil War
#May 29 - Memorial Day'''
#https://www.bankrate.com/investing/stock-market-holidays/
fig3.show()
fig3.write_html(r'/home/pi/StockCharts/TSLA/20230624.html')





