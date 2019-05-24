import numpy as np 
from math import sin, cos, atan2

def RWGE(A):
	X,Y = np.gradient(A)
	out = np.zeros(A.shape)
	c = A.shape[0]//2

	for i in range(len(A)):
		for j in range(len(A[0])):
			x = i - c
			y = j - c
			out[i][j] = ( X[i][j]*cos(atan2(y,x)) + Y[i][j]*sin(atan2(y,x)) )**2

	return np.sum(out)
