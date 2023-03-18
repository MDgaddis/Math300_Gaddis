#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


## Main Goal: Create a plot that is a spiral coming out from (0,0) 

## 1) Make an initial empty plot (with axes defined)
    # make x,y axis from -50 to 50
fig = plt.figure()
ax = plt.axes(xlim=(-1,1),ylim=(-1,1))
line, = ax.plot([],[], lw=2)
    
## 2) Make a function that creates our empty line vector
    # Read about the set_data method in matplotlib
def func():
    line = ax.set_data([],[])
    return line,

## 4) Add each new step of our parametric equation to equations array
    
xarray = [] 
yarray = []
a = .5
## 5) Create animation
def animate(i):
    t = 0.1*i #Create parameter
    
    x = (16*(t**2)*(1-(t**2))*((t**2 - 3)**2)*(t**6 + 12*(t**4) - 3*(t**2) + 2)**2)/(25*((t**2 + 1)**10))
    y = (32*(t**3)*((t**2 - 3)**2)*(t**6 + 12*(t**4) - 3*(t**2) + 2)**2)/(25*((t**2 + 1)**10))

    xarray.append(x)
    yarray.append(y)
   
    line.set_data(xarray,yarray)
    
    return line,

## 6) Plot animation

anim = animation.FuncAnimation(fig,animate,frames = 1000, interval = 20)

plt.show()