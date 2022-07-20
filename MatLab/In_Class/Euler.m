%% Variables

% f'(x) = x^2 + x + 1, f(0) = 0
% Euler method says we have: f(x_{n+1}) - f(x_{n}) / h = x_{n}^{2} + x_{n} + 1 

%% Code for discretized version
l = 100; %length
N = 1000; % steps

h = l/N; %delta x

f(1) = 0; % starting value f(0) = 0


for n = 1:N % x values
    f(n+1) = f(n) + h*((n)^2 + n + 1); 
end

%% actual solution
x = linspace(0,N*h,N+1);
y = (x.^3)/2 + x.^2 + x;


plot(x,f, 'b')
hold on 
plot(x,y, 'r');

