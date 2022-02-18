'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-18 13:16:25
@modify date 2022-02-18 21:58:27
@desc [Gradient Descent Algorithm]
'''

from qn_11 import *
from qn_21 import *
import numpy as np
from typing import Tuple

def gradient_descent() -> List:
    """[Generates a random matrix based on user's mobile number, performs gradient descent and returns the solutions of the system of equation and intermediate steps taken]

    Returns:
        List: [A list of solutions, intermediate values and function values at each step]
    """
    A, b = generate_matrix()
    A = np.array(A)
    b = np.array(b)
    
    current_solution = np.zeros((A.shape[1], 1))

    optimization_steps = []
    while True:
        
        # Find out the function value
        f = np.matmul(A, current_solution) - b
        func_val = 0.5 * (frob_norm(f.tolist()) ** 2)

        # Find the gradient of the function at the current step 
        AtA = np.matmul(A.transpose(), A)
        AtAx = np.matmul(AtA, current_solution)
        Atb = np.matmul(A.transpose(), b)
        gradf = AtAx - Atb

        # Compute the learning rate
        tau_nr = np.matmul(gradf.transpose(), gradf).flatten().item()
        tau_dr = np.matmul(gradf.transpose(), np.matmul(AtA, gradf)).flatten().item()
        
        # Take a step in the opposite direction of the gradient
        previous_solution = current_solution
        current_solution = previous_solution - (tau_nr / tau_dr) * gradf

        # Define the stopping criterion
        stopping_threshold = frob_norm((current_solution - previous_solution).tolist())
        if abs(stopping_threshold) <= 1e-4:
            break

        optimization_steps.append([previous_solution, gradf, func_val])
    
    return optimization_steps

for entry in gradient_descent():
    print(entry[0], entry[1], entry[2])