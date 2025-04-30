import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_C_on_yz_plane(A, B):
    """
    Compute the point C on the line joining A and B such that C lies in the YZ-plane (x=0).
    Uses the parametric equation:
        C = A + t * (B - A)
    with t chosen so that A_x + t*(B_x - A_x) = 0.
    
    Parameters:
        A (tuple or array): Coordinates of A as (x1, y1, z1).
        B (tuple or array): Coordinates of B as (x2, y2, z2).
        
    Returns:
        tuple: (C, t) where C is the computed point (with x=0) and t is the parameter.
    """
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    if B[0] == A[0]:
        if A[0] == 0:
            print("Both A and B lie in the YZ-plane; returning A as C.")
            return A, None
        else:
            raise ValueError("The line joining A and B is parallel to the YZ-plane and does not intersect it.")
    t = -A[0] / (B[0] - A[0])
    C = A + t * (B - A)
    return C, t

def plot_all(A, B, C, t):
    """
    Plot in 3D all the key points and joinings:
      - A, B, and computed C (with C on the YZ-plane, i.e. x=0).
      - Their projections M, N, and L onto the XOY plane (z=0).
      - A horizontal line at z = h (with h = A's z-coordinate) through Q and R,
        where Q = (C_x, C_y, h) and R = (B_x, B_y, h).
      - Extra join lines (A-B, A-Q) are drawn for clarity.
    The computed ratio t is also printed on the figure.
    
    Parameters:
         A, B, C: the 3D points.
         t: the ratio used in computing C.
    """
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    
    # Projections on the XOY plane (z=0)
    M = np.array([A[0], A[1], 0])
    N = np.array([B[0], B[1], 0])
    L = np.array([C[0], C[1], 0])
    
    # Choose horizontal level h
    h = A[2]  # For this construction, we set h = A's z-coordinate.
    Q = np.array([C[0], C[1], h])
    R = np.array([B[0], B[1], h])
    
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw global coordinate axes.
    origin = np.array([0, 0, 0])
    ax.quiver(origin[0], origin[1], origin[2], 15, 0, 0, color='red', arrow_length_ratio=0.1, lw=2, label="X axis")
    ax.quiver(origin[0], origin[1], origin[2], 0, 15, 0, color='green', arrow_length_ratio=0.1, lw=2, label="Y axis")
    ax.quiver(origin[0], origin[1], origin[2], 0, 0, 15, color='blue', arrow_length_ratio=0.1, lw=2, label="Z axis")
    
    # Plot primary points A, B, C.
    ax.scatter(A[0], A[1], A[2], color='blue', s=80, label=f"A {tuple(A)}")
    ax.scatter(B[0], B[1], B[2], color='green', s=80, label=f"B {tuple(B)}")
    ax.scatter(C[0], C[1], C[2], color='red', s=80, label=f"C {tuple(np.round(C,2))} (YZ-plane)")
    
    # Plot the projections M, N, and L.
    ax.scatter(M[0], M[1], M[2], color='blue', s=60, label="M (A proj.)")
    ax.scatter(N[0], N[1], N[2], color='green', s=60, label="N (B proj.)")
    ax.scatter(L[0], L[1], L[2], color='red', s=60, label="L (C proj.)")
    
    # Draw vertical (perpendicular) lines from points to their projections.
    ax.plot([A[0], M[0]], [A[1], M[1]], [A[2], M[2]], color='gray', linestyle='--')
    ax.plot([B[0], N[0]], [B[1], N[1]], [B[2], N[2]], color='gray', linestyle='--')
    ax.plot([C[0], L[0]], [C[1], L[1]], [C[2], L[2]], color='gray', linestyle='--')
    
    # Draw horizontal line in the XOY plane joining M, N (Path MLN).
    ax.plot([M[0], N[0]], [M[1], N[1]], [M[2], N[2]], color='black', linestyle='-', label="MLN (in XOY)")
    
    # Draw horizontal line (at z = h) joining Q and R.
    ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], color='orange', linestyle='-', lw=2, label="Line Q-R (horizontal)")
    
    # Extra joins:
    # a) Draw a line joining A and B (which, by collinearity, passes through C).
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='purple', linestyle='-', lw=2, label="Line A-B (through C)")
    
    # b) Draw a line joining A and Q.
    ax.plot([A[0], Q[0]], [A[1], Q[1]], [A[2], Q[2]], color='brown', linestyle='-', lw=2, label="Line A-Q")
    
    # Annotate key points.
    ax.text(A[0], A[1], A[2], " A", color='blue', fontsize=12)
    ax.text(B[0], B[1], B[2], " B", color='green', fontsize=12)
    ax.text(C[0], C[1], C[2], " C", color='red', fontsize=12)
    ax.text(M[0], M[1], M[2], " M", color='blue', fontsize=10)
    ax.text(N[0], N[1], N[2], " N", color='green', fontsize=10)
    ax.text(L[0], L[1], L[2], " L", color='red', fontsize=10)
    ax.text(Q[0], Q[1], Q[2], " Q", color='orange', fontsize=12)
    ax.text(R[0], R[1], R[2], " R", color='orange', fontsize=12)
    
    # Annotate the computed ratio t on the plot.
    ratio_text = f"Computed ratio t = {t:.2f}" if t is not None else "A and B lie on YZ-plane"
    ax.text2D(0.05, 0.95, ratio_text, transform=ax.transAxes, fontsize=12, color="black")
    
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Intersection with YZ-plane + Projections & Extra Joins (Program 2 Extended)")
    ax.legend(fontsize=9, loc='upper left')
    plt.show()

def main():
    # For Program 2: use A = (4,6,7) and B = (-1,2,5)
    A_input = (4, 6, 7)
    B_input = (-1, 2, 5)
    C_output, t = compute_C_on_yz_plane(A_input, B_input)
    print("Computed point C on the YZ-plane:", C_output)
    print("Computed ratio t =", t)
    
    plot_all(A_input, B_input, C_output, t)

if __name__ == '__main__':
    main()