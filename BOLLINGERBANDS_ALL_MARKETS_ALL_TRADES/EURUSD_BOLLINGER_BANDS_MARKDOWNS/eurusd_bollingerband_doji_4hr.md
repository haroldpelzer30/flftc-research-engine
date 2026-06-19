# EURUSD H4 Bollinger Band + Doji Research

## Test Configuration

* **Asset:** EURUSD
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Band + Doji
* **BB Period:** 20
* **BB Standard Deviations:** 2
* **Doji Threshold:** 10% of Candle Range

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Doji Signals | 260 |
| Bearish Doji Signals | 244 |
| **Total Signals** | **504** |

---

# Bullish Doji Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 48.08% |
| 3 Candles | 45.00% |
| 6 Candles | 36.92% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0399% |
| 3 Candles | -0.1088% |
| 6 Candles | -0.2941% |

---

# Bearish Doji Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 43.44% |
| 3 Candles | 42.62% |
| 6 Candles | 45.49% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0671% |
| 3 Candles | 0.1567% |
| 6 Candles | 0.3713% |

---

# Comparison vs Previous BB Studies

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB Alone | 5,274 | 50.18% |
| BB + Double Bottom/Top | 2,453 | 52.78% |
| BB + Daily Structure | 794 | 56.87% |
| BB + Inside Bar | 556 | 56.20% |
| BB + Doji | 504 | 48.08% |

---

# Key Findings

## Observation 1

Doji was the worst Bollinger Band filter tested.

Despite reducing signals significantly, performance deteriorated substantially.

---

## Observation 2

Bullish performance collapsed as holding periods increased.

Bullish Side:

* 48.08%
* 45.00%
* 36.92%

This is not a mean-reversion edge.

This is worse than randomness.

---

## Observation 3

Bearish performance was equally poor.

Bearish Side:

* 43.44%
* 42.62%
* 45.49%

The bearish side failed at every horizon.

---

## Observation 4

Average returns strongly contradict the reversal hypothesis.

Bullish Doji Signals:

* Negative returns at every horizon
* Losses increased with holding period

Bearish Doji Signals:

* Positive returns at every horizon
* Gains increased with holding period

This suggests price frequently continued in the direction of the Bollinger Band breakout rather than reversing.

---

# Phase 2 Scoreboard

## EURUSD

| Strategy | Best Result |
|----------|----------:|
| BB + Daily Structure | 56.87% |
| BB + Inside Bar | 56.20% |
| BB + Double Bottom/Top | 52.78% |
| BB Alone | 50.18% |
| BB + Doji | 48.08% |

---

# Preliminary Conclusion

The Doji filter failed to improve Bollinger Band signals on EURUSD.

Instead of creating higher-quality reversals, Doji signals produced significantly worse performance than Bollinger Bands alone.

---

# Research Takeaway

The hypothesis was:

> Volatility Expansion + Indecision = Reversal

The evidence suggests the opposite.

On EURUSD, Doji candles occurring at Bollinger Band extremes did not signal reversal behavior and often preceded continued movement in the original direction.

Doji currently ranks as the weakest Bollinger Band filter tested on EURUSD.