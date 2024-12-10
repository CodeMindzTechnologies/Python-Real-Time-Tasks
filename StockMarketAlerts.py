"""
Stock market alerts
1. Get Stock's price from Yahoo Finance continuously
2. check if the price exceeds alert price to notify user
"""
import yfinance as yfin
import time

ticker = "TCS.NS"
target_price = 4000
check_interval_seconds = 60

while True:
    stock = yfin.Ticker(ticker)
    data = stock.history(period="1d",interval="1m")
    if not data.empty:
        current_price = data['Close'][-1]
        print(f"--- Currnt price of the stock is {current_price:.2f}")
        if current_price >= target_price:
            alert_message = f"--- {ticker} price is more than {target_price:.2f}"
            print(alert_message)
            break;
    time.sleep(check_interval_seconds)

