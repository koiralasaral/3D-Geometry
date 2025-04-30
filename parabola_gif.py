import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Constants
pi = np.pi

# Example Data: Time for 20 oscillations (in seconds) and lengths (in meters)
lengths = np.array([0.5, 0.6])  # Pendulum lengths
times_20 = np.array([25.2, 30.0])  # Time for 20 oscillations
time_periods = times_20 / 20  # Time period per oscillation (T)

# Compute l/t^2 and gravitational acceleration (g)
lt2_values = lengths / time_periods**2  # l/t^2
mean_lt2 = np.mean(lt2_values)  # Mean l/t^2
g_values = 4 * pi**2 * lt2_values  # g = 4π² * l/t²
mean_g = np.mean(g_values)  # Mean g

# Create Table
print("Observation Table:")
print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Trial", "Length (m)", "Time (s)", "T (s)", "l/T² (m/s²)"))
for i in range(len(lengths)):
    print("{:<10} {:<15.3f} {:<15.3f} {:<15.3f} {:<15.3f}".format(
        i+1, lengths[i], times_20[i], time_periods[i], lt2_values[i]))
print(f"\nMean l/T²: {mean_lt2:.3f} m/s²")
print(f"Mean g: {mean_g:.3f} m/s²")

# Plot l/t² vs Length
plt.figure(figsize=(8, 6))
plt.scatter(lengths, lt2_values, color='blue', label='l/T²')
plt.axhline(mean_lt2, color='red', linestyle='--', label=f"Mean l/T² = {mean_lt2:.3f}")
plt.xlabel("Length (m)")
plt.ylabel("l/T² (m/s²)")
plt.title("Variation of l/T² with Length")
plt.legend()
plt.grid(True)
plt.show()

# Plot AD, BE, A'D', B'E' on a parabola curve
x = np.linspace(0, 1, 100)
y = x**2 / 0.5  # Parabola equation (example scaling)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Parabola Curve', color='blue')
plt.scatter([0.2, 0.4, 0.6], [0.08, 0.16, 0.36], color='red', label='Measured Points')
plt.text(0.2, 0.08, 'AD', color='purple')
plt.text(0.4, 0.16, 'BE', color='green')
plt.text(0.6, 0.36, "A'D'", color='orange')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Parabola Curve with Measured Distances")
plt.legend()
plt.grid(True)
plt.show()

# Animation of Pendulum Swing
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-1.2, 0.2)
ax.set_aspect('equal')
ax.set_title("Pendulum Swing Animation")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")

line, = ax.plot([], [], 'o-', lw=3, color='purple')  # pendulum (line representation)
pivot_point, = ax.plot(0, 0, 'ko', markersize=8)  # fixed pivot point

def init():
    line.set_data([], [])
    return line, pivot_point

def update(frame):
    t = frame / 30.0  # time in seconds
    theta = np.deg2rad(10) * np.cos(2 * pi * t / time_periods[0])  # oscillation (10°)
    x = lengths[0] * np.sin(theta)
    y = -lengths[0] * np.cos(theta)
    line.set_data([0, x], [0, y])
    return line, pivot_point

ani = FuncAnimation(fig, update, frames=300, init_func=init, interval=33, blit=True)

# Save animation as GIF
ani.save("pendulum_animation.gif", writer=PillowWriter(fps=30))
print("Pendulum animation saved as pendulum_animation.gif.")
plt.show()