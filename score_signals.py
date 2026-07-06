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
SELECT id, symbol, candle_time, close_price, rsi, signal
FROM flightdeck_signals
ORDER BY candle_time DESC;
""")

rows = cur.fetchall()

for row in rows:
    signal_id, symbol, candle_time, close_price, rsi, signal = row

    score = 0

    if signal == "RSI Oversold":
        if rsi <= 20:
            score = 90
        elif rsi <= 25:
            score = 80
        elif rsi <= 30:
            score = 70

    elif signal == "RSI Overbought":
        if rsi >= 80:
            score = 90
        elif rsi >= 75:
            score = 80
        elif rsi >= 70:
            score = 70

    if score >= 90:
        tier = "Hall of Fame"
    elif score >= 80:
        tier = "Tier 1"
    elif score >= 70:
        tier = "Tier 2"
    elif score >= 60:
        tier = "Tier 3"
    else:
        tier = "No Tier"

    print(symbol, candle_time, signal, round(rsi, 2), score, tier)

cur.close()
conn.close()