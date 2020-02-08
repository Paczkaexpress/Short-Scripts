import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
import random

fig= plt.figure()
ax = p3.Axes3D(fig)
xdata, ydata, zdata = [0], [0], [0]
ln, = plt.plot([], [], [], 'b')

def init():
    ax.set_xlim(-25, 25)
    ax.set_zlim(-25, 25)
    ax.set_ylim(-25, 25)
    return ln,

def update(frame):

    xdata.append(xdata[-1] + random.random() - 0.5)
    ydata.append(ydata[-1] + random.random() - 0.5)
    zdata.append(zdata[-1] + random.random() - 0.5)
    ln.set_data(xdata, ydata)
    ln.set_3d_properties(zdata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, interval = 2, blit=True)
plt.show()