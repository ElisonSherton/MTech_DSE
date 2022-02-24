## Author: vinayak <vinayak@vinayak-EXIGO-V2>
## Created: 2022-02-23
% Script to find out the critical points of a polynomial

function [critical_points] = qn32(pol)
  
  % Display the polynomial created from the given cell number
  disp("Polynomial co-efficients entered is as follows");
  disp(pol);
  
  % Create a container to hold the solution values
  critical_points = [];
  
  % Find out the critical points using fsolve
  % Start at different points in the function domain using random
  % Variables and then find the roots of grad(pol) = 0
 
  for i = 1:1000,
    % Define the start point
    startPoint = 1000 * randn(2, 1);
    % Create a wrapper function for the objective/optimization function
    optimFunc = @(pol) @(startPoint) optimizationFunction(startPoint, pol);
    % Define the solver options
    options = optimset ("TolFun", 1e-6, "MaxIter", 5000);
    % Find solutions to the above objective function
    [sol, fval, info] = fsolve(optimFunc(pol), startPoint, options);
    % If the solution converged in this iteration, save the 
    % Point as a critical point in the matrix
    if info == 1,
      critical_points = addToSolution(critical_points, sol);
    endif;
  endfor
  
endfunction

function [distance] = euclideanDistance(v1, v2)
  % Given two vectors v1 and v2, compute the Euclidean distance between them
  distance = sqrt(sum((v1 - v2).^2));
endfunction

function [sol] = addToSolution(solutionSet, newSolution)
  % Given a set of critical points and a new critical point
  % Check if the new point is already present in the given set
  % If no, add it to the solution set, else return the set as is
  n = size(solutionSet)(2);
  present = 0;
  for i = 1:n,
    r = euclideanDistance(solutionSet(:, i), newSolution);
    if r < 1e-6,
      present = 1;
      break;
    endif  
  endfor  
  
  % If the solution doesn't exist in the current set, add it to
  % The current set, otherwise, just return old solution set as is
  if present == 0,
    sol = [solutionSet, newSolution];
  else
    sol = solutionSet;
  endif;  
  
endfunction  

function [out] = optimizationFunction(startPoint, g)
  % Start with the x and y values at this given step
  x = startPoint(1);
  y = startPoint(2);
  
  % Solve for delg/delx = 0; delg/dely = 0 simultaneously
  gx = 3*g(1)*x^2 + 2*g(2)*x*y + g(3)*y^2 + 2*g(5)*x + g(6)*y + g(8);  
  gy = g(2)*x^2 + 2*g(3)*x*y + 3*g(4)*y^2 + g(6)*x + 2*g(7)*y + g(9);
  out = [gx gy];
endfunction  