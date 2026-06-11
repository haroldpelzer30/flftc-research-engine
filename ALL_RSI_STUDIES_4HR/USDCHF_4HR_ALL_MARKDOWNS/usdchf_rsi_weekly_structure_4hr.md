# USDCHF H4 RSI + Weekly Structure Research

## Test Configuration

* **Asset:** USDCHF
* **Timeframe:** H4 (4-Hour)
* **Strategy:** RSI + Weekly Structure
* **RSI Period:** 14
* **Near Weekly Level Threshold:** 0.15%
* **Weekly Structure Source:** Derived from H4 Data

---

## Signal Count

| Signal Type       |   Count |
| ----------------- | ------: |
| Bullish Signals   |      74 |
| Bearish Signals   |      72 |
| **Total Signals** | **146** |

---

## Bullish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   47.30% |
| 3 Candles      |   44.59% |
| 6 Candles      |   48.65% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |       -0.0102% |
| 3 Candles      |       -0.0628% |
| 6 Candles      |       -0.0924% |

---

## Bearish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   50.00% |
| 3 Candles      |   54.17% |
| 6 Candles      |   55.56% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |        0.0027% |
| 3 Candles      |       -0.0917% |
| 6 Candles      |       -0.0791% |

---

# Comparison vs Previous USDCHF Tests

## RSI Alone

| Setup      | Best Result |
| ---------- | ----------: |
| Oversold   |      54.62% |
| Overbought |      57.00% |

**Total Signals:** 1,080

---

## RSI + Daily Structure

| Setup   | Best Result |
| ------- | ----------: |
| Bullish |      53.91% |
| Bearish |      53.19% |

**Total Signals:** 269

---

## RSI + Double Bottom / Double Top

| Setup                 | Best Result |
| --------------------- | ----------: |
| Bullish Double Bottom |      54.70% |
| Bearish Double Top    |      58.46% |

**Total Signals:** 506

---

## RSI + Inside Bar

| Setup              | Best Result |
| ------------------ | ----------: |
| Bullish Inside Bar |      54.13% |
| Bearish Inside Bar |      60.53% |

**Total Signals:** 185

---

## RSI + Weekly Structure

| Setup                    | Best Result |
| ------------------------ | ----------: |
| Bullish Weekly Structure |      48.65% |
| Bearish Weekly Structure |      55.56% |

**Total Signals:** 146

---

# Key Findings

### Observation 1

Weekly Structure produced the lowest trade count of all structure-based tests.

* Only 146 total signals
* Nearly 87% fewer signals than RSI Alone

### Observation 2

Bullish performance collapsed.

* 1 Candle: 47.30%
* 3 Candles: 44.59%
* 6 Candles: 48.65%

All bullish results were below 50%.

### Observation 3

Bearish performance remained modest but failed to exceed RSI Alone.

* RSI Alone Bearish: 57.00%
* Weekly Structure Bearish: 55.56%

### Observation 4

Weekly Structure reduced trade frequency substantially without improving predictive accuracy.

### Observation 5

Average returns remained weak and generally negative.

---

# Preliminary Conclusion

Weekly Structure does not appear to improve RSI reversals on USDCHF.

Unlike the original hypothesis, proximity to prior weekly highs and lows does not appear to provide additional predictive value.

The strongest edge remains associated with RSI extremes themselves rather than weekly location.

---

# Research Verdict

**Status:** Not Recommended

Current USDCHF Leaderboard:

| Strategy               | Best Win Rate |
| ---------------------- | ------------: |
| RSI + Inside Bar       |    **60.53%** |
| RSI + Double Top       |        58.46% |
| RSI Alone              |        57.00% |
| RSI + Weekly Structure |        55.56% |
| RSI + Daily Structure  |        53.91% |

---

# USDCHF Research Summary

The complete RSI research suite suggests:

* RSI Alone contains most of the edge.
* Daily Structure weakened performance.
* Weekly Structure weakened performance.
* Double Top / Double Bottom offered only modest improvement.
* Inside Bars produced the highest win rate but with a significantly smaller sample size.

The evidence currently favors simple RSI mean reversion over location-based structure filters on USDCHF.
