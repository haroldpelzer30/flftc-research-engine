import MetaTrader5 as mt5
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

symbols = ["EURUSD", "XAUUSD", "NASUSD", "SPXUSD"]

if not mt5.initialize():
    print("MT5 connection failed:", mt5.last_error())
    quit()

print("CONNECTED TO MT5")
print("-" * 60)

for symbol in symbols:
    print("\n" + "=" * 60)
    print(f"SYMBOL: {symbol}")

    selected = mt5.symbol_select(symbol, True)

    if not selected:
        print(f"Could not select symbol: {symbol}")
        continue

    rates = mt5.copy_rates_from_pos(
        symbol,
        mt5.TIMEFRAME_H4,
        0,
        10
    )

    if rates is None or len(rates) == 0:
        print(f"No candle data returned for {symbol}")
        continue

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")

    print(df[["time", "open", "high", "low", "close", "tick_volume"]].tail())

mt5.shutdown()

print("\nMT5 connection closed.")