'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-17 18:11:11
@modify date 2022-02-17 19:37:02
@desc [Solve for critical points]
'''

from qn_31 import *
from scipy.optimize import fsolve
import random

import warnings
warnings.filterwarnings("error")

def find_critical_points(polynomial: List) -> List:
    """[Accepts a polynomial of 3rd degree in x and y and finds out the critical points of the same in an iterative manner]

    Args:
        polynomial (List): Co-efs of 3rd degree polynomial as a list

    Returns:
        List: A list of tuples as solution
    """
    g = polynomial
    
    # Define the system of simultaneous equations for scipy to solve
    def equations(p):
        x, y = p

        gx = (3*g[0])*(x**2) + (2*g[1])*(x*y) + (g[2])*(y**2) + (2*g[4])*(x) + (g[5])*(y) + (g[7])
        gy = (g[1])*(x**2) + (2*g[2])*(x*y) + (3*g[3])*(y**2) + (g[5])*(x) + (g[6])*(y) + (g[8])

        return (gx, gy)

    solutions = []
    counter = 0

    # Select a random starting point in the Real landscape and iterate for 1000 
    # times in the landscape
    while counter < 1000:
        initial_x, initial_y = random.randint(-10000, 10000), random.randint(-10000, 10000)
        try:
            # Try to solve the equations
            x, y =  fsolve(equations, (initial_x, initial_y))
            counter += 1

            # Rounding in order to avoid solutions which differ by a very thin margin
            # i.e. in the 8th or 9th decimal place
            sol = (round(x,7),round(y,7))
            
            # If the solution has not been encountered, then add it to the set of
            # solutions container defined above
            if not (sol in solutions):
                solutions.append(sol)
                
        except RuntimeWarning:
            # This is to suppress the solutions which do not converge and simply 
            # raise a warning that the solution didn't converge
            pass
            
    return solutions
