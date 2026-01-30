# Earnings Volatility Crush — Simulation Study

## Overview

This project studies the **earnings-related volatility crush phenomenon** using a
**controlled Monte Carlo simulation framework**.

Rather than relying on historical backtests, the project isolates the interaction between:

- Implied volatility collapse  
- Earnings-related price jumps  
- Option payoff convexity  

Two canonical option strategies are evaluated:

- **Long ATM Straddle** (long volatility, convex payoff)
- **Iron Condor** (short volatility, concave payoff)

The objective is to test whether **volatility crush alone** is sufficient for profitability,
or whether **payoff structure and tail risk** dominate outcomes.



## Motivation

A common belief in options trading is:

> “Selling volatility around earnings is profitable because implied volatility collapses after the announcement.”

This project empirically challenges that assumption by showing that
**earnings returns are jump-driven and fat-tailed**, making payoff structure
more important than volatility direction.



## Simulation Framework

For each simulated earnings event:

- **Pre-earnings price (S₀):**  
  Uniformly sampled from [90, 100]

- **Post-earnings price (S₁):**  
  Uniformly sampled from [90, 100]
- **Pre-earnings implied volatility (IV₀):**  
  Uniformly sampled from [0.20, 0.50]

- **Post-earnings implied volatility (IV₁):**  
  Uniformly sampled from [0.10, 0.30] to model volatility crush

The **same simulated dataset** is used consistently across all notebooks to ensure
reproducibility and fair comparison between strategies.



## Strategies Evaluated

### 1. Long ATM Straddle
- Long call + long put at-the-money
- Positive Gamma and positive Vega
- Convex payoff with unlimited upside
- Sensitive to large earnings moves

### 2. Iron Condor
- Short OTM call spread + short OTM put spread
- Negative Gamma and negative Vega
- Capped profit and large tail risk
- Vulnerable to earnings jumps



## Performance Summary

| Strategy      | Trades | Mean PnL | Median PnL | Win Rate | Total PnL | Max Drawdown |
|---------------|--------|----------|------------|----------|-----------|--------------|
| Straddle      | 400    | +4.80    | +3.78      | 81.5%    | +1919     | 3.18         |
| Iron Condor   | 400    | −1.97    | −1.09      | 30.3%    | −789      | 785          |



## Interpretation of Results

### Long Straddle (Long Volatility)

- High win rate and positive expected value
- Low drawdowns despite volatility crush
- Performance driven by **convex payoff structure**
- Large earnings jumps dominate small volatility losses

The straddle benefits from the **fat-tailed distribution of earnings returns**, where
a small number of large moves contribute disproportionately to total PnL.


### Iron Condor (Short Volatility)

- Low win rate and negative expected value
- Severe drawdowns due to tail events
- Losses dominated by adverse price jumps
- Volatility crush insufficient to offset tail risk

Despite being theoretically aligned with volatility collapse,
the iron condor fails due to its **concave payoff structure**.


## Key Insights

1. **Volatility crush alone does not guarantee profitability**
2. **Payoff convexity is critical in earnings-driven environments**
3. Long volatility strategies benefit from:
   - Fat-tailed price jumps
   - Asymmetric upside
   - Distributional skew
4. Short volatility strategies suffer from:
   - Severe tail losses
   - Large drawdowns
   - Poor risk-adjusted returns


## Core Conclusion

> **Earnings trading is not about volatility direction,  
but about distributional asymmetry and payoff convexity.**

Although implied volatility collapses after earnings,
strategies with convex payoffs dominate in jump-driven markets.



## Limitations

- No transaction costs or bid–ask spreads
- Simplified implied volatility dynamics
- No volatility skew or smile modeling
- Stylized price jump process



## Future Extensions

- Calibration using real earnings data
- Skew-aware option pricing
- CVaR and tail-risk metrics
- Strategy stress testing



## Final Remarks

This project demonstrates that **strategy design matters more than volatility levels**
during earnings announcements.

It highlights the importance of understanding:
- Tail risk
- Payoff curvature
- Return distributions

rather than relying on simplistic volatility-based heuristics.

## Objective
The project analyzes the relationship between trader behavior (profitability, leverage, volume, risk) and market sentiment (Fear vs Greed index). The aim is to identify hidden trends or signals that can help design smarter trading strategies.Also an ML model is made using CatBoost.

## Datasets
1. Historical Trader Data  
   - Columns include: `Account`, `Coin`, `Execution Price`, `Size Tokens`, `Size USD`, `Side`, `Timestamp IST`, `Closed PnL`, `Leverage`, etc.

2. Bitcoin Market Sentiment (Fear & Greed Index)  
   - Columns include: `date`, `value`, `classification` (Fear, Greed, Extreme Fear, Extreme Greed).

## How to Run
1. Open the notebook in Google Colab:  
   - [Insert your Colab link here]  
   (Make sure the notebook is set to “Anyone with the link can view”)

2. Run all cells in `notebook_1.ipynb`.  
   - https://colab.research.google.com/drive/1JSrriGafaVGIeXBtn16Dum3jYl6bhlsl?usp=sharing
   `  
   - Visualizations will be stored in `outputs/`

3. Refer to `ds_report.pdf` for summarized insights and conclusions.

## Outputs
Some of the outputs included in `outputs/`:
- `pnl_vs_sentiment.png` - Scatterplot of PnL vs sentiment  
- `leverage_boxplot.png` - Leverage distribution during Fear vs Greed  
- `risk_profiles.png` - Profitability segmented by risk-taking behavior  

## Notes
- Raw data files were provided in the assignment.  
- Intermediate CSVs are stored in `csv_files/` for reproducibility.  
- Analysis code is written in Google Colab (Python, Pandas, Matplotlib, Seaborn).  
- The structure follows the exact submission guidelines.  
