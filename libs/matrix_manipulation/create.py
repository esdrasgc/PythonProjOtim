import pandas as pd
import numpy as np

def calculate_matrix_of_percentual_change(df : pd.DataFrame) -> np.ndarray:
    """
    Calculate the percentual change of each column in the DataFrame.
    
    Parameters:
    - df: DataFrame with price data
    
    Returns:
    - numpy array of shape (n_days-1, n_assets) with percentage changes
    """
    # Use pct_change to calculate returns and drop NaN values
    return df.pct_change().dropna().to_numpy()

def calculate_matrix_of_volatility(matrix : np.ndarray) -> np.ndarray:
    """
    Calculate the covariance matrix from returns.
    
    Parameters:
    - matrix: returns matrix of shape (n_days, n_assets)
    
    Returns:
    - covariance matrix of shape (n_assets, n_assets)
    """
    # Transpose if necessary - covariance expects variables in columns
    if matrix.shape[0] < matrix.shape[1]:
        print("Warning: Matrix appears to have more assets than days. Check orientation.")
    
    return np.cov(matrix, rowvar=False)  # rowvar=False specifies that variables are in columns

