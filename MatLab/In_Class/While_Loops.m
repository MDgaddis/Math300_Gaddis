clear;
%% Variables
n = 10000000;
sum(1) = 0; %holds the sum

%% Code
for i = 1:n
    sum(i+1) = sum(i) + sin(i/n)*(1/n);
end

disp(sum(i+1));
