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

        context = (
            "Countertrend bullish reversal attempt"
            if close < ema200
            else "Bullish reversal with larger trend support"
        )

        if close >= ema200:
            score += 10

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

        context = (
            "Countertrend bearish reversal attempt"
            if close > ema200
            else "Bearish reversal with larger trend support"
        )

        if close <= ema200:
            score += 10

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

signals_saved = 0

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

    if tier == "Ignore":
        print(f"{symbol}: Ignored")
        continue

    cursor.execute("""
        INSERT INTO market_signals (
            symbol,
            timeframe,
            candle_time,
            setup,
            direction,
            score,
            tier,
            current_price,
            rsi,
            ema20,
            ema50,
            ema200,
            trend_state,
            context
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        symbol,
        timeframe,
        candle_time,
        setup,
        direction,
        score,
        tier,
        close,
        rsi,
        ema20,
        ema50,
        ema200,
        trend_state,
        context
    ))

    signals_saved += 1

    print(f"{symbol}: Saved {tier} | {direction} | Score {score}")

conn.commit()

cursor.close()
conn.close()

print()
print("=" * 60)
print(f"Signals saved: {signals_saved}")
print("=" * 60)