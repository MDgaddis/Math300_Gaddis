#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:18:49 2022

@author: xj9
"""

import math 
import sympy as sp
sp.init_printing()


x = sp.symbols('x')
def f(x):
    return (x**3) - ((sp.cos(sp.pi*x))**2) * (1/2*(x**2))+ ((11/3)*(x**2)) -1 

display(sp.diff(f(x)))