import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

H4_TABLE = "xauusd_h4"
D1_TABLE = "xauusd_d1"

RSI_PERIOD = 14
NEAR_LEVEL_PCT = 0.10

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD DATA
# =========================

h4 = conn.execute(f"""
SELECT *
FROM {H4_TABLE}
ORDER BY trade_date, trade_time
""").fetchdf()

d1 = conn.execute(f"""
SELECT *
FROM {D1_TABLE}
ORDER BY trade_date
""").fetchdf()

# =========================
# DAILY STRUCTURE LEVELS
# =========================

d1["prev_day_high"] = d1["high"].shift(1)
d1["prev_day_low"] = d1["low"].shift(1)

levels = d1[
    [
        "trade_date",
        "prev_day_high",
        "prev_day_low"
    ]
]

df = pd.merge(
    h4,
    levels,
    on="trade_date",
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
# DISTANCE TO STRUCTURE
# =========================

df["distance_to_prev_high_pct"] = (
    (df["close"] - df["prev_day_high"]) / df["prev_day_high"]
) * 100

df["distance_to_prev_low_pct"] = (
    (df["close"] - df["prev_day_low"]) / df["prev_day_low"]
) * 100

# =========================
# RSI + DAILY STRUCTURE SIGNALS
# =========================

df["signal"] = None

# Bullish setup:
# RSI oversold near previous daily low

df.loc[
    (
        df["distance_to_prev_low_pct"].abs() <= NEAR_LEVEL_PCT
    )
    &
    (
        df["rsi"] <= 20
    ),
    "signal"
] = "RSI_OVERSOLD_AT_PREV_DAILY_LOW"

# Bearish setup:
# RSI overbought near previous daily high

df.loc[
    (
        df["distance_to_prev_high_pct"].abs() <= NEAR_LEVEL_PCT
    )
    &
    (
        df["rsi"] >= 80
    ),
    "signal"
] = "RSI_OVERBOUGHT_AT_PREV_DAILY_HIGH"

# =========================
# FORWARD RETURNS
# =========================

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

# =========================
# FILTER SIGNALS
# =========================

signals = df[df["signal"].notna()].copy()

bullish = signals[
    signals["signal"] == "RSI_OVERSOLD_AT_PREV_DAILY_LOW"
]

bearish = signals[
    signals["signal"] == "RSI_OVERBOUGHT_AT_PREV_DAILY_HIGH"
]

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

print("\n===== GOLD RSI + PREVIOUS DAILY HIGH/LOW RESEARCH =====\n")

print(f"H4 Table Tested: {H4_TABLE}")
print(f"Daily Table Used: {D1_TABLE}")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Near Level Threshold: {NEAR_LEVEL_PCT}%")

print(f"\nBullish Signals: {len(bullish)}")
print(f"Bearish Signals: {len(bearish)}")

print("\n===== BULLISH RSI OVERSOLD AT PREVIOUS DAILY LOW =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH RSI OVERBOUGHT AT PREVIOUS DAILY HIGH =====")
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
    "gold_rsi_daily_structure_results.csv",
    index=False
)

print("\nCSV Export Complete.")