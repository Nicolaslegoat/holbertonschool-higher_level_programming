#!/usr/bin/python3
"""empty module"""


class Square:
    """class calculate size of area"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """function to return area"""
    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise ValueError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * '#')
