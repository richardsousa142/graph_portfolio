# importar libraries
import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Definição do portfolio de Markovitz
def markowitz_portfolio(returns, cov_matrix, risk_free_rate=0.0):
    n_assets = cov_matrix.shape[0]
    mean_returns = returns.mean() * 252  # Annualize returns
    args = (mean_returns, cov_matrix, risk_free_rate)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(n_assets))
    result = minimize(neg_sharpe_ratio, n_assets * [1. / n_assets,], args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    portfolio_return = np.sum(mean_returns * weights)
    portfolio_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return -sharpe_ratio