import yfinance as yf
gm = yf.Ticker("GM")
print(gm.info['open'])
print(gm.info['previousClose'])
print(gm.info['dayHigh'])
print(gm.info['dayLow'])