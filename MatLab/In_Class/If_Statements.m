%% Variables
A = [1 -1; 4 -4];
B = A(1,1) + A(1,2) + A(2,1) + A(2,2);
N = 10;
C = [1 2 3 4 5 6 7 8 9 10];
c_sum = 0;

%% If Statements Code

if B > 0
    disp('The sum of the elements of A is Positive!')
elseif B < 0
    disp('The sum of the elements of A is Negative!')
else 
    disp('The sum of the elements of A must be 0! ')
end 

%% For Loops Code

for i = 1:length(C)
    c_sum = c_sum + C(i);
end 