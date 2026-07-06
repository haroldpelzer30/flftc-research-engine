import duckdb
import pandas as pd

# ==========================================
# CONFIG
# ==========================================
TABLE_NAME = "nas100_h4"

BB_PERIOD = 20
BB_STD = 2

LOOKBACK_BARS = 10
NEAR_LEVEL_PCT = 0.15

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
# BOLLINGER BANDS
# ==========================================
df["sma"] = df["close"].rolling(BB_PERIOD).mean()
df["std"] = df["close"].rolling(BB_PERIOD).std()

df["upper_band"] = df["sma"] + BB_STD * df["std"]
df["lower_band"] = df["sma"] - BB_STD * df["std"]

# ==========================================
# DOUBLE BOTTOM / DOUBLE TOP
# ==========================================
df["recent_low"] = df["low"].shift(1).rolling(LOOKBACK_BARS).min()
df["recent_high"] = df["high"].shift(1).rolling(LOOKBACK_BARS).max()

df["distance_to_recent_low_pct"] = (
    (df["close"] - df["recent_low"]) / df["recent_low"]
) * 100

df["distance_to_recent_high_pct"] = (
    (df["close"] - df["recent_high"]) / df["recent_high"]
) * 100

# ==========================================
# SIGNALS
# ==========================================
df["signal"] = None

df.loc[
    (df["close"] < df["lower_band"])
    &
    (df["distance_to_recent_low_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BB_DOUBLE_BOTTOM_BULLISH"

df.loc[
    (df["close"] > df["upper_band"])
    &
    (df["distance_to_recent_high_pct"].abs() <= NEAR_LEVEL_PCT),
    "signal"
] = "BB_DOUBLE_TOP_BEARISH"

# ==========================================
# FORWARD RETURNS
# ==========================================
df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_6"] = ((df["close"].shift(-6) - df["close"]) / df["close"]) * 100

signals = df[df["signal"].notna()].copy()

bullish = signals[signals["signal"] == "BB_DOUBLE_BOTTOM_BULLISH"]
bearish = signals[signals["signal"] == "BB_DOUBLE_TOP_BEARISH"]

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
print("\n===== NAS100 H4 BOLLINGER BAND + DOUBLE BOTTOM / DOUBLE TOP =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"BB Period: {BB_PERIOD}")
print(f"BB Std Dev: {BB_STD}")
print(f"Lookback Bars: {LOOKBACK_BARS}")
print(f"Near Level Threshold: {NEAR_LEVEL_PCT}%")

print(f"\nBullish Double Bottom Signals: {len(bullish)}")
print(f"Bearish Double Top Signals: {len(bearish)}")

print("\n===== BULLISH DOUBLE BOTTOM RESULTS =====")
print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH DOUBLE TOP RESULTS =====")
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
    "nas100_bb_doublebottom_results.csv",
    index=False
)

print("\nCSV Export Complete.")