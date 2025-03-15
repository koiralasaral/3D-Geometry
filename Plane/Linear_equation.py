import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

class Plane:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def equation(self):
        return f"{self.a}x + {self.b}y + {self.c}z + {self.d} = 0"

    def point_on_plane(self, x, y, z):
        return self.a * x + self.b * y + self.c * z + self.d == 0

    def plot_plane(self, xlim=(-10, 10), ylim=(-10, 10)):
        xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 10), np.linspace(ylim[0], ylim[1], 10))
        zz = (-self.a * xx - self.b * yy - self.d) / self.c

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

# Example usage
plane = Plane(1, -2, 3, -4)
print("Equation of the plane:", plane.equation())
print("Is point (1, 2, 3) on the plane?", plane.point_on_plane(1, 2, 3))
plane.plot_plane()