import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cone_equation(alpha, beta, gamma, a, h, b, g, f):
    # Define the variables
    x, y, z = sp.symbols('x y z')
    
    # Define the base equation
    base_eq = a*x**2 + 2*h*x*y + b*y**2 + 2*g*x + 2*f*y + x
    
    # Define the vertex
    vertex = sp.Matrix([alpha, beta, gamma])
    
    # Define the point on the cone
    point = sp.Matrix([x, y, z])
    
    # Define the direction vector from the vertex to the point
    direction = point - vertex
    
    # Define the cone equation
    cone_eq = base_eq.subs({x: direction[0], y: direction[1], z: direction[2]})
    
    return sp.simplify(cone_eq)

def plot_cone(cone_eq, alpha, beta, gamma):
    # Create a grid of points
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    x, y = np.meshgrid(x_vals, y_vals)
    
    # Convert the sympy equation to a lambda function
    z_eq = sp.lambdify((x, y), cone_eq.subs({sp.symbols('x'): x, sp.symbols('y'): y}), 'numpy')
    
    # Calculate z values
    z = z_eq(x, y)
    
    # Plot the surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    
    # Plot the vertex
    ax.scatter(alpha, beta, gamma, color='r', s=100)
    
    plt.show()

# Example usage
alpha, beta, gamma = 1, 2, 3
a, h, b, g, f = 1, 2, 3, 4, 5

cone_eq = cone_equation(alpha, beta, gamma, a, h, b, g, f)
plot_cone(cone_eq, alpha, beta, gamma)