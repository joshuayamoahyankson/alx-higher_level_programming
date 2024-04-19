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
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter method that retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method that sets the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= ')
        self.__width = value

    @property
    def height(self):
        """A getter method that retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method that sets the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """A method that returns the area
        of the recatngle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """A method that returns the
        rectangles perimeter"""
        if (self.__width and self.__height != 0):
            return 2 * (int(self.__width)) + 2 * (int(self.height))
        else:
            return 0
