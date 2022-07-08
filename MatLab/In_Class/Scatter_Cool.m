clear;
%% Variables

theta = linspace(0, 1, 500);
x = exp(theta).*sin(100*theta);
y = exp(theta).*cos(100*theta);

%% Plots

s = scatter(x,y);


%----------Plot Settings-----------%
s.LineWidth = .6;
s.MarkerEdgeColor = 'b';
s.MarkerFaceColor = [0 0.5 0.5];
%----------------------------------%
