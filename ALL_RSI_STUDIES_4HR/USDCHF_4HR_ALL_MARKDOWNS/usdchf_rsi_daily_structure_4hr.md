# USDCHF H4 RSI + Daily Structure Research

## Test Configuration

* **Asset:** USDCHF
* **Timeframe:** H4 (4-Hour)
* **Strategy:** RSI + Daily Structure
* **RSI Period:** 14
* **Near Daily Level Threshold:** 0.10%
* **Daily Structure Source:** Derived from H4 Data

---

## Signal Count

| Signal Type       |   Count |
| ----------------- | ------: |
| Bullish Signals   |     128 |
| Bearish Signals   |     141 |
| **Total Signals** | **269** |

---

## Bullish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   49.22% |
| 3 Candles      |   53.91% |
| 6 Candles      |   53.12% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |       -0.0158% |
| 3 Candles      |       -0.0090% |
| 6 Candles      |       -0.0512% |

---

## Bearish Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   53.19% |
| 3 Candles      |   53.19% |
| 6 Candles      |   53.19% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |        0.0022% |
| 3 Candles      |       -0.0398% |
| 6 Candles      |       -0.0954% |

---

# Comparison vs RSI Alone

## RSI Alone Baseline

| Setup      | Best Result |
| ---------- | ----------: |
| Oversold   |      54.62% |
| Overbought |      57.00% |

## RSI + Daily Structure

| Setup   | Best Result |
| ------- | ----------: |
| Bullish |      53.91% |
| Bearish |      53.19% |

---

# Signal Reduction

| Test                  | Signals |
| --------------------- | ------: |
| RSI Alone             |   1,080 |
| RSI + Daily Structure |     269 |

Reduction:

* Signals decreased by approximately **75%**
* Trade frequency dropped significantly

---

# Key Findings

### Observation 1

Daily Structure dramatically reduced signal count:

* From 1,080 signals
* Down to 269 signals

### Observation 2

The bullish side remained relatively stable:

* RSI Alone Best: 54.62%
* Daily Structure Best: 53.91%

### Observation 3

The bearish side deteriorated:

* RSI Alone Best: 57.00%
* Daily Structure Best: 53.19%

### Observation 4

Daily Structure did not improve win rates despite significantly reducing trade frequency.

### Observation 5

Average returns remained weak and generally negative.

---

# Preliminary Conclusion

Daily Structure does not appear to enhance the RSI edge on USDCHF.

While the filter successfully reduced the number of trades, it failed to improve win rates and weakened the strongest portion of the strategy (bearish reversals).

---

# Research Verdict

**Status:** Not Recommended

Current evidence suggests that Daily Structure is not adding meaningful predictive value to RSI signals on USDCHF.

Recommended next tests:

1. RSI + Double Bottom / Double Top
2. RSI + Inside Bar
3. RSI + Weekly Structure

The most promising path remains identifying filters that can improve upon the 57.00% bearish baseline established by RSI Alone.
