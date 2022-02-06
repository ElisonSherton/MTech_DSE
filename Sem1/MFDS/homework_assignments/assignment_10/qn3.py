'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2022-02-06 16:04:15
@modify date 2022-02-06 20:32:06
@desc [Perform optimization for a specific function]
'''

from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt

START_X = 3.0
START_Y = 4.0

def compute_function_value(alpha:float, beta:float, x:float, y:float) -> float:
    """[Given the value of alpha, beta and the point, maps x,y in domain
    of f to another real number as per the definition of f]

    Args:
        alpha (float): [The co-efficient of x^2]
        beta (float): [The co-efficient of y^2]
        x (float): [x value]
        y (float): [y value]

    Returns:
        [float]: [Function value]
    """
    return alpha * (x ** 2) + beta * (y ** 2)

def compute_tau(alpha: float, beta:float, x:float, y:float) -> float:
    """[Compute tau value for the given function based on the following
    psi(tau) = xi - tau * grad(f)
    F(psi) = f(psi(tau))
    dF/dtau = 0 -> Solve for tau in terms of x and y
    ]

    Args:
        alpha (float): [The co-efficient of x^2]
        beta (float): [The co-efficient of y^2]
        x (float): [x value]
        y (float): [y value]

    Returns:
        [float]: [Tau value at a point (x,y) for the given function]
    """
    return 0.5 * ((alpha **2) * (x **2) + (beta **2) * (y ** 2)) / ((alpha ** 3) * (x ** 2) + (beta ** 3) * (y ** 2))

def update_variables(alpha: float, beta: float, x: float, y:float) -> Tuple:
    """[Perform update step in the opposite direction as gradient with the update parameter tau]

    Args:
        alpha (float): [The co-efficient of x^2]
        beta (float): [The co-efficient of y^2]
        x (float): [x value]
        y (float): [y value]

    Returns:
        Tuple: [Updated values of x,y after performing the step]
    """
    tau = compute_tau(alpha, beta, x, y)
    x_updated = x - 2 * alpha * tau * x
    y_updated = y - 2 * beta * tau * y
    return (x_updated, y_updated)

def optimize_function(alpha: float, beta: float, epsilon: float = 1e-6, plot:bool = True):
    """[Optimize the function alpha*x^2 + beta*y^2 until the optimal solution converges with a threshold of 1e-6]

    Args:
        alpha (float): [The co-efficient of x^2]
        beta (float): [The co-efficient of y^2]
        epsilon (float, optional): [Threshold of convergence]. Defaults to 1e-6.
        plot (bool, optional): [Whether to plot the progress of optimization process]. Defaults to True.
    """

    # Define the starting parameters
    error_margin = 1
    max_iterations = 100
    iteration_counter = 0
    x, y = START_X, START_Y
    f_current = compute_function_value(alpha, beta, x, y)
    entries = []

    # Optimize the solutions
    while error_margin > epsilon:
        
        # Put a hard break on iterations exceeding a set threshold number
        if iteration_counter > max_iterations:
            break

        # Compute the current value of the function
        entries.append([x, y, f_current, error_margin])

        # Update the variables
        x, y = update_variables(alpha, beta, x, y)

        # Compute function value at the updated step and update the 
        # stopping criterion
        f_new = compute_function_value(alpha, beta, x, y)
        error_margin = abs(f_new - f_current)

        # Make the new value to be the current value
        f_current = f_new

        # Increase the iteration counter
        iteration_counter += 1
    
    # Add the last entry
    entries.append([x, y, f_current, error_margin])    
    
    # Create a summary dataframe and plot the function value and relative error at each point
    # During the execution of the optimization
    execution_summary = pd.DataFrame(entries, columns = ["x", "y", "function_value", "delta_f"])
    plt.plot(execution_summary.delta_f.iloc[1:], linestyle = "solid")
    plt.title(f"Alpha: {alpha:.2f} Beta: {beta:.2f} Converged In: {iteration_counter:02d} iterations")
    plt.ylabel("Delta F")
    plt.xlabel("Iteration Counter")
    print(execution_summary.tail())