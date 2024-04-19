#!/usr/bin/python3
"""A definition of a rectangle class"""


class Rectangle:
    """A rectangle class represented"""

    def __init__(self, width=0, height=0):
        """A class constructor that takes in width and height
        as default arguments and initializes them
        Args:
            width: represents the width of the rectangle
            heigth: represents the height of the rectangle
        Errors Raised:
            TypeError: if value is not integer
            ValueError: if value is less tha zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter method that returns width
        as a private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):

        """A setter method that checks for an int
        data type instance and raises specified errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter method that returns height
        as a private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method that checks for an int
        data type instance and raises specified errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
