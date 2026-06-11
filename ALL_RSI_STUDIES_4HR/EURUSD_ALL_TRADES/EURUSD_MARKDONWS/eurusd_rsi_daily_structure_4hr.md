# EURUSD H4 RSI + Daily Structure Research

## Test Configuration

* **Asset:** EURUSD
* **Timeframe:** H4 (4-Hour)
* **Strategy:** RSI + Daily Structure
* **RSI Period:** 14
* **Near Daily Level Threshold:** 0.10%
* **Daily Structure Source:** Derived from H4 Data

---

## Signal Count

| Signal Type       |     Count |
| ----------------- | --------: |
| Bullish Signals   |       576 |
| Bearish Signals   |       575 |
| **Total Signals** | **1,151** |

---

## Bullish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   51.56% |
| 3 Candles      |   56.25% |
| 6 Candles      |   54.69% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |        0.0167% |
| 3 Candles      |        0.0240% |
| 6 Candles      |        0.0010% |

---

## Bearish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   53.74% |
| 3 Candles      |   52.35% |
| 6 Candles      |   50.78% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |       -0.0011% |
| 3 Candles      |        0.0276% |
| 6 Candles      |        0.0403% |

---

# Comparison vs RSI Alone

## RSI Alone Baseline

| Setup      | Best Result |
| ---------- | ----------: |
| Oversold   |      50.12% |
| Overbought |      50.84% |

Signal Count:

* Oversold: 2,426
* Overbought: 2,323
* Total: 4,749

---

## RSI + Daily Structure

| Setup   | Best Result |
| ------- | ----------: |
| Bullish |      56.25% |
| Bearish |      53.74% |

Signal Count:

* Total: 1,151

---

# Signal Reduction

| Test                  | Signals |
| --------------------- | ------: |
| RSI Alone             |   4,749 |
| RSI + Daily Structure |   1,151 |

Reduction:

* Signals decreased by approximately **76%**
* Trade frequency dropped significantly

---

# Key Findings

### Observation 1

Unlike RSI Alone, Daily Structure appears to create a measurable edge on EURUSD.

### Observation 2

Bullish performance improved substantially:

* RSI Alone Best Bullish Result: 50.12%
* Daily Structure Best Bullish Result: 56.25%

### Observation 3

Bearish performance also improved:

* RSI Alone Best Bearish Result: 50.84%
* Daily Structure Best Bearish Result: 53.74%

### Observation 4

The strongest result occurred on the bullish side:

* RSI Oversold
* Near Previous Daily Low
* 3-Candle Holding Period
* **56.25% Win Rate**

### Observation 5

This is one of the first signs that EURUSD may respond to location-based context even though RSI Alone showed almost no edge.

---

# Preliminary Conclusion

This test produced a surprising result.

While EURUSD RSI Alone behaved almost perfectly randomly, combining RSI with Daily Structure generated a meaningful improvement in both bullish and bearish performance.

This suggests:

* RSI Alone may not contain sufficient information.
* Location may matter more than momentum exhaustion on EURUSD.
* Previous Daily Highs and Lows may provide important context for mean-reversion behavior.

---

# Research Verdict

**Status:** Promising

Current EURUSD Leaderboard:

| Strategy              | Best Win Rate |
| --------------------- | ------------: |
| RSI + Daily Structure |    **56.25%** |
| RSI Alone             |        50.84% |

This is the first EURUSD result to demonstrate a potentially meaningful edge and establishes Daily Structure as the current leader for EURUSD research.

---

# Key Insight

This result challenges one of the early assumptions from the project:

> RSI Alone may not contain the edge, but RSI combined with meaningful market location can reveal an edge that was previously hidden.

EURUSD now becomes an important test case for determining whether market structure can create value where a standalone indicator cannot.
