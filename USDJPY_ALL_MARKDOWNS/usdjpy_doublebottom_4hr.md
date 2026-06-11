# USDJPY H4 Bollinger Band + Double Bottom / Double Top Research

## Test Configuration

* **Asset:** USDJPY
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
| Bullish Double Bottom Signals | 1,120 |
| Bearish Double Top Signals | 1,306 |
| **Total Signals** | **2,426** |

---

# Bullish Double Bottom Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 54.46% |
| 3 Candles | 52.41% |
| 6 Candles | 50.80% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0130% |
| 3 Candles | -0.0400% |
| 6 Candles | -0.0936% |

---

# Bearish Double Top Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 48.70% |
| 3 Candles | 43.95% |
| 6 Candles | 47.01% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0144% |
| 3 Candles | 0.0415% |
| 6 Candles | 0.0427% |

---

# Comparison vs Previous USDJPY BB Studies

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB Alone | 5,366 | 52.71% |
| BB + Daily Structure | 689 | 56.78% |
| BB + Double Bottom / Top | 2,426 | 54.46% |

---

# Key Findings

## Observation 1

The Double Bottom / Top filter reduced opportunities but retained a large sample size.

```text
5,366
↓
2,426
```

Opportunity Reduction:

```text
54.8%
```

Unlike many previous pattern studies, the sample remains statistically meaningful.

---

## Observation 2

The bullish side tells a coherent story.

```text
54.46%
52.41%
50.80%
```

The edge gradually decays over time but remains above 50% across all tested horizons.

This suggests:

```text
Short-term bounce
↓
Gradual edge decay
```

rather than a complete failure.

---

## Observation 3

The bearish side completely failed.

```text
48.70%
43.95%
47.01%
```

Every horizon remained below 50%.

---

## Observation 4

Double Bottoms improved the bullish side relative to BB Alone.

### BB Alone Bullish

```text
52.71%
50.59%
50.07%
```

### BB + Double Bottom

```text
54.46%
52.41%
50.80%
```

The improvement is modest but consistent.

---

## Observation 5

Average returns remain unfavorable.

Bullish Side:

```text
-0.0130%
-0.0400%
-0.0936%
```

Bearish Side:

```text
0.0144%
0.0415%
0.0427%
```

The win-rate improvement does not translate into stronger average returns.

---

# Comparison vs USDJPY RSI Research

## USDJPY RSI Alone

```text
~50%
```

## USDJPY RSI + Double Bottom

```text
~52%–54%
```

## USDJPY BB + Double Bottom

```text
54.46%
52.41%
50.80%
```

The results are surprisingly similar to what was observed in the RSI chapter.

---

# Preliminary Conclusion

This is the second consecutive Ninja study showing evidence of a bullish tendency.

Strengths:

* Large sample size.
* Consistent bullish performance.
* Better than BB Alone.
* Better than most previous BB pattern studies.

Weaknesses:

* Bearish side remains ineffective.
* Average returns remain weak.
* Underperforms BB + Daily Structure.

---

# Research Takeaway

Unlike many previous Double Bottom studies throughout the project, the Ninja's Double Bottom filter did not completely collapse.

Instead, it appears to identify:

```text
Short-term bullish exhaustion
```

that produces a modest mean-reversion effect.

---

# Current USDJPY BB Rankings

🥇 BB + Daily Structure — 56.78% (689 signals)

🥈 BB + Double Bottom / Top — 54.46% (2,426 signals)

🥉 BB Alone — 52.71% (5,366 signals)

---

# Research Note

> The USDJPY BB + Double Bottom study is one of the first pattern-recognition studies in the Bollinger Band chapter that appears to improve results without destroying the majority of opportunities. While the improvement is modest, the bullish side remained above 50% across all horizons and retained more than 2,400 signals. This suggests that certain pattern filters may add value when applied to specific markets, even though similar filters failed across many other assets.

---

# Momentum vs Volatility Scoreboard

| Asset | Winner |
|---------|---------|
| EURUSD | RSI |
| GBPUSD | RSI |
| USDCHF | RSI |
| AUDUSD | RSI |
| NZDUSD | RSI |
| USDCAD | RSI |
| USDJPY (so far) | BB |

Current Score:

```text
RSI 6
BB 1
```

The Ninja continues to provide Team BB with its strongest evidence yet that volatility extremes combined with market structure may contain useful information.