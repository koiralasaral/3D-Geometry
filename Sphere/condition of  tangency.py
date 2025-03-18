import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the sphere parameters
u, v, w, d = 1, 1, 1, -10  # Example values
sphere_center = np.array([-u, -v, -w])
sphere_radius = np.sqrt(u**2 + v**2 + w**2 - d)

# Define the plane parameters
l, m, n, p = 1, 1, 1, 5  # Example values

# Condition for tangency
condition = abs(l * u + m * v + n * w - p) / np.sqrt(l**2 + m**2 + n**2) == sphere_radius
print(f"Condition for tangency: {condition}")

# Plotting the sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points
phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
x = sphere_radius * np.sin(theta) * np.cos(phi) + sphere_center[0]
y = sphere_radius * np.sin(theta) * np.sin(phi) + sphere_center[1]
z = sphere_radius * np.cos(theta) + sphere_center[2]

ax.plot_surface(x, y, z, color='b', alpha=0.5)

# Plotting the plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = (p - l * xx - m * yy) / n

ax.plot_surface(xx, yy, zz, color='r', alpha=0.5)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()