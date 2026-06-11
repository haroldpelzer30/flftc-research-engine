import duckdb
import pandas as pd

conn = duckdb.connect("flftc_research.duckdb")

df = conn.execute("""
SELECT *
FROM eurusd_d1
ORDER BY trade_date
""").fetchdf()

df["prev_day_high"] = df["high"].shift(1)
df["prev_day_low"] = df["low"].shift(1)

df["signal"] = None

df.loc[
    (df["low"] < df["prev_day_low"]) &
    (df["close"] > df["prev_day_low"]),
    "signal"
] = "BULLISH_DAILY_SWEEP"

df.loc[
    (df["high"] > df["prev_day_high"]) &
    (df["close"] < df["prev_day_high"]),
    "signal"
] = "BEARISH_DAILY_SWEEP"

df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_5"] = ((df["close"].shift(-5) - df["close"]) / df["close"]) * 100

signals = df[df["signal"].notna()].copy()

bullish = signals[signals["signal"] == "BULLISH_DAILY_SWEEP"]
bearish = signals[signals["signal"] == "BEARISH_DAILY_SWEEP"]

print("\n===== EURUSD DAILY CHART SWEEP RESEARCH =====\n")

print(f"Bullish Daily Sweeps: {len(bullish)}")
print(f"Bearish Daily Sweeps: {len(bearish)}")

print("\n===== BULLISH SWEEP WIN RATE =====")
print(f"1 Day: {(bullish['forward_1'] > 0).mean() * 100:.2f}%")
print(f"3 Days: {(bullish['forward_3'] > 0).mean() * 100:.2f}%")
print(f"5 Days: {(bullish['forward_5'] > 0).mean() * 100:.2f}%")

print("\n===== BEARISH SWEEP WIN RATE =====")
print(f"1 Day: {(bearish['forward_1'] < 0).mean() * 100:.2f}%")
print(f"3 Days: {(bearish['forward_3'] < 0).mean() * 100:.2f}%")
print(f"5 Days: {(bearish['forward_5'] < 0).mean() * 100:.2f}%")

print("\n===== AVERAGE RETURNS =====")
print(f"Bullish 1 Day Avg: {bullish['forward_1'].mean():.4f}%")
print(f"Bullish 3 Day Avg: {bullish['forward_3'].mean():.4f}%")
print(f"Bullish 5 Day Avg: {bullish['forward_5'].mean():.4f}%")

print(f"Bearish 1 Day Avg: {bearish['forward_1'].mean():.4f}%")
print(f"Bearish 3 Day Avg: {bearish['forward_3'].mean():.4f}%")
print(f"Bearish 5 Day Avg: {bearish['forward_5'].mean():.4f}%")

signals.to_csv("eurusd_daily_chart_sweep_results.csv", index=False)

print("\nCSV Export Complete.")