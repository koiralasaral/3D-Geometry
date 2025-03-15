import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def angle_between_lines(v1, v2):
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(cos_theta)
    return np.degrees(angle)

# Define the cone
def cone(radius, height, num_points=50):
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = np.linspace(0, radius, num_points)
    T, R = np.meshgrid(theta, r)
    X = R * np.cos(T)
    Y = R * np.sin(T)
    Z = height - (height / radius) * R
    return X, Y, Z

# Define the plane
def plane(a, b, c, d, x_range, y_range):
    X, Y = np.meshgrid(x_range, y_range)
    Z = (-d - a * X - b * Y) / c
    return X, Y, Z

# Parameters for the cone
radius = 5
height = 10

# Parameters for the plane
a, b, c, d = 1, 1, 1, -5
x_range = np.linspace(-5, 5, 10)
y_range = np.linspace(-5, 5, 10)

# Generate the cone and plane
X_cone, Y_cone, Z_cone = cone(radius, height)
X_plane, Y_plane, Z_plane = plane(a, b, c, d, x_range, y_range)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_cone, Y_cone, Z_cone, color='cyan', alpha=0.5)
ax.plot_surface(X_plane, Y_plane, Z_plane, color='yellow', alpha=0.5)

# Calculate the angle between the lines
v1 = np.array([1, 0, -a/c])
v2 = np.array([0, 1, -b/c])
angle = angle_between_lines(v1, v2)
print(f"The angle between the lines is {angle:.2f} degrees")

plt.show()