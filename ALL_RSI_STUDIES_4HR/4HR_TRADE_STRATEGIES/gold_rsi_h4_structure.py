import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

H4_TABLE = "xauusd_h4"

RSI_PERIOD = 14
NEAR_LEVEL_PCT = 0.08

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD H4 GOLD DATA
# =========================

df = conn.execute(f"""
SELECT *
FROM {H4_TABLE}
ORDER BY trade_date, trade_time
""").fetchdf()

# =========================
# CREATE PREVIOUS H4 STRUCTURE
# =========================

df["prev_h4_high"] = df["high"].shift(1)
df["prev_h4_low"] = df["low"].shift(1)

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
# DISTANCE TO H4 STRUCTURE
# =========================

df["distance_to_prev_h4_high_pct"] = (
    (df["close"] - df["prev_h4_high"])
    / df["prev_h4_high"]
) * 100

df["distance_to_prev_h4_low_pct"] = (
    (df["close"] - df["prev_h4_low"])
    / df["prev_h4_low"]
) * 100

# =========================
# SIGNAL CONDITIONS
# =========================

df["signal"] = None

# Bullish:
# H4 RSI oversold near previous H4 low

df.loc[
    (
        df["distance_to_prev_h4_low_pct"].abs()
        <= NEAR_LEVEL_PCT
    )
    &
    (
        df["rsi"] <= 20
    ),
    "signal"
] = "BULLISH"

# Bearish:
# H4 RSI overbought near previous H4 high

df.loc[
    (
        df["distance_to_prev_h4_high_pct"].abs()
        <= NEAR_LEVEL_PCT
    )
    &
    (
        df["rsi"] >= 80
    ),
    "signal"
] = "BEARISH"

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
    signals["signal"] == "BULLISH"
]

bearish = signals[
    signals["signal"] == "BEARISH"
]

# =========================
# WIN RATES
# =========================

bullish_wr_1 = (
    bullish["forward_1"] > 0
).mean() * 100

bullish_wr_3 = (
    bullish["forward_3"] > 0
).mean() * 100

bullish_wr_6 = (
    bullish["forward_6"] > 0
).mean() * 100

bearish_wr_1 = (
    bearish["forward_1"] < 0
).mean() * 100

bearish_wr_3 = (
    bearish["forward_3"] < 0
).mean() * 100

bearish_wr_6 = (
    bearish["forward_6"] < 0
).mean() * 100

# =========================
# RESULTS
# =========================

print("\n===== GOLD H4 RSI + H4 STRUCTURE =====\n")

print(f"H4 Table Tested: {H4_TABLE}")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Near H4 Level Threshold: {NEAR_LEVEL_PCT}%")

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
    "gold_h4_rsi_h4_structure.csv",
    index=False
)

print("\nCSV Export Complete.")