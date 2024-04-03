#!/usr/bin/python3
"""A defined Class"""


class Square:
    """A class definition that has the name Square"""
    def __init__(self, size=0):
        """A class constructor that takes in an argument
        Arg: size - the size of the defined square class
        Errors Raised:
                    TypeError: executes if size is not an integer
                    ValueError: executes if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """A method named area that takes self
        as its only parameter
        and calculates the area of the Square
        Return: area
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """A public method that prints
        a square using a character
        Character: #
        """
        for _ in range(self.__size):
            print("#" * self.__size)
        if (self.__size == 0):
            print()
