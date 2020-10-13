from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math


plt.axis([-20,20,-20,20])


ax = plt.gca()

X = np.random.randint(-20,20,20).tolist()
Y = np.random.randint(-20,20,20).tolist()

for i in range(20):
    
    ax.scatter(X[i],Y[i],s=10,c='k',marker='.')
    ax.scatter(Y[i],X[i],s=30,c='k',marker='.')
    plt.pause(0.01)

plt.show()