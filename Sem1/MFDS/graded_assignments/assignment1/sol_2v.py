'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-12-06 21:54:41
@modify date 2021-12-06 22:05:38
@desc [Gauss Jacobi way to solve a system of linear equations Ax = b]
'''

import copy
import numpy as np

def solve(input_matrix: np.array, 
          iterations: int = 20) -> np.array:
    """[Given an input matrix, computes the iteration matrix and returns the same]

    Args:
        input_matrix (np.array): [A nxn square matrix]
        iterations (int): [How many iterations of the algorithm to perform]

    Returns:
        np.array: [A stacked array of solutions for the given system of equations]
    """
    
    nr, nc = input_matrix.shape
    
    # Make sure the matrix is a square matrix with one column for the RHS i.e. b
    assert (nr + 1) == nc

    A = input_matrix[:, :-1]
    b = input_matrix[:, -1]
    
    # Create a copy of the input matrix and initialize L and U to be zero matrices
    output_matrix = copy.deepcopy(A)
    L, U = np.zeros((nr, nr)), np.zeros((nr, nr))
    
    # Iterate over all the rows and express A = I + L + U
    for r in range(nr):
        output_matrix[r, :] = output_matrix[r, :] / input_matrix[r, r]
        b[r] = b[r] / input_matrix[r, r]
        L[r, :r] = output_matrix[r, :r]
        U[r, (r + 1):] = output_matrix[r, (r + 1):]
    
    # Create a container to hold all the solutions at different time-steps
    sols = []

    # Start from all 0s as the initial solution
    solution = np.zeros(nr)
    sols.append(solution)

    for it in range(iterations):
        solution = -L @ solution -U @ solution + b
        sols.append(solution)
    
    sols = np.array(sols)
    return sols        

# Create a random matrix of integers (then cast as float)
A = np.random.randint(low = 1, high = 20, size = (4, 5)).astype(np.float)
# A = np.array([[6.185,-2.125, 1.121, 1.23, 11.432], 
#               [-2.357, 7.240, 2.315, 2.104, 5.321], 
#               [1.547, 2.452, -6.142, 1.333, -1.478], 
#               [2.64, 0.150, 1.347, 6.978, 15.784]])

# Print all the matrices obtained in between and their norms
print(f"Original Matrix:\n{np.around(A, 5)}")
sols = solve(A)
print(f"Solutions:\n{sols}")
