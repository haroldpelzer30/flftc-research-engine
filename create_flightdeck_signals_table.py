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
CREATE TABLE IF NOT EXISTS flightdeck_signals (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    candle_time TIMESTAMP NOT NULL,
    close_price DOUBLE PRECISION,
    ema20 DOUBLE PRECISION,
    ema50 DOUBLE PRECISION,
    ema200 DOUBLE PRECISION,
    rsi DOUBLE PRECISION,
    signal TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cur.close()
conn.close()

print("flightdeck_signals table ready.")