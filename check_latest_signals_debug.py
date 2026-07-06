from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT"),
    sslmode="require"
)

cur = conn.cursor()

cur.execute("""
SELECT
    symbol,
    candle_time,
    close_price,
    rsi,
    signal,
    final_score,
    tier,
    created_at
FROM flightdeck_signals
ORDER BY candle_time DESC, created_at DESC
LIMIT 50;
""")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()