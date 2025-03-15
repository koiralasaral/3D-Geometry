import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def perpendicular_distance(x1, y1, z1, l, m, n, p):
    numerator = abs(l*x1 + m*y1 + n*z1 - p)
    denominator = np.sqrt(l**2 + m**2 + n**2)
    return numerator / denominator

def plot_point_and_plane(x1, y1, z1, l, m, n, p):
    # Create a grid of points
    xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
    zz = (p - l*xx - m*yy) / n

    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the plane
    ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)

    # Plot the point
    ax.scatter([x1], [y1], [z1], color='red')

    # Plot the perpendicular line
    d = perpendicular_distance(x1, y1, z1, l, m, n, p)
    x_proj = x1 - d * l / np.sqrt(l**2 + m**2 + n**2)
    y_proj = y1 - d * m / np.sqrt(l**2 + m**2 + n**2)
    z_proj = z1 - d * n / np.sqrt(l**2 + m**2 + n**2)
    ax.plot([x1, x_proj], [y1, y_proj], [z1, z_proj], color='blue')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Example usage
x1, y1, z1 = 1, 2, 3
l, m, n, p = 1, -2, 1, 4
distance = perpendicular_distance(x1, y1, z1, l, m, n, p)
print(f"The perpendicular distance is: {distance}")

plot_point_and_plane(x1, y1, z1, l, m, n, p)