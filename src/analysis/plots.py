# src/analysis/plots.py

import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

# -------------------------------------------------
def plot_equity_and_dd(pnl_series, label, save_path):
    pnl_series = pnl_series.reset_index(drop=True)

    equity = pnl_series.cumsum()
    drawdown = equity.cummax() - equity

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(equity, label="Equity", linewidth=2)
    ax.plot(drawdown, label="Drawdown", linestyle="--")

    ax.set_title(f"{label} – Equity & Drawdown")
    ax.set_xlabel("Trades")
    ax.set_ylabel("PnL")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.show()
    plt.close(fig)


# -------------------------------------------------
def plot_pnl_distribution(df, save_path):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(df["Straddle_PnL"], bins=40, alpha=0.6, label="Straddle")
    ax.hist(df["IronCondor_PnL"], bins=40, alpha=0.6, label="Iron Condor")

    ax.set_title("PnL Distribution")
    ax.set_xlabel("PnL")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.show()
    plt.close(fig)


# -------------------------------------------------
def plot_total_pnl_by_ticker(df, save_path):
    totals = pd.DataFrame({
        "Straddle": df.groupby("Ticker")["Straddle_PnL"].sum(),
        "Iron Condor": df.groupby("Ticker")["IronCondor_PnL"].sum()
    })

    fig, ax = plt.subplots(figsize=(12, 6))
    totals.plot(kind="bar", ax=ax)

    ax.set_title("Total PnL by Ticker")
    ax.set_ylabel("Total PnL")
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.show()
    plt.close(fig)


# -------------------------------------------------
def plot_equity_by_ticker(df, tickers, col, title, save_path):
    fig, ax = plt.subplots(figsize=(12, 6))

    for ticker in tickers:
        temp = df[df["Ticker"] == ticker][col].reset_index(drop=True)
        if len(temp) > 0:
            ax.plot(temp.cumsum(), label=ticker)

    ax.set_title(title)
    ax.set_xlabel("Trades")
    ax.set_ylabel("Cumulative PnL")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(save_path, dpi=300)
    plt.show()
    plt.close(fig)
