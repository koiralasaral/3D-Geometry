import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plane_equation(a, b, c, d):
    if c != 0:
        return lambda x, y: (-a*x - b*y - d) / c
    elif b != 0:
        return lambda x, z: (-a*x - c*z - d) / b
    else:
        return lambda y, z: (-b*y - c*z - d) / a

def bisecting_planes(plane1, plane2):
    a1, b1, c1, d1 = plane1
    a2, b2, c2, d2 = plane2

    norm1 = np.sqrt(a1**2 + b1**2 + c1**2)
    norm2 = np.sqrt(a2**2 + b2**2 + c2**2)

    bisector1 = (a1/norm1 + a2/norm2, b1/norm1 + b2/norm2, c1/norm1 + c2/norm2, d1/norm1 + d2/norm2)
    bisector2 = (a1/norm1 - a2/norm2, b1/norm1 - b2/norm2, c1/norm1 - c2/norm2, d1/norm1 - d2/norm2)

    return bisector1, bisector2

def plot_planes(plane1, plane2, bisector1, bisector2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    Z1 = plane_equation(*plane1)(X, Y)
    Z2 = plane_equation(*plane2)(X, Y)
    Z3 = plane_equation(*bisector1)(X, Y)
    Z4 = plane_equation(*bisector2)(X, Y)

    ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z4, alpha=0.5, rstride=100, cstride=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Example planes
plane1 = (2, -1, 1, -6)  # Plane equation: 2x - y + z - 6 = 0
plane2 = (1, 1, 2, -3)   # Plane equation: x + y + 2z - 3 = 0

bisector1, bisector2 = bisecting_planes(plane1, plane2)
print("Bisecting planes:", bisector1, bisector2)
print("Equation of the plane:", bisector1.plane_equation(), bisector2.plane_equation())
plot_planes(plane1, plane2, bisector1, bisector2)