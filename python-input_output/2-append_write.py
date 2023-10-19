#!/usr/bin/python3
"""Write module"""


def append_write(filename="", text=""):
    """Function that write a text and adding with compteur of new element"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
