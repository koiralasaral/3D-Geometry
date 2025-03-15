import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the planes
plane1 = np.array([1, 2, 3, -4])
plane2 = np.array([2, 1, -1, 5])
plane3 = np.array([5, 3, 6, 8])

# Find the line of intersection of plane1 and plane2
normal1 = plane1[:3]
normal2 = plane2[:3]
direction = np.cross(normal1, normal2)

# Find a point on the line of intersection
A = np.array([plane1[:3], plane2[:3], direction])
b = np.array([-plane1[3], -plane2[3], 0])
point_on_line = np.linalg.solve(A, b)

# Find the equation of the plane perpendicular to plane3 and containing the line of intersection
normal3 = plane3[:3]
d = -np.dot(normal3, point_on_line)
plane_perpendicular = np.append(normal3, d)

# Plotting
sns.set(style="whitegrid")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = (-plane_perpendicular[0] * xx - plane_perpendicular[1] * yy - plane_perpendicular[3]) * 1. / plane_perpendicular[2]

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)

# Plot the line of intersection
t = np.linspace(-10, 10, 100)
x_line = point_on_line[0] + direction[0] * t
y_line = point_on_line[1] + direction[1] * t
z_line = point_on_line[2] + direction[2] * t
ax.plot(x_line, y_line, z_line, color='r', label='Line of Intersection')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane Perpendicular to 5x+3y+6z+8=0 and containing the line of intersection')

plt.legend()
plt.show()