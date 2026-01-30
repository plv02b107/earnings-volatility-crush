from src.pricing.black_scholes import black_scholes_price

def simulate_earnings_trade(S0, S1, iv_pre, iv_post, strategy="straddle"):
    """
    Simulate PnL for an earnings trade.
    
    Parameters:
    S0 : float : Price before earnings
    S1 : float : Price after earnings
    iv_pre : float : Implied volatility before earnings
    iv_post : float : Implied volatility after earnings
    strategy : str : "straddle" or "iron_condor"
    
    Returns:
    float : PnL of the trade
    """
    T = 2/252  # 2 trading days to earnings
    r = 0.0

    if strategy == "straddle":
        K = S0
        call_before = black_scholes_price(S0, K, T, r, iv_pre, "call")
        put_before  = black_scholes_price(S0, K, T, r, iv_pre, "put")
        call_after  = black_scholes_price(S1, K, 1/252, r, iv_post, "call")
        put_after   = black_scholes_price(S1, K, 1/252, r, iv_post, "put")
        pnl = (call_after + put_after) - (call_before + put_before)

    elif strategy == "iron_condor":
        # Short OTM put and call
        K_put_short = S0 * 0.95
        K_call_short = S0 * 1.05
        # Long protective wings
        K_put_long = S0 * 0.90
        K_call_long = S0 * 1.10

        # Premium collected before earnings
        put_short = black_scholes_price(S0, K_put_short, T, r, iv_pre, "put")
        call_short = black_scholes_price(S0, K_call_short, T, r, iv_pre, "call")
        put_long = black_scholes_price(S0, K_put_long, T, r, iv_pre, "put")
        call_long = black_scholes_price(S0, K_call_long, T, r, iv_pre, "call")
        credit = (put_short + call_short) - (put_long + call_long)

        # Value after earnings
        put_short_after = black_scholes_price(S1, K_put_short, 1/252, r, iv_post, "put")
        call_short_after = black_scholes_price(S1, K_call_short, 1/252, r, iv_post, "call")
        put_long_after = black_scholes_price(S1, K_put_long, 1/252, r, iv_post, "put")
        call_long_after = black_scholes_price(S1, K_call_long, 1/252, r, iv_post, "call")
        value_after = (put_short_after + call_short_after) - (put_long_after + call_long_after)

        pnl = credit - value_after

    return pnl
print("simulate trade module started")

