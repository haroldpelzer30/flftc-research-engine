import duckdb
import pandas as pd

# =========================
# SETTINGS
# =========================

TABLE_NAME = "eurusd_h4"

ASIAN_START = "00:00:00"
ASIAN_END = "06:00:00"

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
# BUILD ASIAN SESSION RANGE
# =========================

asian = df[
    (df["trade_time"].astype(str) >= ASIAN_START) &
    (df["trade_time"].astype(str) <= ASIAN_END)
]

asian_range = asian.groupby("trade_date").agg(
    asian_high=("high", "max"),
    asian_low=("low", "min")
).reset_index()

# =========================
# MERGE ASIAN LEVELS INTO H4 DATA
# =========================

df = pd.merge(
    df,
    asian_range,
    on="trade_date",
    how="left"
)

# =========================
# LONDON SESSION CANDLES
# =========================

london = df[
    df["trade_time"].astype(str) > ASIAN_END
].copy()

# =========================
# DETECT BREAKOUTS
# =========================

london["breakout"] = None

london.loc[
    london["high"] > london["asian_high"],
    "breakout"
] = "BUY_BREAKOUT"

london.loc[
    london["low"] < london["asian_low"],
    "breakout"
] = "SELL_BREAKOUT"

signals = london[london["breakout"].notna()].copy()

# Keep only the FIRST breakout per day
signals = signals.sort_values(
    ["trade_date", "trade_time"]
).groupby("trade_date").first().reset_index()

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
# SPLIT BUY / SELL
# =========================

buy = signals[signals["breakout"] == "BUY_BREAKOUT"]
sell = signals[signals["breakout"] == "SELL_BREAKOUT"]

# =========================
# WIN RATE
# =========================

buy_wr_1 = (buy["forward_1"] > 0).mean() * 100
buy_wr_3 = (buy["forward_3"] > 0).mean() * 100
buy_wr_6 = (buy["forward_6"] > 0).mean() * 100

sell_wr_1 = (sell["forward_1"] < 0).mean() * 100
sell_wr_3 = (sell["forward_3"] < 0).mean() * 100
sell_wr_6 = (sell["forward_6"] < 0).mean() * 100

# =========================
# RESULTS
# =========================

print("\n===== LONDON BREAKOUT RESEARCH =====\n")

print(f"Table Tested: {TABLE_NAME}")
print(f"Total Breakout Days: {len(signals)}")
print(f"Buy Breakouts: {len(buy)}")
print(f"Sell Breakouts: {len(sell)}")

print("\n===== BUY BREAKOUT WIN RATE =====")
print(f"1 Candle: {buy_wr_1:.2f}%")
print(f"3 Candles: {buy_wr_3:.2f}%")
print(f"6 Candles: {buy_wr_6:.2f}%")

print("\n===== SELL BREAKOUT WIN RATE =====")
print(f"1 Candle: {sell_wr_1:.2f}%")
print(f"3 Candles: {sell_wr_3:.2f}%")
print(f"6 Candles: {sell_wr_6:.2f}%")

print("\n===== AVERAGE RETURNS =====")
print(f"Buy 1 Candle Avg: {buy['forward_1'].mean():.4f}%")
print(f"Buy 3 Candle Avg: {buy['forward_3'].mean():.4f}%")
print(f"Buy 6 Candle Avg: {buy['forward_6'].mean():.4f}%")

print(f"Sell 1 Candle Avg: {sell['forward_1'].mean():.4f}%")
print(f"Sell 3 Candle Avg: {sell['forward_3'].mean():.4f}%")
print(f"Sell 6 Candle Avg: {sell['forward_6'].mean():.4f}%")

# =========================
# EXPORT
# =========================

signals.to_csv("eurusd_london_breakout_results.csv", index=False)

print("\nCSV Export Complete.")