import pandas as pd

rl = pd.read_excel("dataset_noLag.xlsx",  header=0)

def create():
    rl["Close"]= pd.to_numeric(rl["Close"], errors='coerce')

    rl["20 SMA"]= rl["Close"].rolling(window=20).mean() # 20 SMA formula 
    rl["SD"]= rl["Close"].rolling(window=20).std() # Standard deviation formula
    rl["Upper Band"] = rl["20 SMA"] + (2 * rl["SD"]) # upper band formula
    rl["Middle band"] =rl["20 SMA" ] # middle band formula 
    rl["Lower Band"] = rl["20 SMA"] - (2 * rl["SD"]) # Lower band formula
    rl["chng %"] = rl["Close"].pct_change() * 100 # close price percentage change
    rl["volume %"] =rl["Volume"].pct_change() * 100 # Volume percentage change . 

    rl["sma_20"]= rl['Close'].rolling(20).mean()
    rl["price_vs_sma"]= (rl['Close'] - rl["sma_20"])/ rl["sma_20"] # sma deviation 

    rl["percent_b"] =(rl['Close']- rl['Lower Band']) / (rl["Upper Band"]-rl["Lower Band"]) # B percentage (volatility) 

    rl["future_target_1wk"]= rl["Close"].shift(-1)/rl["Close"] - 1 # Return or Future Target (labelling)





####################################################
def classify_direction(change):
    if change > 0.05:
        return 0  # High Up
    elif change > 0.01:
        return 1  # Low Up
    else  :
        return 2  # High Down
    

rl['direction_class'] = rl['future_target_1wk'].apply(classify_direction)
print(rl['direction_class'].value_counts())
####################################################
label_map = {
    0: "High Up",
    1: "Low Up",
    2: "Down",
}

rl['direction_label'] = rl['direction_class'].map(label_map)
#####################################################



rl.to_excel("Data/dataset_with_3Class.xlsx", index=False)
