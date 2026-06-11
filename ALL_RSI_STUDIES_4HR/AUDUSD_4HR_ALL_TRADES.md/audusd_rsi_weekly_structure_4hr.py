import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "audusd_h4"
RSI_PERIOD = 14
NEAR_LEVEL_PCT = 0.15

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD AUDUSD H4 DATA
# =========================

df = conn.execute(f"""
SELECT *
FROM {TABLE_NAME}
ORDER BY trade_date, trade_time
""").fetchdf()

df["trade_date"] = pd.to_datetime(df["trade_date"])

# =========================
# WEEKLY STRUCTURE FROM H4 DATA
# =========================

df["week"] = df["trade_date"].dt.to_period("W").astype(str)

weekly = df.groupby("week").agg(
    weekly_high=("high", "max"),
    weekly_low=("low", "min")
).reset_index()

weekly["prev_week_high"] = weekly["weekly_high"].shift(1)
weekly["prev_week_low"] = weekly["weekly_low"].shift(1)

df = pd.merge(
    df,
    weekly[["week", "prev_week_high", "prev_week_low"]],
    on="week",
    how="left"
)

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
# DISTANCE TO WEEKLY STRUCTURE
# =========================

df["distance_to_prev_week_high_pct"] = (
    (df["close"] - df["prev_week_high"]) / df["prev_week_high"]
) * 100

df["distance_to_prev_week_low_pct"] = (
    (df["close"] - df["prev_week_low"]) / df["prev_week_low"]
) * 100

# =========================
# SIGNAL CONDITIONS
# =========================

df["signal"] = None

df.loc[
    (df["rsi"] <= 20)
    &
    (df["distance_to_prev_week_low_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BULLISH_WEEKLY_STRUCTURE"

df.loc[
    (df["rsi"] >= 80)
    &
    (df["distance_to_prev_week_high_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BEARISH_WEEKLY_STRUCTURE"

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

bullish = signals[signals["signal"] == "BULLISH_WEEKLY_STRUCTURE"]
bearish = signals[signals["signal"] == "BEARISH_WEEKLY_STRUCTURE"]

# =========================
# WIN RATES
# =========================

bullish_wr_1 = (bullish["forward_1"] > 0).mean() * 100
bullish_wr_3 = (bullish["forward_3"] > 0).mean() * 100
bullish_wr_6 = (bullish["forward_6"] > 0).mean() * 100

bearish_wr_1 = (bearish["forward_1"] < 0).mean() * 100
bearish_wr_3 = (bearish["forward_3"] < 0).mean() * 100
bearish_wr_6 = (bearish["forward_6"] < 0).mean() * 100

# =========================
# RESULTS
# =========================

print("\n===== AUDUSD H4 RSI + WEEKLY STRUCTURE =====\n")

print(f"H4 Table Tested: {TABLE_NAME}")
print("Weekly Structure: Derived from H4 data")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Near Weekly Level Threshold: {NEAR_LEVEL_PCT}%")

print(f"\nBullish Signals: {len(bullish)}")
print(f"Bearish Signals: {len(bearish)}")

print("\n===== BULLISH RESULTS =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH RESULTS =====")
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

# =========================
# EXPORT
# =========================

signals.to_csv(
    "audusd_h4_rsi_weekly_structure_results.csv",
    index=False
)

print("\nCSV Export Complete.")