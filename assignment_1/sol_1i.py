'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-14 17:45:44
@modify date 2021-11-14 21:54:25
@desc [Implementing Gauss Elimination method with partial pivoting]
'''

import copy
import numpy as np

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


def forward_elimination(a: np.array,  pivot_flag: bool = False) -> np.array:
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

    # Pivot if the argument for pivoting is True
    if pivot_flag: a = pivot(a, 0)

    # Iterate for all rows
    for r in range(1, nr):
        
        # Make all the elements below leading diagonal zeros
        for r_inner in range(r, nr):
            a[r_inner, :] = a[r_inner, :] -  (a[r_inner, r-1] / a[r-1, r-1])* a[r - 1, :]
            
        if pivot_flag: a = pivot(a, r)
    return a

a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype = np.float64)

# Without pivoting
print(a, forward_elimination(a), sep = "\n") 

# With pivoting
print(a, forward_elimination(a, pivot_flag=True), sep = "\n")