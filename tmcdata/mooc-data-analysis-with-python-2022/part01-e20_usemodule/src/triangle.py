
__author__ = "Zumhliansang Lung Ler"
__version__ = "1"
__doc__ = "This module responsible for triangle shape's calculation."

# Enter you module contents here
def hypotenuse(a, b):
    """
    hypotenuse which returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle
    """
    from math import sqrt

    return sqrt((a**2) + (b**2))

def area(base, height):
    """
    area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
    """
    
    return (base * height)/2