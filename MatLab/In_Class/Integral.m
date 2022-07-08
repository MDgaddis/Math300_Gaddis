clear;

%% Variables
n = 1000000;
sum(1) = 0;
%x = linspace(0, .6, n+1);


%% Sum Code

for i = 1:n
    sum(i+1) = sum(i) + sin(i/n)*(1/n);
end

%plot(x,sum);

