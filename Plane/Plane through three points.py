import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def plane_from_points(p1, p2, p3):
    # Create vectors from points
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)
    
    # Compute the normal vector by taking the cross product
    normal_vector = np.cross(v1, v2)
    
    # Extract the coefficients A, B, C from the normal vector
    A, B, C = normal_vector
    
    # Compute D using the plane equation Ax + By + Cz + D = 0
    D = -np.dot(normal_vector, p1)
    
    return A, B, C, D

def plot_plane(A, B, C, D, points):
    # Create a grid of points
    xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
    
    # Calculate the corresponding z values
    zz = (-A * xx - B * yy - D) * 1. / C
    
    # Plot the plane
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)
    
    # Plot the points
    ax.scatter(*zip(*points), color='red')
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()

# Define three non-collinear points
p1 = [1, 2, 3]
p2 = [4, 5, 6]
p3 = [7, 8, 9]

# Calculate the plane equation coefficients
A, B, C, D = plane_from_points(p1, p2, p3)

# Print the plane equation
print(f"The equation of the plane is: {A}x + {B}y + {C}z + {D} = 0")

# Plot the plane and points
plot_plane(A, B, C, D, [p1, p2, p3])