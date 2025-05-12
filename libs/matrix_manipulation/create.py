import pandas as pd
import numpy as np

def calculate_matrix_of_percentual_change(df : pd.DataFrame) -> np.ndarray:
    """
    Calculate the percentual change of each column in the DataFrame.
    """
    return df.pct_change().iloc[1:].to_numpy()

def calculate_matrix_of_volatility(matrix : np.ndarray) -> np.ndarray:
    """
    Calculate the volatility of each column in the matrix.
    """
    return np.cov(matrix, rowvar=False)

