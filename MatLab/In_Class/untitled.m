syms L g N I S b k

f_S = (-b*I)/(1+k*I);
f_I = (-b*S)/((1+k*I)^2);
g_S = (b*I)/(1+k*I);
g_I = (b*S)/((1+k*I)^2) - g;

A = sym([f_S f_I ; g_S g_I]);

B = eig(A)

