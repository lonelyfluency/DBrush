from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

class BrushPoint:
    def __init__(self,drawer,t,x,y,z,d,h):
        '''
        drawer is the handle of drawing
        t is the time of the brush point
        z is the height of the brush point over the paper
        d is the diameter of the point area
        h is the brush length
        '''
        self.drawer = drawer
        self.z = z
        self.d = d
        self.x = x
        self.y = y
        self.t = t
        self.h = h
    
    def draw(self,):
        tmp_l = self.h - self.z
        if tmp_l > 0:
            pass
        else:
            self.drawer.scatter(self.x, self.y, s=self.d, c='k', marker='.')




class CBrush:
    def __init__(self,drawer,length=3,width=1,time_lag=1):

        self.drawer = drawer

        self.t = 0

        '''
        length is the length of the brush tip
        width is the width of the root of brush tip
        time_lag is the time lag of each bruch point during the brush move.
        bp_num is the brush point number in the brush tip, which equals to the state preserve stack.
        '''
        
        self.length = length
        self.width = width
        self.time_lag = time_lag
        self.bp_num = 50

        '''
        x,y is the coordination of the brush 
        h is the height over the paper of the brush tip's root
        '''

        self.x = 0
        self.y = 0
        self.z = self.length


        '''
        a list to store state preserve BrushPoint status
        '''

        self.num_brush_point = 50
        self.bp_state_list = []
        dh = self.length / self.bp_num
        dd = self.width / self.bp_num
        for i in range(self.bp_num):
            tmp_bp = BrushPoint(self.drawer,self.t,self.x,self.y,i*dh,i*dd,self.length)
            self.bp_state_list.append(tmp_bp)
        
        

    def set_pos(self,x,y):
        self.x = x
        self.y = y


    def draw(self):
        for bp in self.this_state:
            bp.draw()

if __name__ == "__main__":
    
    plt.axis([-20,20,-20,20])
    ax = plt.gca()
