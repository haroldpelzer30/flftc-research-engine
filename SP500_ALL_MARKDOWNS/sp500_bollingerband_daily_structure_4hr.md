# SP500 H4 Bollinger Band + Daily Structure Research

## Test Configuration

* **Asset:** SP500
* **Timeframe:** H4 (4-Hour)
* **Strategy:** Bollinger Band + Daily Structure
* **Daily Structure:** Derived from H4 Data
* **BB Period:** 20
* **BB Standard Deviations:** 2
* **Near Daily Level Threshold:** 0.10%

---

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 39 |
| Bearish Signals | 37 |
| **Total Signals** | **76** |

---

# Bullish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 56.41% |
| 3 Candles | 58.97% |
| 6 Candles | 58.97% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0147% |
| 3 Candles | 0.0000% |
| 6 Candles | 0.0664% |

---

# Bearish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 45.95% |
| 3 Candles | 40.54% |
| 6 Candles | 35.14% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0309% |
| 3 Candles | 0.1229% |
| 6 Candles | 0.1216% |

---

# Comparison vs SP500 BB Alone

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB Alone | 519 | 58.20% |
| BB + Daily Structure | 76 | 58.97% |

---

# Key Findings

## Observation 1

Daily Structure barely improved the bullish side.

### BB Alone

```text
56.97%
58.20%
54.51%
```

### BB + Daily Structure

```text
56.41%
58.97%
58.97%
```

The improvement exists, but it is modest.

---

## Observation 2

The signal count collapsed.

### BB Alone

```text
519 signals
```

### BB + Daily Structure

```text
76 signals
```

Signal reduction:

```text
85%+
```

---

## Observation 3

The bearish side became even worse.

```text
45.95%
40.54%
35.14%
```

This is one of the strongest examples yet of SP500's bullish asymmetry.

---

## Observation 4

The market continues rejecting short-side reversals.

Even after adding Daily Structure:

```text
35.14%
```

at 6 candles.

The market overwhelmingly prefers upside continuation.

---

## Observation 5

The average return profile supports the bullish drift thesis.

Bullish:

```text
-0.0147%
0.0000%
0.0664%
```

Bearish:

```text
0.0309%
0.1229%
0.1216%
```

The bearish trades continue getting run over by the long-term upward trend.

---

# Comparison vs Gold BB + Daily Structure

## Gold

```text
60.00%
304 signals
```

## SP500

```text
58.97%
76 signals
```

Gold remains the stronger Daily Structure result.

---

# Preliminary Conclusion

Daily Structure did not transform SP500 the way it transformed Gold.

Strengths:

* Bullish edge remains strong.
* Win rate slightly improved.
* Long-horizon performance remained stable.

Weaknesses:

* Massive signal destruction.
* Minimal improvement.
* Bearish side collapsed.

---

# Research Takeaway

This study reinforces a familiar lesson:

> A filter should be judged not only by how much it improves win rate, but also by how many opportunities it destroys.

Daily Structure improved SP500 from:

```text
58.20%
```

to

```text
58.97%
```

while reducing opportunities from:

```text
519
```

to

```text
76
```

---

# Research Note

> The SP500 BB + Daily Structure study produced only a marginal improvement over BB Alone while eliminating more than 85% of opportunities. Unlike Gold, where Daily Structure materially enhanced Bollinger Band performance, the SP500 already possessed a strong bullish tendency without additional filtering. This may be another example of over-filtering a market that already wants to go up.

---

# Current SP500 BB Rankings

🥇 BB + Daily Structure — 58.97% (76 signals)

🥈 BB Alone — 58.20% (519 signals)

---

# Interim SP500 Conclusion

The SP500 appears to possess a strong bullish bias regardless of Daily Structure.

Daily Structure slightly improved performance but did not create a new edge.

The majority of the edge was already present in BB Alone.