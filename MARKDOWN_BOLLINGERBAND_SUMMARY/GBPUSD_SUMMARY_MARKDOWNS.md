# GBPUSD H4 Bollinger Band Research Summary

## Research Objective

This phase of the project tested whether **volatility expansion (Bollinger Bands)** can identify reliable mean-reversion opportunities on GBPUSD and how those results compare to the RSI chapter.

All studies used:

* GBPUSD
* H4 Timeframe
* Bollinger Bands (20,2)

---

# 1. Bollinger Band Alone

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Lower Band Signals | 2,329 |
| Upper Band Signals | 2,346 |
| Total Signals | 4,675 |

## Results

### Lower Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.90% |
| 3 Candles | 50.92% |
| 6 Candles | 49.46% |

### Upper Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.09% |
| 3 Candles | 50.43% |
| 6 Candles | 49.62% |

## Conclusion

Slightly better than EURUSD Bollinger Bands Alone but still weak overall.

The edge faded rapidly and regressed toward randomness.

---

# 2. Bollinger Band + Daily Structure

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 359 |
| Bearish Signals | 371 |
| Total Signals | 730 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 54.87% |
| 3 Candles | 54.60% |
| 6 Candles | 50.14% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.83% |
| 3 Candles | 56.33% |
| 6 Candles | 53.64% |

## Conclusion

Strongest and most repeatable GBPUSD Bollinger Band study.

Daily Structure once again provided the largest improvement.

---

# 3. Bollinger Band + Double Bottom / Double Top

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Double Bottom Signals | 1,199 |
| Bearish Double Top Signals | 1,213 |
| Total Signals | 2,412 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 54.05% |
| 3 Candles | 50.71% |
| 6 Candles | 50.88% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.35% |
| 3 Candles | 50.62% |
| 6 Candles | 49.13% |

## Conclusion

Produced a very large number of retest opportunities.

Most of the edge appeared immediately after the signal and faded quickly.

Supports the short-term bounce hypothesis.

---

# 4. Bollinger Band + Inside Bar

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Inside Bar Signals | 247 |
| Bearish Inside Bar Signals | 259 |
| Total Signals | 506 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 55.06% |
| 3 Candles | 48.99% |
| 6 Candles | 51.82% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 57.14% |
| 3 Candles | 48.65% |
| 6 Candles | 52.12% |

## Conclusion

Highest headline win rate.

However:

* Nearly 90% of opportunities were eliminated.
* Most of the edge disappeared after the first candle.

Classic example of opportunity destruction.

---

# 5. Bollinger Band + Doji

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Doji Signals | 145 |
| Bearish Doji Signals | 131 |
| Total Signals | 276 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.41% |
| 3 Candles | 46.21% |
| 6 Candles | 53.10% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 50.38% |
| 3 Candles | 53.44% |
| 6 Candles | 56.49% |

## Conclusion

Unlike EURUSD, Doji did not completely fail.

However:

* Signal count was extremely small.
* Results are interesting but statistically fragile.
* Requires replication on additional assets.

---

# Final Ranking

## Ranked by Practical Research Value

### 🥇 Bollinger Band + Daily Structure

* Best Result: 56.33%
* Signals: 730

Best combination of edge strength and opportunity count.

---

### 🥈 Bollinger Band + Inside Bar

* Best Result: 57.14%
* Signals: 506

Strong headline statistic but poor scalability.

---

### 🥉 Bollinger Band + Double Bottom / Top

* Best Result: 54.05%
* Signals: 2,412

Most scalable pattern-based study.

---

### 4th Place — Bollinger Band + Doji

* Best Result: 56.49%
* Signals: 276

Interesting result but sample size is too small for strong conclusions.

---

### 5th Place — Bollinger Band Alone

* Best Result: 52.90%
* Signals: 4,675

Weak standalone signal.

---

# Major Research Lessons

## Lesson 1

> **GBPUSD produces an unusually large number of retest opportunities.**

Evidence:

* 2,412 BB + Double Bottom/Top signals.

GBPUSD appears substantially more retest-heavy than strongly trending assets such as NAS100.

---

## Lesson 2

> **A signal that predicts a short-term bounce is not necessarily a signal that predicts a meaningful reversal.**

Evidence:

### BB + Double Bottom

54.05% → 50.71% → 50.88%

### BB + Inside Bar

57.14% → 48.65% → 52.12%

Interpretation:

```text
Signal Forms
↓
Market Bounces
↓
Edge Disappears
```

rather than:

```text
Signal Forms
↓
Market Reverses
↓
Trend Changes
```

---

## Lesson 3

> **Location continues to outperform pattern recognition.**

Daily Structure remained the strongest and most repeatable Bollinger Band filter tested.

---

## Lesson 4

> **Extremely selective filters can create attractive headline statistics while destroying most opportunities.**

Evidence:

| Strategy | Signals |
|-----------|---------:|
| BB Alone | 4,675 |
| BB + Inside Bar | 506 |
| BB + Doji | 276 |

Higher win rates did not necessarily create better overall edges.

---

## Lesson 5

> **The market matters more than the indicator.**

GBPUSD displayed persistent bearish asymmetry across:

* RSI Studies
* Daily Structure Studies
* Bollinger Band Studies
* Doji Studies

The same market personality remained visible despite changing indicators.

---

# Comparison vs RSI Chapter

## Best RSI Result

GBPUSD RSI + Daily Structure

* 55.52% Bearish

---

## Best Bollinger Band Result

GBPUSD BB + Daily Structure

* 56.33% Bearish

---

# GBPUSD Chapter Verdict

The strongest conclusion from the GBPUSD Bollinger Band chapter is:

> **Volatility expansion alone provides only a modest edge, but volatility expansion occurring near meaningful market structure becomes significantly more predictive.**

The chapter also reinforces one of the strongest themes of the entire project:

> **Location-based context appears to contain more predictive information than pattern-based confirmation.**

Finally, the persistence of GBPUSD's bearish asymmetry across both RSI and Bollinger Band studies provides additional evidence that the underlying market behavior may be more important than the indicator used to measure it.