import numpy as np

# Definição do portfolio de pesos iguais
def equal_weighted_portfolio(n_assets):
    return np.ones(n_assets) / n_assets