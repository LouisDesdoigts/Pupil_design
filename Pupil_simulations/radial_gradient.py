import numpy as np 
from math import sin, cos, atan2, hypot

def RWGE(A, max=-1):
    X,Y = np.gradient(A)
    out = np.zeros(A.shape)
    c = A.shape[0]//2

    for i in range(len(A)):
        for j in range(len(A[0])):
            x = i - c
            y = j - c
            r = hypot(x, y)
            
            if max != -1 and r > max:
                out[i][j] = 0
            else:
                out[i][j] = ( X[i][j]*cos(atan2(y,x)) + Y[i][j]*sin(atan2(y,x)) )**2

    return np.sum(out)

def gaussian(x, y, mu, sig):
    a = 1 / (sig * np.sqrt(2 * np.pi)) 
    b = ((x-mu)**2)/(2*sig**2)
    c = ((y-mu)**2)/(2*sig**2)
    g_out = a*np.exp(-(b+c))
    return g_out

if __name__ == "__main__":
    s = 10
    c = s//2
    A = np.zeros((s, s))

    for i in range(len(A)):
        for j in range(len(A[0])):
            x = i - c
            y = j - c
            A[i][j] = gaussian(x, y, 0, 1)

    print(RWGE(A))

