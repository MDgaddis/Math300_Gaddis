# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:28:45 2022

@author: Matt
"""

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def midpoint(f,a=0,b=1,n=10):
    h = (b-a)/n
    heights = []
    total = 0   # Calculating the total
    x = np.arange(a,b+h,h)
    
    for i in range(n):
        total += f((x[i] + (x[i+1]))/2)*(h)       # Calculating the total
        heights.append(f((x[i] + x[i+1])/2))    # Array of the heights given by the midpoint of the function
        
    # x values for the methods   
    x1 = np.arange((a+h/2),(b+h/2),h)
    
    # plots for the methods
    plt.plot(x,f(x))  
    plt.bar(x1, heights, align = 'center', color = 'orange', edgecolor = 'blue', width = h, alpha = 0.5)
    
def func(x):
    return x*x