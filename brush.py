from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

class BrushPoint:
    def __init__(self,drawer,z,d,h):
        '''
        drawer is the handle of drawing
        z is the height of the brush point over the paper
        d is the diameter of the point area
        h is the length of the brush tip
        '''
        self.drawer = drawer
        self.z = z
        self.d = d
        self.h = h
    
    def draw(self,x,y,theta):
        tmp_l = self.h - self.z
        if tmp_l > 0:
            pass
        else:
            self.drawer.scatter(x+tmp_l*math.cos(theta), y+tmp_l*math.sin(theta), s=self.d, c='k', marker='.')




class CBrush:
    def __init__(self,length=3,width=1,time_lag=1):
        '''
        length is the length of the brush tip
        width is the width of the root of brush tip
        time_lag is the time lag of the tip angle follows the opposite direction of the brush move.
        '''
        
        self.length = length
        self.width = width
        self.time_lag = time_lag

        '''
        x,y is the coordination of the brush 
        h is the height over the paper of the brush tip's root
        '''

        self.x = 0
        self.y = 0
        self.h = self.length


        '''
        a mat to store the last 10 BrushPoint status
        '''

        self.num_brush_point = 50
        self.last_state = []

    def set_pos(self,x,y):
        self.x = x
        self.y = y




if __name__ == "__main__":
    
    plt.axis([-20,20,-20,20])
    ax = plt.gca()
