import math
 
def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.
 
    Parameters:
    - radius: float
        The radius of the circle.
 
    Returns:
    - float:
        The area of the circle.
 
    Raises:
    - ValueError:
        Raises an error if the radius is negative.
    """
 
    # Checking if the radius is negative
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
 
    # Calculating the area of the circle using the formula: A = π * r^2
    area = math.pi * (radius ** 2)
 
    return area
 
# Example usage of the calculate_circle_area function:
 
# Example 1: Calculating the area of a circle with radius 5
radius1 = 5
area1 = calculate_circle_area(radius1)
print(f"The area of a circle with radius {radius1} is {area1}.")
 
# Example 2: Calculating the area of a circle with radius -2 (should raise an error)
try:
    radius2 = -2
    area2 = calculate_circle_area(radius2)
    print(f"The area of a circle with radius {radius2} is {area2}.")
except ValueError as e:
    print(f"Error while calculating circle area: {e}")