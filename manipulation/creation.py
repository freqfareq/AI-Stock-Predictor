import pandas as pd

rl = pd.read_excel("Data/dataset_noLag.xlsx",  header=0)

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
    
def create_class():
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



def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

rl['RSI_14'] = calculate_rsi(rl['Close'], 14)

def calculate_macd(series, short_period=12, long_period=26, signal_period=9):
    ema_short = series.ewm(span=short_period, adjust=False).mean()
    ema_long = series.ewm(span=long_period, adjust=False).mean()
    macd_line = ema_short - ema_long
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram

rl['MACD'], rl['MACD_Signal'], rl['MACD_Hist'] = calculate_macd(rl['Close'])




rl.to_excel("Data/dataset_with_3Class.xlsx", index=False)


