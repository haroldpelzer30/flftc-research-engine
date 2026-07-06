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
SELECT id, symbol
FROM flightdeck_signals
""")

rows = cur.fetchall()

for row in rows:

    signal_id = row[0]
    symbol = row[1]

    historical_win_rate = 0
    research_score = 0

    # Research Database

    if symbol == "XAUUSD":
        historical_win_rate = 64.07
        research_score = 30

    elif symbol == "XAGUSD":
        historical_win_rate = 62.50
        research_score = 25

    elif symbol == "NASUSD":
        historical_win_rate = 62.50
        research_score = 25

    elif symbol == "EURUSD":
        historical_win_rate = 56.25
        research_score = 15

    elif symbol == "GBPUSD":
        historical_win_rate = 54.66
        research_score = 10

    elif symbol == "USDCHF":
        historical_win_rate = 57.00
        research_score = 15

    elif symbol == "AUDUSD":
        historical_win_rate = 55.02
        research_score = 10

    elif symbol == "NZDUSD":
        historical_win_rate = 53.31
        research_score = 10

    cur.execute("""
        UPDATE flightdeck_signals
        SET historical_win_rate = %s,
            research_score = %s
        WHERE id = %s
    """, (
        historical_win_rate,
        research_score,
        signal_id
    ))

conn.commit()

cur.close()
conn.close()

print("Research scores updated successfully.")