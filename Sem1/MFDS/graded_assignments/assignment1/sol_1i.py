'''
@author Vinayak
@email vnayak@okkular.io / nayakvinayak95@gmail.com
@create date 2021-11-29 20:48:27
@modify date 2021-12-05 15:23:03
@desc [Solution to 1.i for the assignment questions]

Comment: 
Since addition of first 1e6 numbers could be done but we can't multiply/divide 1e6 numbers, I am sampling pairs of (n,n+1) where n belongs to (0, 1e6] and then performing all operations on these pairs in a loop to keep a common baseline
'''

import time
numbers = list(range(1, 1000001))

# Estimate time taken for addition of two numbers
# TODO: Investigate more on int datatype (int -> 32 bits, then max storage ~ 4e9 but addition result is still stored even if it is actually ~ 5e11)
sum_ = 0

start = time.time()
# for n in numbers:
#     sum_ = sum_ + n
for n1, n2 in zip(numbers[:100000 - 1], numbers[1:]):
    sum_ = n1 + n2

end = time.time()
addition_time = (end - start) / 1e6
print(f"Average time taken per addition operation: {addition_time:.9f}")

# Estimate the time taken for multiplication of two numbers
# Take two consecutive numbers and then multiply them instead 
# of multiplying first 1e6 numbers else it will return in overflow

product = 1
numbers = list(range(1, 1000002))
start = time.time()
for n1, n2 in zip(numbers[:1000001], numbers[1:]):
    product = n1 * n2
# for n in numbers:
#     product = product * n
end = time.time()
multiplication_time = (end - start) / 1e6
print(f"Average time taken per multipln operation: {multiplication_time:.9f}")

# Estimate the time taken for division of two numbers
# Take two consecutive numbers and then divide this pair (in no particular order) instead 
# of dividing first 1e6 numbers else it will return in underflow (i.e. 1/2/3/4/5...)

div = 1
numbers = list(range(1, 1000002))
start = time.time()
for n1, n2 in zip(numbers[:1000001], numbers[1:]):
    div = n1 / n2
end = time.time()
multiplication_time = (end - start) / 1e6
print(f"Average time taken per division operation: {multiplication_time:.9f}")