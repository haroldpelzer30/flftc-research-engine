import os
import MetaTrader5 as mt5
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "USDCHF",
    "AUDUSD",
    "NZDUSD",
    "USDCAD",
    "XAUUSD",
    "XAGUSD",
    "NASUSD",
    "SPXUSD"
]

# -------------------------
# Connect to MT5
# -------------------------

if not mt5.initialize():
    print("MT5 connection failed:", mt5.last_error())
    quit()

print("Connected to MT5")

# -------------------------
# Connect to Postgres
# -------------------------

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT", "5432"),
    sslmode="require"
)

cursor = conn.cursor()

# -------------------------
# Pull candles and insert
# -------------------------

rows_inserted = 0

for symbol in SYMBOLS:

    print(f"Processing {symbol}...")

    mt5.symbol_select(symbol, True)

    rates = mt5.copy_rates_from_pos(
        symbol,
        mt5.TIMEFRAME_H4,
        0,
        100
    )

    if rates is None or len(rates) == 0:
        print(f"No data for {symbol}")
        continue

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT INTO market_candles (
            symbol,
            timeframe,
            candle_time,
            open,
            high,
            low,
            close,
            tick_volume
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (symbol, timeframe, candle_time)
        DO NOTHING
        """,
        (
            symbol,
            "H4",
            row["time"],
            float(row["open"]),
            float(row["high"]),
            float(row["low"]),
            float(row["close"]),
            int(row["tick_volume"])
        ))

        rows_inserted += 1

conn.commit()

cursor.close()
conn.close()
mt5.shutdown()

print()
print("=" * 50)
print(f"Finished. Attempted inserts: {rows_inserted}")
print("=" * 50)