import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variables
x, y, z = sp.symbols('x y z')
a, b, c, f, g, h = sp.symbols('a b c f g h')

# Define the homogeneous equation of second degree
equation = a*x**2 + b*y**2 + c*z**2 + 2*f*y*z + 2*g*z*x + 2*h*x*y

# Define the condition
condition = a*b*c + 2*f*g*h - a*f**2 - b*g**2 - c*h**2

# Check if the condition is zero
if sp.simplify(condition) == 0:
    print("The equation represents a pair of planes.")
    
    # Find the normal vectors of the planes
    A = sp.Matrix([[a, h, g], [h, b, f], [g, f, c]])
    eigensystem = A.eigenvals()
    eigenvectors = A.eigenvects()
    
    # Extract the normal vectors
    normal_vector1 = eigenvectors[0][2][0]
    normal_vector2 = eigenvectors[1][2][0]
    
    # Calculate the angle between the normal vectors
    dot_product = normal_vector1.dot(normal_vector2)
    norm1 = sp.sqrt(normal_vector1.dot(normal_vector1))
    norm2 = sp.sqrt(normal_vector2.dot(normal_vector2))
    angle = sp.acos(dot_product / (norm1 * norm2))
    
    print(f"The angle between the planes is: {sp.deg(angle)} degrees")
    
    # Plot the planes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the planes
    xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
    zz1 = (-normal_vector1[0]*xx - normal_vector1[1]*yy) / normal_vector1[2]
    zz2 = (-normal_vector2[0]*xx - normal_vector2[1]*yy) / normal_vector2[2]
    
    # Plot the planes
    ax.plot_surface(xx, yy, zz1, alpha=0.5, rstride=100, cstride=100)
    ax.plot_surface(xx, yy, zz2, alpha=0.5, rstride=100, cstride=100)
    
    plt.show()
else:
    print("The equation does not represent a pair of planes.")