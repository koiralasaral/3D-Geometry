import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def distance_between_points(P1, P2):
    """
    Calculate the Euclidean distance between two points in 3D.
    
    Parameters:
        P1 (tuple): Coordinates of the first point (x1, y1, z1).
        P2 (tuple): Coordinates of the second point (x2, y2, z2).
    
    Returns:
        float: The distance between P1 and P2.
    """
    dx = P2[0] - P1[0]
    dy = P2[1] - P1[1]
    dz = P2[2] - P1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)

def plot_parallelepiped(P1, P2, distance):
    """
    Plot the rectangular parallelepiped (box) having P1 and P2 as opposite vertices,
    along with the world coordinate axes.
    
    Parameters:
        P1 (tuple): First vertex of the box.
        P2 (tuple): Opposite vertex of the box.
        distance (float): The space diagonal of the box.
    """
    # Determine the eight vertices of the box.
    # Let P1 = A and P2 = G.
    A = (P1[0], P1[1], P1[2])           # (x1, y1, z1)
    B = (P2[0], P1[1], P1[2])           # (x2, y1, z1)
    C = (P2[0], P2[1], P1[2])           # (x2, y2, z1)
    D = (P1[0], P2[1], P1[2])           # (x1, y2, z1)
    E = (P1[0], P1[1], P2[2])           # (x1, y1, z2)
    F = (P2[0], P1[1], P2[2])           # (x2, y1, z2)
    G = (P2[0], P2[1], P2[2])           # (x2, y2, z2)  --> P2
    H = (P1[0], P2[1], P2[2])           # (x1, y2, z2)
    
    # Define the list of edges as pairs of vertices.
    edges = [
        (A, B), (B, C), (C, D), (D, A),   # Bottom face
        (E, F), (F, G), (G, H), (H, E),     # Top face
        (A, E), (B, F), (C, G), (D, H)      # Vertical edges
    ]
    
    # Create the figure and set up the 3D axes.
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Determine the axis limits.
    # We choose a limit that covers both points plus some margin.
    all_x = [P1[0], P2[0]]
    all_y = [P1[1], P2[1]]
    all_z = [P1[2], P2[2]]
    margin = 2
    x_min, x_max = min(all_x)-margin, max(all_x)+margin
    y_min, y_max = min(all_y)-margin, max(all_y)+margin
    z_min, z_max = min(all_z)-margin, max(all_z)+margin
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    
    # Draw the world coordinate axes using quiver.
    # X axis: red, Y axis: green, Z axis: blue.
    axis_length = max(x_max - x_min, y_max - y_min, z_max - z_min)
    ax.quiver(0, 0, 0, axis_length, 0, 0, color='red', arrow_length_ratio=0.1, lw=2, label='X axis')
    ax.quiver(0, 0, 0, 0, axis_length, 0, color='green', arrow_length_ratio=0.1, lw=2, label='Y axis')
    ax.quiver(0, 0, 0, 0, 0, axis_length, color='blue', arrow_length_ratio=0.1, lw=2, label='Z axis')
    
    # Draw each edge of the box.
    for edge in edges:
        xs = [edge[0][0], edge[1][0]]
        ys = [edge[0][1], edge[1][1]]
        zs = [edge[0][2], edge[1][2]]
        ax.plot(xs, ys, zs, color='black', lw=1)
    
    # Highlight the main (space) diagonal from A (P1) to G (P2) in red.
    ax.plot([A[0], G[0]], [A[1], G[1]], [A[2], G[2]], color='red', lw=3,
            label=f'Diagonal (d = {distance:.2f})')
    
    # Plot the two key points P1 and P2.
    ax.scatter(P1[0], P1[1], P1[2], color='blue', s=50, label=f'P1 {P1}')
    ax.scatter(P2[0], P2[1], P2[2], color='green', s=50, label=f'P2 {P2}')
    
    # Optionally, annotate edge lengths.
    ax.text((A[0]+B[0])/2, (A[1]+B[1])/2, (A[2]+B[2])/2, f' dx={P2[0]-P1[0]}', color='magenta')
    ax.text((A[0]+D[0])/2, (A[1]+D[1])/2, (A[2]+D[2])/2, f' dy={P2[1]-P1[1]}', color='magenta')
    ax.text((A[0]+E[0])/2, (A[1]+E[1])/2, (A[2]+E[2])/2, f' dz={P2[2]-P1[2]}', color='magenta')
    
    # Labels and title.
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("Rectangular Parallelepiped Demonstrating the 3D Distance Formula\nwith Coordinate Axes")
    ax.legend()
    plt.show()

def main():
    # Prompt the user for two points.
    print("Enter two 3D points to compute the distance and plot the corresponding box.")
    input_str1 = input("Enter coordinates for point 1 (x,y,z): ")
    input_str2 = input("Enter coordinates for point 2 (x,y,z): ")
    
    # Parse the input as comma-separated numbers.
    try:
        P1 = tuple(map(float, input_str1.strip().split(',')))
        P2 = tuple(map(float, input_str2.strip().split(',')))
    except Exception as e:
        print("Error parsing input. Please enter coordinates as x,y,z (e.g., 1,2,3).")
        return
    
    # Check that both points have three coordinates.
    if len(P1) != 3 or len(P2) != 3:
        print("Please provide exactly three values for each point.")
        return
    
    # Calculate distance.
    dist = distance_between_points(P1, P2)
    print(f"The distance between {P1} and {P2} is {dist:.2f}")
    
    # Plot the box and coordinate axes.
    plot_parallelepiped(P1, P2, dist)

if __name__ == '__main__':
    main()