import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# --------------------------
# Parameters of the simulation
# --------------------------
R = 5                    # Sphere radius
T_max = 100              # Total number of frames (i.e. time parameter)

# Drone: from (-10,0,0) to (10,0,0)
drone_start = np.array([-10, 0, 0])
drone_end   = np.array([10, 0, 0])

# Projectile: from (0, -10, 0) to (0, 0, 0) in 50 frames.
proj_start = np.array([0, -10, 0])
proj_end   = np.array([0,  0, 0])
T_proj = 50  # projectile intercept time

# Print intermediate values.
print("Intermediate Values:")
print("  Sphere Center: (0,0,0), Radius:", R)
print("  Drone starts at:", drone_start, "and ends at:", drone_end)
print("  Projectile starts at:", proj_start, "and reaches (0,0,0) at frame", T_proj)
print("  At frame", T_proj, "the drone's position =", drone_start + (drone_end - drone_start) * (T_proj/T_max))

# --------------------------
# Create figure and 3D axes.
# --------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_zlim(-12, 12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Drone Enters Sphere & Projectile Intercepts")

# --------------------------
# Plot the sphere (translucent surface)
# --------------------------
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
X_sphere = R * np.outer(np.cos(u), np.sin(v))
Y_sphere = R * np.outer(np.sin(u), np.sin(v))
Z_sphere = R * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(X_sphere, Y_sphere, Z_sphere, color='lightblue', alpha=0.3, edgecolor='none')
ax.plot_wireframe(X_sphere, Y_sphere, Z_sphere, color='blue', alpha=0.1)

# --------------------------
# Draw coordinate axes.
# --------------------------
axes_len = 12
ax.plot([-axes_len, axes_len], [0, 0], [0, 0], 'k--', linewidth=1)
ax.plot([0, 0], [-axes_len, axes_len], [0, 0], 'k--', linewidth=1)
ax.plot([0, 0], [0, 0], [-axes_len, axes_len], 'k--', linewidth=1)

# --------------------------
# Initialize the drone and projectile markers.
# --------------------------
drone_marker, = ax.plot([], [], [], 'bo', markersize=8, label='Drone')
proj_marker,  = ax.plot([], [], [], 'ro', markersize=8, label='Projectile')
collision_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, fontsize=12, color='red', weight='bold')

# --------------------------
# Animation update function
# --------------------------
def update(frame):
    # Normalized time for drone
    t = frame / T_max
    drone_pos = drone_start + (drone_end - drone_start) * t

    # Use sequences (lists) for set_data.
    drone_marker.set_data([drone_pos[0]], [drone_pos[1]])
    drone_marker.set_3d_properties([drone_pos[2]])
    
    # Update projectile position.
    if frame <= T_proj:
        t_proj = frame / T_proj
        proj_pos = proj_start + (proj_end - proj_start) * t_proj
    else:
        proj_pos = proj_end
    proj_marker.set_data([proj_pos[0]], [proj_pos[1]])
    proj_marker.set_3d_properties([proj_pos[2]])
    
    # Check if the drone is inside the sphere.
    dist_drone = np.linalg.norm(drone_pos)
    if dist_drone < R:
        status = "Drone Inside Sphere"
    else:
        status = "Drone Outside Sphere"
    
    # Check for collision.
    if np.linalg.norm(drone_pos - proj_pos) < 0.5:
        collision_text.set_text("Collision Occurred!")
        drone_marker.set_color('magenta')
        proj_marker.set_color('magenta')
    else:
        collision_text.set_text(status)
        drone_marker.set_color('blue')
        proj_marker.set_color('red')
    
    return drone_marker, proj_marker, collision_text

# --------------------------
# Create the animation.
# --------------------------
ani = FuncAnimation(fig, update, frames=np.arange(0, T_max+1), interval=50, blit=False)

ax.legend(loc="upper left")
plt.show()