import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the plane equation 3x + 4y - 5z = -8
def plane_eq(x, y):
    return (3*x + 4*y + 8) / 5

# Create a grid of x, y values
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)
z = plane_eq(x, y)

# Plot the plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.5, rstride=100, cstride=100)

# Plot the point (1, 2, 3)
ax.scatter(1, 2, 3, color='red', s=100)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
