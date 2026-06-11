import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "xauusd_d1"

RSI_PERIOD = 14
LOOKBACK_BARS = 10
NEAR_LEVEL_PCT = 0.20

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD GOLD DAILY DATA
# =========================

df = conn.execute(f"""
SELECT *
FROM {TABLE_NAME}
ORDER BY trade_date
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
# DOUBLE BOTTOM / DOUBLE TOP STRUCTURE
# =========================

df["recent_low"] = (
    df["low"]
    .shift(1)
    .rolling(window=LOOKBACK_BARS)
    .min()
)

df["recent_high"] = (
    df["high"]
    .shift(1)
    .rolling(window=LOOKBACK_BARS)
    .max()
)

# =========================
# DISTANCE TO STRUCTURE
# =========================

df["distance_to_recent_low_pct"] = (
    (df["close"] - df["recent_low"])
    / df["recent_low"]
) * 100

df["distance_to_recent_high_pct"] = (
    (df["close"] - df["recent_high"])
    / df["recent_high"]
) * 100

# =========================
# SIGNAL CONDITIONS
# =========================

df["signal"] = None

# Bullish Double Bottom

df.loc[
    (
        df["rsi"] <= 20
    )
    &
    (
        df["distance_to_recent_low_pct"].abs()
        <= NEAR_LEVEL_PCT
    ),
    "signal"
] = "DOUBLE_BOTTOM_BULLISH"

# Bearish Double Top

df.loc[
    (
        df["rsi"] >= 80
    )
    &
    (
        df["distance_to_recent_high_pct"].abs()
        <= NEAR_LEVEL_PCT
    ),
    "signal"
] = "DOUBLE_TOP_BEARISH"

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

df["forward_5"] = (
    (df["close"].shift(-5) - df["close"])
    / df["close"]
) * 100

# =========================
# FILTER SIGNALS
# =========================

signals = df[df["signal"].notna()].copy()

bullish = signals[
    signals["signal"] == "DOUBLE_BOTTOM_BULLISH"
]

bearish = signals[
    signals["signal"] == "DOUBLE_TOP_BEARISH"
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

bullish_wr_5 = (
    bullish["forward_5"] > 0
).mean() * 100

bearish_wr_1 = (
    bearish["forward_1"] < 0
).mean() * 100

bearish_wr_3 = (
    bearish["forward_3"] < 0
).mean() * 100

bearish_wr_5 = (
    bearish["forward_5"] < 0
).mean() * 100

# =========================
# RESULTS
# =========================

print("\n===== GOLD DAILY RSI + DOUBLE BOTTOM / DOUBLE TOP =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Lookback Bars: {LOOKBACK_BARS}")
print(f"Near Level Threshold: {NEAR_LEVEL_PCT}%")

print(f"\nBullish Double Bottom Signals: {len(bullish)}")
print(f"Bearish Double Top Signals: {len(bearish)}")

print("\n===== BULLISH DOUBLE BOTTOM RESULTS =====")
print(f"1 Day: {bullish_wr_1:.2f}%")
print(f"3 Days: {bullish_wr_3:.2f}%")
print(f"5 Days: {bullish_wr_5:.2f}%")

print("\n===== BEARISH DOUBLE TOP RESULTS =====")
print(f"1 Day: {bearish_wr_1:.2f}%")
print(f"3 Days: {bearish_wr_3:.2f}%")
print(f"5 Days: {bearish_wr_5:.2f}%")

print("\n===== AVERAGE RETURNS =====")

print(f"Bullish 1 Day Avg: {bullish['forward_1'].mean():.4f}%")
print(f"Bullish 3 Day Avg: {bullish['forward_3'].mean():.4f}%")
print(f"Bullish 5 Day Avg: {bullish['forward_5'].mean():.4f}%")

print(f"Bearish 1 Day Avg: {bearish['forward_1'].mean():.4f}%")
print(f"Bearish 3 Day Avg: {bearish['forward_3'].mean():.4f}%")
print(f"Bearish 5 Day Avg: {bearish['forward_5'].mean():.4f}%")

# =========================
# EXPORT
# =========================

signals.to_csv(
    "gold_daily_rsi_doublebottom_results.csv",
    index=False
)

print("\nCSV Export Complete.")