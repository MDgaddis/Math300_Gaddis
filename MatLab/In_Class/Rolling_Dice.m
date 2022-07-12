%% Variables
n = 100000;
    
%% Code
for l = 1:n
i = 0;
x1 = 0;
x2 = 0;
    while x1 < 6 || x2 < 6
        x1 = randi([1 6]);
        x2 = randi([1 6]);
        i = i + 1;
    end
    overall_count(l) = i;
end

ave_count = sum(overall_count)/n;
disp(ave_count);

