# EURUSD H4 Bollinger Band + Daily Structure Research

## Test Configuration

* **Asset:** EURUSD
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Band + Daily Structure
* **BB Period:** 20
* **BB Standard Deviations:** 2
* **Daily Structure Threshold:** 0.10%

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 371 |
| Bearish Signals | 423 |
| **Total Signals** | **794** |

---

# Bullish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 56.87% |
| 3 Candles | 52.29% |
| 6 Candles | 50.40% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0119% |
| 3 Candles | 0.0023% |
| 6 Candles | -0.0104% |

---

# Bearish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 53.66% |
| 3 Candles | 52.96% |
| 6 Candles | 52.01% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0151% |
| 3 Candles | -0.0143% |
| 6 Candles | -0.0060% |

---

# Comparison vs BB Alone

## BB Alone

| Horizon | Bullish WR | Bearish WR |
|----------|----------:|----------:|
| 1 Candle | 50.41% | 49.57% |
| 3 Candles | 49.15% | 48.54% |
| 6 Candles | 46.92% | 50.18% |

Signals:

* Lower Band: 2,464
* Upper Band: 2,810

Total: 5,274

---

## BB + Daily Structure

| Horizon | Bullish WR | Bearish WR |
|----------|----------:|----------:|
| 1 Candle | 56.87% | 53.66% |
| 3 Candles | 52.29% | 52.96% |
| 6 Candles | 50.40% | 52.01% |

Signals:

* Bullish: 371
* Bearish: 423

Total: 794

---

# Key Findings

## Observation 1

Daily Structure dramatically improved Bollinger Band performance.

BB Alone:

* Mostly random
* 47–50% win rates

BB + Daily Structure:

* 50–57% win rates
* Meaningful improvement on both sides

---

## Observation 2

Daily Structure removed approximately 85% of opportunities.

| Test | Signals |
|---------|---------:|
| BB Alone | 5,274 |
| BB + Daily Structure | 794 |

Opportunity reduction:

**~84.9%**

---

## Observation 3

The strongest result occurred immediately after the signal.

Bullish:

* 56.87% after 1 candle

Bearish:

* 53.66% after 1 candle

The edge weakened as holding periods increased.

---

## Observation 4

Unlike RSI + Daily Structure, the improvement appears front-loaded.

Most of the benefit occurred within:

* 1 candle
* 3 candles

By 6 candles the edge was largely gone.

---

# Comparison vs RSI + Daily Structure

## RSI + Daily Structure

Signals:

* Bullish: 576
* Bearish: 575

Best Results:

* Bullish 3 Candles: 56.25%
* Bearish 1 Candle: 53.74%

---

## BB + Daily Structure

Signals:

* Bullish: 371
* Bearish: 423

Best Results:

* Bullish 1 Candle: 56.87%
* Bearish 1 Candle: 53.66%

---

# Phase 2 Scoreboard

## Momentum vs Volatility

| Asset | Momentum (RSI) | Volatility (BB) | Current Leader |
|---------|----------:|----------:|---------|
| EURUSD Alone | 52.12% | 50.18% | RSI |
| EURUSD + Daily Structure | 56.25% | 56.87% | BB (1 Candle) |

---

# Preliminary Conclusion

Daily Structure appears to help Bollinger Bands significantly.

The evidence suggests:

* Bollinger Bands alone contain little predictive information.
* Location dramatically improves Bollinger Band signals.
* Volatility expansion near an important level may be more meaningful than volatility expansion alone.

---

# Research Takeaway

The first major lesson of the Bollinger Band chapter is:

> Volatility expansion by itself appears weak on EURUSD.

However:

> Volatility expansion occurring near a meaningful location may contain useful predictive information.

This is the first indication that location may rescue an otherwise weak volatility signal.