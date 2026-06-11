import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "xauusd_h4"

RSI_PERIOD = 14

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD GOLD H4 DATA
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
# INSIDE BAR LOGIC
# =========================

# Current candle is INSIDE previous candle

df["inside_bar"] = (
    (df["high"] < df["high"].shift(1))
    &
    (df["low"] > df["low"].shift(1))
)

# =========================
# SIGNAL CONDITIONS
# =========================

df["signal"] = None

# Bullish:
# RSI oversold + inside bar

df.loc[
    (
        df["rsi"] <= 20
    )
    &
    (
        df["inside_bar"]
    ),
    "signal"
] = "BULLISH_INSIDE_BAR"

# Bearish:
# RSI overbought + inside bar

df.loc[
    (
        df["rsi"] >= 80
    )
    &
    (
        df["inside_bar"]
    ),
    "signal"
] = "BEARISH_INSIDE_BAR"

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
    signals["signal"] == "BULLISH_INSIDE_BAR"
]

bearish = signals[
    signals["signal"] == "BEARISH_INSIDE_BAR"
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

print("\n===== GOLD H4 RSI + INSIDE BAR =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"RSI Period: {RSI_PERIOD}")

print(f"\nBullish Inside Bar Signals: {len(bullish)}")
print(f"Bearish Inside Bar Signals: {len(bearish)}")

print("\n===== BULLISH INSIDE BAR RESULTS =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH INSIDE BAR RESULTS =====")
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
    "gold_h4_rsi_insidebar_results.csv",
    index=False
)

print("\nCSV Export Complete.")