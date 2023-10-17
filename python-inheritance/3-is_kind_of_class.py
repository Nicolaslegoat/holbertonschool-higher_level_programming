#!/usr/bin/python3
"""function that returns if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """function that returns true if is an instance otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
