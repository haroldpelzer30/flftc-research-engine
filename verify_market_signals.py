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
    timeframe,
    candle_time,
    setup,
    direction,
    score,
    tier,
    current_price,
    rsi,
    trend_state,
    context,
    created_at
FROM market_signals
ORDER BY created_at DESC;
""")

rows = cursor.fetchall()

print("\nMARKET SIGNALS")
print("=" * 100)

for row in rows:
    print(f"""
Symbol: {row[0]}
Timeframe: {row[1]}
Candle Time: {row[2]}
Setup: {row[3]}
Direction: {row[4]}
Score: {row[5]}
Tier: {row[6]}
Price: {row[7]}
RSI: {row[8]}
Trend: {row[9]}
Context: {row[10]}
Created: {row[11]}
{"-" * 100}
""")

print(f"\nTotal Signals Found: {len(rows)}")

cursor.close()
conn.close()

print("\nVerification complete.")