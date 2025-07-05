import yfinance as yf
dat = yf.Ticker("MSFT")

rl = yf.download("RELIANCE.NS" , period="max" , interval="1wk")
rl.to_excel("reliance_1week_max.xlsx")
