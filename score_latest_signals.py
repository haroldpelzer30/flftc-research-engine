import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "NZDUSD", "USDCAD",
    "XAUUSD", "XAGUSD", "NASUSD", "SPXUSD"
]


def get_signal_tier(score):
    if score >= 90:
        return "Hall of Fame"
    elif score >= 75:
        return "Tier 1"
    elif score >= 60:
        return "Tier 2"
    elif score >= 40:
        return "Tier 3"
    else:
        return "Ignore"


def get_signal_score(close, rsi, ema20, ema50, ema200, trend_state):
    score = 0
    direction = "NEUTRAL"
    setup = "No Setup"
    context = "No active setup"

    if rsi is None:
        return score, direction, setup, "Ignore", context

    rsi = float(rsi)
    close = float(close)
    ema20 = float(ema20)
    ema50 = float(ema50)
    ema200 = float(ema200)

    # Bullish mean reversion setup
    if rsi <= 30:
        direction = "BULLISH"
        setup = "RSI Oversold Mean Reversion"
        score = 55

        if rsi <= 25:
            score += 15

        if rsi <= 20:
            score += 20

        if close < ema20:
            score += 10

        if close < ema50:
            score += 5

        if close < ema200:
            context = "Countertrend bullish reversal attempt"
        else:
            score += 10
            context = "Bullish reversal with larger trend support"

    # Bearish mean reversion setup
    elif rsi >= 70:
        direction = "BEARISH"
        setup = "RSI Overbought Mean Reversion"
        score = 55

        if rsi >= 75:
            score += 15

        if rsi >= 80:
            score += 20

        if close > ema20:
            score += 10

        if close > ema50:
            score += 5

        if close > ema200:
            context = "Countertrend bearish reversal attempt"
        else:
            score += 10
            context = "Bearish reversal with larger trend support"

    tier = get_signal_tier(score)

    return score, direction, setup, tier, context


conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT", "5432"),
    sslmode="require"
)

cursor = conn.cursor()

print("\nLATEST SIGNAL SCORES")
print("=" * 90)

for symbol in SYMBOLS:
    cursor.execute("""
        SELECT
            symbol,
            timeframe,
            candle_time,
            close,
            rsi,
            ema20,
            ema50,
            ema200,
            trend_state
        FROM market_candles
        WHERE symbol = %s AND timeframe = 'H4'
        ORDER BY candle_time DESC
        LIMIT 1;
    """, (symbol,))

    row = cursor.fetchone()

    if not row:
        print(f"{symbol}: No data found")
        continue

    symbol, timeframe, candle_time, close, rsi, ema20, ema50, ema200, trend_state = row

    score, direction, setup, tier, context = get_signal_score(
        close, rsi, ema20, ema50, ema200, trend_state
    )

    print(f"\n{symbol} | {timeframe} | {candle_time}")
    print(f"Close: {close} | RSI: {rsi} | Trend: {trend_state}")
    print(f"Setup: {setup}")
    print(f"Direction: {direction}")
    print(f"Score: {score}")
    print(f"Tier: {tier}")
    print(f"Context: {context}")

cursor.close()
conn.close()

print("\nSignal scoring complete.")