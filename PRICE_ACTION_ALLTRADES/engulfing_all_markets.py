# engulfing_all_markets.py

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


def run_engulfing(table_name, con):
    print(f"\nProcessing {table_name}...")

    df = con.execute(f"""
        SELECT *
        FROM {table_name}
        ORDER BY trade_date, trade_time
    """).df()

    df["prev_open"] = df["open"].shift(1)
    df["prev_close"] = df["close"].shift(1)

    df["prev_body_high"] = df[["prev_open", "prev_close"]].max(axis=1)
    df["prev_body_low"] = df[["prev_open", "prev_close"]].min(axis=1)

    df["curr_body_high"] = df[["open", "close"]].max(axis=1)
    df["curr_body_low"] = df[["open", "close"]].min(axis=1)

    df["prev_bearish"] = df["prev_close"] < df["prev_open"]
    df["prev_bullish"] = df["prev_close"] > df["prev_open"]

    df["curr_bullish"] = df["close"] > df["open"]
    df["curr_bearish"] = df["close"] < df["open"]

    df["signal"] = None

    # Bullish Engulfing:
    # Previous candle bearish
    # Current candle bullish
    # Current body fully engulfs previous body
    df.loc[
        (df["prev_bearish"]) &
        (df["curr_bullish"]) &
        (df["curr_body_high"] >= df["prev_body_high"]) &
        (df["curr_body_low"] <= df["prev_body_low"]),
        "signal"
    ] = "BULLISH_ENGULFING"

    # Bearish Engulfing:
    # Previous candle bullish
    # Current candle bearish
    # Current body fully engulfs previous body
    df.loc[
        (df["prev_bullish"]) &
        (df["curr_bearish"]) &
        (df["curr_body_high"] >= df["prev_body_high"]) &
        (df["curr_body_low"] <= df["prev_body_low"]),
        "signal"
    ] = "BEARISH_ENGULFING"

    for period in FORWARD_PERIODS:
        df[f"forward_{period}"] = (
            (df["close"].shift(-period) - df["close"]) / df["close"]
        ) * 100

    signals = df[df["signal"].notna()].copy()

    bullish = signals[signals["signal"] == "BULLISH_ENGULFING"]
    bearish = signals[signals["signal"] == "BEARISH_ENGULFING"]

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
        f"{asset.lower()}_engulfing_results.csv",
        index=False
    )

    return row


def main():
    con = duckdb.connect(DB_FILE)

    results = []

    for market in MARKETS:
        try:
            results.append(run_engulfing(market, con))
        except Exception as e:
            print(f"ERROR processing {market}: {e}")

    con.close()

    summary = pd.DataFrame(results)

    summary.to_csv(
        "engulfing_all_markets_summary.csv",
        index=False
    )

    print("\n===== ENGULFING ALL MARKETS SUMMARY =====\n")
    print(summary.to_string(index=False))

    print("\nCSV Export Complete:")
    print("engulfing_all_markets_summary.csv")


if __name__ == "__main__":
    main()