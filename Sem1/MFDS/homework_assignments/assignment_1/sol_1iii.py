'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-25 18:11:40
@modify date 2021-11-25 18:42:09
@desc [Check the time requirements for fe and bs in GE implemented in sol_1i.py]
'''

from sol_1i import pivot, forward_elimination, back_substitution, dot_product
import numpy as np
from tqdm import tqdm
import time, copy

# Create a random set of equations and perform forward substitution and backward elimination
ns = np.arange(5, 501, 5)

# Set a seed for reproducibility
np.random.seed(42)

# Log the time results into a text file
with open("time_log.txt", "w") as f:
    for n in tqdm(ns, desc = "Testing GE fe & bs times"):
        
        A = np.random.randn(n, n)
        b = np.random.randn(n, 1)
        aug_matrix = np.hstack([A, b])
        
        fe_start = time.time()
        fe_result = forward_elimination(copy.copy(aug_matrix))
        fe_end = time.time()
        fe_time = fe_end - fe_start

        bs_start = time.time()
        bs_result = back_substitution(copy.copy(aug_matrix))
        bs_end = time.time()
        bs_time = bs_end - bs_start

        f.writelines(f"n: {n:3d} | forward elimination time: {fe_time:3.4f} s | back substitution time: {bs_time:3.4f} s\n")