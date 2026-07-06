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

major_pairs = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "NZDUSD",
    "USDJPY",
    "USDCHF",
    "USDCAD"
]

cur.execute("""
SELECT DISTINCT ON (symbol)
    symbol,
    candle_time,
    trend
FROM flightdeck_signals
WHERE symbol IN ('EURUSD','GBPUSD','AUDUSD','NZDUSD','USDJPY','USDCHF','USDCAD')
ORDER BY symbol, candle_time DESC;
""")

rows = cur.fetchall()

usd_bullish_votes = 0
usd_bearish_votes = 0

for row in rows:
    symbol = row[0]
    trend = row[2]

    if symbol in ["EURUSD", "GBPUSD", "AUDUSD", "NZDUSD"]:
        if trend == "Bearish":
            usd_bullish_votes += 1
        elif trend == "Bullish":
            usd_bearish_votes += 1

    elif symbol in ["USDJPY", "USDCHF", "USDCAD"]:
        if trend == "Bullish":
            usd_bullish_votes += 1
        elif trend == "Bearish":
            usd_bearish_votes += 1

if usd_bullish_votes >= 5:
    dxy_trend = "DXY Proxy Bullish"
    dxy_score = 80
    dxy_interpretation = "USD is broadly strong across the major pairs."

elif usd_bearish_votes >= 5:
    dxy_trend = "DXY Proxy Bearish"
    dxy_score = 80
    dxy_interpretation = "USD is broadly weak across the major pairs."

else:
    dxy_trend = "DXY Proxy Mixed"
    dxy_score = 50
    dxy_interpretation = "USD strength is mixed across the major pairs."

print("USD Bullish Votes:", usd_bullish_votes)
print("USD Bearish Votes:", usd_bearish_votes)
print("DXY Proxy Trend:", dxy_trend)
print("DXY Proxy Score:", dxy_score)
print("Interpretation:", dxy_interpretation)

cur.execute("""
UPDATE flightdeck_signals
SET dxy_trend = %s,
    dxy_score = %s,
    dxy_interpretation = %s
WHERE candle_time = (
    SELECT MAX(candle_time)
    FROM flightdeck_signals
);
""", (
    dxy_trend,
    dxy_score,
    dxy_interpretation
))

conn.commit()

cur.close()
conn.close()

print("DXY proxy updated successfully.")