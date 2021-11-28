'''
@author Vinayak
@email nayakvinayak95@gmail.com
@create date 2021-11-25 18:41:40
@modify date 2021-11-26 09:44:32
@desc [Perform dolittle LU decomposition using Gauss Elimination Technique]
'''

import numpy as np
import copy
def pivot(a: np.array, k:int) -> np.array:
    """A function to perform partial pivoting for an array

    Args:
        a (np.array): [The input array]
        k (int): [Which row index to pivot]

    Returns:
        np.array: [Array after partial pivoting]
    """
    a = copy.copy(a)
    interested_col = a[k:, k]
    pivot_row_position = interested_col.argmax() + k

    # Due to numpy's pointer referencing of arrays, we can't do a, b = b, a as we do in standard python to 
    # reverse rows
    temp = copy.copy(a[k])
    a[k] = copy.copy(a[pivot_row_position])
    a[pivot_row_position] = temp
    return a


def decompose(a: np.array,  pivot_flag: bool = False) -> np.array:
    """Takes in an array and reduces it to an upper triangular matrix using forward elimination

    Args:
        a (np.array): [Input array]
        pivot_flag (bool): [Whether or not to pivot the rows when reducing them]

    Returns:
        np.array: [REF of the given array]
    """
    # Create a copy of a and get it's dimensionality
    a = copy.copy(a)
    nr, _ = a.shape

    # Initialize the lower triangular L matrix with identity matrix
    L = np.eye(nr)    

    # Pivot if the argument for pivoting is True
    if pivot_flag: a = pivot(a, 0)

    # Iterate for all rows
    for r in range(1, nr):
        
        # Make all the elements below leading diagonal zeros
        for r_inner in range(r, nr):
            L[r_inner, r - 1] = a[r_inner, r-1] / a[r-1, r-1]
            a[r_inner, :] = a[r_inner, :] -  (a[r_inner, r-1] / a[r-1, r-1])* a[r - 1, :]
        if pivot_flag: 
            a = pivot(a, r)
    return (a, L)

a = np.array([[0,2,0,1],[2,2,3,2],[4,-3,0,1], [6,1,-6,-5]], dtype = np.float64)

def dot_product(a1:np.array, a2:np.array) -> object:
    """Takes two numpy vectors, computes their dot product and returns the same

    Args:
        a1 (np.array): [A vector]
        a2 (np.array): [A vector]

    Returns:
        object: [Dot product of vectors]
    """
    n = len(a1)
    dp = 0.0
    for i in range(n):
        dp += a1[i] * a2[i]
    return dp

U, L = decompose(a, pivot_flag = True)

print("a", a, sep = "\n")
print("U", U, sep = "\n")
print("L", L, sep = "\n")
print("L matrixmult U", L @ U, sep = "\n")
