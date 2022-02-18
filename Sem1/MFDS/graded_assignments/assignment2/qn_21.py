'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-18 09:23:43
@modify date 2022-02-18 21:58:29
@desc [Gradient Descent Algorithm generate the problem]
'''

from qn_11 import *

def generate_matrix() -> List:
    """[Creates a matrix of the size n1n2 * n3n4]

    Returns:
        List: A matrix in the form of a list
    """

    # Prompt the user for his mobile number

    # Ascertain the mobile number is valid
    number = input("Enter your phone number:\n")
    try:
        _ = int(number)
        if len(number.strip()) > 10:
            raise AssertionError("Mobile number cannot have more than 10 digits")
    except Exception as e:
        print("{str(e)}\nEntered number invalid. Please enter a valid number")
    
    # Get the last 4 digits of the number and replace
    # 0s in the number with 3s
    rc = number.strip()[-4:]
    rc = rc.replace("0", "3")

    nr, nc = int(rc[:2]), int(rc[2:])
    matrix = create_random_matrix(nr, nc, wide = True)
    b = create_random_matrix(nr, 1, wide = True)

    return (matrix, b)

def linf_norm(matrix: List) -> float:
    """[Given a matrix computes it's linfinity norm]

    Args:
        matrix (List): [Matrix represented as a list of numbers]

    Returns:
        float: The infinity norm of the said matrix
    """
    
    inf_norm = 0

    # For each row in the matrix
    for row in matrix:
        rsum = 0

        # Compute the row sum of absolute vals of elements in that row
        for element in row:
            rsum += abs(element)

        # Store the largest row sum
        if rsum > inf_norm:
            inf_norm = rsum
    return inf_norm