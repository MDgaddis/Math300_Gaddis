%% Variables

A = [1 2 ; 3 4];
b = [4 ; 5];

%% Code

x = A\b;
x2 = inv(A)*b;

disp(x);

