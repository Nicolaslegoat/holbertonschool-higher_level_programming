#!/usr/bin/python3
"""module that writes an object to a text file with JSON"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dumps(my_obj)
