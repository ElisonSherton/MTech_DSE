% Define a matrix a
% Define a wide rectangular matrix and then a square matrix and compare the results for both of them
a = [1 2 3; 4 3 2]
% a = [1 2 3; 4 3 2; -1 5 6]

% Compute atranspose * a  
B1 = a' * a
B2 = a * a'

% Find their eigen values, eigen vectors and determine if the eigen vectors are orthonormal
[E1, V1] = eigs(B1)
[E2, V2] = eigs(B2)

e1_orthonormal = E1 * E1'
e2_orthonormal = E2 * E2'

% Look at the singular value decomposition of a and the eigen vectors of B1, B2
[U, S, V] = svd(a)

% Observations:
% The eigen vectors of AA' and A'A are orthonormal 
% V = k * eigen vectors of a'a
% U = c * eigen vectors of aa'
% S elements are sqrt of eigen values of aa'
% In case of m = n i.e. square matrix, the S = Sigma * Sigma