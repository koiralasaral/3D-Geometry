import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D plotting

# Set up the figure and 3D axes.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 8)
ax.set_zlim(-1, 8)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Change of Origin in Robotics\nNew Coordinates via Translation", fontsize=14)

# -------------------------------------------------------------------
# Original coordinate system (global/world frame)
# -------------------------------------------------------------------
O = np.array([0, 0, 0])
# Draw original coordinate axes using solid arrows.
ax.quiver(O[0], O[1], O[2], 6, 0, 0, color='blue', arrow_length_ratio=0.1, label='Original X')
ax.quiver(O[0], O[1], O[2], 0, 6, 0, color='green', arrow_length_ratio=0.1, label='Original Y')
ax.quiver(O[0], O[1], O[2], 0, 0, 6, color='purple', arrow_length_ratio=0.1, label='Original Z')

# -------------------------------------------------------------------
# Fixed point P in the original coordinate frame.
# -------------------------------------------------------------------
P = np.array([6, 4, 3])
ax.scatter(P[0], P[1], P[2], color='black', s=80, label='P (original)')
ax.text(P[0], P[1], P[2], "  P (6,4,3)", color='black', fontsize=10)

# -------------------------------------------------------------------
# Decide on a final new origin: O₁ = (α, β, γ).
# For demonstration, we take (2, 1, 1).
alpha, beta, gamma = 2, 1, 1

# We will animate the new origin moving linearly from O to (2,1,1).
# Placeholders for new coordinate axes, new-origin marker, and for drawing the transformation vector.
new_origin_marker, = ax.plot([], [], [], 'ro', markersize=8, label='New Origin O₁')
new_axisX_line, = ax.plot([], [], [], 'r--', lw=2, label='New X₁-axis')
new_axisY_line, = ax.plot([], [], [], 'r--', lw=2, label='New Y₁-axis')
new_axisZ_line, = ax.plot([], [], [], 'r--', lw=2, label='New Z₁-axis')
vector_line, = ax.plot([], [], [], 'g-', lw=2, label='Vector P - O₁')

# Annotation text for displaying new coordinates of P.
annotation = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, fontsize=12, color='darkred', weight='bold')

def init():
    new_origin_marker.set_data([], [])
    new_origin_marker.set_3d_properties([])
    new_axisX_line.set_data([], [])
    new_axisX_line.set_3d_properties([])
    new_axisY_line.set_data([], [])
    new_axisY_line.set_3d_properties([])
    new_axisZ_line.set_data([], [])
    new_axisZ_line.set_3d_properties([])
    vector_line.set_data([], [])
    vector_line.set_3d_properties([])
    annotation.set_text("")
    return new_origin_marker, new_axisX_line, new_axisY_line, new_axisZ_line, vector_line, annotation

def update(frame):
    # Let t go from 0 to 1 for frames 0 to 100.
    t = frame / 100.0
    # New origin O₁ moves linearly from (0,0,0) to (alpha, beta, gamma).
    O1 = np.array([alpha * t, beta * t, gamma * t])
    
    # Update new origin marker.
    new_origin_marker.set_data([O1[0]], [O1[1]])
    new_origin_marker.set_3d_properties([O1[2]])
    
    # Define new coordinate axes (keeping directions the same as original).
    L_new = 3  # Axis length for new coordinate frame for visualization.
    X1 = O1 + np.array([L_new, 0, 0])
    Y1 = O1 + np.array([0, L_new, 0])
    Z1 = O1 + np.array([0, 0, L_new])
    
    # Update new axes lines.
    new_axisX_line.set_data([O1[0], X1[0]], [O1[1], X1[1]])
    new_axisX_line.set_3d_properties([O1[2], X1[2]])
    
    new_axisY_line.set_data([O1[0], Y1[0]], [O1[1], Y1[1]])
    new_axisY_line.set_3d_properties([O1[2], Y1[2]])
    
    new_axisZ_line.set_data([O1[0], Z1[0]], [O1[1], Z1[1]])
    new_axisZ_line.set_3d_properties([O1[2], Z1[2]])
    
    # Compute new coordinates of P relative to O₁:
    # P_new = P - O₁, i.e. x₁ = x - O1_x, etc.
    P_new = P - O1
    
    # Draw a vector from the new origin O₁ to P, to illustrate the transformation.
    vector_line.set_data([O1[0], P[0]], [O1[1], P[1]])
    vector_line.set_3d_properties([O1[2], P[2]])
    
    # Update annotation to display the new coordinates of P.
    annotation_text = f"P in new frame: ({P_new[0]:.2f}, {P_new[1]:.2f}, {P_new[2]:.2f})"
    annotation.set_text(annotation_text)
    
    return new_origin_marker, new_axisX_line, new_axisY_line, new_axisZ_line, vector_line, annotation

# Create animation: frames 0 to 100.
ani = FuncAnimation(fig, update, frames=101, init_func=init, interval=50, blit=False)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()