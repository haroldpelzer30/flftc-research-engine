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
    score,
    research_score,
    trend,
    daily_structure_score
FROM flightdeck_signals
""")

rows = cur.fetchall()

for row in rows:

    signal_id = row[0]
    score = row[1] or 0
    research_score = row[2] or 0
    trend = row[3]
    daily_structure_score = row[4] or 0

    trend_score = 0

    if trend == "Bullish":
        trend_score = 10

    elif trend == "Bearish":
        trend_score = 10

    final_score = (
        score
        + research_score
        + trend_score
        + daily_structure_score
    )

    cur.execute("""
        UPDATE flightdeck_signals
        SET final_score = %s
        WHERE id = %s
    """, (final_score, signal_id))

conn.commit()

cur.close()
conn.close()

print("Final scores v2 updated successfully.")