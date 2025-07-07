import pandas as pd 

rl = pd.read_excel("reliance_1wk_BollingerBands.xlsx")

missing = rl.isnull().sum()
print(missing[missing > 0])

rl = rl.dropna(subset=['Close', 'High', 'Low', 'Open', 'Volume', 'volume %', 'sma_20', 'price_vs_sma', 'percent_b', 'future_target_1wk']) 

rl.to_excel("reliance_1wk_BollingerBands.xlsx" , index=False )