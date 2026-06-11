# EURUSD H4 RSI Alone Research

## Test Configuration

* **Asset:** EURUSD
* **Timeframe:** H4 (4-Hour)
* **Strategy:** RSI Alone
* **RSI Period:** 14

---

## Signal Count

| Signal Type       |     Count |
| ----------------- | --------: |
| Oversold          |     2,426 |
| Overbought        |     2,323 |
| **Total Signals** | **4,749** |

---

## Oversold Reversal Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   49.22% |
| 3 Candles      |   50.12% |
| 6 Candles      |   49.22% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |       -0.0155% |
| 3 Candles      |       -0.0359% |
| 6 Candles      |       -0.0799% |

---

## Overbought Reversal Results

### Win Rates

| Forward Period | Win Rate |
| -------------- | -------: |
| 1 Candle       |   50.67% |
| 3 Candles      |   50.84% |
| 6 Candles      |   50.45% |

### Average Returns

| Forward Period | Average Return |
| -------------- | -------------: |
| 1 Candle       |        0.0085% |
| 3 Candles      |        0.0327% |
| 6 Candles      |        0.0393% |

---

# Key Observations

### Signal Frequency

* EURUSD generated the largest sample size observed in the project so far.
* Total signals generated: **4,749**
* Approximately **475 signals per year** over a 10-year sample.

### Bullish Reversals

* Oversold conditions failed to produce a meaningful edge.
* Win rates remained near random across all holding periods.
* Performance slightly deteriorated at longer horizons.

### Bearish Reversals

* Overbought conditions also failed to produce a meaningful edge.
* Win rates remained very close to 50%.
* No evidence of persistent bearish mean reversion was observed.

### Holding Period Analysis

* Longer holding periods did not improve results.
* Neither side demonstrated meaningful persistence.
* EURUSD behaved differently from GBPUSD, USDCHF, Gold, SP500, and USDCAD.

### Average Return Analysis

* Bullish average returns remained negative.
* Bearish average returns remained weak.
* The combination of near-random win rates and weak returns suggests little exploitable edge.

---

# Comparison To Other Markets

| Asset  | Best RSI-Alone Result |
| ------ | --------------------: |
| Gold   |                  ~57% |
| SP500  |                58.50% |
| USDCHF |                57.00% |
| GBPUSD |                54.66% |
| USDCAD |                63.87% |
| EURUSD |                50.84% |

---

# Key Insight

This study produced one of the most important findings in the entire project:

> Opportunity count alone is not a proxy for edge quality.

EURUSD generated:

```text
4,749 signals
```

Yet produced:

```text
~50%
```

win rates.

Meanwhile:

```text
USDCHF
1,080 signals
57.00%
```

and

```text
USDCAD
484 signals
63.87%
```

produced far stronger results despite dramatically fewer opportunities.

---

# Preliminary Conclusion

EURUSD RSI Alone does not appear to contain a meaningful mean-reversion edge.

The pair generated an enormous number of signals but failed to produce statistically significant performance on either the bullish or bearish side.

This establishes an important baseline for future EURUSD research.

The key question becomes:

> Can filters create an edge where RSI Alone appears to have none?

Upcoming tests:

1. RSI + Daily Structure
2. RSI + Double Bottom / Double Top
3. RSI + Inside Bar
4. RSI + Weekly Structure

---

# Research Verdict

**Status:** Weak Baseline

Current interpretation:

* Massive opportunity count.
* Near-random win rates.
* No obvious bullish asymmetry.
* No obvious bearish asymmetry.
* One of the strongest examples so far that frequency does not equal quality.

EURUSD currently represents the benchmark example of:

> A market with many opportunities but little evidence of a meaningful RSI edge.
