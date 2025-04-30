import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------------------
# 1. Define the given points and ratio.
# ---------------------
A = np.array([1, 4, 5])
B = np.array([7, 10, 12])
m1, m2 = 2, 3  # Ratio m1:m2

# ---------------------
# 2. Compute point C dividing AB internally.
#    Using the section formula:
#      C = ( (m2*A + m1*B) / (m1 + m2) )
# ---------------------
C = (m2 * A + m1 * B) / (m1 + m2)
print("Computed C =", C)  # Expected approximately (3.4, 6.4, 7.8)

# ---------------------
# 3. Compute the perpendicular projections onto XOY (z=0).
# ---------------------
M = np.array([A[0], A[1], 0])      # Projection of A
N = np.array([B[0], B[1], 0])      # Projection of B
L = np.array([C[0], C[1], 0])      # Projection of C

# ---------------------
# 4. Choose a horizontal level h for our horizontal line.
# To ensure AQR is horizontal we choose h equal to A's z-coordinate.
# ---------------------
h = A[2]  # h = 5

# Define Q and R so that A, Q, and R are collinear and lie in z = h.
Q = np.array([C[0], C[1], h])       # (3.4, 6.4, 5)
R = np.array([B[0], B[1], h])       # (7, 10, 5)

# ---------------------
# 5. Set up the 3D plot.
# ---------------------
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# --- Draw the global coordinate axes ---
origin = np.array([0, 0, 0])
ax.quiver(origin[0], origin[1], origin[2], 15, 0, 0, color='red', 
          arrow_length_ratio=0.1, lw=2, label='X axis')
ax.quiver(origin[0], origin[1], origin[2], 0, 15, 0, color='green', 
          arrow_length_ratio=0.1, lw=2, label='Y axis')
ax.quiver(origin[0], origin[1], origin[2], 0, 0, 15, color='blue', 
          arrow_length_ratio=0.1, lw=2, label='Z axis')

# ---------------------
# Plot the primary points A, B, C.
# ---------------------
ax.scatter(A[0], A[1], A[2], color='blue', s=60, label="A")
ax.scatter(B[0], B[1], B[2], color='green', s=60, label="B")
ax.scatter(C[0], C[1], C[2], color='magenta', s=60, label="C")

# ---------------------
# Plot the projections M, N, L on the XOY plane.
# ---------------------
ax.scatter(M[0], M[1], M[2], color='blue', s=40, label="M (A projection)")
ax.scatter(N[0], N[1], N[2], color='green', s=40, label="N (B projection)")
ax.scatter(L[0], L[1], L[2], color='magenta', s=40, label="L (C projection)")

# ---------------------
# Draw vertical lines (perpendiculars).
# ---------------------
ax.plot([A[0], M[0]], [A[1], M[1]], [A[2], M[2]], color='gray', linestyle='--')
ax.plot([B[0], N[0]], [B[1], N[1]], [B[2], N[2]], color='gray', linestyle='--')
ax.plot([C[0], L[0]], [C[1], L[1]], [C[2], L[2]], color='gray', linestyle='--')

# ---------------------
# Draw the horizontal line joining the projections in the XOY plane (MLN).
# ---------------------
ax.plot([M[0], N[0]], [M[1], N[1]], [M[2], N[2]], color='black', linestyle='-', label="MLN (in XOY)")

# ---------------------
# Draw the horizontal line (at z = h) joining Q and R.
# This is horizontal because z = h is constant.
# ---------------------
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], color='orange', linestyle='-', lw=2, 
        label="Line Q-R (horizontal)")

# ---------------------
# Extra Joins:
# a) Draw a line joining A, B, C.
# (Since A, B, C are collinear, a line from A to B automatically passes through C.)
# ---------------------
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='red', linestyle='-', lw=2, 
        label="Line through A, C, B")

# b) Draw a line joining A and Q.
# ---------------------
ax.plot([A[0], Q[0]], [A[1], Q[1]], [A[2], Q[2]], color='purple', linestyle='-', lw=2, 
        label="Line A-Q")

# c) Draw the complete line from A through Q to R.
# ---------------------
ax.plot([A[0], R[0]], [A[1], R[1]], [A[2], R[2]], color='brown', linestyle='--', lw=2, 
        label="Line A-Q-R (Horizontal & Perp. to BN)")

# ---------------------
# Draw BN (vertical from B to its projection N).
# ---------------------
ax.plot([B[0], N[0]], [B[1], N[1]], [B[2], N[2]], color='cyan', linestyle='--', lw=2, 
        label="BN (vertical from B)")

# ---------------------
# Annotate key points.
# ---------------------
ax.text(A[0], A[1], A[2], " A", color='blue', fontsize=12)
ax.text(B[0], B[1], B[2], " B", color='green', fontsize=12)
ax.text(C[0], C[1], C[2], " C", color='magenta', fontsize=12)
ax.text(Q[0], Q[1], Q[2], " Q", color='orange', fontsize=12)
ax.text(R[0], R[1], R[2], " R", color='orange', fontsize=12)
ax.text(N[0], N[1], N[2], " N", color='cyan', fontsize=12)

# ---------------------
# Label axes and set title.
# ---------------------
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Section Formula & Projections in 3D\nLine A-Q-R is Horizontal and Perp. to BN")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()