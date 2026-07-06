from dotenv import load_dotenv
import os
import psycopg2
import MetaTrader5 as mt5
import pandas as pd

load_dotenv()

print("FlightDeck Pipeline Starting...")

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT"),
    sslmode="require"
)

cur = conn.cursor()
print("Postgres Connected Successfully")

if not mt5.initialize():
    print("MT5 Connection Failed")
    cur.close()
    conn.close()
    quit()

print("MT5 Connected Successfully")

symbols = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "USDCHF",
    "USDCAD",
    "AUDUSD",
    "NZDUSD",
    "XAUUSD",
    "XAGUSD",
    "SPXUSD",
    "NASUSD"
]

timeframe = mt5.TIMEFRAME_H4
rsi_period = 14

for symbol in symbols:

    print(f"\nChecking {symbol}...")

    candles = mt5.copy_rates_from_pos(symbol, timeframe, 0, 500)

    if candles is None or len(candles) == 0:
        print(f"No candle data found for {symbol}")
        continue

    df = pd.DataFrame(candles)
    df["time"] = pd.to_datetime(df["time"], unit="s")

    df["ema20"] = df["close"].ewm(span=20, adjust=False).mean()
    df["ema50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema200"] = df["close"].ewm(span=200, adjust=False).mean()

    # Wilder RSI - closer to MT5 RSI calculation
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / rsi_period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / rsi_period, adjust=False).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    latest = df.iloc[-1]

    if latest["rsi"] <= 30:
        signal = "RSI Oversold"
    elif latest["rsi"] >= 70:
        signal = "RSI Overbought"
    else:
        signal = "No RSI signal"

    signal_record = {
        "symbol": symbol,
        "time": str(latest["time"]),
        "close": float(latest["close"]),
        "ema20": float(latest["ema20"]),
        "ema50": float(latest["ema50"]),
        "ema200": float(latest["ema200"]),
        "rsi": float(latest["rsi"]),
        "signal": signal
    }

    print(signal_record)

    cur.execute("""
        INSERT INTO flightdeck_signals (
            symbol,
            candle_time,
            close_price,
            ema20,
            ema50,
            ema200,
            rsi,
            signal
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (symbol, candle_time)
        DO UPDATE SET
            close_price = EXCLUDED.close_price,
            ema20 = EXCLUDED.ema20,
            ema50 = EXCLUDED.ema50,
            ema200 = EXCLUDED.ema200,
            rsi = EXCLUDED.rsi,
            signal = EXCLUDED.signal;
    """, (
        signal_record["symbol"],
        signal_record["time"],
        signal_record["close"],
        signal_record["ema20"],
        signal_record["ema50"],
        signal_record["ema200"],
        signal_record["rsi"],
        signal_record["signal"]
    ))

    print("Saved to Postgres")

conn.commit()

mt5.shutdown()
cur.close()
conn.close()

print("\nFlightDeck Pipeline Complete.")