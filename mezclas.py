import numpy as np

def mezclar_filas_numpy(array):
    np.random.shuffle(array)
    return array

print(mezclar_filas_numpy(np.array([[2, 1, -3], [-1, 3, 2], [3, 1, -3]])))
