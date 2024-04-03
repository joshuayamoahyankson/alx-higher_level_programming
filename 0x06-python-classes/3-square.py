#!/usr/bin/python3
"""A defined Class"""


class Square:
    """A class definition that has the name Square"""
    def __init__(self, size=0):
        """A class constructor that takes in an argument
        Arg: size - the size of the defined square class
        Errors Raised:
        TypeError: executes if size is not an integer
        ValueErrorxecutes if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """A method named area that takes self
        as its only parameter
        and calculates the area of the Square
        Return: area
        """
        area = self.__size ** 2
        return area
