'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-19 22:30:28
@modify date 2022-02-20 09:15:33
@desc [Find QR decomposition of a matrix A]
'''

from qn_13 import *
def matrix_multiplication(A:List, B:List) -> Tuple:
    """[Given two matrices as list of lists, computes their matrix product]

    Args:
        A (List): [A matrix of dimension m x n]
        B (List): [A matrix of dimension n x m]

    Returns:
        List: [A tuple of Matrix product as a list of lists and the number of additions, multiplications and divisions needed for performing the operation]
    """

    a, m, d = 0, 0, 0

    nrA, ncA = len(A), len(A[0])
    nrB, ncB = len(B), len(B[0])

    if ncA != nrB:
        print("Matrix dimension mismatch, please input valid matrices")
        return ([], (a, m, d))
    
    B_columns = []
    # Get a list of the columns of B
    for c in range(ncB):
        col = []
        for r in range(nrB):
            col.append(B[r][c])
        B_columns.append(col)
    
    resultant_matrix = []
    
    # Iteratively multiply rows of A and columns of B in order to 
    # Compute the product A matmul B
    for row in A:
        resultant_row = []
        for column in B_columns:
            abij, (add, mult, div) = inner_product(row, column)
            a += add; m += mult; d += div
            resultant_row.append(abij)
        resultant_matrix.append(resultant_row)
    
    return (resultant_matrix, (a, m, d))

def matrix_transpose(A:List) -> List:
    """[Given a matrix A, generate it's transpose]

    Args:
        A (List): [A matrix represented as list of lists]

    Returns:
        List: [Transpose of the matrix represented as list of lists]
    """
    
    # Find the rows and columns of A
    nr, nc = len(A), len(A[0])
    
    # Create a container for A_transpose
    A_transpose = []

    # Compute the transpose of A
    for c in range(nc):
        col = []
        for r in range(nr):
            col.append(A[r][c])
        A_transpose.append(col)
    
    return A_transpose

def normalize_columns(A: List) -> Tuple:
    """[Given a matrix A, normalizes it's columns using l2-norm and returns the normalized matrix as a List of lists and also the number of +, -, /, sqrt needed for computing the result]

    Args:
        A (List): [Matrix represented as list of lists]

    Returns:
        Tuple: [A tuple of the normalized matrix and the count of +,-,/ needed for generating the matrix]
    """
    
    # Initialize the number of additions, multiplications, divisions to zero
    a, m, d, root = 0, 0, 0, 0

    # If given matrix is a null matrix, return a null matrix
    if len(A) == 0:
        return ([], (a, m, d))
    if len(A[0]) == 0:
        return ([[]], (a, m, d))

    # Find the number of rows and columns of matrix A
    nr, nc = len(A), len(A[0])

    # First get the columns of A from A matrix
    A_columns = []
    A_columns = matrix_transpose(A)
    
    # Compute the normed column matrix now
    normalizedA = []

    for col in A_columns:
        
        dot_product, (add, mult, div) = inner_product(col, col)
        a += add; m+= mult; d += div
        
        l2norm = (dot_product) ** 0.5
        root += 1
        scaling_factor = 1 / l2norm
        
        scaled_vector, (add, mult, div) = scalar_multiplication(col, scaling_factor)
        # Since I have considered division ads multiplication with reciprocal here,
        # I am adding the scaling multiplications to division count here
        d += mult
        
        normalizedA.append(scaled_vector)
    
    # Get the matrix A in row major order again
    normedARowMajor = matrix_transpose(normalizedA)   

    return (normedARowMajor, (a, m, d, root))    