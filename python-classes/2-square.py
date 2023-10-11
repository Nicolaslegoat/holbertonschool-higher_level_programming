#!/usr/bin/python3
"""empty module"""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.valeur = size
        if size < 0:
            raise ValueError("size must be >= 0")
