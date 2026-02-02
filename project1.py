# INF601 - Advanced Programming in Python

# Zach Slusser

# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt



stockdata ={}
#list of the 5 stocks to get data for
stocklist = ["GM", "TSLA", "TM","F","RACE"]
getDates = True
for stock in stocklist:
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1mo").tail(10)
    #dates were in timestamp format and i wanted it cleaner
    if getDates:
        date = np.array(hist.index)
        datesonly = np.array(date.astype('datetime64[D]'))
        getDates = False
    stockdata[stock] = []
    for price in hist['Close']:
        # i decided to round it thinking it would show on the chart but it didnt really matter, just makes the printing cleaner
        price = round(price, 2)
        stockdata[stock].append(price)
    
    toChart = np.array(stockdata[stock])
    plt.plot(datesonly, toChart, label=stock)
    plt.xlabel('Date')
    plt.xticks(rotation=45,fontsize=6)
    plt.ylabel('Closing Price USD')
    plt.title('Closing Stock Prices for ' + stock + ' Over Last 10 Closing Days (' + str(datesonly[0]) + ' to ' + str(datesonly[-1]) + ')')
    # not sure if i should do a legend for a single stock and I put it on the top but I did it
    plt.legend()
    plt.savefig('./charts/' + stock + '_prices.png') 
    plt.show()

    


