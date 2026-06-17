import os
import logging
import azure.functions as func
import psycopg2

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 0 */4 * * *",
    arg_name="mytimer",
    run_on_startup=True,
    use_monitor=True
)
def flightdeck_h4_scanner(mytimer: func.TimerRequest) -> None:
    logging.info("FLIGHTDECK H4 SCANNER STARTED")

    try:
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
            ORDER BY created_at DESC
            LIMIT 10;
        """)

        signals = cursor.fetchall()

        if not signals:
            logging.info("No signals found in market_signals table.")
        else:
            logging.info(f"Signals found: {len(signals)}")

            for row in signals:
                logging.info(
                    f"SIGNAL | {row[0]} | {row[1]} | Candle: {row[2]} | "
                    f"Setup: {row[3]} | Direction: {row[4]} | "
                    f"Score: {row[5]} | Tier: {row[6]} | "
                    f"Price: {row[7]} | RSI: {row[8]} | "
                    f"Trend: {row[9]} | Context: {row[10]}"
                )

        cursor.close()
        conn.close()

        logging.info("FLIGHTDECK H4 SCANNER COMPLETED SUCCESSFULLY")

    except Exception as e:
        logging.error(f"FLIGHTDECK H4 SCANNER FAILED: {e}")
        raise