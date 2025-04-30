import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # enables 3D plotting

# =============================================================================
# PARAMETERS
# =============================================================================

# Define the new origin (O₁) as (α, β, γ)
alpha, beta, gamma = 2, -1, 3
O1 = np.array([alpha, beta, gamma])  # New origin

# Original coordinate system origin
O = np.array([0, 0, 0])

# Define a point P in the original coordinate system.
P = np.array([4, 5, 7])

# Compute the coordinates of P in the new system:
# new coordinates = P - O1.
P_new = P - O1  # (4-2, 5-(-1), 7-3) = (2, 6, 4)

# Define N as a point on the original xy-plane that is the vertical projection of O₁.
N = np.array([alpha, beta, 0])  # (2, -1, 0)

# Define M as the projection of P onto the original xy-plane (z = 0).
M = np.array([P[0], P[1], 0])   # (4, 5, 0)

# Define M₁ as the projection of P onto the new x₁y₁ plane.
# Since the new x₁y₁ plane has new z-coordinate = 0, in original coordinates z = γ.
M1 = np.array([P[0], P[1], gamma])  # (4, 5, 3)

# =============================================================================
# PLOTTING
# =============================================================================

# Create a 3D figure.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Draw original coordinate axes from O ---
axis_len = 10
ax.quiver(O[0], O[1], O[2], axis_len, 0, 0, color='red', arrow_length_ratio=0.1, label='Original X-axis')
ax.quiver(O[0], O[1], O[2], 0, axis_len, 0, color='green', arrow_length_ratio=0.1, label='Original Y-axis')
ax.quiver(O[0], O[1], O[2], 0, 0, axis_len, color='blue', arrow_length_ratio=0.1, label='Original Z-axis')

# --- Draw new coordinate axes from O₁ (parallel to original ones) ---
ax.quiver(O1[0], O1[1], O1[2], axis_len, 0, 0, color='magenta', arrow_length_ratio=0.1, linestyle='dashed', label='New X₁-axis')
ax.quiver(O1[0], O1[1], O1[2], 0, axis_len, 0, color='orange', arrow_length_ratio=0.1, linestyle='dashed', label='New Y₁-axis')
ax.quiver(O1[0], O1[1], O1[2], 0, 0, axis_len, color='cyan', arrow_length_ratio=0.1, linestyle='dashed', label='New Z₁-axis')

# --- Plot key points and annotate ---
ax.scatter(P[0], P[1], P[2], color='black', s=80, label='P (4, 5, 7)')
ax.text(P[0], P[1], P[2], f'  P\n(orig) & (new: {P_new})', color='black', fontsize=10)

ax.scatter(O1[0], O1[1], O1[2], color='purple', s=80, label=f'O₁ ({alpha}, {beta}, {gamma})')

ax.scatter(N[0], N[1], N[2], color='brown', s=80, label='N (Projection of O₁ on xy)')
ax.scatter(M[0], M[1], M[2], color='gray', s=80, label='M (Projection of P on xy)')
ax.scatter(M1[0], M1[1], M1[2], color='teal', s=80, label='M₁ (Projection of P on new x₁y₁)')

# --- Draw lines for the various perpendiculars ---
# From P to M (perpendicular to original xy-plane):
ax.plot([P[0], M[0]], [P[1], M[1]], [P[2], M[2]], color='gray', linestyle='--', label='P to M (xy perp.)')

# From P to M₁ (perpendicular to new x₁y₁-plane):
ax.plot([P[0], M1[0]], [P[1], M1[1]], [P[2], M1[2]], color='teal', linestyle='--', label='P to M₁ (new source perp.)')

# Draw O₁N (line from new origin to its projection on xy-plane)
ax.plot([O1[0], N[0]], [O1[1], N[1]], [O1[2], N[2]], color='purple', linestyle='--', label='O₁N')

# --- Draw a line from O₁ to P (for reference) ---
ax.plot([O1[0], P[0]], [O1[1], P[1]], [O1[2], P[2]], color='black', linestyle=':', label='O₁P')

# =============================================================================
# FORMAT THE PLOT
# =============================================================================
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Change of Origin: Original vs. New Coordinate Axes\nand Projections of P", fontsize=14)

# Set reasonable limits
ax.set_xlim(-2, 12)
ax.set_ylim(-4, 12)
ax.set_zlim(-2, 12)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()