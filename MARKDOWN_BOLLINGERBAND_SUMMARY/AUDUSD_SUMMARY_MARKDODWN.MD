# AUDUSD H4 Bollinger Band Research Summary

## Research Objective

This phase of the project evaluated whether **volatility expansion (Bollinger Bands)** can identify profitable mean-reversion opportunities on AUDUSD and how those results compare to the RSI chapter.

All studies used:

* AUDUSD
* H4 Timeframe
* Bollinger Bands (20,2)

---

# 1. Bollinger Band Alone

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Lower Band Signals | 2,360 |
| Upper Band Signals | 2,303 |
| Total Signals | 4,663 |

## Results

### Lower Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 50.97% |
| 3 Candles | 51.86% |
| 6 Candles | 50.51% |

### Upper Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 50.46% |
| 3 Candles | 49.07% |
| 6 Candles | 47.50% |

## Conclusion

AUDUSD generated a very large number of opportunities but remained extremely close to random.

This was the first major indication that opportunity count does not automatically create edge quality.

---

# 2. Bollinger Band + Daily Structure

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 270 |
| Bearish Signals | 256 |
| Total Signals | 526 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 54.44% |
| 3 Candles | 53.70% |
| 6 Candles | 47.78% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 53.91% |
| 3 Candles | 47.66% |
| 6 Candles | 45.31% |

## Conclusion

Daily Structure improved the initial bounce.

However:

```text
54.44%
↓
53.70%
↓
47.78%
```

The edge deteriorated rapidly over time.

This appears to identify short-term reactions rather than durable reversals.

---

# 3. Bollinger Band + Double Bottom / Double Top

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Double Bottom Signals | 1,050 |
| Bearish Double Top Signals | 1,120 |
| Total Signals | 2,170 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 48.48% |
| 3 Candles | 50.76% |
| 6 Candles | 47.71% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 51.16% |
| 3 Candles | 47.41% |
| 6 Candles | 46.07% |

## Conclusion

AUDUSD produced an enormous number of retests.

However:

```text
2170 signals
```

failed to produce meaningful predictive power.

The pattern occurred frequently but provided little forecasting value.

---

# 4. Bollinger Band + Inside Bar

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 197 |
| Bearish Signals | 166 |
| Total Signals | 363 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 44.67% |
| 3 Candles | 50.25% |
| 6 Candles | 53.30% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 44.58% |
| 3 Candles | 46.99% |
| 6 Candles | 45.78% |

## Conclusion

The bullish side improved over time.

However:

* Signal count collapsed.
* Bearish performance failed completely.
* Improvement was too small to justify the opportunity reduction.

---

# 5. Bollinger Band + Doji

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 135 |
| Bearish Signals | 110 |
| Total Signals | 245 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 49.63% |
| 3 Candles | 45.93% |
| 6 Candles | 48.89% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 54.55% |
| 3 Candles | 50.91% |
| 6 Candles | 46.36% |

## Conclusion

Doji produced the strongest headline statistic in the chapter.

However:

* Signal count collapsed by nearly 95%.
* The bullish side showed no edge.
* The bearish edge faded rapidly.
* Average returns remained weak.

---

# Final Ranking

## Ranked by Practical Research Value

### 🥇 BB + Daily Structure

* Best Result: 54.44%
* Signals: 526

Most balanced result in the chapter.

---

### 🥈 BB + Doji

* Best Result: 54.55%
* Signals: 245

Highest headline statistic but poor scalability.

---

### 🥉 BB + Inside Bar

* Best Result: 53.30%
* Signals: 363

Small improvement with major opportunity destruction.

---

### 4th Place — BB Alone

* Best Result: 51.86%
* Signals: 4,663

Largest sample size but little predictive power.

---

### 5th Place — BB + Double Bottom / Top

* Best Result: 51.16%
* Signals: 2,170

Large sample size with almost no forecasting advantage.

---

# Major Research Lessons

## Lesson 1

> **Opportunity frequency alone is not a proxy for edge quality.**

### Evidence

#### AUDUSD BB Alone

```text
4663 signals
51.86%
```

#### USDCHF BB Alone

```text
1248 signals
53.75%
```

AUDUSD generated nearly four times as many opportunities while producing weaker performance.

---

## Lesson 2

> **A pattern can occur frequently without containing meaningful predictive information.**

### Evidence

#### AUDUSD BB + Double Bottom / Top

```text
2170 signals
```

Despite occurring frequently, the pattern remained close to random.

---

## Lesson 3

> **Location may improve a signal's timing without necessarily improving its long-term predictive power.**

### Evidence

#### BB + Daily Structure

```text
54.44%
53.70%
47.78%
```

The edge appeared strongest immediately after the signal and deteriorated over time.

---

## Lesson 4

> **A filter should be judged not only by how much it improves win rate, but also by how many opportunities it destroys.**

### Example

#### BB Alone

```text
4663 signals
51.86%
```

#### BB + Inside Bar

```text
363 signals
53.30%
```

A small improvement in win rate came at the cost of over 92% of opportunities.

---

## Lesson 5

> **A filter can create an attractive headline statistic while simultaneously destroying most of the opportunities.**

### Example

#### BB + Doji

```text
54.55%
245 signals
```

The improvement was accompanied by a 95% reduction in opportunities.

---

# Comparison vs RSI Chapter

## AUDUSD RSI Alone

```text
52.10%
3487 signals
```

## AUDUSD RSI + Daily Structure

```text
55.02%
1052 signals
```

## Best AUDUSD BB Result

```text
54.44%
526 signals
```

---

# Chapter Verdict

The AUDUSD Bollinger Band chapter produced a large number of opportunities but very little evidence of a robust market inefficiency.

Most filters either:

* Reduced opportunities dramatically
* Produced only marginal improvements
* Generated short-term bounces rather than durable reversals

The strongest BB result failed to surpass the strongest RSI result despite operating on roughly half the sample size.

---

# Final Conclusion

The AUDUSD chapter reinforces a growing project theme:

> **More opportunities do not necessarily imply a stronger edge.**

AUDUSD generated thousands of volatility-expansion signals, yet most results remained close to random.

The chapter ultimately suggests that momentum-based signals continue to contain more predictive information than volatility-expansion signals on the H4 timeframe.

---

# Momentum vs Volatility Scoreboard

| Asset | Winner |
|---------|---------|
| EURUSD | RSI |
| GBPUSD | RSI |
| USDCHF | RSI |
| AUDUSD | RSI |

## Current Score

```text
RSI 4
BB 0
```

Team Bollinger Bands now turns to NZDUSD, Gold, Silver, SP500, and NAS100 in an attempt to avoid a complete shutout.