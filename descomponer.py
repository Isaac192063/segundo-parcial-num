import numpy as np

N = 3


matrizTrabajar = np.array([
    [2, 1, -3],
    [-1, 3, 2],
    [3, 1, -3]
])
matriz_u = np.zeros([N,N])
matriz_L = np.zeros([N,N])
print(matrizTrabajar)

for f in range(N):
    for c in range(N):
        matriz_u[f,c] = float(matrizTrabajar[f,c])

for f in range(N):
    for c in range(N):
        if f == c:
            matriz_L[f,c] = 1

        if f < c:
            factor = matrizTrabajar[c,f] / matrizTrabajar[f,f]
            matriz_L[c,f] = factor
            for k in range(N):
                matrizTrabajar[c,k]
            

print("matriz U",matriz_u)
print("matriz L",matriz_L)