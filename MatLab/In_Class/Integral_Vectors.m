clear;

%% Variables
N = 10000000;
x = 0:1/N:1;
y = sin(x);

%% Code

sol = sum(y)/N;