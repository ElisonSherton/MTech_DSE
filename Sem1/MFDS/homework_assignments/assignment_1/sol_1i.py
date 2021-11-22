'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-14 17:45:44
@modify date 2021-11-15 19:30:25
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

a = np.array([[0,2,0,1,0],[2,2,3,2,-2],[4,-3,0,1,-7], [6,1,-6,-5,6]], dtype = np.float64)

# Without pivoting
print("Without Pivoting: ", a, forward_elimination(a), sep = "\n") 

# a = np.array([[0,2,0,1,0],[2,2,3,2,-2],[4,-3,0,1,-7], [6,1,-6,-5,6]], dtype = np.float64)

# With pivoting
print("With Pivoting: ", a, forward_elimination(a, pivot_flag=True), sep = "\n")

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

# Backward substitution
def back_substitution(fw_a: np.array) -> np.array:
    """Takes in an array in row reduced echelon form and performs back substitution for getting the solution to the system of linear equations

    Args:
        fw_a (np.array): [Row reduced array (REF) of augmented matrix of a system of linear equations]

    Returns:
        np.array: [Solution]
    """
    a = copy.copy(fw_a)
    nr, _ = a.shape
    
    # Initialize all the solutions to be zeros
    solutions = np.zeros(nr)

    # Start from last row and go upto the first
    for r in range(nr - 1, -1, -1):  
        # Compute the dot product of the rth row and the solutions column
        dp = dot_product(a[r, :-1], solutions)
        # Compute the rhs
        rhs = fw_a[r, nr] - dp
        # Find the rth element of the solutions array
        solutions[r] = rhs / a[r, r]
 
    return solutions

# Solve the system of equations
print("Solution", back_substitution(forward_elimination(a, pivot_flag=True)), sep = "\n")