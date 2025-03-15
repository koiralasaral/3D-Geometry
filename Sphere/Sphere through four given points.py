import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sphere_through_four_points(p1, p2, p3, p4):
    A = np.array([
        [p1[0], p1[1], p1[2], 1],
        [p2[0], p2[1], p2[2], 1],
        [p3[0], p3[1], p3[2], 1],
        [p4[0], p4[1], p4[2], 1]
    ])

    B = np.array([
        [np.dot(p1, p1), p1[1], p1[2], 1],
        [np.dot(p2, p2), p2[1], p2[2], 1],
        [np.dot(p3, p3), p3[1], p3[2], 1],
        [np.dot(p4, p4), p4[1], p4[2], 1]
    ])

    C = np.array([
        [np.dot(p1, p1), p1[0], p1[2], 1],
        [np.dot(p2, p2), p2[0], p2[2], 1],
        [np.dot(p3, p3), p3[0], p3[2], 1],
        [np.dot(p4, p4), p4[0], p4[2], 1]
    ])

    D = np.array([
        [np.dot(p1, p1), p1[0], p1[1], 1],
        [np.dot(p2, p2), p2[0], p2[1], 1],
        [np.dot(p3, p3), p3[0], p3[1], 1],
        [np.dot(p4, p4), p4[0], p4[1], 1]
    ])

    E = np.array([
        [np.dot(p1, p1), p1[0], p1[1], p1[2]],
        [np.dot(p2, p2), p2[0], p2[1], p2[2]],
        [np.dot(p3, p3), p3[0], p3[1], p3[2]],
        [np.dot(p4, p4), p4[0], p4[1], p4[2]]
    ])

    a = np.linalg.det(A)
    b = -np.linalg.det(B)
    c = np.linalg.det(C)
    d = -np.linalg.det(D)
    e = np.linalg.det(E)

    return a, b, c, d, e

def plot_sphere(a, b, c, d, e):
    # Calculate the center and radius of the sphere
    center = np.array([-b/(2*a), -c/(2*a), -d/(2*a)])
    radius = np.sqrt((b**2 + c**2 + d**2 - 4*a*e) / (4*a**2))

    # Create a grid of points
    phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
    x = radius * np.sin(theta) * np.cos(phi) + center[0]
    y = radius * np.sin(theta) * np.sin(phi) + center[1]
    z = radius * np.cos(theta) + center[2]

    # Plot the sphere
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='b', alpha=0.6)

    # Plot the original points
    ax.scatter([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]], [p1[2], p2[2], p3[2], p4[2]], color='r')

    plt.show()

# Example usage:
p1 = [1, 2, 3]
p2 = [4, 5, 6]
p3 = [7, 8, 9]
p4 = [10, 11, 12]

coefficients = sphere_through_four_points(p1, p2, p3, p4)
print("The coefficients of the sphere are:", coefficients)

plot_sphere(*coefficients)