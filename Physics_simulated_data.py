import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated data: Length (m) and Time Period (s)
data = [
    {'L': 0.50, 'T': 1.42},
    {'L': 0.55, 'T': 1.49},
    {'L': 0.60, 'T': 1.55},
    {'L': 0.65, 'T': 1.61},
    {'L': 0.70, 'T': 1.68},
    {'L': 0.75, 'T': 1.74},
    {'L': 0.80, 'T': 1.79},
    {'L': 0.85, 'T': 1.85},
    {'L': 0.90, 'T': 1.91},
    {'L': 0.95, 'T': 1.96},
]

# Calculate g for each trial
results = []
for trial in data:
    L = trial['L']
    T = trial['T']
    g_calc = (4 * np.pi**2 * L) / T**2
    results.append({'Length (m)': L, 'Time (s)': T, 'Calculated g (m/s²)': g_calc})
    print(f"L = {L:.2f} m, T = {T:.2f} s → g = {g_calc:.4f} m/s²")

# Create DataFrame
df = pd.DataFrame(results)

# Stats
g_values = df['Calculated g (m/s²)'].values
mean_g = np.mean(g_values)
std_dev = np.std(g_values, ddof=1)
std_err = std_dev / np.sqrt(len(g_values))

print("\n=== Summary Statistics ===")
print(f"Mean g: {mean_g:.4f} m/s²")
print(f"Standard Deviation: {std_dev:.4f} m/s²")
print(f"Standard Error: {std_err:.4f} m/s²")

# Plot Histogram
plt.figure(figsize=(8, 5))
plt.hist(g_values, bins=6, edgecolor='black', color='lightgreen')
plt.axvline(mean_g, color='red', linestyle='--', label=f"Mean = {mean_g:.4f}")
plt.title("Histogram of Calculated g Values")
plt.xlabel("g (m/s²)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Simulated data again
data = [
    {'L': 0.50, 'T': 1.42},
    {'L': 0.55, 'T': 1.49},
    {'L': 0.60, 'T': 1.55},
    {'L': 0.65, 'T': 1.61},
    {'L': 0.70, 'T': 1.68},
    {'L': 0.75, 'T': 1.74},
    {'L': 0.80, 'T': 1.79},
    {'L': 0.85, 'T': 1.85},
    {'L': 0.90, 'T': 1.91},
    {'L': 0.95, 'T': 1.96},
]

# Prepare data
L = np.array([entry['L'] for entry in data])
T = np.array([entry['T'] for entry in data])
T_squared = T**2

# Linear regression T² = mL + c
slope, intercept, r_value, p_value, std_err = linregress(L, T_squared)
g_fit = 4 * np.pi**2 / slope

print(f"Fitted Line: T² = {slope:.4f}·L + {intercept:.4f}")
print(f"Calculated g from fit: {g_fit:.4f} m/s²")
print(f"R-squared: {r_value**2:.5f} (goodness of fit)")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(L, T_squared, 'o', label='Measured T²')
plt.plot(L, slope * L + intercept, 'r--', label=f'Fit: T² = {slope:.3f}·L + {intercept:.3f}')
plt.xlabel('Length (m)')
plt.ylabel('Time² (s²)')
plt.title('T² vs Length — Linear Fit')
plt.legend()
plt.grid(True)
plt.show()
