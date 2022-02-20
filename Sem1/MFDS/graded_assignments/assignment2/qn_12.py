'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-16 20:47:43
@modify date 2022-02-20 15:34:52
@desc [Write a function to compute the REF of a given matrix A]
'''

from qn_11 import *
from typing import Tuple
import copy

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


def rreduce(A:List, threshold:float = 1e-6) -> Tuple:
    """[Given a matrix A as a list of lists, compute it's row reduced echelon form.
    Return that along with the rank of the matrix]

    Args:
        A (List): A m x n tall matrix
        threshold (float, optional): When comparing the pivot elements, what magnitude of a value counts as zero magnitude. Defaults to 1e-6.

    Returns:
        Tuple: A tuple of row reduced echelon form and the decision i.e. whether
        the matrix has linearly independent columns or not
    """
    
    # Initialize the number of additions, multiplications divisions to null
    a, m, d = 0, 0, 0
    
    # Create a copy of the original matrix otherwise original
    # matrix will get overwritten
    A = copy.deepcopy(A)
    
    # Check if the matrix is empty
    if len(A) == 0:
        return ([], False)
    if len(A[0]) == 0:
        return ([[]], False)
    
    # Find out number of rows and columns
    nr, nc = len(A), len(A[0])            
    
    # Get Echelon form using row reduction (Only iterate for as many times as columns since tall matrix can't have more pivot elements than number of columns)
    for i in range(nc - 1):
        
        pivot_element = A[i][i]
        
        # Make all the elements below the pivot to be zero
        # in an iterative manner
        for j in range(i + 1, nr):
            
            # Find the pivot element and compute the scaling factor
            div_factor = A[j][i] / pivot_element     
            d += 1
            
            # Scale the ith row based on the above factor
            scaled_vector, (add, mult, div) = scalar_multiplication(A[i], -1 * div_factor)
            a += add; m += mult; d += div
            
            # Subtract the scaled row from A[j]
            transformed_row, (add, mult, div) = vector_addition(A[j], scaled_vector)
            
            # Deduct the counts of add and mult by (i + 1) because when doing row reduction
            # We are computing pivots in such a way that the elements below the pivot
            # should become zeros and the elements to the left of the pivot
            # are already zeros, so no need to compute that term again and add it
            add -= (i + 1); mult -= (i + 1)
            a += add; m += mult; d += div
            
            A[j] = transformed_row
    
    # Check the leading diagonal entries;
    # If a few of them are zeros or near zeros,
    # then given matrix is not a full rank matrix
    full_rank = True
    for i in range(nc):
        if abs(A[i][i]) <= threshold:
            full_rank = False
            break
                    
    return (A, full_rank, (a, m, d))