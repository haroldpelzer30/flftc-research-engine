import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "eurusd_h4"

RSI_PERIOD = 14
BB_PERIOD = 20
BB_STD = 2

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD DATA
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
# CALCULATE BOLLINGER BANDS
# =========================

df["bb_mid"] = df["close"].rolling(window=BB_PERIOD).mean()
df["bb_std"] = df["close"].rolling(window=BB_PERIOD).std()

df["bb_upper"] = df["bb_mid"] + (df["bb_std"] * BB_STD)
df["bb_lower"] = df["bb_mid"] - (df["bb_std"] * BB_STD)

# =========================
# RSI + BOLLINGER SIGNALS
# =========================

df["signal"] = None

# Bullish mean reversion setup
# RSI oversold + close below lower Bollinger Band

df.loc[
    (df["rsi"] <= 20) &
    (df["close"] < df["bb_lower"]),
    "signal"
] = "BULLISH_RSI_BB"

# Bearish mean reversion setup
# RSI overbought + close above upper Bollinger Band

df.loc[
    (df["rsi"] >= 80) &
    (df["close"] > df["bb_upper"]),
    "signal"
] = "BEARISH_RSI_BB"

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

bullish = signals[signals["signal"] == "BULLISH_RSI_BB"]
bearish = signals[signals["signal"] == "BEARISH_RSI_BB"]

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

print("\n===== RSI + BOLLINGER BAND RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"RSI Period: {RSI_PERIOD}")
print(f"Bollinger Period: {BB_PERIOD}")
print(f"Bollinger Std Dev: {BB_STD}")

print(f"\nBullish RSI + BB Signals: {len(bullish)}")
print(f"Bearish RSI + BB Signals: {len(bearish)}")

print("\n===== BULLISH RSI + BB WIN RATE =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH RSI + BB WIN RATE =====")
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

signals.to_csv("eurusd_rsi_bollinger_results.csv", index=False)

print("\nCSV Export Complete.")