# SP500 H4 RSI + Monthly Structure Research

## Test Conditions

- Market: SP500
- Execution Timeframe: H4
- Structure Timeframe: Monthly
- RSI Period: 14
- Near Monthly Level Threshold: 0.20%

---

# Bullish RSI + Monthly Structure Results

## Signal Count

- Bullish Signals: 5

| Forward Window | Win Rate |
|---|---|
| 1 Candle | 60.00% |
| 3 Candles | 20.00% |
| 6 Candles | 20.00% |

### Average Returns

- 1 Candle Avg: 0.0019%
- 3 Candle Avg: -0.1006%
- 6 Candle Avg: -0.0869%

---

# Bearish RSI + Monthly Structure Results

## Signal Count

- Bearish Signals: 38

| Forward Window | Win Rate |
|---|---|
| 1 Candle | 52.63% |
| 3 Candles | 52.63% |
| 6 Candles | 63.16% |

### Average Returns

- 1 Candle Avg: -0.0221%
- 3 Candle Avg: -0.0061%
- 6 Candle Avg: -0.0197%

---

# Observations

- Bullish signal count collapsed almost completely.
- Only 5 bullish signals were generated across the dataset.
- Bullish reversal behavior deteriorated rapidly after the first candle.
- Bearish monthly structure reactions appeared stronger than expected.
- SP500 monthly overbought conditions may contain more informational value than oversold conditions on H4.

---

# Important Statistical Note

The bullish sample size was far too small for reliable conclusions.

With only 5 bullish signals:
- the results are statistically fragile
- highly sensitive to individual trades
- and unsuitable for robust inference

Even the bearish side remains relatively small at 38 signals.

---

# Comparison To Previous SP500 Tests

| Strategy | Bullish Signals | Best Bullish WR |
|---|---|---|
| RSI Alone | 147 | 58.50% |
| RSI + Double Bottom | 45 | 60.00% |
| RSI + Inside Bar | 25 | 68.00% (fragile) |
| RSI + Monthly Structure | 5 | 60.00% (extremely fragile) |

---

# Key Insight

- Monthly structure on SP500 appears too restrictive for practical H4 reversal research.
- Macro monthly levels may be too distant from normal H4 RSI exhaustion behavior.
- The SP500 may trend too smoothly upward to create meaningful oversold monthly retests frequently.
- Over-filtering continues demonstrating severe sample size reduction effects.

---

# Research Conclusion

This test strongly reinforces a major theme emerging throughout the research process:

More filters do NOT automatically create better strategies.

The strongest systems so far appear to balance:
- meaningful behavioral logic
- adequate signal frequency
- statistical robustness
- and believable market structure interaction

rather than maximizing selectivity alone.