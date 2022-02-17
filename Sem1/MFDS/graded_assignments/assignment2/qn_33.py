'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-17 22:04:31
@modify date 2022-02-17 22:39:00
@desc [Identify if a point is a maxima or minima or saddle point]
'''

from qn_32 import *
from typing import Tuple

def determine_nature(polynomial: List, critical_point: Tuple, threshold: float = 1e-6) -> str:
    """[Given a polynomial and an identified critical point for the polynomial,
    computes if the point is a maxima, minima or saddle point]

    Args:
        polynomial (List): Co-efficients of the polynomial
        critical_point (Tuple): A critical point in R2
        threshold (float, default: 1e-6): A zero threshold (i.e. whether the eigen value found is zero or not) 

    Returns:
        str: Type of the point
    """
    g = polynomial
    cx, cy = critical_point

    # Compute hessian matrix values
    h11 = 6*g[0]*cx + 2*g[1]*cy + 2*g[4]
    h12 = 2*g[1]*cx + 2*g[2]*cy + g[5]
    h21 = h12
    h22 = 2*g[2]*cx + 6*g[3]*cy + 2*g[6]

    # Find the determinant of this hessian matrix
    D = h11 * h22 - h12 * h21
       
    # Check the signs of eigen values
    if abs(D) < threshold:
        return "inconclusive"
    elif D < 0:
        return "saddle"
    elif ((D > 0) and (h11 > 0)):
        return "minima"
    elif ((D > 0) and (h11 < 0)):
        return "maxima"
    