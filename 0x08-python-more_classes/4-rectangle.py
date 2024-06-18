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
        self.height =height

    @property
    def width(self):
        """A getter method that retrieves the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
         """A setter method to sets the width"""
         if not isinstance (value, int):
             raise TypeError ("width must be an integer")
         elif (value < 0):
             raise ValueError ("width must be >= 0")
         self.__width = value

    @property
    def height(self):
        """A getter method that retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method to sets the width"""
        if not isinstance (value, int):
            raise TypeError ("height must be an integer")
        elif (value < 0):
            raise ValueError ("height must be >= 0")
        self.__height = value

    def area(self):
        """A method that returns the rectangles area"""
        return self.__width * self.__height

    def perimeter(self):
        """A method that returns the rectangles perimeter"""
        if ((self.__width or self.__height) == 0):
            return 0
        else:
            return 2 * (int(self.__width) + int(self.__height))

    def __str__(self):
        """A diagramatic representation of the rectangle class"""
        if ((self.__width or self.__height) == 0):
            return ""
        rect_str = ""
        for column in (self.__height):
            for row in (self.__width):
                rect_str += "#"
            if column < self.__height - 1:
                rect_str += "\n"
            return rect_str

    def __repr__(self):
        """A method that returns a string that represents the object"""
        return f'Rectangle({self.width}, {self.height})'
