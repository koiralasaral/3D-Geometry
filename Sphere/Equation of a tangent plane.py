import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def tangent_plane(x0, y0, z0, r):
    # The equation of the sphere is x^2 + y^2 + z^2 = r^2
    # The equation of the tangent plane at (x0, y0, z0) is:
    # (x0)*(x - x0) + (y0)*(y - y0) + (z0)*(z - z0) = 0
    # Simplifying, we get:
    # x*x0 + y*y0 + z*z0 = r^2
    return lambda x, y: (r**2 - x*x0 - y*y0) / z0

# Example usage of tangent_plane
x0, y0, z0, r = 1, 1, 1, 5

# Create a grid of points
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)

# Calculate z values for the tangent plane
z = tangent_plane(x0, y0, z0, r)(x, y)

# Print the equation of the tangent plane
print(f"The equation of the tangent plane is: {x0}*x + {y0}*y + {z0}*z = {r**2}")

   