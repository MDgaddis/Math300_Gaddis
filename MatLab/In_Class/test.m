%% Variables

sum(1) = 0;
count = 0;


%% Code 

while sum(count+1) < 20
    sum(count + 2) = sum(count+1) + rand();
    count = count + 1;
end 

