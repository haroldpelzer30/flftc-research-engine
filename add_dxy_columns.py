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
ADD COLUMN IF NOT EXISTS dxy_trend TEXT,
ADD COLUMN IF NOT EXISTS dxy_score INTEGER,
ADD COLUMN IF NOT EXISTS dxy_interpretation TEXT;
""")

conn.commit()

cur.close()
conn.close()

print("DXY columns added.")