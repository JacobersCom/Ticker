import yfinance as yf 

import json

ticker = input("Enter the ticker you would like to get data on: ")
period = input("time frame of history you would like to reviced\n" \
"Time frames\n" \
"1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n")

print(f"Ticker: {ticker}")
print(f"Time frame: {period}")



#function
def get_stock(ticker):
    stock = yf.Ticker(ticker)
    dat = stock.history(period)
    
    data = {
        "Symbol": ticker,
        "data": period
    }
    
    with open("ticker_info.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)


get_stock(ticker)