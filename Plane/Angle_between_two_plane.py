import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Apply Seaborn style
sns.set(style="whitegrid")

# Define the normal vectors of the planes
normal_vector1 = np.array([2, 3, 5])
normal_vector2 = np.array([1, -2, 1])

# Calculate the angle between the planes
cos_theta = np.dot(normal_vector1, normal_vector2) / (np.linalg.norm(normal_vector1) * np.linalg.norm(normal_vector2))
angle = np.arccos(cos_theta)

# Convert the angle to degrees
angle_degrees = np.degrees(angle)

# Print the angle
print(f"The angle between the planes is {angle_degrees:.2f} degrees")

# Plot the planes and the angle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the planes
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
z1 = (-normal_vector1[0] * xx - normal_vector1[1] * yy) * 1. / normal_vector1[2]
z2 = (-normal_vector2[0] * xx - normal_vector2[1] * yy) * 1. / normal_vector2[2]

# Plot the planes
ax.plot_surface(xx, yy, z1, alpha=0.5, rstride=100, cstride=100, color='blue')
ax.plot_surface(xx, yy, z2, alpha=0.5, rstride=100, cstride=100, color='red')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.title(f'Angle between planes: {angle_degrees:.2f} degrees')
plt.show()