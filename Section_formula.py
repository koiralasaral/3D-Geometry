from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def section_formula_3d(x1, y1, z1, x2, y2, z2, m, n):
    x = (m * x2 + n * x1) / (m + n)
    y = (m * y2 + n * y1) / (m + n)
    z = (m * z2 + n * z1) / (m + n)
    return x, y, z

# Coordinates of the points
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6

# Ratio m:n
m, n = 2, 3

# Calculate the coordinates of the point dividing the line segment
x, y, z = section_formula_3d(x1, y1, z1, x2, y2, z2, m, n)

# Plotting the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original points
ax.scatter(x1, y1, z1, color='blue', label='Point 1')
ax.scatter(x2, y2, z2, color='red', label='Point 2')

# Plot the calculated point
ax.scatter(x, y, z, color='green', label='Section Point')

# Plot the line segment
ax.plot([x1, x2], [y1, y2], [z1, z2], color='black')

# Labels and legend
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

plt.show()