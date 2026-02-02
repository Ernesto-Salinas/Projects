"""
Defining Methods in a Class

Complete the Python code to create a class named Circle, which is constructed by a radius having value 5 and two other methods, which will calculate the circumference and area of a circle.
"""

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.circumference = 2*math.pi*radius
        self.area = math.pi*radius**2

circle = Circle(5)
print("Area:")
print(circle.area)
print("Circumference")
print(circle.circumference)