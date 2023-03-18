#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:11:26 2022

@author: xj9
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



# Create the empty figure to be animated
fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim = (-50,50))
line, = ax.plot([], [], lw=2)

#create the function
def line_start():
    #create first set of empty data
    line.set_data([],[])
    return line,

#store x and y values as it moves along
xdata, ydata = [], []

#method to animate the function, i is the variable for frame count

def animate(i):
    # create parameter
    t = 0.1*i
    
    #find x,y values to be plotted
    x = t*np.sin(t)
    y = t*np.cos(t)
    
    #append x,y values to array so they stay showing up
    xdata.append(x)
    ydata.append(y)
    
    #update with new data
    line.set_data(xdata,ydata)
    
    return line,

#call animator that uses animation function
anim = animation.FuncAnimation(fig, animate, init_func = line_start, frames = 500, interval = 20, blit=False)

plt.show()
