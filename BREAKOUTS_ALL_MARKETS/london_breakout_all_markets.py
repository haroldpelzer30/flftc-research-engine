# london_breakout_all_markets.py

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

# Adjust later if your broker time is different
LONDON_START = "07:00:00"
LONDON_END = "11:00:00"


def run_london_breakout(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date
    df["trade_time"] = pd.to_datetime(df["trade_time"].astype(str)).dt.time

    london_start = pd.to_datetime(LONDON_START).time()
    london_end = pd.to_datetime(LONDON_END).time()

    london_range = df[
        (df["trade_time"] >= london_start) &
        (df["trade_time"] < london_end)
    ].copy()

    daily_london = london_range.groupby("trade_date").agg(
        london_high=("high", "max"),
        london_low=("low", "min")
    ).reset_index()

    df = pd.merge(
        df,
        daily_london,
        on="trade_date",
        how="left"
    )

    df["signal"] = None

    after_london = df["trade_time"] >= london_end

    df.loc[
        after_london &
        (df["high"] > df["london_high"]) &
        (df["close"] > df["london_high"]),
        "signal"
    ] = "BULLISH_LONDON_BREAKOUT"

    df.loc[
        after_london &
        (df["low"] < df["london_low"]) &
        (df["close"] < df["london_low"]),
        "signal"
    ] = "BEARISH_LONDON_BREAKOUT"

    # Keep only the first breakout signal per direction per day
    df["bullish_count"] = (
        df["signal"].eq("BULLISH_LONDON_BREAKOUT")
        .groupby(df["trade_date"])
        .cumsum()
    )

    df["bearish_count"] = (
        df["signal"].eq("BEARISH_LONDON_BREAKOUT")
        .groupby(df["trade_date"])
        .cumsum()
    )

    df.loc[
        (df["signal"] == "BULLISH_LONDON_BREAKOUT") &
        (df["bullish_count"] > 1),
        "signal"
    ] = None

    df.loc[
        (df["signal"] == "BEARISH_LONDON_BREAKOUT") &
        (df["bearish_count"] > 1),
        "signal"
    ] = None

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_LONDON_BREAKOUT"]
    bearish = signals[signals["signal"] == "BEARISH_LONDON_BREAKOUT"]

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
        f"{asset.lower()}_london_breakout_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_london_breakout(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "london_breakout_all_markets_summary.csv",
        index=False
    )

    print("\n===== LONDON BREAKOUT ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("london_breakout_all_markets_summary.csv")


if __name__ == "__main__":
    main()