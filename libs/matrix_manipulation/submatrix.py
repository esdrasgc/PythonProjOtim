import numpy as np

def get_submatrix_r(r, indices):
    return r[:, indices]

def get_submatrix_sigma(sigma, indices):
    return sigma[np.ix_(indices, indices)]