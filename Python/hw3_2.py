#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:34:37 2022

@author: xj9
"""

import math
import matplotlib.pyplot as plt

def sum3(N = 100):
    N_totals = []
    total = 0
    for n in range(1,N+1):
        total += ((-1)**(n+1))/n
        
        N_totals.append(total)
        print(N_totals)
    plt.plot(range(n),N_totals)
    plt.show()
    
