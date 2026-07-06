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
SELECT id, rsi, signal
FROM flightdeck_signals
""")

rows = cur.fetchall()

for row in rows:
    signal_id = row[0]
    rsi = row[1]
    signal = row[2]

    daily_structure = "Neutral"
    daily_structure_score = 0

    if signal == "RSI Oversold":
        daily_structure = "Near Daily Low"
        daily_structure_score = 20

    elif signal == "RSI Overbought":
        daily_structure = "Near Daily High"
        daily_structure_score = 20

    cur.execute("""
        UPDATE flightdeck_signals
        SET daily_structure = %s,
            daily_structure_score = %s
        WHERE id = %s
    """, (
        daily_structure,
        daily_structure_score,
        signal_id
    ))

conn.commit()

cur.close()
conn.close()

print("Daily structure values updated successfully.")