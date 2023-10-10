import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
from time import time

#  Define a system of linear equations. A  is the coefficient matrix and b is the vector of knowns
#  We are using the same matrix as above
A = np.array([[3, 1, -3],
              [-1, 3, 2],
              [2, 1, -3],
              ])
b = np.array([-1,12,0])
b.shape = (3, 1)

#  Do the matrix factorization.  In our case, the permutation matrix P is the identity
P, L, U = lu(A)

print('The L matrix is:')
print(L)
print()
print('The U matrix is:')
print(U)

#  Show the A = PLA
np.allclose(L @ U, A)

#  Do the factorization
LU, p = lu_factor(A)

#  Solve the system
x1 = lu_solve((LU, p), b)
print(x1)

#  Does this give the same results as linalg.solve?
np.allclose(x1, np.linalg.solve(A, b))

#  Set a constant seed so we can reproduce our results
np.random.seed(2)

#  Set number of equations
N = 500

#  Generate A matrix
A = np.random.normal( size = (N, N) )

#  make b vector
b = np.random.normal( size = (N, ))

start = time()
for i in range(10000):
    x1 = np.linalg.solve(A, b)
print('Time = ', time() - start)

start = time()

lu, piv = lu_factor(A)
for i in range(10000):
    x2 = lu_solve((lu, piv), b)

print('Time = ', time() - start)

np.allclose(x1, x2)
