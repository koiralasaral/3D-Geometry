import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D plotting

# -----------------------------
# Step 1. Define the intercept values.
# -----------------------------
a = 2.0  # x-intercept
b = 3.0  # y-intercept
c = 4.0  # z-intercept

# Using the intercept form:
#   x/2 + y/3 + z/4 = 1
intercept_form = "x/2 + y/3 + z/4 = 1"

# Multiply by 12 to obtain the standard form:
#   6x + 4y + 3z = 12
standard_form  = "6x + 4y + 3z = 12"

# Solve for z from the standard form:
#   3z = 12 - 6x - 4y  -->  z = (12 - 6x - 4y) / 3
z_expression = "z = (12 - 6x - 4y) / 3"

# -----------------------------
# Step 2. Compute the intercept points.
# -----------------------------
A = np.array([a, 0, 0])
B = np.array([0, b, 0])
C = np.array([0, 0, c])

# Print the intermediate values.
print("Intermediate Values:")
print("Intercept form of the plane: " + intercept_form)
print("Standard form of the plane: " + standard_form)
print("Expression for z: " + z_expression)
print("x-intercept A:", A)
print("y-intercept B:", B)
print("z-intercept C:", C)

# -----------------------------
# Step 3. Create a grid and compute Z for the plane.
# -----------------------------
# Since the intercepts are limited, choose x and y ranges that capture the intercepts.
x_vals = np.linspace(-1, 3, 100)
y_vals = np.linspace(-1, 4, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (12 - 6 * X - 4 * Y) / 3

# -----------------------------
# Step 4. Plotting the plane and labeling the points.
# -----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface.
plane = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='none')

# Plot the intercept points.
ax.scatter(A[0], A[1], A[2], color="red", s=50, label="A (2, 0, 0)")
ax.scatter(B[0], B[1], B[2], color="blue", s=50, label="B (0, 3, 0)")
ax.scatter(C[0], C[1], C[2], color="green", s=50, label="C (0, 0, 4)")

# Annotate the intercept points.
ax.text(A[0], A[1], A[2], "  A", color="red", fontsize=12)
ax.text(B[0], B[1], B[2], "  B", color="blue", fontsize=12)
ax.text(C[0], C[1], C[2], "  C", color="green", fontsize=12)

# Set the axes labels and title.
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Plane with Intercepts (2, 3, 4)\n" + intercept_form + "\nor " + standard_form)

# Add a legend.
ax.legend(loc="upper right")

# Overlay a text box with the intermediate formulas.
formula_text = (
    f"Intercept form: {intercept_form}\n"
    f"Standard form: {standard_form}\n"
    f"{z_expression}\n"
    f"Intercepts:\n  A (2,0,0),  B (0,3,0),  C (0,0,4)"
)
ax.text2D(0.05, 0.95, formula_text, transform=ax.transAxes, fontsize=10,
          verticalalignment='top', bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.show()