#!/usr/bin/python3
"""module JSON"""
import json

def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
