#!/usr/bin/env python3

from numpy import pi, sqrt


class circle:
    def __init__(self, cx = 0, cy = 0, r = 1):
        self.cx = cx
        self.cy = cy
        self.r = r
        
    def area(self):
        return self.r*self.r*pi
    
    def circumference(self):
        return 2.0 * self.r * pi
    
    def inside(self,x,y):
        dist = sqrt((x-self.cx)**2 + (y-self.cy)**2)
        if dist <= self.r:
            return True
        else:
            return False
        
        



    




    





    
