import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT", "5432"),
    sslmode="require"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    symbol,
    candle_time,
    close,
    rsi,
    ema20,
    ema50,
    ema200,
    trend_state
FROM market_candles
WHERE symbol = 'EURUSD'
ORDER BY candle_time DESC
LIMIT 5;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()