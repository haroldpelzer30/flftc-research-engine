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
SELECT symbol, COUNT(*)
FROM market_candles
GROUP BY symbol
ORDER BY symbol;
""")

rows = cursor.fetchall()

print("\nRows by symbol:")
print("-" * 40)

for row in rows:
    print(f"{row[0]} : {row[1]}")

cursor.close()
conn.close()