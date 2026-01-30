import pandas as pd

def performance_summary(pnl):
    """
    Compute overall performance metrics for a series of PnL values.
    Returns a dictionary with key statistics.
    """
    cumulative = pnl.cumsum()
    running_max = cumulative.cummax()
    drawdown = running_max - cumulative  # absolute drawdown
    max_drawdown = drawdown.max()        # positive max drawdown
    
    return {
        "Total Trades": len(pnl),
        "Mean PnL": pnl.mean(),
        "Median PnL": pnl.median(),
        "Win Rate": (pnl > 0).mean(),
        "Total PnL": pnl.sum(),
        "Max Drawdown": max_drawdown
    }

def ticker_summary(df, pnl_col):
    """
    Aggregate PnL metrics by ticker.
    """
    return (
        df.groupby("Ticker")[pnl_col]
        .agg(
            Total_Trades="count",
            Win_Rate=lambda x: (x > 0).mean(),
            Avg_PnL="mean",
            Median_PnL="median",
            Total_PnL="sum",
            Max_Drawdown=lambda x: (x.cumsum() - x.cumsum().cummax()).min()
        )
        .sort_values("Total_PnL", ascending=False)
    )
