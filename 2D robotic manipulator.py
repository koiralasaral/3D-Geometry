import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and a 3D axes.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

L1 = 5  # Length of first link
L2 = 3  # Length of second link

# We will plot the arm as a line connecting the base, first joint, and end-effector.
line, = ax.plot([], [], [], 'o-', lw=3, markersize=8)

def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-5, 5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("2-Link Robotic Manipulator Animation")
    return line,

def update(frame):
    # Let theta1 vary with frame (in degrees) and theta2 vary twice as fast.
    theta1 = np.deg2rad(frame)
    theta2 = np.deg2rad(2 * frame % 360)
    
    # Base is at the origin.
    O = np.array([0, 0, 0])
    # First joint position (end of link 1).
    J1 = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1), 0])
    # End-effector position (end of link 2).
    J2 = J1 + np.array([L2 * np.cos(theta1 + theta2), L2 * np.sin(theta1 + theta2), 0])
    
    # Update line data.
    xs = [O[0], J1[0], J2[0]]
    ys = [O[1], J1[1], J2[1]]
    zs = [O[2], J1[2], J2[2]]
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 180), init_func=init, interval=50)
plt.show()