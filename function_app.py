# function_app.py

import azure.functions as func
import datetime
import logging
import json
from typing import List, Dict, Any

from signal_scoring import get_signal_score, get_signal_tier


app = func.FunctionApp()


MARKETS = [
    "EURUSD",
    "GBPUSD",
    "USDCHF",
    "AUDUSD",
    "NZDUSD",
    "USDCAD",
    "USDJPY",
    "XAUUSD",
    "XAGUSD",
    "SP500",
    "NAS100",
    "DXY",
]


def build_market_snapshot(symbol: str, scan_time: datetime.datetime) -> Dict[str, Any]:
    return {
        "scan_time": scan_time.isoformat(),
        "symbol": symbol,
        "timeframe": "H4",
        "open": None,
        "high": None,
        "low": None,
        "close": None,
        "volume": None,
        "rsi": None,
        "ema20": None,
        "ema50": None,
        "ema200": None,
        "above_ema200": None,
        "trend_state": "UNKNOWN",
    }


def detect_signals(symbol: str, snapshot: Dict[str, Any]) -> List[Dict[str, Any]]:
    signals = []

    if symbol == "NAS100":
        signals.append({
            "symbol": symbol,
            "setup": "LONDON_BREAKOUT",
            "direction": "BULLISH",
            "timeframe": "H4",
            "price": snapshot.get("close"),
        })

    if symbol == "USDCHF":
        signals.append({
            "symbol": symbol,
            "setup": "RSI_OVERBOUGHT",
            "direction": "BEARISH",
            "timeframe": "H4",
            "price": snapshot.get("close"),
        })

    return signals


def add_intelligence_to_signal(signal: Dict[str, Any]) -> Dict[str, Any]:
    score = get_signal_score(
        signal["symbol"],
        signal["setup"],
        signal["direction"],
    )

    tier = get_signal_tier(score)

    signal["score"] = score
    signal["tier"] = tier
    signal["dxy_price"] = None
    signal["dxy_trend"] = "UNKNOWN"
    signal["dxy_score"] = 0
    signal["interpretation"] = "DXY context pending."

    return signal


def save_snapshot(snapshot: Dict[str, Any]) -> None:
    logging.info("SNAPSHOT: %s", json.dumps(snapshot))


def save_signal(signal: Dict[str, Any]) -> None:
    logging.info("SIGNAL: %s", json.dumps(signal))


def send_alert(signal: Dict[str, Any]) -> bool:
    if signal["tier"] in ["HALL_OF_FAME", "TIER_1", "TIER_2"]:
        logging.info(
            "ALERT SENT: %s %s %s Score=%s Tier=%s",
            signal["symbol"],
            signal["setup"],
            signal["direction"],
            signal["score"],
            signal["tier"],
        )
        return True

    return False


@app.timer_trigger(
    schedule="0 0 */4 * * *",
    arg_name="mytimer",
    run_on_startup=False,
    use_monitor=True,
)
def flightdeck_h4_scanner(mytimer: func.TimerRequest) -> None:
    scan_time = datetime.datetime.now(datetime.timezone.utc)

    logging.info("========================================")
    logging.info("FLIGHTDECK H4 MARKET SCAN STARTED")
    logging.info("Scan Time UTC: %s", scan_time.isoformat())
    logging.info("========================================")

    snapshots_saved = 0
    signals_detected = 0
    alerts_sent = 0

    for symbol in MARKETS:
        try:
            snapshot = build_market_snapshot(symbol, scan_time)
            save_snapshot(snapshot)
            snapshots_saved += 1

            raw_signals = detect_signals(symbol, snapshot)

            for raw_signal in raw_signals:
                enriched_signal = add_intelligence_to_signal(raw_signal)
                save_signal(enriched_signal)
                signals_detected += 1

                if send_alert(enriched_signal):
                    alerts_sent += 1

        except Exception as error:
            logging.exception("Error scanning %s: %s", symbol, error)

    logging.info("========================================")
    logging.info("FLIGHTDECK H4 MARKET SCAN COMPLETE")
    logging.info("Markets Scanned: %s", len(MARKETS))
    logging.info("Snapshots Saved: %s", snapshots_saved)
    logging.info("Signals Detected: %s", signals_detected)
    logging.info("Alerts Sent: %s", alerts_sent)
    logging.info("========================================")