import yfinance
import pandas as pd
from datetime import datetime


def fp(*args):  # fp means 'floating print'
    tmps = []
    for arg in args:
        if type(arg) is float: arg = round(arg, 4)  # transform only floats
        tmps.append(str(arg))
    print(" ".join(tmps))
    
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

ticker = 'INTC'
stock = yfinance.Ticker(ticker) # OK

# get all stock info
dictInfo = stock.info

df = pd.DataFrame.from_dict(dictInfo,orient='index')
df = df.reset_index()

price = dictInfo["currentPrice"]
trailingPegRatio = dictInfo["trailingPegRatio"]
forwardPE = dictInfo["forwardPE"]
fp("-----------------New Run--------------------")
fp("Current Date & Time : ", dt_string)
fp(ticker," current price is : ",price)
fp("Trailing Price / Earnings to Growth Ratio : ",trailingPegRatio)
fp("Forward Price / Earnings : ", forwardPE)
print("Dividends")

exDividentDate = dictInfo['exDividendDate']
print("Dividends EX",datetime.fromtimestamp(exDividentDate))
#print(stock.news) - Works

'''

# show news
stock.news

# show financials:
# - income statement
stock.income_stmt
stock.quarterly_income_stmt
# - balance sheet
stock.balance_sheet
stock.quarterly_balance_sheet
# - cash flow statement
stock.cashflow
stock.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
stock.major_holders
stock.institutional_holders
stock.mutualfund_holders
'''

