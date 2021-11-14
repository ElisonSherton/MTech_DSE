'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-14 17:05:16
@modify date 2021-11-14 17:33:06
@desc [Assignment 0 question 4 solution]
'''

import numpy as np

A = np.array([[0.1036, 0.2122],[0.2081, 0.4247]], dtype = np.float64)
B = np.array([[0.7381], [0.9327]], dtype = np.float64) 

augmented_rep = np.hstack([A,B])

def solve(augmented_matrix:np.array, significant_digits: int) -> np.array:
    """Takes in an augmented representation of linear system and returns a vector of solutions

    Args:
        augmented_matrix (np.array): [This is the matrix representation [A|b]]
        significant_digits (int): [The number of signficant decimal places to consider when solving the problem]

    Returns:
        np.array: [The solution to the given system of equations]
    """
    # Assume for simplicity that we have a two variables two equations system

    am = np.around(augmented_matrix, significant_digits)
    print(f"Augmented Representation:\n{am}")
    am[1, :] = am[1, :] - am[0, :] * am[1, 0] / am[0, 0]
    x2 = am[1,-1]/ am[1,-2]
    x1 = (am[0, -1] - x2 * am[0, 1]) / am[0, 0]
    return np.array([x1, x2], dtype = np.float64)

for i in range(5, 1, -1):
    print(f"Significant digits: {i}| Solution: {solve(augmented_rep, i)}")

print("\n\nReversing the rows")
augmented_rep = augmented_rep[::-1, :]

for i in range(5, 1, -1):
    print(f"Significant digits: {i}| Solution: {solve(augmented_rep, i)}")
    