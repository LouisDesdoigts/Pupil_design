import numpy as np
import math as m

# How to handle positions outside of the radius

def create_symmetry(A, f):
    # A is array to create symmetry with
    # f is the number of rotations

    rows = A.shape[0]
    cols = A.shape[1]
    c = rows//2
    B = np.zeros((rows, cols)) 
    alpha = 2*np.pi/f 

    # Iterate over each entry in the array
    for i in range(rows):
        for j in range(cols):
            y = c - i
            x = c - j
            # Only perform operation on pixels within the radius
            if m.hypot(x, y) <= c:
                for k in range(f):
                    x, y = calculate_new(x, y, alpha)
                    B[i][j] += A[i][j]/j
                # Binarization here

    return B

def calculate_new(x, y, alpha):
    # alpha in radians please!
    r = m.hypot(x, y)
    phi = m.atan2(y, x)

    try:
        X = round(r * m.sin(phi + alpha) * (1/m.tan(phi + alpha)))
    except ZeroDivisionError:
        print(phi, alpha)
    Y = round(r * m.cos(phi + alpha) * m.tan(phi + alpha))

    return X, Y

A = np.zeros((10,10))
A[3][3] = 10
B = create_symmetry(A, 4)

