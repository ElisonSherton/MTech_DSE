'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-12-05 18:47:07
@modify date 2021-12-06 22:05:59
@desc [Generate iteration matrix for Gauss Jacobi solution of AX = b]
'''
import copy
import numpy as np
from typing import List

def get_iteration_matrix(input_matrix: np.array) -> List:
    """[Given an input matrix, computes the iteration matrix and returns the same]

    Args:
        input_matrix (np.array): [A nxn square matrix]

    Returns:
        List: [The iteration matrix and the norms of the same]
    """
    
    nr, nc = input_matrix.shape
    
    # Make sure the matrix is a square matrix with a b column
    assert nr == nc

    # Create a copy of the input matrix and initialize L and U to be zero matrices
    output_matrix = copy.deepcopy(input_matrix)
    L, U = np.zeros((nr, nc)), np.zeros((nr, nc))
    
    # Iterate over all the rows and express A = I + L + U
    for r in range(nr):
        # Unify the diagonal (i.e. make all the diagonal elements 1)
        output_matrix[r, :] = output_matrix[r, :] / input_matrix[r, r]
        L[r, :r] = output_matrix[r, :r]
        U[r, (r + 1):] = output_matrix[r, (r + 1):]
    
    iteration_matrix = -1.0 * (L + U)
    l1 = np.linalg.norm(iteration_matrix, ord = 1)
    fro = np.linalg.norm(iteration_matrix, ord = 'fro')
    inf = np.linalg.norm(iteration_matrix, ord = np.inf)
    
    return (iteration_matrix, [l1, fro, inf])

# Create a random matrix of integers (then cast as float)
A = np.random.randint(low = 1, high = 5, size = (4, 4)).astype(np.float)
iteration_matrix, norms = get_iteration_matrix(A)

# Print all the matrices obtained in between and their norms
print(f"Original Matrix:\n{np.around(A, 4)}")
print(f"Iteration Matrix i.e. -D-1(L + U):\n{np.around(iteration_matrix, 4)}")
print(f"l1   norm: {norms[0]:.3f}")
print(f"frob norm: {norms[1]:.3f}")
print(f"linf norm: {norms[2]:.3f}")