from functools import partial
from ..matrix_manipulation.submatrix import get_submatrix_r, get_submatrix_sigma
import numpy as np
from .generate_w import gerar_w_valido

def sharpe_ratio(w, r, sigma, ctes=None, risk_free_rate=0.0):
    """
    Calculate the Sharpe ratio for a portfolio.
    
    Parameters:
    - w: weights array of shape (n_assets,)
    - r: returns matrix of shape (n_days, n_assets)
    - sigma: covariance matrix of shape (n_assets, n_assets)
    - ctes: annualization factor (default: None)
    - risk_free_rate: risk-free rate (default: 0.0)
    
    Returns:
    - Sharpe ratio
    """
    # Calculate portfolio expected return (annualized)
    port_return = np.dot(r, w).mean()
    
    # Calculate portfolio volatility (standard deviation)
    port_vol = np.sqrt(np.dot(np.dot(w.T, sigma), w))
    
    # Calculate Sharpe ratio
    sharpe = (port_return - risk_free_rate) / port_vol
    
    # Apply annualization if provided
    if ctes is not None:
        sharpe = sharpe * ctes
        
    return sharpe

def calcular_n_sharpes_da_carteira(indices_carteira, r, sigma, n=1000):
    """
    Calcula n Sharpe Ratios para uma carteira com os indices passados
    """
    # Check dimensions to make sure they match
    r_sub = get_submatrix_r(r, indices_carteira)
    sigma_sub = get_submatrix_sigma(sigma, indices_carteira)
    
    # Default annualization - assumes daily returns and 252 trading days
    # Multiply returns by 252 and volatility by sqrt(252)
    annualization = 252 / np.sqrt(252)
    
    calculate_sr_with_w = partial(sharpe_ratio, r=r_sub, sigma=sigma_sub, ctes=annualization)
    
    # Generate random portfolios
    w_vectors = [gerar_w_valido(len(indices_carteira)) for _ in range(n)]
    sharpes = list(map(calculate_sr_with_w, w_vectors))
    
    max_sharpe = max(sharpes)
    max_index = sharpes.index(max_sharpe)
    return max_sharpe, w_vectors[max_index]