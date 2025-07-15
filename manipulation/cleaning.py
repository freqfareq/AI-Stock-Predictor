import pandas as pd 

rl = pd.read_excel("Data/dataset_with_lag3.xlsx")

# missing = rl.isnull().sum()
# print(missing[missing > 0])

# rl = rl.dropna(subset=['Close', 'High', 'Low', 'Open', 'Volume', 'volume %', 'sma_20', 'price_vs_sma', 'percent_b', 'future_target_1wk']) 

lag_columns = [col for col in rl.columns if "_lag_" in col]
rl.drop(columns=lag_columns, inplace=True)



rl.to_excel("Data/dataset_noLag.xlsx" , index=False )



