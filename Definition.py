import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D plotting

# ----- Plane equation: ax + by + cz + d = 0 -----
# Define coefficients for our plane:
a, b, c, d = 2, -1, 3, -4

# Compute "slopes" if we solve for z (assuming c != 0)
m1 = -a / c  # slope with respect to x
m2 = -b / c  # slope with respect to y
print(f"m1 = {m1}, m2 = {m2} (so m1:m2 = {m1}:{m2})")

# Create a grid for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Solve for Z in the plane eqn.
Z = (-a * X - b * Y - d) / c

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plane_plot = ax.plot_surface(X, Y, Z, alpha=0.7, cmap="viridis", edgecolor='none')

# ----- Two points A and B -----
# Example points: A = (x1, y1, z1) and B = (x2, y2, z2)
A = (1, 2, 3)
B = (4, 5, 6)
ax.scatter(*A, color='red', s=50, label='Point A')
ax.scatter(*B, color='blue', s=50, label='Point B')

# Label axes and add title & legend
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Plane: 2x - y + 3z - 4 = 0")
ax.legend()
plt.colorbar(plane_plot, shrink=0.5, aspect=5, label="Plane Surface Value")
plt.show()