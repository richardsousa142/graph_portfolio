# importar libraries
import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Definição do portfolio de mínima variância
def min_variance_portfolio(cov_matrix):
    n_assets = cov_matrix.shape[0]
    args = (cov_matrix,)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(n_assets))
    result = minimize(portfolio_variance, n_assets * [1. / n_assets,], args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

def portfolio_variance(weights, cov_matrix):
    return weights.T @ cov_matrix @ weights