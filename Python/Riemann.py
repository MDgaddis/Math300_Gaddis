#!/usr/bin/env python3




import numpy as np
import matplotlib.pyplot as plt


def riemannplot(f,a=0,b=1,n=10):
    length = (b-a)/1000
    length2 = (b-a)/n
    x = np.arange(a,b+length,length)
    plt.plot(x,f(x))
    
    riemannx = np.arange(a,b,length2)
    plt.bar(riemannx, f(riemannx), align='edge', color='orange', edgecolor='blue', width=length2, alpha=0.5)
    plt.xlim(a,b)
    plt.show()

def f(x):
    return 3*x**5 - 4*x**2 - 1