import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd

# Load data
hist = pd.read_csv(#'INTC_1_Years.csv')
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
hist.columns = [col.replace("AAPL.", "") for col in hist.columns]

# Create figure
fig = go.Figure()

hist['diff'] = hist['Close'] - hist['Open']
hist.loc[hist['diff']>=0, 'color'] = 'green'
hist.loc[hist['diff']<0, 'color'] = 'red'

fig = make_subplots(rows=2, cols=1, 
               vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'), 
               row_width=[0.2, 0.7], shared_xaxes=True)

#fig.add_trace(
#    go.Scatter(x=list(hist.Date), y=list(hist.Close)),row=1,col=1)
fig.add_trace(go.Candlestick(x=hist.index,
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                              name='OHLC'),row=1,col=1)

# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
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

fig.show()