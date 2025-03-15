import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def sphere(center, radius):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

def plot_spheres(center1, radius1, center2, radius2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x1, y1, z1 = sphere(center1, radius1)
    x2, y2, z2 = sphere(center2, radius2)

    ax.plot_surface(x1, y1, z1, color='r', alpha=0.5)
    ax.plot_surface(x2, y2, z2, color='b', alpha=0.5)

    plt.show()

def main():
    center1 = [0, 0, 0]
    radius1 = 5
    center2 = [3, 3, 3]
    radius2 = 5

    plot_spheres(center1, radius1, center2, radius2)

if __name__ == "__main__":
    main()