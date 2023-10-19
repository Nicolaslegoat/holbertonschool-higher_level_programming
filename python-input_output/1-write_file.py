#!/usr/bin/python3
"""Write module"""


def write_file(filename="", text=""):
    """Function that write a text"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
