'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-12-05 15:57:37
@modify date 2021-12-05 17:00:13
@desc [Using GE to check runtimes for different values of n]
'''

from sol_1ii import *
import random, time

def get_random_number(ldecimal: int = 1, rdecimal: int = 4) -> float:
    """[Given the number of digits to the left and right of a floating point number, generates a random floating point number]

    Args:
        ldecimal (int, optional): [Number of digits to the left of the decimal]. Defaults to 1.
        rdecimal (int, optional): [Number of digits to the right of the decimal]. Defaults to 4.

    Returns:
        float: [A floating point number]
    """
    number = ''
    for i in range(ldecimal):
        number += str(random.randint(1, 9))   # I want to avoid 0s because when it comes to solving without partial pivoting if first row first column (or any diagonal element for that matter) is 0, then everything will go out for a toss
    number += "."
    for i in range(rdecimal):
        number += str(random.randint(0, 9))
    number = float(number)
    return number

def get_matrix(nr: int, nc:int) -> List:
    """[Given the number of rows and number of columns of a matrix, generates an nr x nc matrix]

    Args:
        nr (int): [Number of rows of the matrix]
        nc (int): [Number of columns of the matrix]

    Returns:
        List: [A matrix as a list of lists]
    """
    matrix = []

    for i in range(nr):
        row = []
        for j in range(nc):
            row.append(get_random_number())
        matrix.append(row)
    
    return matrix

for N in range(100, 1001, 100):
    print(f"N = {N}")
    simulated_augmented_matrix = get_matrix(N, N + 1)
    start = time.time()
    back_substitution(forward_elimination(simulated_augmented_matrix, pivot_flag=True, sig_dig = 5), sig_dig = 5)
    end = time.time()
    print(f"Time taken: {end - start:.6f}")
