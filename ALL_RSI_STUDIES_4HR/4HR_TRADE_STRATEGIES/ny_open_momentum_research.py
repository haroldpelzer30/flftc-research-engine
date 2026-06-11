import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "eurusd_h4"

# Your H4 candle times:
# 00:00
# 04:00
# 08:00
# 12:00
# 16:00
# 20:00

# Using 12:00 as NY Open proxy
NY_START = "12:00:00"

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
# IDENTIFY NY OPEN CANDLE
# =========================

ny = df[
    df["trade_time"].astype(str) == NY_START
].copy()

# =========================
# CREATE MOMENTUM DIRECTION
# =========================

ny["momentum"] = None

ny.loc[
    ny["close"] > ny["open"],
    "momentum"
] = "BULLISH_NY_OPEN"

ny.loc[
    ny["close"] < ny["open"],
    "momentum"
] = "BEARISH_NY_OPEN"

signals = ny[
    ny["momentum"].notna()
].copy()

# =========================
# FORWARD RETURNS
# =========================

signals["forward_1"] = (
    (signals["close"].shift(-1) - signals["close"])
    / signals["close"]
) * 100

signals["forward_3"] = (
    (signals["close"].shift(-3) - signals["close"])
    / signals["close"]
) * 100

signals["forward_6"] = (
    (signals["close"].shift(-6) - signals["close"])
    / signals["close"]
) * 100

# =========================
# SPLIT SIGNALS
# =========================

bullish = signals[
    signals["momentum"] == "BULLISH_NY_OPEN"
]

bearish = signals[
    signals["momentum"] == "BEARISH_NY_OPEN"
]

# =========================
# WIN RATE
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

print("\n===== NY OPEN MOMENTUM RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"NY Open Time Tested: {NY_START}")

print(f"Total NY Signals: {len(signals)}")
print(f"Bullish NY Opens: {len(bullish)}")
print(f"Bearish NY Opens: {len(bearish)}")

print("\n===== BULLISH NY OPEN WIN RATE =====")

print(f"1 Candle: {bullish_wr_1:.2f}%")
print(f"3 Candles: {bullish_wr_3:.2f}%")
print(f"6 Candles: {bullish_wr_6:.2f}%")

print("\n===== BEARISH NY OPEN WIN RATE =====")

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
    "eurusd_ny_open_momentum_results.csv",
    index=False
)

print("\nCSV Export Complete.")