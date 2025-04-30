import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # Enable 3D plotting

# Create a figure and a 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create a grid for x and y values
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

def update(frame):
    # Clear the previous surface in each frame
    ax.clear()
    
    # Use frame to smoothly update the parameter i in the range 1 to 5.
    i = 1 + 4 * (frame / 100)
    
    # Define coefficients that change with i for demonstration:
    # Here, a, b, c, d vary with i.
    a_new = i
    b_new = -i
    c_new = i + 1
    d_new = -i
    
    # Compute the slopes (if you solve for z, i.e., z = m1*x + m2*y - d_new/c_new)
    m1 = -a_new / c_new
    m2 = -b_new / c_new
    
    # Calculate the new Z values from the plane equation
    Z_new = (-a_new * X - b_new * Y - d_new) / c_new
    
    # Plot the updated plane surface
    surf = ax.plot_surface(X, Y, Z_new, alpha=0.6, cmap="cividis", edgecolor='none')
    
    # Label the axes and set a title that displays current parameters and slopes
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    title_str = (f"Frame: {frame} | Equation: {a_new:.2f}x + ({b_new:.2f})y + "
                 f"{c_new:.2f}z + ({d_new:.2f}) = 0\n"
                 f"m1 = {m1:.2f}, m2 = {m2:.2f} (m1:m2 = {m1:.2f}:{m2:.2f})")
    ax.set_title(title_str)
    
    return surf,

# Create the animation:
# Here, we animate for 101 frames (from frame 0 to 100), updating every 100 milliseconds.
ani = FuncAnimation(fig, update, frames=np.arange(0, 101), interval=100, blit=False)

plt.show()