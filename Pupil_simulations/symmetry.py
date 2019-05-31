import numpy as np
from math import sin, cos, hypot, atan2

def create_symmetry(A, f, binarise=False):
    # A is array to create symmetry with
    # f is the number of rotations

    rows = A.shape[0]
    cols = A.shape[1]
    c = rows//2
    B = np.zeros((rows, cols)) 
    alpha = 2*np.pi/f 
    
    max_val = np.max(A)
    min_val = np.min(A)
    threshold = max_val/2

    # Iterate over each entry in the array
    for i in range(rows):
        for j in range(cols):
            x = i - c
            y = j - c
            r = hypot(x, y)
            theta = atan2(y, x)

            # Only perform operation on pixels within the radius
            if r <= c:
                for k in range(f):
                    theta_raw = theta - k*alpha
                    theta_new = theta_raw if theta_raw >= -np.pi else 2*np.pi + theta_raw
                    
                    x_new = round(r*cos(theta_new))
                    y_new = round(r*sin(theta_new))

                    k = x_new - c
                    l = y_new - c

                    B[i][j] += A[k][l]/f
                    
                # This doesn't seem to work - Returns the original pupil
                # Binarise the image, threshold is half the peak value across whole array
#                 if binarise:
#                     B[i][j] = max_val if B[i][j] >= threshold else min_val
                    
            else:
                continue
    return B


# A = np.zeros((15,15))
# A[3][3] = 10
# B = create_symmetry(A, 10)
# print(np.sum(B))
# print(A)
# print(B)

