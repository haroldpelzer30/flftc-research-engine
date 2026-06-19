# daily_low_all_markets.py

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


def run_daily_low_breakout(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date

    daily_levels = df.groupby("trade_date").agg(
        daily_high=("high", "max"),
        daily_low=("low", "min")
    ).reset_index()

    daily_levels["prev_daily_low"] = daily_levels["daily_low"].shift(1)

    df = pd.merge(
        df,
        daily_levels[["trade_date", "prev_daily_low"]],
        on="trade_date",
        how="left"
    )

    df["signal"] = None

    df.loc[
        (df["low"] < df["prev_daily_low"]) &
        (df["close"] < df["prev_daily_low"]),
        "signal"
    ] = "BEARISH_DAILY_LOW_BREAKOUT"

    df["breakout_count"] = (
        df["signal"].eq("BEARISH_DAILY_LOW_BREAKOUT")
        .groupby(df["trade_date"])
        .cumsum()
    )

    df.loc[
        (df["signal"] == "BEARISH_DAILY_LOW_BREAKOUT") &
        (df["breakout_count"] > 1),
        "signal"
    ] = None

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bearish = signals[
        signals["signal"] == "BEARISH_DAILY_LOW_BREAKOUT"
    ]

    asset = table_name.replace("_h4", "").upper()

    row = {
        "Asset": asset,
        "Bearish Signals": len(bearish),
        "Total Signals": len(signals),
    }

    for period in FORWARD_PERIODS:
        row[f"Bearish {period} Candle"] = (
            (bearish[f"forward_{period}"] < 0).mean() * 100
            if len(bearish) > 0 else 0
        )

        row[f"Bearish {period} Avg"] = (
            bearish[f"forward_{period}"].mean()
            if len(bearish) > 0 else 0
        )

    signals.to_csv(
        f"{asset.lower()}_daily_low_breakout_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_daily_low_breakout(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "daily_low_all_markets_summary.csv",
        index=False
    )

    print("\n===== DAILY LOW BREAKOUT ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("daily_low_all_markets_summary.csv")


if __name__ == "__main__":
    main()