import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "audusd_h4"
RSI_PERIOD = 14

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD DATA
# =========================

df = conn.execute(f"""
SELECT *
FROM {TABLE_NAME}
ORDER BY trade_date, trade_time
""").fetchdf()

# =========================
# CALCULATE RSI
# =========================

delta = df["close"].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(window=RSI_PERIOD).mean()
avg_loss = loss.rolling(window=RSI_PERIOD).mean()

rs = avg_gain / avg_loss

df["rsi"] = 100 - (100 / (1 + rs))

# =========================
# SIGNALS
# =========================

df["signal"] = None

df.loc[df["rsi"] <= 20, "signal"] = "OVERSOLD"
df.loc[df["rsi"] >= 80, "signal"] = "OVERBOUGHT"

# =========================
# FORWARD RETURNS
# =========================

df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_6"] = ((df["close"].shift(-6) - df["close"]) / df["close"]) * 100

# =========================
# FILTER SIGNALS
# =========================

signals = df[df["signal"].notna()].copy()

oversold = signals[signals["signal"] == "OVERSOLD"]
overbought = signals[signals["signal"] == "OVERBOUGHT"]

# =========================
# WIN RATES
# =========================

oversold_wr_1 = (oversold["forward_1"] > 0).mean() * 100
oversold_wr_3 = (oversold["forward_3"] > 0).mean() * 100
oversold_wr_6 = (oversold["forward_6"] > 0).mean() * 100

overbought_wr_1 = (overbought["forward_1"] < 0).mean() * 100
overbought_wr_3 = (overbought["forward_3"] < 0).mean() * 100
overbought_wr_6 = (overbought["forward_6"] < 0).mean() * 100

# =========================
# RESULTS
# =========================

print("\n===== AUDUSD H4 RSI ALONE RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"RSI Period: {RSI_PERIOD}")

print(f"\nOversold Signals: {len(oversold)}")
print(f"Overbought Signals: {len(overbought)}")

print("\n===== OVERSOLD REVERSAL WIN RATE =====")
print(f"1 Candle: {oversold_wr_1:.2f}%")
print(f"3 Candles: {oversold_wr_3:.2f}%")
print(f"6 Candles: {oversold_wr_6:.2f}%")

print("\n===== OVERBOUGHT REVERSAL WIN RATE =====")
print(f"1 Candle: {overbought_wr_1:.2f}%")
print(f"3 Candles: {overbought_wr_3:.2f}%")
print(f"6 Candles: {overbought_wr_6:.2f}%")

print("\n===== AVERAGE RETURNS =====")
print(f"Oversold 1 Candle Avg: {oversold['forward_1'].mean():.4f}%")
print(f"Oversold 3 Candle Avg: {oversold['forward_3'].mean():.4f}%")
print(f"Oversold 6 Candle Avg: {oversold['forward_6'].mean():.4f}%")

print(f"Overbought 1 Candle Avg: {overbought['forward_1'].mean():.4f}%")
print(f"Overbought 3 Candle Avg: {overbought['forward_3'].mean():.4f}%")
print(f"Overbought 6 Candle Avg: {overbought['forward_6'].mean():.4f}%")

# =========================
# EXPORT
# =========================

signals.to_csv(
    "audusd_h4_rsi_alone_results.csv",
    index=False
)

print("\nCSV Export Complete.")