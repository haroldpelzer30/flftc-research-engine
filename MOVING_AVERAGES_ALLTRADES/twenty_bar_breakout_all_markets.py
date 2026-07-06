# twenty_bar_breakout_all_markets.py

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

LOOKBACK_BARS = 20
FORWARD_PERIODS = [1, 3, 6]


def run_twenty_bar_breakout(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["prev_20_high"] = df["high"].shift(1).rolling(LOOKBACK_BARS).max()
    df["prev_20_low"] = df["low"].shift(1).rolling(LOOKBACK_BARS).min()

    df["signal"] = None

    # Bullish 20-bar breakout:
    # Price breaks and closes above the highest high of the previous 20 candles
    df.loc[
        (df["high"] > df["prev_20_high"]) &
        (df["close"] > df["prev_20_high"]),
        "signal"
    ] = "BULLISH_20_BAR_BREAKOUT"

    # Bearish 20-bar breakout:
    # Price breaks and closes below the lowest low of the previous 20 candles
    df.loc[
        (df["low"] < df["prev_20_low"]) &
        (df["close"] < df["prev_20_low"]),
        "signal"
    ] = "BEARISH_20_BAR_BREAKOUT"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_20_BAR_BREAKOUT"]
    bearish = signals[signals["signal"] == "BEARISH_20_BAR_BREAKOUT"]

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
        f"{asset.lower()}_twenty_bar_breakout_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_twenty_bar_breakout(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "twenty_bar_breakout_all_markets_summary.csv",
        index=False
    )

    print("\n===== 20-BAR BREAKOUT ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("twenty_bar_breakout_all_markets_summary.csv")


if __name__ == "__main__":
    main()