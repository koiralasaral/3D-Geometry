import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Bar pendulum data: distances (d) and periods (T)
data = [
    (10, 1.5), (20, 1.7), (30, 1.9), (40, 2.1),
    (50, 2.3), (60, 2.5), (70, 2.7), (80, 2.9)
]

# Constants
g = 9.81  # gravity acceleration in m/s^2

# Calculate intermediate values
lengths = []
k_squared = []
for d, T in data:
    T_sec = T  # Assuming T is given in seconds
    k2 = ((T_sec ** 2 * g) / (4 * np.pi ** 2)) - (d ** 2)
    lengths.append(d)
    k_squared.append(k2)
    print(f"For d = {d} cm, T = {T} s: k² = {k2:.2f} cm²")

radius_of_gyration = np.sqrt(np.mean(k_squared))
print(f"\nRadius of Gyration (k) = {radius_of_gyration:.2f} cm")

# Parabola and lines
x = np.linspace(0, 100, 500)
y = (x - radius_of_gyration) ** 2 / radius_of_gyration

fig, ax = plt.subplots()
ax.plot(x, y, label="Parabola")
ax.plot([10, 30], [10, 30], 'r-', label="Line AB")
ax.plot([50, 70], [50, 70], 'g-', label="Line CD")
ax.plot([20, 40], [20, 40], 'b--', label="Line A'B'")
ax.plot([60, 80], [60, 80], 'y--', label="Line C'D'")
ax.set_xlabel("X-axis (cm)")
ax.set_ylabel("Y-axis (cm)")
ax.legend()
ax.set_title("Parabola and Lines")
plt.show()

# Create 3D animation for the bar pendulum
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize pendulum data
t = np.linspace(0, 2 * np.pi, 100)
x = lengths[0] * np.sin(t)
y = lengths[0] * np.cos(t)
z = np.zeros_like(t)

line, = ax.plot(x, y, z, label="Bar Pendulum")
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(-100, 100)
ax.legend()

def update(frame):
    d = lengths[frame % len(lengths)]
    line.set_data(d * np.sin(t), d * np.cos(t))
    line.set_3d_properties(d * np.sin(t / 2))
    return line,

ani = FuncAnimation(fig, update, frames=len(lengths), blit=False, repeat=True)
plt.show()