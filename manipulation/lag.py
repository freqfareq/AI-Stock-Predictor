import pandas as pd

# Load your data
rl = pd.read_excel("Data\dataset_with_3Class_nlg.xlsx")

# List of columns to create lag features for
lag_cols = ['Close', 'volume %', 'chng %', 'percent_b', 'price_vs_sma', 'future_target_1wk']

# Create lag features (1 lag, 2 lags, 3 lags as example)
for col in lag_cols:
    for lag in range(1, 4):  # You can increase range if needed
        rl[f'{col}_lag_{lag}'] = rl[col].shift(lag)

# Drop rows with NaNs created due to lagging
rl.dropna(inplace=True)

# Save updated DataFrame to Excel
rl.to_excel("Data\dataset_with_3Class.xlsx", index=False)
