clear;
%% Variables

[X Y Z] = sphere(16);
x = [0.5*X(:); 0.75*X(:); X(:)];
y = [0.5*Y(:); 0.75*Y(:); Y(:)];
z = [0.5*Z(:); 0.75*Z(:); Z(:)];

%% Plots

s = scatter3(x,y,z);

%----------Plot Settings-----------%
s.LineWidth = .6;
s.MarkerEdgeColor = 'b';
s.MarkerFaceColor = [0 0.5 0.5];
%----------------------------------%
