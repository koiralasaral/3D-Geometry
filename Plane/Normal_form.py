import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the normal vector and the distance from the origin
normal_vector = np.array([1, 1, 1])
distance_from_origin = 5

# Create a grid of points
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))

# Calculate the corresponding z values for the plane
z = (distance_from_origin - normal_vector[0] * xx - normal_vector[1] * yy) / normal_vector[2]

# Plot the plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, z, alpha=0.5, rstride=100, cstride=100)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()