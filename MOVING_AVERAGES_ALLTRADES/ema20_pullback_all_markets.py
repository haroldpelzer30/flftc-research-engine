# ema20_pullback_all_markets.py

import duckdb
import pandas as pd

DB_FILE = "flftc_research.duckdb"

MARKETS = [
    "eurusd_h4",
    "gbpusd_h4",
    "usdchf_h4",
    "audusd_h4",
    "nzdusd_h4",
    "usdcad_h4",
    "usdjpy_h4",
    "xauusd_h4",
    "sp500_h4",
    "nas100_h4",
]

FORWARD_PERIODS = [1, 3, 6]

EMA_FAST = 20
EMA_TREND = 50
PULLBACK_THRESHOLD_PCT = 0.15


def run_ema20_pullback(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["ema20"] = df["close"].ewm(span=EMA_FAST, adjust=False).mean()
    df["ema50"] = df["close"].ewm(span=EMA_TREND, adjust=False).mean()

    df["distance_to_ema20_pct"] = (
        (df["close"] - df["ema20"]) / df["ema20"]
    ) * 100

    df["signal"] = None

    # Bullish Pullback:
    # Price is above EMA50 trend filter
    # Price pulls back near EMA20
    # Candle closes bullish
    df.loc[
        (df["close"] > df["ema50"]) &
        (df["distance_to_ema20_pct"].abs() <= PULLBACK_THRESHOLD_PCT) &
        (df["close"] > df["open"]),
        "signal"
    ] = "BULLISH_EMA20_PULLBACK"

    # Bearish Pullback:
    # Price is below EMA50 trend filter
    # Price pulls back near EMA20
    # Candle closes bearish
    df.loc[
        (df["close"] < df["ema50"]) &
        (df["distance_to_ema20_pct"].abs() <= PULLBACK_THRESHOLD_PCT) &
        (df["close"] < df["open"]),
        "signal"
    ] = "BEARISH_EMA20_PULLBACK"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_EMA20_PULLBACK"]
    bearish = signals[signals["signal"] == "BEARISH_EMA20_PULLBACK"]

    asset = table_name.replace("_h4", "").upper()

    row = {
        "Asset": asset,
        "Bullish Signals": len(bullish),
        "Bearish Signals": len(bearish),
        "Total Signals": len(signals),
    }

    for period in FORWARD_PERIODS:
        row[f"Bullish {period} Candle"] = (
            (bullish[f"forward_{period}"] > 0).mean() * 100
            if len(bullish) > 0 else 0
        )

        row[f"Bearish {period} Candle"] = (
            (bearish[f"forward_{period}"] < 0).mean() * 100
            if len(bearish) > 0 else 0
        )

        row[f"Bullish {period} Avg"] = (
            bullish[f"forward_{period}"].mean()
            if len(bullish) > 0 else 0
        )

        row[f"Bearish {period} Avg"] = (
            bearish[f"forward_{period}"].mean()
            if len(bearish) > 0 else 0
        )

    signals.to_csv(
        f"{asset.lower()}_ema20_pullback_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_ema20_pullback(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "ema20_pullback_all_markets_summary.csv",
        index=False
    )

    print("\n===== EMA20 PULLBACK ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("ema20_pullback_all_markets_summary.csv")


if __name__ == "__main__":
    main()