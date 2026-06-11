import duckdb
import pandas as pd

# =========================
# CONNECT TO DUCKDB
# =========================

conn = duckdb.connect("flftc_research.duckdb")

# =========================
# LOAD H4 DATA
# =========================

h4 = conn.execute("""
SELECT *
FROM eurusd_h4
ORDER BY trade_date, trade_time
""").fetchdf()

# =========================
# LOAD DAILY DATA
# =========================

daily = conn.execute("""
SELECT *
FROM eurusd_d1
ORDER BY trade_date
""").fetchdf()

# =========================
# CALCULATE H4 RSI
# =========================

delta_h4 = h4["close"].diff()

gain_h4 = delta_h4.where(delta_h4 > 0, 0)
loss_h4 = -delta_h4.where(delta_h4 < 0, 0)

avg_gain_h4 = gain_h4.rolling(window=14).mean()
avg_loss_h4 = loss_h4.rolling(window=14).mean()

rs_h4 = avg_gain_h4 / avg_loss_h4

h4["rsi_h4"] = 100 - (100 / (1 + rs_h4))

# =========================
# CALCULATE DAILY RSI
# =========================

delta_d1 = daily["close"].diff()

gain_d1 = delta_d1.where(delta_d1 > 0, 0)
loss_d1 = -delta_d1.where(delta_d1 < 0, 0)

avg_gain_d1 = gain_d1.rolling(window=14).mean()
avg_loss_d1 = loss_d1.rolling(window=14).mean()

rs_d1 = avg_gain_d1 / avg_loss_d1

daily["rsi_d1"] = 100 - (100 / (1 + rs_d1))

# =========================
# KEEP DAILY RSI ONLY
# =========================

daily_rsi = daily[
    [
        "trade_date",
        "rsi_d1"
    ]
]

# =========================
# MERGE DAILY INTO H4
# =========================

merged = pd.merge(
    h4,
    daily_rsi,
    on="trade_date",
    how="left"
)

# =========================
# CREATE SIGNALS
# =========================

merged["signal"] = None

# Oversold Alignment
merged.loc[
    (merged["rsi_h4"] <= 20) &
    (merged["rsi_d1"] <= 30),
    "signal"
] = "OVERSOLD_ALIGN"

# Overbought Alignment
merged.loc[
    (merged["rsi_h4"] >= 80) &
    (merged["rsi_d1"] >= 70),
    "signal"
] = "OVERBOUGHT_ALIGN"

# =========================
# FORWARD RETURNS
# =========================

merged["forward_1"] = (
    (merged["close"].shift(-1) - merged["close"])
    / merged["close"]
) * 100

merged["forward_3"] = (
    (merged["close"].shift(-3) - merged["close"])
    / merged["close"]
) * 100

merged["forward_6"] = (
    (merged["close"].shift(-6) - merged["close"])
    / merged["close"]
) * 100

# =========================
# FILTER SIGNALS
# =========================

signals = merged[
    merged["signal"].notna()
]

# =========================
# DISPLAY SAMPLE
# =========================

print("\n===== MULTI-TIMEFRAME RSI SIGNALS =====\n")

print(
    signals[
        [
            "trade_date",
            "trade_time",
            "close",
            "rsi_h4",
            "rsi_d1",
            "signal",
            "forward_1",
            "forward_3",
            "forward_6"
        ]
    ].tail(20)
)

# =========================
# STATISTICS
# =========================

print("\n===== STATISTICS =====\n")

oversold = signals[
    signals["signal"] == "OVERSOLD_ALIGN"
]

overbought = signals[
    signals["signal"] == "OVERBOUGHT_ALIGN"
]

# =========================
# WIN RATE CALCULATIONS
# =========================

# Oversold continuation:
# Did price continue DOWN?

oversold_winrate_1 = (
    (oversold["forward_1"] < 0).mean()
) * 100

oversold_winrate_3 = (
    (oversold["forward_3"] < 0).mean()
) * 100

oversold_winrate_6 = (
    (oversold["forward_6"] < 0).mean()
) * 100

# Overbought continuation:
# Did price continue UP?

overbought_winrate_1 = (
    (overbought["forward_1"] > 0).mean()
) * 100

overbought_winrate_3 = (
    (overbought["forward_3"] > 0).mean()
) * 100

overbought_winrate_6 = (
    (overbought["forward_6"] > 0).mean()
) * 100

# =========================
# DISPLAY RESULTS
# =========================

print(f"Oversold Alignment Signals: {len(oversold)}")
print(f"Overbought Alignment Signals: {len(overbought)}")

print("\n===== OVERSOLD CONTINUATION WIN RATE =====\n")

print(f"1 Candle: {oversold_winrate_1:.2f}%")
print(f"3 Candles: {oversold_winrate_3:.2f}%")
print(f"6 Candles: {oversold_winrate_6:.2f}%")

print("\n===== OVERBOUGHT CONTINUATION WIN RATE =====\n")

print(f"1 Candle: {overbought_winrate_1:.2f}%")
print(f"3 Candles: {overbought_winrate_3:.2f}%")
print(f"6 Candles: {overbought_winrate_6:.2f}%")

# =========================
# EXPORT CSV
# =========================

signals.to_csv(
    "eurusd_multitimeframe_rsi.csv",
    index=False
)

print("\nCSV Export Complete.")