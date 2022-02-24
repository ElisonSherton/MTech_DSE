## Author: vinayak <vinayak@vinayak-EXIGO-V2>
## Created: 2022-02-23
% Script to find out the nature of critical points of a polynomial function in 2 variables

function [] = qn33 (pol)
  
  % Call the routine to take input and find the critical points of a function
  [cp] = qn32(pol);
  
  % Iterate over the individual points, find out their nature and tabulate them
  % Find out the number of critical points obtained
  n = size(cp)(2);
  
  for i = 1:n,
    [evals, nature] = hessian(pol, cp(:, i));
    printf("\nCritical Point\n");%, num2str(i));
    disp(transpose(cp(:, i)));
    printf("\nEigen Values of Hessian for this critical point as follows\n");
    disp(evals);
    printf("\nNature of the critical point: ");
    disp(nature);
  endfor
  
endfunction

function [evals, nature] = hessian(g, cp)
  % Given a polynomial and it's critical point, computes the
  % hessian matrix and it's eigen values at this point
  x = cp(1, 1); y = cp(2, 1);
  
  % Define the second order partial derivative hessian matrix
  h11 = 6*g(1)*x + 2*g(2)*y + 2*g(5);
  h12 = 2*g(2)*x + 2*g(3)*y + g(6);
  h21 = h12;
  h22 = 2*g(3)*x + 6*g(4)*y + 2*g(7);  
  hessian = [h11 h12; h21 h22];
  
  % Find the eigen vector/eigen value pairs for the hessian matrix
  [_, evs] = eigs(hessian);
  
  % Find out the nature of evs
  sgn = 1;
  evals = [];
  for i = 1:length(evs),
    sgn = sign(evs(i,i)) * sgn;
    evals = [evals evs(i, i)];
  endfor  
  
  % If all eigen values of hessian > 0 ===> Minima
  % If all eigen values of hessian < 0 ===> Maxima
  % If both +ve & -ve eigen values     ===> Saddle
  if sgn == -1,
    nature = "saddle";
  elseif (sgn == 1) && (evs(1,1) > 0),
    nature = "minima";
  elseif (sgn == 1) && (evs(1,1) < 0),
    nature = "maxima";
  endif  
endfunction