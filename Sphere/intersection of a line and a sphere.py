import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Function to find the intersection points
def line_sphere_intersection(line_point, direction_cosine, sphere_center, sphere_radius):
    # Line equation: P = line_point + t * direction_cosine
    # Sphere equation: (x - xc)^2 + (y - yc)^2 + (z - zc)^2 = r^2
    
    # Coefficients for the quadratic equation at^2 + bt + c = 0
    a = np.dot(direction_cosine, direction_cosine)
    oc = line_point - sphere_center
    b = 2 * np.dot(direction_cosine, oc)
    c = np.dot(oc, oc) - sphere_radius**2
    
    # Discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None  # No intersection
    elif discriminant == 0:
        t = -b / (2*a)
        intersection_point = line_point + t * direction_cosine
        return [intersection_point]
    else:
        t1 = (-b + np.sqrt(discriminant)) / (2*a)
        t2 = (-b - np.sqrt(discriminant)) / (2*a)
        intersection_point1 = line_point + t1 * direction_cosine
        intersection_point2 = line_point + t2 * direction_cosine
        return [intersection_point1, intersection_point2]

# Example parameters
line_point = np.array([1, 2, 3])
direction_cosine = np.array([1, 1, 1])
sphere_center = np.array([0, 0, 0])
sphere_radius = 5

# Find intersection points
intersection_points = line_sphere_intersection(line_point, direction_cosine, sphere_center, sphere_radius)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot sphere
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = sphere_radius * np.cos(u) * np.sin(v)
y = sphere_radius * np.sin(u) * np.sin(v)
z = sphere_radius * np.cos(v)
ax.plot_surface(x + sphere_center[0], y + sphere_center[1], z + sphere_center[2], color='b', alpha=0.3)

# Plot line
t = np.linspace(-10, 10, 100)
line_x = line_point[0] + t * direction_cosine[0]
line_y = line_point[1] + t * direction_cosine[1]
line_z = line_point[2] + t * direction_cosine[2]
ax.plot(line_x, line_y, line_z, color='r')

# Plot intersection points
if intersection_points:
    for point in intersection_points:
        ax.scatter(point[0], point[1], point[2], color='g', s=100)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()