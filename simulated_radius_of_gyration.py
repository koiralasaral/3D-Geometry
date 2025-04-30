import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Simulated bar pendulum data
data = [
    {'side': 'A', 'd': 0.02, 'T': 1.80},
    {'side': 'A', 'd': 0.05, 'T': 1.72},
    {'side': 'A', 'd': 0.08, 'T': 1.68},
    {'side': 'A', 'd': 0.11, 'T': 1.70},
    {'side': 'B', 'd': 0.02, 'T': 1.79},
    {'side': 'B', 'd': 0.05, 'T': 1.71},
    {'side': 'B', 'd': 0.08, 'T': 1.66},
    {'side': 'B', 'd': 0.11, 'T': 1.69},
]

pi = np.pi
results = []

# Calculate g from T and d
for entry in data:
    d = entry['d']
    T = entry['T']
    g = 4 * pi**2 * (d**2) / (T**2 - (2 * pi * d / T)**2) if T != 0 else 0
    results.append({'Side': entry['side'], 'd (m)': d, 'T (s)': T, 'g (m/s²)': g})

df = pd.DataFrame(results)

# Split and compute averages
side_a = df[df['Side'] == 'A']
side_b = df[df['Side'] == 'B']
g_avg_a = side_a['g (m/s²)'].mean()
g_avg_b = side_b['g (m/s²)'].mean()
g_avg = df['g (m/s²)'].mean()

# l1, l2 (minimum time positions)
l1 = side_a.loc[side_a['T (s)'].idxmin(), 'd (m)']
l2 = side_b.loc[side_b['T (s)'].idxmin(), 'd (m)']
k = np.sqrt(l1 * l2)  # radius of gyration

# Plot raw data
plt.figure(figsize=(10, 6))
plt.plot(side_a['d (m)'], side_a['T (s)'], 'o-', label="Side A", color='blue')
plt.plot(side_b['d (m)'], side_b['T (s)'], 's--', label="Side B", color='green')
plt.axvline(x=l1, color='blue', linestyle=':', label="l1 (min T A)")
plt.axvline(x=l2, color='green', linestyle=':', label="l2 (min T B)")
plt.annotate("A", xy=(0.02, 1.80), xytext=(0.015, 1.81), fontsize=12)
plt.annotate("B", xy=(0.11, 1.80), xytext=(0.115, 1.81), fontsize=12)
plt.annotate("D'", xy=(0.02, 1.79), xytext=(0.015, 1.80), fontsize=12)
plt.annotate("C'", xy=(0.11, 1.79), xytext=(0.115, 1.80), fontsize=12)
plt.xlabel("Distance from C.G. (m)")
plt.ylabel("Time Period T (s)")
plt.title("Bar Pendulum: Time vs Distance from C.G.")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Curve Fitting ===

# Combine and sort data
df_sorted = df.sort_values(by='d (m)')

# Model: T = A + B * d^2
def model(d, A, B):
    return A + B * d**2

# Fit model
popt, _ = curve_fit(model, df_sorted['d (m)'], df_sorted['T (s)'])
A_fit, B_fit = popt

# Generate fit curve
d_vals = np.linspace(0, 0.12, 200)
T_fit = model(d_vals, A_fit, B_fit)

# Plot fit
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['d (m)'], df_sorted['T (s)'], 'o', label='Observed Data', color='black')
plt.plot(d_vals, T_fit, '-', label=f'Fitted Curve: T = {A_fit:.3f} + {B_fit:.3f}·d²', color='red')
plt.xlabel('Distance from C.G. (m)')
plt.ylabel('Time Period T (s)')
plt.title('Curve Fitting: Time Period vs Distance from C.G.')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print summary
print("\n=== Summary ===")
print(f"Side A average g: {g_avg_a:.5f} m/s²")
print(f"Side B average g: {g_avg_b:.5f} m/s²")
print(f"Overall average g: {g_avg:.5f} m/s²")
print(f"l1 (Side A, min T): {l1:.3f} m")
print(f"l2 (Side B, min T): {l2:.3f} m")
print(f"Radius of Gyration k = √(l1 * l2): {k:.4f} m")
print(f"Fitted model: T = {A_fit:.3f} + {B_fit:.3f}·d²")
