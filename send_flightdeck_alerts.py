from dotenv import load_dotenv
import os
import psycopg2
import requests

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

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
    symbol,
    candle_time,
    close_price,
    rsi,
    signal,
    trend,
    historical_win_rate,
    research_score,
    daily_structure,
    daily_structure_score,
    dxy_trend,
    dxy_score,
    final_score,
    tier
FROM flightdeck_signals
WHERE candle_time = (
    SELECT MAX(candle_time)
    FROM flightdeck_signals
)
AND tier IN ('Hall of Fame', 'Tier 1', 'Tier 2')
ORDER BY final_score DESC;
""")

rows = cur.fetchall()

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

if not rows:
    message = "FlightDeck scan complete. No Hall of Fame, Tier 1, Tier 2 signals on the latest candle."

    response = requests.post(url, data={
        "chat_id": chat_id,
        "text": message
    })

    print(response.status_code)
    print(response.text)

else:
    for row in rows:
        (
            symbol,
            candle_time,
            close_price,
            rsi,
            signal,
            trend,
            historical_win_rate,
            research_score,
            daily_structure,
            daily_structure_score,
            dxy_trend,
            dxy_score,
            final_score,
            tier
        ) = row

        message = f"""
🚨 FLIGHTDECK ALERT

Asset: {symbol}
Candle Time: {candle_time}
Price: {close_price}

Signal: {signal}
RSI: {round(rsi, 2)}
Trend: {trend}
Structure: {daily_structure}

Historical Win Rate: {historical_win_rate}%
Research Score: {research_score}
Structure Score: {daily_structure_score}

DXY Context: {dxy_trend}
DXY Score: {dxy_score}

Final Score: {final_score}
Tier: {tier}
"""

        response = requests.post(url, data={
            "chat_id": chat_id,
            "text": message
        })

        print(symbol, response.status_code)

cur.close()
conn.close()

print("FlightDeck alerts sent.")