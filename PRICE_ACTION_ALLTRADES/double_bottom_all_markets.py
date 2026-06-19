# double_bottom_all_markets.py

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

LOOKBACK_BARS = 10
NEAR_LEVEL_PCT = 0.15
FORWARD_PERIODS = [1, 3, 6]


def run_double_bottom(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["recent_low"] = df["low"].shift(1).rolling(LOOKBACK_BARS).min()
    df["recent_high"] = df["high"].shift(1).rolling(LOOKBACK_BARS).max()

    df["distance_to_recent_low_pct"] = (
        (df["close"] - df["recent_low"]) / df["recent_low"]
    ) * 100

    df["distance_to_recent_high_pct"] = (
        (df["close"] - df["recent_high"]) / df["recent_high"]
    ) * 100

    df["signal"] = None

    df.loc[
        df["distance_to_recent_low_pct"].abs() <= NEAR_LEVEL_PCT,
        "signal"
    ] = "DOUBLE_BOTTOM_BULLISH"

    df.loc[
        df["distance_to_recent_high_pct"].abs() <= NEAR_LEVEL_PCT,
        "signal"
    ] = "DOUBLE_TOP_BEARISH"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "DOUBLE_BOTTOM_BULLISH"]
    bearish = signals[signals["signal"] == "DOUBLE_TOP_BEARISH"]

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
        f"{asset.lower()}_double_bottom_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_double_bottom(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "double_bottom_all_markets_summary.csv",
        index=False
    )

    print("\n===== DOUBLE BOTTOM / DOUBLE TOP ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("double_bottom_all_markets_summary.csv")


if __name__ == "__main__":
    main()