import sympy as sp

def sphere_equation(x1, y1, z1, x2, y2, z2):
    # Midpoint of the line segment joining the two points
    x0 = (x1 + x2) / 2
    y0 = (y1 + y2) / 2
    z0 = (z1 + z2) / 2

    # Radius of the sphere (half the distance between the two points)
    radius = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) / 2

    # Equation of the sphere
    x, y, z = sp.symbols('x y z')
    equation = (x - x0)**2 + (y - y0)**2 + (z - z0)**2 - radius**2

    return sp.simplify(equation)

# Example usage
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6
equation = sphere_equation(x1, y1, z1, x2, y2, z2)
print(f"The equation of the sphere is: {equation} = 0")