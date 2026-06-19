import os
import logging
import azure.functions as func
import psycopg

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

        conn = psycopg.connect(
            host=os.getenv("POSTGRES_HOST"),
            dbname=os.getenv("POSTGRES_DB"),
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
            LIMIT 20
        """)

        signals = cursor.fetchall()

        logging.info("Signals found: %s", len(signals))

        for row in signals:

            logging.info(
                """
==================================================
Symbol: %s
Timeframe: %s
Candle Time: %s
Setup: %s
Direction: %s
Score: %s
Tier: %s
Price: %s
RSI: %s
Trend: %s
Context: %s
Created: %s
==================================================
                """,
                row[0],   # symbol
                row[1],   # timeframe
                row[2],   # candle_time
                row[3],   # setup
                row[4],   # direction
                row[5],   # score
                row[6],   # tier
                row[7],   # current_price
                row[8],   # rsi
                row[9],   # trend_state
                row[10],  # context
                row[11]   # created_at
            )

        cursor.close()
        conn.close()

        logging.info("========================================")
        logging.info("FLIGHTDECK H4 SCANNER COMPLETE")
        logging.info("========================================")

    except Exception as e:

        logging.exception(
            "FLIGHTDECK H4 SCANNER FAILED: %s",
            str(e)
        )

        raise