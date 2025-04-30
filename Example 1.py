import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Define the plane: 2x - 3y + 2z = 4.
# We can express the plane in the form:
#    2x - 3y + 2z - 4 = 0.
#
# To plot the surface, we solve for z:
#    2z = 4 - 2x + 3y  =>  z = (4 - 2x + 3y) / 2.
# -----------------------------

# Create grid values for x and y:
x_vals = np.linspace(-4, 4, 40)
y_vals = np.linspace(-4, 4, 40)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (4 - 2 * X + 3 * Y) / 2

# -----------------------------
# Compute the intercepts on the axes.
# -----------------------------
# x-intercept: set y=0, z=0   => 2x = 4  =>  x = 2.
A = np.array([2, 0, 0])  # A = (2, 0, 0)

# y-intercept: set x=0, z=0   => -3y = 4  =>  y = -4/3.
B = np.array([0, -4/3, 0])  # B = (0, -4/3, 0)

# z-intercept: set x=0, y=0   => 2z = 4  =>  z = 2.
C = np.array([0, 0, 2])  # C = (0, 0, 2)

# -----------------------------
# Compute the distance from the origin (O = (0,0,0)) to the plane.
#
# For a plane written as: Ax + By + Cz = D,
# the distance from the origin is:
#     d = |D| / sqrt(A^2 + B^2 + C^2).
#
# Here A = 2, B = -3, C = 2 and D = 4.
# -----------------------------
d = 4 / np.sqrt(2**2 + (-3)**2 + 2**2)  # = 4 / sqrt(4 + 9 + 4) = 4/sqrt(17)

# -----------------------------
# Compute the foot of the perpendicular from the origin to the plane.
#
# For the plane 2x - 3y + 2z - 4 = 0, the foot P from O is given by:
#   P = -D/(A^2+B^2+C^2) * (A, B, C),
# where now we treat D as the constant from the equation written in form 2x-3y+2z-4 = 0,
# that is, D = -4. Thus:
#   P = -(-4)/(4+9+4) * (2, -3, 2) = (4/17)*(2, -3, 2).
# -----------------------------
P = (4 / 17) * np.array([2, -3, 2])
O = np.array([0, 0, 0])  # Origin

# -----------------------------
# Print the intermediate values.
# -----------------------------
print("Intermediate Values:")
print(f"Plane equation: 2x - 3y + 2z = 4")
print(f"x-intercept A: {A}")         # (2, 0, 0)
print(f"y-intercept B: {B}")         # (0, -4/3, 0)
print(f"z-intercept C: {C}")         # (0, 0, 2)
print(f"Distance from O to plane d: {d:.4f}")
print(f"Foot of the perpendicular P: {P}")

# -----------------------------
# Set up the figure and 3D axes.
# -----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface.
plane = ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha=0.5, edgecolor="none")

# Plot the intercept points.
ax.scatter(A[0], A[1], A[2], color="green", s=50, label="x-intercept A (2, 0, 0)")
ax.scatter(B[0], B[1], B[2], color="purple", s=50, label="y-intercept B (0, -4/3, 0)")
ax.scatter(C[0], C[1], C[2], color="orange", s=50, label="z-intercept C (0, 0, 2)")

# Label the origin and the foot of the perpendicular.
ax.scatter(O[0], O[1], O[2], color="black", s=50, label="Origin O (0,0,0)")
ax.scatter(P[0], P[1], P[2], color="red", s=50, label=f"Foot P ({P[0]:.2f}, {P[1]:.2f}, {P[2]:.2f})")

# Draw a line from the origin to the foot of the perpendicular.
ax.plot([O[0], P[0]], [O[1], P[1]], [O[2], P[2]], "k--", linewidth=3, label=f"Distance d = {d:.2f}")

# Optionally, connect the intercepts to form a triangle.
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color="gray", linestyle=":", linewidth=2)
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color="gray", linestyle=":", linewidth=2)
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], color="gray", linestyle=":", linewidth=2)

# Annotate the intercept points and key points.
ax.text(A[0], A[1], A[2], "  A", color="green", fontsize=12)
ax.text(B[0], B[1], B[2], "  B", color="purple", fontsize=12)
ax.text(C[0], C[1], C[2], "  C", color="orange", fontsize=12)
ax.text(O[0], O[1], O[2], "  O", color="black", fontsize=12)
ax.text(P[0], P[1], P[2], "  P", color="red", fontsize=12)

# Set the labels and title.
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Plane: 2x - 3y + 2z = 4\nIntercepts & Distance from Origin")

# Add legend and colorbar.
ax.legend(loc="upper left")
plt.colorbar(plane, shrink=0.5, aspect=10, label="Plane Surface")

plt.show()