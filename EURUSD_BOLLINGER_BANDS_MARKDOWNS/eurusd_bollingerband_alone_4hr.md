# EURUSD H4 Bollinger Band Alone Research

## Test Configuration

* **Asset:** EURUSD
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Bands Alone
* **BB Period:** 20
* **BB Standard Deviations:** 2

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Lower Band Signals | 2,464 |
| Upper Band Signals | 2,810 |
| **Total Signals** | **5,274** |

---

# Lower Band Reversal Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 50.41% |
| 3 Candles | 49.15% |
| 6 Candles | 46.92% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0195% |
| 3 Candles | -0.0376% |
| 6 Candles | -0.0710% |

---

# Upper Band Reversal Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 49.57% |
| 3 Candles | 48.54% |
| 6 Candles | 50.18% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0135% |
| 3 Candles | 0.0217% |
| 6 Candles | 0.0447% |

---

# Key Findings

## Observation 1

Bollinger Bands generated a very large number of opportunities.

| Strategy | Signals |
|----------|---------:|
| RSI Alone | ~2,426 Oversold / ~2,387 Overbought |
| BB Alone | 2,464 Lower Band / 2,810 Upper Band |

Signal frequency is comparable to RSI Alone.

---

## Observation 2

The bullish side showed no meaningful edge.

Lower Band results:

* 50.41%
* 49.15%
* 46.92%

Performance deteriorated as holding periods increased.

---

## Observation 3

The bearish side also showed no meaningful edge.

Upper Band results:

* 49.57%
* 48.54%
* 50.18%

Results remained near random.

---

## Observation 4

Average returns were unfavorable.

Lower Band signals:

* Negative average return at every horizon.

Upper Band signals:

* Positive average return at every horizon.

This suggests EURUSD continued moving in the direction of the Bollinger Band break more often than it reversed.

---

# Comparison vs RSI Alone

## RSI Alone (EURUSD)

| Horizon | Bullish WR |
|----------|----------:|
| 1 Candle | 51.57% |
| 3 Candles | 51.61% |
| 6 Candles | 52.12% |

| Horizon | Bearish WR |
|----------|----------:|
| 1 Candle | 50.38% |
| 3 Candles | 51.15% |
| 6 Candles | 51.81% |

---

## Bollinger Bands Alone (EURUSD)

| Horizon | Bullish WR |
|----------|----------:|
| 1 Candle | 50.41% |
| 3 Candles | 49.15% |
| 6 Candles | 46.92% |

| Horizon | Bearish WR |
|----------|----------:|
| 1 Candle | 49.57% |
| 3 Candles | 48.54% |
| 6 Candles | 50.18% |

---

# Preliminary Conclusion

EURUSD Bollinger Band Alone appears weaker than EURUSD RSI Alone.

The evidence suggests:

* Bollinger Band breaches do not create a reliable mean-reversion signal on EURUSD.
* Volatility expansion alone may not be sufficient to predict reversals.
* Momentum exhaustion (RSI) appears more informative than volatility expansion on EURUSD.

---

# Research Verdict

**Status:** No Meaningful Edge

Current Leader:

* EURUSD RSI Alone

Current Loser:

* EURUSD Bollinger Band Alone

---

# Phase 2 Scoreboard

## Momentum vs Volatility

| Asset | Momentum (RSI) | Volatility (BB) | Leader |
|---------|----------:|----------:|---------|
| EURUSD | 52.12% | 50.18% | RSI |

---

# Research Takeaway

The first test of the Volatility vs Momentum project produced a clear result:

> On EURUSD, momentum exhaustion appears more informative than volatility expansion.

At least for the initial Bollinger Band framework, volatility alone failed to produce a meaningful mean-reversion edge despite generating more than 5,000 signals.