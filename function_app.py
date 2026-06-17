import os
import logging
import azure.functions as func
import psycopg2

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 0 */4 * * *",
    arg_name="mytimer",
    run_on_startup=False,
    use_monitor=True
)
def flightdeck_h4_scanner(mytimer: func.TimerRequest) -> None:
    logging.info("========================================")
    logging.info("FLIGHTDECK H4 SCANNER STARTED")
    logging.info("========================================")

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
            logging.info("Signals found: %s", len(signals))

            for row in signals:
                logging.info(
                    "SIGNAL | %s | %s | Candle: %s | Setup: %s | "
                    "Direction: %s | Score: %s | Tier: %s | "
                    "Price: %s | RSI: %s | Trend: %s | Context: %s",
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                )

        cursor.close()
        conn.close()

        logging.info("========================================")
        logging.info("FLIGHTDECK H4 SCANNER COMPLETED SUCCESSFULLY")
        logging.info("========================================")

    except Exception as e:
        logging.exception("FLIGHTDECK H4 SCANNER FAILED: %s", e)
        raise