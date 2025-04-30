import numpy as np
import matplotlib.pyplot as plt

# Grid of survey points
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)

# Simulate L (length constant) and synthetic T (time period with anomaly)
L = 0.75  # meters

# Time period: normal T = 1.74s, but faster (lower T) near mineral
T = 1.74 - 0.05 * np.exp(-((X-5)**2 + (Y-5)**2)/2)

# Calculate gravity
g_map = (4 * np.pi**2 * L) / T**2

# Plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, g_map, levels=30, cmap='viridis')
plt.colorbar(contour, label='g (m/s²)')
plt.title('Gravity Anomaly Map — Mineral Deposit (High g)')
plt.xlabel('X Position (km)')
plt.ylabel('Y Position (km)')
plt.grid(True)
plt.show()
# Reuse the same grid
L = 0.75

# Simulate gravity drop on one side of fault
T = np.where(X < 5, 1.74, 1.78)  # Right side slower (lower g)

# Calculate gravity
g_map_fault = (4 * np.pi**2 * L) / T**2

# Plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, g_map_fault, levels=30, cmap='coolwarm')
plt.colorbar(contour, label='g (m/s²)')
plt.title('Gravity Fault Line Map — Tectonic Boundary')
plt.xlabel('X Position (km)')
plt.ylabel('Y Position (km)')
plt.grid(True)
plt.show()
