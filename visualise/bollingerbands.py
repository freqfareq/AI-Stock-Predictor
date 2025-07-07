import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df_full = pd.read_excel("reliance_1wk_BollingerBands.xlsx")

df = pd.concat([df_full.iloc[:2], df_full.iloc[1000:]], ignore_index=True)
plt.figure(figsize=(14, 6))

plt.plot(df['Price'], df['Close'], label='Close Price', color='black')
plt.plot(df['Price'], df['20 SMA'], label='20 SMA', color='blue')
plt.plot(df['Price'], df['Upper Band'], label='Upper Band', color='green')
plt.plot(df['Price'], df['Lower Band'], label='Lower Band', color='red')

# Optional: Fill Bollinger Band area
plt.fill_between(df['Price'], df['Upper Band'], df['Lower Band'], color='gray', alpha=0.2)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Close Price with Bollinger Bands')
plt.legend()
plt.grid(True)

# Rotate dates for readability
# plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
