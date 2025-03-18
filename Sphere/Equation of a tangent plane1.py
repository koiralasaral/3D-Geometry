


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
def tangent_plane_sphere(x0, y0, z0, r):
    # Define the variables
    x, y, z = sp.symbols('x y z')
    
    # Equation of the sphere
    sphere_eq = x**2 + y**2 + z**2 - r**2
    
    # Gradient of the sphere equation
    grad_sphere = sp.Matrix([sp.diff(sphere_eq, var) for var in (x, y, z)])
    
    # Point on the sphere
    point = sp.Matrix([x0, y0, z0])
    
    # Tangent plane equation
    tangent_plane_eq = grad_sphere.dot(point - sp.Matrix([x, y, z]))
    
    return tangent_plane_eq, grad_sphere

def plot_sphere_and_tangent_plane(x0, y0, z0, r):
    """
    Plots a sphere and its tangent plane at a given point.
    Parameters:
    x0 (float): x-coordinate of the point on the sphere where the tangent plane is to be plotted.
    y0 (float): y-coordinate of the point on the sphere where the tangent plane is to be plotted.
    z0 (float): z-coordinate of the point on the sphere where the tangent plane is to be plotted.
    r (float): Radius of the sphere.
    Returns:
    None
    This function creates a 3D plot of a sphere and its tangent plane at the specified point (x0, y0, z0).
    The sphere is plotted in blue with some transparency, the tangent plane is plotted in red with some transparency,
    and the point on the sphere is plotted in green.
    """
    tangent_plane_eq, grad_sphere = tangent_plane_sphere(x0, y0, z0, r)
    x, y, z = symbols('x y z')
    # Convert sympy expressions to numerical functions
    tangent_plane_func = sp.lambdify((x, y, z), tangent_plane_eq, 'numpy')
    # Create a grid of points
    x_vals = np.linspace(-r, r, 100)
    y_vals = np.linspace(-r, r, 100)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    
    # Calculate z values for the tangent plane
    z_vals = (grad_sphere[0] * (x_vals - x0) + grad_sphere[1] * (y_vals - y0)) / -grad_sphere[2] + z0
    
    # Plot the sphere
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x_sphere = r * np.outer(np.cos(u), np.sin(v))
    y_sphere = r * np.outer(np.sin(u), np.sin(v))
    z_sphere = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.3)
    
    # Plot the tangent plane
    ax.plot_surface(x_vals, y_vals, z_vals, color='r', alpha=0.5)
    
    # Plot the point on the sphere
    ax.scatter([x0], [y0], [z0], color='g', s=100)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Example usage
x0, y0, z0 = 1, 1, 1  # Point on the sphere
r = 5  # Radius of the sphere
plot_sphere_and_tangent_plane(x0, y0, z0, r)