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
    id,
    ema20,
    ema50,
    ema200
FROM flightdeck_signals
""")

rows = cur.fetchall()

for row in rows:

    signal_id = row[0]
    ema20 = row[1]
    ema50 = row[2]
    ema200 = row[3]

    trend = "Neutral"

    if ema20 > ema50 and ema50 > ema200:
        trend = "Bullish"

    elif ema20 < ema50 and ema50 < ema200:
        trend = "Bearish"

    cur.execute("""
        UPDATE flightdeck_signals
        SET trend = %s
        WHERE id = %s
    """, (trend, signal_id))

conn.commit()

cur.close()
conn.close()

print("Trend values updated successfully.")