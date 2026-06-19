import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "NZDUSD", "USDCAD",
    "XAUUSD", "XAGUSD", "NASUSD", "SPXUSD"
]

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT", "5432"),
    sslmode="require"
)

cursor = conn.cursor()

print("\nLATEST MARKET SNAPSHOT")
print("=" * 80)

for symbol in SYMBOLS:
    cursor.execute("""
        SELECT
            symbol,
            timeframe,
            candle_time,
            open,
            high,
            low,
            close,
            tick_volume,
            rsi,
            ema20,
            ema50,
            ema200,
            trend_state
        FROM market_candles
        WHERE symbol = %s AND timeframe = 'H4'
        ORDER BY candle_time DESC
        LIMIT 1;
    """, (symbol,))

    row = cursor.fetchone()

    if row:
        print(f"\n{row[0]} | {row[1]} | {row[2]}")
        print(f"Open: {row[3]}  High: {row[4]}  Low: {row[5]}  Close: {row[6]}")
        print(f"Volume: {row[7]}")
        print(f"RSI: {row[8]}")
        print(f"EMA20: {row[9]}")
        print(f"EMA50: {row[10]}")
        print(f"EMA200: {row[11]}")
        print(f"Trend: {row[12]}")
    else:
        print(f"\nNo data found for {symbol}")

cursor.close()
conn.close()

print("\nSnapshot complete.")