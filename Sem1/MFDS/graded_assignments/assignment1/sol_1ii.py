'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-29 21:01:55
@modify date 2021-11-30 21:14:04
@desc [Gauss Elimination with and without partial pivoting ]
'''

import math
from typing import List

def pivot(a: List, k:int) -> List:
    """A function to perform partial pivoting for an array

    Args:
        a (List): [The input matrix as a list of lists]
        k (int): [Which row index to pivot]

    Returns:
        List: [Matrix after partial pivoting]
    """

    interested_col = []

    n = len(a) # Number of rows
    for idx in range(k, n):
        interested_col.append(a[idx][k])
    
    pivot_row_position = interested_col.index(max(interested_col)) + k

    a[k], a[pivot_row_position] = a[pivot_row_position], a[k]
    return a

def custom_round(a: float, sig_dig:int = 5) -> float:
    """[Takes an array and keeps only sig_dig digits in the array elements]

    Args:
        a (float): [A floating point number]
        sig_dig (int, optional): [Number of significant digits to which to round to]. Defaults to 5.

    Returns:
        float: [Number rounded to sig_dig significant digits]
    """

    if a != 0.0:
        to_round_to = int(math.floor(math.log10(abs(a))))
        rounded_number =  round(a, sig_dig - to_round_to - 1)
    else:
        rounded_number = float('0.' + '0' * (sig_dig - 1))
    return rounded_number

def forward_elimination(a: List,  sig_dig:int = 10, print_progress:bool = True,
                        pivot_flag: bool = False) -> List:
    """Takes in a matrix and reduces it to an upper triangular matrix using forward elimination

    Args:
        a (List): [Input matrix]
        sig_dig (int): [How many significant digits to consider]
        pivot_flag (bool): [Whether or not to pivot the rows when reducing them]
        print_progress (bool): [Whether or not to print the number of primitive operations]
        
    Returns:
        List: [REF of the given matrix]
    """
    # Create a copy of a and get it's dimensionality
    nr = len(a)
    nc = nr + 1

    # Pivot if the argument for pivoting is True
    if pivot_flag: a = pivot(a, 0)

    divisions, multiplications, additions = 0, 0, 0

    # Iterate for all rows
    for r in range(1, nr):
        
        # Make all the elements below leading diagonal zeros
        for r_inner in range(r, nr):
            # Create a substitute row and initialize it to all zeros as a placeholder 
            # for the row transformation operation
            substitute_row = [0.0] * (nc)
            scale_factor = a[r_inner][r - 1] / a[r - 1][r - 1]
            divisions += 1
            
            for idx in range(r, nc):    
                substitute_row[idx] = a[r_inner][idx] -  scale_factor * a[r - 1][idx]
                
                # Round each entry to sig_dig number of significant digits
                substitute_row[idx] = custom_round(substitute_row[idx], sig_dig)
                
                # Add one multiplication and addition each for every element update
                multiplications += 1
                additions += 1
            
            a[r_inner] = substitute_row
        if pivot_flag: a = pivot(a, r)
    
    if print_progress:
        print(f"Forward Elimination\n#Additions: {additions:10d}\t#Multiplications: {multiplications:10d}\t#Divisions{divisions:10d}")
    return a


# Backward substitution
def back_substitution(a: List, print_progress:bool = True, sig_dig:int = 5) -> List:
    """Takes in an array in row reduced echelon form and performs back substitution for getting the solution to the system of linear equations

    Args:
        fw_a (List): [Row reduced array (REF) of augmented matrix of a system of linear equations]
        print_progress (bool): [Whether to print the number of additions, multiplications, divisions or not]
        sig_dig (bool): [The number of significant digits to consider when carrying out the arithmetic operations]

    Returns:
        List: [Solution]
    """
    nr = len(a)
    
    # Initialize all the solutions to be zeros
    solutions = [0.] * nr
    divisions, additions, multiplications = 0, 0, 0

    # Start from last row and go upto the first
    for r in range(nr - 1, -1, -1):  
        
        # Compute the sum of product of columns on LHS
        dp = 0.0
        for idx in range(r, nr):    
            dp = dp + custom_round(a[r][idx] * solutions[idx], sig_dig)
            additions = additions + 1
            multiplications = multiplications + 1
            
        # Compute the rhs
        rhs = custom_round(a[r][nr] - dp, sig_dig)
        # Find the rth element of the solutions array
        solutions[r] = custom_round(rhs / a[r][r], sig_dig)
        divisions += 1
        
    if print_progress:
        print(f"Backward Substitution\n#Additions: {additions:10d}\t#Multiplications: {multiplications:10d}\t#Divisions{divisions:10d}")
    return solutions

a = [[0.,2.,0.,1.,0.],[2.,2.,3.,2.,-2.],[4.,-3.,0.,1.,-7.], [6.,1.,-6.,-5.,6.]]

# Solve the system of equations
print("Solution", back_substitution(forward_elimination(a, pivot_flag=True, sig_dig = 6), sig_dig = 6), sep = "\n")