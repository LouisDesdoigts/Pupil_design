import numpy as np
import math

def generate_pupil(fits_file):
    """
    Takes in the fits file and returns a complex array of the pupil
    """
    gridsize = fits_file.shape[0]
    c = gridsize//2
    pupil = np.zeros(fits_file.shape, dtype=complex)

    white = np.complex(1,0)
    black = -np.complex(1,0)

    for i in range(gridsize):
        for j in range(gridsize):
            x = i - c
            y = j - c 
            r = math.hypot(x, y)
            if r >= gridsize//2:
                pupil[i][j] = np.complex(0,0)
            else:
    #             pupil[i][j] = black if np.abs(np.angle(im[i][j])) > threshold else white
                pupil[i][j] = np.exp(1j*fits_file[i][j])
        
    return pupil