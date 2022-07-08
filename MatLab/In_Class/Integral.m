clear;

%% Variables
n = 1000000;
sum(1) = 0;

%% Sum Code

for i = 1:n
    sum(i+1) = sum(i) + sin(i/n)*(1/n);
end

disp(sum(n+1));