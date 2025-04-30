import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D plotting

# Define the range for the cube: from -L to L.
L = 5

# Create the figure and 3D axes.
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the octants data.
# Each tuple contains:
#   (Octant number, x sign, y sign, z sign, lower corner (x0, y0, z0), color)
# Note: For each octant, we use a cube of size L.
octants = [
    (1, '+', '+', '+',  0,   0,   0,  'lightskyblue'),   # Octant 1: x>0, y>0, z>0
    (2, '–', '+', '+', -L,   0,   0,  'lightgreen'),       # Octant 2: x<0, y>0, z>0
    (3, '–', '–', '+', -L,  -L,   0,  'lightcoral'),        # Octant 3: x<0, y<–, z>0
    (4, '+', '–', '+',  0,  -L,   0,  'khaki'),             # Octant 4: x>0, y<0, z>0
    (5, '+', '+', '–',  0,   0,  -L,  'plum'),              # Octant 5: x>0, y>0, z<0
    (6, '–', '+', '–', -L,   0,  -L,  'palegreen'),         # Octant 6: x<0, y>0, z<0
    (7, '–', '–', '–', -L,  -L,  -L,  'lightpink'),          # Octant 7: x<0, y<0, z<0
    (8, '+', '–', '–',  0,  -L,  -L,  'lightsalmon')         # Octant 8: x>0, y<0, z<0
]

# Draw each octant as a translucent bar (cuboid) using bar3d.
dx = dy = dz = L  # Dimensions of each cuboid

for oct_num, sx, sy, sz, x0, y0, z0, color in octants:
    # Draw the cuboid in its octant.
    ax.bar3d(x0, y0, z0, dx, dy, dz, color=color, alpha=0.5, edgecolor='black')
    # Add a label at the center of the cuboid.
    cx = x0 + dx/2
    cy = y0 + dy/2
    cz = z0 + dz/2
    ax.text(cx, cy, cz, f"Oct {oct_num}", color='black',
            ha='center', va='center', fontsize=10, weight='bold')

# Draw the coordinate planes (x=0, y=0, z=0) as thick black lines.
# x=0 plane line on ground.
ax.plot([0, 0], [-L, L], [0, 0], color='black', linewidth=2)
# y=0 line on ground.
ax.plot([-L, L], [0, 0], [0, 0], color='black', linewidth=2)
# z-axis.
ax.plot([0, 0], [0,0], [-L, L], color='black', linewidth=2)

# Set the limits of the plot.
ax.set_xlim([-L, L])
ax.set_ylim([-L, L])
ax.set_zlim([-L, L])

# Set axis labels and title.
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("Cartesian 3D System: 8 Octants", fontsize=14, weight='bold')

# Prepare table data summarizing the sign of x, y, z in each octant.
table_data = []
for oct_num, sx, sy, sz, x0, y0, z0, color in octants:
    table_data.append([str(oct_num), sx, sy, sz])

column_labels = ["Octant", "x", "y", "z"]

# Create a table at the bottom of the plot.
the_table = plt.table(cellText=table_data,
                      colLabels=column_labels,
                      cellLoc='center',
                      loc='bottom')
the_table.set_fontsize(12)
the_table.scale(1, 2)

# Adjust the layout to make room for the table.
plt.subplots_adjust(bottom=0.25)

plt.show()