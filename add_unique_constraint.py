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
ALTER TABLE flightdeck_signals
ADD CONSTRAINT unique_symbol_candle_time
UNIQUE (symbol, candle_time);
""")

conn.commit()
cur.close()
conn.close()

print("Unique constraint added.")