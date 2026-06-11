# SP500 H4 Bollinger Band + Doji Research

## Test Configuration

* **Asset:** SP500
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Band + Doji
* **BB Period:** 20
* **BB Standard Deviations:** 2
* **Doji Body Threshold:** 10% of Candle Range

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Doji Signals | 24 |
| Bearish Doji Signals | 18 |
| **Total Signals** | **42** |

---

# Bullish Doji Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 66.67% |
| 3 Candles | 62.50% |
| 6 Candles | 58.33% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.1019% |
| 3 Candles | 0.1012% |
| 6 Candles | 0.1023% |

---

# Bearish Doji Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 50.00% |
| 3 Candles | 61.11% |
| 6 Candles | 50.00% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0295% |
| 3 Candles | -0.0213% |
| 6 Candles | -0.0901% |

---

# Comparison vs Previous SP500 BB Studies

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB Alone | 519 | 58.20% |
| BB + Double Bottom | 207 | 59.30% |
| BB + Daily Structure | 76 | 58.97% |
| BB + Doji | 42 | 66.67% |

---

# Key Findings

## Observation 1

The bullish side produced the highest headline win rate in the SP500 chapter.

```text
66.67%
62.50%
58.33%
```

However, the sample size is extremely small.

---

## Observation 2

The bullish average returns are remarkably consistent.

```text
0.1019%
0.1012%
0.1023%
```

Unlike many previous studies, returns remained positive across all horizons.

---

## Observation 3

The bearish side produced mixed results.

```text
50.00%
61.11%
50.00%
```

The signal count is too small to draw strong conclusions.

---

## Observation 4

Signal count collapsed.

### BB Alone

```text
519 signals
```

### BB + Doji

```text
42 signals
```

Opportunity reduction:

```text
More than 90%
```

---

## Observation 5

The Doji filter improved headline statistics but at a severe opportunity cost.

The result illustrates one of the recurring themes of the project:

```text
Higher Win Rate
≠
Better Strategy
```

if most opportunities disappear.

---

# Comparison vs SP500 BB Alone

## BB Alone

```text
58.20%
519 signals
```

## BB + Doji

```text
66.67%
42 signals
```

The Doji filter improved the headline win rate dramatically but removed the vast majority of opportunities.

---

# Comparison vs Gold BB + Doji

## Gold

```text
44.00%
46.00%
52.00%
```

## SP500

```text
66.67%
62.50%
58.33%
```

The same pattern filter produced dramatically different outcomes depending on the market.

---

# Preliminary Conclusion

The Doji filter generated impressive statistics but the sample size is too small to treat the result as robust.

Strengths:

* Highest bullish win rate in the SP500 chapter.
* Positive average returns.
* Consistent bullish performance.

Weaknesses:

* Extremely small sample size.
* Opportunity count reduced by over 90%.
* Statistical confidence remains limited.

---

# Research Takeaway

This study reinforces two major project themes:

> The market matters more than the indicator.

and

> An edge should be evaluated by both its strength and its frequency.

While the Doji produced strong headline numbers, the opportunity count is too small to place it above the more robust BB Alone study.

---

# Research Note

> The SP500 BB + Doji study produced the strongest headline bullish win rates observed in the SP500 chapter. However, those results were generated from only 24 bullish signals over the research period. The findings are intriguing but statistically fragile. The study provides another example of how highly selective filters can create impressive-looking results while dramatically reducing practical opportunity frequency.

---

# Current SP500 BB Rankings

🥇 BB Alone — 58.20% (519 signals)

🥈 BB + Double Bottom — 59.30% (207 signals)

🥉 BB + Daily Structure — 58.97% (76 signals)

4️⃣ BB + Doji — 66.67% (42 signals, statistically fragile)

5️⃣ BB + Inside Bar — 61.11% (39 signals, statistically fragile)

---

# Current SP500 Chapter Conclusion

The SP500 chapter consistently supports the same underlying message:

```text
Oversold Volatility
+
SP500
=
Bullish Opportunity
```

Every filter tested pointed toward bullish behavior.

The primary difference between studies was not direction, but the tradeoff between:

```text
Win Rate
vs
Opportunity Count
```

The strongest practical result remains BB Alone due to its combination of edge strength, consistency, and scalability.