import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s²
I = 0.1   # kg·m²

# Experimental data
data = [
    {'mass': 0.6, 'cases': [(0.80, 11), (0.72, 10), (0.65, 9), (0.58, 8)]},
    {'mass': 0.4, 'cases': [(0.80, 11), (0.72, 10), (0.65, 9), (0.58, 8)]}
]

# Calculate results
results = []
for entry in data:
    mass = entry['mass']
    for L, N in entry['cases']:
        r = L / (2 * np.pi * N)
        numerator = mass * g * r
        denominator = I + mass * r**2
        alpha = numerator / denominator
        t = np.sqrt(4 * np.pi * N / alpha)
        results.append({
            'Mass (kg)': mass,
            'L (m)': L,
            'N': N,
            'r (m)': r,
            'Alpha (rad/s²)': alpha,
            'Time (s)': t
        })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv('alpha_data.csv', index=False)

# Plotting
plt.figure(figsize=(10, 6))
for mass in [0.6, 0.4]:
    subset = df[df['Mass (kg)'] == mass]
    plt.plot(subset['L (m)'], subset['Alpha (rad/s²)'], 'o-', label=f'{mass} kg')
plt.xlabel('Thread Length (m)')
plt.ylabel('Angular Acceleration (rad/s²)')
plt.title('Angular Acceleration vs. Thread Length')
plt.legend()
plt.grid(True)
plt.savefig('alpha_vs_length.png')
plt.show()

plt.figure(figsize=(10, 6))
for mass in [0.6, 0.4]:
    subset = df[df['Mass (kg)'] == mass]
    plt.plot(subset['N'], subset['Alpha (rad/s²)'], 'o-', label=f'{mass} kg')
plt.xlabel('Number of Turns')
plt.ylabel('Angular Acceleration (rad/s²)')
plt.title('Angular Acceleration vs. Number of Turns')
plt.legend()
plt.grid(True)
plt.savefig('alpha_vs_turns.png')
plt.show()

# First case calculation
L_first, N_first, mass_first = 0.875, 12, 0.6
r_first = L_first / (2 * np.pi * N_first)
alpha_first = (mass_first * g * r_first) / (I + mass_first * r_first**2)
t_first = np.sqrt(4 * np.pi * N_first / alpha_first)

print(f"Case: L={L_first}m, N={N_first}, Mass={mass_first}kg")
print(f"Radius: {r_first:.4f} m")
print(f"Alpha: {alpha_first:.3f} rad/s²")
print(f"Time: {t_first:.2f} s")