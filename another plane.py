import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------
# 1. Define a fixed unit normal vector.
#    In normal form, the plane is given by: l*x + m*y + n*z = p.
#    Here we choose l = m = n = 1/√3 so that (l,m,n) is a unit vector.
# ---------------------------
l = 1 / np.sqrt(3)
m = 1 / np.sqrt(3)
n = 1 / np.sqrt(3)

# ---------------------------
# 2. Define a candidate point (point2) to check whether it lies on the plane.
#    Only if it satisfies the plane equation for the given p will it be plotted.
# ---------------------------
candidate2 = np.array([1, 2, 3])
tol = 1e-6  # tolerance for floating-point comparisons

# ---------------------------
# 3. Loop over different plane positions (i.e. using different p values)
#    p is the distance from the origin to the plane along the normal.
# ---------------------------
for p in range(1, 6):  # p = 1,2,3,4,5
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # ------------------------------------------------
    # Plot the plane: l*x + m*y + n*z = p.
    # Solve for z (assuming n != 0):  z = (p - l*x - m*y) / n.
    # ------------------------------------------------
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = (p - l * X - m * Y) / n
    plane_surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha=0.5, edgecolor='none')
    
    # ------------------------------------------------
    # (a) Compute the perpendicular (OP) from the origin, O=(0,0,0),
    # to the plane.  For a plane in normal form the foot of the perpendicular is:
    #       P = p*(l, m, n)
    # ------------------------------------------------
    O = np.array([0, 0, 0])
    P = p * np.array([l, m, n])
    ax.scatter(O[0], O[1], O[2], color="black", s=50, label="Origin O")
    ax.scatter(P[0], P[1], P[2], color="red", s=50, label="Foot P (OP ⟂ plane)")
    ax.plot([O[0], P[0]], [O[1], P[1]], [O[2], P[2]], "r--", label="OP")
    
    # ------------------------------------------------
    # (b) Extend the normal vector to show PN.
    # Let N = P + (l, m, n). (This is not on the plane but shows the direction of the normal.)
    # ------------------------------------------------
    N = P + np.array([l, m, n])
    ax.scatter(N[0], N[1], N[2], color="magenta", s=50, label="Point N (extended normal)")
    ax.plot([P[0], N[0]], [P[1], N[1]], [P[2], N[2]], "m--", label="PN")
    
    # ------------------------------------------------
    # (c) Find and plot the intercepts (points where the plane meets the axes).
    # For a plane in normal form (l*x + m*y + n*z = p):
    #   - x-intercept (A):  set y = 0 and z = 0 => l*x = p  →  x = p/l.
    #   - y-intercept (B):  set x = 0 and z = 0 => m*y = p  →  y = p/m.
    #   - z-intercept (C):  set x = 0 and y = 0 => n*z = p  →  z = p/n.
    # (We assume l, m, n are nonzero.)
    # ------------------------------------------------
    A_pt = np.array([p / l, 0, 0])
    B_pt = np.array([0, p / m, 0])
    C_pt = np.array([0, 0, p / n])
    
    ax.scatter(A_pt[0], A_pt[1], A_pt[2], color="green", s=50, marker="o", label="x-intercept (A)")
    ax.scatter(B_pt[0], B_pt[1], B_pt[2], color="purple", s=50, marker="^", label="y-intercept (B)")
    ax.scatter(C_pt[0], C_pt[1], C_pt[2], color="orange", s=50, marker="s", label="z-intercept (C)")
    
    # Connect the intercepts to form the triangle ABC.
    ax.plot([A_pt[0], B_pt[0]], [A_pt[1], B_pt[1]], [A_pt[2], B_pt[2]], color="gray", linestyle=":")
    ax.plot([B_pt[0], C_pt[0]], [B_pt[1], C_pt[1]], [B_pt[2], C_pt[2]], color="gray", linestyle=":")
    ax.plot([C_pt[0], A_pt[0]], [C_pt[1], A_pt[1]], [C_pt[2], A_pt[2]], color="gray", linestyle=":")
    
    # ------------------------------------------------
    # (d) Check if candidate2 lies on the plane.
    # For the candidate point (1,2,3) to lie on the plane,
    # we need l*1 + m*2 + n*3 = p (within tolerance).
    # Only if that is true will we plot it.
    # ------------------------------------------------
    candidate2_val = l * candidate2[0] + m * candidate2[1] + n * candidate2[2]
    if abs(candidate2_val - p) < tol:
        ax.scatter(candidate2[0], candidate2[1], candidate2[2],
                   color="blue", s=50, label="Candidate (1,2,3) on plane")
    else:
        # Candidate (1,2,3) does not satisfy the plane eq.
        # We choose not to plot it if it is not on the locus.
        print(f"For p = {p}, candidate (1,2,3) is NOT on the plane (LHS = {candidate2_val:.4f}).")
    
    # ------------------------------------------------
    # (e) Set labels, title, and legend.
    # ------------------------------------------------
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title(f"Normal Form Plane: {l:.3f}x + {m:.3f}y + {n:.3f}z = {p}")
    ax.legend(loc="upper left")
    
    plt.show()