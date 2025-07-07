import pandas as pd 
import matplotlib.pyplot as mt
import matplotlib.dates as mdates

df_full = pd.read_excel("reliance_1wk_BollingerBands.xlsx")

rl = pd.concat([df_full.iloc[1411:]], ignore_index=True)
# Set up a figure with 2 subplots (Close + % Change)
fig, axs = mt.subplots(2, 1, figsize=(14, 6), sharex=True)

# 1️⃣ Price & Bollinger Bands
axs[0].plot(rl["Price"], rl["Close"], label="Close", color="black")
axs[0].plot(rl["Price"], rl["20 SMA"], label="20 SMA", color="blue")
axs[0].plot(rl["Price"], rl["Upper Band"], label="Upper Band", color="green")
axs[0].plot(rl["Price"], rl["Lower Band"], label="Lower Band", color="red")
axs[0].fill_between(rl["Price"], rl["Upper Band"], rl["Lower Band"], color="gray", alpha=0.1)
axs[0].legend()
axs[0].set_title("Close Price with Bollinger Bands")
axs[0].grid(True)

# 2️⃣ % Change Chart
axs[1].plot(rl["Price"], rl["volume %"], label="% Volume", color="purple")
axs[1].axhline(0, linestyle="--", color="gray", linewidth=1)
axs[1].set_ylabel("% Volume")
axs[1].legend()
axs[1].grid(True)

# Format x-axis date
# axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# mt.xticks(rotation=45)
mt.tight_layout()
mt.show()
