clear;
%% Variables

x = linspace(0, 3*pi,200);
y = cos(x) + rand(1,200);
y1 = cos(x);

%% Plots

scatter(x,y);
xlabel('x');
ylabel('y');
title('this is a title');
hold on
plot(x,y1,'--r')
