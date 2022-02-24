## Author: vinayak <vinayak@vinayak-EXIGO-V2>
## Created: 2022-02-21
% Script to read a phone number and create a polynomial 

function [pol] = qn31()
  a = input("Enter your mobile number\n");
  % Allocate memory for the polynomial to be created
  pol = []; 
  num = a;
  counter = 1;
  
  % Parse through the input number and then convert them 
  % into a vector of values in sequential manner
  % Alternate +ve and -ve signs for co-efficients
  % If a zero is present in the number, substitute it with +-3
  while num > 1,
    
    x = mod(num, 10);
    if x == 0,
      x = 3;
    endif;  
    
    if mod(counter, 2) == 1,
      x = -x;
    endif;  
    
    pol = [pol; x];
    num = idivide(num, 10);
    counter = counter + 1;
  endwhile
  
  % Flip around the polynomial co-efficients
  pol = transpose(flip(pol));
  displayPolynomial(pol);
end

function [] = displayPolynomial(pol)
    % Function to display the formed polynomial
    polynomial_terms = ["x^3"; "x^2y"; "xy^2 "; "y^3"; "x^2"; "xy"; "y^2"; "x"; "y"; " "];
    poly_str = [""];
    
    for i=1:length(pol),
      if mod(i,2) == 0,
        poly_str = [poly_str num2str(pol(i)) polynomial_terms(i, :)];
      else
        poly_str = [poly_str " +" num2str(pol(i)) polynomial_terms(i, :)];
      endif
    endfor
    
    printf("Polynomial generated from the entered mobile number\n");
    disp(poly_str);
    
endfunction
