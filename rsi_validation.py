import MetaTrader5 as mt5
import pandas as pd

symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H4
rsi_period = 14

if not mt5.initialize():
    print("MT5 connection failed")
    quit()

candles = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)

df = pd.DataFrame(candles)
df["time"] = pd.to_datetime(df["time"], unit="s")

delta = df["close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.copy()
avg_loss = loss.copy()

avg_gain.iloc[:rsi_period] = None
avg_loss.iloc[:rsi_period] = None

avg_gain.iloc[rsi_period] = gain.iloc[1:rsi_period + 1].mean()
avg_loss.iloc[rsi_period] = loss.iloc[1:rsi_period + 1].mean()

for i in range(rsi_period + 1, len(df)):
    avg_gain.iloc[i] = ((avg_gain.iloc[i - 1] * (rsi_period - 1)) + gain.iloc[i]) / rsi_period
    avg_loss.iloc[i] = ((avg_loss.iloc[i - 1] * (rsi_period - 1)) + loss.iloc[i]) / rsi_period

rs = avg_gain / avg_loss
df["rsi"] = 100 - (100 / (1 + rs))

print(df[["time", "close", "rsi"]].tail(10))

mt5.shutdown()