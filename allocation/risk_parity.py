import numpy as np

# Definição do portfolio de paridade de riscos
def risk_parity_portfolio(cov_matrix):
    inv_vol = 1 / np.sqrt(np.diag(cov_matrix))
    weights = inv_vol / np.sum(inv_vol)
    return weights