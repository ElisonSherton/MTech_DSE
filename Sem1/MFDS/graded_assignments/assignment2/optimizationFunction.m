## Author: vinayak <vinayak@vinayak-EXIGO-V2>
## Created: 2022-02-22

function [out] = optimizationFunction(startPoint, g)
  % Start with the x and y values at this given step
  x = startPoint(1, 1);
  y = startPoint(1, 2);
  
  % Allocate memory for the output variable
  out = [0 0];
 
  % Solve for delg/delx = 0; delg/dely = 0 simultaneously
  out(1) = 3*g(1)*x^2 + 2*g(2)*x*y + g(3)*y^2 + 2*g(5)*x + g(6)*y + g(8);  
  out(2) = g(2)*x^2 + 2*g(3)*x*y + 3*g(4)*y^2 + g(6)*x + 2*g(7)*y + g(9);
endfunction