# newyork_breakout_all_markets.py

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

NY_START = "13:00:00"
NY_END = "17:00:00"


def run_newyork_breakout(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date
    df["trade_time"] = pd.to_datetime(df["trade_time"].astype(str)).dt.time

    ny_start = pd.to_datetime(NY_START).time()
    ny_end = pd.to_datetime(NY_END).time()

    ny_range = df[
        (df["trade_time"] >= ny_start) &
        (df["trade_time"] < ny_end)
    ].copy()

    daily_ny = ny_range.groupby("trade_date").agg(
        ny_high=("high", "max"),
        ny_low=("low", "min")
    ).reset_index()

    df = pd.merge(df, daily_ny, on="trade_date", how="left")

    df["signal"] = None
    after_ny = df["trade_time"] >= ny_end

    df.loc[
        after_ny &
        (df["high"] > df["ny_high"]) &
        (df["close"] > df["ny_high"]),
        "signal"
    ] = "BULLISH_NEWYORK_BREAKOUT"

    df.loc[
        after_ny &
        (df["low"] < df["ny_low"]) &
        (df["close"] < df["ny_low"]),
        "signal"
    ] = "BEARISH_NEWYORK_BREAKOUT"

    df["bullish_count"] = (
        df["signal"].eq("BULLISH_NEWYORK_BREAKOUT")
        .groupby(df["trade_date"])
        .cumsum()
    )

    df["bearish_count"] = (
        df["signal"].eq("BEARISH_NEWYORK_BREAKOUT")
        .groupby(df["trade_date"])
        .cumsum()
    )

    df.loc[
        (df["signal"] == "BULLISH_NEWYORK_BREAKOUT") &
        (df["bullish_count"] > 1),
        "signal"
    ] = None

    df.loc[
        (df["signal"] == "BEARISH_NEWYORK_BREAKOUT") &
        (df["bearish_count"] > 1),
        "signal"
    ] = None

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_NEWYORK_BREAKOUT"]
    bearish = signals[signals["signal"] == "BEARISH_NEWYORK_BREAKOUT"]

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
        f"{asset.lower()}_newyork_breakout_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_newyork_breakout(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "newyork_breakout_all_markets_summary.csv",
        index=False
    )

    print("\n===== NEW YORK BREAKOUT ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("newyork_breakout_all_markets_summary.csv")


if __name__ == "__main__":
    main()