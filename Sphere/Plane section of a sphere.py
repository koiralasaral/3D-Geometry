import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the sphere
def sphere(radius, center):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

# Define the plane
def plane_section(radius, center, z_plane):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta) + center[0]
    y = radius * np.sin(theta) + center[1]
    z = np.full_like(theta, z_plane)
    return x, y, z

# Parameters
radius = 5
center = [0, 0, 0]
z_plane = 2

# Generate sphere and plane section
x_sphere, y_sphere, z_sphere = sphere(radius, center)
x_plane, y_plane, z_plane = plane_section(np.sqrt(radius**2 - z_plane**2), center, z_plane)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.3)

# Plot the plane section
ax.plot(x_plane, y_plane, z_plane, color='r', linewidth=2)

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane Section of a Sphere')

plt.show()