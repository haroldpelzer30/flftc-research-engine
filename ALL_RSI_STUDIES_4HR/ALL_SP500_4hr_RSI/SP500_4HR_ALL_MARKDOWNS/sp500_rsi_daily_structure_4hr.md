# SP500 H4 RSI + Daily Structure Research

## Test Conditions

* Market: SP500
* Execution Timeframe: H4
* Structure Timeframe: Daily
* RSI Period: 14
* Near Daily Level Threshold: 0.10%

---

# Signal Statistics

### Bullish Signals

* Total Bullish Signals: 16

### Bearish Signals

* Total Bearish Signals: 118

### Total Signals

* 134

---

# Bullish Results

| Forward Window | Win Rate |
| -------------- | -------- |
| 1 Candle       | 50.00%   |
| 3 Candles      | 43.75%   |
| 6 Candles      | 50.00%   |

### Average Returns

| Horizon   | Avg Return |
| --------- | ---------- |
| 1 Candle  | 0.0626%    |
| 3 Candles | -0.1750%   |
| 6 Candles | -0.6652%   |

---

# Bearish Results

| Forward Window | Win Rate |
| -------------- | -------- |
| 1 Candle       | 53.39%   |
| 3 Candles      | 50.00%   |
| 6 Candles      | 50.00%   |

### Average Returns

| Horizon   | Avg Return |
| --------- | ---------- |
| 1 Candle  | -0.0097%   |
| 3 Candles | 0.0428%    |
| 6 Candles | 0.0408%    |

---

# Comparison to SP500 RSI Alone

| Strategy              | Bullish Signals | Bearish Signals | Best Win Rate |
| --------------------- | --------------: | --------------: | ------------: |
| RSI Alone             |             147 |             462 |        58.50% |
| RSI + Daily Structure |              16 |             118 |        53.39% |

---

# Observations

* Daily Structure dramatically reduced signal count.
* Bullish opportunities collapsed from 147 to only 16 signals.
* The bullish edge observed in RSI Alone disappeared entirely.
* Average bullish returns deteriorated significantly.
* Bearish performance remained near random despite the additional filter.
* Daily Structure failed to improve either side of the market.

---

# Opportunity Reduction

### Bullish Signals

```text
147
↓
16
```

Reduction:

```text
89.1%
```

### Total Signals

```text
609
↓
134
```

Reduction:

```text
78.0%
```

This is one of the largest opportunity reductions observed in the entire project.

---

# Key Insight

This study provides strong evidence that:

> Higher selectivity does not automatically improve strategy quality.

In this case:

* Opportunity count collapsed.
* Bullish performance deteriorated.
* Average returns worsened.
* Statistical confidence weakened.

The filter removed most of the opportunities while failing to improve expectancy.

---

# Comparison to Gold

Gold Daily Structure:

* Improved bullish reversals.
* Maintained a meaningful edge.
* Reinforced location-based behavior.

SP500 Daily Structure:

* Reduced opportunities dramatically.
* Destroyed the bullish edge.
* Produced weaker performance than RSI Alone.

This suggests Daily Structure carries significantly more informational value in Gold than in the SP500.

---

# Research Interpretation

One possible explanation is that the SP500 already possesses a strong bullish drift.

When Daily Structure is added, the filter may be selecting only the most severe selloffs rather than the highest-quality reversals.

Instead of identifying strength, the filter may be identifying distress.

---

# Research Conclusion

The Daily Structure filter failed to improve SP500 performance.

Compared to RSI Alone:

* Fewer opportunities
* Lower win rates
* Worse average returns
* Smaller sample size

The evidence suggests that the SP500's bullish mean-reversion tendency may be stronger when RSI is allowed to operate without additional structural restrictions.

This study reinforces one of the strongest themes in the project:

> A filter can reduce opportunities without improving edge quality.

For the SP500, RSI Alone remains the superior framework based on current evidence.
