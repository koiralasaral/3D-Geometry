import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Define the vertices of the cube
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Define the diagonals of the cube
diagonal1 = vertices[6] - vertices[0]  # From (0,0,0) to (1,1,1)
diagonal2 = vertices[5] - vertices[3]  # From (0,1,0) to (1,0,1)

# Calculate the direction cosines of the diagonals
def direction_cosines(vector):
    magnitude = np.linalg.norm(vector)
    return vector / magnitude

cosines1 = direction_cosines(diagonal1)
cosines2 = direction_cosines(diagonal2)

# Calculate the angle between the two diagonals using the dot product
dot_product = np.dot(cosines1, cosines2)
angle = np.arccos(dot_product)

# Convert the angle from radians to degrees
angle_degrees = np.degrees(angle)

print(f"The angle between the two diagonals is {angle_degrees:.2f} degrees.")

# Plot the cube and the diagonals
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the edges of the cube
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

for edge in edges:
    ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color="b")

# Plot the diagonals
ax.plot3D(*zip(vertices[0], vertices[6]), color="r", label="Diagonal 1")
ax.plot3D(*zip(vertices[3], vertices[5]), color="g", label="Diagonal 2")

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Angle between diagonals: {angle_degrees:.2f} degrees')
ax.legend()

plt.show()
