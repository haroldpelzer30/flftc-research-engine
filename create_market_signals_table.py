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
CREATE TABLE IF NOT EXISTS market_signals (
    id SERIAL PRIMARY KEY,

    symbol VARCHAR(20) NOT NULL,
    timeframe VARCHAR(10) NOT NULL,

    candle_time TIMESTAMP NOT NULL,

    setup VARCHAR(100),
    direction VARCHAR(20),

    score INTEGER,
    tier VARCHAR(30),

    current_price NUMERIC,

    rsi NUMERIC,
    ema20 NUMERIC,
    ema50 NUMERIC,
    ema200 NUMERIC,

    trend_state VARCHAR(20),
    context TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()

cursor.close()
conn.close()

print("market_signals table created successfully.")