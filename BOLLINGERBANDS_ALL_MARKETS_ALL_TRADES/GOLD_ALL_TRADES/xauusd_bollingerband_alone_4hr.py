import duckdb
import pandas as pd

# ==========================================
# CONFIG
# ==========================================
TABLE_NAME = "xauusd_h4"

BB_PERIOD = 20
BB_STD = 2

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
# SIGNALS
# ==========================================
df["signal"] = None

df.loc[df["close"] < df["lower_band"], "signal"] = "LOWER_BAND"
df.loc[df["close"] > df["upper_band"], "signal"] = "UPPER_BAND"

# ==========================================
# FORWARD RETURNS
# ==========================================
df["forward_1"] = ((df["close"].shift(-1) - df["close"]) / df["close"]) * 100
df["forward_3"] = ((df["close"].shift(-3) - df["close"]) / df["close"]) * 100
df["forward_6"] = ((df["close"].shift(-6) - df["close"]) / df["close"]) * 100

signals = df[df["signal"].notna()].copy()

lower_band = signals[signals["signal"] == "LOWER_BAND"]
upper_band = signals[signals["signal"] == "UPPER_BAND"]

# ==========================================
# WIN RATES
# ==========================================
lower_wr_1 = (lower_band["forward_1"] > 0).mean() * 100
lower_wr_3 = (lower_band["forward_3"] > 0).mean() * 100
lower_wr_6 = (lower_band["forward_6"] > 0).mean() * 100

upper_wr_1 = (upper_band["forward_1"] < 0).mean() * 100
upper_wr_3 = (upper_band["forward_3"] < 0).mean() * 100
upper_wr_6 = (upper_band["forward_6"] < 0).mean() * 100

# ==========================================
# OUTPUT
# ==========================================
print("\n===== XAUUSD H4 BOLLINGER BAND ALONE RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"BB Period: {BB_PERIOD}")
print(f"BB Std Dev: {BB_STD}")

print(f"\nLower Band Signals: {len(lower_band)}")
print(f"Upper Band Signals: {len(upper_band)}")

print("\n===== LOWER BAND REVERSAL WIN RATE =====")
print(f"1 Candle: {lower_wr_1:.2f}%")
print(f"3 Candles: {lower_wr_3:.2f}%")
print(f"6 Candles: {lower_wr_6:.2f}%")

print("\n===== UPPER BAND REVERSAL WIN RATE =====")
print(f"1 Candle: {upper_wr_1:.2f}%")
print(f"3 Candles: {upper_wr_3:.2f}%")
print(f"6 Candles: {upper_wr_6:.2f}%")

print("\n===== AVERAGE RETURNS =====")
print(f"Lower Band 1 Candle Avg: {lower_band['forward_1'].mean():.4f}%")
print(f"Lower Band 3 Candle Avg: {lower_band['forward_3'].mean():.4f}%")
print(f"Lower Band 6 Candle Avg: {lower_band['forward_6'].mean():.4f}%")

print(f"Upper Band 1 Candle Avg: {upper_band['forward_1'].mean():.4f}%")
print(f"Upper Band 3 Candle Avg: {upper_band['forward_3'].mean():.4f}%")
print(f"Upper Band 6 Candle Avg: {upper_band['forward_6'].mean():.4f}%")

# ==========================================
# EXPORT CSV
# ==========================================
signals.to_csv(
    "xauusd_bb_alone_results.csv",
    index=False
)

print("\nCSV Export Complete.")