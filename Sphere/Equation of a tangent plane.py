import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Function to calculate the equation of the tangent plane
def tangent_plane(x0, y0, z0, r):
    # The equation of the sphere is x^2 + y^2 + z^2 = r^2
    # The equation of the tangent plane at (x0, y0, z0) is:
    # x0*(x - x0) + y0*(y - y0) + z0*(z - z0) = 0
    # Simplifying, we get:
    # x0*x + y0*y + z0*z = r^2
    return lambda x, y: (r**2 - x0*x - y0*y) / z0

# Sphere parameters
r = 5
x0, y0, z0 = 3, 2, 4

# Create a grid of points
x = np.linspace(-r, r, 400)
y = np.linspace(-r, r, 400)
x, y = np.meshgrid(x, y)

# Calculate z values for the tangent plane
z = tangent_plane(x0, y0, z0, r)(x, y)

# Plot the sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = r * np.outer(np.cos(u), np.sin(v))
y_sphere = r * np.outer(np.sin(u), np.sin(v))
z_sphere = r * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.3)

# Plot the tangent plane
ax.plot_surface(x, y, z, color='r', alpha=0.5)

# Plot the point of tangency
ax.scatter(x0, y0, z0, color='g', s=100)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()