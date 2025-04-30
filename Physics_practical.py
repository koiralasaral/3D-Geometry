import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # m/s²
r_axle = 0.02  # Axle radius (m)
I = 0.1  # Moment of inertia (kg·m²)
L = 1.0  # Thread length (m)
N = L / (2 * np.pi * r_axle)  # Number of turns

# Simulation parameters
masses = [0.6, 0.4]  # kg
trials = 5
noise_std = 0.15  # Time measurement noise

# Generate simulated data
data = []
for mass in masses:
    alpha_theo = (mass * g * r_axle) / (I + mass * r_axle**2)
    t_theo = np.sqrt(4 * np.pi * N / alpha_theo)
    
    for _ in range(trials):
        t_sim = np.random.normal(t_theo, noise_std)
        alpha_exp = (4 * np.pi * N) / t_sim**2
        data.append({
            'Mass (kg)': mass,
            'Length (m)': L,
            'Turns': N,
            'Time (s)': t_sim,
            'Alpha (rad/s²)': alpha_exp
        })

df = pd.DataFrame(data)
df.to_csv('flywheel_data.csv', index=False)

# Calculate mean angular acceleration
mean_alphas = df.groupby('Mass (kg)')['Alpha (rad/s²)'].mean()

# Plot results
plt.figure(figsize=(10, 6))
for mass in masses:
    subset = df[df['Mass (kg)'] == mass]
    plt.scatter([mass]*trials, subset['Alpha (rad/s²)'], 
                label=f'{mass} kg Trials', s=100)
    plt.hlines(mean_alphas[mass], mass-0.05, mass+0.05, 
               colors='red', linewidths=3, label='Mean' if mass == 0.6 else "")
plt.title('Angular Acceleration Measurements')
plt.xlabel('Mass (kg)')
plt.ylabel('Angular Acceleration (rad/s²)')
plt.legend()
plt.grid(True)
plt.savefig('alpha_results.png')
plt.show()

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Flywheel components
circle = plt.Circle((0, 0), 1, fc='none', ec='black', lw=2)
ax.add_patch(circle)
spoke, = ax.plot([], [], 'r-', lw=2)

def init():
    spoke.set_data([], [])
    return spoke,

def update(frame):
    theta = 0.5 * mean_alphas[0.6] * (frame/10)**2  # Using 600g mean alpha
    x = np.cos(theta)
    y = np.sin(theta)
    spoke.set_data([0, x], [0, y])
    return spoke,

ani = FuncAnimation(fig, update, frames=150, init_func=init, blit=True)
ani.save('flywheel.gif', writer='pillow', fps=20)