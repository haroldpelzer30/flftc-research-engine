import os
import psycopg2
import pandas as pd
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

# Add indicator columns if they do not exist
cursor.execute("""
ALTER TABLE market_candles
ADD COLUMN IF NOT EXISTS rsi NUMERIC,
ADD COLUMN IF NOT EXISTS ema20 NUMERIC,
ADD COLUMN IF NOT EXISTS ema50 NUMERIC,
ADD COLUMN IF NOT EXISTS ema200 NUMERIC,
ADD COLUMN IF NOT EXISTS trend_state VARCHAR(20);
""")

conn.commit()

symbols = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "NZDUSD", "USDCAD",
    "XAUUSD", "XAGUSD", "NASUSD", "SPXUSD"
]

for symbol in symbols:
    print(f"Updating indicators for {symbol}...")

    df = pd.read_sql_query(
        """
        SELECT id, candle_time, close
        FROM market_candles
        WHERE symbol = %s AND timeframe = 'H4'
        ORDER BY candle_time ASC;
        """,
        conn,
        params=(symbol,)
    )

    if df.empty:
        print(f"No data for {symbol}")
        continue

    df["ema20"] = df["close"].ewm(span=20, adjust=False).mean()
    df["ema50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema200"] = df["close"].ewm(span=200, adjust=False).mean()

    delta = df["close"].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss
    df["rsi"] = 100 - (100 / (1 + rs))

    df["trend_state"] = df.apply(
        lambda row: "BULLISH" if row["close"] > row["ema200"] else "BEARISH",
        axis=1
    )

    for _, row in df.iterrows():
        cursor.execute(
            """
            UPDATE market_candles
            SET rsi = %s,
                ema20 = %s,
                ema50 = %s,
                ema200 = %s,
                trend_state = %s
            WHERE id = %s;
            """,
            (
                None if pd.isna(row["rsi"]) else float(row["rsi"]),
                float(row["ema20"]),
                float(row["ema50"]),
                float(row["ema200"]),
                row["trend_state"],
                int(row["id"])
            )
        )

    conn.commit()

cursor.close()
conn.close()

print("Indicator update complete.")