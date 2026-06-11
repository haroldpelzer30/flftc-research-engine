import duckdb
import pandas as pd

# ==========================================
# CONFIG
# ==========================================
TABLE_NAME = "eurusd_h4"

# ==========================================
# CONNECT
# ==========================================
conn = duckdb.connect("flftc_research.duckdb")

# ==========================================
# LOAD DATA
# ==========================================
df = conn.execute(f"""
SELECT *
FROM {TABLE_NAME}
ORDER BY trade_date, trade_time
""").fetchdf()

print(f"Rows Loaded: {len(df)}")

# ==========================================
# DATE CONVERSION
# ==========================================
df["trade_date"] = pd.to_datetime(df["trade_date"])

# ==========================================
# BUILD DAILY HIGH / LOW LEVELS
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
# DAILY SWEEP LOGIC
# ==========================================
df["signal"] = None

# Bullish Sweep
df.loc[
    (df["low"] < df["prev_daily_low"])
    &
    (df["close"] > df["prev_daily_low"]),
    "signal"
] = "BULLISH_SWEEP"

# Bearish Sweep
df.loc[
    (df["high"] > df["prev_daily_high"])
    &
    (df["close"] < df["prev_daily_high"]),
    "signal"
] = "BEARISH_SWEEP"

# ==========================================
# FORWARD RETURNS
# ==========================================
df["forward_1"] = (
    (df["close"].shift(-1) - df["close"])
    / df["close"]
) * 100

df["forward_3"] = (
    (df["close"].shift(-3) - df["close"])
    / df["close"]
) * 100

df["forward_6"] = (
    (df["close"].shift(-6) - df["close"])
    / df["close"]
) * 100

signals = df[df["signal"].notna()].copy()

bullish = signals[
    signals["signal"] == "BULLISH_SWEEP"
]

bearish = signals[
    signals["signal"] == "BEARISH_SWEEP"
]

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
print("\n===== EURUSD H4 DAILY SWEEP RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")

print(f"\nBullish Sweep Signals: {len(bullish)}")
print(f"Bearish Sweep Signals: {len(bearish)}")

print("\n===== BULLISH SWEEP RESULTS =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH SWEEP RESULTS =====")
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
    "eurusd_daily_sweep_results.csv",
    index=False
)

print("\nCSV Export Complete.")