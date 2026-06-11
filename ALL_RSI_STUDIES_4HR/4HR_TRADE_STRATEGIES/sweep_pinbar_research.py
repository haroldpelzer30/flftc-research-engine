import duckdb
import pandas as pd

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD DATA
# =========================

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

# =========================
# PREVIOUS DAILY LEVELS
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

# =========================
# MERGE DAILY LEVELS
# =========================

df = pd.merge(
    h4,
    levels,
    on="trade_date",
    how="left"
)

# =========================
# CANDLE MEASUREMENTS
# =========================

df["body"] = abs(df["close"] - df["open"])

df["upper_wick"] = (
    df["high"] - df[["open", "close"]].max(axis=1)
)

df["lower_wick"] = (
    df[["open", "close"]].min(axis=1) - df["low"]
)

df["range"] = df["high"] - df["low"]

# =========================
# PINBAR DETECTION
# =========================

df["bullish_pinbar"] = (
    (df["lower_wick"] > df["body"] * 2)
    &
    (df["close"] > df["open"])
)

df["bearish_pinbar"] = (
    (df["upper_wick"] > df["body"] * 2)
    &
    (df["close"] < df["open"])
)

# =========================
# SWEEP + PINBAR LOGIC
# =========================

df["signal"] = None

# Bullish Sweep + Bullish Pinbar

df.loc[
    (
        (df["low"] < df["prev_day_low"])
        &
        (df["close"] > df["prev_day_low"])
        &
        (df["bullish_pinbar"])
    ),
    "signal"
] = "BULLISH_SWEEP_PINBAR"

# Bearish Sweep + Bearish Pinbar

df.loc[
    (
        (df["high"] > df["prev_day_high"])
        &
        (df["close"] < df["prev_day_high"])
        &
        (df["bearish_pinbar"])
    ),
    "signal"
] = "BEARISH_SWEEP_PINBAR"

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

signals = df[
    df["signal"].notna()
]

bullish = signals[
    signals["signal"] == "BULLISH_SWEEP_PINBAR"
]

bearish = signals[
    signals["signal"] == "BEARISH_SWEEP_PINBAR"
]

# =========================
# WIN RATES
# =========================

bullish_wr_1 = (
    (bullish["forward_1"] > 0).mean()
) * 100

bullish_wr_3 = (
    (bullish["forward_3"] > 0).mean()
) * 100

bullish_wr_6 = (
    (bullish["forward_6"] > 0).mean()
) * 100

bearish_wr_1 = (
    (bearish["forward_1"] < 0).mean()
) * 100

bearish_wr_3 = (
    (bearish["forward_3"] < 0).mean()
) * 100

bearish_wr_6 = (
    (bearish["forward_6"] < 0).mean()
) * 100

# =========================
# RESULTS
# =========================

print("\n===== SWEEP + PINBAR RESEARCH =====\n")

print(f"Bullish Signals: {len(bullish)}")
print(f"Bearish Signals: {len(bearish)}")

print("\n===== BULLISH WIN RATE =====")

print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH WIN RATE =====")

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
    "eurusd_sweep_pinbar_results.csv",
    index=False
)

print("\nCSV Export Complete.")