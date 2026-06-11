import duckdb
import pandas as pd

conn = duckdb.connect("flftc_research.duckdb")

# Load EURUSD H4 and Daily data
h4 = conn.execute("""
SELECT *
FROM eurusd_h4
ORDER BY trade_date, trade_time
""").fetchdf()

d1 = conn.execute("""
SELECT *
FROM eurusd_d1
ORDER BY trade_date
""").fetchdf()

# Previous daily high/low
d1["prev_day_high"] = d1["high"].shift(1)
d1["prev_day_low"] = d1["low"].shift(1)

levels = d1[["trade_date", "prev_day_high", "prev_day_low"]]

# Merge prior daily levels into H4 candles
df = pd.merge(h4, levels, on="trade_date", how="left")

# Detect sweeps
df["sweep"] = None

df.loc[
    (df["high"] > df["prev_day_high"]) &
    (df["close"] < df["prev_day_high"]),
    "sweep"
] = "BEARISH_SWEEP"

df.loc[
    (df["low"] < df["prev_day_low"]) &
    (df["close"] > df["prev_day_low"]),
    "sweep"
] = "BULLISH_SWEEP"

# Forward returns
df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_6"] = ((df["close"].shift(-6) - df["close"]) / df["close"]) * 100

signals = df[df["sweep"].notna()]

bullish = signals[signals["sweep"] == "BULLISH_SWEEP"]
bearish = signals[signals["sweep"] == "BEARISH_SWEEP"]

# Win rates
bullish_wr_1 = (bullish["forward_1"] > 0).mean() * 100
bullish_wr_3 = (bullish["forward_3"] > 0).mean() * 100
bullish_wr_6 = (bullish["forward_6"] > 0).mean() * 100

bearish_wr_1 = (bearish["forward_1"] < 0).mean() * 100
bearish_wr_3 = (bearish["forward_3"] < 0).mean() * 100
bearish_wr_6 = (bearish["forward_6"] < 0).mean() * 100

print("\n===== EURUSD H4 DAILY HIGH/LOW SWEEP RESEARCH =====\n")

print(f"Bullish Sweeps: {len(bullish)}")
print(f"Bearish Sweeps: {len(bearish)}")

print("\n===== BULLISH SWEEP WIN RATE =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH SWEEP WIN RATE =====")
print(f"1 Candle: {bearish_wr_1:.2f}%")
print(f"3 Candles: {bearish_wr_3:.2f}%")
print(f"6 Candles: {bearish_wr_6:.2f}%")

print("\n===== AVERAGE RETURNS =====")
print(f"Bullish 1 Candle Avg: {bullish['forward_1'].mean():.4f}%")
print(f"Bullish 3 Candle Avg: {bullish['forward_3'].mean():.4f}%")
print(f"Bullish 6 Candle Avg: {bullish['forward_6'].mean():.4f}%")

print(f"Bearish 1 Candle Avg: {bearish['forward_1'].mean():.4f}%")
print(f"Bearish 3 Candle Avg: {bearish['forward_3'].mean():.4f}%")
print(f"Bearish 6 Candle Avg: {bearish['forward_6'].mean():.4f}%")

signals.to_csv("eurusd_h4_daily_sweep_results.csv", index=False)

print("\nCSV Export Complete.")