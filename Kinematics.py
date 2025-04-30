import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D plotting

# --- Define the Homogeneous Transformation Function ---
def transformation_matrix(theta, tx, ty, tz):
    """
    Returns a 4x4 homogeneous transformation matrix that rotates about the z-axis
    by angle theta (radians) and translates by (tx, ty, tz).
    """
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                   [np.sin(theta),  np.cos(theta), 0, 0],
                   [0,              0,             1, 0],
                   [0,              0,             0, 1]])
    T  = np.array([[1, 0, 0, tx],
                   [0, 1, 0, ty],
                   [0, 0, 1, tz],
                   [0, 0, 0, 1]])
    return T @ Rz  # First apply rotation, then translation.

# --- Set up the 3D figure and axes ---
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 8)
ax.set_zlim(-1, 8)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Rotation & Translation in Robotics\n(Changing Coordinate Frames)", fontsize=14)

# Draw static world (global) coordinate axes (solid arrows).
world_origin = np.array([0,0,0])
axis_length = 5
ax.quiver(world_origin[0], world_origin[1], world_origin[2],
          axis_length, 0, 0, color='blue', arrow_length_ratio=0.1, label='World X')
ax.quiver(world_origin[0], world_origin[1], world_origin[2],
          0, axis_length, 0, color='green', arrow_length_ratio=0.1, label='World Y')
ax.quiver(world_origin[0], world_origin[1], world_origin[2],
          0, 0, axis_length, color='purple', arrow_length_ratio=0.1, label='World Z')

# --- Define a fixed point P in the local coordinate system (of a sensor/tool)
# For example, let P_local = (2, 1, 0) in the new frame.
P_local = np.array([2, 1, 0, 1])  # expressed in homogeneous coordinates.

# --- Set up placeholders for the animated new coordinate frame and transformed point ---
# Markers for the new (local) coordinate frame axes:
new_origin_marker, = ax.plot([], [], [], 'ro', markersize=8, label='New Origin O₁')
new_axisX_line, = ax.plot([], [], [], 'r--', lw=2, label='New X₁-axis')
new_axisY_line, = ax.plot([], [], [], 'r--', lw=2, label='New Y₁-axis')
new_axisZ_line, = ax.plot([], [], [], 'r--', lw=2, label='New Z₁-axis')
# Marker for the transformed point (P expressed in world frame).
P_transformed_marker, = ax.plot([], [], [], 'ko', markersize=8, label='P (transformed)')

# A vector from the new origin to P (for illustration).
vector_line, = ax.plot([], [], [], 'g-', lw=2, label='P - O₁')

# Annotation to display the new coordinates of P relative to the new origin.
annotation = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, fontsize=12, color='darkred', weight='bold')

# --- Animation Initialization and Update Functions ---
def init():
    new_origin_marker.set_data([], [])
    new_origin_marker.set_3d_properties([])
    new_axisX_line.set_data([], [])
    new_axisX_line.set_3d_properties([])
    new_axisY_line.set_data([], [])
    new_axisY_line.set_3d_properties([])
    new_axisZ_line.set_data([], [])
    new_axisZ_line.set_3d_properties([])
    P_transformed_marker.set_data([], [])
    P_transformed_marker.set_3d_properties([])
    vector_line.set_data([], [])
    vector_line.set_3d_properties([])
    annotation.set_text("")
    return (new_origin_marker, new_axisX_line, new_axisY_line, 
            new_axisZ_line, P_transformed_marker, vector_line, annotation)

def update(frame):
    # Animate over 100 frames.
    # Let the rotation angle theta (radians) vary linearly from 0 to 2*pi.
    theta = 2 * np.pi * frame / 100.0
    # Let the translation vector vary linearly from (0,0,0) to (2,1,1).
    tx = 2 * frame / 100.0
    ty = 1 * frame / 100.0
    tz = 1 * frame / 100.0

    # Compute the homogeneous transformation matrix.
    T = transformation_matrix(theta, tx, ty, tz)
    
    # Compute the new origin (should equal T applied to (0,0,0,1)).
    O1_homog = T @ np.array([0,0,0,1])
    O1 = O1_homog[:3]
    
    # Compute the endpoints of the new axes.
    L_new = 3  # length for drawing the new axes.
    # New X₁-axis endpoint: T * [L_new, 0, 0, 1]
    X1_homog = T @ np.array([L_new, 0, 0, 1])
    Y1_homog = T @ np.array([0, L_new, 0, 1])
    Z1_homog = T @ np.array([0, 0, L_new, 1])
    
    X1 = X1_homog[:3]
    Y1 = Y1_homog[:3]
    Z1 = Z1_homog[:3]
    
    # Transform the local point P_local from the new frame to world coordinates.
    P_world_homog = T @ P_local
    P_world = P_world_homog[:3]
    
    # Update new coordinate frame markers.
    new_origin_marker.set_data([O1[0]], [O1[1]])
    new_origin_marker.set_3d_properties([O1[2]])
    
    new_axisX_line.set_data([O1[0], X1[0]], [O1[1], X1[1]])
    new_axisX_line.set_3d_properties([O1[2], X1[2]])
    
    new_axisY_line.set_data([O1[0], Y1[0]], [O1[1], Y1[1]])
    new_axisY_line.set_3d_properties([O1[2], Y1[2]])
    
    new_axisZ_line.set_data([O1[0], Z1[0]], [O1[1], Z1[1]])
    new_axisZ_line.set_3d_properties([O1[2], Z1[2]])
    
    # Update the transformed point marker.
    P_transformed_marker.set_data([P_world[0]], [P_world[1]])
    P_transformed_marker.set_3d_properties([P_world[2]])
    
    # Draw a vector from the new origin O₁ to the transformed point P (illustrates P - O₁).
    vector_line.set_data([O1[0], P_world[0]], [O1[1], P_world[1]])
    vector_line.set_3d_properties([O1[2], P_world[2]])
    
    # Update annotation with the coordinates of P relative to O₁.
    # Note: P in new frame is simply P_local; but here we show value after transformation.
    P_new = P_world - O1
    annotation_text = f"P in new frame: ({P_new[0]:.2f}, {P_new[1]:.2f}, {P_new[2]:.2f})"
    annotation.set_text(annotation_text)
    
    return (new_origin_marker, new_axisX_line, new_axisY_line, 
            new_axisZ_line, P_transformed_marker, vector_line, annotation)

# Create and run animation (frames 0 to 100).
ani = FuncAnimation(fig, update, frames=101, init_func=init, interval=50, blit=False)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()