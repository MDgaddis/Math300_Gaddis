clear; 
%% Variables
N = 100000;
num_rol = zeros(N,1);
avg_num_rol  = 0;

%% Code

for n = 1:N
    x(1,n) = randi([1 6]);
    x(2,n) = randi([1 6]);
end
        
avg_sum = sum(x);

%% Plot     

histogram(avg_sum, 'Normalization','probability');


