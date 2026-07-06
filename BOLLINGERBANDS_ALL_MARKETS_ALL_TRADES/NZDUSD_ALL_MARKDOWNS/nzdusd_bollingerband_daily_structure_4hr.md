# NZDUSD H4 Bollinger Band + Daily Structure Research

## Test Configuration

* **Asset:** NZDUSD
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
| Bullish Signals | 244 |
| Bearish Signals | 274 |
| **Total Signals** | **518** |

---

# Bullish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 50.41% |
| 3 Candles | 45.90% |
| 6 Candles | 45.08% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | -0.0126% |
| 3 Candles | -0.0389% |
| 6 Candles | -0.0295% |

---

# Bearish Results

## Win Rates

| Forward Period | Win Rate |
|--------------|----------:|
| 1 Candle | 47.81% |
| 3 Candles | 50.00% |
| 6 Candles | 48.91% |

## Average Returns

| Forward Period | Average Return |
|--------------|---------------:|
| 1 Candle | 0.0002% |
| 3 Candles | -0.0076% |
| 6 Candles | 0.0312% |

---

# Comparison vs NZDUSD BB Alone

| Strategy | Signals | Best Result |
|----------|---------:|------------:|
| BB Alone | 4,612 | 51.94% |
| BB + Daily Structure | 518 | 50.41% |

---

# Key Findings

## Observation 1

Daily Structure destroyed opportunity count.

```text
4612
↓
518
```

Opportunity Reduction:

**~88.8%**

---

## Observation 2

Daily Structure failed to improve the signal.

### BB Alone

```text
51.94%
```

### BB + Daily Structure

```text
50.41%
```

The filter actually made performance worse.

---

## Observation 3

The bullish side deteriorated significantly over time.

```text
50.41%
↓
45.90%
↓
45.08%
```

This is one of the weakest Daily Structure results observed so far.

---

## Observation 4

The bearish side remained effectively random.

```text
47.81%
50.00%
48.91%
```

No meaningful edge is visible.

---

## Observation 5

Average returns remained weak or negative.

Bullish Side:

```text
-0.0126%
-0.0389%
-0.0295%
```

Bearish Side:

```text
0.0002%
-0.0076%
0.0312%
```

The economic value of the signal appears negligible.

---

# Comparison vs Previous Daily Structure Studies

| Asset | Best Result | Signals |
|---------|----------:|---------:|
| GBPUSD BB + Daily Structure | 56.33% | 730 |
| AUDUSD BB + Daily Structure | 54.44% | 526 |
| USDCHF BB + Daily Structure | 53.62% | 150 |
| NZDUSD BB + Daily Structure | 50.41% | 518 |

---

# Comparison to NZDUSD RSI Research

## NZDUSD RSI Alone

```text
52.86%
3343 signals
```

## NZDUSD RSI + Daily Structure

```text
53.31%
640 signals
```

## NZDUSD BB + Daily Structure

```text
50.41%
518 signals
```

RSI continues to outperform Bollinger Bands by a meaningful margin.

---

# Preliminary Conclusion

The Daily Structure filter failed completely on NZDUSD.

The filter:

* Reduced opportunity count by nearly 89%
* Failed to improve win rates
* Produced weak average returns
* Generated results close to random

Unlike AUDUSD, where Daily Structure produced a modest improvement, NZDUSD showed virtually no benefit from adding Daily Structure.

---

# Research Takeaway

This study reinforces a major project lesson:

> **A filter can reduce opportunity count dramatically without creating any additional predictive power.**

The Daily Structure filter removed nearly 4,100 opportunities while producing weaker results than the underlying Bollinger Band signal.

This is one of the clearest examples so far that additional confirmation is not automatically beneficial.

---

# Early Chapter Verdict

Current NZDUSD BB Standings:

🥇 BB Alone — 51.94%

🥈 BB + Daily Structure — 50.41%

So far the Kiwi chapter is following the Aussie chapter closely:

```text
Lots of opportunities
↓
Very little edge
↓
Filters fail to help
```

---

# Momentum vs Volatility Scoreboard

| Asset | Winner |
|---------|---------|
| EURUSD | RSI |
| GBPUSD | RSI |
| USDCHF | RSI |
| AUDUSD | RSI |
| NZDUSD | RSI (so far) |

Current Score:

```text
RSI 4
BB 0
```

Team Bollinger Bands desperately needs a comeback in the remaining Kiwi studies.