import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of trials
n_trials = 8

# Simulate random distances (l1 and l2 in meters) using Monte Carlo sampling
np.random.seed(42)
l1 = np.random.uniform(0.10, 0.50, n_trials)  # l1 ranges from 10 cm to 50 cm
l2 = np.random.uniform(0.10, 0.50, n_trials)  # l2 ranges from 10 cm to 50 cm

# Calculate radius of gyration for each trial
k = np.sqrt(l1 * l2)

# Print observation table
print("Observation Table:")
print("{:<6} {:<10} {:<10} {:<10}".format("Trial", "l1 (m)", "l2 (m)", "k (m)"))
for i in range(n_trials):
    print("{:<6} {:<10.3f} {:<10.3f} {:<10.3f}".format(i+1, l1[i], l2[i], k[i]))

# Plot l1, l2, and k
plt.figure(figsize=(8, 6))
plt.plot(range(1, n_trials + 1), l1, marker='o', label="l1 (m)", color='blue')
plt.plot(range(1, n_trials + 1), l2, marker='s', label="l2 (m)", color='green')
plt.plot(range(1, n_trials + 1), k, marker='^', label="k (m)", color='red')
plt.xlabel("Trial Number")
plt.ylabel("Length (m)")
plt.title("Observation of l1, l2, and k")
plt.legend()
plt.grid(True)
plt.show()

# Animation of a swinging bar pendulum
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-1, 0.2)
ax.set_aspect('equal')
ax.set_title("Bar Pendulum Animation")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")

line, = ax.plot([], [], 'o-', lw=3, color='purple')  # pendulum (bar) representation
pivot_point, = ax.plot(0, 0, 'ko', markersize=8)  # pivot point

def init():
    line.set_data([], [])
    return line, pivot_point

def update(frame):
    t = frame / 30.0  # time in seconds
    theta = np.deg2rad(10) * np.cos(2 * np.pi * t)  # oscillation (10 degrees)
    x1 = -l1[0] * np.sin(theta)  # One end of the bar
    y1 = -l1[0] * np.cos(theta)
    x2 = l2[0] * np.sin(theta)  # Other end of the bar
    y2 = -l2[0] * np.cos(theta)
    line.set_data([x1, x2], [y1, y2])
    return line, pivot_point

ani = FuncAnimation(fig, update, frames=300, init_func=init, interval=33, blit=True)
plt.show()