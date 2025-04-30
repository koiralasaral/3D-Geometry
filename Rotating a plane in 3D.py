import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axes.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points.
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)

# Define the plane: for instance, 0.5x + 0.2y + z = 3.
# Solve for z: z = 3 - 0.5x - 0.2y.
Z = 3 - 0.5 * X - 0.2 * Y

# Plot the plane.
plane = ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis', edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Rotating Plane Animation")

def update(frame):
    # Animate by updating the view's azimuth.
    ax.view_init(elev=30, azim=frame)
    return ax,

# Animate from 0° to 360° in steps.
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False)
plt.show()