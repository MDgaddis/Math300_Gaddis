clear;
%% Variables
z = linspace(0,4*pi,250);
x = 2*cos(z); %+ rand(1,250);
y = 2*sin(z); %+ rand(1,250);
%% Plots

s = scatter3(x,y,z);

%----------Plot Settings-----------%
s.LineWidth = .6;
s.MarkerEdgeColor = 'b';
s.MarkerFaceColor = [0 0.5 0.5];
%----------------------------------%
