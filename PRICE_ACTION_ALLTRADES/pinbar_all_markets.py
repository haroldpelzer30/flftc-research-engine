# pinbar_all_markets.py

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

# Pin bar settings
WICK_TO_BODY_RATIO = 2.0
MAX_BODY_TO_RANGE = 0.35


def run_pinbar(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["candle_range"] = df["high"] - df["low"]
    df["body_size"] = (df["close"] - df["open"]).abs()

    df["upper_wick"] = df["high"] - df[["open", "close"]].max(axis=1)
    df["lower_wick"] = df[["open", "close"]].min(axis=1) - df["low"]

    df["body_to_range"] = df["body_size"] / df["candle_range"]

    df["signal"] = None

    # Bullish Pin Bar:
    # Long lower wick, small body
    df.loc[
        (df["candle_range"] > 0) &
        (df["body_to_range"] <= MAX_BODY_TO_RANGE) &
        (df["lower_wick"] >= df["body_size"] * WICK_TO_BODY_RATIO) &
        (df["lower_wick"] > df["upper_wick"]),
        "signal"
    ] = "BULLISH_PINBAR"

    # Bearish Pin Bar:
    # Long upper wick, small body
    df.loc[
        (df["candle_range"] > 0) &
        (df["body_to_range"] <= MAX_BODY_TO_RANGE) &
        (df["upper_wick"] >= df["body_size"] * WICK_TO_BODY_RATIO) &
        (df["upper_wick"] > df["lower_wick"]),
        "signal"
    ] = "BEARISH_PINBAR"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_PINBAR"]
    bearish = signals[signals["signal"] == "BEARISH_PINBAR"]

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
        f"{asset.lower()}_pinbar_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_pinbar(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "pinbar_all_markets_summary.csv",
        index=False
    )

    print("\n===== PIN BAR ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("pinbar_all_markets_summary.csv")


if __name__ == "__main__":
    main()