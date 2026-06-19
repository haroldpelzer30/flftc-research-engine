# EURUSD H4 Bollinger Band Research Summary

## Research Objective

This phase of the project tested whether **volatility expansion (Bollinger Bands)** produces a stronger mean-reversion signal than **momentum exhaustion (RSI)**.

All studies used:

* EURUSD
* H4 Timeframe
* Bollinger Bands (20,2)

---

# 1. Bollinger Band Alone

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Lower Band Signals | 2,464 |
| Upper Band Signals | 2,810 |
| Total Signals | 5,274 |

## Results

### Lower Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 50.41% |
| 3 Candles | 49.15% |
| 6 Candles | 46.92% |

### Upper Band Reversal

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 49.57% |
| 3 Candles | 48.54% |
| 6 Candles | 50.18% |

## Conclusion

Bollinger Bands alone produced essentially random results.

---

# 2. Bollinger Band + Daily Structure

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Signals | 371 |
| Bearish Signals | 423 |
| Total Signals | 794 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 56.87% |
| 3 Candles | 52.29% |
| 6 Candles | 50.40% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 53.66% |
| 3 Candles | 52.96% |
| 6 Candles | 52.01% |

## Conclusion

Daily Structure dramatically improved Bollinger Band performance.

This was the strongest filter tested.

---

# 3. Bollinger Band + Double Bottom / Double Top

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Double Bottom | 1,169 |
| Bearish Double Top | 1,284 |
| Total Signals | 2,453 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.78% |
| 3 Candles | 50.73% |
| 6 Candles | 49.36% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 52.34% |
| 3 Candles | 51.48% |
| 6 Candles | 51.48% |

## Conclusion

Double Bottoms and Double Tops improved performance slightly but failed to create a strong edge.

Most gains faded back toward randomness.

---

# 4. Bollinger Band + Inside Bar

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Inside Bar | 258 |
| Bearish Inside Bar | 298 |
| Total Signals | 556 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 56.20% |
| 3 Candles | 50.78% |
| 6 Candles | 51.94% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 50.34% |
| 3 Candles | 47.32% |
| 6 Candles | 52.35% |

## Conclusion

Inside Bars produced strong headline numbers but eliminated nearly 90% of opportunities.

Performance was similar to Daily Structure despite dramatically fewer trades.

---

# 5. Bollinger Band + Doji

## Signal Count

| Signal Type | Count |
|------------|-------:|
| Bullish Doji | 260 |
| Bearish Doji | 244 |
| Total Signals | 504 |

## Results

### Bullish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 48.08% |
| 3 Candles | 45.00% |
| 6 Candles | 36.92% |

### Bearish

| Horizon | Win Rate |
|----------|----------:|
| 1 Candle | 43.44% |
| 3 Candles | 42.62% |
| 6 Candles | 45.49% |

## Conclusion

Doji was the worst-performing Bollinger Band filter tested.

Rather than signaling reversal, the results suggest Doji candles may often represent a temporary pause before continuation.

---

# Final Ranking

## Ranked by Practical Value

### 🥇 BB + Daily Structure

* 56.87%
* 794 signals
* Best combination of edge and opportunity count

---

### 🥈 BB + Inside Bar

* 56.20%
* 556 signals
* Similar edge to Daily Structure but with fewer opportunities

---

### 🥉 BB + Double Bottom / Top

* 52.78%
* 2,453 signals
* Modest improvement over BB Alone

---

### 4th Place — BB Alone

* 50.18%
* 5,274 signals
* Essentially random

---

### 💀 Last Place — BB + Doji

* 48.08%
* 504 signals
* Worse than BB Alone

---

# Comparison vs RSI

## Best EURUSD RSI Result

RSI + Daily Structure

* 56.25%
* 1,151 signals

---

## Best EURUSD Bollinger Band Result

BB + Daily Structure

* 56.87%
* 794 signals

---

# Major Research Lessons

## Lesson 1

> **Location appears to matter more than the indicator itself.**

Both RSI and Bollinger Bands improved dramatically when Daily Structure was added.

---

## Lesson 2

> **Pattern recognition appears less valuable than location-based context.**

Daily Structure consistently outperformed Double Bottoms, Double Tops, and most candlestick filters.

---

## Lesson 3

> **Most filters reduce opportunity count far more than they improve edge quality.**

Inside Bars, Double Bottoms, and Dojis all demonstrated this effect.

---

## Lesson 4

> **A filter can improve a statistic without creating an edge.**

Several filters improved headline win rates while producing little follow-through.

---

## Lesson 5

> **Indecision is not necessarily exhaustion.**

The Doji study suggests that indecision at a volatility extreme often precedes continuation rather than reversal.

---

# EURUSD Bollinger Band Chapter Verdict

The strongest conclusion from the EURUSD Bollinger Band chapter is:

> **Volatility expansion alone does not appear to contain a meaningful mean-reversion edge. However, volatility expansion occurring near an important location can become significantly more predictive.**

The evidence suggests that location remains the dominant explanatory factor behind EURUSD reversal behavior.