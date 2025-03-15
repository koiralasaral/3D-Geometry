import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Given points
points = np.array([[0, -2, -4], [2, -1, -1]])

# Line equations: 5y + 2z = 0 and 2x - 3y = 0
# Solve for y and z in terms of x
def line_equations(x):
    y = (2/3) * x
    z = -(5/2) * y
    return np.array([x, y, z])

# Find the center of the sphere
# Assume x = 1 for simplicity
center = line_equations(1)

# Calculate the radius using the distance formula
radius = np.linalg.norm(points[0] - center)

# Equation of the sphere: (x - alpha)^2 + (y - beta)^2 + (z - gamma)^2 = r^2
alpha, beta, gamma = center
r = radius

# Plotting the sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = alpha + r * np.outer(np.cos(u), np.sin(v))
y = beta + r * np.outer(np.sin(u), np.sin(v))
z = gamma + r * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z, color='b', alpha=0.3)

# Plot the given points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r', s=100)

# Plot the center of the sphere
ax.scatter(center[0], center[1], center[2], color='g', s=100)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Print the equation of the sphere
print(f"The equation of the sphere is: (x - {alpha})^2 + (y - {beta})^2 + (z - {gamma})^2 = {r**2}")