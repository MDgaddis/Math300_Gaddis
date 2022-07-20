#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def midpoint(f,a=0,b=1,n=10):
    h = (b-a)/n
    heights = []
    total = 0   # Calculating the total

    for i in range(n):
        total += f((i*h + (i+1)*h)/2)*(h)       # Calculating the total
        heights.append(f((i*h + (i+1)*h)/2))    # Array of the heights given by the midpoint of the function
        
    # x values for the methods   
    x1 = np.arange((a+h/2),(b+h/2),h)
    x = np.arange(a,b,h)
    
    # plots for the methods
    plt.plot(x1,f(x1))  
    plt.bar(x,heights, align = 'edge', color = 'orange', edgecolor = 'blue', width = h, alpha = 0.5)
    
def func(x):
    return x*x