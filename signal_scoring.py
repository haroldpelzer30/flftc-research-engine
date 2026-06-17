# signal_scoring.py

SETUP_SCORES = {

    ("NAS100", "LONDON_BREAKOUT", "BULLISH"): 96,

    ("SP500", "NEWYORK_BREAKOUT", "BULLISH"): 94,

    ("SP500", "LONDON_BREAKOUT", "BULLISH"): 93,

    ("NAS100", "TWENTY_BAR_BREAKOUT", "BULLISH"): 91,

    ("NAS100", "DAILY_SWEEP", "BULLISH"): 92,

    ("XAUUSD", "RSI_OVERSOLD", "BULLISH"): 89,

    ("XAUUSD", "DAILY_SWEEP", "BULLISH"): 89,

    ("USDCHF", "RSI_OVERBOUGHT", "BEARISH"): 84,

    ("USDCHF", "RSI_OVERSOLD", "BULLISH"): 82,

    ("GBPUSD", "RSI_OVERBOUGHT", "BEARISH"): 80,
}


def get_signal_score(symbol, setup, direction):

    return SETUP_SCORES.get(
        (symbol, setup, direction),
        50
    )


def get_signal_tier(score):

    if score >= 95:
        return "HALL_OF_FAME"

    elif score >= 90:
        return "TIER_1"

    elif score >= 80:
        return "TIER_2"

    elif score >= 70:
        return "TIER_3"

    return "INFO"