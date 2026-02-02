# Zach Slusser
# Advanced Python - Project 1
# Due: 02/15/2026

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


allStocks = np.array([])

#list of the 5 stocks to get data for
stocklist = ["GM", "TSLA", "TM","F","RACE"]
getDates = True
for stock in stocklist:
    ticker = yf.Ticker(stock)
    #dates were in timestamp format and i wanted it cleaner
    if getDates:
        hist = ticker.history(period="1mo").tail(10)
        date = np.array(hist.index)
        datesonly = np.array(date.astype('datetime64[D]'))

        getDates = False
    hist = ticker.history(period="1mo").tail(10)
    allStocks = np.append(allStocks, hist['Close'].to_numpy())


print(datesonly)
print(allStocks)
plt.plot([allStocks], [datesonly])
