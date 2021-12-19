'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-12-05 17:54:16
@modify date 2021-12-06 22:14:49
@desc [Write a function to check if a given SQUARE matrix is diagonally dominant or not, if not, then indicate if it could be converted into a diagonally dominant matrix]

Algorithm:
1. Find the maximum in each row.
2. If any row has multiple maxes, it can never be DD
3. If the maxima in any row are in the same col, it can never be DD
4. If the sum of all elements except the maxima elements in any one row exceeds the maxima element, then it can never be DD.
5. If all checks have passed above, and it is not DD, then we can make the matrix DD

Algorithm Credit:
https://www.mathworks.com/matlabcentral/answers/511902-making-a-matrix-strictly-diagonally-dominant#answer_421082
'''

from typing import List, Tuple

def check_row(matrix: List) -> Tuple:
    """[Given a square matrix, check the rowwise sums, if any row has multiple maxes, it can never be a DD matrix]

    Args:
        matrix (List): [A list of lists]

    Returns:
        Tuple: [A tuple of two elements - A list of max indices, A boolean which has checked if any row has two maxes]
    """

    # Initialize an empty container for the max indices
    max_indices = []

    # Initialize a Flag which indicates if the matrix could be diagonally dominant
    DD_flag = True
    
    for row in matrix:
        # Get the max element of the row
        r_max = max(row)
        
        # Check for the columns which have the max element
        temp = []
        for idx, element in enumerate(row):
            if element == r_max:
                temp.append(idx)
        
        # If there's more than one max per row, then it can never be a DD matrix
        if len(temp) > 1:
            DD_flag = False
            break
        
        max_indices.append(temp[0])
    
    return (max_indices, DD_flag)


def check_row_sum(matrix: List, indices: List) -> bool:
    """[This function checks the possibility of a diagonal dominance in each row]

    Args:
        matrix (List): [A square matrix]
        indices (List): [A list of index for checking which row in the matrix has which diagonal dominance]

    Returns:
        bool: [If the list of provided rows has diagonal dominance]
    """
    n = len(matrix)

    # Iterate over the index and matrix together
    for i, r in zip(indices, matrix):
        # Get a slice of the row without the diagonal element
        sub_row = r[:i] + r[(i+1):]
        # If sum of absolute values of all other elements is more than the diagonal element, then return False
        if r[i] <= sum([abs(x) for x in sub_row]):
            return False
    
    return True

def check_diagonal_dominance(matrix: List):
    """[Whether or not it is diagonally dominant or could be made diagonally dominant]

    Args:
        matrix (List): [A list of lists i.e. Matrix]
    """
    n = len(matrix)
    indices, decision = check_row(matrix)

    if not decision:
        print("This matrix can never be made diagonally dominant. One or more rows has repeated maximae")
    elif indices == list(range(0, n)):
        print("This matrix is already diagonally dominant")
    elif len(set(indices).difference(set(range(0, n)))) != 0:
        print("This matrix can never be made diagonally dominant. Multiple rows have diagonal dominance in the same column position")
    elif check_row_sum(matrix, indices):
        print(f"This matrix is not diagonally dominant, but it could be made diagonally dominant in the following row ordering {indices}")
    else:
        print(f"This matrix cannot be made diagonally dominant. One or more rows don't satisfy `Diagonal Element > Sum of all non-diagonal elements`")

m0 = [[8, 1, 6], 
      [3, 5, 0], 
      [0, 0, 1]]
print(f"Matrix: {m0}")
check_diagonal_dominance(m0)
    
m1 = [[8, 1, 6], 
      [3, 5, 7], 
      [4, 9, 2]]
print(f"Matrix: {m1}")
check_diagonal_dominance(m1)

m2= [[4,     2,     1,   101,     1],
     [5,   104,     3,     4,     1],
   [105,     5,     2,     2,     3],
     [5,     4,   105,     4,     4],
     [2,     4,     4,     1,   101 ]]
print(f"Matrix: {m2}")
check_diagonal_dominance(m2)

m3 = [[8, 1, 6], 
      [3, 5, 12], 
      [4, 9, 2]]
print(f"Matrix: {m1}")
check_diagonal_dominance(m3)