'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-16 20:27:47
@modify date 2022-02-16 20:45:55
@desc [Generate a tall matrix m x n of the form r.dddd and calc it's frobenius norm]
'''

from typing import List
import random
import math

def generate_random_entry() -> float:
    """[Returns a random number of the form r.dddd]

    Returns:
        float: A random number
    """

    digits = ""
    for i in range(5):
        dig = random.randint(0, 9)
        if i == 4: dig = random.randint(1, 9)
        digits = digits + str(dig)
        if i == 0: digits += "."
    return float(digits)

def create_random_matrix(m:int, n:int) -> List:
    """[Takes in the number of rows and columns and generates a matrix of size m x n]

    Args:
        m (int): Number of rows of the matrix
        n (int): Number of columns of the matrix

    Returns:
        List: A matrix as a list of lists
    """
    
    if m <= n:
        raise AssertionError("Requested matrix is square or wide; It must be tall. Please give m > n")
    
    A = []
    for i in range(m):
        ith_row = []
        for j in range(n):
            ith_row.append(generate_random_entry())
        A.append(ith_row)
    
    return A

def frob_norm(A: List) -> float:
    """[Takes in a matrix A and computes the frobenius norm of that matrix]

    Args:
        A (List): A matrix represented as List of Lists

    Returns:
        float: The frobenius norm of the matrix
    """
    
    if len(A) == 0:
        raise AssertionError("Empty matrix passed. Pass a finite matrix")

    fro_norm = 0.0

    for row in A:
        for element in row:
            fro_norm += element * element
    
    fro_norm = math.sqrt(fro_norm)
    return fro_norm        