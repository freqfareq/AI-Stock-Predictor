import yfinance as yf
dat = yf.Ticker("MSFT")

df = yf.download("RELIANCE.NS" , period="max" , interval="1wk")
df.to_excel(r"Test\Test_1_LGBM\testData.xlsx")
