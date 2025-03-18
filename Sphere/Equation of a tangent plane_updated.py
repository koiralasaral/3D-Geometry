import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the radius of the sphere
r = 5

# Define a point on the sphere (x0, y0, z0)
x0, y0, z0 = 3, 4, 0

# Ensure the point is on the sphere
assert x0**2 + y0**2 + z0**2 == r**2, "The point is not on the sphere"

# Define the sphere
phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Equation of the tangent plane at (x0, y0, z0)
# x0*x + y0*y + z0*z = r^2
# Normal vector to the plane is (x0, y0, z0)
d = x0*x0 + y0*y0 + z0*z0

# Create a grid for the tangent plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = (d - x0*xx - y0*yy) / z0

# Plot the sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', alpha=0.3)

# Plot the tangent plane
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3)

# Plot the point of tangency
ax.scatter([x0], [y0], [z0], color='g', s=100)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()