# ema50_sma50_all_markets.py

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


def run_ema_sma_cross(table_name, con):

    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    # Moving Averages

    df["ema50"] = df["close"].ewm(span=50, adjust=False).mean()

    df["sma50"] = (
        df["close"]
        .rolling(window=50)
        .mean()
    )

    # Previous Values

    df["prev_ema50"] = df["ema50"].shift(1)
    df["prev_sma50"] = df["sma50"].shift(1)

    df["signal"] = None

    # Golden Cross

    df.loc[
        (df["prev_ema50"] <= df["prev_sma50"]) &
        (df["ema50"] > df["sma50"]),
        "signal"
    ] = "BULLISH_CROSS"

    # Death Cross

    df.loc[
        (df["prev_ema50"] >= df["prev_sma50"]) &
        (df["ema50"] < df["sma50"]),
        "signal"
    ] = "BEARISH_CROSS"

    for period in FORWARD_PERIODS:

        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"])
            / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[
        signals["signal"] == "BULLISH_CROSS"
    ]

    bearish = signals[
        signals["signal"] == "BEARISH_CROSS"
    ]

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
        f"{asset.lower()}_ema50_sma50_results.csv",
        index=False
    )

    return row


def main():

    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:

        try:

            results.append(
                run_ema_sma_cross(
                    market,
                    con
                )
            )

        except Exception as e:

            print(
                f"ERROR processing {market}: {e}"
            )

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "ema50_sma50_all_markets_summary.csv",
        index=False
    )

    print(
        "\n===== EMA50 / SMA50 CROSS ALL MARKETS SUMMARY =====\n"
    )

    print(
        summary.to_string(index=False)
    )

    print("\nCSV Export Complete:")
    print(
        "ema50_sma50_all_markets_summary.csv"
    )


if __name__ == "__main__":
    main()