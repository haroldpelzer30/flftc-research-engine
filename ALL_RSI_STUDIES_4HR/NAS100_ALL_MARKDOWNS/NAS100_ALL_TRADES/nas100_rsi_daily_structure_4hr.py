import duckdb
import pandas as pd

# ==========================================
# CONFIG
# ==========================================
H4_TABLE = "nas100_h4"
RSI_PERIOD = 14
NEAR_LEVEL_PCT = 0.10

# ==========================================
# CONNECT
# ==========================================
conn = duckdb.connect("flftc_research.duckdb")

# ==========================================
# LOAD H4 DATA
# ==========================================
df = conn.execute(f"""
SELECT *
FROM {H4_TABLE}
ORDER BY trade_date, trade_time
""").fetchdf()

print(f"H4 Rows Loaded: {len(df)}")

# ==========================================
# DATE CONVERSION
# ==========================================
df["trade_date"] = pd.to_datetime(df["trade_date"])

# ==========================================
# BUILD DAILY STRUCTURE FROM H4 DATA
# ==========================================
daily = df.groupby("trade_date").agg(
    daily_high=("high", "max"),
    daily_low=("low", "min")
).reset_index()

daily["prev_daily_high"] = daily["daily_high"].shift(1)
daily["prev_daily_low"] = daily["daily_low"].shift(1)

df = pd.merge(
    df,
    daily[["trade_date", "prev_daily_high", "prev_daily_low"]],
    on="trade_date",
    how="left"
)

# ==========================================
# CALCULATE RSI
# ==========================================
delta = df["close"].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(window=RSI_PERIOD).mean()
avg_loss = loss.rolling(window=RSI_PERIOD).mean()

rs = avg_gain / avg_loss
df["rsi"] = 100 - (100 / (1 + rs))

# ==========================================
# DISTANCE TO DAILY LEVELS
# ==========================================
df["distance_to_low_pct"] = (
    (df["close"] - df["prev_daily_low"]) / df["prev_daily_low"]
) * 100

df["distance_to_high_pct"] = (
    (df["close"] - df["prev_daily_high"]) / df["prev_daily_high"]
) * 100

# ==========================================
# SIGNALS
# ==========================================
df["signal"] = None

df.loc[
    (df["rsi"] <= 20)
    &
    (df["distance_to_low_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BULLISH"

df.loc[
    (df["rsi"] >= 80)
    &
    (df["distance_to_high_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BEARISH"

# ==========================================
# FORWARD RETURNS
# ==========================================
df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_6"] = ((df["close"].shift(-6) - df["close"]) / df["close"]) * 100

signals = df[df["signal"].notna()].copy()

bullish = signals[signals["signal"] == "BULLISH"]
bearish = signals[signals["signal"] == "BEARISH"]

# ==========================================
# WIN RATES
# ==========================================
bullish_wr_1 = (bullish["forward_1"] > 0).mean() * 100
bullish_wr_3 = (bullish["forward_3"] > 0).mean() * 100
bullish_wr_6 = (bullish["forward_6"] > 0).mean() * 100

bearish_wr_1 = (bearish["forward_1"] < 0).mean() * 100
bearish_wr_3 = (bearish["forward_3"] < 0).mean() * 100
bearish_wr_6 = (bearish["forward_6"] < 0).mean() * 100

# ==========================================
# OUTPUT
# ==========================================
print("\n===== NAS100 H4 RSI + DAILY STRUCTURE =====\n")

print(f"H4 Table Tested: {H4_TABLE}")
print("Daily Structure: Derived from H4 data")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Near Daily Level Threshold: {NEAR_LEVEL_PCT}%")

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

# ==========================================
# EXPORT CSV
# ==========================================
signals.to_csv(
    "nas100_h4_rsi_daily_structure_results.csv",
    index=False
)

print("\nCSV Export Complete.")