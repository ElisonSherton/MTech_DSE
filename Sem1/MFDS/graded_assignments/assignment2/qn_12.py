'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-16 20:47:43
@modify date 2022-02-16 22:39:03
@desc [Find if GS Algorithm can be applied to the columns of a matrix A]
'''

from qn_11 import *
from typing import Tuple
import copy

def rreduce(A:List, threshold:float = 1e-6) -> Tuple:
    """[Given a matrix A as a list of lists, compute it's row reduced echelon form.
    Return that along with the rank of the matrix]

    Args:
        A (List): A m x n tall matrix
        threshold (float, optional): When comparing the pivot elements, what magnitude of a value counts as zero magnitufe. Defaults to 1e-6.

    Returns:
        Tuple: A tuple of row reduced echelon form and the decision i.e. whether
        the matrix has linearly independent columns or not
    """
    # Create a copy of the original matrix
    A = copy.deepcopy(A)
            
    # Find out number of rows and columns
    nr, nc = len(A), len(A[0])            
    
    # Get Echelon form using row reduction (Only iterate for as many times as columns since tall matrix can't have more pivot elements than number of columns)
    for i in range(nc - 1):
        
        pivot_element = A[i][i]
        # TODO: Handle pivot = zero
        
        # Make all the elements below the pivot to be zero
        # in an iterative manner
        for j in range(i + 1, nr):
                        
            div_factor = A[j][i] / pivot_element     
            
            transformed_row = []
            for idx, element in enumerate(A[j]):
                transformed_element = element - div_factor * A[i][idx]
                if idx == i: transformed_element = 0.0
                transformed_row.append(transformed_element)
            
            A[j] = transformed_row
    
    # Check the leading diagonal entries;
    # If a few of them are zeros or near zeros,
    # then given matrix is not a full rank matrix
    full_rank = True
    for i in range(nc):
        if abs(A[i][i]) <= threshold:
            full_rank = False
            break
                    
    return (A, full_rank)