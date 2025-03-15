import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def plot_cone(radius, height, num_points=100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the mesh in polar coordinates
    r = np.linspace(0, radius, num_points)
    p = np.linspace(0, 2 * np.pi, num_points)
    R, P = np.meshgrid(r, p)

    # Convert to cartesian coordinates
    X = R * np.cos(P)
    Y = R * np.sin(P)
    Z = height - (height / radius) * R

    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Example usage
plot_cone(radius=5, height=10)