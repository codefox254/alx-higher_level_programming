#!/usr/bin/python3

# Define the class Rectangle
class Rectangle:
    # Define the constructor with optional width and height
    def __init__(self, width=0, height=0):
        # Set the width and height using the property setters
        self.width = width
        self.height = height

    # Define the property getter for width
    @property
    def width(self):
        # Return the private instance attribute __width
        return self.__width

    # Define the property setter for width
    @width.setter
    def width(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            # Raise a TypeError exception
            raise TypeError("width must be an integer")
        # Check if the value is negative
        if value < 0:
            # Raise a ValueError exception
            raise ValueError("width must be >= 0")
        # Set the private instance attribute __width
        self.__width = value

    # Define the property getter for height
    @property
    def height(self):
        # Return the private instance attribute __height
        return self.__height

    # Define the property setter for height
    @height.setter
    def height(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            # Raise a TypeError exception
            raise TypeError("height must be an integer")
        # Check if the value is negative
        if value < 0:
            # Raise a ValueError exception
            raise ValueError("height must be >= 0")
        # Set the private instance attribute __height
        self.__height = value

