import pandas as pd

rl = pd.read_excel("reliance_1week_max_20sma.xlsx",  header=0)


rl["Close"]= pd.to_numeric(rl["Close"], errors='coerce')

rl["20 SMA"]= rl["Close"].rolling(window=20).mean() # 20 SMA formula 
rl["SD"]= rl["Close"].rolling(window=20).std() # Standard deviation formula
rl["Upper Band"] = rl["20 SMA"] + (2 * rl["SD"]) # upper band formula
rl["Middle band"] =rl["20 SMA" ] # middle band formula 
rl["Lower Band"] = rl["20 SMA"] - (2 * rl["SD"]) # Lower band formula



rl.to_excel("reliance_1week_max_20sma.xlsx", index=False)
