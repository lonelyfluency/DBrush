from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

class BrushPoint:
    def __init__(self,drawer,x,y,z,d,h):
        '''
        drawer is the handle of drawing
        z is the height of the brush point over the paper
        d is the diameter of the point area
        h is the brush length
        '''
        self.drawer = drawer
        self.z = z
        self.d = d
        self.x = x
        self.y = y
        self.h = h
    
    def draw(self):
        if self.z > 0:
            pass
        else:
            self.drawer.scatter(self.x, self.y, s=self.d**2 / 4, c='k', marker='.')




class CBrush:
    def __init__(self,drawer,length=3,width=50,delta_t=0.01):

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
        self.delta_t = delta_t
        self.bp_num = 10

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

        self.bp_state_list = []
        dh = self.length / self.bp_num
        dd = self.width / self.bp_num
        for i in range(self.bp_num):
            tmp_bp = BrushPoint(self.drawer,self.x,self.y,i*dh,i*dd,self.length)
            self.bp_state_list.append(tmp_bp)
        self.bp_state_list = self.bp_state_list[::-1]
        
    def get_avg(self,bp_l,axis):
        res = 0
        if axis == 0:
            for i in bp_l:
                res += i.x
        else:
            for i in bp_l:
                res += i.y
        return res/len(bp_l)
    
    def update_bp(self,dz):
        for i in range(1,self.bp_num):
            # self.bp_state_list[i].x = self.get_avg(self.bp_state_list[:i],0)
            # self.bp_state_list[i].y = self.get_avg(self.bp_state_list[:i],1)
            self.bp_state_list[i].x = self.bp_state_list[i-1].x
            self.bp_state_list[i].y = self.bp_state_list[i-1].y
            self.bp_state_list[i].z += dz
        self.bp_state_list[0].x = self.x
        self.bp_state_list[0].y = self.y
        self.bp_state_list[0].z = self.z


    def move(self,dx,dy,dz,dt):
        times = int(dt / self.delta_t) + 1
        tx = dx / times
        ty = dy / times
        tz = dz / times
        for i in range(times):
            self.set_pos(self.x + tx, self.y + ty, self.z + tz)
            self.update_bp(tz)
            self.draw()
        for i in range(self.bp_num):
            self.update_bp(tz)
            self.draw()
        self.t += dt

    def drop(self,dx,dy,dz,dt):
        times = int(dt / self.delta_t) + 1
        tx = dx / times
        ty = dy / times
        tz = dz / times
        for i in range(times):
            self.set_pos(self.x + tx, self.y + ty, self.z + tz)
            self.update_bp(tz)
            self.draw()
        self.t += dt

    def set_pos(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def draw(self):
        for bp in self.bp_state_list:
            bp.draw()

    def show_bp_list(self):
        for bp in self.bp_state_list:
            print('z: ',bp.z,'w: ',bp.d)

if __name__ == "__main__":
    
    plt.axis([-20,20,-20,20])
    ax = plt.gca()
    bs = CBrush(ax)
    bs.drop(2,-2,-2,0.5)
    bs.move(10,10,0.5,1)
    bs.show_bp_list()
    plt.show()

