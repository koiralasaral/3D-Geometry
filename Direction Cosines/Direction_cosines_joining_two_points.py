import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

# Function to calculate direction cosines
def direction_cosines(point1, point2):
    vector = np.array(point2) - np.array(point1)
    magnitude = np.linalg.norm(vector)
    direction_cosines = vector / magnitude
    return direction_cosines

# Function to plot the line and direction cosines
def plot_direction_cosines(point1, point2):
    direction_cos = direction_cosines(point1, point2)
    
    # Plotting the line
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], [point1[2], point2[2]], marker='o')
    
    # Annotating the direction cosines
    ax.text(point2[0], point2[1], point2[2], f'({direction_cos[0]:.2f}, {direction_cos[1]:.2f}, {direction_cos[2]:.2f})', color='red')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Direction Cosines of the Line Joining Two Points')
    plt.show()

# Example points
point1 = [1, 2, 3]
point2 = [4, 5, 6]

# Calculate and plot direction cosines
plot_direction_cosines(point1, point2)
# Function to calculate the angle between two vectors
def angle_between_vectors(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    cos_angle = dot_product / (magnitude1 * magnitude2)
    angle = np.arccos(cos_angle)
    return np.degrees(angle)

# Function to plot two lines and the angle between them
def plot_lines_and_angle(point1, point2, point3, point4):
    vector1 = np.array(point2) - np.array(point1)
    vector2 = np.array(point4) - np.array(point3)
    angle = angle_between_vectors(vector1, vector2)
    
    # Plotting the lines
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], [point1[2], point2[2]], marker='o', label='Line 1')
    ax.plot([point3[0], point4[0]], [point3[1], point4[1]], [point3[2], point4[2]], marker='o', label='Line 2')
    
    # Annotating the angle
    mid_point1 = (np.array(point1) + np.array(point2)) / 2
    mid_point2 = (np.array(point3) + np.array(point4)) / 2
    ax.text(mid_point1[0], mid_point1[1], mid_point1[2], f'Angle: {angle:.2f}°', color='blue')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Angle Between Two Lines in 3D Space')
    plt.legend()
    plt.show()

# Example points for the second line
point3 = [1, 0, 0]
point4 = [0, 1, 1]

# Plot lines and angle between them
plot_lines_and_angle(point1, point2, point3, point4)