from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

def f(x,y):
    return 0.1742*(x**2+y**2)**2+1.69*(x**2+y**2)

ax = plt.axes(projection='3d')


x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)

ax.contour3D(X, Y, Z, 50, cmap='Dark2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(60, 35)

plt.show()
