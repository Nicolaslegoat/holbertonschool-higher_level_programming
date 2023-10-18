#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """That class represent a square"""
    def __init__(self, size):
        """This initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area of the square"""
        return self.__size ** 2
