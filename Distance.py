import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance_between_points(point1, point2):
    """
    Calculate the distance between two points in 3D space.

    Parameters:
    point1 (tuple): A tuple of three coordinates (x1, y1, z1).
    point2 (tuple): A tuple of three coordinates (x2, y2, z2).

    Returns:
    float: The distance between the two points.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def plot_points(point1, point2):
    """
    Plot the two points and the line connecting them in 3D space.

    Parameters:
    point1 (tuple): A tuple of three coordinates (x1, y1, z1).
    point2 (tuple): A tuple of three coordinates (x2, y2, z2).
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    z_values = [point1[2], point2[2]]
    
    ax.scatter(x_values, y_values, z_values, color='r')
    ax.plot(x_values, y_values, z_values, color='b')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    plt.show()

# Example usage
point1 = (1, 2, 3)
point2 = (4, 5, 6)
print(f"The distance between {point1} and {point2} is {distance_between_points(point1, point2)}")
plot_points(point1, point2)