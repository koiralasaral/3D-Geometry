import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81
true_k = 0.3  # True radius of gyration (m) - to be determined

# Experimental setup
h_values = np.linspace(0.2, 0.8, 5)  # Pivot distances from COM (m)
trials = 5
noise_level = 0.02  # Measurement noise

# Generate simulated data
data = []
for h in h_values:
    for _ in range(trials):
        T = 2 * np.pi * np.sqrt((true_k**2 + h**2) / (g * h))
        T_noisy = T * (1 + np.random.normal(0, noise_level))
        data.append({
            'h': h,
            'T': T_noisy
        })

df = pd.DataFrame(data)
df['k_calculated'] = np.sqrt((g * df['T']**2 * df['h']) / (4 * np.pi**2) - df['h']**2)
df.to_csv('bar_pendulum_data.csv', index=False)

# Calculate mean radius of gyration
mean_k = df['k_calculated'].mean()

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(df['h'], df['k_calculated'], c='blue', label='Trials')
plt.hlines(mean_k, df['h'].min(), df['h'].max(), colors='red', 
           label=f'Mean k = {mean_k:.3f} m')
plt.xlabel('Pivot Distance (h) [m]')
plt.ylabel('Radius of Gyration (k) [m]')
plt.title('Radius of Gyration Calculation')
plt.legend()
plt.grid(True)
plt.savefig('k_results.png')
plt.show()

# Animation
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1.2, 0.2)
ax.set_aspect('equal')
ax.axis('off')

# Pendulum components
rod, = ax.plot([], [], 'k-', lw=3)
com = ax.scatter([], [], c='red', s=100)
k_marker = ax.scatter([], [], c='blue', s=50)

def init():
    rod.set_data([], [])
    com.set_offsets([[0, 0]])
    k_marker.set_offsets([[0, 0]])
    return rod, com, k_marker

def update(frame):
    t = frame/10
    theta_max = np.radians(20)
    theta = theta_max * np.cos(2 * np.pi * t / 1.5)  # Arbitrary period for visualization
    
    # Pendulum position
    x_pivot = 0
    y_pivot = 0
    x_com = -h * np.sin(theta)
    y_com = -h * np.cos(theta)
    
    # Rod endpoints
    x_rod = [x_pivot, x_com * 2]
    y_rod = [y_pivot, y_com * 2]
    
    rod.set_data(x_rod, y_rod)
    com.set_offsets([[x_com, y_com]])
    
    # Radius of gyration markers
    k_x = [x_com + mean_k * np.cos(theta), x_com - mean_k * np.cos(theta)]
    k_y = [y_com + mean_k * np.sin(theta), y_com - mean_k * np.sin(theta)]
    k_marker.set_offsets(np.c_[k_x, k_y])
    
    return rod, com, k_marker

ani = FuncAnimation(fig, update, frames=150, init_func=init, blit=True)
ani.save('pendulum.gif', writer='pillow', fps=20)