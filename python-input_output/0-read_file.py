#!/usr/bin/python3
"""Read module"""


def read_file(filename=""):
    """read and prints the content of a text file"""
    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
    print(read_data, end="")
