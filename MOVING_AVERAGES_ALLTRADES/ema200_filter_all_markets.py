# ema200_filter_all_markets.py

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
EMA_TREND = 200


def run_ema200_filter(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["ema200"] = df["close"].ewm(span=EMA_TREND, adjust=False).mean()

    df["signal"] = None

    # Bullish trend filter:
    # Price closes above EMA200
    df.loc[
        df["close"] > df["ema200"],
        "signal"
    ] = "BULLISH_ABOVE_EMA200"

    # Bearish trend filter:
    # Price closes below EMA200
    df.loc[
        df["close"] < df["ema200"],
        "signal"
    ] = "BEARISH_BELOW_EMA200"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_ABOVE_EMA200"]
    bearish = signals[signals["signal"] == "BEARISH_BELOW_EMA200"]

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
        f"{asset.lower()}_ema200_filter_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_ema200_filter(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "ema200_filter_all_markets_summary.csv",
        index=False
    )

    print("\n===== EMA200 FILTER ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("ema200_filter_all_markets_summary.csv")


if __name__ == "__main__":
    main()