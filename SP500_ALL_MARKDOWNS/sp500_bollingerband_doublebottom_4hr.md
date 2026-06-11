# SP500 H4 Bollinger Band + Double Bottom / Double Top Research

## Test Configuration

* **Asset:** SP500
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Band + Double Bottom / Double Top
* **BB Period:** 20
* **BB Standard Deviations:** 2
* **Lookback Bars:** 10
* **Near Level Threshold:** 0.15%

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Double Bottom Signals | 86 |
| Bearish Double Top Signals | 121 |
| **Total Signals** | **207** |

---

# Bullish Double Bottom Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 59.30% |
| 3 Candles | 55.81% |
| 6 Candles | 51.16% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0288% |
| 3 Candles | -0.0101% |
| 6 Candles | -0.0840% |

---

# Bearish Double Top Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 47.11% |
| 3 Candles | 48.76% |
| 6 Candles | 49.59% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0161% |
| 3 Candles | 0.0034% |
| 6 Candles | -0.0427% |

---

# Comparison vs Previous SP500 BB Studies

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB + Daily Structure | 76 | 58.97% |
| BB + Double Bottom / Top | 207 | 59.30% |
| BB Alone | 519 | 58.20% |

---

# Key Findings

## Observation 1

The strongest result in the study occurs immediately.

```text
59.30%
```

However, performance steadily declines afterward.

```text
59.30%
↓
55.81%
↓
51.16%
```

---

## Observation 2

Unlike Gold, the Double Bottom filter did not improve longer-term performance.

The edge fades as the holding period increases.

---

## Observation 3

The signal count fell dramatically.

### BB Alone

```text
519 signals
```

### BB + Double Bottom

```text
207 signals
```

Opportunity reduction:

```text
~60%
```

---

## Observation 4

The bearish side remains ineffective.

```text
47.11%
48.76%
49.59%
```

Even after adding a Double Top filter, SP500 continues exhibiting strong bullish asymmetry.

---

## Observation 5

Average returns raise concerns.

Bullish:

```text
0.0288%
-0.0101%
-0.0840%
```

Despite respectable win rates, average returns deteriorate over longer holding periods.

---

# Comparison vs SP500 BB Alone

## BB Alone

```text
56.97%
58.20%
54.51%
```

## BB + Double Bottom

```text
59.30%
55.81%
51.16%
```

The Double Bottom filter improves the immediate reaction but weakens the longer-horizon profile.

---

# Comparison vs Gold BB + Double Bottom

## Gold

```text
54.62%
54.22%
55.22%
```

Stable performance.

## SP500

```text
59.30%
55.81%
51.16%
```

Declining performance.

Gold's Double Bottom results were actually more durable.

---

# Preliminary Conclusion

The Double Bottom filter helped identify stronger short-term reactions but failed to improve long-term edge quality.

Strengths:

* Strong 1-candle performance.
* Reasonable sample size.
* Clear bullish bias.

Weaknesses:

* Edge fades over time.
* Negative longer-horizon returns.
* Reduced opportunity count substantially.

---

# Research Takeaway

This study resembles a familiar project pattern:

> A signal that predicts a short-term bounce is not necessarily a signal that predicts a durable reversal.

The Double Bottom appears to identify:

```text
Short-Term Exhaustion
```

more effectively than:

```text
Long-Term Reversal
```

---

# Research Note

> The SP500 BB + Double Bottom study produced the strongest short-term win rate observed in the SP500 chapter but failed to maintain that advantage over longer horizons. While the pattern appears effective at identifying immediate rebounds following volatility extremes, the edge steadily decays. This suggests that Double Bottoms may capture short-term exhaustion more reliably than durable reversals in the SP500.

---

# Current SP500 BB Rankings

🥇 BB + Double Bottom — 59.30% (short-term)

🥈 BB + Daily Structure — 58.97%

🥉 BB Alone — 58.20%

---

# Current SP500 Chapter Scorecard

### Strong

✅ BB Alone

### Strong but Short-Term

✅ BB + Double Bottom

### Strong but Opportunity-Starved

✅ BB + Daily Structure

---

# Interim SP500 Conclusion

The SP500 continues to support the broader hypothesis that Bollinger Bands perform better in markets with persistent bullish drift.

However, unlike Gold, additional filters have not produced a dramatic improvement over the already-strong BB Alone baseline.

The majority of the edge appears to exist before the filters are applied.