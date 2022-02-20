'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-19 21:04:01
@modify date 2022-02-20 08:57:45
@desc [Gram Schmidt Orthogonalization Method]
'''

from qn_12 import *

def inner_product(v1:List, v2:List) -> Tuple:
    """Given two vectors v1 and v2, computes their inner product

    Args:
        v1 (List): [A vector represented as a list]
        v2 (List): [A vector represented as a list]

    Returns:
        Tuple: [A tuple of the inner product & number of additions, multiplications and divisions needed for performing the inner product]
    """
    
    additions, multiplications, divisions = -1, 0, 0
    
    dot_product = 0.0
    for e1, e2 in zip(v1, v2):
        dot_product += e1 * e2
        additions += 1; multiplications += 1
    
    return (dot_product, (additions, multiplications, divisions))

def vector_addition(v1:List, v2:List) -> Tuple:
    """[Given two vectors, adds them and computes the number of +, -, / needed for the same]

    Args:
        v1 (List): [A vector represented as a list]
        v2 (List): [A vector represented as a list]

    Returns:
        Tuple: [A tuple representing vector subtraction result and the number of +, -, / needed to compute the result]
    """
    
    additions, multiplications, divisions = 0, 0, 0
    resultant = []
    
    for e1, e2 in zip(v1, v2):
        resultant.append(e1 + e2)
        additions += 1
    
    return (resultant, (additions, multiplications, divisions))

def scalar_multiplication(v1:List, k: float) -> Tuple:
    """[Given a vector and a scalar, scales the vector appropriately]

    Args:
        v1 (List): [A vector represented as a list]
        k (float): [A scalar]

    Returns:
        Tuple: [A tuple representing scalar multiplication result and the number of +, -, / needed to compute the result]
    """
    
    additions, multiplications, divisions = 0, 0, 0
    resultant = []
    
    for e1 in v1:
        resultant.append(k * e1)
        multiplications += 1
    
    return (resultant, (additions, multiplications, divisions))
    

def gram_schmidt_orthogonalization(A: List) -> Tuple:
    """[Given a matrix A, checks if it's columns are Linearly Independent and if yes, generates an orthogonal matrix from the same]

    Args:
        A (List): [Matrix represented as list of lists]

    Returns:
        Tuple: (A tuple representing whether A contains linearly independent columns and if yes, an orthogonal matrix generated from A)
    """
    
    A_columns = []
    
    # Get the number of rows and columns of A
    nr, nc = len(A), len(A[0])

    # Get a list of the columns of A
    for c in range(nc):
        col = []
        for r in range(nr):
            col.append(A[r][c])
        A_columns.append(col)
    
    _ , dec = rreduce(A)
    
    # If A is not full rank, then return that the matrix is non-orthogonalizable
    if not dec:
        return (False, [])

    # Start generating an orthogonal basis for A
    v = []
    vi_inner_product = []

    additions, multiplications, divisions = 0, 0, 0
    
    # Iterate over the columns of A
    for n in range(nc):

        xi = A_columns[n]
        vi = xi
        
        # Iteratively find vi = xi - summation of components of xi in previous vi-1 
        for it in range(n):
            
            # Compute xi.vi inner product
            xivi, (a, m, d) = inner_product(xi, v[it])
            additions += a; multiplications += m; divisions += d
            
            # Check if vi's inner product exists 
            # If it is computed previously, just access it
            # Otherwise, compute vi.vi 
            if it < (len(vi_inner_product)):
                vivi = vi_inner_product[it]
            else:
                vivi, (a, m, d) = inner_product(v[-1], v[-1])
                additions += a; multiplications += m; divisions += d
                vi_inner_product.append(vivi)
            
            # Compute the scaling factor for a vector
            scaling_factor = -1 * xivi / vivi
            divisions += 1
            
            # Scale the vector with the scaling factor
            scaled_vector, (a, m, d) = scalar_multiplication(v[it], scaling_factor)
            additions += a; multiplications += m; divisions += d

            # Accumulate the component into this vi
            vi, (a, m, d) = vector_addition(vi, scaled_vector)
            additions += a; multiplications += m; divisions += d
        
        v.append(vi)
    
    # Reframe the matrix in row major order
    O = []
    
    for r in range(nr):
        col = []
        for c in range(nc):
            col.append(v[c][r])
        O.append(col)
    
    return (O, (additions, multiplications, divisions))

A = create_random_matrix(5, 4)
print(gram_schmidt_orthogonalization(A))