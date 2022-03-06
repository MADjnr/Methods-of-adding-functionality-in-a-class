"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Circle:

    def __init__(self, radius):
        self.radius = radius

    # Printing the value
    def find_diameter(self):
        print(f"Diameter: {self.radius * 2}")
        # The value could be returned too with:
        # return self.radius * 2
'''

## method in the Rectangle class
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    ## Writing the method
    def find_area(self):
        print(f'The area of the rectangle is:{self.length * self.width}' )

my_rectangle = Rectangle(23, 54)

my_rectangle.find_area()
