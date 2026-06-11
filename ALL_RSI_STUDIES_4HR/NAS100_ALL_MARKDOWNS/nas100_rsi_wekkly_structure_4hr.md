# NAS100 H4 RSI + Weekly Structure Research

## Test Configuration

* **Asset:** NAS100
* **Timeframe:** H4 (4-Hour)
* **Strategy:** RSI + Weekly Structure
* **RSI Period:** 14
* **Near Weekly Level Threshold:** 0.15%
* **Weekly Structure Source:** Derived from H4 Data

---

## Signal Count

| Signal Type | Count |
|------------|------:|
| Bullish Signals | 12 |
| Bearish Signals | 40 |
| **Total Signals** | **52** |

---

## Bullish Results

### Win Rates

| Forward Period | Win Rate |
|--------------|---------:|
| 1 Candle | 50.00% |
| 3 Candles | 33.33% |
| 6 Candles | 66.67% |

### Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.1295% |
| 3 Candles | -0.4426% |
| 6 Candles | 0.0363% |

---

## Bearish Results

### Win Rates

| Forward Period | Win Rate |
|--------------|---------:|
| 1 Candle | 45.00% |
| 3 Candles | 50.00% |
| 6 Candles | 55.00% |

### Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0243% |
| 3 Candles | 0.0100% |
| 6 Candles | -0.0673% |

---

# Comparison vs Previous NAS100 Tests

## RSI Alone

| Setup | Best Result |
|--------|-----------:|
| Oversold | 56.57% |
| Overbought | 43.89% |

**Total Signals:** 617

---

## RSI + Daily Structure

| Setup | Best Result |
|--------|-----------:|
| Bullish | 55.00% |
| Bearish | 49.02% |

**Total Signals:** 122

---

## RSI + Double Bottom / Double Top

| Setup | Best Result |
|--------|-----------:|
| Bullish Double Bottom | 62.50% |
| Bearish Double Top | 48.65% |

**Total Signals:** 217

---

## RSI + Inside Bar

| Setup | Best Result |
|--------|-----------:|
| Bullish Inside Bar | 62.96% |
| Bearish Inside Bar | 41.33% |

**Total Signals:** 102

---

## RSI + Weekly Structure

| Setup | Best Result |
|--------|-----------:|
| Bullish Weekly Structure | 66.67% |
| Bearish Weekly Structure | 55.00% |

**Total Signals:** 52

---

# Key Findings

### Observation 1

Weekly Structure produced the smallest sample size of any NAS100 test.

* Only 12 bullish signals
* Only 40 bearish signals
* Only 52 total signals

### Observation 2

The bullish win rate appears extremely strong.

* 6-Candle Bullish Result: 66.67%

However, this result is based on only 12 observations.

### Observation 3

Bearish performance improved relative to previous NAS100 tests.

* 6-Candle Bearish Result: 55.00%

However, the sample remains extremely small.

### Observation 4

Average returns remain inconsistent.

The combination of:

* Tiny sample size
* Volatile average returns

makes statistical confidence very limited.

### Observation 5

Weekly Structure dramatically reduced opportunity count.

* RSI Alone: 617 signals
* Weekly Structure: 52 signals

A reduction of more than 90%.

---

# Preliminary Conclusion

Weekly Structure produced the highest win rates observed so far on NAS100.

However:

* Sample size is extremely small.
* Confidence is limited.
* Results may be heavily influenced by randomness.

The dramatic reduction in opportunities makes practical deployment difficult without additional historical data.

---

# Research Verdict

**Status:** Interesting but Statistically Fragile

Current NAS100 Leaderboard:

| Strategy | Best Win Rate |
|----------|-------------:|
| RSI + Weekly Structure | **66.67%** |
| RSI + Inside Bar | 62.96% |
| RSI + Double Bottom | 62.50% |
| RSI Alone | 56.57% |
| RSI + Daily Structure | 55.00% |

---

# Important Statistical Note

The strongest NAS100 result currently comes from only:

* 12 bullish signals

This is far below the sample sizes generally required for strong statistical confidence.

The result is directionally interesting but should not be treated as robust evidence of a tradable edge without additional data.

---

# Research Takeaway

Weekly Structure improved headline win rates but at the cost of almost all opportunities.

This result reinforces a recurring theme of the project:

> Higher selectivity does not automatically create a better strategy.

A filter can produce impressive win rates while simultaneously making the strategy statistically fragile and difficult to scale.

The practical value of a strategy depends on both:

* Edge strength
* Opportunity frequency

and not win rate alone.