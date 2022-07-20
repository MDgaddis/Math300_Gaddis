clear; 
%% Variables
N = 100000;
num_rol = zeros(N,1);
avg_num_rol  = 0;

%% Code
for n = 1:N
    x1 = 0;
    x2 = 0;
    i = 0;
    while x1 < 6 || x2 < 6
        x1 = randi([1 6]);
        x2 = randi([1 6]);
        i = i + 1;
    end
    num_rol(n) = i;
end

avg_num_rol = mean(num_rol);
disp(avg_num_rol);

%% Plot 

histogram(num_rol,'Normalization','probability');


