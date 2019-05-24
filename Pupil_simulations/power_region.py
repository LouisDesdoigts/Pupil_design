import numpy as np
from math import hypot

def power_ratio(A, radius):
    """
    Assumes square inputs
    """
    
    gridsize = A.shape[0]
    c = gridsize//2
    inner = 0
    
    for i in range(gridsize):
        for j in range(gridsize):
            x = i - c
            y = j - c
            r = hypot(x, y)
            if r < radius:
                inner += A[i][j]
                
    inner_percentage = inner/np.sum(A)
    return inner_percentage

